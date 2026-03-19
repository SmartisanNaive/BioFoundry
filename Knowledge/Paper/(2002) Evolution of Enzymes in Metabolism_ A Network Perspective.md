<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1710063817089-ceb1041d-1bcf-4f9c-9f6f-96b016b40aee.gif)

[https://doi.org/10.1016/S0022-2836(02)00546-6](https://doi.org/10.1016/S0022-2836(02)00546-6)

[https://www.sciencedirect.com/science/article/abs/pii/S0022283602005466](https://www.sciencedirect.com/science/article/abs/pii/S0022283602005466)

Referred to by

Journal of Molecular Biology, Volume 324, Issue 2, 22 November 2002, Pages 387

Rui Alves, Raphael A.G Chaleil, Michael J.E Sternberg

[View PDF](https://www.sciencedirect.com/science/article/pii/S0022283602011579/pdfft?md5=05807b7227158d1e93f650596f73fe1f&pid=1-s2.0-S0022283602011579-main.pdf)

## Abstract
Several models have been proposed to explain the origin and evolution of [enzymes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme) in metabolic pathways. Initially, the retro-evolution model proposed that, as enzymes at the end of pathways depleted their substrates in the primordial soup, there was a pressure for earlier enzymes in pathways to be created, using the later ones as initial [template](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/dna-template), in order to replenish the pools of depleted metabolites. Later, the recruitment model proposed that initial templates from other pathways could be used as long as those enzymes were similar in chemistry or [substrate specificity](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-specificity). These two models have dominated recent studies of enzyme evolution. These studies are constrained by either the small scale of the study or the artificial restrictions imposed by pathway definitions. Here, a network approach is used to study enzyme evolution in fully [sequenced genomes](https://www.sciencedirect.com/topics/immunology-and-microbiology/sequenced-genomes), thus removing both constraints. We find that homologous pairs of enzymes are roughly twice as likely to have evolved from enzymes that are less than three steps away from each other in the reaction network than pairs of non-homologous enzymes. These results, together with the conservation of the type of chemical reaction catalyzed by evolutionarily related enzymes, suggest that functional blocks of similar chemistry have evolved within [metabolic networks](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/metabolic-network). One possible explanation for these observations is that this local evolution phenomenon is likely to cause less global physiological disruptions in metabolism than evolution of enzymes from other enzymes that are distant from them in the metabolic network.

## Introduction
Cellular metabolism is a complex network of physico-chemical processes, most of them catalyzed by enzymes, that allows the survival and reproduction of cells. In the early stages of evolution of metabolism, it is likely that a small number of enzymes with low effectiveness and broad specificity existed. Under natural selection, these enzymes were duplicated, becoming increasingly specialized and effective. The broad specificity of many of these enzymes must have been lost. A “second wave” of enzyme evolution would then have started with even more specialized enzymes evolving from pre-existing enzymes that already had high specificity and efficiency. 

There are two prevalent models currently used to explain enzyme evolution. Retro-evolution,1 originally suggested by Horowitz, proposes that enzymes at the beginning of pathways evolve from the enzymes at the end of pathways, by duplication and mutation of the latter. As substrates from the end of the pathway were depleted in the primordial soup, there was a selective pressure for new enzymes to produce these substrates from other pre-existing compounds. Later, Jensen proposed the recruitment model of enzyme evolution,2 suggesting that enzymes are likely to have evolved by duplication and mutations of similar enzymes from other pathways. One way to quantify this similarity is by using the enzyme commission (EC) classification scheme, based on a number hierarchy of four digits.3 The first digit describes the class of the enzyme, namely 1 for oxyreductases, 2 for tranferases, 3 for hydrolases, 4 for lyases, 5 for isomerases and 6 for synthetases. Subsequent digits define further details of function and reactants. If two enzymes belong to the same class in this classification, they are considered to have similar chemical function. Recent studies,4., 5., 6., 7., 8., 9., 10. using both sequence and structure similarity to identify probable homology, have examined the evolution of enzymes in pathways. Copley & Bork10 studied the evolution of 23 different TIM barrel SCOP superfamilies and found indications that at least 12 of these had a common evolutionary origin. Tsoka & Ouzounis7 have studied the enzymes of _Escherichia coli_ and found that enzymes from the same family are distributed among different pathways. Teichmann _et al._5 found that homologues are twice as likely to be found in different pathways than in the same pathway. These studies suggest, as a general model, that new enzymes are more likely to have evolved from enzymes belonging to the same enzyme class than from enzymes in the same pathway, thus <font style="color:#DF2A3F;">following the recruitment model</font>.

One constraint of studying enzyme evolution in a pathway context is that metabolism is a very intricate network, with pathways branching into each other. There are several databases that provide annotated metabolic pathways for different organisms, like EcoCYC,11 KEGG12 and WIT13. Many enzymes that are thought to have evolved by recruitment may have evolved by retro evolution, being only one or two reactions away from their homologues in a different pathway. Here, we study enzyme evolution in the context of the metabolic network, thus avoiding this problem. This change of context also makes it useful to redefine the retro-evolution and recruitment models as local (homologous enzymes being close to each other in the reaction network, independent of the pathway they belong to) evolution and long-distance (homologous enzymes being far from each other in the reaction network, independent of the pathway they belong to) evolution, respectively.

Another constraint of those studies is the small scale of the study, either in the sense of using a limited number of proteins9 or that they study only one organism,4., 5., 6., 7., 8., 10. usually _E. coli_. There are now several fully sequenced and annotated genomes that lend themselves to the same kinds of study and evolutionary results from several organisms are needed to build a more accurate picture of the evolution of metabolism. Here, a network approach is used to study enzyme evolution in the fully sequenced genomes of 12 organisms, thus removing both constraints.

## Section snippets
## Building and Analyzing Metabolic Networks
Our approach is summarized in Figure 1. We parsed the information in the LIGAND part of KEGG 12 and BRENDA† databases to construct a new database, with all of the known enzyme activities defined by the enzyme commission according to their EC number. BRENDA is a database that was used to complete the information in the LIGAND regarding substrates, products and stoichiometry of enzyme reactions. We included information about the substrates, products and

## Evolution of Enzymes in a Metabolic Network
Figure 4 shows that, on average, long-distance evolution is at least as common as local evolution in the metabolic network. However, local evolution, as measured by the percentage of pairs of homologues that are less than three steps away from each other in the network, is always significantly higher than would be expected by chance alone. This is independent of the promiscuity index that is set as threshold in the connectivity matrix. Random shuffling (see Materials and Methods for an

## Chemistry Conservation in Evolution
Recent general surveys of the structure and function of homologous proteins have highlighted the fact that chemistry tends to be more conserved than substrate specificity.4., 5., 17., 18. However, as the degree of sequence identity between pairs of enzymes decreases, the extent of commonality of function decreases. Todd _et al_.6 have shown that some fairly close homologues can differ in chemistry, sometimes having greater similarity of substrate specificity. In keeping with this study, we

## Discussion and Conclusions
Our key results are: (1) the percentage of pairs of homologous enzymes that are less than three steps away from each other in the metabolic network is significantly higher than what is expected had the network evolved randomly. (2) There often is a clustering effect of enzymes belonging to the same class in metabolic networks. (3) In several species, these two effects are linked and there is a particularly strong tendency for homologous enzymes with similar chemistry to be found less than three 

## Database construction
We used LIGAND (version 19.0) and BRENDA (Internet version of August 2001†) for Metabolic Network general reconstruction. Version 4.01 of Mathematica30 was used to analyze the characteristics of metabolic network graphs. We used SWISSPROT (version 39), WIT (version December 1999) and KEGG (current version) for reconstructing the enzyme sequence of each organism and SCOP (version 1.50) for structure-based homology. We ran PSIBLAST version 4.2.3 with the default

## Acknowledgements
R.A. was supported by the Imperial Cancer Research Fund (ICRF) and the BBSRC. R.A.G.C. was supported by the ICRF. M.J.E.S. was supported by the ICRF and Imperial College. We thank Dr Peter Sasieni (ICRF) for statistical advice.

## Cited by (63)
### [Enzyme-free multicolor biosensor based on Cu<sup>2+</sup>-modified carbon nitride nanosheets and gold nanobipyramids for sensitive detection of neuron specific enolase](https://www.sciencedirect.com/science/article/pii/S0925400518321269)
2019, Sensors and Actuators, B: Chemical

Natural enzymes are usually made up of proteins and they are higher molecular weight compounds, which composed of amino acid chains linked together with peptide bonds [22]. Principally, enzymes are involving in a wide range of biological functions including metabolism, digestion, etc [25]. However, they have some inherent disadvantages, such as expensive, extraction and separation difficulties, and protein susceptibility to the temperature and pH stability, which limited their widespread use [26,27].

### [A global evolutionary and metabolic analysis of human obesity gene risk variants](https://www.sciencedirect.com/science/article/pii/S0378111917305139)
2017, Gene

Groups with observable differences in genetic variation between ancestral and derived variant frequencies (AFR, ASW, and MKK; all of African descent but now in an environment of genetic admixture) support the hypothesis that these variants were selected in different evolutionary environments. The selection of obesity gene risk variants during the course of human evolution has shaped the efficiency of our digestion, absorption, and assimilation of nutrients to optimize energy metabolism involved in storage of energy for later use when food becomes limiting (Alves et al., 2002; Caetano-Anolles et al., 2009). However, since most developed populations no longer experience seasonal food shortages and episodic famines, these obesity gene risk variants now interact with our obesogenic environment, characterized by energy dense foods and a sedentary lifestyle, to increase the prevalence of obesity (Chakravarthy and Booth, 2004).

### [Origins of specificity and promiscuity in metabolic networks](https://www.sciencedirect.com/science/article/pii/S0021925820684927)
2011, Journal of Biological Chemistry

This diversity might be explained, in part, by the role that enzyme promiscuity plays, providing a common background level of metabolism to the organisms (4). Thus, how enzymes have evolved to their present form in organisms appears to be linked to the question of how metabolic pathways emerged and configured extant metabolic networks (5). In fact, although many enzyme families and superfamilies sharing structural and functional features have been identified, it has been recognized that distant evolutionary relationships are expected to be difficult to identify solely from global sequence comparison (6).

[View all citing articles on Scopus](http://www.scopus.com/scopus/inward/citedby.url?partnerID=10&rel=3.0.0&eid=2-s2.0-0036303685&md5=d924590aec03595417eca655af37fe7)

[†](https://www.sciencedirect.com/science/article/abs/pii/S0022283602005466#bFN1)

Present address: R. Alves, Departament Ciencies Mediques Basiques, Universidad de Lleida, Av Rouvira Roure 44, 25198 Lleida, Spain.

[View full text](https://www.sciencedirect.com/science/article/pii/S0022283602005466)

Copyright © 2002 Elsevier Science Ltd. All rights reserved.  


> 来自: [Evolution of Enzymes in Metabolism: A Network Perspective - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022283602005466)
>

