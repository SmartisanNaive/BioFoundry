## Introduction
Evolutionary novelties frequently depend on the fixation of multiple, highly specific mutations, where intermediate stages of evolution seemingly provide little or no benefit[1](https://www.nature.com/articles/ncomms11607#ref-CR1). Such complex adaptations are widespread in molecular networks and include the origin of multimeric protein machineries, establishment of interactions between transcription factors and their binding sites, receptor–ligand interactions and multi-step metabolic pathways[2](https://www.nature.com/articles/ncomms11607#ref-CR2),[3](https://www.nature.com/articles/ncomms11607#ref-CR3),[4](https://www.nature.com/articles/ncomms11607#ref-CR4). According to the notion that evolutionary adaptation proceeds by the sequential fixation of single beneficial mutations[5](https://www.nature.com/articles/ncomms11607#ref-CR5), complex adaptations are expected to occur only sporadically. One theory suggests that many evolutionary innovations, that is, qualitatively new adaptive traits, have non-adaptive origins, where neutral mutations prepare the ground for later beneficial mutations that lead to innovations[6](https://www.nature.com/articles/ncomms11607#ref-CR6),[7](https://www.nature.com/articles/ncomms11607#ref-CR7). Evidence for this process comes from laboratory evolution of RNA enzymes[8](https://www.nature.com/articles/ncomms11607#ref-CR8), but its role in the establishment of complex molecular pathways remains unclear. In the case of metabolic networks, the theory proposes that ‘many additions of individual reactions to a metabolic network will not change a metabolic phenotype until a second added reaction connects the first reaction to an already existing metabolic pathway’[7](https://www.nature.com/articles/ncomms11607#ref-CR7). However, this non-adaptive process is expected to be extremely slow, and furthermore, there is no direct empirical support for this scenario in bacteria, which are especially prolific in producing metabolic innovations. Although free-living bacteria increase their genome size through horizontal gene transfer and gene duplication, their genomes remain compact, and non-functional sequences appear to be rare compared with most eukaryotes[9](https://www.nature.com/articles/ncomms11607#ref-CR9). Genes under relaxed selection are rapidly inactivated and subsequently lost in free-living bacteria, not least because there is a pervasive mutational bias towards deletions of genomic segments[9](https://www.nature.com/articles/ncomms11607#ref-CR9). Consequently, genes encoding functionally completely intact enzymes that provide no immediate fitness advantage are generally unlikely to be maintained for long periods. Even under a scenario where the neutral intermediate-step mutation is not required to reach high population frequencies (that is, ‘stochastic tunnelling’[10](https://www.nature.com/articles/ncomms11607#ref-CR10)), evolution is expected to be slower than traversing purely adaptive trajectories through natural selection. Thus, understanding the evolution of complex innovations remains a formidable challenge.

Previous population genetic models[11](https://www.nature.com/articles/ncomms11607#ref-CR11) and computer simulations of genetic circuits and RNA molecules[12](https://www.nature.com/articles/ncomms11607#ref-CR12) offer a potential solution to the problem of complex adaptations. These works indicate that complex or temporally fluctuating conditions can facilitate adaptation, partly by allowing populations to escape fitness plateaus and reach new adaptive peaks. Similarly, a study on digital organisms revealed that populations often evolve complex features by building on simpler functions that had evolved earlier[13](https://www.nature.com/articles/ncomms11607#ref-CR13). However, the extent to which these abstract considerations apply to specific cellular subsystems remained unknown, partly due to the shortage of systems-level analysis that would combine computational modelling and evolutionary experiments.

In this work, we focus on bacterial metabolic networks to examine how novel nutrient utilization phenotypes can be acquired via the addition of new reactions to an organism’s enzyme repertoire. While not all complexity at the level of molecular systems are expected to provide a functional advantage[14](https://www.nature.com/articles/ncomms11607#ref-CR14),[15](https://www.nature.com/articles/ncomms11607#ref-CR15), metabolic pathways utilizing novel nutrients arguably qualify as adaptive traits. The problem of the evolution of novel metabolic pathways has two complementary aspects, relating to their origin and subsequent evolutionary establishment across multiple species. Previous works were largely concerned by how novel biochemical reactions arise first during the course of evolution[16](https://www.nature.com/articles/ncomms11607#ref-CR16),[17](https://www.nature.com/articles/ncomms11607#ref-CR17). In this paper, we ask how existing enzymatic reactions can assemble to form a novel metabolic pathway in an organism that already harbours a complex metabolic network. We extend and generalize an early suggestion that varying nutrient environments play a prominent role in the establishment of biosynthetic pathways[16](https://www.nature.com/articles/ncomms11607#ref-CR16).

Specifically, we employ detailed simulations on a pan-genome scale to demonstrate that complex metabolic innovations can evolve via the successive acquisition of single biochemical reactions that each confers a benefit to utilize specific nutrients. Thus, temporal changes in nutrient availability or complex environments (where multiple nutrients are available) can facilitate adaptive evolution of metabolic pathways through the step-by-step expansion of metabolic niches. Gene acquisition patterns across bacterial genomes and _de novo_ laboratory evolution of nutrient utilizations in _Escherichia coli (E. coli)_ provide clear support for the hypothesis.

## Results
### Most metabolic innovations demand only a few novel reactions
In this work, we systematically studied the expansion of metabolic networks. We specifically asked whether metabolic innovations can evolve in a purely Darwinian manner through series of adaptive steps. Our starting point was the previously reconstructed metabolic network of _E. coli_ K-12, arguably the best studied and most reliable reconstruction of a genome-scale metabolic system, composed of 2,077 unique reactions, including transport processes[18](https://www.nature.com/articles/ncomms11607#ref-CR18). Previous studies showed that bacterial networks expand largely by acquiring genes involved in the transport and catalysis of external nutrients, driven by adaptations to changing environments[19](https://www.nature.com/articles/ncomms11607#ref-CR19). On the basis of these observations, here we studied the potential selective advantages conferred by the addition of new metabolic reactions to the _E. coli_ network. We compiled a data set of 2,566 known enzymatic and 159 transport reactions across the three kingdoms of life (‘universal reaction set’) absent from the _E. coli_ model[20](https://www.nature.com/articles/ncomms11607#ref-CR20) (see Methods). We next defined a comprehensive sample of the external nutrient space, consisting of 1,776 environments comprised of nutrient sources that can potentially be imported into the network ([Supplementary Data 1](https://www.nature.com/articles/ncomms11607#MOESM1070)). We focused on minimal media that differ from each other in a single carbon, nitrogen, sulphur or phosphorus source, thereby maximizing the variability between conditions while remaining computationally feasible (Methods). We determined the phenotypic impact of adding one or more reactions from the universal reaction set to the _E. coli_ network in each of these environments using flux balance analysis (FBA)[21](https://www.nature.com/articles/ncomms11607#ref-CR21). FBA identifies a steady-state flux distribution that maximizes the production of biomass (a weighted combination of major biosynthetic components) from a given set of available nutrients. This framework successfully predicts the growth capacity of wild-type _E. coli_ across nutrient conditions[18](https://www.nature.com/articles/ncomms11607#ref-CR18), and it is biologically more realistic than graph-theoretical approaches[22](https://www.nature.com/articles/ncomms11607#ref-CR22).

Before the addition of novel reactions, the reconstructed _E. coli_ metabolic network was unable to grow (that is, the rate of biomass production was zero) in 321 environments in which the network expanded by the complete universal reaction set was able to grow ([Supplementary Data 1](https://www.nature.com/articles/ncomms11607#MOESM1070)). Using a mixed integer linear programming (MILP) algorithm, we determined the minimal number of reactions from the universal reaction set that need to be added to the _E. coli_ network to support growth in these novel environments. Strikingly, growth in additional environments required the addition of only one to three enzymatic and transport reactions in 74% of the cases (239 out of 321 environments; see [Fig. 1](https://www.nature.com/articles/ncomms11607#Fig1)). In 21.5% of the novel environments, acquisition of only one reaction was sufficient for growth (69 out of 321 environments, see [Supplementary Data 2](https://www.nature.com/articles/ncomms11607#MOESM1070)). These results suggest that in the genotype space around the _E. coli_ metabolic network, most metabolic innovations are only a few gene acquisition steps away.

**Figure 1: Metabolic innovations in the genotype space around the **_**E. coli**_** network.**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710077450429-cb750257-7db6-4fe1-a7d0-8d34452ddd4f.jpeg)

Only few reactions need to be added to the _E. coli_ metabolic network to enable growth in metabolic environments where the wild-type cannot grow. The histogram shows the distribution of additional minimal reaction set sizes needed for biomass production in 321 novel nutrient environments.

[Full size image](https://www.nature.com/articles/ncomms11607/figures/1)

### Complex innovations can arise via changing environments
One can envisage a simple adaptationist hypothesis by which complex metabolic innovations can arise. A metabolic phenotype accessible through the addition of a single reaction may serve as an exaptation[23](https://www.nature.com/articles/ncomms11607#ref-CR23) from which metabolic phenotypes that demand the acquisition of multiple reactions can be developed. A major corollary of this hypothesis is that evolutionary adaptation to temporally varying environmental conditions facilitates the expansion of metabolic networks (see also ref. [16](https://www.nature.com/articles/ncomms11607#ref-CR16)). In the parlance of fitness landscapes, varying environments result in dynamic landscapes with moving peaks which can be more easily tracked by hill-climbing evolution (see [Fig. 2a,b](https://www.nature.com/articles/ncomms11607#Fig2)).

**Figure 2: Evolution in varying environments is expected to facilitate the establishment of complex metabolic traits.**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710077450870-5dfaf29f-8924-476e-a505-1b071ee1dcbf.jpeg)

(**a**, top) Hypothetical fitness landscape over a two-dimensional genotype space. The red genotype is well-adapted, that is, it is located on the fitness peak of this starting fitness landscape. A change to the target environment shifts the fitness peak, so that the red genotype is no longer of high fitness (bottom). Adaptation to the shifted peak now cannot proceed purely through adaptive steps (that is, hill climbing); it requires the non-adaptive exploration of the neutral part of the landscape, illustrated by the yellow dotted line. (**b**) Depicting the same situation, but with an intermediate environment in which the fitness peak is only slightly shifted relative to the starting environment. The red genotype is located at the foot of the shifted fitness peak in this intermediate environment and can thus progress through purely adaptive steps, culminating in the yellow high-fitness genotype. When the environment now changes to the same target environment as in **a**, the blue genotype represents an exaptation, such that it can now progress towards the target fitness peak through purely adaptive steps. While **b** only shows one intermediate environment, the same reasoning applies to more complex scenarios including dynamic landscapes with moving peaks. (**c**) Example from simulated metabolic network expansions. _E. coli_ K-12 is unable to utilize chorismate and L-phenylalanine as sole carbon sources. Simulations show that while chorismate utilization demands the simultaneous addition of two reactions to the network, one of these reactions (first step; catalysed by phenylalanine ammonia lyase) also confers L-phenylalanine utilization when added individually.

[Full size image](https://www.nature.com/articles/ncomms11607/figures/2)

To test the feasibility of the stepwise network expansion scenario, we focused on reaction pairs that are jointly required to provide a fitness benefit in at least one environment (for a list of the 538 such reaction pairs, see [Supplementary Data 3](https://www.nature.com/articles/ncomms11607#MOESM1070)). Next, we added each of the corresponding reactions individually into the network and asked whether their presence alone provides a selective advantage across the set of 321 novel environments. Consistent with the hypothesis, we found that in 40% of the 538 growth-promoting reaction pairs, one of the reactions enables growth on its own in at least one environmental setting, which therefore can serve as stepping stones along adaptive trajectories. For example, while the ability to metabolize chorismate demands the simultaneous acquisition of two reactions, one of them also confers L-phenylalanine utilization when added individually to the network ([Fig. 2c](https://www.nature.com/articles/ncomms11607#Fig2)). We note that many growth-promoting reaction pairs are phenotypically equivalent (that is, confer growth in the same environment) and share the same stepping-stone reaction ([Supplementary Data 3](https://www.nature.com/articles/ncomms11607#MOESM1070)). As a result, in total 8.5% of the 118 novel environments that require the simultaneous addition of two reactions becomes accessible through purely adaptive walks.

To more generally assess the potential for exaptation, we examined for each novel environment if its growth-promoting reactions are involved in adaptation to another (intermediate) environment. To this end, for each environment, we enumerated all possible minimal reaction sets that can support growth when added to the _E. coli_ network from the universal reaction set. On average, 26% of the alternative minimal reaction sets required for growth in a given environment are also entirely present in at least one minimal growth-promoting reaction set of a second environment. This finding indicates that some of the growth-promoting reaction sets contribute to growth in multiple environments as parts of larger reaction sets. These figures are likely underestimates due to incomplete knowledge of available enzymatic reactions (including promiscuous side activities in the _E. coli_ metabolic network[24](https://www.nature.com/articles/ncomms11607#ref-CR24)) and environmental conditions. We conclude that traversing complex evolutionary trajectories can be facilitated by exaptations when the environment varies.

### Metabolic gene acquisition patterns support the hypothesis
The model predicts that acquisition of new metabolic genes during bacterial evolution should be contingent on the presence of other genes providing specific adaptations to intermediate environments. It has been established that a major source of metabolic network expansion is horizontal gene transfer in bacteria[19](https://www.nature.com/articles/ncomms11607#ref-CR19),[25](https://www.nature.com/articles/ncomms11607#ref-CR25). Genes recently acquired by _E. coli_ through horizontal gene transfer confer condition-specific advantages and contribute to growth only in specific environments[19](https://www.nature.com/articles/ncomms11607#ref-CR19). To test whether acquisition of an enzyme pair that is potentially accessible via adaptive steps occurs via a defined order, we used genomic data from 943 bacteria to reconstruct gene-gain events along the corresponding phylogeny using parsimony ([Fig. 3a](https://www.nature.com/articles/ncomms11607#Fig3), Methods). As expected under the hypothesis, enzymes that are predicted to confer fitness benefits on their own and can hence serve as stepping stones towards two-step adaptations _in silico_ tend to be gained on an earlier branch of the phylogenetic tree than their partner enzyme (in 65% of cases, _N_=33, as opposed to 50% expected by chance, _P_=0.037, one-tailed one-sample Wilcoxon signed-rank test, see Methods). We note that this pattern holds for different parameter values of the gene-gain reconstruction procedure (see [Supplementary Table 1](https://www.nature.com/articles/ncomms11607#MOESM1070)).

**Figure 3: Evolutionary history of gene gains supports the dynamic environment model.**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710077450539-9321de42-3868-450f-a19e-6a5a25c6a886.jpeg)

(**a**) Schematic representation of the phylogenetic comparisons to study the interdependence between gene-gain events. According to the dynamic environment model, if initial adaptation via a single gain of gene _A_ serves as a stepping-stone for complex adaptation via a gain of gene _B_, then acquisition of _B_ is expected to occur more frequently with gene _A_ being present (contingent gain) compared with _A_ being absent in the ancestral branch points of the bacterial tree (upper panel). Furthermore, enzyme pairs that confer a growth benefit only when present together are expected to be more frequently co-gained along branches of the bacterial tree in comparison to a gain of only one of the two (lower panel). Detailed description of the procedures is presented in Methods. (**b**) Phylogenetic co-gain measure (see Methods) of jointly beneficial enzymes based on analysis of hundreds of bacterial genomes. Orthologs of enzyme pairs that are beneficial jointly but not accessible gradually (‘beneficial without individual effect’, _N_=21) tend to be co-gained on the same branch of the phylogenetic tree. This trend is statistically significant when compared both with randomized pairs and to enzymes that are growth-promoting as a pair but are accessible gradually through adaptive evolution via varying environments (‘beneficial with combined and individual effect’, _N_=40), _P_<0.001 (randomization analysis) and _P_=0.0038 (one-sided Wilcoxon rank test), respectively. In addition, such ‘accessible’ pairs are not more likely to be co-gained than expected by chance (_P_=0.637).

[Full size image](https://www.nature.com/articles/ncomms11607/figures/3)

In contrast to such cases, growth-promoting enzyme pairs not accessible gradually are the most likely candidates for co-gain via horizontal gene transfer. In agreement with this expectation, such enzyme pairs show a much higher co-gain fraction, that is, number of co-gain relative to single gain events, compared with random gene pairs and growth-promoting gene pairs predicted to be accessible gradually through adaptive evolution via environmental changes (_P_<0.001, randomization analysis and _P_=0.0038, one-sided Wilcoxon rank test, respectively, _N_=21, [Fig. 3b](https://www.nature.com/articles/ncomms11607#Fig3), see Methods). Also consistent with the hypothesis, growth-promoting enzyme pairs that are accessible gradually through adaptive evolution via environmental changes, have very low co-gain fractions that are indistinguishable from that of random gene pairs (_P_=0.64, randomization analysis, _N_=40, [Fig. 3b](https://www.nature.com/articles/ncomms11607#Fig3), see Methods). These conclusions are robust to changes in parameter values of the gene-gain reconstruction procedure (see [Supplementary Tables 2,3](https://www.nature.com/articles/ncomms11607#MOESM1070)).

### Experimental evolution of a complex metabolic innovation
New metabolic pathways can evolve not only through the acquisition of full-blown enzymes from other organisms but also through the enhancement of weak side activities of existing enzymes[3](https://www.nature.com/articles/ncomms11607#ref-CR3),[24](https://www.nature.com/articles/ncomms11607#ref-CR24). Thus, a further prediction of the hypothesis is that evolutionary adaptation to a specific nutrient via accumulating mutations in endogenous genes can influence the accessibility of adaptive paths towards the utilization of other nutrients. An early work[26](https://www.nature.com/articles/ncomms11607#ref-CR26) suggests that acquiring the ability to grow on ethylene glycol (EG, ethane-1, 2-diol) and propylene glycol (PG, (S)-propane-1, 2-diol), two related carbon sources unavailable for utilization by wild-type _E. coli_ K12, might depend on one another in a contingent manner. Specifically, according to the anecdotal report, _E. coli_ mutants able to grow on EG could be obtained from mutants that could grow on propylene glycol[26](https://www.nature.com/articles/ncomms11607#ref-CR26). Using these phenotypes as a test bed we aimed at directly testing the stepwise metabolic niche expansion scenario by examining (i) whether mutations that enable growth on propylene glycol _per se_ increase adaptation rates to EG and (ii) whether the mutations conferring these two distinct growth phenotypes exhibit epistasis on EG, as predicted by the hypothesis.

First, we attempted to isolate mutants that can grow on EG (EG+) or propylene glycol (PG+) from large populations of bacteria ([Supplementary Methods](https://www.nature.com/articles/ncomms11607#MOESM1070)). No EG+ or PG+ cells were isolated from ∼1011 cells with wild-type mutation rate ([Table 1](https://www.nature.com/articles/ncomms11607#Tab1)), demonstrating that these substrates demand the acquisition of one or more very rare specific mutations. Next, we employed an _E. coli_ strain with an approximately 1,000-fold increased mutation rate[27](https://www.nature.com/articles/ncomms11607#ref-CR27). In this case, PG+ cells occurred at a low, but detectable frequency of 1.5 × 10−9, but still no EG+ mutants were found ([Table 1](https://www.nature.com/articles/ncomms11607#Tab1)). As discussed, the evolution of EG utilization might be facilitated by prior adaptation to PG[26](https://www.nature.com/articles/ncomms11607#ref-CR26). This was indeed so: EG-utilizing cells were detected in PG+ populations at a frequency of ∼3.8 × 10−9 ([Table 1](https://www.nature.com/articles/ncomms11607#Tab1)), indicating an increase in adaptation rate of at least two orders of magnitude.

**Table 1 Adaptation frequencies of different strains to PG and EG.**

[Full size table](https://www.nature.com/articles/ncomms11607/tables/1)

It has been reported that constitutive activation of _fucO_, a gene encoding an enzyme involved in fucose and rhamnose catabolism, is a prerequisite for growth in PG[28](https://www.nature.com/articles/ncomms11607#ref-CR28). We therefore hypothesized that _fucO_ upregulation acts as a stepping-stone mutation towards EG utilization. To test this scenario, we overexpressed _fucO_ from a strong constitute promoter in wild-type background[29](https://www.nature.com/articles/ncomms11607#ref-CR29). As expected, _fucO_ overexpression conferred the ability to utilize PG ([Fig. 4a](https://www.nature.com/articles/ncomms11607#Fig4)). Remarkably, employing a _fucO_ overexpressed PG+ strain yielded EG-utilizing cells at a frequency of ∼2 × 10−8 ([Table 1](https://www.nature.com/articles/ncomms11607#Tab1)). As this strain retained a wild-type mutation rate ([Supplementary Fig. 1](https://www.nature.com/articles/ncomms11607#MOESM1070)), this finding shows that the ability to metabolize PG _per se_ promotes adaptation to EG. Whole-genome sequencing of an EG-utilizing strain suggested that ∼10-fold amplification of a genomic segment encoding _aldA_ might underlie EG utilization ([Supplementary Table 4](https://www.nature.com/articles/ncomms11607#MOESM1070)). Indeed, simultaneous overexpression of both _fucO_ and _aldA_ in wild-type background conferred the ability to grow on EG ([Fig. 4b](https://www.nature.com/articles/ncomms11607#Fig4)) with a growth kinetics akin to the strain adapted to EG ([Supplementary Fig. 2](https://www.nature.com/articles/ncomms11607#MOESM1070)). Furthermore, as neither _fucO_ nor _aldA_ alone conferred growth on EG, this finding provides evidence that the two overexpression mutations act epistatically, as predicted by the stepwise metabolic niche expansion hypothesis.

**Figure 4: Utilization of propylene glycol increases adaptation rates towards growth on EG in the laboratory.**

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1710077451000-9e270856-3bb5-4570-811f-741f6b8d9cf2.jpeg)

(**a**) Growth curve measurements demonstrating that overexpression of _fucO_ (red) is sufficient for growth in propylene glycol. Wild-type MG1655 strain is depicted in grey. OD600 measurements of six independent replicates were taken every 60 min. (**b**) Growth curve measurements demonstrating that joint overexpression of both _fucO_ and _aldA_ is required for growth on EG (black). Neither _fucO_ (red) nor _aldA_ (blue) can achieve this when overexpressed individually. Wild-type MG1655 strain is depicted in grey. OD600 measurements of six independent replicates were taken every 240 min. One replicate population with joint overexpression of _fucO_ and _aldA_ failed to grow for unknown reason and is not shown. (**c**) Schematic pathway diagram representing the role of FucO and AldA enzymes in the utilization of PG and EG. In the first step, FucO catalyses the oxidation of PG and EG to glycolaldehyde and L-lactaldehyde, respectively. We note that the native activity of FucO operates in the reverse direction by reducing L-lactaldehyde to PG during the catabolism of L-fucose and L-rhamnose. In the next step, AldA oxidizes the products of FucO to hydroxycarboxylic acids which can be wired into central carbon metabolism following further enzymatic modifications. The affinity of AldA for L-lactaldehyde (PG utilization) is higher than for glycolaldehyde (EG utilization)[30](https://www.nature.com/articles/ncomms11607#ref-CR30), potentially explaining why growth on EG requires multiple copies of _aldA_.

[Full size image](https://www.nature.com/articles/ncomms11607/figures/4)

How do these two enzymes, FucO and AldA, contribute to EG utilization? FucO likely acts on EG in addition to its native substrate to produce glycolaldehyde from EG[26](https://www.nature.com/articles/ncomms11607#ref-CR26); AldA, an enzyme with broad substrate specificity, further converts glycolaldehyde to glycolate[30](https://www.nature.com/articles/ncomms11607#ref-CR30) ([Fig. 4c](https://www.nature.com/articles/ncomms11607#Fig4)). Interestingly, in addition to their role in EG metabolism, both enzymes are involved in PG utilization as well, indicating that regulatory rewiring of the same enzyme toolkit can produce multiple qualitatively different phenotypes.

## Discussion
Explaining the origin of evolutionary innovations that require the simultaneous acquisition of multiple mutations, none of which seemingly confer a benefit individually, remains a central challenge in evolutionary biology. On the basis of prior theoretical considerations[11](https://www.nature.com/articles/ncomms11607#ref-CR11),[12](https://www.nature.com/articles/ncomms11607#ref-CR12),[16](https://www.nature.com/articles/ncomms11607#ref-CR16), here we propose that metabolic innovations accessible through the addition of a single reaction serve as stepping stones towards the later establishment of complex metabolic features in another environment. We provided several lines of evidences in support of the hypothesis by focusing on the most well-studied molecular network, cellular metabolism, and by employing three complementary approaches. First, we simulated the adaptation of the _E. coli_ metabolic network to novel environments. We revealed that new complex pathways can evolve via the successive acquisition of single biochemical reactions that allow the utilization of specific nutrients. Second, by reconstructing the evolutionary history of gene gains in bacteria, we demonstrated that complex metabolic pathways are indeed often established in a defined order as predicted. Finally, we conducted a laboratory evolution study of _E. coli_ adaptation to two novel carbon sources; evolving the ability to utilize one nutrient remarkably facilitated later adaptation to the other. Thus, complex metabolic traits can emerge without the need to invoke neutral exploration of genotype space, a view that is in sharp contrast to non-adaptive scenarios of evolutionary innovation that rely on the accumulation of neutral intermediate mutations[6](https://www.nature.com/articles/ncomms11607#ref-CR6),[7](https://www.nature.com/articles/ncomms11607#ref-CR7),[31](https://www.nature.com/articles/ncomms11607#ref-CR31).

Taken together, our study demonstrates that complex metabolic innovations can evolve by adaptive means through the step-by-step expansion of nutrient utilization capacities. An important prediction is that metabolic innovations should be intertwined in nature: the ability to metabolize certain nutrients should act as a stepping stone towards the utilization of other nutrient sources[32](https://www.nature.com/articles/ncomms11607#ref-CR32). A preliminary systems-level analysis based on nutrient utilization of 168 _E. coli_ strains[33](https://www.nature.com/articles/ncomms11607#ref-CR33) suggests that it may indeed be so ([Supplementary Fig. 3](https://www.nature.com/articles/ncomms11607#MOESM1070)). Experimental case studies on the evolution of the catabolism of β-galactoside sugars[34](https://www.nature.com/articles/ncomms11607#ref-CR34) and citrate utilization[35](https://www.nature.com/articles/ncomms11607#ref-CR35) are also consistent with the scenario, but it remains to be seen how general these findings are. In addition, it is important to note that functionally linked enzymes frequently cluster in the bacterial genome or are encoded in the same operon and tend to be acquired together during evolution[19](https://www.nature.com/articles/ncomms11607#ref-CR19). Future systematic works should study the extent to which simultaneous uptake of multiple physiologically linked reactions by horizontal gene transfer speeds up the evolution of metabolic networks.

We speculate that the major barrier to the dynamic environment model of complex adaptation may be the absence of relevant series of environmental conditions. This restriction could be lifted when multiple novel substrates are simultaneously present in a single environment and evolution proceeds by successively acquiring the capacity to utilize them. We emphasize that other conceptually different mechanisms might also contribute to the adaptive expansion of metabolic networks. For example, stepping-stone reactions might evolve as repair processes in an adaptive response to metabolite damage[36](https://www.nature.com/articles/ncomms11607#ref-CR36), to degrade toxic environmental chemicals[3](https://www.nature.com/articles/ncomms11607#ref-CR3), or to produce novel secondary metabolites[37](https://www.nature.com/articles/ncomms11607#ref-CR37).

Our work has important ramifications for understanding genetic interaction networks and the development of industrially useful microbes. First, epistatic interactions between metabolic genes of the same pathway should often be environment-specific: our results suggest that in many cases, one of the genes should provide fitness benefits independently of the other in at least one environment. Large-scale mapping of genetic interactions across a broad range of environmental conditions would provide a direct way to test this prediction[38](https://www.nature.com/articles/ncomms11607#ref-CR38). Second, we anticipate that evolutionary engineering of microbes to obtain desired phenotypes could be facilitated by temporally varying the traits under selection[39](https://www.nature.com/articles/ncomms11607#ref-CR39).

Finally, our study could have important implications beyond the evolution of metabolism. Earlier studies claimed that varying environments accelerate evolutionary adaptation in genetic circuits and RNA molecules[12](https://www.nature.com/articles/ncomms11607#ref-CR12). In computer science, standard genetic algorithms have a tendency to quickly converge to a local solution, and hence frequently fail to identify more promising regions of the search space[40](https://www.nature.com/articles/ncomms11607#ref-CR40). Application of dynamically changing ‘environments’ offers a natural strategy to maintain the diversity required to explore the adaptive surface[41](https://www.nature.com/articles/ncomms11607#ref-CR41).

## Methods
### Reconstruction of the universal reaction set
To study the potential adaptive value of adding new reactions to the _E. coli_ metabolic network, we compiled a data set of metabolic reactions reported from species across the three kingdoms of life (universal reaction set) and absent from _E. coli_. First, we mapped the metabolites of the manually curated _E. coli_ genome-scale metabolic model[18](https://www.nature.com/articles/ncomms11607#ref-CR18) to the Model SEED database[20](https://www.nature.com/articles/ncomms11607#ref-CR20) (and [http://blog.theseed.org/model_seed/](http://blog.theseed.org/model_seed/)), a comprehensive resource for automatically generated genome-scale metabolic network reconstructions. Because Model SEED does not contain the most recent version (iJO1366 (ref. [42](https://www.nature.com/articles/ncomms11607#ref-CR42))) of the _E. coli_ network reconstruction, we used an earlier version (iAF1260 (ref. [18](https://www.nature.com/articles/ncomms11607#ref-CR18))) that is widely utilized and has been extensively tested[43](https://www.nature.com/articles/ncomms11607#ref-CR43). As a second step, we added all mass-balanced biochemical reactions from the Model SEED database to the _E. coli_ model. From this draft network, we removed duplicate reactions. Next, we removed ‘perpetuum mobile’ cycles, that is, flux distributions capable of producing energy without consuming any nutrients (see [Supplementary Methods](https://www.nature.com/articles/ncomms11607#MOESM1070) and [Supplementary Table 5](https://www.nature.com/articles/ncomms11607#MOESM1070)). Finally, we removed unconditionally blocked reactions (that is, those unable to carry a flux under any condition). The resulting curated universal reaction network contains 4,949 metabolic reactions and 444 nutrient uptake reactions, of which 2,566 and 159 are not present in the _E. coli_ network, respectively. The universal network is available as a computational Systems Biology Markup Language (SBML) model ([Supplementary Data 4](https://www.nature.com/articles/ncomms11607#MOESM1070)).

For more details on the reconstruction of the universal reaction set, see [Supplementary Methods](https://www.nature.com/articles/ncomms11607#MOESM1070).

### Defining novel _in silico_ nutrient environments
We first defined a comprehensive set of nutrient environments by starting from a glucose minimal medium for _E. coli_. For each environment, we replaced the carbon (C), nitrogen (N), phosphate (P) or sulfur (S) source by an alternative one. To obtain a list of environments that is both representative of novel nutrient compounds and computationally tractable, we focused on only those growth media that differed from glucose minimal medium by one compound instead of enumerating all possible combinations of C, N, P and S-sources, as in previous works[24](https://www.nature.com/articles/ncomms11607#ref-CR24),[31](https://www.nature.com/articles/ncomms11607#ref-CR31). Although this approach does not take into account more complex conditions, it allowed us to focus on single C, N, P and S-sources and to maximize the variability between conditions. See [Supplementary Data 1](https://www.nature.com/articles/ncomms11607#MOESM1070) for the list of resulting 1,776 conditions.

Next, we determined the viability of both the _E. coli_ network and the universal network across these conditions using FBA[21](https://www.nature.com/articles/ncomms11607#ref-CR21). A network was deemed inviable in a given environment if its maximum biomass production was zero. Before adding novel reactions, the reconstructed _E. coli_ metabolic network was unable to grow in 321 environments in which the network expanded by the universal reaction set allowed growth ([Supplementary Data 1](https://www.nature.com/articles/ncomms11607#MOESM1070)). We considered these 321 conditions as the set of available novel environments to which _E. coli_ can possibly adapt by adding reactions from other species.

### Finding growth-promoting reaction sets in new environments
To calculate the minimum number of active, non-coli reactions in a particular environment we applied a MILP-based algorithm on the universal metabolic model similar to the problem of finding the shortest elementary flux mode[44](https://www.nature.com/articles/ncomms11607#ref-CR44). The basis of the MILP problem was the steady-state assumption:

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1710077450251-4e8219c7-aae9-4115-ad5c-337dab6f9e94.png)

Where _S_ is the stoichiometric matrix and **v** is the flux vector for all reactions. The reactions of the model were handled differently depending on whether they are part of the _E. coli_ model or they can be added to the coli model during evolution. The flux constraints on the _E. coli_ reactions were the same as in FBA:

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1710077450857-8ad81ba1-54a9-40dc-9ba8-6d208cc0dc7c.png)

Next, for each environment in which the universal network was viable but the wild-type _E. coli_ network was not able to grow we set the nutrient uptake constraints to mimic the environment (**l**_i_ of the exchange reactions). The lower bound of the biomass production reaction was then constrained to 10−4 as the minimal growth requisite:

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1710077451007-fe977d0e-34ed-4de2-8ec9-513509e0a55c.png)

The reversible non-coli reactions of the universal network were decomposed into two opposing irreversible reactions. This way the fluxes of the non-coli reactions can only take positive values. Let _N′_ be the number of non-coli reactions. We assigned a binary variable to each non-coli reaction, **b**i, which tells whether the non-coli reaction r′_i__(i=1, …, N′)_ is active (**b**_i__=1)_ or not (**b**_i__=0)_. The following equations ensure these rules:

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1710077451018-4f4dc1b4-e185-4966-9e82-5606be8be7e4.png)

Where **v**′_i_ is the flux and **u**′_i_ is the maximal possible flux of reaction r′_i_, while _ɛ_ is the minimal flux value (in our calculations _ɛ=_10−8). Also to avoid having two opposing reactions derived from the same reversible reaction being active simultaneously we introduced the following constraint:

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1710077451055-d0abf6ec-268e-4019-b445-a7f8247738e2.png)

Finally, the objective of the MILP problem was to minimize the active non-coli reactions:

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1710077451159-f47ffc1b-4ce9-43b6-b259-62dc23b774bb.png)

The result of this minimization is the minimum number of non-coli reactions need to be added to the coli model to allow growth in a particular environment.

### Enumerating all possible minimal reaction sets _in silico_
The MILP optimization model described above not only provide the minimal number of reactions that support growth in new environments but also the list of the non-coli reactions involved in this solution: one of the minimal reaction sets. However, multiple equivalent minimal sets might exist for any given environment. To identify another minimal reaction set we extended the MILP problem with a new constraint which prevents the algorithm to find the same solution again:

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1710077451276-ecfbc1fc-63ee-4560-a252-5f013784957f.png)

Where _B__i_ is the binary solution of the first minimal reaction set, and _B__i_ equals to 1 or 0 if reaction r′_i_ was active or inactive in the first solution, respectively. This constraint is fulfilled only if the two solutions differ in at least one active reaction. We can harvest more minimal reaction sets in an iterative way where after each solution we add a new constraint and we run the algorithm again. Our algorithm stopped when the new solution had more active reactions than the size of the minimal reaction sets, that is, when we collected all minimal reaction sets. This algorithm is based on the method of finding the k-shortest elementary flux modes[44](https://www.nature.com/articles/ncomms11607#ref-CR44).

### Defining growth-promoting reaction pairs using modelling
To systematically test the dynamic environment model, we investigated all possible two-step adaptation scenarios. First, we inactivated all non-coli reactions in the universal reaction network. Next, we activated two non-coli reactions at a time and applied FBA to calculate the fitness of the model in each environment where the native _E. coli_ model cannot grow. By repeating this procedure we probed all possible reaction pairs in the universal reaction set and identified those that provide growth in at least one environmental condition (3,290,895 reaction pairs in total, 538 are beneficial in at least one condition). As a next step, we determined if the identified two-reaction adaptations can be accessed by the consecutive addition of single beneficial reactions to the network, that is, whether at least one of the two reactions provide a fitness benefit on its own in any of the environments. For this purpose, we repeated the above procedure but instead of activating reaction pairs we activated single reactions and evaluated their fitness effect across environments using FBA. The list of 538 reaction pairs and corresponding environments can be found in [Supplementary Data 3](https://www.nature.com/articles/ncomms11607#MOESM1070).

### Software and computation used in metabolic network analyses
All simulations were implemented in GNU R (ref. [45](https://www.nature.com/articles/ncomms11607#ref-CR45)) using the sybil package for constraint-based modelling[46](https://www.nature.com/articles/ncomms11607#ref-CR46). As optimizer for linear programming and MILP we used ILOG CPLEX 12.5. The linear programming was done on a 64-bit Ubuntu Linux system with an Intel Core-i7 quadcore processor. MILP problems were solved on a Red Hat Enterprise Linux Server release 6.2 with 96 Intel Xeon central processing units.

### Phylogenetic analysis of gene-gain events
To investigate contingent gain and co-gain in the evolutionary history of genes, we first generated the phylogenetic presence and absence profile across the present-day species for each reaction by mapping the profiles from gene to reaction level. Presence and absence profiles of orthologous genes across 943 bacterial species were obtained from EggNOG v3.0 (ref. [47](https://www.nature.com/articles/ncomms11607#ref-CR47)). Reactions catalysed by enzyme complexes consisting of multiple gene products (‘AND’ relationships) are considered to be present in a species only when all genes of the complex are present in the genome. Reactions catalysed by isoenzymes (‘OR’ relationships) are considered to be present when at least one isoenzyme is encoded in the genome.

Next, we inferred the most parsimonious ancestral presence/absence states of each reaction by using a phylogenetic tree of the 943 eubacteria, retrieved from STRING v9.05 ([http://string905.embl.de/newstring_download/species.tree.v9.05.txt](http://string905.embl.de/newstring_download/species.tree.v9.05.txt)) (ref. [48](https://www.nature.com/articles/ncomms11607#ref-CR48)). Reaction presence and absence states across branch points along the phylogenetic tree, that is, the ancestral states, are calculated by using the tree and the present-day presence/absence state of the reaction. The ancestral state is inferred by minimizing the number of gene-gain and loss events across the tree that matches the present-day state. Such a maximum parsimony strategy is commonly used as it allows for the analysis of gene histories on a genome-wide scale in a computationally efficient manner, and has shown to be successful in explaining patterns in genome content and evolution[19](https://www.nature.com/articles/ncomms11607#ref-CR19),[49](https://www.nature.com/articles/ncomms11607#ref-CR49),[50](https://www.nature.com/articles/ncomms11607#ref-CR50). Calculations were carried out using PAUP[51](https://www.nature.com/articles/ncomms11607#ref-CR51) with a gain/loss penalty ratio of 2/1 (ref. [52](https://www.nature.com/articles/ncomms11607#ref-CR52)) and a delayed transition assumption (DELTRAN)[49](https://www.nature.com/articles/ncomms11607#ref-CR49). We note that our results are robust against variations in PAUP parameter values (see [Supplementary Tables 1–3](https://www.nature.com/articles/ncomms11607#MOESM1070)).

### Contingent gain analysis
For each stepping-stone reaction pair A–B, A is defined as the reaction that is beneficial in a given nutrient environment without B, while a gain of B is only beneficial in another environment when A is already present. For each A–B pair we calculated the phylogenetic contingent gain fraction (_f_), defined as _f=p_1/(_p_1+_p_2), where _p_1 is calculated by dividing the number of evolutionary events where B is gained in the descendent (d) when A is already present in the ancestor (a) (a10_d11) by the total number of all possible gain and loss scenarios taking place in the descendant when A is present but B is absent in the ancestor (a10_dXX, where X=0 or 1), and p2 is calculated by dividing the number of evolutionary events where B is gained in the descendant when A is absent in the ancestor (a00_d01) by the total number of all possible gain and loss scenarios taking place in the descendant when both A and B are absent in the ancestor (a00_dXX, where X=0 or 1). The observed distribution of fractions was then compared with the null-hypothesis that a gain of B is independent of the presence of A, that is, _f_=0.5, using a one-tailed one-sample Wilcoxon signed-rank test.

### Co-gain analysis
For the phylogenetic co-gain analysis we calculated for reaction pairs the co-gain fraction, defined as _f=n_1/(_n_1+_n_2), where _n_1 is the number of evolutionary events where both reactions were absent in the ancestor (a) and both were gained in the descendent (d) (a00_d11), and _n_2 is the number of evolutionary events where both reactions were absent in the ancestor and only one was gained in the descendent (a00_d10 or a00_d01). We compared the fractions (_f_) from reaction pairs that are predicted to be beneficial for growth only when they are simultaneously gained, referred to as ‘beneficial without individual effect’, with the fractions from reaction pairs that are beneficial for growth in a specific environment when co-gained, but at least one of the reactions is also beneficial on its own in a different environment (beneficial with combined and individual effect) (see [Fig. 3b](https://www.nature.com/articles/ncomms11607#Fig3) in main text). A one-sided Wilcoxon rank test was used. In addition, we compared the fractions from ‘beneficial without individual effect’ reaction pairs with the expected co-gain fraction by chance (randomization (without individual effect)). To do that, we broke the pairing between reactions and shuffled the reactions into new pairs, thereby generating a new list of gene pairs. This was repeated 1,000 times. Then we determined for each of the 1,000 reaction pair list if the mean co-gain fraction is higher than that of the ‘beneficial without individual effect’ and summed these (n1). _P_-value was calculated as _P_=(_n_1+1)/1,001. The randomization analysis was also carried out for reaction pairs that are beneficial for growth in a specific environment when co-gained, but at least one of the reactions is also beneficial on its own in a different environment (beneficial with combined and individual effect versus randomization (combined and individual effect)).

### Strains and plasmids and primers for laboratory adaptation
_E. coli_ K-12 MG1655 was considered as the wild-type strain in our experiments. MG1655 mutD5 was constructed using a suicide plasmid-based genome engineering method incorporating a C->T mutation at position 236,110 on the genome (within the _dnaQ_ gene) resulting in a T15I mutation of the encoded enzyme described previously[27](https://www.nature.com/articles/ncomms11607#ref-CR27). Standard steps and plasmids (pST76-A, pSTKST) of this methodology have been described[53](https://www.nature.com/articles/ncomms11607#ref-CR53). Briefly, an approximately 800-bp-long targeting DNA fragment carrying the desired point mutation in the middle was synthesized by PCR, then cloned into a thermosensitive suicide plasmid (pST76-A). This plasmid construct was then transformed into the cell, where it was able to integrate into the chromosome by way of a single crossover between the mutant allele and the corresponding chromosomal region. The desired co-integrates were selected by the antibiotic resistance carried on the plasmid at a non-permissive temperature for plasmid replication (42 °C). Next, the pSTKST helper plasmid was transformed, then induced within the cells, resulting in the expression of the I-SceI meganuclease enzyme, which cleaves the chromosome at the 18 bp recognition site present on the integrated plasmid. The resulting chromosomal gap is repaired by way of RecA-mediated intramolecular recombination between the homologous segments in the vicinity of the broken ends. The recombinational repair results in either a reversion to the wild-type chromosome, or in a markerless allele replacement, which can be distinguished by sequencing the given chromosomal region. See [Supplementary Table 6](https://www.nature.com/articles/ncomms11607#MOESM1070) for the primers used for the mutation construction.

For the overexpression of FucO, the pCA24N plasmid containing the _fucO_ gene was selected from the ASKA library[29](https://www.nature.com/articles/ncomms11607#ref-CR29) and isolated from the host strain, then electroporated into the MG1655 strain. Overexpression of the gene was achieved by the addition of 50 μM IPTG.

For the simultaneous overexpression of _fucO_ and _aldA_, the chloramphenicol resistance cassette (CmR) of the pCA24N-_aldA_ plasmid from the ASKA library was exchanged to the kanamycin resistance marker (KmR), resulting in pCA24N-_aldA_-Km. The pCA24N-_aldA_ plasmid was first linearized by inverse PCR amplification using the pCA24N_frame_1 and pCA24N_frame_2 primer pair flanking the CmR cassette. The PCR product was treated with DpnI for 60 min at 37 °C and purified using the DNA Clean & Concentrator-5 Kit (Zymo Research #D4004). The KmR marker was PCR amplified from a pSTKST template using the ASKA-Gibson_Kan_Fw and ASKA-Gibson_Kan_Rev primers. The PCR fragment was then isolated from 1% agarose gel using the GeneJET Gel Extraction Kit (Thermo Scientific #K0691). The resulting DNA fragments were assembled using Gibson assembly cloning (Gibson Assembly Master Mix, New England Biolabs #E2611), according to the manufacturer’s protocol, then electroporated into electrocompetent _E. coli_ DH10B cells. Correct assemblies were verified by colony PCR using the ASKA-S2 and aldA-1 primer pair. Sequences of primers used in this construction are listed in [Supplementary Table 7](https://www.nature.com/articles/ncomms11607#MOESM1070).

### Media used in laboratory adaptation
Minimal salts (MS) medium was used as described previously[34](https://www.nature.com/articles/ncomms11607#ref-CR34), supplemented either with 0.4% glycerol, 30 mM (S)-propane-1, 2-diol (propylene glycol, PG), or 30 mM ethane-1, 2-diol (EG). Antibiotics were employed in the following working concentrations: 50 μg ml−1 ampicillin (Ap), 25 μg ml−1 chloramphenicol (Cm) and 25 μg ml−1 kanamycin (Km).

### Adaptation of strains for growth on PG and EG
Three replicates of each individual strain were started from single colonies grown on MS+0.4% glycerol agar plates (with Cm added where the _fucO_ overexpression plasmid was present) at 30 °C. An MG1655 strain carrying the pCA24N-_fucO_ plasmid was previously found to grow at 30 °C in 2 ml MS media supplemented with 30 mM PG (with 25 μg ml−1 Cm and 50 μM IPTG added). This culture was subsequently plated onto MS+0.4% glycerol (+Cm) agar plates, from which the PG+colonies, starters for selection for EG-utilization, were isolated. We opted for glycerol as a base carbon source to avoid catabolite repression (that is, the inhibition of utilization of various other carbon sources) as in ref. [28](https://www.nature.com/articles/ncomms11607#ref-CR28). Starter cultures were then grown in 2 ml MS+0.4% glycerol (+Cm where needed), from which 250 μl was then transferred to 25 ml fresh liquid MS media+0.4% glycerol (and Cm where needed). Cultures were grown to stationary phase at 30 °C, after which total cell count was determined by plating of appropriate dilutions onto MS+0.4% glycerol agar plates. The remainder of the cultures were then harvested and resuspended in 400 μl MS media without carbon source and finally plated in two halves onto MS agar plates supplemented with either 30 mM PG or 30 mM EG (with Cm and 50 μM IPTG added where the _fucO_ overexpression plasmid was present). Plates were then incubated at 30 °C for 40 days after which adapted colonies were counted and isolated. The plates were placed in plastic bags for the duration of the incubation to prevent significant drying of the agar media. Rates of adaptive mutations were calculated based on three replicate experiments as follows. When adapted colonies were observed, we simply calculated the average ratio of the number of adapted colonies per total cell number. In cases where no growing colonies were obtained, we calculated an upper limit to the adaptive mutation rate following the approach presented in ref. [35](https://www.nature.com/articles/ncomms11607#ref-CR35). Specifically, we made use of the fact that the Poisson distribution has a 5% probability of yielding zero events when the expected number of events is three. Thus, assuming no more than three adaptive mutations among all the cells tested in the three replicate experiments gives an upper bound on the adaptive mutation rate per cell per generation.

### Growth curve measurements
Individual colonies of strains MG1655, MG1655+pCA24N-_fucO_, MG1655+pCA24N-_aldA_-Km and MG1655+pCA24N-_fucO_+pCA24N-_aldA_-Km were grown and isolated from MS+0.4% glycerol plates carrying the desired antibiotic for the given plasmids. Starter cultures from single colonies were grown in 5 ml liquid MS media supplemented with 0.4% glycerol, as well as 50 μM IPTG and 25 μg ml−1 Cm and/or 25 μg ml−1 Km in the case of plasmid-harbouring strains. Cultures were grown until saturation after which 10 ml MS media supplemented with 30 mM of either PG or EG as well as 50 μM IPTG and 25 μg ml−1 Cm and/or 25 μg ml−1 Km where needed, were inoculated with the overnight cultures at a 100 × dilution. A total of 100 μl of these samples were then placed in six separate wells on a 96-well tissue culture plate (Jet Biofil), and placed in a PowerWave XS2 (BioTek) microplate spectrophotometer and grown at 30 °C. The edges of the plate were sealed with Breathe-Easy gas permeable sealing membrane (Diversified Biotech) to prevent evaporation.

### Mutation rate measurements
We estimated mutation frequencies of BW25113 (wild-type) and BW25113 overexpressing the FucO protein from the pCA24N_fucO plasmid. Briefly, cells resistant to rifampicin (carrying mutations in _rpoB_ (ref. [54](https://www.nature.com/articles/ncomms11607#ref-CR54))) were selected and counted. After overnight growth at 37 °C, ten tubes of 1 ml LB (+25 μg ml−1 chloramphenicol in the case of pCA24N_fucO carrying samples) were inoculated with approximately 104 cells each. FucO overexpression was induced by adding 50 μM IPTG after 2 h of growth, and cultures were grown to early stationary phase, all at 37 °C. Appropriate dilutions were spread onto non-selective LB agar plates and LB agar plates containing rifampicin (100 μg ml−1). The samples were incubated at 37 °C and colony counts were performed after 24 or 48 h, respectively. Mutation rates were calculated with the Ma–Sandri–Sarkar maximum-likelihood method[55](https://www.nature.com/articles/ncomms11607#ref-CR55) using the FALCOR web tool[56](https://www.nature.com/articles/ncomms11607#ref-CR56).

### Ion Torrent library construction for whole-genome sequencing
Fragment libraries were constructed from purified genomic DNA using NEBNext Fast DNA Fragmentation & Library Prep Set for Ion Torrent (New England Biolabs) according to manufacturer’s instructions. Briefly, genomic DNA was enzymatically digested and the fragments were end-repaired. Ion Xpress Barcode Adaptors (Life Technologies) were than ligated and the template fragments size-selected using AmPure beads (Agencourt). Adaptor ligated fragments were then PCR amplified, cleaned-up using AmPure beads, quality checked on D1000 ScreenTape and Reagents using TapeStation instrument (Agilent) and finally quantitated using Ion Library TaqMan Quantitation Kit (Life Technologies). The library templates were prepared for sequencing using the Life Technologies Ion OneTouch protocols and reagents. Briefly, library fragments were clonally amplified onto Ion Sphere Particles (ISPs) through emulsion PCR and then enriched for template-positive ISPs. More specifically, PGM emulsion PCR reactions utilized the Ion OneTouch 200 Template Kit (Life Technologies), and as specified in the accompanying protocol, emulsions and amplification were generated using the Ion OneTouch System (Life Technologies). Enrichment was completed by selectively binding the ISPs containing amplified library fragments to streptavidin-coated magnetic beads, removing empty ISPs through washing steps, and denaturing the library strands to allow for collection of the template-positive ISPs. For all reactions, these steps were accomplished using the Life Technologies ES module of the Ion OneTouch System. Template-positive ISPs were deposited onto the Ion 318 chips (Life Technologies); finally, sequencing was performed with the Ion PGM Sequencing Kit (Life Technologies).

### Ion PGM sequencing data processing and mutation calling
The PGM sequencing data was processed using Ion Torrent Suite v4.2.1 in order to perform signal processing and base calling. Read mapper module of Torrent Suite (tmap) was used to align raw reads to the _E. coli_ K12 MG1655 genome sequence (U00096.3). Torrent Variant caller (tvc) module of Torrent Suite was subsequently applied to detect single nucleotide mutations as well as small in/del variants. Variant caller was programmed to run in high stringency mode requesting at least 12 × read coverage and at least 66% mutation frequency. Only those variants were taken into account that were supported by sequencing on both strands. BAM alignment files were imported in CLC Genomics Workbench v7.5.1 (CLCBio) and variant regions were manually inspected in all strains. Large genomic rearrangements (deletions or amplifications with lengths above 10 kb) were manually identified using CLC Genomics Workbench Tool.

Sequencing data of the ancestral and evolved strains are deposited in the NCBI SRA database (accession numbers [SRX1167076](http://www.ncbi.nlm.nih.gov/sra?term=SRX1167076) and [SRX1167031](http://www.ncbi.nlm.nih.gov/sra?term=SRX1167031)).

## Additional information
**Accession codes:** Sequencing data of the ancestral and evolved strains are deposited in the NCBI SRA database with accession codes [SRX1167076](http://www.ncbi.nlm.nih.gov/sra?term=SRX1167076) and [SRX1167031](http://www.ncbi.nlm.nih.gov/sra?term=SRX1167031).

**How to cite this article:** Szappanos, B. _et al_. Adaptive evolution of complex innovations through stepwise metabolic niche expansion. _Nat. Commun._ 7:11607 doi: 10.1038/ncomms11607 (2016).

## Accession codes
### Accessions
#### Sequence Read Archive
## References
1. Lynch, M. & Abegg, A. The rate of establishment of complex adaptations. _Mol. Biol. Evol._**27**, 1404–1414 (2010).

[Article](https://doi.org/10.1093%2Fmolbev%2Fmsq020)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXmsVGjs74%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20rate%20of%20establishment%20of%20complex%20adaptations&journal=Mol.%20Biol.%20Evol.&doi=10.1093%2Fmolbev%2Fmsq020&volume=27&pages=1404-1414&publication_year=2010&author=Lynch%2CM&author=Abegg%2CA)  

2. Lynch, M. Scaling expectations for the time to establishment of complex adaptations. _Proc. Natl Acad. Sci. USA_**107**, 16577–16582 (2010).

[Article](https://doi.org/10.1073%2Fpnas.1010836107)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXht1Wru7%2FE)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2010PNAS..10716577L)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Scaling%20expectations%20for%20the%20time%20to%20establishment%20of%20complex%20adaptations&journal=Proc.%20Natl%20Acad.%20Sci.%20USA&doi=10.1073%2Fpnas.1010836107&volume=107&pages=16577-16582&publication_year=2010&author=Lynch%2CM)  

3. Copley, S. D. Evolution of efficient pathways for degradation of anthropogenic chemicals. _Nat. Chem. Biol._**5**, 559–566 (2009).

[Article](https://doi.org/10.1038%2Fnchembio.197)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD1MXoslenu7g%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Evolution%20of%20efficient%20pathways%20for%20degradation%20of%20anthropogenic%20chemicals&journal=Nat.%20Chem.%20Biol.&doi=10.1038%2Fnchembio.197&volume=5&pages=559-566&publication_year=2009&author=Copley%2CSD)  

4. Harms, M. J. & Thornton, J. W. Evolutionary biochemistry: revealing the historical and physical causes of protein properties. _Nat. Rev. Genet._**14**, 559–571 (2013).

[Article](https://doi.org/10.1038%2Fnrg3540)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3sXhtFWrs73J)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Evolutionary%20biochemistry%3A%20revealing%20the%20historical%20and%20physical%20causes%20of%20protein%20properties&journal=Nat.%20Rev.%20Genet.&doi=10.1038%2Fnrg3540&volume=14&pages=559-571&publication_year=2013&author=Harms%2CMJ&author=Thornton%2CJW)  

5. Orr, H. A. Adaptation and the cost of complexity. _Evolution_**54**, 13–20 (2000).

[Article](https://doi.org/10.1111%2Fj.0014-3820.2000.tb00002.x)  [CAS](https://www.nature.com/articles/cas-redirect/1:STN:280:DC%2BD3cvjsFOmuw%3D%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Adaptation%20and%20the%20cost%20of%20complexity&journal=Evolution&doi=10.1111%2Fj.0014-3820.2000.tb00002.x&volume=54&pages=13-20&publication_year=2000&author=Orr%2CHA)  

6. Wagner, A. Neutralism and selectionism: a network-based reconciliation. _Nat Rev Genet_**9**, 965–974 (2008).

[Article](https://doi.org/10.1038%2Fnrg2473)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD1cXhtlyhtbjF)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Neutralism%20and%20selectionism%3A%20a%20network-based%20reconciliation&journal=Nat%20Rev%20Genet&doi=10.1038%2Fnrg2473&volume=9&pages=965-974&publication_year=2008&author=Wagner%2CA)  

7. Wagner, A. _The Origins of Evolutionary Innovations: A Theory of Transformative Change in Living Systems_ Oxford University Press (2011).
8. Hayden, E. J., Ferrada, E. & Wagner, A. Cryptic genetic variation promotes rapid evolutionary adaptation in an RNA enzyme. _Nature_**474**, 92–95 (2011).

[Article](https://doi.org/10.1038%2Fnature10083)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3MXmvFyqt7o%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Cryptic%20genetic%20variation%20promotes%20rapid%20evolutionary%20adaptation%20in%20an%20RNA%20enzyme&journal=Nature&doi=10.1038%2Fnature10083&volume=474&pages=92-95&publication_year=2011&author=Hayden%2CEJ&author=Ferrada%2CE&author=Wagner%2CA)  

9. Mira, A., Ochman, H. & Moran, N. A. Deletional bias and the evolution of bacterial genomes. _Trends Genet._**17**, 589–596 (2001).

[Article](https://doi.org/10.1016%2FS0168-9525%2801%2902447-7)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD3MXnt1Wju7g%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deletional%20bias%20and%20the%20evolution%20of%20bacterial%20genomes&journal=Trends%20Genet.&doi=10.1016%2FS0168-9525%2801%2902447-7&volume=17&pages=589-596&publication_year=2001&author=Mira%2CA&author=Ochman%2CH&author=Moran%2CNA)  

10. Iwasa, Y., Michor, F. & Nowak, M. A. Stochastic tunnels in evolutionary dynamics. _Genetics_**166**, 1571–1579 (2004).

[Article](https://doi.org/10.1534%2Fgenetics.166.3.1571)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Stochastic%20tunnels%20in%20evolutionary%20dynamics&journal=Genetics&doi=10.1534%2Fgenetics.166.3.1571&volume=166&pages=1571-1579&publication_year=2004&author=Iwasa%2CY&author=Michor%2CF&author=Nowak%2CMA)  

11. Coyne, J. A., Barton, N. H. & Turelli, M. Perspective: A critique of Sewall Wright’s shifting balance theory of evolution. _Evolution_**51**, 643–671 (1997).

[Article](https://doi.org/10.1111%2Fj.1558-5646.1997.tb03650.x)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Perspective%3A%20A%20critique%20of%20Sewall%20Wright%E2%80%99s%20shifting%20balance%20theory%20of%20evolution&journal=Evolution&doi=10.1111%2Fj.1558-5646.1997.tb03650.x&volume=51&pages=643-671&publication_year=1997&author=Coyne%2CJA&author=Barton%2CNH&author=Turelli%2CM)  

12. Kashtan, N., Noor, E. & Alon, U. Varying environments can speed up evolution. _Proc. Natl Acad. Sci. USA_**104**, 13711–13716 (2007).

[Article](https://doi.org/10.1073%2Fpnas.0611630104)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD2sXpvVOjsb0%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2007PNAS..10413711K)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Varying%20environments%20can%20speed%20up%20evolution&journal=Proc.%20Natl%20Acad.%20Sci.%20USA&doi=10.1073%2Fpnas.0611630104&volume=104&pages=13711-13716&publication_year=2007&author=Kashtan%2CN&author=Noor%2CE&author=Alon%2CU)  

13. Lenski, R. E., Ofria, C., Pennock, R. T. & Adami, C. The evolutionary origin of complex features. _Nature_**423**, 139–144 (2003).

[Article](https://doi.org/10.1038%2Fnature01568)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD3sXjsVOrt7g%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2003Natur.423..139L)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20evolutionary%20origin%20of%20complex%20features&journal=Nature&doi=10.1038%2Fnature01568&volume=423&pages=139-144&publication_year=2003&author=Lenski%2CRE&author=Ofria%2CC&author=Pennock%2CRT&author=Adami%2CC)  

14. Gray, M. W., Lukes, J., Archibald, J. M., Keeling, P. J. & Doolittle, W. Irremediable complexity? _Science_**330**, 920–921 (2010).

[Article](https://doi.org/10.1126%2Fscience.1198594)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXhsVyqur7O)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2010Sci...330..920G)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Irremediable%20complexity%3F&journal=Science&doi=10.1126%2Fscience.1198594&volume=330&pages=920-921&publication_year=2010&author=Gray%2CMW&author=Lukes%2CJ&author=Archibald%2CJM&author=Keeling%2CPJ&author=Doolittle%2CW)  

15. Finnigan, G. C., Hanson-Smith, V., Stevens, T. H. & Thornton, J. W. Evolution of increased complexity in a molecular machine. _Nature_**481**, 360–364 (2012).

[Article](https://doi.org/10.1038%2Fnature10724)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC38XlsFyluw%3D%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2012Natur.481..360F)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Evolution%20of%20increased%20complexity%20in%20a%20molecular%20machine&journal=Nature&doi=10.1038%2Fnature10724&volume=481&pages=360-364&publication_year=2012&author=Finnigan%2CGC&author=Hanson-Smith%2CV&author=Stevens%2CTH&author=Thornton%2CJW)  

16. Horowitz, N. H. On the Evolution of Biochemical Syntheses. _Proc. Natl Acad. Sci. USA_**31**, 153–157 (1945).

[Article](https://doi.org/10.1073%2Fpnas.31.6.153)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DyaH2MXjt1amsg%3D%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=1945PNAS...31..153H)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=On%20the%20Evolution%20of%20Biochemical%20Syntheses&journal=Proc.%20Natl%20Acad.%20Sci.%20USA&doi=10.1073%2Fpnas.31.6.153&volume=31&pages=153-157&publication_year=1945&author=Horowitz%2CNH)  

17. Jensen, R. A. Enzyme recruitment in evolution of new function. _Annu. Rev. Microbiol._**30**, 409–425 (1976).

[Article](https://doi.org/10.1146%2Fannurev.mi.30.100176.002205)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DyaE28XlvVyitLs%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Enzyme%20recruitment%20in%20evolution%20of%20new%20function&journal=Annu.%20Rev.%20Microbiol.&doi=10.1146%2Fannurev.mi.30.100176.002205&volume=30&pages=409-425&publication_year=1976&author=Jensen%2CRA)  

18. Feist, A. M. et al. A genome-scale metabolic reconstruction for Escherichia coli K-12 MG1655 that accounts for 1260 ORFs and thermodynamic information. _Mol. Syst. Biol._**3**, 121 (2007).

[Article](https://doi.org/10.1038%2Fmsb4100155)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20genome-scale%20metabolic%20reconstruction%20for%20Escherichia%20coli%20K-12%20MG1655%20that%20accounts%20for%201260%20ORFs%20and%20thermodynamic%20information&journal=Mol.%20Syst.%20Biol.&doi=10.1038%2Fmsb4100155&volume=3&publication_year=2007&author=Feist%2CAM)  

19. Pál, C., Papp, B. & Lercher, M. J. Adaptive evolution of bacterial metabolic networks by horizontal gene transfer. _Nat. Genet._**37**, 1372–1375 (2005).

[Article](https://doi.org/10.1038%2Fng1686)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Adaptive%20evolution%20of%20bacterial%20metabolic%20networks%20by%20horizontal%20gene%20transfer&journal=Nat.%20Genet.&doi=10.1038%2Fng1686&volume=37&pages=1372-1375&publication_year=2005&author=P%C3%A1l%2CC&author=Papp%2CB&author=Lercher%2CMJ)  

20. Henry, C. S. et al. High-throughput generation, optimization and analysis of genome-scale metabolic models. _Nat. Biotechnol._**28**, 977–982 (2010).

[Article](https://doi.org/10.1038%2Fnbt.1672)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXhtVyiu73M)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=High-throughput%20generation%2C%20optimization%20and%20analysis%20of%20genome-scale%20metabolic%20models&journal=Nat.%20Biotechnol.&doi=10.1038%2Fnbt.1672&volume=28&pages=977-982&publication_year=2010&author=Henry%2CCS)  

21. Price, N. D., Reed, J. L. & Palsson, B. O. Genome-scale models of microbial cells: evaluating the consequences of constraints. _Nat. Rev. Microbiol._**2**, 886–897 (2004).

[Article](https://doi.org/10.1038%2Fnrmicro1023)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD2cXos1Kqurc%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Genome-scale%20models%20of%20microbial%20cells%3A%20evaluating%20the%20consequences%20of%20constraints&journal=Nat.%20Rev.%20Microbiol.&doi=10.1038%2Fnrmicro1023&volume=2&pages=886-897&publication_year=2004&author=Price%2CND&author=Reed%2CJL&author=Palsson%2CBO)  

22. Papp, B., Notebaart, R. A. & Pal, C. Systems-biology approaches for predicting genomic evolution. _Nat. Rev. Genet._**12**, 591–602 (2011).

[Article](https://doi.org/10.1038%2Fnrg3033)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3MXhtVeiurrJ)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Systems-biology%20approaches%20for%20predicting%20genomic%20evolution&journal=Nat.%20Rev.%20Genet.&doi=10.1038%2Fnrg3033&volume=12&pages=591-602&publication_year=2011&author=Papp%2CB&author=Notebaart%2CRA&author=Pal%2CC)  

23. Gould, S. J. & Vrba, E. S. Exaptation-a missing term in the science of form. _Paleobiology_**8**, 4–15 (1982).

[Article](https://doi.org/10.1017%2FS0094837300004310)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Exaptation-a%20missing%20term%20in%20the%20science%20of%20form&journal=Paleobiology&doi=10.1017%2FS0094837300004310&volume=8&pages=4-15&publication_year=1982&author=Gould%2CSJ&author=Vrba%2CES)  

24. Notebaart, R. A. et al. Network-level architecture and the evolutionary potential of underground metabolism. _Proc. Natl Acad. Sci. USA_**111**, 11762–11767 (2014).

[Article](https://doi.org/10.1073%2Fpnas.1406102111)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC2cXht1amsLfM)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2014PNAS..11111762N)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Network-level%20architecture%20and%20the%20evolutionary%20potential%20of%20underground%20metabolism&journal=Proc.%20Natl%20Acad.%20Sci.%20USA&doi=10.1073%2Fpnas.1406102111&volume=111&pages=11762-11767&publication_year=2014&author=Notebaart%2CRA)  

25. Ochman, H., Lawrence, J. G. & Groisman, E. A. Lateral gene transfer and the nature of bacterial innovation. _Nature_**405**, 299–304 (2000).

[Article](https://doi.org/10.1038%2F35012500)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD3cXjs1Kmu7w%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2000Natur.405..299O)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Lateral%20gene%20transfer%20and%20the%20nature%20of%20bacterial%20innovation&journal=Nature&doi=10.1038%2F35012500&volume=405&pages=299-304&publication_year=2000&author=Ochman%2CH&author=Lawrence%2CJG&author=Groisman%2CEA)  

26. Boronat, A., Caballero, E. & Aguilar, J. Experimental evolution of a metabolic pathway for ethylene glycol utilization by Escherichia coli. _J. Bacteriol._**153**, 134–139 (1983).

[CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DyaL3sXosF2nsw%3D%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=6336729)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC217350)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Experimental%20evolution%20of%20a%20metabolic%20pathway%20for%20ethylene%20glycol%20utilization%20by%20Escherichia%20coli&journal=J.%20Bacteriol.&volume=153&pages=134-139&publication_year=1983&author=Boronat%2CA&author=Caballero%2CE&author=Aguilar%2CJ)  

27. Fijalkowska, I. J. & Schaaper, R. M. Mutants in the Exo I motif of Escherichia coli dnaQ: defective proofreading and inviability due to error catastrophe. _Proc. Natl Acad. Sci. USA_**93**, 2856–2861 (1996).

[Article](https://doi.org/10.1073%2Fpnas.93.7.2856)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DyaK28XitVCitrY%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=1996PNAS...93.2856F)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Mutants%20in%20the%20Exo%20I%20motif%20of%20Escherichia%20coli%20dnaQ%3A%20defective%20proofreading%20and%20inviability%20due%20to%20error%20catastrophe&journal=Proc.%20Natl%20Acad.%20Sci.%20USA&doi=10.1073%2Fpnas.93.7.2856&volume=93&pages=2856-2861&publication_year=1996&author=Fijalkowska%2CIJ&author=Schaaper%2CRM)  

28. Lee, D. H. & Palsson, B. O. Adaptive evolution of Escherichia coli K-12 MG1655 during growth on a nonnative carbon source, L-1, 2-propanediol. _Appl. Environ. Microbiol._**76**, 4158–4168 (2010).

[Article](https://doi.org/10.1128%2FAEM.00373-10)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXptFOjsLo%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Adaptive%20evolution%20of%20Escherichia%20coli%20K-12%20MG1655%20during%20growth%20on%20a%20nonnative%20carbon%20source%2C%20L-1%2C%202-propanediol&journal=Appl.%20Environ.%20Microbiol.&doi=10.1128%2FAEM.00373-10&volume=76&pages=4158-4168&publication_year=2010&author=Lee%2CDH&author=Palsson%2CBO)  

29. Kitagawa, M. et al. Complete set of ORF clones of Escherichia coli ASKA library (a complete set of E. coli K-12 ORF archive): unique resources for biological research. _DNA Res._**12**, 291–299 (2006).

[Article](https://doi.org/10.1093%2Fdnares%2Fdsi012)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Complete%20set%20of%20ORF%20clones%20of%20Escherichia%20coli%20ASKA%20library%20%28a%20complete%20set%20of%20E.%20coli%20K-12%20ORF%20archive%29%3A%20unique%20resources%20for%20biological%20research&journal=DNA%20Res.&doi=10.1093%2Fdnares%2Fdsi012&volume=12&pages=291-299&publication_year=2006&author=Kitagawa%2CM)  

30. Baldoma, L. & Aguilar, J. Involvement of lactaldehyde dehydrogenase in several metabolic pathways of Escherichia coli K12. _J. Biol. Chem._**262**, 13991–13996 (1987).

[CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DyaL2sXlvFertr0%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=3308886)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Involvement%20of%20lactaldehyde%20dehydrogenase%20in%20several%20metabolic%20pathways%20of%20Escherichia%20coli%20K12&journal=J.%20Biol.%20Chem.&volume=262&pages=13991-13996&publication_year=1987&author=Baldoma%2CL&author=Aguilar%2CJ)  

31. Barve, A. & Wagner, A. A latent capacity for evolutionary innovation through exaptation in metabolic systems. _Nature_**500**, 203–206 (2013).

[Article](https://doi.org/10.1038%2Fnature12301)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3sXhtFShtL%2FF)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2013Natur.500..203B)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20latent%20capacity%20for%20evolutionary%20innovation%20through%20exaptation%20in%20metabolic%20systems&journal=Nature&doi=10.1038%2Fnature12301&volume=500&pages=203-206&publication_year=2013&author=Barve%2CA&author=Wagner%2CA)  

32. Maslov, S., Krishna, S., Pang, T. Y. & Sneppen, K. Toolbox model of evolution of prokaryotic metabolic networks and their regulation. _Proc. Natl Acad. Sci. USA_**106**, 9743–9748 (2009).

[Article](https://doi.org/10.1073%2Fpnas.0903206106)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD1MXotFGjsrs%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2009PNAS..106.9743M)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Toolbox%20model%20of%20evolution%20of%20prokaryotic%20metabolic%20networks%20and%20their%20regulation&journal=Proc.%20Natl%20Acad.%20Sci.%20USA&doi=10.1073%2Fpnas.0903206106&volume=106&pages=9743-9748&publication_year=2009&author=Maslov%2CS&author=Krishna%2CS&author=Pang%2CTY&author=Sneppen%2CK)  

33. Sabarly, V. et al. The decoupling between genetic structure and metabolic phenotypes in Escherichia coli leads to continuous phenotypic diversity. _J. Evol. Biol._**24**, 1559–1571 (2011).

[Article](https://doi.org/10.1111%2Fj.1420-9101.2011.02287.x)  [CAS](https://www.nature.com/articles/cas-redirect/1:STN:280:DC%2BC3Mnht1ahsg%3D%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20decoupling%20between%20genetic%20structure%20and%20metabolic%20phenotypes%20in%20Escherichia%20coli%20leads%20to%20continuous%20phenotypic%20diversity&journal=J.%20Evol.%20Biol.&doi=10.1111%2Fj.1420-9101.2011.02287.x&volume=24&pages=1559-1571&publication_year=2011&author=Sabarly%2CV)  

34. Hall, B. G. The EBG system of E. coli: origin and evolution of a novel beta-galactosidase for the metabolism of lactose. _Genetica_**118**, 143–156 (2003).

[Article](https://doi.org/10.1023%2FA%3A1024149508376)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD3sXksFWnt7g%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20EBG%20system%20of%20E.%20coli%3A%20origin%20and%20evolution%20of%20a%20novel%20beta-galactosidase%20for%20the%20metabolism%20of%20lactose&journal=Genetica&doi=10.1023%2FA%3A1024149508376&volume=118&pages=143-156&publication_year=2003&author=Hall%2CBG)  

35. Blount, Z. D., Borland, C. Z. & Lenski, R. E. Historical contingency and the evolution of a key innovation in an experimental population of Escherichia coli. _Proc. Natl Acad. Sci. USA_**105**, 7899–7906 (2008).

[Article](https://doi.org/10.1073%2Fpnas.0803151105)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD1cXns1Sqs7c%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2008PNAS..105.7899B)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Historical%20contingency%20and%20the%20evolution%20of%20a%20key%20innovation%20in%20an%20experimental%20population%20of%20Escherichia%20coli&journal=Proc.%20Natl%20Acad.%20Sci.%20USA&doi=10.1073%2Fpnas.0803151105&volume=105&pages=7899-7906&publication_year=2008&author=Blount%2CZD&author=Borland%2CCZ&author=Lenski%2CRE)  

36. Linster, C. L., Van Schaftingen, E. & Hanson, A. D. Metabolite damage and its repair or pre-emption. _Nat. Chem. Biol._**9**, 72–80 (2013).

[Article](https://doi.org/10.1038%2Fnchembio.1141)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3sXhtFSnu7k%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Metabolite%20damage%20and%20its%20repair%20or%20pre-emption&journal=Nat.%20Chem.%20Biol.&doi=10.1038%2Fnchembio.1141&volume=9&pages=72-80&publication_year=2013&author=Linster%2CCL&author=Van%20Schaftingen%2CE&author=Hanson%2CAD)  

37. Weng, J. K., Philippe, R. N. & Noel, J. P. The rise of chemodiversity in plants. _Science_**336**, 1667–1670 (2012).

[Article](https://doi.org/10.1126%2Fscience.1217411)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC38XptFWnu7g%3D)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2012Sci...336.1667W)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20rise%20of%20chemodiversity%20in%20plants&journal=Science&doi=10.1126%2Fscience.1217411&volume=336&pages=1667-1670&publication_year=2012&author=Weng%2CJK&author=Philippe%2CRN&author=Noel%2CJP)  

38. Bandyopadhyay, S. et al. Rewiring of genetic networks in response to DNA damage. _Science_**330**, 1385–1389 (2010).

[Article](https://doi.org/10.1126%2Fscience.1195618)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3cXhsVyrsbnL)  [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2010Sci...330.1385B)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Rewiring%20of%20genetic%20networks%20in%20response%20to%20DNA%20damage&journal=Science&doi=10.1126%2Fscience.1195618&volume=330&pages=1385-1389&publication_year=2010&author=Bandyopadhyay%2CS)  

39. Sauer, U. Evolutionary engineering of industrially important microbial phenotypes. _Adv. Biochem. Eng. Biotechnol._**73**, 129–169 (2001).

[CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD3MXotlKitr0%3D)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=11816810)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Evolutionary%20engineering%20of%20industrially%20important%20microbial%20phenotypes&journal=Adv.%20Biochem.%20Eng.%20Biotechnol.&volume=73&pages=129-169&publication_year=2001&author=Sauer%2CU)  

40. O’Neill, M., Vanneschi, L., Gustafson, S. & Banzhaf, W. Open issues in genetic programming. _Genet. Program. Evolvable Mach._**11**, 339–363 (2010).

[Article](https://link.springer.com/doi/10.1007/s10710-010-9113-2)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Open%20issues%20in%20genetic%20programming&journal=Genet.%20Program.%20Evolvable%20Mach.&doi=10.1007%2Fs10710-010-9113-2&volume=11&pages=339-363&publication_year=2010&author=O%E2%80%99Neill%2CM&author=Vanneschi%2CL&author=Gustafson%2CS&author=Banzhaf%2CW)  

41. Das, S., Mandal, A. & Mukherjee, R. An adaptive differential evolution algorithm for global optimization in dynamic environments. _IEEE Trans. Cybern._**44**, 966–978 (2014).

[Article](https://doi.org/10.1109%2FTCYB.2013.2278188)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=An%20adaptive%20differential%20evolution%20algorithm%20for%20global%20optimization%20in%20dynamic%20environments&journal=IEEE%20Trans.%20Cybern.&doi=10.1109%2FTCYB.2013.2278188&volume=44&pages=966-978&publication_year=2014&author=Das%2CS&author=Mandal%2CA&author=Mukherjee%2CR)  

42. Orth, J. D. et al. A comprehensive genome-scale reconstruction of Escherichia coli metabolism--2011. _Mol. Syst. Biol._**7**, 535 (2011).

[Article](https://doi.org/10.1038%2Fmsb.2011.65)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20comprehensive%20genome-scale%20reconstruction%20of%20Escherichia%20coli%20metabolism--2011&journal=Mol.%20Syst.%20Biol.&doi=10.1038%2Fmsb.2011.65&volume=7&publication_year=2011&author=Orth%2CJD)  

43. McCloskey, D., Palsson, B. O. & Feist, A. M. Basic and applied uses of genome-scale metabolic network reconstructions of Escherichia coli. _Mol. Syst. Biol._**9**, 661 (2013).

[Article](https://doi.org/10.1038%2Fmsb.2013.18)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3sXhtFSqsbjE)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Basic%20and%20applied%20uses%20of%20genome-scale%20metabolic%20network%20reconstructions%20of%20Escherichia%20coli&journal=Mol.%20Syst.%20Biol.&doi=10.1038%2Fmsb.2013.18&volume=9&publication_year=2013&author=McCloskey%2CD&author=Palsson%2CBO&author=Feist%2CAM)  

44. de Figueiredo, L. F. et al. Computing the shortest elementary flux modes in genome-scale metabolic networks. _Bioinformatics_**25**, 3158–3165 (2009).

[Article](https://doi.org/10.1093%2Fbioinformatics%2Fbtp564)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD1MXhsVGlsb%2FM)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Computing%20the%20shortest%20elementary%20flux%20modes%20in%20genome-scale%20metabolic%20networks&journal=Bioinformatics&doi=10.1093%2Fbioinformatics%2Fbtp564&volume=25&pages=3158-3165&publication_year=2009&author=de%20Figueiredo%2CLF)  

45. R Core Team. _R_: _A Language and Environment for Statistical Computing_ (R Foundation for Statistical Computing, Vienna, Austria, 2015).
46. Gelius-Dietrich, G., Amer Desouki, A., Fritzemeier, C. J. & Lercher, M. J. sybil - Efficient constraint-based modelling in R. _BMC Syst. Biol._**7**, 125 (2013).

[Article](https://link.springer.com/doi/10.1186/1752-0509-7-125)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=sybil%20-%20Efficient%20constraint-based%20modelling%20in%20R&journal=BMC%20Syst.%20Biol.&doi=10.1186%2F1752-0509-7-125&volume=7&publication_year=2013&author=Gelius-Dietrich%2CG&author=Amer%20Desouki%2CA&author=Fritzemeier%2CCJ&author=Lercher%2CMJ)  

47. Powell, S. et al. eggNOG v3.0: orthologous groups covering 1133 organisms at 41 different taxonomic ranges. _Nucleic Acids Res._**40**, D284–D289 (2012).

[Article](https://doi.org/10.1093%2Fnar%2Fgkr1060)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3MXhs12htbbM)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=eggNOG%20v3.0%3A%20orthologous%20groups%20covering%201133%20organisms%20at%2041%20different%20taxonomic%20ranges&journal=Nucleic%20Acids%20Res.&doi=10.1093%2Fnar%2Fgkr1060&volume=40&pages=D284-D289&publication_year=2012&author=Powell%2CS)  

48. Szklarczyk, D. et al. The STRING database in 2011: functional interaction networks of proteins, globally integrated and scored. _Nucleic Acids Res._**39**, D561–D568 (2011).

[Article](https://doi.org/10.1093%2Fnar%2Fgkq973)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC3sXivF2lt7w%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20STRING%20database%20in%202011%3A%20functional%20interaction%20networks%20of%20proteins%2C%20globally%20integrated%20and%20scored&journal=Nucleic%20Acids%20Res.&doi=10.1093%2Fnar%2Fgkq973&volume=39&pages=D561-D568&publication_year=2011&author=Szklarczyk%2CD)  

49. Notebaart, R. A., Kensche, P. R., Huynen, M. A. & Dutilh, B. E. Asymmetric relationships between proteins shape genome evolution. _Genome Biol._**10**, R19 (2009).

[Article](https://link.springer.com/doi/10.1186/gb-2009-10-2-r19)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Asymmetric%20relationships%20between%20proteins%20shape%20genome%20evolution&journal=Genome%20Biol.&doi=10.1186%2Fgb-2009-10-2-r19&volume=10&publication_year=2009&author=Notebaart%2CRA&author=Kensche%2CPR&author=Huynen%2CMA&author=Dutilh%2CBE)  

50. Lu, X., Kensche, P. R., Huynen, M. A. & Notebaart, R. A. Genome evolution predicts genetic interactions in protein complexes and reveals cancer drug targets. _Nat. Commun._**4**, 2124 (2013).

[Article](https://doi.org/10.1038%2Fncomms3124)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Genome%20evolution%20predicts%20genetic%20interactions%20in%20protein%20complexes%20and%20reveals%20cancer%20drug%20targets&journal=Nat.%20Commun.&doi=10.1038%2Fncomms3124&volume=4&publication_year=2013&author=Lu%2CX&author=Kensche%2CPR&author=Huynen%2CMA&author=Notebaart%2CRA)  

51. Swofford, D. L. {_PAUP*. Phylogenetic Analysis Using Parsimony (*and Other Methods). Version 4._} Sinauer Associates (2003).
52. Snel, B., Bork, P. & Huynen, M. A. Genomes in flux: the evolution of archaeal and proteobacterial gene content. _Genome Res._**12**, 17–25 (2002).

[Article](https://doi.org/10.1101%2Fgr.176501)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD38XksV2rsQ%3D%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Genomes%20in%20flux%3A%20the%20evolution%20of%20archaeal%20and%20proteobacterial%20gene%20content&journal=Genome%20Res.&doi=10.1101%2Fgr.176501&volume=12&pages=17-25&publication_year=2002&author=Snel%2CB&author=Bork%2CP&author=Huynen%2CMA)  

53. Fehér, T. et al. Scarless engineering of the Escherichia coli genome. in _Microbial Gene Essentiality: Protocols and Bioinformatics_ Springer (2008).
54. Jin, D. J. & Gross, C. A. Mapping and sequencing of mutations in the Escherichia coli rpoB gene that lead to rifampicin resistance. _J. Mol. Biol._**202**, 45–58 (1988).

[Article](https://doi.org/10.1016%2F0022-2836%2888%2990517-7)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DyaL1cXls1Cntrg%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Mapping%20and%20sequencing%20of%20mutations%20in%20the%20Escherichia%20coli%20rpoB%20gene%20that%20lead%20to%20rifampicin%20resistance&journal=J.%20Mol.%20Biol.&doi=10.1016%2F0022-2836%2888%2990517-7&volume=202&pages=45-58&publication_year=1988&author=Jin%2CDJ&author=Gross%2CCA)  

55. Sarkar, S., Ma, W. T. & Sandri, G. H. On fluctuation analysis: a new, simple and efficient method for computing the expected number of mutants. _Genetica_**85**, 173–179 (1992).

[Article](https://link.springer.com/doi/10.1007/BF00120324)  [CAS](https://www.nature.com/articles/cas-redirect/1:STN:280:DyaK38zisVKhtA%3D%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=On%20fluctuation%20analysis%3A%20a%20new%2C%20simple%20and%20efficient%20method%20for%20computing%20the%20expected%20number%20of%20mutants&journal=Genetica&doi=10.1007%2FBF00120324&volume=85&pages=173-179&publication_year=1992&author=Sarkar%2CS&author=Ma%2CWT&author=Sandri%2CGH)  

56. Hall, B. M., Ma, C. X., Liang, P. & Singh, K. K. Fluctuation analysis CalculatOR: a web tool for the determination of mutation rate using Luria-Delbruck fluctuation analysis. _Bioinformatics_**25**, 1564–1565 (2009).

[Article](https://doi.org/10.1093%2Fbioinformatics%2Fbtp253)  [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BD1MXms1CjtL0%3D)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fluctuation%20analysis%20CalculatOR%3A%20a%20web%20tool%20for%20the%20determination%20of%20mutation%20rate%20using%20Luria-Delbruck%20fluctuation%20analysis&journal=Bioinformatics&doi=10.1093%2Fbioinformatics%2Fbtp253&volume=25&pages=1564-1565&publication_year=2009&author=Hall%2CBM&author=Ma%2CCX&author=Liang%2CP&author=Singh%2CKK)  

[Download references](https://citation-needed.springer.com/v2/references/10.1038/ncomms11607?format=refman&flavour=references)

## Acknowledgements
We acknowledge the insightful comments of the anonymous reviewers on a previous version of the paper. This work was supported by the ‘Lendület’ Programme of the Hungarian Academy of Sciences and The Wellcome Trust (B.P. and C.P.), European Research Council (C.P.), the Hungarian Scientific Research Fund PD 109572 (B.C.), the European Union and the State of Hungary, co-financed by the European Social Fund in the framework of TÁMOP 4.2.4. A/2-11-/1-2012-0001 ‘National Excellence Program’ (B.S.), the János Bolyai Research Scholarship of the Hungarian Academy of Sciences (I.N.), the Hungarian Academy of Sciences Postdoctoral Fellowship Programme (V.L.), the Seventh Framework Programme (FP7) of the European Union through the GENCODYS Consortium, FP7-HEALTH-241995 (XL), German Research Foundation (CRC 680) (MJL) and a fellowship from the graduate school E-Norm of the Heinrich-Heine University (J.F.). Computational support of the Zentrum für Informations- und Medientechnologie (ZIM) at the Heinrich-Heine University is gratefully acknowledged.

## Author information
Author notes

1. Balázs Szappanos, Jonathan Fritzemeier and Bálint Csörgő: These authors contributed equally to this work

### Authors and Affiliations
1. Synthetic and Systems Biology Unit, Institute of Biochemistry, Biological Research Centre of the Hungarian Academy of Sciences, Temesvári krt. 62, Szeged, H-6726, Hungary

Balázs Szappanos, Bálint Csörgő, Viktória Lázár, Gergely Fekete, Csaba Pál & Balázs Papp

2. Department for Computer Science, Heinrich Heine University, Universitätsstraße 1, Düsseldorf, D-40221, Germany

Jonathan Fritzemeier & Martin J. Lercher

3. Department of Bioinformatics (CMBI), Radboud University Medical Centre, Geert Grooteplein Zuid 26–28, Nijmegen, 6525 GA, The Netherlands

Xiaowen Lu & Richard A. Notebaart

4. SeqOmics Biotechnology Ltd, Vállalkozók útja 7, Mórahalom, H-6782, Hungary

Balázs Bálint, Róbert Herczeg & István Nagy

5. Sequencing Platform, Institute of Biochemistry, Biological Research Centre of the Hungarian Academy of Sciences, Temesvári krt. 62, Szeged, H-6726, Hungary

István Nagy

6. Department of Internal Medicine, Radboud University Medical Center, Geert Grooteplein Zuid 8, Nijmegen, 6525 GA, The Netherlands

Richard A. Notebaart

Authors

1. Balázs Szappanos

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Bal%C3%A1zs%20Szappanos) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Bal%C3%A1zs%20Szappanos%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

2. Jonathan Fritzemeier

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Jonathan%20Fritzemeier) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Jonathan%20Fritzemeier%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

3. Bálint Csörgő

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=B%C3%A1lint%20Cs%C3%B6rg%C5%91) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22B%C3%A1lint%20Cs%C3%B6rg%C5%91%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

4. Viktória Lázár

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Vikt%C3%B3ria%20L%C3%A1z%C3%A1r) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Vikt%C3%B3ria%20L%C3%A1z%C3%A1r%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

5. Xiaowen Lu

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Xiaowen%20Lu) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Xiaowen%20Lu%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

6. Gergely Fekete

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Gergely%20Fekete) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Gergely%20Fekete%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

7. Balázs Bálint

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Bal%C3%A1zs%20B%C3%A1lint) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Bal%C3%A1zs%20B%C3%A1lint%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

8. Róbert Herczeg

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=R%C3%B3bert%20Herczeg) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22R%C3%B3bert%20Herczeg%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

9. István Nagy

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Istv%C3%A1n%20Nagy) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Istv%C3%A1n%20Nagy%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

10. Richard A. Notebaart

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Richard%20A.%20Notebaart) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Richard%20A.%20Notebaart%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

11. Martin J. Lercher

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Martin%20J.%20Lercher) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Martin%20J.%20Lercher%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

12. Csaba Pál

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Csaba%20P%C3%A1l) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Csaba%20P%C3%A1l%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

13. Balázs Papp

You can also search for this author in [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Bal%C3%A1zs%20Papp) [Google Scholar](http://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Bal%C3%A1zs%20Papp%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

### Contributions
B.P., C.P. and M.J.L. conceived and supervised the project; B.C., V.L., B.S. and I.N. designed the experiments; B.C., V.L., I.N., B.B. and R.H. performed the experiments; B.S., J.F., X.L., R.A.N. and G.F. performed computational data analysis; and B.S., J.F., B.C., M.J.L., R.A.N., C.P. and B.P. wrote the paper.

### Corresponding authors
Correspondence to [Csaba Pál](mailto:cpal@brc.hu) or [Balázs Papp](mailto:pappb@brc.hu).

## Ethics declarations
### Competing interests
The authors declare no competing financial interests.

## Supplementary information
### [Supplementary Information](https://static-content.springer.com/esm/art%3A10.1038%2Fncomms11607/MediaObjects/41467_2016_BFncomms11607_MOESM1070_ESM.pdf)
Supplementary figures 1-3, supplementary tables 1-7, supplementary methods, supplementary references (PDF 579 kb)

### [Supplementary Dataset 1](https://static-content.springer.com/esm/art%3A10.1038%2Fncomms11607/MediaObjects/41467_2016_BFncomms11607_MOESM1071_ESM.xlsx)
lists the set of 1776 environmental conditions defined in the present study and the in silico biomass flux for both the E. coli and the universal reaction networks. (XLSX 97 kb)

### [Supplementary Dataset 2](https://static-content.springer.com/esm/art%3A10.1038%2Fncomms11607/MediaObjects/41467_2016_BFncomms11607_MOESM1072_ESM.xlsx)
lists the reactions which enable in silico growth in a condition where the E. coli metabolic network cannot grow (XLSX 21 kb)

### [Supplementary Dataset 3](https://static-content.springer.com/esm/art%3A10.1038%2Fncomms11607/MediaObjects/41467_2016_BFncomms11607_MOESM1073_ESM.xlsx)
lists all reaction pairs which can confer a novel nutrient utilization phenotype when added to the E. coli metabolic network (XLSX 64 kb)

### [Supplementary Dataset 4](https://static-content.springer.com/esm/art%3A10.1038%2Fncomms11607/MediaObjects/41467_2016_BFncomms11607_MOESM1074_ESM.zip)
the universal metabolic network in SBML format (ZIP 237 kb)

## Rights and permissions
This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)

[Reprints and permissions](https://s100.copyright.com/AppDispatchServlet?title=Adaptive%20evolution%20of%20complex%20innovations%20through%20stepwise%20metabolic%20niche%20expansion&author=Bal%C3%A1zs%20Szappanos%20et%20al&contentID=10.1038%2Fncomms11607&copyright=The%20Author%28s%29&publication=2041-1723&publicationDate=2016-05-20&publisherName=SpringerNature&orderBeanReset=true&oa=CC%20BY)

## About this article
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/svg/22983715/1710077451283-46599c8b-4c7e-41cd-8f1b-38f4c9775b6c.svg)

### Cite this article
Szappanos, B., Fritzemeier, J., Csörgő, B. _et al._ Adaptive evolution of complex innovations through stepwise metabolic niche expansion. _Nat Commun_**7**, 11607 (2016). https://doi.org/10.1038/ncomms11607

[Download citation](https://citation-needed.springer.com/v2/references/10.1038/ncomms11607?format=refman&flavour=citation)

+ Received: 02 December 2015
+ Accepted: 12 April 2016
+ Published: 20 May 2016
+ DOI: https://doi.org/10.1038/ncomms11607

### Subjects
  


> 来自: [Adaptive evolution of complex innovations through stepwise metabolic niche expansion | Nature Communications](https://www.nature.com/articles/ncomms11607)
>

