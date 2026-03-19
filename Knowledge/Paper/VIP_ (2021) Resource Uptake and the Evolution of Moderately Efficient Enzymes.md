Florian Labourel, Etienne Rajon, Resource Uptake and the Evolution of Moderately Efficient Enzymes, _Molecular Biology and Evolution_, Volume 38, Issue 9, September 2021, Pages 3938–3952, [https://doi.org/10.1093/molbev/msab132](https://doi.org/10.1093/molbev/msab132)

## Abstract
Enzymes speed up reactions that would otherwise be too slow to sustain the metabolism of selfreplicators. Yet, most enzymes seem only moderately efficient, exhibiting kinetic parameters orders of magnitude lower than their expected physically achievable maxima and spanning over surprisingly large ranges of values. Here, we question how these parameters evolve using a mechanistic model where enzyme efficiency is a key component of individual competition for resources. We show that kinetic parameters are under strong directional selection only up to a point, above which enzymes appear to evolve under near-neutrality, thereby confirming the qualitative observation of other modeling approaches. While the existence of a large fitness plateau could potentially explain the extensive variation in enzyme features reported, we show using a population genetics model that such a widespread distribution is an unlikely outcome of evolution on a common landscape, as mutation–selection–drift balance occupy a narrow area even when very moderate biases towards lower efficiency are considered. Instead, differences in the evolutionary context encountered by each enzyme should be involved, such that each evolves on an individual, unique landscape. Our results point to drift and effective population size playing an important role, along with the kinetics of nutrient transporters, the tolerance to high concentrations of intermediate metabolites, and the reversibility of reactions. Enzyme concentration also shapes selection on kinetic parameters, but we show that the joint evolution of concentration and efficiency does not yield extensive variance in evolutionary outcomes when documented costs to protein expression are applied.

Associate Editor: Banu Ozkan

Banu Ozkan 

Associate Editor 

Search for other works by this author on: 

   


## Introduction
Livingorganisms need to uptake and metabolize nutrients, relying on enzymes to catalyze chemical reactions along metabolic pathways. Accordingly, and despite being intrinsically reversible (Haldane 1930; Klipp and Heinrich 1994), in vivo enzyme-catalyzed reactions are commonly thought of as an irreversible two-step process (Michaelis and Menten 1913; Bar-Even et al. 2011, 2015; Michaelis et al. 2011): 

where _k__f_ and _k__r_ are the rates of association and dissociation between enzyme and substrate, and kcat is the turnover number, that is the rate of formation of the product _P_ from _ES_ complexes. The first part of this chemical equation describes the encounters between the enzyme _E_ and the substrate _S_; the enzyme will be efficient if _ES_ complexes form often and do not dissociate before the substrate has been turned into a product, which is reflected by the constant KM=kr+kcatkf⁠. The efficiency _v_ of an enzyme—the rate at which it makes a product _P_ from _S—_depends on these two constants through [equation (2)](https://academic.oup.com/mbe/article/38/9/3938/6272522?login=false#E2): 

under the assumption that the concentration [S] is approximately constant and that of [ES] is at a steady state (Michaelis and Menten 1913; Briggs and Haldane 1925).

At first glance, Natural Selection is presumed to optimize enzymatic efficiency by pushing kcat upwards and KM downwards to universal physical limits. Enzyme efficiencies are for instance limited by the diffusion properties of their aqueous environment, which sets an upper bound of approximately 108−1010M−1s−1 for the ratio kcat/KM (Alberty and Hammes 1958; Zhou and Zhong 1982). Nearly optimal enzymes indeed seem to exist, as exemplified by triosephosphate isomerase (TIM) whose ratio is close to this theoretical ceiling (Knowles and Albery 1977). But they are uncommon: most enzymes appear to be only moderately efficient and far off these physical limits—including enzymes immediately flanking TIM in the glycolysis metabolic pathway (Davidi et al. 2018). Indeed, Bar-Even _et al._ (2011) have analyzed a data set of several hundreds of enzymes and found a wide diversity among enzyme parameters, thus sketching a puzzling pattern that has far more in common with a zoo than it looks like variations around an archetypal form.

This wide distribution of enzyme features could partly be explained by differences between enzyme behavior in vivo and in vitro. Such differences are expected, first because diffusion in a test tube is hardly comparable to diffusion in the cytoplasm (Ellis 2001; Rivas et al. 2004; Zhou et al. 2008; Rivas and Minton 2018). As the cytoplasm gets packed, the cell approaches a state where molecules are less mobile, hindering substrate-enzyme encounters (Muramatsu and Minton 1988; Zimmerman and Minton 1993; Blanco et al. 2018). In this regard, KM values are likely underestimated in vitro, and enzymes should perform less efficiently _in vivo_. Simultaneously, macromolecular crowding can sometimes improve catalytic activity _in vivo_, making specificity constants kcat/KM higher than their in vitro estimates (Ralston 1990; Ellis 2001; Jiang and Guo 2007; Pozdnyakova and Wittung-Stafshede 2010). Crowding effects are obviously important for our understanding of enzyme evolution but, alone, they are definitely too weak to explain the wide variability across enzymes insofar as their reported estimates typically lie in the range of one order of magnitude (Davidi et al. 2016).

Another source of explanation to the observed distribution of enzymes (in)efficiencies is a failure of Evolution to consistently optimize them, possibly due to physical constraints. Indeed, Heckmann _et al._ (2018) have shown how a variety of kcats may evolve provided that some of them are physically constrained. Besides the diffusion limit already mentioned, constraints on enzyme evolution might include an intrinsic trade-off (Gudelj et al. 2010; Stiffler et al. 2015) that originates from the dependency of both kcat and KM on intermediate energy profiles (Heinrich et al. 1991). Nonetheless, this trade-off is scarcely observable among evolved enzymes—Bar-Even _et al._ (2011) report a coefficient of determination around 0.09 for the correlation between log10(kcat) and log10(KM)—suggesting that it can be overcome. Other constraints may exist and be specific of a given reaction (Klipp and Heinrich 1994)—for example, reaction reversibility—potentially explaining a part of the variance in enzyme efficiencies. It remains that estimating constraints on all individual enzymes appears like a daunting task, which could be guided, in part, by the identification of deviations from evolutionary predictions.

Following this idea, the premise of our theoretical investigation into the origins of enzyme diversity is that it results mainly from unconstrained evolution, such that the reported differences may be caused by the combined action of selection and genetic drift. It is important to notice that the information we have is partial, as an enzyme’s activity is the joint result of its kinetic constants and cellular concentration, perhaps also contributing to the reported variance in the former. In fact, Davidi _et al._ (2016)’s method to determine in vivo turn-over rates lends some credence to the idea that increased levels of expression make up for lower kinetic constants (Davidi et al. 2018). It is therefore obvious that an enzyme’s expression needs to be considered as another dimension of its activity, especially since it has been shown that the evolutionary tuning of gene expression can happen very quickly (Dekel and Alon 2005).

Concomitantly, an enzyme’s activity can be impacted by protein misfolding, which reduces the effective enzyme concentration (Drummond et al. 2005; Yue et al. 2005; Tokuriki and Tawfik 2009; Echave and Wilke 2017) while also impacting fitness by enhancing protein erroneous interactions (Yang et al. 2012) and the formation of toxic protein aggregates (Bucciantini et al. 2002; Sabate et al. 2010; Geiler-Samerotte et al. 2011). Protein stability is thus under strong purifying selection to avoid the deleterious effects of misfolding (Drummond and Wilke 2008). Accordingly, it has been shown that proteins have evolved to stand beyond a stability threshold (Bloom et al. 2005), although marginally (Taverna and Goldstein 2002). Because mutations are on average destabilizing, this definitely narrows down the spectrum of adaptive mutations (Shoichet et al. 1995; DePristo et al. 2005; Weinreich et al. 2006; Tokuriki et al. 2007, 2008; Lunzer et al. 2010). Nevertheless, several studies have reported the existence of a genotype space where activity can be optimized without compromising stability (Schreiber et al. 1994; van den Burg and Eijsink 2002; Bloom et al. 2004; Knies et al. 2017; Miller 2017). Even when improving function requires the fixation of destabilizing mutations, compensatory mutations can in principle cancel out stability losses arising from active site evolution (DePristo et al. 2005; Tokuriki et al. 2008; Tokuriki and Tawfik 2009; Storz 2018). Adaptive evolution may even be facilitated by preexisting mutational robustness against misfolding (Bloom et al. 2006, 2007). Therefore, although the requirement of a stable, correctly folding protein may sometimes slow down the evolutionary process, it is rather unlikely that stability explains the distribution of enzyme kinetic parameters albeit marginally.

Enzyme kinetics evolution has often been considered theoretically through the lens of flux control (Burns et al. 1985; Clark 1991; Fell 1992; Kacser et al. 1995; Yi and Dean 2019). Indeed, the control of the flux in a metabolic pathway is shared between all enzymes, in what is known as the summation theorem (Kacser and Burns 1973; Heinrich and Rapoport 1974). Thence, because the sum of control coefficients must equal 1 within a pathway, if all enzymes have similar kinetic parameters, none of them exerts a strong influence (Dean 1995). But if one enzyme departs from this trend and becomes inefficient, it exerts a strong control at the expense of others (Dykhuizen and Dean 1990). This leads to diminishing-returns epistasis in which the fitness landscape flattens because, as an enzyme becomes more efficient, subsequent mutations have smaller effects (Kacser and Burns 1973; Dykhuizen et al. 1987; Tokuriki et al. 2012), a finding that has since received empirical confirmation (Fell 1992; Dean 1995; Lunzer et al. 2005; Yi and Dean 2019; Chou et al. 2014).

Hartl et al. (1985) and Dean et al. (1986) have considered such a fitness landscape under a population genetics framework to conclude that enzymes may quickly reach a fitness plateau and evolve on nearly neutral landscapes (Ohta 1992). Nonetheless, these studies fall short of explaining why inefficient enzymes having stronger control do not evolve higher activities (Yi and Dean 2019). In these models as in most, an enzyme’s efficiency is captured by its activity, generally represented by a composite of kcat,KM and enzyme concentration (Hartl et al. 1985; Clark 1991; Chou et al. 2014; Kaltenbach and Tokuriki 2014), such that the distinct evolutionary dynamics of these parameters, together with an enzyme’s concentration, is ignored. This reduction of an enzyme’s dimensionality goes against the empirical observation that each dimension may have a differential impact on fitness in the context of antibiotic resistance (Walkiewicz et al. 2012; Stiffler et al. 2015; Rodrigues et al. 2016) and that each is thus necessary to predict evolutionary outcomes (Walkiewicz et al. 2012).

Perhaps more importantly, Heinrich et al. (1991) and Schuster et al. (2008) have pointed out that these modeling frameworks assume a constant value for either or both concentrations of the first substrate and of the final product (Orth et al. 2010), whereas evolution should instead maximize the amount of final products generated. Klipp and Heinrich (1994) found that the aforementioned concentrations indeed have a major influence on optimal rate constants under certain assumptions. Likewise, nutrient uptake is most often not considered explicitly in existing models of enzyme evolution, while it is obviously critical in the competition for resources (Dykhuizen and Dean 1994).

Nutrient uptake occurs when metabolites move inwards across cell membranes; it may rely on membrane permeability only (passive diffusion) or involve channels and carrier proteins, be they transporters or cotransporters (Stein 1986a). Here, we build a model that explicitly includes passive (PD hereafter) or facilitated diffusion (FD) followed by an unbranched metabolic pathway to study how resource availability coupled to transport modulates the evolution of enzymes along the pathway. In ecological scenarios where individuals compete for resources, natural selection should favor genotypes that maximize the net intake of molecules and their transformation, which are linked under both PD and FD.

Based on this premise, we confirm that the evolution of enzyme kinetic parameters _k__f_ and kcat takes place on cliff-like fitness landscapes where a fitness plateau covers a wide part of the relevant parameter space. Kinetic parameters have codependent but distinct evolutionary dynamics—and thus distinct sensitivities to certain parameters of the model—such that the shape of the plateau can be modulated by changing parameters of the model within realistic ranges. We show that this fitness landscape depends on features of transporters that initiate a metabolic pathway, along with parameters that vary among enzymes within a pathway, like the tolerance to high concentrations of intermediate metabolites or the reversibility of reactions.

We further demonstrate, using a simple population genetics model, that the evolutionarily expected features of an enzyme should be predictable, even though enzymes evolve near-neutrally on the fitness plateau. This is because the model includes slightly biased mutations that tend to produce a majority of less efficient enzymes. We thus postulate that the wide variety of enzyme features reported might be explained in a large part by differences in the shape of their fitness landscapes. While testing this hypothesis will require extensive information about individual enzymes, we made a small step in this direction, showing that enzymes involved in metabolic pathways with different types of transporters exhibit differences that our model qualitatively predicts.

## Results
### Passive Diffusion is Generally Inadequate to Sustain Cell Metabolism
In the version of our model in which intake relies on passive diffusion (PD), the net uptake of a nutrient is a direct outcome of its concentration gradient, and therefore of how efficiently the first enzyme catalyzes its transformation inside the cell. Assuming that fitness is proportional to the flux of product of this reaction, we find that the fitness landscape has a cliff-like shape with fitness increasing steeply as parameters kcat and _k__f_ increase (see [Supplementary materials](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), section Text S1). The precise shape will not be commented in detail here, for it is very similar to landscapes obtained under facilitated diffusion (FD, treated in the rest of this manuscript).

Importantly, our results indicate that PD can only sustain a small part of the metabolism of most living cells given cell permeabilities reported in the literature (Wood et al. 1968; Milo et al. 2010), suggesting that this process may not be a determining factor in the evolution of enzymes along metabolic pathways. Indeed, even extremely efficient enzymes, harboring values of kcat and kcat/KM close to their physical limits, yield low inward fluxes that approach 10−2mM.s−1 when considering a spherical cell with a diameter D=1μm⁠. To get a sense of how low these fluxes are, we calculated the maximum cell size they can theoretically sustain. Considering that basal metabolic demands are approximately proportional to the cell volume and using estimates by Lynch and Marinov (2015) for this relationship, we predicted the maximum size enabled by sugar passive diffusion (see Materials and Methods section). Setting a (conservatively high) medium concentration in glucose [G]=1M yields a theoretical volume ceiling Vest=0.84μm3⁠.

Nearly all eukaryotes, and most prokaryotes are _de facto_ larger than this threshold (Heim et al. 2017), which might help explain the apparent ubiquity of FD. While this demonstration hinges on numbers for sugar uptake, which may arguably be the task requiring the highest flux, PD may be limiting for many other metabolites (Boer et al. 2010), depending on their permeability and availability in the environment: even for very high amino-acids concentrations that may only be met in multicellular organisms (Schmidt et al. 2016) and assuming the highest observed permeability for such metabolites (Chakrabarti 1994), these levels are orders of magnitude lower than with FD (see [Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)—section Text S1 for PD results).

### General Shape of the Fitness Landscape under Facilitated Diffusion
For most metabolites, FD relies on the specific binding of the substrate to transmembrane carrier proteins (transporters hereafter), followed by its translocation to the other side of the membrane (Danielli 1954; Kotyk 1967; Stein 1986b). Our model builds on ter Kuile and Cook (1994)’s approach to model FD, considering the simplifying assumption of symmetric transport. Within this framework, FD operates on the concentration gradient (Bosdriesz et al. 2018) and is susceptible to saturation, represented by constant _K__T__—_similar to _K__M_ in the Michaelis–Menten equation—and an interaction constant _α_ (see Materials and Methods section for details). We assessed how this saturation phenomenon influences the selection pressure acting on forward enzyme kinetic parameters (_k__f_ and kcat⁠) under various scenarios.

In order to depict a fitness landscape representative of an average enzyme, we first consider a situation where transporters induce a moderately low rate _V__Tm_ and saturate with a relatively high affinity—corresponding to a low _K__T_ (fig. 1). In this situation, the inward flux at steady-state (which, as argued in the introduction, can be considered representative of fitness) forms a plateau when the upstream enzyme in the metabolic pathway has high kcat and _k__f_. This low equilibrium flux elasticity coincides with the saturation theory (Wright 1934; Kacser and Burns 1973; Hartl et al. 1985; Dykhuizen et al. 1987; Dean 1995; Yi and Dean 2019), especially with its version incorporating facilitated diffusion (ter Kuile and Cook 1994; Dean 1995). The flux plateau is delineated by parallel isoclines (solid and interrupted lines in fig. 1) oriented in the bottom-right direction of the landscape for intermediate values of kcat and _k__f_, such that decreasing _k__f_ by one order of magnitude can be compensated by a similar increase in kcat⁠. While this mutual dependency holds even for high _k__f_ values as long as kcat is not critically low (i.e., when kcat>10−3⁠), it stops when kcat≥103⁠, where increasing kcat no longer improves fitness. Besides, the influence of kcat and _k__f_ is not strictly equivalent, since the increase in flux is more gradual in response to _k__f_.

Fig. 1

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709301096911-caacb8dc-dff8-456a-b0f9-641f49d0c88b.jpeg)

The flux of product following substrate uptake by transporters and conversion by a dedicated enzyme depends on kinetic parameters _k__f_ and kcat⁠. This landscape is based on a moderately low flux at saturation VTm=1μM.s−1 close to those measured for amino acids and nucleosides in E. _coli_ (Zampieri et al. 2019). We also set the transport saturation ratio [Sout]/KT to 10 such that the FD process approaches saturation, and relatively high transporter affinity KT=50μM⁠, also in line with estimates for nucleosides (Griffith and Jarvis 1996; Xie et al. 2004). Other parameter values include kr=103s−1 and [Etot]=1mM⁠. The color gradient indicates the absolute and normalized (with a maximum flux of 1) values of equilibrium flux.

Furthermore, and contrary to the textbook picture whereby most biological reactions are not limited by diffusion at all (Bar-Even et al. 2011; Sweetlove and Fernie 2018), increasing an enzyme’s association rate _k__f_—be it through its diffusivity or its binding rate—may still enhance the equilibrium flux when diffusion is substantially faster than catalysis.

### Properties of Facilitated Diffusion Modulate the Landscape
To explore the effect of FD kinetics on the evolution of enzymes in the metabolic pathway, we studied the influence of _K__T__—_the affinity of the transporter for the substrate—and _V__Tm__—_the maximum transport rate—still assuming that the substrate is close to saturation (⁠[Sout]/KT=10⁠). We find that increasing the transport flux _V__Tm_ exerts a positive selection pressure on kinetic parameters for the upstream enzyme (i.e., for increasing kcat and _k__f_). The plateau is shifted accordingly (see fig. 2A), towards the top-right corner of the landscape, at a distance that corresponds to the magnitude of the change in _V__Tm_. Increasing the affinity of the transporter (i.e., decreasing _K__T_), however, selects for higher _k__f_ (the isoclines are displaced to the right and the fold change is similar to that of _K__T_) but has no other visible influence on kcat than increasing its codependency with _k__f_, a result that holds regardless of the flux at saturation _V__Tm_ (notice that we only considered high _V__Tm_s, larger than in the average case, because these cases are more likely to be under directional selection).

Fig. 2

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709301096911-3e6ec69f-8558-4938-aa17-6952c3a97040.jpeg)

Features of a transporter have an impact on the flux landscape for upstream enzymes, as shown by the 0.9 isoclines—above which the relative flux is >90% – that delineate the fitness plateau for each set of parameter. (_A_) low (⁠KT=0.1M⁠) and high (⁠10μM⁠) transporter affinities are considered, in combination with low (⁠VTm=10−6M⁠), moderate (⁠10−4.5M⁠) or high maximum flux (⁠10−3M⁠). Increasing _K__T_ extends the plateau only towards the left part of the landscape, allowing enzymes with lower _k__f_ on the plateau, whereas decreasing _V__Tm_ extends the plateau in both directions. (_B_) the shape of the fitness plateau is however little dependent on the saturation of the transporter, for a transporter with moderate flux (⁠VTm=10−4.5M.s−1⁠; the effect is identical for higher _V__Tm_, see [supplementary fig. S2](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). Other parameter values: kr=1000/s,[Etot]=1mM and [Senv]=10×KT⁠.

This specific effect on the affinity of the upstream enzyme is likely due to a competition between the transporter—which can transport the substrate in both directions—and the enzyme, which harvests the substrate at a rate that depends on the dissociation constant KD=kr/kf⁠. It should be noted that nutrients under lower demands—for example, amino acids—are generally less concentrated in the environment, often coinciding with a higher affinity of their transporter. Therefore, the possible combinations of flux and affinity likely occupy a restricted space of possibilities where flux and affinity are negatively linked (Gudelj et al. 2010; Bosdriesz et al. 2018), which as can be seen in [supplementary figure S3](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)_A, E_, and _I_ results in landscapes that mainly differ by the minimum value of kcat on the plateau. In figure 2A, we have considered ranges of empirical estimates for sugars (high flux with low to moderate affinity) (Stein 1986b; Maier et al. 2002), nucleosides (Griffith and Jarvis 1996) and amino acids (Stein 1986b; Zampieri et al. 2019) (weak to moderate flux with moderate to high affinity), which indeed mainly correspond to these combinations.

So far, we have considered transporters saturated by high external substrate concentrations. Relaxing this assumption has little impact on the fitness landscape, except that very low values of kcat (lower than 10−2 in fig. 2B) can only sustain the low influx of transporters far from saturation, but fail to keep up with higher influxes in richer environments.

### Enzymes Differ among Metabolic Pathways
We then superimposed empirical estimates of kinetic parameters over our theoretical fitness landscapes, after substituting parameter _k__f_ for its usual empirical counterpart, kcat/KM⁠. Because kcat/KM=kfkcat/(kr+kcat)⁠, this approximation only holds when kcat≫kr⁠. Representing the fitness landscape in this parameter space sets an inaccessible area in the bottomright part of the landscapes where _k__f_ would exceed the diffusion limit (gray area on fig. 3). For purposes of inclusiveness, we used kr=102s−1 by default—noting that this limit would be displaced upwards for larger _k__r_ (and downwards otherwise).

Fig. 3

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709301096940-775a98ef-322f-4bcd-9e9e-ce485df14d55.jpeg)

In vitro experimental estimates of kinetic parameters kcat and kcat/KM exhibit different distributions for enzymes involved in different categories of pathways—as identified by Bar-Even _et al._ (2011)—namely (AFN): amino acids, fatty acids, and nucleotides and (CE): carbohydrates and energy. Corresponding fitness landscapes—differing by transporter features—are superimposed, with the parameter space narrowed down due to the diffusion limit (grey area, set for kr=102s−1⁠). The isoclines shown correspond to parameter values typical of sugar transporters (⁠KT=5mM,VTm=1mM.s−1⁠, in red) (Maier et al. 2002) or amino acids transporters (same as in fig. 1, in black).

We otherwise used sets of parameters that correspond to typical features of sugar and amino acid/nucleoside transporters to obtain fig. 3. Because we have previously shown that changing the affinity or maximum flux of transporters may move the fitness plateau, our model predicts that enzymes involved in the corresponding pathways (e.g., of sugars and amino acids) should have their own specific distributions. We see that enzymes involved in the central carbohydrate metabolism as categorized by Bar-Even et al. (2011) have on average higher kcat and KM than those metabolizing amino-acids and nucleotides. Our superimposition with the predicted fitness plateaus in figure 3 suggests that there may indeed be an explainable difference between enzymes contributing to carbohydrate processing (in red) and to that of other primary metabolites (in black, e.g., amino acids). We acknowledge that this result implicitly suggests that enzymes within a pathway have evolved on a common fitness landscape, spreading neutrally onto the fitness plateau. This is by no means our interpretation, as this subset of the full data set includes enzymes that differ in many other ways that, as we will see, make each enzyme evolve on its own fitness landscape and thereby potentially explain a large part of this observed variance.

### Downstream Enzymes also Evolve on Cliff-like Fitness Landscapes
One of the factors that make enzymes different along a pathway is their position, such that the fitness landscape in figure 1 may only hold for the most upstream enzyme in a pathway. Indeed, because the flux of the first product in a pathway increases with the substrate gradient across the cell membrane, the upstream enzyme of a given metabolic pathway is selected for efficiency as described above. In contrast, this selection pressure does not apply directly downstream; at steady-state, even inefficient enzymes can in principle process newly formed substrate molecules at an elevated rate, assuming that the concentration of the substrate is allowed to reach any steady-state value. This is an obviously unreasonable assumption, since a part of this standing substrate should be lost by outward diffusion or degradation (Jones et al. 2015; Bosdriesz et al. 2018). The loss of fitness may therefore result from the loss of metabolites in a way that can be modeled by a constant degradation rate _η__d_ (Chou et al. 2014) (assuming that the external environment is infinite, the degradation term can as well represent an efflux). Highly concentrated metabolites may also be involved in widespread nonspecific (Keller et al. 2015) or promiscuous interactions (Khersonsky and Tawfik 2010; Schäuble et al. 2013; Peracchi 2018) that may interfere with other cellular processes; this is well captured by the linear cost as nonspecific interactions should follow Michaelis–Menten kinetics albeit with much lower affinities, hence following an approximately linear relationship up to very high cellular concentrations (see Materials and Methods section for more details). However, for some reactions the accumulation of metabolites may result in the production of toxic compounds (Lilja and Johnson 2017; Niehaus and Hillmann 2020), hence triggering toxicity best modeled as a nonlinear fitness cost (Clark 1991; Wright and Rausher 2010).

We first consider a “perfect,” highly concentrated upstream enzyme (⁠kf=1010M−1s−1,kcat=106s−1,kr=103s−1,[Etot]=10−3M⁠) and focus on the second enzyme in the pathway, showing that it evolves on a fitness landscape that has a similar shape than described above, still hitting a plateau (fig. 4, with the same parameterization as fig. 1). The degradation rate creates a ceiling for the concentration of the product of the first reaction, such that reducing _η__d_ allows for higher concentrations (see [supplementary fig. S4](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online) and makes the flux tolerant to second enzymes with lower _k__f_s, whereas selection on kcat is barely impacted by this parameter. The plateau is therefore extended to the left when high product concentrations are enabled at low _η__d_ (see fig. 4B). The shape of the plateau is little impacted by changes in the efficiency of the first enzyme, especially when it stands on the plateau. These results are almost independent of the transporter initiating the pathway (see [supplementary fig. S6](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for the case of moderate affinity, high flux transporters).

Fig. 4

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709301096887-5e70750c-8947-459b-a9f8-db3d4b9ca3fe.jpeg)

Downstream enzymes exhibit similar fitness landscapes as those upstream, with a dependency to degradation parameter _η__d_. (_A_) A high degradation rate (⁠ηd=10−2/s⁠) results in a fitness plateau for the second enzyme very similar to that of the first enzyme; in the case presented the first enzyme is considered “perfect” in order to draw the fitness landscape of the second enzyme (⁠kf=1010M−1.s−1,kcat=106s−1,kr=103s−1,[Etot]=1mM⁠). (_B_) decreasing the degradation rate allows less efficient enzymes (with lower kcat or _k__f_) to reach the fitness plateau. Considering the first enzyme to be inefficient (⁠kf=102M−1.s−1,kcat=10−2s−1,kr=103s−1⁠) instead of perfect marginally changes the fitness landscape by making organisms tolerant to extremely low kcat⁠. Other parameter values are identical to fig. 1 (findings are relatively similar for sugar-like transporters, as reported in [supplementary fig. S6](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online).

The shape of the negative relationship between metabolite concentration and fitness can be important ([supplementary figs. S7–S9](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online), as it can make the fitness landscape of an enzyme dependent on the overall flux of the metabolic pathway, and therefore on other enzymes in the pathway. Indeed, low general fluxes (as modeled by an inefficient first enzyme in [supplementary figs. S7 and S8](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online) make the metabolite concentration below its toxicity threshold, therefore making organisms tolerant to enzymes with lower _k__f_ and kcat⁠. Taken together, these results show that the precise epistatic relationship between enzymes in a pathway will depend on the exact cost function applied, with a linear cost generating epistasis for kcat only and a nonlinear cost possibly impacting both _k__f_ and kcat⁠.

### The Reversibility of Reactions also Matters
Reversibility is an intrinsic feature of chemical reactions that cannot be directly overcome by Evolution (Haldane 1930; Cornish-Bowden 1979). A highly reversible reaction corresponds to a large intrinsic equilibrium constant Keq=[S]eq/[P]eq (Klipp and Heinrich 1994), and results in higher backward than forward rates in the following chemical equation: 

where _k_inh represents the rate at which enzyme and product combine back. Such a (reversible) reaction could in principle influence the selective pressure acting on the following enzyme in the pathway, for both enzymes compete to process the same metabolite _P_1. We thus quantified how reversibility affects the evolution of an enzyme downstream ([supplementary figs. S10 and S11](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online).

The equilibrium constant _K_eq has a similar (nonlinear) impact on the fitness landscape of the second enzyme to that of the degradation rate, with a highly reversible upstream enzyme exerting a selection pressure downstream towards an increase of kinetic parameters ([supplementary fig. S10A](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). Indeed, increasing _K_eq moves the fitness plateau toward the upper-right corner in the (_k__f_, kcat⁠) parameter space, hence selecting for more efficient downstream enzymes. The effect appears linear, except for very low values of _K_eq where metabolite accumulation exerts a dominant role in shaping the fitness landscape (through the degradation rate _η__d_, set to a low residual value). Therefore, the reversibility of the upstream reaction appears like a critical parameter for the evolution of an enzyme.

### Evolutionary Dynamics of Enzyme Kinetic Parameters
How much variance in evolutionary outcomes these differences in fitness landscapes may explain is contingent on the interplay between selection, mutation, and drift. Small differences in an isocline position should indeed be of little importance if populations perform random walks on the fitness plateau, for instance. To approach how populations evolve on our mathematically derived fitness landscapes, we built a simple population genetics model in which absolute fitness is directly proportional to the flux arising from the first enzyme at steady-state—which itself equals the net inward flux of nutrients. Two different levels of metabolic demands were considered, corresponding to parameter values of amino acids/nucleosides and sugar transporters ([supplementary fig. S3A](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) and I, [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). In this instance of the model, only kcat and _k__f_ were susceptible to evolve through mutations. Mutational effects on log10kcat and log10kf were drawn from independent normal distributions with mean b≤0⁠, and the absolute value of _b_ setting the intensity of a mutational bias towards less efficient parameter values, as has been widely documented in many contexts (Eyre-Walker and Keightley 2007; Serohijos et al. 2012; Heckmann et al. 2018). The standard deviation of the distribution of mutational effects equals 0.3 such that most mutations explore the neighboring parameter space, seldom changing a parameter by more than one order of magnitude (one log10 unit) in compliance with empirical estimates (Carlin et al. 2016). Since the relation between kinetic parameters may be constrained—for example, due to shared properties of the energy profile of a reaction—we tested the influence of negative and positive relationships using bivariate normal distributions, with three different values of _ρ_ (see Materials and Methods section for details).

In the absence of mutational bias (_b _=0), simulated enzymes spread over the fitness plateau, as expected ([supplementary fig. S16A](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for low flux, [supplementary fig. S17A](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online otherwise). The onset of the plateau depends on the strength of drift and hence derive from the effective population size _N__e_, following the classical expectation that selection becomes inefficient when Ne×s<1 (Wright 1931; Kimura 1968). Introducing a mutational bias that makes enzyme kinetics less efficient on average has a strong effect on both kcat and _k__f_, preventing simulated enzymes from improving far above the drift barrier (fig. 5A for low flux, fig. 5B otherwise). Even weak biases (⁠b=−0.1⁠) lead to enzymes evolving in the vicinity of the isocline where Ne×s≈1⁠. Increasing the strength of this bias to 0.2 only slightly decreases the population variance around this expectation. Finally, mutational correlations do not impact much the distribution of evolutionary outcomes ([supplementary fig. S18](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online).

Fig. 5

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709301096883-740645b7-1be3-4270-a3c9-8aa87b0d29be.jpeg)

Population genetic simulations predict that enzymes should reach a predictable set of features when mutation biases towards lower efficiencies are considered (see [supplementary fig. S17](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for the case of an absence of bias). Indeed, the mutation selection drift equilibrium establishes close to an isocline indicative of effective selection that depends on the effective population size _N__e_. The cases considered here are that of a transporter with a low flux at saturation and high affinity (_A_; VTm=1μMs−1 and KT=10μM⁠) and one with a high flux at saturation but low affinity (_B_; VTm=1mMs−1 and KT=100mM⁠) with effective population sizes ranging from 102 to 105 (different colors) and two strengths of the mutational bias (the absence of mutational bias was also considered, see [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). Each of 30 independent simulations for each scenario is represented a dot in the “empirical” parameter space (⁠kcat,kcat/KM⁠), but only kcat and _k__f_ were susceptible to evolve. _k__r_ is set to 103s−1 such that the grey part of the parameter space is inaccessible to enzymes that would otherwise exceed the diffusion limit.

Our results suggest a strong effect of the effective population size on enzyme evolution, such that species with _N__e_ above 105 (Bobay and Ochman 2018, most unicellular organisms) should express extremely efficient enzymes. This appears to not be the case, as for instance Eukaryotes and Prokaryotes display similar enzymes despite large differences in effective population sizes (Bar-Even et al. 2011). As we will later discuss, this conundrum might resolve when considering the smaller size of organisms forming larger populations, making them more sensitive to noise in gene expression and favoring higher concentrations. Notwithstanding this issue, the prediction of enzymes evolving a predictable set of kinetic parameters strongly suggests that a large part of the broad variance in enzyme features is due to differences in the selective context experienced by each, thereupon requiring further investigation on the dependency of the position of the fitness plateau to parameters of our model.

### The Joint Evolution of Enzyme Concentrations and Kinetic Parameters
Hitherto, we have considered enzymes to be highly concentrated, an assumption that we now relax since it is an important component of the presumed kinetic activity (Koshland 2002). Predictably, increasing the concentration of the first or second enzyme in a pathway releases the selection on their kinetic parameters (Noor et al. 2016), producing larger fitness plateaus as an enzyme concentration increases (see [supplementary figs. S12B and S13B](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for this influence in different contexts). Due to the compensatory effects between concentration and activity, we anticipate that the joint evolutionary dynamics of the concentration and kinetic parameters should yield a negative correlation between them, as reported by Davidi _et al._ (2016, 2018).

Despite their common role on reaction efficiency, enzyme concentration expectedly responds to very different selection pressures than kinetic parameters, as increased gene expression levels come with costs (Wagner 2005; Lang et al. 2009; Scott et al. 2010; Noor et al. 2016; Kafri et al. 2016). Indeed, producing extra proteins requires both energy and matter (Novick and Weiner 1957; Stoebel et al. 2008; Wagner 2005; Lynch and Marinov 2015) and may impede the efficiency of physical processes that rely on an optimal intermediate content (Dong et al. 1995; Dill et al. 2011; Andrews 2020). We designed a new instance of our population genetics model to study the tangled evolution of kinetic constants and enzyme concentration, introducing two of these costs: 1) the cost of producing proteins _c_, considered to be proportional to concentration (Wagner 2005; Chou et al. 2014; Lynch and Marinov 2015) and 2) the exponential cost of an increase in macromolecular crowding, which hinders diffusion and thus slows down reactions (Dill et al. 2011; Schavemaker et al. 2018; Andrews 2020) (see [supplementary fig. S15](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for the resulting fitness landscapes of enzyme concentration).

The two types of costs result in a different shape of the fitness landscape, with the noticeable difference that evolutionarily expected concentration depends on _N__e_ when the cost of production is considered ([supplementary fig. S19](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online) but not with crowding effects ([supplementary fig. S20](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). With a combination of the two costs, enzyme concentrations decrease with _N__e_ and production costs, resulting in the evolution of higher kinetic constants (fig. 6). This is because at higher effective sizes, direct costs of protein production are large enough to incur effective selection for lower protein expression. This is no longer the case when _N__e_ decreases, such that the major force driving the optimization of enzyme concentration becomes that opposing macromolecular crowding, which is less sensitive to _N__e_ (as shown in [supplementary fig. S19](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online). The balance between these two selective forces, and the dependency to _N__e_, obviously depend on the relative importance of these costs ([supplementary fig. S20](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online), itself depending on many parameters (protein length, molecular weight, etc.) that should only make enzymes marginally different within a given species (when their activity evolves on similar fitness landscapes).

Fig. 6

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/jpeg/22983715/1709301103530-57d680d7-7f4d-4036-9434-41b7b189c1ae.jpeg)

Simulations of the joint evolution of enzyme concentration and kinetic parameters, with a 2-fold cost of enzyme overexpression (the direct metabolic cost and the indirect cost of cell packing). The case considered here is that of a transporter with a high flux at saturation and low affinity (⁠VTm=1mMs−1 and KT=1mM⁠) under a high mutational bias on kinetic constants (⁠b=−0.2⁠). Two different costs of protein production _c_ are considered along with four effective population sizes ranging from 102 to 105. We ran 30 independent simulations for each scenario, each represented by a dot in the “empirical” parameter space as described in fig. 5.

## Discussion
Most enzymes have been considered to be only moderately efficient (Bar-Even et al. 2011), if not sloppy (Bar-Even et al. 2015). This claim was put into perspective by Newton et al. (2018) who argued that the link between fitness and enzyme efficiencies is complex and may be partly enzyme dependent, such that all enzymes may not evolve on a common fitness landscape. Through this work, we have developed a model where enzyme efficiencies are mechanistically linked to fitness through the impact of nutrient gradients on the production of metabolites. Our results emphasize that an enzyme’s fitness landscape—and the resulting mutation–selection–drift balance—may indeed be largely context dependent, possibly explaining a large part of the extreme observed variance in enzyme features.

At first sight, all enzymes evolve on fitness landscapes that have the same general shape, with a fitness plateau surrounded by a steep slope. While this shape is usual in models of enzyme evolution (Hartl et al. 1985; Kaltenbach and Tokuriki 2014; Yi and Dean 2019), in our model the landscape is drawn in the parameter space formed by the two forward kinetic parameters kcat and _k__f_, instead of a composite “efficiency” whose relevance is questionable (Koshland 2002; Eisenthal et al. 2007). Our model allows to predict the precise position of the fitness plateau in various contexts, showing that model parameters may have a selective impact on _k__f_, kcat⁠, or both, thereby confirming the relevance of considering their distinct evolutionary dynamics.

We have shown that the exact position of the plateau is important through a population genetics model including mutational biases that produce less efficient enzymes at a slightly higher frequency. Despite their small effect, these biases are sufficient to have a significant impact on the evolutionary dynamics occurring on the fitness plateau, preventing enzymes to explore the parameter space far away from an isocline whose precise value can be predicted. Because the mutation–selection–drift balance occupies a narrow part of the landscape, this makes the evolution of an enzyme, in principle, highly predictable. Likewise, we anticipate that differences between enzymes should largely be explained by differences in the shapes of their individual fitness landscapes.

Overall, the selective pressure acting on an enzyme results from an interplay between several biochemical factors. We have effectively found that the shape of the fitness landscape is first governed by features of the transporter initiating a pathway, especially the maximum flux they can sustain. Using parameters that correspond to empirical estimates for sugars and amino acids/nucleosides, we have found that enzymes contributing to subsequent metabolic pathways should be different, with those in the “sugars” pathway being selected for faster kinetics.

While sharing a common transporter, enzymes along a pathway are also subject to a variety of local chemical contexts, making each evolve on its own unique fitness landscape. This could explain, at least in part, the large within-pathway variance of enzyme kinetic parameters. Physical constraints may for instance act differentially on different enzymes, as exemplified by the intrinsic reversibility of a reaction that fuels the selective pressure towards higher efficiency in downstream enzymes. This may contribute to explain the high efficiency of a few enzymes like TIM (Williamson et al. 1967; Davidi et al. 2018).

One way to compensate for low kinetic constants is to enhance the level of expression of an enzyme, as confirmed by our model—concentration indeed has a strong influence on the fitness landscape of _k__f_ and kcat⁠. Nonetheless, concentration and kinetic parameters face very distinct selection regimes: while the latter are both under directional selection, vanishing at high efficiencies, concentration is under stabilizing selection—owing to a combination between its positive impact on the flux and the adverse costs to high expression—as already pinpointed by Chou et al. (2014). Their joint evolution is complex because the position of the concentration optimum depends on an enzyme’s kinetic constants, whose fitness landscape itself depends on concentration. This results in a slightly increased variance in enzyme efficiencies compared to simulations with fixed concentrations, along with a complex relationship with genetic drift, because smaller populations tend to tolerate higher enzyme concentrations and, therefore, evolve less efficient enzymes.

It should be noted that our model does not consider another selection pressure on enzyme concentrations that arises from noise in gene expression, as argued by Wang and Zhang (2011). Indeed, low expression results in detrimental noise that should be avoided by pushing enzyme concentrations towards higher values in small organisms like Prokaryotes (see [supplementary Text S6](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary Material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for an estimate of this effect). This could result in a different relationship between _N__e_ and enzyme efficiencies than considered here, possibly explaining the confusing observation that species with larger populations (and smaller sizes) do not express markedly more efficient catalysts. Furthermore, an enzyme’s effective concentration can also increase through compartmentalization (Ovádi and Saks 2004; Diekmann and Pereira-Leal 2013; Cornejo et al. 2014) and substrate channeling (Welch and Easterby 1994; Huang et al. 2001; Sweetlove and Fernie 2018), within the limits imposed by noise, and modify the selective pressure acting on kinetic parameters.

This illustrates that rather than making precise predictions, our study aims at making the strong claim that selection acting on enzyme features is important for their diversity, possibly largely overcoming the diversity arising from neutral processes. If this is indeed the case, trends in enzyme evolution can be predicted—as it was shown empirically in the context of antibiotic resistance (Walkiewicz et al. 2012)—and further improvements of this model should allow one to predict the expected features of individual enzymes. Such improvements are made easier by the use of a mechanistic framework, where fitness arises as enzymatic efficiency helps ingesting nutrients and win the competition for resources. This framework could even be enriched by other dimensions relevant to the genotype-phenotype-fitness map (Bershtein et al. 2017; Echave 2019; Kinsler et al. 2020).

Unfortunately, mechanistic does not mean free of a definition of fitness, as we have here assumed that the latter is proportional to metabolic flux, hence considering each flux in isolation. Fitness instead results from a wide range of metabolic pathways that combine together and should all be competitive to certain degrees. How global epistasis builds up (Weinreich et al. 2013; Otwinowski et al. 2018; Reddy and Desai 2021), and genetic drift acts in this context, is far from obvious (Iwasa et al. 2004; Weinreich and Chao 2005; Weissman et al. 2009). But this should not impact much how enzymes evolve in old, overall efficient pathways, as any impediment in efficiency should have a relatively independent effect on fitness in this context, as captured by our model. Understanding these complex interactions between pathways would nevertheless be crucial to understand how metabolic pathways arose and improved, likely from a highly inefficient state during early steps in the evolution of life on Earth (Kacser and Beeby 1984; Schmidt et al. 2003; Heckmann et al. 2018).

## Materials and Methods
### Quantifying the Maximum Size for Cells Using Passive Diffusion
If a cell is to be viable, it has, at least, to uptake enough glucose to compensate for basal metabolism—metabolism that allows to maintain the same cell size for nonactively growing cells (Lynch and Marinov 2015)—leading to the following equation: ϕPD=CM⁠, with ϕPD the uptake through passive diffusion and _C__M_ the basal metabolism demand. To calculate the maximum size a cell can reach using only passive diffusion, we relied on the formula CM=0.39V0.88(109ATP/hr) estimated in (Lynch and Marinov 2015). We also assumed the cell to be of spherical shape, both concentrations—inside and outside the cell—to be constant with the cellular concentration staying so low that it can be overlooked, meaning that the uptake resulting from passive diffusion can merely be written as ϕPD=P.[Sout].SAsphereVsphere⁠, where SAsphere and Vsphere are the surface area and the volume of a sphere, and _P_ represents the cell permeability and was measured to 10−6μm−1 (Wood et al. 1968) for glucose. Finally, we considered that each glucose yields 30 ATP molecules (Rich 2003).

### Flux Sustained by the First Enzyme
When assessing the flux of product made by the first enzyme in a pathway, both (PD) and (FD) result in similar sets of equations; we focus on FD here (see [supplementary Text S5](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) - Mathematical appendix, [Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for a comparison with PD). FD typically relies on the specific binding of substrate molecules—located outside the cell—by transmembrane carrier proteins, followed by their translocation into the cytoplasm (Danielli 1954; Wilbrandt and Rosenberg 1961; Kotyk 1967; Bosdriesz et al. 2018). This specific process obeys Michaelis–Menten-like kinetics when transport is assumed to be symmetric (Kotyk 1967), which can be modeled through Brigg–Haldane equations (Briggs and Haldane 1925; Haldane 1930; Stein 1986b): 

d[Sin]dt=VTm.[Sout]−[Sin]KT+([Sout]+[Sin])+α.[Sout][Sin]KT

(4)

with: 

{VTm:themaximumrateofagivencarrierprotein;KT:aconstantinverselyproportionaltothetransporterefficiency;α:theKotykinteractiveconstantcapturingthedisequilibrium between boundand free transporters.

By construction, _α_ cannot exceed 1 Kotyk (1967) and is close to this upper limit for sugars (e.g., α=0.91 for glucose (Teusink et al. 1998), so we set _α _= 1 by default in this study, maximizing the effect of interaction).

A model including both FD and irreversible substrate conversion by an enzyme therefore corresponds to the following chemical equation: 

Sout⇌αVTm,KTSin+E⇌krkfES→kcatE+P

(5)

### Multiple Enzymes Model
In order to study the evolution of downstream enzymes, we considered an unbranched metabolic pathway in which the product formed by the first reaction serves as the substrate for a second reaction whose flux determines fitness. Theoretically, as there is nothing prohibiting increase in product concentrations—for it is not considered reversible at this point—any second enzyme should be able to sustain any metabolic demand. We penalized large increases in cellular concentrations through a degradation process of the product of the first reaction, occurring at rate _η__d_ (× this concentration). The chemical reactions occurring after uptake (Michaelis Menten part of [equation 5](https://academic.oup.com/mbe/article/38/9/3938/6272522?login=false#E6)) are described by the following equations: 

Sin+E1⇌kr1kf1E1S→kcat1E1+P1

(10)

P1+E2⇌kr2kf2E2P1→kcat2E2+P2 ↓ηd  P1out

(11)

Such a system may reach a steady-state at which the cellular concentrations of the substrate _S__in_ and of the first product _P_1 are constant. At this point, the net instantaneous uptake of substrate equals the instantaneous production of _P_1 which, in turn, equals the sum of the instantaneous amount of degraded _P_1 and the instantaneous production of _P_2, according to the principle of mass conservation. It yields the following system of equations: 

VTm.([Sout]−[Sin])KT+([Sout]+[Sin])+α.[Sout][Sin]KT=Vm1.[Sin]KM1+[Sin]

(12)

Vm1.[Sin]KM1+[Sin]=Vm2.[P1]KM2+[P1]+ηd.[P1],

(13)

where appear the traditional Michaelis–Menten kinetic parameters for the (ieth) reaction: 

{Vmi=kcati[Etoti]KMi=kri+kcatikfi.

To test the potential influence of toxicity, we defined the absolute fitness as a function of both the flux and a toxicity factor whose influence is represented through a sigmoid function and reflects the nonlinearity nature of toxic effects (Clark 1991; Wright and Rausher 2010): f=ϕ(1−[P][P]+T)

In an independent section, we also introduced reversibility through the modification of [equation (10)](https://academic.oup.com/mbe/article/38/9/3938/6272522?login=false#E11), which becomes: 

Sin+E1⇌kr1kf1E1S⇌kinh1kcat1E1+P1

(14)

Such a phenomenon is described by the more general form of Haldane equation (Haldane 1930; Cornish-Bowden 1979), which changes the contribution of the first reaction (⁠Vm1.[Sin]KM1+[Sin]⁠) in both [equations (12)](https://academic.oup.com/mbe/article/38/9/3938/6272522?login=false#E13) and [(13)](https://academic.oup.com/mbe/article/38/9/3938/6272522?login=false#E14) to: 

Vm1+.[Sin]KM1++[Sin]+KI[P1]−Vm1−.[P1]KM1−+[P1]+[Sin]/KI

with Vm1+ and KM1+ respectively corresponding to the previous Vm1 and KM1⁠, while: 

{Vm1−=kr1[Etot1]KI=kinh1/kf1KM1−=KM1+/KI.

To solve these systems, we implemented the Newton method (Atkinson 1989) aiming to find [Sin]* and [P1]*⁠. We ran the algorithm starting from very low values of concentration (both set to 10−20M⁠) to determine numerically the equilibrium without facing convergence problems. The final flux can then be determined through the “production” part of [equation (13)](https://academic.oup.com/mbe/article/38/9/3938/6272522?login=false#E14), that is, Vm2.[P1]KM2+[P1]⁠.

### Validation of the Method and Computing of the Fitness Landscapes
To validate the approach, we compared equilibrium results obtained with Raphson–Newton algorithm to those obtained when simulating the process with Euler explicit schemes for a set of (3x3) kinetic values – kcat and _k__f__ -_ encompassing three orders of magnitude (see [supplementary Section Text 5](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for further details).

We then drew fitness landscapes after determining the flux—assumed to be to be linearly related to fitness—achieved for enzyme kinetic parameters kcat and _k__f_ varying by 10 orders of magnitude, setting _k__r_ to 103s−1—within the range found for several enzymes (Klipp and Heinrich 1994; Knowles and Albery 1977)—unless stated otherwise. Except in the section dedicated to the influence of enzyme concentration, we set the enzyme concentration such that [Etot]=1mM⁠, lying nearby the highest observed values (Albe et al. 1990; Noor et al. 2016). Other parameters are detailed on a case-by-case basis as they may change depending on the goal of each section. To compare with the data and visualize results in the experimenter’s parameter space, we also determined the flux and plotted simulation results using kcat and kcatKM⁠, also making them vary by 10 orders of magnitude. We divided the parameter space in 100 log-equidistant values (250 for representations with kcat/KM to obtain a cleaner demarcation for the diffusion limit).

### Population Genetics Model
Evolutionary simulations rely on a Wright–Fisher process including the selective effects of mutations displacing enzymes on mathematically derived fitness landscapes. Two fitness landscapes were considered: weak flux, high affinity ([supplementary fig. S3A](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online) and high flux, low affinity ([supplementary fig. S3I](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online), both with saturated facilitated diffusion (⁠[Sout]=10KT⁠) and the following constant parameters: kr=103s−1 and [Etot]=1mM⁠. Mutations occur at a rate μ=10−1/Ne following reproduction, with an effect sampled in Gaussian distributions with dispersion (⁠σ=0.3⁠). The mean effect of a mutation is given by parameter _b_, hence representing the mutation bias—absent with _b _=0, low (⁠b=−0.1⁠) or high (⁠b=−0.2⁠). Kinetic parameters were initiated to the inefficient values of kcat=10−3s−1 and kf=102M−1s−1 and _k__f_ was limited to values under the diffusion limit—1010M−1s−1 (_k__cat_ was also limited to 106s−1 when _b _=0 to avoid physical outliers). To analyses simulation outcomes, we picked out the kinetic and fitness values of the most represented genotype when multiple variants were segregating. Thirty simulations were ran for each set of parameters. Finally, we verified that evolutionary steady-states were reached and considered it was the case when at least the average fitnesses (over all simulations) of the last three time-steps were not significantly different one from another ([supplementary figs. S5 and S6](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online).

We also simulated the case where mutations between parameters are correlated. We tested both positive and negative mutational relationships through a bivariate Gaussian distribution whose correlation coefficient were set to ρ=−0.8,ρ=−0.5,ρ=+0.5 (see [supplementary fig. 18](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for the results with a moderate flux).

### Evolution of Enzyme Concentrations
Finally, we simulated the joint evolution between kinetic parameters and enzyme concentration, repeating the previous procedure with concentration as an evolvable quantity and the fitness function including deleterious effects of extra gene expression (see [supplementary section Text S5](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA), [Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) online for the effect of each cost considered independently one from another). Mutations affected either levels of expression or kinetic constants, with those affecting levels of expression (in log values) being drawn from Gaussian distributions with mean 0 and σ=0.2 to comply with existing estimates (Landry et al. 2007; Metzger et al. 2016; Hodgins-Davis et al. 2019). Because sugars are directly involved in energy metabolism, we computed these simulations for the case of a high flux which can more readily be linked to the cost of expression.

As explained above, producing extra proteins is costly, both energetically and because it may increase a cell’s crowding. The cost of protein production is considered to be proportional to the steady-state enzyme concentration, with a slope _c_. Empirical estimates suggest that _c_ should be in the range [10−4,10−3] (Wagner 2005; Lynch and Marinov 2015), such that producing an extra mM of a protein would impede the whole energy budget by one 10,000th to one 1,000th (we also consider c=10−5 and 10−2 in the SM). Accordingly, we calculate the absolute fitness f=Φ−[Etot]c⁠, where Φ is the flux generated by the enzyme.

The influence of crowding was computed by penalizing _k__f_ through an effective kf,act=kf.10−([Etot]+[Mb])/[2Mb]⁠, where [Mb]=2.5.10−3M represents the basal protein concentration of a viable cell and also constitutes a scaling factor that complies with Andrews (2020) log-linear influence of crowding or glass transition effects described by Dill et al. (2011).

### Data Availability
The models have been implemented using R. The source code for these models and the simulated data are available from [https://gitlab.in2p3.fr/florian.labourel/ruemee](https://gitlab.in2p3.fr/florian.labourel/ruemee).

All the enzyme data used in this work to compare fitness landscapes and measured values were recovered from (Bar-Even et al. 2011) and so was the classification of reactions with regards to metabolic groups. Thanks to their authors and publisher, data sets are publicly available at [https://pubs.acs.org/doi/10.1021/bi2002289](https://pubs.acs.org/doi/10.1021/bi2002289). Apart from that, no new empirical data were generated in support of this research.

## Supplementary Material
[Supplementary material](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/mbe/38/9/10.1093_molbev_msab132/2/msab132_supplementary_data.zip?Expires=1711515194&Signature=2b84JC8hRrlHzk1WqKw7ul5WDtWTnYT5zE422MJNJintTUiVCBp~ZDQFqhyeRXzobERIsS~P0J87-yNYkjSUc-lJut9b1d590DPyGlfa6EV-k~nAHp3vKvvteUepDq~YRtTiV66f~Oj4eCw7MqdejSoKmdJRaAc7HJbL2AKE2hMIB3cuzrZ~gBKuQOU8lHzelFyTV0Jo98YgpiPFSMzuDJ0Mc282roE2EKoRRT47YFgIzHQ-2O91FvRNy-KUCyo9a65KosRJIrtPZ19UQVEB8HcwSsaPYWtKw3km1yl3eZjCxVybV8NVnW5gG57LDZcQc4xns54PZTN-zfZI6BTClg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) is available at _Molecular Biology and Evolution_ online.

## Acknowledgments
The authors gratefully acknowledge the editor and two anonymous reviewers for their helpful comments.

## References
Albe

KR

, 

Butler

MH

, 

Wright

BE.

1990

. 

Cellular concentrations of enzymes and their substrates

. 

J Theor Biol

. 

143

(

2

):

163

–

195

.

Alberty

RA

, 

Hammes

GG.

1958

. 

Application of the theory of diffusion-controlled reactions to enzyme kinetics

. 

J Phys Chem

. 

62

(

2

):

154

–

159

.

Andrews

SS.

2020

. 

Effects of surfaces and macromolecular crowding on bimolecular reaction rates

. 

Phys Biol

. 

17

(

4

):045001.

Atkinson

K.

1989

. 

An introduction to numerical analysis

. 2nd ed. 

New York

: 

Wiley

.

Bar-Even

A

, 

Noor

E

, 

Savir

Y

, 

Liebermeister

W

, 

Davidi

D

, 

Tawfik

DS

, 

Milo

R.

2011

. 

The moderately efficient enzyme: evolutionary and physicochemical trends shaping enzyme parameters

. 

Biochemistry

50

(

21

):

4402

–

4410

.

Bar-Even

A

, 

Milo

R

, 

Noor

E

, 

Tawfik

DS.

2015

. 

The moderately efficient enzyme: futile encounters and enzyme floppiness

. 

Biochemistry

54

(

32

):

4969

–

4977

.

Bershtein

S

, 

Serohijos

AW

, 

Shakhnovich

EI.

2017

. 

Bridging the physical scales in evolutionary biology: from protein sequence space to fitness of organisms and populations

. 

Curr Opin Struct Biol

. 

42

:

31

–

40

.

Blanco

PM

, 

Garcés

JL

, 

Madurga

S

, 

Mas

F.

2018

. 

Macromolecular diffusion in crowded media beyond the hard-sphere model

. 

Soft Matter

. 

14

(

16

):

3105

–

3114

.

Bloom

J

, 

Wilke

C

, 

Arnold

F

, 

Adami

C.

2004

. 

Stability and the evolvability of function in a model protein

. 

Biophys J

. 

86

(

5

):

2758

–

2764

.

Bloom

JD

, 

Lu

Z

, 

Chen

D

, 

Raval

A

, 

Venturelli

OS

, 

Arnold

FH.

2007

. 

Evolution favors protein mutational robustness in sufficiently large populations

. 

BMC Biol

. 

5

(

1

):

29

.

Bloom

JD

, 

Labthavikul

ST

, 

Otey

CR

, 

Arnold

FH.

2006

. 

Protein stability promotes evolvability

. 

Proc Natl Acad Sci U S A.

103

(

15

):

5869

–

5874

.

Bloom

JD

, 

Silberg

JJ

, 

Wilke

CO

, 

Drummond

DA

, 

Adami

C

, 

Arnold

FH.

2005

. 

Thermodynamic prediction of protein neutrality

. 

Proc Natl Acad Sci U S A

. 

102

(

3

):

606

–

611

.

Bobay

L-M

, 

Ochman

H.

2018

. 

Factors driving effective population size and pan-genome evolution in bacteria

. 

BMC Evol Biol

. 

18

(

1

):

153

.

Boer

VM

, 

Crutchfield

CA

, 

Bradley

PH

, 

Botstein

D

, 

Rabinowitz

JD.

2010

. 

Growth-limiting intracellular metabolites in yeast growing under diverse nutrient limitations

. 

Mol Biol Cell

. 

21

(

1

):

198

–

211

.

Bosdriesz

E

, 

Wortel

MT

, 

Haanstra

JR

, 

Wagner

MJ

, 

de la Torre Cortés

P

, 

Teusink

B.

2018

. 

Low affinity uniporter carrier proteins can increase net substrate uptake rate by reducing efflux

. 

Sci Rep

. 

8

(

1

):

5576

.

Briggs

GE

, 

Haldane

JB.

1925

. 

A note on the kinetics of enzyme action

. 

Biochem J

. 

19

(

2

):

338

–

339

.

Bucciantini

M

, 

Giannoni

E

, 

Chiti

F

, 

Baroni

F

, 

Formigli

L

, 

Zurdo

J

, 

Taddei

N

, 

Ramponi

G

, 

Dobson

CM

, 

Stefani

M.

2002

. 

Inherent toxicity of aggregates implies a common mechanism for protein misfolding diseases

. 

Nature

416

(

6880

):

507

–

511

.

Burns

J

, 

Cornish-Bowden

A

, 

Groen

A

, 

Heinrich

R

, 

Kacser

H

, 

Porteous

J

, 

Rapoport

S

, 

Rapoport

T

, 

Stucki

J

, 

Tager

J

, et al.  

1985

. 

Control analysis of metabolic systems

. 

Trends Biochem Sci

. 

10

(

1

):

16

.

Carlin

DA

, 

Caster

RW

, 

Wang

X

, 

Betzenderfer

SA

, 

Chen

CX

, 

Duong

VM

, 

Ryklansky

CV

, 

Alpekin

A

, 

Beaumont

N

, 

Kapoor

H

, et al. . 

2016

. 

Kinetic Characterization of 100 _Glycoside Hydrolase_ Mutants Enables the Discovery of Structural Features Correlated with Kinetic Constants

. 

PLoS One

. 

11

(

1

):

e0147596

.

Chakrabarti

AC.

1994

. 

Permeability of membranes to amino acids and modified amino acids: mechanisms involved in translocation

. 

Amino Acids

6

(

3

):

213

–

229

.

Chou

H-H

, 

Delaney

NF

, 

Draghi

JA

, 

Marx

CJ.

2014

. 

Mapping the fitness landscape of gene expression uncovers the cause of antagonism and sign epistasis between adaptive mutations

. 

PLoS Genet

. 

10

(

2

):

e1004149

.

Clark

AG.

1991

. 

Mutation-selection balance and metabolic control theory

. 

Genetics

129

(

3

):

909

–

923

.

Cornejo

E

, 

Abreu

N

, 

Komeili

A.

2014

. 

Compartmentalization and organelle formation in bacteria

. 

Curr Opin Cell Biol

. 

26

:

132

–

138

.

Cornish-Bowden

A.

1979

. Fundamentals of Enzyme Kinetics. Chapter 2 - Introduction to enzyme kinetics. Butterworth-Heinemann. 

16

–

38

.

Danielli

J.

1954

. Morphological and molecular aspects of active transport. _Symp Soc Exp Biol_. 

8

:

502

–

516

.

Davidi

D

, 

Longo

LM

, 

Jabłońska

J

, 

Milo

R

, 

Tawfik

DS.

2018

. 

A bird’s-eye view of enzyme evolution: chemical, physicochemical, and physiological considerations

. 

Chem Rev

. 

118

(

18

):

8786

–

8797

.

Davidi

D

, 

Noor

E

, 

Liebermeister

W

, 

Bar-Even

A

, 

Flamholz

A

, 

Tummler

K

, 

Barenholz

U

, 

Goldenfeld

M

, 

Shlomi

T

, 

Milo

R.

2016

. 

Global characterization of in vivo enzyme catalytic rates and their correspondence to in vitro _kcat_ measurements

. 

Proc Natl Acad Sci U S A

. 

113

(

12

):

3401

–

3406

.

Dean

AM.

1995

. 

A molecular investigation of genotype by environment interactions

. 

Genetics

139

(

1

):

19

–

33

.

Dean

AM

, 

Dykhuizen

DE

, 

Hartl

DL.

1986

. 

Fitness as a function of _β_-galactosidase activity in _Escherichia coli_

. 

Genet Res

. 

48

(

1

):

1

–

8

.

Dekel

E

, 

Alon

U.

2005

. 

Optimality and evolutionary tuning of the expression level of a protein

. 

Nature

436

(

7050

):

588

–

592

.

DePristo

MA

, 

Weinreich

DM

, 

Hartl

DL.

2005

. 

Missense meanderings in sequence space: a biophysical view of protein evolution

. 

Nat Rev Genet

. 

6

(

9

):

678

–

687

.

Diekmann

Y

, 

Pereira-Leal

J.

2013

. 

Evolution of intracellular compartmentalization

. 

Biochem J

. 

449

(

2

):

319

–

331

.

Dill

KA

, 

Ghosh

K

, 

Schmit

JD.

2011

. 

Physical limits of cells and proteomes

. 

Proc Natl Acad Sci U S A

. 

108

(

44

):

17876

–

17882

.

Dong

H

, 

Nilsson

L

, 

Kurland

CG.

1995

. 

Gratuitous overexpression of genes in escherichia coli leads to growth inhibition and ribosome destruction

. 

J Bacteriol

. 

177

(

6

):

1497

–

1504

.

Drummond

DA

, 

Wilke

CO.

2008

. 

Mistranslation-induced protein misfolding as a dominant constraint on coding-sequence evolution

. 

Cell

. 

134

(

2

):

341

–

352

.

Drummond

DA

, 

Bloom

JD

, 

Adami

C

, 

Wilke

CO

, 

Arnold

FH.

2005

. 

Why highly expressed proteins evolve slowly

. 

Proc Natl Acad Sci U S A

. 

102

(

40

):

14338

–

14343

.

Dykhuizen

DE

, 

Dean

AM.

1990

. 

Enzyme activity and fitness: evolution in solution

. 

Trends Ecol Evol

. 

5

(

8

):

257

–

262

.

Dykhuizen

DE

, 

Dean

AM.

1994

. 

Predicted fitness changes along an environmental gradient

. 

Evol Ecol

. 

8

(

5

):

524

–

541

.

Dykhuizen

DE

, 

Dean

AM

, 

Hartl

DL.

1987

. 

Metabolic flux and fitness

. 

Genetics

115

(

1

):

25

–

31

.

Echave

J.

2019

. 

Beyond stability constraints: a biophysical model of enzyme evolution with selection on stability and activity

. 

Mol Biol Evol

. 

36

(

3

):

613

–

620

.

Echave

J

, 

Wilke

CO.

2017

. 

Biophysical models of protein evolution: understanding the patterns of evolutionary sequence divergence

. 

Annu Rev Biophys

. 

46

:

85

–

103

.

Eisenthal

R

, 

Danson

MJ

, 

Hough

DW.

2007

. 

Catalytic efficiency and _kcat_/_kM_: a useful comparator?

Trends Biotechnol

. 

25

(

6

):

247

–

249

.

Ellis

RJ.

2001

. 

Macromolecular crowding: obvious but underappreciated

. 

Trends Biochem Sci

. 

26

(

10

):

597

–

604

.

Eyre-Walker

A

, 

Keightley

PD.

2007

. 

The distribution of fitness effects of new mutations

. 

Nat Rev Genet

. 

8

(

8

):

610

–

618

.

Fell

DA.

1992

. 

Metabolic control analysis: a survey of its theoretical and experimental development

. 

Biochem J

. 

286

(

2

):

313

–

330

.

Geiler-Samerotte

KA

, 

Dion

MF

, 

Budnik

BA

, 

Wang

SM

, 

Hartl

DL

, 

Drummond

DA.

2011

. 

Misfolded proteins impose a dosage-dependent fitness cost and trigger a cytosolic unfolded protein response in yeast

. 

Proc Natl Acad Sci U S A

. 

108

(

2

):

680

–

685

.

Griffith

DA

, 

Jarvis

SM.

1996

. 

Nucleoside and nucleobase transport systems of mammalian cells

. 

Biochim Biophys Acta

. 

1286

(

3

):

153

–

181

.

Gudelj

I

, 

Weitz

JS

, 

Ferenci

T

, 

Claire Horner-Devine

M

, 

Marx

CJ

, 

Meyer

JR

, 

Forde

SE.

2010

. 

An integrative approach to understanding microbial diversity: from intracellular mechanisms to community structure

. 

Ecol Lett

. 

13

(

9

):

1073

–

1084

.

Haldane

JBS.

1930

. 

Enzymes

. 

London, New York

: 

Longmans, Green

.

Hartl

DL

, 

Dykhuizen

DE

, 

Dean

AM.

1985

. 

Limits of adaptation: the evolution of selective neutrality

. 

Genetics

. 

111

(

3

):

655

–

674

.

Heckmann

D

, 

Zielinski

DC

, 

Palsson

BO.

2018

. 

Modeling genome-wide enzyme evolution predicts strong epistasis underlying catalytic turnover rates

. 

Nat Commun

. 

9

(

1

):

5270

.

Heim

NA

, 

Payne

JL

, 

Finnegan

S

, 

Knope

ML

, 

Kowalewski

M

, 

Lyons

SK

, 

McShea

DW

, 

Novack-Gottshall

PM

, 

Smith

FA

, 

Wang

SC.

2017

. 

Hierarchical complexity and the size limits of life

. 

Proc R Soc B

. 

284

(

1857

):

20171039

.

Heinrich

R

, 

Rapoport

TA.

1974

. 

A linear steady-state treatment of enzymatic chains. general properties, control and effector strength

. 

Eur J Biochem

. 

42

(

1

):

89

–

95

.

Heinrich

R

, 

Schuster

S

, 

Holzhütter

HG.

1991

. 

Mathematical analysis of enzymic reaction systems using optimization principles

. 

Eur J Biochem

. 

201

(

1

):

1

–

21

.

Hodgins-Davis

A

, 

Duveau

F

, 

Walker

EA

, 

Wittkopp

PJ.

2019

. 

Empirical measures of mutational effects define neutral models of regulatory evolution in _Saccharomyces cerevisiae_

. 

Proc Natl Acad Sci U S A

.

116

(

42

):

21085

–

21093

.

Huang

X

, 

Holden

HM

, 

Raushel

FM.

2001

. 

Channeling of substrates and intermediates in enzyme-catalyzed reactions

. 

Annu Rev Biochem

. 

70

(

1

):

149

–

180

.

Iwasa

Y

, 

Michor

F

, 

Nowak

MA.

2004

. 

Evolutionary dynamics of invasion and escape

. 

J Theor Biol

. 

226

(

2

):

205

–

214

.

Jiang

M

, 

Guo

Z.

2007

. 

Effects of macromolecular crowding on the intrinsic catalytic efficiency and structure of enterobactin-specific

_isochorismate synthase_. 

J Am Chem Soc

. 

129

(

4

):

730

–

731

.

Jones

CM

, 

Hernández Lozada

NJ

, 

Pfleger

BF.

2015

. 

Efflux systems in bacteria and their metabolic engineering applications

. 

Appl Microbiol Biotechnol

. 

99

(

22

):

9381

–

9393

.

Kacser

H

, 

Beeby

R.

1984

. 

Evolution of catalytic proteins

. 

J Mol Evol

. 

20

(

1

):

38

–

51

.

Kacser

H

, 

Burns

JA.

1973

. 

The control of flux

. 

Symp Soc Exp Biol

. 

27

:

65

–

104

.

Kacser

H

, 

Burns

JA

, 

Kacser

H

, 

Fell

DA.

1995

. 

The control of flux

. 

Biochem Soc Trans

. 

23

(

2

):

341

–

366

.

Kafri

M

, 

Metzl-Raz

E

, 

Jona

G

, 

Barkai

N.

2016

. 

The cost of protein production

. 

Cell Rep

. 

14

(

1

):

22

–

31

.

Kaltenbach

M

, 

Tokuriki

N.

2014

. 

Dynamics and constraints of enzyme evolution

. 

J Exp Zool B Mol Dev Evol

. 

322

(

7

):

468

–

487

.

Keller

MA

, 

Piedrafita

G

, 

Ralser

M.

2015

. 

The widespread role of non-enzymatic reactions in cellular metabolism

. 

Curr Opin Biotechnol

. 

34

:

153

–

161

.

Khersonsky

O

, 

Tawfik

DS.

2010

. 

Enzyme promiscuity: a mechanistic and evolutionary perspective

. 

Annu Rev Biochem

. 

79

:

471

–

505

.

Kimura

M.

1968

. 

Evolutionary rate at the molecular level

. 

Nature

217

(

5129

):

624

–

626

.

Kinsler

G

, 

Geiler-Samerotte

K

, 

Petrov

DA

, 

Cooper

VS

, 

Barkai

N

, 

Gresham

D.

2020

. 

Fitness variation across subtle environmental perturbations reveals local modularity and global pleiotropy of adaptation

. 

eLife

9

:

e61271

.

Klipp

E

, 

Heinrich

R.

1994

. 

Evolutionary optimization of enzyme kinetic parameters; effect of constraints

. 

J Theoret Biol

. 

171

(

3

):

309

–

323

.

Knies

J

, 

Cai

F

, 

Weinreich

DM.

2017

. 

Enzyme efficiency but not thermostability drives cefotaxime resistance evolution in tem-1 _β_-lactamase

. 

Mol Biol Evol

. 

34

(

5

):

1040

–

1054

.

Knowles

JR

, 

Albery

WJ.

1977

. 

Perfection in enzyme catalysis: the energetics of triosephosphate isomerase

. 

Accounts Chem Res

. 

10

(

4

):

105

–

111

.

Koshland

DE.

2002

. 

The application and usefulness of the ratio kcat/km

. 

Bioorgan. Chem

. 

30

(

3

):

211

–

213

.

Kotyk

A.

1967

. 

Mobility of the free and of the loaded monosaccharide carrier in saccharomyces cerevisiae

. 

Biochim Biophys Acta

. 

135

(

1

):

112

–

119

.

Landry

CR

, 

Lemos

B

, 

Rifkin

SA

, 

Dickinson

WJ

, 

Hartl

DL.

2007

. 

Genetic properties influencing the evolvability of gene expression

. 

Science

317

(

5834

):

118

–

121

.

Lang

GI

, 

Murray

AW

, 

Botstein

D.

2009

. 

The cost of gene expression underlies a fitness trade-off in yeast

. 

Proc Natl Acad Sci U S A

. 

106

(

14

):

5755

–

5760

.

Lilja

EE

, 

Johnson

DR.

2017

. 

Metabolite toxicity determines the pace of molecular evolution within microbial populations

. 

BMC Evol Biol

. 

17

(

1

):

52

.

Lunzer

M

, 

Miller

SP

, 

Felsheim

R

, 

Dean

AM.

2005

. 

The biochemical architecture of an ancient adaptive landscape

. 

Science

310

(

5747

):

499

–

501

.

Lunzer

M

, 

Golding

GB

, 

Dean

AM.

2010

. 

Pervasive cryptic epistasis in molecular evolution

. 

PLoS Genet

. 

6

(

10

):

e1001162

.

Lynch

M

, 

Marinov

GK.

2015

. 

The bioenergetic costs of a gene

. 

Proc Natl Acad Sci U S A

. 

112

(

51

):

15690

–

15695

.

Maier

A

, 

Völker

B

, 

Boles

E

, 

Fuhrmann

GF.

2002

. 

Characterisation of glucose transport in Saccharomyces cerevisiae with plasma membrane vesicles (countertransport) and intact cells (initial uptake) with single _Hxt1_,_Hxt2_,_Hxt3_,_Hxt4_,_Hxt6_,_Hxt7 or Gal2_ transporters

. 

FEMS Yeast Res

. 

2

(

4

):

539

–

550

.

Metzger

BPH

, 

Duveau

F

, 

Yuan

DC

, 

Tryban

S

, 

Yang

B

, 

Wittkopp

PJ.

2016

. 

Contrasting frequencies and effects of cis- and trans-regulatory mutations affecting gene expression

. 

Mol Biol Evol

. 

33

(

5

):

1131

–

1146

.

Michaelis

L

, 

Menten

M.

1913

. 

Die kinetik der invertinwirkung. biochemische zeitschrift

. 

Biochemische Zeitschrift

. 

49

:

333

–

369

.

Michaelis, 

Menten

ML

, 

Johnson

KA

, 

Goody

RS.

2011

. 

The original michaelis constant: translation of the 1913 Michaelis–Menten paper

. 

Biochemistry

50

(

39

):

8264

–

8269

.

Miller

SR.

2017

. 

An appraisal of the enzyme stability activity trade off

. 

Evolution

71

(

7

):

1876

–

1887

.

Milo

R

, 

Jorgensen

P

, 

Moran

U

, 

Weber

G

, 

Springer

M.

2010

. 

Bionumbers–the database of key numbers in molecular and cell biology

. 

Nucleic Acids Res

. 

38

(

Database issue

):

D750

–

D753

.

Muramatsu

N

, 

Minton

AP.

1988

. 

Tracer diffusion of globular proteins in concentrated protein solutions

. 

Proc Natl Acad Sci U S A

. 

85

(

9

):

2984

–

2988

.

Newton

MS

, 

Arcus

VL

, 

Gerth

ML

, 

Patrick

WM.

2018

. 

Enzyme evolution: innovation is easy, optimization is complicated

. 

Curr Opin Struct Biol

. 

48

:

110

–

116

.

Niehaus

TD

, 

Hillmann

KB.

2020

. 

Enzyme promiscuity, metabolite damage, and metabolite damage control systems of the tricarboxylic acid cycle

. 

FEBS J

. 

287

(

7

):

1343

–

1358

.

Noor

E

, 

Flamholz

A

, 

Bar-Even

A

, 

Davidi

D

, 

Milo

R

, 

Liebermeister

W.

2016

. 

The protein cost of metabolic fluxes: prediction from enzymatic rate laws and cost minimization

. 

PLOS Comput Biol

. 

12

(

11

):

e1005167

.

Novick

A

, 

Weiner

M.

1957

. 

Enzyme induction as an all-or-none phenomenon

. 

Proc Natl Acad Sci U S A

. 

43

(

7

):

553

–

566

.

Ohta

T.

1992

. 

The nearly neutral theory of molecular evolution

. 

Annu Rev Ecol Syst

. 

23

(

1

):

263

–

286

.

Orth

JD

, 

Thiele

I

, 

Palsson

BØ.

2010

. 

What is flux balance analysis?

Nat Biotechnol

. 

28

(

3

):

245

–

248

.

Otwinowski

J

, 

McCandlish

DM

, 

Plotkin

JB.

2018

. 

Inferring the shape of global epistasis

. 

Proc Natl Acad Sci U S A

. 

115

(

32

):

E7550

–

E7558

.

Ovádi

J

, 

Saks

V.

2004

. 

On the origin of intracellular compartmentation and organized metabolic systems

. 

Mol Cell Biochem

. 

256

(

1/2

):

5

–

12

.

Peracchi

A.

2018

. 

The limits of enzyme specificity and the evolution of metabolism

. 

Trends Biochem Sci

. 

43

(

12

):

984

–

996

.

Pozdnyakova

I

, 

Wittung-Stafshede

P.

2010

. 

Non-linear effects of macromolecular crowding on enzymatic activity of multi-copper oxidase

. 

Biochim Biophys Acta (BBA)

. 

1804

(

4

):

740

–

744

.

Ralston

GB.

1990

. 

Effects of “crowding” in protein solutions

. 

J Chem Educ

. 

67

(

10

):

857

.

Reddy

G

, 

Desai

MM.

2021

. Global epistasis emerges from a generic model of a complex trait. _eLife_ 10:e64740.

Rich

PR.

2003

. 

The molecular machinery of keilin’s respiratory chain

. 

Biochem Soc Trans

. 

31(Pt 6

):

1095

–

1105

.

Rivas

G

, 

Minton

AP.

2018

. 

Toward an understanding of biochemical equilibria within living cells

. 

Biophys Rev

. 

10

(

2

):

241

–

253

.

Rivas

G

, 

Ferrone

F

, 

Herzfeld

J.

2004

. 

Life in a crowded world

. 

EMBO Rep

. 

5

(

1

):

23

–

27

.

Rodrigues

JV

, 

Bershtein

S

, 

Li

A

, 

Lozovsky

ER

, 

Hartl

DL

, 

Shakhnovich

EI.

2016

. 

Biophysical principles predict fitness landscapes of drug resistance

. 

Proc Natl Acad Sci U S A

. 

113

(

11

):

E1470

–

8

.

Sabate

R

, 

de Groot

NS

, 

Ventura

S.

2010

. 

Protein folding and aggregation in bacteria

. 

Cell Mol Life Sci

. 

67

(

16

):

2695

–

2715

.

Schäuble

S

, 

Stavrum

AK

, 

Puntervoll

P

, 

Schuster

S

, 

Heiland

I.

2013

. 

Effect of substrate competition in kinetic models of metabolic networks

. 

FEBS Lett

. 

587

(

17

):

2818

–

2824

.

Schavemaker

PE

, 

Boersma

AJ

, 

Poolman

B.

2018

. 

How important is protein diffusion in prokaryotes?

Front Mol Biosci

. 

5

:

93

.

Schmidt

JA

, 

Rinaldi

S

, 

Scalbert

A

, 

Ferrari

P

, 

Achaintre

D

, 

Gunter

MJ

, 

Appleby

PN

, 

Key

TJ

, 

Travis

RC.

2016

. 

Plasma concentrations and intakes of amino acids in male meat-eaters, fish-eaters, vegetarians and vegans: a cross-sectional analysis in the epic-oxford cohort

. 

Eur J Clin Nutr

. 

70

(

3

):

306

–

312

.

Schmidt

S

, 

Sunyaev

S

, 

Bork

P

, 

Dandekar

T.

2003

. 

Metabolites: a helping hand for pathway evolution?

Trends Biochem Sci

. 

28

(

6

):

336

–

341

.

Schreiber

G

, 

Buckle

AM

, 

Fersht

AR.

1994

. 

Stability and function: two constraints in the evolution of barstar and other proteins

. 

Structure

2

(

10

):

945

–

951

.

Schuster

S

, 

Pfeiffer

T

, 

Fell

DA.

2008

. 

Is maximization of molar yield in metabolic networks favoured by evolution?

J Theor Biol

. 

252

(

3

):

497

–

504

.

Scott

M

, 

Gunderson

CW

, 

Mateescu

EM

, 

Zhang

Z

, 

Hwa

T.

2010

. 

Interdependence of cell growth and gene expression: origins and consequences

. 

Science

330

(

6007

):

1099

–

1102

.

Serohijos

AWR

, 

Rimas

Z

, 

Shakhnovich

EI.

2012

. 

Protein biophysics explains why highly abundant proteins evolve slowly

. 

Cell Rep

. 

2

(

2

):

249

–

256

.

Shoichet

BK

, 

Baase

WA

, 

Kuroki

R

, 

Matthews

BW.

1995

. 

A relationship between protein stability and protein function

. 

Proc Natl Acad Sci U S A

. 

92

(

2

):

452

–

456

.

Stein

WD.

1986a

. Transport and Diffusion Across Cell Membranes. Physical basis of movement across cell membranes, chapter 1. Academic Press. p. 

1

–

68

.

Stein

WD.

1986b

. Transport and Diffusion Across Cell Membranes. Facilitated diffusion: the simple carrier, chapter 4. Academic Press. p. 

231

–

361

.

Stiffler

MA

, 

Hekstra

DR

, 

Ranganathan

R.

2015

. 

Evolvability as a function of purifying selection in tem-1 _β_-lactamase

. 

Cell

160

(

5

):

882

–

892

.

Stoebel

DM

, 

Dean

AM

, 

Dykhuizen

DE.

2008

. 

The cost of expression of _Escherichia coli lac operon_ proteins is in the process, not in the products

. 

Genetics

178

(

3

):

1653

–

1660

.

Storz

JF.

2018

. 

Compensatory mutations and epistasis for protein function

. 

Curr Opin Struct Biol

. 

50

:

18

–

25

.

Sweetlove

LJ

, 

Fernie

AR.

2018

. 

The role of dynamic enzyme assemblies and substrate channelling in metabolic regulation

. 

Nat Commun

. 

9

(

1

):

2136

.

Taverna

DM

, 

Goldstein

RA.

2002

. 

Why are proteins marginally stable?

Proteins: Struct Funct Bioinformatics

. 

46

(

1

):

105

–

109

.

ter Kuile

BH

, 

Cook

M.

1994

. 

The kinetics of facilitated diffusion followed by enzymatic conversion of the substrate

. 

Biochim Biophys Acta

. 

1193

(

2

):

235

–

239

.

Teusink

B

, 

Diderich

JA

, 

Westerhoff

HV

, 

van Dam

K

, 

Walsh

MC.

1998

. 

Intracellular glucose concentration in derepressed yeast cells consuming glucose is high enough to reduce the glucose transport rate by 50%

. 

J Bacteriol

. 

180

(

3

):

556

–

562

.

Tokuriki

N

, 

Tawfik

DS.

2009

. 

Stability effects of mutations and protein evolvability

. 

Curr Opin Struct Biol

. 

19

(

5

):

596

–

604

.

Tokuriki

N

, 

Jackson

CJ

, 

Afriat-Jurnou

L

, 

Wyganowski

KT

, 

Tang

R

, 

Tawfik

DS.

2012

. 

Diminishing returns and tradeoffs constrain the laboratory optimization of an enzyme

. 

Nat Commun

. 

3

(

1

):

1257

.

Tokuriki

N

, 

Stricher

F

, 

Serrano

L

, 

Tawfik

DS.

2008

. 

How protein stability and new functions trade off

. 

PLoS Comput Biol

. 

4

(

2

):

e1000002

.

Tokuriki

N

, 

Stricher

F

, 

Schymkowitz

J

, 

Serrano

L

, 

Tawfik

DS.

2007

. 

The stability effects of protein mutations appear to be universally distributed

. 

J Mol Biol

. 

369

(

5

):

1318

–

1332

.

van den Burg

B

, 

Eijsink

VGH.

2002

. 

Selection of mutations for increased protein stability

. 

Curr Opin Biotechnol

. 

13

(

4

):

333

–

337

.

Wagner

A.

2005

. 

Energy Constraints on the Evolution of Gene Expression

. 

Mol Biol Evol

. 

22

(

6

):

1365

–

1374

.

Walkiewicz

K

, 

Benitez Cardenas

AS

, 

Sun

C

, 

Bacorn

C

, 

Saxer

G

, 

Shamoo

Y.

2012

. 

Small changes in enzyme function can lead to surprisingly large fitness effects during adaptive evolution of antibiotic resistance

. 

Proc Natl Acad Sci U S A

. 

109

(

52

):

21408

–

21413

.

Wang

Z

, 

Zhang

J.

2011

. 

Impact of gene expression noise on organismal fitness and the efficacy of natural selection

. 

Proc Natl Acad Sci U S A

. 

108

(

16

):

E67

–

E76

.

Weinreich

DM

, 

Chao

L.

2005

. 

Rapid evolutionary escape by large populations from local fitness peaks is likely in nature

. 

Evolution

59

(

6

):

1175

–

1182

.

Weinreich

DM

, 

Delaney

NF

, 

DePristo

MA

, 

Hartl

DL.

2006

. 

Darwinian evolution can follow only very few mutational paths to fitter proteins

. 

Science

312

(

5770

):

111

–

114

.

Weinreich

DM

, 

Lan

Y

, 

Wylie

CS

, 

Heckendorn

RB.

2013

. 

Should evolutionary geneticists worry about higher-order epistasis?

Curr Opin Genet Dev

. 

23

(

6

):

700

–

707

.

Weissman

DB

, 

Desai

MM

, 

Fisher

DS

, 

Feldman

MW.

2009

. 

The rate at which asexual populations cross fitness valleys

. 

Theor Popul Biol

. 

75

(

4

):

286

–

300

.

Welch

GR

, 

Easterby

JS.

1994

. 

Metabolic channeling versus free diffusion: transition-time analysis

. 

Trends Biochem Sci

. 

19

(

5

):

193

–

197

.

Wilbrandt

W

, 

Rosenberg

T.

1961

. 

The concept of carrier transport and its corollaries in pharmacology

. 

Pharmacol Rev

. 

13

(

2

):

109

–

183

.

Williamson

DH

, 

Lund

P

, 

Krebs

HA.

1967

. 

The redox state of free nicotinamide-adenine dinucleotide in the cytoplasm and mitochondria of rat liver

. 

Biochem J

. 

103

(

2

):

514

–

527

.

Wood

RE

, 

Wirth

FPJ

, 

Morgan

HE.

1968

. 

Glucose permeability of lipid bilayer membranes

. 

Biochim Biophys Acta

. 

163

(

2

):

171

–

178

.

Wright

KM

, 

Rausher

MD.

2010

. 

The evolution of control and distribution of adaptive mutations in a metabolic pathway

. 

Genetics

184

(

2

):

483

–

502

.

Wright

S.

1931

. 

Evolution in mendelian populations

. 

Genetics

16

(

2

):

97

–

159

.

Wright

S.

1934

. 

Physiological and evolutionary theories of dominance

. 

Am Nat

. 

68

(

714

):

24

–

53

.

Xie

H

, 

Patching

SG

, 

Gallagher

MP

, 

Litherland

GJ

, 

Brough

AR

, 

Venter

H

, 

Yao

SYM

, 

Ng

AML

, 

Young

JD

, 

Herbert

RB

, et al.  

2004

. 

Purification and properties of the _Escherichia coli_ nucleoside transporter _nupg_, a paradigm for a major facilitator transporter sub-family

. 

Mol Membr Biol

. 

21

(

5

):

323

–

336

.

Yang

J-R

, 

Liao

B-Y

, 

Zhuang

S-M

, 

Zhang

J.

2012

. 

Protein misinteraction avoidance causes highly expressed proteins to evolve slowly

. 

Proc Natl Acad Sci U S A

. 

109

(

14

):

E831

–

E840

.

Yi

X

, 

Dean

AM.

2019

. 

Adaptive landscapes in the age of synthetic biology

. 

Mol Biol Evol

. 

36

(

5

):

890

–

907

.

Yue

P

, 

Li

Z

, 

Moult

J.

2005

. 

Loss of protein structure stability as a major causative factor in monogenic disease

. 

J Mol Biol

. 

353

(

2

):

459

–

473

.

Zampieri

M

, 

Hörl

M

, 

Hotz

F

, 

Müller

NF

, 

Sauer

U.

2019

. 

Regulatory mechanisms underlying coordination of amino acid and glucose catabolism in escherichia coli

. 

Nat Commun

. 

10

(

1

):

3354

.

Zhou

G-Q

, 

Zhong

W-Z.

1982

. 

Diffusion-controlled reactions of enzymes

. 

Eur J Biochem

. 

128

(

2-3

):

383

–

387

.

Zhou

H-X

, 

Rivas

G

, 

Minton

AP.

2008

. 

Macromolecular crowding and confinement: biochemical, biophysical, and potential physiological consequences

. 

Annu Rev Biophys

. 

37

(

1

):

375

–

397

.

Zimmerman

SB

, 

Minton

AP.

1993

. 

Macromolecular crowding: biochemical, biophysical, and physiological consequences

. 

Annu Rev Biophys Biomol Struct

. 

22

(

1

):

27

–

65

.

© The Author(s) 2021. Published by Oxford University Press on behalf of the Society for Molecular Biology and Evolution.

This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License ([http://creativecommons.org/licenses/by-nc/4.0/](http://creativecommons.org/licenses/by-nc/4.0/)), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contact journals.permissions@oup.com

## Supplementary data
### Citations
### Views
### Altmetric
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2024/png/22983715/1709301103532-cb4381bb-15c4-46bf-8360-e327394ee004.png)

Metrics

Total Views1,835

1,362Pageviews

473PDF Downloads

Since 5/1/2021

| Month: | Total Views: |
| --- | --- |
| May 2021 | 122 |
| June 2021 | 12 |
| July 2021 | 32 |
| August 2021 | 119 |
| September 2021 | 175 |
| October 2021 | 133 |
| November 2021 | 124 |
| December 2021 | 67 |
| January 2022 | 66 |
| February 2022 | 68 |
| March 2022 | 45 |
| April 2022 | 56 |
| May 2022 | 39 |
| June 2022 | 43 |
| July 2022 | 30 |
| August 2022 | 42 |
| September 2022 | 59 |
| October 2022 | 77 |
| November 2022 | 40 |
| December 2022 | 61 |
| January 2023 | 26 |
| February 2023 | 48 |
| March 2023 | 39 |
| April 2023 | 30 |
| May 2023 | 31 |
| June 2023 | 22 |
| July 2023 | 12 |
| August 2023 | 21 |
| September 2023 | 19 |
| October 2023 | 29 |
| November 2023 | 31 |
| December 2023 | 49 |
| January 2024 | 46 |
| February 2024 | 22 |


Citations

[3](https://www.webofscience.com/api/gateway?GWVersion=2&SrcApp=PARTNER_APP&SrcAuth=Silverchair&KeyUT=WOS:000693664800033&DestLinkType=CitingArticles&DestApp=WOS_CPL&UsrCustomerID=61f30d8ae69c46f86624c5f98a3bc13a)Web of Science

×

### Email alerts
### Email alerts
### Recommended
1. [Computational Modeling of Anthocyanin Pathway Evolution: Biases, Hotspots, and Trade-offs](https://academic.oup.com/icb/article/59/3/585/5497801?itm_medium=sidebar&itm_source=trendmd-widget&itm_campaign=Integrative_and_Comparative_Biology&itm_content=Integrative_and_Comparative_Biology_0)

L C Wheeler et al., Integrative and Comparative Biology, 2019

2. [High-Order Epistasis in Catalytic Power of Dihydrofolate Reductase Gives Rise to a Rugged Fitness Landscape in the Presence of Trimethoprim Selection](https://academic.oup.com/mbe/article/36/7/1533/5458069?itm_medium=sidebar&itm_source=trendmd-widget&itm_campaign=Molecular_Biology_and_Evolution&itm_content=Molecular_Biology_and_Evolution_0)

Yusuf Talha Tamer et al., Molecular Biology and Evolution, 2019

3. [SodaPop: a forward simulation suite for the evolutionary dynamics of asexual populations on protein fitness landscapes](https://academic.oup.com/bioinformatics/article/35/20/4053/5380769?itm_medium=sidebar&itm_source=trendmd-widget&itm_campaign=Bioinformatics&itm_content=Bioinformatics_0)

Louis Gauthier et al., Bioinformatics, 2019

1. [CRISPR interference screens reveal growth–robustness tradeoffs in Synechocystis sp. PCC 6803 across growth conditions](https://academic.oup.com/plcell/advance-article/doi/10.1093/plcell/koad208/7231705?utm_source=TrendMD&utm_medium=cpc&utm_content=The_Plant_Cell_1&utm_campaign=The_Plant_Cell_TrendMD_1)

Rui Miao et al., The Plant Cell 

2. [Elements Required for an Efficient NADP-Malic Enzyme Type C4 Photosynthesis](https://academic.oup.com/plphys/article/164/4/2231/6113276?utm_source=TrendMD&utm_medium=cpc&utm_content=Plant_Phyisol_1&utm_campaign=Plant_Phyisol_TrendMD_1)

Yu Wang et al., Plant Phyisol, 2014

3. [Geospatial Informatics Key to Recovering and Sharing Historical Ecological Data for Modern Use](https://www.ingentaconnect.com/contentone/asprs/pers/2017/00000083/00000011/art00016?utm_source=TrendMD&utm_medium=cpc&utm_campaign=Photogrammetric_Engineering_%2526_Remote_Sensing_TrendMD_1)

Maggi Kelly et al., Photogrammetric Engineering & Remote Sensing, 2017

### Citing articles via
### Latest 
### Most Read 
### Most Cited 
More from Oxford Academic  


> 来自: [Resource Uptake and the Evolution of Moderately Efficient Enzymes | Molecular Biology and Evolution | Oxford Academic](https://academic.oup.com/mbe/article/38/9/3938/6272522?login=false)
>

