ARTICLE

https://doi.org/10.1007/s40820-026-02194-9

# Entropy‑Modulated Oxide–Metal Catalyst Architectures for Direct Ammonia Protonic Ceramic Fuel Cells

![](images/cc1dc92ac353f122213657c72f84775b95e23844190732120894845d85a6f819.jpg)

Cite as Nano-Micro Lett. (2026) 18:335

Received: 22 January 2026 Accepted: 16 March 2026 © The Author(s) 2026

Dongyeon Kim<sup>1</sup>, Dong Jae Park<sup>2</sup>, Incheol Jeong<sup>3</sup>, Seeun Oh<sup>4</sup>, Hyeonggeun Kim<sup>4</sup>, Mincheol Lee<sup>4</sup>, Sang Won Lee<sup>2</sup>, Kangyong Lee<sup>4</sup>, Daehan Chung<sup>4</sup>, Ki‑Min Roh<sup>3</sup> <sup>\*</sup>, Joongmyeon Bae<sup>4</sup> <sup>\*</sup>, Tae Ho Shin<sup>2</sup> <sup>\*</sup>, Kang Taek Lee<sup>1,4,5</sup> <sup>\*</sup>

## HIGHLIGHTS

• Entropy-modulated oxide–metal catalyst exsolving Ni–Fe–Cu alloy nanoparticles from a high-entropy perovskite matrix enables eficient and durable ammonia decomposition.

• Density functional theory calculations reveal that the high-entropy oxide framework facilitates cation exsolution and lowers the kinetic barriers for $\mathrm { N H } _ { 3 }$ decomposition; additionally, the exsolved Ni–Fe–Cu alloy nanoparticles exhibit markedly higher catalytic activity than single-metal surfaces.

• Direct ammonia protonic ceramic fuel cells (DA-PCFCs) incorporating the Sr Fe $_ 1 \mathrm { M o _ { 0 . 2 } M n _ { 0 . 2 } C r _ { 0 . 2 } C u _ { 0 . 2 } N i _ { 0 . 2 } O _ { 6 - \delta } }$ (SFMMCCN) catalyst layer achieve a record-high power density of 2.04 $\mathrm { \Delta W } \mathrm { c m } ^ { - 2 }$ at $7 0 0 ~ ^ { \circ } \mathrm { C }$ with stable operation for over 255 h under $\mathrm { N H } _ { 3 }$ fuel, demonstrating the efectiveness of the entropy-modulated catalyst in designing durable and high-performance DA-PCFCs for carbon-free ammonia-to-power technologies.

ABSTRACT Protonic ceramic fuel cells (PCFCs) operating on $\mathrm { N H } _ { 3 }$ present a promising carbon-free energy pathway, yet their performance is often constrained by limited catalytic activity and degradation of conventional Ni-based anodes. Here, we report a high-entropy perovskite catalyst, $\mathrm { S r _ { 2 } F e _ { 1 } M o _ { 0 . 2 } M n _ { 0 . 2 } C r _ { 0 . 2 } C u _ { 0 . 2 } N i _ { 0 . 2 } O _ { 6 - \delta } }$ (SFM-MCCN), employed as an anode catalyst layer in direct ammonia-fed PCFCs. Upon reduction, SFMMCCN undergoes in situ exsolution of Ni–Fe–Cu alloy nanoparticles within a stable oxide matrix. This architecture provides synergistic enhancement of

![](images/2c9da2a14784f2f6062d054a12bfe551bb995430c38dc9998d0c9822649237df.jpg)

![](images/d64eab02a99d7836df158243a9f1ddf274ce36566eb15d8266e557edca2e4c49.jpg)

NH adsorption and decomposition through the combined efects of abundant surface acid sites and catalytically active alloy interfaces As a result, the SFMMCCN cell achieves a record peak power density of 2.04 $\mathrm { \Delta W ~ c m } ^ { - 2 }$ at $7 0 0 ^ { \circ } \mathrm { C }$ and demonstrates excellent operationa stability for over 255 h at $6 0 0 ~ ^ { \circ } \mathrm { C }$ under $\mathrm { N H } _ { 3 }$ fuel. Compared to a bare cell, it exhibits significantly reduced polarization resistance and efectively suppresses Ni coarsening. Density functional theory calculations reveal that the high-entropy oxide framework, together wit the exsolved Ni–Fe–Cu alloy, lowers the energy barriers for $\mathrm { N H } _ { 3 }$ decomposition, thereby accelerating overall catalytic kinetics. These findings highlight entropy-controlled oxide–metal architectures as a powerful strategy to achieve both high performance and durability in $\mathrm { N H } _ { 3 } .$ -fueled electrochemical systems, ofering a viable pathway toward scalable and eficient hydrogen-based power generation.

KEYWORDS Protonic ceramic fuel cells (PCFCs); Ammonia; High-entropy perovskite; Anode catalyst layer; Density functional theory

## 1 Introduction

The global transition toward decarbonization and reduced reliance on fossil fuel intensified interest in hydrogen as a clean and versatile energy carrier [1]. Within this context, protonic ceramic fuel cells (PCFCs) have emerged as promising electrochemical devices that directly convert hydrogen into electricity through proton conduction, ofering high eficiency and environmentally benign operation [2]. Despite these advantages, the large-scale adoption of hydrogen faces substantial challenges, including energy-intensive production pathways and limited distribution infrastructure [3]. Common delivery strategies—such as compression, liquefaction, or chemical storage in hydrides and carbonaceous compounds—remain technologically complex and economically unattractive [4].

Beyond hydrogen, carbon-based fuels such as methane and natural gas can be supplied to fuel cells, benefiting from fast kinetics and well-established distribution networks [5]. However, their utilization inevitably generates $\mathrm { C O } _ { 2 }$ and other pollutants, which conflict with increasingly stringent environmental regulations. Ammonia $\left( \mathrm { N H } _ { 3 } \right)$ has therefore attracted considerable attention as an alternative energy carrier, due to its carbon-free composition, hydrogen-rich nature, favorable energy density, low flammability, and compatibility with existing large-scale storage and transport infrastructure [6, 7]. Leveraging these properties, direct ammonia-fed PCFCs (DA-PCFCs) operating at intermediate temperatures provide notable advantages, including higher system eficiency and reduced balance-of-plant complexity. Unlike conventional solid oxide fuel cells (SOFCs), which rely on oxygen-ion transport [8], the proton conduction mechanism of PCFCs inherently suppresses $\mathrm { N O } _ { \mathrm { x } }$ formation during ammonia utilization [9]. This synergy highlights DA-PCFCs as a particularly attractive pathway for clean and scalable power generation [10]. Nevertheless, the practical realization of DA-PCFCs is hindered by inadequate catalytic activity of conventional anodes toward NH $\mathrm { N H } _ { 3 }$ decomposition. Ni-based cermet anodes, widely employed in PCFCs, show poor intrinsic activity, leading to incomplete conversion of $\mathrm { N H } _ { 3 }$ to $\Nu _ { 2 }$ and $\mathrm { H } _ { 2 }$ . This results in nitridation of metallic Ni to nickel nitride $( \mathrm { N i } _ { 3 } \mathrm { N } )$ via the reaction: $\mathrm { N H } _ { 3 } + 3 \mathrm { N i }$ $ \mathrm { N i } _ { 3 } \mathrm { N } + 1 . 5 \mathrm { H } _ { 2 } \ : [ 1 1 ]$ . Because $\mathrm { N i } _ { 3 } \mathrm { N }$ is unstable in $\mathrm { H } _ { 2 } .$ -rich atmospheres, it readily reverts to Ni [12], causing cyclic phase transformations that induce structural degradation within the anode framework [13]. Over time, these processes undermine both catalytic eficiency and electrochemical stability, posing a critical obstacle to the reliable operation of DA-PCFC systems [14].

To overcome these limitations, surface engineering approaches have been explored to improve $\mathrm { N H } _ { 3 }$ decomposition kinetics. One strategy involves generating catalytically active nanoparticles on the anode surface. For instance, Liu et  al. developed a $\mathrm { N i  – B a ( Z r _ { 0 . 1 } C e _ { 0 . 7 } Y _ { 0 . 1 } Y b _ { 0 . 1 } ) _ { 0 . 9 4 } R u _ { 0 . 0 3 } F }$ $\mathrm { e } _ { 0 . 0 3 } \mathrm { O } _ { 3 - \delta }$ (BZCYYbRF) anode, where Ru and Fe co-doping facilitated the exsolution of RuFe alloy nanoparticles under reducing conditions, yielding a peak power density of 807 mW $\mathrm { c m } ^ { - 2 }$ at $6 5 0 ~ ^ { \circ } \mathrm { C }$ with $\mathrm { N H } _ { 3 }$ fuel [15]. Similarly, Shao et  al. reported a $\mathrm { N i  – B a ( Z r _ { 0 . 1 } C e _ { 0 . 7 } Y _ { 0 . 1 } Y b _ { 0 . 1 } ) _ { 0 . 9 5 } P d _ { 0 . 0 5 } O _ { 3 - \delta } }$ (BZCYYbPd) anode, in which Pd incorporation enhanced ammonia decomposition activity and improved overall performance [16]. Infiltration-based methods have also been pursued; for example, $\mathrm { R u } _ { 0 . 9 5 } \mathrm { C u } _ { 0 . 0 5 } \mathrm { N i } _ { \mathrm { x } }$ (RCN) nanoparticles introduced via one-step infiltration improved long-term stability, reducing the voltage degradation rate to 0.016 V over 100 h, compared to 0.095 V in the pristine anode [17]. Nevertheless, the reliance on noble metals such as Ru and Pd raises cost concerns [18], and challenges including direct $\mathrm { N H } _ { 3 } – \mathrm { N i }$ interactions and Ni particle agglomeration persist [10].

Recent studies have demonstrated that interface engineering is an efective route to improving the activity and durability of non-noble metal catalysts for ammonia decomposition. Engineered metal–oxide interfaces, in turn, regulate surface reaction energetics and stabilize active sites under harsh $\mathrm { N H } _ { 3 }$ environments [9, 19]. Alternatively, beyond tailoring local interfacial chemistry, the incorporation of an anode catalyst layer (ACL) has been proposed as a complementary strategy to spatially decouple $\mathrm { N H } _ { 3 }$ decomposition from the Ni-based anode, thereby minimizing direct ${ \mathrm { N i - N H } } _ { 3 }$ contact and enhancing chemical stability [20, 21]. Pan et al. demonstrated tubular PCFCs employing a catalytic Fe layer, which suppressed $\mathrm { N i } _ { 3 } \mathrm { N }$ formation and improved durability. Density functional theory (DFT) calculations further revealed that Fe promotes $\mathrm { N H } _ { 3 }$ decomposition due to its favorable nitrogen adsorption energetics [22]. More recently, Mo-containing perovskite oxides such as $\mathrm { S r } _ { 2 } \mathrm { F e } _ { 2 - \mathrm { x } } \mathrm { M o } _ { \mathrm { x } } \mathrm { O } _ { 6 - \delta }$ 2 (SFM) have emerged as attractive ACL candidates, as Moinduced acidic sites accelerate $\mathrm { N H } _ { 3 }$ decomposition [9, 23]. He et al. reported that a $\mathrm { S r } _ { 2 } \mathrm { F e } _ { 1 . 3 5 } \mathrm { M o } _ { 0 . 4 5 } \mathrm { C u } _ { 0 . 2 } \mathrm { O } _ { 6 - \delta }$ (SFMC) layer, integrated atop a Ni-BZCYYb anode, delivered excellent performance above $6 5 0 ~ ^ { \circ } \mathrm { C } .$ Under reducing conditions, exsolved Fe and Cu nanoparticles alloyed with Ni, producing highly active Ni–Cu and Ni–Fe species that markedly improved $\mathrm { N H } _ { 3 }$ conversion [24]. Building on these findings, we hypothesized that co-doping SFM with both acidic and reducible elements could synergistically maximize catalytic eficiency for $\mathrm { N H } _ { 3 }$ decomposition. Acidic dopants more potent than Mo may promote N–H bond cleavage, while reducible elements with strong exsolution tendencies can generate highly active metallic species under operating conditions. Furthermore, adopting a high-entropy oxide design—incorporating five or more equimolar cations—may introduce entropy-stabilization efects, thereby improving long-term durability under fuel cell conditions [25, 26].

In this study, we designed and synthesized a highentropy perovskite oxide catalyst, $\mathrm { S r } _ { 2 } \mathrm { F e } _ { 1 } \mathrm { M o } _ { 0 . 2 } \mathrm { M n } _ { 0 . 2 } \mathrm { C r } _ { 0 . 2 }$ $\mathrm { C u } _ { 0 . 2 } \mathrm { N i } _ { 0 . 2 } \mathrm { O } _ { 6 - \delta }$ (SFMMCCN), incorporating Mn and Cr as acidic dopants and Cu and Ni as reducible dopants. SFM-MCCN was systematically evaluated as an ACL for DA-PCFCs. Structural integrity and entropy-stabilization efects were confirmed through comprehensive physicochemical characterization, while catalytic activity and durability toward $\mathrm { N H } _ { 3 }$ decomposition were assessed under relevant fuel conditions. Complementary DFT calculations provided mechanistic insights into the role of entropy-driven design in promoting $\mathrm { N H } _ { 3 }$ decomposition kinetics. Finally, a full DA-PCFC incorporating SFMMCCN as the ACL was fabricated, demonstrating strong functional viability in practical cell operation.

## 2 Experimental Section

## 2.1 Material Preparation

Powders of $\mathrm { S r } _ { 2 } \mathrm { F e } _ { 1 . 5 } \mathrm { M o } _ { 0 . 5 } \mathrm { O } _ { 6 - \delta }$ (SFM), $\mathrm { S r } _ { 2 } \mathrm { F e } _ { 1 } \mathrm { M o } _ { 0 . 6 }$ $\mathrm { C u } _ { 0 . 2 } \mathrm { N i } _ { 0 . 2 } \mathrm { O } _ { 6 - \delta }$ (SFMCN), and SFMMCCN were synthesized via a sol–gel process. For SFM, high-purity $\mathrm { S r } ( \mathrm { N O } _ { 3 } ) _ { 2 } ,$ $\mathrm { F e ( N O _ { 3 } ) _ { 3 } \cdot 9 H _ { 2 } O }$ , and $( \mathrm { N H } _ { 4 } ) _ { 2 } \mathrm { M o O } _ { 4 }$ were used as cation precursors. For SFMMCCN, the same precursors were combined with $\mathbf { M n } ( \mathbf { N O } _ { 3 } ) _ { 2 } { \cdot } 6 \mathbf { H } _ { 2 } \mathbf { O }$ $\mathrm { C r } ( \mathrm { N O } _ { 3 } ) _ { 3 } { \cdot } 9 \mathrm { H } _ { 2 } \mathrm { O }$ $\mathrm { C u } ( \mathrm { N O } _ { 3 } ) _ { 2 } { \cdot } 3 \mathrm { H } _ { 2 } \mathrm { O }$ , and $\mathrm { N i } ( \mathrm { N O } _ { 3 } ) _ { 2 } { \cdot } 6 \mathrm { H } _ { 2 } \mathrm { O }$ in the appropriate molar ratios. All precursors were dissolved in deionized water at $8 0 ~ ^ { \circ } \mathrm { C }$ , after which ethylenediaminetetraacetic acid (EDTA) and citric acid were introduced. The solution $\mathrm { p H }$ was adjusted to 8 by the controlled addition of ammonia.

The gel formed upon evaporation was heated at $3 0 0 ~ ^ { \circ } \mathrm { C }$ for 2 h, and the resulting precursor was calcined at $1 0 0 0 ^ { \circ } \mathrm { C }$ for 5 h to obtain a phase-pure perovskite. The powders were subsequently ball-milled in ethanol to produce fine particles. The $\mathrm { B a S c _ { 0 . 1 } T a _ { 0 . 1 } C o _ { 0 . 8 } O _ { 3 - \delta } }$ (BSTC) cathode was synthesized by a solid-state reaction using stoichiometric precursor compositions [27].

## 2.2 Physicochemical Characterizations

High-resolution X-ray difraction (XRD) was performed using $\mathrm { C u - K } \alpha _ { 1 }$ radiation and a Ge (111) monochromator over a 2θ range of $2 0 ^ { \circ } - 8 0 ^ { \circ }$ . The microstructure of SFM-MCCN pellets and single cells was examined by scanning electron microscopy (SEM) with energy-dispersive X-ray spectroscopy (EDS) (JEOL, JSM-IT800). Atomic-scale features were further investigated using a high-resolution transmission electron microscope (HR-TEM; Thermo Fisher, Spectra Ultra). X-ray photoelectron spectroscopy (XPS; K-Alpha, Thermo VG Scientific) with monochromatic Al Kα radiation was employed to determine the valence states of the elements. $\mathrm { N H } _ { 3 }$ temperature-programmed desorption $( \mathrm { N H } _ { 3 } – \mathrm { T P D } )$ was performed on samples pretreated at $5 0 0 ^ { \circ } \mathrm { C }$ in He for 2 h, reduced at $7 0 0 ~ ^ { \circ } \mathrm { C }$ in $\mathrm { H } _ { 2 }$ for 2 h, and then exposed to $\mathrm { N H } _ { 3 }$ . Desorption was monitored during heating at $1 0 ~ ^ { \circ } \mathrm { C }$ min⁻<sup>1</sup> using an AutoChem II 2920 (Micromeritics).

## 2.3 Catalytic Activity Test

The catalytic activities of SFM, SFMMCCN, and $\mathrm { N i { - } B a Z r _ { 0 . 4 } C e _ { 0 . 4 } Y _ { 0 . 1 } Y b _ { 0 . 1 } O _ { 3 - \delta } }$ (BZCYYb) were evaluated in a fixed-bed quartz reactor. Each catalyst powder (0.2 g) was pre-reduced in a flow of $\mathrm { H } _ { 2 }$ (50 sccm) at $7 0 0 ~ ^ { \circ } \mathrm { C }$ for 2 h, followed by the introduction of $\mathrm { N H } _ { 3 }$ (20 sccm). The specific surface areas of all catalysts were determined by Brunauer–Emmett–Teller (BET) $\Nu _ { 2 }$ adsorption measurements (Fig. S1). The $\mathrm { N H } _ { 3 }$ decomposition ratio was measured as a function of temperature. Residual $\mathrm { N H } _ { 3 }$ and $\mathrm { H } _ { 2 } \mathrm { O }$ in the efluent were removed using dilute ${ \mathrm { H } } _ { 2 } { \mathrm { S O } } _ { 4 }$ solution and $\mathrm { C a S O _ { 4 } }$ absorbent, respectively. Efluent gas composition was measured with a mass flow meter (Bronkhorst, Ruurlo, Netherlands). The $\mathrm { N H } _ { 3 }$ conversion eficiency, corresponding to a theoretical product ratio of 75% $\mathrm { H } _ { 2 }$ and 25% $\Nu _ { 2 } .$ , was determined by the following Eq. (1)

$\mathrm { N H } _ { 3 }$ conversion $( \% ) = { \frac { F _ { \mathrm { o u t } } } { 2 F _ { \mathrm { i n } } } } \times 1 0 0 $

(1)

where $F _ { \mathrm { i n } }$ and $F _ { \mathrm { o u t } }$ denote the inlet and outlet gas flow rates, respectively [28].

## 2.4 Computational Details

The DFT calculations were conducted with the Vienna ab  initio simulation package (VASP) [29]. The Perdew–Burke–Ernzerhof generalized gradient approximation (GGA-PBE) was considered for the exchange–correlation functionals. Valence configurations were $4 p ^ { 6 } 3 d ^ { 6 } 4 s ^ { 1 }$ for Mn, $4 p ^ { 6 } 3 d ^ { 5 } 4 s ^ { 1 }$ for $\mathrm { C r } , 3 d ^ { 1 0 } 4 s ^ { 1 }$ for $\mathrm { C u } , 3 d ^ { 9 } 4 s ^ { 1 }$ for Ni, $4 s ^ { 2 } 4 p ^ { 6 } 4 d ^ { 5 } 5 s ^ { 1 }$ for Mo, $4 s ^ { 2 } 4 p ^ { 6 } 5 s ^ { 2 }$ for $\mathrm { S r } , 3 d ^ { 6 } 4 s ^ { 1 }$ for Fe, and $2 s ^ { 2 } p ^ { 4 }$ for O. DFT + U approach was applied and the values employed for Mn, Cr, Cu, Ni, Mo, and Fe were 3.9, 3.7, 4.0, 6.2, 4.38, and 5.3 eV, respectively. Plane waves with an energy cutof of 450 eV were used. A Monkhorst–Pack [30] k-point mesh of $1 \times 2 \times 1$ and $3 \times 3 \times 1$ was applied to the 156-atom perovskite and 54-atom metal (Ni and $\mathrm { N i - F e { \mathrm { - } } C u ) }$ slabs, respectively. The convergence threshold for electronic selfconsistent iterations was $1 0 ^ { - 6 } \mathrm { e V } \mathrm { c e l l ^ { - 1 } }$ . Cell parameters and atomic positions were relaxed until the remaining force was less than $1 \times 1 0 ^ { - 1 } \ \mathrm { e V } \ \mathring { \mathrm { A } } ^ { - 1 }$ . Each slab was separated along the z-axis by $\mathrm { ~ a ~ } 2 0 \mathring \mathrm { A }$ of vacuum region. $\mathrm { N H } _ { 3 }$ adsorption sites were determined by identifying those with the lowest energy cost among all possible cation sites in perovskites and atop, bridge, FCC, and HCP sites in metals.

## 2.5 Single Cell Fabrication

Anode-supported protonic ceramic fuel cells (PCFCs) were fabricated in a multilayer configuration consisting of a NiO–BZCYYb anode, a NiO–BZCYYb anode functional layer, a BZCYYb electrolyte, and a BSTC cathode. For the supporting layer slurry, NiO (Sumitomo) and BZCYYb powder (Kceracell) were blended at a 6:4 weight ratio, followed by sequential addition of ethanol and toluene as solvents, Hypermer KD-1 (CRODA) as a dispersant, polyvinyl butyral (Eastman Chemical Company) as a binder, di-n-butyl phthalate (Junsei) as a plasticizer, and poly(methyl methacrylate) (Sunjin Chemical) as a pore former. Slurries for the functional layer and electrolyte (prepared without pore former) were produced using the same procedure. The resulting slurries were tape-cast, dried, and laminated to form green tapes. These laminates were pre-sintered at $9 0 0 ~ ^ { \circ } \mathrm { C }$ for 3 h to remove organic components then sintered at $1 4 0 0 ^ { \circ } \mathrm { C }$ for 5 min in a microwave furnace (Unicera, UMF-04; 2.45 GHz, 2 kW). The SFMMCCN anode catalyst layer (ACL) ink was prepared by mixing SFMMCCN powder with a commercial binder system (ElectroScience, 441 ESL), which was brushcoated onto the anode surface and sintered at $9 5 0 ~ ^ { \circ } \mathrm { C }$ for 3 min in a microwave furnace. The BSTC cathode slurry was then screen-printed onto the electrolyte and sintered at $8 5 0 ~ ^ { \circ } \mathrm { C }$ for 3 min in a microwave furnace.

## 2.6 Electrochemical Characterizations

Single cells were afixed to an alumina tube and sealed hermetically with Ceramabond 571 (Aremco). Prior to electrochemical testing of the DA-PCFCs, the anode was reduced in humidified H (3% $\mathrm { H } _ { 2 } \mathrm { O } .$ 50 sccm) and subsequently exposed to $\mathrm { N H } _ { 3 }$ (50 sccm), while the BSTC cathode was supplied with humidified air $( 3 \% \mathrm { ~ H } _ { 2 } \mathrm { O } ;$ , 50 sccm). Current–voltage (I–V) curves and electrochemical impedance spectroscopy (EIS) were recorded using a potentiostat (Bio-Logic, VMP-300). EIS spectra were collected over a frequency range of 1 MHz–0.1 Hz with an AC perturbation amplitude of 50 mV.

## 3 Results and Discussion

## 3.1 Physicochemical Characterization of the Material

SFM and SFMMCCN, were synthesized via a sol–gel method. Figure 1a presents the XRD patterns. The results confirm the formation of well-defined double perovskite structures in both materials, indicating successful incorporation of $\mathrm { M n , C r , C u }$ , and Ni into the SFM lattice without secondary phases. To probe the structural evolution under reduction conditions, in situ high-temperature XRD (HT-XRD) was performed in 3% $\mathrm { H } _ { 2 } / \mathrm { A r }$ from room temperature (RT) to $7 0 0 ~ ^ { \circ } \mathrm { C } .$ . As shown in Fig. 1b, c, the lattice progressively expands with increasing temperature, reflecting the combined contributions of thermal expansion and reduction-induced chemical expansion [31]. Notably, a new difraction feature emerges near $4 4 ^ { \circ }$ above $4 0 0 ~ ^ { \circ } \mathrm { C }$ consistent with the nucleation of a metallic phase via exsolution. In contrast, no additional difraction peaks associated with exsolved metallic species were detected for SFM after reduction (Fig. S2). To validate these findings under PCFC operating conditions, SFMMCCN pellets were reduced at $7 0 0 ~ ^ { \circ } \mathrm { C }$ in pure $\mathrm { H } _ { 2 }$ . The SEM images (Fig. 1d, e) reveal a pronounced surface transformation: the pristine surface evolves into one decorated with dense, uniformly distributed nanoparticles after reduction. This confirms the successful activation of exsolution under practical thermal and chemical conditions. Furthermore, particle size distribution analysis indicates an average nanoparticle radius of \~ 20.4 nm, underscoring both the high dispersion and nanoscale uniformity of the exsolved phase (Fig. 1f).

a  
![](images/4580fe908dd7ff07ae355f56b3deecba735cec2bb0a58bfd4b8e21e1dabbc522.jpg)

b  
![](images/6cc72f53f0509c9d8f4b7626ee9bfc56807b7024fb942c2c4a36c3f69bda2c1b.jpg)  
C

![](images/aca1db32060a40f160a24280a18446a116b7ae034195b4e5fbb0bdf4ad6b55c2.jpg)

d  
![](images/1595e82a4eafffc0e18c5acee89bb24611dd2315150be1294eabff1ec34a336b.jpg)  
e

![](images/b30d034233693bef8f6b2f8a261837b7894b45a629e837056c4a6de56e04f80a.jpg)

f  
![](images/804eb14a6c821bf959c2eacb6d7e24ecfe3e85f545584a893e97ca4204fc9caf.jpg)  
Fig. 1 a XRD patterns of the as-synthesized SFM and SFMMCCN. In situ HT-XRD b patterns and c contour plot of SFMMCCN under reduc ing atmosphere (3% $\mathrm { H } _ { 2 } / \mathrm { A r } )$ from RT to $7 0 0 ~ ^ { \circ } \mathrm { C } .$ SEM images of the SFMMCCN pellet surface in the d as-synthesized and e after reduction. f Particle size distribution histogram of exsolved nanoparticles on the surface of the reduced SFMMCCN pellet

Figure 2a displays the HR-TEM image of reduced SFM-MCCN, revealing a well-defined perovskite lattice with distinct sublattices occupied by multiple transition-metal cations. After reduction, finely dispersed nanoparticles were observed within the bulk matrix. High-angle annular dark-field scanning transmission electron microscopy (HAADF-STEM) combined with the EDS confirms a uniform elemental distribution across the reduced perovskite oxide, validating the successful incorporation of Mn, Cr, Cu, and Ni into the B-site lattice. Figure 2b shows the HR-TEM lattice fringe of an exsolved nanoparticle. The measured d-spacing of 0.28 nm corresponds to the (110) plane of the perovskite phase, indicating coherent lattice integration between the nanoparticle and the host matrix. The nanoparticle exhibited an average diameter of\~ 20 nm, with robust particle–matrix interfaces that mitigate detachment and aggregation—two key degradation pathways that typically compromise long-term catalytic performance [32, 33]. Figure 2c further provides EDS elemental maps of the exsolved nanoparticles, showing homogeneous distributions of Ni, Fe, and Cu, consistent with the formation of a Ni–Fe–Cu alloy. Additional structural confirmation is presented in Fig. S3, where HR-TEM and fast Fourier transform (FFT) analysis suggest that the exsolved phase adopts a face-centered cubic (FCC) structure, in agreement with reported Ni-based alloys [34, 35].

To characterize the atomic distribution and calculate configurational entropy $( \Delta \mathrm { { S _ { c o n f g } ) } }$ of both the exsolved alloy and the bulk perovskite, STEM-EDS analysis was performed (Fig. S4–S6). The $\Delta S _ { \mathrm { c o n f i g } }$ of metallic alloys is calculated using Eq. (2) [36]:

e  
a  
![](images/40abd9cead712ca5b1218aa4ef799303d5345eb0bac7290da99f293de32c13e9.jpg)  
b

d  
![](images/833234ce5fca809b13a5e75a5b483b2397854bfc59a8491a389cffd0f3caea69.jpg)

![](images/fd5faa89da7e26f62d1bedf24d5bfb02d373eeda8963379fd3a8ef88756a7923.jpg)

![](images/a8f280bf60f3bbc709c016d5e9a150e1786845339bc52af94b633c0ce407a50f.jpg)  
Fig. 2 a HR-TEM, HAADF-STEM and elemental mapping images of reduced SFMMCCN powder. b HR-TEM, lattice fringe, and c HAADF-STEM and EDS mapping images of exsolved nanoparticles. d Configuration entropy of the pristine and reduced SFMMCCN. e Schematic illustration of the in situ entropy-controlled process

$$
\Delta S _ {\mathrm{config}} = - R \sum_ {\mathrm{i} = 1} ^ {\mathrm{N}} x _ {\mathrm{i}} l n x _ {\mathrm{i}}\tag{2}
$$

where R is the gas constant, N denotes the number of constituent elements, and $x _ { \mathrm { i } }$ is the mole fraction of the i-th component. Based on this metric, alloys are classified as high-, medium-, or low-entropy systems when $\Delta \mathrm { \Delta S _ { c o n f i g } \geq }$

1.5R, $1 . 0 \mathrm { R } \leq \Delta \mathrm { S } _ { \mathrm { c o n f i g } } \leq 1 . 5 \mathrm { R }$ , and $\Delta \mathrm { \Delta S _ { c o n f i g } } \le 1 . 0 \mathrm { R }$ , respectively [37]. For perovskite oxides, $\Delta S _ { \mathrm { c o n f i g } }$ can similarly be expressed as Eq. (3) [38]:

$$
\Delta S _ {\text { config }} = - R \left[ \left(\sum_ {a = 1} ^ {A} x _ {a} l n x _ {a} + \sum_ {b = 1} ^ {B} x _ {b} l n x _ {b}\right) _ {\text { cation }} + \left(\sum_ {c = 1} ^ {C} x _ {c} l n x _ {c}\right) _ {\text { anion }} \right]\tag{3}
$$

where A and B denote the number of species occupying the A- and B-sites, respectively, C the number of anion types, and $x _ { \mathrm { a } } , x _ { \mathrm { b } } ,$ and $x _ { \mathrm { c } }$ the mole fractions. As shown in Fig. 2d, pristine SFMMCCN exhibits a configurational entropy of 1.60 R, qualifying as a high-entropy perovskite oxide (HEPO). Upon reduction, the bulk retains a high-entropy state, albeit slightly lower at 1.50 R. In contrast, the exsolved Ni–Fe–Cu alloy displays a medium-entropy value of 1.09 R. The schematic in Fig. 2e illustrates this entropy-controlled process: under reducing conditions, selective exsolution of a medium-entropy alloy occurs from the high-entropy oxide matrix.

The XPS analysis was employed to investigate the valence states of the constituent elements in SFMMCCN before and after exposure to reducing conditions. All spectra were calibrated using the C 1s as a reference. As shown in Fig. 3a, characteristic binding energy signals corresponding to Sr, Fe, Mo, Mn, Cr, Cu, and Ni were consistently observed in both the pristine and reduced samples. Detailed spectral deconvolution of the Fe $2 p ,$ Cu $2 p .$ , and Ni $2 p$ regions is presented in Fig. 3b–d. In the pristine sample, only oxidized states of the transition metals were identified. After reduction at $7 0 0 ~ ^ { \circ } \mathrm { C }$ for 2 h in a pure $\mathrm { H } _ { 2 }$ atmosphere, additional features indicative of metallic species emerged. Specifically, a distinct $\mathrm { F e } ^ { 0 }$ peak appears at \~ 707 eV in the Fe 2p spectrum (Fig. 3b) [10]. The corresponding Fe $2 p$ fitting parameters are summarized in Table S1. In addition, the Cu $2 p$ spectra (Fig. 3c) revealed characteristic $\mathrm { C u } ^ { 0 }$ peaks near 933 and 953 eV [39]. Figure 3d displays the Ni 2p spectrum, where a peak at \~ 852 eV is assigned to metallic $\mathrm { N i } ^ { 0 }$ species [17]. Complementary XPS analyses of Mo, Mn, $\mathrm { C r } ,$ and O species before and after reduction are presented in Fig. S7. Collectively, these observations confirm the reduction of Ni, $\mathrm { F e , }$ and $\mathrm { C u } ,$ , leading to the in situ exsolution of a Ni–Fe–Cu alloy from the SFMMCCN perovskite matrix, consistent with the structural evidence in Fig. 2. The formation of this multi-metallic alloy is anticipated to significantly improve catalytic activity for ammonia decomposition through synergistic efects and enhanced surface reactivity compared to monometallic catalysts. A detailed evaluation of this catalytic performance is provided in the following section.

## 3.2 Catalytic Properties for $\mathbf { N H } _ { 3 }$ Decomposition

To assess the catalytic potential of SFMMCCN as an ACL in DA-PCFCs, its $\mathrm { N H } _ { 3 }$ conversion eficiency was compared against those of a low-entropy perovskite catalyst (SFM), a medium-entropy perovskite catalyst (SFMCN), and a bare anode (Ni-BZCYYb). Prior to testing, all materials were thermally treated at $7 0 0 ~ ^ { \circ } \mathrm { C }$ for 2 h under a pure $\mathrm { H } _ { 2 }$ atmosphere, identical to the conditions used during cell operation. As shown in Fig. 4a, SFMMCCN exhibits a remarkable $\mathrm { N H } _ { 3 }$ conversion of 96% at $6 0 0 ~ ^ { \circ } \mathrm { C } .$ far exceeding that of SFM (47%) and SFMCN (57%). Interestingly, the bare Ni-BZCYYb anode exhibits higher $\mathrm { N H } _ { 3 }$ conversion than SFM and SFMCN, reflecting the intrinsically high catalytic activ ity of metallic Ni toward $\mathrm { N H } _ { 3 }$ decomposition. These observations imply that the exceptional reactivity of SFMMCCN arises from the combined efects of high configurationa entropy and in situ formation of Ni–Fe–Cu alloy nanoparticles. Since surface acidity is a critical factor influencing $\mathrm { N H } _ { 3 }$ adsorption and subsequent decomposition, the $\mathrm { N H } _ { 3 }$ -TPD was performed. As depicted in Fig. 4b, SFMMCCN exhib ited a higher onset temperature compared to Ni-BZCYYb, signifying the presence of stronger acid sites favorable for $\mathrm { N H } _ { 3 }$ adsorption. Materials with stronger $\mathrm { N H } _ { 3 }$ adsorption generally facilitate more eficient surface reactions, thereby accelerating decomposition kinetics [40]. To exclude the possible contribution of exsolved alloy nanoparticles to the ${ \mathrm { N H } } _ { 3 } – \mathrm { T P D }$ response, additional control experiments were performed without prior $\mathrm { H } _ { 2 }$ reduction pretreatment, thereby minimizing alloy exsolution before the measurement (Figs. S8 and S9). Under these exsolution-suppressed conditions, SFMMCCN still exhibits an elevated $\mathrm { N H } _ { 3 }$ desorption onset compared with Ni-BZCYYb, indicating that the enhanced $\mathrm { N H } _ { 3 }$ adsorption is not governed by metallic nanoparticles. Moreover, comparison with the Mn- and Cr-free control sample (SFMCN) further confirms that the strengthened surface acidity originates from the intrinsic oxide matrix induced by Mn and Cr incorporation. The long term catalytic durability is shown in Fig. 4c. While SFM MCCN sustained nearly complete $\mathrm { N H } _ { 3 }$ conversion for over

a  
![](images/04bc39e0590d8dd3a9e74f8e707abfef8d41c89892e98d30b512abda3799c53e.jpg)

b  
![](images/7d05b09f560a51468b9e4726d676576de99122990826a958fdf25133f2a2e5d1.jpg)

C  
![](images/d00583f4cd652db3967b0459240f5553e7bf30e0f908869e99732a3465f765ff.jpg)

d  
![](images/3cb99ac8af890654443d288d54c37b01375358cd1c578d214dfb4e025db3ea3e.jpg)  
Fig. 3 XPS spectra of a survey, b Fe $2 p ,$ , c Cu ${ 2 p , }$ , and d Ni $2 p$ for SFMMCCN before and after reduction at $7 0 0 ^ { \circ } \mathrm { C }$ for 2 h in a 100% $\mathrm { H } _ { 2 }$ atmosphere

50 h at $6 0 0 ~ ^ { \circ } \mathrm { C } ,$ Ni-BZCYYb exhibited rapid deactivation within 20 h. This degradation is attributed to Ni nanoparticle coarsening, triggered by repeated phase nitridation $( \mathrm { N i }  $ $\mathrm { N i } _ { 3 } \mathrm { N } )$ and subsequent reversion to metallic Ni. Consistent with this mechanism, SEM analysis after durability testing (Fig. S10) revealed pronounced structural degradation of Ni-BZCYYb, whereas SFMMCCN preserved its morphology. Post-test XRD and STEM–EDS analyses further indicate that beyond the structural evolution of Ni, the Ni-BZCYYb undergoes phase separation of the BZCYYb component under $\mathrm { N H } _ { 3 }$ operation, accompanied by BaO formation (Figs. S11 and S12). In contrast, the SFMMCCN remains structurally and chemically intact after long-term operation, with no detectable secondary phases observed, indicating excellent phase stability (Figs. S13 and S14). XPS analysis further confirms that the chemical states of the exsolved Ni–Fe–Cu alloy nanoparticles are largely preserved after durability testing (Fig. S15).

## 3.3 DFT Analysis of $\mathbf { N H } _ { 3 }$ Decomposition and Exsolution Mechanism

Figure 4d and e display DFT calculation results to determine energy profiles for $\mathrm { N H } _ { 3 }$ decomposition on SFM and SFM-MCCN, respectively. The reaction pathway consists of 5 elementary steps including the adsorption of $\mathrm { N H } _ { 3 }$ (Eq. 4), a series of deprotonation generating hydrogen gas (Eqs. 5–7), and desorption of nitrogen (Eq. 8) as follows:

$$
^ {*} + \mathrm{NH} _ {3} (\mathrm{g}) \rightarrow^ {*} \mathrm{NH} _ {3}\tag{4}
$$

a  
![](images/4aefa1d52691edd538e0adab75dc80421c8fc0fd1e9d0c1865d5ffdefe246301.jpg)

b  
![](images/6eb0a6f822611b8a22582eb724da036c11a91ffdd11a401f85001b736b63c4b3.jpg)  
C

![](images/4950eab0259bd8c846db25335e0e68a0307d65c2afea88198a3675ce6fae666c.jpg)

d  
e  
![](images/89cdbc7ce2e8349e2398f5314944f91122e6015aa24c26f9f29272c6e9e4b4ed.jpg)

![](images/f9b984dfa0b62a8135986062469bf217873715d66aa57add3ef953468dec8172.jpg)

f  
![](images/1c637bbf28b74070ee452eae707fadcb0c33385ecd3e95c01a74bf2838c3eb02.jpg)

g  
![](images/eb901be464f214f7576077fd333593e7b77aa4c43a7a219e734a849f256ceedc.jpg)

![](images/1034efa8cb075c93b871d7e6c3c26f3a2e744240eeae2c96f7f903698d81206b.jpg)

![](images/6fe6ec3f313fcdbcd6933e736792a2ddc11eb9f8f737c18fa0f3063b2d4a2714.jpg)

j  
![](images/6394d88833c95413e4905240005441d32914843211ea9ebad0ebae7fa74a3e88.jpg)  
Fig. 4 a $\mathrm { N H } _ { 3 }$ conversion of SFM, SFMCN, SFMMCCN, and Ni-BZCYYb measured across the temperature range of 450–700 °C. b NH -TPD profiles and c durability test of SFMMCCN and Ni-BZCYYb. Energy profiles for $\mathrm { N H _ { \it 3 } }$ decomposition on d SFM and e SFMMCCN. f O 2p band center. g COHP profiles and average ICOHP values of cation–oxygen pairs. h ICOHP of high-entropy elements in SFMMCCN. O 2p band center. Energy profiles for $\mathrm { N H } _ { 3 }$ on i Ni and j Ni–Fe–Cu alloy

$$
^ {*} \mathrm{NH} _ {3} \rightarrow {} ^ {*} \mathrm{NH} _ {2} + \frac {1}{2} \mathrm{H} _ {2} (\mathrm{g})\tag{5}
$$

$$
^ {*} \mathrm{NH} _ {2} \rightarrow {} ^ {*} \mathrm{NH} + \frac {1}{2} \mathrm{H} _ {2} (\mathrm{g})\tag{6}
$$

$$
^ {*} \mathrm{NH} \rightarrow^ {*} \mathrm{N} + \frac {1}{2} \mathrm{H} _ {2} (\mathrm{g})\tag{7}
$$

$$
^ {*} \mathrm{N} \rightarrow^ {*} + \frac {1}{2} \mathrm{N} _ {2} (\mathrm{g})
$$

(8)

Optimized structure models for SFM, SFMMCCN, Ni, and Ni–Fe–Cu systems are provided in Figs. S16–S19, respectively. The adsorption site \* was determined by searching the configu ration with the lowest energy cost. The reaction sites considered in this study, including atop, bridge, FCC, and HCP sites, along with their corresponding energetics for the SFM, SFMMCCN, Ni, and Ni–Fe–Cu models, are presented in Fig. S20. For the oxide systems (SFM and SFMMCCN), only metal atop sites were considered. In the Ni–Fe–Cu model, the adsorbate initially placed on the FCC site was found to relocate to the Fe atop site upon structural relaxation. The calculated highest energy barrier was 3.40 eV for SFM, compared to 2.63 eV for SFM MCCN, confirming that the high-entropy perovskite lowers the kinetic barriers for $\mathrm { N H } _ { 3 }$ decomposition. We further investigated the driving force for exsolution in SFMMCCN. Figure 4f dis plays that the $\mathrm { ~ O ~ } 2 p$ band center in SFMMCCN (−3.5 eV) lie at a higher energy level than in SFM (−3.8 eV), indicating that oxygen vacancy formation—and hence cation exsolution—is more favorable in SFMMCCN. Crystal orbital Hamilton popula tion (COHP) analysis (Fig. 4g) revealed less negative integrated COHP (ICOHP) value for SFMMCCN compared with SFM, suggesting weaker cation–oxygen bonds and greater exsolution propensity. The ICOHP values for individual elements in SFM-MCCN (Fig. 4h) further showed that Ni, Cu, and Fe possess the weakest bonding to oxygen, correlating with the experimentally observed exsolved alloy composition (Fig. 2). Finally, the energy profiles for $\mathrm { N H } _ { 3 }$ decomposition were compared between bare Ni and the exsolved Ni–Fe–Cu alloy (Fig. 4i, j). The maximum energy barrier for Ni was $2 . 0 9 \mathrm { e V } ,$ while the exsolved Ni–Fe–Cu alloy exhibited a significantly lower barrier of 1.46 eV. The overall order of energy barriers was: Ni–Fe–Cu (1.46 eV)<Ni (2.09 eV)<SFMMCCN (2.63 eV)<SFM (3.40 eV).

These findings confirm that the exsolved metallic alloy provides superior catalytic activity in $\mathrm { N H } _ { 3 }$ decomposition compared to either the parent. We suggest that transition-state searches could further provide detailed information on reaction kinetics, including energy barriers, difusion processes, and $\Nu _ { 2 }$ formation. To this end, developing computational methodologies that incorporate high-entropy configurations without compromising accuracy would be an interesting topic for future work.

## 3.4 Electrochemical Performance

To assess the practical application of SFMMCCN as an ACL for DA-PCFCs, a cell configuration was constructed as depicted in Fig. 5a. In this system, $\mathrm { N H } _ { 3 }$ is supplied directly to the anode, where it is initially adsorbed on the ACL and subsequently decomposed into $\Nu _ { 2 }$ and $\mathrm { H } _ { 2 }$ by the catalyst sites. The crosssectional SEM image in Fig. 5b shows the assembled cell structure, comprising a SFMMCCN ACL, a Ni-BZCYYb anode, a BZCYYb electrolyte, and a BSTC cathode (hereafter referred to as the SFMMCCN cell). The ACL was deposited uniformly on the anode with a thickness of approximately 30 µm, forming a well-adhered interface without observable delamination. This robust interfacial contact can be attributed, in part, to the favorable thermo-mechanical compatibility between SFMMCCN and NiO–BZCYYb, as evidenced by their similar thermal expansion coeficients (TECs) measured by thermal dilatometry (Fig. S21). High-resolution imaging revealed well-dispersed Ni–Fe–Cu alloy nanoparticles exsolved from the SFMMCCN surface, with no signs of agglomeration. For comparison, a reference cell with an identical configuration but without the ACL was fabricated, hereafter denoted as the bare cell (Fig. S22). Figure 5c presents the electrochemical performance under $\mathrm { N H } _ { 3 }$ fuel at $6 0 0 ^ { \circ } \mathrm { C }$ . The SFMMCCN cell achieved a maximum power density (MPD) of $1 . 1 1 \mathrm { W } \mathrm { c m } ^ { - 2 }$ , reflecting a 32.1% enhancement relative to the bare cell. This improvement underscores the catalytic role of the SFMMCCN layer in facilitating $\mathrm { N H } _ { 3 }$ decomposition. Impedance spectra collected at $6 0 0 ^ { \circ } \mathrm { C }$ (Fig. 5d) further support this conclusion: compared to the bare cell, the SFMMCCN cel exhibits markedly lower non-ohmic resistances, as summarized in the inset, suggesting more eficient catalytic conversion of $\mathrm { N H } _ { 3 }$ into $\Nu _ { 2 }$ and $\mathrm { H } _ { 2 } .$ Consistently, distribution of relaxation time (DRT) analysis (Fig. S23) reveals a substantially reduced highfrequency contribution for the SFMMCCN cell, reflecting accelerated anodic kinetics enabled by rapid $\mathrm { N H } _ { 3 ^ { - } } \mathrm { t o } { \cdot } \mathrm { H } _ { 2 }$ conversion and subsequent $\mathrm { H } _ { 2 } {  } \mathrm { H } ^ { + }$ electrochemical reactions. In contrast, a slightly increased low-frequency contribution is observed, which is attributed to the relatively lower porosity of the SFM-MCCN ACL compared with the bare Ni-BZCYYb anode.

a  
![](images/dfd08bdfb003d66ae8593f63794e93c967f1366f3d71a469a111ea879c748f2f.jpg)

b  
![](images/c215661a3998e111f253bf13700864a54acc182385f590bd1e5a58e51e59a174.jpg)

![](images/92838da198117ec62c3e0255485472d9e59f80a081cbbf665d7072227097b08c.jpg)

![](images/bf4d339e09cd85b6a90c2c5cbc8e6e53212180895961c130cccece411528d52a.jpg)

C  
![](images/a574f29de8587e11f977603f34eaf905bae6b074f6bfd419f5551db180b8ed82.jpg)

d  
![](images/ce0d1e7884018f4f8db812748184eca34f1eb6b16747ea327bfe66e0b4122215.jpg)

e  
![](images/f41853d7885468b4ebf15eeade593867526940582af5475a9632fe429f976c36.jpg)

f  
![](images/0c40c7f66f6f5c41559d70669389bbee73ce38a4cf3fea694da3d0a9bff5b195.jpg)

g  
![](images/2e150bd4c63a04d9aaaa9592ba46ce9f5b89afc466ac7b0f4c5a7157072e90dc.jpg)

h  
![](images/fbeb08f44c5a4df4c0d53ee7cd4a56c98e26bd03dbe25252bedeb4dfa52e73e4.jpg)

![](images/d006252be473f9ed46b6366131043bef224dcd605386f5eb438bfdcc3d31f2a8.jpg)

![](images/838d78c1501265da9f7a468c022b48d85316be977d4973fbc3f139eaf28cd0fa.jpg)  
Conceptual schematic and  cross-sectional SEM images of the DA-PCFC incorporating the SFMMCCN ACL. I–V–P curves and d Nyquist plots of DA-PCFCs with ACL (SFMMCCN cell) and without ACL (bare cell) under NH fuel at 600 °C. e MPD comparison between SFMMCCN and bare cells over the $5 5 0 – 7 0 0 ^ { \circ } \mathrm { C }$ range. f Comparison of the MPDs of various DA-PCFCs. g Long-term durability test at $0 . 3 \mathrm { A c m } ^ { - 2 }$ using NH fuel. h Comparison of non-ohmic resistance during long-term durability testing. Schematic representations of $\mathrm { N H } _ { 3 }$ adsorption and stepwise decomposition pathways on Ni-BZCYYb anodes i without the ACL and j with the ACL

Nevertheless, this modest gas-difusion penalty is outweighed by the pronounced enhancement in anodic charge-transfer kinetics, resulting in superior overall performance under $\mathrm { N H } _ { 3 }$ fuel. Figures S24 and S25 show temperature-dependent impedance spectra for both PCFCs. Figure 5e compares MPD values across the range of $5 5 0 { \mathrm { - } } 7 0 0 ^ { \circ } \mathrm { C } ,$ demonstrating that the SFMMCCN cell consistently outperformed the bare cell. The corresponding I–V–P curves are presented in Figs. S26 and S27. As summarized in Fig. 5f and Table 1, the SFMMCCN cell also surpasses the performance of other state-of-the-art DA-PCFCs. To the best of our knowledge, this is the first demonstration of a DA-PCFC achieving an MPD of 2.04 $\mathrm { W ~ c m } ^ { - 2 }$ at $7 0 0 ^ { \circ } \mathrm { C } ,$ surpassing all previously reported values irrespective of catalyst design.

The durability of both cells was further examined under constant current operation of $0 . 3 \mathrm { A c m } ^ { - 2 }$ at $6 0 0 ^ { \circ } \mathrm { C }$ with $\mathrm { N H } _ { 3 }$ fuel. As shown in Fig. 5g, the bare cell exhibited rapid performance decay, attributable to accelerated Ni nitridation and particle coarsening arising from direct exposure to $\mathrm { N H } _ { 3 } .$ These degradation mechanisms reduce the number of electrochemically active sites and hinder mass transport. In sharp contrast, the SFMMCCN cell maintained stable output for over 255 h of continuous operation without signs of abrupt degradation.

Table 1   Comparison of the of various DA-PCFCs at the temperature range of 550–700 °C

<table><tr><td rowspan="3">Cathode</td><td rowspan="3">Electrolyte</td><td rowspan="3">Anode</td><td rowspan="3">Anode catalyst</td><td colspan="4">MPD (W cm-2)</td><td rowspan="3">References</td></tr><tr><td colspan="4">Temperature (°C)</td></tr><tr><td>550</td><td>600</td><td>650</td><td>700</td></tr><tr><td>BSTC</td><td>BZCYYb4411</td><td>Ni-BZCYYb4411</td><td>SFMMCCN layer</td><td>0.67</td><td>1.11</td><td>1.60</td><td>2.04</td><td>This work</td></tr><tr><td>BSTC</td><td>BZCYYb4411</td><td>Ni-BZCYYb4411</td><td>-</td><td>0.54</td><td>0.92</td><td>1.33</td><td>1.68</td><td></td></tr><tr><td>BCFZYNa</td><td>BZCYYb1711b</td><td>Ni-BZCYYb1711</td><td>PSCFR15c layer</td><td>0.32</td><td>0.45</td><td>0.63</td><td>-</td><td>[10]</td></tr><tr><td>PBSCFd</td><td>BZCYYb1711</td><td>Ni-BZCYYb1711</td><td>SFMCe layer</td><td>-</td><td>0.62</td><td>1.03</td><td>1.64</td><td>[24]</td></tr><tr><td>PBSCF</td><td>BZCYYb1711</td><td>RC/OPM-Anodef</td><td>-</td><td>0.55</td><td>0.75</td><td>1.01</td><td>-</td><td>[41]</td></tr><tr><td>PBSCF</td><td>BZCYYb1711</td><td>Ni-BZCYYb1711</td><td>Fe layer</td><td>-</td><td>0.33</td><td>0.69</td><td>1.08</td><td>[22]</td></tr><tr><td>BCCYg</td><td>BZCYYbNh</td><td>Ni-BZCYYbN</td><td>-</td><td>0.24</td><td>0.36</td><td>0.52</td><td>-</td><td>[42]</td></tr><tr><td>PBSCF</td><td>BZCYYb1711</td><td>RCNi-decorated Ni-BZCYYb1711</td><td>-</td><td>0.73</td><td>0.94</td><td>1.31</td><td>1.77</td><td>[17]</td></tr><tr><td>PBSCF</td><td>BZCYYb2611j</td><td>Pd-decorated Ni-BZCYYb2611</td><td>-</td><td>0.34</td><td>0.61</td><td>0.85</td><td>-</td><td>[43]</td></tr><tr><td>BCFZYk</td><td>BZCYYb1711</td><td>Ni-BZCYYbRFl</td><td>-</td><td>0.45</td><td>0.65</td><td>0.81</td><td>-</td><td>[15]</td></tr><tr><td>BCFZY</td><td>BZCYYbPdm</td><td>Ni-BZCYYbPd</td><td>-</td><td>0.37</td><td>0.51</td><td>0.72</td><td>-</td><td>[16]</td></tr><tr><td>BCFZY</td><td>BZCYYb1711</td><td>Ni-BZCYYb-KMgn</td><td>-</td><td>-</td><td>0.45</td><td>-</td><td>-</td><td>[44]</td></tr><tr><td>BCFZY</td><td>BZCYYb1711</td><td>Ni-BZCYYb1711</td><td>BZCYYbNRu0 filler</td><td>0.12</td><td>0.22</td><td>0.35</td><td>0.48</td><td>[45]</td></tr><tr><td>PBSCF</td><td>BZCYYb1711</td><td>Ni97Co3-BZCYYb1711</td><td>-</td><td>-</td><td>0.48</td><td>0.60</td><td>0.85</td><td>[46]</td></tr><tr><td>PBSCF</td><td>BZCYYb1711</td><td>Fe-decorated Ni-BZCYYb1711</td><td>-</td><td>0.35</td><td>0.71</td><td>1.25</td><td>1.61</td><td>[9]</td></tr></table>

Figures 5h, S28, and S29 reveal that while the SFMMCCN cell experienced only a slight increase in non-ohmic resistance up to 200 h before stabilizing, the bare cell exhibited a continuous rise, reflecting ongoing degradation. Post-test SEM analysis (Fig. S30) confirmed that Ni particles in the SFM-MCCN cell remained significantly finer than those in the bare cell, reinforcing the protective role of the ACL in mitigating Ni agglomeration and nitridation. In addition, Fig. S31 shows that the exsolved nanoparticles on the SFMMCCN surface remain uniformly dispersed without noticeable coalescence even after long-term operation, demonstrating the intrinsic structural stability of the exsolved alloy under operating conditions. Figure 5i, j schematically illustrates the mechanistic diferences in $\mathrm { N H } _ { 3 }$ decomposition. In the bare Ni-BZCYYb anode (Fig. 5i), $\mathrm { N H } _ { 3 }$ adsorbs onto the Ni surfaces and undergoes sequential dehydrogenation. However, the high energy barrier of this pathway limits reaction kinetics and suppresses efective $\mathrm { N H } _ { 3 }$ conversion. By contrast, in the SFMMCCN cell (Fig. 5j), in situ exsolved Ni–Fe–Cu alloy nanoparticles, embedded in the high-entropy oxide matrix, provide abundant acid sites and catalytically active medium-entropy alloy interfaces. This synergistic architecture lowers the barriers for $\mathrm { N H } _ { 3 }$ adsorption and dehydrogenation, thereby enhancing charge-transfer kinetics while maintaining efective mass transport. Moreover, the ACL minimizes direct $\mathrm { N H } _ { 3 }$ exposure to Ni particles, suppressing agglomeration and ensuring long-term stability.

## 4 Conclusion

In this study, we developed a high-entropy perovskite catalyst layer (SFMMCCN) incorporating in situ exsolved Ni–Fe–Cu alloy nanoparticles to address the limitations of conventional anodes in DA-PCFCs. The tailored composition and entropystabilized structure endowed the catalyst with superior activity for $\mathrm { N H } _ { 3 }$ decomposition and exceptional electrochemical stability. Compared with the bare cell, the SFMMCCN-based cell achieved a remarkable power output of 2.04 W $\mathrm { c m } ^ { - 2 }$ at 700 °C and preserved both structural and functional integrity during prolonged operation under $\mathrm { N H } _ { 3 } \mathrm { a t } 6 0 0 ^ { \circ } \mathrm { C } .$ By integrating comprehensive experimental characterization with DFT calculations, we revealed that the enhanced performance originates from favorable exsolution thermodynamics and synergistic alloy-highentropy oxide interfaces that accelerate reaction kinetics. These findings demonstrate that catalytic eficiency in DA-PCFCs can be substantially advanced through high-entropy materials design. More broadly, this work establishes a rational framework for engineering anode catalyst layers, ofering a promising route toward eficient, durable, and scalable NH -to-power technologies.

Acknowledgements This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (No. RS-2024-00406086 and No. RS-2024- 00338569). This work was supported by the Basic Research Project (GP2025-039) of KIGAM. Furthermore, this work was supported by the InnoCORE program of the Ministry of Science and ICT (N10250154).

Author Contributions K.T.L. conceived the concept and supervised the project. D.K. conducted the following experiments: material synthesis, XRD, SEM, TEM, XPS analyses, catalyst testing, and cell fabrication. D.J.P. and S.W.L. performed DA-PCFC cell testing. I.J. carried out DFT calculations. S.O., H.K., and M.L. assisted with PCFC cell fabrication. K.L. and D.C. conducted the $\mathrm { N H } _ { 3 }$ conversion test. D.K., D.J.P., I.J., K.-M.R., J.B., T.H.S., and K.T.L. contributed to writing the paper.

## Declarations

Conflict of interest The authors declare no interest conflict. They have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

Supplementary Information The online version contains supplementary material available at https://doi.org/10.1007 s40820-026-02194-9.

## References

1. I. Stafell, D. Scamman, A. Velazquez Abad, P. Balcombe, P.E. Dodds et al., The role of hydrogen and fuel cells in the global energy system. Energy Environ. Sci. 12(2), 463–491 (2019). https://doi.org/10.1039/c8ee01157e

2. C. Duan, R.J. Kee, H. Zhu, C. Karakaya, Y. Chen et al., Highly durable, coking and sulfur tolerant, fuel-flexible

protonic ceramic fuel cells. Nature 557(7704), 217–222 (2018). https://doi.org/10.1038/s41586-018-0082-6

3. A.M. Abdalla, S. Hossain, O.B. Nisfindy, A.T. Azad, M. Dawood et al., Hydrogen production, storage, transportation and key challenges with applications: a review. Energy Convers. Manag. 165, 602–627 (2018). https://doi.org/10. 1016/j.enconman.2018.03.088

4. L. Schlapbach, A. Züttel, Hydrogen-storage materials for mobile applications. Nature 414(6861), 353–358 (2001). https://doi.org/10.1038/35104634

5. D. Ding, Y. Zhang, W. Wu, D. Chen, M. Liu et al., A novel low-thermal-budget approach for the co-production of ethylene and hydrogen via the electrochemical non-oxidative deprotonation of ethane. Energy Environ. Sci. 11(7), 1710– 1716 (2018). https://doi.org/10.1039/c8ee00645h

6. A. Klerke, C.H. Christensen, J.K. Nørskov, T. Vegge, Ammonia for hydrogen storage: challenges and opportunities. J. Mater. Chem. 18(20), 2304 (2008). https://doi.org/ 10.1039/b720020j

7. B. Wang, T. Li, F. Gong, M.H.D. Othman, R. Xiao, Ammonia as a green energy carrier: electrochemical synthesis and direct ammonia fuel cell - a comprehensive review. Fuel Process. Technol. 235, 107380 (2022). https://doi.org/10. 1016/j.fuproc.2022.107380

8. D. Kim, J.W. Park, M.S. Chae, I. Jeong, J.H. Park et al., An eficient and robust lanthanum strontium cobalt ferrite catalyst as a bifunctional oxygen electrode for reversible solid oxide cells. J. Mater. Chem. A 9(9), 5507–5521 (2021). https://doi.org/10.1039/d0ta11233j

9. H. Zhang, Y. Zhou, K. Pei, Y. Pan, K. Xu et al., An eficient and durable anode for ammonia protonic ceramic fuel cells. Energy Environ. Sci. 15(1), 287–295 (2022). https://doi.org/ 10.1039/d1ee02158c

10. M. Liang, Y. Song, B. Xiong, D. Liu, D. Xue et al., In situ exsolved CoFeRu alloy decorated perovskite as an anode catalyst layer for high-performance direct-ammonia protonic ceramic fuel cells. Adv. Funct. Mater. 34(48), 2408756 (2024). https://doi.org/10.1002/adfm.202408756

11. J. Yang, A.F.S. Molouk, T. Okanishi, H. Muroyama, T. Matsui et al., A stability study of Ni/yttria-stabilized zirconia anode for direct ammonia solid oxide fuel cells. ACS Appl. Mater. Interfaces 7(51), 28701–28707 (2015). https://doi. org/10.1021/acsami.5b11122

12. Z. Wan, Y. Tao, J. Shao, Y. Zhang, H. You, Ammonia as an efective hydrogen carrier and a clean fuel for solid oxide fuel cells. Energy Convers. Manag. 228, 113729 (2021). https://doi.org/10.1016/j.enconman.2020.113729

13. M. Liang, J. Kim, X. Xu, H. Sun, Y. Song et al., Electricity-to-ammonia interconversion in protonic ceramic cells: advances, challenges and perspectives. Energy Environ. Sci. 18(8), 3526–3552 (2025). https://doi.org/10.1039/D4EE0 6100D

14. M.Z. Khan, R.-H. Song, A. Hussain, S.-B. Lee, T.-H. Lim et al., Efect of applied current density on the degradation behavior of anode-supported flat-tubular solid oxide fuel cells.

J. Eur. Ceram. Soc. 40(4), 1407–1417 (2020). https://doi.org 10.1016/j.jeurceramsoc.2019.11.017

15. Z. Liu, H. Di, D. Liu, G. Yang, Y. Zhu et al., Boosting ammonia-fueled protonic ceramic fuel cells with RuFe nanoparticle exsolution: enhanced performance via secondary redox treatment. Adv. Funct. Mater. 35(15), 2420214 (2025). https://doi. org/10.1002/adfm.202420214

16. F. He, Q. Gao, Z. Liu, M. Yang, R. Ran et al., A new Pd doped proton conducting perovskite oxide with multiple functionalities for eficient and stable power generation from ammonia at reduced temperatures. Adv. Energy Mater. 11(19), 2003916 (2021). https://doi.org/10.1002/aenm.202003916

17. H. Zhang, K. Xu, Y. Xu, F. He, F. Zhu et al., In situ formed catalysts for active, durable, and thermally stable ammonia protonic ceramic fuel cells at $5 5 0 ~ ^ { \circ } \mathrm { C } .$ . Energy Environ. Sci. 17(10), 3433–3442 (2024). https://doi.org/10.1039/d4ee0 0219a

18. F. Schüth, R. Palkovits, R. Schlögl, D.S. Su, Ammonia as a possible element in an energy infrastructure: catalysts for ammonia decomposition. Energy Environ. Sci. 5(4), 6278– 6289 (2012). https://doi.org/10.1039/c2ee02865d

19. H. Zhang, R. Xiong, Z. Chen, Z. Cheng, J. Huang et al., Eficient and robust nanocomposite cermet anode with strong metal–oxide interaction for direct ammonia solid oxide fuel cells. Adv. Funct. Mater. 35(38), 2501223 (2025). https://doi. org/10.1002/adfm.202501223

20. H. Zhang, K. Xu, F. He, F. Zhu, Y. Zhou et al., Challenges and advancements in the electrochemical utilization of ammonia using solid oxide fuel cells. Adv. Mater. 36(33), 2313966 (2024). https://doi.org/10.1002/adma.202313966

21. N. Tsvetkov, D. Kim, I. Jeong, J.H. Kim, S. Ahn et  al., Advances in materials and interface understanding in protonic ceramic fuel cells. Adv. Mater. Technol. 8(20), 2201075 (2023). https://doi.org/10.1002/admt.202201075

22. Y. Pan, H. Zhang, K. Xu, Y. Zhou, B. Zhao et al., A high-performance and durable direct NH tubular protonic ceramic fuel cell integrated with an internal catalyst layer. Appl. Catal. B Environ. 306, 121071 (2022). https://doi.org/10.1016/j.apcatb. 2022.121071

23. Y.-F. Sun, Y.-Q. Zhang, B. Hua, Y. Behnamian, J. Li et al., Molybdenum doped $\mathrm { P r } _ { 0 . 5 } \mathrm { B a } _ { 0 . 5 } \mathrm { M n O } _ { 3 - \delta }$ (Mo-PBMO) double perovskite as a potential solid oxide fuel cell anode material. J. Power. Sources 301, 237–241 (2016). https://doi.org/10. 1016/j.jpowsour.2015.09.127

24. F. He, M. Hou, Z. Du, F. Zhu, X. Cao et al., Self-construction of eficient interfaces ensures high-performance direct ammonia protonic ceramic fuel cells. Adv. Mater. 35(42), 2304957 (2023). https://doi.org/10.1002/adma.202304957

25. S. Oh, D. Kim, H.J. Ryu, K.T. Lee, A novel high-entropy perovskite electrolyte with improved proton conductivity and stability for reversible protonic ceramic electrochemical cells. Adv. Funct. Mater. 34(17), 2311426 (2024). https://doi.org/10. 1002/adfm.202311426

26. Y. Wang, M.J. Robson, A. Manzotti, F. Ciucci, High-entropy perovskites materials for next-generation energy applications.

Joule 7(5), 848–854 (2023). https://doi.org/10.1016/j.joule. 2023.03.020

27. D. Kim, I. Jeong, S. Ahn, S. Oh, H.-N. Im et al., On the role of bimetal-doped BaCoO perovskites as highly active oxygen electrodes of protonic ceramic electrochemical cells. Adv. Energy Mater. 14(14), 2304059 (2024). https://doi.org/ 10.1002/aenm.202304059

28. K. Okura, T. Okanishi, H. Muroyama, T. Matsui, K. Eguchi, Ammonia decomposition over nickel catalysts supported on rare-earth oxides for the on-site generation of hydrogen. ChemCatChem 8(18), 2988–2995 (2016). https://doi.org/10. 1002/cctc.201600610

29. G. Kresse, J. Furthmüller, Eficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 54(16), 11169–11186 (1996). https://doi.org/10. 1103/physrevb.54.11169

30. H.J. Monkhorst, J.D. Pack, Special points for Brillouin-zone integrations. Phys. Rev. B 13(12), 5188–5192 (1976). https:// doi.org/10.1103/physrevb.13.5188

31. D. Marrocchelli, N.H. Perry, S.R. Bishop, Understanding chemical expansion in perovskite-structured oxides. Phys. Chem. Chem. Phys. 17(15), 10028–10039 (2015). https://doi. org/10.1039/c4cp05885b

32. H. Lv, L. Lin, X. Zhang, Y. Song, H. Matsumoto et al., In situ investigation of reversible exsolution/dissolution of CoFe alloy nanoparticles in a Co-doped $\mathrm { S r } _ { 2 } \mathrm { F e } _ { 1 . 5 } \mathrm { M o } _ { 0 . 5 } \mathrm { O } _ { 6 - \delta }$ cathode for $\mathrm { C O } _ { 2 }$ electrolysis. Adv. Mater. 32(6), 1906193 (2020). https:// doi.org/10.1002/adma.201906193

33. K.J. Kim, C. Lim, K.T. Bae, J.J. Lee, M.Y. Oh et al., Concurrent promotion of phase transition and bimetallic nanocatalyst exsolution in perovskite oxides driven by Pd doping to achieve highly active bifunctional fuel electrodes for reversible solid oxide electrochemical cells. Appl. Catal. B Environ. 314, 121517 (2022). https://doi.org/10.1016/j.apcatb.2022.121517

34. J. Kudrnovský, V. Drchal, P. Bruno, Magnetic properties of FCC Ni-based transition metal alloys. Phys. Rev. B 77(22), 224422 (2008). https://doi.org/10.1103/physrevb.77.224422

35. S.A. Theofanidis, V.V. Galvita, M. Sabbe, H. Poelman, C. Detavernier et al., Controlling the stability of a Fe–Ni reforming catalyst: structural organization of the active components. Appl. Catal. B Environ. 209, 405–416 (2017). https://doi.org/ 10.1016/j.apcatb.2017.03.025

36. S.S. Aamlid, M. Oudah, J. Rottler, A.M. Hallas, Understanding the role of entropy in high entropy oxides. J. Am. Chem. Soc. 145(11), 5991–6006 (2023). https://doi.org/10.1021/jacs. 2c11608

37. X. Chen, Y. Tan, Z. Li, T. Liu, Y. Song et al., Advanced air electrodes for reversible protonic ceramic electrochemical

cells: a comprehensive review. Adv. Mater. 37(48), 2418620 (2025). https://doi.org/10.1002/adma.202418620

38. A. Hu, C. Yang, Y. Li, K. Xia, Y. Tian et al., High-entropy driven self-assembled dual-phase composite air electrodes with enhanced performance and stability for reversible protonic ceramic cells. Adv. Energy Mater. 15(22), 2405466 (2025). https://doi.org/10.1002/aenm.202405466

39. J. Qiao, H. Chen, Z. Wang, W. Sun, H. Li et al., Enhancing the catalytic activity of $\mathrm { Y } _ { 0 . 0 8 } \mathrm { S r } _ { 0 . 9 2 } \mathrm { T i O } _ { 3 - \delta }$ anodes through in situ Cu exsolution for direct carbon solid oxide fuel cells. Ind. Eng. Chem. Res. 59(29), 13105–13112 (2020). https://doi.org/10. 1021/acs.iecr.0c02203

40. Z. Li, C. Wang, I.T. Bello, M. Guo, N. Yu et al., Direct ammonia protonic ceramic fuel cell: a modelling study based on elementary reaction kinetics. J. Power. Sources 556, 232505 (2023). https://doi.org/10.1016/j.jpowsour.2022.232505

41. Z. Liu, M. Tao, M. Xiao, J. Li, R. Xu et al., Direct ammonia protonic ceramic fuel cells through heterogeneous interface engineering. Chem. Catal. ${ \mathfrak { s } } ( 7 ) .$ , 101365 (2025). https://doi. org/10.1016/j.checat.2025.101365

42. Y. Song, J. Chen, M. Yang, M. Xu, D. Liu et al., Realizing simultaneous detrimental reactions suppression and multiple benefits generation from nickel doping toward improved protonic ceramic fuel cell performance. Small 18(16), 2200450 (2022). https://doi.org/10.1002/smll.202200450

43. H.J. Jeong, W. Chang, B.G. Seo, Y.S. Choi, K.H. Kim et al., High-performance ammonia protonic ceramic fuel cells using a Pd inter-catalyst. Small 19(22), e2208149 (2023). https://doi. org/10.1002/smll.202208149

44. D. Feng, T. Zhu, M. Li, V.K. Peterson, H. Rabiee et al., K and Mg Co-doped perovskite oxide for enhanced anode of direct ammonia protonic ceramic fuel cell. Int. J. Hydrogen Energy 88, 272–278 (2024). https://doi.org/10.1016/j.ijhydene.2024. 09.186

45. W. Sheng, M. Fei, W. Chen, Z. Chen, D. Liu et al., A new eficient and anti-sintering perovskite oxide-based internal catalyst for tubular direct-ammonia protonic ceramic fuel cells. J. Power. Sources 642, 237008 (2025). https://doi.org/10.1016/j. jpowsour.2025.237008

46. B. Wu, X. Yu, Z. Zhao, B. He, Z. Jin et al., Improving the catalytic activity and sintering resistance of Ni-Ba $\mathrm { { C e } _ { 0 . 7 } { Z r } _ { 0 . 1 } \mathrm { { Y } _ { 0 . 1 } \mathrm { { \Sigma } } } }$ Yb $_ { 0 . 1 } \mathrm { O } _ { 3 }$ –cermet anode for ammonia-fueled protonic ceramic fuel cells via cobalt addition. Chem. Eng. J. 507, 160757 (2025). https://doi.org/10.1016/j.cej.2025.160757

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.