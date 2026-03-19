[https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3)

[s12915-023-01585-3.pdf](https://www.yuque.com/attachments/yuque/0/2024/pdf/22983715/1709451709469-4f2449f7-4481-4673-9865-6e77b1889e53.pdf)

## Abstract
As organisms evolve, the effects of mutations change as a result of epistatic interactions with other mutations accumulated along the line of descent. This can lead to shifts in adaptability or robustness that ultimately shape subsequent evolution. Here, we review recent advances in measuring, modeling, and predicting epistasis along evolutionary trajectories, both in microbial cells and single proteins. We focus on simple patterns of global epistasis that emerge in this data, in which the effects of mutations can be predicted by a small number of variables. The emergence of these patterns offers promise for efforts to model epistasis and predict evolution.

## Predicting evolution requires an understanding of epistasis
Individual mutations often have phenotypic effects that vary widely depending on the genetic background in which they occur, due to interactions with other variants both within the same gene and elsewhere in the genome (Fig. [1](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Fig1); [Box 1](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Sec13)). These genetic interactions, known as epistasis, can provide clues into functional relationships and physical interactions within and between important proteins, pathways, and modules within the cell. For example, epistatic interactions can reflect physical contacts between residues within protein complexes or alterations in the function of enzymes involved in coupled metabolic pathways. This has driven widespread interest in systematic screens for epistasis (e.g., between all pairs of gene deletions in yeast [[1](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR1)]). Numerous studies have shown that epistatic interactions are also common among mutations that accumulate along the line of descent in adapting laboratory microbial populations [[2](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR2), [3](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR3)], and play an important role in a variety of natural evolutionary processes (e.g., in maintaining binding to host cell receptors during the evolution of antibody escape in SARS-CoV-2 [[4](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR4)-[6](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR6)]). Epistasis has the potential to shape the course of evolution by opening up or closing off potential adaptive trajectories, and by collectively shifting the entire distribution of fitness effects (DFE) of new mutations available to the adapting population.

**Fig. 1**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1709451331491-5ab0c1a2-b8f4-43d7-9d89-24a5f2cd7994.png)

Illustration of types of epistasis. See [Box 1](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Sec13) for definitions of these terms

[Full size image](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3/figures/1)

The DFE influences the dynamics of adaptation — for example, the rate of fitness increase or the accumulation of deleterious load — in analytically tractable ways [[7](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR7)-[9](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR9)]. Thus predicting evolutionary dynamics requires predicting how this distribution changes as mutations accumulate during evolution. In recent years, high-throughput experimental techniques have begun to make it possible to empirically quantify these effects (Fig. [2](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Fig2)). This body of work suggests that, even when individual epistatic interactions between specific mutations are largely unpredictable, we may still be able to predict “macroscopic” changes in the DFE as populations evolve, at least in the context of relatively short-term evolution of laboratory microbial populations [[10](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR10)-[13](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR13)]. However, it remains unclear how broadly these patterns will apply across other biological systems or over longer evolutionary timescales.

**Fig. 2**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1709451336363-9f5a1c3b-2715-4bb5-a6a2-cb6215eba51b.png)

Illustration of methods for measuring the fitness effects of a large number of mutations in a number of genetic backgrounds

[Full size image](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3/figures/2)

Whether we are trying to predict how the DFE changes during short-term laboratory adaptation or how the effect of one mutation will differ in two distantly related strain backgrounds, we face a difficult, high-dimensional problem. In the worst-case scenario, the fitness effect of each mutation depends irreducibly on the state of every other locus in the genome. In a best-case scenario, mutations combine additively with respect to fitness, such that predicting the fitness effect of a mutation is as simple as measuring its effect once on any genetic background. Recent evidence suggests that the reality lies between these two extremes: epistasis is common, but structured in a way that sometimes allows us to predict the effects of mutations from relatively few predictors or parameters. These simplified forms of epistasis have been generically termed “global,” “nonspecific,” or “unidimensional” [[14](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR14)-[16](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR16)], though the specific phenomenology depends on the context.

In microbial evolution, the single best predictor of mutational effects is often fitness itself: the effects of mutations and certain aspects of the DFE can sometimes be predicted based only on the fitness of the genetic background on which these effects are measured. The most commonly observed form of fitness-correlated epistasis in microbes is “diminishing-returns,” in which a beneficial mutation is less beneficial on more fit backgrounds ([Box 1](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Sec13)).

In this review, we start with recent studies describing examples of diminishing-returns epistasis, before turning to consider how this work motivates broader questions about epistasis and evolution:

1. 1)

How often do we see fitness-correlated epistasis during evolution? What other patterns of global epistasis emerge over shorter and longer evolutionary timescales?

2. 2)

What models can explain global epistasis?

3. 3)

Can we infer patterns of global epistasis and use them to predict phenotypes or forecast evolutionary outcomes?

## Patterns of global epistasis in microbial evolution experiments
### Diminishing-returns epistasis can explain declining adaptability in evolving populations
A common observation in experimental microbial evolution is declining adaptability: populations tend to adapt quicker at the beginning of an evolution experiment. Further, among closely related strains, the best predictor of adaptability is often the initial fitness of the population, such that populations which have lower initial fitness adapt more quickly (reviewed in Couce and Tenaillon [[17](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR17)]). This pattern is best reflected in the _E. coli_ long-term evolution experiment (LTEE), where the rate of fitness increase has declined dramatically and reproducibly across tens of thousands of generations [[10](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR10), [18](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR18)]. Declining adaptability has also been observed in yeast strains that differ by a few mutations [[14](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR14)], tens of thousands of mutations [[19](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR19)], in different bacteriophage isolates [[20](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR20)] and in panels of bacteria, phages, and yeast that have disruptive or deleterious mutations (often referred to as compensatory adaptation or repair experiments [[21](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR21)-[27](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR27)]).

A potential explanation for patterns of declining adaptability is diminishing-returns epistasis. Diminishing-returns epistasis often manifests as a simple negative linear relationship between the fitness effect of individual mutations and the background fitness and has been observed in many microbial evolution experiments [[2](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR2), [3](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR3), [13](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR13), [14](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR14), [27](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR27)-[34](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR34)]. Wünsche et al. [[12](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR12)] showed that the average strength of beneficial mutations sharply decreased as populations gained fitness in the LTEE by using marker divergence experiments to track the prevalence and effects of beneficial mutations. This experiment convincingly showed that declining adaptability results _primarily_ from a shift in the beneficial DFE due to epistasis, in contrast to the scenario where the number of beneficial mutations decreases while their effects remain constant. Several recent transposon mutagenesis studies have shown a reduction in the beneficial DFE during the LTEE, though we should note that these studies only include loss-of-function mutations [[35](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR35)-[37](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR37)]. A recent study in yeast has also shown that fixation of even a single beneficial mutation can lead to a shift towards a DFE with less beneficial mutations [[13](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR13)].

While evidence for declining adaptability and diminishing-returns epistasis is now widespread, it is useful to identify exceptions to this rule. For example, when Rojas Echenique et al. [[24](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR24)] allowed yeast gene-deletion strains to evolve, initial fitness predicted some, but not all, of the variation in the rate of adaptation: this study found that the functional module in which genes were deleted also played a role (i.e., in some cases two strains with similar initial fitness adapted at significantly different rates). Smith et al. [[38](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR38)] evolved four highly diverged _E. coli_ strains (the two most diverged strains only shared 57% of their genes), starting populations with one of three engineered mutations, and found that while declining adaptability held across mutated populations of each strain (when initial genotypes differed by single mutations), it did not hold across strains. However, we note that in Kavvas et al. [[39](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR39)] the initially less fit genotypes among a different panel of _E. coli_ strains did gain more fitness during evolution than their higher-initial-fitness counterparts. In contrast to diminishing-returns epistasis, many studies have reported specific cases of synergistic epistasis between beneficial mutations that drive important evolutionary dynamics [[3](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR3), [40](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR40)-[43](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR43)]. Thus a key question, which we will return to later in this review, is when and why we should expect to find patterns of diminishing-returns epistasis, and when we might expect to see something different.

### Increasing-costs epistasis can lead to a reduction in mutational robustness during evolution
We recently used a transposon mutagenesis system in yeast to show that a set of 91 mostly deleterious insertion mutations became, on average, more deleterious over the course of 10,000 generations of evolution in one lab environment [[11](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR11)]. We had previously used this library to show that these mutations also tend to be more deleterious in higher-fitness strains isolated from a cross between two diverged yeast strains [[44](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR44)]. In both cases, these DFE-level patterns did not emerge from a consistent decrease in the fitness effects of each mutation. Instead, we observed highly variable patterns of epistasis: some mutations have a constant effect independent of genetic background (no epistasis), some have specific interactions with individual loci, and others show consistent patterns of diminishing-returns, increasing-costs, or decreasing-costs epistasis. While increasing-costs epistasis was widespread enough to cause consistent changes to the DFE in the strains isolated from the yeast cross and from one of our evolution environments, fewer mutations showed this trend in another evolution environment, suggesting that the nature of selection acting on the evolving population can influence whether this trend is reliably observed.

Three recent studies have used transposon mutagenesis to study how the fitness effects of mutations change during the LTEE, focusing on overall changes to the distribution of fitness effects [[35](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR35)], changes in gene essentiality [[36](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR36)], and the effect of ecological interactions between coexisting lineages on the effects of mutations [[37](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR37)]. None of these LTEE-based studies documented a reduction in the mean of the distribution of fitness effects. However, Limdi et al. [[36](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR36)] showed that more genes transitioned from non-essential to essential than vice versa. That is, insertions in some genes became highly deleterious or lethal over the course of evolution.

Together, these studies suggest that as microbial populations adapt to laboratory conditions, deleterious insertion mutations show a tendency towards becoming more deleterious (increasing-costs), though their effects change less consistently than beneficial mutations. Again, the key question is when and why we expect to see increasing-costs epistasis leading to a reduction in mutational robustness. How do these phenomena depend on the environment, biological system, or evolutionary timescale?

## Patterns of epistasis within proteins
To start asking whether we should expect to see patterns of global epistasis in other systems or on other timescales, we first consider another level of biological organization on which data on epistasis is being rapidly accumulated: within-protein evolution. The advent of deep mutational scanning technologies (which screen the local mutational neighborhood around a focal genotype; reviewed in [[45](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR45)] and [[46](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR46)]), along with ancestral reconstruction techniques and high-throughput assays for protein function, have opened the door to directly study how the array of mutational effects possible for a given protein sequence changes as the protein evolves (Fig. [2](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Fig2)).

Deep mutational scanning studies have frequently observed a pattern of global epistasis in which mutations have additive effects on an unobserved trait (which presumably represents one or several biophysical properties such as stability or enzyme activity) that in turn maps nonlinearly to the observed phenotype (often binding affinity or fluorescence) [[15](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR15), [47](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR47)]. This simplification of the genotype–phenotype map allows us to predict the effects of mutations using relatively few parameters (i.e., the additive effects of mutations on the unobserved trait and the form of the nonlinearity). However, we note that this form of global epistasis is distinct from fitness-correlated global epistasis: for example, two mutations that have the same effect on one genetic background will have the same effect on another, which is not necessarily the case for fitness-correlated epistasis.

### Epistatic drift makes the effects of mutations less predictable as proteins evolve
While the models of within-protein global epistasis discussed above were built from deep mutational scanning datasets in which genotypes differ by a few mutations, these methods have now been combined with ancestral sequence reconstruction to study epistasis along long-term evolutionary trajectories. For example, recent work has quantified how the effects of mutations change as the DNA binding domain of steroid hormone receptors evolved over 700 million years [[48](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR48)], and as the receptor-binding domain (RBD) of the spike protein evolved in the family of sarbecoviruses containing SARS-CoV-2 [[4](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR4)]. It is difficult to look for phenotype-correlated epistasis (e.g., diminishing-returns) in these datasets for three reasons: (1) there are fewer genetic backgrounds than in multi-mutation deep mutational scanning datasets, (2) in some cases (e.g., Park et al. [[48](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR48)]), we do not have measurements of the phenotypes of the relevant genetic backgrounds, and (3) the limited dynamic range of these assays can present statistical challenges. Presumably for these reasons, neither of these studies specifically investigate phenotype-correlated epistasis. However, as these approaches grow more common and produce even larger datasets, it will be interesting to study whether patterns of global epistasis hold predictive power over long evolutionary timescales.

While these studies do not directly analyze global epistasis, they do find a consistent pattern: the effects of different mutations “drift” randomly during evolution, and each mutation has a different characteristic speed at which its effect drifts. Park et al. [[48](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR48)] show that these mutation-specific rates of change are consistent in different parts of the phylogenetic tree (proportional to the number of background substitutions on the branch). Starr et al. [[4](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR4)] find a similar pattern, in which mutational effects at different sites in the RBD drift across increasingly different genetic backgrounds, again with site-specific speeds. Together, these studies show that certain mutations are more likely to have unchanging effects over evolutionary timescales, while others will change rapidly as a result of epistatic patterns that are currently difficult to simplify. These different rates of epistatic drift, which can in principle be estimated from much smaller datasets, can tell us how likely it is that the phenotypic effect of mutating a particular site is similar to its effect on another background. This is a useful parameter for large-scale Bayesian models seeking to predict epistasis [[49](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR49)].

## Models of global epistasis
Our best hope for building predictive models of epistasis during evolution is to reduce the dimensionality of the mapping between genotypic configurations and fitness, often referred to as the fitness landscape. The commonality of global or fitness-correlated epistasis suggests that these reductions are _sometimes_ possible, but as we have seen above, these patterns are not universal. Instead, they depend on environmental conditions, the level of biological organization considered, and the genetic distance over which we are trying to predict epistasis. What we need, then, are models that can tell us, using either biological knowledge and/or sparse datasets as inputs, what forms of epistasis to expect. In this section, we will review a few nascent efforts towards this end.

### Statistical models
One way to understand the emergence of patterns such as fitness-correlated epistasis is to describe statistical models of the genotype to phenotype map that could lead to such phenomena (Diaz-Colunga et al. [[50](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR50)] provide an in-depth review of these types of explanations for patterns of global epistasis). Recent studies [[51](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR51), [52](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR52)] have proposed models where diminishing-returns and increasing-costs epistasis arise when a mutation has a large number of epistatic interactions with the genetic loci that vary in the background. These studies show that extensive idiosyncratic epistasis can lead to a general pattern of fitness-correlated global epistasis. Intuitively, in a highly epistatic fitness landscape, fitter genotypes will tend to have a larger excess of positive (relative to negative) interactions between loci. Consequently, a mutation that interacts with many of these loci will disrupt, on average, a larger number of positively-contributing interactions when it occurs on a fitter background. Provided that the mutation has numerous interactions with the background loci, a mathematical argument based on the central limit theorem shows that the mutation’s fitness effect has a negative linear dependence on background fitness, irrespective of whether the mutation is beneficial or deleterious on average [[51](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR51), [52](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR52)].

In this framework, mutations can be broadly classified into three classes: (1) additive mutations that have an effect independent of the background, (2) mutations which have strong and specific epistatic interactions with one or a few other genetic loci, and whose fitness effect can be positively or negatively correlated with background fitness, and (3) mutations that have epistatic interactions with numerous loci and thereby show a negative linear dependence on background fitness. Figure [3](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Fig3) shows example mutations from [[44](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR44)] that correspond to these three cases. The model predicts that for mutations of the third class, the _negative slope_ of the linear trend is proportional to the _variance of the residuals_ around this trend, which is consistent with data from Bakerlee et al. [[53](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR53)].

**Fig. 3**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1709451330582-85010367-2f15-4d37-b61d-90a0bca937cd.png)

Statistical models of epistasis. **a** The fitness effects of three example insertion mutations on background strains obtained from a yeast cross (data from [[44](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR44)]). These examples illustrate a mutation that shows no detectable epistatic interactions (left), a mutation that has a specific interaction with one locus in the background (middle) and a mutation that shows a negative linear trend (right), which arises if a mutation has many idiosyncratic interactions with background loci. **b** Theory predicts that the slope of the linear global epistasis trend depends on the number and magnitude of interactions the mutation has with background loci. The variability in slopes across mutations can potentially be explained by their involvement in a variable number of pathways that contribute to fitness. **c** An empirical fitness landscape with ten mutations (85% complete) shows a linear global epistasis trend for mutation PMA1. This trend emerges as terms of increasing orders of epistasis are added to the model. Data from [[53](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR53)]

[Full size image](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3/figures/3)

Another feature of the data from Bakerlee et al. [[53](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR53)] is that the negative slope of the fitness-correlated trend varies significantly across mutations. This variation in slope could arise if mutations with steeper slopes are involved in more biological pathways that contribute to fitness, and therefore have a larger number of interaction terms (Fig. [3](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Fig3)b). [[52](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR52)] introduced a Gaussian fitness landscape model to quantify this intuition, which also predicts that the rate of adaptation should decline as a power law with time and that the DFE of beneficial mutations should be exponential when the organism is well-adapted to the environment. If acquired mutations are uncorrelated with fitness, this model also leads to epistatic drift at a site-dependent rate.

While this theory assumes that mutations have numerous epistatic interactions with other loci, diminishing-returns epistasis has also been observed across lineages that have acquired fewer than ten mutations. For example, a recent study used a hierarchical CRISPR gene drive system to construct 875 of the 1024 possible combinations of 10 mutations that affect diverse functions in yeast [[53](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR53)]. By directly measuring higher-order epistasis terms, this work shows that fitness-correlated linear trends can emerge even from a small number (~ 5–10) of idiosyncratic interactions (Fig. [3](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Fig3)c).

### Functional models
Another class of explanations for patterns of global epistasis derives from a mechanistic perspective on biological systems. Lehner [[54](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR54)] provides an excellent review of a diverse set of potential molecular mechanisms underlying epistasis, including protein stability thresholds, functional redundancy, and <font style="background-color:#FBDE28;">metabolic pathway structure</font>. Here we review recent work that has attempted to devise functional models of global epistasis. 

Several studies have attempted to explain patterns of fitness-correlated epistasis through the lens of metabolic control theory (MCT), which is a framework used to relate the sensitivity of the flux through a metabolic pathway to changes in enzyme concentration or to mutations that modulate enzyme kinetics [[55](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR55), [56](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR56)]. 

+ MacLean [[57](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR57)] applied the basic ideas of MCT beyond metabolic pathways into the core processes of transcription and translation, showing that strains that grow more slowly are more robust to a ribosome-inhibiting antibiotic. This relationship provides a functional explanation for increasing-costs epistasis in transcription or translation machinery: as flux through this pathway increases, mutations become more costly. 
+ We have also recently used an MCT framework to rationalize why patterns of diminishing-returns and increasing-costs arise in microbial evolution experiments [[11](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR11)]. We explore these ideas further in [Box 2](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Sec14) and Fig. [4](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#Fig4).

**Fig. 4**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1709451351812-2c43e496-30c9-4933-87fc-55906e1cabc7.png)

Diminishing-returns and increasing-costs epistasis in simple models of enzyme kinetics. (Left) The dependence of flux on two enzymes in a serial metabolic pathway, given by \(J = a/(1/{E}_{1 }+ 1/{E}_{2} + b)\) [[56](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR56)]. (Right) Michaelis–Menten kinetics. In the unsaturated regime, the downstream flux depends multiplicatively on \({k}_{on}\) and \({k}_{cat}\). Mutations that increase \(\log {k}_{\text{on}}\) experience diminishing-returns, whereas mutations that reduce \(\log {k}_{\text{cat}}\) incur larger costs at larger values of \(\log {k}_{\text{on}}.\)

> 56 Do deleterious mutations act synergistically? Metabolic control theory provides a partial answer
>

[genetics0127.pdf](https://www.yuque.com/attachments/yuque/0/2024/pdf/22983715/1709452063150-8fd04388-f642-48a0-89ec-9d4d3bbef603.pdf)

[Full size image](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3/figures/4)

<font style="color:#DF2A3F;">More recently, Kryazhimskiy [</font>[<font style="color:#DF2A3F;">58</font>](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR58)<font style="color:#DF2A3F;">] used MCT to show how epistasis between two mutations within a given sub-pathway can change as we zoom out to consider their effect on the larger pathways in which this sub-pathway is embedded. Under a linearity assumption, this analysis finds a non-trivial asymmetry in how positive and negative epistasis propagate: negative epistasis at smaller scales remains negative on larger scales, while positive epistasis can change sign. This could lead to a skew in the distribution of epistatic coefficients that can in principle lead to global epistasis, though the paper is careful to point out that the specific structure of the metabolic network itself can also lead to different likelihoods of negative and positive epistasis.</font>

Husain and Murugan [[59](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR59)] take an alternative physics-inspired approach, relating patterns of global epistasis in proteins to the collective relaxation modes of protein conformations. For example, if a single mode dominates the relaxation dynamics of a protein and the measured phenotype is predominantly influenced by protein conformation, then mutational effects will show changes primarily along this dominant relaxation mode. If these mutational effects act additively on the dominant mode, the genotype–phenotype map can be approximated as a nonlinear function applied to an additive trait. More generally, if the relaxation dynamics of a system are dominated by \(k\) modes, then epistatic effects should span a \(k\)-dimensional subspace, provided that mutational effects are small and specific epistasis mediated by direct contacts is negligible. This argument provides a physical explanation for global epistasis, which can be further tested by measuring the dimensionality of epistatic effects (possibly acquired through deep mutational scans) on a protein and its normal mode spectrum.

## Predicting epistasis, predicting evolution
### Inference of landscape structure
While many of the models described in the previous section make a priori predictions about global epistasis, we can also use them alongside data-driven inference approaches that aim to find simpler patterns in epistatic effects. A common goal of these methods is to predict the phenotypes of unobserved genotypes using a relatively limited set of genotype–phenotype measurements.

One conceptually straightforward approach to this problem is to model the fitness of each genotype as a sum of additive effects of individual mutations, along with pairwise and higher-order interactions between them. We can then infer the additive effects and interaction coefficients (typically up to some maximum order, and potentially with some regularization term) from genotype–phenotype data. This defines a model that can be used to predict phenotypes of unobserved genotypes. Bakerlee et al. [[53](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR53)] and Poelwijk et al. [[60](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR60)] took this approach to infer epistatic effects in combinatorially complete or near-complete libraries spanning sets of mutations across and within genes, respectively. Both found that a relatively small number of epistatic terms can explain the vast majority of the variation in phenotype. In other words, strong epistatic effects on phenotypes are sparse, such that it is possible to accurately predict phenotypes for the entire set based on a sparse sample of phenotypic measurements (e.g., 6–11% of the combinatorially complete set of measurements in Poelwijk et al. [[60](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR60)]). Poelwijk et al. [[60](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR60)] also demonstrates that epistatic coefficients can be accurately inferred from the subset of sequences that cross some phenotypic threshold, suggesting that it may be possible to predict these coefficients from the set of extant, presumably functional, sequences of a protein.

A second category of inference uses genotype–phenotype data to infer the functional architecture of biological systems, which can later be used to predict the effects of mutations. The most comprehensive work in this direction has aimed to characterize the genetic organization of budding yeast based on measurements of epistatic interactions between gene knockouts and knockdowns [[1](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR1)]. While this type of work can provide the foundation for genome-scale models of microorganisms that predict how changes in gene activities will affect phenotypes (reviewed in Fang et al. [[61](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR61)]), the data generally requires careful curation and typically cannot model the effects of individual mutations.

A third category of approaches is to assume that the genotype–phenotype map has a low-dimensional structure. For example, a global epistasis model analyzed by Otwinowski et al. [[47](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR47)] assumes that the observed phenotype is a nonlinear function of a continuous additive trait. To build a predictive model, these authors use training data to infer the effect of each mutation on the additive trait, as well as the nonlinear function that maps this trait to the measured phenotype. An alternative approach is to use some dimensionality reduction method on large-scale genotype–phenotype data sets to infer the map between genotype and a low-dimensional latent space and between the latent space and observed phenotypes. For example, [[62](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR62)] used singular value decomposition to infer a latent space, and then used the inferred structure to predict the fitness effects of many mutations across many environments in yeast.

These dimensionality reduction approaches are also present in new machine-learning methods for predicting patterns of epistasis, which we expect to become more common and accurate in the coming few years [[63](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR63), [64](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR64)]. For example, Tareen et al. [[64](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR64)] present a flexible method for learning the relationship between genotype and phenotype. This method includes additive, pairwise, or neural-net-based models to produce a single latent phenotype, which may then be related to the measured phenotype through a nonlinear function, as described in Otwinowski et al. [[47](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR47)]. In contrast, Tonner et al. [[63](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR63)] use a hierarchical Bayesian model that explicitly attempts to identify a relatively small number of uncorrelated latent variables that collectively determine phenotypes. In three within-protein datasets, their model identifies 3–5 latent dimensions, some of which may be interpretable in terms of biologically meaningful traits such as ligand binding affinity.

Given good data, the goal of predicting fitness effects of mutations is well-defined, in the same way that protein structure prediction has been well-defined for decades. A combination of machine learning and functionally motivated approaches should make high-accuracy phenotype prediction possible, at least among relatively closely related genotypes. The question will be whether we can predict effects more widely using sparse or mutationally distant datasets. Currently, we are limited both by data and by our modeling approaches. As these both improve, we will approach the limits set by the true dimensionality of the phenotypes produced by biological systems.

The concept of “epistatic drift” provides one simple framework to think about these limitations: we should expect our ability to predict epistasis to decline as the genetic distance between the backgrounds in our data set and our prediction target increases, and we should expect this effect to vary between mutations [[4](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR4), [48](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR48)]. Importantly, we can use this relationship between genetic distance and fitness correlations to build priors that take into account the structure of higher-order epistasis [[49](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3#ref-CR49)]. As we gather more high-throughput datasets on within-protein epistasis, we hope it will be possible to connect these patterns of epistatic drift to functional and structural properties of proteins, such that even when using sparse mutation data, structural information can be used to bolster predictive models.

### Predicting evolution
Characterizing how the fitness effects of mutations change during evolution is essential if we are to predict evolutionary dynamics. The work reviewed here shows that this is a difficult task. While the effects of some mutations follow predictable fitness-correlated patterns, these patterns are not universal: they depend on the biological system and phenotype under selection (e.g., a protein’s binding efficiency, a microbial cell’s growth rate) and the timescale (e.g., strains separated by few mutations and generations or by hundreds of thousands of mutations and generations). We are cautiously optimistic that as we gain the ability to predict epistasis in different systems and to identify the functional basis of the latent phenotypes that generate this epistasis, we will improve our ability to predict when phenomena such as declining adaptability or robustness, among other patterns of changing mutational effects, will occur as cells or proteins evolve in nature.

## Availability of data and materials
Not applicable.

## Abbreviations
DFE:

Distribution of fitness effects

LTEE:

Long-term evolution experiment

RBD:

Receptor binding domain

MCT:

Metabolic control theory

## References
1. Costanzo M, Baryshnikova A, Bellay J, Kim Y, Spear ED, Sevier CS, et al. The genetic landscape of a cell. Science. 2010;327:425–31.

[Article](https://doi.org/10.1126%2Fscience.1180823)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXnt1ahug%3D%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=20093466)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC5600254)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20genetic%20landscape%20of%20a%20cell&journal=Science&doi=10.1126%2Fscience.1180823&volume=327&pages=425-431&publication_year=2010&author=Costanzo%2CM&author=Baryshnikova%2CA&author=Bellay%2CJ&author=Kim%2CY&author=Spear%2CED&author=Sevier%2CCS)  

2. Chou H-H, Chiu H-C, Delaney NF, Segrè D, Marx CJ. Diminishing returns epistasis among beneficial mutations decelerates adaptation. Science. 2011;332:1190–2.

[Article](https://doi.org/10.1126%2Fscience.1203799)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC3MXmslyisbo%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=21636771)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3244271)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Diminishing%20returns%20epistasis%20among%20beneficial%20mutations%20decelerates%20adaptation&journal=Science&doi=10.1126%2Fscience.1203799&volume=332&pages=1190-1192&publication_year=2011&author=Chou%2CH-H&author=Chiu%2CH-C&author=Delaney%2CNF&author=Segr%C3%A8%2CD&author=Marx%2CCJ)  

3. Khan AI, Dinh DM, Schneider D, Lenski RE, Cooper TF. Negative epistasis between beneficial mutations in an evolving bacterial population. Science. 2011;332:1193–6.

[Article](https://doi.org/10.1126%2Fscience.1203801)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC3MXmslyisbs%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=21636772)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Negative%20epistasis%20between%20beneficial%20mutations%20in%20an%20evolving%20bacterial%20population&journal=Science&doi=10.1126%2Fscience.1203801&volume=332&pages=1193-1196&publication_year=2011&author=Khan%2CAI&author=Dinh%2CDM&author=Schneider%2CD&author=Lenski%2CRE&author=Cooper%2CTF)  

4. Starr TN, Zepeda SK, Walls AC, Greaney AJ, Alkhovsky S, Veesler D, et al. ACE2 binding is an ancestral and evolvable trait of sarbecoviruses. Nature. 2022;603:913–8.

[Article](https://doi.org/10.1038%2Fs41586-022-04464-z)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB38XnvFSit7g%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35114688)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC8967715)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=ACE2%20binding%20is%20an%20ancestral%20and%20evolvable%20trait%20of%20sarbecoviruses&journal=Nature&doi=10.1038%2Fs41586-022-04464-z&volume=603&pages=913-918&publication_year=2022&author=Starr%2CTN&author=Zepeda%2CSK&author=Walls%2CAC&author=Greaney%2CAJ&author=Alkhovsky%2CS&author=Veesler%2CD)  

5. Moulana A, Dupic T, Phillips AM, Chang J, Nieves S, Roffler AA, et al. Compensatory epistasis maintains ACE2 affinity in SARS-CoV-2 Omicron BA.1. Nat Commun. 2022;13:7011.

[Article](https://doi.org/10.1038%2Fs41467-022-34506-z)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB38XivFCmt7vI)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=36384919)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9668218)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Compensatory%20epistasis%20maintains%20ACE2%20affinity%20in%20SARS-CoV-2%20Omicron%20BA.1&journal=Nat%20Commun&doi=10.1038%2Fs41467-022-34506-z&volume=13&publication_year=2022&author=Moulana%2CA&author=Dupic%2CT&author=Phillips%2CAM&author=Chang%2CJ&author=Nieves%2CS&author=Roffler%2CAA)  

6. Moulana A, Dupic T, Phillips AM, Chang J, Roffler AA, Greaney AJ, et al. The landscape of antibody binding affinity in SARS-CoV-2 Omicron BA.1 evolution. Elife. 2023;12:e83442.

[Article](https://doi.org/10.7554%2FeLife.83442)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=36803543)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9949795)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20landscape%20of%20antibody%20binding%20affinity%20in%20SARS-CoV-2%20Omicron%20BA.1%20evolution&journal=Elife&doi=10.7554%2FeLife.83442&volume=12&publication_year=2023&author=Moulana%2CA&author=Dupic%2CT&author=Phillips%2CAM&author=Chang%2CJ&author=Roffler%2CAA&author=Greaney%2CAJ)  

7. Good BH, Rouzine IM, Balick DJ, Hallatschek O, Desai MM. Distribution of fixed beneficial mutations and the rate of adaptation in asexual populations. Proc Natl Acad Sci U S A. 2012;109:4950–5.

[Article](https://doi.org/10.1073%2Fpnas.1119910109)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC38Xlt1agtbo%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=22371564)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3323973)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Distribution%20of%20fixed%20beneficial%20mutations%20and%20the%20rate%20of%20adaptation%20in%20asexual%20populations&journal=Proc%20Natl%20Acad%20Sci%20U%20S%20A&doi=10.1073%2Fpnas.1119910109&volume=109&pages=4950-4955&publication_year=2012&author=Good%2CBH&author=Rouzine%2CIM&author=Balick%2CDJ&author=Hallatschek%2CO&author=Desai%2CMM)  

8. Good BH, Desai MM. Deleterious passengers in adapting populations. Genetics. 2014;198:1183–208.

[Article](https://doi.org/10.1534%2Fgenetics.114.170233)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=25194161)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4224160)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deleterious%20passengers%20in%20adapting%20populations&journal=Genetics&doi=10.1534%2Fgenetics.114.170233&volume=198&pages=1183-1208&publication_year=2014&author=Good%2CBH&author=Desai%2CMM)  

9. Hallatschek O. The noisy edge of traveling waves. Proc Natl Acad Sci U S A. 2011;108:1783–7.

[Article](https://doi.org/10.1073%2Fpnas.1013529108)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC3MXhslyjsrc%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=21187435)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20noisy%20edge%20of%20traveling%20waves&journal=Proc%20Natl%20Acad%20Sci%20U%20S%20A&doi=10.1073%2Fpnas.1013529108&volume=108&pages=1783-1787&publication_year=2011&author=Hallatschek%2CO)  

10. Good BH, Desai MM. The impact of macroscopic epistasis on long-term evolutionary dynamics. Genetics. 2015;199:177–90.

[Article](https://doi.org/10.1534%2Fgenetics.114.172460)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=25395665)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20impact%20of%20macroscopic%20epistasis%20on%20long-term%20evolutionary%20dynamics&journal=Genetics&doi=10.1534%2Fgenetics.114.172460&volume=199&pages=177-190&publication_year=2015&author=Good%2CBH&author=Desai%2CMM)  

11. Johnson MS, Desai MM. Mutational robustness changes during long-term adaptation in laboratory budding yeast populations. Elife. 2022;11:e76491.

[Article](https://doi.org/10.7554%2FeLife.76491)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3sXltVCms7g%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35880743)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9355567)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Mutational%20robustness%20changes%20during%20long-term%20adaptation%20in%20laboratory%20budding%20yeast%20populations&journal=Elife&doi=10.7554%2FeLife.76491&volume=11&publication_year=2022&author=Johnson%2CMS&author=Desai%2CMM)  

12. Wünsche A, Dinh DM, Satterwhite RS, Arenas CD, Stoebel DM, Cooper TF. Diminishing-returns epistasis decreases adaptability along an evolutionary trajectory. Nat Ecol Evol. 2017;1:0061.

[Article](https://doi.org/10.1038%2Fs41559-016-0061)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Diminishing-returns%20epistasis%20decreases%20adaptability%20along%20an%20evolutionary%20trajectory&journal=Nat%20Ecol%20Evol&doi=10.1038%2Fs41559-016-0061&volume=1&publication_year=2017&author=W%C3%BCnsche%2CA&author=Dinh%2CDM&author=Satterwhite%2CRS&author=Arenas%2CCD&author=Stoebel%2CDM&author=Cooper%2CTF)  

13. Aggeli D, Li Y, Sherlock G. Changes in the distribution of fitness effects and adaptive mutational spectra following a single first step towards adaptation. Nat Commun. 2021;12:5193.

[Article](https://doi.org/10.1038%2Fs41467-021-25440-7)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3MXhvFGmsLzM)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=34465770)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC8408183)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Changes%20in%20the%20distribution%20of%20fitness%20effects%20and%20adaptive%20mutational%20spectra%20following%20a%20single%20first%20step%20towards%20adaptation&journal=Nat%20Commun&doi=10.1038%2Fs41467-021-25440-7&volume=12&publication_year=2021&author=Aggeli%2CD&author=Li%2CY&author=Sherlock%2CG)  

14. Kryazhimskiy S, Rice DP, Jerison ER, Desai MM. Global epistasis makes adaptation predictable despite sequence-level stochasticity. Science. 2014;344:1519–22.

[Article](https://doi.org/10.1126%2Fscience.1250939)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC2cXhtVaks7zI)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=24970088)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4314286)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Global%20epistasis%20makes%20adaptation%20predictable%20despite%20sequence-level%20stochasticity&journal=Science&doi=10.1126%2Fscience.1250939&volume=344&pages=1519-1522&publication_year=2014&author=Kryazhimskiy%2CS&author=Rice%2CDP&author=Jerison%2CER&author=Desai%2CMM)  

15. Starr TN, Thornton JW. Epistasis in protein evolution. Protein Sci. 2016;25:1204–18.

[Article](https://doi.org/10.1002%2Fpro.2897)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC28Xjt1Cnt78%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=26833806)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4918427)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Epistasis%20in%20protein%20evolution&journal=Protein%20Sci&doi=10.1002%2Fpro.2897&volume=25&pages=1204-1218&publication_year=2016&author=Starr%2CTN&author=Thornton%2CJW)  

16. de Visser JAGM, Cooper TF, Elena SF. The causes of epistasis. Proc Biol Sci. 2011;278:3617–24.

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=21976687)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3203509)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20causes%20of%20epistasis&journal=Proc%20Biol%20Sci&volume=278&pages=3617-3624&publication_year=2011&author=Visser%2CJAGM&author=Cooper%2CTF&author=Elena%2CSF)  

17. Couce A, Tenaillon OA. The rule of declining adaptability in microbial evolution experiments. Front Genet. 2015;6:99.

[Article](https://doi.org/10.3389%2Ffgene.2015.00099)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=25815007)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4356158)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20rule%20of%20declining%20adaptability%20in%20microbial%20evolution%20experiments&journal=Front%20Genet&doi=10.3389%2Ffgene.2015.00099&volume=6&publication_year=2015&author=Couce%2CA&author=Tenaillon%2COA)  

18. Wiser MJ, Ribeck N, Lenski RE. Long-term dynamics of adaptation in asexual populations. Science. 2013;342:1364–7.

[Article](https://doi.org/10.1126%2Fscience.1243357)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC3sXhvV2lsLvK)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=24231808)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Long-term%20dynamics%20of%20adaptation%20in%20asexual%20populations&journal=Science&doi=10.1126%2Fscience.1243357&volume=342&pages=1364-1367&publication_year=2013&author=Wiser%2CMJ&author=Ribeck%2CN&author=Lenski%2CRE)  

19. Jerison ER, Kryazhimskiy S, Mitchell JK, Bloom JS, Kruglyak L, Desai MM. Genetic variation in adaptability and pleiotropy in budding yeast. Elife. 2017;6:e27167.

[Article](https://doi.org/10.7554%2FeLife.27167)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=28826486)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC5580887)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Genetic%20variation%20in%20adaptability%20and%20pleiotropy%20in%20budding%20yeast&journal=Elife.&doi=10.7554%2FeLife.27167&volume=6&publication_year=2017&author=Jerison%2CER&author=Kryazhimskiy%2CS&author=Mitchell%2CJK&author=Bloom%2CJS&author=Kruglyak%2CL&author=Desai%2CMM)  

20. Rokyta DR, Abdo Z, Wichman HA. The genetics of adaptation for eight microvirid bacteriophages. J Mol Evol. 2009;69:229–39.

[Article](https://link.springer.com/doi/10.1007/s00239-009-9267-9)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BD1MXhtlegs77K)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=19693424)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2746890)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20genetics%20of%20adaptation%20for%20eight%20microvirid%20bacteriophages&journal=J%20Mol%20Evol&doi=10.1007%2Fs00239-009-9267-9&volume=69&pages=229-239&publication_year=2009&author=Rokyta%2CDR&author=Abdo%2CZ&author=Wichman%2CHA)  

21. Barrick JE, Kauth MR, Strelioff CC, Lenski RE. Escherichia coli rpoB mutants have increased evolvability in proportion to their fitness defects. Mol Biol Evol. 2010;27:1338–47.

[Article](https://doi.org/10.1093%2Fmolbev%2Fmsq024)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXmsVCqu7g%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=20106907)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2872623)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Escherichia%20coli%20rpoB%20mutants%20have%20increased%20evolvability%20in%20proportion%20to%20their%20fitness%20defects&journal=Mol%20Biol%20Evol&doi=10.1093%2Fmolbev%2Fmsq024&volume=27&pages=1338-1347&publication_year=2010&author=Barrick%2CJE&author=Kauth%2CMR&author=Strelioff%2CCC&author=Lenski%2CRE)  

22. Sanjuán R, Cuevas JM, Moya A, Elena SF. Epistasis and the adaptability of an RNA virus. Genetics. 2005;170:1001–8.

[Article](https://doi.org/10.1534%2Fgenetics.105.040741)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=15879507)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1451175)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Epistasis%20and%20the%20adaptability%20of%20an%20RNA%20virus&journal=Genetics&doi=10.1534%2Fgenetics.105.040741&volume=170&pages=1001-1008&publication_year=2005&author=Sanju%C3%A1n%2CR&author=Cuevas%2CJM&author=Moya%2CA&author=Elena%2CSF)  

23. Moore FB, Rozen DE, Lenski RE. Pervasive compensatory adaptation in Escherichia coli. Proc Biol Sci. 2000;267:515–22.

[Article](https://doi.org/10.1098%2Frspb.2000.1030)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:STN:280:DC%2BD3c7pvFKksw%3D%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=10737410)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1690552)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Pervasive%20compensatory%20adaptation%20in%20Escherichia%20coli&journal=Proc%20Biol%20Sci&doi=10.1098%2Frspb.2000.1030&volume=267&pages=515-522&publication_year=2000&author=Moore%2CFB&author=Rozen%2CDE&author=Lenski%2CRE)  

24. Rojas Echenique JI, Kryazhimskiy S, Nguyen Ba AN, Desai MM. Modular epistasis and the compensatory evolution of gene deletion mutants. PLoS Genet. 2019;15:e1007958.

[Article](https://doi.org/10.1371%2Fjournal.pgen.1007958)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=30768593)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6395002)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Modular%20epistasis%20and%20the%20compensatory%20evolution%20of%20gene%20deletion%20mutants&journal=PLoS%20Genet&doi=10.1371%2Fjournal.pgen.1007958&volume=15&publication_year=2019&author=Rojas%20Echenique%2CJI&author=Kryazhimskiy%2CS&author=Nguyen%20Ba%2CAN&author=Desai%2CMM)  

25. Fumasoni M, Murray AW. Ploidy and recombination proficiency shape the evolutionary adaptation to constitutive DNA replication stress. PLoS Genet. 2021;17:e1009875.

[Article](https://doi.org/10.1371%2Fjournal.pgen.1009875)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3MXisFKntLbE)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=34752451)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC8604288)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Ploidy%20and%20recombination%20proficiency%20shape%20the%20evolutionary%20adaptation%20to%20constitutive%20DNA%20replication%20stress&journal=PLoS%20Genet&doi=10.1371%2Fjournal.pgen.1009875&volume=17&publication_year=2021&author=Fumasoni%2CM&author=Murray%2CAW)  

26. Perfeito L, Sousa A, Bataillon T, Gordo I. Rates of fitness decline and rebound suggest pervasive epistasis. Evolution. 2014;68:150–62.

[Article](https://doi.org/10.1111%2Fevo.12234)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:STN:280:DC%2BC2czgtlKqsw%3D%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=24372601)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Rates%20of%20fitness%20decline%20and%20rebound%20suggest%20pervasive%20epistasis&journal=Evolution&doi=10.1111%2Fevo.12234&volume=68&pages=150-162&publication_year=2014&author=Perfeito%2CL&author=Sousa%2CA&author=Bataillon%2CT&author=Gordo%2CI)  

27. Persson K, Stenberg S, Tamás MJ, Warringer J. Adaptation of the yeast gene knockout collection is near-perfectly predicted by fitness and diminishing return epistasis. G3. 2022;12(11):jkac240.

[Article](https://doi.org/10.1093%2Fg3journal%2Fjkac240)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3sXnslGmsbw%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=36083011)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9635671)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Adaptation%20of%20the%20yeast%20gene%20knockout%20collection%20is%20near-perfectly%20predicted%20by%20fitness%20and%20diminishing%20return%20epistasis&journal=G3&doi=10.1093%2Fg3journal%2Fjkac240&volume=12&issue=11&publication_year=2022&author=Persson%2CK&author=Stenberg%2CS&author=Tam%C3%A1s%2CMJ&author=Warringer%2CJ)  

28. MacLean RC, Perron GG, Gardner A. Diminishing returns from beneficial mutations and pervasive epistasis shape the fitness landscape for rifampicin resistance in Pseudomonas aeruginosa. Genetics. 2010;186:1345–54.

[Article](https://doi.org/10.1534%2Fgenetics.110.123083)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:STN:280:DC%2BC3M%2FjtVCqsQ%3D%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=20876562)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2998316)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Diminishing%20returns%20from%20beneficial%20mutations%20and%20pervasive%20epistasis%20shape%20the%20fitness%20landscape%20for%20rifampicin%20resistance%20in%20Pseudomonas%20aeruginosa&journal=Genetics&doi=10.1534%2Fgenetics.110.123083&volume=186&pages=1345-1354&publication_year=2010&author=MacLean%2CRC&author=Perron%2CGG&author=Gardner%2CA)  

29. Flynn KM, Cooper TF, Moore FB-G, Cooper VS. The environment affects epistatic interactions to alter the topology of an empirical fitness landscape. PLoS Genet. 2013;9:e1003426.

[Article](https://doi.org/10.1371%2Fjournal.pgen.1003426)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC3sXnt1aqsb0%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=23593024)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3616912)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20environment%20affects%20epistatic%20interactions%20to%20alter%20the%20topology%20of%20an%20empirical%20fitness%20landscape&journal=PLoS%20Genet&doi=10.1371%2Fjournal.pgen.1003426&volume=9&publication_year=2013&author=Flynn%2CKM&author=Cooper%2CTF&author=Moore%2CFB-G&author=Cooper%2CVS)  

30. Schick A, Bailey SF, Kassen R. Evolution of fitness trade-offs in locally adapted populations of pseudomonas fluorescens. Am Nat. 2015;186(Suppl 1):S48-59.

[Article](https://doi.org/10.1086%2F682932)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=26656216)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Evolution%20of%20fitness%20trade-offs%20in%20locally%20adapted%20populations%20of%20pseudomonas%20fluorescens&journal=Am%20Nat&doi=10.1086%2F682932&volume=186&issue=Suppl%201&pages=S48-59&publication_year=2015&author=Schick%2CA&author=Bailey%2CSF&author=Kassen%2CR)  

31. Schoustra S, Hwang S, Krug J, de Visser JAGM. Diminishing-returns epistasis among random beneficial mutations in a multicellular fungus. Proc Biol Sci. 1837;2016(283):20161376.

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Diminishing-returns%20epistasis%20among%20random%20beneficial%20mutations%20in%20a%20multicellular%20fungus&journal=Proc%20Biol%20Sci.&volume=2016&issue=283&publication_year=1837&author=Schoustra%2CS&author=Hwang%2CS&author=Krug%2CJ&author=Visser%2CJAGM)  

32. Wang Y, Diaz Arenas C, Stoebel DM, Flynn K, Knapp E, Dillon MM, et al. Benefit of transferred mutations is better predicted by the fitness of recipients than by their ecological or genetic relatedness. Proc Natl Acad Sci U S A. 2016;113:5047–52.

[Article](https://doi.org/10.1073%2Fpnas.1524988113)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC28Xmt1Shu70%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=27091964)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4983819)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Benefit%20of%20transferred%20mutations%20is%20better%20predicted%20by%20the%20fitness%20of%20recipients%20than%20by%20their%20ecological%20or%20genetic%20relatedness&journal=Proc%20Natl%20Acad%20Sci%20U%20S%20A&doi=10.1073%2Fpnas.1524988113&volume=113&pages=5047-5052&publication_year=2016&author=Wang%2CY&author=Diaz%20Arenas%2CC&author=Stoebel%2CDM&author=Flynn%2CK&author=Knapp%2CE&author=Dillon%2CMM)  

33. Sackman AM, Rokyta DR. Additive phenotypes underlie epistasis of fitness effects. Genetics. 2018;208:339–48.

[Article](https://doi.org/10.1534%2Fgenetics.117.300451)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC1cXitFGrtrjO)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=29113978)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Additive%20phenotypes%20underlie%20epistasis%20of%20fitness%20effects&journal=Genetics&doi=10.1534%2Fgenetics.117.300451&volume=208&pages=339-348&publication_year=2018&author=Sackman%2CAM&author=Rokyta%2CDR)  

34. Hall AE, Karkare K, Cooper VS, Bank C, Cooper TF, Moore FB-G. Environment changes epistasis to alter trade-offs along alternative evolutionary paths. Evolution. 2019;73:2094–105.

[Article](https://doi.org/10.1111%2Fevo.13825)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=31418459)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Environment%20changes%20epistasis%20to%20alter%20trade-offs%20along%20alternative%20evolutionary%20paths&journal=Evolution.&doi=10.1111%2Fevo.13825&volume=73&pages=2094-105&publication_year=2019&author=Hall%2CAE&author=Karkare%2CK&author=Cooper%2CVS&author=Bank%2CC&author=Cooper%2CTF&author=Moore%2CFB-G)  

35. Couce A, Magnan M, Lenski RE, Tenaillon O. The evolution of fitness effects during long-term adaptation in bacteria. bioRxiv. 2022. [https://doi.org/10.1101/2022.05.17.492360](https://doi.org/10.1101/2022.05.17.492360).
36. Limdi A, Owen SV, Herren C, Lenski RE, Baym M. Parallel changes in gene essentiality over 50,000 generations of evolution. bioRxiv. 2022. [https://doi.org/10.1101/2022.05.17.492023](https://doi.org/10.1101/2022.05.17.492023).
37. Ascensao JA, Wetmore KM, Good BH, Arkin AP, Hallatschek O. Quantifying the adaptive potential of a nascent bacterial community. bioRxiv. 2022:2022.02.03.475969.
38. Smith CE, Smith ANH, Cooper TF, Moore FB-G. Fitness of evolving bacterial populations is contingent on deep and shallow history but only shallow history creates predictable patterns. Proc Biol Sci. 2022;289:20221292.

[PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=36100026)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9470251)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fitness%20of%20evolving%20bacterial%20populations%20is%20contingent%20on%20deep%20and%20shallow%20history%20but%20only%20shallow%20history%20creates%20predictable%20patterns&journal=Proc%20Biol%20Sci&volume=289&publication_year=2022&author=Smith%2CCE&author=Smith%2CANH&author=Cooper%2CTF&author=Moore%2CFB-G)  

39. Kavvas ES, Long CP, Sastry A, Poudel S, Antoniewicz MR, Ding Y, et al. Experimental evolution reveals unifying systems-level adaptations but diversity in driving genotypes. mSystems. 2022;7(6):e0016522.

[Article](https://doi.org/10.1128%2Fmsystems.00165-22)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=36226969)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Experimental%20evolution%20reveals%20unifying%20systems-level%20adaptations%20but%20diversity%20in%20driving%20genotypes&journal=mSystems&doi=10.1128%2Fmsystems.00165-22&volume=7&issue=6&publication_year=2022&author=Kavvas%2CES&author=Long%2CCP&author=Sastry%2CA&author=Poudel%2CS&author=Antoniewicz%2CMR&author=Ding%2CY)  

40. Chou H-H, Berthet J, Marx CJ. Fast growth increases the selective advantage of a mutation arising recurrently during evolution under metal limitation. PLoS Genet. 2009;5:e1000652.

[Article](https://doi.org/10.1371%2Fjournal.pgen.1000652)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=19763169)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732905)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fast%20growth%20increases%20the%20selective%20advantage%20of%20a%20mutation%20arising%20recurrently%20during%20evolution%20under%20metal%20limitation&journal=PLoS%20Genet&doi=10.1371%2Fjournal.pgen.1000652&volume=5&publication_year=2009&author=Chou%2CH-H&author=Berthet%2CJ&author=Marx%2CCJ)  

41. Hsieh Y-YP, Makrantoni V, Robertson D, Marston AL, Murray AW. Evolutionary repair: Changes in multiple functional modules allow meiotic cohesin to support mitosis. PLoS Biol. 2020;18:e3000635.

[Article](https://doi.org/10.1371%2Fjournal.pbio.3000635)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3cXpsVSis7w%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32155147)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7138332)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Evolutionary%20repair%3A%20Changes%20in%20multiple%20functional%20modules%20allow%20meiotic%20cohesin%20to%20support%20mitosis&journal=PLoS%20Biol.&doi=10.1371%2Fjournal.pbio.3000635&volume=18&publication_year=2020&author=Hsieh%2CY-YP&author=Makrantoni%2CV&author=Robertson%2CD&author=Marston%2CAL&author=Murray%2CAW)  

42. Fumasoni M, Murray AW. The evolutionary plasticity of chromosome metabolism allows adaptation to constitutive DNA replication stress. Elife. 2020;9:e51963.

[Article](https://doi.org/10.7554%2FeLife.51963)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3cXhvVagtbnP)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32043971)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7069727)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20evolutionary%20plasticity%20of%20chromosome%20metabolism%20allows%20adaptation%20to%20constitutive%20DNA%20replication%20stress&journal=Elife&doi=10.7554%2FeLife.51963&volume=9&publication_year=2020&author=Fumasoni%2CM&author=Murray%2CAW)  

43. Blount ZD, Barrick JE, Davidson CJ, Lenski RE. Genomic analysis of a key innovation in an experimental Escherichia coli population. Nature. 2012;489:513–8.

[Article](https://doi.org/10.1038%2Fnature11514)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC38XhtlKrsrjE)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=22992527)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3461117)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Genomic%20analysis%20of%20a%20key%20innovation%20in%20an%20experimental%20Escherichia%20coli%20population&journal=Nature&doi=10.1038%2Fnature11514&volume=489&pages=513-518&publication_year=2012&author=Blount%2CZD&author=Barrick%2CJE&author=Davidson%2CCJ&author=Lenski%2CRE)  

44. Johnson MS, Martsul A, Kryazhimskiy S, Desai MM. Higher-fitness yeast genotypes are less robust to deleterious mutations. Science. 2019;366:490–3.

[Article](https://doi.org/10.1126%2Fscience.aay4199)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC1MXitVemtrfP)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=31649199)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7204892)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Higher-fitness%20yeast%20genotypes%20are%20less%20robust%20to%20deleterious%20mutations&journal=Science&doi=10.1126%2Fscience.aay4199&volume=366&pages=490-493&publication_year=2019&author=Johnson%2CMS&author=Martsul%2CA&author=Kryazhimskiy%2CS&author=Desai%2CMM)  

45. Fowler DM, Fields S. Deep mutational scanning: a new style of protein science. Nat Methods. 2014;11:801–7.

[Article](https://doi.org/10.1038%2Fnmeth.3027)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC2cXhslelsLvK)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=25075907)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4410700)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20mutational%20scanning%3A%20a%20new%20style%20of%20protein%20science&journal=Nat%20Methods&doi=10.1038%2Fnmeth.3027&volume=11&pages=801-807&publication_year=2014&author=Fowler%2CDM&author=Fields%2CS)  

46. Kemble H, Nghe P, Tenaillon O. Recent insights into the genotype-phenotype relationship from massively parallel genetic assays. Evol Appl. 2019;12:1721–42.

[Article](https://doi.org/10.1111%2Feva.12846)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=31548853)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6752143)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Recent%20insights%20into%20the%20genotype-phenotype%20relationship%20from%20massively%20parallel%20genetic%20assays&journal=Evol%20Appl&doi=10.1111%2Feva.12846&volume=12&pages=1721-1742&publication_year=2019&author=Kemble%2CH&author=Nghe%2CP&author=Tenaillon%2CO)  

47. Otwinowski J, McCandlish DM, Plotkin JB. Inferring the shape of global epistasis. Proc Natl Acad Sci U S A. 2018;115:E7550–8.

[Article](https://doi.org/10.1073%2Fpnas.1804015115)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC1cXitVanu77E)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=30037990)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6094095)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Inferring%20the%20shape%20of%20global%20epistasis&journal=Proc%20Natl%20Acad%20Sci%20U%20S%20A&doi=10.1073%2Fpnas.1804015115&volume=115&pages=E7550-E7558&publication_year=2018&author=Otwinowski%2CJ&author=McCandlish%2CDM&author=Plotkin%2CJB)  

48. Park Y, Metzger BPH, Thornton JW. Epistatic drift causes gradual decay of predictability in protein evolution. Science. 2022;376:823–30.

[Article](https://doi.org/10.1126%2Fscience.abn6895)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB38XhsVSlurjN)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35587978)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9429997)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Epistatic%20drift%20causes%20gradual%20decay%20of%20predictability%20in%20protein%20evolution&journal=Science&doi=10.1126%2Fscience.abn6895&volume=376&pages=823-830&publication_year=2022&author=Park%2CY&author=Metzger%2CBPH&author=Thornton%2CJW)  

49. Zhou J, Wong MS, Chen W-C, Krainer AR, Kinney JB, McCandlish DM. Higher-order epistasis and phenotypic prediction. Proc Natl Acad Sci U S A. 2022;119:e2204233119.

[Article](https://doi.org/10.1073%2Fpnas.2204233119)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB38XisFKlurjO)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=36129941)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9522415)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Higher-order%20epistasis%20and%20phenotypic%20prediction&journal=Proc%20Natl%20Acad%20Sci%20U%20S%20A&doi=10.1073%2Fpnas.2204233119&volume=119&publication_year=2022&author=Zhou%2CJ&author=Wong%2CMS&author=Chen%2CW-C&author=Krainer%2CAR&author=Kinney%2CJB&author=McCandlish%2CDM)  

50. Diaz-Colunga J, Skwara A, Gowda K, Diaz-Uriarte R, Tikhonov M, Bajic D, et al. Global epistasis on fitness landscapes. Phil Trans R Soc B. 2023;378:20220053.

[Article](https://doi.org/10.1098%2Frstb.2022.0053)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=37004717)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10067270)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Global%20epistasis%20on%20fitness%20landscapes&journal=Phil%20Trans%20R%20Soc%20B&doi=10.1098%2Frstb.2022.0053&volume=378&publication_year=2023&author=Diaz-Colunga%2CJ&author=Skwara%2CA&author=Gowda%2CK&author=Diaz-Uriarte%2CR&author=Tikhonov%2CM&author=Bajic%2CD)  

51. Lyons DM, Zou Z, Xu H, Zhang J. Idiosyncratic epistasis creates universals in mutational effects and evolutionary trajectories. Nat Ecol Evol. 2020;4(12):1685–93.

[Article](https://doi.org/10.1038%2Fs41559-020-01286-y)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32895516)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7710555)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Idiosyncratic%20epistasis%20creates%20universals%20in%20mutational%20effects%20and%20evolutionary%20trajectories&journal=Nat%20Ecol%20Evol.&doi=10.1038%2Fs41559-020-01286-y&volume=4&issue=12&pages=1685-1693&publication_year=2020&author=Lyons%2CDM&author=Zou%2CZ&author=Xu%2CH&author=Zhang%2CJ)  

52. Reddy G, Desai MM. Global epistasis emerges from a generic model of a complex trait. Elife. 2021;10:e64740.

[Article](https://doi.org/10.7554%2FeLife.64740)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3MXitFeitLnM)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=33779543)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC8057814)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Global%20epistasis%20emerges%20from%20a%20generic%20model%20of%20a%20complex%20trait&journal=Elife&doi=10.7554%2FeLife.64740&volume=10&publication_year=2021&author=Reddy%2CG&author=Desai%2CMM)  

53. Bakerlee CW, Ba ANN, Shulgina Y, Echenique JIR, Desai MM. Idiosyncratic epistasis leads to global fitness–correlated trends. Science. 2022;376:630–5.

[Article](https://doi.org/10.1126%2Fscience.abm4774)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB38XhsVSlur7I)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35511982)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10124986)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Idiosyncratic%20epistasis%20leads%20to%20global%20fitness%E2%80%93correlated%20trends&journal=Science&doi=10.1126%2Fscience.abm4774&volume=376&pages=630-635&publication_year=2022&author=Bakerlee%2CCW&author=Ba%2CANN&author=Shulgina%2CY&author=Echenique%2CJIR&author=Desai%2CMM)  

54. Lehner B. Molecular mechanisms of epistasis within and between genes. Trends Genet. 2011;27:323–31.

[Article](https://doi.org/10.1016%2Fj.tig.2011.05.007)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BC3MXptlWqtrk%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=21684621)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Molecular%20mechanisms%20of%20epistasis%20within%20and%20between%20genes&journal=Trends%20Genet&doi=10.1016%2Fj.tig.2011.05.007&volume=27&pages=323-331&publication_year=2011&author=Lehner%2CB)  

55. Kacser H, Burns JA. The control of flux. Biochem Soc Trans. 1995;23:341–66.

[Article](https://doi.org/10.1042%2Fbst0230341)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DyaK2MXmsVOns74%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=7672373)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20control%20of%20flux&journal=Biochem%20Soc%20Trans&doi=10.1042%2Fbst0230341&volume=23&pages=341-366&publication_year=1995&author=Kacser%2CH&author=Burns%2CJA)  

56. Szathmáry E. Do deleterious mutations act synergistically? Metabolic control theory provides a partial answer. Genetics. 1993;133:127–32.

[Article](https://doi.org/10.1093%2Fgenetics%2F133.1.127)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=8417983)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1205292)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Do%20deleterious%20mutations%20act%20synergistically%3F%20Metabolic%20control%20theory%20provides%20a%20partial%20answer&journal=Genetics&doi=10.1093%2Fgenetics%2F133.1.127&volume=133&pages=127-132&publication_year=1993&author=Szathm%C3%A1ry%2CE)  

57. MacLean RC. Predicting epistasis: an experimental test of metabolic control theory with bacterial transcription and translation. J Evol Biol. 2010;23:488–93.

[Article](https://doi.org/10.1111%2Fj.1420-9101.2009.01888.x)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:STN:280:DC%2BC3czkvFWlsA%3D%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=20070461)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Predicting%20epistasis%3A%20an%20experimental%20test%20of%20metabolic%20control%20theory%20with%20bacterial%20transcription%20and%20translation&journal=J%20Evol%20Biol&doi=10.1111%2Fj.1420-9101.2009.01888.x&volume=23&pages=488-493&publication_year=2010&author=MacLean%2CRC)  

58. Kryazhimskiy S. Emergence and propagation of epistasis in metabolic networks. Elife. 2021;10:e60200.

[Article](https://doi.org/10.7554%2FeLife.60200)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3MXhslaiurvO)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=33527897)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7924954)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Emergence%20and%20propagation%20of%20epistasis%20in%20metabolic%20networks&journal=Elife&doi=10.7554%2FeLife.60200&volume=10&publication_year=2021&author=Kryazhimskiy%2CS)  

59. Husain K, Murugan A. Physical constraints on epistasis. Mol Biol Evol. 2020;37:2865–74.

[Article](https://doi.org/10.1093%2Fmolbev%2Fmsaa124)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3MXhtlCrsLrL)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32421772)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physical%20constraints%20on%20epistasis&journal=Mol%20Biol%20Evol&doi=10.1093%2Fmolbev%2Fmsaa124&volume=37&pages=2865-2874&publication_year=2020&author=Husain%2CK&author=Murugan%2CA)  

60. Poelwijk FJ, Socolich M, Ranganathan R. Learning the pattern of epistasis linking genotype and phenotype in a protein. Nat Commun. 2019;10:4213.

[Article](https://doi.org/10.1038%2Fs41467-019-12130-8)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=31527666)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6746860)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Learning%20the%20pattern%20of%20epistasis%20linking%20genotype%20and%20phenotype%20in%20a%20protein&journal=Nat%20Commun&doi=10.1038%2Fs41467-019-12130-8&volume=10&publication_year=2019&author=Poelwijk%2CFJ&author=Socolich%2CM&author=Ranganathan%2CR)  

61. Fang X, Lloyd CJ, Palsson BO. Reconstructing organisms in silico: genome-scale models and their emerging applications. Nat Rev Microbiol. 2020;18:731–43.

[Article](https://doi.org/10.1038%2Fs41579-020-00440-4)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3cXhvVOmtb7L)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32958892)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7981288)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Reconstructing%20organisms%20in%20silico%3A%20genome-scale%20models%20and%20their%20emerging%20applications&journal=Nat%20Rev%20Microbiol&doi=10.1038%2Fs41579-020-00440-4&volume=18&pages=731-743&publication_year=2020&author=Fang%2CX&author=Lloyd%2CCJ&author=Palsson%2CBO)  

62. Kinsler G, Geiler-Samerotte K, Petrov DA. Fitness variation across subtle environmental perturbations reveals local modularity and global pleiotropy of adaptation. Elife. 2020;9:e61271.

[Article](https://doi.org/10.7554%2FeLife.61271)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB3MXovVersr8%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=33263280)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7880691)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fitness%20variation%20across%20subtle%20environmental%20perturbations%20reveals%20local%20modularity%20and%20global%20pleiotropy%20of%20adaptation&journal=Elife&doi=10.7554%2FeLife.61271&volume=9&publication_year=2020&author=Kinsler%2CG&author=Geiler-Samerotte%2CK&author=Petrov%2CDA)  

63. Tonner PD, Pressman A, Ross D. Interpretable modeling of genotype-phenotype landscapes with state-of-the-art predictive power. Proc Natl Acad Sci U S A. 2022;119:e2114021119.

[Article](https://doi.org/10.1073%2Fpnas.2114021119)  [CAS](https://bmcbiol.biomedcentral.com/articles/cas-redirect/1:CAS:528:DC%2BB38XhvVGqtrbK)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35733251)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9245639)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Interpretable%20modeling%20of%20genotype-phenotype%20landscapes%20with%20state-of-the-art%20predictive%20power&journal=Proc%20Natl%20Acad%20Sci%20U%20S%20A&doi=10.1073%2Fpnas.2114021119&volume=119&publication_year=2022&author=Tonner%2CPD&author=Pressman%2CA&author=Ross%2CD)  

64. Tareen A, Kooshkbaghi M, Posfai A, Ireland WT, McCandlish DM, Kinney JB. MAVE-NN: learning genotype-phenotype maps from multiplex assays of variant effect. Genome Biol. 2022;23:98.

[Article](https://link.springer.com/doi/10.1186/s13059-022-02661-7)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35428271)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9011994)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=MAVE-NN%3A%20learning%20genotype-phenotype%20maps%20from%20multiplex%20assays%20of%20variant%20effect&journal=Genome%20Biol&doi=10.1186%2Fs13059-022-02661-7&volume=23&publication_year=2022&author=Tareen%2CA&author=Kooshkbaghi%2CM&author=Posfai%2CA&author=Ireland%2CWT&author=McCandlish%2CDM&author=Kinney%2CJB)  

[Download references](https://citation-needed.springer.com/v2/references/10.1186/s12915-023-01585-3?format=refman&flavour=references)

## Acknowledgements
Not applicable.

## Funding
M.S.J. acknowledges support from the NSF Postdoctoral Research Fellowships in Biology Program (Grant No. 2109800), G.R. and M.M.D. acknowledge support from the NSF-Simons Center for Mathematical and Statistical Analysis of Biology at Harvard University, supported by NSF grant no. DMS-1764269 and the Harvard FAS Quantitative Biology Initiative, and M.M.D. acknowledges support from grant PHY-1914916 from the NSF and grant GM104239 from the NIH.

## Author information
### Authors and Affiliations
1. Department of Integrative Biology, University of California, Berkeley, CA, USA

Milo S. Johnson

2. Biological Systems and Engineering Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA

Milo S. Johnson

3. Physics & Informatics Laboratories, NTT Research, Inc., Sunnyvale, CA, USA

Gautam Reddy

4. Center for Brain Science, Harvard University, Cambridge, MA, USA

Gautam Reddy

5. Department of Organismic and Evolutionary Biology and Department of Physics, Harvard University, Cambridge, MA, USA

Michael M. Desai

Authors

1. Milo S. Johnson

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Milo%20S.%20Johnson) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Milo%20S.%20Johnson%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

2. Gautam Reddy

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Gautam%20Reddy) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Gautam%20Reddy%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

3. Michael M. Desai

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Michael%20M.%20Desai) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Michael%20M.%20Desai%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

### Contributions
MSJ, GR, and MMD conceived and wrote the paper. The author(s) read and approved the final manuscript.

### Corresponding author
Correspondence to [Michael M. Desai](mailto:mdesai@oeb.harvard.edu).

## Ethics declarations
### Ethics approval and consent to participate
Not applicable.

### Consent for publication
Not applicable.

### Competing interests
The authors declare that they have no competing interests.

## Additional information
### Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions
**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/). The Creative Commons Public Domain Dedication waiver ([http://creativecommons.org/publicdomain/zero/1.0/](http://creativecommons.org/publicdomain/zero/1.0/)) applies to the data made available in this article, unless otherwise stated in a credit line to the data.

[Reprints and permissions](https://s100.copyright.com/AppDispatchServlet?title=Epistasis%20and%20evolution%3A%20recent%20advances%20and%20an%20outlook%20for%20prediction&author=Milo%20S.%20Johnson%20et%20al&contentID=10.1186%2Fs12915-023-01585-3&copyright=The%20Author%28s%29&publication=1741-7007&publicationDate=2023-05-24&publisherName=SpringerNature&orderBeanReset=true&oa=CC%20BY%20%2B%20CC0)

## About this article
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/svg/22983715/1709451330309-8fabcb15-3179-4bdc-a1e8-250f851a928c.svg)

### Cite this article
Johnson, M.S., Reddy, G. & Desai, M.M. Epistasis and evolution: recent advances and an outlook for prediction. _BMC Biol_**21**, 120 (2023). https://doi.org/10.1186/s12915-023-01585-3

[Download citation](https://citation-needed.springer.com/v2/references/10.1186/s12915-023-01585-3?format=refman&flavour=citation)

+ Received: 06 January 2023
+ Accepted: 30 March 2023
+ Published: 24 May 2023
+ DOI: https://doi.org/10.1186/s12915-023-01585-3

### Keywords
  


> 来自: [Epistasis and evolution: recent advances and an outlook for prediction | BMC Biology | Full Text](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01585-3)
>

