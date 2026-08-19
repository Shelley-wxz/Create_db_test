# Digital Discovery

Accepted Manuscript

Published on 28 July 2026 Licensed under CC-BY-NC 4.0

![](images/70695af092a5ec5a6e7970d59c049842fd848ea4475a9fc8a35a76e80c9944d0.jpg)

Check for updates

## Digital Discovery

![](images/926236d278f9f25a6b967ffd126a2d10d5c6a902beef3dc1206d690fce697f7d.jpg)

![](images/e021a9cc2ae81254e763d984cfecb77bd0e814bd9a3eb02af385d8c5497cdfaa.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the Information for Authors.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal’s standard Terms & Conditions and the Ethical guidelines still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

# Journal Name

ARTICLE TYPE

Cite this: DOl: 00.0000/xxxxxxxxxx

# Electronic manifolds for extrapolative alloy discovery

Pranoy Ray<sup>a,b,c</sup>, Sayan Bhowmik<sup>d</sup>, Phanish Suryanarayana<sup>c,e</sup>, Surya R. Kalidindi<sup>b,c</sup> and Andrew J. Medford<sup>d†</sup>

Received Date

Accepted Date

DOI:00.0000/xxxxxxxxxx

This study presents a computationally eficient framework for accelerated alloy discovery that uses the non-interacting electron density to capture intrinsic structure-property relationships in refractory high-entropy alloys (HEAs). Unlike state-of-the-art approaches relying on expensive, self-consistent density functional theory calculations, our method employs the non-interacting electron density as the primary structural descriptor. By extracting physical features through directionally resolved twopoint spatial correlations and compressing them via Principal Component Analysis, we eficiently map the design space. Coupling these descriptors with Bayesian active learning, we achieve a normalized mean absolute error (NMAE) of <2% for the bulk modulus of Al-Nb-Ti-Zr alloys using only 10 training samples (<0.2% of the dataset). Furthermore, we demonstrate that the model learns an electronic packing manifold that is transferable within the refractory BCC alloy family. Validated on a distinct 7-component refractory system (Mo-Nb-Ta-Ti-V-W-Zr) containing four elements entirely absent from the training data, the framework enables intra-family transfer within the refractory BCC alloy class. An internal cross-composition ablation within D , training exclusively on Al+Nbdominant compositions and testing on a disjoint Ti+Zr-dominant subset, yields NMAE = 2.4% and R<sup>2</sup> = 0.8, further confirming cross-group descriptor transferability without requiring additional DFT calculations. Moreover, by augmenting the base model with just 20 samples from the target domain (<0.1% of the total dataset), we achieve high-fidelity predictions (NMAE < 3%) for 7-component alloys, reducing data acquisition costs by orders of magnitude compared to standard workflows. A controlled comparison confirms that composition-based descriptors under the identical pipeline do not reach the same accuracy threshold within the same sample budget, establishing that the spatial autocorrelation encoding of the non-interacting electron density provides information beyond elemental composition statistics alone.

## Introduction

High-entropy alloys (HEAs) <sup>1–3</sup> encompass a vast compositional design space that offers exceptional tunability for mechanical and thermal properties, yet this combinatorial magnitude renders exhaustive experimental exploration intractable. While Kohn-Sham density functional theory (DFT) <sup>4,5</sup> offers first-principles accuracy <sup>6–8</sup>, its large computational cost and $\mathcal { O } ( N ^ { 3 } )$ scaling with system size render exhaustive high-throughput screening <sup>9,10</sup> of HEA compositional spaces computationally prohibitive. Machine learning (ML) surrogates <sup>11–21</sup> address this by approximating property predictions at reduced cost. Recent efforts have further enhanced sample efficiency through Bayesian active learning <sup>22–34</sup> and Gaussian Process Regression (GPR) <sup>35–40</sup>, though their efficacy depends critically on the choice of structural descriptors.

Recent advances<sup>10,41–44</sup> in physics-based feature engineering have established the electron density field as a robust, chemically agnostic descriptor for atomic structures. These methods are powerful because the converged charge density encodes the quantum mechanical ground state, but this fidelity comes at substantial computational cost. State-of-the-art frameworks, such as the Voxelized Atomic Structure (VASt) method<sup>45–47</sup>, utilize the fully converged elecron density field to quantify structural features via two-point spatial correlations <sup>10,13,48–51</sup>. While these descriptors achieve high fidelity, they create a fundamental inefficiency: the calculation of the electronic ground state via self-consistent field (SCF) iteration, the dominant computational cost in static DFT, must be completed for every candidate structure merely to generate input features for the surrogate model. This limits the primary value proposition of machine learning surrogates, as the computational budget required for feature generation becomes comparable to that of directly computing the target property.

To address this bottleneck, we investigate the efficacy of the non-interacting valence electron density, hereafter referred to as pseudo-density. In practice, the pseudo-density represents the superposition of isolated valence electron densities corresponding to atoms placed at the Special Quasirandom<sup>52</sup> (SQS) lattice sites, determined via Vegard’s Law to bypass equilibrium geometry optimization, with no subsequent electronic relaxation. By eliminating the iterative SCF cycle, the presented approach reduces the computational cost of feature generation by orders of magnitude compared to fully converged $\mathrm { D F T } ^ { 4 6 }$ , while preserving essential chemical and valence electron information. Our approach rests on the premise that in HEAs, property variance is driven by chemical composition wherein superimposed valence densities could act as an effective descriptor. Consequently, the pseudo-density should retain sufficient physical fidelity for predictive modeling; a hypothesis supported by recent work<sup>14</sup>. Furthermore, because these descriptors are derived via unsupervised learning, solely from atomic configuration and elemental identity independent of any target property, they form a property-agnostic representation capable of predicting disparate physical quantities, $\boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . ,$ mechanical and thermodynamic properties, without feature re-engineering. Crucially, we posit that this physics-based encoding offers a route to transferability: because pseudo-electron densities capture the spatial packing and overlap of valence electrons, they may encode a transferable electronic manifold within structurally and chemically constrained alloy families. This would enable a model trained on a lower-order system, e.g., 4-component, to achieve predictive transfer to higher-order systems, e.g., 7- component, within the same alloy class with minimal additional data.

In this work, we present a framework integrating pseudodensity descriptors: quantified via two-point spatial correlations and PCA, with Gaussian Process Regression (GPR) driven Bayesian active learning. We validate the approach on the Al-Nb-Ti-Zr system $\left( \mathcal { D } _ { 4 } \right)$ , achieving $R ^ { 2 } > 0 . 9 7$ for both bulk modulus and alloy formation energy. Notably, the bulk modulus model attains a normalized mean absolute percentage error (NMAE) of $< 2 \%$ using only 10 training samples, surpassing benchmarks utilizing converged densities. We further demonstrate extrapolative power by applying the ${ \mathcal { D } } _ { 4 }$ -trained model to a distinct 7-component system (D : Mo-Nb-Ta-Ti-V-W-Zr). The framework enables zero-shot transfer within the refractory BCC alloy class, and with the augmentation of just 20 actively selected D<sub>7</sub> samples, recovers highfidelity predictions (NMAE < 3%), establishing pseudo-density as a practical descriptor for sample-efficient refractory alloy discovery.

## Data Curation and Design Space

This study investigates the quaternary Al-Nb-Ti-Zr refractory HEA system, spanning a large compositional space defined by:

$$
\mathcal {D} _ {4} = \left\{\mathrm{Al} _ {\alpha} \mathrm{Nb} _ {\beta} \mathrm{Ti} _ {\gamma} \mathrm{Zr} _ {\delta} | \alpha , \beta , \gamma , \delta \in \{0, 4, \dots , 1 2 8 \}, \right.
$$

$$
\left. \alpha + \beta + \gamma + \delta = 1 2 8 \right\}.\tag{1}
$$

This discrete set yields a total of $^ { 6 , }$ ,545 unique structures when including elemental, binary, ternary, and quaternary compositions, and 4,495 alloys when restricted to the quaternary space. To validate the extrapolative transferability of the model, we leverage the distinct 7-component domain (D<sub>7</sub>) which contains 12012 unique compositions, defined by the set:

$$
\begin{array}{r l} \mathcal {D} _ {7} = & \left\{\mathrm{Mo} _ {\alpha} \mathrm{Nb} _ {\beta} \mathrm{Ta} _ {\gamma} \mathrm{Ti} _ {\delta} \mathrm{V} _ {\varepsilon} \mathrm{W} _ {\zeta} \mathrm{Zr} _ {\eta} \mid \right. \\ & \alpha , \ldots , \eta \in \{0, 1 5, 2 3, 3 0, 3 8, \ldots , 1 0 5, 1 2 8 \}, \\ & \alpha + \beta + \gamma + \delta + \varepsilon + \zeta + \eta = 1 2 8 \}. \end{array}\tag{2}
$$

The ground truth values for bulk modulus and alloy formation energy were obtained from the converged DFT dataset established by Barry et al. <sup>44,46</sup>. Note that the alloy formation energies were available only for ${ \mathcal { D } } _ { 4 }$

## Background

## Pseudo-Density

In this framework, the material structure is defined by the pseudodensity field, $\rho _ { \mathrm { p s e u d o } } : \Omega \to \mathbb { R } _ { \ge 0 } .$ , where $\Omega \subset \mathbb { R } ^ { 3 }$ represents the spatial domain of the atomic system. This framework’s key innovation is bypassing the computationally expensive SCF cycle. While converged densities require iterative Hamiltonian diagonalization, pseudo-densities are constructed via a single-shot superposition of isolated atom electron densities<sup>53,54</sup>, where each element contributes its valence electron density according to its specific spatial distribution. This effectively decouples feature generation from the computationally expensive electronic relaxation process.

We modeled the random solid solution behavior of refractory HEAs through Special Quasirandom Structures $( \mathsf { S Q S } ) ^ { 5 2 }$ generated via the Alloy Theoretic Automated Toolkit $( \mathsf { A T A T } ) ^ { 5 5 }$ using sqsgenerator <sup>56</sup>. All SQS structures were generated with the same set of lattice parameters. For each structure, the pseudo-density was computed using valence electron densities in the Optimized Norm-Conserving Vanderbilt $( \mathrm { O N C V } ) ^ { 5 7 }$ pseudopotential files from the SPMS $\sec ^ { 5 8 }$ . We employed the PBE exchange-correlation functional inherent to these pseudopotentials. While higher-level functionals (e.g., SCAN or Hybrids) of fer improved energetic accuracy for ground-state calculations, the non-interacting pseudo-density relies primarily on the spatial topology of valence orbitals rather than absolute energy minimization. The Generalized Gradient Approximation $( \mathsf { G G A } ) ^ { 5 9 }$ sufficiently captures the characteristic atomic radii and overlap features required for this topological mapping, while maintaining consistency with standard high-throughput screening li braries. The pseudo-density was mapped onto a 3D real-space grid closely mimicking the implementation in the M-SPARC<sup>60,61</sup> and SPARC <sup>62,63</sup> electronic structure codes. Critically, the generation of $\rho _ { \mathrm { p s e u d o } }$ bypasses the iterative SCF procedure <sup>64</sup>, hence the computational cost is significantly reduced compared to fully converged DFT calculations, thereby facilitating high-throughput screening of complex composition spaces.

## Feature Engineering using Spatial Correlations

To quantify the salient structural features governing the material response, we employ directionally resolved two-point spatial correlations <sup>48,65</sup>. This measure captures spatial positioning of charge density features, creating a translationally invariant descriptor. For computational efficiency, the discrete two-point autocorrelations, $f _ { r } ,$ are calculated using Fast Fourier Transforms (FFT) <sup>66–68</sup> on a discretized grid:

$$
f _ {r} = \frac {1}{| S |} \mathscr {F} ^ {- 1} \left[ \mathscr {F} \left(\sqrt {\rho_ {\text { pseudo }}}\right) * \mathscr {F} \left(\sqrt {\rho_ {\text { pseudo }}}\right) \right],\tag{3}
$$

where $\mathcal { F }$ denotes the discrete Fourier transform operation, the asterisk (∗) indicates the autocorrelation operation, and S represents the set of voxel indices. The spatial domain for $\rho _ { p s e u d o }$ was discretized with a fixed voxel size of $\lambda = 0 . 2 \mathring \mathrm { A } ,$ as done in previous work <sup>46</sup> utilizing converged electron charge densitites. This approach enables efficient computation of spatial correlations for high-throughput screening.

The resulting high-dimensional autocorrelation vectors are projected onto a low-dimensional feature space using Principal Component Analysis $\mathrm { ( P C A ) } ^ { 6 9 }$ . This projection compresses the feature space while preserving the variance that distinguishes different atomic configurations.

Because $\rho _ { \mathrm { p s e u d o } }$ requires no iterative Hamiltonian diagonalization (and takes ${ \sim } 3 0$ seconds per sample), its generation scales as $\mathcal { O } ( N _ { \mathrm { g r i d } } )$ per structure, a single-pass operation, compared to $\mathcal { O } ( N _ { \mathrm { S C F } } \times N _ { \mathrm { b a s i s } } ^ { 3 } )$ for a converged DFT charge density, yielding a reduction in descriptor generation cost of approximately two orders of magnitude for the 128-atom BCC SQS supercells used in this work<sup>46</sup>.

## Dimensionality Reduction using PCA

We apply PCA to the autocorrelation feature vectors to obtain a compact, low-dimensional representation. The PCA transformation matrix is estimated jointly from the combined $\mathcal { D } _ { 4 } + \mathcal { D } _ { 7 }$ feature space, ensuring that both datasets are projected onto a common basis. We note that this means the PC-space overlap between ${ \mathcal { D } } _ { 4 }$ and $\mathcal { D } _ { 7 }$ (Supplementary Figure ??) reflects partly the shared basis; the physical interpretation that the pseudo-density feature scales of the two alloy families are compatible, is confirmed independently by Supplementary Figure $^ { ? ? , }$ which shows that the trapezoidal ${ \mathcal { D } } _ { 4 }$ simplex topology is fully preserved under a PCA estimated from ${ \mathcal { D } } _ { 4 }$ alone. In the combined feature space, the first three principal components capture approximately 50% of the total variance, with the first component accounting for approximately 36%. The PCA basis vectors systematically decompose the structural hierarchy: the first principal component captures the mean charge density, while subsequent components resolve the complex spatial patterns associated with local atomic disorder.

The low-dimensional representation maintains the physical hierarchy of the alloy system. As illustrated in Figure 1 for ${ \mathcal { D } } _ { 4 } .$ , the data points naturally arrange into a trapezoidal geometry where pure elements occupy the vertices and all alloy compositions fill the interior volume. This smooth variation of principal component scores across the composition space facilitates robust interpolation and accurate property prediction for unexplored alloy stoichiometries. Because this dimensionality reduction is unsupervised, the resulting descriptors are property-agnostic and can be reused to train independent models for different target properties, e.g., mechanical or thermodynamic, without re-computation. Notably, this unsupervised PC projection remains fixed regardless of the target property, allowing the same structural map to be colored by distinct physical responses, e.g., bulk modulus or alloy formation energy: see Figure 1 to reveal property-specific manifolds. Based on the variance and loading-vector analysis, we truncate the descriptor space to the first three principal components \* for all subsequent regression modeling. The scree plot shows a pronounced elbow after PC3, with PC1 capturing ∼36% of variance and PCs 2-3 capturing ∼2.5% and ∼2% respectively, followed by a near-flat decay through PC4–50 (each <0.5%). Inspection of the PC loading vectors (center slices of the 3D auto correlation basis) confirms that PC1–3 display spatially coherent, periodic patterns reflecting the BCC lattice structure, elemental density contrast, and compositional disorder respectively. PC4 and above exhibit progressively higher spatial-frequency content with no discernible periodic structure, indicating that they encode stochastic noise in the autocorrelation representation rather than chemically interpretable structural features. These three components therefore capture the full chemically relevant structural hi erarchy, and their empirical sufficiency is further evidenced by $R ^ { 2 } \ge 0 . 9 8$ achieved in-domain.

## Impact of Structural Relaxation on Manifold Topology

A critical and counter-intuitive finding of this work is that structural descriptors derived from initial SQS configurations with a uniform, common lattice constant yield a more cohesive feature space than those derived from fully relaxed geometries. Figure 1 visualizes the Principal Component space for the initial uniform SQS structures compared to those relaxed via $\mathrm { V A S P } ^ { 7 0 }$ –73 and $\mathrm { M A C E } ^ { 7 4 }$ (see plots $\qquad \mathrm { { c , d , } }$ e and f in Supplementary Figure ??). Here, relaxation refers to the full optimization of both internal ionic coordinates and cell volume. The uniform SQS data forms a continuous, cohesive simplex, where the variance is driven purely by the combinatorial arrangement of chemical species. In contrast, the relaxed structures fracture into a distinct, disjoint, hyper-branched topology.

This fracturing is fundamentally driven by the loss of volumet ric uniformity during relaxation. In the uniform initial state, a globally constant spatial metric is enforced for the two-point spatial statistics across all samples. During relaxation, individual lattice parameters deviate significantly from this uniform baseline, rendering the spatial metric sample-dependent. As the concentration of larger atoms like Zr increases (Zr’s ionic radius is approximately 10% larger than that of Al, Nb, and Ti), the lattice undergoes significant global cell expansion to minimize steric hindrance.

![](images/a465ee282c14c22c1ab7866f7961784a67778b89b043a31b4c856b3723d94cb2.jpg)

![](images/ab09e11c3704bebf5cbabb7d7863c6b32a40585c6abbd1447120efb023d65976.jpg)  
Fig. 1 Principal component visualization of the ${ \mathcal { D } } _ { 4 }$ composition space. (top) PC1 vs PC2 colored by alloy formation energy; (bottom) PC2 vs PC3 colored by bulk modulus. Pure elements reside at the vertices of the trapezoidal simplex; alloy compositions fill the interior. Properties vary smoothly and monotonically across the manifold, confirming that the pseudo-density spatial autocorrelations preserve the chemical and structural hierarchy of the composition space. Al occupies a spatially distinct vertex attributable to its s-p valence character, while the d-metal vertices (Ti, Nb, Zr) cluster more closely, consistent with their shared group 4-5 d-electron profiles.

This phenomenon can be rigorously understood by considering the variance maximization objective of PCA acting on absolute spatial coordinates. Because the $f _ { r }$ are computed on an absolute real-space grid, global cell expansion physically dilates the interatomic distances between charge density peaks. Consequently, the variance is dominated by different lattice constants scaling the spatial metric, rather than strictly chemical variations. PCA aggressively captures this spatial dilation, fracturing the manifold into discrete arms. When the relaxed PC space is colored by the final relaxed lattice parameter, the distinct branches stratify per fectly by cell volume, with the arms corresponding to discrete lattice parameter bands (see Figure ??) scaling from approximately 12.8 Å to 14.2 Å. The terminal tips of these disjoint manifolds correspond exactly to the absolute structural limits of the dataset, specifically the highly expanded Zr-rich compositions.

To rigorously validate that this non-uniform volumetric scaling is the primary driver of the fracturing, we performed an ablation test where the absolute-grid $f _ { r }$ were divided by the cell volume $( a ^ { 3 } )$ before performing PCA (see Figure ??). This operation effectively normalizes the magnitude-dependent variance driven by the cell expansion. Suppressing this volume-dependent information caused the previously disjoint branches to coalesce back into a single, continuous cluster. This mathematically confirms that the geometric relaxation, specifically the variance in the final relaxed lattice constants, is responsible for the manifold fracturing.

It is worth noting that if the $f _ { r }$ were computed on a normalized grid using relative fractional coordinates $\left( x / a \right)$ , the affine volume expansion would be factored out, isolating the variance purely to local ionic displacements. However, by using the initial system’s pseudo-density with a uniform lattice constant on an absolute grid, we inherently bypass both the volumetric and ionic strain artifacts. By enforcing this globally constant spatial metric, we effectively treat the ideal lattice as a canonical reference state. It is important to acknowledge the trade-off explicitly: the smoother manifold topology observed for unrelaxed structures arises in part because physically meaningful variability-latticemismatch strain, local ionic distortion, and site-specific bonding has been suppressed. For macroscopic, composition-averaged properties of ideal solid solutions, where bulk modulus and formation enthalpy are primarily determined by elemental identity and proportion rather than by individual SQS configurations, this suppression is a defensible approximation. The framework is not designed to capture configuration-sensitive properties, and performance on such quantities has not been tested. This enables the Gaussian Process<sup>36</sup> to interpolate across a smooth manifold $( f ( \mathrm { c h e m i s t r y } ) \to P _ { \mathrm { p r o p e r t y } } )$ without the interference of highvariance geometric noise introduced by relaxation.

## Physical basis for descriptor efficacy and transferability

Several physically grounded arguments underpin the efficacy of the pseudo-density for the properties and alloy class studied here. First, for macroscopic, composition-averaged properties of ideal disordered BCC solid solutions, such as bulk modulus and formation enthalpy, the dominant source of inter-composition vari ance is elemental identity and proportion rather than individual atomic configurations. In this regime, a descriptor that faithfully encodes the spatial envelope of valence electron overlap captures the primary variance driver without requiring full self-consistency. Second, the omission of electron-electron interactions and SCF relaxation is acceptable for these specific properties because electronic screening in metallic solid solutions constitutes a subordinate perturbation on the zeroth-order charge topology set by the pseudo-density; the self-consistent correction is a compositioninvariant shift that does not alter the relative ordering of compositions across the manifold. This is consistent with the empirical observation that the unrelaxed pseudo-density manifold is smoother and more predictive than that of relaxed structures. Third, intrafamily transferability from ${ \mathcal { D } } _ { 4 }$ to D is physically enabled by the similarity of d-electron radial density profiles across the group 4–6 refractory metals (Ti, Zr, Nb, Mo, Ta, V, W): these elements share the same angular momentum quantum number and comparable effective nuclear charges, so their pseudopotential-derived valence densities are similar in spatial extent and nodal structure. Consequently, the autocorrelation features of Mo, $\mathrm { T a } , \mathrm { V } ,$ and W fall in a region of feature space continuously connected to those of Nb, Ti, and $\operatorname { Z r } ,$ enabling regression rather than requiring interpolation between disjoint clusters. Fourth, Al is an s-p metal whose diffuse, nearly-spherical valence density produces a qualitatively distinct autocorrelation signature, placing it at a spatially separated vertex of the ${ \mathcal { D } } _ { 4 }$ simplex (visible in Figure 1). Because Al is absent from $\mathcal { D } _ { 7 }$ , all D compositions lie in the d-metal-dominated region of the joint manifold, away from the Al vertex. The zeroshot and few-shot predictions for $\mathcal { D } _ { 7 }$ therefore extrapolate within a chemically coherent subspace and do not require the model to generalize through the Al-anchored region of the descriptor space. It must be emphasized that this framework is explicitly designed for composition-averaged properties of single-phase disordered BCC solid solutions and is not expected to capture properties governed by local chemical order, short-range order, segregation, magnetic ordering, defects, or finite-temperature configurational sampling.

## Model Building

## Gaussian Process Regression

We employ Gaussian Process Regression (GPR)<sup>75</sup> to model the mapping between the low-dimensional structural features (PC scores) and the material properties. GPR provides a nonparametric, probabilistic framework that yields both a predictive mean and a variance, which is essential for uncertainty quantification. The covariance between inputs is computed using an Automatic Relevance Determination Squared Exponential (ARDSE)<sup>76</sup> kernel:

$$
k (\mathbf {x}, \mathbf {x} ^ {\prime}) = \sigma_ {s} ^ {2} \exp \left[ - \frac {1}{2} \sum_ {d = 1} ^ {D} \frac {(x _ {d} - x _ {d} ^ {\prime}) ^ {2}}{l _ {d} ^ {2}} \right] + \sigma_ {n} ^ {2} \delta_ {\mathbf {x x} ^ {\prime}}\tag{4}
$$

![](images/08d0526bff6c994fdfacd8a29d5ea1820190f566fac3cb46a5765ffd9c82f65c.jpg)  
Fig. 2 Controlled comparison of bulk modulus prediction error (NMAE) as a function of training set size on ${ \mathcal { D } } _ { 4 }$ , for three descriptor classes under the identical GPR and active-learning pipeline: pseudo-density spatial autocorrelations $( \rho _ { \mathsf { p s e u d o } } ,$ , active and random), composition-based (MAG-PIE) features projected onto their leading three principal components prior to GPR (active and random), matching the descriptor dimensionality of $\rho _ { \mathsf { p s e u d o } }$ exactly and giving both ARDSE kernels the same number of length-scale hyperparameters to estimate, and a single reference datum for the converged charge-density descriptor $( \rho _ { \mathsf { c o n v e r g e d } } ,$ , active, at ∼26 samples<sup>46</sup>). The 3-PC MAGPIE projection captures 60% of total MAG-PIE variance. The pseudo-density active strategy reaches NMAE <2% at 10 samples. The matched-dimensionality composition-based descriptor does not reach the 2% threshold within the 30-sample window evaluated here, confirming that the pseudo-density’s advantage is a property of its physical information content rather than a consequence of operating in a lower-dimensional space, and that the spatial autocorrelation encoding of the valence electron density provides structural information beyond elemental composition statistics alone.

where $\sigma _ { s } ^ { 2 }$ scales the output variance, $l _ { d }$ represents the characteristic length-scale for feature dimension $d ,$ and $\sigma _ { n } ^ { 2 }$ accounts for observation noise. The ARDSE kernel allows the model to inherently determine the relevance of each principal component, weighting them according to their influence on the target property. This choice reflects the expectation that different principal components encode distinct physical scales, e.g., mean density versus local disorder, and allows the GP to adapt its sensitivity accordingly. All hyperparameters are optimised by maximising the log marginal likelihood using the Adam<sup>77</sup> optimiser for 200 epochs at a learning rate of 0.1.

## Bayesian Experiment Design

To minimize the computational expense of data generation, we utilize a Bayesian active learning strategy driven by a relativeuncertainty acquisition function inspired by information-based design<sup>78,79</sup>. Specifically, the acquisition selects candidate structures that maximize the ratio of predictive uncertainty to the predicted magnitude:

$$
I (\mathbf {x}) = \left| \frac {\sigma (\mathbf {x})}{\mu (\mathbf {x})} \right|\tag{5}
$$

where $\mu ( \mathbf { x } )$ and $\sigma ( \mathbf { x } )$ are the predictive mean and standard deviation provided by the GPR model, respectively. In each iteration, the algorithm identifies the k structure with the highest I(x) for ground-truth evaluation. In a prospective discovery campaign, this step would selectively trigger DFT calculations for these spe cific unlabelled candidates, thereby augmenting the training set with high-fidelity data only where strictly necessary. While active learning strategies have been successfully applied to descriptors derived from converged densities <sup>46</sup>, such workflows inherently face a "pre-computation" bottleneck: the computationally expensive SCF cycle must be completed for every candidate structure merely to generate the input features for the surrogate model. In contrast, our pseudo-density framework eliminates this redundancy, enabling the rapid, low-cost scanning of the entire candi date pool prior to triggering any expensive DFT calculations. This iterative process (see Figure 3) empirically leads to rapid convergence by prioritizing sampling in regions in the design space where the predictive confidence is lowest.

![](images/96f18fe85acd64b5b1d524e365d93dafff37d2c7381b2737540837bbf1ccc3bc.jpg)  
Fig. 3 End-to-end Bayesian active learning workflow for ${ \mathcal { D } } _ { 4 } .$ Starting from HEA Special Quasirandom Structures (SQS), the pseudo-density $\rho _ { \mathsf { p s e u d o } }$ is constructed via single-pass superposition of isolated valence densities, bypassing the SCF cycle. Two-point spatial autocorrelations $f _ { r }$ are computed via FFT and compressed to three principal components. The GPR model is iteratively updated by querying ground-truth DFT labels only at the highestuncertainty candidates identified by the acquisition function $I ( \mathbf { x } ) = | \sigma ( \mathbf { x } ) / \mu ( \mathbf { x } ) |$ |, minimizing the number of expensive DFT calculations required.

## Extrapolative Validation Protocol

To rigorously assess the transferability of the pseudo-density descriptors, we designed a disjoint training-testing protocol. The GPR model was actively trained exclusively on samples from the lower-order domain $\mathcal { D } _ { 4 } \ \left( \mathrm { A l - N b - T i - Z r } \right)$ . This model was then frozen and tasked with predicting the properties of the full extrapolation domain $\mathcal { D } _ { 7 }$ (Mo-Nb-Ta-Ti-V-W-Zr) without any re-training or exposure to the new chemical elements. This zero-shot transfer protocol evaluates whether the learned regression mapping $f : \mathbf { P C } \to K$ generalizes across chemically distinct refractory systems without re-training, fine-tuning, or element-specific feature engineering. Both ${ \mathcal { D } } _ { 4 }$ and $\mathcal { D } _ { 7 }$ share the BCC crystal structure and consist exclusively of group 4 to 6 transition metals; the transfer demonstrated here is therefore intra-family transfer within the refractory BCC alloy class, not unconditional extrapolation to arbitrary chemistries. To further substantiate transferability using only existing data, we performed an internal cross-composition ablation entirely within ${ \mathcal { D } } _ { 4 }$ . The GPR model was trained exclusively on compositions in which the combined Al+Nb mole fraction exceeds 0.5 (group 13 and group 5 elements) and evaluated on a disjoint test set of compositions in which the combined $\mathrm { T i } + \mathrm { Z r }$ mole fraction exceeds 0.5 (group 4 elements). These subsets share no direct compositional overlap and represent elements from distinct periodic-table groups. Using Bayesian active learning on the Al+Nb training pool, the model achieves NMAE = 2.39% and $R ^ { 2 } = 0 . 8 0 8$ on the Ti+Zr test set at 30 training samples, stabilising around NMAE ≈ 1.6–1.7% and $R ^ { 2 } \approx 0 . 8 9$ from 20 samples onward (Supplementary Figure ??), demonstrating that the pseudo-density descriptor encodes transferable valenceoverlap structure across compositionally and chemically distinct subregions of the same alloy family.

## Error metrics

Across all experiments, model performance is quantified using the mean absolute error (MAE), normalized MAE (NMAE), mean absolute percentage error (MAPE), and coefficient of determination $( R ^ { 2 } )$ . For a set of N predictions {yˆ<sub>i</sub>} and corresponding ground truth values $\{ y _ { i } \}$ , these are defined as

$$
\mathrm{MAE} = \frac {1}{N} \sum_ {i = 1} ^ {N} | \hat {y} _ {i} - y _ {i} |,\tag{6}
$$

$$
\mathrm{NMAE} = \frac {\mathrm{MAE}}{\bar {y}} \times 100 \%,\tag{7}
$$

where y¯ is the mean of the ground-truth values $\{ y _ { i } \}$

## Results and Discussion

## Performance on Bulk Modulus predictions

The GPR model demonstrates high predictive accuracy for the bulk modulus across the complete compositional dataset $\left( \mathcal { D } _ { 4 } \right)$ The active learning campaign selects labels from a pre-existing DFT candidate pool over a fixed compositional $\mathrm { g r i d } ^ { 4 6 }$ , initialized with a minimal seed of 4 randomly selected samples, followed by iterative acquisition. As shown in Figure $^ { 2 , }$ the model stabilizes rapidly, achieving an NMAE of <2% with only 10 total training samples (4 seed + 6 active). This efficiency highlights a significant advantage over competing descriptor frameworks. While state-of-the-art methods typically require significantly larger datasets $( 1 0 ^ { 2 } – 1 0 ^ { 3 }$ samples) or approximately 26 samples for converged charge density descriptors <sup>46</sup> to reach convergence, our approach achieves this fidelity with fewer samples and orders of magnitude lower computational cost for feature generation.

The robustness of the pseudo-density descriptor is further evi denced by the performance of random sampling. As summarized in Table 1, even the random selection strategy yields high accuracy $( R ^ { 2 } = 0 . 9 8 , \mathrm { M A E } = 1 . 4 1 \mathrm { \ G P a } )$ on the full dataset $( \mathcal { D } _ { 4 } )$ . This indicates that the unrelaxed pseudo-density manifold is naturally well-correlated with the mechanical response, such that complex active learning acquisition functions are not strictly required to achieve good global accuracy; though they still offer superior efficiency in the low-data limit (Figure 2). The parity plot in Figure 4(a) confirms this strong linear correlation $( R ^ { 2 } = 0 . 9 8 )$ across the full range of 80 GPa to 160 GPa, confirming that the superposition of non-interacting electron densities contains sufficient physical information to resolve variations in mechanical stiffness without systematic bias. Uncertainty calibration on the held-out ${ \mathcal { D } } _ { 4 }$ bulk modulus predictions yields coverage of 65.1% within $\pm 1 \sigma$ and 92.3% within $\pm 2 \sigma _ { \mathrm { { \scriptscriptstyle i } } }$ , consistent with a well-calibrated probabilistic model near theoretical Gaussian expectations (68%, 95%).

![](images/d65824e862579da2fbcd33a127d91af1eb7b1a6a120ce86f54f90266edc9226c.jpg)

![](images/bb3073b29aa8fd7e1641d68dd156fe9b08b4fb940743a717929b9db81a406c8b.jpg)  
Fig. 4 Parity plots of predicted versus DFT-computed properties for all held-out samples in ${ \mathcal { D } } _ { 4 } ,$ , with GPR predictive uncertainty shown as error bars (±1σ). (a) Bulk modulus predictions using a model trained on 10 actively selected samples $\left( R ^ { 2 } = 0 . 9 8 , \mathsf { N M A E } = 1 . 5 5 \% \right)$ . (b) Alloy formation energy predictions using a distinct GPR model trained on 18 actively selected samples $\textstyle ( R ^ { 2 } = 0 . 9 9 ,$ $\mathsf { N M A E } = 2 . 2 0 \% )$ , with uncertainty coverage of 88.8% within ±1σ and 99.8% within ±2σ.

![](images/cf813f9e33f6b60dafb0dc05bc7ef5875603bf50c44ec746f3ea666ec85e72c4.jpg)

![](images/bcf9198f131d493e56821f5a163394b0c80c062dceed1d15e0cc5a49bd322e07.jpg)  
Fig. 5 Extrapolative performance of the D -trained model on the full D bulk modulus dataset (12,012 compositions), following few-shot augmentation with 20 actively selected $\mathcal { D } _ { 7 }$ samples. (a) Parity plot with GPR predictive uncertainty shown as error bars (±1σ). (b) Distribution of predicted standard deviations σ across all $\mathcal { D } _ { 7 }$ test compositions. Coverage of 43.2% within ±1σ and 78.8% within ±2σ indicates moderate overconfidence in the extrapolative regime, consistent with $\mathsf { G P }$ posterior uncertainty being prior-dominated outside the training chemical space.

Table 1 Compiled error metrics for bulk modulus and alloy formation energy predictions for all ${ \mathcal { D } } _ { 4 }$ compositions (6,545 structures).

<table><tr><td>Material Property</td><td>Strategy</td><td>MAE</td><td>NMAE (%)</td><td> $R^{2}$ </td></tr><tr><td rowspan="2">Bulk Modulus (GPa)</td><td>Active</td><td>1.50</td><td>1.55</td><td>0.98</td></tr><tr><td>Random</td><td>1.41</td><td>1.46</td><td>0.98</td></tr><tr><td rowspan="2">Alloy Formation Energy (eV)</td><td>Active</td><td>1.19</td><td>2.20</td><td>0.99</td></tr><tr><td>Random</td><td>1.23</td><td>2.33</td><td>0.97</td></tr></table>

## Performance on Alloy Formation Energy predictions

Crucially, this physics-based feature set exhibits high transferability across properties. The same 3-PC pseudo-density features accurately predict both mechanical stiffness (bulk modulus) and thermodynamic stability (alloy formation energy) without modification. Starting with the same initial seed size of 4 samples, the active selection strategy applied to the full compositional space of ${ \mathcal { D } } _ { 4 }$ (Table 1), achieves an MAE of 1.19 eV (2.20% NMAE) with an $R ^ { 2 }$ of 0.99.

The parity plot in Figure 4(b) confirms this strong correlation using only 18 actively selected training samples. This result indicates that the pseudo electron density spatial correlations effectively capture the local chemical environment variations that dictate the energetic stability of the solid solution. The uncertainty coverage for $\Delta E _ { \mathrm { f o r m } }$ is similarly robust, achieving 88.8% within ±1σ and 99.8% within ±2σ.

## Comparative Performance and Scientific Implications

Table 1 summarizes the compiled error metrics, confirming that the pseudo-density descriptor yields high fidelity $( R ^ { 2 } \ge 0 . 9 8 )$ with both active and random sampling. While both strategies converge to similar accuracy in the limit, Figure 2 demonstrates that the active learning strategy provides a superior sample efficiency advantage in the low-data regime. The central finding of this study is the demonstration that pseudo electron densities are a sufficient structural descriptor for high-fidelity property prediction in complex alloy systems. PCA projections of the pseudo electron densities naturally recover the trapezoidal geometry of the 4-element structure space (Figure 1), placing elements at the vertices and alloys in the interior. This confirms that atomic packing and chemical identity; both captured by the pseudo-density, dominate the structural hierarchy of HEAs. Electronic relaxation acts predominantly as a local perturbation relative to these primary chemical variations, though the geometric variance introduced by ionic relaxation is sufficient to fracture the low-dimensional manifold if not accounted for (as confirmed by both PCA and Partial Least Squares analyses). This indicates that for these HEA solid solutions, the electronic environment is dominated by the initial, superposition of atomic charges, and the subsequent self-consistent electronic relaxation introduces differences that are subordinate to the chemical variations across the de sign space. By replacing the converged density with the pseudo density, the framework effectively decouples the feature generation step from the most computationally demanding part of the DFT calculation. This combination of eliminating the SCF bottleneck for feature generation and reducing the required number of training samples substantially enhances the feasibility of highthroughput computational materials discovery for HEAs. This efficiency gain does not merely accelerate existing workflows; it unlocks regimes previously inaccessible to DFT-based screening. As demonstrated by the extrapolation results, the pseudo-density descriptor creates a transferable feature space that bridges distinct chemical systems. By projecting the 4-component and $7 -$ component datasets into the same Principal Component space (as discussed in the Methods), we observe that they occupy overlapping manifolds. This indicates that the model predominantly learns electronic packing rules rather than overfitting to elementspecific labels, enabling more rapid exploration of combinatorial spaces (including 5+ component systems) without the need to retrain on every new element. The pseudo-density’s advantage over composition-based representations stems from three physically distinct information channels that elemental fractions alone cannot encode: (i) the spatial distribution of valence charge, captured via the two-point autocorrelation $f _ { r } ,$ which distinguishes arrangements that are compositionally identical but structurally distinct; (ii) the configurational disorder of the SQS lattice, whose specific atomic arrangement modulates the local overlap topology of the superimposed densities beyond what is recoverable from mean elemental proportions; and (iii) electronic character encoded in the pseudopotential-derived valence densities, which carry element-specific radial and angular orbital information beyond atomic number or mass. To isolate the contribution of the descriptor itself, Figure 2 presents a controlled substitution experiment in which composition-based (MAGPIE) features, projected onto their leading three principal components to match the dimensionality of $\rho _ { \mathrm { p s e u d o } }$ and equalize the number of ARDSE length-scale hyperparameters, are used as the descriptor within the identical GPR framework and active-learning pipeline. Under this substitution, the matched-dimensionality composition-based descriptor does not reach the 2% NMAE threshold within 30 training samples, whereas the pseudo-density active strategy crosses this threshold at 10 samples (converged charge-density descrip-$\mathrm { t o r s } ^ { 4 6 }$ reach comparable accuracy $\tt a t \sim 2 6$ samples but at ordersof-magnitude greater computational cost per feature evaluation, as discussed in the Pseudo-Density subsection). This controlled comparison, with all modeling choices and descriptor dimensionality held fixed, confirms that the spatial autocorrelation encoding of the pseudo-density provides information beyond elemental composition statistics. Furthermore, composition-based representations are defined over a fixed elemental vocabulary and have no principled mechanism for generalizing to elements absent from training, which is the defining limitation for $\mathcal { D } _ { 4 } \to \mathcal { D } _ { 7 }$ transfer. The capability to achieve high accuracy for both bulk modulus and formation energy with minimal training data using a low-cost descriptor represents a critical step towards realizing true high-throughput screening of the vast compositional space.

## Generalization to Higher-Order Systems

To rigorously test the physical fidelity of the pseudo-density descriptor, we evaluated the model’s ability to extrapolate to the broader chemical space $\mathcal { D } _ { 7 }$ . We first established a robust base model trained on a budget of 200 samples from the 4-component domain ${ \mathcal { D } } _ { 4 }$ . While the previous section demonstrated that 10 samples suffice for in-domain screening, this larger training budget was employed here to ensure the model fully captures the electronic manifold’s topology prior to extrapolation. This distinct step allows us to decouple the quality of the descriptor from data scarcity effects during zero-shot testing. As shown in Supplementary Figure ??, this base model exhibits non-trivial zeroshot predictive power on the 5-, 6-, and 7-component alloys of $\mathcal { D } _ { 7 }$ (Mo-Nb-Ta-Ti-V-W-Zr), despite the presence of four elements (Mo, Ta, V, W) never encountered during training. This confirms the existence of a transferable electronic manifold.

However, to achieve high-fidelity quantitative predictions suitable for materials screening, we employed a few-shot domain adaptation strategy. The base model was augmented with a min imal batch of 20 actively selected samples from the respective higher-order domains. As summarized in Table 2 and illustrated in Figure $^ { 6 , }$ this rapid adaptation yields significant predictive accuracy. For the 5-component alloys, the model achieves an $R ^ { 2 }$ of 0.85 and a NMAE of 5.54%. As the chemical complexity increases to 7 components, the model maintains a strong correlation $( R ^ { 2 } = 0 . 6 8 )$ and a low NMAE of 2.87%. Visually confirmed in Figure 5, the predictions track the $y = x$ line closely. The accompanying uncertainty distribution (Figure 5, right panel) shows a peaked distribution of predicted standard deviations. Quantitative calibration on the $\mathcal { D } _ { 7 }$ test set yields coverage of 43.2% within ±1σ and 78.8% within ±2σ, indicating moderate overconfidence in the extrapolative regime: an expected consequence of predicting outside the training chemical space where the GP posterior uncertainty is governed by prior assumptions rather than observed data. Per-complexity calibration improves systematically with chemical complexity: 40.9%/76.3% (5- component), 51.6%/88.0% (6-component), and 67.3%/100.0% (7-component) within ±1σ/±2σ respectively, consistent with the unseen-element fraction analysis in Supplementary Figure ??.

![](images/d2f044d2342c04d08bb0c26b7b9ce2458aa4ef6c51da19ad372bf6aace4b03e2.jpg)  
DFT-computed Bulk Moduli (GPa)

![](images/406c44e2415189bbfa4dbba7fe895dca6953a2402431153406a3624fffdfc98d.jpg)  
DFT-computed Bulk Moduli (GPa)

![](images/c0cda3ec8bcbacf2feff4eba4e88a3234753cae0adb2ec663531df163aaef8fb.jpg)  
DFT-computed Bulk Moduli (GPa)  
Fig. 6 Few-shot domain adaptation performance by chemical complexity within D . Parity plots for (a) 5-component $\left( R ^ { 2 } = 0 . 8 5 , \mathsf { N M A E } = 5 . 5 4 \% \right)$ (b) 6-component $( R ^ { 2 } = 0 . 8 2 , \mathsf { N M A E } = 4 . 1 6 \% )$ , and (c) 7-component $( R ^ { 2 } = 0 . 6 8 , \mathsf { N M A E } = 2 . 8 7 \% )$ alloys, obtained by augmenting the D<sub>4</sub>-trained base model with 20 actively selected samples from the respective target domains. Error bars denote GPR predictive uncertainty $( \pm 1 \sigma )$ . The systematic improvement with increasing chemical complexity is consistent with the unseen-element fraction analysis in Supplementary Figure ??.

This result directly addresses a central limitation of many descriptor-based machine learning approaches in materials science, namely the difficulty of extrapolating beyond the chemical species present in the training set. Unlike composition-based descriptors that require explicit knowledge of all constituent elements, the pseudo-density descriptor operates on a transferable electronic packing manifold. Because the local valence overlap environments in $\mathcal { D } _ { 7 }$ structurally resemble those in ${ \mathcal { D } } _ { 4 }$ (confirmed by the PC-space overlap in Supp. Fig. ??), the regression mapping adapts rapidly to the new chemical labels with minimal data.

To provide a more granular assessment of the framework’s extrapolative capability, Supplementary Figure ?? reports NMAE as a function of the unseen-element mole fraction $f _ { \mathrm { u n s e e n } } = x _ { \mathrm { M o } } +$ $x _ { \mathrm { { T a } } } + x _ { \mathrm { { V } } } + x _ { \mathrm { { W } } } ,$ binned by quartile across $\mathcal { D } _ { 7 }$ . The result exhibits a monotonically decreasing NMAE from 10.17% at low $f _ { \mathrm { u n s e e n } }$ (Q1: compositions dominated by the shared elements Nb, Ti, Zr) to 3.86% at high f<sub>unseen</sub> (Q4: compositions predominantly constituted by the four novel elements). To verify that this trend is not an artifact of the few-shot augmentation strategy, we examined the zero-shot quartile NMAE (no D data at all) and found the values to be numerically identical: $\begin{array} { r } { \mathsf { Q 1 } = 1 0 . 1 7 \% , 0 2 = 7 . 0 1 \% . } \end{array}$ , Q3 $= 5 . 2 7 \% , 0 4 = 3 . 8 6 \%$ . The monotonically decreasing trend therefore exists prior to any augmentation and is a genuine property of the untrained model’s generalisation behaviour. Reconstruction of the 20 actively selected augmentation samples (Supplementary Figure ??) confirms that all 20 fall in $\mathbf { Q } 1 _ { : }$ , consistent with the acquisition function $I ( \mathbf { x } ) = | \sigma ( \mathbf { x } ) / \mu ( \mathbf { x } ) |$ targeting the region of highest relative uncertainty; zero samples are drawn from Q2, Q3, or Q4. A Q1-restricted augmentation ablation, in which all 20 samples are forced into the Q1 pool, reduces Q1 NMAE from 10.17% to 8.67% while leaving Q3 and Q4 essentially unchanged (5.54% and 4.32% respectively), confirming that Q1 accuracy can be directly targeted at a marginal cost to higher-quartile performance (Supplementary Figure ??). This trend is physically interpretable: Q1 compositions dominated by Nb/Ti/Zr occupy the transitional region of the joint PC manifold where the $\mathcal { D } _ { 4 } { - } \mathrm { t o } { - } \mathcal { D } _ { 7 }$ feature-space boundary is most abrupt and the model must interpolate across the largest chemical gradient, whereas compositions with high $_ { \mathrm { M o + T a + V + W } }$ content lie in a region whose d-electron autocorrelation signature is coherently distinct and well-separated, permitting more reliable regression despite being chemically novel. The superior accuracy in the $\mathrm { h i g h - } f _ { \mathrm { u n s e e n } }$ regime is further con firmed by the parity plot for Mo/Ta/V/W-dominated compositions in Supplementary Figure $? ? ,$ which demonstrates that the pseudo-density descriptor generalizes to the fully novel compositional regime without systematic bias.

Table 2 Extrapolative performance metrics. The model was trained only on 4-component Al-Nb-Ti-Zr and tested on 5, 6, and 7-component alloys containing Mo, Ta, V, and W.

<table><tr><td>Components</td><td>N (Test Samples)</td><td>NMAE (%)</td><td>MAE (GPa)</td></tr><tr><td>5</td><td>3675</td><td>5.54</td><td>9.20</td></tr><tr><td>6</td><td>882</td><td>4.16</td><td>7.01</td></tr><tr><td>7</td><td>49</td><td>2.87</td><td>4.89</td></tr></table>

## Conclusions

We demonstrated that the non-interacting electron density offers a rigorous and scalable alternative to standard DFT-based descriptors for HEA discovery. By decoupling descriptor generation from the SCF bottleneck, this framework effectively reduces the computational investment of high-throughput screening. The integration of this descriptor with Bayesian active learning demonstrated superior sample efficiency in the Al-Nb-Ti-Zr RHEA system. The framework achieved a NMAE of <2% for the bulk modulus using only 10 actively selected training samples, surpassing the efficiency of state-of-the-art benchmarks that rely on fully converged densities. Beyond sample efficiency within the training domain, we demonstrated the model’s rigorous capability for chemical extrapolation. A model trained exclusively on the quaternary Al-Nb-Ti-Zr system successfully predicted the bulk moduli of a distinct 7-component system (Mo-Nb-Ta-Ti-V-W-Zr) containing four elements entirely absent from the training set. Furthermore, we demonstrated that augmenting this base model with just 20 samples from the target domain recovers high predictive fidelity (NMAE=2.87% for 7-component alloys). This suggests that the pseudo-density descriptor captures a transferable electronic packing manifold within the refractory BCC alloy family, enabling efficient few-shot domain adaptation without elementspecific feature engineering. Furthermore, we demonstrate the property transferability of this singular feature set; without modification, the descriptors accurately predict alloy formation energies (achieving an $R ^ { 2 }$ of 0.99 for the full compositional space for D ). The robustness of the approach was further validated through uncertainty quantification: bulk modulus predictions on ${ \mathcal { D } } _ { 4 }$ achieve 65.1% and 92.3% coverage within ±1σ and ±2σ respectively, consistent with a well-calibrated GPR. In the extrapolative D regime, coverage of 43.2%/±1 and 78.8%/±2 reflects expected mild overconfidence outside the training chemical space (Figure 5b). For the alloy formation energy, the coverage was even closer to nominal, with 88.8% and 99.8% of the data falling within ±1σ and ±2σ, respectively. Collectively, these results validate the voxelized atomic structure approach using pseudodensities as a practical route to decoupling descriptor generation from the most computationally demanding stages of DFT.

The overall reduction in computational investment by lowering the requisite DFT calculations via active learning, facilitates the extensive exploration of vast compositional landscapes. Avenues for future research include: (i) validating transferability beyond BCC crystal structures, e.g., FCC and HCP systems, and across periodic-table blocks beyond the group 4–6 refractory metals studied here; (ii) testing robustness of the pseudodensity descriptor to different SQS realizations per composition, supercell sizes, and pair-correlation matching quality, to determine whether the model learns transferable alloy physics or a regularized fingerprint of a specific disorder proxy; (iii) incorporating temperature-dependent properties via on-the-fly machinelearned molecular dynamics<sup>80,81</sup>, and (iv) extending the framework to predict functional properties, $\mathrm { e . g . } _ { }$ , thermal conductivity, oxidation resistance, critical for high-temperature applications. Nonetheless, the demonstrated capacity for zero-shot transfer within the refractory BCC alloy class, and few-shot domain adaptation with as few as 20 target-domain labels, marks a meaningful step toward sample-efficient computational screening of complex refractory alloy spaces. The framework is explicitly scoped to bulk modulus and formation enthalpy prediction for single-phase disordered BCC solid solutions; extension to FCC/HCP systems, configuration-sensitive properties, and magnetically ordered al loys remains an open direction for future validation.

## Author contributions

Pranoy Ray: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review & editing, Visualization. Sayan Bhowmik: Investigation, Software, Validation, Formal analysis, Writing – review & editing. Phanish Suryanarayana: Conceptu alization, Methodology, Validation, Resources, Writing – review & editing, Supervision, Project administration, Funding acquisition. Surya R. Kalidindi: Conceptualization, Methodology, Validation, Resources, Writing – review & editing, Supervision, Project administration, Funding acquisition. Andrew J. Medford: Concep tualization, Methodology, Validation, Resources, Writing – review & editing, Supervision, Project administration, Funding acquisition.

## Acknowledgements

PR and SK acknowledge support from NSF DMREF Award 2119640. SB, PS, and AJM gratefully acknowledge the support of the U.S. Department of Energy, Office of Science under grant DE-SC0023445. PR also acknowledhges support recieved from the Novelis Graduate Scholarship and the William H. Glenn Se. Fellowship.

## Data availability

All data and scripts for feature engineering (computing pseudo electron densities & spatial correlations), model training, and post-processing (uncertainty analysis) are archived on Zenodo at https://doi.org/10.5281/zenodo.21339835. Alternatively, the codes are also available at https://github.com/pranoyray/AlloyDiscovery .

## Conflicts of interest

There are no conflicts to declare.

## References

1 S. O. Jeje and M. B. Shongwe, Engineering Reports, 2025, 7, e70141.

2 P. Dang, J. Hu, Y. Xian, C. Li, Y. Zhou, X. Ding, J. Sun and D. Xue, Advanced Materials, 2025, 37, 2412198.

3 D. P. Tabor, L. M. Roch, S. K. Saikin, C. Kreisbeck, D. Sheberla, J. H. Montoya, S. Dwaraknath, M. Aykol, C. Ortiz, H. Tribukait, C. Amador-Bedolla, C. J. Brabec, B. Maruyama, K. A. Persson and A. Aspuru-Guzik, Nature Reviews Materials, 2018, 3, 5–20.

4 W. Kohn and L. J. Sham, Physical Review, 1965, 140, A1133– A1138.

5 P. Hohenberg and W. Kohn, Physical Review, 1964, 136, B864–B871.

6 B. Chakraborty, P. Ray, N. Garg and S. Banerjee, International Journal of Hydrogen Energy, 2021, 46, 4154–4167.

7 A. Kundu, A. Jaiswal, P. Ray, S. Sahu and B. Chakraborty, Journal of Physics D: Applied Physics, 2024, 57, 495502.

8 H. T. Nair, A. Kundu, P. Ray, P. K. Jha and B. Chakraborty, Sustainable Energy & Fuels, 2023, 7, 5109–5119.

9 S. Ramakrishna, T.-Y. Zhang, W.-C. Lu, Q. Qian, J. S. C. Low, J. H. R. Yune, D. Z. L. Tan, S. Bressan, S. Sanvito and S. R. Kalidindi, Journal of Intelligent Manufacturing, 2019, 30, 2307– 2326.

10 P. Ray, K. Choudhary and S. R. Kalidindi, Integrating Materials and Manufacturing Innovation, 2025, 14, 1–13.

11 L. Ward, A. Agrawal, A. Choudhary and C. Wolverton, npj Computational Materials, 2016, 2, 1–7.

12 L. Ward, A. Dunn, A. Faghaninia, N. E. R. Zimmermann, S. Bajaj, Q. Wang, J. Montoya, J. Chen, K. Bystrom, M. Dylla, K. Chard, M. Asta, K. A. Persson, G. J. Snyder, I. Foster and A. Jain, Computational Materials Science, 2018, 152, 60–69.

13 P. Ray, A. R. Castillo, M. Kolel-Veetil and S. R. Kalidindi, Advanced Science, 2026, n/a, e23817.

14 X. Lei and A. J. Medford, The Journal of Physical Chemistry Letters, 2022, 13, 7911–7919.

15 P. R. Kaundinya, K. Choudhary and S. R. Kalidindi, JOM, 2022, 74, 1395–1405.

16 S. R. Kalidindi, A. J. Medford and D. L. McDowell, JOM, 2016, 68, 2126–2137.

17 F. Brockherde, L. Vogt, L. Li, M. E. Tuckerman, K. Burke and K.-R. Müller, Nature Communications, 2017, 8, 872.

18 T. Xie and J. C. Grossman, Physical Review Letters, 2018, 120, 145301.

19 K. Choudhary and B. DeCost, npj Computational Materials, 2021, 7, 1–8.

20 A. Merchant, S. Batzner, S. S. Schoenholz, M. Aykol, G. Cheon and E. D. Cubuk, Nature, 2023, 624, 80–85.

21 A. P. Bartók, R. Kondor and G. Csányi, Physical Review B, 2013, 87, 184115.

22 P. Lyngby, C. Larsen and K. W. Jacobsen, Physical Review Materials, 2024, 8, 123802–123802.

23 A. G. Kusne, H. Yu, C. Wu, H. Zhang, J. Hattrick-Simpers,

B. DeCost, S. Sarker, C. Oses, C. Toher, S. Curtarolo, A. V. Davydov, R. Agarwal, L. A. Bendersky, M. Li, A. Mehta and I. Takeuchi, Nature Communications, 2020, 11, 5966.

24 X. Qian, B.-J. Yoon, R. Arróyave, X. Qian and E. R. Dougherty, Patterns, 2023, 4, 1–20.

25 T. Lookman, P. V. Balachandran, D. Xue and R. Yuan, npj Com putational Materials, 2019, 5, 21.

26 P. Ray, A. P. Generale, N. Vankireddy, Y. Asoma, M. Nakauchi, H. Lee, K. Yoshida, Y. Okuno and S. R. Kalidindi, npj Compu tational Materials, 2025, 11, 234.

27 P. Ray, A. Yuichiro, N. Vankireddy, A. P. Generale, N. Masataka, L. Haein, Y. Katsuhisa, S. R. Kalidindi and O. Yoshishige, Assessing the accuracy of Bayesianoptimized CGMD in predicting polymer miscibility, 2025, https://chemrxiv.org/engage/chemrxiv/ article-details/69263681a10c9f5ca1c0700b.

28 M. O. Buzzy, D. Montes de Oca Zapiain, A. P. Generale, S. R. Kalidindi and H. Lim, Acta Materialia, 2025, 284, 120537.

29 D. Khatamsaz, B. Vela, P. Singh, D. D. Johnson, D. Allaire and R. Arróyave, npj Computational Materials, 2023, 9, 49.

30 R. Nakayama, R. Shimizu, T. Haga, T. Kimura, Y. Ando, S. Kobayashi, N. Yasuo, M. Sekijima and T. Hitosugi, Science and Technology ofAdvanced Materials: Methods, 2022, 2, 119– 128.

31 J. Startt, M. J. McCarthy, M. A. Wood, S. Donegan and R. Din greville, npj Computational Materials, 2024, 10, 164.

32 Z. Hou and K. Tsuda, Machine Learning Meets Quantum Physics, Springer International Publishing, Cham, 2020, pp. 413–426.

33 P. I. Frazier, A Tutorial on Bayesian Optimization, 2018, https://arxiv.org/abs/1807.02811, Version Number: 1.

34 S. M. A. A. Alvi, J. Janssen, D. Khatamsaz, D. Perez, D. Allaire and R. Arróyave, Acta Materialia, 2025, 289, 120908.

35 T. Hastie, J. Friedman and R. Tibshirani, The Elements of Sta tistical Learning, Springer New York, New York, NY, 2001.

36 C. E. Rasmussen and C. K. I. Williams, Gaussian Processes for Machine Learning, The MIT Press, 2005.

37 C. G. E. Boender and J. Mockus, Mathematics of Computation, 1991, p. 878.

38 J. Mockus, Bayesian Approach to Global Optimization: Theory and Applications, Springer Netherlands, Dordrecht, 1989.

39 K. Hanaoka, iScience, 2021, 24, 1–19.

40 M. A. Seyed Mahmoud, D. Renner, A. Khosravani and S. R. Kalidindi, Acta Materialia, 2026, 306, 121902.

41 Y. Zhao, K. Yuan, Y. Liu, S.-Y. Louis, M. Hu and J. Hu, The Journal of Physical Chemistry C, 2020, 124, 17262–17273.

42 A. D. Casey, S. F. Son, I. Bilionis and B. C. Barnes, Journal of Chemical Information and Modeling, 2020, 60, 4457–4473.

43 M. C. Barry, Ph.D., Georgia Institute of Technology, United States – Georgia, 2023.

44 M. C. Barry, I. S. Winter, M. Chandross, J. R. Gissinger, S. R. Kalidindi and S. Kumar, npj Computational Materials, 2026.

45 M. C. Barry, K. E. Wise, S. R. Kalidindi and S. Kumar, The Journal of Physical Chemistry Letters, 2020, 11, 9093–9099.

46 M. C. Barry, J. R. Gissinger, M. Chandross, K. E. Wise, S. R. Kalidindi and S. Kumar, Computational Materials Science, 2023, 230, 112431.

47 M. C. Barry, S. Kumar and S. R. Kalidindi, Machine Learning in Molecular Sciences, Springer International Publishing, Cham, 2023, vol. 36, pp. 67–89.

48 S. R. Kalidindi, Hierarchical Materials Informatics, Elsevier, 2015.

49 P. R. Kaundinya, K. Choudhary and S. R. Kalidindi, Physical Review Materials, 2021, 5, 063802.

50 A. Cecen, H. Dai, Y. C. Yabansu, S. R. Kalidindi and L. Song, Acta Materialia, 2018, 146, 76–84.

51 A. Mann and S. R. Kalidindi, Frontiers in Materials, 2022, 9, 1–14.

52 A. Zunger, S.-H. Wei, L. G. Ferreira and J. E. Bernard, Physical Review Letters, 1990, 65, 353–356.

53 O. Certík, J. E. Pask and J. Vacká <sup>ˇ</sup> ˇr, Computer Physics Communications, 2013, 184, 1777–1791.

54 S. Bhowmik, J. E. Pask, A. J. Medford and P. Suryanarayana, Computer Physics Communications, 2025, 308, 109448.

55 A. van de Walle, M. Asta and G. Ceder, Calphad, 2002, 26, 539–553.

56 D. Gehringer, M. Friák and D. Holec, Computer Physics Communications, 2023, 286, 108664.

57 D. R. Hamann, Physical Review B, 2013, 88, 085117.

58 M. F. Shojaei, J. E. Pask, A. J. Medford and P. Suryanarayana, Computer Physics Communications, 2023, 283, 108594.

59 J. P. Perdew, K. Burke and M. Ernzerhof, Physical Review Letters, 1996, 77, 3865–3868.

60 B. Zhang, X. Jing, S. Kumar and P. Suryanarayana, SoftwareX, 2023, 21, 101295.

61 Q. Xu, A. Sharma and P. Suryanarayana, SoftwareX, 2020, 11, 100423.

62 B. Zhang, X. Jing, Q. Xu, S. Kumar, A. Sharma, L. Erlandson, S. J. Sahoo, E. Chow, A. J. Medford, J. E. Pask and P. Suryanarayana, Software Impacts, 2024, 20, 100649.

63 Q. Xu, A. Sharma, B. Comer, H. Huang, E. Chow, A. J. Medford, J. E. Pask and P. Suryanarayana, SoftwareX, 2021, 15, 100709.

64 F. Ren and F. Liu, The Journal of Chemical Physics, 2022, 157, 184106.

65 D. T. Fullwood, S. R. Kalidindi, S. R. Niezgoda, A. Fast and N. Hampson, Materials Science and Engineering: A, 2008, 494, 68–72.

66 T. Fast and S. R. Kalidindi, Acta Materialia, 2011, 59, 4595– 4605.

67 S. R. Niezgoda, D. T. Fullwood and S. R. Kalidindi, Acta Materialia, 2008, 56, 5285–5292.

68 S. R. Niezgoda, Y. C. Yabansu and S. R. Kalidindi, Acta Mate rialia, 2011, 59, 6387–6400.

69 A. Ma´ckiewicz and W. Ratajczak, Computers & Geosciences, 1993, 19, 303–342.

70 G. Kresse and J. Hafner, Physical Review B, 1993, 47, 558–561.

71 G. Kresse and J. Furthmüller, Computational Materials Science, 1996, 6, 15–50.

72 G. Kresse and J. Furthmüller, Physical Review B, 1996, 54, 11169–11186.

73 G. Kresse and D. Joubert, Physical Review B, 1999, 59, 1758– 1775.

74 S. Maes, F. D. Ceuster, M. V. d. Sande and L. Decin, Journal of Open Source Software, 2025, 10, 7148.

75 C. E. Rasmussen and H. Nickisch, Journal ofMachine Learning Research, 2010, 11, 3011–3015.

76 C. E. Rasmussen and C. K. I. Williams, Gaussian processes for machine learning, MIT Press, Cambridge, Mass, 2006.

77 D. P. Kingma and J. Ba, Adam: A Method for Stochastic Optimization, 2017, http://arxiv.org/abs/1412.6980, arXiv:1412.6980 [cs].

78 D. V. Lindley, The Annals of Mathematical Statistics, 1956, 27, 986–1005.

79 X. Huan and Y. M. Marzouk, Journal of Computational Physics, 2013, 232, 288–317.

80 S. Kumar, X. Jing, J. E. Pask, A. J. Medford and P. Suryanarayana, The Journal of Chemical Physics, 2023, 159, 244106.

81 L. R. Timmerman, S. Kumar, P. Suryanarayana and A. J. Medford, Journal of Chemical Theory and Computation, 2024, 20, 5788–5795.

## Data Availability Statement

All data and scripts for feature engineering (computing pseudo electron densities & spatial correlations), model training, and post-processing (uncertainty analysis) are archived on Zenodo at https://doi.org/10.5281/zenodo.21339835 . Alternatively, the codes are also available at https://github.com/pranoy-ray/AlloyDiscovery .