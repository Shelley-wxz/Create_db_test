
e-ISSN 2150-5551

CN 31-2103/TB

ARTICLE https://doi.org/10.1007/s40820-026-02194-9

Nano-Micro Lett. (2026) 18:335

Received: 22 January 2026

Accepted: 16 March 2026

© The Author(s) 2026

# Entropy‑Modulated Oxide–Metal Catalyst Architectures for Direct Ammonia Protonic Ceramic Fuel Cells

# HIGHLIGHTS

- Entropy-modulated oxide–metal catalyst exsolving Ni–Fe–Cu alloy nanoparticles from a high-entropy perovskite matrix enables efficient and durable ammonia decomposition.
- Density functional theory calculations reveal that the high-entropy oxide framework facilitates cation exsolution and lowers the kinetic barriers for NH3 decomposition; additionally, the exsolved Ni–Fe–Cu alloy nanoparticles exhibit markedly higher catalytic activity than single-metal surfaces.
- Direct ammonia protonic ceramic fuel cells (DA-PCFCs) incorporating the Sr2Fe1Mo0.2Mn0.2Cr0.2Cu0.2Ni0.2O6-δ (SFMMCCN) catalyst layer achieve a record-high power density of 2.04 W cm−2 at 700 °C with stable operation for over 255 h under NH3 fuel, demonstrating the effectiveness of the entropy-modulated catalyst in designing durable and high-performance DA-PCFCs for carbon-free ammonia-to-power technologies.

# ABSTRACT

Protonic ceramic fuel cells (PCFCs) operating on NH3 present a promising carbon-free energy pathway, yet their performance is often constrained by limited catalytic activity and degradation of conventional Ni-based anodes. Here, we report a high-entropy perovskite catalyst, Sr2Fe1Mo0.2Mn0.2Cr0.2Cu0.2Ni0.2O6-δ (SFMMCCN), employed as an anode catalyst layer in direct ammonia-fed PCFCs. Upon reduction, SFMMCCN undergoes in situ exsolution of Ni–Fe–Cu alloy nanoparticles within a stable oxide matrix. This architecture provides synergistic enhancement of NH3 adsorption and decomposition through the combined effects of abundant surface acid sites and catalytically active alloy interfaces. As a result, the SFMMCCN cell achieves a record peak power density of 2.04 W cm−2 at 700 °C and demonstrates excellent operational stability for over 255 h at 600 °C under NH3 fuel. Compared to a bare cell, it exhibits significantly reduced polarization resistance and effectively suppresses Ni coarsening. Density functional theory calculations reveal that the high-entropy oxide framework, together with the exsolved Ni–Fe–Cu alloy, lowers the energy barriers for NH3 decomposition, thereby accelerating overall catalytic kinetics. These findings highlight entropy-controlled oxide–metal architectures as a powerful strategy to achieve both high performance and durability in NH3-fueled electrochemical systems, offering a viable pathway toward scalable and efficient hydrogen-based power generation.

# KEYWORDS

Protonic ceramic fuel cells (PCFCs); Ammonia; High-entropy perovskite; Anode catalyst layer; Density functional theory

Dongyeon Kim, Dong Jae Park, and Incheol Jeong contributed equally to this work.

* Ki Min Roh, kmroh@kigam.re.kr; Joongmyeon Bae, jmbae@kaist.ac.kr; Tae Ho Shin, ths@kicet.re.kr; Kang Taek Lee, leekt@kaist.ac.kr

| 1 | KAIST InnoCORE PRISM AI Center, KAIST, Daejeon, Republic of Korea                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 2 | Hydrogen Energy Materials Center, Korea Institute of Ceramic Engineering and Technology (KICET), Jinju Si, Gyeongsangnam Do, Republic of Korea |
| 3 | Department of Mechanical Engineering, KAIST, Daejeon, Republic of Korea                                                                        |
| 4 | Resources Utilization Research Center, Korea Institute of Geoscience and Mineral Resources (KIGAM), Daejeon, Republic of Korea                 |
| 5 | KAIST Graduate School of Green Growth & Sustainability, Daejeon, Republic of Korea                                                             |

Published online: 17 April 2026

Vol.:(0123456789)




Nano-Micro Lett. (2026) 18:335

# 1 Introduction

The global transition toward decarbonization and reduced reliance on fossil fuel intensified interest in hydrogen as a clean and versatile energy carrier [1]. Within this context, protonic ceramic fuel cells (PCFCs) have emerged as promising electrochemical devices that directly convert hydrogen into electricity through proton conduction, offering high efficiency and environmentally benign operation [2]. Despite these advantages, the large-scale adoption of hydrogen faces substantial challenges, including energy-intensive production pathways and limited distribution infrastructure [3]. Common delivery strategies—such as compression, liquefaction, or chemical storage in hydrides and carbonaceous compounds—remain technologically complex and economically unattractive [4].

Beyond hydrogen, carbon-based fuels such as methane and natural gas can be supplied to fuel cells, benefiting from fast kinetics and well-established distribution networks [5]. However, their utilization inevitably generates CO2 and other pollutants, which conflict with increasingly stringent environmental regulations. Ammonia (NH3) has therefore attracted considerable attention as an alternative energy carrier, due to its carbon-free composition, hydrogen-rich nature, favorable energy density, low flammability, and compatibility with existing large-scale storage and transport infrastructure [6, 7]. Leveraging these properties, direct ammonia-fed PCFCs (DA-PCFCs) operating at intermediate temperatures provide notable advantages, including higher system efficiency and reduced balance-of-plant complexity. Unlike conventional solid oxide fuel cells (SOFCs), which rely on oxygen-ion transport [8], the proton conduction mechanism of PCFCs inherently suppresses NOx formation during ammonia utilization [9]. This synergy highlights DA-PCFCs as a particularly attractive pathway for clean and scalable power generation [10]. Nevertheless, the practical realization of DA-PCFCs is hindered by inadequate catalytic activity of conventional anodes toward NH3 decomposition.

Ni-based cermet anodes, widely employed in PCFCs, show poor intrinsic activity, leading to incomplete conversion of NH3 to N2 and H2. This results in nitridation of metallic Ni to nickel nitride (Ni3N) via the reaction: NH3 + 3Ni → Ni3N + 1.5H2 [11]. Because Ni3N is unstable in H2-rich atmospheres, it readily reverts to Ni [12], causing cyclic phase transformations that induce structural degradation. Recent studies have demonstrated that interface engineering is an effective route to improving the activity and durability of non-noble metal catalysts for ammonia decomposition. Engineered metal–oxide interfaces, in turn, regulate surface reaction energetics and stabilize active sites under harsh NH3 environments [9, 19]. Alternatively, beyond tailoring local interfacial chemistry, the incorporation of an anode catalyst layer (ACL) has been proposed as a complementary strategy to spatially decouple NH3 decomposition from the Ni-based anode, thereby minimizing direct Ni–NH3 contact and enhancing chemical stability [20, 21].

Pan et al. demonstrated tubular PCFCs employing a catalytic Fe layer, which suppressed Ni3N formation and improved durability. Density functional theory (DFT) calculations further revealed that Fe promotes NH3 decomposition due to its favorable nitrogen adsorption energetics [22]. More recently, Mo-containing perovskite oxides such as Sr2Fe2-xMoxO6-δ (SFM) have emerged as attractive ACL candidates, as Mo-induced acidic sites accelerate NH3 decomposition [9, 23]. He et al. reported that a Sr2Fe1.35Mo0.45Cu0.2O6-δ (SFMC) layer, integrated atop a Ni-BZCYYb anode, delivered

© The authors https://doi.org/10.1007/s40820-026-02194-9



Nano-Micro Lett. (2026) 18:335

excellent performance above 650 °C. Under reducing con- conditions, exsolved Fe and Cu nanoparticles alloyed with Ni, producing highly active Ni–Cu and Ni–Fe species that mark- edly improved NH3 conversion [24]. Building on these find- ings, we hypothesized that co-doping SFM with both acidic and reducible elements could synergistically maximize catalytic efficiency for NH3 decomposition. Acidic dopants more potent than Mo may promote N–H bond cleavage, while reducible elements with strong exsolution tendencies can generate highly active metallic species under operat- ing conditions. Furthermore, adopting a high-entropy oxide design—incorporating five or more equimolar cations—may introduce entropy-stabilization effects, thereby improving long-term durability under fuel cell conditions [25, 26].

In this study, we designed and synthesized a high-entropy perovskite oxide catalyst, Sr2Fe1Mo0.2Mn0.2Cr0.2Cu0.2Ni0.2O6-δ (SFMMCCN), incorporating Mn and Cr as acidic dopants and Cu and Ni as reducible dopants. SFM-MCCN was systematically evaluated as an ACL for DA-PCFCs. Structural integrity and entropy-stabilization effects were confirmed through comprehensive physicochemical characterization, while catalytic activity and durability toward NH3 decomposition were assessed under relevant fuel conditions. Complementary DFT calculations provided mechanistic insights into the role of entropy-driven design in promoting NH3 decomposition kinetics. Finally, a full DA-PCFC incorporating SFMMCCN as the ACL was fabricated, demonstrating strong functional viability in practical cell operation.

# 2 Experimental Section

# 2.1 Material Preparation

Powders of Sr2Fe1.5Mo0.5O6-δ (SFM), Sr2Fe1Mo0.6Cu0.2Ni0.2O6-δ (SFMCN), and SFMMCCN were synthe- sized via a sol–gel process. For SFM, high-purity Sr(NO3)2, Fe(NO3)3 ⋅ 9H2O, and (NH4)2MoO4 were used as cation precursors. For SFMMCCN, the same precursors were combined with Mn(NO3)2·6H2O, Cr(NO3)3·9H2O, Cu(NO3)2·3H2O, and Ni(NO3)2·6H2O in the appropriate molar ratios. All precursors were dissolved in deionized water at 80 °C, after which ethylenediaminetetraacetic acid (EDTA) and citric acid were introduced. The solution pH was adjusted to 8 by the controlled addition of ammonia.

# 2.2 Physicochemical Characterizations

High-resolution X-ray diffraction (XRD) was performed using Cu-Kα1 radiation and a Ge (111) monochromator over a 2θ range of 20°–80°. The microstructure of SFM-MCCN pellets and single cells was examined by scanning electron microscopy (SEM) with energy-dispersive X-ray spectroscopy (EDS) (JEOL, JSM-IT800). Atomic-scale features were further investigated using a high-resolution transmission electron microscope (HR-TEM; Thermo Fisher, Spectra Ultra). X-ray photoelectron spectroscopy (XPS; K-Alpha, Thermo VG Scientific) with monochromatic Al Kα radiation was employed to determine the valence states of the elements. NH3 temperature-programmed desorption (NH3-TPD) was performed on samples pretreated at 500 °C in He for 2 h, reduced at 700 °C in H2 for 2 h, and then exposed to NH3. Desorption was monitored during heating at 10 °C min−1 using an AutoChem II 2920 (Micromeritics).

# 2.3 Catalytic Activity Test

The catalytic activities of SFM, SFMMCCN, and Ni-BaZr0.4Ce0.4Y0.1Yb0.1O3-δ (BZCYYb) were evaluated in a fixed-bed quartz reactor. Each catalyst powder (0.2 g) was pre-reduced in a flow of H2 (50 sccm) at 700 °C for 2 h, followed by the introduction of NH3 (20 sccm). The specific surface areas of all catalysts were determined by Brunauer–Emmett–Teller (BET) N2 adsorption measure- ments (Fig. S1). The NH3 decomposition ratio was measured as a function of temperature. Residual NH3 and H2O in the effluent were removed using dilute H2SO4 solution and CaSO4 absorbent, respectively. Effluent gas composition was measured with a mass flow meter (Bronkhorst, Ruurlo, Netherlands). The NH3 conversion efficiency, corresponding to a theoretical product ratio of 75% H2 and 25% N2, was determined by the following Eq. (1)




Page 4 of 15
Nano-Micro Lett. (2026) 18:335

NH3 conversion (%) =  Fout × 100 (1)

where Fin and Fout denote the inlet and outlet gas flow rates, respectively [28].

# 2.4 Computational Details

The DFT calculations were conducted with the Vienna ab initio simulation package (VASP) [29]. The Perdew–Burke–Ernzerhof generalized gradient approximation (GGA-PBE) was considered for the exchange–correlation functionals. Valence configurations were 4p63d64s1 for Mn, 4p63d54s1 for Cr, 3d104s1 for Cu, 3d94s1 for Ni, 4s24p64d55s1 for Mo, 4s24p65s2 for Sr, 3d64s1 for Fe, and 2s2p4 for O. DFT + U approach was applied and the values employed for Mn, Cr, Cu, Ni, Mo, and Fe were 3.9, 3.7, 4.0, 6.2, 4.38, and 5.3 eV, respectively. Plane waves with an energy cutoff of 450 eV were used. A Monkhorst–Pack [30] k-point mesh of 1 × 2 × 1 and 3 × 3 × 1 was applied to the 156-atom perovskite and 54-atom metal (Ni and Ni–Fe–Cu) slabs, respectively. The convergence threshold for electronic self-consistent iterations was 10−6 eV cell−1. Cell parameters and atomic positions were relaxed until the remaining force was less than 1 × 10−1 eV Å−1. Each slab was separated along the z-axis by a 20 Å of vacuum region. NH3 adsorption sites were determined by identifying those with the lowest energy cost among all possible cation sites in perovskites and atop, bridge, FCC, and HCP sites in metals.

# 2.5 Single Cell Fabrication

Anode-supported protonic ceramic fuel cells (PCFCs) were fabricated in a multilayer configuration consisting of a NiO–BZCYYb anode, a NiO–BZCYYb anode functional layer, a BZCYYb electrolyte, and a BSTC cathode. For the supporting layer slurry, NiO (Sumitomo) and BZCYYb powder (Kceracell) were blended at a 6:4 weight ratio, followed by sequential addition of ethanol and toluene as solvents, Hypermer KD-1 (CRODA) as a dispersant, polyvinyl butyral (Eastman Chemical Company) as a binder, di-n-butyl phthalate (Junsei) as a plasticizer, and poly(methyl methacrylate) (Sunjin Chemical) as a pore former. Slurries for the functional layer and electrolyte (prepared without pore former) were produced using the same procedure. The resulting SFM and SFMMCCN were synthesized via a sol–gel method. Figure 1a presents the XRD patterns. The results confirm the formation of well-defined double perovskite structures in both materials, indicating successful incorporation of Mn, Cr, Cu, and Ni into the SFM lattice without secondary phases. To probe the structural evolution under reduction conditions, in situ high-temperature XRD (HT-XRD) was performed in 3% H2/Ar from room temperature (RT) to 700 °C. As shown in Fig. 1b, c, the lattice progressively expands with increasing temperature, reflecting the combined contributions of thermal expansion and reduction-induced chemical expansion [31]. Notably, a new diffraction feature emerges near 44° above 400 °C, consistent with the nucleation of a metallic phase via exsolution. In contrast, no additional diffraction peaks associated with exsolved metallic species were detected for SFM.

© The authors https://doi.org/10.1007/s40820-026-02194-9


Nano-Micro Lett. (2026) 18:335
Page 5 of 15  335

a                                   b            Reducing condition : 3% H/Ar c     700                                   3000

SFMMCCN              700 °                     SFMMCCN            600                           Heating 2725

20                                  20 600 °                                     20 500                                   2450

500                                        400                                   2175

SFM                    400                                     300     Alloy                       1900

300                                                                              1625

200                                        200                                   1350

100 °C                                       100                   SFMMCCN         1075

RT                                                                                     800.0

20  30  40   50  60  70        80  42              44       46       48        42                    44  46     48

d         2    Theta (degree)           e          2 Theta (degree)              f 140     2           Theta   (degree)

Pristine                             After reduction                               120                    20.4 nm

100

2 80

60

40

20

500 nm                               500 nm                                       0                     10     20  30   40

0

Particle radius (nm)

# Fig. 1

a XRD patterns of the as-synthesized SFM and SFMMCCN. In situ HT-XRD b patterns and c contour plot of SFMMCCN under reducing atmosphere (3% H₂/Ar) from RT to 700 °C. SEM images of the SFMMCCN pellet surface in the d as-synthesized and e after reduction. f Particle size distribution histogram of exsolved nanoparticles on the surface of the reduced SFMMCCN pellet

after reduction (Fig. S2). To validate these findings under lattice fringe of an exsolved nanoparticle. The measured d-spacing of 0.28 nm corresponds to the (110) plane of the perovskite phase, indicating coherent lattice integration between the nanoparticle and the host matrix. The nanoparticle exhibited an average diameter of ~ 20 nm, with robust particle–matrix interfaces that mitigate detachment and aggregation—two key degradation pathways that typically compromise long-term catalytic performance [32, 33]. Fig-ure 2c further provides EDS elemental maps of the exsolved nanoparticles, showing homogeneous distributions of Ni, Fe, and Cu, consistent with the formation of a Ni–Fe–Cu alloy.

Figure 2a displays the HR-TEM image of reduced SFM-MCCN, revealing a well-defined perovskite lattice with distinct sublattices occupied by multiple transition-metal cations. After reduction, finely dispersed nanoparticles were observed within the bulk matrix. High-angle annular dark-field scanning transmission electron microscopy (HAADF-STEM) combined with the EDS confirms a uniform elemental distribution across the reduced perovskite oxide, validating the successful incorporation of Mn, Cr, Cu, and Ni into the B-site lattice. Figure 2b shows the HR-TEM using Eq. (2) [36]:


Page 6 of 15

# Nano-Micro Lett. (2026) 18:335

|          | Sr     | Fe     | Mo     |        |   |   |   |
| -------- | ------ | ------ | ------ | ------ | - | - | - |
| SFMMCCN  | 500 pm |        |        |        |   |   |   |
| Mn       | Cr     |        | Cu     | Ni     |   |   |   |
| Exsolved | 100 nm | 500 pm | 500 pm | 500 pm |   |   |   |

|          |      | Sr    | Fe   | Mo   |      |      |      |      |
| -------- | ---- | ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| 5 nm     | 2 nm | 2 nm  | 2 nm | 2 nm |      |      |      |      |
| d=0.28nm | Mn   | Cr    | Cu   | Ni   |      |      |      |      |
|          |      | (110) |      |      | 2 nm | 2 nm | 2 nm | 2 nm |

d

e

Sr Fe Mo Mn Cr Cu NiO

2.0 R pristine

After reduction

ArTE

Exsolved nanoparticle

201.5 R

1.0 R

0.5 R

0

Bulk

Bulk

Exsolved

SFMMCCN

Reduced SFMMCCN

Fig. 2 a HR-TEM, HAADF-STEM and elemental mapping images of reduced SFMMCCN powder. b HR-TEM, lattice fringe, and c HAADF-STEM and EDS mapping images of exsolved nanoparticles. d Configuration entropy of the pristine and reduced SFMMCCN. e Schematic illustration of the in situ entropy-controlled process

N where R is the gas constant, N denotes the number of constituent elements, and xi is the mole fraction of the i-th component. Based on this metric, alloys are classified as high-, medium-, or low-entropy systems when Δ Sconfig ≥

© The authors

https://doi.org/10.1007/s40820-026-02194-9




Nano-Micro Lett. (2026) 18:335
1.5R, 1.0R ≤ Δ Sconfig ≤ 1.5R, and Δ Sconfig ≤ 1.0R, respectively [37]. For perovskite oxides, ΔSconfig can similarly be expressed as Eq. (3) [38]:

ΔSconfig = −R ∑ xalnxa + ∑ xblnxb + ∑ xclnxc
a=1        b=1       c=1

where A and B denote the number of species occupying A- and B-sites, respectively, C the number of anion types, and xa, xb, and xc the mole fractions. As shown in Fig. 2d, pristine SFMMCCN exhibits a configurational entropy of 1.60 R, qualifying as a high-entropy perovskite oxide (HEPO). Upon reduction, the bulk retains a high-entropy state, albeit slightly lower at 1.50 R. In contrast, the exsolved Ni–Fe–Cu alloy displays a medium-entropy value of 1.09 R. The schematic in Fig. 2e illustrates this entropy-controlled process: under reducing conditions, selective exsolution of a medium-entropy alloy occurs from the high-entropy oxide matrix.

To assess the catalytic potential of SFMMCCN as an ACL in DA-PCFCs, its NH3 conversion efficiency was compared against those of a low-entropy perovskite catalyst (SFM), a medium-entropy perovskite catalyst (SFMCN), and a bare anode (Ni-BZCYYb). Prior to testing, all materials were thermally treated at 700 °C for 2 h under a pure H2 atmosphere, identical to the conditions used during cell operation. As shown in Fig. 4a, SFMMCCN exhibits a remarkable NH3 conversion of 96% at 600 °C, far exceeding that of SFM (47%) and SFMCN (57%). Interestingly, the bare Ni-BZCYYb anode exhibits higher NH3 conversion than SFM and SFMCN.

The XPS analysis was employed to investigate the valence states of the constituent elements in SFMMCCN before and after exposure to reducing conditions. All spectra were calibrated using the C 1s as a reference. As shown in Fig. 3a, characteristic binding energy signals corresponding to Sr, Fe, Mo, Mn, Cr, Cu, and Ni were consistently observed in both the pristine and reduced samples. Detailed spectral deconvolution of the Fe 2p, Cu 2p, and Ni 2p regions is presented in Fig. 3b–d. In the pristine sample, only oxidized states of the transition metals were identified. After reduction at 700 °C for 2 h in a pure H2 atmosphere, additional features indicative of metallic species emerged. Specifically, a distinct Fe0 peak appears at ~ 707 eV in the Fe 2p spectrum (Fig. 3b) [10]. The corresponding Fe 2p fitting parameters are summarized in Table S1. In addition, the Cu 2p spectra (Fig. 3c) revealed characteristic Cu0 peaks near 933 and 953 eV [39]. Figure 3d displays the Ni 2p spectrum, where a peak at ~ 852 eV is assigned to metallic Ni0 species [17]. Complementary XPS analyses of Mo, Mn, Cr, and O species before and after reduction are presented in Fig. S7. Collectively, these observations confirm the reduction of Ni, Fe, and Cu, leading to the in situ exsolution of a Ni–Fe–Cu alloy from the SFMMCCN perovskite matrix, consistent with the structural evidence in Fig. 2. The formation of this multi-metallic alloy is anticipated to significantly improve catalytic activity for ammonia decomposition through synergistic effects and enhanced surface reactivity compared to monometallic catalysts.

The long-term catalytic durability is shown in Fig. 4c. While SFMMCCN sustained nearly complete NH3 conversion for over...




Page 8 of 15

# Nano-Micro Lett. (2026) 18:335

# Fig. 3 XPS spectra of a survey, b Fe 2p, c Cu 2p, and d Ni 2p for SFMMCCN before and after reduction at 700 °C for 2 h in a 100% H₂ atmosphere

| a        | b                  |
| -------- | ------------------ |
| Pristine | Pristine           |
| Fe 2p    | Fe4+               |
| Fe2+     | 20 After reduction |
| Cu 2p    | Ni 2p              |
| Fe 2p    | Mn 2p              |
|          | Mo 3d              |
|          | 20 After reduction |
| Fe4+     | Fe2+               |
|          | sat Fe0            |

1000 800 600 400 200 0 730 725 720 715 710 705

Binding energy (eV)

| c                  | d                  |
| ------------------ | ------------------ |
| Pristine           | Pristine           |
| Cu 2p              | Ni 2p              |
| Cu2+               | sat. Ni2+          |
| 20 After reduction | Cu^2+              |
| Cu0                | 20 After reduction |
| Ni2+               | Nio                |
| Cu^2+              | Cu0                |
| sat.               |                    |

955 950 945 940 935 930 865 860 855 850

Binding energy (eV)

50 h at 600 °C, Ni-BZCYYb exhibited rapid deactivation within 20 h. This degradation is attributed to Ni nanoparticle coarsening, triggered by repeated phase nitridation (Ni → Ni3N) and subsequent reversion to metallic Ni. Consistent with this mechanism, SEM analysis after durability testing revealed pronounced structural degradation of Ni-BZCYYb, whereas SFMMCCN preserved its morphology. Post-test XRD and STEM–EDS analyses further indicate that beyond the structural evolution of Ni, the Ni-BZCYYb undergoes phase separation of the BZCYYb component under NH3 operation, accompanied by BaO formation. In contrast, the SFMMCCN remains structurally and chemically intact after long-term operation, with no detectable secondary phases observed, indicating excellent phase stability. XPS analysis further confirms that the chemical states of the exsolved Ni–Fe–Cu.

© The authors https://doi.org/10.1007/s40820-026-02194-9


Nano-Micro Lett. (2026) 18:335

# Fig. 4

# a

| 100 | SFM       | NH3-TPD   | 100     |
| --- | --------- | --------- | ------- |
| 20  | 80        | SFMCN     | 20      |
|     | SFMMCCN   |           | SFMMCCN |
| 60  | Ni-BZCYYb |           | 60      |
| 40  |           | Ni-BZCYYb | 40      |
| 20  |           |           | 20      |
| 0   |           |           | 0       |

# b

# c

|     |     | 600 | °   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 450 | 500 | 550 | 600 | 650 | 700 |     |     |
|     | 100 | 200 | 300 | 400 | 500 | 600 | 700 |
| 0   | 10  | 20  | 30  | 40  | 50  |     |     |

# d

| 14 | SFM | 3.40  | 3.37 | \*+N   |       |                      |        |
| -- | --- | ----- | ---- | ------ | ----- | -------------------- | ------ |
| 20 | 7-  | 0.06  | 3.26 | \*+NH2 | \*+NH | -8.98                |        |
| 0  |     | \*+NH |      |        | 0-    | \*+NH                | \*+NH2 |
| -7 |     |       |      |        |       | Reaction Coordinates |        |

# e

| -3.2      |        |        | g       |                 | h              | 0      |         |       |      |       |    |    |    |
| --------- | ------ | ------ | ------- | --------------- | -------------- | ------ | ------- | ----- | ---- | ----- | -- | -- | -- |
| SFM       |        | 50     | -3.4    | -               | Band           | O2p    |         |       |      |       |    |    |    |
|           |        | -3.5   | -0.4    | ICOHPavg: -0.66 |                | -1     | Weak    | High  |      |       |    |    |    |
|           |        |        | ICOHP   |                 |                |        | SFMMCCN |       | Low  | ICOHP |    |    |    |
| -3.8      | -3.8   | 8      | (E)dE   | 0.0             |                |        |         |       |      |       |    |    |    |
| -4.0      |        | -∞     | (E)dE   | -0.4            | ICOHPavg:-0.63 | -2     |         |       |      |       |    |    |    |
|           | SFM    |        | SFMMCCN |                 | -20            | -10    | 0       | Mo    | Cr   | Mn    | Fe | Cu | Ni |
| E-E= (eV) |        | 8      | Ni      | 1.51            |                |        |         |       |      |       |    |    |    |
| 20        | 4-     | 0.10   | 0.03    | 2.09            | \*+NH          | \*+N   | -2.63   |       |      |       |    |    |    |
| 20        | 4      |        |         |                 | 1.22           |        | -1.51   | -1.08 | 1.46 | 1.02  |    |    |    |
| 0         | \*+NH3 | \*+NH2 |         | 0               | \*+NH3         | \*+NH2 | \*+NH   | \*+N  |      |       |    |    |    |

# Reaction Coordinates

# Reaction Coordinates




Page 10 of 15
# Nano-Micro Lett. (2026) 18:335

∗NH → ∗NH2 + 1 H(g) (5) could further provide detailed information on reaction kinetics, including energy barriers, diffusion processes, and N2 formation. To this end, developing computational methodologies that incorporate high-entropy configurations without compromising accuracy would be an interesting topic for future work.

∗NH2 → ∗NH + 1 H2(g) (6)

∗NH → ∗N + 1 H2(g) (7)

∗N → ∗ + 1 N2(g) (8)

Optimized structure models for SFM, SFMMCCN, Ni, and Ni–Fe–Cu systems are provided in Figs. S16–S19, respectively. The adsorption site * was determined by searching the configuration with the lowest energy cost. The reaction sites considered in this study, including atop, bridge, FCC, and HCP sites, along with their corresponding energetics for the SFM, SFMMCCN, Ni, and Ni–Fe–Cu models, are presented in Fig. S20. For the oxide systems (SFM and SFMMCCN), only metal atop sites were considered. In the Ni–Fe–Cu model, the adsorbate initially placed on the FCC site was found to relocate to the Fe atop site upon structural relaxation. The calculated highest energy barrier was 3.40 eV for SFM, compared to 2.63 eV for SFM-MCCN, confirming that the high-entropy perovskite lowers the kinetic barriers for NH3 decomposition.

We further investigated the driving force for exsolution in SFMMCCN. Figure 4f displays that the O 2p band center in SFMMCCN (− 3.5 eV) lies at a higher energy level than in SFM (− 3.8 eV), indicating that oxygen vacancy formation—and hence cation exsolution—is more favorable in SFMMCCN. Crystal orbital Hamilton population (COHP) analysis (Fig. 4g) revealed less negative integrated COHP (ICOHP) value for SFMMCCN compared with SFM, suggesting weaker cation–oxygen bonds and greater exsolution propensity. The ICOHP values for individual elements in SFM-MCCN (Fig. 4h) further showed that Ni, Cu, and Fe possess the weakest bonding to oxygen, correlating with the experimentally observed exsolved alloy composition (Fig. 2).

Finally, the energy profiles for NH3 decomposition were compared between bare Ni and the exsolved Ni–Fe–Cu alloy (Fig. 4i, j). The maximum energy barrier for Ni was 2.09 eV, while the exsolved Ni–Fe–Cu alloy exhibited a significantly lower barrier of 1.46 eV. The overall order of energy barriers was: Ni–Fe–Cu (1.46 eV) &#x3C; Ni (2.09 eV) &#x3C; SFMMCCN (2.63 eV) &#x3C; SFM (3.40 eV).

These findings confirm that the exsolved metallic alloy provides superior catalytic activity in NH3 decomposition compared to either the parent. We suggest that transition-state searches could further provide insights into the reaction mechanisms involved.

# 3.4 Electrochemical Performance

To assess the practical application of SFMMCCN as an ACL for DA-PCFCs, a cell configuration was constructed as depicted in Fig. 5a. In this system, NH3 is supplied directly to the anode, where it is initially adsorbed on the ACL and subsequently decomposed into N2 and H2 by the catalyst sites. The cross-sectional SEM image in Fig. 5b shows the assembled cell structure, comprising a SFMMCCN ACL, a Ni-BZCYYb anode, a BZCYYb electrolyte, and a BSTC cathode (hereafter referred to as the SFMMCCN cell). The ACL was deposited uniformly on the anode with a thickness of approximately 30 µm, forming a well-adhered interface without observable delamination. This robust interfacial contact can be attributed, in part, to the favorable thermo-mechanical compatibility between SFMMCCN and NiO–BZCYYb, as evidenced by their similar thermal expansion coefficients (TECs) measured by thermal dilatometry (Fig. S21).

High-resolution imaging revealed well-dispersed Ni–Fe–Cu alloy nanoparticles exsolved from the SFMMCCN surface, with no signs of agglomeration. For comparison, a reference cell with an identical configuration but without the ACL was fabricated, hereafter denoted as the bare cell (Fig. S22). Figure 5c presents the electrochemical performance under NH3 fuel at 600 °C. The SFMMCCN cell achieved a maximum power density (MPD) of 1.11 W cm−2, reflecting a 32.1% enhancement relative to the bare cell. This improvement underscores the catalytic role of the SFMMCCN layer in facilitating NH3 decomposition.

Impedance spectra collected at 600 °C (Fig. 5d) further support this conclusion: compared to the bare cell, the SFMMCCN cell exhibits markedly lower non-ohmic resistances, as summarized in the inset, suggesting more efficient catalytic conversion of NH3 into N2 and H2. Consistently, distribution of relaxation time (DRT) analysis (Fig. S23) reveals a substantially reduced high-frequency contribution for the SFMMCCN cell, reflecting accelerated anodic kinetics enabled by rapid NH3-to-H2 conversion and subsequent H2 → H+ electrochemical reactions. In contrast, a slightly increased low-frequency contribution is observed, which is attributed to the relatively lower porosity of the SFM-MCCN ACL compared with the bare Ni-BZCYYb anode.

© The authors https://doi.org/10.1007/s40820-026-02194-9


Nano-Micro Lett. (2026) 18:335
# Fig. 5

# a

Conceptual schematic and

# b

cross-sectional SEM images of the DA-PCFC incorporating the SFMMCCN ACL.

# c

I–V–P curves

# d

Nyquist plots of DA-PCFCs with ACL (SFMMCCN cell) and without ACL (bare cell) under NH₃ fuel at 600 °C.

# e

MPD comparison between SFMMCCN and bare cells over the 550–700 °C range.

# f

Comparison of the MPDs of various DA-PCFCs.

# g

Long-term durability test at 0.3 A cm−2 using NH₃ fuel.

# h

Comparison of non-ohmic resistance during long-term durability testing.

Schematic representations of NH₃ adsorption and stepwise decomposition pathways on Ni-BZCYYb anodes

# i

without the ACL

# j

with the ACL

| O2 + 4H+ + 4e → 2H2O | Cathode              | SFMMCCN              |
| -------------------- | -------------------- | -------------------- |
| Electrolyte          | BSTC                 | (NH catalyst)        |
| Cathode              |                      |                      |
| Electrolyte          | H+                   | Anode                |
| Anode                | Anode catalyst layer | BZCYYb               |
| Anode catalyst layer | Ni-BZCYYb            | Exsolved             |
|                      | \~30 μm              | 100 μm               |
|                      | (Anode)              | 10 um Ni-Fe-Cu alloy |
|                      | 200 nm               |                      |

| Current density (A cm-²) | Re(Z) (Ω cm²) | Temperature (°C)   |
| ------------------------ | ------------- | ------------------ |
| 2.0                      | This work     | PSCFR15            |
| SFMC                     | 1.2           | 600 °C, 0.3 A cm-2 |
| RC/OPM-Anode             | Fe layer      | BZCYYbNi           |
| RCN                      | Pd ALD        | 1.0                |
| BZCYYbRF                 | BZCYYbPd      | 20                 |
| BZCYYb-KMg               | BZCYYbNRu     | 201.5              |
| Ru-B2CA                  | NiCo-BZCYYb   | 20                 |
| Fe infiltration          |               |                    |

| Temperature (°C) | Time (h) |
| ---------------- | -------- |
| 550              | 0.0      |
| 600              | 50       |
| 650              | 100      |
| 700              | 150      |
|                  | 200      |
|                  | 250      |





Nano-Micro Lett. (2026) 18:335

Nevertheless, this modest gas-diffusion penalty is outweighed by the pronounced enhancement in anodic charge-transfer kinetics, resulting in superior overall performance under NH3 fuel. Figures S24 and S25 show temperature-dependent impedance spectra for both PCFCs. Figure 5e compares MPD values across the range of 550–700 °C, demonstrating that the SFMMCCN cell consistently outperformed the bare cell. The corresponding I–V–P curves are presented in Figs. S26 and S27. As summarized in Fig. 5f and Table 1, the SFMMCCN cell also surpasses the performance of other state-of-the-art DA-PCFCs. To the best of our knowledge, this is the first demonstration of a DA-PCFC achieving an MPD of 2.04 W cm−2 at 700 °C, surpassing all previously reported values irrespective of catalyst design. The durability of both cells was further examined under constant current operation of 0.3 A cm−2 at 600 °C with NH3 fuel. As shown in Fig. 5g, the bare cell exhibited rapid performance decay, attributable to accelerated Ni nitridation and particle coarsening arising from direct exposure to NH3. These degradation mechanisms reduce the number of electrochemically active sites and hinder mass transport. In sharp contrast, the SFMMCCN cell maintained stable output for over 255 h of continuous operation without signs of abrupt degradation.

# 1. Comparison of the of various DA-PCFCs at the temperature range of 550–700 °C

| Cathode | Electrolyte | Anode                        | Anode catalyst    | MPD (W cm−2)     |      |      |      |     |      |   |   |
| ------- | ----------- | ---------------------------- | ----------------- | ---------------- | ---- | ---- | ---- | --- | ---- | - | - |
|         |             |                              |                   | Temperature (°C) | 550  | 600  | 650  | 700 |      |   |   |
| BSTC    | BZCYYb₄₄₁₁  | Ni-BZCYYb₄₄₁₁                | SFMMCCN layer     | 0.67             | 1.11 | 1.60 | 2.04 |     |      |   |   |
| BSTC    | BZCYYb₄₄₁₁  | Ni-BZCYYb₄₄₁₁                | –                 | 0.54             | 0.92 | 1.33 | 1.68 |     |      |   |   |
| BCFZYNa | BZCYYb₁₇₁₁b | Ni-BZCYYb₁₇₁₁                | PSCFR₁₅c layer    | 0.32             | 0.45 | 0.63 | –    |     |      |   |   |
| PBSCFd  | BZCYYb₁₇₁₁  | Ni-BZCYYb₁₇₁₁                | SFMCe layer       | –                | 0.62 | 1.03 | 1.64 |     |      |   |   |
| PBSCF   | BZCYYb₁₇₁₁  | RC/OPM-Anodef                | –                 | 0.55             | 0.75 | 1.01 | –    |     |      |   |   |
| PBSCF   | BZCYYb₁₇₁₁  | Ni-BZCYYb₁₇₁₁                | Fe layer          | –                | 0.33 | 0.69 | 1.08 |     |      |   |   |
| BCCYg   | BZCYYbNh    | Ni-BZCYYbN                   | –                 | 0.24             | 0.36 | 0.52 | –    |     |      |   |   |
| PBSCF   | BZCYYb₁₇₁₁  | RCNi-decorated Ni-BZCYYb₁₇₁₁ | –                 | 0.73             | 0.94 | 1.31 | 1.77 |     |      |   |   |
| PBSCF   | BZCYYb₂₆₁₁j | Pd-decorated Ni-BZCYYb₂₆₁₁   | –                 | 0.34             | 0.61 | 0.85 | –    |     |      |   |   |
| BCFZYk  | BZCYYb₁₇₁₁  | Ni-BZCYYbRFl                 | –                 | 0.45             | 0.65 | 0.81 | –    |     |      |   |   |
| BCFZY   | BZCYYbPdm   | Ni-BZCYYbPd                  | –                 | 0.37             | 0.51 | 0.72 | –    |     |      |   |   |
| BCFZY   | BZCYYb₁₇₁₁  | Ni-BZCYYbKMgn                |                   |                  |      |      | –    | –   | 0.45 | – | – |
| BCFZY   | BZCYYb₁₇₁₁  | Ni-BZCYYb₁₇₁₁                | BZCYYbNRuo filler | 0.12             | 0.22 | 0.35 | 0.48 |     |      |   |   |
| PBSCF   | BZCYYb₁₇₁₁  | Ni0.97Co₃-BZCYYb₁₇₁₁         | –                 | –                | 0.48 | 0.60 | 0.85 |     |      |   |   |
| PBSCF   | BZCYYb₁₇₁₁  | Fe-decorated Ni-BZCYYb₁₇₁₁   | –                 | 0.35             | 0.71 | 1.25 | 1.61 |     |      |   |   |

a Ba0.95(Co0.4Fe0.4Zr0.1Y0.1)0.95Ni0.05O3−δ;

b BaZr0.1Ce0.7Y0.1Yb0.1O3−δ;

c Pr0.6Sr0.4(Co0.2Fe0.8)0.85Ru0.15O3−δ;

d PrBa0.5Sr0.5Co1.5Fe0.5O5+δ;

e Sr2Fe1.35Mo0.45Cu0.2O6−δ;

f Cs2O-modified Ru catalyst (RC) on the anode prepared by a one-step precursor mixing (OPM-Anode);

g BaCo0.7Ce0.24Y0.06O3−δ;

h Ba(Zr0.1Ce0.7Y0.1Yb0.1)0.95Ni0.05O3−δ;

i Ru0.95Cu0.05-Nix;

j BaZr0.2Ce0.6Y0.1Yb0.1O3−δ;

k BaCo0.4Fe0.4Zr0.1Y0.1O3−δ;

l Ba(Zr0.1Ce0.7Y0.1Yb0.1)0.94Ru0.03Fe0.03O3−δ;

m Ba(Zr0.1Ce0.7Y0.1Yb0.1)0.95Pd0.05O3−δ;

n Ba0.95K0.05(Zr0.1Ce0.7Y0.1Yb0.1)0.95Mg0.05O3−δ;

o B(Zr0.1Ce0.7Y0.1Yb0.1)0.9Ni0.05Ru0.05O3−δ

© The authors https://doi.org/10.1007/s40820-026-02194-9



 Nano-Micro Lett. (2026) 18:335 
Figures 5h, S28, and S29 reveal that while the SFMMCCN design cell experienced only a slight increase in non-ohmic resistance up to 200 h before stabilizing, the bare cell exhibited a continuous rise, reflecting ongoing degradation. Post-test SEM analysis (Fig. S30) confirmed that Ni particles in the SFMMCCN cell remained significantly finer than those in the bare cell, reinforcing the protective role of the ACL in mitigating Ni agglomeration and nitridation. In addition, Fig. S31 shows that the exsolved nanoparticles on the SFMMCCN surface remain uniformly dispersed without noticeable coalescence even after long-term operation, demonstrating the intrinsic structural stability of the exsolved alloy under operating conditions.

Figure 5i, j schematically illustrates the mechanistic differences in NH3 decomposition. In the bare Ni-BZCYYb anode (Fig. 5i), NH3 adsorbs onto the Ni surfaces and undergoes sequential dehydrogenation. However, the high energy barrier of this pathway limits reaction kinetics and suppresses effective NH3 conversion. By contrast, in the SFMMCCN cell (Fig. 5j), in situ exsolved Ni–Fe–Cu alloy nanoparticles, embedded in the high-entropy oxide matrix, provide abundant acid sites and catalytically active medium-entropy alloy interfaces. This synergistic architecture lowers the barriers for NH3 adsorption and dehydrogenation, thereby enhancing charge-transfer kinetics while maintaining effective mass transport. Moreover, the ACL minimizes direct NH3 exposure to Ni particles, suppressing agglomeration and ensuring long-term stability.

# Conclusion

In this study, we developed a high-entropy perovskite catalyst layer (SFMMCCN) incorporating in situ exsolved Ni–Fe–Cu alloy nanoparticles to address the limitations of conventional anodes in DA-PCFCs. The tailored composition and entropy-stabilized structure endowed the catalyst with superior activity for NH3 decomposition and exceptional electrochemical stability. Compared with the bare cell, the SFMMCCN-based cell achieved a remarkable power output of 2.04 W cm−2 at 700 °C and preserved both structural and functional integrity during prolonged operation under NH3 at 600 °C. By integrating comprehensive experimental characterization with DFT calculations, we revealed that the enhanced performance originates from favorable exsolution thermodynamics and synergistic alloy-high-entropy oxide interfaces that accelerate reaction kinetics. These findings demonstrate that catalytic efficiency in DA-PCFCs can be substantially advanced through high-entropy materials.

# Acknowledgements

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (No. RS-2024-00406086 and No. RS-2024-00338569). This work was supported by the Basic Research Project (GP2025-039) of KIGAM. Furthermore, this work was supported by the InnoCORE program of the Ministry of Science and ICT (N10250154).

# Author Contributions

K.T.L. conceived the concept and supervised the project. D.K. conducted the following experiments: material synthesis, XRD, SEM, TEM, XPS analyses, catalyst testing, and cell fabrication. D.J.P. and S.W.L. performed DA-PCFC cell testing. I.J. carried out DFT calculations. S.O., H.K., and M.L. assisted with PCFC cell fabrication. K.L. and D.C. conducted the NH3 conversion test. D.K., D.J.P., I.J., K.-M.R., J.B., T.H.S., and K.T.L. contributed to writing the paper.

# Declarations

Conflict of interest: The authors declare no interest conflict. They have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Open Access: This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

# Supplementary Information

The online version contains supplementary material available at https://doi.org/10.1007/s40820-026-02194-9.

# References

1. I. Staffell, D. Scamman, A. Velazquez Abad, P. Balcombe, P.E. Dodds et al., The role of hydrogen and fuel cells in the global energy system. Energy Environ. Sci. 12(2), 463–491 (2019). https://doi.org/10.1039/c8ee01157e
2. C. Duan, R.J. Kee, H. Zhu, C. Karakaya, Y. Chen et al., Highly durable, coking and sulfur tolerant, fuel-flexible





Nano-Micro Lett. (2026) 18:335

1. A.M. Abdalla, S. Hossain, O.B. Nisfindy, A.T. Azad, M. Dawood et al., Hydrogen production, storage, transportation and key challenges with applications: a review. Energy Convers. Manag. 165, 602–627 (2018). https://doi.org/10.1016/j.enconman.2018.03.088
2. L. Schlapbach, A. Züttel, Hydrogen-storage materials for mobile applications. Nature 414(6861), 353–358 (2001). https://doi.org/10.1038/35104634
3. D. Ding, Y. Zhang, W. Wu, D. Chen, M. Liu et al., A novel low-thermal-budget approach for the co-production of ethylene and hydrogen via the electrochemical non-oxidative deprotonation of ethane. Energy Environ. Sci. 11(7), 1710–1716 (2018). https://doi.org/10.1039/c8ee00645h
4. A. Klerke, C.H. Christensen, J.K. Nørskov, T. Vegge, Ammonia for hydrogen storage: challenges and opportunities. J. Mater. Chem. 18(20), 2304 (2008). https://doi.org/10.1039/b720020j
5. B. Wang, T. Li, F. Gong, M.H.D. Othman, R. Xiao, Ammonia as a green energy carrier: electrochemical synthesis and direct ammonia fuel cell - a comprehensive review. Fuel Process. Technol. 235, 107380 (2022). https://doi.org/10.1016/j.fuproc.2022.107380
6. D. Kim, J.W. Park, M.S. Chae, I. Jeong, J.H. Park et al., An efficient and robust lanthanum strontium cobalt ferrite catalyst as a bifunctional oxygen electrode for reversible solid oxide cells. J. Mater. Chem. A 9(9), 5507–5521 (2021). https://doi.org/10.1039/d0ta11233j
7. H. Zhang, Y. Zhou, K. Pei, Y. Pan, K. Xu et al., An efficient and durable anode for ammonia protonic ceramic fuel cells. Energy Environ. Sci. 15(1), 287–295 (2022). https://doi.org/10.1039/d1ee02158c
8. M. Liang, Y. Song, B. Xiong, D. Liu, D. Xue et al., In situ exsolved CoFeRu alloy decorated perovskite as an anode catalyst layer for high-performance direct-ammonia protonic ceramic fuel cells. Adv. Funct. Mater. 34(48), 2408756 (2024). https://doi.org/10.1002/adfm.202408756
9. J. Yang, A.F.S. Molouk, T. Okanishi, H. Muroyama, T. Matsui et al., A stability study of Ni/yttria-stabilized zirconia anode for direct ammonia solid oxide fuel cells. ACS Appl. Mater. Interfaces 7(51), 28701–28707 (2015). https://doi.org/10.1021/acsami.5b11122
10. Z. Wan, Y. Tao, J. Shao, Y. Zhang, H. You, Ammonia as an effective hydrogen carrier and a clean fuel for solid oxide fuel cells. Energy Convers. Manag. 228, 113729 (2021). https://doi.org/10.1016/j.enconman.2020.113729
11. M. Liang, J. Kim, X. Xu, H. Sun, Y. Song et al., Electricity-to-ammonia interconversion in protonic ceramic cells: advances, challenges and perspectives. Energy Environ. Sci. 18(8), 3526–3552 (2025). https://doi.org/10.1039/D4EE06100D
12. M.Z. Khan, R.-H. Song, A. Hussain, S.-B. Lee, T.-H. Lim et al., Effect of applied current density on the degradation behavior of anode-supported flat-tubular solid oxide fuel cells.
13. Z. Liu, H. Di, D. Liu, G. Yang, Y. Zhu et al., Boosting ammonia-fueled protonic ceramic fuel cells with RuFe nanoparticle exsolution: enhanced performance via secondary redox treatment. Adv. Funct. Mater. 35(15), 2420214 (2025). https://doi.org/10.1002/adfm.202420214
14. F. He, Q. Gao, Z. Liu, M. Yang, R. Ran et al., A new Pd doped proton conducting perovskite oxide with multiple functionalities for efficient and stable power generation from ammonia at reduced temperatures. Adv. Energy Mater. 11(19), 2003916 (2021). https://doi.org/10.1002/aenm.202003916
15. H. Zhang, K. Xu, Y. Xu, F. He, F. Zhu et al., In situ formed catalysts for active, durable, and thermally stable ammonia protonic ceramic fuel cells at 550 °C. Energy Environ. Sci. 17(10), 3433–3442 (2024). https://doi.org/10.1039/d4ee00219a
16. F. Schüth, R. Palkovits, R. Schlögl, D.S. Su, Ammonia as a possible element in an energy infrastructure: catalysts for ammonia decomposition. Energy Environ. Sci. 5(4), 6278–6289 (2012). https://doi.org/10.1039/c2ee02865d
17. H. Zhang, R. Xiong, Z. Chen, Z. Cheng, J. Huang et al., Efficient and robust nanocomposite cermet anode with strong metal–oxide interaction for direct ammonia solid oxide fuel cells. Adv. Funct. Mater. 35(38), 2501223 (2025). https://doi.org/10.1002/adfm.202501223
18. N. Tsvetkov, D. Kim, I. Jeong, J.H. Kim, S. Ahn et al., Advances in materials and interface understanding in protonic ceramic fuel cells. Adv. Mater. Technol. 8(20), 2201075 (2023). https://doi.org/10.1002/admt.202201075
19. Y. Pan, H. Zhang, K. Xu, Y. Zhou, B. Zhao et al., A high-performance and durable direct NH3 tubular protonic ceramic fuel cell integrated with an internal catalyst layer. Appl. Catal. B Environ. 306, 121071 (2022). https://doi.org/10.1016/j.apcatb.2022.121071
20. Y.-F. Sun, Y.-Q. Zhang, B. Hua, Y. Behnamian, J. Li et al., Molybdenum doped Pr0.5Ba0.5MnO3−δ (Mo-PBMO) double perovskite as a potential solid oxide fuel cell anode material. J. Power. Sources 301, 237–241 (2016). https://doi.org/10.1016/j.jpowsour.2015.09.127
21. F. He, M. Hou, Z. Du, F. Zhu, X. Cao et al., Self-construction of efficient interfaces ensures high-performance direct ammonia protonic ceramic fuel cells. Adv. Mater. 35(42), 2304957 (2023). https://doi.org/10.1002/adma.202304957
22. S. Oh, D. Kim, H.J. Ryu, K.T. Lee, A novel high-entropy perovskite electrolyte with improved proton conductivity and stability for reversible protonic ceramic electrochemical cells. Adv. Funct. Mater. 34(17), 2311426 (2024). https://doi.org/10.1002/adfm.202311426
23. Y. Wang, M.J. Robson, A. Manzotti, F. Ciucci, High-entropy perovskites materials for next-generation energy applications.

© The authors https://doi.org/10.1007/s40820-026-02194-9



Nano-Micro Lett. (2026) 18:335
Page 15 of 15  335

Joule 7(5), 848–854 (2023). https://doi.org/10.1016/j.joule.2023.03.020

cells: a comprehensive review. Adv. Mater. 37(48), 2418620 (2025). https://doi.org/10.1002/adma.202418620

1. D. Kim, I. Jeong, S. Ahn, S. Oh, H.-N. Im et al., On the role of bimetal-doped BaCoO3−δ perovskites as highly active oxygen electrodes of protonic ceramic electrochemical cells. Adv. Energy Mater. 14(14), 2304059 (2024). https://doi.org/10.1002/aenm.202304059
2. K. Okura, T. Okanishi, H. Muroyama, T. Matsui, K. Eguchi, Ammonia decomposition over nickel catalysts supported on rare-earth oxides for the on-site generation of hydrogen. ChemCatChem 8(18), 2988–2995 (2016). https://doi.org/10.1002/cctc.201600610
3. G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 54(16), 11169–11186 (1996). https://doi.org/10.1103/physrevb.54.11169
4. H.J. Monkhorst, J.D. Pack, Special points for Brillouin-zone integrations. Phys. Rev. B 13(12), 5188–5192 (1976). https://doi.org/10.1103/physrevb.13.5188
5. D. Marrocchelli, N.H. Perry, S.R. Bishop, Understanding chemical expansion in perovskite-structured oxides. Phys. Chem. Chem. Phys. 17(15), 10028–10039 (2015). https://doi.org/10.1039/c4cp05885b
6. H. Lv, L. Lin, X. Zhang, Y. Song, H. Matsumoto et al., In situ investigation of reversible exsolution/dissolution of CoFe alloy nanoparticles in a Co-doped Sr2Fe1.5Mo0.5O6−δ cathode for CO2 electrolysis. Adv. Mater. 32(6), 1906193 (2020). https://doi.org/10.1002/adma.201906193
7. K.J. Kim, C. Lim, K.T. Bae, J.J. Lee, M.Y. Oh et al., Concurrent promotion of phase transition and bimetallic nanocatalyst exsolution in perovskite oxides driven by Pd doping to achieve highly active bifunctional fuel electrodes for reversible solid oxide electrochemical cells. Appl. Catal. B Environ. 314, 121517 (2022). https://doi.org/10.1016/j.apcatb.2022.121517
8. J. Kudrnovský, V. Drchal, P. Bruno, Magnetic properties of FCC Ni-based transition metal alloys. Phys. Rev. B 77(22), 224422 (2008). https://doi.org/10.1103/physrevb.77.224422
9. S.A. Theofanidis, V.V. Galvita, M. Sabbe, H. Poelman, C. Detavernier et al., Controlling the stability of a Fe–Ni reforming catalyst: structural organization of the active components. Appl. Catal. B Environ. 209, 405–416 (2017). https://doi.org/10.1016/j.apcatb.2017.03.025
10. S.S. Aamlid, M. Oudah, J. Rottler, A.M. Hallas, Understanding the role of entropy in high entropy oxides. J. Am. Chem. Soc. 145(11), 5991–6006 (2023). https://doi.org/10.1021/2c11608
11. X. Chen, Y. Tan, Z. Li, T. Liu, Y. Song et al., Advanced air electrodes for reversible protonic ceramic electrochemical cells: a comprehensive review. Adv. Mater. 37(48), 2418620 (2025). https://doi.org/10.1002/adma.202418620
12. A. Hu, C. Yang, Y. Li, K. Xia, Y. Tian et al., High-entropy driven self-assembled dual-phase composite air electrodes with enhanced performance and stability for reversible protonic ceramic cells. Adv. Energy Mater. 15(22), 2405466 (2025). https://doi.org/10.1002/aenm.202405466
13. J. Qiao, H. Chen, Z. Wang, W. Sun, H. Li et al., Enhancing the catalytic activity of Y0.08Sr0.92TiO3–δ anodes through in situ Cu exsolution for direct carbon solid oxide fuel cells. Ind. Eng. Chem. Res. 59(29), 13105–13112 (2020). https://doi.org/10.1021/acs.iecr.0c02203
14. Z. Li, C. Wang, I.T. Bello, M. Guo, N. Yu et al., Direct ammonia protonic ceramic fuel cell: a modelling study based on elementary reaction kinetics. J. Power. Sources 556, 232505 (2023). https://doi.org/10.1016/j.jpowsour.2022.232505
15. Z. Liu, M. Tao, M. Xiao, J. Li, R. Xu et al., Direct ammonia protonic ceramic fuel cells through heterogeneous interface engineering. Chem. Catal. 5(7), 101365 (2025). https://doi.org/10.1016/j.checat.2025.101365
16. Y. Song, J. Chen, M. Yang, M. Xu, D. Liu et al., Realizing simultaneous detrimental reactions suppression and multiple benefits generation from nickel doping toward improved protonic ceramic fuel cell performance. Small 18(16), 2200450 (2022). https://doi.org/10.1002/smll.202200450
17. H.J. Jeong, W. Chang, B.G. Seo, Y.S. Choi, K.H. Kim et al., High-performance ammonia protonic ceramic fuel cells using a Pd inter-catalyst. Small 19(22), e2208149 (2023). https://doi.org/10.1002/smll.202208149
18. D. Feng, T. Zhu, M. Li, V.K. Peterson, H. Rabiee et al., K and Mg Co-doped perovskite oxide for enhanced anode of direct ammonia protonic ceramic fuel cell. Int. J. Hydrogen Energy 88, 272–278 (2024). https://doi.org/10.1016/j.ijhydene.2024.09.186
19. W. Sheng, M. Fei, W. Chen, Z. Chen, D. Liu et al., A new efficient and anti-sintering perovskite oxide-based internal catalyst for tubular direct-ammonia protonic ceramic fuel cells. J. Power. Sources 642, 237008 (2025). https://doi.org/10.1016/j.jpowsour.2025.237008
20. B. Wu, X. Yu, Z. Zhao, B. He, Z. Jin et al., Improving the catalytic activity and sintering resistance of Ni-BaCe0.7Zr0.1Y0.1Yb0.1O3–cermet anode for ammonia-fueled protonic ceramic fuel cells via cobalt addition. Chem. Eng. J. 507, 160757 (2025). https://doi.org/10.1016/j.cej.2025.160757

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


