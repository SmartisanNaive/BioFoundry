Science Advances

3 Jun 2020

Vol 6, Issue 23

## Abstract
Our ability to predict the impact of mutations on traits relevant for disease and evolution remains severely limited by the dependence of their effects on the genetic background and environment. Even when molecular interactions between genes are known, it is unclear how these translate to organism-level interactions between alleles. We therefore characterized the interplay of genetic and environmental dependencies in determining fitness by quantifying ~4000 fitness interactions between expression variants of two metabolic genes, starting from various environmentally modulated expression levels. We detect a remarkable variety of interactions dependent on initial expression levels and demonstrate that they can be quantitatively explained by a mechanistic model accounting for catabolic flux, metabolite toxicity, and expression costs. Complex fitness interactions between mutations can therefore be predicted simply from their simultaneous impact on a few connected molecular phenotypes.

#### SIGN UP FOR THE _SCIENCE_ADVISER NEWSLETTER
The latest news, commentary, and research, free to your inbox daily

## INTRODUCTION
Despite its centrality to medical and evolutionary genetics, our ability to predict the impact of mutations on even the apparently simplest of organismal traits ([1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R1)–[4](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R4)), let alone complex ones ([5](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R5)), remains minimal. 

Three of the main factors proposed to account for this “missing heritability” ([5](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R5)) are 

+ the large number of possible alleles at any locus, each having a potentially different impact on a gene’s function; 
+ interaction between alleles at different loci (intergenic epistasis), such that their combined effect is not simply the sum of their individual effects; 
+ interaction between genotype and environment, such that different genotypes respond to the environment in different ways ([1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R1)–[5](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R5)). 

A promise of recent –omics approaches is the ability to predict the influence of these factors on phenotypes from an increasing characterization of <font style="color:#DF2A3F;">molecular interaction networks</font> ([4](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R4), [6](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R6)). 

<font style="color:#DF2A3F;">Metabolic networks are the best characterized of these and are of great practical interest for medicine and engineering, but even for metabolic genes, it remains unclear how functional interactions at the molecular level translate to allelic interactions at the level of integrated traits relevant for disease, industry, and adaptation</font> ([7](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R7)).

## RESULTS
### Experimental system
We therefore developed an experimental system with which to systematically quantify the fitness interactions occurring between many alleles of two metabolic genes from the same pathway ([8](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R8)). Furthermore, the design enabled us to probe the dependence of these interactions on environmentally modulated gene expression (hereafter referred to simply as environment), a common nongenetic mechanism for the modification of physiological traits ([3](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R3), [9](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R9)).

For genetic tractability, our system was composed of the adjacent genes (_araA_ and _araB_) encoding the enzymes responsible for the first two steps of the well-characterized, linear _Escherichia coli_l-arabinose utilization pathway ([10](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R10)): l-arabinose isomerase (AraA) and l-ribulokinase (AraB), which together transform the sugar, l-arabinose, into the intermediate, l-ribulose-5-phosphate ([Fig. 1A](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1)). l-Ribulose-5-phosphate enters the pentose phosphate pathway (PPP) of central metabolism via further enzymatic reactions, ultimately supporting cell growth, but like many intermediates ([11](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R11)), its accumulation is toxic, retarding growth ([12](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R12)). Environmental modulation of gene expression was achieved by placing each of the two genes under an independent, trans-regulated chemically inducible promoter.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710074316520-51649edb-4271-4b3d-a76a-24cdc3b0820a.jpeg)

Fig. 1 Quantitative mapping of fitness interactions between expression variants of two metabolic genes in expression-modifying environments.

(**A**) l-Arabinose pathway of _E. coli_. (**B**) _araA_ and _araB_ were placed under the control of inducible promoters, making their expression sensitive to the concentration of their respective inducers, anhydrotetracycline (aTc) and isopropyl β-d-1-thiogalactopyranoside (IPTG). A barcoded library of mutant promoter combinations was constructed, with mutations targeting the −35 and −10 RNA polymerase-binding hexamers (black letters). Underlined bases are annotated repressor binding sites. (**C**) Competitive fitness was measured under different inducer concentrations defining three environments. PLtetO-1 single mutants, green; PLlacO-1 single mutants, purple; double mutants, orange. Contours are hypothetical fitness isoclines. (**D**) Epistasis was quantified for all mutant promoter pairs across environments. Epistasis can be categorized as either magnitude or sign type. Sign epistasis is further categorized as simple (effect of one mutation changes sign in presence of the other) or reciprocal (effects of both mutations change sign in the presence of the other). Capitalized letters represent mutant alleles of PLtetO-1-_araA_ and PLlacO-1-_araB_. Superscript plus and minus denote that individual alleles are beneficial or deleterious, respectively.

[Open in viewer](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1)

For each promoter, 36 single-base variants were constructed, along with the initial “wild-type” (WT) sequence, and combined with all variants of the other promoter ([Fig. 1B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1)). The organismal phenotype, competitive fitness, was then measured for the entire set of 1369 genotypes under three different inducer concentration combinations ([Fig. 1, C and D](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1)). Fitness was measured by tagging the mutant library with unique DNA barcodes (tens to thousands per genotype) (figs. S1 and S2), culturing the pooled library for ~30 population generations, and tracking barcode frequencies over time with next-generation sequencing (figs. S3 and S4). The barcodes act as internal replicates for every genotype, enabling precise fitness estimates at high throughput (log relative fitness, _F_rel, median SD of 0.0011 for single mutants and 0.0047 for double mutants; fig. S5).

### Fitness effects across inducer environments
The overall distribution of fitness effects depended critically on the inducer environment, i.e., the trans-regulatory input ([Fig. 2A](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F2), fig. S6A, and data S1). The proportion of beneficial effects varied from 88% in Env1 (median _F_rel = 0.12) to 51% in Env3 (median _F_rel = −0.03) and 12% in Env2 (median _F_rel = −0.12). Furthermore, the correlation of fitness effects between environments ranged from strongly positive (Env1–Env3, Pearson’s _r_ = 0.74, _P_ < 2.2 × 10−16) to weakly negative (Env1–Env2, Pearson’s _r_ = −0.11, _P_ = 1 × 10−4) (fig. S6B), demonstrating that fitness in one environment can be an extremely poor predictor of fitness in other environments due simply to expression differences. At the level of individual alleles, all but one had changing patterns of effects across environments ([Fig. 2B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F2)). In some environments, they were universally beneficial or deleterious across genetic backgrounds, and in others, they switched between being beneficial and deleterious depending on the allele at the second promoter. This pervasive and inconsistent variability poses a clear challenge for the prediction of mutation effects.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710074316729-25dfcbfc-4353-44b6-8975-6f1da8d305d8.jpeg)

Fig. 2 Fitness effects of promoter mutations across backgrounds and environments.

(**A**) Genotypes are colored according to the natural logarithm of their fitness relative to the WT (_F_rel). Gray denotes unquantifiable fitness effects. Letters show WT bases, and the three mutations at each position are ordered alphabetically as in (B). Single promoter mutants make up the right-most column (_araA_) and top row (_araB_). Inducer concentrations were aTc (20 ng/ml) and 30 μM IPTG (Env1), aTc (5 ng/ml) and no IPTG (Env2), and aTc (200 ng/ml) and no IPTG (Env3). (**B**) Fitness changes when an allele of one promoter is added to alleles of the second promoter. Large points indicate the “background” promoter is WT. Red, blue, and gray points indicate positive, negative, and nonsignificant fitness changes, respectively. Red, blue, and gray rectangles indicate that, in that environment, an allele can be beneficial but never deleterious, deleterious but never beneficial, or both beneficial and deleterious. G7A of PLtetO-1-_araA_ (*) is the only allele conferring a qualitatively consistent fitness effect (beneficial) across all backgrounds and environments.

[Open in viewer](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F2)

### Epistasis across inducer environments
To further characterize how the effects of mutations in one gene depended on the allele present at the other gene, we computed epistasis ([13](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R13)) for all mutation pairs in each environment. Epistasis evaluates quantitatively and qualitatively how the log fitness of a double mutant deviates from the sum of that of the constituent single mutants ([Fig. 3A](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F3) and fig. S7A). Epistasis was found to be pervasive (89, 39, and 81% of pairs in Env1–3, respectively), heterogeneous, and environment dependent. A trend of antagonism reported for several other systems ([14](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R14)) was recovered between pairs of individually beneficial (negative epistasis in 89, 72, and 100% in Env1–3, respectively) and individually deleterious [positive epistasis in 100 (1/1), 97, and 98%, respectively] mutations, while interactions between a beneficial and a deleterious mutation could be mostly positive or mostly negative, depending on the environment and on which gene carried the beneficial/deleterious mutation. This epistatic diversity extended to individual mutation pairs, with more than 20% interacting both positively and negatively across environments (fig. S7, B and C). Notably, sign epistasis, an extreme interaction that occurs when the sign of a mutation effect changes in the presence of a second mutation ([Fig. 1D](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1)), represented 31% of significant interactions in Env1, 17% in Env2, and 34% in Env3.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710074316495-0c10dca3-8748-4f6a-a5d9-c61cf5f82c15.jpeg)

Fig. 3 Strength, types, and trends of epistasis across environments.

(**A**) Violins show epistasis for different kinds of mutation pairs (white point, median; black point, mean). Mutation pairs may contain mutations that are individually both beneficial (A+ B+), both deleterious (A− B−), or mixed (A+ B− and A− B+), or one of which confers an undetectable effect (A0 B+/− and A+/− B0). The number of each such pair is provided. Stacked bars show fractions of different epistasis types (colors as in [Fig. 1D](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1), with white where epistasis could not be computed). Scatterplots show fitness of double mutants against that expected if mutation effects combined additively. Points colored as in [Fig. 1D](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1). (**B**) Relationship between background fitness and the fitness change induced by mutations in the second promoter in Env1. Top: _araA_ promoter mutations added to existing _araB_ promoter mutations. Bottom: Inverse case. Colored points highlight particular alleles. Top: PLtetO-1-_araA_ alleles T2C (red) and G7C (blue). Bottom: PLlacO-1-_araB_ alleles T1A (red) and C11A (blue). Large points show effects in the WT background.

[Open in viewer](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F3)

### Correlation between fitness effects and epistasis across inducer environments
Confronted with such a variety of interactions, we asked whether they might be understood simply in terms of the quantitative fitness effects of the interacting mutations, as has been found for some other mutation sets ([15](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R15)). We found that the effects of individual mutations were weakly predictive of the type and value of epistasis they exhibited with mutations at the second promoter ([Fig. 3A](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F3), scatterplots). In all environments, there was a significantly negative correlation between the sum of individual fitness effects and the value of epistasis (Pearson’s _r_ = −0.36, −0.37, and −0.51 in Env1–3, respectively; _P_ < 2.2 × 10−16 for all), a trend of diminishing returns that appears common across experimental systems (fig. S8A) ([15](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R15)–[17](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R17)). However, when the two genes were considered separately, the relationship between individual fitness effects and epistasis was found to be markedly different between _araA_ and _araB_: The negative correlation was stronger for PLtetO-1-_araA_ mutations being added to existing PLlacO-1-_araB_ mutations than for the inverse case [Pearson’s _r_ = −0.67, −0.73, and −0.63 in Env1–3 (_P_ < 2.2 × 10−16 for all) versus 0.12, −0.20, and −0.34 (_P_ < 1.6 × 10−5 for all); fig. S8, B and C], in which the correlation can even be positive, an extremely rare trend in existing studies ([15](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R15)). Moreover, we found that the average trend was, in some cases, markedly nonmonotonic (fig. S8, B and C), revealing that different alleles of a particular promoter can cause similar fitness changes on their own but interact very differently with alleles at the second promoter.

The relationship between individual mutation effects and epistasis was further complicated by the fact that it could be different for different alleles of the same promoter. For example, in Env1, the numerous beneficial PLtetO-1-_araA_ mutations caused the average negative trend with PLlacO-1-_araB_ background fitness, while the rare deleterious PLtetO-1-_araA_ mutations showed no such trend ([Fig. 3B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F3), top). For individual PLlacO-1-_araB_ mutations in PLtetO-1-_araA_ backgrounds, the relationship was consistently nonmonotonic but had a different average direction for individually beneficial or deleterious alleles ([Fig. 3B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F3), bottom). Moreover, the trend for a given allele could vary greatly with the environment (fig. S8, B and C). These results demonstrate that genes interacting simply through their common participation in a linear pathway can exhibit complex allele- and environment-dependent trends of epistasis. The smooth patterns exemplified by [Fig. 3B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F3), however, suggest that they may in principle be understood from an underlying phenotypic mechanism.

### Phenotype fitness model
To this end, we derived a quantitative model of the metabolic pathway from Michaelis-Menten kinetics, where flux, , increases with cellular AraA and AraB activities (denoted as _A_ and _B_, respectively) and saturates at a maximum (denoted as 1/η) imposed by downstream metabolism ([18](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R18), [19](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R19)). Flux increase results not only in a fitness benefit ([20](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R20)), _u_, but also a cost, _v_, of toxic intermediate accumulation (fig. S9) ([18](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R18), [21](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R21), [22](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R22)), which diverges as  when downstream metabolism saturates (Supplementary Materials and Methods). Integrating these ingredients together with a basal growth rate, ω, and enzyme expression costs ([22](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R22), [23](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R23)), θ_A_ and θ_B_, log fitness was computed as . The six parameters of this model are expected to account for all nonlinearities of the phenotype-to-fitness relationship and particularly replace the 3888 coefficients required for parameterizing epistasis across the three environments.

Each promoter mutation was then characterized as a change in the activity (via expression) of AraA or AraB. Because most mutations lay outside of the repressor binding sites governing promoter inducibility ([Fig. 1B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1)), the fold change in activity caused by each mutation was kept constant across inducer environments. Expression costs were also quantified independently of flux-fitness effects by measuring the fitness of all genotypes in the absence of arabinose (fig. S10). Parameterization of the fitness function, WT activities across environments, and expression effects of individual mutations was then performed on fitness data from all four environments simultaneously, with the metabolic terms of the fitness function vanishing in the absence of arabinose (reducing it to the noninteractional function, _F_ = ω(1 – θ_A__A_ – θ_B__B_)) (data S2 and fig. S11).

The fitted model is in excellent agreement with our data, yielding _r_2 values of >0.97 between experimental and predicted fitness effects and >0.80 between experimental and predicted epistasis coefficients ([Fig. 4, A and B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F4) and figs. S12 and S13; see fig. S14 for more minimal models). Notably, fitting on just 5% of the dataset, and in particular on single mutants alone, yields a fit as good as when using the complete dataset (_r_2 of 0.97; fig. S15). Inferred expression effects are well supported by reverse transcription quantitative polymerase chain reaction (RT-qPCR) measurements (Pearson’s _r_ > 0.94; fig. S16), which also confirm the expected lack of direct interactions between promoters at the level of expression (as does the disappearance of epistasis in the absence of arabinose) (fig. S17). The model is capable of recapitulating the diverse and complex trends of epistasis seen in the data. We find that the nonmonotonic relationships between single-mutant fitness and the fitness impact of alleles at the second promoter are well explained by the single mutants lying at two sides of a phenotypic optimum ([Fig. 4B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F4)). This overshooting, which is also the cause of sign epistasis ([Fig. 4C](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F4)) ([24](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R24)), is relatively common in our dataset, mostly because l-ribulose-5-phosphate toxicity results in an optimum in the flux-fitness relationship (fig. S18) ([18](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R18), [21](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R21)). Two alleles of the same gene may, thus, result in similar fitness changes individually but cause substantially different expression levels and fluxes, resulting in different responses to mutations at the second gene. This is principally due to enzymes having different degrees of flux control on each side of the optimum, with lower levels of one resulting in the second having less control.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710074316597-495f1b71-045e-46b9-b988-0c6f7cf6f118.jpeg)

Fig. 4 Mechanistic basis of heterogeneous, environmentally dependent epistasis.

(**A**) Fitted activity fitness model. Spheres are positioned according to predicted activity levels and observed _F_rel (Env1–3: red, blue, and orange, respectively). Three largest spheres are WT, intermediate-sized spheres are single mutants, and small pale spheres are double mutants. (**B**) Upper plots recapitulate [Fig. 3B](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F3). Lower plots show highlighted genotypes within fitness landscape (black point is WT; other large points are single mutants, gray for the gene considered as carrying the background alleles). (**C**) Fitness surface on log activity scale colored by predicted intergenic epistasis type (colors as in [Fig. 1D](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F1); determined as nonsignificant (gray) if magnitude is <0.01). Large black point is WT. Smaller, opaque blue, red, and black points are single mutants, colored by observed _F_rel (deleterious, beneficial, and neutral, respectively). Transparent points are double mutants, colored by observed epistasis type and sized by epistasis strength. (**D**) Dark gray marks area below a hypothetical disease threshold (40% of maximum fitness). Points are four genotypes in Env2 (blue) and Env3 (orange): WT (largest), C11A of PLtetO-1-_araA_ and G7T of PLlacO-1-_araB_ (intermediate size), and the resulting double mutant (smallest). Green arrow represents a change in activity levels caused by nongenetic factors like aging or environment. A disease state results here from one combination of alleles and environment (pale orange).

[Open in viewer](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F4)

The model reveals how the biology underlying a linear pathway can result in heterogeneous, environmentally dependent intergenic interactions. It disentangles the contributions of the “specific” genotype-to-expression and “nonspecific” expression-to-fitness relationship ([25](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R25)), and integration with molecular models of the former could allow end-to-end prediction of epistasis from genotype ([26](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R26)). When fitness depends solely on flux ([18](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R18), [20](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R20)), the nature of epistasis should be guaranteed by pathway topology alone ([18](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R18)). Under the slightly more complex selection pressure resulting from metabolite toxicity ([18](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R18), [21](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R21)) and gene expression costs, however, interactions can be both positive and negative. We find that epistatic categories form several localized domains over the fitness landscape, their size and position dependent on the WT phenotype, controlled here by the environment ([Fig. 4C](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F4) and fig. S19). These domains are large and orderly enough to be predictable, but only through knowledge of the underlying expression-fitness landscape and the position of the relevant genotypes within it—its nonmonotonic form, which may be a common property ([27](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R27)) due to general physiological trade-offs like resource allocation ([23](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R23), [28](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R28)), precludes the prediction of how two mutations will interact from knowledge of their fitness effects in one context alone.

## DISCUSSION
The importance of this knowledge becomes immediately apparent when considering the existence of a disease threshold ([1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R1)–[3](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R3)), as, for example, in hyperphenylalaninemia, where multiple genetic and environmental factors governing phenylalanine metabolism and transport can combine to produce the clinical cognitive phenotype ([1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R1)). Because of the landscape’s nonlinearity, the two mutant alleles shown in [Fig. 4D](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F4) can lead to a below-threshold phenotype, but only when they co-occur (small, pale-orange point) in one particular condition (orange points), while being masked in others (blue points). The model thus provides a mechanism by which potential physiological defects can be manifested, aggravated, or alleviated by particular combinations of alleles and environments ([1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R1)–[5](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R5)). Insight into intergenic fitness landscapes for other biological systems ([29](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R29), [30](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R30)), and for genes connected by more complex topologies, will be indispensable for progress across medicine, bioengineering, and evolution.

## MATERIALS AND METHODS
### General microbiology and molecular biology
Lysogeny broth (LB) powder, agar, salts, sugars, growth supplements, antibiotics, and inducers were all purchased from Sigma-Aldrich. Bacteria were cultured in LB, unless otherwise stated. Liquid LB was the standard Lennox formulation, except for when blasticidin S was included, in which case the Luria low-salt formulation [NaCl (0.5 g/liter)] was used. LB agar always contained the Luria low-salt formulation. M9 base medium consisted of 1X M9 salts supplemented with 1 mM MgSO4 and 100 μM CaCl2. Unless otherwise stated, l-arabinose was used at a concentration of 0.03% (w/v). Ampicillin (amp) was used at 100 μg/ml, chloramphenicol (cm) at 10 μg/ml, streptomycin (str) at 50 μg/ml, blasticidin S (bsd) at 100 μg/ml, erythromycin (erm) at 20 μg/ml, and kanamycin (kan) at 50 μg/ml. Bacterial cultures were grown at 37°C (with shaking at 200 rpm for liquid cultures; Multitron, Infors HT), unless otherwise stated, and culture stocks were stored at −80°C in LB with 40% glycerol. For electroporation, DNA was added to 50 μl of homemade electrocompetent cells (unless otherwise stated), transferred to a 1-mm gap electroporation cuvette (VWR), and submitted to a pulse of 1800 V (Electroporator 2510, Eppendorf). Cells were immediately transferred to fresh LB for recovery at 37°C (unless otherwise stated) with shaking for 30 to 90 min before being plated on the appropriate selective media and left to grow overnight.

All enzymes and molecular biology reagents were purchased from New England Biolabs (NEB) unless otherwise stated. Primers were purchased from IDT or Eurofins and designed with the help of Primer3 ([31](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R31)). For sensitive applications like barcoding and next-generation sequencing library preparation, primers were ordered high-performance liquid chromatography (HPLC) purified, otherwise they were ordered desalted. UltraPure agarose was supplied by Invitrogen, and all agarose gels were stained with SYBR Safe (Thermo Fisher Scientific) and visualized with a GelDoc XR+ imager (Bio-Rad). The GeneRuler 1 kb Plus ladder (Thermo Fisher Scientific) was used for DNA fragment size estimation.

All plasmids used in this study, excluding the mutant library, are detailed in table S1. DNA fragments used in cloning are detailed in table S2. Primers, excluding those used for promoter mutagenesis, are provided in table S3. All strains are detailed in table S4. Primers used in promoter mutagenesis are provided in table S5.

### Plasmid construction
Our library creation strategy depended on two plasmids, pKH1511c and pKH1511d, which were created in this study. pKH1511c serves as the library “backbone,” carrying all the necessary elements of the final plasmid library except for the PLtetO-1 and PLlacO-1 promoters destined to drive _araA_ and _araB_ expression, respectively: _p15A_ origin of replication (_ori_), _lacI_-_tetR_ repressor cassette (for inducibility of PLtetO-1 and PLlacO-1), _araA_, and _araB_. _araA_ and _araB_ open reading frames (ORFs) (with their upstream ribosome binding site–containing regions) are divergently oriented (with each followed by an artificial transcriptional terminator) and are separated by two restriction sites to allow easy insertion of divergently oriented PLtetO-1 and PLlacO-1 promoters. pKH1511d serves as a template for amplification of a _bsd_ blasticidin S resistance cassette with primers containing the PLtetO-1 and PLlacO-1 variant sequences, allowing their eventual insertion into pKH1511c (fig. S1). pKH1511d replication is pir dependent, abolishing the occurrence of false-positive colonies caused by PCR template carryover during library cloning. Plasmids, DNA fragments, PCR primers, and bacterial strains used in the construction of these two plasmids are detailed in tables S1 to S4, respectively, and the detailed cloning methods follow.

The DNA fragments used to construct pKH1503a, pKH1511c, and pKH1511d come from either PCR amplification or from direct restriction digestion of purified plasmid DNA and were joined by either standard restriction-ligation or by Gibson Assembly (in which case, overlaps of ~40 nucleotides were used) ([32](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R32)). PCR amplifications were all performed with Phusion Hot Start II High-Fidelity DNA Polymerase (Thermo Fisher Scientific) in its High-Fidelity buffer, following the manufacturer’s recommendations. Restriction enzymes were used according to the manufacturer’s instructions. When found necessary to reduce the occurrence of false-positive colonies, DNA was treated with calf intestinal alkaline phosphatase (to reduce vector self-ligation) and/or Dpn I (to digest PCR template). After PCR amplification and/or digestion, DNA fragments were either verified by electrophoresis and column purified (QIAquick PCR Purification Kit, QIAGEN) or, when necessary, gel purified (QIAquick Gel Extraction Kit, QIAGEN). Gel purification was always followed by a second clean-up (QIAquick PCR Purification Kit, QIAGEN) to improve DNA quality for ligation. For gel extractions, agarose gels were stained with SYBR Safe (Thermo Fisher Scientific), and DNA was visualized with blue light to avoid ultraviolet-induced DNA damage (Blue Transilluminator, Pearl Biotech). A NanoDrop ND-1000 spectrophotometer (Thermo Fisher Scientific) was used to determine DNA concentration for all fragments before ligation/Gibson Assembly. Standard ligation and Gibson Assembly were performed using T4 ligase and Gibson Assembly Master Mix (NEB), respectively, according to the manufacturer’s recommendations (T4 ligase was then inactivated by heating at 65°C for 10 min). In both cases, DNA was subsequently microdialyzed against water for >30 min (MF-Millipore, Merck), and 1 to 5 μl were electroporated into 50 μl of electrocompetent cells. DH5α ΔaraBA was used as the cloning strain, except when the plasmid was pir dependent, in which case PIR1 was used. After electroporation, cells were recovered in 1 ml of LB for 30 to 90 min at 37°C with shaking at 200 rpm, plated on LB agar in the presence of the antibiotic indicated in table S1, and incubated overnight at 37°C. Plasmid DNA was purified from several colonies (QIAquick PCR Purification Kit, QIAGEN) and verified by both restriction analysis and Sanger sequencing of the insert region.

### Strain engineering and adaptation
The final library host strain, _E. coli_ MG1655 Δ_araBA_ D-ara+/evo Δ_fucK_ Δ_lacIZYA_::_cat_ D/L-araevo (table S4), was originally designed to have a rewired d-arabinose metabolism ([33](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R33)–[35](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R35)), in which _araB_ (but not _araA_) participates. d-Arabinose was not used in this study; however, this feature (d-ara+/evo Δ_fucK_) is not relevant here. In addition, _araA_ and _araB_ ORFs were removed from the chromosome to allow them to be expressed exclusively from plasmids [the third gene of the _araBAD_ operon (_araD_) was kept on the chromosome under the control of its native l-arabinose–responsive promoter, as were the transcriptional regulator gene (_araC_) and the transporter genes (_araE_, _araFGH_, and _araJ_)]; given the all-or-nothing response of the positive feedback loop governing l-arabinose uptake, all these genes are expected to be maximally induced by internal l-arabinose by the time of fitness measurement ([36](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R36))). Furthermore, _lacIZYA_ was replaced by a _cat_ chloramphenicol resistance cassette. This allows the use of isopropyl-β-d-thiogalactopyranoside (IPTG) to control the artificial promoter, PLlacO-1, in the absence of any effects resulting from induction of the native _lac_ operon, and the absence of _lacY_ also causes this control to be titratable rather than all or nothing ([37](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R37)). Last, this strain was transformed with plasmid pKH1503a (which carries an _araBA_ cassette under the control of PLlacO-1; table S1) and briefly adapted to M9 with alternating d-/l-arabinose (see above) in the presence of a low concentration of IPTG. This adaptation step was included to allow fixation of any mutations conferring a very high fitness advantage to our engineered strain in our approximate experimental conditions, to avoid them interfering with mutant library competition experiments. For the growth curve experiments assessing l-ribulose-5-phosphate toxicity, the final library host strain was further modified by deleting _araD_ from the chromosome to obtain _E. coli_ MG1655 Δ_araBA_ D-ara+/evo Δ_fucK_ Δ_lacIZYA_::_cat_ D/L-araevo Δ_araD_::_kan__R__._ Detailed strain engineering methods follow.

Details of the final library host strain, its Δ_araD_ derivative, and all intermediates used in their creation are provided in table S4. Gene knockouts (KOs) were performed using the method of Datsenko and Wanner ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)). The relevant strain was made electrocompetent and electroporated with 10 ng of plasmid pKD46 DNA, and transformants were selected on LB agar with ampicillin (100 μg/ml) at 30°C. Several colonies were then reisolated under the same conditions. The _cat_ chloramphenicol resistance cassette was PCR amplified from pKD3 ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)) using primer pairs KO-araBA-fwd/KO-araBA-rev for _araBA_, KO-lacIZYA-fwd/KO-lacIZYA-rev for _lacIZYA_, and KO-fucK-fwd/KO-fucK-rev for _fucK_, and a 2:1 mix of GoTaq/Pfu DNA polymerases (Promega). Similarly, the _kan__R_ kanamycin resistance cassette was PCR amplified from pKD4 ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)) using primer pair KO-araBA-fwd/KO-araD-rev for _araD_. PCR products were verified by 1% agarose gel electrophoresis, column purified (QIAquick PCR Purification Kit, QIAGEN), and spectrophotometrically quantified (NanoDrop ND-1000). A preculture of a single pKD46-transformed colony was grown overnight (LB-amp) at 30°C and then diluted 100× into LB-amp with 0.2% l-arabinose and grown at 30°C to an OD600nm (optical density at 600 nm) of ~0.7 (3 to 5 hours; BioMate 3S, Thermo Fisher Scientific). The culture was made electrocompetent and electroporated with ~200 ng of the purified PCR product, and recombinants were selected on LB agar with chloramphenicol (10 μg/ml) [or kanamycin (50 μg/ml)] at 37°C for curing of pKD46. Several colonies were then reisolated under the same conditions and tested in parallel for pKD46 curing by plating on LB-amp and checking for colonies after an overnight growth at 30°C. Several of the reisolated colonies were verified by colony PCR using three primer pairs for each KO ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)). The gene-specific primers are verif-araBA-fwd/verif-araBA-rev for _araBA_, verif-lacIZYA-fwd/verif-lacIZYA-rev for _lacIZYA_, verif-fucK-fwd/verif-fucK-rev for _fucK_, and verif-araBA-fwd/verif-araD-rev for _araD_; the common _cat_ and _kan__R_ primers are c1/c2 and k1/k2, respectively, from ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)). For each KO, the three primer pairs were gene-specific fwd/gene-specific rev, gene-specific fwd/c1 (or k1), and gene-specific rev/c2 (or k2). GoTaq DNA polymerase (Promega) was used for amplification, following the manufacturer’s recommendations, and PCR products were analyzed by agarose gel electrophoresis (1.5%). In the case of _araBA_ and _fucK_, we wished to retain function of the remaining genes in their respective operons, and so the _cat_ cassette was removed as described in ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)). For this, a preculture of a single recombineered colony was grown overnight (LB-cm, 37°C) and then diluted 100× into LB-cm and grown at 37°C to an OD600nm of ~0.7 (2 to 4 hours; BioMate 3S, Thermo Fisher Scientific). The culture was made electrocompetent and electroporated with 10 ng of plasmid pCP20 DNA, and transformants were selected on LB agar with ampicillin (100 μg/ml) at 30°C. Several colonies were then reisolated under the same conditions and then again in the absence of ampicillin at 42°C to cure pCP20 ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)). Last, several colonies were streaked in parallel on LB (37°C, purification), LB-cm (37°C, verify _cat_ loss), and LB-amp (30°C, verify pCP20 loss). The loss of the _cat_ cassette through flippase recognition target (FRT) recombination was molecularly verified for several clones by colony PCR using the same primer pairs and conditions described above for _cat_ insertion verification. The PCR products resulting from amplification with the gene-specific primer pairs were also Sanger sequenced (GATC; using the amplification primers) as a final verification.

Adaptations were performed as described in table S4. For the initial adaptation step, precultures were grown overnight in LB and washed twice in an equal volume of M9, and 1 ml washed cells was diluted in 100 ml of the appropriate adaptation media. Once growth became apparent, cultures were serially transferred in a volume of 20 ml, being left to grow for ~24 hours between each transfer, at which point they were diluted ~100× into fresh media. After adaptation, colonies were isolated on agar plates containing the same media used for adaptation.

To cure the plasmid from MG1655 Δ_araBA_ D-ara+/evo Δ_fucK_ Δ_lacIZYA_::_cat_ D/L-araevo, a preculture was grown overnight in LB-cm, and dilutions were plated on LB-cm with 2% ribitol and 200 μM IPTG. IPTG induces _araBA_ from the plasmid, and AraB converts ribitol to the toxic compound ribitol phosphate ([39](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R39)), rendering plasmid-harboring cells unable to grow. Several colonies were tested and confirmed for plasmid loss by streaking on LB-str and by colony PCR (primers oKH150401c/oKH150202d, GoTaq, Promega), with comparison to control colonies grown in the absence of ribitol. The final plasmid-less host strain was also tested once more for its marker-less _ΔaraBA_ and _ΔfucK_ deletions using colony PCR (primer pairs verif-araBA-fwd/verif-araBA-rev and verif-fucK-fwd/verif-fucK-rev, as above).

### Library creation strategy
On the evolutionary scale, direct changes in the total cellular activity of a particular enzyme can occur through either regulatory mutations, which alter the concentration of active enzyme, or structural mutations, which can affect both active enzyme concentration and kinetic parameters. A common target of regulatory mutations is the promoter ([40](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R40)), which controls a protein’s expression level by determining transcription rate, and we decided to focus on promoter mutations in this study. We first placed _araA_ and _araB_ under the control of the well-known artificial, chemically inducible promoters, PLtetO-1 and PLlacO-1, developed by Lutz and Bujard ([41](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R41)). They are each regulated by a single transcription factor (_tetR_ repressor for PLtetO-1 and _lacI_ repressor for PLlacO-1) and can be specifically induced to different levels by the addition of a small, nonmetabolizable compound [anhydrotetracycline (aTc) for PLtetO-1 and IPTG for PLlacO-1]. We focused mutagenesis on the RNA polymerase-binding sites (−35 and −10 hexamers) of the two promoters, as these sites are known to be the most significant determinants of expression level in the core promoter ([42](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R42), [43](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R43)). Conveniently, these sites are identical between PLtetO-1 and PLlacO-1, coming from phage lambda PL in both cases ([41](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R41)). For each promoter, we constructed all possible single–base pair (bp) substitutions over this 12-bp region (36 mutants for each promoter), along with the WT sequence. All 37 sequence variants of the two promoters were combined together, resulting in a plasmid library containing all 1296 double-promoter mutants, all 36 single-promoter mutants for each promoter (one promoter is mutated, and the other is WT), and the full WT (both promoters are WT). Most of the mutations in the RNA polymerase-binding sites are expected to have little or no effect on repressor binding, and their relative effect on expression should be similar across different inducer concentrations ([44](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R44), [45](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R45)). However, one of the −10 bases on PLtetO-1 overlaps with a _tet_ operator, and three of the −35 bases on PLlacO-1 are expected to overlap with a _lac_ operator (fig. S1) ([41](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R41)), meaning that the effect on expression of mutations at these positions could depend on inducer concentration ([46](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R46)).

The overall structure of the plasmid on which the library is based is shown in fig. S1. _araA_ and _araB_ are divergently expressed from PLtetO-1 and PLlacO-1 promoters, respectively. These two promoters are separated from each other by a short _bsd_ blasticidin S resistance cassette ([47](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R47)) to reduce any physical interactions between them. The presence of a resistance cassette between the promoters also considerably increased cloning efficiency, as explained below, and _bsd_, in particular, was chosen for its small size (396-bp ORF), making it possible to sequence both promoters on a single amplicon using paired-end Illumina technology (fig. S1). The promoters’ repressors, _tetR_ and _lacI_, were included on the plasmid.

Plasmid molecules were also intergenically tagged with unique DNA barcodes, similarly to ([48](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R48)) (fig. S1). These were used to help overcome the problem of PCR and sequencing errors and to increase the confidence in mutant fitness estimates by providing many independent frequency trajectories for each mutant (figs. S2 to S4). The barcodes, thus, also allowed us to account for anomalous lineages containing off-target mutations (present in the initial library) and de novo mutations (arising during competition assays). They consist of 20 random nucleotides split into four blocks of five ([49](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R49)) to avoid the creation of restriction sites used in a later sequencing step: N5ATN5ATN5ATN5. Barcodes were inserted downstream of the _lacI_-_tetR_ cassette, far from the PLtetO-1 and PLlacO-1 promoters, to avoid any effects on _araA_ and _araB_ expression and so are expected to be effectively neutral for fitness (fig. S1). Care was taken throughout to avoid loss of library complexity (fig. S2), and quality controls were used at each step of library construction.

The pooled plasmid library was constructed using standard restriction-ligation cloning (fig. S1). Because of their short length, promoter sequences could be introduced facing outward on the 5′ ends of PCR primers that were used to amplify a _bsd_ ([47](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R47)) blasticidin S resistance cassette from plasmid pKH1511d (PLtetO-1 on forward primers and PLlacO-1 on reverse primers). This was done using primer pools with randomized nucleotides at each of the 12 target positions for each promoter. The primers also contained restriction sites on their 5′ extremities, allowing the resulting amplicon pool to be ligated into the library backbone, pKH11511c, in the desired orientation. The resulting plasmid library was transformed into DH5α Δ_araBA_, and colonies were selected on blasticidin S. This strategy ensured that the occurrence of false-positive colonies from undigested or self-ligated vector was negligible, as a functional _ori_ could only come from pKH11511c (the pKH1511d _ori_ is _pir_ dependent), while _bsd_ was only present in pKH1511d. Because of the use of fully randomized nucleotides at each target position and the combinatorial way in which variants of the two promoters were cloned together, the expected genotype frequencies in this initial library are 1 of 16 for WT, 1 of 192 for each of the 72 single-promoter mutants, and 1 of 2304 for each of the 1296 double-promoter mutants. With this in mind, an estimated 40,000 colonies were harvested in this step to avoid loss of library complexity. Barcodes were added in a second round of restriction-ligation cloning and introduced via a randomized PCR primer. The primer, containing fully randomized nucleotides at 20 positions, was used to amplify the _bla_ β-lactamase gene from plasmid pKD3 ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)), and the resulting amplicon pool was swapped with the _aadA1_ streptomycin/spectinomycin resistance gene in the plasmid library backbone. The primer contains restriction sites on its 5′ extremity, one of which is used for this ligation, and another of which allows the barcodes to be moved closer to the mutated promoter region in a later step (see the “Barcode promoter association” section). The barcoded plasmid library was again transformed into DH5α Δ_araBA_, and colonies were time selected on ampicillin. False-positive colonies were avoided for the same reason as above, as pKD3 also has a pir-dependent _ori_. An estimated 100,000 colonies were harvested during this step, with the vast majority expected to contain a unique barcode. Expected barcode richness was, thus, 6250 for WT, 521 for each single-promoter mutant, and 43 for each double-promoter mutant. In the final step, the engineered host strain, MG1655 Δ_araBA_ D-ara+/evo Δ_fucK_ Δ_lacIZYA_::_cat_ D/L-araevo, was transformed with this barcoded plasmid library, and an estimated 600,000 colonies were harvested after selection on ampicillin. Detailed library construction methods follow.

### Library creation methods
To create the initial library, two promoter-containing primer sets, oPtetLib-fwd and oPlacLib-rev, were each pooled in equimolar quantity (table S5). These two primer pools were then used together at a concentration of 0.5 μM each pool to PCR amplify _bsd_ from plasmid pKH1511d using Phusion Hot Start II High-Fidelity DNA Polymerase (Thermo Fisher Scientific) in its High-Fidelity buffer, following the manufacturer’s recommendations. Cycling conditions were 98°C for 30 s, followed by 35 cycles of 98°C for 10 s, 60°C for 30 s, and 72°C for 15 s, with a final extension step of 72°C for 2 min. PCR product quality was checked by agarose gel electrophoresis, after which the product was column purified (QIAquick PCR Purification Kit, QIAGEN) and quantified with a NanoDrop ND-1000 spectrophotometer (Thermo Fisher Scientific). The purified product and plasmid pKH1511c were then both digested for 90 min with Xho I and SacI-HF restriction enzymes (NEB CutSmart buffer), and digested DNA was again column purified (QIAquick PCR Purification Kit, QIAGEN) and quantified with a NanoDrop ND-1000 spectrophotometer. The pKH1511c vector fragment (70 ng) was ligated in a 1:3 molar ratio with the _bsd/_promoter-containing insert in a total volume of 20 μl. The ligation was carried out at 16°C overnight using T4 DNA ligase (NEB T4 DNA ligase reaction buffer), which was then deactivated by heating at 65°C for 10 min. The ligate was microdialyzed against water for 30 min (MF-Millipore, Merck), after which several transformations were performed as follows: 3 μl was electroporated into 50 μl of electrocompetent DH5α Δ_araBA_ cells, and cells were recovered in 500 μl of low-salt (Miller) LB for 1 hour at 37°C with shaking at 200 rpm, plated on LB agar with blasticidin S (100 μg/ml), and incubated overnight at 37°C. Colony PCR and Sanger sequencing (GATC) of the mutated promoter region was performed on four of the resulting colonies as a preliminary test of library quality, and all four clones had a unique promoter genotype with a single base substitution in the target region of either one or both promoters, as expected. An estimated 40,000 colonies were scraped off the agar into LB-glycerol (40%), and plasmid DNA was purified from a sample of this cell suspension (QIAprep Spin Miniprep Kit, QIAGEN) after thorough mixing.

To barcode the plasmid library, primers oBarcodeBla-fwd and oBarcodeBla-rev (table S3) were used at a concentration of 0.5 μM each to PCR amplify _bla_ from plasmid pKD3 ([38](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R38)) using Phusion Hot Start II High-Fidelity DNA Polymerase (Thermo Fisher Scientific) in its High-Fidelity buffer, following the manufacturer’s recommendations. Cycling conditions were 98°C for 30 s, followed by 30 cycles of 98°C for 10 s, 60°C for 30 s, and 72°C for 25 s, with a final extension step of 72°C for 3 min. PCR product quality was checked by agarose gel electrophoresis, after which the product was column purified (QIAquick PCR Purification Kit, QIAGEN) and quantified with a NanoDrop ND-1000 spectrophotometer (Thermo Fisher Scientific). The purified product was then digested for 1 hour with SpeI-HF restriction enzyme (NEB CutSmart buffer), while the purified plasmid library obtained above was digested for 1 hour with BstZ17I and SpeI-HF restriction enzymes (NEB CutSmart buffer). Digested DNA was again column purified (QIAquick PCR Purification Kit, QIAGEN) and quantified with a NanoDrop ND-1000 spectrophotometer. The digested library (60 ng) was ligated in a 1:4 molar ratio with the _bla_/barcode-containing insert in a total volume of 20 μl. The ligation was carried out at 16°C overnight using T4 DNA ligase (NEB T4 DNA ligase reaction buffer), which was then deactivated by heating at 65°C for 10 min. The ligate was microdialyzed against water for 30 min (MF-Millipore, Merck), after which several transformations were performed as follows: 1 μl was electroporated into 15 μl of commercially prepared Electromax DH5α-E electrocompetent cells (Invitrogen), and cells were recovered in 500 μl of LB for 30 min (to minimize cell replication) at 37°C with shaking at 200 rpm, plated on LB agar with ampicillin (100 μg/ml), and incubated overnight at 37°C. The use of commercially prepared electrocompetent cells was necessary due to reduced cloning efficiency at this step, possibly due to the ligation reaction involving blunt ends. Plasmid DNA was purified from three colonies (QIAquick PCR Purification Kit, QIAGEN) for Sanger sequencing (GATC) of the mutated promoter and barcode regions as a preliminary test of barcoding efficiency. All three colonies were found to have a unique promoter genotype, as before, along with a unique, correctly inserted barcode. An estimated 100,000 colonies were scraped off the agar into LB-glycerol (40%), and plasmid DNA was purified from a sample of this cell suspension (QIAprep Spin Miniprep Kit, QIAGEN) after thorough mixing.

To move the barcoded plasmid library into the final host strain while avoiding the creation of transformants harboring multiple unique plasmids ([50](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R50)), several transformations were performed as follows, with plasmid concentration kept low: 5 ng of the purified barcoded plasmid library obtained above was electroporated into 50 μl of electrocompetent MG1655 Δ_araBA_ D-ara+/evo Δ_fucK_ Δ_lacIZYA_::_cat_ D/L-araevo cells, and cells were recovered in 500 μl of LB for 30 min at 37°C with shaking at 200 rpm, plated on LB agar with ampicillin (100 μg/ml), and incubated overnight at 37°C. An estimated 600,000 colonies were scraped off the agar into LB-glycerol (40%), and this cell suspension was aliquoted and stored at −80°C after thorough mixing.

### Barcode promoter association
To reveal the PLtetO-1 and PLlacO-1 promoter sequences linked to each barcode sequence, barcodes were first brought closer to the promoters by excision of the intervening region from the plasmid followed by recircularization ([48](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R48)). PCR amplification was then used to add the technical sequences necessary for paired-end Illumina MiSeq sequencing of barcode promoter amplicons (fig. S1B).

To first move barcodes closer to the promoter region, the purified barcoded plasmid library was digested for 90 min with Xho I, SalI-HF, and Sph I restriction enzymes (NEB CutSmart buffer). The largest fragment (~5.5 kb), which contains the mutated promoters and the barcode, was gel purified (QIAquick Gel Extraction Kit, QIAGEN) using a 1% agarose gel and quantified using a NanoDrop ND-1000 spectrophotometer before being self-ligated. Xho I and Sal I are isocaudamers, so they create complementary cohesive ends, but the sequence resulting from ligation between these ends is no longer recognized by either enzyme (Sph I cuts within the region being discarded and was simply included to ease gel extraction of the desired fragment). Because of this, they can be included in the reaction mix during self-ligation of the purified fragment to help reduce intermolecular ligation [undesired intermolecular ligation events that recreate Xho I and Sal I sites can be reversed, releasing the original monomers and so increasing the efficiency of the desired intramolecular ligation reaction ([48](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R48), [51](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R51))]. Because of the inclusion of these restriction enzymes, the self-ligation reaction was carried out in a restriction enzyme buffer, with adenosine 5′-triphosphate (ATP) added for ligase activity. In addition, the concentration of DNA and ligase was substantially reduced compared to standard ligation reactions to further reduce the occurrence of intermolecular ligation. The self-ligation reaction mix, thus, consisted of 1X NEB restriction buffer 2 supplemented with bovine serum albumin (100 μg/ml) and 1 mM ribo-ATP (NEB), 30 ng of DNA, 1 U each of Xho I and SalI-HF, and 800 U of T4 DNA ligase, in a total volume of 200 μl. Inspired by the strategy in ([51](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R51)), the reaction was cycled 50 times between 37°C (restriction enzyme and ligase activity optimum) for 5 min and 16°C (promote annealing of DNA termini) for 15 min. A final incubation of 37°C was carried out for 15 min to promote digestion of any remaining Xho I and Sal I sites, followed by one of 65°C for 20 min to inactivate all enzymes. The ligate was concentrated to ~20 μl using a SpeedVac concentrator (Savant DNA 120, Thermo Fisher Scientific) and then microdialyzed against water for 90 min (MF-Millipore, Merck). As a preliminary test of the success of this ligation step, a portion of the ligate was used in a transformation to allow isolation and sequencing of several recircularized plasmids: 2 μl was electroporated into 50 μl of electrocompetent DH5α Δ_araBA_ cells; cells were recovered in 500 μl of LB for 30 min at 37°C with shaking at 200 rpm, plated on LB agar with ampicillin (100 μg/ml), and incubated overnight at 37°C; and plasmid DNA was purified from six colonies (QIAquick PCR Purification Kit, QIAGEN) for Sanger sequencing (GATC) of the ligated region containing the mutated promoters and barcode. All six clones were found to have the expected linking sequence between promoters and barcode, and all plasmids were inferred to be monomeric due to the high Phred scores of the chromatograms (suggesting the presence of a single unique barcode on each recircularized plasmid).

With the recircularized DNA placing barcodes in proximity to their respective mutated promoters, this region was then PCR amplified in a 40-μl reaction using 25 ng of the ligated DNA as template and 0.6 μM each of primers oLinkBarcode-fwd and oLinkBarcode-rev (table S3). These primers contain adaptors for a second PCR at their 5′ extremities, followed by fully randomized hexamers added to increase amplicon diversity to facilitate MiSeq flow cell clustering. The KAPA HiFi HotStart ReadyMixPCR Kit (Kapa Biosystems) was used for amplification under the following cycling conditions (cycle number was kept low to reduce PCR errors and artefacts): 95°C for 3 min, followed by 15 cycles of 98°C for 20 s, 60°C for 30 s, and 68°C for 30 s, with a final extension step of 68°C for 2 min. The amplicon (~0.9 kb) was gel purified (QIAquick Gel Extraction Kit, Qiagen) using a 1.5% agarose gel and quantified fluorometrically (dsDNA HS Assay Kit with a QuBit 2.0, Thermo Fisher Scientific). A second 40-μl PCR was then performed using 5 ng of this amplicon as template and 0.6 μM each of the P5 and P7 Nextera Index Kit primer (Illumina) to add Illumina adaptors and multiplexing indexes. The KAPA HiFi HotStart ReadyMixPCR Kit (Kapa Biosystems) was again used for amplification under the following cycling conditions (cycle number was again kept low): 95°C for 30 s, followed by 12 cycles of 95°C for 10 s, 55°C for 30 s, and 68°C for 30 s, with a final extension step of 68°C for 5 min. The amplicon library (~1 kb) was gel purified (QIAquick Gel Extraction Kit, Qiagen) using a 1.5% agarose gel, and a 20,000× dilution was quantified by qPCR using the KAPA Library Quantification Kit for Illumina (Kapa Biosystems) on a LightCycler 480 (Roche) following the manufacturer’s recommendations.

The resulting amplicon library is composed of DNA fragments of the structure, P5 - i5 - N6 PCR tag - PLtetO-1 (rev) - _bsd_ (rev) - PLlacO-1 - N20 plasmid barcode - N6 PCR tag - i7 - P7, which are ~1 kb in size (close to the size limit for reliable MiSeq sequencing). A 300–nucleotide (nt) paired-end MiSeq sequencing allowed us to sequence the entire PLtetO-1 promoter on Read 1 and the plasmid barcode and entire PLlacO-1 promoter on Read 2 (note that Reads 1 and 2 do not overlap). For this, the 600-cycle MiSeq Reagent Kit v3 (Illumina) was used, and DNA was loaded at a concentration of 12 pM, with a 20% PhiX DNA spike-in (PhiX Control v3, Illumina). Preliminary quality filtering and demultiplexing by the standard MiSeq software package (Illumina) resulted in an output of >22 M read pairs, giving an expected coverage of >220× for each plasmid barcode.

MiSeq reads were processed using the mothur (version 1.37.6) ([52](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R52)) software package via the following steps: Reads were quality filtered by size (>199 bases), number of uncalled bases (<3 Ns), and length of the longest homopolymer stretch, another indicator of overall read quality (<9 bases). Entire PLtetO-1 sequences were extracted from Read 1, and barcode sequences and entire PLlacO-1 were extracted from Read 2 by Needleman alignment to reference sequences (default alignment parameters). Reads for which the PLtetO-1, PLlacO-1, or barcode region contained insertions or did not generate a full alignment with the reference were discarded. The mothur precluster algorithm was then used to cluster barcode sequences differing by a hamming distance of 1, with the aim of correcting for PCR and sequencing errors [the potential barcode diversity is so high (>1 × 1012) that the presence of immediately neighboring sequences is very likely due to these errors (fig. S2C)]. The algorithm uses sequence abundance to decide the “true” (majority) sequence for each cluster and to decide where a sequence clusters if it has >1 immediate neighbor. After degapping and regrouping barcode sequences to account for any alignment ambiguities resulting from small deletions, barcode clusters were used to build a dictionary assigning each true barcode sequence to a PLtetO-1 and PLlacO-1 sequence. Because of a high rate of PCR-derived recombination ([53](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R53)) being observed (caused by the extensive homology between all fragments and resulting in some molecules displaying incorrect barcode promoter associations), a haplotype-based strategy was used for this step rather than one in which each nucleotide is considered independently as in ([48](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R48)). This is because the small number of mutations expected to be present in each mutant (0–2) means that, at any particular position, most of the molecules will have the WT base. If the consensus PLtetO-1 and PLlacO-1 sequences attached to a particular barcode are computed by considering each nucleotide independently, then a high recombination rate can, thus, result in mutant bases being assigned as the WT base. The haplotype-based strategy, executed in Python (v3.5), consists of the following steps: For each barcode cluster (consisting of reads whose barcode sequences are identical to or the immediate neighbor of the inferred true barcode sequence), the associated complete PLtetO-1-PLlacO-1 concatenate sequences were grouped; the number of occurrences of each of these 108-nt PLtetO-1-PLlacO-1 sequences was tabulated; and if the cluster contained more than two read pairs in total, the most abundant concatenate PLtetO-1-PLlacO-1 sequence is ≥5× more abundant than the second most abundant one, and if the most abundant concatenate PLtetO-1-PLlacO-1 sequence contains no Ns (uncalled bases), then this PLtetO-1-PLlacO-1 sequence is assigned to the true barcode sequence for that cluster (else the cluster is discarded). This stringent requirement is aimed at reducing barcode promoter misassignments caused by PCR and sequencing errors, PCR-derived recombination, or intermolecular ligation during the first step of barcode promoter association, as well as to avoid any barcodes that may be linked to multiple promoter genotypes. Only barcodes associated to promoter genotypes for which the entire promoter regions contain no unexpected mutations were considered for further analysis.

### Mutant library competition assays
The final mutant library (host strain transformed with barcoded plasmid library) was competed over ~30 mean generations (~3 days) in the presence of casamino acids, l-arabinose (except for the no-arabinose control assay), and different concentrations of the inducers, aTc and IPTG. Cell density was kept low during competition (OD600 < 0.2) by serial transfer into fresh medium to maintain the culture in exponential phase and to avoid large changes in medium composition. Large volumes of media (100 ml) were used to avoid severe population bottlenecks during serial transfer (>1 × 108 cells each transfer). Plasmid DNA was purified from the culture at several time points for HiSeq sequencing of plasmid barcodes. Plasmid barcode abundance serves as a proxy for the abundance of cells carrying that particular barcode. The change in frequency over time of a barcode thus provides an estimate of competitive fitness for the lineage carrying that barcode ([54](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R54)). Since we know the PLtetO-1-PLlacO-1 sequence associated to each barcode (see the “Barcode promoter association” section), this in turn provides us with a distribution of fitness estimates for every mutant.

The base competition medium consisted of M9 + 0.1% casamino acids (for basal growth) + 0.03% l-arabinose (absent in the no-arabinose control assay), with ampicillin (100 μg/ml) to select against plasmid loss. A preliminary competition experiment was performed under inducer concentrations of aTc (20 ng/ml) and 30 μM IPTG, expected to endow the WT with near-maximal fitness (although this was found to be incorrect). A second round of competition experiments was carried out at a later date and was composed of three different inducer concentration combinations. One duplicated those of the initial experiment to check reproducibility (figs. S3 and S5), and the other two were 5 ng/ml aTc and no IPTG, and 200 ng/ml aTc and no IPTG. No IPTG was chosen to reduce _araB_ expression as much as possible, as the preliminary experiments suggested that the WT overexpressed _araB_ even in the absence of inducer ([23](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R23)) because of promoter leakiness. The range of aTc was chosen to explore the full range of achievable _araA_ expression. A final control competition experiment was performed on a third occasion in the absence of arabinose to isolate fitness effects resulting purely from changes in AraA and AraB expression burden. Inducer concentrations were as for the initial experiment [aTc (20 ng/ml) and 30 μM IPTG].

In detail, a sample of the frozen library cell stock was thawed and diluted in 200 ml of M9 + 0.5% casamino acids [with ampicillin (100 μg/ml)] in a 500-ml flask for a final blank-subtracted OD600 of 0.12 (200-μl read by a Varioskan microplate reader, Thermo Fisher Scientific). This common starting culture was recovered for ~3.5 hours at 37°C with shaking at 200 rpm, reaching an OD600 of 0.3, before being washed with 200 ml of M9 + 0.1% casamino acids. Washed cell pellets (each coming from 50 ml of the original culture) were resuspended directly in 100 ml of the different competition media for an effective 2× dilution of the original culture (OD600 of ~0.15; flasks of competition media were always prewarmed at 37°C to keep temperature constant and detect any contamination, with aTc, IPTG, and ampicillin being added at the time of transfer to avoid degradation). These cultures were then acclimatized to their respective competition media for ~2.25 hours (37°C, 200 rpm), reaching an OD600 of 0.23 to 0.28, to allow time for stable induction by aTc, IPTG, and l-arabinose. These acclimatized cultures were taken as _t_0, and so plasmid DNA was purified from a 50-ml sample of each culture (QIAprep Spin Miniprep Kit, QIAGEN) and quantified fluorometrically (dsDNA HS Assay Kit with a QuBit 2.0, Thermo Fisher Scientific) for eventual HiSeq sequencing of plasmid barcodes (the rest remaining after this and transfer was pelleted, resuspended in LB-40% glycerol, and stored at −80°C as an archive). Each culture (3.2 ml) was transferred to 100 ml of fresh competition media (~32× dilution) and left to grow (37°C, 200 rpm) to an OD600 of ~0.12 (three to four population generations). DNA was purified from a 50-ml sample of each culture (_t_1) as before, and 3.2 ml of each culture was again transferred to 100 ml of fresh competition media and left to grow to an OD600 of ~0.12 (~5 mean generations). This procedure was repeated until _t_6 (or _t_8 in an initial experiment), for a total of ~29 mean generations of competition (or ~39), over which time the impact of de novo mutation appears low (fig. S3). The precise number of population generations between each sampling was calculated from OD600 values and used for estimating fitness.

### Barcode sequencing of competed mutant library
To track plasmid barcode frequencies throughout the competition experiments, barcodes were PCR amplified from plasmid DNA in two steps, as for “Barcode promoter association” section, to add technical sequences necessary for 100-nt overlapping paired-end Illumina HiSeq sequencing. This was performed for time points _t_0, _t_1, _t_2, _t_4, _t_6, and _t_8 (approximately 0, 4, 9, 19, 29, and 39 mean generations) for the preliminary experiment; _t_1, _t_2, _t_4, and _t_6 for the next three experiments; and _t_0, _t_1, _t_2, _t_3,_t_4, _t_5,_t_6,_t_7, and _t_8 for the no-arabinose control experiment. These time points were chosen with the aim of obtaining precise fitness estimates for both large-effect and small-effect mutations.

In detail, at each selected time point, 20 ng of purified plasmid DNA was PCR amplified in a 40-μl reaction using 0.6 μM each of primers oBarcodeSeq-fwd and oBarcodeSeq-rev (table S3). These primers contain adaptors for a second PCR at their 5′ extremities, followed by fully randomized hexamers to increase amplicon diversity, as in the “Barcode promoter association” section. In this case, the randomized hexamers were also used to detect PCR duplicates arising from the second PCR. The KAPA HiFi HotStart ReadyMixPCR Kit (Kapa Biosystems) was used for amplification under the following cycling conditions (cycle number was kept low to reduce PCR errors and artefacts): 95°C for 3 min, followed by 12 cycles of 98°C for 20 s, 60°C for 30 s, and 68°C for 30 s, with a final extension step of 68°C for 2 min. Amplicons (~200 bp) were gel purified (QIAquick Gel Extraction Kit, QIAGEN) using a 2% agarose gel and quantified fluorometrically (dsDNA HS Assay Kit with a QuBit 2.0, Thermo Fisher Scientific). A second 40-μl PCR was then performed using 5 to 8 ng of each amplicon as template and 0.6 μM each of the P5 and P7 Nextera Index Kit primer (Illumina) to add Illumina adaptors and multiplexing indexes. The KAPA HiFi HotStart ReadyMixPCR Kit (Kapa Biosystems) was again used for amplification under the following cycling conditions: 95°C for 3 min, followed by 13 cycles of 98°C for 20 s, 55°C for 30 s, and 68°C for 30 s, with a final extension step of 68°C for 5 min. These ~300-bp amplicons, of the structure, P5 - i5 - N6 PCR tag - N20 plasmid barcode - N6 PCR tag - i7 - P7, were gel purified (QIAquick Gel Extraction Kit, Qiagen) using a 2% agarose gel and sent to IntegraGen (Evry, France) for qPCR-based quantification, equimolar pooling, and 100-nt paired-end HiSeq-4000 sequencing (Illumina). Preliminary quality filtering and demultiplexing (Integragen, Evry, France) resulted in ~18 M read pairs per time point per competition experiment, giving, for each point, an expected barcode coverage of ~200× and an expected mutant coverage of >14,000×.

HiSeq sequencing reads were processed using the mothur (version 1.37.6) ([52](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R52)) software package by the following steps: Forward and reverse reads were joined into contigs using mothur’s make.contigs command with the default parameters. Contigs were then quality filtered by size (<131 bp, as longer contigs imply forward and reverse reads could not be properly overlapped), number of uncalled bases (no Ns), and length of longest homopolymer stretch, an indicator of overall read quality (<9 bases). To remove most of the PCR duplicates arising from the second PCR [made possible by randomized hexamers introduced on each side of the barcode during the first PCR ([49](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R49))], if a particular full contig was present more than once, then only one copy was kept. Barcode sequences were then extracted after aligning contigs to the reference sequence (Needleman global alignment). Reads containing insertions or not generating a full alignment with the reference were discarded. Next, the mothur precluster algorithm was used to cluster barcode sequences differing by a hamming distance of 1, with the aim of correcting for PCR and sequencing errors, as described in the “Barcode promoter association” section. After degapping and reclustering barcode sequences to account for any alignment ambiguities resulting from small deletions, the number of occurrences of each true barcode was tabulated across all time points for each competition experiment. Last, a custom R (v.3.4.3) script was used to merge these barcode counts tables with the barcode promoter mutant dictionary generated in the “Barcode promoter association” section.

### Estimation of competitive fitness and epistasis
We found that competitive fitness was not constant over the course of competition, with, for example, reduced selection between _t_0 and _t_2 for certain inducer environments (figs. S3 and S4). By _t_6, a substantial number of lower fitness mutants begin to escape detection completely, and so to ensure the reliability of fitness estimates, we consider only the frequency changes between _t_2 and _t_4 (two time points). We begin by removing outlier barcodes associated to the WT genotype to avoid any systematic biases coming from inaccurate WT estimates. This was done by computing the log ratio of _t_4 to _t_2 counts for all WT barcodes and removing those giving values >1.5× the interquartile range above (below) the upper (lower) quartile. We also removed all barcodes giving <8 reads at _t_2 from our dataset. For every remaining mutant barcode, _i_, we then estimate its log fitness relative to the WT as

where _f__i_ is the frequency of a mutant barcode, ∑_f_wt is the total frequency of all WT barcodes, and _t_4 – _t_2 is the number of population generations between the two time points considered (~9). We now estimate log relative fitness of a mutant _g_, , as the median of that of its associated barcodes, . We use the median barcode fitness as a fitness estimate for each promoter genotype as a convenient way to filter out the many sources of error in a competition experiment (especially undetected mutations introduced during library construction, de novo mutations arising during competition, and barcode promoter misassignments due to PCR and sequencing errors) (fig. S3A). The number of eligible barcodes for each promoter genotype ranges from a few to thousands (exact numbers are provided in data S1). Some barcodes disappear from our sequencing sample by _t_4, and so are given an  of –Inf. In Env1 and Env3, for a very few genotypes, this is the case for most of their barcodes, and we identify these mutants as being less fit than the WT but cannot estimate total/marginal fitness effects or epistasis for them.

To estimate the precision of mutant fitness estimates, we used standard bootstrapping of the eligible mutant and WT barcodes (_n_ = 1000), each time computing the mutants’ fitness, , as the median fitness of their associated barcodes, . The same 1000 sets of randomly sampled WT barcodes were used as the references for all mutants. The bootstrap distributions were then used to determine significance (empirical 95% confidence) for non-neutrality of total () and marginal () fitness effects, nonzero epistasis, simple sign epistasis, and reciprocal sign epistasis, pairing bootstrap estimates by sampled WT barcode set when necessary.

The marginal fitness change induced by adding mutation _A_ to the genetic background _B_ is defined as , and epistasis between mutations _A_ and _B_ is defined as  ([13](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R13)).

### Growth curves to assess l-ribulose-5-phosphate toxicity
The absolute growth of monocultures of four different strains was monitored over a range of l-arabinose concentrations via their optical density. The strain’s phenotypes are summarized as AraAB+ AraD+, AraAB− AraD+, AraAB+ AraD−, and AraAB− AraD−. The AraAB+ phenotype is endowed by a (unbarcoded) plasmid like that used in the PLtetO-1-_araA_–PLlacO-1-_araB_ plasmid mutant library, with the WT PLtetO-1 and PLlacO-1 promoters. This was constructed exactly as for the mutant library, except that a single WT promoter–containing primer pair, oPtetWT-fwd/oPlacWT-rev (table S3), was used in place of the oPtetLib-fwd/oPlacLib-rev primer pool pair. The AraAB− phenotype indicates carriage of the library “backbone” plasmid, pKH1511c, which just lacks the PLtetO-1 and PLlacO-1 promoters and the _bsd_ cassette between them. The AraD+ host strain is the final library host strain, and the AraD− host is a derivative of this strain with _araD_ replaced by a _kan__R_ resistance cassette (table S4).

Precultures of each strain were grown overnight in M9 + 0.5% casamino acids [with streptomycin (50 μg/ml)] at 37°C and then diluted four times into the same fresh medium. Five microliters of these diluted precultures was used to inoculate 120 μl of assay media in a Costar flat-bottom 96-well plate well composed of M9 + 0.5% casamino acids + 20 ng/ml aTc and 30 μM IPTG (Env1 inducer concentrations) + l-arabinose (various concentrations) {with streptomycin (50 μg/ml)]. Mineral oil (25 μl) was then pipetted on top of each well to reduce evaporation. OD600nm was monitored during growth at 37°C with agitation by a Tecan Infinite 200 plate reader. Each strain/medium pair was replicated eight times within the 96-well plate.

### Phenotype fitness model
We consider a linear metabolic reaction path,

where _S_ is the substrate (l-arabinose) concentration. As shown in ([18](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R18), [19](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R19)), for _S_ and _Z_ fixed, the steady-state flux for nonsaturated enzymes and the intermediate concentration are respectively given by

where _A_ and _B_ are proportional to the maximum reaction rates provided by each enzyme, η is the inverse of the maximal flux, φmax, as imposed by the fixed pathway steps, and _D_ is a certain function of _S_ and equilibrium constants [see ([19](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R19)) for detailed equations]. We note that the flux, φ, is an increasing function of _A_ and _B_ and saturates at φmax for very efficient enzymes _A_ and _B_ or very high concentrations of them. However, at high fluxes, the hypothesis of unsaturated downstream enzymes breaks down, and a reaction step becomes limiting, such that the concentrations of metabolic intermediates may build up to toxic levels.

To account for such saturation, we extend the model above by considering the full reversible Michaelis-Menten (RMM) form for the step _C_ instead of its first-order approximation (similar reasoning applies for longer paths). At steady state, all reaction speeds must be equal, giving for the third step

where α, β, γ, δ are the RMM parameters for _C_. Equivalently, expressing _Y_ as a function of φ:

We could eliminate _Y_ by combining [Eqs. 2](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E2) and [4](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E4), _Z_ being fixed, and obtain an exact expression for φ. Note that [Eq. 1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E1) is recovered for δ = γ = 0, as this corresponds to the unsaturated case. In the general case, φ would still be an increasing function of _A_ and _B_ and saturate at a certain value, but its expression becomes more complicated.

Instead of using the full expression of φ, we report here an approximation with less parameters, which consistently recovers the monotonicity with _A_ and _B_ and the limit regimes for unsaturated and saturated downstream steps. For this, we simply keep [Eq. 1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E1) for the flux and set its saturation by the saturation of the reaction catalyzed by _C_, as obtained in the limit of very high _Y_ in [Eq. 4](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E4)

With this, [Eq. 4](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E4) becomes

where _P_ and _Q_ are functions of the fixed downstream enzyme properties and concentrations. We note in particular that _Y_ diverges when the flux becomes maximal, meaning that the downstream reaction is saturated, leading to an accumulation of _Y_.

We now assume fitness to be a function of flux and the toxic intermediate (l-ribulose-5-phosphate) concentration, _Y_, and that there exist constants _e_ and _f_ such that from [Eqs. 1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E1) to [5](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E5)

This expression can be further simplified by considering the low- and high-flux regimes:

For φ < < φmax, [Eq. 6](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E6) behaves as _F_ = − _fP_/φmax + _u_φ, with _u_ = _e_ − _f_(_Q_ + _P_/φmax)/φmax, the offset −_fP_/φmax being determined solely by properties of the fixed downstream enzyme, _C_. Thus, any fitness change due to mutations in _A_ and _B_ is of the form _u_φ.

For φ~φmax, the first term in [Eq. 6](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E6) remains finite, while the second with numerator _v_ = _f_(_P_ + _Q_φmax) diverges. Thus, replacing _e_ by _u_ as defined in the regime φ < < φmax has a negligible contribution.

Introducing a basal growth rate, ω, supplied by alternative nutrients in the medium (casamino acids), fitness is then well approximated by

In addition to flux and toxic metabolite concentration, gene expression burden can also contribute to fitness changes ([23](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R23), [55](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R55)–[57](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R57)). Following the observation that protein expression burden depends on metabolic state/growth rate ([58](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R58), [59](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R59)), we include an expression cost factor in which θ_A_ and θ_B_ describe the cost of increasing cellular enzyme activity, including potential contributions from both the amount of expression and the specific enzyme activity constants

This expression is considered valid only when both factors are positive. [Eqs. 1](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E1) and [8](https://www.science.org/doi/full/10.1126/sciadv.abb2236#E8) together define a fitness surface in the two-dimensional space of AraA and AraB activities, described by the six independent parameters ω, _u_, _v_, θ_A_, θ_B_, and η.

The entire model consists of 83 parameters: the 6 detailed immediately above, 5 defining the WT activity levels (AraA and AraB activities for the three inducer environments, with Env2 and Env3 having the same WT AraB activity, as both contained the same IPTG concentration), and 72 defining the relative impact of the single mutations (36 for each gene) on enzyme expression/activity. For a given parameter set, the fitness, _F_rel, of the 72 single mutants and 1296 double mutants was computed in each of the four environments, relative to the respective WT fitness. The 83-parameter model was fitted on 5447 data points corresponding to the computable set of relative fitnesses ([Fig. 2A](https://www.science.org/doi/full/10.1126/sciadv.abb2236#F2)) of the 1368 mutants measured in four different environments (Envs1–3 and the no-arabinose control environment).

The model was fit using multiple Monte Carlo Markov chains ([60](https://www.science.org/doi/full/10.1126/sciadv.abb2236#core-R60)). Parameters were generated randomly from uniform distributions, both initially and at each step of the chain for a randomly chosen parameter (bounds are provided in fig. S11A and data S2; bounds for expression effects of inducer concentration changes and a few mutations were guided by preliminary experimental expression measurements). A total of 800 chains, each of 300,000 steps, were simulated, and for each chain, the parameter set giving the best fit with measured fitness values was stored (residuals were weighted to give equal consideration overall to single and double mutants and were also normalized to the mean fitness effect in the environment from which they came). The distribution of goodness-of-fit values from the 800 chains was multimodal (i.e., convergence was not guaranteed), with ~5 to 10% of the chains achieving a best fit residing in the lowest peak. We take the best of all these parameter sets as the most likely fit, but the distributions of parameter values from the best 2.5% of chains are also provided in fig. S11A and data S2. When fitting on random subsets of the mutants, they were sampled with the constraint that all alleles of the two promoters are represented an equal number of times.

Several fitness function variations containing less parameters than the one presented in the main text were fit in the same way, and we conclude that the flux, toxicity, and gene expression burden must all be accounted for to explain the observed fitness and epistasis values (fig. S14).

### RT-qPCR expression measurements
Two separate single-mutant (unbarcoded) plasmid libraries, one for PLtetO-1-_araA_ and one for PLlacO-1-_araB_, were constructed exactly as for the complete mutant library, except for replacing the appropriate mutation-conferring primer pool (oPtetLib-fwd or oPlacLib-rev) in each case with the appropriate WT promoter–carrying primer (oPtetWT-fwd or oPlacWT-rev). These plasmid libraries were ultimately electroporated into the final library host strain following the protocol for the complete mutant library, plated on LB agar with streptomycin (50 μg/ml), and incubated overnight at 37°C. For each single-mutant library, 64 isolated colonies were randomly picked and used to inoculate liquid cultures (LB-str), which were grown overnight (37°C with agitation) and then miniprepped (QIAprep Spin Miniprep Kit, Qiagen). Plasmid DNA was Sanger sequenced (GATC) to obtain the sequence of the entire region containing the PLtetO-1--_bsd_--PLlacO-1 insert, and a sample of overnight cultures was stored in LB-glycerol (40%) at −80°C. The set of isolated single mutants (and four WT clones) with no unexpected mutations detected in the entire PLtetO-1--_bsd_--PLlacO-1 insert region was analyzed by RT-qPCR to measure expression of both _araA_ and _araB_ mRNAs. This set comprised 20 of 36 PLtetO-1-_araA_ single mutants (T2A.WT, T2C.WT, T2G.WT, G3A.WT, G3C.WT, A4C.WT, C5A.WT, C5G.WT, A6C.WT, A6T.WT, G7A.WT, G7C.WT, G7T.WT, T9A.WT, T9C.WT, A10G.WT, C11G.WT, C11T.WT, T12A.WT, T12G.WT) and 17 of 36 PLlacO-1-_araB_ single mutants (WT.T1A, WT.T2A, WT.T2G, WT.A4C, WT.C5A, WT.C5T, WT.A6C, WT.G7A, WT.G7C, WT.A8C, WT.A8G, WT.T9A, WT.A10C, WT.A10G, WT.C11A, WT.T12A, and WT.T12C).

For RNA extraction, precultures of each single-mutant strain and four independently isolated WT clones were grown overnight in 5 ml of M9 + 0.5% casamino acids [with streptomycin (50 μg/ml)] at 37°C with agitation, and 10 μl was taken to inoculate 5 ml of fresh M9 + 0.5% casamino acids + 20 ng/ml aTc and 30 μM IPTG [Env1 inducer concentrations] [with streptomycin (50 μg/ml)]. These cultures were then grown at 37°C with agitation until an OD600nm of 0.1 to 0.15 (BioMate 3S, Thermo Fisher Scientific), amounting to ~5 to 6 hours. At this point, cultures were pelleted by centrifugation (8000 rpm, 5 min), the supernatant was discarded, and the pellet was resuspended in 1 ml of TRIzol (Zymo Research). RNA was purified using the Direct-zol RNA Miniprep Kit (Zymo Research) following the manufacturer’s instructions including optional steps. RNA was eluted in 50 μl of deoxyribonuclease (DNAse)/ribonuclease (RNAse)–free water, and its concentration was measured spectrophotometrically (NanoDrop ND-1000). DNA was digested using a TURBO DNAse kit (Thermo Fisher Scientific) following the manufacturer’s instructions for concentrated samples.

RT-qPCRs were performed using the KAPA SYBR FAST qPCR Master Mix Kit (Kapa Biosystems) in 20-μl total volume with 0.2 μM each primer [validated primer pairs were oQPCR-araA-fwd/ oQPCR-araA-rev for _araA_ reactions and oQPCR-araB-fwd/ oQPCR-araB-rev for _araB_ reactions (table S3)]. Total RNA was normalized to 10 ng/μl. Reactions were performed in a LightCycler 480 (Roche) following the manufacturer’s recommendations. The entire experiment was performed on two separate occasions (two technical replicates of all samples on one occasion and three on the other), each time including negative controls for contamination (no RNA) and undigested DNA (no reverse transcriptase). Fold changes in expression relative to the WT were computed from the Δ_C_t between mutant and WT using the mean of the four WT clones as the reference each time.

### Statistical analyses
All statistical analyses were performed in R (v.3.4.3), and figures were made using the R packages ggplot2, cowplot, and rgl (for the three-dimensional plot). Bottom and top hinges of box plots correspond to the first and third quartiles. Center line is the median. Top and bottom whiskers extend from the hinges to the largest and lowest value no further than 1.5× the interquartile range away, respectively. Points outside this range are plotted individually.

## Acknowledgments
We thank A. Birgy, A. Decrulle, I. Matic, M. Deyell, A. Soler, and D. Mazel for providing genetic material and technical advice, A. Baron, J. Chatel, A. Bridier-Nahmias, and the CRI cytometry facility for technical assistance, and L.-M. Chevin, B. Gaut, E. Denamur, and C. Landry for the critical reading of the manuscript. MiSeq sequencing was performed using equipment provided by the Genetics Department of Bichat-Claude Bernard Hospital. **Funding:** This work was supported by the European Research Council under the European Union’s Seventh Framework Programme (ERC grant 310944 to O.T.). H.K. was supported by the Ecole Doctorale Frontières du Vivant (FdV)–Programme Bettencourt. **Author contributions:** H.K., P.N., and O.T. conceived the idea for the experiment. H.K. and O.T. designed the experiments. H.K., C.E., A.Co., A.Ch., M.M., G.G., and H.L.N. performed the experiments. H.K., P.N., and O.T. performed the analyses. H.K., P.N., and O.T. wrote the paper. **Competing interests:** The authors declare that they have no competing interests. **Data and materials availability:** All genotype fitness estimates, along with their bootstrap 95% CIs and the number of replicates used to compute them, are provided in data S1. Raw and processed sequencing data have been submitted to Gene Expression Omnibus (accession number GSE115725). Custom code used in this study is available from the authors upon request. All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to this paper may be requested from the authors.

## Supplementary Material
File(abb2236_data_s1.xlsx)

+ [Download](https://www.science.org/doi/suppl/10.1126/sciadv.abb2236/suppl_file/abb2236_data_s1.xlsx)
+ 355.22 KB

File(abb2236_data_s2.xlsx)

+ [Download](https://www.science.org/doi/suppl/10.1126/sciadv.abb2236/suppl_file/abb2236_data_s2.xlsx)
+ 22.52 KB

## REFERENCES AND NOTES
1

C. R. Scriver, P. J. Waters, Monogenic traits are not simple: Lessons from phenylketonuria. _Trends Genet._**15**, 267–272 (1999).

2

J. L. Badano, N. Katsanis, Beyond Mendel: An evolving view of human genetic disease transmission. _Nat. Rev. Genet._**3**, 779–789 (2002).

3

D. N. Cooper, M. Krawczak, C. Polychronakos, C. Tyler-Smith, H. Kehrer-Sawatzki, Where genotype is not predictive of phenotype: Towards an understanding of the molecular basis of reduced penetrance in human inherited disease. _Hum. Genet._**132**, 1077–1130 (2013).

4

C. A. Argmann, S. M. Houten, J. Zhu, E. E. Schadt, A next generation multiscale view of inborn errors of metabolism. _Cell Metab._**23**, 13–26 (2016).

5

T. A. Manolio, F. S. Collins, N. J. Cox, D. B. Goldstein, L. A. Hindorff, D. J. Hunter, M. I. McCarthy, E. M. Ramos, L. R. Cardon, A. Chakravarti, J. H. Cho, A. E. Guttmacher, A. Kong, L. Kruglyak, E. Mardis, C. N. Rotimi, M. Slatkin, D. Valle, A. S. Whittemore, M. Boehnke, A. G. Clark, E. E. Eichler, G. Gibson, J. L. Haines, T. F. C. Mackay, S. A. McCarroll, P. M. Visscher, Finding the missing heritability of complex diseases. _Nature_**461**, 747–753 (2009).

6

E. J. O’Brien, J. M. Monk, B. O. Palsson, Using Genome-scale Models to Predict Biological Capabilities. _Cell_**161**, 971–987 (2015).

7

L. Xu, B. Barker, Z. Gu, Dynamic epistasis for different alleles of the same gene. _Proc. Natl. Acad. Sci. U.S.A._**109**, 10420–10425 (2012).

8

H. Kemble, P. Nghe, O. Tenaillon, Recent insights into the genotype–phenotype relationship from massively parallel genetic assays. _Evol Appl._**12**, 1721–1742 (2019).

9

M.-J. Favé, F. C. Lamaze, D. Soave, A. Hodgkinson, H. Gauvin, V. Bruat, J.-C. Grenier, E. Gbeha, K. Skead, A. Smargiassi, M. Johnson, Y. Idaghdour, P. Awadalla, Gene-by-environment interactions in urban populations modulate risk phenotypes. _Nat. Commun._**9**, 827 (2018).

10

R. Schleif, Regulation of the L-arabinose operon of _Escherichia coli_. _Trends Genet._**16**, 559–565 (2000).

11

J. Ewald, M. Bartl, T. Dandekar, C. Kaleta, Optimality principles reveal a complex interplay of intermediate toxicity and kinetic efficiency in the regulation of prokaryotic metabolism. _PLOS Comput. Biol._**13**, e1005371 (2017).

12

E. Englesberg, R. L. Anderson, R. Weinberg, N. Lee, P. Hoffee, G. Huttenhauer, H. Boyer, L-arabinose-sensitive, L-ribulose 5-phosphate 4-epimerase-deficient mutants of _Escherichia coli_. _J. Bacteriol._**84**, 137–146 (1962).

13

J. B. Wolf, E. D. Brodie III, M. J. Wade, _Epistasis and the Evolutionary Process_ (Oxford Univ. Press, 2000), pp. 20–38.

14

J. A. G. M. de Visser, T. F. Cooper, S. F. Elena, The causes of epistasis. _Proc. Biol. Sci._**278**, 3617–3624 (2011).

15

D. Berger, E. Postma, Biased estimates of diminishing-returns epistasis? Empirical evidence revisited. _Genetics._**198**, 1417–1420 (2014).

16

A. I. Khan, D. M. Dinh, D. Schneider, R. E. Lenski, T. F. Cooper, Negative epistasis between beneficial mutations in an evolving bacterial population. _Science_**332**, 1193–1196 (2011).

17

H.-H. Chou, H.-C. Chiu, N. F. Delaney, D. Segrè, C. J. Marx, Diminishing returns epistasis among beneficial mutations decelerates adaptation. _Science_**332**, 1190–1192 (2011).

18

E. Szathmáry, Do deleterious mutations act synergistically? Metabolic Control Theory provides a partial answer. _Genetics_**133**, 127–132 (1993).

19

H. Kacser, J. A. Burns, The molecular basis of dominance. _Genetics_**97**, 639–666 (1981).

20

D. E. Dykhuizen, A. M. Dean, D. L. Hartl, Metabolic flux and fitness. _Genetics_**115**, 25–31 (1987).

21

A. G. Clark, Mutation-selection balance and metabolic control theory. _Genetics_**129**, 909–923 (1991).

22

L. Perfeito, S. Ghozzi, J. Berg, K. Schnetz, M. Lässig, Nonlinear fitness landscape of a molecular pathway. _PLOS Genet._**7**, e1002160 (2011).

23

H.-H. Chou, N. F. Delaney, J. A. Draghi, C. J. Marx, Mapping the fitness landscape of gene expression uncovers the cause of antagonism and sign epistasis between adaptive mutations. _PLOS Genet._**10**, e1004149 (2014).

24

F. Blanquart, G. Achaz, T. Bataillon, O. Tenaillon, Properties of selected mutations and genotypic landscapes under Fisher’s Geometric Model. _Evolution_**68**, 3537–3554 (2014).

25

T. N. Starr, J. W. Thornton, Epistasis in protein evolution. _Protein Sci._**25**, 1204–1218 (2016).

26

J. Otwinowski, I. Nemenman, Genotype to Phenotype Mapping and the Fitness Landscape of the _E. coli lac_ Promoter. _PLOS ONE._**8**, e61570 (2013).

27

L. Keren, J. Hausser, M. Lotan-Pompan, I. Vainberg Slutskin, H. Alisar, S. Kaminski, A. Weinberger, U. Alon, R. Milo, E. Segal, Massively parallel interrogation of the effects of gene expression levels on fitness. _Cell_**166**, 1282–1294.e18 (2016).

28

B. D. Towbin, Y. Korem, A. Bren, S. Doron, R. Sorek, U. Alon, Optimality and sub-optimality in a bacterial growth law. _Nat. Commun._**8**, 14123 (2017).

29

P. Nghe, M. Kogenaru, S. J. Tans, Sign epistasis caused by hierarchy within signalling cascades. _Nat. Commun._**9**, 1451 (2018).

30

G. Diss, B. Lehner, The genetic landscape of a physical interaction. _eLife_**7**, e32472 (2018).

31

S. Rozen, H. Skaletsky, Primer3 on the WWW for General Users and for Biologist Programmers. _Methods Mol. Biol._**132**, 365–386 (2000).

32

D. G. Gibson, L. Young, R.-Y. Chuang, J. C. Venter, C. A. Hutchison III, H. O. Smith, Enzymatic assembly of DNA molecules up to several hundred kilobases. _Nat. Methods_**6**, 343–345 (2009).

33

D. J. Leblanc, R. P. Mortlock, The metabolism of D-arabinose: Alternate kinases for the phosphorylation of D-ribulose in _Escherichia coli_ and _Aerobacter aerogenes_. _Arch. Biochem. Biophys._**150**, 774–781 (1972).

34

D. J. LeBlanc, R. P. Mortlock, Metabolism of D-Arabinose: A New Pathway in _Escherichia coli_. _J. Bacteriol._**106**, 90–96 (1971).

35

D. J. LeBlanc, R. P. Mortlock, Metabolism of D-Arabinose: Origin of a D- Ribulokinase Activity in _Escherichia coli_. _J. Bacteriol._**106**, 82–89 (1971).

36

G. Fritz, J. A. Megerle, S. A. Westermayer, D. Brick, R. Heermann, K. Jung, J. O. Rädler, U. Gerland, Single Cell Kinetics of Phenotypic Switching in the Arabinose Utilization System of _E. coli_. _PLOS ONE._**9**, e89532 (2014).

37

A. Khlebnikov, J. D. Keasling, Effect of _lacY_ Expression on Homogeneity of Induction from the Ptac and Ptrc Promoters by Natural and Synthetic Inducers. _Biotechnol. Prog._**18**, 672–674 (2002).

38

K. A. Datsenko, B. L. Wanner, One-step inactivation of chromosomal genes in _Escherichia coli_ K-12 using PCR products. _Proc. Natl. Acad. Sci. U.S.A._**97**, 6640–6645 (2000).

39

L. Katz, Selection of _AraB_ and _AraC_ Mutants of _Escherichia coli_ B/r by Resistance to Ribitol. _J. Bacteriol._**102**, 593–595 (1970).

40

G. A. Wray, The evolutionary significance of _cis_-regulatory mutations. _Nat. Rev. Genet._**8**, 206–216 (2007).

41

R. Lutz, H. Bujard, Independent and tight regulation of transcriptional units in _Escherichia coli_ via the LacR/O, the TetR/O and AraC/I1-I2 regulatory elements. _Nucleic Acids Res._**25**, 1203–1210 (1997).

42

R. K. Shultzaberger, D. S. Malashock, J. F. Kirsch, M. B. Eisen, The Fitness Landscapes of _cis_-Acting Binding Sites in Different Promoter and Environmental Contexts. _PLOS Genet._**6**, e1001042 (2010).

43

J. B. Kinney, A. Murugan, C. G. Callan Jr., E. C. Cox, Using deep sequencing to characterize the biophysical mechanism of a transcriptional regulatory sequence. _Proc. Natl. Acad. Sci. U.S.A._**107**, 9158–9163 (2010).

44

R. C. Brewster, D. L. Jones, R. Phillips, Tuning Promoter Strength through RNA Polymerase Binding Site Design in _Escherichia coli_. _PLOS Comput. Biol._**8**, e1002811 (2012).

45

L. Bintu, N. E. Buchler, H. G. Garcia, U. Gerland, T. Hwa, J. Kondev, R. Phillips, Transcriptional regulation by the numbers: Models. _Curr. Opin. Genet. Dev._**15**, 116–124 (2005).

46

M. Lagator, T. Paixão, N. H. Barton, J. P. Bollback, C. C. Guet, On the mechanistic nature of epistasis in a canonical _cis_-regulatory element. _eLife_**6**, e25192 (2017).

47

M. Kimura, A. Takatsuki, I. Yamaguchi, Blasticidin S deaminase gene from _Aspergillus terreus_ (_BSD_): A new drug resistance gene for transfection of mammalian cells. _Biochim. Biophys. Acta_**1219**, 653–659 (1994).

48

K. S. Sarkisyan, D. A. Bolotin, M. V. Meer, D. R. Usmanova, A. S. Mishin, G. V. Sharonov, D. N. Ivankov, N. G. Bozhanova, M. S. Baranov, O. Soylemez, N. S. Bogatyreva, P. K. Vlasov, E. S. Egorov, M. D. Logacheva, A. S. Kondrashov, D. M. Chudakov, E. V. Putintseva, I. Z. Mamedov, D. S. Tawfik, K. A. Lukyanov, F. A. Kondrashov, Local fitness landscape of the green fluorescent protein. _Nature_**533**, 397–401 (2016).

49

S. F. Levy, J. R. Blundell, S. Venkataram, D. A. Petrov, D. S. Fisher, G. Sherlock, Quantitative evolutionary dynamics using high-resolution lineage tracking. _Nature_**519**, 181–186 (2015).

50

M. Goldsmith, C. Kiss, A. R. M. Bradbury, D. S. Tawfik, Avoiding and controlling double transformation artifacts. _Protein Eng. Des. Sel._**20**, 315–318 (2007).

51

C. Pusch, H. Schmitt, N. Blin, Increased cloning efficiency by cycle restriction−ligation (CRL). _Tech. Tips Online._**2**, 35–37 (1997).

52

P. D. Schloss, S. L. Westcott, T. Ryabin, J. R. Hall, M. Hartmann, E. B. Hollister, R. A. Lesniewski, B. B. Oakley, D. H. Parks, C. J. Robinson, J. W. Sahl, B. Stres, G. G. Thallinger, D. J. Van Horn, C. F. Weber, Introducing mothur: Open-Source, Platform-Independent, Community-Supported Software for Describing and Comparing Microbial Communities. _Appl. Environ. Microbiol._**75**, 7537–7541 (2009).

53

A. Meyerhans, J.-P. Vartanian, S. Wain-Hobson, DNA recombination during PCR. _Nucleic Acids Res._**18**, 1687–1691 (1990).

54

R. T. Hietpas, J. D. Jensen, D. N. A. Bolon, Experimental illumination of a fitness landscape. _Proc. Natl. Acad. Sci.U.S.A._**108**, 7896–7901 (2011).

55

E. Dekel, U. Alon, Optimality and evolutionary tuning of the expression level of a protein. _Nature_**436**, 588–592 (2005).

56

T. N. Nguyen, Q. G. Phan, L. P. Duong, K. P. Bertrand, R. E. Lenski, Effects of carriage and expression of the Tn10 tetracycline-resistance operon on the fitness of Escherichia coli K12. _Mol. Biol. Evol._**6**, 213–225 (1989).

57

A. L. Koch, The protein burden of _lac_ operon products. _J. Mol. Evol._**19**, 455–462 (1983).

58

M. Kafri, E. Metzl-Raz, G. Jona, N. Barkai, The cost of protein production. _Cell Rep._**14**, 22–31 (2016).

59

M. S. Bienick, K. W. Young, J. R. Klesmith, E. E. Detwiler, K. J. Tomek, T. A. Whitehead, The Interrelationship between promoter strength, gene expression, and growth rate. _PLOS ONE._**9**, e109105 (2014).

60

S. Brroks, A. Gelman, G. L. Jones, X.-L. Meng, Handbook of Markov Chain Monte Carlo, in _Handbooks of Modern Statistical Methods_, G. Fitzmaurice, Ed. (Chapman and Hall/CRC, 2011).

61

E. Firnberg, M. Ostermeier, PFunkel: Efficient, expansive, user-defined mutagenesis. _PLOS ONE._**7**, e52031 (2012).

62

M. Gossen, H. Bujard, Tight control of gene expression in mammalian cells by tetracycline-responsive promoters. _Proc. Natl. Acad. Sci. U.S.A._**89**, 5547–5551 (1992).

63

A. Pant, D. Anbumani, S. Bag, O. Mehta, P. Kumar, S. Saxena, G. B. Nair, B. Das, Effect of LexA on Chromosomal Integration of CTXϕ in _Vibrio cholerae_. _J. Bacteriol._**198**, 268–275 (2016).

## Information & Authors
### Information
#### Published In
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710074316776-00174d76-c5e6-4d05-a9a9-45579f3d447e.jpeg)

Science Advances

Volume 6 | Issue 23  
June 2020

#### Copyright
Copyright © 2020 The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original U.S. Government Works. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC).

This is an open-access article distributed under the terms of the [Creative Commons Attribution-NonCommercial license](http://creativecommons.org/licenses/by-nc/4.0/), which permits use, distribution, and reproduction in any medium, so long as the resultant use is **not** for commercial advantage and provided the original work is properly cited.

#### Submission history
**Received**: 8 February 2020

**Accepted**: 31 March 2020

#### Permissions
#### Acknowledgments
We thank A. Birgy, A. Decrulle, I. Matic, M. Deyell, A. Soler, and D. Mazel for providing genetic material and technical advice, A. Baron, J. Chatel, A. Bridier-Nahmias, and the CRI cytometry facility for technical assistance, and L.-M. Chevin, B. Gaut, E. Denamur, and C. Landry for the critical reading of the manuscript. MiSeq sequencing was performed using equipment provided by the Genetics Department of Bichat-Claude Bernard Hospital. **Funding:** This work was supported by the European Research Council under the European Union’s Seventh Framework Programme (ERC grant 310944 to O.T.). H.K. was supported by the Ecole Doctorale Frontières du Vivant (FdV)–Programme Bettencourt. **Author contributions:** H.K., P.N., and O.T. conceived the idea for the experiment. H.K. and O.T. designed the experiments. H.K., C.E., A.Co., A.Ch., M.M., G.G., and H.L.N. performed the experiments. H.K., P.N., and O.T. performed the analyses. H.K., P.N., and O.T. wrote the paper. **Competing interests:** The authors declare that they have no competing interests. **Data and materials availability:** All genotype fitness estimates, along with their bootstrap 95% CIs and the number of replicates used to compute them, are provided in data S1. Raw and processed sequencing data have been submitted to Gene Expression Omnibus (accession number GSE115725). Custom code used in this study is available from the authors upon request. All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to this paper may be requested from the authors.

### Authors
#### Affiliations
##### AlejandroCouce
##### GregoryGautier
#### Funding Information
#### Notes
## Metrics & Citations
### Metrics
#### Article Usage 
#### Altmetrics 
### Citations
#### Cite as 
+ Harry Kemble _et al._

,

Flux, toxicity, and expression costs generate complex genetic interactions in a metabolic pathway._Sci. Adv._**6**,eabb2236(2020).DOI:[10.1126/sciadv.abb2236](https://doi.org/10.1126/sciadv.abb2236)

#### Export citation
Select the format you want to export the citation of this publication.

 	 

#### Cited by 
    - Florian Baier, 
    - Florence Gauye, 
    - Ruben Perez-Carrasco, 
    - Joshua L. Payne, 
    - Yolanda Schaerli, 
1. Environment-dependent epistasis increases phenotypic diversity in gene regulatory networks, Science Advances, **9**, 21, (2023).[/doi/10.1126/sciadv.adf1773](https://www.science.org/doi/10.1126/sciadv.adf1773)
    - Zaigao Tan, 
    - Jian Li, 
    - Jin Hou, 
    - Ramon Gonzalez, 
2. Designing artificial pathways for improving chemical production, Biotechnology Advances, **64**, (108119), (2023).[https://doi.org/10.1016/j.biotechadv.2023.108119](https://doi.org/10.1016/j.biotechadv.2023.108119)
    - Malvika Srivastava, 
    - Joshua L. Payne, 
3. On the incongruence of genotype-phenotype and fitness landscapes, PLOS Computational Biology, **18**, 9, (e1010524), (2022).[https://doi.org/10.1371/journal.pcbi.1010524](https://doi.org/10.1371/journal.pcbi.1010524)
    - Claudia Bank, 
4. Epistasis and Adaptation on Fitness Landscapes, Annual Review of Ecology, Evolution, and Systematics, **53**, 1, (457-479), (2022).[https://doi.org/10.1146/annurev-ecolsys-102320-112153](https://doi.org/10.1146/annurev-ecolsys-102320-112153)
    - Olivier Tenaillon, 
    - Ivan Matic, 
5. L’impact des mutations neutres sur l’évolvabilité et l’évolution des génomes, médecine/sciences, **38**, 10, (777-785), (2022).[https://doi.org/10.1051/medsci/2022122](https://doi.org/10.1051/medsci/2022122)
    - J. Z. Chen, 
    - D. M. Fowler, 
    - N. Tokuriki, 
6. Environmental selection and epistasis in an empirical phenotype–environment–fitness landscape, Nature Ecology & Evolution, **6**, 4, (427-438), (2022).[https://doi.org/10.1038/s41559-022-01675-5](https://doi.org/10.1038/s41559-022-01675-5)
    - Alaksh Choudhury, 
7. High-throughput navigation of the sequence space, New Frontiers and Applications of Synthetic Biology, (123-146), (2022).[https://doi.org/10.1016/B978-0-12-824469-2.00011-7](https://doi.org/10.1016/B978-0-12-824469-2.00011-7)
    - Sergey Kryazhimskiy, 
8. Emergence and propagation of epistasis in metabolic networks, eLife, **10**, (2021).[https://doi.org/10.7554/eLife.60200](https://doi.org/10.7554/eLife.60200)
    - Grant Kinsler, 
    - Kerry Geiler-Samerotte, 
    - Dmitri A Petrov, 
9. Fitness variation across subtle environmental perturbations reveals local modularity and global pleiotropy of adaptation, eLife, **9**, (2020).[https://doi.org/10.7554/eLife.61271](https://doi.org/10.7554/eLife.61271)
    - Kefu Liu, 
    - Juan Zhao, 
    - Chunnuan Chen, 
    - Jie Xu, 
    - Richard L. Bell, 
    - Frank S. Hall, 
    - George F. Koob, 
    - Nora D. Volkow, 
    - Hong Qing, 
    - Zhicheng Lin, 
10. Epistatic evidence for gender-dependant slow neurotransmission signalling in substance use disorders: PPP1R12B versus PPP1R1B, EBioMedicine, **61**, (103066), (2020).[https://doi.org/10.1016/j.ebiom.2020.103066](https://doi.org/10.1016/j.ebiom.2020.103066)

## View Options
### View options
#### PDF format
Download this article as a PDF file

[Download PDF](https://www.science.org/doi/pdf/10.1126/sciadv.abb2236?download=true)

## Tables
## References
### References
1

C. R. Scriver, P. J. Waters, Monogenic traits are not simple: Lessons from phenylketonuria. _Trends Genet._**15**, 267–272 (1999).

2

J. L. Badano, N. Katsanis, Beyond Mendel: An evolving view of human genetic disease transmission. _Nat. Rev. Genet._**3**, 779–789 (2002).

3

D. N. Cooper, M. Krawczak, C. Polychronakos, C. Tyler-Smith, H. Kehrer-Sawatzki, Where genotype is not predictive of phenotype: Towards an understanding of the molecular basis of reduced penetrance in human inherited disease. _Hum. Genet._**132**, 1077–1130 (2013).

4

C. A. Argmann, S. M. Houten, J. Zhu, E. E. Schadt, A next generation multiscale view of inborn errors of metabolism. _Cell Metab._**23**, 13–26 (2016).

5

T. A. Manolio, F. S. Collins, N. J. Cox, D. B. Goldstein, L. A. Hindorff, D. J. Hunter, M. I. McCarthy, E. M. Ramos, L. R. Cardon, A. Chakravarti, J. H. Cho, A. E. Guttmacher, A. Kong, L. Kruglyak, E. Mardis, C. N. Rotimi, M. Slatkin, D. Valle, A. S. Whittemore, M. Boehnke, A. G. Clark, E. E. Eichler, G. Gibson, J. L. Haines, T. F. C. Mackay, S. A. McCarroll, P. M. Visscher, Finding the missing heritability of complex diseases. _Nature_**461**, 747–753 (2009).

6

E. J. O’Brien, J. M. Monk, B. O. Palsson, Using Genome-scale Models to Predict Biological Capabilities. _Cell_**161**, 971–987 (2015).

7

L. Xu, B. Barker, Z. Gu, Dynamic epistasis for different alleles of the same gene. _Proc. Natl. Acad. Sci. U.S.A._**109**, 10420–10425 (2012).

8

H. Kemble, P. Nghe, O. Tenaillon, Recent insights into the genotype–phenotype relationship from massively parallel genetic assays. _Evol Appl._**12**, 1721–1742 (2019).

9

M.-J. Favé, F. C. Lamaze, D. Soave, A. Hodgkinson, H. Gauvin, V. Bruat, J.-C. Grenier, E. Gbeha, K. Skead, A. Smargiassi, M. Johnson, Y. Idaghdour, P. Awadalla, Gene-by-environment interactions in urban populations modulate risk phenotypes. _Nat. Commun._**9**, 827 (2018).

10

R. Schleif, Regulation of the L-arabinose operon of _Escherichia coli_. _Trends Genet._**16**, 559–565 (2000).

11

J. Ewald, M. Bartl, T. Dandekar, C. Kaleta, Optimality principles reveal a complex interplay of intermediate toxicity and kinetic efficiency in the regulation of prokaryotic metabolism. _PLOS Comput. Biol._**13**, e1005371 (2017).

12

E. Englesberg, R. L. Anderson, R. Weinberg, N. Lee, P. Hoffee, G. Huttenhauer, H. Boyer, L-arabinose-sensitive, L-ribulose 5-phosphate 4-epimerase-deficient mutants of _Escherichia coli_. _J. Bacteriol._**84**, 137–146 (1962).

13

J. B. Wolf, E. D. Brodie III, M. J. Wade, _Epistasis and the Evolutionary Process_ (Oxford Univ. Press, 2000), pp. 20–38.

14

J. A. G. M. de Visser, T. F. Cooper, S. F. Elena, The causes of epistasis. _Proc. Biol. Sci._**278**, 3617–3624 (2011).

15

D. Berger, E. Postma, Biased estimates of diminishing-returns epistasis? Empirical evidence revisited. _Genetics._**198**, 1417–1420 (2014).

16

A. I. Khan, D. M. Dinh, D. Schneider, R. E. Lenski, T. F. Cooper, Negative epistasis between beneficial mutations in an evolving bacterial population. _Science_**332**, 1193–1196 (2011).

17

H.-H. Chou, H.-C. Chiu, N. F. Delaney, D. Segrè, C. J. Marx, Diminishing returns epistasis among beneficial mutations decelerates adaptation. _Science_**332**, 1190–1192 (2011).

18

E. Szathmáry, Do deleterious mutations act synergistically? Metabolic Control Theory provides a partial answer. _Genetics_**133**, 127–132 (1993).

19

H. Kacser, J. A. Burns, The molecular basis of dominance. _Genetics_**97**, 639–666 (1981).

20

D. E. Dykhuizen, A. M. Dean, D. L. Hartl, Metabolic flux and fitness. _Genetics_**115**, 25–31 (1987).

21

A. G. Clark, Mutation-selection balance and metabolic control theory. _Genetics_**129**, 909–923 (1991).

22

L. Perfeito, S. Ghozzi, J. Berg, K. Schnetz, M. Lässig, Nonlinear fitness landscape of a molecular pathway. _PLOS Genet._**7**, e1002160 (2011).

23

H.-H. Chou, N. F. Delaney, J. A. Draghi, C. J. Marx, Mapping the fitness landscape of gene expression uncovers the cause of antagonism and sign epistasis between adaptive mutations. _PLOS Genet._**10**, e1004149 (2014).

24

F. Blanquart, G. Achaz, T. Bataillon, O. Tenaillon, Properties of selected mutations and genotypic landscapes under Fisher’s Geometric Model. _Evolution_**68**, 3537–3554 (2014).

25

T. N. Starr, J. W. Thornton, Epistasis in protein evolution. _Protein Sci._**25**, 1204–1218 (2016).

26

J. Otwinowski, I. Nemenman, Genotype to Phenotype Mapping and the Fitness Landscape of the _E. coli lac_ Promoter. _PLOS ONE._**8**, e61570 (2013).

27

L. Keren, J. Hausser, M. Lotan-Pompan, I. Vainberg Slutskin, H. Alisar, S. Kaminski, A. Weinberger, U. Alon, R. Milo, E. Segal, Massively parallel interrogation of the effects of gene expression levels on fitness. _Cell_**166**, 1282–1294.e18 (2016).

28

B. D. Towbin, Y. Korem, A. Bren, S. Doron, R. Sorek, U. Alon, Optimality and sub-optimality in a bacterial growth law. _Nat. Commun._**8**, 14123 (2017).

29

P. Nghe, M. Kogenaru, S. J. Tans, Sign epistasis caused by hierarchy within signalling cascades. _Nat. Commun._**9**, 1451 (2018).

30

G. Diss, B. Lehner, The genetic landscape of a physical interaction. _eLife_**7**, e32472 (2018).

31

S. Rozen, H. Skaletsky, Primer3 on the WWW for General Users and for Biologist Programmers. _Methods Mol. Biol._**132**, 365–386 (2000).

32

D. G. Gibson, L. Young, R.-Y. Chuang, J. C. Venter, C. A. Hutchison III, H. O. Smith, Enzymatic assembly of DNA molecules up to several hundred kilobases. _Nat. Methods_**6**, 343–345 (2009).

33

D. J. Leblanc, R. P. Mortlock, The metabolism of D-arabinose: Alternate kinases for the phosphorylation of D-ribulose in _Escherichia coli_ and _Aerobacter aerogenes_. _Arch. Biochem. Biophys._**150**, 774–781 (1972).

34

D. J. LeBlanc, R. P. Mortlock, Metabolism of D-Arabinose: A New Pathway in _Escherichia coli_. _J. Bacteriol._**106**, 90–96 (1971).

35

D. J. LeBlanc, R. P. Mortlock, Metabolism of D-Arabinose: Origin of a D- Ribulokinase Activity in _Escherichia coli_. _J. Bacteriol._**106**, 82–89 (1971).

36

G. Fritz, J. A. Megerle, S. A. Westermayer, D. Brick, R. Heermann, K. Jung, J. O. Rädler, U. Gerland, Single Cell Kinetics of Phenotypic Switching in the Arabinose Utilization System of _E. coli_. _PLOS ONE._**9**, e89532 (2014).

37

A. Khlebnikov, J. D. Keasling, Effect of _lacY_ Expression on Homogeneity of Induction from the Ptac and Ptrc Promoters by Natural and Synthetic Inducers. _Biotechnol. Prog._**18**, 672–674 (2002).

38

K. A. Datsenko, B. L. Wanner, One-step inactivation of chromosomal genes in _Escherichia coli_ K-12 using PCR products. _Proc. Natl. Acad. Sci. U.S.A._**97**, 6640–6645 (2000).

39

L. Katz, Selection of _AraB_ and _AraC_ Mutants of _Escherichia coli_ B/r by Resistance to Ribitol. _J. Bacteriol._**102**, 593–595 (1970).

40

G. A. Wray, The evolutionary significance of _cis_-regulatory mutations. _Nat. Rev. Genet._**8**, 206–216 (2007).

41

R. Lutz, H. Bujard, Independent and tight regulation of transcriptional units in _Escherichia coli_ via the LacR/O, the TetR/O and AraC/I1-I2 regulatory elements. _Nucleic Acids Res._**25**, 1203–1210 (1997).

42

R. K. Shultzaberger, D. S. Malashock, J. F. Kirsch, M. B. Eisen, The Fitness Landscapes of _cis_-Acting Binding Sites in Different Promoter and Environmental Contexts. _PLOS Genet._**6**, e1001042 (2010).

43

J. B. Kinney, A. Murugan, C. G. Callan Jr., E. C. Cox, Using deep sequencing to characterize the biophysical mechanism of a transcriptional regulatory sequence. _Proc. Natl. Acad. Sci. U.S.A._**107**, 9158–9163 (2010).

44

R. C. Brewster, D. L. Jones, R. Phillips, Tuning Promoter Strength through RNA Polymerase Binding Site Design in _Escherichia coli_. _PLOS Comput. Biol._**8**, e1002811 (2012).

45

L. Bintu, N. E. Buchler, H. G. Garcia, U. Gerland, T. Hwa, J. Kondev, R. Phillips, Transcriptional regulation by the numbers: Models. _Curr. Opin. Genet. Dev._**15**, 116–124 (2005).

46

M. Lagator, T. Paixão, N. H. Barton, J. P. Bollback, C. C. Guet, On the mechanistic nature of epistasis in a canonical _cis_-regulatory element. _eLife_**6**, e25192 (2017).

47

M. Kimura, A. Takatsuki, I. Yamaguchi, Blasticidin S deaminase gene from _Aspergillus terreus_ (_BSD_): A new drug resistance gene for transfection of mammalian cells. _Biochim. Biophys. Acta_**1219**, 653–659 (1994).

48

K. S. Sarkisyan, D. A. Bolotin, M. V. Meer, D. R. Usmanova, A. S. Mishin, G. V. Sharonov, D. N. Ivankov, N. G. Bozhanova, M. S. Baranov, O. Soylemez, N. S. Bogatyreva, P. K. Vlasov, E. S. Egorov, M. D. Logacheva, A. S. Kondrashov, D. M. Chudakov, E. V. Putintseva, I. Z. Mamedov, D. S. Tawfik, K. A. Lukyanov, F. A. Kondrashov, Local fitness landscape of the green fluorescent protein. _Nature_**533**, 397–401 (2016).

49

S. F. Levy, J. R. Blundell, S. Venkataram, D. A. Petrov, D. S. Fisher, G. Sherlock, Quantitative evolutionary dynamics using high-resolution lineage tracking. _Nature_**519**, 181–186 (2015).

50

M. Goldsmith, C. Kiss, A. R. M. Bradbury, D. S. Tawfik, Avoiding and controlling double transformation artifacts. _Protein Eng. Des. Sel._**20**, 315–318 (2007).

51

C. Pusch, H. Schmitt, N. Blin, Increased cloning efficiency by cycle restriction−ligation (CRL). _Tech. Tips Online._**2**, 35–37 (1997).

52

P. D. Schloss, S. L. Westcott, T. Ryabin, J. R. Hall, M. Hartmann, E. B. Hollister, R. A. Lesniewski, B. B. Oakley, D. H. Parks, C. J. Robinson, J. W. Sahl, B. Stres, G. G. Thallinger, D. J. Van Horn, C. F. Weber, Introducing mothur: Open-Source, Platform-Independent, Community-Supported Software for Describing and Comparing Microbial Communities. _Appl. Environ. Microbiol._**75**, 7537–7541 (2009).

53

A. Meyerhans, J.-P. Vartanian, S. Wain-Hobson, DNA recombination during PCR. _Nucleic Acids Res._**18**, 1687–1691 (1990).

54

R. T. Hietpas, J. D. Jensen, D. N. A. Bolon, Experimental illumination of a fitness landscape. _Proc. Natl. Acad. Sci.U.S.A._**108**, 7896–7901 (2011).

55

E. Dekel, U. Alon, Optimality and evolutionary tuning of the expression level of a protein. _Nature_**436**, 588–592 (2005).

56

T. N. Nguyen, Q. G. Phan, L. P. Duong, K. P. Bertrand, R. E. Lenski, Effects of carriage and expression of the Tn10 tetracycline-resistance operon on the fitness of Escherichia coli K12. _Mol. Biol. Evol._**6**, 213–225 (1989).

57

A. L. Koch, The protein burden of _lac_ operon products. _J. Mol. Evol._**19**, 455–462 (1983).

58

M. Kafri, E. Metzl-Raz, G. Jona, N. Barkai, The cost of protein production. _Cell Rep._**14**, 22–31 (2016).

59

M. S. Bienick, K. W. Young, J. R. Klesmith, E. E. Detwiler, K. J. Tomek, T. A. Whitehead, The Interrelationship between promoter strength, gene expression, and growth rate. _PLOS ONE._**9**, e109105 (2014).

60

S. Brroks, A. Gelman, G. L. Jones, X.-L. Meng, Handbook of Markov Chain Monte Carlo, in _Handbooks of Modern Statistical Methods_, G. Fitzmaurice, Ed. (Chapman and Hall/CRC, 2011).

61

E. Firnberg, M. Ostermeier, PFunkel: Efficient, expansive, user-defined mutagenesis. _PLOS ONE._**7**, e52031 (2012).

62

M. Gossen, H. Bujard, Tight control of gene expression in mammalian cells by tetracycline-responsive promoters. _Proc. Natl. Acad. Sci. U.S.A._**89**, 5547–5551 (1992).

63

A. Pant, D. Anbumani, S. Bag, O. Mehta, P. Kumar, S. Saxena, G. B. Nair, B. Das, Effect of LexA on Chromosomal Integration of CTXϕ in _Vibrio cholerae_. _J. Bacteriol._**198**, 268–275 (2016).  


> 来自: [Flux, toxicity, and expression costs generate complex genetic interactions in a metabolic pathway | Science Advances](https://www.science.org/doi/full/10.1126/sciadv.abb2236)
>

