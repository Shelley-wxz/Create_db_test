
# Digital Discovery

# Accepted Manuscript

Published on 28 July 2026

Licensed under CC-BY-NC 4.0

Check for updates

# Volume 1

# Number 1

# January 2022

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the Information for Authors.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal’s standard Terms &#x26; Conditions and the Ethical guidelines still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

ISSN 2635-098X

rsc.li/digitaldiscovery




Page 1 of 13    Digital Discovery

# Electronic manifolds for extrapolative alloy discovery

Pranoy Rayᵃ,ᵇ,ᶜ, Sayan Bhowmikᵈ, Phanish Suryanarayanaᶜ,ᵉ, Surya R. Kalidindiᵇ,ᶜ and Andrew J. Medfordᵈ†

Digital Discovery Accepted Manuscript

This study presents a computationally efficient framework for accelerated alloy discovery that uses the non-interacting electron density to capture intrinsic structure-property relationships in refractory high-entropy alloys (HEAs). Unlike state-of-the-art approaches relying on expensive, self-consistent density functional theory calculations, our method employs the non-interacting electron density as the primary structural descriptor. By extracting physical features through directionally resolved two-point spatial correlations and compressing them via Principal Component Analysis, we efficiently map the design space. Coupling these descriptors with Bayesian active learning, we achieve a normalized mean absolute error (NMAE) of &#x3C;2% for the bulk modulus of Al-Nb-Ti-Zr alloys using only 10 training samples (&#x3C;0.2% of the dataset). Furthermore, we demonstrate that the model learns an electronic packing manifold that is transferable within the refractory BCC alloy family. Validated on a distinct 7-component refractory system (Mo-Nb-Ta-Ti-V-W-Zr) containing four elements entirely absent from the training data, the framework enables intra-family transfer within the refractory BCC alloy class. An internal cross-composition ablation within D4, training exclusively on ANb-dominant compositions and testing on a disjoint Ti+Zr-dominant subset, yields NMAE = 2.4% and R2 = 0.8, further confirming cross-group descriptor transferability without requiring additional DFT calculations. Moreover, by augmenting the base model with just 20 samples from the target domain (&#x3C;0.1% of the total dataset), we achieve high-fidelity predictions (NMAE &#x3C; 3%) for 7-component alloys, reducing data acquisition costs by orders of magnitude compared to standard workflows. A controlled comparison confirms that composition-based descriptors under the identical pipeline do not reach the same accuracy threshold within the same sample budget, establishing that the spatial autocorrelation encoding of the non-interacting electron density provides information beyond elemental composition statistics alone.

# Introduction

High-entropy alloys (HEAs)1–3 encompass a vast compositional design space that offers exceptional tunability for mechanical and thermal properties, yet this combinatorial magnitude renders exhaustive experimental exploration intractable. While Kohn-Sham density functional theory (DFT)4,5 offers first-principles accuracy6–8, its large computational cost and O(N3) scaling with system size render exhaustive high-throughput screening9,10 of HEA compositional spaces computationally prohibitive. Machine learning (ML) surrogates11–21 address this by approximating property predictions at reduced cost. Recent efforts have further enhanced sample efficiency through Bayesian active learning22–34 and Gaussian Process Regression (GPR)35–40, though their efficacy depends critically on the choice of structural descriptors.

Recent advances10,41–44 in physics-based feature engineering have established the electron density field as a robust, chemically agnostic descriptor for atomic structures. These methods are powerful because the converged charge density encodes the quantum mechanical ground state, but this fidelity comes at substantial computational cost. State-of-the-art frameworks, such as the Voxelized Atomic Structure (VASt) method45–47, utilize the fully converged electron density field to quantify structural features via two-point spatial correlations10,13,48–51. While these descriptors achieve high fidelity, they create a fundamental inefficiency: the calculation of the electronic ground state via self-consistent field (SCF) iteration, the dominant computational cost in static DFT, must be completed for every candidate structure merely to render predictions.

Journal     [vol.] Name, [year],   ,  | 1–12  1


Digital Discovery    Page 2 of 13

ate input features for the surrogate model. This limits the primary value proposition of machine learning surrogates, as the computational budget required for feature generation becomes comparable to that of directly computing the target property.

# Data Curation and Design Space

This study investigates the quaternary Al-Nb-Ti-Zr refractory HEA system, spanning a large compositional space defined by:

D₄ = AlαNbβTiγZrδ     α, β, γ, δ ∈ {0, 4,..., 128},

α + β + γ + δ = 128.

This discrete set yields a total of 6,545 unique structures when including elemental, binary, ternary, and quaternary compositions, and 4,495 alloys when restricted to the quaternary space. To validate the extrapolative transferability of the model, we leverage the distinct 7-component domain (D₇) which contains 12012 unique compositions, defined by the set:

D₇ = MoαNbβTaγTiδVεWζZrη    α,..., η ∈ {0, 15, 23, 30, 38,..., 105, 128},

α + β + γ + δ + ε + ζ + η = 128.

The ground truth values for bulk modulus and alloy formation energy were obtained from the converged DFT dataset established by Barry et al. Note that the alloy formation energies were available only for D₄.

# Background

# Pseudo-Density

In this framework, the material structure is defined by the pseudo-density field, ρpseudo: Ω → R≥0, where Ω ⊂ R3 represents the spatial domain of the atomic system. This framework’s key innovation is bypassing the computationally expensive SCF cycle. While converged densities require iterative Hamiltonian diagonalization, pseudo-densities are constructed via a single-shot superposition of isolated atom electron densities, where each element contributes its valence electron density according to its specific spatial distribution. This effectively decouples feature generation from the computationally expensive electronic relaxation process.

In this work, we present a framework integrating pseudo-density descriptors: quantified via two-point spatial correlations and PCA, with Gaussian Process Regression (GPR) driven Bayesian active learning. We validate the approach on the Al-Nb-Ti-Zr system (D₄), achieving R² > 0.97 for both bulk modulus and alloy formation energy. Notably, the bulk modulus model attains a normalized mean absolute percentage error (NMAE) of &#x3C; 2% using only 10 training samples, surpassing benchmarks utilizing converged densities. We further demonstrate extrapolative power by applying the D₄-trained model to a distinct 7-component system (D₇: Mo-Nb-Ta-Ti-V-W-Zr). The framework enables zero-shot transfer within the refractory BCC alloy class, and with the augmentation of just 20 actively selected D₇ samples, recovers high-fidelity predictions (NMAE &#x3C; 3%), establishing pseudo-density as a practical descriptor for sample-efficient refractory alloy discovery.

Journal     [vol.] Name, 2 |                 [year],   , 1–12


Page 3 of 13 Digital Discovery

braries. The pseudo-density was mapped onto a 3D real-space mean charge density, while subsequent components resolve the complex spatial patterns associated with local atomic disorder. The low-dimensional representation maintains the physical hierarchy of the alloy system. As illustrated in Figure 1 for D₄, the data points naturally arrange into a trapezoidal geometry where pure elements occupy the vertices and all alloy compositions fill the interior volume. This smooth variation of principal component scores across the composition space facilitates robust interpolation and accurate property prediction for unexplored alloy stoichiometries. Because this dimensionality reduction is unsupervised, the resulting descriptors are property-agnostic and can be reused to train independent models for different target properties, e.g., mechanical or thermodynamic, without re-computation. Notably, this unsupervised PC projection remains fixed regardless of the target property, allowing the same structural map to be colored by distinct physical responses, e.g., bulk modulus or alloy formation energy: see Figure 1 to reveal property-specific manifolds.

Based on the variance and loading-vector analysis, we truncate the descriptor space to the first three principal components for all subsequent regression modeling. The scree plot shows a pronounced elbow after PC3, with PC1 capturing ∼36% of variance and PCs 2-3 capturing ∼2.5% and ∼2% respectively, followed by a near-flat decay through PC4–50 (each &#x3C;0.5%). Inspection of the PC loading vectors (center slices of the 3D autocorrelation basis) confirms that PC1–3 display spatially coherent, periodic patterns reflecting the BCC lattice structure, elemental density contrast, and compositional disorder respectively. PC4 and above exhibit progressively higher spatial-frequency content with no discernible periodic structure, indicating that they encode stochastic noise in the autocorrelation representation rather than chemically interpretable structural features. These three components therefore capture the full chemically relevant structural hierarchy, and their empirical sufficiency is further evidenced by R² ≥ 0.98 achieved in-domain.

Because ρpseudo requires no iterative Hamiltonian diagonalization (and takes ∼30 seconds per sample), its generation scales as O(Ngrid) per structure, a single-pass operation, compared to O(NSCF × N3) for a converged DFT charge density, yielding a reduction in descriptor generation cost of approximately two orders of magnitude for the 128-atom BCC SQS supercells used in this work.

# Impact of Structural Relaxation on Manifold Topology

A critical and counter-intuitive finding of this work is that structural descriptors derived from initial SQS configurations with a uniform, common lattice constant yield a more cohesive feature space than those derived from fully relaxed geometries. Figure 1 visualizes the Principal Component space for the initial uniform SQS structures compared to those relaxed via VASP and MACE (see plots c, d, e and f in Supplementary Figure ??). Here, relaxation refers to the full optimization of both internal ionic coordinates and cell volume. The uniform SQS data forms a continuous, cohesive simplex, where the variance is driven purely by the combinatorial arrangement of chemical species. In contrast, the relaxed structures fracture into a distinct, disjoint, hyper-branched topology.

This fracturing is fundamentally driven by the loss of volumetric uniformity during relaxation. In the uniform initial state, a globally constant spatial metric is enforced for the two-point spatial statistics across all samples. During relaxation, individual lattice metrics are altered, leading to a more complex topology.

* see Supplementary Figure ?? (a) and (b) and ?? (scree plot and PC basis vectors)

Journal [vol.] Name, [year], , 1–12 3


Digital Discovery    Page 4 of 13

the spatial metric, rather than strictly chemical variations. PCA aggressively captures this spatial dilation, fracturing the manifold into discrete arms. When the relaxed PC space is colored by the final relaxed lattice parameter, the distinct branches stratify perfectly by cell volume, with the arms corresponding to discrete lattice parameter bands (see Figure ??) scaling from approximately 12.8 Å to 14.2 Å. The terminal tips of these disjoint manifolds correspond exactly to the absolute structural limits of the dataset, specifically the highly expanded Zr-rich compositions.

To rigorously validate that this non-uniform volumetric scaling is the primary driver of the fracturing, we performed an ablation test where the absolute-grid fᵣ were divided by the cell volume (a³) before performing PCA (see Figure ??). This operation effectively normalizes the magnitude-dependent variance driven by the cell expansion. Suppressing this volume-dependent information caused the previously disjoint branches to coalesce back into a single, continuous cluster. This mathematically confirms that the geometric relaxation, specifically the variance in the final relaxed lattice constants, is responsible for the manifold fracturing.

It is worth noting that if the fᵣ were computed on a normalized grid using relative fractional coordinates (x/a), the affine volume expansion would be factored out, isolating the variance purely to local ionic displacements. However, by using the initial system’s pseudo-density with a uniform lattice constant on an absolute grid, we inherently bypass both the volumetric and ionic strain artifacts. By enforcing this globally constant spatial metric, we effectively treat the ideal lattice as a canonical reference state. It is important to acknowledge the trade-off explicitly: the smoother manifold topology observed for unrelaxed structures arises in part because physically meaningful variability-lattice mismatch strain, local ionic distortion, and site-specific bonding has been suppressed. For macroscopic, composition-averaged properties of ideal solid solutions, where bulk modulus and formation enthalpy are primarily determined by elemental identity and proportion rather than by individual SQS configurations, this suppression is a defensible approximation. The framework is not designed to capture configuration-sensitive properties, and performance on such quantities has not been tested. This enables the Gaussian Process to interpolate across a smooth manifold (f(chemistry) → Pproperty) without the interference of high-variance geometric noise introduced by relaxation.

# Physical basis for descriptor efficacy and transferability

Several physically grounded arguments underpin the efficacy of the pseudo-density for the properties and alloy class studied here. First, for macroscopic, composition-averaged properties of ideal disordered BCC solid solutions, such as bulk modulus and formation enthalpy, the dominant source of inter-composition variance is elemental identity and proportion rather than individual atomic configurations. In this regime, a descriptor that faithfully encodes the spatial envelope of valence electron overlap captures the primary variance driver without requiring full self-consistency. Second, the omission of electron-electron interactions and SCF relaxation is acceptable for these specific properties because electronic screening in metallic solid solutions constitutes a subordinate perturbation on the zeroth-order charge topology set by the

Journal [vol.] Name, 4 | [year], 1–12




Page 5 of 13    Digital Discovery

pseudo-density; the self-consistent correction is a composition-invariant shift that does not alter the relative ordering of compositions across the manifold. This is consistent with the empirical observation that the unrelaxed pseudo-density manifold is smoother and more predictive than that of relaxed structures. Third, intra-family transferability from D₄ to D₇ is physically enabled by the similarity of d-electron radial density profiles across the group 4–6 refractory metals (Ti, Zr, Nb, Mo, Ta, V, W): these elements share the same angular momentum quantum number and comparable effective nuclear charges, so their pseudopotential-derived valence densities are similar in spatial extent and nodal structure. Consequently, the autocorrelation features of Mo, Ta, V, and W fall in a region of feature space continuously connected to those of Nb, Ti, and Zr, enabling regression rather than requiring interpolation between disjoint clusters. Fourth, Al is an s-p metal whose diffuse, nearly-spherical valence density produces a qualitatively distinct autocorrelation signature, placing it at a spatially separated vertex of the D₄ simplex (visible in Figure 1). Because Al is absent from D₇, all D₇ compositions lie in the d-metal-dominated region of the joint manifold, away from the Al vertex. The zero-shot and few-shot predictions for D₇ therefore extrapolate within a chemically coherent subspace and do not require the model to generalize through the Al-anchored region of the descriptor space. It must be emphasized that this framework is explicitly designed for composition-averaged properties of single-phase disordered BCC solid solutions and is not expected to capture properties governed by local chemical order, short-range order, strain, magnetic ordering, defects, or finite-temperature configurational sampling.

# Model Building

# Gaussian Process Regression

We employ Gaussian Process Regression (GPR) to model the mapping between the low-dimensional structural features (PC scores) and the material properties. GPR provides a non-parametric, probabilistic framework that yields both a predictive mean and a variance, which is essential for uncertainty quantification. The covariance between inputs is computed using an Automatic Relevance Determination Squared Exponential (ARDSE) kernel:

k(x, x′) = σ² exp(- ½ ∑(D(xd - x′d)²) + σ²n δxx′)

where σ² scales the output variance, ld represents the characteristic length-scale for feature dimension d, and σ²n accounts for observation noise. The ARDSE kernel allows the model to inherently determine the relevance of each principal component, weighting them according to their influence on the target property. This choice reflects the expectation that different principal components encode distinct physical scales, e.g., mean density versus local disorder, and allows the GP to adapt its sensitivity accordingly. All hyperparameters are optimised by maximising the log marginal likelihood using the Adam optimiser for 200 epochs at a learning rate of 0.1.

# Bayesian Experiment Design

To minimize the computational expense of data generation, we utilize a Bayesian active learning strategy driven by a relative uncertainty acquisition function inspired by information-based design. Specifically, the acquisition selects candidate structures that maximize the ratio of predictive uncertainty to the predicted magnitude:

I(x) = σ(x) / µ(x)

In each iteration, the algorithm identifies the k structure with the highest I(x) for ground-truth evaluation. In a prospective discovery campaign, this step would selectively trigger DFT calculations for these specific unlabelled candidates, thereby augmenting the training set with high-fidelity data only where strictly necessary. While active learning strategies have been successfully applied to descriptors derived from converged densities, such workflows inherently face a "pre-computation" bottleneck: the computationally expensive SCF cycle must be completed for every candidate structure merely to generate the input features for the surrogate model. In contrast, our pseudo-density framework eliminates this redundancy, enabling the rapid, low-cost scanning of the entire candidate space.

Journal Name, [year], 1–12


Digital Discovery    Page 6 of 13

HEA SQS    Pseudo Electron Density    Autocorrelations    Unsupervised Analysis    Active Learning

Active Selection

Random Selection

20

10  20

Traising samples

Fig. 3 End-to-end Bayesian active learning workflow for D4. Starting from HEA Special Quasirandom Structures (SQS), the pseudo-density ρpseudo is constructed via single-pass superposition of isolated valence densities, bypassing the SCF cycle. Two-point spatial autocorrelations f are computed via FFT and compressed to three principal components. The GPR model is iteratively updated by querying ground-truth DFT labels only at the iest uncertainty candidates identified by the acquisition function I(x) = |σ (x)/µ(x)|, minimizing the number of expensive DFT calculations required.

date pool prior to triggering any expensive DFT calculations. This (R²). For a set of N predictions { ˆ } and corresponding ground-truth values {yi}, these are defined as

MAE = 1 N ∑ | ˆ - |, (6)

N i=1 yi yi

NMAE = MAE × 100%, (7)

where ¯ is the mean of the ground-truth values {yi}.

# Extrapolative Validation Protocol

To rigorously assess the transferability of the pseudo-density descriptors, we designed a disjoint training-testing protocol. The GPR model was actively trained exclusively on samples from the lower-order domain D₄ (Al-Nb-Ti-Zr). This model was then frozen and tasked with predicting the properties of the full extrapolation domain D₇ (Mo-Nb-Ta-Ti-V-W-Zr) without any re-training or exposure to the new chemical elements. This zero-shot transfer protocol evaluates whether the learned regression mapping f : PC → K generalizes across chemically distinct refractory systems without re-training, fine-tuning, or element-specific feature engineering. Both D₄ and D₇ share the BCC crystal structure and consist exclusively of group 4 to 6 transition metals; the transfer demonstrated here is therefore intra-family transfer within the refractory BCC alloy class, not unconditional extrapolation to arbitrary chemistries.

To further substantiate transferability using only existing data, we performed an internal cross-composition ablation entirely within D₄. The GPR model was trained exclusively on compositions in which the combined Al+Nb mole fraction exceeds 0.5 (group 13 and group 5 elements) and evaluated on a disjoint test set of compositions in which the combined Ti+Zr mole fraction exceeds 0.5 (group 4 elements). These subsets share no direct compositional overlap and represent elements from distinct periodic-table groups. Using Bayesian active learning on the Al+Nb training pool, the model achieves NMAE = 2.39% and R² = 0.808 on the Ti+Zr test set at 30 training samples, stabilizing around NMAE ≈ 1.6–1.7% and R² ≈ 0.89 from 20 samples onward, demonstrating that the pseudo-density descriptor encodes transferable valence overlap structure across compositionally and chemically distinct subregions of the same alloy family.

# Results and Discussion

# Performance on Bulk Modulus predictions

The GPR model demonstrates high predictive accuracy for the bulk modulus across the complete compositional dataset (D₄). The active learning campaign selects labels from a pre-existing DFT candidate pool over a fixed compositional grid 46, initialized with a minimal seed of 4 randomly selected samples, followed by iterative acquisition. As shown in Figure 2, the model stabilized rapidly, achieving an NMAE of &#x3C;2% with only 10 total training samples (4 seed + 6 active). This efficiency highlights a significant advantage over competing descriptor frameworks. While state-of-the-art methods typically require significantly larger datasets (10² –10³ samples) or approximately 26 samples for converged charge density descriptors 46 to reach convergence, our approach achieves this fidelity with fewer samples and orders of magnitude lower computational cost for feature generation.

The robustness of the pseudo-density descriptor is further evidenced by the performance of random sampling. As summarized in Table 1, even the random selection strategy yields high accuracy (R² = 0.98, MAE = 1.41 GPa) on the full dataset (D₄). This indicates that the unrelaxed pseudo-density manifold is naturally well-correlated with the mechanical response, such that complex active learning acquisition functions are not strictly required to achieve good global accuracy; though they still offer superior efficiency in the low-data limit. The parity plot in Figure 4(a) confirms this strong linear correlation (R² = 0.98) across the full range of 80 GPa to 160 GPa, confirming that the superposition of non-interacting electron densities contains sufficient physical information to resolve variations in mechanical stiffness without systematic bias.

# Error metrics

Across all experiments, model performance is quantified using the mean absolute error (MAE), normalized MAE (NMAE), mean absolute percentage error (MAPE), and coefficient of determination.

Journal     [vol.] Name, 6 |                [year],   , 1–12


Page 7 of 13    Digital Discovery

Fig. 4 Parity plots of predicted versus DFT-computed properties for all held-out samples in D4, with GPR predictive uncertainty shown as error bars (±1σ). (a) Bulk modulus predictions using a model trained on 10 actively selected samples (R² = 0.98, NMAE= 1.55%). (b) Alloy formation energy predictions using a distinct GPR model trained on 18 actively selected samples (R² = 0.99, NMAE= 2.20%), with uncertainty coverage of 88.8% within ±1σ and 99.8% within ±2σ.

|   |    | DFT-computed Bulk Moduli (GPa) | DFT-computed Alloy Formation Energy (eV) |     |     |     |     |     |
| - | -- | ------------------------------ | ---------------------------------------- | --- | --- | --- | --- | --- |
|   |    | 160                            | 140                                      | 120 | 100 | 80  | 60  | 40  |
|   | 80 | 100                            | 120                                      | 140 | 160 | -50 | -40 | -30 |

Fig. 5 Extrapolative performance of the D4-trained model on the full D7 bulk modulus dataset (12,012 compositions), following few-shot augmentation with 20 actively selected D7 samples. (a) Parity plot with GPR predictive uncertainty shown as error bars (±1σ). (b) Distribution of predicted standard deviations σ across all D7 test compositions. Coverage of 43.2% within ±1σ and 78.8% within ±2σ indicates moderate overconfidence in the extrapolative regime, consistent with GP posterior uncertainty being prior-dominated outside the training chemical space.

Performance on Alloy Formation Energy predictions. Crucially, this physics-based feature set exhibits high trans rabil- ity across properties. The same 3-PC pseudo-density features accurately predict both mechanical stiffness (bulk modulus) and thermodynamic stability (alloy formation energy) without modification. Starting with the same initial seed size of 4 samples, the active selection strategy applied to the full compositional space of D₄ (Table 1), achieves an MAE of 1.19 eV (2.20% NMAE) with an R² of 0.99.

| Material Property           | Strategy | MAE  | NMAE (%) | R²   |
| --------------------------- | -------- | ---- | -------- | ---- |
| Bulk Modulus (GPa)          | Active   | 1.50 | 1.55     | 0.98 |
|                             | Random   | 1.41 | 1.46     | 0.98 |
| Alloy Formation Energy (eV) | Active   | 1.19 | 2.20     | 0.99 |
|                             | Random   | 1.23 | 2.33     | 0.97 |

This result indicates that the pseudo electron density spatial correlations effectively capture the local chemical environment variations that dictate the properties.

Journal Name, [year], 1–12


Digital Discovery    Page 8 of 13

tate the energetic stability of the solid solution. The uncertainty from mean elemental proportions; and (iii) electronic character coverage for ∆Eform is similarly robust, achieving 88.8% within ±1σ and 99.8% within ±2σ.

# Comparative Performance and Scientific Implications

Table 1 summarizes the compiled error metrics, confirming that the pseudo-density descriptor yields high fidelity (R² ≥ 0.98) with both active and random sampling. While both strategies converge to similar accuracy in the limit, Figure 2 demonstrates that the active learning strategy provides a superior sample efficiency advantage in the low-data regime. The central finding of this study is the demonstration that pseudo electron densities are a sufficient structural descriptor for high-fidelity property prediction in complex alloy systems. PCA projections of the pseudo electron densities naturally recover the trapezoidal geometry of the 4-element structure space (Figure 1), placing elements at the vertices and alloys in the interior. This confirms that atomic packing and chemical identity; both captured by the pseudo-density, coordinate the structural hierarchy of HEAs. Electronic relaxation acts predominantly as a local perturbation relative to these primary chemical variations, though the geometric variance introduced by ionic relaxation is sufficient to fracture the low-dimensional manifold if not accounted for (as confirmed by both PCA and Partial Least Squares analyses). This indicates that for these HEA solid solutions, the electronic environment is dominated by the initial, superposition of atomic charges, and the subsequent self-consistent electronic relaxation introduces differences that are subordinate to the chemical variations across the design space. By replacing the converged density with the pseudo-density, the framework effectively decouples the feature generation step from the most computationally demanding part of the DFT calculation. This combination of eliminating the SCF bottleneck for feature generation and reducing the required number of training samples substantially enhances the feasibility of high-throughput computational materials discovery for HEAs. This efficiency gain does not merely accelerate existing workflows; it unlocks regimes previously inaccessible to DFT-based screening.

As demonstrated by the extrapolation results, the pseudo-density descriptor creates a transferable feature space that bridges distinct chemical systems. By projecting the 4-component and 7-component datasets into the same Principal Component space (as discussed in the Methods), we observe that they occupy overlapping manifolds. This indicates that the model predominantly learns electronic packing rules rather than overfitting to element-specific labels, enabling more rapid exploration of combinatorial spaces (including 5+ component systems) without the need to retrain on every new element. The pseudo-density’s advantage over composition-based representations stems from three physically distinct information channels that elemental fractions alone cannot encode: (i) the spatial distribution of valence charge, captured via the two-point autocorrelation fr, which distinguishes arrangements that are compositionally identical but structurally distinct; (ii) the configurational disorder of the SQS lattice, whose specific atomic arrangement modulates the local overlap topology of the superimposed densities beyond what is recoverable.

As summarized in Table 2 and illustrated in Figure 6, this rapid adaptation yields significant predictive accuracy. For the 5-component alloys, the model achieves an R² of 0.85 and a NMAE of 5.54%. As the chemical complexity increases to 7 components, the model maintains a strong correlation (R² = 0.68) and a low NMAE of 2.87%.

Journal     [vol.] Name, 8 |                [year],   , 1–12


Page 9 of 13 Digital Discovery

# Fig. 6 Few-shot domain adaptation performance by chemical complexity within D7.

| DFT-computed Bulk Moduli (GPa) |                     |                     |
| :----------------------------: | :-----------------: | :-----------------: |
|           5-component          |     6-component     |     7-component     |
|               300              |         300         |         300         |
|               250              |         250         |         250         |
|               200              |         200         |         200         |
|               150              |         150         |         150         |
|               100              |         100         |         100         |
|       100 150 200 250 300      | 100 150 200 250 300 | 100 150 200 250 300 |

Parity plots for (a) 5-component (R² = 0.85, NMAE = 5.54%), (b) 6-component (R² = 0.82, NMAE = 4.16%), and (c) 7-component (R² = 0.68, NMAE = 2.87%) alloys, obtained by augmenting the D₄-trained base model with 20 actively selected samples from the respective target domains. Error bars denote GPR predictive uncertainty (±1σ). The systematic improvement with increasing chemical complexity is consistent with the unseen-element fraction analysis in Supplementary Figure ??.

In Figure 5, the predictions track the y = x line closely. The accompanying uncertainty distribution (Figure 5, right panel) shows a peaked distribution of predicted standard deviations. Quantitative calibration on the D₇ test set yields coverage of 43.2% within ±1σ and 78.8% within ±2σ, indicating moderate overconfidence in the extrapolative regime: an expected consequence of predicting outside the training chemical space where the GP posterior uncertainty is governed by prior assumptions rather than observed data. Per-complexity calibration improves systematically with chemical complexity: 40.9%/76.3% (5-component), 51.6%/88.0% (6-component), and 67.3%/100.0% (7-component) within ±1σ/±2σ respectively, consistent with the unseen-element fraction analysis in Supplementary Figure ??.

This result directly addresses a central limitation of many descriptor-based machine learning approaches in materials science, namely the difficulty of extrapolating beyond the chemical species present in the training set. Unlike composition-based descriptors that require explicit knowledge of all constituent elements, the pseudo-density descriptor operates on a transferable electronic packing manifold. Because the local valence overlap environments in D₇ structurally resemble those in D₄ (confirmed by the PC-space overlap in Supp. Fig. ??), the regression mapping adapts rapidly to the new chemical labels with minimal data.

To provide a more granular assessment of the framework’s extrapolative capability, Supplementary Figure ?? reports NMAE as a function of the unseen-element mole fraction funseen = xMo + xTa + xV + xW, binned by quartile across D7. The result exhibits a monotonically decreasing NMAE from 10.17% at low funseen (Q1: compositions dominated by the shared elements Nb, Ti, Zr) to 3.86% at high funseen (Q4: compositions predominantly constituted by the four novel elements). To verify that this trend is not an artifact of the few-shot augmentation strategy, we examined the zero-shot quartile NMAE (no D₇ data at all) and found the values to be numerically identical: Q1 = 10.17%, Q2 = 7.01%, Q3 = 5.27%, Q4 = 3.86%. The monotonically decreasing trend therefore exists prior to any augmentation and is a genuine property of the model.

# Table 2 Extrapolative performance metrics.

The model was trained only on 4-component Al-Nb-Ti-Zr and tested on 5, 6, and 7-component alloys containing Mo, Ta, V, and W.

| Components | N (Test Samples) | NMAE (%) | MAE (GPa) |
| ---------- | ---------------- | -------- | --------- |
| 5          | 3675             | 5.54     | 9.20      |
| 6          | 882              | 4.16     | 7.01      |
| 7          | 49               | 2.87     | 4.89      |

# Conclusions

We demonstrated that the non-interacting electron density offers a rigorous and scalable alternative to standard DFT-based descriptors.

Journal Name, [year], 1–12 9


Digital Discovery
# 10

tors for HEA discovery. By decoupling descriptor generation from the SCF bottleneck, this framework effectively reduces the computational investment of high-throughput screening. The integration of this descriptor with Bayesian active learning demonstrated superior sample efficiency in the Al-Nb-Ti-Zr RHEA system. The framework achieved a NMAE of &#x3C;2% for the bulk modulus using only 10 actively selected training samples, surpassing the efficiency of state-of-the-art benchmarks that rely on fully converged densities. Beyond sample efficiency within the training domain, we demonstrated the model’s rigorous capability for chemical extrapolation. A model trained exclusively on the quaternary Al-Nb-Ti-Zr system successfully predicted the bulk moduli of a distinct 7-component system (Mo-Nb-Ta-Ti-V-W-Zr) containing four elements entirely absent from the training set. Furthermore, we demonstrated that augmenting this base model with just 20 samples from the target domain recovers high predictive fidelity (NMAE=2.87% for 7-component alloys). This suggests that the pseudo-density descriptor captures a transferable electronic packing manifold within the refractory BCC alloy family, enabling efficient few-shot domain adaptation without element-specific feature engineering. Furthermore, we demonstrate the property transferability of this singular feature set; without modification, the descriptors accurately predict alloy formation energies (achieving an R² of 0.99 for the full compositional space for D₄). The robustness of the approach was further validated through uncertainty quantification: bulk modulus predictions on D₄ achieve 65.1% and 92.3% coverage within ±1σ and ±2σ respectively, consistent with a well-calibrated GPR. In the extrapolative D₇ regime, coverage of 43.2%/±1σ and 78.8%/±2σ reflects expected mild overconfidence outside the training chemical space (Figure 5b). For the alloy formation energy, the coverage was even closer to nominal, with 88.8% and 99.8% of the data falling within ±1σ and ±2σ, respectively. Collectively, these results validate the voxelized atomic structure approach using pseudo-densities as a practical route to decoupling descriptor generation from the most computationally demanding stages of DFT.

# Author contributions

Pranoy Ray: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review &#x26; editing, Visualization. Sayan Bhowmik: Investigation, Software, Validation, Formal analysis, Writing – review &#x26; editing. Phanish Suryanarayana: Conceptualization, Methodology, Validation, Resources, Writing – review &#x26; editing, Supervision, Project administration, Funding acquisition. Surya R. Kalidindi: Conceptualization, Methodology, Validation, Resources, Writing – review &#x26; editing, Supervision, Project administration, Funding acquisition. Andrew J. Medford: Conceptualization, Methodology, Validation, Resources, Writing – review &#x26; editing, Supervision, Project administration, Funding acquisition.

# Acknowledgements

PR and SK acknowledge support from NSF DMREF Award 2119640. SB, PS, and AJM gratefully acknowledge the support of the U.S. Department of Energy, Office of Science under grant DE-SC0023445. PR also acknowledges support received from the Novelis Graduate Scholarship and the William H. Glenn Scholarship.

# Data availability

All data and scripts for feature engineering (computing pseudo electron densities &#x26; spatial correlations), model training, and post-processing (uncertainty analysis) are archived on Zenodo at https://doi.org/10.5281/zenodo.21339835. Alternatively, the codes are also available at https://github.com/pranoyray/AlloyDiscovery.

# Conflicts of interest

There are no conflicts to declare.

The overall reduction in computational investment by lowering the requisite DFT calculations via active learning facilitates the extensive exploration of vast compositional landscapes. Avenues for future research include: (i) validating transferability beyond BCC crystal structures, e.g., FCC and HCP systems, and across periodic-table blocks beyond the group 4–6 refractory metals studied here; (ii) testing robustness of the pseudo-density descriptor to different SQS realizations per composition, supercell sizes, and pair-correlation matching quality, to determine whether the model learns transferable alloy physics or a regularized fingerprint of a specific disorder proxy; (iii) incorporating temperature-dependent properties via on-the-fly machine-learned molecular dynamics, and (iv) extending the framework to predict functional properties, e.g., thermal conductivity, oxidation resistance, critical for high-temperature applications. Nonetheless, the demonstrated capacity for zero-shot transfer within the refractory BCC alloy class, and few-shot domain adaptation with as few as 20 target-domain labels, marks a meaningful step toward sample-efficient computational screening of complex refractory alloy spaces. The framework is explicitly scoped to

Journal [vol.] 10 | [year], 1–12


Page 11 of 13    Digital Discovery

References

1. S. O. Jeje and M. B. Shongwe, Engineering Reports, 2025, 7, e70141.
2. P. Dang, J. Hu, Y. Xian, C. Li, Y. Zhou, X. Ding, J. Sun and D. Xue, Advanced Materials, 2025, 37, 2412198.
3. D. P. Tabor, L. M. Roch, S. K. Saikin, C. Kreisbeck, D. Shberla, J. H. Montoya, S. Dwaraknath, M. Aykol, C. Ortiz, H. Tribukait, C. Amador-Bedolla, C. J. Brabec, B. Maruyama, K. A. Persson and A. Aspuru-Guzik, Nature Reviews Materials, 2018, 3, 5–20.
4. W. Kohn and L. J. Sham, Physical Review, 1965, 140, A1133–A1138.
5. P. Hohenberg and W. Kohn, Physical Review, 1964, 136, B864–B871.
6. B. Chakraborty, P. Ray, N. Garg and S. Banerjee, International Journal of Hydrogen Energy, 2021, 46, 4154–4167.
7. A. Kundu, A. Jaiswal, P. Ray, S. Sahu and B. Chakraborty, Journal of Physics D: Applied Physics, 2024, 57, 495502.
8. H. T. Nair, A. Kundu, P. Ray, P. K. Jha and B. Chakraborty, Sustainable Energy &#x26; Fuels, 2023, 7, 5109–5119.
9. S. Ramakrishna, T.-Y. Zhang, W.-C. Lu, Q. Qian, J. S. C. Low, J. H. R. Yune, D. Z. L. Tan, S. Bressan, S. Sanvito and S. R. Kalidindi, Journal of Intelligent Manufacturing, 2019, 30, 2307–2326.
10. P. Ray, K. Choudhary and S. R. Kalidindi, Integrating Materials and Manufacturing Innovation, 2025, 14, 1–13.
11. L. Ward, A. Agrawal, A. Choudhary and C. Wolverton, npj Computational Materials, 2016, 2, 1–7.
12. L. Ward, A. Dunn, A. Faghaninia, N. E. R. Zimmermann, S. Bajaj, Q. Wang, J. Montoya, J. Chen, K. Bystrom, M. Dylla, K. Chard, M. Asta, K. A. Persson, G. J. Snyder, I. Foster and A. Jain, Computational Materials Science, 2018, 152, 60–69.
13. P. Ray, A. R. Castillo, M. Kolel-Veetil and S. R. Kalidindi, Advanced Science, 2026, n/a, e23817.
14. X. Lei and A. J. Medford, The Journal of Physical Chemistry Letters, 2022, 13, 7911–7919.
15. P. R. Kaundinya, K. Choudhary and S. R. Kalidindi, JOM, 2022, 74, 1395–1405.
16. S. R. Kalidindi, A. J. Medford and D. L. McDowell, JOM, 2016, 68, 2126–2137.
17. F. Brockherde, L. Vogt, L. Li, M. E. Tuckerman, K. Burke and K.-R. Müller, Nature Communications, 2017, 8, 872.
18. T. Xie and J. C. Grossman, Physical Review Letters, 2018, 120, 145301.
19. K. Choudhary and B. DeCost, npj Computational Materials, 2021, 7, 1–8.
20. A. Merchant, S. Batzner, S. S. Schoenholz, M. Aykol, G. Cheon and E. D. Cubuk, Nature, 2023, 624, 80–85.
21. A. P. Bartók, R. Kondor and G. Csányi, Physical Review B, 2013, 87, 184115.
22. P. Lyngby, C. Larsen and K. W. Jacobsen, Physical Review Materials, 2024, 8, 123802–123802.
23. A. G. Kusne, H. Yu, C. Wu, H. Zhang, J. Hattrick-Simpers, I. Takeuchi, Nature Communications, 2020, 11, 5966.
24. X. Qian, B.-J. Yoon, R. Arróyave, X. Qian and E. R. Dougherty, Patterns, 2023, 4, 1–20.
25. T. Lookman, P. V. Balachandran, D. Xue and R. Yuan, npj Computational Materials, 2019, 5, 21.
26. P. Ray, A. P. Generale, N. Vankireddy, Y. Asoma, M. Nakauchi, H. Lee, K. Yoshida, Y. Okuno and S. R. Kalidindi, npj Computational Materials, 2025, 11, 234.
27. P. Ray, A. Yuichiro, N. Vankireddy, A. P. Generale, N. Masataka, L. Haein, Y. Katsuhisa, S. R. Kalidindi and O. Yoshishige, Assessing the accuracy of Bayesian-optimized CGMD in predicting polymer miscibility, 2025, https://chemrxiv.org/engage/chemrxiv/article-details/69263681a10c9f5ca1c0700b.
28. M. O. Buzzy, D. Montes de Oca Zapiain, A. P. Generale, S. R. Kalidindi and H. Lim, Acta Materialia, 2025, 284, 120537.
29. D. Khatamsaz, B. Vela, P. Singh, D. D. Johnson, D. Allaire and R. Arróyave, npj Computational Materials, 2023, 9, 49.
30. R. Nakayama, R. Shimizu, T. Haga, T. Kimura, Y. Ando, S. Kobayashi, N. Yasuo, M. Sekijima and T. Hitosugi, Science and Technology of Advanced Materials: Methods, 2022, 2, 119–128.
31. J. Startt, M. J. McCarthy, M. A. Wood, S. Donegan and R. Dingreville, npj Computational Materials, 2024, 10, 164.
32. Z. Hou and K. Tsuda, Machine Learning Meets Quantum Physics, Springer International Publishing, Cham, 2020, pp. 413–426.
33. P. I. Frazier, A Tutorial on Bayesian Optimization, 2018, https://arxiv.org/abs/1807.02811, Version Number: 1.
34. S. M. A. A. Alvi, J. Janssen, D. Khatamsaz, D. Perez, D. Allaire and R. Arróyave, Acta Materialia, 2025, 289, 120908.
35. T. Hastie, J. Friedman and R. Tibshirani, The Elements of Statistical Learning, Springer New York, New York, NY, 2001.
36. C. E. Rasmussen and C. K. I. Williams, Gaussian Processes for Machine Learning, The MIT Press, 2005.
37. C. G. E. Boender and J. Mockus, Mathematics of Computation, 1991, p. 878.
38. J. Mockus, Bayesian Approach to Global Optimization: Theory and Applications, Springer Netherlands, Dordrecht, 1989.
39. K. Hanaoka, iScience, 2021, 24, 1–19.
40. M. A. Seyed Mahmoud, D. Renner, A. Khosravani and S. R. Kalidindi, Acta Materialia, 2026, 306, 121902.
41. Y. Zhao, K. Yuan, Y. Liu, S.-Y. Louis, M. Hu and J. Hu, The Journal of Physical Chemistry C, 2020, 124, 17262–17273.
42. A. D. Casey, S. F. Son, I. Bilionis and B. C. Barnes, Journal of Chemical Information and Modeling, 2020, 60, 4457–4473.
43. M. C. Barry, Ph.D., Georgia Institute of Technology, United States – Georgia, 2023.
44. M. C. Barry, I. S. Winter, M. Chandross, J. R. Gissinger, S. R. Kalidindi and S. Kumar, npj Computational Materials, 2026.
45. M. C. Barry, K. E. Wise, S. R. Kalidindi and S. Kumar, The Journal of Physical Chemistry Letters, 2020, 11, 9093–9099.

Journal               [vol.] Name, [year], ,   | 1–12 11


Digital Discovery
1. M. C. Barry, J. R. Gissinger, M. Chandross, K. E. Wise, S. R. Kalidindi and S. Kumar, Computational Materials Science, 2023, 230, 112431.
2. M. C. Barry, S. Kumar and S. R. Kalidindi, Machine Learning in Molecular Sciences, Springer International Publishing, Cham, 2023, vol. 36, pp. 67–89.
3. S. R. Kalidindi, Hierarchical Materials Informatics, Elsevier, 2015.
4. P. R. Kaundinya, K. Choudhary and S. R. Kalidindi, Physical Review Materials, 2021, 5, 063802.
5. A. Cecen, H. Dai, Y. C. Yabansu, S. R. Kalidindi and L. Song, Acta Materialia, 2018, 146, 76–84.
6. A. Mann and S. R. Kalidindi, Frontiers in Materials, 2022, 9, 1–14.
7. A. Zunger, S.-H. Wei, L. G. Ferreira and J. E. Bernard, Physical Review Letters, 1990, 65, 353–356.
8. O. Certík, J. E. Pask and J. Vackár, Computer Physics Communications, 2013, 184, 1777–1791.
9. S. Bhowmik, J. E. Pask, A. J. Medford and P. Suryanarayana, Computer Physics Communications, 2025, 308, 109448.
10. A. van de Walle, M. Asta and G. Ceder, Calphad, 2002, 26, 539–553.
11. D. Gehringer, M. Friák and D. Holec, Computer Physics Communications, 2023, 286, 108664.
12. D. R. Hamann, Physical Review B, 2013, 88, 085117.
13. M. F. Shojaei, J. E. Pask, A. J. Medford and P. Suryanarayana, Computer Physics Communications, 2023, 283, 108594.
14. J. P. Perdew, K. Burke and M. Ernzerhof, Physical Review Letters, 1996, 77, 3865–3868.
15. B. Zhang, X. Jing, S. Kumar and P. Suryanarayana, SoftwareX, 2023, 21, 101295.
16. Q. Xu, A. Sharma and P. Suryanarayana, SoftwareX, 2020, 11, 100423.
17. B. Zhang, X. Jing, Q. Xu, S. Kumar, A. Sharma, L. Erlandson, S. J. Sahoo, E. Chow, A. J. Medford, J. E. Pask and P. Suryanarayana, Software Impacts, 2024, 20, 100649.
18. Q. Xu, A. Sharma, B. Comer, H. Huang, E. Chow, A. J. Medford, J. E. Pask and P. Suryanarayana, SoftwareX, 2021, 15, 100709.
19. F. Ren and F. Liu, The Journal of Chemical Physics, 2022, 157, 184106.
20. D. T. Fullwood, S. R. Kalidindi, S. R. Niezgoda, A. Fast and N. Hampson, Materials Science and Engineering: A, 2008, 494, 68–72.
21. T. Fast and S. R. Kalidindi, Acta Materialia, 2011, 59, 4595–4605.
22. S. R. Niezgoda, D. T. Fullwood and S. R. Kalidindi, Acta Materialia, 2008, 56, 5285–5292.
23. S. R. Niezgoda, Y. C. Yabansu and S. R. Kalidindi, Acta Materialia, 2011, 59, 6387–6400.
24. A. Máckiewicz and W. Ratajczak, Computers &#x26; Geosciences, 1993, 19, 303–342.
25. G. Kresse and J. Hafner, Physical Review B, 1993, 47, 558–561.
26. G. Kresse and J. Furthmüller, Computational Materials Science, 1996, 6, 15–50.
27. G. Kresse and J. Furthmüller, Physical Review B, 54, 1996, 11169–11186.
28. G. Kresse and D. Joubert, Physical Review B, 1999, 59, 1758–1775.
29. S. Maes, F. D. Ceuster, M. V. d. Sande and L. Decin, Journal of Open Source Software, 2025, 10, 7148.
30. C. E. Rasmussen and H. Nickisch, Journal of Machine Learning Research, 2010, 11, 3011–3015.
31. C. E. Rasmussen and C. K. I. Williams, Gaussian processes for machine learning, MIT Press, Cambridge, Mass, 2006.
32. D. P. Kingma and J. Ba, Adam: A Method for Stochastic Optimization, 2017, http://arxiv.org/abs/1412.6980, arXiv:1412.6980 [cs].
33. D. V. Lindley, The Annals of Mathematical Statistics, 1956, 27, 986–1005.
34. X. Huan and Y. M. Marzouk, Journal of Computational Physics, 2013, 232, 288–317.
35. S. Kumar, X. Jing, J. E. Pask, A. J. Medford and P. Suryanarayana, The Journal of Chemical Physics, 2023, 159, 244106.
36. L. R. Timmerman, S. Kumar, P. Suryanarayana and A. J. Medford, Journal of Chemical Theory and Computation, 2024, 20, 5788–5795.

Journal [vol.] Name, 12 | [year], , 1–12


Page 13 of 13 Digital Discovery

# Data Availability Statement

All data and scripts for feature engineering (computing pseudo electron densities &#x26; spatial correlations), model training, and post-processing (uncertainty analysis) are archived on Zenodo at https://doi.org/10.5281/zenodo.21339835. Alternatively, the codes are also available at https://github.com/pranoy-ray/AlloyDiscovery.

# Digital Discovery Accepted Manuscript


