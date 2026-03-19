[https://doi.org/10.1016/j.plantsci.2016.11.006](https://doi.org/10.1016/j.plantsci.2016.11.006)[Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S0168945216306495&orderBeanReset=true)

## Highlights
+ •

An experimental approach to isolating epistatic networks is presented.

+ •

Theoretical approaches to quantifying epistasis are enumerated.

+ •

Biophysical models of protein epistasis are described.

+ •

A speculative scenario of epistasis and dominance in catalytic function is described.

+ •

A synthesis of evolutionary theory and mechanistic [enzymology](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzymology) is presented.

## Abstract
Epistasis, the interaction between mutations and the genetic background, is a pervasive force in evolution that is difficult to predict yet derives from a simple principle − biological systems are interconnected. Therefore, one effect may be intimately linked to another, hence interdependent. Untangling epistatic interactions between and within genes is a vibrant area of research. Deriving a mechanistic understanding of epistasis is a major challenge. Particularly, elucidating how epistasis can attenuate the effects of otherwise dominant mutations that control phenotypes. Using the emergence of terpene cyclization in specialized metabolism as an excellent example, this review describes the process of discovery and interpretation of dominance and epistasis in relation to current efforts. Specifically, we outline experimental approaches to isolating epistatic networks of mutations in protein structure, formally quantifying epistatic interactions, then building biochemical models with chemical mechanisms in efforts to achieve an understanding of the physical basis for epistasis. From these models we describe informed conjectures about past evolutionary events that underlie the emergence, divergence and specialization of terpene synthases to illustrate key principles of the constraining forces of epistasis in enzyme function.

+ [Previous](https://www.sciencedirect.com/science/article/pii/S0168945216306227)
+ [Next](https://www.sciencedirect.com/science/article/pii/S016894521630810X)

## Keywords
Epistasis

Plant specialized metabolism

Protein structure

Evolutionary theory

Chemical mechanisms

Networks

## 1. Introduction
Advances in genomics are yielding unprecedented access to sequence information, while the advent of [synthetic biology](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/synthetic-biology) and genome editing technologies such as CRISPR/Cas9 are empowering us to author the code [[1]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0005). The coming era promises to deliver personalized cures for [genetic](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/genetics) disease, enhanced crops for sustainable production of foods and fuels. Identifying and modifying dominant genes (or mutations) that control the phenotype of interest, holds the key to achieving our future goals. However, our limited ability to interpret the genome and the fundamental genotype-phenotype relationship are major barriers, in large part due to the pervasive and confounding force of epistasis [[2]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0010).

Epistasis comes from a rich genetic tradition that has brought keen observations and insights along with the requisite vocabulary to describe the interactions between genes controlling phenotypes. Though we discuss historical context here, we proffer a conceptually simplified definition, where dominance and epistasis are considered opposite ends of a continuum: dominant mutations/alleles act _**independent**_ of one another (and the genetic background) and hence additively affect the fitness of a given gene (phenotype) in either positive or negative ways. Conversely, the effects of other mutations/alleles are critically _**interdependent**_ upon each other (and genetic backgrounds) and hence give rise to non-additive (non-linear) effects. Of critical note, relationships can change as biological systems evolve and ‘re-wire’ over time. Indeed, a given gene may be ‘dominant’ − a definition that may hold up across many genetic backgrounds. However, given the right combination of [genetic changes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/gene-mutation), the effect of an otherwise dominant mutation/allele will become entangled in the genetic background, and hence relationships can shift from dominant to epistatic and visa versa. Thus, while we use static operational definitions for epistasis and dominance, evolution is dynamic and relationships change over time.

Epistasis is the influence of the genetic background on a gene, an effect most pronounced for complex traits that involve multiple genetic interactions. Put another way, epistasis describes a systems phenomenon where the whole is greater (or lesser) than the sum. This phenomenon is well described in [classical genetics](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/classical-genetics), exemplified by pioneering studies of DDT resistance in _Drosophila_ where adult [insecticide resistance](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/insecticide-resistance) was found to be polygenic [[3]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0015). Increasingly, studies focused on [molecular evolution](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/molecular-evolution) of proteins describe epistasis within genes (intragenic epistasis), as illustrated by a recent systematic study of yeast [heat shock protein](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/heat-shock-protein)[[4]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0020). In such cases, the functional effects of a single substitution will often depend on the presence or absence of other substitutions in the protein background [[5]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0025). This becomes particularly relevant in [combinatorial libraries](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/combinatorial-library) (discussed here) where numerous higher-order interactions are explored by simultaneous mutation of several [positions](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/position). While some genes (or mutations therein) clearly display dominance, the capacity to dictate phenotype outcomes in most-all genetic (or protein) backgrounds, many gene mutations do not. These other genes seem to have a phenotypic robustness to mutations. However as mentioned above, the shifting genetic background can sometimes attenuate the effects of otherwise dominant mutations in seemingly mysterious ways. Thus, we desperately need a mechanistic understanding of epistasis, derived from the physical and chemical principles that govern biological systems as a necessary step to understand how natural [genetic variation](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/genetic-divergence) impacts [phenotypic characters](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/morphological-trait).

The dominance of certain genes in determining the phenotype of an organism (i.e. round pea shape), enabled Mendel to posit an underlying unit of inheritance in organisms (the gene), giving rise to the dominant-recessive paradigm of genetics. Bateson et al. coined the term epistasis to describe the masking of phenotypic effects of one allele by another at a different locus [[6]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0030). Epistasis was already apparent in the early days of genetics, and broke the mold of [Mendelian inheritance](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/mendelian-inheritance)[[7]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0035). Later unification of [population genetics](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/population-genetics) with Darwinian evolution resulted in the modern synthesis that reshaped our concept of epistasis. The fitness landscape metaphor of Wright gave us a topographical image of the genotype-phenotype relationship − a landscape with peaks, valleys and adaptive ridges [[8]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0040). We build on this landscape metaphor here with the parable of the sower from the Synoptic Gospels wherein a sower sows seed widely. Some seed lands on the trodden path and is eaten by birds, whereas other seed lands on rocky ground and among thorns, and the seed is lost; but some seed falls upon fertile soil where it takes root, grows, yielding thirty, sixty, and a hundredfold. In the context of this review, the counterbalancing forces of dominance (the seed) and epistasis (the soil) play a role in the emergence of a novel phenotypic character (e.g. catalytic function in enzymes). Accordingly, dominant mutations carry great potential to dictate phenotypic outcomes (i.e. redirect catalytic specificity), and hence give rise to new and successful [lineages](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/lineages). However, dominant mutations must fall on the permissive background of other mutations to take root in a progenitor before rising to prominence.

Here we frame our discussion of dominance and epistasis using terpene [synthase](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/synthase)[enzymes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme) of plant specialized metabolism. Plants synthesize an astounding array of diverse metabolites, traits that enable plants to mediate important ecological interactions and adapt and thrive in myriad ecological niches, an adaptive capacity likely critical for colonization of land [[9]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0045). Terpenes constitute a major branch of plant specialized metabolism, numbering well over 30,000 characterized compounds [[10]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0050). These metabolites attract [pollinators](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/pollinator)[[11]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0055) and natural enemies of herbivores [[12]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0060), repel microbial pathogens [[13]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0065), and mediate symbiotic relations [[14]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0070). Numerous enzymes form dedicated pathways leading to the [biosynthesis](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/anabolism) of terpenes. A single enzyme family, the terpene synthases, are engines of much of this chemical diversity, responsible for converting a limited number of linear substrates into hundreds of structurally complex, often multi-cyclic hydrocarbons, through a remarkable [cyclization](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/cyclization) reaction [[15]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0075). The complexity of cyclization mechanisms renders terpene synthases sensitive to mutational perturbations, thus redirecting the output of chemically diverse products. This is a favourable property for plants, which relay on an adaptable chemical synthesis platform to keep pace with ecological and environmental changes. In the context of plant specialized metabolism, these properties make terpene synthases ideal model systems to study epistasis. By contrast, most enzymes generate one or a few products depending on the range of substrates they accept, and thus contribute substantially less to chemical novelty. Finally, the intensive study of terpene synthases is timely; harnessing these enzymes by synthetic biology has driven biotechnology applications that provide new access to high-value chemicals from flavours and fragrances to vital medicines [[16]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0080).

Our recent discovery of the emergence of terpene cyclization in the [medicinal plant](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/medicinal-plant)[Artemisia annua](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/artemisia-annua)[[17]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0085) serves as an ideal example to illustrate the counterbalancing forces of dominance and epistasis in protein evolution. Specifically, the discovery of a dominant natural substitution (mutation) that unlocks cyclization chemistry in an otherwise ‘simple’ linear product-producing enzyme likely had a profound impact on the plant’s ecological interactions (and fitness) owing to an expanded vocabulary of specialized metabolites. In this review, we use our example as a framework to describe an experimental process for dissection of epistatic networks of [amino acid](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/amino-acid) residues that control transitions between catalytic phenotypes. This shows how modularizing epistasis into networks facilitates the systematic exploration of epistasis in other protein backgrounds. Then, we will discuss formal quantification of epistasis for simple to higher-order interactions and how to build simple visualizations for comparative analysis of epistasis in different protein backgrounds. Further, we describe the use of biochemical models incorporating chemical mechanisms as a basis for examining and interpreting the physical manifestations of epistasis and dominance. Finally, we use our models to draw inferences into evolutionary scenarios where novel catalytic functions emerged and diverged leading to specialized activities. Extant enzymes of the [Asteraceae](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/asteraceae) plant family are used as an example. The principles of epistasis in protein evolution are broad though the discussion here is focused. However, we will draw in supporting examples from the literature throughout while directing the reader to comprehensive reviews that expand ideas beyond what is covered here.

## 2. Dissecting epistatic interactions
Dissecting specific genetic interactions underlying prevalent epistatic phenomena involving higher-order interactions (3 or more loci) remains a challenge [[18]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0090). Higher-order interactions likely contribute substantially to complex traits and evolutionary processes [[19]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0095) yet remain poorly understood. Most commonly, organismal-scale studies only report pairwise genetic interactions [[20]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0100), [[21]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0105), [[22]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0110), [[23]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0115), [[24]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0120), mainly due to challenges with [sample sizes](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/sample-size) and statistical power. By contrast, studies of intragenic epistasis in protein evolution are more tractable given advances in gene library synthesis, directed evolution, and high-throughput screening techniques [[25]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0125), [[26]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0130), [[27]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0135), [[28]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0140). For example, large-scale biochemical studies reveal pervasive epistasis in the [molecular evolution](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/molecular-evolution) of _E. coli_ isopropymalate [dehydrogenase](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/dehydrogenase)[[29]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0145), while [next generation sequencing](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/next-generation-sequencing) linked to selection systems mapped extensive epistasis in the protein-protein interface of _E. coli_[protein kinase](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/protein-kinases) PhoQ [[30]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0150). More focused studies have employed careful biochemical dissection using ancestral reconstruction approaches to uncover pronounced epistatic effects in the evolution of [glucocorticoid receptor](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/glucocorticoid-receptor) specificity [[31]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0155). Combinatorial gene library synthesis and biochemical characterization of plant [enzyme](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme)[lineages](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/lineages) have revealed extensive non-additivity in the effects of mutations separating two close terpene [synthase](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/synthase) homologues from [Solanaceae](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/solanaceae)[[32]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0160), composed of significant higher-order interactions [[19]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0095). While most reports retrospectively examine epistatic interactions, a forward experimental approach to dissecting epistasis, borrowing principles from traditional breeding, may provide a useful experimental framework for isolating higher-order epistatic interactions, as illustrated here for the emergence of terpene [cyclization](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/cyclization) in [Artemisia annua](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/artemisia-annua)[[17]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0085) ([Fig. 1](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0005)).

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710065109725-f927573f-ef48-4716-b6c8-e4a3381da85f.jpeg)

1. [Download : Download high-res image (413KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0168945216306495-gr1_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0168945216306495-gr1.jpg)

Fig. 1. Experimental dissection of an epistatic network of residues. (A) The phenotype under investigation; the core cyclization mechanism of sesquiterpene synthases of the terpene synthase enzyme family. Farnesyl pyrophosphate (FPP) is a universal substrate, that when cleaved by terpene synthases, generates a reactive farnesyl cation (orange) that can either be quenched by proton abstraction to give a linear hydrocarbon (_E_)-β-farnesene (blue) as in the case for BFS, or undergo intramolecular cyclization reactions and rearrangements prior to quenching, forming a diverse array of cyclic hydrocarbons, such as amorpha-4,11-diene (green) in the case of ADS. (B) An iterative breeding strategy was used to isolate an epistatic network wherein natural sequence variation from ADS was introgressed (horizontal arrows) into BFS then backcrossed (vertical arrows) to identify minimal contributions of ADS (in this case single point mutations) carried forward as the parental background in each successive round. Color-coding of spheres (according to the scheme in A) denotes linear (blue) or cyclic (green) product production by a given enzyme. (C) Three residues form an epistatic network, which interact in antagonistic and/or agonistic ways to activate or supress cyclization. (D) A shaded punnet square (blue = linear, green = cyclic) illustrates the effect of modifier position 430. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

### 2.1. The phenotype and choice of starting point
Analysis of global sequence alignments can lead to testable biochemical hypotheses about the role of epistasis in protein families. For example, studies of [phosphoglycerate kinase](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/phosphoglycerate-kinase) revealed that [position](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/position) 219 was highly conserved active site Lys residue in Eukaryota and Bacteria kingdoms while a Ser in [Archea](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/archaea)[[33]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0165). Further [mutagenesis](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/mutagenesis) and biochemical characterization revealed this residue position was non-exchangeable between the different protein backgrounds, a hallmark of epistasis. These observations set the stage for directed evolution approaches that identified residue substitutions ultimately making the protein background permissible to substitutions at position 219. In our example, we focus on transitions in enzyme function that mark key evolutionary events in protein families. In considering the evolutionary origins of a biochemical trait (i.e. catalytic specificity), a [phylogenetic analysis](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/phylogeny) can readily identify homologues that share substantial sequence identity yet possesses divergent catalytic specificities. The natural sequence variation separating such a pair, in turn, can be mapped onto protein structure to guide an experimental survey to elucidate important substitutions underlying functionally divergent events. To gain insights into the evolutionary origins of the terpene cyclization mechanism, a pair of terpene synthase homologues were identified from _A. annua_ that differ in their biochemical phenotypes ([Fig. 1](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0005)A). Specifically, amorpha-4,11-diene synthase (ADS), a prototypical ‘cyclase’, which converts a linear substrate [farnesyl pyrophosphate](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/farnesyl-pyrophosphate) (FPP) into a multi-cyclic hydrocarbon amorpha-4,11-diene, the precursor to the antimalarial compound [artemisinin](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/artemisinin). In contrast, (_E_)-β-farnesene synthase (BFS) produces a linear product (_E_)-β-farnesene from FPP, lacking the ability to activate the generalized cyclization reaction. Despite their functional differences, these two enzymes share ca. 50% sequence identity including the structurally conserved terpene synthase fold typical of the greater family [[34]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0170), [[35]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0175). A focused gene library synthesis approach was employed to sample ADS substitutions in the background of BFS to identify functionally important [amino acid](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/amino-acid) residues that confer the cyclization phenotype in an otherwise linear product-producing enzyme.

### 2.2. Iterative breeding − introgression and backcrosses
To simulate traditional breeding approaches, we applied structure-based combinatorial protein engineering (SCOPE) [[36]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0180), [[37]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0185), to perform iterative rounds of ‘introgression’ (incorporating ADS substitutions into structurally-equivalent positions in BFS) then ‘backcrossing’ to remove extraneous ADS substitutions not contributing to the phenotypic change (i.e. cyclization versus linear product formation). Phenotypic screening using gas chromatography-mass spectrometry [[38]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0190) enabled detection of cyclic hydrocarbons. It is worth noting alternative, high throughput functional screens for terpene synthases have been recently developed using [carotenoid](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/carotenoid) pigment formation in yeast [[39]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0195) or modified substrates for in vitro measurements [[40]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0200) for activity measurements. However, [mass spectrometry](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/mass-spectrometry) methods are currently necessary to characterize the linear (or cyclic) structure of terpene products. In our breeding example, each round of [introgression](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/introgression) and backcrossing produced a variant with minimal substitutions (a single-point mutation in this case) that conferred a phenotypic switch (e.g. linear or cyclic products) that was carried forward as the new parental background in the next iteration ([Fig. 1](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0005)B). This process outlines how one can sequentially identify mutations that confer a gain of function (activation), reversion to the wild type (suppression), and re-gain of function (re-activation) as alternating phenotypic layers.

### 2.3. Isolation of a sub-network of amino acid residues
The result of applying an iterative breeding strategy to a pair of plant terpene synthase enzymes was the isolation of a sub-network of [amino acid](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/amino-acids) residues that control the emergence of cyclization in _A. annua_ ([Fig. 1](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0005)C). Qualitative examination of phenotypic data revealed a pattern of interactions between mutations that were agonistic, promoting the same phenotype (i.e. cyclization), or antagonistic interactions, counteracting effects on activation versus suppression of cyclization. These agonistic and antagonistic mutational effects provided a basis for developing structural and mechanistic hypotheses, as discussed later. A single ‘gateway’ mutation (Y402L) may activate cyclization in BFS, yet a corresponding mutation of a modifier position (Y430A) ensured the persistence of a newly emerged cyclization phenotype. From the pattern of interactions, the modifier suppressed the second site suppressor (V467G) while promoting cyclization of the gateway mutation (Y402L) through antagonistic and agonistic interactions, respectively. Viewed as a Punnet square, the interaction between alleles at position 402 and 467 shows a pattern reminiscent of a [monohybrid cross](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/monohybrid-cross) where the F2 generation exhibits a 3:1 ratio of dominant to recessive phenotypes, corresponding to linear versus cyclic products, respectively ([Fig. 1](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0005)D). However, the dominance of V467G over position 402 is broken in the Y430A background, leaving the cyclization reaction under independent control by the 402 locus. These results provide a compelling basis to further examine epistasis in the greater terpene synthase enzyme family, given the discovery of specificity switches from single mutations in mono- and di-terpene synthases [[41]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0205), [[42]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0210), enzyme utilizing linear C10 and C20 substrates, respectively.

### 2.4. Modularizing epistasis: transplanting epistatic networks into other homologues
Experimental isolation of epistatic networks allows the effective modularization epistasis; treating the network as a unit, and then to examine the behavior of epistatic networks across different protein backgrounds by mutating structurally equivalent positions in other homologues. Taking this approach, we mutated residues within the 402-430-467 network in a BFS homologue from [Citrus junos](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/citrus-junos) that shares 51% sequence identity with _A. annua_ BFS and observed strong epistasis among these residue positions. Therefore, this ‘module’ controlled the activation of the cyclization mechanism in other terpene synthase backgrounds. However the functional roles of residue positions shifted markedly. Most dramatically, position 467, which was a second site suppressor in _A. annua_, acted as a gateway mutation in _C. junos_, activating cyclization in this homologue. This result suggests that cyclization may have emerged independently in different plant lineages by alternative mutational trajectories within a common, modular epistatic network. This observation underscores the shifting epistatic character of the evolving protein background in otherwise structurally conserved enzymes. This in turn points to a more general approach to systematically exploring the effects of epistatic residue networks throughout protein families that share a common structural architecture.

## 3. Quantitative analysis of epistasis
The contrasting and non-additive phenotypic effects of mutations in biochemical and [genetic](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/genetics) studies qualitatively reveal the forces of epistasis. However, a formal quantitative definition is essential for developing a common language (and metric) that enables meaningful cross comparison between biochemical systems. This is currently a vibrant and critical area of theoretical investigation that is formalizing our mathematical description of epistasis in the evolutionary pathways of enzymes [[43]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0215). As such, we can now mathematically define precise terms to capture “our surprise at the phenotype when mutations are combined, given the constituent mutations’ individual effects” [[19]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0095).

### 3.1. Quantification of epistasis
Given the phenotype or the fitness criterion under consideration, a multiplicative or additive model of epistasis can be chosen to use under the null model (absence of epistasis) [[44]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0220). We recommend evaluating both models to assess how each fits the data. This can be based on the trait (“phenotype”) and the distribution of its values. For instance, a phenotype such as growth can be better explained by “multiplicative” (logarithmic) model. In particular, according to a multiplicative fitness model [[45]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0225), two mutations (A and B) with wild-type fitness (_F_0) are considered independent if the fitness effect of the combined mutation equals the product of the individual fitness effect. If the fitness effect of each single mutation is defined as FA/F0 and FB/F0, and the effect of double mutant is defined as FAB/F0, then mutational independence implies:FAF0FBF0=FABF0

Then one can quantify the amount of epistasis as the deviation (ε) from the above equality which is zero when the combined effect of a double mutation equals the product of the individual contribution on fitness, such that:ε=log(F0FABFAFB)

So positive (ε>0) and negative (ε<0) values imply synergistic and antagonistic epistasis, respectively.

### 3.2. Higher-order epistasis
To capture higher-order epistatic interactions, viz. the contribution of multi-way epistatic interactions for a combinatorially complete set of mutations, a Fourier (polynomial) expansion analysis can be employed as described for our BFS example [[17]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0085) using previously developed formulations [[46]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0230). This requires a function that maps a binary string (b) to fitness, written as an expansion in terms of both main effects and the interaction between individual _L_ sites. For a given experimental data set with phenotype measurements of fitness for a combination of _L_ sites (loci), this can be denoted as binary strings taking two possible values (0 or 1) to indicate the absence and presence of a mutation in each string to represent a given genotype. The resulting genotype space can then be considered as a multi-dimensional object with 2L vertices. For example, with three sites the following expansion maps fitness function as a Fourier expansion:F(b)=FWT+∑ai(1)βi+∑βiβjaij(2)+∑βiβjβkaijk(3)where βi∈{0,1} denotes a variant to indicate the absence or presence of a mutation at a given site. The first order coefficient a(1) in the expansion captures the linear, non-epistatic effects. The second order coefficient a(2) denotes the pairwise epistatic contribution and a(3) is a three-way epistatic interaction. In total there are 2L coefficients. One can determine coefficients in turn by solving a system of linear equations. Coefficients can be calculated in the βi∈{0,1} basis to define an epistasis-free landscape for reference by summing-up only the constant and first order terms while predicting the fitted landscape. The fitted Fourier coefficients and contribution of different orders of epistasis (pairwise, three way, etc.) truly captures global epistasis of landscapes for a given phenotype. Other approaches have estimated multi-way, higher-order epistasis by performing a Walsh Transform on fitness values leading to a prescient conclusion that pairwise epistatic interactions cannot capture or fully explain higher-order epistasis [[19]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0095). The importance of this conclusion is underscored by observations of significant and substantive amounts of higher-order epistasis in many biological systems [[19]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0095), [[47]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0235), [[48]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0240).

### 3.3. Visualizing epistatic interactions
Making complex, epistatic interactions visually accessible is an important area of development. New tools have been crafted that allow the visualization of genetic interactions in large-scale association studies [[49]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0245) and statistical epistasis networks [[50]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0250). In our BFS example, we devised a plot to visualize the effects of epistasis in comparison to a reference non-epistatic landscape ([Fig. 2](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0010)) [[17]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0085). This diagram reveals the profound distortion caused by epistasis from visual inspection of the deviation from an idealized epistatic-free landscape. Importantly, one can then readily compare the pattern of epistatic interactions among a network of equivalent residues between homologues, such as _A. annua_ and _C. junos_ in our example. Simple visual diagrams, such as this one, highlight the constraining effect of epistasis to reach a more general audience. More recently, selection-weighted attraction graphing has been developed to capture more complex visualizations of higher dimensional fitness landscapes [[51]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0255).

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710065109559-e136de88-73ee-4205-ac01-84f2d4ce26b5.jpeg)

1. [Download : Download high-res image (208KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0168945216306495-gr2_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0168945216306495-gr2.jpg)

Fig. 2. Visualizing fitness landscape analysis of an epistatic residue interaction network. The fitness effects of mutations among residue positions 402, 467, and 430 (the 402–467-430 epistatic network) were calculated using % cyclization as a proxy for fitness for (A) _A. annua_ and (B) _C. junos_ BFS homologues relative to their respective wild type proteins. The epistatic effects are plotted overtop of non-epistatic networks (shaded cubes for reference). Of note, the cubes differ since the effects of individual mutations in each background differ. Blue and red lines denote gain and loss of fitness, respectively. Figure adapted with permission from Salmon et al. [[13]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0065). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

## 4. Building biophysical models of epistatic systems
Constructing biophysical and biochemical models of epistasis is critical for developing a first principles understanding of this phenomenon. This, in turn, enables inferences into how constraining forces shape evolutionary pathways. Computational investigations have enabled broad reach in surveying epistasis in massive theoretical populations highlighting contingency in evolution [[52]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0260). Experimental dissection of epistasis in the [glucocorticoid receptor](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/glucocorticoid-receptor) illustrates this point to atomic scale resolution. The biochemical and crystallographic characterization of ancestral enzymes uncovered ‘permissive’ mutations that have minimal impact on receptor function. Once other changes in the protein background were in place, they enabled functionally important (dominant) mutations to be structurally tolerated and take affect [[31]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0155). Though these and other structural models make important contributions to the definition of more general biophysical principles of epistasis, more are needed to incorporate unique elements of the biochemical system under study − from the [protein fold](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/protein-folds) to the reactions catalyzed by enzyme families.

### 4.1. Gateway mutation unlocks the substrate to cyclization
[Homology modelling](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/homology-modeling) and substrate docking in our example provided a starting point to physically reconstruct the emergence of the terpene cyclization in a putative BFS progenitor ([Fig. 3](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0015)). Analysis of our model suggested a mechanistic explanation for the dominance of the Y402L gateway mutation activating cyclization in the BFS wild type background. The spatial proximity of Y402L to the [pyrophosphate](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/pyrophosphate) and proximal end of the substrate, the site where bond breaking and making occurs, suggests a strong influence of steric effects. The Y402L mutation effectively creates space in this active site region necessary for an [isomerization](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/isomerization) step, which critically ‘unlocks’ the substrate for cyclization. An allelic series supported this notion. The presence of bulky aromatic residues (Phe, Tyr, Trp) blocks cyclization whereas substitutions of decreasing size (Leu, Val, Ile, and Ala) progressively promote cyclization. However, the manner in which V467G and Y430A suppress and re-activate cyclization, respectively, is unclear from this model given the distance of these residue positions (ca. 10 Å) from the Y402L mutation. This observation suggests that epistatic interactions are mediated through the protein, consistent with documented long-range non-additive interactions among residues in proteins [[53]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0265). Intriguingly this observation also implicates the role of the ligand in the evolution of terpene synthase enzymes and other enzyme families more generally, where the underlying chemical mechanisms demand inclusion in physical models of epistatic phenomena.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710065109605-52016ae9-edb3-4693-953c-15ccb0ec863b.jpeg)

1. [Download : Download high-res image (433KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0168945216306495-gr3_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0168945216306495-gr3.jpg)

Fig. 3. Structural model of proposed mechanism of substrate unlocking by position 402. (A) Global 3-dimensional model of a terpene synthase enzyme (BFS) shown as a [ribbon diagram](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/ribbon-diagram) colored grey and yellow to indicate the N- and C-terminal domains, respectively. (B) Spatial positions of the 402–467-430 network mapped onto a structural model of the _A. annua_ BFS active site. (C) Proposed mechanism of substrate unlocking by the Y402L mutation involving (1) ionization of [pyrophosphate](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/pyrophosphate), (2) recapture of pyrophosphate at C3 to form the neutral intermediate nerolidyl pyrophosphate (NPP), (3) rotation of the 2,3-σ bond, (4) re-ionization to form the cisoid carbocation and (5) 1,6 cyclization to the bisabolyl cation that parents the observed diversity of cyclic terpene products. The synthesis of cyclic products is dependent on rotation (isomerization) of the 2,3-σ bond of NPP. This operation unlocks the trans conformation of the ligand, which can then undergo cyclization to form the ubiquitous bisabolyl cation precursor of cyclic terpenes. In the absence of the Y402L mutation, [isomerization](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/isomerization) cannot occur, leaving the substrate in a locked conformation only activated for the formation of linear products. Figure adapted with permission from Salmon et al. [[13]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0065). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

### 4.2. Ligand contributes to epistasis
The fact that the ligand participates in epistatic interactions highlights the adaptability of the terpene synthase family in creating a diverse range of chemical structures through the interplay of intrinsic reactivity of the substrate and the evolving protein background [[54]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0270). Delineation of a stereochemical blueprint for cyclization chemistry serves as a critical guide [[55]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0275). Terpene cyclization involves transient carbocation intermediates that currently escape direct biochemical measurement [[56]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0280). [Quantum mechanics](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/quantum-mechanics) does offer a computational means to spatially and energetically reconstruct cyclization pathways inferred from the known stereochemistry of the products [[56]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0280). The staggering complexity of these reactions is vividly illustrated in the cyclization of the bisabolyl cation [[57]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0285) − a central intermediate in the cyclization mechanism emerging from BFS Y402L in our example. These calculated structures provide a physical basis for constructing new enzyme-complex models that incorporate the key chemical transition structures into protein active sites. Indeed, physical models of unstable carbocationic intermediates have been constructed for tobacco 5-_epi_-aristolochene synthase, both for the native transoid and alternative, cisoid cyclization pathways [[58]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0290). Major advances demonstrate the integration of quantum mechanics methods with structural analysis to yield powerful tools for computational-guided discovery of terpene synthase functions [[59]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0295). The recent development of the first high-resolution model for the reaction intermediates in the active site of tobacco 5-_epi_-aristolochene synthase [[60]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0300) set the stage for an integrated system to link protein epistasis from catalytic landscapes [[32]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0160) with the chemical transformations of an evolving enzyme lineage.

### 4.3. Negative catalysis by terpene synthase enzymes
The emerging picture from quantum mechanics studies and structural analysis is that highly reactive carbocation intermediates have many competing cyclization pathways of similar energies, sometimes with multiple products arising from a common transition structure. This is illustrated in miltiradiene [biosynthesis](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/anabolism)[[61]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0305) and by the eudesm-5-yl cation, which parents a diverse collection of [phytoalexins](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/phytoalexin) in the [Solanaceae](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/solanaceae)[[62]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0310). These observations suggest that terpene synthase enzymes operate by negative catalysis [[63]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0315). The enzyme actively excludes some cyclization pathways by spatial and stereoelectronic effects. Intriguingly, the reactivity of carbocations introduces a further constraint given the potential for [alkylation](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/alkylation) of the active site akin to a suicide inhibitor [[64]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0320). Collectively, these observations carry implications for understanding the evolutionary capacity of terpene synthase enzymes and the critical importance of substrate pre-organization by the enzyme in achieving product specificity. While negative catalysis may have a pronounced effect on the product specificity of terpene synthases, active site mutations likely impact the substrate selectivity of other enzyme classes.

## 5. Epistasis in the emergence and specialization of protein function
Epistasis clearly plays a significant role in the specialization of terpene synthase function. This is readily apparent from experiments exploring natural sequence variation in the outer tiers of protein structure of [Nicotiana](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/nicotiana)_ tabbacum_ 5-_epi_-aristolochene synthase, an enzyme that synthesizes a hydrocarbon precursor of plant defence compounds [[32]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0160). This study highlights mutational control of a ‘late’ carbocation intermediate along the cyclization mechanism, and suggests a probable role of promiscuous intermediates in diversification events. By contrast, engineering experiments using active site saturation [mutagenesis](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/mutagenesis) on a highly promiscuous γ-humulene synthase progenitor, an enzyme from [Abies grandis](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/abies-grandis) involved in [oleoresin](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/oleoresins) production, suggest the importance of incremental, [additive effects](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/additive-effect) of mutations in designed [divergent evolution](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/divergent-evolution) of specialized function [[65]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0325). Further investigation of the contributions of additive and epistatic effects in terpene synthase specialization is needed, in particular, tracing mutational pathways extending from generalists, like Y402L BFS to specialists enzymes in _A. annua_ (i.e. ADS), incorporating ancestral states for the enzyme background and functionally amino acid positions.

### 5.1. BFS as a progenitor
The experimental isolation of epistatic networks coupled with biophysical models of protein structure and substrate reactivity provide a platform for developing a speculative scenario describing the emergence of cyclization and specialization of function in the [Asteraceae](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/asteraceae) ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0020)). Accordingly, BFS − the mechanistically simplest terpene synthase, acquired the Y402L gateway mutation, thereby converting a specialist enzyme to a generalist, capable of generating 15 distinct cyclic terpenes ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0020)A). The modifier mutation Y430A may have preceded this event, priming the basic protein background for cyclization by counteracting suppressive mutations such as V467G. The appearance of a promiscuous generalist, often ascribed as the progenitor of subsequent specialists [[66]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0330), endowed an ancestral plant with an expanded repertoire of specialized metabolites, likely imparting adaptive advantages in different ecological niches. [Natural selection](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/natural-selection), in turn, could select mutations appearing in the nascent generalist, enhancing [enzyme specificity](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-specificity) and promoting higher yields of beneficial compounds.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710065109742-b883ce0d-c2ee-45ac-a60d-092759985f27.jpeg)

1. [Download : Download high-res image (376KB)](https://ars.els-cdn.com/content/image/1-s2.0-S0168945216306495-gr4_lrg.jpg)
2. [Download : Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S0168945216306495-gr4.jpg)

Fig. 4. Speculative model of the emergence and specialization of terpene synthase enzymes in the _Asteraceae_. (A) _Asteraceae_ terpene synthase enzymes produce numerous cyclic products (dark green spheres) from the bisabolyl cation (orange sphere), sometimes involving intervening carbocation intermediates (light green spheres) along cyclization pathways. BFS Y402L generates 15 distinct cyclic products 11 of which have been identified are shown. The pathways of BFS Y402L and ADS are outlined with light and darker green shading, respectively. (B) A Y402L BFS generalist ancestor parents several cyclic terpene producing specialist (cyclases). A stylized [phylogenetic tree](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/phylogenetic-tree) depicts the relationships between modern _Asteraceae_[cyclases](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/cyclase), adapted from Salmon et al. [[13]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0065). Enzyme names (GAS, [germacrene](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/germacrene) A synthase; 8ECS, 8-_epi_-cedrol synthase; BCS, β-caryophylene synthase; ADS, amorpha-4,11-diene synthase; GBS, (_Z_)-γ-bisabolene synthase; BOS, α-bisabolol synthase; and BFS, (_E_)-β-farnesene synthase) are abbreviate for simplicity. (C) A theoretical model positing the progressive changes in substrate folding induced by accumulating mutations along a putative evolutionary trajectory leading from a BFS progenitor, through a 1,6 cyclase intermediate (i.e. α-bisabolol synthase), before arriving at the modern ADS activity, where the substrate fold minimizes the interatomic distance between reacting carbons in the pre-organized fold. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

### 5.2. Folding a pathway to specialization
The unique appearance of the Y402L gateway mutation among a branch of terpene synthases in Asteraceae, correlates with shared mechanistic relationships involving a 1,6 cyclization, as typified by the recently discovered (_Z_)-γ-bisabolene synthase in [Helianthus](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/helianthus)[[67]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0335). Such observations support the hypothesis that a BFS progenitor gave rise to these extant enzymes ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0020)B). However, the mutational pathway leading from a putative ancestral BFS Y402L generalist to specialist enzymes such as [ADS](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/amorpha), which predominantly form a single product, remain an open question. The mutational pathway to specialization likely remodelled the [enzyme active site](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/enzyme-active-site) leading to the progressive refolding of the substrate ([Fig. 4](https://www.sciencedirect.com/science/article/pii/S0168945216306495#fig0020)C). The spatial requirements for cyclization to ADS lead us to posit that accumulating mutations progressively enforce a more compact and folded substrate-binding conformation. Accordingly, a more extended conformation of [FPP](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/farnesyl-pyrophosphate) in BFS was likely reshaped by subsequent mutations following Y402L through an intermediary state, pre-organizing α-bisabolol and (Z)-γ-bisabolene synthase-like activities, before achieving the requisite fold that pre-organizes cyclization to amorpha-4,11-diene. Crystallographic snapshots and structural models augmented with transition structures calculated via [quantum mechanics](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/quantum-mechanics) for cyclization pathways will be essential for testing this hypothesis at atomic scale resolution to enable dissection of the epistatic contribution to terpene synthase specialization.

### 5.3. Window of opportunity − point of no return
The BFS narrative illustrates a common principle of the constraining forces of epistasis on protein evolution. The dominant Y402L gateway mutation provides a window of opportunity for the emergence of new catalytic function when falling in the right background of an _Asteraceae_ terpene synthase. This accentuates the importance of historical contingency. Perhaps it is unsurprising that the reciprocal L402Y mutation in ADS fails to revert this enzyme to a linear product producer similar to wild type BFS, given the extensive accumulation of substitutions in the ADS background after divergence from a common ancestor. The L402Y substitution in ADS only has marginal effects on product specificity; amorpha-4,11-diene remains the dominant product despite [catalytic efficiency](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/catalytic-efficiency) being notably impaired. Extensive [mutagenesis](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/mutagenesis) studies in ADS resulted in most substitutions that deactivate the enzyme, with little or no effect on product specificity [[68]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0340). These observations suggest that a point of no return was reached somewhere along the mutational pathway to ADS. Mutation back to the ancestral function was blocked at this point by epistatic constraints and the dominant functional role of position 402 was lost. Therefore, accumulated mutations in the protein background of ADS attenuate the mutational effects of position 402. This principle is a commonly emerging theme from discoveries in other biochemical systems, such as evolving glucocorticoid receptors [[69]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0345), and brought into focus by rigorous studies of [phosphoglycerate kinase](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/phosphoglycerate-kinase), where the incompatibility of the protein background may reject [amino acid substitutions](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/amino-acid-substitution)[[33]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bib0165).

## 6. Outlook
Great strides have been made in the experimental and theoretical analysis of dominance and epistasis, yet we must continue to widely sow seed. Rooting these investigations in natural sequence variation will contextualize the problem and yield new insights into the natural history of enzyme families underlying adaptation and survival. Modularizing epistasis into simplified networks and casting them into extant, ancestral and computer-generated [protein folds](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/protein-folds) may yet reveal discernible hierarchical structures that propagate through sequence space, aiding our limited capacity to predict and control. A mechanistic understanding of epistasis based on physical and chemical principles coupled with a common mathematical and visual language will be essential for developing a unified framework aimed at examining epistasis across differing scales of organization, from proteins, metabolic pathways and [gene regulatory networks](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/gene-regulatory-network) to ecological connectivity. This massive future effort must engage researchers across diverse disciplines, as we look to reconstruct the evolutionary past and author genomes for a healthy and bountiful future.

## Acknowledgements
We wish to dedicate this work to the late Chris Lamb, FRS. We acknowledge support from the Biotechnology and Biological Sciences Research Council grant [BB/K003690/1](https://www.sciencedirect.com/science/article/pii/S0168945216306495#gs0005) and the Institute Strategic Program Grants [BB/J004561/1](https://www.sciencedirect.com/science/article/pii/S0168945216306495#gs0010) (Understanding and Exploiting Plant and Microbial Secondary Metabolism) at JIC and BB/I015345/1 (Food and Health) at IFR. We also thank the John Innes Foundation and the John Innes Centre, Norwich.

## References
1. [[1]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0005)

Biology and applications of crispr systems: harnessing nature's toolbox for genome engineering

Cell, 164 (2016), pp. 29-44

2. [[2]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0010)

J.B. Holland

Genetic architecture of complex traits in plants

Curr. Opin. Plant Biol., 10 (2007), pp. 156-161

3. [[3]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0015)

J.F. Crow

Genetics of insect resistance to chemicals

Annu. Rev. Entomol., 2 (1957), pp. 227-246

4. [[4]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0020)

C. Bank, R.T. Hietpas, J.D. Jensen, D.N.A. Bolon

A systematic survey of an intragenic epistatic landscape

Mol. Biol. Evol., 32 (2014), pp. 229-238

[Google Scholar](https://scholar.google.com/scholar_lookup?title=A%20systematic%20survey%20of%20an%20intragenic%20epistatic%20landscape&publication_year=2014&author=C.%20Bank&author=R.T.%20Hietpas&author=J.D.%20Jensen&author=D.N.A.%20Bolon)

5. [[5]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0025)

E. Zuckerkandl, L. Pauling

Evolutionary Divergence and Convergence in Proteins

Elsevier, New York (1965)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Evolutionary%20Divergence%20and%20Convergence%20in%20Proteins&publication_year=1965&author=E.%20Zuckerkandl&author=L.%20Pauling)

6. [[6]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0030)

W. Bateson, E.R. Saunders, R.C. Punnett, C.C. Hurst

Reports to the Evolution Committee of the Royal Society, Report ii

Harrison and Sons, London UK (1905)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Reports%20to%20the%20Evolution%20Committee%20of%20the%20Royal%20Society%2C%20Report%20ii&publication_year=1905&author=W.%20Bateson&author=E.R.%20Saunders&author=R.C.%20Punnett&author=C.C.%20Hurst)

7. [[7]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0035)

J.A.G.M. De Visser, T.F. Cooper, S.F. Elena

The causes of epistasis

Proc. Biol. Sci., 278 (2011), pp. 3617-3624

8. [[8]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0040)

S. Wright

The roles of mutation, inbreeding, crossbreeding, and selection in evolution

Proceedings of the Sixth International Congress on Genetics (1932), pp. 355-366

[Google Scholar](https://scholar.google.com/scholar_lookup?title=The%20roles%20of%20mutation%2C%20inbreeding%2C%20crossbreeding%2C%20and%20selection%20in%20evolution&publication_year=1932&author=S.%20Wright)

9. [[9]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0045)

J.-K. Weng, R.N. Philippe, J.P. Noel

The rise of chemodiversity in plants

Science, 336 (2012), pp. 1667-1670

10. [[10]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0050)

J.D. Connolly, R.A. Hill

Dictionary of Terpenoids

Chapman & Hall, New York (1992)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Dictionary%20of%20Terpenoids&publication_year=1992&author=J.D.%20Connolly&author=R.A.%20Hill)

11. [[11]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0055)

E. Pichersky, J. Gershenzon

The formation and function of plant volatiles: perfumes for pollinator attraction and defense

Curr. Opin. Plant Biol., 5 (2002), pp. 237-243

12. [[12]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0060)

C.M. De Moraes, W.J. Lewis, P.W. Pare, H.T. Alborn, J.H. Tumlinson

Herbivore-infested plants selectively attract parasitoids

Nature, 393 (1998), pp. 570-573

13. [[13]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0065)

K. Tomiyama, _ et al._

A new antifungal substance isolated from resistant potato tuber tissue infected by pathogens

Phytopathology, 58 (1968), pp. 115-116

[Google Scholar](https://scholar.google.com/scholar_lookup?title=A%20new%20antifungal%20substance%20isolated%20from%20resistant%20potato%20tuber%20tissue%20infected%20by%20pathogens&publication_year=1968&author=K.%20Tomiyama)

14. [[14]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0070)

K. Akiyama, K. Matsuzaki, H. Hayashi

Plant sesquiterpenes induce hyphal branching in arbuscular mycorrhizal fungi

Nature, 435 (2005), pp. 824-827

15. [[15]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0075)

J. Degenhardt, T.G. Kollner, J. Gershenzon

Monoterpene and sesquiterpene synthases and the origin of terpene skeletal diversity in plants

Phytochemistry, 70 (2009), pp. 1621-1637

16. [[16]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0080)

P. Zerbe, J. Bohlmann

Plant diterpene synthases: exploring modularity and metabolic diversity for bioengineering

Trends Biotechnol., 33 (2015), pp. 419-428

17. [[17]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0085)

M. Salmon, _ et al._

Emergence of terpene cyclization in artemisia annua

Nat. Commun., 6 (2015), pp. 1-10

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Emergence%20of%20terpene%20cyclization%20in%20artemisia%20annua&publication_year=2015&author=M.%20Salmon)

18. [[18]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0090)

M.B. Taylor, I.M. Ehrenreich

Higher-order genetic interactions and their contribution to complex traits

Trends Genet., 31 (2015), pp. 34-40

19. [[19]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0095)

D.M. Weinreich, Y. Lan, C.S. Wylie, R.B. Heckendorn

Should evolutionary geneticists worry about higher-order epistasis?

Curr. Opin. Genet. Dev., 23 (2013), pp. 700-707

20. [[20]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0100)

J.P. Jarvis, J.M. Cheverud

Mapping the epistatic network underlying murine reproductive fatpad variation

Genetics, 187 (2011), pp. 597-610

21. [[21]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0105)

H.C. Rowe, B.G. Hansen, B.A. Halkier, D.J. Kliebenstein

Biochemical networks and epistasis shape the arabidopsis thaliana metabolome

Plant Cell, 20 (2008), pp. 1199-1216

22. [[22]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0110)

R.B. Brem, J.D. Storey, J. Whittle, L. Kruglyak

Genetic interactions between polymorphisms that affect gene expression in yeast

Nature, 436 (2005), pp. 701-703

23. [[23]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0115)

B.E. Gaertner, M.D. Parmenter, M.V. Rockman, L. Kruglyak, P.C. Phillips

More than the sum of its parts: a complex epistatic network underlies natural variation in thermal preference behavior in caenorhabditis elegans

Genetics, 192 (2012), pp. 1533-1542

24. [[24]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0120)

A.L. Caicedo, J.R. Stinchcombe, K.M. Olsen, J. Schmitt, M.D. Purugganan

Epistatic interaction between arabidopsis fri and flc flowering time genes generates a latitudinal cline in a life history trait

Proc. Nat. Acad. Sci. U. S. A., 101 (2004), pp. 15670-15675

25. [[25]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0125)

J.L. Porter, R.A. Rusli, D.L. Ollis

Directed evolution of enzymes for industrial biocatalysis

Chembiochem, 17 (2016), pp. 197-203

26. [[26]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0130)

T.J. Magliery

Protein stability: computation, sequence statistics, and new experimental methods

Curr. Opin. Struct. Biol., 33 (2015), pp. 161-168

27. [[27]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0135)

H. Xiao, Z.H. Bao, H.M. Zhao

High throughput screening and selection methods for directed enzyme evolution

Ind. Eng. Chem. Res., 54 (2015), pp. 4011-4020

28. [[28]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0140)

A. Currin, N. Swainston, P.J. Day, D.B. Kell

Synthetic biology for the directed evolution of protein biocatalysts: navigating sequence space intelligently

Chem. Soc. Rev., 44 (2015), pp. 1172-1239

29. [[29]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0145)

M. Lunzer, G.B. Golding, A.M. Dean

Pervasive cryptic epistasis in molecular evolution

PLoS Genet., 6 (2010), p. e1001162

30. [[30]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0150)

A.I. Podgornaia, M.T. Laub

Protein evolution. Pervasive degeneracy and epistasis in a protein-protein interface

Science, 347 (2015), pp. 673-677

31. [[31]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0155)

E.A. Ortlund, J.T. Bridgham, M.R. Redinbo, J.W. Thornton

Crystal structure of an ancient protein: evolution by conformational epistasis

Science, 317 (2007), pp. 1544-1548

32. [[32]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0160)

P.E. O'Maille, _ et al._

Quantitative exploration of the catalytic landscape separating divergent plant sesquiterpene synthases

Nat. Chem. Biol., 4 (2008), pp. 617-623

33. [[33]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0165)

A. Wellner, M. Raitses Gurevich, D.S. Tawfik

Mechanisms of protein sequence divergence and incompatibility

PLoS Genet., 9 (2013), p. e1003665

34. [[34]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0170)

Y. Gao, R.B. Honzatko, R.J. Peters

Terpenoid synthase structures: a so far incomplete view of complex catalysis

Nat. Prod. Rep., 29 (2012), pp. 1153-1175

35. [[35]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0175)

D.W. Christianson

Unearthing the roots of the terpenome

Curr. Opin. Chem. Biol., 12 (2008), pp. 141-150

36. [[36]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0180)

M. Dokarry, C. Laurendon, P.E. O'Maille

Automating gene library synthesis by structure-based combinatorial protein engineering: examples from plant sesquiterpene synthases

Meth. Enzymol., 515 (2012), pp. 21-42

37. [[37]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0185)

P.E. O'Maille, M. Bakhtina, M.D. Tsai

Structure-based combinatorial protein engineering (scope)

J. Mol. Biol., 321 (2002), pp. 677-691

38. [[38]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0190)

P.E. O'Maille, J. Chappell, J.P. Noel

A single-vial analytical and quantitative gas chromatography-mass spectrometry assay for terpene synthases

Anal. Biochem., 335 (2004), pp. 210-217

39. [[39]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0195)

M. Furubayashi, _ et al._

A high-throughput colorimetric screening assay for terpene synthase activity based on substrate consumption

PLoS One, 9 (2014), pp. e93317-93311

40. [[40]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0200)

R. Lauchli, _ et al._

High-throughput screening for terpene-synthase-cyclization activity and directed evolution of a terpene synthase

Angew. Chem. Int. Ed., 52 (2013), pp. 5571-5574

41. [[41]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0205)

S.C. Kampranis, _ et al._

Rational conversion of substrate and product specificity in a salvia monoterpene synthase: structural insights into the evolution of terpene synthase function

Plant Cell, 19 (2007), pp. 1994-2005

42. [[42]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0210)

M. Xu, P.R. Wilderman, R.J. Peters

Following evolution's lead to a single residue switch for diterpene synthase product outcome

Proc. Nat. Acad. Sci. U. S. A., 104 (2007), pp. 7397-7401

43. [[43]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0215)

D.A. Kondrashov, F.A. Kondrashov

Topological features of rugged fitness landscapes in sequence space

Trends Genet., 31 (2015), pp. 24-33

44. [[44]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0220)

B. Ostman, A. Hintze, C. Adami

Impact of epistasis and pleiotropy on evolutionary adaptation

Proc. Biol. Sci., 279 (2012), pp. 247-256

45. [[45]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0225)

J.F. Crow, M. Kimura

An Introduction to Population Genetics Theory

Blackburn Press (2009)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=An%20Introduction%20to%20Population%20Genetics%20Theory&publication_year=2009&author=J.F.%20Crow&author=M.%20Kimura)

46. [[46]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0230)

I.G. Szendro, M.F. Schenk, J. Franke, J. Krug, J. de Visser

Quantitative analyses of empirical fitness landscapes

J. Stat. Mech.—Theory Exp. (2013), p. 22

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Quantitative%20analyses%20of%20empirical%20fitness%20landscapes&publication_year=2013&author=I.G.%20Szendro&author=M.F.%20Schenk&author=J.%20Franke&author=J.%20Krug&author=J.%20de%20Visser)

47. [[47]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0235)

D.L. Hartl

What can we learn from fitness landscapes?

Curr. Opin. Microbiol., 21 (2014), pp. 51-57

48. [[48]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0240)

O. Haq, R.M. Levy, A.V. Morozov, M. Andrec

Pairwise and higher-order correlations among drug-resistance mutations in hiv-1 subtype b protease

BMC Bioinf., 10 (2009), pp. S10-14

49. [[49]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0245)

Y. Wu, X. Zhu, J. Chen, X. Zhang

Einvis: a visualization tool for analyzing and exploring genetic interactions in large-scale association studies

Genet. Epidemiol., 37 (2013), pp. 675-685

50. [[50]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0250)

T. Hu, Y. Chen, J.W. Kiralis, J.H. Moore

Visen: methodology and software for visualization of statistical epistasis networks

Genet. Epidemiol., 37 (2013), pp. 283-285

51. [[51]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0255)

B. Steinberg, M. Ostermeier

Environmental changes bridge evolutionary valleys

Sci. Adv., 2 (2016)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Environmental%20changes%20bridge%20evolutionary%20valleys&publication_year=2016&author=B.%20Steinberg&author=M.%20Ostermeier)

52. [[52]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0260)

P. Shah, D.M. McCandlish, J.B. Plotkin

Contingency and entrenchment in protein evolution under purifying selection

Proc. Natl. Acad. Sci. U. S. A., 112 (2015), pp. E3226-3235

53. [[53]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0265)

A.Y. Istomin, M.M. Gromiha, O.K. Vorov, D.J. Jacobs, D.R. Livesay

New insight into long-range nonadditivity within protein double-mutant cycles

Proteins, 70 (2007), pp. 915-924

[Google Scholar](https://scholar.google.com/scholar_lookup?title=New%20insight%20into%20long-range%20nonadditivity%20within%20protein%20double-mutant%20cycles&publication_year=2007&author=A.Y.%20Istomin&author=M.M.%20Gromiha&author=O.K.%20Vorov&author=D.J.%20Jacobs&author=D.R.%20Livesay)

54. [[54]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0270)

M.B. Austin, P.E. O'Maille, J.P. Noel

Evolving biosynthetic tangos negotiate mechanistic landscapes

Nat. Chem. Biol., 4 (2008), pp. 217-222

55. [[55]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0275)

D.E. Cane

Isoprenoid biosynthesis. Stereochemistry of the cyclization of allylic pyrophosphates

Acc. Chem. Res., 18 (1985), pp. 220-226

56. [[56]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0280)

D.J. Tantillo

Biosynthesis via carbocations: theoretical studies on terpene formation

Nat. Prod. Rep., 28 (2011)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Biosynthesis%20via%20carbocations%3A%20theoretical%20studies%20on%20terpene%20formation&publication_year=2011&author=D.J.%20Tantillo)

57. [[57]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0285)

Y.J. Hong, D.J. Tantillo

Consequences of conformational preorganization in sesquiterpene biosynthesis: theoretical studies on the formation of the bisabolene, curcumene, acoradiene, zizaene, cedrene, duprezianene, and sesquithuriferol sesquiterpenes

J. Am. Chem. Soc., 131 (2009), pp. 7999-8015

58. [[58]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0290)

J.P. Noel, _ et al._

Structural elucidation of cisoid and transoid cyclization pathways of a sesquiterpene synthase using 2-fluorofarnesyl diphosphates

ACS Chem. Biol., 5 (2010), pp. 377-392

59. [[59]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0295)

J.-Y. Chow, _ et al._

Computational-guided discovery and characterization of a sesquiterpene synthase from streptomyces clavuligerus

Proc. Nat. Acad. Sci. U. S. A., 112 (2015), pp. 5661-5666

60. [[60]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0300)

T.E. O'Brien, S.J. Bertolani, D.J. Tantillo, J.B. Siegel

Mechanistically informed predictions of binding modes for carbocation intermediates of a sesquiterpene synthase reaction

Chem. Sci., 00 (2016), pp. 1-7

61. [[61]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0305)

Y.J. Hong, D.J. Tantillo

Biosynthetic consequences of multiple sequential post-transition-state bifurcations

Nat. Chem., 6 (2014), pp. 104-111

62. [[62]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0310)

B.A. Hess Jr., L. Smentek, J.P. Noel, P.E. O’Maille

Physical constraints on sesquiterpene diversity arising from cyclization of the eudesm-5-yl carbocation

J. Am. Chem. Soc., 133 (2011), pp. 12632-12641

63. [[63]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0315)

J. Retey

Enzyme reaction selectivity by negative catalysis or how do enzymes deal with highly reactive intermediates?

Angew. Chem. Int. Ed., 29 (1990), pp. 355-361

64. [[64]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0320)

R.D. Kersten, J.K. Diedrich, J.R. Yates, J.P. Noel

Mechanism-based post-translational modification and inactivation in terpene synthases

ACS Chem. Biol., 10 (2015), pp. 2501-2511

65. [[65]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0325)

Y. Yoshikuni, T.E. Ferrin, J.D. Keasling

Designed divergent evolution of enzyme function

Nature, 440 (2006), pp. 1078-1082

66. [[66]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0330)

R.A. Jensen

Enzyme recruitment in evolution of new function

Annu. Rev. Micro., 30 (1976), pp. 409-425

67. [[67]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0335)

A.-K. Aschenbrenner, M. Kwon, J. Conrad, D.-K. Ro, O. Spring

Identification and characterization of two bisabolene synthases from linear glandular trichomes of sunflower (Helianthus annuus l., asteraceae)

Phytochemistry, 124 (2016), pp. 29-37

68. [[68]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0340)

M.K. Julsing, _ et al._

Amorphadiene synthase: probing the active site model with directed mutagenesis

Mathematics and Natural Sciences, University of Groningen (2006)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Amorphadiene%20synthase%3A%20probing%20the%20active%20site%20model%20with%20directed%20mutagenesis&publication_year=2006&author=M.K.%20Julsing)

69. [[69]](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bbib0345)

J.T. Bridgham, E.A. Ortlund, J.W. Thornton

An epistatic ratchet constrains the direction of glucocorticoid receptor evolution

Nature, 461 (2009), pp. 515-519

## Cited by (0)
[1](https://www.sciencedirect.com/science/article/pii/S0168945216306495#bfn0005)

School of Chemistry, Cardiff University, Main Building, Park Place, Cardiff CF10 3AT, UK (Present address).

[View Abstract](https://www.sciencedirect.com/science/article/abs/pii/S0168945216306495)

© 2016 Elsevier Ireland Ltd. All rights reserved.  


> 来自: [REVIEW: Epistasis and dominance in the emergence of catalytic function as exemplified by the evolution of plant terpene synthases - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0168945216306495)
>

