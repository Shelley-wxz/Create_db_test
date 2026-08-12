#解析纯xml 和 pdf文件


from os import listdir
from os.path import isfile, join
import os

import lxml.etree as ET

try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

output_folder = "elsevier_txt"
# 2. 如果文件夹不存在，就自动创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def detect_file_type(file_path):
    """Detect whether the file is XML or PDF by checking the file header."""
    with open(file_path, 'rb') as f:
        header = f.read(5)
    if header.startswith(b'%PDF'):
        return 'pdf'
    elif header.startswith(b'<?xml') or header.startswith(b'<\?xml') or header.startswith(b'<!DOCTYPE') or header.startswith(b'<'):
        return 'xml'
    else:
        # Try to parse as XML to see if it works
        return 'xml'  # default fallback


def extract_namespaces(xml_file):
    """
    Extract all namespaces from the XML file and create a prefix-to-namespace mapping.
    """
    events = ("start", "start-ns")
    ns_map = {}
    for event, elem in ET.iterparse(xml_file, events):
        if event == "start-ns":
            prefix, uri = elem
            ns_map[prefix] = uri
        else:
            break  # Only need to parse the root element for namespaces
    return ns_map


def extract_text(element):
    """
    Recursively extract text content from an XML element, including tail texts.
    """
    texts = []
    if element.text:
        texts.append(element.text)
    for child in element:
        texts.append(extract_text(child))
        if child.tail:
            texts.append(child.tail)
    return ''.join(texts)


def extract_article_content_xml(xml_file):
    """Extract article content from Elsevier XML format."""
    namespaces = extract_namespaces(xml_file)

    parser = ET.XMLParser(remove_blank_text=True)
    tree = ET.parse(xml_file, parser)
    root = tree.getroot()

    default_ns = root.nsmap.get(None)
    if default_ns:
        namespaces['default'] = default_ns

    coredata = root.find('.//{%s}coredata' % namespaces.get('default', ''), namespaces)
    if coredata is None:
        print("No coredata found in the XML.")
        return None

    title = coredata.find('.//{%s}title' % namespaces.get('dc', ''), namespaces)
    doi = coredata.find('.//{%s}doi' % namespaces.get('prism', ''), namespaces)
    publication_name = coredata.find('.//{%s}publicationName' % namespaces.get('prism', ''), namespaces)
    publication_date = coredata.find('.//{%s}coverDate' % namespaces.get('prism', ''), namespaces)
    description_element = coredata.find('.//{%s}description' % namespaces.get('dc', ''), namespaces)
    description = extract_text(description_element).strip() if description_element is not None else ''

    original_text = root.find('.//{%s}originalText' % namespaces.get('default', ''), namespaces)
    if original_text is None:
        print("No originalText found in the XML.")
        return None

    doc = original_text.find('.//{%s}doc' % namespaces.get('xocs', ''), namespaces)
    if doc is None:
        print("No doc found in originalText.")
        return None

    serial_item = doc.find('.//{%s}serial-item' % namespaces.get('xocs', ''), namespaces)
    if serial_item is None:
        print("No serial-item found in doc.")
        return None

    article = serial_item.find('.//{%s}article' % namespaces.get('ja', ''), namespaces)
    if article is None:
        print("No article found in serial-item.")
        return None

    body = article.find('.//{%s}body' % namespaces.get('ja', ''), namespaces)
    if body is None:
        print("No body found in article.")
        return None

    article_content = ""

    for section in body.findall('.//{%s}section' % namespaces.get('ce', ''), namespaces):
        section_title_element = section.find('.//{%s}section-title' % namespaces.get('ce', ''), namespaces)
        if section_title_element is not None:
            section_title = extract_text(section_title_element).strip()
            if section_title:
                article_content += f"\n\n{section_title}\n"

        for para in section.findall('.//{%s}para' % namespaces.get('ce', ''), namespaces):
            para_text = extract_text(para).strip()
            if para_text:
                article_content += f"\n{para_text}"

    article_data = {
        'title': title.text.strip() if title is not None else '',
        'doi': doi.text.strip() if doi is not None else '',
        'publication_name': publication_name.text.strip() if publication_name is not None else '',
        'publication_date': publication_date.text.strip() if publication_date is not None else '',
        'abstract': description,
        'content': article_content.strip()
    }

    return article_data


def extract_article_content_pdf(pdf_file):
    """Extract article content from PDF format (when .xml file is actually a PDF)."""
    if not HAS_FITZ:
        print("PyMuPDF (fitz) is not installed. Please install it with: pip install pymupdf")
        return None

    doc = fitz.open(pdf_file)

    # Extract metadata
    metadata = doc.metadata
    title = metadata.get('title', '') or ''
    author = metadata.get('author', '') or ''
    subject = metadata.get('subject', '') or ''
    creator = metadata.get('creator', '') or ''

    # Extract full text from all pages
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n"

    doc.close()

    # Try to extract DOI from text
    doi = ''
    import re
    doi_match = re.search(r'10\.\d{4,9}/[^\s]+', full_text)
    if doi_match:
        doi = doi_match.group(0)
    # Also check subject field
    if not doi and subject:
        doi_match2 = re.search(r'doi:\s*(10\.\d{4,9}/[^\s]+)', subject)
        if doi_match2:
            doi = doi_match2.group(1).replace('doi:', '')

    # Try to extract publication name from subject or text
    publication_name = ''
    if subject:
        # Subject often contains journal info like "Journal of Materials Research and Technology, 33 (2024) 9405-9414"
        pub_match = re.match(r'([^,]+),', subject)
        if pub_match:
            publication_name = pub_match.group(1).strip()
    if not publication_name and creator:
        publication_name = creator

    # Try to extract publication date
    publication_date = ''
    # Check subject for date info
    date_match = re.search(r'(\d{4})', subject)
    if date_match:
        publication_date = date_match.group(1)
    # Check creationDate from metadata
    if not publication_date:
        creation_match = re.search(r'(\d{4})', str(metadata.get('creationDate', '')))
        if creation_match:
            publication_date = creation_match.group(1)

    # Extract abstract
    abstract = ''
    abstract_match = re.search(r'(?i)A\s*B\s*S\s*T\s*R\s*A\s*C\s*T\s*(.*?)(?=1\.\s*Introduction|Keywords|A\s*R\s*T\s*I\s*C\s*L\s*E\s*I\s*N\s*F\s*O|References)', full_text, re.DOTALL)
    if abstract_match:
        abstract = abstract_match.group(1).strip()
        # Clean up the abstract
        abstract = re.sub(r'\s+', ' ', abstract).strip()
    else:
        # Try simpler pattern
        abstract_match2 = re.search(r'(?i)(A\s*B\s*S\s*T\s*R\s*A\s*C\s*T\s*)(.*?)(?=\d+\.\s*[Ii]ntroduction)', full_text, re.DOTALL)
        if abstract_match2:
            abstract = abstract_match2.group(2).strip()
            abstract = re.sub(r'\s+', ' ', abstract).strip()

    # Clean the full text content - remove page numbers and headers
    content = full_text.strip()
    # Remove footer lines like "H. Yi et al. Journal of Materials Research and Technology 33 (2024) 9405–9414 9406"
    content = re.sub(r'[A-Z]\.\s*Yi\s*et\s*al\.\s*\n\s*Journal of Materials Research and Technology \d+ \(\d{4}\) \d+-\d+ \d+\n?', '', content)
    # Remove standalone page numbers
    content = re.sub(r'\n\d{4,5}\s*\n', '\n', content)
    # Clean up extra whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)

    article_data = {
        'title': title.strip() if title else '',
        'doi': doi.strip() if doi else '',
        'publication_name': publication_name.strip() if publication_name else '',
        'publication_date': publication_date.strip() if publication_date else '',
        'abstract': abstract,
        'content': content
    }

    return article_data


def extract_article_content(file_path):
    """
    Main extraction function that auto-detects file type (XML or PDF) and extracts article content.
    """
    file_type = detect_file_type(file_path)

    if file_type == 'pdf':
        print(f"[INFO] Detected PDF file (despite .xml extension): {file_path}")
        return extract_article_content_pdf(file_path)
    else:
        print(f"[INFO] Detected XML file: {file_path}")
        return extract_article_content_xml(file_path)


# Usage example
if __name__ == "__main__":
    mypath = "elsevier"
    yes, no = 0, 0
    for xml_file_path in [f for f in listdir(mypath) if isfile(join(mypath, f))]:
        if xml_file_path.startswith('.'):
            continue  # 跳过隐藏文件（如 .DS_Store）

        full_path = join(mypath, xml_file_path)

        article_data = extract_article_content(full_path)

        if article_data:
            # Print the extracted content
            print("Title:", article_data['title'])
            print("DOI:", article_data['doi'])
            print("Publication Name:", article_data['publication_name'])
            print("Publication Date:", article_data['publication_date'])
            print("\nAbstract:", article_data['abstract'])
            # print("\nArticle Content:", article_data['content'])

            # Save the article content to a text file
            output_file_path = os.path.join(output_folder, f"{article_data['doi'].replace('/', '-')}.txt")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(f"Title: {article_data['title']}\n")
                f.write(f"DOI: {article_data['doi']}\n")
                f.write(f"Publication Name: {article_data['publication_name']}\n")
                f.write(f"Publication Date: {article_data['publication_date']}\n\n")
                f.write(f"Abstract:\n{article_data['abstract']}\n\n")
                f.write(f"Article Content:\n{article_data['content']}\n")
            yes += 1
            print(f"文件已成功保存到: {output_file_path}")
        else:
            print("Failed to extract article data.")
            print(xml_file_path)
            no += 1
    print(f"converted: {yes}")
    print(f"failed {no}")
