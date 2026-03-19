+ [PDF](https://academic.oup.com/mbe/article-pdf/31/1/165/13171388/mst189.pdf)
+  Split View 
    - Figures & tables
    - Supplementary Data
+ [Cite](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#)

### Cite
Adrian W.R. Serohijos, Eugene I. Shakhnovich, Contribution of Selection for Protein Folding Stability in Shaping the Patterns of Polymorphisms in Coding Regions, _Molecular Biology and Evolution_, Volume 31, Issue 1, January 2014, Pages 165–176, [https://doi.org/10.1093/molbev/mst189](https://doi.org/10.1093/molbev/mst189)

Close

Journal Article

, 

1Department of Chemistry and Chemical Biology, Harvard University

Search for other works by this author on: 

1Department of Chemistry and Chemical Biology, Harvard University

Search for other works by this author on: 

Published:

11 October 2013

+ [PDF](https://academic.oup.com/mbe/article-pdf/31/1/165/13171388/mst189.pdf)
+  Split View 
    - Figures & tables
    - Supplementary Data
+ [Cite](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#)

### Cite
Adrian W.R. Serohijos, Eugene I. Shakhnovich, Contribution of Selection for Protein Folding Stability in Shaping the Patterns of Polymorphisms in Coding Regions, _Molecular Biology and Evolution_, Volume 31, Issue 1, January 2014, Pages 165–176, [https://doi.org/10.1093/molbev/mst189](https://doi.org/10.1093/molbev/mst189)

Close

Navbar Search Filter  Mobile Enter search term Search

## Abstract
The patterns of polymorphisms in genomes are imprints of the evolutionary forces at play in nature. In particular, polymorphisms have been extensively used to infer the fitness effects of mutations and their dynamics of fixation. However, the role and contribution of molecular biophysics to these observations remain unclear. Here, we couple robust findings from protein biophysics, enzymatic flux theory, the selection against the cytotoxic effects of protein misfolding, and explicit population dynamics simulations in the polyclonal regime. First, we recapitulate results on the dynamics of clonal interference and on the shape of the DFE, thus providing them with a molecular and mechanistic foundation. Second, we predict that if evolution is indeed under the dynamic equilibrium of mutation–selection balance, the fraction of stabilizing and destabilizing mutations is almost equal among single-nucleotide polymorphisms segregating at high allele frequencies. This prediction is proven true for polymorphisms in the human coding region. Overall, our results show how selection for protein folding stability predominantly shapes the patterns of polymorphisms in coding regions.

## Introduction
How and why the observed patterns of DNA polymorphisms arise in the genome, and what are their molecular and phenotypic effects, is central to our understanding of the evolutionary forces at play in nature. In public health and medicine, polymorphisms are crucial in inferring the origin of diseases and genetic traits (McCarthy et al. 2008) and in understanding the spread of pathogens such as viruses (Vignuzzi et al. 2006).

A major utility of polymorphisms is in estimating the distribution of fitness effects (DFE) of mutations. Although the DFE has been measured for viruses (Sanjuan et al. 2004), its measurement in living organisms is difficult and resolution-limited (Eyre-Walker and Keightley 2007). Thus, studies on the DFE have largely relied on Bayesian maximum-likelihood approaches to fit population dynamic and demographic models to patterns of polymorphisms and amino acid differences between species (Bustamante et al. 2005; Eyre-Walker et al. 2006; Sawyer et al. 2007; Kryukov et al. 2009). A consensus result is that the DFE is characteristically skewed and can be described by a gamma distribution (Bustamante et al. 2005; Eyre-Walker et al. 2006; Kryukov et al. 2009). There is, however, a debate on the magnitude and relative balance between the types of substitutions that fix in the population—some consider them to be neutral or near neutral (Ohta 1973; Nei et al. 2010), whereas others consider them to be predominantly adaptive and beneficial (Smith and Eyre-Walker 2002; Eyre-Walker and Keightley 2007). Indeed, there is a longstanding debate (with patterns of polymorphisms used as empirical support by all sides) on whether evolution is primarily neutral (Kimura 1968; Ohta 1973; Nei et al. 2010), adaptive (McDonald and Kreitman 1991; Smith and Eyre-Walker 2002), or driven by drift (Lynch and Conery 2003). Distinguishing adaptive, neutral, and nearly neutral modes of molecular evolution remains challenging (Akashi et al. 2012) because the predictions are overlapping.

The patterns of polymorphisms can also be used to gain insight into the dynamics of allele segregation and in determining which mutations are eventually fixed or lost in evolution (for a practical example, see Strelkowa and Lassig 2012). In general, the dynamics is expectedly complicated because of the intrinsic stochasticity of drift and mutation, compounded by history and demography of the evolving population. The trajectories of mutations in polyclonal populations are dynamically rich because of potential clonal interference, hitchhiking, and/or background selection. Major advances have been described in recent years to infer the dynamics (Gerrish and Lenski 1998; Wilke 2004; Desai and Fisher 2007), but their connection to molecular biophysics is still unclear.

Most of the approaches in the studies above assume the DFE and then infer the possible dynamics (Gerrish and Lenski 1998; Desai and Fisher 2007) or assume the possible dynamics and then infer the DFE (McDonald and Kreitman 1991; Bustamante et al. 2002; Smith and Eyre-Walker 2002). This poses a potential limitation because demography and the DFE are intrinsically coupled (Silander et al. 2007). More importantly, these approaches lack explicit connection to the molecular properties of segregating polymorphisms, such as folding stability, or to the widely accepted selective constraints on protein evolution, such as avoidance of protein misfolding and misinteraction (Pal et al. 2006; Drummond and Wilke 2008; Zhang et al. 2008; Koonin and Wolf 2010).

An alternative and complementary approach is to develop an evolutionary framework based on a realistic genotype–phenotype relationship and allow the patterns of polymorphisms, mutational dynamics, and the DFE to be consequences of the model. Knowledge of the genotype–phenotype relationship entails systematic accounting of the molecular properties encoded by the genome and the extensive mapping of their interactions whether physical, biochemical, or genetic. Although these relationships are overall complex, at least for coding regions, there is a general consensus that the fitness of the organism is a function of the metabolic output (Edwards et al. 2001; Duarte et al. 2007), itself also a function of the biophysical properties of proteins (Bar-Even et al. 2010). Another emerging constraint on protein evolution is the global selection against the cytotoxic effect of aggregated, presumably misfolded proteins (Bucciantini et al. 2002). The universality of such a constraint is manifested in the consistent correlation between the rate of protein evolution and cellular abundance (Drummond and Wilke 2008; Yang et al. 2010; Serohijos et al. 2012).

To arrive at a more mechanistic origin of the patterns of polymorphisms that explicitly account for their biophysical effects, we coupled molecular biophysics, the emerging knowledge of the genotype–phenotype relationship, and explicit population dynamics simulations. First, we show that the DFE is not constant but a dynamic consequence of the evolutionary process. Specifically, under the equilibrium of mutation–selection balance and because of the epistatic interactions between mutational effects on protein folding stability, the DFE evolves to be concentrated around effective near neutrality with the characteristic gamma distribution (Kryukov et al. 2009). Second, even under equilibrium, we observe pervasive background selection and hitchhiking that expand the regime of effective near neutrality, consistent with prior studies (e.g., McVean and Charlesworth 2000; Neher and Shraiman 2011). Because we base our premise on molecular biophysics and emerging genotype–phenotype relationships, our approach could provide a molecular foundation to these observations. More importantly, we could also relate these findings in evolutionary biology to predictions of their molecular consequences. In particular, we predict that if evolution is indeed under equilibrium, the fraction of stabilizing and destabilizing mutations are almost equal among single-nucleotide polymorphisms (SNPs) segregating at high allele frequencies. Despite some simplifying assumptions, this prediction is proven true for polymorphisms in the human coding region.

## Results
### Coupling Biophysics and Population Dynamics in the Polyclonal Regime
To couple population dynamics and molecular biophysics, we model an evolving population of _N__e_ = 103 organisms with explicit genomic sequences consisting of ten open reading frames that code enzymes from the folate biosynthetic pathway (fig. 1_A_ and [supplementary table S1](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online), an essential biochemical pathway for amino acid synthesis. These model genes have corresponding 3D structures from the protein databank that can be used in estimating the biophysical effects of mutations (see Materials and Methods). We assume that the fitness _f_ of the organism or its probability of replication is a function of both the total metabolic output (Dykhuizen et al. 1987) and the total number of misfolded proteins in the cell; the latter accounts for the cytotoxicity of misfolded proteins (Drummond and Wilke 2008). Thus, the total fitness is 

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215414360-a8412313-4454-4689-a4ad-8652f3ada108.gif)

(1)

Fig. 1.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709215411622-e270cd5b-631b-41d8-bb17-459fad3a3fe8.jpeg)

Model of protein evolution that couples biophysics and population dynamics in the polyclonal regime. (_A_) A model of organism composed of ten genes from the folate biosynthetic pathway ([supplementary table S1](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). Cellular fitness _f_ is proportional to the effective metabolic output of this pathway and the total number misfolded proteins ([eqs. 1–3](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1%20mst189-M2%20mst189-M3)). The population is subject to mutation, drift, and purifying selection. Mutations can change the folding stability Δ_G_ of a gene and hence the fitness of the cell (see Materials and Methods). Effective population size is _N__e_ = 103. (_B_) Fitness under mutation–selection balance. (_C_) Detailed trajectory of the folding stability of each gene in individuals in the population. Individual cells are indexed along the _y_ axis, where spatial proximity is proportional to kinship.

From linear pathway theory, the flux term may be expressed as (see Materials and Methods) 

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215414358-f62f1901-7270-45ca-8477-22862061c909.gif)

(2)

where _ε__i_ is the enzyme efficiency, _A__i_ is the cellular abundance, and Δ_G_i is the folding free energy. The index _i_ is for each gene in the model. We make the simplifying assumption that all enzymes have the same efficiency _ε__i_ = 1. The factor _β_ = 1/_k__B__T_ (_k__B__T_ = 0.593 kcal/mol) and _a_0 is a normalizing constant (see Materials and Methods). The contribution to fitness of the misfolding toxicity may be expressed as (Serohijos et al. 2012) 

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215414358-f7aa4ea6-e7fb-4bb9-bbb4-3935a8236a64.gif)

(3)

where _c_ = 10−4 is the fitness cost per misfolded protein (Drummond and Wilke 2008). In this formulation, the optimal fitness is 1 and occurs in the regime where proteins are very stable ([supplementary fig. S1](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). [Equations (1)–(3)](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1%20mst189-M2%20mst189-M3) constitute an explicit biophysics-based genotype–phenotype relationship. The model also features epistasis between genes because they are all coupled in the fitness function ([eqs. 1–3](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1%20mst189-M2%20mst189-M3)).

We coupled the genotype–phenotype relationship to an evolutionary dynamics model that includes mutation, selection, and drift (see Materials and Methods and [supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). Specifically, at each replication event, a cell divides into two daughter cells, each can potentially mutate at the rate of _µ_ = 0.01/genome/replication (1.5 × 10−6/base pair/replication). If the mutation is nonsynonymous, we estimate the change in folding stability (ΔΔ_G_ = Δ_G_mutant − Δ_G_wildtype) using a physical force field (Yin et al. 2007) and then update the fitness of the organism (see Materials and Methods). We ran our simulation until it achieved mutation–selection balance (fig. 1_B_). Throughout the simulation run, we saved the full history of all arising mutations and the genomes of all surviving individuals (see Materials and Methods). Analysis was performed only in the regime of mutation–selection balance.

### Mutation–Selection Balance Under Pervasive Clonal Interference
We then analyzed the various types of mutations and the dynamics of their segregation in the population. Because the simulations are performed at high mutation rate, there is pervasive clonal interference (fig. 1_C_). We classified all arising mutations according to their fitness effect, quantified by the selection coefficient _s_ = (_f_mutant_ − __f_wildtype)/_f_wildtype. Because the fitness function is protein-centric, mutations that increase folding stability (ΔΔ_G_ < 0) are beneficial, whereas those that decrease stability (ΔΔ_G_ > 0) are deleterious. Synonymous substitutions are considered neutral. In figure 2_A_, we show typical trajectories of mutations that eventually fixed in the population (see also [supplementary fig. S3](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). In the regime of high mutation rate, several mutations arise over the lifetime of a segregating allele (fig. 1_C_ and 2_A_). The distribution of minor allele frequencies for the SNPs in simulation and the human coding region are shown in [supplementary figure S4](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529046&Signature=KIleYeE8xaFeXx66obnt8eGI~amLZ3mq2UnXJQ-jq02~RCXSJJ3JE~e9g7fLRqL6yQwd5Mzo6cFN7VRKXaJ0KCVuNaRA0t8gEXOPinQIfoTPHgxHH1tnQQ7hSDVeZ4DMJ5vn0ld27HKW1dH3SLYw7AoD8gBHQ5kBWAjPu5i3mZYqL3vr-ooKtisM3UdbatjpmENHJtawsyjV3I~2vfMYSWXpIkTs0DdX~u7oZVi4r2BnOmV4UAwNCrcMih62KhAz8APcmkTgMOfwTis5ggBdf~46ZMAoHIeaYzO-dguJwpOAnsomBVO4CrGUHehmYu6YVwVEQDNORHTY1BSRJ~DMCg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online. 

Fig. 2.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709215414361-90fa6af3-bbc4-4555-a481-6285366bf2ca.jpeg)

Mutation–selection balance under pervasive clonal interference. (_A_) Sample history of mutations that reached fixation. Time interval corresponds to figure 1_C_. Arrows indicate the correlated fixation of mutations. (Only three genes are shown; see [supplementary fig. S3](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online, for the complete trajectory.) (_B_) Selection coefficients of mutations that successfully fixed. (_C_) Extent of polymorphism in the evolving population. Drop in diversity accompany clonal sweeps. (_D_) Distribution of SNPs in the simulation. All SNPs (blue); SNPs with allele frequencies ≥1% (black).

Our simulations exhibit clonal sweeps, characterized by the correlated fixation of mutations, usually driven by a beneficial mutation (fig. 2_B_). Such clonal sweeps are typically characterized by a slow rise followed by a rapid drop in polymorphisms (fig. 2_C_). The anatomy of such sweeps entails deleterious mutations hitchhiking on the beneficial mutations; consequently, these deleterious mutations now have a significant probability of fixation compared with the monoclonal regime (fig. 3). Beneficial mutations, however, do not fix as likely as in the monoclonal regime because they now arise in the context of many deleterious mutations (fig. 4_A_, _C_, and _E_; [supplementary fig. S3](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). The deleterious hitchhikers effectively dampen a beneficial mutation’s overall fitness effect, thus lowering its probability of fixation (fig. 3). The extent of hitchhiking by destabilizing mutations on stabilizing ones can be estimated from the distribution of ΔΔ_G_ for all possible arising nonsynonymous mutations available to a wildtype sequence. This distribution appears to be universal across types of protein folds (Tokuriki et al. 2007). Approximately 20% of nonsynonymous mutations are stabilizing (ΔΔ_G_ < 0), whereas the rest are destabilizing (Tokuriki et al. 2007; Zeldovich et al. 2007); see also the blue curve in (fig. 6_B_). The extent of hitchhiking and background selection is generally a function of mutation rate and population size; nonetheless, from purely biophysical considerations, there are potentially four destabilizing mutations that could hitchhike for every stabilizing mutation. 

Fig. 3.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709215414389-7cc44596-ae1d-40bb-bc3d-144da85a2490.jpeg)

Probability of an arising mutation to reach an allele frequency _λ_. _λ_ = 1 corresponds to fixation. Red line is the probability of fixation in the monoclonal regime. Fixation probability of a neutral mutation in the monoclonal regime (1/2_N__e_) is indicated. Interference among clones takes two specific forms: background selection and hitchhiking.

Fig. 4.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709215416724-9399d50a-8988-46dc-9b30-834dde778bbe.jpeg)

Influence of epistasis in the mapping between the molecular effect of a mutation ΔΔ_G_ to its phenotypic effect _s_. _X_ axis is the premutation Δ_G_. Mutations are colored according to the magnitude of the ΔΔ_G_ (see leftmost panel for color assignment). (_A_) Arising random beneficial (stabilizing) mutations. (_B_) Fixed beneficial mutations. (_C_) Arising random deleterious (destabilizing) mutations. (_D_) Fixed deleterious mutations. In panels (A)–(D), premutation Δ_G_ modulates the magnitude of _s_ for a given ΔΔ_G_ such that mutations are more neutral when it occurs in more stable proteins. (_E_) Solid line is the distribution of arising beneficial mutations (panel A) while dashed line is the distribution of arising deleterious mutations (panel C). Each histogram is normalized to the total number of mutations. (_F_) Similar to panel E but for fixed mutations. In the stable regime, drift dominates, whereas in the unstable regime, selection dominates. For the sake of clarity, we plot only 1/102 or 1/(10_N__e_) of the total number of arising mutations sampled randomly.

We also show the probability that a mutation reaches an allele frequency _λ_ (fig. 3). Interestingly, alleles segregating at ∼50% are almost determined to fix (fig. 3). We note that the pervasive clonal interference in our simulation occurs under mutation–selection balance and is distinct from the more common treatment of clonal interference in literature, which is only among beneficial mutations and specifically in the context of adaptation (Gerrish and Lenski 1998; Fogle et al. 2008).

### Fitness and Molecular Effects of Mutations Under Mutation–Selection Balance
As noted earlier, one of the primary utilities of the patterns of polymorphism in genomes is quantitatively estimating the DFE. Thus, we next explore the resulting DFE from our simulation and compare the distribution with estimates from Bayesian approaches.

In the genotype–phenotype relationship defined by [equations (1)–(3)](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1%20mst189-M2%20mst189-M3), epistatic interactions on folding stability play a crucial role in determining the fitness effects of mutations (fig. 4). Specifically, in our model, the fitness effect of a mutation with a molecular effect ΔΔ_G_ depends on the folding stability of the current wildtype or Δ_G_premutation (fig. 4). The same ΔΔ_G_ can have very near neutral effect if it occurs in proteins that are stable but can have sizable effects if it occurs in proteins that are unstable. For example, a destabilizing mutation of ΔΔ_G_ = 1 kcal/mol occurring in genes with Δ_G_premutation = −8 kcal/mol has a fitness effect of <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215416728-c67a694a-5bb4-4c09-b1e5-56199e48f6a0.gif)⁠; however, the same mutation occurring in genes with Δ_G_premutation = −0.5 is lethal. A stabilizing mutation of ΔΔ_G_ = −1 kcal/mol occurring in genes with Δ_G_premutation = −8 kcal/mol has a fitness effect of <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215416725-69bb8f2e-f03d-4e22-988a-c68e121f18e7.gif)⁠; however, if it occurs in genes with Δ_G_premutation = −0.5 kcal/mol, the mutation is extremely beneficial <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215416733-feed4c78-cb61-479d-a98f-3c9a1f9a41fd.gif)⁠. Thus, in the regime where proteins are stable, both destabilizing and stabilizing mutations have <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215416725-8b3b15e8-a8a7-47c8-84ba-2e2d68a7c45c.gif)⁠; however, because of the larger supply of destabilizing than stabilizing mutations, most mutations that fix are destabilizing. This imbalance gives rise to a mutational drift of Δ_G_ toward less stable proteins and away from the flatter part of the fitness landscape (fig. 4_f_ and [supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). In the regime where proteins are less stable, selection for stabilizing and selection against destabilizing mutations lead to fixation of a larger fraction of stabilizing mutations (fig. 4_f_ and [supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). This dominance of selection drives Δ_G_ toward more stable proteins and away from the less fit part of the fitness landscape ([supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). The balance between selection and drift occurs at some intermediate folding stability (fig. 4_f_, ∼4 kcal/mol), where stabilizing and destabilizing mutations have equal likelihood of being fixed.

Because mutation–selection balance is a dynamic equilibrium, the protein finds itself on the left or right hand side of ∼4 kcal/mol, but on average, it resides in this neighborhood, giving rise to the observation that proteins are “marginally stable” (Taverna and Goldstein 2002; Bloom et al. 2007; Zeldovich et al. 2007). The balance between drift and selection defines the mode of the equilibrium distribution of folding stabilities (fig. 4_E_). This equilibrium distribution is in agreement with the empirically measured Δ_G_ distribution in ProTherm (Kumar et al. 2006), as pointed out in earlier works (Zeldovich et al. 2007; Wylie and Shakhnovich 2011). Additionally, for protein coding regions, the strictly neutral regime (_s_ = 0) is not a stable attractor in protein evolution because mutational drift due to nonsynonymous substitutions always drives proteins toward marginal stability (figs. 4_F_ and 5) (Taverna and Goldstein 2002).

Because the folding stability Δ_G_ evolves as consequence of mutation–selection balance, so should the fitness effect _s_, which itself is a function of folding stability. Thus, the DFE is expectedly a dynamic consequence of the resulting population dynamics. Shown in figure 5_B_ and _C_ are the resulting DFE of arising random mutations and fixed nonsynonymous substitutions. The DFE of fixed deleterious mutations is bounded on one side by drift away from the neutral regime (i.e., drift from stable Δ_G_) and on another side by selection (fig. 4_C_). The DFE of fixed beneficial mutations is more nuanced. It is bounded on one side by drift and limited on the other side by the supply of stabilizing mutations. These stabilizing and beneficial mutations have only effectively near neutral effect in the background of the folding stability values under mutation–selection balance (fig. 4_B_). In short, the observation of marginal folding stabilities of proteins is coupled to the effective near neutrality of the fitness effects of fixed amino acid substitutions. 

Fig. 5.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709215418811-714a4d10-561e-4055-8b8e-179ccbf77d4b.jpeg)

Fitness and molecular effects of mutations under mutation–selection balance. (_A_) Mapping of ΔΔ_G_ to the selection coefficient among fixed mutations. Dots are colored similar to figure 4. (_B_) Arising random mutations are predominantly deleterious (fig. 4_A_, _C_). The deleterious and beneficial DFE are both characteristically leptokurtic and fits a gamma distribution. Stricly lethal mutations (_Ns_ = −103) are excluded in the fit to a gamma distribution. (_C_) The consequence of mutation–selection balance is a bimodal distribution of s and, in particular, equal number of fixed beneficial and deleterious mutations. Strict neutrality (_s_ = 0) is not a stable fix point because mutational drift drives proteins to destabilization (fig. 4_F_). (_D_) Bimodal and equal fraction of fixed beneficial and deleterious _s_ (panel _C_) maps into a symmetric distribution ΔΔ_G_.

Additionally, under mutation–selection balance, the magnitude of the selection coefficient is of near neutral effect, whereas the magnitude of the folding stability changes is far from neutral (fig. 5_A_). The nonneutrality of the molecular effect (ΔΔ_G_) and the near neutrality of fitness effect _s_ are due to the background Δ_G_, which evolves to an equilibrium distribution that ensures the near neutrality of the fixed deleterious and beneficial mutations (fig. 5_A_). The effective near neutral theory, originally a postulate (Ohta 1973), finds a solid and mechanistic foundation in protein biophysics and the selection against protein misfolding and selection for function due to metabolic flux.

We note that the resulting DFE from simulations is skewed and can be fitted to a gamma distribution (fig. 5_C_ and _D_), in agreement with studies that estimated the DFE using maximum likelihood methods on human and in flies (Bustamante et al. 2005; Eyre-Walker et al. 2006; Kryukov et al. 2009). Similar works have also shown that most mutations could be of near neutral effect (Bustamante et al. 2005; Eyre-Walker et al. 2006; Sawyer et al. 2007; Kryukov et al. 2009); however, the molecular basis was unclear. Our work provides a molecular and mechanistic origin of these observations based on the emerging genotype–phenotype relationships (eqns. 1–3).

Mutation–selection balance is a dynamic equilibrium; thus, there should be equal numbers of fixed beneficial and deleterious mutations, a result hypothesized as early as 1930 by Fisher (1930) and articulated recently in the monoclonal regime by some groups (Sella and Hirsh 2005; Mustonen and Lassig 2009). Our own simulations in the monoclonal regime with a biophysics-based genotype–phenotype relationship (Serohijos et al. 2012) also confirm this hypothesis ([supplementary figs. S7](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) and [Supplementary Data](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). We show that despite the more complicated dynamics in the polyclonal regime, this inference is robust as manifested by the bimodal distribution of the selection coefficients of fixed mutations (fig. 5_C_). In strictly monoclonal populations, the boundary of near neutrality is at _N_|_s_|∼ 1 (Sella and Hirsh 2005; Goldstein 2011; see also [supplementary figs. S7](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) and [Supplementary Data](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). However, in the polyclonal regime, because of extensive hitchhiking and background selection that effectively lead to a flatter probability of fixation (fig. 3), the bounds of effective near neutrality extend beyond _N_|_s_|∼ 1 (fig. 5_A, C_).

### Stability Effects of Nonsynonymous SNPs Segregating at Various Allelic Frequencies
We have shown that the inferred DFE (Bustamante et al. 2005; Eyre-Walker et al. 2006; Kryukov et al. 2009) can be explained under mutation–selection balance. Because this result from simulations seem to contradict the large body of literature arguing for a predominantly adaptive (hence, out of equilibrium) tempo of protein evolution (McDonald and Kreitman 1991; Smith and Eyre-Walker 2002), we then sought to establish another empirical support for our analysis.

We know the full history of all mutations, thus we can relate the stability effects (ΔΔ_G_) of SNPs to their allele frequencies (fig. 6_A_). Most arising mutations are destabilizing, and those SNPs segregating at low frequencies are still predominantly destabilizing (fig. 6_A_). This high fraction of destabilizing mutations among low-frequency SNPs is directly supported by explicit biophysical measurements of the stability effects of SNPs from a diverse set of 16 human enzymes (Allali-Hassani et al. 2009) and by bioinformatics analysis (Yue and Moult 2006). This result is also in agreement with the observation that disease-associated SNPs, because of their very deleterious effects, segregate at lower frequencies than regular polymorphisms (De Baets et al. 2012). On the other hand, among SNPs segregating at higher allele frequencies, the fraction of destabilizing SNPs decreases because of purifying selection. In particular, for SNPs segregating at 40% allele frequency, close to the probability of fixation (fig. 3), the fraction of stabilizing and destabilizing SNPs are almost equal (fig. 6_A_). The estimates of the folding stability effects of SNPs in the human coding region (fig. 6_B_) indeed show the increasing manifestation of purifying selection among SNPs of higher allele frequencies. Most importantly, arguing for mutation–selection balance (at least for protein evolution), SNPs that are close to fixation approach the limit of equal fraction of stabilizing and destabilizing ΔΔ_G_ (fig. 6_B_). 

Fig. 6.

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709215418928-f8e3656a-2780-4a08-a384-755aee9a2386.jpeg)

Stability effects of nonsynonymous SNPs segregating at various allelic frequencies. (_A_) _**λ**_ is the maximum frequency that a segregating SNP attains over its lifetime. Selection shifts the distribution of higher frequency alleles toward more stabilizing SNPs. (_B_) ΔΔ_G_ of SNPs in the coding region of the human genome estimated using FoldX (Schymkowitz et al. 2005) and compiled by the database SNPeffect (De Baets et al. 2012) (see Materials and Methods). Allele frequency is taken from dBSNP. For arising ΔΔ_G_, we use the empirically measured ΔΔ_G_ from a diverse set of proteins in the ProTherm database (Kumar et al. 2006; Tokuriki et al. 2007). Enclosed in parentheses are the number of SNPs for the indicated frequency cutoff.

## Discussion
By developing an evolutionary model based on molecular biophysics and on an intuitive genotype–phenotype relationship, we provide a more mechanistic and molecular understanding on how polymorphisms could arise and segregate in the coding region of genomes. Several works have tried to bridge molecular biophysics and population genetics both in coding (DePristo et al. 2005; Bloom et al. 2007; Drummond and Wilke 2008; Goldstein 2011; Serohijos et al. 2012) and noncoding (Mustonen et al. 2008) regions of genomes. However, these studies are in the monoclonal regime and do not explore the relevance of biophysics to polymorphisms as we do here.

The DFE is not a constant in evolution but an evolvable property and a consequence of the evolutionary dynamics. In this work, we showed how, in the context of coding region evolution, the protein folding stability evolves to ensure the near neutrality of the fitness effects of stabilizing mutations, reaching a dynamic steady state defined by the mutation–selection balance. Specifically, the DFE evolves to be centered around effective near neutrality with a characteristic skewed gamma distribution. The boundaries of effective near neutrality are strongly determined by the population dynamics; in this case, pervasive clonal interference leads to weakened selection that expands the regime of near neutrality. This effective weakening of selection due to hitchhiking has been described previously (e.g., McVean and Charlesworth 2000; Neher and Shraiman 2011). However, here, we provide a mechanistic and direct connection on how it can arise in the context of protein evolution. The extent of the weakening of selection is expectedly a function of population size and mutation rate (Neher and Shraiman 2011; Wylie and Shakhnovich 2011)—in this work, we chose the population size of 103 organisms, which we tried to be as close the human effective population size (104) (Lynch and Conery 2003) but still computationally tractable.

Under this dynamic equilibrium of mutation–selection balance, the near neutral theory (Ohta 1973) is not a postulate but a robust consequence of the interplay between biophysics and evolutionary dynamics. The standard molecular argument for the claimed neutrality of most mutations is that a significant fraction of residues in a protein (∼85%) do not participate in the active site thus unrelated to function. However, this is inconsistent with molecular biophysics where mutations are never neutral, as they always affect folding stability (Tokuriki et al. 2007; Zeldovich et al. 2007) and other molecular properties of proteins such as their interactions with other proteins in cytoplasm (Vavouri et al. 2009; Heo et al. 2011). Here, we have shown the despite the nonneutral effects of mutations at the level of macromolecules, the population evolve to ensure the near neutrality of their fitness effects (fig. 5).

We also note the major distinctions between our work and the theoretical models that advocate selection for mutational robustness (van Nimwegen et al. 1999; Wilke et al. 2001). First, these neutral network models assume that mutations are either neutral or lethal. The relative fraction of neutral to lethal neighbors defines the degree of mutational robustness. In our model, no a priori assumptions are made on the DFE. As argued above, the same ΔΔ_G_ mutations could have a fitness effect of be <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215418934-2d4172c9-a5ac-4273-b7a8-b940cff5f629.gif) or <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215418930-d7a8f242-0482-44ed-83ea-3628adf5a265.gif) depending on background Δ_G_premutation.

Second, these theoretical and computational models also assume that there are multiple peaks in the fitness landscape—the flattest, most mutationally robust peak is distinct from the highest peak, which could be less robust. In our, genotype–phenotype model based on the thermodynamics of protein folding stability, the regime that is most robust is also the regime that is most fit ([supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online), and this is the regime of high folding stability. We note, however, that under our model of mutation–selection balance, proteins evolve toward marginal stability, hence organisms are not optimally fit ([supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online).

Third, in the models arguing for mutational robustness, under low mutation rate, the population evolves to higher peaks even if less robust. Under high mutation rate, the population evolves to the flatter peaks, because selection for mutational robustness outweighs selection for fitness, hence the “survival of the flattest.” In both cases of high and low mutation rates, evolution is always a process of optimization—high robustness at high mutation rate or high fitness under low mutation rate. In our model, however, the evolution is always toward mutation–selection balance, where proteins are marginally stable (fig. 4), the fitness effects are near neutral (fig. 5), and the organisms are not optimally fit ([supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). This evolution toward marginal folding stability and suboptimal fitness holds under low mutation rate, where the bounds of near neutrality is _N_|_s_|∼ 1 ([supplementary figs. S7](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) and [Supplementary Data](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)), and under high mutation rate, where the bounds of near neutrality is greater than _N_|_s_|∼ 1 because of hitchhiking and background selection (fig. 5). Of course, when the mutation rate is very high or when the population size is too small, the condition for mutation–selection balance may not be satisfied leading to extinction (Zeldovich et al. 2007; Wylie and Shakhnovich 2011). In short, in our model, evolution is not necessarily a process of optimization.

Fourth, in the neutral network models of sequence evolution, the most neutral part of the landscape represents a stable attractor. In our model, however, the flattest part of the landscape is not an attractor because of mutational drift. Thus, evolution proceeds “toward _near_ neutrality” is the correct description rather than simply “toward neutrality.”

Altogether, the terms _neutral_ and _near neutral_ is rather unfortunate, because they suggest that the latter is simply an update or a correction to the neutral theory. However, as noted above, there are fundamental mechanistic and conceptual differences between the two, and it is the near neutral theory that is most consistent with protein biophysics.

We have also shown that the patterns of polymorphisms, when framed in very direct observables such as changes in folding stability, in fact, support the argument for a predominantly nonadaptive tempo of evolution (Bustamante et al. 2005), contrary to prior claims resulting from the so-called tests of neutrality (McDonald and Kreitman 1991; Smith and Eyre-Walker 2002). In the future, to further reconcile the adaptive view of evolution and the effective near neutrality (as argued here), an extensive analysis of polymorphisms generated from our approach and the McDonald–Kreitman tests must follow. Additionally, biophysical analysis of SNPs in model organisms across all kingdoms of life will systematically test the universality of the results demonstrated in figure 6_B_.

We explicitly discussed the mechanism for how the DFE of coding region mutations becomes centered around effective near neutrality under mutation–selection balance. This result may be extended to the noncoding region because the emergent near neutrality under mutation–selection balance is robust to the details of the fitness function, as long as the genotype–phenotype relationship features a convex curved functional form reflecting the diminishing fitness improvement upon further optimization of molecular properties (Akashi et al. 2012). In the noncoding region, a “curved” genotype–phenotype relationship arises from the ability of replication-related proteins (such as polymerases, transcription factors) to bind to DNA or RNA (Mustonen and Lassig 2009). In this respect, the thermodynamics of protein–DNA interaction is analogous to the thermodynamics of protein folding.

The molecular view of mutation–selection balance described here also clarifies a meaningful distinction (previously pointed out in Mustonen and Lassig [2009]) between positive selection (existence of beneficial mutations that eventually outcompetes wildtype) and _true_ adaptation (moving selection target). Indeed, here, there is an ample supply of beneficial mutations originating from constantly arising stabilizing mutations; however, these beneficial mutations are not truly adaptive but only maintain mutation–selection balance. That is, the observation among biophysicists that proteins are marginally stable (Privalov 1979; Taverna and Goldstein 2002; Kumar et al. 2006; Bloom et al. 2007; Zeldovich et al. 2007) and the observation in evolutionary biology that coding region evolution is predominantly nonadaptive (e.g., in human; Bustamante et al. 2005) are the molecular and phenotypic manifestation of the balance between drift and selection for folding stability.

The nature and shape of the DFE should depend on the mutation rate, population size, and number of genes in the organism. However, the natural expectation is that the higher population sizes and higher mutation rates increase the extent of clonal interference and thus could in principle further expand the bounds of near neutrality. The systematic effects of mutation rate, population, and the number of genes on polymorphisms in the context of this biophysics-based population dynamics model will be explored in future studies.

The approach we present here can only be improved as we become more quantitative and systematic in our understanding of the genotype–phenotype relationship and integrate it into a comprehensive cellular model (Karr et al. 2012). The explicit genotype–phenotype relationship could be the starting point for investigating the evolutionary consequences of the cellular quality control machinery (chaperones and proteases) that can modulate the fitness effects of mutations and hence the expected patterns of polymorphisms. Additionally, a realistic cellular model representing more complete proteomic and metabolic network information could explore the relationship between the DFE per gene and the DFE on the whole organism (Soskine and Tawfik 2010).

We note that this approach of coupling molecular biophysics and population genetics has already been crucial in explaining other emerging genomic patterns, such as why highly abundant proteins consistently evolve slowly (Pal et al. 2001; Drummond and Wilke 2008; Yang et al. 2010; Serohijos et al. 2012) or tend to be more stable (Drummond and Wilke 2008; Cherry 2010; Serohijos et al. 2012, 2013). Because the representation of the evolving population is explicit, our approach could also provide a framework to account for the role of changing environments. We also believe that this approach could provide an explicit, mechanistic null model for statistically inferring mutations that are truly functional and adaptive (Kumar et al. 2012).

## Materials and Methods
### Fitness Function
To begin with the most basic model of evolution that has some semblance of realism in accounting for the biophysical properties of proteins and the genotype–phenotype relationship, we choose to model an organism ([supplementary table S1](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online) based on a core metabolic pathway and postulate that its fitness is proportional to the metabolic flux (Milo and Last 2012). Assuming that all the enzymes follow a linear metabolic pathway, the fitness due to flux <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215418938-892a9535-e6ae-460a-96de-f2f741bf141f.gif)⁠, where _a_ is the number of input metabolites, _ε__i_ is the enzymatic efficiency, and _C__i_ is the number of functional copies. The functional copies correspond to number of enzymes in the folded (native) state _C__i_ = _A__i__P_nat,_i_, where _P_nat,_i_ is the Boltzmann probability of the protein _i_ to be in the native state and _A__i_ is the total concentration of protein _i_ in the cell. Assuming a two-state folding thermodynamics <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215419057-25d8c5f7-e24d-4ef1-a936-ebdcb2a7e2c4.gif) (Privalov 1979).

Another emerging constraint in protein evolution is the global selection against the cytotoxicity of protein misfolding (Drummond and Wilke 2008; Serohijos et al. 2013). Formally, the fitness due to toxicity is <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215420192-a30745f9-6436-4b30-be12-288b494f86a8.gif)⁠, where _c_ = 10−4, the fitness cost per misfolded protein (Drummond and Wilke 2008; Geiler-Samerotte et al. 2011). Altogether, the total fitness is described by [equation (1)](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1). Without loss of generality, we require that fitness is optimally 1 at very stable regimes, <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215420199-96833670-82fb-40ee-97a6-593d320fc1f6.gif)⁠, leading to <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215420189-c13be511-f8f7-4dbf-9af9-b045c7ff7eed.gif)⁠. When _f_toxicity > _f_flux, the fitness is defined to be _f_ = 0, hence <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215420195-ebd5193b-fb0d-4cb2-9619-f2a5eb9b78dd.gif)⁠. The resulting fitness defined by [equations (1)–(3)](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1%20mst189-M2%20mst189-M3) is essentially parameter-free.

In our earlier work (Serohijos et al. 2012), the goal was to determine whether selection against the cytotoxity of protein misfolding is sufficient to explain the widely observed abundance–evolutionary rate correlation (Drummond and Wilke 2008). Thus, to make an explicit comparison and connection with earlier literature, we only focused on the selection against protein misfolding. In this study, we generalize the fitness function to include the notion of selection for more functional copies, motivated by numerous works that map metabolic output to fitness (Edwards et al. 2001; Duarte et al. 2007), which depends on the biophysical properties of proteins (Bar-Even et al. 2010).

We note that in our model, there is epistasis between genes because they are coupled in the nonlinear fitness function ([eqs. 1–3](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1%20mst189-M2%20mst189-M3)). In the fitness effect <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215420193-ac7e1e06-a779-4a5c-8139-13cb65e4559b.gif)<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215421500-1b280ffc-d709-490b-8604-2e090956168e.gif)⁠, the value of _f_premutation is determined by the biophysical properties of all genes in the cell. Thus, the quantitative effect of a prior mutation in one gene could influence the fitness effect of the current mutation in another gene. The epistasis is strongest when mutations fall on the genes with low folding stability, because this is where the curvature of the fitness landscape is most pronounced ([supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online).

### Evolutionary Dynamics with Mutation, Selection, and Drift
We follow the standard Moran process in the evolutionary simulations ([supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). The fitness function ([eq. 1](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1)) defines the replication rate. We make no prior assumption on the dynamics and/or the resulting DFE. To update the evolution of the organism, we use the Gillespie algorithm: At each replication event, the replicating cell splits into two daughter cells, each can potentially mutate at the rate of _µ_ = 0.01/genome/replication. If the mutation is nonsynonymous, the folding stability of the mutated gene is updated with ΔΔ_G_ values estimated using a physical force field and the 3D structures as input (discussed later). We performed this simulation of mutation, selection, and drift toward the dynamic equilibrium imposed by mutation–selection balance (fig. 1_B_).

All the genes are initialized with folding stability Δ_G_0 = −5 kcal/mol at time _t_ = 0. This dynamic equilibrium of mutation–selection balance is robust to the choice of starting Δ_G_0. When the proteins are initialized at the very stable regime, these genes will migrate toward less stable regime because of drift. On the other hand, when the proteins are initialized in the less stable regime, the genes migrate toward greater folding stability because of selection. All analysis reported are performed only after the population has reached mutation–selection balance (fig. 1).

After the simulation reaches mutation–selection balance, we save the information of all arising mutations, including their location in the genome, nucleotide change, ΔΔ_G_, and _s_. We also save the genomes of all cells in the population every 10 generations (i.e., every 10_N__e_ replication events). The information allows us to reconstruct the trajectories and all arising mutations.

In our earlier work (Serohijos et al. 2012), where _Nµ _≪ 1 and the population is monoclonal, we employed Wright–Fisher’s discrete nonoverlapping generations model. Also, in the earlier work, we defined the fitness as <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215421487-d0f2aa8a-c5e7-46ec-a281-e03781d4ced0.gif) following Drummond and Wilke (2008). In the present work, where we wish to determine the dynamics of segregation and clonal interference between alleles, we perform our simulations in the overlapping generations model where the fitness ([eq 1](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false#mst189-M1)) is of the Malthusian type. Both fitness definitions satisfy the transformation <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215421491-7111a17f-6409-4051-88d9-a10bdb1014a3.gif) (Orr 2009).

### Updating the Folding Stability During Nonsynonymous Substitutions
When a nonsynonymous substitution occurs, we update the folding stability according to <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215421498-d6535492-0a97-4454-a2f0-65e733de5ab6.gif)⁠, where Δ_G_0 is the stability of the protein at time _t_ = 0, ΔΔ_G__i_ is the estimated change in folding stability due to a single point mutation, and _n_ is the total number of amino acid differences of the current sequence with respect to the sequence at time = 0. ΔΔ_G_ is estimated using a physical force field (Yin et al. 2007). Our protocol assumes that the effect on folding stability of multiple mutations is simply the additive effect of all mutations acting independently (Fersht et al. 1992).

This assumption cannot accurately predict the Δ_G_ of a sequence that is significantly diverged from the sequence at time = 0. Indeed, we do not claim that when a specific sequence from simulation is experimentally expressed and purified, the measured Δ_G_ is similar to the one predicted in simulation. Ideally, one could calculate the ΔΔ_G_ using the 3D structure as input as soon as these mutations arise in the population during an evolutionary run. However, this implementation is currently computationally intractable because estimation of the ΔΔ_G_ of one mutation takes ∼5 min per mutation, and the evolutionary simulation evaluates 108 mutations. The assumption of linearity, however, does not compromise biophysical correctness because the model captures the essential features of protein evolution.

First, these force fields coupled with selection for folding stability can recapitulate the extent of per site amino acid conservation among naturally occurring homologous sequences (Ding and Dokholyan, 2006). Indeed, this is one important test during the development of these biophysical tools.

Second, for any “wildtype” sequence in our simulation, the distribution of ΔΔG for all arising single amino acid mutations is consistent with the ΔΔG distribution for random mutations in naturally occuring sequences (Tokuriki et al. 2007). This feature is important because it quantitatively determines the balance between the supply of destabilizing and stabilizing mutations and the strength of the mutational drift.

### Analysis of Simulation Trajectories
After simulation, we trace the history of each arising mutation by counting the number of individuals that exhibit the mutation in the future generations. The tracing of mutational history ends when the mutation fixes in the population or is lost to random drift (fig. 2 and [supplementary fig. S3](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). From these trajectories, we calculate the correlated fixation events (fig. 2_B_). To estimate the probability of fixation (fig. 3), we group the trajectories according to their allele frequencies and selection coefficients. The estimated probability is the number of trajectories that reached a given allele frequency <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/gif/22983715/1709215421493-4180bb6e-42c3-45d6-ae35-a1e04cc08bab.gif) divided by all arising trajectories of that given selection coefficient.

We use Matlab to fit a gamma distribution to the DFE. Also, we follow the standard procedure in evolutionary biology to model the demography of an asexual organism in estimating the DFE among sexual organisms such as human and flies (Bustamante et al. 2005; Eyre-Walker et al. 2006; Kryukov et al. 2009).

### Bioinformatics Analysis
For bioinformatics analysis of the SNPs in the human genome, we use the database dBSNP (Sherry et al. 2001) for allele frequency information and SNPEffect (De Baets et al. 2012) for biophysical estimation of the ΔΔ_G_. SNPEffect used the 3D structure of the protein as input to FoldX (Schymkowitz et al. 2005). We group the SNPs according to their allele frequencies and plotted the distribution of their ΔΔ_G_ (fig. 6_B_). For arising ΔΔ_G_ (fig 6_B_, blue line), we use the empirically measured ΔΔ_G_ from a diverse set of proteins in the ProTherm database (Kumar et al. 2006; Tokuriki et al. 2007).

### Simulations in Monoclonal Populations as Control
To serve as a control and show that the results in this study are robust to the modeling of the cell or to the formal equation of the fitness function, we perform simulations of an evolving monoclonal population. The methods are described in greater detail in a recent work (Serohijos et al. 2012). Briefly, in the monoclonal simulations, the cell is composed of 103 genes, each with protein abundances ranging from 10 to 106 copies per cell to recapitulate the broad distribution of abundances in real organisms (Ghaemmaghami et al. 2003; Ishihama et al. 2008). The effective population size in the monoclonal simulation is _N__e_ = 104. Effects of folding stability are estimated from the Gaussian distribution of ΔΔ_G_ whose parameters are derived from the ProTherm database (Kumar et al. 2006). The evolutionary dynamics likewise include mutation, selection, and drift (see Serohijos et al. [2012] for details). This specific approach, which recapitulates the universal observation of highly expressed proteins evolving slowly (Drummond and Wilke 2008; Serohijos et al. 2012) or that highly expressed proteins tend to be more stable (Cherry 2010; Serohijos et al. 2013), also exhibits the near neutrality of the fixed beneficial mutations ([supplementary figs. S7](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) and [Supplementary Data](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/31/1/10.1093_molbev_mst189/2/mst189_Supplementary_Data.zip?Expires=1711529047&Signature=tODPxpjfGSwa~RBca1idwFx9nlL3iCM74ynjmtQ5oBx5IMnm~W-juqUkV-Jco0wDEoCrq2nfh3okiKxivFKelqmaQv~qtQU6n~ddDPJj1vbqPrRAdVPv~P1kTBukEfXoQjYgpGvpU5HaGH8bEAyxdWRSsV0uLSV-L--37Usd~wcRpOmXmc1K7XvXtrE47fZfs~vO0fVMtTKmUWFtld4uaXcA2h~8frhCr-FbXGtsyhFDSklPv22ASi9VF8~MHurzW~R5yiG66aCKnslqMAKKuMFf0f-uPOvlhTuA5ZvG3QY2jPitAzzKHFsoL-Mywbf6ud9pJt0oP4Wn12DuTdgA5g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online) and the equal partitioning of fixed mutations into ΔΔ_G_ > 0 and ΔΔ_G_ < 0.

## Acknowledgments
The authors are very grateful to Dan Hartl, Michael Lynch, and Shamil Sunyaev for discussions and comments on the manuscript. This work was funded by NIH (RO1 068670).

## References
,  ,  . 

Weak selection and protein evolution

, 

Genetics

, 

2012

, vol. 

192

(pg. 

15

-

31

)

,  ,  , et al. , 

(13 co-authors)

. 

A survey of proteins encoded by non-synonymous single nucleotide polymorphisms reveals a significant fraction with altered stability and activity

, 

Biochem J.

, 

2009

, vol. 

424

(pg. 

15

-

26

)

,  ,  ,  . 

Design and analysis of synthetic carbon fixation pathways

, 

Proc Natl Acad Sci U S A.

, 

2010

, vol. 

107

(pg. 

8889

-

8894

)

,  ,  . 

Thermodynamics of neutral protein evolution

, 

Genetics

, 

2007

, vol. 

175

(pg. 

255

-

266

)

,  ,  ,  ,  ,  ,  ,  ,  ,  . 

Inherent toxicity of aggregates implies a common mechanism for protein misfolding diseases

, 

Nature

, 

2002

, vol. 

416

(pg. 

507

-

511

)

,  ,  , et al. , 

(14 co-authors)

. 

Natural selection on protein-coding genes in the human genome

, 

Nature

, 

2005

, vol. 

437

(pg. 

1153

-

1157

)

,  ,  ,  ,  ,  . 

The cost of inbreeding in Arabidopsis

, 

Nature

, 

2002

, vol. 

416

(pg. 

531

-

534

)

. 

Highly expressed and slowly evolving proteins share compositional properties with thermophilic proteins

, 

Mol Biol Evol.

, 

2010

, vol. 

27

(pg. 

735

-

741

)

,  ,  ,  ,  ,  ,  ,  . 

SNPeffect 4.0: on-line prediction of molecular and structural effects of protein-coding variants

, 

Nucleic Acids Res.

, 

2012

, vol. 

40

(pg. 

D935

-

D939

)

,  ,  . 

Missense meanderings in sequence space: a biophysical view of protein evolution

, 

Nat Rev Genet.

, 

2005

, vol. 

6

(pg. 

678

-

687

)

,  . 

Beneficial mutation selection balance and the effect of linkage on positive selection

, 

Genetics

, 

2007

, vol. 

176

(pg. 

1759

-

1798

)

,  . 

Emergence of protein fold families through rational design

, 

PLoS Comput Biol.

, 

2006

, vol. 

2

pg. 

e85

 

,  . 

Mistranslation-induced protein misfolding as a dominant constraint on coding-sequence evolution

, 

Cell

, 

2008

, vol. 

134

(pg. 

341

-

352

)

,  ,  ,  ,  ,  ,  ,  . 

Global reconstruction of the human metabolic network based on genomic and bibliomic data

, 

Proc Natl Acad Sci U S A.

, 

2007

, vol. 

104

(pg. 

1777

-

1782

)

,  ,  . 

Metabolic flux and fitness

, 

Genetics

, 

1987

, vol. 

115

(pg. 

25

-

31

)

,  ,  . 

In silico predictions of _Escherichia coli_ metabolic capabilities are consistent with experimental data

, 

Nat Biotechnol.

, 

2001

, vol. 

19

(pg. 

125

-

130

)

,  . 

The distribution of fitness effects of new mutations

, 

Nat Rev Genet.

, 

2007

, vol. 

8

(pg. 

610

-

618

)

,  ,  . 

The distribution of fitness effects of new deleterious amino acid mutations in humans

, 

Genetics

, 

2006

, vol. 

173

(pg. 

891

-

900

)

,  ,  . 

The folding of an enzyme. I. Theory of protein engineering analysis of stability and pathway of protein folding

, 

J Mol Biol.

, 

1992

, vol. 

224

(pg. 

771

-

782

)

. , 

The genetical theory of natural selection

, 

1930

Oxford

The Clarendon Press

,  ,  . 

Clonal interference, multiple mutations and adaptation in large asexual populations

, 

Genetics

, 

2008

, vol. 

180

(pg. 

2163

-

2173

)

,  ,  ,  ,  ,  . 

Misfolded proteins impose a dosage-dependent fitness cost and trigger a cytosolic unfolded protein response in yeast

, 

Proc Natl Acad Sci U S A.

, 

2011

, vol. 

108

(pg. 

680

-

685

)

,  . 

The fate of competing beneficial mutations in an asexual population

, 

Genetica

, 

1998

, vol. 

102–103

(pg. 

127

-

144

)

,  ,  ,  ,  ,  ,  ,  . 

Global analysis of protein expression in yeast

, 

Nature

, 

2003

, vol. 

425

(pg. 

737

-

741

)

. 

The evolution and evolutionary consequences of marginal thermostability in proteins

, 

Proteins

, 

2011

, vol. 

79

(pg. 

1396

-

1407

)

,  ,  . 

Topology of protein interaction network shapes protein abundances and strengths of their functional and nonspecific interactions

, 

Proc Natl Acad Sci U S A.

, 

2011

, vol. 

108

(pg. 

4258

-

4263

)

,  ,  ,  ,  ,  ,  . 

Protein abundance profiling of the _Escherichia coli_ cytosol

, 

BMC Genomics

, 

2008

, vol. 

9

pg. 

102

 

,  ,  ,  ,  ,  ,  ,  ,  . 

A whole-cell computational model predicts phenotype from genotype

, 

Cell

, 

2012

, vol. 

150

(pg. 

389

-

401

)

. 

Evolutionary rate at the molecular level

, 

Nature

, 

1968

, vol. 

217

(pg. 

624

-

626

)

,  . 

Constraints and plasticity in genome and molecular-phenome evolution

, 

Nat Rev Genet.

, 

2010

, vol. 

11

(pg. 

487

-

498

)

,  ,  ,  . 

Power of deep, all-exon resequencing for discovery of human trait genes

, 

Proc Natl Acad Sci U S A.

, 

2009

, vol. 

106

(pg. 

3871

-

3876

)

,  ,  ,  ,  ,  ,  . 

ProTherm and ProNIT: thermodynamic databases for proteins and protein–nucleic acid interactions

, 

Nucleic Acids Res.

, 

2006

, vol. 

34

(pg. 

D204

-

D206

)

,  ,  ,  ,  . 

Statistics and truth in phylogenomics

, 

Mol Biol Evol.

, 

2012

, vol. 

29

(pg. 

457

-

472

)

,  . 

The origins of genome complexity

, 

Science

, 

2003

, vol. 

302

(pg. 

1401

-

1404

)

,  ,  ,  ,  ,  ,  . 

Genome-wide association studies for complex traits: consensus, uncertainty and challenges

, 

Nat Rev Genet.

, 

2008

, vol. 

9

(pg. 

356

-

369

)

,  . 

Adaptive protein evolution at the Adh locus in _Drosophila_

, 

Nature

, 

1991

, vol. 

351

(pg. 

652

-

654

)

,  . 

The effects of Hill-Robertson interference between weakly selected mutations on patterns of molecular evolution and variation

, 

Genetics

, 

2000

, vol. 

155

(pg. 

929

-

944

)

,  . 

Achieving diversity in the face of constraints: lessons from metabolism

, 

Science

, 

2012

, vol. 

336

(pg. 

1663

-

1667

)

,  ,  ,  . 

Energy-dependent fitness: a quantitative model for the evolution of yeast transcription factor binding sites

, 

Proc Natl Acad Sci U S A.

, 

2008

, vol. 

105

(pg. 

12376

-

12381

)

,  . 

From fitness landscapes to seascapes: non-equilibrium dynamics of selection and adaptation

, 

Trends Genet.

, 

2009

, vol. 

25

(pg. 

111

-

119

)

,  . 

Genetic draft and quasi-neutrality in large facultatively sexual populations

, 

Genetics

, 

2011

, vol. 

188

(pg. 

975

-

996

)

,  ,  . 

The neutral theory of molecular evolution in the genomic era

, 

Annu Rev Genomics Hum Genet.

, 

2010

, vol. 

11

(pg. 

265

-

289

)

. 

Slightly deleterious mutant substitutions in evolution

, 

Nature

, 

1973

, vol. 

246

(pg. 

96

-

98

)

. 

Fitness and its role in evolutionary genetics

, 

Nat Rev Genet.

, 

2009

, vol. 

10

(pg. 

531

-

539

)

,  ,  . 

Highly expressed genes in yeast evolve slowly

, 

Genetics

, 

2001

, vol. 

158

(pg. 

927

-

931

)

,  ,  . 

An integrated view of protein evolution

, 

Nat Rev Genet.

, 

2006

, vol. 

7

(pg. 

337

-

348

)

. 

Stability of proteins: small globular proteins

, 

Adv Protein Chem.

, 

1979

, vol. 

33

(pg. 

167

-

241

)

,  ,  . 

The distribution of fitness effects caused by single-nucleotide substitutions in an RNA virus

, 

Proc Natl Acad Sci U S A.

, 

2004

, vol. 

101

(pg. 

8396

-

8401

)

,  ,  ,  . 

Prevalence of positive selection among nearly neutral amino acid replacements in _Drosophila_

, 

Proc Natl Acad Sci U S A.

, 

2007

, vol. 

104

(pg. 

6504

-

6510

)

,  ,  ,  ,  ,  . 

The FoldX web server: an online force field

, 

Nucleic Acids Res.

, 

2005

, vol. 

33

(pg. 

W382

-

W388

)

,  . 

The application of statistical physics to evolutionary biology

, 

Proc Natl Acad Sci U S A.

, 

2005

, vol. 

102

(pg. 

9541

-

9546

)

,  ,  . 

Highly abundant proteins favor more stable 3D structures in yeast

, 

Biophys J.

, 

2013

, vol. 

104

(pg. 

L1

-

L3

)

,  ,  . 

Protein biophysics explains why highly abundant proteins evolve slowly

, 

Cell Rep.

, 

2012

, vol. 

2

(pg. 

249

-

256

)

,  ,  ,  ,  ,  ,  . 

dbSNP: the NCBI database of genetic variation

, 

Nucleic Acids Res.

, 

2001

, vol. 

29

(pg. 

308

-

311

)

,  ,  . 

Understanding the evolutionary fate of finite populations: the dynamics of mutational effects

, 

PLoS Biol.

, 

2007

, vol. 

5

pg. 

e94

 

,  . 

Adaptive protein evolution in _Drosophila_

, 

Nature

, 

2002

, vol. 

415

(pg. 

1022

-

1024

)

,  . 

Mutational effects and the evolution of new protein functions

, 

Nat Rev Genet.

, 

2010

, vol. 

11

(pg. 

572

-

582

)

,  . 

Clonal interference in the evolution of influenza

, 

Genetics

, 

2012

, vol. 

192

(pg. 

671

-

682

)

,  . 

Why are proteins marginally stable?

, 

Proteins

, 

2002

, vol. 

46

(pg. 

105

-

109

)

,  ,  ,  ,  . 

The stability effects of protein mutations appear to be universally distributed

, 

J Mol Biol.

, 

2007

, vol. 

369

(pg. 

1318

-

1332

)

,  ,  . 

Neutral evolution of mutational robustness

, 

Proc Natl Acad Sci U S A.

, 

1999

, vol. 

96

(pg. 

9716

-

9720

)

,  ,  ,  . 

Intrinsic protein disorder and interaction promiscuity are widely associated with dosage sensitivity

, 

Cell

, 

2009

, vol. 

138

(pg. 

198

-

208

)

,  ,  ,  ,  . 

Quasispecies diversity determines pathogenesis through cooperative interactions in a viral population

, 

Nature

, 

2006

, vol. 

439

(pg. 

344

-

348

)

. 

The speed of adaptation in large asexual populations

, 

Genetics

, 

2004

, vol. 

167

(pg. 

2045

-

2053

)

,  ,  ,  ,  . 

Evolution of digital organisms at high mutation rates leads to survival of the flattest

, 

Nature

, 

2001

, vol. 

412

(pg. 

331

-

333

)

,  . 

A biophysical protein folding model accounts for most mutational fitness effects in viruses

, 

Proc Natl Acad Sci U S A.

, 

2011

, vol. 

108

(pg. 

9916

-

9921

)

,  ,  . 

Impact of translational error-induced and error-free misfolding on the rate of protein evolution

, 

Mol Syst Biol.

, 

2010

, vol. 

6

pg. 

421

 

,  ,  . 

Eris: an automated estimator of protein stability

, 

Nat Methods.

, 

2007

, vol. 

4

(pg. 

466

-

467

)

,  . 

Identification and analysis of deleterious human SNPs

, 

J Mol Biol.

, 

2006

, vol. 

356

(pg. 

1263

-

1274

)

,  ,  . 

Protein stability imposes limits on organism complexity and speed of molecular evolution

, 

Proc Natl Acad Sci U S A.

, 

2007

, vol. 

104

(pg. 

16152

-

16157

)

,  ,  . 

Constraints imposed by non-functional protein-protein interactions on gene expression and proteome size

, 

Mol Syst Biol.

, 

2008

, vol. 

4

pg. 

210

 

## Author notes
**Associate editor:** Jeffrey Thorne

© The Author 2013. Published by Oxford University Press on behalf of the Society for Molecular Biology and Evolution.

This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/3.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contact journals.permissions@oup.com

## Supplementary data
### Citations
### Views
### Altmetric
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1709215422126-3cf27054-c9c2-4c18-a8e5-4c7be1502723.png)

Metrics

Total Views950

675Pageviews

275PDF Downloads

Since 11/1/2016

| Month: | Total Views: |
| --- | --- |
| November 2016 | 1 |
| December 2016 | 1 |
| January 2017 | 2 |
| February 2017 | 2 |
| March 2017 | 19 |
| May 2017 | 8 |
| June 2017 | 13 |
| July 2017 | 5 |
| August 2017 | 8 |
| September 2017 | 9 |
| October 2017 | 9 |
| November 2017 | 12 |
| December 2017 | 15 |
| January 2018 | 24 |
| February 2018 | 27 |
| March 2018 | 29 |
| April 2018 | 25 |
| May 2018 | 7 |
| June 2018 | 18 |
| July 2018 | 14 |
| August 2018 | 10 |
| September 2018 | 4 |
| October 2018 | 7 |
| November 2018 | 8 |
| December 2018 | 8 |
| January 2019 | 6 |
| February 2019 | 12 |
| March 2019 | 23 |
| April 2019 | 19 |
| May 2019 | 19 |
| June 2019 | 16 |
| July 2019 | 9 |
| August 2019 | 7 |
| September 2019 | 12 |
| October 2019 | 9 |
| November 2019 | 8 |
| December 2019 | 10 |
| January 2020 | 9 |
| February 2020 | 12 |
| March 2020 | 6 |
| April 2020 | 7 |
| May 2020 | 5 |
| June 2020 | 9 |
| July 2020 | 10 |
| August 2020 | 6 |
| September 2020 | 8 |
| October 2020 | 7 |
| November 2020 | 4 |
| December 2020 | 12 |
| January 2021 | 8 |
| February 2021 | 30 |
| March 2021 | 8 |
| April 2021 | 11 |
| May 2021 | 2 |
| June 2021 | 5 |
| July 2021 | 7 |
| August 2021 | 7 |
| September 2021 | 7 |
| October 2021 | 13 |
| November 2021 | 8 |
| December 2021 | 6 |
| January 2022 | 6 |
| February 2022 | 8 |
| March 2022 | 15 |
| April 2022 | 9 |
| May 2022 | 12 |
| June 2022 | 4 |
| July 2022 | 23 |
| August 2022 | 15 |
| September 2022 | 18 |
| October 2022 | 10 |
| November 2022 | 15 |
| December 2022 | 28 |
| January 2023 | 27 |
| February 2023 | 15 |
| March 2023 | 15 |
| April 2023 | 19 |
| May 2023 | 3 |
| June 2023 | 8 |
| July 2023 | 1 |
| August 2023 | 11 |
| September 2023 | 4 |
| October 2023 | 9 |
| November 2023 | 5 |
| December 2023 | 10 |
| January 2024 | 9 |
| February 2024 | 9 |


Citations

[35](https://www.webofscience.com/api/gateway?GWVersion=2&SrcApp=PARTNER_APP&SrcAuth=Silverchair&KeyUT=WOS:000329253200017&DestLinkType=CitingArticles&DestApp=WOS_CPL&UsrCustomerID=61f30d8ae69c46f86624c5f98a3bc13a)Web of Science

×

### Email alerts
### Email alerts
### Recommended
1. [A Comprehensive, High-Resolution Map of a Gene’s Fitness Landscape](https://academic.oup.com/mbe/article/31/6/1581/2925654?login=false&itm_medium=sidebar&itm_source=trendmd-widget&itm_campaign=Molecular_Biology_and_Evolution&itm_content=Molecular_Biology_and_Evolution_0)

Elad Firnberg et al., Molecular Biology and Evolution, 2014

2. [Deleterious Passengers in Adapting Populations](https://academic.oup.com/genetics/article/198/3/1183/6082482?itm_medium=sidebar&itm_source=trendmd-widget&itm_campaign=GENETICS&itm_content=GENETICS_0)

Benjamin H Good et al., GENETICS, 2014

3. [Evolution on the Biophysical Fitness Landscape of an RNA Virus](https://academic.oup.com/mbe/article/35/10/2390/5046249?itm_medium=sidebar&itm_source=trendmd-widget&itm_campaign=Molecular_Biology_and_Evolution&itm_content=Molecular_Biology_and_Evolution_0)

Assaf Rotem et al., Molecular Biology and Evolution, 2018

1. [Global simulations of energetic electron excitation of beta-induced Alfven eigenmodes](https://wulixb.iphy.ac.cn/en/article/doi/10.7498/aps.72.20230794?utm_source=TrendMD&utm_medium=cpc&utm_campaign=Acta_Physica_Sinica_TrendMD_1)

Bao Jian et al., Acta Physica Sinica, 2023

2. [Non-volatile multi-state magnetic domain transformation in a Hall balance](https://iopscience.iop.org/article/10.1088/1674-1056/ac65f5?utm_source=trendmd&utm_campaign=china&utm_medium=cpc)

Yang Gao et al., Chinese Physics B, 2022

3. [The 20-nm Skyrmion Generated at Room Temperature by Spin-Orbit Torques](https://iopscience.iop.org/article/10.1088/0256-307X/39/1/017501?utm_source=trendmd&utm_campaign=china&utm_medium=cpc)

Jiahao Liu et al., Chinese Physics Letters, 2022

### Citing articles via
### Latest 
### Most Read 
### Most Cited 
More from Oxford Academic  


> 来自: [Contribution of Selection for Protein Folding Stability in Shaping the Patterns of Polymorphisms in Coding Regions | Molecular Biology and Evolution | Oxford Academic](https://academic.oup.com/mbe/article/31/1/165/1049192?login=false)
>

