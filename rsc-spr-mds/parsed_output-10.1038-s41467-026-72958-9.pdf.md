
Article            https://doi.org/10.1038/s41467-026-72958-9

# Non-equilibrium reducing flame aerosol process to create supported high-entropy alloy nanoparticles

Received: 13 September 2025

Accepted: 29 April 2026

Published online: 11 May 2026

Shuo Liu 1,2,10, Jiashun Liang 1,10, Jonas L. Kaufman 3, Qike 4, Jiang Dominik Wierzbicki 5,6, Kang-Lan Tung Kaiwen 1, Chen 1, Haolan Sun 7, Zhengxi Xuan 1,8, Mohd Ashhar Khan ¹, Chengyu Song 9, Shinyoung Kang 3, Wei Chen 7, Gang Wu 1,11, Jeffrey J. Urban 2,11, Mark T. Swihart 1,8,11 &#x26; Chaochao Dun 2,11

High-entropy alloy (HEA) nanomaterials provide opportunities and property combinations for energy and electronic applications, but their practical synthesis faces challenges of elemental immiscibility, metal reducibility, and particle aggregation during their synthesis. Herein, we report a broadly applicable non-equilibrium, scalable, and in-situ reducing flame aerosol process for synthesis of supported HEA nanoparticles. This versatile process can directly load a high concentration of 2 ~ 4 nm HEA nanoparticles on various 1- to 3-dimensional supports. Notably, simultaneous formation of HEA nanoparticles and a mesoporous silica support was successfully realized in a single step. Exploration of this process demonstrates the role of kinetics and entropy on decreasing alloy particle size and altering the reducibility of elements. We propose an entropy-induced reduction mechanism to incorporate oxidizable elements into HEAs, which extends the compositional space of HEA nanoparticles. As a representative catalytic application, we present a RuPdOsIrPt/graphene electrocatalyst with high activity and stability for hydrogen oxidation reaction. Our findings open horizons for high-performance HEA design and applications in diverse fields such as catalysis, electrochemistry, and sensing.

Alloys in which multiple elements randomly occupy sites in a single crystallographic lattice are known as solid solutions. In 2004, Yeh¹ and Cantor² et al. reported solid solution alloys containing 5 or 6 elements with near-equiatomic compositions. The presence of multiple elements in a solid solution increases the system configurational entropy, via the entropy of mixing, to overcome the unfavorable enthalpy of mixing. This entropic effect stabilizes the high-entropy solid solution relative to phase separation or formation of ordered.

1Department of Chemical and Biological Engineering, University at Buffalo, The State University of New York, Buffalo, NY, USA. 2The Molecular Foundry, Lawrence Berkeley National Laboratory, Berkeley, CA, USA. 3Materials Science Division and Laboratory for Energy Applications for the Future (LEAF), Lawrence Livermore National Laboratory, Livermore, CA, USA. 4Instrumentation and Service Center for Physical Sciences, Westlake University, Hangzhou, Zhejiang, China. 5National Synchrotron Light Source ǁ, Brookhaven National Laboratory, Upton, NY, USA. 6AGH University of Science and Technology, Faculty of Energy and Fuels, Cracow, Poland. 7Department of Materials Design and Innovation, University at Buffalo, The State University of New York, Buffalo, NY, USA. 8RENEW Institute, University at Buffalo, The State University of New York, Buffalo, NY, USA. 9The National Center for Electron Microscopy, The Molecular Foundry, Lawrence Berkeley National Laboratory, Berkeley, CA, USA. 10These authors contributed equally: Shuo Liu, Jiashun Liang. 11These authors jointly supervised this work: Gang Wu, Jeffrey J. Urban, Mark T. Swihart, Chaochao Dun. e-mail: gangw@wustl.edu; jjurban@lbl.gov; swihart@buffalo.edu; cdun@lbl.gov

| 1 Nature Communications (2026) 17:6314




Article                                                                                                    https://doi.org/10.1038/s41467-026-72958-9

intermetallic phases, resulting in enhanced mechanical properties³. As immiscible elements in a single-phase bi-metallic or high-entropy nanostructure13,³²–³⁴. Traditional FSP techniques dissolve metal salts in organic solvents with high combustion enthalpy, driving particle formation through combustion of this precursor solution. The use of organic solvents and precursors soluble in them increases production costs, relative to use of inorganic salts dissolved in water, and particle formation within the flame limits the use of carbon and other thermally unstable supports (such as metal–organic frameworks, MOFs) that cannot withstand flame conditions. Flame-assisted spray pyrolysis allows the use of aqueous precursors³⁵. Normally, in the gas-to-particle route, both FSP and FASP produce particles ranging from a few nanometers to several tens of nanometers in size, whereas the droplet-to-particle route generally yields much larger particles³⁶–³⁸. Additionally, increased configurational entropy can also offer low Gibbs energy positions for active sites, which contributes to catalyst structural stability under harsh reaction conditions¹³.

Traditional HEAs are fabricated by top-down methods like vacuum arc melting¹⁴, which produce bulk materials with limited uniformity and crystallite size control and are not suitable for catalysis and other applications where high specific surface area is needed. Recently, many advanced methods have been developed for the synthesis of HEA nanomaterials¹⁵. For example, wet-chemistry synthesis methods, such as co-reduction¹⁶, continuous-flow reduction¹⁷, Mo-assisted reduction diffusion¹⁸, and CO adsorption reduction¹⁹, can achieve low-dimensional HEA nanomaterials with small particle size or controllable morphology. However, under equilibrium reaction conditions, these methods can only integrate elements with similar physicochemical properties (such as crystal structure, atomic radius, and electronegativity) into a single-phase alloy solid solution. Phase separation will occur when the entropy of mixing is insufficient to overcome the positive enthalpy of mixing, resulting in a limited compositional space at the atomic scale²⁰. Some special equilibrium synthesis approaches can overcome elemental immiscibility, e.g., the use of liquid gallium to decrease system mixing enthalpy21,²², but generate large nanoparticles due to the high surface tension, fluidity and Ostwald ripening effect of Ga. Achieving high loadings of HEA nanoparticles is desirable for enhancing current density and reducing mass transport resistance in electrochemical devices; however, a trade-off between particle size and loading is commonly encountered²³.

In recent years, non-equilibrium synthesis approaches have been developed to fabricate HEA nanomaterials, such as flash Joule heating²⁴, high-temperature plasma²⁵, graphdiyne-assisted fast sparking platform²⁶, and laser scanning ablation²⁷. These methods provide high reaction temperature and rapid material formation on timescales of milliseconds to nanoseconds. These short timescales result in kinetic mixing of otherwise immiscible metals in a single-phase metastable alloy. However, their violent synthesis environments often lead to inhomogeneous particle size distribution, and the high-energy input and harsh operation conditions limit industrial application of these methods. Therefore, development of a versatile and scalable methodology to fabricate highly homogeneous HEA nanoparticles at high loadings on support materials is important. Likewise, understanding the mechanisms of rapid reaction kinetics and configurational entropy on particle dispersion, elemental miscibility, and metal reducibility in the non-equilibrium synthesis processes remains challenging.

Flame aerosol processing, including flame spray pyrolysis (FSP), has been one of the most common technologies to fabricate inorganic powders in industry²⁸. Benefiting from this rapid, one-step, and continuous synthesis route, millions of tons of flame-made nanoparticles like carbon black, fumed SiO₂, TiO₂, and Al₂O₃ have been manufactured by industry leaders like DuPont and Evonik²⁹,³⁰. In an FSP process, the reactant precursors are first vaporized or atomized, and products are then formed in the vapor phase or within droplets³¹. The rapid gas-to-particle or droplet-to-particle conversion can combine immiscible elements³². A second key mechanism is entropy-driven mixing. According to ΔG = ΔH – T•ΔS, the increase in configurational entropy due to mixing decreases the system’s Gibbs energy.

# Results

# Synthesis mechanism

The supported HEA nanoparticles were fabricated by the single-step, continuous, and in-situ reducing flame aerosol process described in the Methods section (Fig. 1a, Supplementary Figs. 1, 2). A homogeneous precursor suspension containing five different metal cations and commercial carbon black support (Supplementary Fig. 3) was continuously injected into the reactor, while the product was continuously collected downstream. In general, the non-equilibrium flame synthesis adopted here involves four mechanisms. The first is kinetically-driven mixing. When the precursor suspension entered the reactor, it was immediately shear-atomized by a sonic-velocity hot stream of combustion products into droplets of a few micrometers in diameter41,⁴², and the evaporation time of such a small droplet was on the order of a few to several tens of milliseconds, with heating and cooling rates on the order of 10⁵ ~ 10⁶ K/s⁴³. Therefore, the HEA nanoparticle nucleation and growth occurred on a timescale too short for atoms of different elements to segregate via diffusion. This results in kinetic mixing (trapping) of different atoms in a single-phase, including immiscible elements³².

|     2
Nature Communications (2026) 17:6314




Article                                            https://doi.org/10.1038/s41467-026-72958-9

a Cold N2 Ru{}
Rh3+
Pd{2 Atomization Heterogeneous
nucleation P14

In-situ Carbon reducing

Temperature

Solute partitioning TTT curve

| Precursor suspension | A | Soncoling | Quenching                | Growth Time             |
| -------------------- | - | --------- | ------------------------ | ----------------------- |
| H₂:O₂:N₂=15:3.5:6    | b | d 40      | Arithmetic mean: 2.90 nm | Geometric mean: 2.46 nm |

hD  25

224A  (111)  20

15

1 nm  ©[1T0]  10

5

%  m  25  30

5  10  15  20

100 nm  10 nm  Particle size (nm)

C  Ru  Rh  Pd  Pt  C  e  RuRhPdIrPt/carbon

100 nm  100 nm    100 nm    100 nm    100 nm                                      100 nm    100 nm      20

Ru        Rh        Pd

5 nm     5 nm      5 nm      5 nm      5 nm                                        5 nm      5 nm          30  40  50  60  70

2 Theta (deg.)

Fig. 1 | HEA nanoparticle formation process. a Schematic of non-equilibrium reducing flame aerosol synthesis of supported HEA nanoparticles; b TEM images, FFT pattern, and AC-STEM images; c HAADF-STEM elemental maps of RuRhPdIrPt; d particle size distribution; and e XRD pattern of a representative RuRhPdIrPt/carbon. Source data for d, e are provided in the Source Data file.

facilitating the incorporation of multiple elements into a homogeneous solid solution⁴⁴. The third key mechanism is in-situ reduction. Although the metal precursors are introduced as ions in solution, we supplied excess H2 to the flame, thereby creating a reducing atmosphere in the reaction chamber, which resulted in the formation of metals rather than oxides for materials that can be reduced by H2 in the presence of H2O. The fourth key mechanism is heterogeneous nucleation. We included a support material in the precursor suspension, which shifted the particle nucleation mechanism from homogeneous nucleation⁴⁵,⁴⁶ to heterogeneous nucleation and significantly decreased the energy barrier for nucleation. In this case, the surface of the support material provided numerous nucleation sites to disperse alloy particles, which greatly decreased the particle size from tens of nanometers, typical of a gas-to-particle formation route by traditional flame spray pyrolysis34, to below 3 nm. For example, the support-free HEA formed in our current flame aerosol process exhibited large particles. This sample also exhibited phase separation between RuRhPdIrPt high-entropy alloy and (RuRhPdIrPt)O high-entropy oxide (Supplementary Fig. 4a). H2 temperature-programmed reduction (H2

|     3 Nature Communications (2026) 17:6314




Article                                                                                                         https://doi.org/10.1038/s41467-026-72958-9

(Supplementary Fig. 6) was limited by calibration uncertainty and peak overlap, leading to larger differences from the ICP and XRF results. Compositions from all three techniques are included in Supplementary Table 1, but the EDS result cannot be considered quantitatively accurate. In addition, the Raman spectra of pure carbon support and RuRhPdIrPt/carbon were nearly identical, with similar ID/IG ratio, demonstrating the rapid flame process did not damage the carbon structure (Supplementary Fig. 7). N₂ ad-/desorption analysis showed the high porosity and surface area of RuRhPdIrPt/carbon with a Brunauer-Emmett-Teller (BET) specific surface area of 508 m²/g (Supplementary Fig. 8). In another flame synthesized RuRhPdIrPt/carbon with a higher metal:carbon loading of 80 wt.% (Supplementary Fig. 9), the HEA still maintained the small geometric mean particle size of 3.80 nm. Together, these material characterization results conclusively demonstrate the successful synthesis of single-phase, highly homogeneous, and highly dispersed HEA nanoparticles.

# Extension to a diverse range of support materials

To demonstrate the versatility of this method, we applied it to a diverse range of 0- to 3-dimensional support materials, including TiO₂ nanocrystals (Supplementary Fig. 10), carbon nanotubes (Supplementary Fig. 11), graphene (Supplementary Fig. 12), Zr UiO-66 MOF (Supplementary Fig. 13), and Fe-N-C prepared as reported in our previous study⁴⁷ (Supplementary Fig. 14). These support materials decorated with metal nanoparticles have broad potential for application in energy-related fields, such as photocatalysis⁴⁸, sensing⁴⁹, H₂ storage⁵⁰, organic synthesis⁵¹, and electrocatalysis⁵². Fig. 2a shows representative examples of the aerosol-synthesized 10 wt.% RuRhPdIrPt/TiO₂, 40 wt.% RuRhPdIrPt/Carbon nanotube, 40 wt.% RuRhPdIrPt/Graphene, 10 wt.% RuRhPdIrPt/UiO-66. The high-entropy material system is not limited to specific compositions; therefore, we also developed a 40 wt.% PdO-sIrPtAu/Fe-N-C. TEM imaging revealed that HEA nanoparticles were highly dispersed across all the support materials (Fig. 2a, Supplementary Figs. 15-19), coexisting with a few anomalously larger particles. These anomalously large particles are likely caused by the uneven distribution of the support materials in the precursor suspension. The measured average diameters of HEA nanoparticles were 4.76 nm on TiO₂ nanocrystals, 2.76 nm on carbon nanotubes, 2.92 nm on graphene, 4.00 nm on UiO-66 MOF, and 4.09 nm on Fe-N-C (Fig. 2c, Supplementary Fig. 20). The HAADF-STEM element maps confirmed the homogeneous mixing of all constituent elements within each alloy nanoparticle (Fig. 2b). Meanwhile, all the XRD patterns showed a single-phase FCC crystalline structure (Fig. 2d, Supplementary Fig. 21). As observed for HEA/carbon, the Raman spectra of HEA/carbon nanotubes, HEA/graphene, and HEA/Fe-N-C were consistent with those of the pure support materials, indicating no damage to their carbon structure (Fig. 2e, Supplementary Fig. 22). All the materials retained their porosity and pore size distribution after loading with HEA nanoparticles (Fig. 2f, Supplementary Fig. 23). The observed decreases in BET surface area compared to pure support materials can be attributed to addition of mass (in the form of HEA nanoparticles) without addition of surface area, and possibly some pore blockage by the HEA nanoparticles. These results collectively demonstrate that our flame aerosol process can be successfully applied to various support materials, greatly expanding its potential applications.

# Simultaneous formation of HEA nanoparticles and mesoporous silica support

Mesoporous silica is a widely used support material in heterogeneous catalysis due to its high porosity and structural stability⁵³. In a previous study⁵⁴, we presented an evaporation-driven micelle self-assembly and inorganic macromolecular sol-gel process to synthesize mesoporous silica in this flame aerosol process. It produced a mesoporous silica material with hollow nanoshell morphology, amorphous structure, and BET surface area of 856 m²/g, and pore size distribution of 1 ~ 5 nm (Supplementary Fig. 24). Here, we found that adding metal salts to the mesoporous silica precursor solution allowed formation of mesoporous silica supported HEA nanoparticles in a single step (Fig. 3a). After atomization, the precursor droplet contained Ru, Rh, Pd, Ir, and Pt cations, along with tetraethyl orthosilicate (TEOS) and cetyl-trimethylammonium bromide (CTAB). As the droplet evaporated, CTAB self-assembled into a soft template of cylindrical micelles, and TEOS molecules co-polymerized around the micelles via sol-gel chemistry, forming the intermediate of mesoporous silica. At the same time, HEA nanoparticles formed on the intermediate via the mechanisms shown in Fig. 1a. Removal of the micelle template and other organic residues (Fig. 3b) by simple ethanol washing produced the final HEA/Mesoporous silica product.

In this manner, both RuRhPdIrPt/mesoporous silica and PdOsIrPtAu/mesoporous silica materials with metal:SiO₂ loadings of 15 wt.% were successfully fabricated. Both types of HEA nanoparticles exhibited high dispersion, small and uniform particle size, and homogeneous mixing of all constituent elements within each nanoparticle at the atomic level (Fig. 3d, f, Supplementary Fig. 25). Their single FCC phase was also confirmed by XRD patterns (Fig. 3e, Supplementary Fig. 26). Even with loading of HEA nanoparticles, the materials provided high BET surface areas of 517 and 526 m²/g for RuRhPdIrPt/silica and PdOsIrPtAu/silica, respectively, and large volumes of mesopores (Fig. 3c, Supplementary Fig. 27).

The simultaneous formation of mesoporous silica and HEA nanoparticles could greatly decrease the preparation cost of these materials relative to sequential processes in solution, improve the dispersity of the HEA nanoparticles, and prevent the formation of anomalous large particles. Additionally, the formed HEA nanoparticles were embedded within the mesoporous silica rather than forming on the surface. This nanoscale confinement can significantly enhance the sintering resistance of the nanoparticles⁵⁵.

# Role of kinetics and entropy in decreasing particle size

The good dispersibility of flame aerosol synthesized HEA nanoparticles prompted us to probe this effect further. For example, in a previous study on fabricating graphene oxide supported HEA nanoparticles via fast moving bed pyrolysis⁵⁶, the HEA particle size was ~2 nm at a low loading of 3 wt.%. When the HEA loading was increased to 10 wt.%, the particle size grew to over 20 nm. In contrast, in our flame synthesized HEA/Carbon, the particle size of HEA increased from ~2.9 nm at 40 wt.% metal:carbon loading (Fig. 1d, Supplementary Fig. 5) to only 4.3 nm at high loading amount of 80 wt.% (Supplementary Fig. 9). Meanwhile, the mentioned study⁵⁶ also discussed the effect of HEA nucleation and growth time on the particle size. The ~2 nm HEA was achieved through a fast 5 s material formation process at 923 K. When the heating time was extended to 30 minutes, the particle size exceeded 100 nm, and phase separation occurred. However, in the current flame aerosol process, the HEA formed within a few milliseconds, as microdroplets evaporated at ~700 °C⁴³, and downstream quenching with cold N₂ prevented further growth or sintering. Therefore, we hypothesize that the non-equilibrium kinetic processes adopted here can greatly limit the growth of metal nanoparticles, reducing the overall particle sizes (Fig. 4a). To further confirm our hypothesis, we used a traditional wet-impregnation method to load Pd nanoparticles on a typical mesoporous silica MCM-41 (ex situ loaded Pd/MCM-41) at 500 °C, which is a typical temperature in thermal annealing process for preparing catalysts⁵⁷. Meanwhile, we used the non-equilibrium flame aerosol process to load Pd nanoparticles on mesoporous silica (in-situ formed Pd/F-SiO₂) and RuRhPdIrPt HEA nanoparticles on mesoporous silica (in-situ formed HEA/F-SiO₂). The metal:SiO₂ ratio range varied from 1 wt.% to 50 wt.% and their ratio in the product is shown in Supplementary Tables 2-4.

|     4
Nature Communications (2026) 17:6314




Article    https://doi.org/10.1038/s41467-026-72958-9

# HEA nanoparticles on 1D - 3D support materials

| 20 nm | 20 nm | 50 nm | 50 nm | 50 nm |       |                          |                         |   |
| ----- | ----- | ----- | ----- | ----- | ----- | ------------------------ | ----------------------- | - |
| 10 nm | b     | Pd    | Os    | Ir    | Pt    | Au                       | C₃₅                     |   |
|       |       |       |       |       |       | Arithmetic mean: 4.09 nm | Geometric mean: 3.35 nm |   |
| 50 nm | 50 nm | 50 nm | 50 nm | 50 nm | 50 nm | 2²⁰                      |                         |   |
| Pd    | c     | Ir    | Pt    | Au    | 15    | 10                       |                         |   |
| 20 nm | 20 nm | 20 nm | 20 nm | 20 nm | 20 nm |                          |                         |   |

10 15 20 25 30 35 40 45 50 55

Particle size (nm)

Fig. 2 | HEA nanoparticles on 1D-3D support materials. a Schematic and TEM images of HEA nanoparticles on various supports; b HAADF-STEM elemental maps of PdOsIrPtAu on Fe-N-C support; c particle size distribution (HEA loading 40 wt.%); d XRD pattern; e Raman spectra; f N2 adsorption/desorption isotherm plot and BJH desorption pore width distribution curve of PdOsIrPtAu/Fe-N-C. Source data for c–f are provided in the Source Data file.

The results indicated that under equilibrium reaction conditions of thermal annealing at 500 °C for Pd/MCM-41, heavy sintering of Pd nanoparticles occurred. As the Pd:SiO₂ ratio increased from 1 wt.% to 50 wt.%, the average size of Pd nanoparticles increased from 10.2 nm to 60.9 nm, and the Pd nanoparticle size distribution broadened substantially (Fig. 4b, Supplementary Fig. 28). In contrast, the non-equilibrium flame aerosol synthesized Pd/F-SiO2 exhibited small nanoparticle size and narrow particle size distribution. As the Pd:SiO₂ ratio increased from 1 wt.% to 50 wt.%, the average size of Pd nanoparticles increased from 3.05 nm to 8.51 nm, demonstrating the role of rapid reaction kinetics in decreasing particle size (Fig. 4b, Supplementary Fig. 29). This can be attributed to their different particle nucleation and growth rates. Generally, the formation of nanocrystals undergoes the “Precursor → Monomer → Nuclei → Nanocrystal” process according to LaMer’s nucleation mechanism (Supplementary Fig. 31)⁵⁶. The small critical nucleus served as the foundation for nanoparticle growth, resulting in smaller.

| 5 Nature Communications (2026) 17:6314




Article    https://doi.org/10.1038/s41467-026-72958-9

a  RuCl3 + RhCl3 + PdCl2 + IrCl + PtCl4 + TEOS + CTAB + H2O + EtOH + HCl (pH~2)

Flame aerosol process    Ethanol washing

# Mesoporous SiO2 support route

Poly-           Template

Self-assemble     condensation    Growth    removal

b  Intermediate product    Inorganic Si-O bond  C 300     Adsorption isotherm plot

Mesoporous silica                                      Desorption isotherm plot

| 20  | C-H stretching        | 20             | 250 BET surface area: 517 m²/g |
| --- | --------------------- | -------------- | ------------------------------ |
| 200 | Physical adsorbed H₂O | C-C stretching | C-H bending                    |
| 150 | C-N bond              | Structured -OH |                                |
| 022 | 100                   | to             | 100                            |
| 300 | Pore width (nm)       |                |                                |

4000 3500 3000           2500 2000      1500           1000              0.0  0.2  0.4   0.6               0.8    1.0

Wavenumber (cm-1)                                                        Relative pressure (P/P0)

d                                   (111)                                           e                    RuRhPdIrPt/mesoporous SiO2,

Pt (PDF #001-1190)

M11F22A

20

Mesopores                   T    O

50 nm                         10 nm                                              30  40  50                60        70

2 Theta (deg.)

f               Ru                  Rh                    Pd         Ir             Pt     Si

500 nm  500 nm  500 nm  500 nm     500 nm  500 nm     500 nm  500 nm

Ru      Rh      Pd         Ir      Pt         Si

20 nm  20 nm    20 nm  20 nm                                                       20 nm  20 nm  20 nm                          20 nm

Fig. 3 | HEA nanoparticles on mesoporous silica. a Schematic of the process of     distribution curve; d TEM images and FFT pattern; e XRD pattern of

simultaneous HEA nanoparticle and mesoporous silica support formation;             RuRhPdIrPt/Mesoporous silica; and f HAADF-STEM elemental maps of

RuRhPdIrPt embedded within the mesoporous silica. Source data for

b, c, e are provided in the Source Data file.

|     6 Nature Communications (2026) 17:6314




Article                                                       https://doi.org/10.1038/s41467-026-72958-9

# a Kinetic &#x26; thermodynamic dispersion

|                    | 90 | Pd/MCM-41 | Pd/F-SiO2 | HEA/F-SiO |
| ------------------ | -- | --------- | --------- | --------- |
| Kinetic dispersion | 80 |           |           |           |
| Precursor 2        | 20 | 20        | 20        | 60        |
|                    | 50 |           |           |           |
|                    | 40 | 100 nm    |           |           |
|                    | 30 |           |           |           |
|                    | 20 |           |           |           |
|                    | 10 |           |           |           |

Particle size decreasing 0 1 wt.% 3 wt.% 8 wt.% 15 wt.% 30 wt.% 50 wt.%

Metal:SiO2

| C | 3.0   | 0.20   |
| - | ----- | ------ |
|   | 2.5   | -0.15  |
|   | 202.0 | -0.102 |
|   | 1.5   |        |
|   | 1.0   | 0.05   |
|   | 0.5   |        |
|   | 0.0   | 0.00   |

Fig. 4 | Decrease in particle size. a Schematic of non-equilibrium flame process and entropic effects on decreasing particle size; b Average particle size of wet-impregnation synthesized Pd on MCM-41 mesoporous silica (Pd/MCM-41) prepared in the liquid phase, flame-synthesized Pd on in-situ formed mesoporous silica (Pd/F-SiO2), and flame-synthesized HEA on in-situ formed mesoporous silica (HEA/F-SiO2), at varied metal:SiO2 ratio of 1 ~ 50 wt.%, The insert TEM comes from the nanoparticles. Meanwhile, the fast material formation process followed by rapid quenching can dramatically limit the particle aggregation and coalescence observed in equilibrium synthesis methods, aiding in controlling the final nanoparticle size and uniformity.

In our non-equilibrium flame aerosol method, we further observed that the HEA/F-SiO₂ exhibited even smaller particle size, i.e., better dispersion than Pd/F-SiO₂. As the HEA:SiO₂ ratio increased from 1 wt.% to 50 wt.%, the average size of HEA nanoparticles only increased from 2.66 nm to 4.62 nm (Fig. 4b, Supplementary Fig. 32). The 50 wt.% HEA/F-SiO₂ still retained highly dispersed nanoparticles and narrow size distribution (Supplementary Fig. 33), suggesting a role of the HEA composition in decreasing the particle size.

To explain this phenomenon, first-principles calculations based on Density Functional Theory (DFT) were conducted to investigate the formation of HEA nanoparticles. For modeling equimolar quinary HEA systems, we generated a 125-atom Special Quasi-random Structure (SQS) by optimizing near-neighbor pair and many-body correlation functions through a Monte Carlo search approach⁵⁹. The SQS was fully relaxed, and surface energies for three (111) terminations were calculated using a slab concentration gradient perpendicular to the solid-liquid interface⁶⁰. In a concentrated multi-component solution, a sufficient concentration gradient is difficult to sustain for all constituent elements, limiting the size that HEA nanoparticles can grow.

Based on the Classical growth model, this condition limits the size during HEA nanoparticle growth, rcrit = — Δγ, where γ represents the surface energy, and ΔGv is the bulk Gibbs energy change during nucleation. The PdOsIrPtAu system exhibited a low average (111) surface energy of 1.35 J/m², compared to the weighted average (111) surface energy of the constituent pure metals (1.68 J/m²). However, this system showed a high bulk enthalpy of mixing of 0.19 eV/atom. In contrast, the RuRhPdIrPt system had a similar surface energy (1.96 J/m²) to the weighted average for pure metal surfaces but displayed a much lower bulk enthalpy of mixing (0.02 eV/atom). At a synthesis temperature of 800 °C, the configurational entropy contribution for the Gibbs energy of a random equimolar quinary system was calculated as 0.14 eV/atom (kB Tlnn with n = 5). This high configurational entropy significantly reduces the bulk Gibbs energy and thus lowers the critical nucleation radius for both systems, increasing the nucleation rate for HEA nanoparticles relative to single-component nanoparticles.

Following nucleation, classical growth theory suggests the growth of HEA nanoparticles requires the transport of constituent elements to the nanoparticle surface via a concentration gradient perpendicular to the solid-liquid interface. In a concentrated multi-component solution, a sufficient concentration gradient is difficult to sustain for all constituent elements, limiting the size that HEA nanoparticles can grow.

| 7 Nature Communications (2026) 17:6314





Article                                                                                                       https://doi.org/10.1038/s41467-026-72958-9

resulting in similar nanoparticle sizes and narrow size distribution as multiple M-O bonds in pure M metals, while there is only one M-O bond observed in our experiments⁶⁰. This observation is consistent with our previous report on high-entropy ceramic oxides, where increasing the configurational entropy of the solid solution induced a transition from long-range to short-range order, thereby reducing crystallinity and grain size⁶¹.

Similarly, a recent report also described the preparation of high-density, highly dispersed HEA nanoparticles on carbon supports by a spray drying aerosol process²³. Supplementary Table 6 summarizes reports on the preparation of HEA nanoparticles using combustion or pyrolysis processes. As can be seen there, both the spray drying aerosol method and our flame aerosol method have clear advantages in HEA loading and density. The spray aerosol method has achieved finer particle sizes. Our method, however, allows for a broader range of support materials than has been demonstrated for spray drying, especially for the HEA embedded in mesoporous silica, offering advantages in stability and loading. Additionally, our method provides an in-situ reduction environment that promotes metal reduction (even with high oxidation potential) to a certain extent.

In addition, we adopted another DFT calculation to investigate the Gibbs free energies for the reduction of W/Zr/Ce oxide clusters in vacuum and HEA surface cases. The results showed that ΔG of the reduction reactions changing from 0.15 eV under vacuum condition to −0.5 ± 0.3 eV on HEA (111) surface for W, from 2.38 eV to −1.0 ± 0.3 eV for Ce, and from 1.76 eV to −1.3 ± 0.3 eV for Zr (Supplementary Table 10), confirming the effect of HEA in promoting metal reduction.

# Reduction of high oxidation potential elements

Reduction-based alloying methods are often constrained by the oxidation potential of the metal elements, resulting in phase separation between metallic and oxidized elements. To this point, we have shown that the current flame aerosol process can directly reduce noble metals, including Ru, Rh, Pd, Os, Ir, Pt, Au, and Ag⁶², which have low oxidation potential in the Ellingham diagram⁶³. Meanwhile, a recent study suggests that through thermodynamic design, the mixture of metal oxides can be directly reduced into bulk alloys by H₂ in one step⁶⁴. Here, in the nanoscale alloying process, we address the role of RuRhPdIrPt HEA in the reduction and incorporation of metals with moderate to strongly negative redox potentials that otherwise would be challenging to produce as metals in conventional reduction-based alloying methods (Fig. 5a).

The entropic stabilization effect favors this reduction⁴, where the increase in system configurational entropy promotes the alloying of multiple elements in a single FCC metallic phase, along with a catalytic role of the HEA nanoparticles for breaking M-O bonds at high temperatures.

First, to theoretically investigate the catalytic reactivity of the HEA, we performed DFT calculations of oxygen desorption energies as an indicator of M-O bond strength (Fig. 5b). Here, the M-O bond is between oxygen and a metal with moderate to strongly negative oxidation potential. We considered a FCC (111) surface of the RuRhPdIrPt HEA with full coverage of oxygen in the FCC “hollow” sites⁶⁵, and substituted one of the surface atoms with a M atom (M = W, Ce, or Zr). A decrease in the crystallinity of the RuRhPdIrPtW HEA was also evident (Supplementary Fig. 37), but without a significant change in lattice parameters. We attribute this phenomenon to the physicochemical property differences between W and other elements.

For the nanoparticles observed in RuRhPdIrPtW HEA samples, the elemental maps of W, like the other elements, showed homogeneous distribution throughout the particle, indicating W was successfully incorporated into the alloy lattice (Supplementary Fig. 40). However, the FCC lattice of RuRhPdIrPtW HEA nanoparticles (Fig. 5e, Supplementary Fig. 39) showed significant lattice distortion compared to RuRhPdIrPt (Fig. 1b). Specifically, we captured a particle with a significant number of defects (Supplementary Fig. 40). This particle contains a large internal cavity and is likely in an intermediate state between a nanoparticle and a nanocluster, on the verge of splitting.

While the total oxygen desorption energies are indeed lowest in the HEA case, this does not necessarily indicate a weakening of the M-O bonds (M = W, Ce, Zr), because oxygen desorption requires breaking bonds. This further demonstrates that under non-equilibrium reaction conditions, immiscible elements play a key role in disrupting the alloy nanoparticle growth.

|     8
Nature Communications (2026) 17:6314



Article    https://doi.org/10.1038/s41467-026-72958-9

Low oxidation potential                    Medium oxidation potential    High oxidation potential

|             | b            | e             | Single-atoms           |
| ----------- | ------------ | ------------- | ---------------------- |
| M surface   |              | (111), 2.30 A | desorption             |
| HEA surface |              |               | Nanoclusters           |
|             | 2 nm         | 5 nm          |                        |
| c           | HEA surface  | d W surface   | HEA surface Ce surface |
| 6           | 6            | 20            | 5                      |
| 2           | 37           | 0.6           |                        |
| 0           | 1.8          |               |                        |
| Total       | Per M-O bond | Total         | Per M-O bond           |
| b           | Ru           | Rh            | Pd                     |
|             | Ni           | Cu            | W                      |
|             | 5 nm         | 5 nm          | 5 nm                   |
|             | 5 nm         | 5 nm          | 5 nm                   |

Fig. 5 | Extension of HEA compositional space. a Schematic of entropy-driven incorporation of metals with increased oxidation potential; b DFT calculation of O atom desorption energy; c O desorption energy from HEA and W surface; d O desorption energy from HEA and Ce surface. The error bars represent the standard deviation of the desorption energy; e AC-STEM images of RuRhPdIrPtW/carbon after post-treatment in H2 at 900 °C for 6 h; g HAADF-STEM elemental maps of a representative 10-element HEA/carbon; h Ni K-edge EXAFS spectra, i Pd K-edge EXAFS spectra, and j Pt L3-edge EXAFS spectra of the 10-elements HEA/carbon. Source data for c, d, h–j are provided in the Source Data file.

alloy lattice and promoting the formation of more highly dispersed species. A possible reason is that, during the non-equilibrium process, rapid particle formation prevents immiscible elements from diffusing slowly to achieve phase separation to form highly crystalline, thermodynamically stable nanoparticles. Due to significant differences in atomic radius and electronegativity, the immiscible component disrupts the orderly arrangement of metal atoms, inhibiting lattice formation, causing lattice distortion and defects, and promoting the generation of more dispersed species, such as nanoclusters, amorphous particles, or even single atoms. We note that, in many reactions, these highly dispersed active sites have shown high catalytic activity⁷¹.

Specifically, using low-melting-point metals (such as Ga) is an effective approach to reducing the system’s mixing enthalpy and facilitating HEA formation. However, during the HEA formation process, the surrounding metal elements tend to coalesce into Ga, leading to the formation of large particles (20–100 nm)²¹. In contrast, the non-equilibrium method employed in this study suppresses the diffusion process. As an immiscible element, low-melting-point Ga not only avoids particle growth but, similar to W, it plays a role in inhibiting particle growth and even reducing particle size (Supplementary Fig. 45).

Furthermore, the flame aerosol process failed to directly reduce ceramic component elements with much lower oxidation potential in the Ellingham diagram, such as Ce, La, Mg, and Zr. However, according to ΔG ΔH – •Δ •Δ, the increased value of T S at elevated temperatures could further decrease Gibbs energy, so we adopted an H₂ heating post-treatment (800 ~ 1000 °C) to reduce and incorporate ceramic elements in HEA nanoparticles (Fig. 5a). Taking Ce as an example, the flame-synthesized RuRhPdIrPt-CeO₂/carbon was heated in H₂ at 900 °C for 6 h. The post-reduced RuRhPdIrPtCe/carbon adopted a single-phase metallic FCC structure (Supplementary Fig. 46), and the FCC crystal lattice was further confirmed by AC-STEM.

|     9 Nature Communications (2026) 17:6314



Article                                                                                                         https://doi.org/10.1038/s41467-026-72958-9

(Fig. 5f). The slight deviations in lattice parameters from RuRhPdIrPt            enhanced configurational entropy in alloy nanoparticles provides structural stability in acid, alkaline, or high-temperature reaction conditions6,7,¹². For example, alkaline hydrogen oxidation reaction (HOR) is one critical half-cell reaction for anion exchange membrane fuel cell applications. Unfortunately, the HOR in alkaline electrolyte suffers from sluggish kinetics due to strong hydrogen binding energy (HBE) and the participation of multiple reaction intermediates, i.e. *H, *OH and *H₂O⁷². Introducing oxyphilic elements in Pt, such as RuPt, has been identified as an efficient approach to accelerate the oxidation of *H and promote the reaction kinetics⁷⁹,⁸⁰. Further engineering the catalyst structure with multiple adsorption will be promising for further enhancing the HOR activity. Here, as an example, the flame aerosol synthesized RuPdOsIrPt/graphene high-entropy nanoparticles were employed as a hydrogen oxidation reaction (HOR)⁸¹ catalyst in an alkaline electrolyte (Fig. 6a). The optimized high-entropy catalyst showed single-phase FCC crystalline, highly dispersed HEA nanoparticles with average diameter of 2.48 ± 0.51 nm, and composition molar ratio of Ru:Pd:Os:Ir:Pt=1.09:1.48:1.00:1.50:1.93 (Supplementary Fig. 59, Supplementary Table 12). Commercial RuPt/carbon (TKK) catalyst (Supplementary Fig. 60) and graphene supported mono-metallic metal catalysts synthesized at the same conditions were used as references.

The entropy-induced reduction mechanism enabled mixing more elements in the HEA nanoparticles. For example, a 10-element RuRhPdIrPtFeCoNiCuW/carbon was successfully fabricated (Supplementary Fig. 53). The HAADF-STEM element maps revealed the homogeneous mixing of all 10 constituent elements within the nanoparticles (Fig. 5g). The bonding structures of the 10-element HEA was measured using X-ray absorption spectroscopy (XAS), in which the Ni, Pd, and Pt elements from the 3rd, 4th, and 5th periods were selected for investigation. In their X-ray absorption near edge structure (XANES) spectra, the significantly lower white-line intensity compared to their oxides confirmed the high occupancy of their d orbitals (Supplementary Figs. 54-56), and the Fourier-transformed extended X-ray absorption fine structure (EXAFS) (Fig. 5h) spectra indicated 14% higher than commercial RuPt/Carbon suggesting faster HOR kinetics on the HEA catalyst. In addition, we further calculated the kinetic mass activity at an overpotential of 50 mV (Fig. 6e). The HEA catalyst reveals the highest mass activity of 4.3 ± 0.15 A mgPGM⁻¹, which is about 7.2, 30, and 2.1 times higher than those of Pt/graphene (0.65 A mgPGM⁻¹), Ir/graphene (0.15 A mgPGM⁻¹), and commercial RuPt/carbon (2.05 A mgPGM⁻¹), respectively.

Moreover, we studied the stability of the HEA catalyst and commercial RuPt/carbon catalyst by accelerated stress tests (ASTs, cycling between -0.1 to 0.4 V for 10000 cycles) (Fig. 6e). The RuPdOsIrPt/graphene shows good stability. After 10000 AST cycles, the ECSA loss was only 13% (from 28.3 to 24.7 m² gPGM⁻¹, Supplementary Fig. 64a). In contrast, the commercial RuPt/Carbon lost 48% of the ECSA (from 39 to 20.4 m² gPGM⁻¹, Supplementary Fig. 64b). The HEA catalyst showed negligible changes in the HOR polarization curve. After 10000 cycles, only 1.5 mV loss in E1/2 was observed, demonstrating the stability of the HEA catalyst. In contrast, the commercial RuPt/Carbon showed obvious activity decay after 10,000 cycles (Fig. 6f). To be more quantitative, we calculated the change in exchange current density and mass activity before and after the stability test. The HEA catalyst retained 91% and 81% of the exchange current density and mass activity (Fig. 6g), respectively, outperforming the commercial RuPt/Carbon (46% in exchange current density and 14% in mass activity).

In recent years, HEA nanomaterials have shown significant advantages in high-performance catalyst design⁷⁶. Their compositional diversity enables fine-tuning of catalytic activity and selectivity, and the local structures of both RuPdOsIrPt and commercial RuPt catalysts were investigated using EXAFS.

|     10 Nature Communications (2026) 17:6314




Article                                                                                                                https://doi.org/10.1038/s41467-026-72958-9

# Fig. 6

Catalytic application in hydrogen oxidation reaction (HOR).

|                                                                                                                                                                        | a Illustration of the advantages of RuPdOsIrPt/graphene high-entropy catalyst;               | b 98% iR-corrected polarization curves (electrode area = 0.196 cm²); |                                                                                        |   |   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | - | - |
|                                                                                                                                                                        |                                                                                              |                                                                      | c Tafel plots;                                                                         |   |   |
| d normalized mass activity and exchange current density of the studied catalysts;                                                                                      | e HOR polarization curves of RuPdOsIrPt/graphene high-entropy catalyst before and after AST; |                                                                      |                                                                                        |   |   |
|                                                                                                                                                                        |                                                                                              | f HOR polarization curves of commercial RuPt/Carbon                  | g Normalized mass activity and exchange current density before and after 10000 cycles. |   |   |
| The resistance in 0.1 M KOH was measured to be \~46.3 ± 2.4 Ω. The pH is about 12.9 ± 0.1. The error bars are the standard deviation from three separate measurements. |                                                                                              |                                                                      |                                                                                        |   |   |

Source data for b-g are provided in the Source Data file.

# Fig. 7

The main peaks at ~ 2.5 Å are assigned to metallic Ru-Ru or Ru-M scattering. Notably, in the RuPdOsIrPt catalyst, these Ru-M peaks appeared significantly broader and partially split compared to those in the commercial RuPt, indicating pronounced local lattice deformation induced by the high-entropy configuration. In high-entropy systems, such lattice distortions arise from size and electronic mismatches among constituent elements, manifesting as uneven coordination environments, strain-induced shifts in the d-band center, and broken local symmetry. These structural irregularities generate a diverse distribution of local electronic states and multiple non-equivalent metal–metal bond lengths, resulting in a quasi-continuous adsorption energy landscape. This, in turn, promotes the co-adsorption and activation of key HOR intermediates (*H, *OH, and *H₂O) on the catalyst surface.

Furthermore, symmetry breaking introduces a greater variety of interfacial sites (e.g., Ru–Os, Pt–Ir), thereby increasing the density of catalytically active centers and contributing to the high performance of the HEA catalyst under alkaline conditions. Specifically, the Ru-M bond lengths of the RuPdOsIrPt catalyst became longer (2.689-2.701 Å) than those of the RuPt catalyst (2.668-2.699 Å). In general, elongated metal-metal bonds reduce orbital overlap, leading to a narrower d-band width and an upshift of the d-band center. This electronic modulation enhances the adsorption strength of reaction intermediates.

In contrast, Ru, Os, and Pt show significant overlaps between d-orbitals of different metal elements, indicating their enhanced electron delocalization and strong bonding. Specifically, the Pd 4d and Pt 5d states are primarily located below the Fermi level, indicating their roles as electron-donor sites favorable for *H adsorption.

Nature Communications (2026) 17:6314




Article    https://doi.org/10.1038/s41467-026-72958-9

# Fig. 7 | Catalysis mechanism analysis.

a k³-weight FT-EXAFS spectra of the RuPt and *H2O on RuPt or RuPdOsIrPt surface.

b Ru-M bond length and Ru-O coordinate pathway on RuPt or RuPdOsIrPt surfaces.

c Site-dependent PDOS of the RuPdOsIrPt HEA model.

d Adsorption energies of *H, *OH and Ir exhibit broader band structures with substantial DOS above the Fermi level, serving as electron-acceptor sites conducive to *OH adsorption.

e Free energy diagrams of the HOR and RuPdOsIrPt catalysts in R-space.

Source data for a-e are provided in the Source Data file.

More importantly, the HEA displayed a stronger OHBE and weaker H₂O binding energy (H₂OBE) compared to RuPt. The stronger *OH adsorption promotes the removal of surface-bound protons, while the weaker *H₂O adsorption facilitates its desorption, both of which are crucial for accelerating the alkaline HOR. Additionally, we calculated reaction free energy diagrams for HOR on both RuPt and RuPdOsIrPt surfaces (Fig. 7e). The results identify the adsorption of *OH would be the (rate-determining step) RDS for HOR.

Thanks to the enhanced OHBE and weakened H₂OBE on the RuPdOsIrPt surfaces, the adsorption of *OH and formation of water becomes more favorable. The RuPdOsIrPt surface achieves a low RDS energy barrier of 0.16 eV, lower than RuPt surface (0.19 eV), further confirming the high HOR activity of HEA to PtRu. Taken together, the combination of diverse active sites, tailored electronic structure, and optimized intermediate binding energies could explain the high HOR.

|     12 Nature Communications (2026) 17:6314




Article                                                                                                      https://doi.org/10.1038/s41467-026-72958-9

activity of the RuPdOsIrPt HEA catalyst relative to the conventional PtRu system. Moreover, after HOR operation, although XPS analysis did not reveal significant changes in the oxidation states of Ru and Pt in either catalyst (Supplementary Figs. 69, 70), the decreased stability of the commercial RuPt was associated with substantial particle agglomeration and sintering (evident in TEM imaging, Supplementary Figs. 71, 72) and metal dissolution (as confirmed by XRF in Supplementary Fig. 73). These degradative changes are also consistent with the observed decline in ECSA, showing a 48% loss for the RuPt catalyst compared to only a 13% loss for the RuPdOsIrPt HEA catalyst. This enhanced structural robustness in the HEA catalyst aligns with our previous study in high-entropy oxides¹³, and can be attributed to the entropy stabilization effect⁴. This effect suppresses phase segregation and reduces atomic diffusivities, thereby slowing or preventing aggregation and sintering.

# Discussion

This research establishes a versatile flame aerosol methodology to produce supported HEA nanoparticles. The non-equilibrium reaction kinetics and entropy-driven alloying provide flexibility in both support materials and HEA composition, enabling rational material design across an enormous composition space for target applications. The produced HEA nanomaterials demonstrate many fascinating characteristics, such as high nanoparticle dispersion, atomic homogeneity of multi-element mixing, and enhanced catalytic performance, which are promising for use in energy and electronic fields. Meanwhile, the one-step, continuous, and scalable nature of the flame aerosol process makes it ideal for industrial production, paving the way to large-scale development and application of HEA nanomaterials.

# Methods

# Chemicals

RuCl₃•H₂O (35-40% Ru, Thermo Scientific), RhCl₃•H₂O (38 wt.% Rh, Thermo Scientific), PdCl₂ (59.5% Pd, Thermo Scientific), IrCl₃•3H₂O (53-56 % Ir, Thermo Scientific), PtCl₄ (99%, Acros Organics), OsCl₃•3H₂O (52-56% Os, Thermo Scientific), AuCl₃ (99%, Thermo Scientific), FeCl₂•4H₂O (99%, Acros Organics), CoCl₂•6H₂O (98%, Thermo Scientific), NiCl₂ (98%, Thermo Scientific), CuCl₂•2H₂O (98%, Thermo Scientific), ZnCl₂ (98%, Thermo Scientific), Ammonium tungsten oxide (NH₄)₆H₂W₁₂O₄₀•H₂O (99.9%, Thermo Scientific), Ga(NO₃)₃•H₂O (99.9%, Thermo Scientific), Ce(NO₃)₃•6H₂O (99.5%, Acros Organics), La(NO₃)₃•6H₂O (98 + %, Acros Organics), Mg(NO₃)₂•6H₂O (99 + %, Acros Organics), ZrCl₄ (99.5%, Alfa Aesar), sodium dodecyl sulfate (SDS, 99%, Acros Organics), tetraethyl orthosilicate (TEOS, 98%, Thermo Scientific), hexadecyltrimethylammonium bromide (CTAB, 99 + %, Acros Organics), HCl (37%, Acros Organics), and ethanol (200 proof, Decon Labs).

# Support materials

Carbon substrate was purchased from fuel cell store (Ketjenblack 300, #NC 9849314); TiO₂ nanocrystal substrate was purchased from Sigma-Aldrich (anatase, nanopowder &#x3C;25 nm, #637254-50 G); Carbon nanotube substrate was purchased from Cheap Tubes (8-15 nm outer diameter, #03040302); Graphene substrate was provided by HydroGraph (fractal dimension D = 2.5 ± 0.1, #RGA-COOH-1); UiO-66 MOF substrate was synthesized via the following procedures based on a previous study⁸⁸: 0.6 mmol of 1,4-benzenedicarboxylic acid (BDC, 99%, Thermo Scientific) and 1.2 mmol of triethylamine (TEA, Thermo Scientific) were dissolved in 140 mL of N,N-dimethylformamide (DMF, 99.8%, Fisher Chemical), and 20.62 mL of acetic acid (99.7%, Thermo Scientific) was added. The mixture was stirred at 24 °C room temperature for 10 minutes. Then, 0.6 mmol of ZrCl₄ was dissolved in 10 mL of DMF and added to the previous solution. The reaction precursor was kept at 120 °C for 6 h to grow the MOF.

# Material characterizations

High-angle annular dark-field scanning transmission electron microscopy (HAADF-STEM) imaging with elemental mapping by energy dispersive x-ray spectroscopy (EDS), and live fast-Fourier-transform (FFT) patterns were obtained using a JEOL 2100-F 200 kV field-emission analytical transmission electron microscope; Aberration.

|     13 Nature Communications (2026) 17:6314




Article                                                                                                       https://doi.org/10.1038/s41467-026-72958-9

corrected scanning transmission electron microscopy (AC-STEM) was carried out on a JEOL JEM-ARM200F thermal-field emission microscope with a probe spherical aberration (Cs) corrector working at 200 kV. A JEOL JEM 2010 Transmission Electron Microscope (TEM) was also used to observe the materials. The particle size distribution curve was obtained by statistically analyzing 100 HEA nanoparticles dispersed on different substrate grains. A Cross-Beam Focused Ion Beam-Scanning Electron Microscopy (FIB-SEM) Workstation (Carl Zeiss AURIGA) also was used to observe the morphology of substrates; X-ray diffraction (XRD) patterns were acquired using an X-ray diffractometer (Rigaku Ultima IV) with Cu Kα source (λ = 0.15418 nm). The diffractometer was operated at 40 mA and 40 kV at a scanning rate of 2°/min; The ex-situ X-ray absorption spectroscopy (XAS) spectra were collected at 8-ID beamline (Inner Shell Spectroscopy) of Brookhaven Lab’s National Synchrotron Light Source II. X-ray photoelectron spectroscopy (XPS, Thermo Fisher K-Alpha Plus) measurements were conducted to analyze the surface metal state, with surface etching time of 0 s, 120 s, and 240 s, respectively. The photoelectron spectrometer system was configured with an Al Kα excitation source with spot size of 400 μm; The inductively coupled plasma optical emission spectrometer (ICP-OES, Thermo Scientific iCAP 6000) and X-ray fluorescence (XRF, Epsilon 1, Malvern Panalytical) were used to measure the HEA elemental composition; N₂ physisorption measurements (Micromeritics Tri-Star II) were used to characterize surface area and pore structure of the materials. Reported specific surface area was calculated based on the Brunauer-Emmett-Teller (BET) method, and the pore size distribution were calculated by the Barrett-Joyner-Halenda (BJH) or Horvath-Kawazoe methods based on the isotherms; Fourier transform infrared (FTIR) spectra was collected using a Bruker Vertex 70 Spectrometer; Raman spectra were measured by a Renishaw In Via spectrometer with 514 nm excitation laser focused through a 20× microscope objective; H₂ temperature programmed reduction (H₂-TPR) was conducted using an Auto Chem II 2920 apparatus (Micromeritics) with 10% H₂ in Ar and a flow rate of 50 mL/min. The material was heated up to 850 °C with a 10 °C/min ramp rate.

# DFT calculations

Calculations of surface energy and O desorption were performed using the Vienna Ab initio Simulation Package (VASP). The PBE exchange correlation functional was used, with a plane wave energy cutoff of 520 eV. The O, Ir, Pd, Pt, Au, Os pv, Rh pv, Ru pv, Zr sv, W sv, and Ce projector augmented wave (PAW) pseudopotentials were chosen. All calculations were spin-polarized, with magnetic moments initialized ferromagnetically. Relaxations were performed with a force convergence criterion of 0.02 eV/Å and final static calculations were run with the linear tetrahedron method enabled to obtain accurate energies. Γ-centered Monkhorst-Pack k-point meshes were used to sample the Brillouin zone. Bulk metal and HEA structures were fully relaxed to obtain their equilibrium lattice parameters, which were then used to construct surface slabs with vacuum gaps of at least 10 Å. For the HEA case, a 125-atom special quasirandom structure (SQS) of bulk RuRhPdIrPt and PdPtIrOsAu consisting of five FCC (111) layers was generated using the Alloy Theoretic Automated Toolkit (ATAT). For surface energy calculations, three different (111) surfaces were calculated for each HEA. For O adsorption calculations, this was then cleaved to construct a five-layer slab exposing a surface layer with a near-equiatomic composition of Ir₄Pd₅Pt₅Rh₅Ru₆. For the bulk metal relaxations, k-meshes were automatically generated with a density of 30 Å along each reciprocal lattice vector, while for the HEA structure, a 2 × 2 × 2 mesh was used. Details of the surface slab structures are provided in Additional Supplementary Files. After applying a full coverage of O atoms to one surface (and, in the HEA case, substituting one of the surface metal sites), the ions were relaxed before and after removing a single O atom to obtain the O desorption energy, given by Edes = Eslab— O + EO — Eslab, where Eslab and Eslab—O are the energies.

To compute reaction energies, the energies of each reactant/product were calculated from DFT. We used the same HEA surface structures used in our desorption calculations (excluding the oxygen layer), with a vacuum gap of at least 15 Å. For each element, all 25 HEA surface sites were sampled for substitution to obtain an average defect/reaction energy. Metal oxide cluster structures were obtained from literature. Cubic boxes of side length 25 Å and 15 Å were used for relaxations of the metal oxide clusters and H₂/H₂O, respectively. All settings from our desorption calculations were maintained, except that a DFT-D3 van der Waals correction was used in combination with the PBE functional. For the molecules, vibrational modes were calculated using finite (central) differences without symmetry, as implemented in VASP.

To account for finite temperature vibrational effects, we calculated Gibbs free energies at T= 800 °C = 1073.15 K. For the molecules we used:

G = EDFT + EZP + Hvib, T — TSvib, T

where EZP, Hvib, T, Svib, T are the zero-point energy, vibrational enthalpy, and vibrational entropy at temperature T obtained from the calculated vibrational modes using post-processing tools in VASPKIT. For the bulk metals we used:

G = EDFT + HT — H0 — TS

where HT — H0 and ST are the enthalpy (relative to T= 0) and entropy obtained from available thermodynamic data (linearly interpolating between data at 1000 K and 1100 K when necessary). No finite temperature term was added to the HEA surface energies, since these appear on opposite sides of the reduction reaction and should therefore cancel if we assume the entropy difference from substituting a single surface atom to be negligible.

In addition, we investigated the HOR catalytic reaction. The adsorption energies of *H, *OH, and *H₂O on the (111) surface of the high-entropy alloy (HEA) and a reference PtRu alloy were calculated using four-layer surface slabs constructed from representative 64-atom SQSs. The lateral lattice constants were fixed to the equilibrium bulk values of each SQS. A vacuum space of 15 Å was introduced to avoid interactions between periodic images. The adsorbates were initially placed at their most stable sites, namely FCC hollow for *H, and atop for *OH and *H₂O, as determined from preliminary site tests. Adsorption was evaluated independently on both the top and bottom.

|     14
Nature Communications (2026) 17:6314




Article                                                                                                                                 https://doi.org/10.1038/s41467-026-72958-9

slab surfaces to sample diverse local environments. During structural optimization, the bottom slab layer was fixed, while the top three layers and all adsorbates were fully relaxed. Free energy diagrams for HOR were then constructed by averaging the adsorption energies over all non-equivalent configurations across the two surfaces.

# Electrochemical measurements

Electrochemical measurements were performed using a CHI 760e potentialstat. A PTFE container (100 mL) was used as the electrochemical cell to avoid the possible corrosion of a glass cell. A glassy carbon rotating disk electrode (5 mm in diameter), a saturated calomel electrode (SCE, saturated KCl), and a graphite rod were employed as the working electrode, the reference electrode, and the counter electrode, respectively. All potentials were converted to values with reference to a reversible hydrogen electrode (vs. RHE). The calibration was performed in H₂-saturated 0.1 M KOH using PtRu/C as a working electrode, and the potential at 0 mA cm−² was used to convert SCE to RHE potential.

The 0.1 M KOH solution was prepared by dissolving 5.6 g KOH in 1.0 L DI water, and the prepared electrolyte was stored in a plastic container. The pH is about 12.9 ± 0.1.

Catalyst ink was prepared by dispersing the electrocatalysts in a mixture of isopropanol and Nafion (5%) (v/v = 1:0.01, 2 mgcatal mL⁻¹) by sonication. 10 μL of ink was cast on the working electrode and dried under ambient conditions. The final PGM loadings were determined by ICP-OES ( ~ 10 μgPGM cm−²).

PGM loading (mg cm—2) = 2mgml—1 * wPGM * 0.01 mL  (5)  0:196 cm—2

Where wPGM is the PGM loading in the catalyst obtained by ICP-OES. The ECSA value is calculated as shown below:

ECSA (m²/g) = 0.21 mCcm—2 * PGM loading (mg) * 10 (6)

Where QHUPD is the hydrogen desorption charge obtained by integrating the area in CVs.

All of the measurements were carried out at 24 °C room temperature. The catalysts were activated by performing cyclic voltammetry (CV) in N₂-saturated 0.1 M KOH solutions (50 mL) at a scan rate of 200 mV/s between 0-1.0 V (vs. RHE). The HOR measurements were carried out with a rotating disk electrode (RDE) in H₂-saturated 0.1 M KOH at a rotation speed of 1600 rpm and a sweep rate of 10 mV s−¹. Kinetic currents were calculated using the Koutecky-Levich equation:

i k = ii l * i 0:05 (7) l — i₀:₀₅

Where ik is the kinetic current, il limited current and i0:05 current at 0.05 V after iR-correction.

Exchange current density J₀ was calculated from the Butler-Volmer equation:

J = J₀ h eηαF — eη (1—α)F i (8) k 0 RT

Where α, R, T, η represent the transfer coefficient, the universal gas constant (8.314 J mol−¹ K−¹), the operating temperature (297 K in this work), and the overpotential, respectively.

Accelerated durability test was performed at 24 °C room temperature by potential cycles between -0.1 and 0.4 V in H₂-saturated 0.1 M KOH at a scan rate of 100 mV/s.

The resistance of the electrochemical cell was evaluated by the iR compensation (98%) on a CHI 760e potentialstat, where the resistance values in 0.1 M KOH are ~ 46.3 ± 2.4 Ω.

# Data availability

The data that support the findings and conclusions generated in this study are provided in the main article and the Supplementary Information. The calculation information is provided in the Supplementary Data 1 file. Source data are provided with this paper.

# References

1. Yeh, J. W. et al. Nanostructured high-entropy alloys with multiple principal elements: novel alloy design concepts and outcomes. Adv. Eng. Mater. 6, 299–303 (2004).
2. Cantor, B., Chang, I. T. H., Knight, P. &#x26; Vincent, A. J. B. Microstructural development in equiatomic multicomponent alloys. Mater. Sci. Eng. A Struct. Mater. Prop. Microstruct. Process. 375, 213–218 (2004).
3. George, E. P., Raabe, D. &#x26; Ritchie, R. O. High-entropy alloys. Nat. Rev. Mater. 4, 515–534 (2019).
4. Hsu, W. L., Tsai, C. W., Yeh, A. C. &#x26; Yeh, J. W. Clarifying the four core effects of high-entropy materials. Nat. Rev. Chem. 8, 471–485 (2024).
5. Schweidler, S. et al. High-entropy materials for energy and electronic applications. Nat. Rev. Mater. 9, 266–281 (2024).
6. Yao, Y. et al. High-entropy nanoparticles: synthesis-structure-property relationships and data-driven discovery. Science 376, eabn3103 (2022).
7. Li, M. et al. High-entropy alloy electrocatalysts go to (sub-) nanoscale. Sci. Adv. 10, eadn2877 (2024).
8. Zeng, Y. et al. High-entropy mechanism to boost ionic conductivity. Science 378, 1320–1324 (2022).
9. Jiang, B. B. et al. High-entropy-stabilized chalcogenides with high thermoelectric performance. Science 371, 830-+ (2021).
10. Kozelj, P. et al. Discovery of a superconducting high-entropy alloy. Phys. Rev. Lett. 113, 107001 (2014).
11. Mondal, B. et al. A resistance-driven H₂ gas sensor: high-entropy alloy nanoparticles decorated 2D MoS₂. Nanoscale 15, 17097–17104 (2023).
12. Loffler, T., Ludwig, A., Rossmeisl, J. &#x26; Schuhmann, W. What makes high-entropy alloys exceptional electrocatalysts? Angew. Chem. Int. Ed. 60, 26894–26903 (2021).
13. Liu, S. et al. A general flame aerosol route to high-entropy nano-ceramics. Matter 7, 3994–4013 (2024).
14. Gludovatz, B. et al. A fracture-resistant high-entropy alloy for cryogenic applications. Science 345, 1153–1158 (2014).
15. Kar, N. &#x26; Skrabalak, S. E. Synthetic methods for high-entropy nanomaterials. Nat. Rev. Mater. 10, 638–653 (2025).
16. Feng, G. et al. Sub-2 nm ultrasmall high-entropy alloy nanoparticles for extremely superior electrocatalytic hydrogen evolution. J. Am. Chem. Soc. 143, 17117–17127 (2021).
17. Minamihara, H. et al. Continuous-flow reactor synthesis for homogeneous 1 nm-sized extremely small high-entropy alloy nanoparticles. J. Am. Chem. Soc. 144, 11525–11529 (2022).
18. Sun, Y. et al. A general approach to high-entropy metallic nanowire electrocatalysts. Matter 6, 193–205 (2023).
19. Wei, M. et al. High-entropy alloy nanocrystal assembled by nanosheets with d-d electron interaction for hydrogen evolution reaction. Energy Environ. Sci. 16, 4009–4019 (2023).
20. Yang, C. P. et al. Overcoming immiscibility toward bimetallic catalyst library. Sci. Adv. 6, eaaz6844 (2020).
21. Cao, G. et al. Liquid metal for high-entropy alloy nanoparticles synthesis. Nature 619, 73–77 (2023).
22. Zhang, Q. et al. Isothermal solidification for high-entropy alloy synthesis. Nature 646, 323–330 (2025).
23. He, G. et al. Hydrocarbothermal flow synthesis of carbon-supported small and dense high-entropy alloy nanoparticles as electrocatalysts. Nat. Commun. 16, 8172 (2025).

| 15 Nature Communications (2026) 17:6314




Article                                                                                                     https://doi.org/10.1038/s41467-026-72958-9

1. Yao, Y. G. et al. Carbothermal shock synthesis of high-entropy-alloy nanoparticles. Science 359, 1489–1494 (2018).
2. Xie, H. et al. A stable atmospheric-pressure plasma for extreme-temperature synthesis. Nature 623, 964–971 (2023).
3. Zheng, X. et al. Hydrogen-substituted graphdiyne-assisted ultra-fast sparking synthesis of metastable nanomaterials. Nat. Nanotechnol. 18, 153–159 (2023).
4. Wang, B. et al. General synthesis of high-entropy alloy and ceramic nanoparticles in nanoseconds. Nat. Synth. 1, 138–146 (2022).
5. Ensor, D. S. Aerosol science and technology: History and reviews, (RTI Press, 2011).
6. Meierhofer, F. &#x26; Fritsching, U. Synthesis of metal oxide nanoparticles in flame sprays: review on process technology, modeling, and diagnostics. Energy Fuels 35, 5495–5537 (2021).
7. Teoh, W. Y., Amal, R. &#x26; Madler, L. Flame spray pyrolysis: an enabling technology for nanoparticles design and fabrication. Nanoscale 2, 1324–1347 (2010).
8. Liu, S., Mohammadi, M. M. &#x26; Swihart, M. T. Fundamentals and recent applications of catalyst synthesis using flame aerosol technology. Chem. Eng. J. 405, 126958 (2021).
9. Liu, S. et al. Challenging thermodynamics: combining immiscible elements in a single-phase nano-ceramic. Nat. Commun. 15, 1167 (2024).
10. Luo, L. et al. The micron-droplet-confined continuous-flow synthesis of freestanding high-entropy-alloy nanoparticles by flame spray pyrolysis. Small, 20, 2401360 (2024).
11. Phakatkar, A. H. et al. Ultrafast synthesis of high entropy oxide nanoparticles by flame spray pyrolysis. Langmuir 37, 9059–9068 (2021).
12. Rudin, T., Wegner, K. &#x26; Pratsinis, S. E. Towards carbon-free flame spray synthesis of homogeneous oxide nanoparticles from aqueous solutions. Adv. Powder Technol. 24, 632–642 (2013).
13. Schimmoeller, B., Pratsinis, S. E. &#x26; Baiker, A. Flame aerosol synthesis of metal oxide catalysts with unprecedented structural and catalytic properties. ChemCatChem 3, 1234–1256 (2011).
14. Tran-Phu, T., Daiyan, R., Ta, X. M. C., Amal, R. &#x26; Tricoli, A. From stochastic self-assembly of nanoparticles to nanostructured (photo)electrocatalysts for renewable power-to-X applications via scalable flame synthesis. Adv. Funct. Mater. 32, 2110020 (2021).
15. Koirala, R., Pratsinis, S. E. &#x26; Baiker, A. Synthesis of catalytic materials in flames: opportunities and challenges. Chem. Soc. Rev. 45, 3053–3068 (2016).
16. Deng, X., Mammen, L., Butt, H.-J. &#x26; Vollmer, D. Candle soot as a template for a transparent robust superamphiphobic coating. Science 335, 67–70 (2012).
17. Liu, Z. et al. Flame synthesis achieves compositionally tailorable high-entropy metal-containing nanomaterials. Nat. Chem. 17, 1497–1504 (2025).
18. Zhao, H., Wu, Z.-W., Li, W.-F., Xu, J.-L. &#x26; Liu, H.-F. Transition Weber number between surfactant-laden drop bag breakup and shear breakup of secondary atomization. Fuel 221, 138–143 (2018).
19. Kastengren, A. et al. Measurements of droplet size in shear-driven atomization using ultra-small angle x-ray scattering. Int. J. Multiph. Flow. 92, 131–139 (2017).
20. Eslamian, M., Ahmed, M. &#x26; Ashgriz, N. Modeling of solution droplet evaporation and particle evolution in droplet-to-particle spray methods. Dry. Technol. 27, 3–13 (2009).
21. Aamlid, S. S., Oudah, M., Rottler, J. &#x26; Hallas, A. M. Understanding the role of entropy in high entropy oxides. J. Am. Chem. Soc. 145, 5991–6006 (2023).
22. Liu, S. et al. Producing ultrastable Ni-ZrO₂ nanoshell catalysts for dry reforming of methane by flame synthesis and Ni exsolution. Chem. Catal. 2, 2262–2274 (2022).

| 16 Nature Communications (2026) 17:6314




Article                                                                                             https://doi.org/10.1038/s41467-026-72958-9

1. Tian, F. H., Liu, Z. Z., Tian, J. &#x26; Zhang, Y. F. Oxygen vacancy O-terminated surface: The most exposed surface of hexagonal WO3 (001) surface. Chin. Chem. Lett. 31, 2095–2098 (2020).
2. Pérez-Bailac, P., Lustemberg, P. G. &#x26; Ganduglia-Pirovano, M. V. Facet-dependent stability of near-surface oxygen vacancies and excess charge localization at CeO₂ surfaces. J. Phys. Condes. Matter 33, 504003 (2021).
3. Gao, L. et al. Autocatalytic surface reduction-assisted synthesis of PtW ultrathin alloy nanowires for highly efficient hydrogen evolution reaction. Adv. Energy Mater. 12, 2103943 (2022).
4. Liu, L. &#x26; Corma, A. Confining isolated atoms and clusters in crystalline porous materials for catalysis. Nat. Rev. Mater. 6, 244–263 (2020).
5. Xu, S.-L. et al. Synthesis of a Hexagonal-Phase Platinum–Lanthanide Alloy as a Durable Fuel-Cell-Cathode Catalyst. Chem. Mat. 34, 10789–10797 (2022).
6. Toher, C., Oses, C., Hicks, D. &#x26; Curtarolo, S. Unavoidable disorder and entropy in multi-component systems. npj Comput. Mater. 5, 69 (2019).
7. Yao, Y. et al. Extreme mixing in nanoscale transition metal alloys. Matter 4, 2340–2353 (2021).
8. Yao, Y. G. et al. Computationally aided, entropy-driven synthesis of highly efficient and durable multi-elemental alloy catalysts. Sci. Adv. 6, eaaz0510 (2020).
9. Sun, Y. F. &#x26; Dai, S. High-entropy materials for catalysis: a new frontier. Sci. Adv. 7, eabg1600 (2021).
10. Zhan, C. et al. Subnanometer high-entropy alloy nanowires enable remarkable hydrogen oxidation catalysis. Nat. Commun. 12, 6261 (2021).
11. Lin, F. et al. Synthesis of isolated Ru–O3 sites on hexagonal close-packed intermetallic penta-metallene for hydrogen oxidation electrocatalysis. Nat. Synth. 4, 399–409 (2025).
12. Men, Y. et al. Understanding alkaline hydrogen oxidation reaction on PdNiRuIrRh high-entropy-alloy by machine learning potential. Angew. Chem. Int. Ed. 62, e202217976 (2023).
13. Luo, H. et al. Sub-2 nm microstrained high-entropy-alloy nano-particles boost hydrogen electrocatalysis. Adv. Mater. 36, 2403674 (2024).
14. Yao, Z. C. et al. Electrocatalytic hydrogen oxidation in alkaline media: from mechanistic insights to catalyst design. ACS Nano 16, 5153–5183 (2022).
15. Li, X. et al. Element screening engineering for high-entropy alloy anodes: achieving fast and robust Li-storage with optimal working potential. Adv. Mater. 36, 2409278 (2024).
16. He, R. et al. Active site switching on high entropy phosphides as bifunctional oxygen electrocatalysts for rechargeable/robust Zn–air battery. Energy Environ. Sci. 17, 7193–7208 (2024).
17. Cao, P. et al. Breaking symmetry for better catalysis: insights into single-atom catalyst design. Chem. Soc. Rev., 54, 3848–3905 (2025).
18. Li, H., Zhao, J., Luo, L., Du, J. &#x26; Zeng, J. Symmetry-breaking sites for activating linear carbon dioxide molecules. Acc. Chem. Res. 54, 1454–1464 (2021).
19. Luo, M. &#x26; Guo, S. Strain-controlled electrocatalysis on mult-metallic nanomaterials. Nat. Rev. Mater. 2, 1–13 (2017).
20. Wang, Y. et al. Pt–Ru catalyzed hydrogen oxidation in alkaline media: oxophilic effect or electronic effect? Energy Environ. Sci. 8, 177–181 (2015).
21. Zhao, Y., Zhang, Q., Li, Y., Zhang, R. &#x26; Lu, G. Large-scale synthesis of monodisperse UiO-66 crystals with tunable sizes and missing linker defects via acid/base Co-modulation. ACS Appl. Mater. Interfaces 9, 15079–15085 (2017).
22. Kresse, G. &#x26; Hafner, J. Ab initio molecular dynamics for liquid metals. Phys. Rev. B 47, 558 (1993).

|     17
Nature Communications (2026) 17:6314




Article                                                                                            https://doi.org/10.1038/s41467-026-72958-9

112. Arblaster, J. The thermodynamic properties of ruthenium on ITS-90. Calphad 19, 339–347 (1995).

113. Arblaster, J. The thermodynamic properties of rhodium on ITS-90. Calphad 19, 357–364 (1995).

114. Arblaster, J. The thermodynamic properties of palladium on ITS-90. Calphad 19, 327–337 (1995).

115. Arblaster, J. The thermodynamic properties of iridium on ITS-90. Calphad 19, 365–372 (1995).

116. Arblaster, J. The thermodynamic properties of platinum on ITS-90. Platin. Met. Rev. 38, 119–125 (1994).

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-026-72958-9.

Correspondence and requests for materials should be addressed to Gang Wu, Jeffrey J. Urban, Mark T. Swihart or Chaochao Dun.

# Acknowledgements

A portion of the research was performed using computational resources sponsored by the Department of Energy’s Office of Critical Minerals and Energy Innovation and located at the National Laboratory of the Rockies. This work at the University at Buffalo (SUNY) was supported by the DOE Buildings Technology Office under Contract number DEEE-0008675, by the DOE National Energy Technology Laboratory under Grant number DE-FE0032209, by the U.S. National Science Foundation under Grant number CBET-1804996, and by the U.S. National Science Foundation under Grant number DMR-2427094; Work at the Molecular Foundry at Lawrence Berkeley National Laboratory was supported by the Office of Science, Office of Basic Energy Sciences of the U.S. Department of Energy (DOE) under Contract No. DE-AC02-05CH11231; This research used resources of the 8-ID (ISS) beamline of the National Synchrotron Light Source II, a U.S. Department of Energy (DOE) Office of Science User Facility operated for the DOE Office of Science by Brookhaven National Laboratory under Contract no. DE-SC0012704. The work authored by Lawrence Livermore National Laboratory was performed under the auspices of the U.S. Department of Energy (DOE) under Contract No. DE-AC52-07NA27344.

# Peer review information

Nature Communications thanks Huilong Fei, Kai Lu, Yifan Sun, and the other anonymous reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

# Reprints and permissions

Reprints and permissions information is available at http://www.nature.com/reprints.

# Publisher’s note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

# Open Access

This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

# Author contributions

S.L., M.T.S. and C.D. conceived the idea and experiments; S.L. designed all materials; S.L., K.T., K.C., and M.A.K. performed the materials synthesis; S.L., Q.J, D.W., Z.X., C.S., and C.D. performed the materials characterizations; J.L. performed the electrochemical tests and analysis; J.L.K., H.S., S.K., and W.C. performed DFT calculations and theoretical analysis; S.L. wrote the first draft of the manuscript; J.L, S.K., W.C., G.W., J.J.U., M.T.S., and C.D. revised the manuscript; S.L. and J.L. contributed equally; G.W., J.J.U., M.T.S., and C.D. jointly supervised this work.

© The Author(s) 2026

