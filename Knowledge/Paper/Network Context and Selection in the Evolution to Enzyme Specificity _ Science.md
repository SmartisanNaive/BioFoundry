Science

31 Aug 2012

Vol 337, Issue 6098

pp. 1101-1104

## Good Enough Can Be Good Enough
To begin to understand why some enzymes are promiscuous and have many substrates, whereas others are highly specific, and why some have high activity, whereas others appear not to be optimized, **Nam **_**et al.**_ (p. [1101](https://doi.org/10.1126/science.1216861)) analyzed metabolic networks in bacteria. Specialist enzymes are essential for life, catalyze a high flux of enzymatic activity, and are more highly regulated. However, not all enzymes appear to be on a track of gradual improvement of specificity and efficiency. Generalist enzymes seem to well serve their own purposes, and their optimization may not justify the evolutionary cost.

## Abstract
Enzymes are thought to have evolved highly specific catalytic activities from promiscuous ancestral proteins. By analyzing a genome-scale model of _Escherichia coli_ metabolism, we found that 37% of its enzymes act on a variety of substrates and catalyze 65% of the known metabolic reactions. However, it is not apparent why these generalist enzymes remain. Here, we show that there are marked differences between generalist enzymes and specialist enzymes, known to catalyze a single chemical reaction on one particular substrate in vivo. Specialist enzymes (i) are frequently essential, (ii) maintain higher metabolic flux, and (iii) require more regulation of enzyme activity to control metabolic flux in dynamic environments than do generalist enzymes. Furthermore, these properties are conserved in Archaea and Eukarya. Thus, the metabolic network context and environmental conditions influence enzyme evolution toward high specificity.

#### SIGN UP FOR THE _SCIENCE_ADVISER NEWSLETTER
The latest news, commentary, and research, free to your inbox daily

Ancestral enzymes are proposed to have exhibited broad substrate specificity and low catalytic efficiency ([1](https://www.science.org/doi/full/10.1126/science.1216861#core-R1)). Through mutation, duplication, and horizontal gene transfer, gene families diversified and promiscuous enzymes apparently were refined to exhibit specific and more efficient catalytic abilities ([2](https://www.science.org/doi/full/10.1126/science.1216861#core-R2), [3](https://www.science.org/doi/full/10.1126/science.1216861#core-R3)). Thus, today’s metabolic enzymes are commonly assumed to be “specialists,” having evolved to catalyze one reaction on a unique primary substrate in an organism. However, some enzymes are “generalists” that promiscuously catalyze reactions on a variety of substrates in vivo ([2](https://www.science.org/doi/full/10.1126/science.1216861#core-R2)) or exhibit multifunctionality by catalyzing multiple classes of reactions, often at different active sites ([4](https://www.science.org/doi/full/10.1126/science.1216861#core-R4)). Thus, a fundamental question arises: Why do some enzymes evolve to become specialists, whereas others retain generalist characteristics? By analyzing enzyme functions and properties in experimental data and in silico metabolic network models, we show that the in vivo biochemical network context in which an enzyme resides may influence the evolution of enzyme specificity.

How many metabolic enzymes are generalists? To answer this question, we used a comprehensive reconstruction of the _Escherichia coli_ K-12 MG1655 metabolic network, which accounts for the metabolic functions of 1260 gene products (28% of the predicted and experimentally validated open reading frames in _E. coli_) ([5](https://www.science.org/doi/full/10.1126/science.1216861#core-R5)), which contribute to 1081 enzyme complexes analyzed in this study. In the reconstruction, we define a reaction as a unique set of substrates that are chemically transformed into a unique set of products. With this definition, we classified 677 enzymes as specialists because they catalyze one unique reaction and 404 as generalists because they catalyze multiple reactions. Thus, we estimate that 37% of metabolic enzymes in _E. coli_ are generalists, most of which exhibit substrate promiscuity (fig. S1A). Furthermore, specialist and generalist enzymes catalyze 454 and 859 metabolic reactions, respectively, distributed across many metabolic subsystems ([Fig. 1, A and B](https://www.science.org/doi/full/10.1126/science.1216861#F1)). Thus, contrary to the textbook view of enzymes as “specific catalysts,” generalist enzymes have a prominent role in _E. coli_, catalyzing at least 65% of the nonspontaneous metabolic reactions.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073530850-a3ca48cf-6aed-47b1-8c7e-bb98b721d1bd.jpeg)

Fig. 1 (**A**) Specialist and generalist genes and proteins and their associated reactions were enumerated in _E. coli_ metabolism. (**B**) Several metabolic subsystems were enriched in specialist enzyme reactions (SERxns) or generalist enzyme reactions (GERxns) in _E_. _coli_ (hypergeometric _P _≤ 0.05). (**C**) Reaction flux magnitudes were rank-ordered and binned in histograms for each unique media condition. A heat map was used to visualize histograms for all 174 media conditions (columns) with each row representing bins spanning the given flux rank ranges (_y_ axis). Color intensity shows histogram bin height, corresponding to the percentage of reactions in the bin. Example histograms (shown on the right) provide for one representative condition. SERxns tend to have a higher flux, but low-flux SERxns are enriched in enzymes that synthesize low-abundance essential cell components, such as cofactors and prosthetic groups (fig. S4C). (**D**) Genes for specialist enzymes are more frequently essential in vivo. (**E**) In silico, few essential GERxns were identified for growth on glucose minimal medium. (**F**) For all 174 simulated growth conditions, SERxns are significantly enriched among in silico–predicted reactions essential for growth, representing 56% of the essential reactions (inset).

[Open in viewer](https://www.science.org/doi/full/10.1126/science.1216861#F1)

We performed several network-wide analyses to provide additional support for our estimates and the classification. First, we found that almost all genes in the network have been well characterized and studied in more than 61,727 published studies (fig. S1D). Second, we found no correlation between our classification and knowledge depth, i.e., neither specialist nor generalist enzymes had been studied in more depth (fig. S1E). Third, our generalist enzymes did not likely include many latent promiscuous reactions measured in vitro that likely do not occur in vivo, because 85% of the generalist enzymes reactions (GERxns) were active in silico in common growth conditions. This is the same percentage seen for specialist enzyme reactions (SERxns) (fig. S2). Fourth, because enzyme classification may vary with further study, we tested the sensitivity of the results presented in this work. We found the results to be qualitatively robust with improvements in the metabolic network from the discovery of new enzymes, variations in enzyme classification, and the exclusion of promiscuous enzymes or multifunctional enzymes from the generalist class (fig. S3). Although transporter reactions were not included in the groups of SERxns or GERxns, their inclusion would not qualitatively change the results in this work (fig. S3). Thus, the classification and results from our subsequent analysis are robust.

Why are so many generalist enzymes evolutionarily retained, whereas others became specialists? Demands for higher metabolic flux may provide an evolutionary selective pressure to enhance an enzyme’s catalytic rate and reduce the required enzyme concentration. However, catalytic improvements for one substrate of a generalist enzyme can suppress other catalytic activities ([6](https://www.science.org/doi/full/10.1126/science.1216861#core-R6)). To determine if specialists maintain higher flux, we estimated the steady-state metabolic flux rates ([7](https://www.science.org/doi/full/10.1126/science.1216861#core-R7)) for all _E. coli_ enzymes using a genome-scale metabolic network model. We employed a Markov chain Monte Carlo sampling method ([8](https://www.science.org/doi/full/10.1126/science.1216861#core-R8)) to simulate flux on 174 media conditions with different nutrient compositions ([9](https://www.science.org/doi/full/10.1126/science.1216861#core-R9)). For each growth condition, the median flux for each reaction was rank-ordered to determine the relative flux among reactions.

Across all simulated growth conditions, SERxns maintained higher flux than GERxns ([Fig. 1C](https://www.science.org/doi/full/10.1126/science.1216861#F1) and fig. S4). Gene duplications may have been fixed in the population when specialization occurred to increase activity of high-flux enzymes. Higher activity would permit lower enzyme concentrations, thereby offsetting the cost of duplication ([10](https://www.science.org/doi/full/10.1126/science.1216861#core-R10)). Consistent with this reasoning, _k_cat values are significantly higher for high-flux specialist enzymes than for all other enzymes (fig. S5C, Wilcoxon _P _= 2.8 × 10−7).

Although flux level may contribute to enzyme specialization, gene essentiality may also contribute. High substrate affinity for essential enzymes could mitigate substrate competition in the synthesis of necessary biomass components, irrespective of flux level. Consistent with this hypothesis, we found that essential enzymes have lower _K_m values and therefore higher substrate affinity (fig. S5F, Wilcoxon _P _= 1.1 × 10−11). Furthermore, specialist enzymes are enriched among experimentally determined essential genes ([11](https://www.science.org/doi/full/10.1126/science.1216861#core-R11)) (hypergeometric _P _= 8.65 × 10−5, [Fig. 1D](https://www.science.org/doi/full/10.1126/science.1216861#F1)). In silico simulation also demonstrated that cell growth rarely directly depends on flux through generalist enzymes ([Fig. 1E](https://www.science.org/doi/full/10.1126/science.1216861#F1)), whereas many SERxns were essential for growth across all 174 tested media conditions ([Fig. 1F](https://www.science.org/doi/full/10.1126/science.1216861#F1) and fig. S6).

Gene essentiality ([12](https://www.science.org/doi/full/10.1126/science.1216861#core-R12), [13](https://www.science.org/doi/full/10.1126/science.1216861#core-R13)) and reaction fluxes often vary ([8](https://www.science.org/doi/full/10.1126/science.1216861#core-R8), [14](https://www.science.org/doi/full/10.1126/science.1216861#core-R14), [15](https://www.science.org/doi/full/10.1126/science.1216861#core-R15)) because natural environments are dynamic and nutrient concentrations fluctuate in the microbial microenvironment ([16](https://www.science.org/doi/full/10.1126/science.1216861#core-R16)). The need to regulate reaction flux in dynamic environments could induce gene duplication and enzyme specialization to simplify the combinatorial complexity of regulating multiple reactions on a single enzyme (e.g., see serine hydroxymethyltransferase in fig. S7). To test this hypothesis, we identified enzymes that will require more metabolic regulation in dynamic environments by simulating changes in carbon source and electron acceptors for _E. coli_. For each substrate shift, the model predicted whether reaction flux should increase or decrease, and these predictions were consistent with measured differential gene expression (fig. S8) ([17](https://www.science.org/doi/full/10.1126/science.1216861#core-R17)).

Across all shifts in growth media, there was a considerable difference in the percentages of active SERxns and GERxns that significantly changed their flux between growth conditions ([Fig. 2A](https://www.science.org/doi/full/10.1126/science.1216861#F2)). SERxn fluxes were often more than twice as likely to change than GERxn fluxes. Thus, flux through SERxns is considerably more sensitive to environmental change, whereas GERxn fluxes vary less. To examine if this is a general property, we simulated 15,051 pairwise environmental shifts. In 96% of these shifts, SERxns changed more frequently than GERxns ([Fig. 2B](https://www.science.org/doi/full/10.1126/science.1216861#F2)). This difference was strongest for environmental shifts that cause more than 8% of the reactions to change flux (fig. S9). Because SERxns are subject to greater flux changes in nutritionally dynamic environments, it seems that duplication may have occurred to allow more focused regulation of fluxes. This duplication would be reinforced as the enzymes enhance their catalytic specificity.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073530680-e3040e10-0ef7-41a1-83dd-4089ff60b65e.jpeg)

Fig. 2 (**A**) Phenotypic measurements, such as substrate uptake rates ([9](https://www.science.org/doi/full/10.1126/science.1216861#core-R9)), were acquired and used to parameterize the model to predict the percentage of reactions that change flux in four nutritional shifts. (**B**) A systematic computational screen of 15,051 shifts between 174 carbon substrates shows that SERxns tend to change more frequently. By rank-ordering shifts based on the number of enzyme-catalyzed reaction fluxes that change, the difference is particularly clear for shifts that cause more reactions to change. Most cases in which there is only a weak difference involve shifts between two similar primary carbon susbstrates, as measured by their Tanimoto coefficients (inset; Tanimoto coefficients are averaged across sets of 100 shifts).

[Open in viewer](https://www.science.org/doi/full/10.1126/science.1216861#F2)

In dynamic environments, metabolic flux can be regulated through metabolite-protein interactions or posttranslational modifications (PTMs) ([18](https://www.science.org/doi/full/10.1126/science.1216861#core-R18), [19](https://www.science.org/doi/full/10.1126/science.1216861#core-R19)). We quantified the association of metabolic regulation with enzyme specificity, using a few hundred metabolite-mediated regulatory interactions obtained from the EcoCyc database and enzyme PTMs from mass spectrometry studies in _E. coli_ ([9](https://www.science.org/doi/full/10.1126/science.1216861#core-R9)). Allosteric, uncompetitive, and noncompetitive regulatory interactions were enriched among specialists (hypergeometric _P _= 9 × 10−4), as were PTMs (hypergeometric _P _= 5 × 10−3). Metabolic regulation was less prevalent among generalists, consistent with the decreased need to change flux through their reactions in dynamic environments. Moreover, fluxes for reactions catalyzed by the same generalist often covary, thereby reducing requirements for more complex regulation (fig. S10).

To further assess the association of specificity with regulation, we quantified how frequently each reaction changed flux across all simulated 15,051 media shifts. K-means clustering elucidated three dominant reaction clusters ([Fig. 3A](https://www.science.org/doi/full/10.1126/science.1216861#F3)). Two clusters show frequent changes in flux, and these were enriched in specialists, particularly those associated with central and amino acid metabolism ([Fig. 3B](https://www.science.org/doi/full/10.1126/science.1216861#F3)). The reaction cluster with few changes in flux was significantly enriched in generalists ([Fig. 3C](https://www.science.org/doi/full/10.1126/science.1216861#F3)). PTMs and small-molecule–mediated allosteric regulation were enriched within the cluster that experienced the most change in flux (hypergeometric _P _= 5 × 10−3), but depleted from the cluster dominated by generalists (hypergeometric _P _= 3 × 10−3; [Fig. 3D](https://www.science.org/doi/full/10.1126/science.1216861#F3) and fig. S11). Thus, enzymes that exhibit more extensive metabolic regulation tend to have evolved increased enzyme specificity.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073530926-fa5081e6-e1d3-4670-92ce-98503fefd09a.jpeg)

Fig. 3 (**A**) Clustering reactions that change (blue) or do not change (white) across 15,051 different media shifts (_x_ axis) yields three distinct groups, (**B**) which are each enriched in unique metabolic subsystems. (**C**) Specialist enzymes are enriched in more sensitive clusters, whereas generalist enzymes are enriched in the cluster with few flux changes. (**D**) The number of PTMs (acetylation, phosphorylation, and/or succinylation) on enzymes increases with sensitivity of clusters.

[Open in viewer](https://www.science.org/doi/full/10.1126/science.1216861#F3)

The aforementioned properties show how enzyme specificity correlates with holistic functions of the _E. coli_ metabolic network. However, these properties should be conserved if they influence selection of enzyme specificity in protein evolution. Thus, we examined their conservation using genome-scale metabolic models of microbes from the other domains of life, including the archeon _Methanosarcina barkeri_ ([20](https://www.science.org/doi/full/10.1126/science.1216861#core-R20)) and the eukaryotes _Saccharomyces cerevisiae_ ([21](https://www.science.org/doi/full/10.1126/science.1216861#core-R21)) and _Chlamydomonas reinhardtii_ ([22](https://www.science.org/doi/full/10.1126/science.1216861#core-R22)). Similar to _E. coli_, the three organisms contain numerous generalist enzymes. Common growth conditions were simulated for each organism to estimate metabolic flux. In each organism, specialist enzymes maintained a higher flux on average than generalist enzymes. Moreover, when environmental shifts were simulated for each organism, generalist enzymes were less likely to change flux between growth conditions (fig. S12). Even as microbes diversified, high flux and a need for focused regulation in varying environments remained as general features of specialist enzymes.

It is generally believed that highly promiscuous ancestral enzymes eventually evolved to become specific and highly efficient ([1](https://www.science.org/doi/full/10.1126/science.1216861#core-R1)). However, many current enzymes are only moderately efficient ([23](https://www.science.org/doi/full/10.1126/science.1216861#core-R23)), and there are numerous generalists. Thus, evolution has not converged to a point where metabolic enzymes are all specialists. Our results suggest that this convergence has been hindered in part by the lower essentiality, smaller flux, and reduced regulatory requirements of generalist enzymes, including those that are multifunctional and those exhibiting substrate promiscuity (figs. S3B and S4C). The specialization of these enzymes may not provide adequate fitness advantages to offset the cost of gene duplication and maintenance ([10](https://www.science.org/doi/full/10.1126/science.1216861#core-R10)) that accompanies the separation of catalytic functions into several specialists. In addition, these selective pressures may not influence some classes of enzymes if their generalist activities are desirable, such as in the degradation and clearance of diverse toxins ([24](https://www.science.org/doi/full/10.1126/science.1216861#core-R24)) or the synthesis of structural lipids or glycoconjugates. However, our results suggest that many metabolic enzymes will specialize when an environmental change elicits a fitness challenge that causes a generalist to contribute to the high-flux ([8](https://www.science.org/doi/full/10.1126/science.1216861#core-R8)) or essential biomass-producing core ([25](https://www.science.org/doi/full/10.1126/science.1216861#core-R25)) of metabolism, or if new environmental fluctuations require more focused regulation of flux. Preliminary analysis suggests that potential examples of this divergence include serine hydroxymethyltransferase and its isozyme LtaE (fig. S7) or pyruvate formate lyase and TdcE (see supplementary materials).

Our results demonstrate that the metabolic network, as a whole, supports organismal survival and influences cell physiology in a given environment. By analyzing the functions of its pathways and using biomolecular networks to integrate many disparate data types into a coherent whole, we show that systems biology allows the elucidation of selection pressures that are not apparent at the level of a single enzyme ([26](https://www.science.org/doi/full/10.1126/science.1216861#core-R26)–[29](https://www.science.org/doi/full/10.1126/science.1216861#core-R29)).

## Acknowledgments
We thank D. Zielinski for insightful discussion on this work. This work was supported by NIH, NSF, and U.S. Department of Energy grants 2R01GM057089-13, NSF GK-12 742551, DE-SC0004917, and DE-FG02-09ER25917. Data are available at the NCBI Gene Expression Omnibus (GEO) database (GSE34631).

## Supplementary Material
### Summary
Materials and Methods

Supplementary Text

Figs. S1 to S17

Tables S1 and S2

References ([30](https://www.science.org/doi/full/10.1126/science.1216861#core-R30)_–_[78](https://www.science.org/doi/full/10.1126/science.1216861#core-R78))

Database S1

### Resources
File(database_s1.xlsx)

+ [Download](https://www.science.org/doi/suppl/10.1126/science.1216861/suppl_file/database_s1.xlsx)
+ 284.39 KB

## References and Notes
1

Jensen R. A., Enzyme recruitment in evolution of new function. _Annu. Rev. Microbiol.__**30**_, 409 (1976).

2

Khersonsky O., Tawfik D. S., Enzyme promiscuity: A mechanistic and evolutionary perspective. _Annu. Rev. Biochem.__**79**_, 471 (2010).

3

Innan H., Kondrashov F., The evolution of gene duplications: Classifying and distinguishing between models. _Nat. Rev. Genet.__**11**_, 97 (2010).

4

Khersonsky O., Malitsky S., Rogachev I., Tawfik D. S., Role of chemistry versus substrate binding in recruiting promiscuous enzyme functions. _Biochemistry__**50**_, 2683 (2011).

5

Feist A. M., et al., A genome-scale metabolic reconstruction for _Escherichia coli_ K-12 MG1655 that accounts for 1260 ORFs and thermodynamic information. _Mol. Syst. Biol.__**3**_, 121 (2007).

6

Aharoni A., et al., The ‘evolvability’ of promiscuous protein functions. _Nat. Genet.__**37**_, 73 (2005).

7

Lewis N. E., Nagarajan H., Palsson B. O., Constraining the metabolic genotype-phenotype relationship using a phylogeny of in silico methods. _Nat. Rev. Microbiol.__**10**_, 291 (2012).

8

Almaas E., Kovács B., Vicsek T., Oltvai Z. N., Barabási A. L., Global organization of metabolic fluxes in the bacterium _Escherichia coli_. _Nature__**427**_, 839 (2004).

9

Materials and methods are available as supplementary materials on _Science_ Online.

10

Wagner A., Energy costs constrain the evolution of gene expression. _J. Exp. Zool. B Mol. Dev. Evol.__**308B**_, 322 (2007).

11

Baba T., et al., Construction of _Escherichia coli_ K-12 in-frame, single-gene knockout mutants: The Keio collection. _Mol. Syst. Biol.__**2**_, 2006.0008 (2006).

12

Papp B., Pál C., Hurst L. D., Metabolic network analysis of the causes and evolution of enzyme dispensability in yeast. _Nature__**429**_, 661 (2004).

13

Deutscher D., Meilijson I., Kupiec M., Ruppin E., Multiple knockout analysis of genetic robustness in the yeast metabolic network. _Nat. Genet.__**38**_, 993 (2006). !

14

Bordel S., Agren R., Nielsen J., Sampling the solution space in genome-scale metabolic networks reveals transcriptional regulation in key enzymes. _PLOS Comput. Biol.__**6**_, e1000859 (2010).

15

Schuetz R., Kuepfer L., Sauer U., Systematic evaluation of objective functions for predicting intracellular fluxes in _Escherichia coli_. _Mol. Syst. Biol.__**3**_, 119 (2007).

16

Gur E., Biran D., Ron E. Z.,Regulated proteolysis in Gram-negative bacteria—how and when? _Nat. Rev. Microbiol.__**9**_, 839 (2011).

17

Lewis N. E., Cho B. K., Knight E. M., Palsson B. O., Gene expression profiling and the use of genome-scale in silico models of _Escherichia coli_ for analysis: Providing context for content. _J. Bacteriol.__**191**_, 3437 (2009).

18

Zhang Z., et al., Identification of lysine succinylation as a new post-translational modification. _Nat. Chem. Biol.__**7**_, 58 (2011).

19

Gerosa L., Sauer U., Regulation and control of metabolic fluxes in microbes. _Curr. Opin. Biotechnol.__**22**_, 566 (2011).

20

Feist A. M., Scholten J. C., Palsson B. O., Brockman F. J., Ideker T., Modeling methanogenesis with a genome-scale metabolic reconstruction of _Methanosarcina barkeri_. _Mol. Syst. Biol.__**2**_, 2006.0004 (2006).

21

Mo M. L., Palsson B. O., Herrgård M. J., Connecting extracellular metabolomic measurements to intracellular flux states in yeast. _BMC Syst. Biol.__**3**_, 37 (2009).

22

Chang R. L., et al., Metabolic network reconstruction of _Chlamydomonas_ offers insight into light-driven algal metabolism. _Mol. Syst. Biol.__**7**_, 518 (2011).

23

Bar-Even A., et al., The moderately efficient enzyme: Evolutionary and physicochemical trends shaping enzyme parameters. _Biochemistry__**50**_, 4402 (2011).

24

Morar M., Wright G. D., The genomic enzymology of antibiotic resistance. _Annu. Rev. Genet.__**44**_, 25 (2010).

25

Almaas E., Oltvai Z. N., Barabási A. L., The activity reaction core and plasticity of metabolic networks. _PLOS Comput. Biol.__**1**_, e68 (2005).

26

Copley S. D., Toward a systems biology perspective on enzyme evolution. _J. Biol. Chem.__**287**_, 3 (2012).

27

Papp B., Notebaart R. A., Pál C., Systems-biology approaches for predicting genomic evolution. _Nat. Rev. Genet.__**12**_, 591 (2011).

28

Nam H., Conrad T. M., Lewis N. E., The role of cellular objectives and selective pressures in metabolic pathway evolution. _Curr. Opin. Biotechnol.__**22**_, 595 (2011).

29

Carbonell P., Lecointre G., Faulon J. L., Origins of specificity and promiscuity in metabolic networks. _J. Biol. Chem.__**286**_, 43994 (2011).

30

Lee D. H., Palsson B. O., Adaptive evolution of _Escherichia coli_ K-12 MG1655 during growth on a nonnative carbon source, L-1,2-propanediol. _Appl. Environ. Microbiol.__**76**_, 4158 (2010).

31

Covert M. W., Knight E. M., Reed J. L., Herrgard M. J., Palsson B. O., Integrating high-throughput and computational data elucidates bacterial networks. _Nature__**429**_, 92 (2004).

32

Fong S. S., Joyce A. R., Palsson B. O., Parallel adaptive evolution cultures of _Escherichia coli_ lead to convergent growth phenotypes with different gene expression states. _Genome Res.__**15**_, 1365 (2005).

33

Orth J. D., Thiele I., Palsson B. O., What is flux balance analysis? _Nat. Biotechnol.__**28**_, 245 (2010).

34

Conrad T. M., Lewis N. E., Palsson B. O., Microbial laboratory evolution in the era of genome-scale science. _Mol. Syst. Biol.__**7**_, 509 (2011).

35

Keseler I. M., et al., EcoCyc: A comprehensive database of _Escherichia coli_ biology. _Nucleic Acids Res.__**39**_ (Database issue), D583 (2011).

36

Schellenberger J., Palsson B. O., Use of randomized sampling for analysis of metabolic networks. _J. Biol. Chem.__**284**_, 5457 (2009).

37

Bordbar A., Lewis N. E., Schellenberger J., Palsson B. O., Jamshidi N., Insight into human alveolar macrophage and M. tuberculosis interactions via metabolic reconstructions. _Mol. Syst. Biol.__**6**_, 422 (2010).

38

Lewis N. E., et al., Large-scale in silico modeling of metabolic interactions between cell types in the human brain. _Nat. Biotechnol.__**28**_, 1279 (2010).

39

Schellenberger J., et al., Quantitative prediction of cellular metabolism with constraint-based models: The COBRA Toolbox v2.0. _Nature Protocols__**6**_, 1290 (2011).

40

Schuster S., Pfeiffer T., Fell D. A., Is maximization of molar yield in metabolic networks favoured by evolution? _J. Theor. Biol.__**252**_, 497 (2008).

41

Feist A. M., Palsson B. O., The biomass objective function. _Curr. Opin. Microbiol.__**13**_, 344 (2010).

42

Schellenberger J., Lewis N. E., Palsson B. O., Elimination of thermodynamically infeasible loops in steady-state metabolic models. _Biophys. J.__**100**_, 544 (2011).

43

Beard D. A., Liang S. D., Qian H., Energy balance for analysis of complex metabolic networks. _Biophys. J.__**83**_, 79 (2002).

44

Daran-Lapujade P., et al., Role of transcriptional regulation in controlling fluxes in central carbon metabolism of Saccharomyces cerevisiae. A chemostat culture study. _J. Biol. Chem.__**279**_, 9125 (2004).

45

Bar-Even A., Noor E., Lewis N. E., Milo R., Design and analysis of synthetic carbon fixation pathways. _Proc. Natl. Acad. Sci. U.S.A.__**107**_, 8889 (2010).

46

Yu B. J., Kim J. A., Moon J. H., Ryu S. E., Pan J. G., The diversity of lysine-acetylated proteins in _Escherichia coli_. _J. Microbiol. Biotechnol.__**18**_, 1529 (2008).

47

Zhang J., et al., Lysine acetylation is a highly abundant and evolutionarily conserved modification in _Escherichia coli_. _Mol. Cell. Proteomics__**8**_, 215 (2009).

48

Macek B., et al., Phosphoproteome analysis of _E. coli_ reveals evolutionary conservation of bacterial Ser/Thr/Tyr phosphorylation. _Mol. Cell. Proteomics__**7**_, 299 (2008).

49

Khersonsky O., Tawfik D. S., Enzyme promiscuity: A Mechanistic and evolutionary perspective. _Annu. Rev. Biochem.__**79**_, 471 (2010).

50

Kanehisa M., Goto S., Furumichi M., Tanabe M., Hirakawa M., KEGG for representation and analysis of molecular networks involving diseases and drugs. _Nucleic Acids Res.__**38**_ (Database issue), D355 (2010).

51

Orth J. D., et al., A comprehensive genome-scale reconstruction of _Escherichia coli_ metabolism—2011. _Mol. Syst. Biol.__**7**_, 535 (2011).

52

Majewski R. A., Domach M. M., Simple constrained-optimization view of acetate overflow in _E. coli_. _Biotechnol. Bioeng.__**35**_, 732 (1990).

53

Varma A., Palsson B. O., Metabolic capabilities of _Escherichia coli_: I. synthesis of biosynthetic precursors and cofactors. _J. Theor. Biol.__**165**_, 477 (1993).

54

Pramanik J., Keasling J. D., Stoichiometric model of _Escherichia coli_ metabolism: Incorporation of growth-rate dependent biomass composition and mechanistic energy requirements. _Biotechnol. Bioeng.__**56**_, 398 (1997).

55

Edwards J. S., Palsson B. O., The _Escherichia coli_ MG1655 in silico metabolic genotype: Its definition, characteristics, and capabilities. _Proc. Natl. Acad. Sci. U.S.A.__**97**_, 5528 (2000).

56

Reed J. L., Palsson B. O., Thirteen years of building constraint-based in silico models of _Escherichia coli_. _J. Bacteriol.__**185**_, 2692 (2003).

57

Feist A. M., Palsson B. O., The growing scope of applications of genome-scale metabolic reconstructions using _Escherichia coli_. _Nat. Biotechnol.__**26**_, 659 (2008).

58

Lewis N. E., et al., Omic data from evolved _E. coli_ are consistent with computed optimal growth from genome-scale models. _Mol. Syst. Biol.__**6**_, 390 (2010).

59

Shou C., et al., Measuring the evolutionary rewiring of biological networks. _PLOS Comput. Biol.__**7**_, e1001050 (2011).

60

Ibarra R. U., Edwards J. S., Palsson B. O., _Escherichia coli_ K-12 undergoes adaptive evolution to achieve in silico predicted optimal growth. _Nature__**420**_, 186 (2002).

61

Cocks G. T., Aguilar T., Lin E. C., Evolution of L-1, 2-propanediol catabolism in _Escherichia coli_ by recruitment of enzymes for L-fucose and L-lactate metabolism. _J. Bacteriol.__**118**_, 83 (1974).

62

Thiele I., Jamshidi N., Fleming R. M., Palsson B. O., Genome-scale reconstruction of _Escherichia coli_’s transcriptional and translational machinery: A knowledge base, its mathematical formulation, and its functional characterization. _PLOS Comput. Biol.__**5**_, e1000312 (2009).

63

Zhang Y., et al., Three-dimensional structural view of the central metabolic network of Thermotoga maritima. _Science__**325**_, 1544 (2009).

64

Chang R. L., Xie L., Xie L., Bourne P. E., Palsson B. Ø., Drug off-target effects predicted using structural analysis in the context of a metabolic network model. _PLOS Comput. Biol.__**6**_, e1000938 (2010).

65

Bennett B. D., et al., Absolute metabolite concentrations and implied enzyme active site occupancy in _Escherichia coli_. _Nat. Chem. Biol.__**5**_, 593 (2009).

66

Mitchell A., et al., Adaptive prediction of environmental changes by microorganisms. _Nature__**460**_, 220 (2009).

67

Stover P., Schirch V., Serine hydroxymethyltransferase catalyzes the hydrolysis of 5,10-methenyltetrahydrofolate to 5-formyltetrahydrofolate. _J. Biol. Chem.__**265**_, 14227 (1990).

68

Schirch V., Hopkins S., Villar E., Angelaccio S., Serine hydroxymethyltransferase from _Escherichia coli_: Purification and properties. _J. Bacteriol.__**163**_, 1 (1985).

69

Hopkins S., Schirch V., Properties of a serine hydroxymethyltransferase in which an active site histidine has been changed to an asparagine by site-directed mutagenesis. _J. Biol. Chem.__**261**_, 3363 (1986).

70

Contestabile R., et al., l-Threonine aldolase, serine hydroxymethyltransferase and fungal alanine racemase. A subgroup of strictly related enzymes specialized for different functions. _Eur. J. Biochem.__**268**_, 6508 (2001).

71

Taniguchi Y., et al., Quantifying _E. coli_ proteome and transcriptome with single-molecule sensitivity in single cells. _Science__**329**_, 533 (2010).

72

Heath R. J., Rock C. O., Roles of the FabA and FabZ beta-hydroxyacyl-acyl carrier protein dehydratases in _Escherichia coli_ fatty acid biosynthesis. _J. Biol. Chem.__**271**_, 27795 (1996).

73

Sawers G., Böck A., Anaerobic regulation of pyruvate formate-lyase from _Escherichia coli_ K-12. _J. Bacteriol.__**170**_, 5330 (1988).

74

Knappe J., Sawers G., A radical-chemical route to acetyl-CoA: The anaerobically induced pyruvate formate-lyase system of _Escherichia coli_. _FEMS Microbiol. Rev.__**6**_, 383 (1990).

75

Hesslinger C., Fairhurst S. A., Sawers G., Novel keto acid formate-lyase and propionate kinase enzymes are components of an anaerobic pathway in _Escherichia coli_ that degrades L-threonine to propionate. _Mol. Microbiol.__**27**_, 477 (1998).

76

Mahadevan R., Schilling C. H., The effects of alternate optimal solutions in constraint-based genome-scale metabolic models. _Metab. Eng.__**5**_, 264 (2003).

77

S. Ohno, _Evolution by gene duplication_. (Springer-Verlag, Berlin, New York, 1970), pp. xv, 160 p.

78

Soskine M., Tawfik D. S., Mutational effects and the evolution of new protein functions. _Nat. Rev. Genet.__**11**_, 572 (2010).

## Information & Authors
### Information
#### Published In
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073531322-d44021f6-bbe2-4620-8317-ef1c728502cc.jpeg)

Science

Volume 337 | Issue 6098  
31 August 2012

#### Copyright
Copyright © 2012, American Association for the Advancement of Science.

#### Submission history
**Received**: 21 November 2011

**Accepted**: 29 June 2012

**Published in print**: 31 August 2012

#### Permissions
Request permissions for this article.

[Request permissions](https://s100.copyright.com/AppDispatchServlet?publisherName=AAAS&publication=sci&title=Network+Context+and+Selection+in+the+Evolution+to+Enzyme+Specificity&publicationDate=2012-08-31&author=Hojung+Nam%2C+Nathan+E.+Lewis%2C+Joshua+A.+Lerman%2C+Dae-Hee+Lee%2C+et+al.&contentID=10.1126%2Fscience.1216861&volumeNum=337&issueNum=6098&startPage=1101&endPage=1104&orderBeanReset=true)

#### Acknowledgments
We thank D. Zielinski for insightful discussion on this work. This work was supported by NIH, NSF, and U.S. Department of Energy grants 2R01GM057089-13, NSF GK-12 742551, DE-SC0004917, and DE-FG02-09ER25917. Data are available at the NCBI Gene Expression Omnibus (GEO) database (GSE34631).

### Authors
#### Affiliations
##### HojungNam[*](https://www.science.org/doi/full/10.1126/science.1216861#afn1)
##### Joshua A.Lerman
##### Dae-HeeLee
##### Roger L.Chang
##### DonghyukKim
#### Notes
*

These authors contributed equally to this work.

## Metrics & Citations
### Metrics
#### Article Usage 
#### Altmetrics 
**495** readers on Mendeley 

**17** readers on CiteULike 

### Citations
#### Cite as 
Network Context and Selection in the Evolution to Enzyme Specificity._Science_**337**,1101-1104(2012).DOI:[10.1126/science.1216861](https://doi.org/10.1126/science.1216861)

#### Export citation
Select the format you want to export the citation of this publication.

 	 

#### Cited by 
    - Tianhao Yu, 
    - Haiyang Cui, 
    - Jianan Canal Li, 
    - Yunan Luo, 
    - Guangde Jiang, 
    - Huimin Zhao, 
1. Enzyme function prediction using contrastive learning, Science, **379**, 6639, (1358-1363), (2023).[/doi/10.1126/science.adf2465](https://www.science.org/doi/10.1126/science.adf2465)

## View Options
### View options
#### PDF format
Download this article as a PDF file

[Download PDF](https://www.science.org/doi/pdf/10.1126/science.1216861?download=true)

## Tables
## References
### References
1

Jensen R. A., Enzyme recruitment in evolution of new function. _Annu. Rev. Microbiol.__**30**_, 409 (1976).

2

Khersonsky O., Tawfik D. S., Enzyme promiscuity: A mechanistic and evolutionary perspective. _Annu. Rev. Biochem.__**79**_, 471 (2010).

3

Innan H., Kondrashov F., The evolution of gene duplications: Classifying and distinguishing between models. _Nat. Rev. Genet.__**11**_, 97 (2010).

4

Khersonsky O., Malitsky S., Rogachev I., Tawfik D. S., Role of chemistry versus substrate binding in recruiting promiscuous enzyme functions. _Biochemistry__**50**_, 2683 (2011).

5

Feist A. M., et al., A genome-scale metabolic reconstruction for _Escherichia coli_ K-12 MG1655 that accounts for 1260 ORFs and thermodynamic information. _Mol. Syst. Biol.__**3**_, 121 (2007).

6

Aharoni A., et al., The ‘evolvability’ of promiscuous protein functions. _Nat. Genet.__**37**_, 73 (2005).

7

Lewis N. E., Nagarajan H., Palsson B. O., Constraining the metabolic genotype-phenotype relationship using a phylogeny of in silico methods. _Nat. Rev. Microbiol.__**10**_, 291 (2012).

8

Almaas E., Kovács B., Vicsek T., Oltvai Z. N., Barabási A. L., Global organization of metabolic fluxes in the bacterium _Escherichia coli_. _Nature__**427**_, 839 (2004).

9

Materials and methods are available as supplementary materials on _Science_ Online.

10

Wagner A., Energy costs constrain the evolution of gene expression. _J. Exp. Zool. B Mol. Dev. Evol.__**308B**_, 322 (2007).

11

Baba T., et al., Construction of _Escherichia coli_ K-12 in-frame, single-gene knockout mutants: The Keio collection. _Mol. Syst. Biol.__**2**_, 2006.0008 (2006).

12

Papp B., Pál C., Hurst L. D., Metabolic network analysis of the causes and evolution of enzyme dispensability in yeast. _Nature__**429**_, 661 (2004).

13

Deutscher D., Meilijson I., Kupiec M., Ruppin E., Multiple knockout analysis of genetic robustness in the yeast metabolic network. _Nat. Genet.__**38**_, 993 (2006). !

14

Bordel S., Agren R., Nielsen J., Sampling the solution space in genome-scale metabolic networks reveals transcriptional regulation in key enzymes. _PLOS Comput. Biol.__**6**_, e1000859 (2010).

15

Schuetz R., Kuepfer L., Sauer U., Systematic evaluation of objective functions for predicting intracellular fluxes in _Escherichia coli_. _Mol. Syst. Biol.__**3**_, 119 (2007).

16

Gur E., Biran D., Ron E. Z.,Regulated proteolysis in Gram-negative bacteria—how and when? _Nat. Rev. Microbiol.__**9**_, 839 (2011).

17

Lewis N. E., Cho B. K., Knight E. M., Palsson B. O., Gene expression profiling and the use of genome-scale in silico models of _Escherichia coli_ for analysis: Providing context for content. _J. Bacteriol.__**191**_, 3437 (2009).

18

Zhang Z., et al., Identification of lysine succinylation as a new post-translational modification. _Nat. Chem. Biol.__**7**_, 58 (2011).

19

Gerosa L., Sauer U., Regulation and control of metabolic fluxes in microbes. _Curr. Opin. Biotechnol.__**22**_, 566 (2011).

20

Feist A. M., Scholten J. C., Palsson B. O., Brockman F. J., Ideker T., Modeling methanogenesis with a genome-scale metabolic reconstruction of _Methanosarcina barkeri_. _Mol. Syst. Biol.__**2**_, 2006.0004 (2006).

21

Mo M. L., Palsson B. O., Herrgård M. J., Connecting extracellular metabolomic measurements to intracellular flux states in yeast. _BMC Syst. Biol.__**3**_, 37 (2009).

22

Chang R. L., et al., Metabolic network reconstruction of _Chlamydomonas_ offers insight into light-driven algal metabolism. _Mol. Syst. Biol.__**7**_, 518 (2011).

23

Bar-Even A., et al., The moderately efficient enzyme: Evolutionary and physicochemical trends shaping enzyme parameters. _Biochemistry__**50**_, 4402 (2011).

24

Morar M., Wright G. D., The genomic enzymology of antibiotic resistance. _Annu. Rev. Genet.__**44**_, 25 (2010).

25

Almaas E., Oltvai Z. N., Barabási A. L., The activity reaction core and plasticity of metabolic networks. _PLOS Comput. Biol.__**1**_, e68 (2005).

26

Copley S. D., Toward a systems biology perspective on enzyme evolution. _J. Biol. Chem.__**287**_, 3 (2012).

27

Papp B., Notebaart R. A., Pál C., Systems-biology approaches for predicting genomic evolution. _Nat. Rev. Genet.__**12**_, 591 (2011).

28

Nam H., Conrad T. M., Lewis N. E., The role of cellular objectives and selective pressures in metabolic pathway evolution. _Curr. Opin. Biotechnol.__**22**_, 595 (2011).

29

Carbonell P., Lecointre G., Faulon J. L., Origins of specificity and promiscuity in metabolic networks. _J. Biol. Chem.__**286**_, 43994 (2011).

30

Lee D. H., Palsson B. O., Adaptive evolution of _Escherichia coli_ K-12 MG1655 during growth on a nonnative carbon source, L-1,2-propanediol. _Appl. Environ. Microbiol.__**76**_, 4158 (2010).

31

Covert M. W., Knight E. M., Reed J. L., Herrgard M. J., Palsson B. O., Integrating high-throughput and computational data elucidates bacterial networks. _Nature__**429**_, 92 (2004).

32

Fong S. S., Joyce A. R., Palsson B. O., Parallel adaptive evolution cultures of _Escherichia coli_ lead to convergent growth phenotypes with different gene expression states. _Genome Res.__**15**_, 1365 (2005).

33

Orth J. D., Thiele I., Palsson B. O., What is flux balance analysis? _Nat. Biotechnol.__**28**_, 245 (2010).

34

Conrad T. M., Lewis N. E., Palsson B. O., Microbial laboratory evolution in the era of genome-scale science. _Mol. Syst. Biol.__**7**_, 509 (2011).

35

Keseler I. M., et al., EcoCyc: A comprehensive database of _Escherichia coli_ biology. _Nucleic Acids Res.__**39**_ (Database issue), D583 (2011).

36

Schellenberger J., Palsson B. O., Use of randomized sampling for analysis of metabolic networks. _J. Biol. Chem.__**284**_, 5457 (2009).

37

Bordbar A., Lewis N. E., Schellenberger J., Palsson B. O., Jamshidi N., Insight into human alveolar macrophage and M. tuberculosis interactions via metabolic reconstructions. _Mol. Syst. Biol.__**6**_, 422 (2010).

38

Lewis N. E., et al., Large-scale in silico modeling of metabolic interactions between cell types in the human brain. _Nat. Biotechnol.__**28**_, 1279 (2010).

39

Schellenberger J., et al., Quantitative prediction of cellular metabolism with constraint-based models: The COBRA Toolbox v2.0. _Nature Protocols__**6**_, 1290 (2011).

40

Schuster S., Pfeiffer T., Fell D. A., Is maximization of molar yield in metabolic networks favoured by evolution? _J. Theor. Biol.__**252**_, 497 (2008).

41

Feist A. M., Palsson B. O., The biomass objective function. _Curr. Opin. Microbiol.__**13**_, 344 (2010).

42

Schellenberger J., Lewis N. E., Palsson B. O., Elimination of thermodynamically infeasible loops in steady-state metabolic models. _Biophys. J.__**100**_, 544 (2011).

43

Beard D. A., Liang S. D., Qian H., Energy balance for analysis of complex metabolic networks. _Biophys. J.__**83**_, 79 (2002).

44

Daran-Lapujade P., et al., Role of transcriptional regulation in controlling fluxes in central carbon metabolism of Saccharomyces cerevisiae. A chemostat culture study. _J. Biol. Chem.__**279**_, 9125 (2004).

45

Bar-Even A., Noor E., Lewis N. E., Milo R., Design and analysis of synthetic carbon fixation pathways. _Proc. Natl. Acad. Sci. U.S.A.__**107**_, 8889 (2010).

46

Yu B. J., Kim J. A., Moon J. H., Ryu S. E., Pan J. G., The diversity of lysine-acetylated proteins in _Escherichia coli_. _J. Microbiol. Biotechnol.__**18**_, 1529 (2008).

47

Zhang J., et al., Lysine acetylation is a highly abundant and evolutionarily conserved modification in _Escherichia coli_. _Mol. Cell. Proteomics__**8**_, 215 (2009).

48

Macek B., et al., Phosphoproteome analysis of _E. coli_ reveals evolutionary conservation of bacterial Ser/Thr/Tyr phosphorylation. _Mol. Cell. Proteomics__**7**_, 299 (2008).

49

Khersonsky O., Tawfik D. S., Enzyme promiscuity: A Mechanistic and evolutionary perspective. _Annu. Rev. Biochem.__**79**_, 471 (2010).

50

Kanehisa M., Goto S., Furumichi M., Tanabe M., Hirakawa M., KEGG for representation and analysis of molecular networks involving diseases and drugs. _Nucleic Acids Res.__**38**_ (Database issue), D355 (2010).

51

Orth J. D., et al., A comprehensive genome-scale reconstruction of _Escherichia coli_ metabolism—2011. _Mol. Syst. Biol.__**7**_, 535 (2011).

52

Majewski R. A., Domach M. M., Simple constrained-optimization view of acetate overflow in _E. coli_. _Biotechnol. Bioeng.__**35**_, 732 (1990).

53

Varma A., Palsson B. O., Metabolic capabilities of _Escherichia coli_: I. synthesis of biosynthetic precursors and cofactors. _J. Theor. Biol.__**165**_, 477 (1993).

54

Pramanik J., Keasling J. D., Stoichiometric model of _Escherichia coli_ metabolism: Incorporation of growth-rate dependent biomass composition and mechanistic energy requirements. _Biotechnol. Bioeng.__**56**_, 398 (1997).

55

Edwards J. S., Palsson B. O., The _Escherichia coli_ MG1655 in silico metabolic genotype: Its definition, characteristics, and capabilities. _Proc. Natl. Acad. Sci. U.S.A.__**97**_, 5528 (2000).

56

Reed J. L., Palsson B. O., Thirteen years of building constraint-based in silico models of _Escherichia coli_. _J. Bacteriol.__**185**_, 2692 (2003).

57

Feist A. M., Palsson B. O., The growing scope of applications of genome-scale metabolic reconstructions using _Escherichia coli_. _Nat. Biotechnol.__**26**_, 659 (2008).

58

Lewis N. E., et al., Omic data from evolved _E. coli_ are consistent with computed optimal growth from genome-scale models. _Mol. Syst. Biol.__**6**_, 390 (2010).

59

Shou C., et al., Measuring the evolutionary rewiring of biological networks. _PLOS Comput. Biol.__**7**_, e1001050 (2011).

60

Ibarra R. U., Edwards J. S., Palsson B. O., _Escherichia coli_ K-12 undergoes adaptive evolution to achieve in silico predicted optimal growth. _Nature__**420**_, 186 (2002).

61

Cocks G. T., Aguilar T., Lin E. C., Evolution of L-1, 2-propanediol catabolism in _Escherichia coli_ by recruitment of enzymes for L-fucose and L-lactate metabolism. _J. Bacteriol.__**118**_, 83 (1974).

62

Thiele I., Jamshidi N., Fleming R. M., Palsson B. O., Genome-scale reconstruction of _Escherichia coli_’s transcriptional and translational machinery: A knowledge base, its mathematical formulation, and its functional characterization. _PLOS Comput. Biol.__**5**_, e1000312 (2009).

63

Zhang Y., et al., Three-dimensional structural view of the central metabolic network of Thermotoga maritima. _Science__**325**_, 1544 (2009).

64

Chang R. L., Xie L., Xie L., Bourne P. E., Palsson B. Ø., Drug off-target effects predicted using structural analysis in the context of a metabolic network model. _PLOS Comput. Biol.__**6**_, e1000938 (2010).

65

Bennett B. D., et al., Absolute metabolite concentrations and implied enzyme active site occupancy in _Escherichia coli_. _Nat. Chem. Biol.__**5**_, 593 (2009).

66

Mitchell A., et al., Adaptive prediction of environmental changes by microorganisms. _Nature__**460**_, 220 (2009).

67

Stover P., Schirch V., Serine hydroxymethyltransferase catalyzes the hydrolysis of 5,10-methenyltetrahydrofolate to 5-formyltetrahydrofolate. _J. Biol. Chem.__**265**_, 14227 (1990).

68

Schirch V., Hopkins S., Villar E., Angelaccio S., Serine hydroxymethyltransferase from _Escherichia coli_: Purification and properties. _J. Bacteriol.__**163**_, 1 (1985).

69

Hopkins S., Schirch V., Properties of a serine hydroxymethyltransferase in which an active site histidine has been changed to an asparagine by site-directed mutagenesis. _J. Biol. Chem.__**261**_, 3363 (1986).

70

Contestabile R., et al., l-Threonine aldolase, serine hydroxymethyltransferase and fungal alanine racemase. A subgroup of strictly related enzymes specialized for different functions. _Eur. J. Biochem.__**268**_, 6508 (2001).

71

Taniguchi Y., et al., Quantifying _E. coli_ proteome and transcriptome with single-molecule sensitivity in single cells. _Science__**329**_, 533 (2010).

72

Heath R. J., Rock C. O., Roles of the FabA and FabZ beta-hydroxyacyl-acyl carrier protein dehydratases in _Escherichia coli_ fatty acid biosynthesis. _J. Biol. Chem.__**271**_, 27795 (1996).

73

Sawers G., Böck A., Anaerobic regulation of pyruvate formate-lyase from _Escherichia coli_ K-12. _J. Bacteriol.__**170**_, 5330 (1988).

74

Knappe J., Sawers G., A radical-chemical route to acetyl-CoA: The anaerobically induced pyruvate formate-lyase system of _Escherichia coli_. _FEMS Microbiol. Rev.__**6**_, 383 (1990).

75

Hesslinger C., Fairhurst S. A., Sawers G., Novel keto acid formate-lyase and propionate kinase enzymes are components of an anaerobic pathway in _Escherichia coli_ that degrades L-threonine to propionate. _Mol. Microbiol.__**27**_, 477 (1998).

76

Mahadevan R., Schilling C. H., The effects of alternate optimal solutions in constraint-based genome-scale metabolic models. _Metab. Eng.__**5**_, 264 (2003).

77

S. Ohno, _Evolution by gene duplication_. (Springer-Verlag, Berlin, New York, 1970), pp. xv, 160 p.

78

Soskine M., Tawfik D. S., Mutational effects and the evolution of new protein functions. _Nat. Rev. Genet.__**11**_, 572 (2010).  


> 来自: [Network Context and Selection in the Evolution to Enzyme Specificity | Science](https://www.science.org/doi/full/10.1126/science.1216861)
>

