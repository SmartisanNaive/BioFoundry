## Abstract
### Background
Determining the value of kinetic constants for a metabolic system in the exact physiological conditions is an extremely hard task. However, this kind of information is of pivotal relevance to effectively simulate a biological phenomenon as complex as metabolism.

### Results
To overcome this issue, we propose to investigate emerging properties of ensembles of sets of kinetic constants leading to the biological readout observed in different experimental conditions. To this aim, we exploit information retrievable from constraint-based analyses (i.e. metabolic flux distributions at steady state) with the goal to generate feasible values for kinetic constants exploiting the mass action law. The sets retrieved from the previous step will be used to parametrize a mechanistic model whose simulation will be performed to reconstruct the dynamics of the system (until reaching the metabolic steady state) for each experimental condition. Every parametrization that is in accordance with the expected metabolic phenotype is collected in an ensemble whose features are analyzed to determine the emergence of properties of a phenotype. In this work we apply the proposed approach to identify ensembles of kinetic parameters for five metabolic phenotypes of _E. Coli_, by analyzing five different experimental conditions associated with the ECC2comp model recently published by Hädicke and collaborators.

### Conclusions
Our results suggest that the parameter values of just few reactions are responsible for the emergence of a metabolic phenotype. Notably, in contrast with constraint-based approaches such as Flux Balance Analysis, the methodology used in this paper does not require to assume that metabolism is optimizing towards a specific goal.

### Similar content being viewed by others
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1710064148514-3b9c4cb8-d31c-4c09-907c-b5cc98b98214.png)

Chiara Damiani, Dario Pescini, … Giancarlo Mauri

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710064148519-d9cc69b6-0127-40ee-9fce-df208c04d9c0.jpeg)

Michael MacGillivray, Amy Ko, … Allen Holder

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064148516-4c5ba061-32e5-4721-a8c9-1294e92640ff.webp)

## Background
Advances in the understanding of biological processes has revealed that living organisms must be analyzed by taking into account the complex network of interactions among different entities such as genes, transcripts, proteins and metabolites in order to decipher emergent behaviors and regulatory processes. In the context of Systems Biology [[1](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR1)], the study of metabolism has received great interest, especially due to the fruitful applications in metabolic engineering [[2](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR2)]. In these studies, metabolic networks are typically represented as hyper-graphs in which nodes denote metabolites and edges indicate reactions [[3](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR3)].

### Omics data in metabolic modeling
High throughput information allowed the generation of detailed genome-scale metabolic reconstructions, defined ad hoc for different cell types (as e.g. unicellular organisms [[4](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR4)], healthy and diseased tissues in mammalian [[5](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR5)]). Despite this, there are still technological hindrances preventing mechanistic simulation of genome-scale metabolic models: currently, simulated temporal dynamics of metabolic concentrations are practical only for small models due to shortage of retrievable parameter values and high computational costs [[6](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR6)].

### Constraint-based methods
The points raised above determine the current strategy in metabolic modeling, namely the exploitation of the so called constraint-based approaches [[7](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR7)]. This modeling framework uses information about the structure of the metabolic network and assumes that internal metabolites reach a steady-state concentration. Even if these approaches neglect the temporal evolution of the system, they can be considered a valid framework to describe metabolism because of experimental studies pointing out that in vivo metabolism reaches the steady state in few seconds [[8](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR8)]. In the context of constraint-based modeling, a metabolic network is usually described as a set of chemical reactions from which it is possible to retrieve the stoichiometric matrix, i.e. the table illustrating changes in metabolites quantities due to the firing of reactions. Moreover constraint-based approaches define the mathematical space containing flux distributions (i.e. flux values for each reaction in the model) that can be reached by the system under different functional states. This “feasible solution space”, is determined by imposing a mass balance constraint, as well as boundaries on fluxes (e.g. to specify their reversibility). Once the stoichiometric matrix and the boundaries are defined, it is possible to assume that the system is optimal toward a given Objective Function (OF) – such as the production of biomass or a given metabolite – to be maximized or minimized. Following this an optimal flux distributions can be calculated by means of optimization techniques such as Flux Balance Analysis (FBA) [[9](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR9)].

Choosing an appropriate formulation of the OF is of paramount importance when conducting FBA, however often its exact formulation is not definable. Moreover, questioning the concept of optimal behavior, recent studies [[10](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR10)] speculate that it is reasonable to assume that the system is found in a sub-optimal state.

### Ensemble FBA
To analyze the potentiality of a cell to explore alternative metabolic behaviors by altering its fluxes, we previously introduced the Ensemble Evolutionary FBA (eeFBA): [[11](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR11)] an extension of FBA defined with a goal to investigate putative flux distributions that can give rise to a specific metabolic behavior. With eeFBA, analyses are performed by generating a set of OFs where both terms and coefficients are selected randomly. Random OFs are subsequently optimized by means of linear programming and the computed flux distributions are filtered on the basis of one or more metabolic phenotypes definitions, to retrieve ensembles of solutions that are in agreement with the defined phenotypes.

### Retrieving kinetic parameters form a mechanism-based ensemble approach
Due to lack of information on kinetic constants, either with FBA or eeFBA it is not possible to determine metabolic concentrations at steady state. To overcome this limitation, in a recent paper [[12](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR12)], we proposed a strategy, where ensembles of phenotypes are still populated according to flux properties, but steady states are retrieved from mechanism based simulations. The parameters of the kinetic model are set using initial concentrations from the literature (whenever possible) and values for kinetic constants have been sampled randomly from a given interval (e.g. from 0 to the thermodynamic limit) thereby avoiding biases in their definition (see “[Methods](https://link.springer.com/article/10.1186/s12859-018-2181-7#Sec7)” section for further information).

With the above described procedure, we have been able to determine steady state metabolic concentrations that satisfy the definition of a given metabolic response to changing experimental conditions. It is worth to underline that, this readout was obtained without defining an OF, thus avoiding the assumption that the cell is performing an optimization towards a certain objective.

In this work we slightly modify the approach in order to take into account the fact that kinetic constants may assume different values under various experimental conditions due to enzymatic regulation. In order to associate a set of specific rate constants to the phenotype associated to each experimental condition, the kinetic constants are retrieved from a set of parameterizations of a mechanistic model that, when dynamically simulated with those constants, is able to generate time courses in agreement with the phenotype definition.

Strikingly, our method can be used to predict ensembles of rate constants that are in agreement with a given metabolic phenotype of interest only by providing its definition and a flux distribution for the same condition, obtained by means of FBA.

### EColiCore2: a case study
In [[12](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR12)], we applied our procedure exploiting a toy metabolic model of _S. cerevisie_ and filtering trajectories accordingly to a definition of the Crabtree phenotype. In the present paper, we aim at investigating a more realistic metabolic reconstruction focusing on _Escherichia coli_, the prokaryotic model organism for which a number of core models have been built in a bottom-up fashion and are currently retrievable from the literature. A notable example, due to its wide exploitation, is the _E. coli_ core model illustrated in Orth et al. [[13](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR13)].

Conversely, there is a relative scarcity of top-down metabolic models built starting from genome scale reconstructions of these bacteria. The EColiCore1 reconstruction was manually derived from the iAF1260 [[14](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR14)] genome scale model. However, this model has mainly testing and training purposes and is not completely consistent with the corresponding genome wide model.

Starting from the genome wide model iJO1366 [[15](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR15)], Hädicke et al. in [[16](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR16)] aimed at reconstructing a metabolic model of the central metabolism of _E. coli_ called EColiCore2. This model, built with the final goal of establishing a reference core model for _E. coli_ constraint-based analyses, has been derived reducing redundancies in biosynthetic routes and maintaining the degrees of freedom in the central metabolism, moreover, this core model is completely consistent with its genome wide counterpart. One key aspect of EColiCore2 is its ability to reproduce pivotal features of iJO1366, achieving a notable complexity reduction without losing its ability to depict emerging behaviors of _E. coli_ metabolism.

ECC2comp, presented in [[16](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR16)] and illustrated in Fig. [1](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig1), is a further reduction of EColiCore2 derived by exploiting NetworkReducer [[17](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR17)], i.e., an algorithm able to automatically compress metabolic models by lumping linear chains of reactions in a single cumulative equation and by removing elements (metabolites and reactions) that are non essential to represent key metabolic functions referred to as “protected functions”. 

**Fig. 1**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064148534-2b9924a9-22db-4288-ad4b-ce23ee99c289.webp)

Wiring diagram of the EColiCore2 model. Metabolic network is modified (adding reverse reactions and cofactors) from Hädicke et al. [[16](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR16)]. In the map, reaction names are labeled in blue and placed next to the corresponding edge. The external environment is represented by a dashed contour, the cell is delimited by a solid contour. Significant reactions emerging from the Kolmogorov-Smirnov test described in section Results are labeled in red

[Full size image](https://link.springer.com/article/10.1186/s12859-018-2181-7/figures/1)

## Methods
The procedure introduced in [[12](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR12)] and schematically represented in Fig. [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2) has been used here to setup the “experiments” hereafter illustrated. For a large number _P_ of parametrizations we extract each of the M distinct kinetic constants of the model \(\left (\vec {k}_{p} = \left (k^{1}_{p}, \ldots, k^{M}_{p}\right)\right)\) from a uniform distribution in [ 0,100). Every parametrization of this set is exploited to produce different simulations in accordance with each metabolic phenotype under study. We call metabolic phenotype a set of values assumed by key fluxes in defined experimental conditions. The mechanism based simulations, one for each different experimental condition, is performed using constant concentrations of the associated nutrient (e.g., glucose), oxygenation level and ions. 

**Fig. 2**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064148526-a571d8b3-1ed4-4a11-8fe4-f3f349b49a6f.webp)

Schematic workflow illustrating the four main phases of the computational procedure. **a** Run deterministic simulations; **b** Calculation of flux values; **c** Filtering of experiments; **d** Analysis of outcomes. See main text for a complete description of the approach

[Full size image](https://link.springer.com/article/10.1186/s12859-018-2181-7/figures/2)

### Running deterministic simulations
To perform mechanism based simulations we assume mass-action kinetics within the ODEs deterministic framework. The metabolic model has been simulated until the achievement of a steady state for internal metabolites concentrations (Fig. [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)[a](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)). Every simulation is considered at steady state at its ending time _t__e_ if 

$$ \frac{\sum^{M}_{w=1} \sigma\left(\left[\chi_{w}\right](\bar{t}, t_{e})\right)}{M - S} < \theta $$ 

(1) 

where \(\sigma ([\!\chi _{w}](\bar {t}, t_{e}))\) is the standard deviation of the concentration [ _χ__w_] of species _w_ computed over \(t_{e} - \bar {t}\) with \(\bar {t} = 0.9\ t_{e}\) and _S_ the number of species kept constant throughout the simulation and _θ_ is a tolerance threshold.

### Calculating flux values
Afterwards, fluxes values _v__i_ are calculated for every reaction (when the dynamic reaches the steady state) by means of the relation expressed by the mass action law illustrated in Eq. ([2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Equ2)). 

$$ v_{i} = k_{i} \prod_{w=1}^{M} [\!\chi_{w}]^{\alpha_{w i}} $$ 

(2) 

where _k__i_ is the rate constant of reaction _i_, [_χ__w_] is the concentration of species _w_ and _α__w__i_ the stoichiometric coefficient with which species _w_ participates in reaction _i_ (Fig. [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)[b](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)).

### Filtering the experiments
Once flux values have been obtained, experiments are filtered exploiting key metabolic fluxes in order to populate ensembles of metabolic phenotypes that are in agreement with the filter definition (Fig. [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)[c](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)). In particular, in this work, to filter the experiments we defined 5 different phenotypes based on FBA simulations presented in [[16](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR16)].

### Analyzing the experiments
Finally, it is possible to analyze (Fig. [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)[d](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)) the experiments to identify properties shared by elements of each ensemble, e.g., by investigating the presence of putative subphenotypes or by evaluating which reactions exhibit kinetic constants whose value depart from the average.

### _E. coli_ case study
To test the procedure herein described we defined 5 different metabolic phenotypes (“protected phenotypes” in [[16](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR16)]) built on the basis of both the nutrient supplied and the oxygenation state observed (Table [1](https://link.springer.com/article/10.1186/s12859-018-2181-7#Tab1)): exp1 - aerobic growth on glucose, exp2 - anaerobic growth on glucose, exp3 - aerobic growth on acetate, exp4 - aerobic growth on succinate, exp5 - aerobic growth on glycerol. 

**Table 1 Protected phenotypes. Phenotypes and maximal growth rate in the core model ECC2 obtained with FBA**

[Full size table](https://link.springer.com/article/10.1186/s12859-018-2181-7/tables/1)

To evaluate the effectiveness of the procedure in discriminating the 5 phenotypes and in selecting corresponding ensembles of kinetic constants and steady state metabolic concentrations, we used ECC2comp [[16](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR16)]. We split the reversible reactions of the original compressed “core” into backward and forward reaction, obtaining a total of 114 irreversible reactions and 93 metabolites, of which 60 are internal, while 33 are external. The final model used in this study is provided in Additional file [1](https://link.springer.com/article/10.1186/s12859-018-2181-7#MOESM1).

To determine the initial concentrations of metabolites involved in the _E. coli_ model, we set them accordingly to the average values illustrated in the _E. coli_ Metabolome Database (ECMDB) [[18](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR18)], an expertly curated database containing extensive metabolomic data and metabolic pathway diagrams about _Escherichia coli_ (strain K12, MG1655). The ECMDB contains 3755 entries for metabolites and small molecules manually compiled including identification, taxonomy, concentrations, spectra, physical and biological properties. Information are derived from “original” data and from metabolic reconstructions, scientific articles, textbooks and other electronic databases. For metabolites in the model not having a concentration in ECMDB, we used the average value calculated over other retrieved values. The set of metabolic concentrations is provided in Additional file [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#MOESM2).

Metabolic phenotypes defined in this section need to be translated using a mathematical formalism in order to unequivocally characterize them as described in the following section. To this end we evaluated fluxes that in the ECC2comp model are proxies for the 5 phenotypes listed in Table [1](https://link.springer.com/article/10.1186/s12859-018-2181-7#Tab1).

### Populating the ensembles
To perform the procedure illustrated in this section, we implemented a set of scripts in plain vanilla Python available on GitHub (see Additional file [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#MOESM3)). As already mentioned, dynamic simulations of the _E. coli_ “core” metabolic model (step Fig. [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)[a](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig2)) have been performed until reaching of the steady state exploiting a set of ordinary differential equations (ODEs) determined under the mass action kinetic assumption. The numerical integration of the ODEs system has been realized exploiting the software library LSODA (Livermore solver for ODEs with automatic method) [[19](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR19)] efficiently implemented in SciPy [[20](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR20)].

Due to a large volume of data produced with simulations (stored on GitHub, see Additional file [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#MOESM3)), we decided to separate data generation and analysis phases. An efficient way to organize and access simulation outputs is to store them in a database. In particular here we exploited PyTables [[21](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR21)], a package for managing hierarchical datasets designed to efficiently and easily cope with extremely large amounts of data. PyTables makes use of the NumPy package and of the HDF5 library under the Python language.

Ensembles of kinetic constants sustaining the 5 different metabolic phenotypes have been populated by performing a large number of “experiments” conducted first by randomly defining, for each of them, the set of kinetic constants and then by executing a simulation for each given experimental condition providing, for each of them, a unique nutrient selected among glucose (exp1 and exp2), acetate (exp3), succinate (exp4), glycerol (exp5) and a non limiting amount of oxygen.

To populate the ensembles of kinetic constants, we filtered the experimental dataset according to conditions that have been implemented on the basis of fluxes illustrated in Table [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Tab2). The flux values in the table have been obtained by simulating the ECC2comp model under the 5 different experimental conditions (see Table [1](https://link.springer.com/article/10.1186/s12859-018-2181-7#Tab1)) with FBA. 

**Table 2 Flux values used to set up filters in order to populate the 5 ensembles of kinetic constants corresponding to experimental conditions**

[Full size table](https://link.springer.com/article/10.1186/s12859-018-2181-7/tables/2)

In particular, to build filters we evaluated only ECC2comp reactions: (A) having non zero flux value in just one of the experimental conditions (Table [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Tab2), in bold), (B) defining the experimental conditions and oxygenation state (Table [2](https://link.springer.com/article/10.1186/s12859-018-2181-7#Tab2), in italic). For example, as the reaction GLYK is active only in metabolic phenotype exp5, flux distribution is assigned to metabolic phenotype exp5 iff the GLYK flux is greater than zero. Along similar lines O2Up, which defines the oxidation state, is active in every metabolic phenotype except exp2. Its flux distribution is assigned to metabolic phenotype exp2 iff the O2Up flux is equal to zero.

Formally these constraints relative to the phenotypes are summarized by logical expressions shown in Eqs. ([3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Equ3)) to ([6](https://link.springer.com/article/10.1186/s12859-018-2181-7#Equ6)) where _v__i_ represent the metabolic flux through the _i_ reaction. 

$$ {{}\begin{aligned} \mathbf{exp1:} \left({ v_{G6PDH2r}} > 0 \right) &\wedge \left({ v_{GND}} > 0 \right) \wedge \left({ v_{PGL}} > 0 \right)\\ & \wedge \left({ v_{GLCptspp}} > 0 \right) \wedge \left({ v_{O2Up}} > 0\right) \end{aligned}} $$ 

(3) 

$$ {\begin{aligned} \mathbf{exp2:} \left({ v_{AcEx}} > 0 \right) &\wedge \left({ v_{ALCD2x}} > 0\right) \wedge \left({ v_{EthEx}} > 0 \right) \\ &\wedge \left({ v_{GLCptspp}} > 0 \right) \wedge \left({ v_{O2Up}} = 0 \right) \end{aligned}} $$ 

(4) 

$$ {\begin{aligned} \mathbf{exp3:} \left({ v_{MALS}} > 0 \right) \wedge \left({ v_{ICL}} > 0 \right) &\wedge \left({ v_{AcUp}} > 0 \right) \wedge \left({ v_{O2Up}} > 0\right) \end{aligned}} $$ 

(5) 

$$ {\begin{aligned} \mathbf{exp4:} \left({ v_{SUCCt2_{2}pp}} > 0\right) &\wedge \left({ v_{ME2}} > 0 \right) \wedge \left({ v_{O2Up}} > 0 \right) \end{aligned}} $$ 

(6) 

$$ {\begin{aligned} \mathbf{exp5:} \left({ v_{GLYK}} > 0\right) &\wedge \left({ v_{F6PA}} > 0 \right) \wedge \left({ v_{GLYCDx}} > 0 \right) \\ &\wedge \left({ v_{O2Up}} > 0 \right) \end{aligned}} $$ 

(7) 

An experimental set of kinetic constants is assigned to a given ensemble (metabolic phenotype) if and only if all the constraints associated to that phenotype are satisfied.

## Results
### Obtained ensembles
To test the procedure on the simplified _E. coli_ model, we tossed multiple different random sets of kinetic constants, keeping the concentration of ions and exchanged species (i.e., ac_ex, ca2_ex, cl_ex, co2_ex cobalt2_ex, cu2_ex, fe2_ex, fe3_ex, for_ex, glc_DASH_D_c, glc_DASH_D_ex, glc_DASH_D_p, h_ex, h2_ex, h2o_ex, k_ex, mg2_ex, mn2_ex, mobd_ex, MTHTHF_ex, nh4_ex, ni2_ex, o2_ex, pi_ex, so4_ex, succ_ex and zn2_ex) constant throughout the simulation time of 100 seconds, defined accordingly to [[8](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR8)] in order to allow the metabolic steady state to be reached after a perturbation (e.g. a pulse of nutrient).

Every simulation is considered at steady state if _θ_ < 0.1_%_. If the steady state is verified, the random parametrization is retained, otherwise is dropped. To obtain a dataset of 104 random sets of kinetic constants, we performed a total of 11520 samplings, thereby discarding the 13.2% of performed simulations. The total computational time to produce the data set has been 1d 2h 20min to run ODEs simulations on a workstation (8 x CPU 3.8 GHz Intel Core i7, RAM 32 GB) and producing 20.3 GB of data.

The input of the filtering procedure has been a dataset composed of 5·104 simulations, i.e. 104 random sets of kinetic constants tested over 5 experimental conditions.

We tamed numerical instability by imposing a threshold considering fluxes with a value less than 10−10 to be 0. From the dataset of 5·104 solutions 15267 have been assigned to exp1, 101 to exp2, 19616 to exp3, 22719 to exp4 and 16033 to exp5, as illustrated by the last 6 rows of Fig. [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig3) reporting the cardinality of solutions, i.e. the number of random parameterizations that are assigned to one or more phenotypes at the same time. 

**Fig. 3**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064148731-d0d1ed55-b175-4341-98d4-e93bce1ff5d4.webp)

Cardinality of solutions illustrating the intersection among the different ensembles. Numbers on Y axis indicate the ensemble(s) (e.g. 12, indicates the ensemble exp1 and exp2) while the length of the bar indicates the number of solutions belonging to the ensemble or group of ensembles

[Full size image](https://link.springer.com/article/10.1186/s12859-018-2181-7/figures/3)

Data presented in Fig. [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig3) show that we have been able to identify a subset of parametrization that work for all cases (1345 in Fig. [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig3)) but not for the anaerobic condition (exp2 – 2 in Fig. [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig3)). This reflects the consistent metabolic differences that can be pointed out in vivo between aerobic and anaerobic conditions.

In connection to this issue, we noticed that combinations exp2 - exp3 (23 in Fig. [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig3)) and exp2 - exp5 (25 in Fig. [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig3)) are empty sets due to the fact that in phenotype exp2 (anaerobic) reactions sustaining respiration are blocked (e.g. in TCA cycle the flux for reaction CS, leading to citrate is almost zero – see Fig. [4](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig4)) while in exp3 and exp5 (aerobic conditions) the same reactions are active. 

**Fig. 4**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064148817-1603f8bd-a8b8-494b-963f-53b42234635e.webp)

Heatmap. Figure illustrates median flux values through model reactions (rows) at the steady state, when the dynamic is labeled according to flux values at steady state emerging from their parameterization (columns labeled with sC#) and when it is filtered according to phenotypes (columns labeled with fC#). Red labels indicate reactions used to implement the filtering conditions for the metabolic phenotypes

[Full size image](https://link.springer.com/article/10.1186/s12859-018-2181-7/figures/4)

To compare flux values at steady state for each reaction in the system before and after the filtering, we drew the heatmap of Fig. [4](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig4) where rows list reactions, columns list sets of dynamics ensembles associated with each metabolic phenotype and the color represents the median value of that ensemble for that reaction at steady state (range [ 1·10−13, 1·101]). We made two distinct associations of the dynamics to the phenotypes, the columns labeled as sC# have the dynamics assigned according to flux values at steady state emerging from their parameterization, whereas columns labeled as fC#, the filtered ones, are populated with the dynamics that satisfies phenotypes constraints at steady state, disregarding their initial condition. Overall, it is possible to notice that flux values in sC# and fC# for a given phenotype exhibit almost always a comparable flux value, there with only few exceptions to this behavior (e.g. reactions: O2Up_reverse less active in the fC2; h2Ex, PGM, PGM_reverse, PGK less active in fC3, SUCCt2_2pp more active in fC3; GlcUp and GLCt2pp more active in fC4). Moreover, comparing the different phenotypes, it is possible to notice that exp5 (sC and fC5) has flux values dissimilar to the other 4 phenotypes.

To better characterize the ensembles, we also plotted the median and the standard deviation for kinetic constants values retrieved for each ensemble after the filtering. Results illustrated in Fig. [5](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig5) show that there are little but non negligible differences in the median of kinetic constant values for all the reactions of the model (e.g. exp1 has different median values for h2o_Ex_reverse, F6PA_reverse, PGL, PGI, GND, h2o_Ex; exp5 has constant associated to ATPM greater than the average). Furthermore, supporting the findings that have emerged from analyzing cardinalities (Fig. [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig3)), median values for the group of four aerobic phenotypes are very similar, while the medians for anaerobic phenotype are different form the previous group. 

**Fig. 5**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064148826-0928c901-f39d-4494-aac6-6818ea19a59b.webp)

Boxplot. Illustration represents model reactions (rows), median for kinetic constants associated to the 5 phenotypes and not associated with any phenotype (colored vertical bars, see key for color code)

[Full size image](https://link.springer.com/article/10.1186/s12859-018-2181-7/figures/5)

### Relevant fluxes
To identify relevant fluxes able to discriminate the 5 metabolic phenotypes, we performed a Kolmogorov-Smirnov (KS) test, a non-parametric hypothesis test procedure able to discern if two samples derive from the same distribution without investigating the actual shape of the distributions. The KS test has been performed for each possible pair of conditions and for each flux. The goal was to identify those fluxes that statistically differ for each pair of conditions (with significance 0.05) and that should thus be able to discriminate each of the 5 conditions.

From the output of the KS test we found a subset of 38 fluxes that can be regarded as relevant fluxes. Relevant fluxes are reported (red color) in Fig. [1](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig1). From their mapping on the metabolic network it emerges that these reactions are mainly part of functional elements in the network: in particular exchange reactions and hubs (i.e. network junctions connecting different pathways). Instead, reactions internal to pathways are less represented among the significant ones. This may suggest that the cell performs a tight regulation of fluxes among different pathways and a less stringent tuning for reactions belonging to the same pathway.

## Discussion
The analysis of average concentrations and relative standard deviations for molecular species during time courses shed light on some relevant issues hereafter discussed.

Overall, we underline that standard deviation values (_σ_) are small and few parameterizations (only 13% of the total) are discarded, suggesting that for the sampled interval [0, 1·102] metabolism is robust towards kinetic constant variation. This parameter insensitivity has been further investigated in [[22](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR22)] where authors showed that many models in Systems Biology exhibit a “sloppy” spectrum of parameter sensitivities, concluding that besides the mere estimation of the parameter value, the community should focus on analyzing models in a predictive fashion.

Concerning biomass (Fig. [6](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig6)) it is possible to notice that it is accumulating over time in all metabolic phenotypes. Interestingly, when we tested a further experimental condition (exp0 – not used as a metabolic phenotype) representing an enriched growth media (i.e., when all the nutrients are simultaneously available), this turned out not to be the condition leading to the maximal level of biomass (it is for instance the aerobic growth on succinate, exp4 – purple line). 

**Fig. 6**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064148812-b71d935c-46ec-4a87-b020-be8c6670ab2a.webp)

Time course for the species “biomass”. Figure shows that the mass of the system is accumulating during the simulation for every experimental condition, i.e., the system is able to grow under the experimental conditions. Shaded areas indicate the _σ_ for every experiment, solid line represent a trajectory averaged over a subset of 200 parameterizations due to computational time limitations

[Full size image](https://link.springer.com/article/10.1186/s12859-018-2181-7/figures/6)

Furthermore, the analysis of time courses (Fig. [7](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig7)) reveals that many metabolic pathways remain active throughout the simulation since they are generating metabolic intermediates. As an example _E. coli_ is performing both alcoholic fermentation, as it appear from the time course for ethanol (Fig. [7](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig7) top), and TCA cycle, a pathway considered as indicator for respiration and illustrated at the bottom of Fig. [7](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig7), with the time course for malate. 

**Fig. 7**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064148832-9711f552-cbca-4f64-961e-195dbcd92680.webp)

Time course for the species ethanol and malate. The time course for the species ethanol (top) shows that the species (not evaluated for the determination of the steady state) is accumulating during the simulation for every experimental condition, i.e., the system is able to perform alcoholic fermentation. Instead the time course for malate (bottom), shows the reaching of the steady state indicating that the system is also using the TCA cycle. Shaded areas indicate the _σ_ for every experiment, solid line represent a trajectory averaged over a subset of 200 parametrizations due to computational time limitations

[Full size image](https://link.springer.com/article/10.1186/s12859-018-2181-7/figures/7)

Data supporting the actual activation of biochemical pathways in the model are also the presence of steady states for cofactors such as NAD/NADH and NADP/NADP which appear to be dynamically inter-converted as shown in Fig. [8](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig8) where, comparing the time courses for NAD (top) and NADH (bottom), it is possible to notice a symmetrical trend. This fact indicates that metabolic pathways are maintaining the system energetically active and capable of generating biomass. Focusing on the set of kinetic constants assigned to the different metabolic phenotypes, the procedure illustrated in the present paper led to the population of all the 5 phenotypes and to the identification of a subset of kinetic constants assignable to the four aerobic conditions. Unfortunately, there is no single “universal” parametrization assignable to all 5 phenotypes. This fact could be determined by different causes such as an under sampling of random kinetic constants, a too narrow sampling interval (in this study 2 orders of magnitude), or an excessively relaxed filtering condition not allowing a complete discrimination among the phenotypes. 

**Fig. 8**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/webp/22983715/1710064149000-6353e0e2-94e7-4547-b708-c42bc755c1ce.webp)

Time courses for the species NAD (top) and (NADH) bottom. Figure illustrate that the species are satisfying the steady state condition (i.e., are not varying more than 1% in the last 10 s of simulation. Moreover, NAD/NADH ratio is compatible with “sustained steady states” in all experimental condition except experiment 5. Similar time courses are obtained for NADP and NADPH. Shaded areas indicate the _σ_ for every experiment, solid line represent a trajectory averaged over a subset of 200 parametrizations due to computational time limitations

[Full size image](https://link.springer.com/article/10.1186/s12859-018-2181-7/figures/8)

Furthermore, the evaluation of median and standard deviation for the kinetic constants belonging to the 5 ensembles (Figs. [4](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig4) and [5](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig5)) suggests that there are only few reactions that have to be finely tuned in order to direct the system towards a specific metabolic phenotype, a fact that suggests once more that metabolism is a system particularly robust towards perturbations. In this case a global sensitivity analysis would help to investigate the issue of robustness more specifically.

## Conclusions
Constraint-based models have been successfully implemented to study metabolic fluxes at steady state, nevertheless, information about the temporal evolution of the system during the transient phase preceding the steady state can not be derived from them. In addition, the metabolic concentrations at steady state can not be deduced from constraint-based methods since there is no information about kinetic constants.

Computational approaches developed in [[12](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR12)] and exploited in the present work are an improvement designed to override limitations by exploiting mechanism-based simulations. Here, initial conditions are partially retrieved from the literature (molecular concentrations) and kinetic constants are randomly determined. Figure [3](https://link.springer.com/article/10.1186/s12859-018-2181-7#Fig3) sums up the readout of the procedure: through a filtering procedure based on a loose definition of the 5 experimental conditions (metabolic phenotypes) involving some key reactions, the developed method is able to assign random sets of kinetic constants to one or more metabolic phenotypes.

With the present contribution we aimed at improving and testing a computational framework capable of retrieving ensembles of kinetic constants that can be associated with different metabolic phenotypes. It is worth underlying that, in contrast with constraint-base approaches, our method is not assuming that metabolism is optimized to perform a specific task.

We underline that the methodology used here can be exploited to retrieve ensembles of kinetic constants for any metabolic phenotype providing only its formal definition (in terms of nutrients supplied and oxygenation state together with an estimation of initial concentrations for modeled species) and a flux distribution obtained by means of a constraint-based simulation (for which no kinetic parameters are needed).

For what concerns perspectives, we plan to better characterize the metabolic steady state by exploiting more efficient strategies to calculate whether the system reaches a stationary condition. Among these strategies a promising approach includes the use of the NLEQ2 non-linear root-finding algorithm [[23](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR23)]. Moreover, we are considering to significantly expand the sampled set of kinetic constants through a significant speed-up of simulations achieved by means of high performance and parallel computing applied to Systems Biology modeling problems [[24](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR24), [25](https://link.springer.com/article/10.1186/s12859-018-2181-7#ref-CR25)].

## Abbreviations
ECMDB:

E. coli metabolome database

eeFBA:

Ensemble evolutionary FBA

FBA:

Flux balance analysis

KS:

Kolmogorov-Smirnov LSODA: Livermore solver for ODEs with automatic method

ODEs:

Ordinary differential equations

OF:

Objective function

## References
1. Alberghina L, Westerhoff HV. Systems Biology. Definitions and Perspectives, volume 13 of Topics in Current Genetics. Berlin - Heidelberg: Springer-Verlag; 2005.

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Systems%20Biology.%20Definitions%20and%20Perspectives%2C%20volume%2013%20of%20Topics%20in%20Current%20Genetics&publication_year=2005&author=Alberghina%2CL&author=Westerhoff%2CHV)  

2. Park JM, Kim TY, Lee SY. Constraints-based genome-scale metabolic simulation for systems metabolic engineering. Biotechnol Adv. 2009; 27(6):979–88.

[Article](https://doi.org/10.1016%2Fj.biotechadv.2009.05.019)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=19464354)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Constraints-based%20genome-scale%20metabolic%20simulation%20for%20systems%20metabolic%20engineering&journal=Biotechnol%20Adv&doi=10.1016%2Fj.biotechadv.2009.05.019&volume=27&issue=6&pages=979-88&publication_year=2009&author=Park%2CJM&author=Kim%2CTY&author=Lee%2CSY)  

3. Zhao J, Yu H, Luo J, Cao Z, Li Y. Complex networks theory for analyzing metabolic networks. Chin Sci Bull. 2006; 51(13):1529–37.

[Article](https://link.springer.com/doi/10.1007/s11434-006-2015-2)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BD28XmvFSgu70%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Complex%20networks%20theory%20for%20analyzing%20metabolic%20networks&journal=Chin%20Sci%20Bull&doi=10.1007%2Fs11434-006-2015-2&volume=51&issue=13&pages=1529-37&publication_year=2006&author=Zhao%2CJ&author=Yu%2CH&author=Luo%2CJ&author=Cao%2CZ&author=Li%2CY)  

4. Aung HW, Henry SA, Walker LP. Revising the representation of fatty acid, glycerolipid, and glycerophospholipid metabolism in the consensus model of yeast metabolism. Ind Biotechnol. 2013; 9(4):215–28.

[Article](https://doi.org/10.1089%2Find.2013.0013)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC3sXht1Oisr7F)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Revising%20the%20representation%20of%20fatty%20acid%2C%20glycerolipid%2C%20and%20glycerophospholipid%20metabolism%20in%20the%20consensus%20model%20of%20yeast%20metabolism&journal=Ind%20Biotechnol&doi=10.1089%2Find.2013.0013&volume=9&issue=4&pages=215-28&publication_year=2013&author=Aung%2CHW&author=Henry%2CSA&author=Walker%2CLP)  

5. Di Filippo M, Colombo R, Damiani C, Pescini D, Gaglio D, Vanoni M, Alberghina L, Mauri G. Zooming-in on cancer metabolic rewiring with tissue specic constraint-based models. Comput Biol Chem. 2016; 62:60–69.

[Article](https://doi.org/10.1016%2Fj.compbiolchem.2016.03.002)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=27085310)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC28XksFKntrs%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Zooming-in%20on%20cancer%20metabolic%20rewiring%20with%20tissue%20specic%20constraint-based%20models&journal=Comput%20Biol%20Chem&doi=10.1016%2Fj.compbiolchem.2016.03.002&volume=62&pages=60-69&publication_year=2016&author=Di%20Filippo%2CM&author=Colombo%2CR&author=Damiani%2CC&author=Pescini%2CD&author=Gaglio%2CD&author=Vanoni%2CM&author=Alberghina%2CL&author=Mauri%2CG)  

6. Cazzaniga P, Damiani C, Besozzi D, Colombo R, Nobile MS, Gaglio D, Pescini D, Molinari S, Mauri G, Alberghina L, et al. Computational strategies for a system-level understanding of metabolism. Metabolites. 2014; 4(4):1034–87.

[Article](https://doi.org/10.3390%2Fmetabo4041034)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=25427076)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4279158)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC2cXitFGgtLbI)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Computational%20strategies%20for%20a%20system-level%20understanding%20of%20metabolism&journal=Metabolites&doi=10.3390%2Fmetabo4041034&volume=4&issue=4&pages=1034-87&publication_year=2014&author=Cazzaniga%2CP&author=Damiani%2CC&author=Besozzi%2CD&author=Colombo%2CR&author=Nobile%2CMS&author=Gaglio%2CD&author=Pescini%2CD&author=Molinari%2CS&author=Mauri%2CG&author=Alberghina%2CL)  

7. Gianchandani EP, Chavali AK, Papin JA. The application of flux balance analysis in systems biology. Wiley Interdiscip Rev Syst Biol Med. 2010; 2(3):372–82.

[Article](https://doi.org/10.1002%2Fwsbm.60)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=20836035)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXmtVSrtrw%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20application%20of%20flux%20balance%20analysis%20in%20systems%20biology&journal=Wiley%20Interdiscip%20Rev%20Syst%20Biol%20Med&doi=10.1002%2Fwsbm.60&volume=2&issue=3&pages=372-82&publication_year=2010&author=Gianchandani%2CEP&author=Chavali%2CAK&author=Papin%2CJA)  

8. Theobald U, Mailinger W, Baltes M, Rizzi M, Reuss M. In vivo analysis of metabolic dynamics in _Saccharomyces cerevisiae: I. Experimental observations_. Biotech Bioeng. 1997; 55(2):305–16.

[Article](https://doi.org/10.1002%2F%28SICI%291097-0290%2819970720%2955%3A2%3C305%3A%3AAID-BIT8%3E3.0.CO%3B2-M)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DyaK2sXksFCrurw%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=In%20vivo%20analysis%20of%20metabolic%20dynamics%20in%20Saccharomyces%20cerevisiae%3A%20I.%20Experimental%20observations&journal=Biotech%20Bioeng&doi=10.1002%2F%28SICI%291097-0290%2819970720%2955%3A2%3C305%3A%3AAID-BIT8%3E3.0.CO%3B2-M&volume=55&issue=2&pages=305-16&publication_year=1997&author=Theobald%2CU&author=Mailinger%2CW&author=Baltes%2CM&author=Rizzi%2CM&author=Reuss%2CM)  

9. Orth JD, Thiele I, Palsson BØ. What is flux balance analysis?Nat Biotechnol. 2010; 28(3):245–8.

[Article](https://doi.org/10.1038%2Fnbt.1614)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=20212490)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3108565)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXivV2rtL4%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=What%20is%20flux%20balance%20analysis%3F&journal=Nat%20Biotechnol&doi=10.1038%2Fnbt.1614&volume=28&issue=3&pages=245-8&publication_year=2010&author=Orth%2CJD&author=Thiele%2CI&author=Palsson%2CB%C3%98)  

10. Feist A, Palsson B. The biomass objective function. Curr Opin Microbiol. 2010; 13(3):344–9.

[Article](https://doi.org/10.1016%2Fj.mib.2010.03.003)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=20430689)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2912156)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXntVSlu7w%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20biomass%20objective%20function&journal=Curr%20Opin%20Microbiol&doi=10.1016%2Fj.mib.2010.03.003&volume=13&issue=3&pages=344-9&publication_year=2010&author=Feist%2CA&author=Palsson%2CB)  

11. Damiani C, Pescini D, Colombo R, Molinari S, Alberghina L, Vanoni M, Mauri G. An ensemble evolutionary constraint-based approach to understand the emergence of metabolic phenotypes. Nat Comput. 2014; 13(3):321–31.

[Article](https://link.springer.com/doi/10.1007/s11047-014-9439-4)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=An%20ensemble%20evolutionary%20constraint-based%20approach%20to%20understand%20the%20emergence%20of%20metabolic%20phenotypes&journal=Nat%20Comput&doi=10.1007%2Fs11047-014-9439-4&volume=13&issue=3&pages=321-31&publication_year=2014&author=Damiani%2CC&author=Pescini%2CD&author=Colombo%2CR&author=Molinari%2CS&author=Alberghina%2CL&author=Vanoni%2CM&author=Mauri%2CG)  

12. Colombo R, Damiani C, Mauri G, Pescini D, Caravagna G, Gilbert D, Tagliaferri R. Constraining mechanism based simulations to identify ensembles of parametrizations to characterize metabolic features In: Bracciali A, editor. Computational Intelligence Methods for Bioinformatics and Biostatistics. CIBB 2016. Lecture Notes in Computer Science. Cham: Springer: 2017. p. 10477:107–117.

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Constraining%20mechanism%20based%20simulations%20to%20identify%20ensembles%20of%20parametrizations%20to%20characterize%20metabolic%20features&publication_year=2017&author=Colombo%2CR&author=Damiani%2CC&author=Mauri%2CG&author=Pescini%2CD&author=Caravagna%2CG&author=Gilbert%2CD&author=Tagliaferri%2CR)  

13. Orth JD, Ronan RMT, Palsson BØ. Reconstruction and use of microbial metabolic networks: the core _Escherichia coli_ metabolic model as an educational guide. EcoSal plus. 2010; 4:1.

[Article](https://doi.org/10.1128%2Fecosalplus.10.2.1)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC2MXotV2ltQ%3D%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Reconstruction%20and%20use%20of%20microbial%20metabolic%20networks%3A%20the%20core%20Escherichia%20coli%20metabolic%20model%20as%20an%20educational%20guide&journal=EcoSal%20plus&doi=10.1128%2Fecosalplus.10.2.1&volume=4&publication_year=2010&author=Orth%2CJD&author=Ronan%2CRMT&author=Palsson%2CB%C3%98)  

14. Feist AM, Henry CS, Reed JL, Krummenacker M, Joyce AR, Karp PD, Broadbelt LJ, Hatzimanikatis V, Palsson BØ. A genome-scale metabolic reconstruction for Escherichia coli K-12 MG1655 that accounts for 1260 ORFs and thermodynamic information. Mol Syst Biol. 2007; 3(1):121.

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=17593909)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1911197)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20genome-scale%20metabolic%20reconstruction%20for%20Escherichia%20coli%20K-12%20MG1655%20that%20accounts%20for%201260%20ORFs%20and%20thermodynamic%20information&journal=Mol%20Syst%20Biol&volume=3&issue=1&publication_year=2007&author=Feist%2CAM&author=Henry%2CCS&author=Reed%2CJL&author=Krummenacker%2CM&author=Joyce%2CAR&author=Karp%2CPD&author=Broadbelt%2CLJ&author=Hatzimanikatis%2CV&author=Palsson%2CB%C3%98)  

15. Orth JD, Conrad TM, Na J, Lerman JA, Nam H, Feist AM, Palsson BØ. A comprehensive genome-scale reconstruction of Escherichia coli metabolism—2011. Mol Syst Biol. 2011; 7(1):535.

[Article](https://doi.org/10.1038%2Fmsb.2011.65)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=21988831)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3261703)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20comprehensive%20genome-scale%20reconstruction%20of%20Escherichia%20coli%20metabolism%E2%80%942011&journal=Mol%20Syst%20Biol&doi=10.1038%2Fmsb.2011.65&volume=7&issue=1&publication_year=2011&author=Orth%2CJD&author=Conrad%2CTM&author=Na%2CJ&author=Lerman%2CJA&author=Nam%2CH&author=Feist%2CAM&author=Palsson%2CB%C3%98)  

16. Hädicke O, Klamt S. EColiCore2: a reference network model of the central metabolism of _Escherichia coli_ and relationships to its genome-scale parent model. Scientific Reports. 2017; 7:39647.

[Article](https://doi.org/10.1038%2Fsrep39647)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=28045126)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC5206746)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC2sXkslGqtQ%3D%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=EColiCore2%3A%20a%20reference%20network%20model%20of%20the%20central%20metabolism%20of%20Escherichia%20coli%20and%20relationships%20to%20its%20genome-scale%20parent%20model&journal=Scientific%20Reports&doi=10.1038%2Fsrep39647&volume=7&publication_year=2017&author=H%C3%A4dicke%2CO&author=Klamt%2CS)  

17. Erdrich P, Steuer R, Klamt S. An algorithm for the reduction of genome-scale metabolic network models to meaningful core models. BMC Syst Biol. 2015; 9(1):48.

[Article](https://link.springer.com/doi/10.1186/s12918-015-0191-x)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=26286864)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4545695)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC28XivF2gtLw%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=An%20algorithm%20for%20the%20reduction%20of%20genome-scale%20metabolic%20network%20models%20to%20meaningful%20core%20models&journal=BMC%20Syst%20Biol&doi=10.1186%2Fs12918-015-0191-x&volume=9&issue=1&publication_year=2015&author=Erdrich%2CP&author=Steuer%2CR&author=Klamt%2CS)  

18. Guo AC, Jewison T, Wilson M, Liu Y, Knox C, Djoumbou Y, Lo P, Mandal R, Krishnamurthy R, Wishart DS. ECMDB: the E. coli Metabolome Database. Nucleic acids research. 2013; 41(D1):D625–D630.

[Article](https://doi.org/10.1093%2Fnar%2Fgks992)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=23109553)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC38XhvV2ktr%2FN)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=ECMDB%3A%20the%20E.%20coli%20Metabolome%20Database&journal=Nucleic%20acids%20research&doi=10.1093%2Fnar%2Fgks992&volume=41&issue=D1&pages=D625-D630&publication_year=2013&author=Guo%2CAC&author=Jewison%2CT&author=Wilson%2CM&author=Liu%2CY&author=Knox%2CC&author=Djoumbou%2CY&author=Lo%2CP&author=Mandal%2CR&author=Krishnamurthy%2CR&author=Wishart%2CDS)  

19. Petzold L. Automatic selection of methods for solving stiff and nonstiff systems of ordinary differential equations. SIAM J Sci Stat Comp. 1983; 1(4):136–48.

[Article](https://doi.org/10.1137%2F0904010)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Automatic%20selection%20of%20methods%20for%20solving%20stiff%20and%20nonstiff%20systems%20of%20ordinary%20differential%20equations&journal=SIAM%20J%20Sci%20Stat%20Comp&doi=10.1137%2F0904010&volume=1&issue=4&pages=136-48&publication_year=1983&author=Petzold%2CL)  

20. Jones E, Oliphant E, Peterson P, et al. SciPy: Open Source Scientific Tools for Python. 2001. [http://www.scipy.org/](http://www.scipy.org/). Accessed 24 Mar 2018.
21. Alted F, Vilata I, et al. PyTables: Hierarchical Datasets in Python. 2002. [http://www.pytables.org](http://www.pytables.org/). Accessed 24 Mar 2018.
22. Gutenkunst RN, Waterfall JJ, Casey FP, Brown KS, Myers CR, Sethna JP. Universally sloppy parameter sensitivities in systems biology models. PLoS Comput Biol. 2007; 3(10):e189.

[Article](https://doi.org/10.1371%2Fjournal.pcbi.0030189)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2000971)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BD2sXhsVCnu7bI)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Universally%20sloppy%20parameter%20sensitivities%20in%20systems%20biology%20models&journal=PLoS%20Comput%20Biol&doi=10.1371%2Fjournal.pcbi.0030189&volume=3&issue=10&publication_year=2007&author=Gutenkunst%2CRN&author=Waterfall%2CJJ&author=Casey%2CFP&author=Brown%2CKS&author=Myers%2CCR&author=Sethna%2CJP)  

23. Olivier BG, Rohwer JM, Hofmeyr JHS. Modelling cellular systems with PySCeS. Bioinformatics. 2005; 21(4):560–561.

[Article](https://doi.org/10.1093%2Fbioinformatics%2Fbti046)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=15454409)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BD2MXhsFSgurs%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Modelling%20cellular%20systems%20with%20PySCeS&journal=Bioinformatics&doi=10.1093%2Fbioinformatics%2Fbti046&volume=21&issue=4&pages=560-561&publication_year=2005&author=Olivier%2CBG&author=Rohwer%2CJM&author=Hofmeyr%2CJHS)  

24. Nobile MS, Besozzi D, Cazzaniga P, et al. GPU-accelerated simulations of mass-action kinetics models with cupSODA. J Supercomput. 2014; 69(1):17–24.

[Article](https://link.springer.com/doi/10.1007/s11227-014-1208-8)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=GPU-accelerated%20simulations%20of%20mass-action%20kinetics%20models%20with%20cupSODA&journal=J%20Supercomput&doi=10.1007%2Fs11227-014-1208-8&volume=69&issue=1&pages=17-24&publication_year=2014&author=Nobile%2CMS&author=Besozzi%2CD&author=Cazzaniga%2CP)  

25. Nobile MS, Cazzaniga P, Besozzi D, et al. cuTauLeaping: A GPU-powered tau-leaping stochastic simulator for massive parallel analyses of biological systems. PLoS ONE. 2014; 9(3):e91963.

[Article](https://doi.org/10.1371%2Fjournal.pone.0091963)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=24663957)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3963881)  [CAS](https://link.springer.com/articles/cas-redirect/1:CAS:528:DC%2BC2cXhsVKiu73M)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=cuTauLeaping%3A%20A%20GPU-powered%20tau-leaping%20stochastic%20simulator%20for%20massive%20parallel%20analyses%20of%20biological%20systems&journal=PLoS%20ONE&doi=10.1371%2Fjournal.pone.0091963&volume=9&issue=3&publication_year=2014&author=Nobile%2CMS&author=Cazzaniga%2CP&author=Besozzi%2CD)  

[Download references](https://citation-needed.springer.com/v2/references/10.1186/s12859-018-2181-7?format=refman&flavour=references)

## Acknowledgements
We thank Diletta Paone for conducting the Kolmogorov-Smirnov test and Nataliya Khomchyna for language editing.

### Funding
This work has been supported by SYSBIO Centre of Systems Biology, through the MIUR grant SysBioNet—Italian Roadmap for ESFRI Research Infrastructures. Publication costs of the manuscript have been funded by the MIUR grant SysBioNet—Italian Roadmap for ESFRI Research Infrastructures.

### Availability of data and materials
Dataset and python scripts implemented for this study are deposited on a GitHub repository at http://github.com/riccardocolombo/kineticensemble.

### About this supplement
This article has been published as part of _BMC Bioinformatics_ Volume 19 Supplement 7, 2018: 12th and 13th International Meeting on Computational Intelligence Methods for Bioinformatics and Biostatistics (CIBB 2015/16). The full contents of the supplement are available online at [https://bmcbioinformatics.biomedcentral.com/articles/supplements/volume-19-supplement-7](https://bmcbioinformatics.biomedcentral.com/articles/supplements/volume-19-supplement-7).

## Author information
Author notes

### Authors and Affiliations
1. Department of Informatics, Systems and Communication, University of Milan - Bicocca, Viale Sarca, 336, Milan, 20126, Italy

Riccardo Colombo, Chiara Damiani & Giancarlo Mauri

2. SYSBIO - Centre of Systems Biology, Piazza della Scienza, 2, Milan, 20126, Italy

Riccardo Colombo, Chiara Damiani, Giancarlo Mauri & Dario Pescini

3. Department of Statistics and Quantitative Methods, University of Milan - Bicocca, Via Bicocca degli Arcimboldi, 8, Milan, 20126, Italy

Dario Pescini

4. College of Engineering, Design and Physical Sciences, Brunel University, Middlesex, London, Uxbridg, UB8 3PH, UK

David Gilbert

5. Computer Science Department, Brandenburg University of Technology Cottbus-Senftenberg, Walther-Pauer-Str. 2, Cottbus, D-03046, Germany

Monika Heiner

Authors

1. Riccardo Colombo

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Riccardo%20Colombo) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Riccardo%20Colombo%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

2. Chiara Damiani

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Chiara%20Damiani) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Chiara%20Damiani%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

3. David Gilbert

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=David%20Gilbert) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22David%20Gilbert%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

4. Monika Heiner

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Monika%20Heiner) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Monika%20Heiner%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

5. Giancarlo Mauri

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Giancarlo%20Mauri) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Giancarlo%20Mauri%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

6. Dario Pescini

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Dario%20Pescini) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Dario%20Pescini%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

### Contributions
RC, DP, DG, MH conceived and designed the study, DG, MH acquired data DP and RC performed the analysis and interpretation of data, RC drafted the manuscript, CD and GM provided critical revision and suggestions. All of the authors have read and approved the final manuscript.

### Corresponding author
Correspondence to [Riccardo Colombo](mailto:riccardo.colombo@disco.unimib.it).

## Ethics declarations
### Competing interests
The authors declare that they have no competing interests.

### Ethics approval and consent to participate
Not applicable.

### Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Additional files
### [Additional file 1](https://static-content.springer.com/esm/art%3A10.1186%2Fs12859-018-2181-7/MediaObjects/12859_2018_2181_MOESM1_ESM.xml)
ECC2C.xml. SBML file for the ECC2comp model of _E. coli_ used for the analysis. (XML 69. 8 kb)

### [Additional file 2](https://static-content.springer.com/esm/art%3A10.1186%2Fs12859-018-2181-7/MediaObjects/12859_2018_2181_MOESM2_ESM.xlsx)
X0etc.xlsx. In tab “conc” are listed initial concentrations of metabolites for the 5 different phenotypes. In tab “FeedNoFilt” are listed metabolites provided at constant concentration throughout the simulation and metabolites not evaluated to verify the steady state. (XLSX 14.8 kb)

### [Additional file 3](https://static-content.springer.com/esm/art%3A10.1186%2Fs12859-018-2181-7/MediaObjects/12859_2018_2181_MOESM3_ESM.zip)
Github. The generated dataset (ECcoliExpsParam_10_Filter_0.001.h5) and python scripts implemented for this study are deposited on a GitHub repository at [http://github.com/riccardocolombo/kineticensemble](http://github.com/riccardocolombo/kineticensemble) (ZIP 1.52e+7 kb)

## Rights and permissions
**Open Access** This article is distributed under the terms of the Creative Commons Attribution 4.0 International License([http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the CreativeCommons license, and indicate if changes were made. The Creative Commons Public Domain Dedication waiver([http://creativecommons.org/publicdomain/zero/1.0/](http://creativecommons.org/publicdomain/zero/1.0/)) applies to the data made available in this article, unless otherwise stated.

[Reprints and permissions](https://s100.copyright.com/AppDispatchServlet?title=Emerging%20ensembles%20of%20kinetic%20parameters%20to%20characterize%20observed%20metabolic%20phenotypes&author=Riccardo%20Colombo%20et%20al&contentID=10.1186%2Fs12859-018-2181-7&copyright=The%20Author%28s%29&publication=1471-2105&publicationDate=2018-07-09&publisherName=SpringerNature&orderBeanReset=true&oa=CC%20BY%20%2B%20CC0)

## About this article
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/svg/22983715/1710064149074-c10e88d9-b707-4f82-9e14-9725e7c3f412.svg)

### Cite this article
Colombo, R., Damiani, C., Gilbert, D. _et al._ Emerging ensembles of kinetic parameters to characterize observed metabolic phenotypes. _BMC Bioinformatics_**19** (Suppl 7), 251 (2018). https://doi.org/10.1186/s12859-018-2181-7

[Download citation](https://citation-needed.springer.com/v2/references/10.1186/s12859-018-2181-7?format=refman&flavour=citation)

+ Published: 09 July 2018
+ DOI: https://doi.org/10.1186/s12859-018-2181-7

### Keywords
  


> 来自: [Emerging ensembles of kinetic parameters to characterize observed metabolic phenotypes | BMC Bioinformatics](https://link.springer.com/article/10.1186/s12859-018-2181-7?fromPaywallRec=false)
>

