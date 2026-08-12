
#!/usr/bin/env python3
"""
HEA Paper Processing Pipeline - Main Orchestrator

Pipeline flow:
  Group 1 (Parallel downloads, based on database_HEA.csv source):
    Step 1: download_rsc.py          -> rsc/*.pdf
    Step 2: download_springer.py     -> springer/*.pdf
    Step 3: download_elsevier.py     -> elsevier/*.xml

  Group 2 (Parallel processing, after Group 1 completes):
    Step 4: pdf_to_md.py             -> rsc-spr-mds/*.md  (PDFs from rsc/ + springer/)
    Step 5: xml_extractor2.py        -> elsevier_txt/*.txt (XMLs from elsevier/)

  Group 3 (Sequential, after Group 2 completes):
    Step 6: ds_mult_prompts.py       -> database_of_all_prompts.csv
    Step 7: merge_metadata_and_results.py -> database_of_raw_responses.csv + db_HEAs.csv
    Step 8: comprehensive_dict2csv.py       -> final_db_HEAs.csv

Usage:
    python main.py                  # Run entire pipeline
    python main.py --step 1,2,3     # Run only steps 1, 2, 3 (downloads)
    python main.py --resume         # Resume from last completed step
    python main.py --status         # Show pipeline status
"""

import os
import sys
import subprocess
import time
import json
import argparse
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==================== Configuration ====================
BASE_DIR = Path(__file__).parent
WORK_DIR = BASE_DIR
STATUS_FILE = WORK_DIR / '.pipeline_status.json'

# Subdirectory structure - scripts live here, no copying needed
DOWNLOADERS_DIR = WORK_DIR / 'downloaders'
PROCESSORS_DIR = WORK_DIR / 'processors'
FINAL_DIR = WORK_DIR / 'final'

# Required files in working directory
REQUIRED_FILES = ['database_HEA.csv']

# Pipeline step definitions
STEPS = {
    1: {
        'name': 'download_rsc',
        'script': 'download_rsc.py',
        'folder': 'downloaders',
        'description': 'Download RSC PDFs (source=rsc)',
        'output_dirs': ['rsc'],
        'deps': []
    },
    2: {
        'name': 'download_springer',
        'script': 'download_springer.py',
        'folder': 'downloaders',
        'description': 'Download Springer PDFs (source=springer)',
        'output_dirs': ['springer'],
        'deps': []
    },
    3: {
        'name': 'download_elsevier',
        'script': 'download_elsevier.py',
        'folder': 'downloaders',
        'description': 'Download Elsevier XMLs (source=elsevier)',
        'output_dirs': ['elsevier'],
        'deps': []
    },
    4: {
        'name': 'pdf_to_md',
        'script': 'pdf_to_md.py',
        'folder': 'processors',
        'description': 'Convert PDFs to Markdown (RSC + Springer)',
        'output_dirs': ['rsc-spr-mds'],
        'deps': [1, 2]
    },
    5: {
        'name': 'xml_extractor2',
        'script': 'xml_extractor2.py',
        'folder': 'processors',
        'description': 'Extract text from Elsevier XMLs',
        'output_dirs': ['elsevier_txt'],
        'deps': [3]
    },
    6: {
        'name': 'ds_mult_prompts',
        'script': 'ds_mult_prompts.py',
        'folder': 'final',
        'description': 'Run LLM multi-prompt analysis on papers',
        'output_dirs': [],
        'deps': [4, 5]
    },
    7: {
        'name': 'merge_metadata_and_results',
        'script': 'merge_metadata_and_results.py',
        'folder': 'final',
        'description': 'Merge metadata with LLM results',
        'output_dirs': [],
        'deps': [6]
    },
    8: {
        'name': 'comprehensive_dict2csv',
        'script': 'comprehensive_dict2csv.py',
        'folder': 'final',
        'description': 'Generate final comprehensive CSV (final_db_HEAs.csv)',
        'output_dirs': [],
        'deps': [7]
    },
}

# Timeout settings per step (in seconds)
# LLM steps (6) need very long timeouts; set None for no timeout
STEP_TIMEOUTS = {
    1: 3600 * 6,    # 6 hours for downloads
    2: 3600 * 6,
    3: 3600 * 6,
    4: 3600 * 12,   # 12 hours for PDF parsing
    5: 3600 * 6,
    6: None,         # No timeout for LLM step (can run very long)
    7: 3600 * 2,    # 2 hours
    8: 3600 * 2,
}

# Folder path mapping
FOLDER_PATHS = {
    'downloaders': DOWNLOADERS_DIR,
    'processors': PROCESSORS_DIR,
    'final': FINAL_DIR,
}

# ==================== Logging Setup ====================
log_file = WORK_DIR / 'pipeline.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_file, mode='w', encoding='utf-8'),
    ]
)
logger = logging.getLogger(__name__)


# ==================== Status Management ====================
def load_status():
    """Load pipeline status from file."""
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            return json.load(f)
    return {'completed_steps': {}, 'start_time': None, 'end_time': None}


def save_status(status):
    """Save pipeline status to file."""
    with open(STATUS_FILE, 'w') as f:
        json.dump(status, f, indent=2, default=str)


def mark_step_completed(step_id):
    """Mark a step as completed."""
    status = load_status()
    status['completed_steps'][str(step_id)] = {
        'status': 'completed',
        'completed_at': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    save_status(status)


def mark_step_failed(step_id, error=None):
    """Mark a step as failed."""
    status = load_status()
    status['completed_steps'][str(step_id)] = {
        'status': 'failed',
        'error': str(error) if error else '',
        'failed_at': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    save_status(status)


def is_step_completed(step_id):
    """Check if a step has been completed."""
    status = load_status()
    return status['completed_steps'].get(str(step_id), {}).get('status') == 'completed'


def show_status():
    """Show pipeline status."""
    logger.info("=" * 60)
    logger.info("Pipeline Status")
    logger.info("=" * 60)
    status = load_status()
    logger.info(f"Start time: {status.get('start_time', 'N/A')}")
    logger.info(f"End time: {status.get('end_time', 'N/A')}")
    logger.info("")

    for step_id, step_info in STEPS.items():
        step_status = status['completed_steps'].get(str(step_id), {})
        status_str = step_status.get('status', 'pending')
        completed_at = step_status.get('completed_at', '')
        error = step_status.get('error', '')

        deps = step_info['deps']
        if deps:
            dep_str = f" (depends on: {', '.join(str(d) for d in deps)})"
        else:
            dep_str = " (no dependencies)"

        if status_str == 'completed':
            icon = "[OK]"
        elif status_str == 'failed':
            icon = "[FAIL]"
        else:
            icon = "[ ]"

        logger.info(f"  {icon} Step {step_id}: {step_info['description']}")
        logger.info(f"      Script: {step_info['folder']}/{step_info['script']}{dep_str}")
        logger.info(f"      Status: {status_str}" + (f"  ({completed_at})" if completed_at else ""))
        if error:
            logger.info(f"      Error: {error}")
        logger.info("")

    logger.info("-" * 60)
    logger.info("Output files:")
    expected_files = [
        'rsc/', 'springer/', 'elsevier/', 'rsc-spr-mds/', 'elsevier_txt/',
        'database_of_all_prompts.csv', 'database_of_raw_responses.csv',
        'db_HEAs.csv', 'final_db_HEAs.csv', 'pipeline.log'
    ]
    for f in expected_files:
        full_path = WORK_DIR / f
        if full_path.exists():
            if full_path.is_dir():
                file_count = sum(1 for _ in full_path.rglob('*') if _.is_file())
                logger.info(f"  [EXISTS] {f} ({file_count} files)")
            else:
                size_mb = full_path.stat().st_size / (1024 * 1024)
                logger.info(f"  [EXISTS] {f} ({size_mb:.1f} MB)")
        else:
            logger.info(f"  [MISSING] {f}")


# ==================== Environment Validation ====================
def validate_environment():
    """Validate that required files and directories exist."""
    logger.info("Validating environment...")

    # Check required files
    for req_file in REQUIRED_FILES:
        if not (WORK_DIR / req_file).exists():
            logger.error(f"  Required file not found: {req_file}")
            logger.error(f"  Please ensure {req_file} is in the pipeline root directory.")
            return False

    # Check script directories exist
    for folder_name, folder_path in FOLDER_PATHS.items():
        if not folder_path.exists():
            logger.error(f"  Script directory not found: {folder_path}")
            logger.error(f"  Please create {folder_name}/ and place scripts inside.")
            return False

    # Check all scripts exist
    for step_id, step_info in STEPS.items():
        script_path = FOLDER_PATHS[step_info['folder']] / step_info['script']
        if not script_path.exists():
            logger.error(f"  Script not found: {script_path}")
            return False

    logger.info("  Environment validation passed.")
    return True


# ==================== Step Execution ====================
def run_step(step_id):
    """
    Execute a single pipeline step.

    Returns:
        bool: True if step completed successfully, False otherwise.
    """
    step = STEPS[step_id]
    logger.info(f"")
    logger.info(f"{'=' * 60}")
    logger.info(f"Step {step_id}: {step['description']}")
    logger.info(f"{'=' * 60}")

    # Create output directories
    for dir_name in step.get('output_dirs', []):
        dir_path = WORK_DIR / dir_name
        dir_path.mkdir(exist_ok=True)
        logger.info(f"  Output directory: {dir_path}")

    # Check if already completed (for resume)
    if is_step_completed(step_id):
        logger.info(f"  Step {step_id} already completed. Skipping (use --force to re-run).")
        return True

    # Build script path from folder
    folder_path = FOLDER_PATHS[step['folder']]
    script_path = folder_path / step['script']

    timeout = STEP_TIMEOUTS.get(step_id)

    logger.info(f"  Running: {step['folder']}/{step['script']}")
    if timeout:
        logger.info(f"  Timeout: {timeout / 3600:.1f} hours")
    else:
        logger.info(f"  Timeout: unlimited")

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(WORK_DIR),
            capture_output=False,
            timeout=timeout
        )
        if result.returncode != 0:
            logger.error(f"  Step {step_id} failed with return code {result.returncode}")
            mark_step_failed(step_id, f"Return code: {result.returncode}")
            return False

        mark_step_completed(step_id)
        logger.info(f"  Step {step_id} completed successfully!")
        return True

    except subprocess.TimeoutExpired:
        logger.error(f"  Step {step_id} timed out!")
        mark_step_failed(step_id, "Timeout")
        return False

    except KeyboardInterrupt:
        logger.warning(f"  Step {step_id} interrupted by user!")
        mark_step_failed(step_id, "KeyboardInterrupt")
        return False

    except Exception as e:
        logger.error(f"  Step {step_id} failed with exception: {e}")
        mark_step_failed(step_id, str(e))
        return False


# ==================== Dependency Resolution ====================
def get_parallel_groups(step_ids):
    """
    Get parallel execution groups for the given step IDs.

    Returns:
        list: List of lists, where each inner list contains step IDs that can run in parallel.
    """
    groups = []
    remaining = set(step_ids)
    completed = set()

    while remaining:
        ready = []
        for sid in remaining:
            step = STEPS[sid]
            deps = [d for d in step['deps'] if d in step_ids]
            if all(d in completed for d in deps):
                ready.append(sid)

        if not ready:
            logger.error(f"  Cannot execute steps {remaining} - unmet dependencies!")
            break

        groups.append(ready)
        completed.update(ready)
        remaining -= set(ready)

    return groups


# ==================== Pipeline Orchestration ====================
def run_pipeline(step_ids=None, force=False, resume=False):
    """
    Run the pipeline with the specified steps.

    Args:
        step_ids: List of step IDs to run. If None, run all steps.
        force: If True, re-run completed steps.
        resume: If True, skip already completed steps.
    """
    if step_ids is None:
        step_ids = list(STEPS.keys())

    if not validate_environment():
        sys.exit(1)

    # Record start time
    status = load_status()
    status['start_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
    save_status(status)

    logger.info("")
    logger.info("=" * 60)
    logger.info("HEA Paper Processing Pipeline")
    logger.info(f"Working directory: {WORK_DIR}")
    logger.info(f"Steps to run: {step_ids}")
    logger.info(f"Force mode: {force}")
    logger.info(f"Resume mode: {resume}")
    logger.info("=" * 60)
    logger.info("")

    groups = get_parallel_groups(step_ids)

    for group_idx, group in enumerate(groups):
        group_name = {0: "Group 1 (Downloads)", 1: "Group 2 (Processing)", 2: "Group 3 (Final)"}
        logger.info(f"--- {group_name.get(group_idx, f'Phase {group_idx + 1}')}: Steps {group} ---")

        if len(group) == 1:
            logger.info(f"  Sequential step:")
            step_id = group[0]
            if resume and is_step_completed(step_id) and not force:
                logger.info(f"  Step {step_id} already completed. Skipping.")
                continue
            if not run_step(step_id):
                logger.error(f"Pipeline failed at step {step_id}. Stopping.")
                sys.exit(1)
        else:
            logger.info(f"  Parallel steps (running concurrently):")
            # Check which steps are already completed
            pending = []
            for sid in group:
                if resume and is_step_completed(sid) and not force:
                    logger.info(f"  Step {sid} already completed. Skipping.")
                else:
                    pending.append(sid)

            if not pending:
                logger.info(f"  All steps in this group already completed. Skipping.")
                continue

            success = True
            with ThreadPoolExecutor(max_workers=len(pending)) as executor:
                futures = {}
                for sid in pending:
                    futures[executor.submit(run_step, sid)] = sid

                for future in as_completed(futures):
                    sid = futures[future]
                    try:
                        result = future.result()
                        if not result:
                            success = False
                    except Exception as e:
                        logger.error(f"  Step {sid} raised exception: {e}")
                        success = False

            if not success:
                logger.error(f"Pipeline failed in {group_name.get(group_idx, f'phase {group_idx + 1}')}. Stopping.")
                sys.exit(1)

    # Record end time
    status = load_status()
    status['end_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
    save_status(status)

    logger.info("")
    logger.info("=" * 60)
    logger.info("Pipeline completed successfully!")
    logger.info("=" * 60)

    logger.info("")
    logger.info("Generated files:")
    for item in sorted(WORK_DIR.iterdir()):
        if item.is_dir() and item.name not in ['__pycache__', 'venv']:
            file_count = sum(1 for _ in item.rglob('*') if _.is_file())
            logger.info(f"  {item.name}/ ({file_count} files)")
        elif item.suffix in ['.csv', '.log']:
            size_mb = item.stat().st_size / (1024 * 1024)
            logger.info(f"  {item.name} ({size_mb:.1f} MB)")


# ==================== Cleanup ====================
def cleanup():
    """Clean up pipeline output directories and status file."""
    logger.info("Cleaning up pipeline output...")
    dirs_to_clean = ['rsc', 'springer', 'elsevier', 'rsc-spr-mds', 'elsevier_txt']
    files_to_clean = [
        'database_of_all_prompts.csv',
        'database_of_raw_responses.csv',
        'db_HEAs.csv',
        'final_db_HEAs.csv',
        'pipeline.log',
        '.pipeline_status.json',
    ]

    for d in dirs_to_clean:
        path = WORK_DIR / d
        if path.exists():
            import shutil
            shutil.rmtree(path)
            logger.info(f"  Removed: {d}/")

    for f in files_to_clean:
        path = WORK_DIR / f
        if path.exists():
            path.unlink()
            logger.info(f"  Removed: {f}")

    logger.info("Cleanup complete.")


# ==================== Main Entry Point ====================
def main():
    parser = argparse.ArgumentParser(
        description='HEA Paper Processing Pipeline Orchestrator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                          Run entire pipeline
  python main.py --step 1,2,3             Run only steps 1-3 (downloads)
  python main.py --step 6                 Run only step 6 (LLM analysis)
  python main.py --resume                 Resume from last position
  python main.py --status                 Show pipeline status
  python main.py --cleanup                Clean all generated files
  python main.py --force --step 4         Force re-run step 4
        """
    )
    parser.add_argument(
        '--step', type=str, default=None,
        help='Comma-separated list of step IDs to run (e.g., "1,2,3")'
    )
    parser.add_argument(
        '--resume', action='store_true', default=False,
        help='Resume from last completed step (skip already completed)'
    )
    parser.add_argument(
        '--force', action='store_true', default=False,
        help='Force re-run of completed steps'
    )
    parser.add_argument(
        '--status', action='store_true', default=False,
        help='Show pipeline status'
    )
    parser.add_argument(
        '--cleanup', action='store_true', default=False,
        help='Clean all generated files and directories'
    )

    args = parser.parse_args()

    if args.status:
        show_status()
        return

    if args.cleanup:
        cleanup()
        return

    step_ids = None
    if args.step:
        try:
            step_ids = [int(s.strip()) for s in args.step.split(',')]
            for sid in step_ids:
                if sid not in STEPS:
                    logger.error(f"Invalid step ID: {sid}. Valid steps: {list(STEPS.keys())}")
                    sys.exit(1)
        except ValueError:
            logger.error(f"Invalid step IDs: {args.step}. Use comma-separated integers.")
            sys.exit(1)

    run_pipeline(step_ids=step_ids, force=args.force, resume=args.resume)


if __name__ == '__main__':
    main()