[https://doi.org/10.1074/jbc.M111.274050](https://doi.org/10.1074/jbc.M111.274050)

Carbonell, P.; Lecointre, G.; Faulon, J.-L. Origins of Specificity and Promiscuity in Metabolic Networks. _J Biol Chem_**2011**, _286_ (51), 43994–44004. [https://doi.org/10.1074/jbc.M111.274050](https://doi.org/10.1074/jbc.M111.274050).

How [enzymes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme) have evolved to their present form is linked to the question of how pathways emerged and evolved into extant [metabolic networks](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/metabolic-network). To investigate this mechanism, we have explored the chemical diversity present in a largely unbiased data set of catalytic reactions processed by modern enzymes across the [tree of life](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/tree-of-life). In order to get a quantitative estimate of enzyme chemical diversity, we <font style="background-color:#FBDE28;">measure enzyme multispecificity or promiscuity using the reaction molecular signatures</font>. 

+ Our main finding is that reactions that are catalyzed by a highly specific enzyme are shared by poorly divergent species, suggesting a later emergence of this function during evolution. 
+ In contrast, reactions that are catalyzed by highly promiscuous enzymes are more likely to appear uniformly distributed across species in the tree of life. 

From a functional point of view, promiscuous enzymes are mainly involved in amino acid and <font style="background-color:#FBDE28;">lipid metabolisms</font>, which might be associated with the earliest form of biochemical reactions. In this way, results presented in this paper might assist us with the identification of primeval promiscuous catalytic functions contributing to life's minimal metabolism.

+ [Previous](https://www.sciencedirect.com/science/article/pii/S0021925820685167)
+ [Next](https://www.sciencedirect.com/science/article/pii/S002192582068485X)

Bioinformatics

Computational Biology

Computer Modeling

Evolution

Metabolism

## Introduction
Recent [phylogenetic](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/phylogeny) studies of cellular metabolism suggest a core set of highly conserved [enzymes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme) involved in amino acid, energy, carbohydrate, and lipid metabolism, which is likely to be associated with the ancestral form of the extant [metabolic network](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/metabolic-network) ([1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib1), [2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib2)). However, the essentiality of this core for life and the existence of a universally essential minimal gene set are currently under debate, because essential genes show a diverse overall organization across multiple organisms in metabolic maps ([3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib3)). This diversity might be explained, in part, by the role that enzyme promiscuity plays, providing a common background level of metabolism to the organisms ([4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib4)). Thus, how enzymes have evolved to their present form in organisms appears to be linked to the question of how metabolic pathways emerged and configured extant metabolic networks ([5](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib5)). 

In fact, although many enzyme families and superfamilies sharing structural and functional features have been identified, it has been recognized that distant evolutionary relationships are expected to be difficult to identify solely from global sequence comparison ([6](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib6)). Here, we propose to extend previous studies of metabolic network evolution ([7](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib7), [8](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib8), [9](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib9), [10](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib10)) by studying the evolutionary aspect of enzyme promiscuity (_i.e._ of the latent capabilities of enzymes to broaden their specificity to substrates or to process diverse biochemical reactions) ([11](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib11), [12](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib12)).

### retrograde vs patchwork evolution model
An early theory on how metabolic pathways have evolved was the retrograde evolution model, proposed by Horowitz ([13](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib13)), which states that the earliest [biosynthetic pathways](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/anabolism) evolved in a backward direction in response to depletion of substrates from the environment. In the retrograde model, the recruitment of an enzyme capable of synthesizing the depleted substrate from some other available precursor brings a selective advantage to the organism. 

In contrast, the patchwork evolution model originally proposed by Jensen ([14](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib14)) states that primitive enzymes possessed broad [substrate specificity](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-specificity) and that [gene duplication](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/gene-duplication) and divergence led to the specialized and increased metabolic efficiency observed in extant enzymes. 

Both models might be interpreted in the context of a similar evolutionary mechanism, driven either by selective pressure of the substrate in the retrograde model or by the chemical reaction in the patchwork model ([7](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib7)). A current view assumes that although the retrograde model could have played a role on the evolution of the ancestral form of the metabolic network, the patchwork evolution model is the predominant player in modern metabolic enzyme evolution ([9](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib9), [15](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib15)).

As has been observed by Tawfik's group ([16](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib16)), an intriguing aspect of evolved enzymes is that their promiscuous activities or latent functions can usually be enhanced and diversified without impairing the traditional function. There are, however, some practical limits in the efficiency that modern enzymes have achieved, as if they had evolved and become specialized up to the required level in the cell to perform their task ([17](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib17)), suggesting that keeping some level of latent promiscuous capabilities might be a selective advantage allowing adaptation to environmental pressure ([18](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib18)). In many cases, such <font style="background-color:#FBDE28;">enhancement of latent catalytic activities</font> does not seem to trade off with parallel decreases in the original function, in contradiction with the commonly accepted assumption that broad substrate acceptance generally comes at the price of low reaction [turnover numbers](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/turnover-number) ([19](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib19)). Mutations in enzymes that are neutral with respect to the protein's primary [biological function](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/biological-functions) can provide in many cases a way to induce substantial changes in other promiscuous functions present in the enzyme at lower efficiency levels ([20](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib20)). Subsequent gene duplications might allow [natural selection](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/natural-selection) to transform one of the genes into a protein with high efficiency for the new functional role ([21](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib21)).

Furthermore, enzyme evolution might be influenced by the<font style="background-color:#FBDE28;"> structure and function of the metabolic network</font>. For instance, enzymes in central parts of the metabolism, such as the [tricarboxylic acid cycle](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/citric-acid-cycle), evolve more slowly than less connected enzymes ([22](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib22)). Also, enzymes carrying high [metabolic fluxes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/metabolic-flux) under natural biological conditions experience higher evolutionary constraints. Genes encoding enzymes with high connectivity and high metabolic flux have higher chances to retain duplicates in evolution. Similarly, highly expressed enzymes have been observed to evolve slowly ([23](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib23)). Finally, another mechanism that we want to examine in this study is how the environment influences enzyme evolution. The presence of substrates plays a pivotal role in determining whether latent catalytic abilities become manifest in a novel enzyme ([24](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib24)), as has been observed in recent years with the emergence of enzymes that degrade novel synthetic chemicals and with the alarming evolution of drug resistance.

In our study of origins of enzyme multispecificity and promiscuity, we plan to overcome the limitations of sequence comparison studies by performing a comparison between enzyme promiscuity and phylogenetic diversity of species. 

:::info
<font style="background-color:#FBDE28;">Our hypothesis is that </font>

+ if promiscuous enzymes are more evolvable (_i.e._ they have a greater capacity to evolve, they should be present in distant species, and their corresponding common ancestors should be deeper in the tree of life). 
+ Conversely, non-promiscuous enzymes, which exhibit specific catalytic activities, might be found within smaller groups of more closely related species. 

:::

Nevertheless, our approach based on enzyme promiscuity might also be prone to investigation bias, since a well known observed fact is that the number of identified cross-reactants increases exponentially with the number of tested ligands ([18](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib18)). Therefore, a rigorous definition of enzyme promiscuity needs to be introduced and applied to an unbiased data set. The term “enzyme promiscuity,” however, has been used with different interpretations. Several authors reserve the term “promiscuity” in order to describe [enzyme activities](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-activity) other than their native function ([18](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib18)), a sort of adventitious secondary activity ([25](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib25)), which might have appeared accidentally or have been induced ([17](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib17)), whereas “multispecificity” is used to designate enzymes with the ability to transform a whole range of substrates ([18](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib18)). 

:::info
A further classification of enzyme promiscuity distinguishes between three different forms ([17](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib17)): 

+ enzyme condition promiscuity (other reaction conditions than the natural one)
+ [enzyme substrate](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-substrate) promiscuity (broad substrate specificity)
+ enzyme catalytic promiscuity (different chemical transformations). 

:::

To consider two chemical transformations as different, the functional groups involved and/or the transition states of the two reactions must differ ([26](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib26)).

In order to clarify these concepts, it is necessary to define a quantitative measure of the levels of enzyme promiscuity. 

+ Nath and Atkins ([21](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib21)) introduced a quantitative index of promiscuity, which quantifies the degree of similarity between <font style="background-color:#FBDE28;">different substrates of the same enzyme</font>. This index, however, does not take into account the chemical transformation, and it is, therefore, more suitable for measuring cross-reactivity between multispecific enzymes. 
+ Khersonsky and Tawfik ([18](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib18)) propose the use of <font style="background-color:#FBDE28;">EC number comparison</font> in order to assess the degree of promiscuity. Multispecific enzymes should differ at most in the fourth digit, whereas differences in the third, second, or even first digits would refer to catalytic promiscuity. The authors, however, pointed out some cases where EC numbers of even the first digit are misleading, because they actually refer to transformations with considerable similarity in the chemistry of catalysis. 
+ In order to circumvent the limitations of these definitions, we propose here to use a quantitative measure of similarity between reactions based on <font style="background-color:#FBDE28;">molecular signatures</font>, a representation of the molecular graph ([27](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib27)), which provides a consistent way to characterize enzyme multispecificity and promiscuity ([28](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib28)).

## EXPERIMENTAL PROCEDURES
### Data
We downloaded from the KEGG (release version 50) ([29](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib29)) and [MetaCyc](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/metacyc) (release version 15.1) ([30](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib30)) databases the list of proteins with annotated catalytic activity. Enzymes annotated with more than one EC number, a basic definition of enzyme promiscuity, <font style="background-color:#FBDE28;">correspond to ∼2% of the total </font>([Table 1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl1)). Annotations corresponding to partial EC numbers were not considered in the study. Redundancy in the KEGG database was removed within each set at a threshold of 90% of sequence similarity. In our study, we were interested in those sequences from the data set belonging to organisms in the reference [tree](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/tree) of life (see definition below). Additionally, in order to apply our analysis of chemical similarity, the information in KEGG about the biochemical reactions that catalyze the enzymes was collected. Finally, we obtained 152,041 enzyme sequences from KEGG verifying simultaneously these specifications ([Table 1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl1)). In the case of MetaCyc, we were able to identify 1080 entries verifying these specifications ([Table 1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl1)).

TABLE 1. Data set of enzyme entries, organisms, and their catalytic activities

For each database, values are given for enzymes belonging to organisms in the tree of life and for total enzymes (in parentheses).

| Empty Cell | Subset (total data set) from KEGG with annotated reactions and organisms in the tree of life | Subset (total data set) from MetaCyc with annotated reactions and organisms in the tree of life |
| --- | --- | --- |
| Total entries | 152,041 (404,205) | 1080 (7287) |
| Non-promiscuous enzymes | 148,594 (394,732) | 927 (6465) |
| Promiscuous enzymes | 3447 (9293) | 153 (822) |
| Total EC numbers | 770 (2039) | 766 (2018) |
| Total organisms | 356 (1096) | 120 (1130) |


We used as the reference tree of life the [phylogenetic tree](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/phylogenetic-tree) reconstructed by Ciccarelli _et al._ ([31](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib31)) from a multiple alignment of 31 [DNA](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/dna) orthologs occurring in 191 organisms with sequenced genome. In this set, data were curated by these authors in order to avoid horizontal gene transfer events, and phylogenetic inferences were made by maximum likelihood and the JTT substitution matrix by using PHYML ([32](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib32)). In our study, we grouped together branches of the same genus in this reference tree, resulting in 108 species (see [supplemental Table S1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)). The apparent speed of sequence evolution can be measured as the cumulative branch length distance from a species to the root, being the root placed through automatic midpoint rooting. The choice of such a rooting is not a problem for the purpose of our study because midpoint rooting falls somewhere between the three domains, and our results are actually based on what happens within each of them. In the present paper, we refer only to relative divergence times (_i.e._ the ordering of divergence times of taxonomic groups), not to absolute ones. Divergence times of broad taxonomic groups, when considered, are those given in Ref. [33](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib33).

To link enzyme and phylogenetic information, organisms in the databases were mapped into the tree of life. Different strains from the same species were assigned to the same organism. When several organisms were matched to the same taxon in the tree of life, values were averaged. We were able to assign 108 species in the tree of life to 356 organisms in KEGG (33%) and 120 in MetaCyc (11%) (See [Table 2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl2) and [supplemental Tables S1 and S2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10) for details).

TABLE 2. Number of species by taxonomic group

Shown are the numbers of species contained in different taxonomic groups in the reference tree of life.

| Taxonomic group | Species in taxonomic group |
| --- | --- |
| Archaea | Crenarchaeota: 3 |
| | Euryarchaeota: 9 |
| | Nanoarchaeota: 1 |
| Eubacteria | Actinobacteria: 5 |
| | Bacteroidetes/Chlorobi group: 4 |
| | Chlamydiae/Verrucomicrobia group: 2 |
| | Chlroflexi: 1 |
| | Cyanobacteria: 4 |
| | Deinococcus-Thermus: 2 |
| | Firmicutes: 10 |
| | Fusobacteria: 1 |
| | Planctomycetes: 2 |
| | Proteobacteria: 35 |
| | Spirochaetes: 3 |
| | Tenericutes: 3 |
| | Thermotogae: 1 |
| Eukaryota | Alveolata: 4 |
| | Amoebozoa: 1 |
| | Animals: 10 |
| | Excavobionta: 2 |
| | Fungi: 3 |
| | Plants (_i.e._ Chlorobionta): 3 |


### Evaluation of Enzyme Promiscuity
The term “enzyme promiscuity” is used throughout to refer to the general concept of the ability of an enzyme to process multiple substrates or reactions. Furthermore, we introduce more specific definitions of enzyme promiscuity in [Table 3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl3) at the enzyme level by looking at the chemical diversity of the reactions that the enzyme can process, the enzyme chemical diversity, and at the catalytic activity level by looking at the list of reactions that can be simultaneously processed by enzymes annotated for this activity, the enzyme latent promiscuity.

First, we evaluated enzyme chemical diversity by computing the average chemical dissimilarity between the reactions in the list of biochemical reactions annotated for the enzymes in the databases. Chemical similarity was evaluated for pairs of reactions _R__A_ and _R__B_ using the well known Tanimoto coefficient _T__c_(_R__A_,_R__B_), a number ranging between 0 (dissimilar reactions) and 1 (identical reactions). In this study, _T__c_ was evaluated by using the molecular signature of the reactions ([28](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib28)). Molecular signatures are vectors whose components correspond to canonical representations of the graph associated with molecular structures ([27](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib27)). If _G_ = (_V_,_E_) is a molecular graph, where vertices _V_ correspond to atoms and edges _E_ correspond to bonds, then the molecular signature of _G_ is given by [Equation 1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#FD1), (Eq. 1)σ(G)=∑x∈Vσ(x) where σ(_x_) represents the atomic signature of _G_ rooted at atom _x_. The molecular signature of reaction _R_, REACTION 1s1S1+…+snSn→p1P1+…+pmPm where _s__i_ and _p__i_ are the stoichiometric coefficients of substrates _S__i_ and products _P__j_, is defined by the difference between the signatures of products and substrates, (Eq. 2)σ(R)=∑j=1mpjσ(Pj)−∑i=1npiσ(Si) Based on the previous definition, reaction chemical similarity between the pair of reactions _R__A_ and _R__B_ is given by [Equation 3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#FD3), (Eq. 3)Tc(RA,RB)=‖σ(RA)⋅σ(RB)‖‖σ(RA)‖2+‖σ(RB)‖2−‖σ(RA)⋅σ(RB)‖ where the chemical points represent the dot product between the signatures.

Second, our definition of latent enzyme promiscuity for one EC number was given by the number of different activities where enzymes annotated with this activity have been observed to participate. It was computed as follows. We listed all enzymes that were annotated with a given EC number, and we counted the total number of different EC numbers where these enzymes have been annotated.

### Evaluation of Phylogenetic Diversity
The phylogenetic distance between two species _o__i_ and _o__j_ was computed as the intertaxa branch length distance δ(_o__i_,_o__j_) of the two taxa within the tree of life ([31](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib31)); this is generally called a patristic distance. This value corresponds to their average sequence divergence in the multiple alignment of 31 orthologs ([31](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib31)). Phylogenetic diversity of a set of organisms was computed as in ([34](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib34)), by averaging the patristic or taxonomic distance between individual organisms. Phylogenetic diversity of a reaction or EC number was estimated by computing the phylogenetic diversity of organisms annotated with this reaction or catalytic function.

### Catalytic Function Classification and Efficiency Estimation
We used two types of functional classification for enzymes, one based on pathway modules and another on ortholog groups. KEGG pathway modules for each catalytic function (EC number) were downloaded from the KEGG site. Cluster of ortholog groups in _Escherichia coli_ were downloaded from the NCBI, National Institutes of Health, Web site. [Catalytic efficiency](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/catalytic-efficiency) was computed from the BRENDA database ([35](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib35)) (see [Table 4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl4)). For each EC number, we stored the values of _K__m_ and _K_cat of those reactions involving native enzymes (_i.e._ excluding mutants) where we were able to match substrate information with KEGG by means of the following procedure. For each entry in Brenda corresponding to an enzyme, we went through the list of substrates processed by this enzyme, flagging the entry as consistent if the same substrate was annotated in KEGG for the EC number that corresponds to the enzyme. Finally, we collected all available catalytic efficiency values in the consistent entries.

TABLE 4. Enzyme efficiency data set

Shown are the numbers of catalytic reactions, activities, and organisms with experimental efficiency from BRENDA, which were considered in our study.

| Definition | Total |
| --- | --- |
| Catalytic reactions | 4313 |
| EC numbers | 861 |
| Reactions with (_k_cat/_K__m_) full information | 485 |
| EC with (_k_cat/_K__m_) full information | 210 |
| Organisms | 620 |
| Organisms (_k_cat/_K__m_) full information | 151 |


## RESULTS
### Reaction and Annotation Level Enzyme Promiscuity
To characterize enzyme promiscuity, our basic definition is given by the chemical diversity found among the reactions that an enzyme can process. Typically, the number of biochemical reactions annotated for an enzyme is higher than the number of catalytic functions according to their EC classification because enzymes can use the same catalytic activity to process more than one substrate ([supplemental Fig. S1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)). Therefore, in order to get a more accurate estimate of the enzyme catalytic capabilities, enzyme promiscuity at the reaction level was measured by computing the average chemical dissimilarity (see [Table 3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl3)) between the reactions in the list of biochemical reactions annotated for each enzyme in the KEGG ([29](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib29)) or [MetaCyc](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/metacyc) database ([30](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib30)). Contrarily to the two previous parameters (number of annotated reactions and EC numbers), our definition based on reaction chemical diversity provides an overall estimate of enzymatic capabilities and a [quantitative characterization](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/quantitative-technique) of enzyme promiscuity, which is less likely to be affected by the bias arising from redundant annotations or arbitrary/inconsistent classifications ([36](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib36)). In fact, it is not always the case that an enzyme annotated with a large number of reactions is able to process chemically more diverse substrates (see [supplemental Fig. S2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)). The number of substrates, however, might be underestimated when they are labeled uniquely in generic terms, such as “alcohol” or “dialkyl ketone,” an issue that was found in 33 EC numbers (4.3% of total ECs in the data set) in our data set. Of these, only 15 EC numbers (1.9% of total ECs in the data set) were annotated uniquely with one generic substrate. The effect of the presence of this small set of enzymes mislabeled as non-promiscuous, thus, is not going to alter significantly any general trend observed in the results.

To further characterize enzyme promiscuity, our second definition is at the EC number annotation level, which might be more properly defined as _latent_ enzyme promiscuity because its definition is the number of different activities where enzymes have been annotated simultaneously with a given EC number. Therefore, this value is a measure of the total number of potential catalytic activities that an enzyme can process, based on the different functions that have been observed within its orthologs across the species.

Both definitions of promiscuity at the reaction and annotation activity level are interrelated because enzymes with the ability of catalyzing a greater chemical diversity are potentially more likely to be involved in a greater number of catalytic functions across organisms. On average, we observed this trend (_r_ = 0.77, _p_ = 2.6 × 10−2) (see [Fig. 1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig1)_A_). In some cases, however, enzymes annotated with one EC number, and therefore with no latent promiscuity, are actually able to process a significant number of chemically diverse substrates, a fact that could be related to the EC number definition. For example, aspartate aminotransferases (EC 2.6.1.1), which are enzymes with no latent promiscuity according to KEGG annotation, can potentially process [tyrosine](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/tyrosine), phenylanine, and trytophan as well ([37](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib37)), making its reaction chemical diversity 0.51. This value is one of the highest in the group of EC numbers with no latent promiscuity. Therefore, reaction level chemical diversity is in general a more accurate promiscuity measure than EC number annotation level.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073216399-8b38f1e9-1d25-43f4-ba61-f08c702a0c35.jpeg)

1. [Download : Download high-res image (137KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr1_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr1.jpg)

FIGURE 1. **Relationship between latent promiscuity and reaction diversity.**_A_, relationship between latent promiscuity and substrate chemical diversity; _B_, comparison between the measure of promiscuity at the annotation level (EC number) and based on EC dissimilarity in digits.

To examine how both of our definitions of promiscuity relate to the definition in Ref. [18](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib18), which is based on EC difference in digits, we plot in [Fig. 1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig1)_B_ for each enzyme the relationship between EC number dissimilarity and latent promiscuity. As it is shown in the plot, higher values of latent enzyme promiscuity usually correspond to a greater dissimilarity in digits, whereas lower values appear more scattered according to their EC number dissimilarity. Nevertheless, both measures are highly correlated (_r_ = 0.85, _p_ = 3.5 × 10−3).

### Phylogenetic Distance in Trees of Life and Enzyme Promiscuity
To perform our study of origins of enzyme promiscuity, we need an unbiased and comprehensive data set of phylogenetic and metabolic data. Phylogenetic diversity of any subset in a list of species might be estimated once a reference [tree](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/tree) of life is established. As described under “Experimental Procedures,” we took here as a reference the tree in Ref. [31](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib31), where genes in 191 species (see [Table 1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl1)) with completely annotated genomes were carefully selected in order to minimize horizontal gene transfer effects. The number of species was further reduced to 108 when branches of the same genus were grouped together (see [supplemental Tables S1 and S2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)). In order to estimate phylogenetic diversity, we took two approaches: tree distances calculated from sequence data following the procedure in the reference tree ([31](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib31)) and a tree based solely on evolutionary relationships through the use of phylogenetic systematics ([38](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib38)) (see [dendrograms](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/phylogenetic-tree) in [supplementary Fig. S3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)).

The reason for using two reference trees in this study is motivated by the fact that patristic distances (sum of the length of the branches) extracted from sequence alignment data should be used with caution. We hope that such pairwise distances will reflect phylogenetic diversity; however, some species with a much higher rate of [DNA](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/dna) change than others will bias the estimation by having a higher terminal branch length. To limit the risk of facing such bias, results are presented in this section comparatively for the estimation of phylogenetic diversity using pairwise patristic distances on the reference tree based on sequence data and for the estimation of phylogenetic diversity using a purely taxonomic (or topological) approach by counting the number of nodes separating each pair of species in the reference tree based on evolutionary relationships (_i.e._ by looking at the tree without its branch lengths).

To investigate how effects associated with the sequence data selection, such as the unequal rate of change among selected orthologs, the effects from horizontal gene transfer events ([39](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib39), [40](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib40)), and species sampling ([41](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib41)), might be introducing some bias in the tree of life, we evaluated the distribution of phylogenetic distances, finding that some taxa such as “prokaryotes” were overrepresented in our reference tree due to their greater availability of sequenced genomes. In fact, we observed that the distribution of phylogenetic distances (patristic distances from a maximum likelihood tree calculated from aligned DNA sequences) between organisms in the reference tree (see “Experimental Procedures” for definitions) follows a bimodal distribution (see [supplemental Fig. S4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)), illustrating the fact that some phyla are overrepresented in the tree, as is the case for proteobacteria and [firmicutes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/firmicutes) (see [Table 1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl1)). From this form of distribution, we might expect that phylogenetic distances between pairs in a random set of species would not monotonically increase with [sample size](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/sample-size) (see [supplemental Fig. S5](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)). Therefore, we can assume for this study that obtaining higher average phylogenetic distances can be properly interpreted as greater phylogenetic diversity or spread of species across the tree of life rather than a bias coming from a tree artifact.

To further evaluate the effect of investigation bias, we relied on the BRENDA database ([35](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib35)), which is one of the most comprehensive resources on experimental enzymatic data. One can hypothesize that enzymes present in many organisms might have been investigated in more detail, which could have led consequently to its annotation with multiple reactions. We assumed that the number of entries in Brenda for a given EC number provides a good estimate of the extent of the overall number of experimental studies performed on the enzyme. On the other hand, the presence of the enzyme in multiple organisms can be quantified, as previously, by computing the average phylogenetic distance between all organisms annotated with this enzyme. In our tests, the comparison between these two measures revealed no significant correlation, suggesting that the number of experimental studies performed on enzymes is not directly related to their phylogenetic extent in the tree of life, as can be seen in [supplemental Fig. S6, A and B](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10). This result rules out a potential artifact in our observations due to investigation bias.

To test the hypothesis that those catalytic functions in enzymes with greater chemical diversity are to be found and shared across more distant species in the tree of life and therefore come from deeper ancestral enzymes in the tree of life, we measured the chemical diversity of an enzyme by using the promiscuity definitions previously introduced. That hypothesis is preferring an ACCTRAN optimization of [homoplasies](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/homoplasy), favoring reversions over convergences; indeed, part of the tested hypothesis is that losing chemical diversity by progressive specialization is easier than having greater (twice or more) chemical diversity formed by ancestral enzymatic reactions. Conversely, enzymatic reactions that process specific substrates might be expected to be found usually confined within groups of more closely related species. Because catalytic specialization is an emergent property driven by evolution, based on our hypothesis, it should be observed at both enzyme and catalytic activity levels of promiscuity.

Similarly to the chemical distance between the substrates for a reaction pair, we measured the phylogenetic diversity of the reaction pair, which we define as the average phylogenetic distance between all of the organisms that can process that pair of reactions. In [Fig. 2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig2)_A_, we plot the relationship between the reaction chemical diversity and reaction phylogenetic diversity of enzymes in our set. Interestingly, we found a significant high correlation. Therefore, this result suggests that the capability of an enzyme to process more than one substrate is intimately related to its evolvability. Reactions that are catalyzed by a highly specific enzyme are shared by poorly divergent species (_i.e._ specific taxa in the tree of life), suggesting a later emergence of this function during evolution. In contrast, promiscuous enzymes are more likely to appear uniformly distributed across species in the tree of life.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073216631-a01b1efd-2e98-403a-a5d6-1b926781bf17.jpeg)

1. [Download : Download high-res image (135KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr2_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr2.jpg)

FIGURE 2. Relationship between reaction chemical diversity and reaction [phylogenetic](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/phylogeny) diversity._A_, phylogenetic distances from pairwise genetic distances calculated from multiple alignments; _B_, phylogenetic distances calculated from pairwise taxonomic node count in the [tree of life](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/tree-of-life). _C_, relationship between latent [enzyme promiscuity](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-promiscuity) and phylogenetic diversity of catalytic functions (EC numbers).

The conclusion does not change significantly according to the type of distance used to calculate species pairwise distances in the reaction phylogenetic diversity ([Fig. 2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig2), _A_ and _B_); the correlation coefficient is _r_ = 0.86, _p_ = 1.3 × 10−3 when using patristic distances of a tree based on sequence data and _r_ = 0.83, _p_ = 3.0 × 10−3 when using taxonomic distances in the tree, showing that the first estimation of the correlation was not affected by too strong inequalities in DNA rate of change among lineages.

Similar results were obtained in [Fig. 2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig2)_C_ at annotation level (_r_ = 0.81, _p_ = 1.4 × 10−2). In this case, we studied the relationship between all potential activities and phylogenetic distance of EC numbers, which was computed as the average distance between the species annotated with this particular EC number. This common trend reveals that not only are biochemical reactions found across more diverse species more likely to be processed by promiscuous enzymes, but also catalytic functions present in a greater diversity of species are potentially more promiscuous.

To evaluate the consistency of our previous results, which were based on KEGG, we recomputed them on MetaCyc, which has a higher curation level in terms of enzyme function annotation. For instance, although latent enzyme promiscuity values were found similar for both databases (correlation between promiscuity values _r_ = 0.88, _p_ = 7.1 × 10−4, shown in [supplemental Fig. S7](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)), there were nevertheless specific cases where EC numbers that appeared in KEGG as non-promiscuous were found in MetaCyc annotated as promiscuous. This result is due to the fact that KEGG annotations are performed, in their majority, by automated methods. Therefore, KEGG annotations might have overlooked some of the species-specific enzymatic functions of the [multifunctional proteins](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/multifunctional-protein) present in the tree of life, a problem that could lead our study to underestimate the actual distribution of enzymatic functions across species in the tree. Thus, to evaluate any bias arising from the way KEGG is annotated, our previous tests were repeated on the MetaCyc database. The data set that we were able to process from MetaCyc was, in turn, considerably smaller than the one from KEGG. This difference in size is due to the fact that MetaCyc does not contain complete genomes as KEGG does but rather a small number of highly curated reference enzymes for each biochemical activity. The results nonetheless followed the same trend as before, despite the way enzyme promiscuity was measured either from the chemical diversity of their reactions (_r_ = 0.74, _p_ = 1.5 × 10−2; [supplemental Fig. S8](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)) or as latent promiscuity (_r_ = 0.94, _p_ = 4.7 × 10−4; [supplemental Fig. S9](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)). The fact that the results from the highly curated MetaCyc database closely mirror the results from KEGG provides some confirmation that the larger but much less accurate KEGG data set is providing meaningful results.

### Chemical Diversity and Latent Enzyme Promiscuity across Species
Our previous findings show a close relationship between reaction chemical diversity and evolutionary time as measured through phylogenetic divergence. Based on this result, we might expect to see some distinctive shift in species with highly specialized catalytic activities. In fact, using our measure of reaction chemical diversity, it is possible to parallel successive divergence times of groups in the tree of life of species with metabolic annotations. In [Fig. 3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig3), _A_ and _B_, reaction chemical diversity of enzymes was averaged and plotted for each organism and taxonomic group. [Fig. 3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig3), _C_ and _D_, shows the results obtained by using latent enzyme promiscuity. Interestingly, taxonomic groups going from less to more specialized catalytic function appear in the following order [archaea](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/archaeon), bacteria, fungi, plants, and animals, which is the order of divergence times of each group ([33](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib33)), illustrating the fact that groups of later divergence in evolution are in general more specialized in their catalytic functions. We found that the separation between phylogenetic groups Archaea, Eubacteria, and Eukaryota, represented in [Fig. 4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig4), _A_ and _B_, is significant in both latent enzyme promiscuity and reaction chemical diversity (_p_ < 2.2 × 10−16 for a [multivariate analysis](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/multivariate-analysis) of variance test).

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073216624-71cc5131-0dd4-4119-ba3e-f93d4534d2d4.jpeg)

1. [Download : Download high-res image (144KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr3_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr3.jpg)

FIGURE 3. [Enzyme promiscuity](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-promiscuity) at different levels of taxonomic grouping._A_ and _B_, distribution of reaction chemical diversity; _C_ and _D_, latent enzyme promiscuity at two different levels of taxonomic grouping.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073216321-1b0c691d-d655-427d-b5de-496566803b8c.jpeg)

1. [Download : Download high-res image (171KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr4_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr4.jpg)

FIGURE 4. **Scatter plot of latent enzyme promiscuity and reaction chemical diversity in organisms.**_A_, grouping by taxonomic groups; _B_, grouping at the organism level.

Reaction chemical diversity and latent enzyme promiscuity together provide an account of how catalytic capabilities of organisms have evolved and adapted to their environments. For instance, [euryarchaeota](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/euryarchaeota), which can both process many substrates and contain high latent promiscuity, are an example of [extremophiles](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/extremophile), which can survive under extreme conditions and therefore need a highly adaptable metabolic system. The same goes for deinococcus-thermus, which are a small group of bacteria highly resistant to environmental hazards. To generalize an evolutionary interpretation of the plot ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig4), _A_ and _B_), we must keep in mind that all species here are today's products of [genetic](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/genetics) lineages that do have the same evolutionary time since the origins of life. However, those species do not face the same chemical changes in their environments, and their [position](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/position) in the plot could also reflect past adaptive pressures. We infer that organisms showing high latent enzyme promiscuity and high reaction chemical diversity ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig4), _A_ and _B_, _top right_) must be pioneers that have to face strong chemical variations in their recently colonized environments. Organisms showing low latent enzyme promiscuity and high reaction chemical diversity ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig4), _A_ and _B_, _top left_) must be “old warriors” that have been accustomed to facing strong environmental changes since long ago. If the data set can be considered as “transfer-free,” the [spirochaetes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/spirochete) and [tenericutes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/mollicutes) are “old warriors” in the sense that their ancestors might have faced very strong environmental changes in a recent past and therefore they still kept a high reaction chemical diversity but do not have to face strong environmental pressure anymore. In other words, they are not in a pioneering situation anymore or are less so than in their recent past. Similarly, organisms exhibiting high latent enzyme promiscuity and low reaction chemical diversity ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig4), _A_ and _B_, _bottom right_) must be organisms that recently arrived in stable chemical conditions, like, for instance, recent parasites, commensals, or symbionts, such as those observed in [actinobacteria](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/actinobacteria), a bacteria with mutualistic tendencies ([42](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib42)). Last, organisms with low latent enzyme promiscuity and low reaction chemical diversity ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig4), _A_ and _B_, _bottom left_) must be highly integrated organisms. Pluricellularity, for instance, is buffering the genetic/enzymatic effects of environmental chemical changes. Moreover, multicellular mobile organisms have the choice to rapidly escape from chemical hazards and actively reach chemical optima. It is not surprising to find animals in that area of the plot. Plants are multicellular organisms; however, they cannot move and escape chemical aggression. This may be why we find them at the middle of the plot, with moderate latent enzyme promiscuity and moderate reaction chemical diversity.

### Metabolic Functions of Promiscuous Enzymes
We did not observe a link between enzyme promiscuity and gene essentiality ([3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib3), [43](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib43)) (_i.e._ with genes that are absolutely required for cell survival). However, analysis of metabolic functions found in promiscuous enzymes, given in [Table 5](https://www.sciencedirect.com/science/article/pii/S0021925820684927#tbl5), revealed that catalytic activities with a higher degree of latent promiscuity (≥5) are mainly involved in [amino acid](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/amino-acids) (_p_ = 1.7 × 10−2) and lipid metabolism (_p_ = 1.9 × 10−2). This fact was seen both in the whole data set using the functional classification of pathways where they are involved (KEGG modules) ([44](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib44)) and using the NCBI clusters of ortholog groups for enzyme sequences in _E. coli_, shown in [Fig. 5](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig5), _A_ and _B_), respectively. Based on our previous finding of a greater phylogenetic extent of promiscuous enzymes, amino acid and lipid metabolisms might be associated here with the earliest form of biochemical reactions, which still are being processed by multifunctional enzymes ([45](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib45), [46](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib46)). It is not surprising; free amino acids are found in abiotic environments like interstellar meteorites and ice ([47](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib47), [48](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib48)). They must have been one of the very first complex organic compounds (_i.e._ with all main atomic species of life: carbon, hydrogen, oxygen, nitrogen, and sulfur) already available to the earliest protobionts and enzymatic functions). Enzymes performing amino acid catabolism and [anabolism](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/anabolism) must have been the very first ones in life. Conversely, metabolisms of glycans (_p_ = 7.4 × 10−3) and [secondary metabolites](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/secondary-metabolite) (_p_ = 4.4 × 10−1) are catalyzed by enzymes with a low degree of latent promiscuity, probably therefore of more recent origin. Their greater specificity might be linked to the fact that secondary metabolism is generally associated with defense mechanisms specific to organisms, and glycan pathways are usually associated with multicellular developmental processes and restricted to the metazoa ([43](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib43)).

TABLE 5. Enrichment (+) or depletion (−) in the metabolic function according to KEGG module classification for the set of enzymes with high latent promiscuity (≥5) compared with the total set in [Fig. 5](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig5)_A_

Significant _p_ values (_p_ < 5.0 × 10−2) are shown in boldface type.

| Metabolism | _p_ value | Enrichment/Depletion |
| --- | --- | --- |
| Amino acids | **1.7 × 10****−2** | + |
| Lipids | **1.9 × 10****−2** | + |
| Central + energy | 1.1 × 10−1 | − |
| Glycans | **7.4 × 10****−3** | − |
| Secondary | 4.4 × 10−1 | − |
| Nucleotides | 9.7 × 10−1 | − |


<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710073216742-966ed24e-3105-4c5a-b44e-7811c4129426.jpeg)

1. [Download : Download high-res image (188KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr5_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0021925820684927-gr5.jpg)

FIGURE 5. Distribution of metabolic functions on [enzymes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme) depending on their latent promiscuity._A_, KEGG orthologies; _B_, _E. coli_ based on clusters of ortholog groups.

### Catalytic Efficiency of Promiscuous Enzymes
We used our definition of latent promiscuity in order to investigate the previously reported experimental observation that enhancement of latent catalytic activities does not seem often to trade off with parallel decreases in the original function ([16](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib16), [24](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib24)), in contradiction with the commonly accepted assumption that broad substrate acceptance generally comes at the price of low reaction [turnover numbers](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/turnover-number) ([19](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib19)). In our results, catalytic efficiency, estimated from experimental data as described under “Experimental Procedures,” does not seem to be related in general to the latent promiscuity of enzymes because the trend that we observed remains flat for most of the values of latent enzyme promiscuity (_r_ = 0.02, _p_ = 0.27; see [supplemental Fig. S10](https://www.sciencedirect.com/science/article/pii/S0021925820684927#ecomp10)). This result, thus, corroborates the observed fact ([16](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bib16)) that enzyme promiscuity can be in many cases achieved without compromising efficiency, suggesting that although there is a trend in evolution toward specialization, catalytic efficiency has remained on average at the same level during the history of life, perhaps due to energy constraints.

## DISCUSSION
In this work, we have shown that enzyme promiscuity plays a prominent role in the study of the evolution of [metabolic networks](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/metabolic-network). A distinctive property of our given definition of promiscuity, which is based on the chemical diversity of catalytic reactions that enzymes can process, is that it does not depend on [protein sequence](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/peptide-sequence) comparisons. As a matter of fact, the same evolutionary trend in enzyme promiscuity was observed in the tree of life independently of the way pairwise distances between species were measured, either based on sequence data or on pure taxonomic hierarchy. We find that the fact that a particular enzyme catalyzes a chemically diverse set of substrates is related to the wider spread of the underlying processing reactions across the tree of life ([Fig. 2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig2), _A_ and _B_), suggesting an older origin for these nonspecific enzymes. In turn, enzymes that process more specific substrates are usually shared by organisms of lower divergence times (_i.e._ constrained to some smaller taxa in the tree of life, which might be interpreted as a later emergence of their function during evolution). These observations are confirmed when we look at catalytic functions that potentially can be performed simultaneously, a property that we term latent enzyme promiscuity. Again, the fact that a catalytic function is potentially more promiscuous is related to the fact that the activities are more widespread across the tree of life ([Fig. 2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#fig2)_C_).

The evolutionary aspect of enzyme promiscuity appears to be a feature with broad applicability. In particular, it was shown in this study that promiscuity at both the enzyme and catalytic level paralleled divergence times in the tree of life. These results can provide new clues to explain the mechanism of how [enzymatic activities](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-activity) evolve and specialize under environmental pressure. Namely, because promiscuous catalysis is mainly found in metabolic functions associated with [amino acid metabolism](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/amino-acid-metabolism), our hypothesis suggests an early origin of these functions, whereas glycan and secondary metabolisms appear as highly specialized functions of later origin.

We observe, however, that [catalytic efficiency](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/catalytic-efficiency) of enzymes is a property essentially independent of their latent promiscuity. This intriguing result might suggest that despite the general trend in evolution toward specialization, energy constraints have kept average catalytic efficiency at the same level through the history of life. Open questions remain in the study of how [metabolic fluxes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/metabolic-flux) are related to enzyme promiscuity and whether these results can be extended to other biological networks, such as transcription regulatory and signaling networks. A better understanding of the underlying model of enzyme evolution will have important implications for [protein design](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/protein-design) through directed and _in silico_ evolution and might assist us with the identification of primeval promiscuous catalytic activities in metabolic pathways contributing to life's minimal metabolism.

## REFERENCES
1. [1](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib1) Genome Res., 13 (2003), pp. 422-427
2. [2](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib2)

J.M. Peregrín-Alvarez, C. Sanford, J. Parkinson

Genome Biol., 10 (2009), p. R63

3. [3](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib3)

S. Gerdes, R. Edwards, M. Kubal, M. Fonstein, R. Stevens, A. Osterman

Curr. Opin. Biotechnol., 17 (2006), pp. 448-456

4. [4](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib4)

Curr. Opin. Biotechnol., 20 (2009), pp. 504-508

5. [5](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib5)

R. Alves, R.A. Chaleil, M.J. Sternberg

J. Mol. Biol., 320 (2002), pp. 751-770

6. [6](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib6)

P.J. O'Brien, D. Herschlag

Chem. Biol., 6 (1999), pp. R91-R105

7. [7](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib7)

S.C. Rison, J.M. Thornton

Curr. Opin. Struct. Biol., 12 (2002), pp. 374-382

8. [8](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib8)

S.C. Rison, S.A. Teichmann, J.M. Thornton

J. Mol. Biol., 318 (2002), pp. 911-932

9. [9](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib9)

Nat. Rev. Mol. Cell Biol., 10 (2009), pp. 791-803

10. [10](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib10)

S. Freilich, L. Goldovsky, C.A. Ouzounis, J.M. Thornton

BMC Evol. Biol., 8 (2008), p. 247

11. [11](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib11)

M.J. de Groot, R.J. van Berlo, W.A. van Winden, P.J. Verheijen, M.J. Reinders, D. de Ridder

Bioinformatics, 25 (2009), pp. 2975-2982

12. [12](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib12)

M. Marcet-Houben, P. Puigbò, A. Romeu, S. Garcia-Vallve

Bioinformation, 2 (2007), pp. 135-144

13. [13](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib13)

Proc. Natl. Acad. Sci. U.S.A., 31 (1945), pp. 153-157

14. [14](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib14)

Annu. Rev. Microbiol., 30 (1976), pp. 409-425

15. [15](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib15)

BMC Bioinformatics, 5 (2004), p. 15+

[Google Scholar](https://scholar.google.com/scholar?q=Light%2C%20S.%2C%20Kraulis%2C%20P.%2C%20(2004)%20BMC%20Bioinformatics%205%2C%2015%2B.)

16. [16](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib16)

O. Khersonsky, C. Roodveldt, D.S. Tawfik

Curr. Opin Chem. Biol., 10 (2006), pp. 498-508

17. [17](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib17)

Trends Biotechnol., 25 (2007), pp. 231-238

18. [18](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib18)

O. Khersonsky, D.S. Tawfik

L. Mander, H.W. Lui (Eds.), Comprehensive Natural Products II: Chemistry and Biology, Elsevier, Oxford (2010), pp. 48-90

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Comprehensive%20Natural%20Products%20II%3A%20Chemistry%20and%20Biology&publication_year=2010&author=O.%20Khersonsky&author=D.S.%20Tawfik)

19. [19](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib19)

W.B. Jakoby, D.M. Ziegler

J. Biol. Chem., 265 (1990), pp. 20715-20718

20. [20](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib20)

J.D. Bloom, P.A. Romero, Z. Lu, F.H. Arnold

Biol. Direct, 2 (2007), p. 17

21. [21](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib21)

Biochemistry, 47 (2008), pp. 157-166

22. [22](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib22)

D. Vitkup, P. Kharchenko, A. Wagner

Genome Biol., 7 (2006), p. R39

23. [23](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib23)

C. Pál, B. Papp, L.D. Hurst

Genetics, 158 (2001), pp. 927-931

24. [24](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib24)

S. Kurtovic, A. Shokeer, B. Mannervik

J. Mol. Biol., 382 (2008), pp. 136-153

25. [25](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib25)

Curr. Opin Chem. Biol., 7 (2003), pp. 265-272

26. [26](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib26)

Curr. Opin. Chem. Biol., 9 (2005), pp. 195-201

27. [27](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib27)

J.L. Faulon, M.J. Collins, R.D. Carr

J. Chem. Inf. Comput. Sci., 44 (2004), pp. 427-436

28. [28](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib28)

P. Carbonell, J.L. Faulon

Bioinformatics, 26 (2010), pp. 2012-2019

29. [29](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib29)

M. Kanehisa, M. Araki, S. Goto, M. Hattori, M. Hirakawa, M. Itoh, T. Katayama, S. Kawashima, S. Okuda, T. Tokimatsu, Y. Yamanishi

Nucleic Acids Res., 36 (2008), pp. D480-D484

30. [30](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib30)

R. Caspi, T. Altman, J.M. Dale, K. Dreher, C.A. Fulcher, F. Gilham, P. Kaipa, A.S. Karthikeyan, A. Kothari, M. Krummenacker, M. Latendresse, L.A. Mueller, S. Paley, L. Popescu, A. Pujar, A.G. Shearer, P. Zhang, P.D. Karp

Nucleic Acids Res., 38 (2010), pp. D473-D479

31. [31](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib31)

F.D. Ciccarelli, T. Doerks, C. von Mering, C.J. Creevey, B. Snel, P. Bork

Science, 311 (2006), pp. 1283-1287

32. [32](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib32)

Syst. Biol., 52 (2003), pp. 696-704

33. [33](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib33)

The Timetree of Life, Oxford University Press, New York (2009), pp. 3-18

34. [34](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib34)

R.M. Warwick, K.R. Clarke

Mar. Ecol. Prog. Ser., 129 (1995), pp. 301-305

35. [35](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib35)

A. Chang, M. Scheer, A. Grote, I. Schomburg, D. Schomburg

Nucleic Acids Res., 37 (2009), pp. D588-D592

36. [36](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib36)

G. Markov, G. Lecointre, B. Demeneix, V. Laudet

BioEssays, 30 (2008), pp. 349-357

37. [37](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib37)

S.C. Rothman, J.F. Kirsch

J. Mol. Biol., 327 (2003), pp. 593-608

38. [38](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib38)

G. Lecointre, H. Le Guyader

The Tree of Life: A Phylogenetic Classification, Belknap Press of Harvard University Press, Cambridge, MA (2007), pp. 18-24

[Google Scholar](https://scholar.google.com/scholar_lookup?title=The%20Tree%20of%20Life%3A%20A%20Phylogenetic%20Classification&publication_year=2007&author=G.%20Lecointre&author=H.%20Le%20Guyader)

39. [39](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib39)

W.F. Doolittle, E. Bapteste

Proc. Natl. Acad. Sci. U.S.A., 104 (2007), pp. 2043-2049

40. [40](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib40)

C. R. Biol., 332 (2009), pp. 171-182

41. [41](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib41)

G. Lecointre, H. Philippe, H.L. Vân Lê, H. Le Guyader

Mol. Phylogenet. Evol., 2 (1993), pp. 205-224

42. [42](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib42)

Trends Microbiol., 17 (2009), pp. 529-535

43. [43](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib43)

T. Baba, T. Ara, M. Hasegawa, Y. Takai, Y. Okumura

Mol. Syst. Biol., 2 (2006), Article 2006.0008

44. [44](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib44)

T. Yamada, M. Kanehisa, S. Goto

BMC Bioinformatics, 7 (2006), p. 130

45. [45](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib45)

C. Cunchillos, G. Lecointre

J. Biol. Chem., 278 (2003), pp. 47960-47970

46. [46](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib46)

U.J. Meierhenrich, G.M. Muñoz Caro, J.H. Bredehöft, E.K. Jessberger, W.H. Thiemann

Proc. Natl. Acad. Sci. U.S.A., 101 (2004), pp. 9182-9186

47. [47](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib47)

G.M. Muñoz Caro, U.J. Meierhenrich, W.A. Schutte, B. Barbier, A. Arcones Segovia, H. Rosenbauer, W.H. Thiemann, A. Brack, J.M. Greenberg

Nature, 416 (2002), pp. 403-406

[Google Scholar](https://scholar.google.com/scholar?q=Mu%C3%B1oz%20Caro%2C%20G.%20M.%2C%20Meierhenrich%2C%20U.%20J.%2C%20Schutte%2C%20W.%20A.%2C%20Barbier%2C%20B.%2C%20Arcones%20Segovia%2C%20A.%2C%20Rosenbauer%2C%20H.%2C%20Thiemann%2C%20W.%20H.%2C%20Brack%2C%20A.%2C%20Greenberg%2C%20J.%20M.%2C%20(2002)%20Nature%20416%2C%20403%E2%80%93406.)

48. [48](https://www.sciencedirect.com/science/article/pii/S0021925820684927#bbib48)

M.P. Bernstein, J.P. Dworkin, S.A. Sandford, G.W. Cooper, L.J. Allamandola

Nature, 416 (2002), pp. 401-403

## Cited by (63)
### [Supramolecular enzyme-mimicking catalysts self-assembled from peptides](https://www.sciencedirect.com/science/article/pii/S2589004222021046)
2023, iScience

The kinetic parameters of the hydrolase mimics are listed in Table 4. It is believed that primitive enzymes could catalyze a wide range of biochemical transformations to establish the protometabolic reaction networks, and the substrate specificity of modern enzymes is a result of long-term natural evolution and selection.104,105,106 However, it is difficult to identify the evolutionary pathways from promiscuous primitive enzymes to functionally specific extant enzymes.

### [Application of free and immobilized novel bifunctional biocatalyst in biotransformation of recalcitrant lignocellulosic biomass](https://www.sciencedirect.com/science/article/pii/S0045653521018841)
2021, Chemosphere

In general concepts, it has been proposed that enzymes perform as proteins catalyzing only one reaction with specific substrates. However, there are some enzymes that play multiple physiological roles, known as multi-functional enzymes, which are specified as moonlighting or promiscuous enzymes (Carbonell et al., 2011). Moonlighting is a phenomenon by which an enzyme performs a primary function of enzymatic catalysis and some secondary non-catalytic roles like signal transduction, apoptosis, or structural (Sriram et al., 2005).

### [Moonlighting Biochemistry of Cysteine Synthase: A Species-specific Global Regulator](https://www.sciencedirect.com/science/article/pii/S0022283621004885)
2021, Journal of Molecular Biology

Characterized as moonlighting proteins (MP), multifunctional proteins display functional diversity in a condition-dependent manner or bind to another protein and modulate its activity. In the first type, changes in cellular localization, expression in different cell types, changes in oligomerization, and chemical modifications such as post-translational modifications alter its functions.3–5,15–17 In the second type, a multifunctional MP like CS modulates the functional properties of other proteins by binding to them dynamically in a context-dependent manner.6–14

[View all citing articles on Scopus](http://www.scopus.com/scopus/inward/citedby.url?partnerID=10&rel=3.0.0&eid=2-s2.0-83755171600&md5=5d80d87d1da5396894f334b59c9ae980)

© 2011 ASBMB. Currently published by Elsevier Inc; originally published by American Society for Biochemistry and Molecular Biology.  


> 来自: [Origins of Specificity and Promiscuity in Metabolic Networks - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0021925820684927)
>

