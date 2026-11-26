---
layout: single
title: "Questions"
permalink: /questions/
classes: []
toc: true
toc_sticky: true
---

## Current status

*Last updated: November 26, 2026.*

Of the **57 numbered questions**, **37 have complete answers** in the scopes stated below and **20 do not yet have a complete answer**. This count includes subquestions and answers already in the literature; it is not a count of new results. I distinguish results stated in the literature from consequences of published results or public preprints. Where I give only the status, the proof or construction is left for separate notes. **Open** means that no complete answer is recorded here, not a claim about the entire literature.

| Topic | Complete answers | Open, partial, or open-ended |
| --- | --- | --- |
| Self-orthogonal modules and Wakamatsu tilting modules | [Q1](#q1), [Q2](#q2), [Q3](#q3), [Q5](#q5), [Q6](#q6), [Q7](#q7), [Q8](#q8) | [Q4](#q4), [Q9](#q9), [Q10](#q10) |
| Combinatorics of Auslander-Reiten quivers | [Q11](#q11), [Q12](#q12), [Q13](#q13), [Q14](#q14), [Q15](#q15), [Q16](#q16), [Q17](#q17), [Q18](#q18) | — |
| Torsion classes | [Q20](#q20), [Q23](#q23), [Q24](#q24), [Q25](#q25), [Q26](#q26), [Q27](#q27), [Q28](#q28) | [Q19](#q19), [Q21](#q21), [Q22](#q22), [Q29](#q29), [Q30](#q30) |
| Wide subcategories | [Q31](#q31), [Q37](#q37) | [Q32](#q32), [Q33](#q33), [Q34](#q34), [Q35](#q35), [Q36](#q36), [Q38](#q38) |
| ICE-closed subcategories | [Q39](#q39), [Q40](#q40), [Q42](#q42), [Q43](#q43) | [Q41](#q41) |
| Extension-closed subcategories | [Q44](#q44), [Q45](#q45), [Q46](#q46) | [Q47](#q47), [Q48](#q48), [Q49](#q49) |
| Higher homological algebra | [Q50](#q50), [Q51](#q51) | — |
| Grothendieck monoid | [Q52](#q52), [Q53](#q53), [Q54](#q54), [Q56](#q56) | [Q55](#q55), [Q57](#q57) |

## The questions

These are questions in the representation theory of algebras that I have collected over time. I do not claim originality for them. Longer notes may be added separately; where a proof or example is already in a paper or public preprint, I point to it below.

Unless otherwise specified, $A$ is an Artin algebra and $\mathsf{mod}\,A$ is its category of finitely generated left modules. Questions on formalization and software are listed separately at the end.

## Self-orthogonal modules and Wakamatsu tilting modules

See [Maximal self-orthogonal modules and a new generalization of tilting modules](/papers/mso/) for the original background. An $A$-module $T$ is self-orthogonal if $\operatorname{Ext}^{>0}(T,T)=0$. The notation $\lvert T\rvert$ counts the nonisomorphic indecomposable direct summands.

- <a id="q1"></a>**Q1. Boundedness.** Must every finite self-orthogonal $A$-module $T$ satisfy $\lvert T\rvert\leq\lvert A\rvert$?

  **Status:** **No; immediate consequence of a public counterexample.** In [OpenAI's Auslander–Reiten counterexample](https://github.com/openai/math/blob/main/preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/paper.pdf), Theorem 1.1, the nonprojective module $M$ satisfies $\operatorname{Ext}^{>0}(M,M\oplus A)=0$. Thus $A\oplus M$ is self-orthogonal and has more indecomposable summand types than $A$. The symmetric example in [OpenAI's Tachikawa counterexample](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf), Theorem 1.1, works as well. The examples are over $\mathbb F_2(q,H_1,H_2)$ and persist under extension of that field. This does not address boundedness under a finite-projective-dimension hypothesis.

- <a id="q2"></a>**Q2. Proj=Inj.** If an extension- and summand-closed subcategory has an Ext-progenerator $P$ and an Ext-injective cogenerator $I$, must $\lvert P\rvert=\lvert I\rvert$? Equivalently, must every Wakamatsu tilting module $T$ satisfy $\lvert T\rvert=\lvert A\rvert$?

  **Status:** **No; consequence of a public counterexample.** Use the symmetric pair $(A,M)$ from [OpenAI's Tachikawa counterexample](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf), Theorem 1.1. Then $G=A\oplus M$ is Wakamatsu tilting (the regular module already belongs to $\mathsf{add}\,G$), with $\lvert G\rvert>\lvert A\rvert$. For the relative formulation see [Q5](#q5). In the other direction, the projective-injective Wakamatsu tilting module in Corollary 1.2(3) has fewer summand types than its ambient algebra.

- <a id="q3"></a>**Q3. Maximal self-orthogonality.** Is every Wakamatsu tilting module $T$ maximal self-orthogonal: does self-orthogonality of $T\oplus M$ imply $M\in\mathsf{add}\,T$?

  **Status:** **No; immediate consequence of a public counterexample.** For the symmetric pair in [OpenAI's Tachikawa counterexample](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf), Theorem 1.1, the regular module $A$ is Wakamatsu tilting but $A\oplus M$ is a strict self-orthogonal enlargement.

- <a id="q4"></a>**Q4. Finiteness of Ext-injectives.** If an extension- and summand-closed E has an Ext-progenerator and enough Ext-injectives, must it have a finite Ext-injective cogenerator? What if E is functorially finite?

  **Status:** **Partial.** With the stated hypotheses, the answer is yes if the subcategory is functorially finite (in fact, contravariant finiteness suffices). The general existence question remains open here. The negative answer to the separate equality question [Q5](#q5) does not answer this existence question.

- <a id="q5"></a>**Q5. Equality in the preceding setting.** Under the hypotheses of [Q4](#q4), if a finite Ext-injective cogenerator exists, must its summand count equal that of the Ext-progenerator?

  **Status:** **No; consequence of a public counterexample.** For the symmetric pair in [OpenAI's Tachikawa counterexample](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf), Theorem 1.1, take $G=A\oplus M$ and $\mathcal E=G^\perp$. A surjective right $\mathsf{add}\,G$-approximation of an object in $\mathcal E$ has kernel in $\mathcal E$ by the Ext sequence. Dually, embedding that object into an injective in $\mathsf{add}\,A$ has cokernel in $\mathcal E$. Thus $G$ and $A$ give the Ext-progenerator and Ext-injective cogenerator, respectively, with unequal summand counts.

- <a id="q6"></a>**Q6. Self-orthogonality over Gorenstein algebras.** Over an Iwanaga–Gorenstein Artin algebra, must every self-orthogonal finite module have finite projective dimension?

  **Status:** **No; immediate consequence of a public counterexample.** The nonprojective self-orthogonal module in [OpenAI's Tachikawa counterexample](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf), Theorem 1.1, is over a symmetric algebra and has infinite projective dimension, since a finite module of finite projective dimension over a self-injective algebra is projective. The representation-finite case is affirmative; see [Enomoto, *Maximal self-orthogonal modules and a new generalization of tilting modules*](https://arxiv.org/html/2301.13498v2).

- <a id="q7"></a>**Q7. Wakamatsu tilting over Gorenstein algebras.** Over an Iwanaga–Gorenstein Artin algebra, must every Wakamatsu tilting module be a tilting module of finite projective dimension?

  **Status:** **No; immediate consequence of a public counterexample.** With $(A,M)$ as in [OpenAI's Tachikawa counterexample](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf), Theorem 1.1, the Wakamatsu tilting module $A\oplus M$ from [Q2](#q2) has infinite projective dimension over the symmetric algebra $A$. This is different from the failure of the finite-projective-dimension Wakamatsu tilting conjecture in Corollary 1.2(3), which uses a different algebra.

- <a id="q8"></a>**Q8. Covariant finiteness.** If $T$ is an Ext-progenerator of $T^\perp$, must $T^\perp$ be covariantly finite in $\mathsf{mod}\,A$? Here $T^\perp$ is defined using all positive Ext degrees.

  **Status:** **No; details to appear separately.** [*Tilting Completion and Full-Rank Self-Orthogonal Modules*, Corollary 5.2](https://arxiv.org/html/2608.20722#S5) also shows that an Ext-perpendicular need not be covariantly finite, but does not provide the Ext-progenerator required in this question.

- <a id="q9"></a>**Q9. A partial order on Wakamatsu tilting modules.** For which algebras is the relation $\operatorname{Ext}^{>0}(T,U)=0$ a partial order on basic Wakamatsu tilting modules? Is there a combinatorial criterion for Nakayama algebras?

  **Status:** **Open in general.** The transitivity failure is explicit: see [Enomoto, Example 6.6](https://arxiv.org/html/2301.13498v2#S6), even in finite representation type. This does not supply a criterion for the relation to be a partial order.

- <a id="q10"></a>**Q10. Mutation.** Is there a mutation theory computing all Wakamatsu tilting modules from the regular module, allowing two summands to change along a Hasse arrow?

  **Status:** Open.

  For a related result, [Liu–Feng–Gao, Theorem 3.5](https://arxiv.org/html/2604.10118#S3) shows that one-point extensions preserve certain mutations of projectively Wakamatsu tilting modules. It does not give a general enumeration of Wakamatsu tilting modules.

## Combinatorics of Auslander-Reiten quivers

Throughout Q11–Q18, $A$ is a representation-finite Artin algebra. The input is the valued Auslander–Reiten quiver with translation and with projective and injective vertices marked. The results are for this finite-type setting, not arbitrary representation type.

- <a id="q11"></a>**Q11. Extension-closed subcategories.** For a representation-finite algebra A, can the AR quiver determine the extension- and summand-closed subcategories, viewed as subsets of its indecomposable vertices?

  **Status:** **Yes in the stated Artin setting; details of the general reconstruction to appear separately.** Over an algebraically closed field, this is a consequence of [Pütz–Sauter, Theorem 2.3](https://arxiv.org/html/2412.13710v1#S2) and the finite-type Hom-order theorem ([Smalø, Theorem 5.2](https://inmabb.criba.edu.ar/revuma/pdf/v48n2/v48n2a03.pdf)): extension closure is tested by degeneration, and the Hom data are recovered from the AR meshes.

- <a id="q12"></a>**Q12. Syzygies.** For a representation-finite algebra A, can the AR quiver determine the syzygy of an indecomposable module, including summand multiplicities?

  **Status:** **Yes; consequence of AR ladder and mesh formulas.** Recover the projective cover from the top, then recover its kernel from the Hom and stable-Hom lengths; the latter are obtained by the ladder in the quotient by projectives. See [Iyama, *τ-Categories I: Ladders*, §7](https://doi.org/10.1007/s10468-005-0968-5) and [the equidistribution preprint, Theorem 5.8 and Corollary 5.10](https://arxiv.org/html/2608.18024v2#S5). The usual unvalued version is implemented in [ARquiver](https://github.com/haruhisa-enomoto/ARquiver).

- <a id="q13"></a>**Q13. Projective dimension.** For a representation-finite algebra A, can the AR quiver determine each indecomposable module’s projective dimension?

  **Status:** **Yes; immediate consequence of [Q12](#q12).** Iterate syzygies; the projective dimension is infinite precisely when the graph of nonprojective syzygy summands has a cycle reachable from the given module.

- <a id="q14"></a>**Q14. Injective dimension.** For a representation-finite algebra A, can the AR quiver determine each indecomposable module’s injective dimension?

  **Status:** **Yes; immediate dual of [Q13](#q13).** Use cosyzygies, or apply the projective-dimension calculation to the opposite algebra.

- <a id="q15"></a>**Q15. Global dimension.** For a representation-finite algebra A, can the AR quiver determine the global dimension of the algebra?

  **Status:** **Yes; immediate consequence of [Q13](#q13).** Take the maximum over the simples, which are exactly the vertices whose additive closures are quotient-closed.

- <a id="q16"></a>**Q16. Factor modules.** For a given finite module $M$, can the AR quiver determine $\mathsf{Fac}\,M$, the quotients of finite direct sums of $M$?

  **Status:** **Yes; immediate consequence of the published factor-ladder criterion in its stated field setting.** By [the equidistribution preprint, Theorem 5.8 and Corollary 5.10](https://arxiv.org/html/2608.18024v2#S5), take the smallest quotient-closed subcategory containing the summands of $M$. The same argument with valued ladders over Artin algebras uses [Iyama, *τ-Categories I: Ladders*, §7](https://doi.org/10.1007/s10468-005-0968-5).

- <a id="q17"></a>**Q17. Submodules.** For a given finite module $M$, can the AR quiver determine $\mathsf{Sub}\,M$, the submodules of finite direct sums of $M$?

  **Status:** **Yes; dual consequence of the same criterion.** Use the smallest submodule-closed subcategory containing the summands of $M$ and the reverse factor ladder in [the equidistribution preprint, Theorem 5.8 and Corollary 5.10](https://arxiv.org/html/2608.18024v2#S5). The valued Artin version again uses [Iyama, *τ-Categories I: Ladders*, §7](https://doi.org/10.1007/s10468-005-0968-5).

- <a id="q18"></a>**Q18. Approximation kernels.** Can the AR quiver determine the kernel of a minimal right $\mathsf{add}\,M$-approximation of an indecomposable module $X$?

  **Status:** **Yes in the stated finite-type setting; details to appear separately.** The ingredients include reverse quotient ladders and functor socles; see [Iyama, *τ-Categories I: Ladders*, §7](https://doi.org/10.1007/s10468-005-0968-5) for the ladder machinery. The kernel calculation in [Q12](#q12) alone only handles projective covers.

## Torsion classes

- <a id="q19"></a>**Q19. Realizing finite lattices.** Which finite lattices occur as $\mathsf{tors}\,A$ for a $\tau$-tilting finite Artin algebra A?

  **Status:** Open.

- <a id="q20"></a>**Q20. Two proposed necessary conditions.** Does congruence-uniformity together with regularity of the undirected Hasse graph characterize finite torsion lattices? Does semidistributivity together with that regularity suffice?

  **Status:** **No; counterexample previously given on this page, using a published obstruction.** A finite torsion lattice has a core-label order isomorphic to the lattice of wide subcategories ([Enomoto, §4.4](https://arxiv.org/pdf/2201.00595)). The congruence-uniform regular example on the earlier page has a core-label order without a meet. The realization problem [Q19](#q19) is separate.

- <a id="q21"></a>**Q21. Join-irreducibles and infinite bricks.** Can join-irreducible torsion classes that need not be completely join-irreducible be described using appropriate infinitely generated bricks, perhaps pure-injective ones?

  **Status:** **Open here for join-irreducibles that need not be completely join-irreducible.** The brick correspondence for completely join-irreducible torsion classes is in [Demonet–Iyama–Reading–Reiten–Thomas](https://arxiv.org/abs/1711.01785). [Sentieri](https://arxiv.org/abs/2011.09253) studies bricks of infinite length, but this is not the requested general correspondence.

- <a id="q22"></a>**Q22. Exact categories.** Is there an analogue of $\tau$-tilting theory classifying torsion classes of exact categories through projective objects?

  **Status:** Open.

- <a id="q23"></a>**Q23. Recognizing functorial finiteness.** Can functorially finite torsion classes be recognized from the abstract unlabelled poset $\mathsf{tors}\,A$?

  **Status:** **Yes for finite-dimensional algebras over arbitrary fields; details to appear separately.** The full Artin-algebra scope is not claimed here.

- <a id="q24"></a>**Q24. Recognizing faithfulness.** Can faithful torsion classes be recognized from the abstract unlabelled poset $\mathsf{tors}\,A$?

  **Status:** **No; details to appear separately.**

- <a id="q25"></a>**Q25. Recognizing faithful functorially finite classes.** Can faithful functorially finite torsion classes be recognized from the abstract unlabelled poset $\mathsf{tors}\,A$?

  **Status:** **No, even when both algebras are representation-finite; details to appear separately.**

- <a id="q26"></a>**Q26. The tilting complex.** Does the abstract torsion poset determine the simplicial complex of classical tilting modules, with basic partial tilting modules of projective dimension at most one as faces?

  **Status:** **No, for classical partial tilting modules of projective dimension at most one; details to appear separately.** The correspondence between tilting modules and faithful functorially finite torsion classes itself is classical; see [Adachi–Iyama–Reiten](https://doi.org/10.1073/pnas.1313075111).

- <a id="q27"></a>**Q27. Hearts of intervals.** Can one characterize the hearts $\mathcal T\cap\mathcal U^{\perp_0}$ of torsion intervals $\mathcal U\subseteq\mathcal T$ categorically, without specifying the endpoints? Here $\perp_0$ denotes Hom-orthogonality.

  **Status:** **Yes; details of an endpoint-free criterion to appear separately.** For the published characterization in the special case of wide hearts, see [Asai–Pfeifer](https://arxiv.org/abs/1905.01148).

- <a id="q28"></a>**Q28. Regularity in length categories.** If an essentially small abelian length category has finitely many torsion classes, is its undirected torsion Hasse graph regular?

  **Status:** Yes. Published preprint.

  By [Sentieri, Theorem 2.27 and Corollary 5.2](https://arxiv.org/html/2607.15991v1#S5), finiteness of the torsion lattice implies brick-finiteness, and its Hasse graph is regular. Its degree is the number of simple objects up to isomorphism, as seen at the zero torsion class.

- <a id="q29"></a>**Q29. Beyond module categories.** Which results about torsion classes over Artin algebras extend to arbitrary abelian length categories?

  **Status:** **Open-ended; several generalizations are already available.** For example, [Asai–Pfeifer](https://arxiv.org/abs/1905.01148) treat brick labels and wide intervals in abelian length categories, and [Enomoto](https://arxiv.org/abs/2201.00595) recovers the posets of wide and ICE-closed subcategories in that setting from the torsion lattice. See also [Q28](#q28).

- <a id="q30"></a>**Q30. Finite length over non-artinian rings.** What is the structure of torsion classes of finite-length modules over non-Artinian rings, for example commutative Cohen–Macaulay rings?

  **Status:** **Open-ended in general.** For a commutative ring, the finite-length case is elementary: a finite-length module decomposes into its local parts, and each nonzero local part has the corresponding residue field as a quotient. Hence a torsion class is precisely the finite-length modules supported on some subset of the maximal ideals.

## Wide subcategories

- <a id="q31"></a>**Q31. Infinitely many projectives.** Can $\mathsf{mod}\,A$ contain a wide subcategory with enough projectives and infinitely many nonisomorphic indecomposable internal projectives?

  **Status:** **Yes; construction to appear separately.** The example can be taken to be semisimple as an abelian category. The split exact subcategory in [Q44](#q44) is not asserted to be wide.

- <a id="q32"></a>**Q32. A bound on semibricks.** Does a common finite bound on the cardinalities of semibricks force $\tau$-tilting finiteness?

  **Status:** **Open here.** A common finite bound implies that every semibrick is finite and hence that the algebra is E-finite by [Characterizations of E-finite algebras and conjectures on brick-finiteness](https://hexagonmath.org/2611.01059v1), Theorem A. This does not settle whether the additional uniform bound forces brick-finiteness.

- <a id="q33"></a>**Q33. The strong Sperner property.** For a $\tau$-tilting finite algebra A, is $\mathsf{wide}\,A$ strongly Sperner (with the rank properties of a Peck poset)?

  **Status:** Partial; the general conjecture remains open.

  For the special case of finite Coxeter noncrossing partition lattices, see [Mühle](https://arxiv.org/abs/1509.06942); the corresponding wide-subcategory realization is discussed in [From the lattice of torsion classes …](https://arxiv.org/abs/2201.00595).

- <a id="q34"></a>**Q34. Symmetric Boolean decompositions.** For a $\tau$-tilting finite algebra A, does $\mathsf{wide}\,A$ admit a symmetric Boolean decomposition?

  **Status:** Partial; the general conjecture remains open.

  For published noncrossing-partition cases, see [Mühle](https://arxiv.org/abs/1509.06942) and [Petersen](https://arxiv.org/abs/1108.5761).

- <a id="q35"></a>**Q35. Other lattice properties.** What other order properties do wide-subcategory lattices have, especially in the $\tau$-tilting infinite case?

  **Status:** **Open-ended; some finite-case properties are known.** In the $\tau$-tilting finite case the numbers of wide subcategories by number of simple objects are symmetric and unimodal, by [Aoki et al., Theorem 3.15 and Corollary 3.17](https://arxiv.org/html/2203.15213v4#S3) and the semibrick–wide correspondence. This does not give the strong Sperner property or a Boolean decomposition.

- <a id="q36"></a>**Q36. Left finite wide subcategories.** What order properties hold for the left finite wide subcategories, those whose generated torsion class is functorially finite?

  **Status:** **Open-ended.** Left finite wide subcategories are parametrized by functorially finite torsion classes via the left-wide construction. The inclusion orders should not be identified by this bijection without further argument. See [Asai–Pfeifer](https://arxiv.org/abs/1905.01148) and [Buan–Hanson](https://arxiv.org/abs/2107.01141) for the relation to $\tau$-perpendicular wide subcategories.

- <a id="q37"></a>**Q37. Realizing the dual lattice.** For every Artin algebra $A$, is there an Artin algebra $B$ whose poset of all wide subcategories is dual to that of $A$?

  **Status:** **No; an elementary consequence of the regular-tube decomposition for the Kronecker algebra.** Over $\mathbb C$, the regular tubes are independent wide components (see [Ringel's description of the regular modules](https://link.springer.com/article/10.1007/s13373-013-0042-2)). Omitting finitely many tubes at a time gives a filtered family of nonzero wide subcategories with zero intersection. By contrast, the top of the wide lattice of an Artin algebra is compact for directed joins: any wide subcategory containing the regular module contains all finitely generated modules. These two properties rule out a dual realization. The $\tau$-tilting finite variant also has a negative answer; details of that example will appear separately.

- <a id="q38"></a>**Q38. Gentle algebras.** Is there a combinatorial or surface model for the lattice of all wide subcategories of a gentle algebra?

  **Status:** **Partial.** [Garver–McConville](https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/oriented-flip-graphs-noncrossing-tree-partitions-and-representation-theory-of-tiling-algebras/1DB8002BAE0E4F75F036DCB961534A5F) give a noncrossing-tree-partition model of the wide lattice for their representation-finite tiling algebras. [Baur–Coelho Simões](https://arxiv.org/abs/1803.05802) give a geometric model of the module category for general gentle algebras. These do not by themselves give a direct inclusion rule for all wide subcategories in the general case.

## ICE-closed subcategories

Hasse arrows here point from larger to smaller subcategories. The gentle-algebra question appearing in both sections of the original page is listed once, as [Q38](#q38).

- <a id="q39"></a>**Q39. The number of outgoing arrows.** Can one characterize the number of outgoing Hasse arrows at an ICE-closed subcategory, with arrows oriented from larger to smaller subcategories?

  **Status:** **Yes; the general count follows from the cover description in [Q40](#q40), whose details will appear separately.**

- <a id="q40"></a>**Q40. Cover relations.** Can one characterize the minimal strict inclusions between ICE-closed subcategories?

  **Status:** **Yes; details of the cover criterion to appear separately.** The criterion uses the least wide hull of an ICE-closed subcategory, which is described in [Enomoto–Sakai, Theorem 4.3](https://arxiv.org/html/2010.05433v2#S4.SS1).

- <a id="q41"></a>**Q41. Arrows and Ext-projectives.** For which classes of algebras does every ICE-closed subcategory have as many outgoing arrows as indecomposable Ext-projectives?

  **Status:** **Partial.** The hereditary Dynkin case is affirmative; see [Enomoto–Sakai, §5](https://arxiv.org/html/2010.05433v2#S5) for the hereditary mutation theorem. The general classification is not known here.

- <a id="q42"></a>**Q42. Dynkin preprojective algebras.** How many ICE-closed subcategories does an ordinary Dynkin preprojective algebra have?

  **Status:** **Computed for ordinary Dynkin preprojective algebras of types A, D and E over algebraically closed fields; consequence of public results.** Applying [Enomoto–Sakai, Corollary 4.31](https://arxiv.org/html/2010.05433v2#S4.SS4) to [Mizuno's weak-order description](https://arxiv.org/abs/1304.0667), the number is the sum, over $u$ in the Weyl group, of the number of full-support elements in the parabolic subgroup generated by the right ascents of $u$. See [Q43](#q43).

- <a id="q43"></a>**Q43. A Lie-theoretic interpretation.** Is there a Lie-theoretic interpretation of the ICE-closed subcategories of ordinary Dynkin preprojective algebras?

  **Status:** **Yes in the setting of [Q42](#q42); consequence of public results.** In the right weak-order convention, the join of the upper covers of $u$ is $u w_0(J)$, where $J$ is the set of right ascents of $u$ and $w_0(J)$ is the parabolic longest element. The sincerity test in [Enomoto–Sakai, Corollary 4.31](https://arxiv.org/html/2010.05433v2#S4.SS4) translates into full support in $J$. Thus the parameters are pairs $(u,x)$ with $x$ of full support in that parabolic subgroup; the corresponding sincere interval is $[u,ux]$.

## Extension-closed subcategories

- <a id="q44"></a>**Q44. Infinitely many Ext-projectives.** Can an extension- and summand-closed subcategory have enough Ext-projectives and infinitely many nonisomorphic indecomposable Ext-projectives?

  **Status:** **Yes; immediate consequence of a published result.** The additive subcategory of $n$-preprojective modules for an $n$-representation-infinite algebra with $n>1$ has infinitely many indecomposables and all first extensions between them vanish. It is therefore extension-closed with the split exact structure, and all its objects are relatively projective and injective. See [Herschend–Iyama–Oppermann, Corollary 4.10](https://arxiv.org/html/1205.1272#S4). Thanks to Sondre Kvamme for pointing out the example.

- <a id="q45"></a>**Q45. Finiteness of Ext-projectives.** Does every functorially finite extension- and summand-closed subcategory of $\mathsf{mod}\,A$ have only finitely many indecomposable Ext-projectives?

  **Status:** **No over $\mathbb C$, and also over $\overline{\mathbb Q}$; details to appear separately.**

- <a id="q46"></a>**Q46. Finiteness of Ext-injectives.** Does every functorially finite extension- and summand-closed subcategory of $\mathsf{mod}\,A$ have only finitely many indecomposable Ext-injectives?

  **Status:** **No over $\mathbb C$, and also over $\overline{\mathbb Q}$; details to appear separately.**

- <a id="q47"></a>**Q47. Equality of the two numbers.** In such a functorially finite extension- and summand-closed subcategory, do the numbers of indecomposable Ext-projectives and Ext-injectives coincide?

  **Status:** **Open here.** In the finite-count case with enough relative projectives and injectives the comparison is the equality in [Q2](#q2), but that counterexample is not asserted to be functorially finite.

- <a id="q48"></a>**Q48. Further classifications.** Which additional classes of subcategories of module categories admit useful classifications?

  **Status:** **Open-ended.** One recent example is the classification of image-closed subcategories via intersections of pretorsion theories; see [*Pretorsion theories and image-closed subcategories*, Theorem 4.4](https://hexagonmath.org/2611.00207v1), with explicit computations for linearly oriented type A. See [Q49](#q49) for the additional extension-closure condition.

- <a id="q49"></a>**Q49. Images and extensions.** Can one classify image- and extension-closed subcategories over nonhereditary algebras?

  **Status:** A general categorical characterization is published; a finer classification remains open.

  [Enomoto–Sakai, Proposition 2.3](https://arxiv.org/html/2208.13937#S2) characterizes IE-closed subcategories as intersections of a torsion class and a torsion-free class, without assuming heredity. The two classes need not form a torsion pair.

## Higher homological algebra

- <a id="q50"></a>**Q50. Classifying higher exact structures.** Can all $n$-exact structures on a given additive category be classified, for every $n\geq 1$?

  **Status:** **Yes.** For $n=1$, see [Enomoto](https://arxiv.org/abs/2005.13381) for the classification by Serre subcategories of the defect category in the skeletally small setting. For idempotent-complete additive categories, [Klapproth, Theorem 3.18](https://arxiv.org/html/2410.05242v1#S3.SS2), gives a classification for higher $n$. Details of the extension beyond idempotent completeness will appear separately.

- <a id="q51"></a>**Q51. A maximum exact structure.** Does every additive category admit a greatest $n$-exact structure for every $n\geq 1$?

  **Status:** **Yes.** For $n=1$ this is [Rump, Corollary 2](https://doi.org/10.4064/fm214-1-5). In higher degrees [Klapproth, Theorem 3.23](https://arxiv.org/html/2410.05242v1#S3.SS3), gives the greatest structure for idempotent-complete additive categories. Details beyond idempotent completeness will appear separately.

## Grothendieck monoid

- <a id="q52"></a>**Q52. Torsion classes in Dynkin type.** Can one compute the Grothendieck monoid of every torsion class over a Dynkin path algebra?

  **Status:** **Yes; immediate consequence of a public preprint.** By [Characterizations of E-finite algebras and conjectures on brick-finiteness](https://hexagonmath.org/2611.01059v1), Theorem 4.1, the dimension-vector map embeds the Grothendieck monoid of every torsion class of an E-finite algebra into the ambient Grothendieck group. Dynkin path algebras are representation-finite, hence E-finite over any field, so the answer is the additive monoid generated by the dimension vectors of the indecomposables in the torsion class.

- <a id="q53"></a>**Q53. Torsion-free classes in Dynkin type.** Can one compute the Grothendieck monoid of every torsion-free class over a Dynkin path algebra?

  **Status:** **Yes; immediate dual of [Q52](#q52).** Duality turns a torsion-free class into a torsion class over the opposite algebra, so the same dimension-vector formula holds over any field. See also Corollary 4.3 of [Characterizations of E-finite algebras and conjectures on brick-finiteness](https://hexagonmath.org/2611.01059v1).

- <a id="q54"></a>**Q54. Reducedness.** Are the Grothendieck monoids in [Q52–Q53](#q52) reduced, meaning that their only additive unit is zero?

  **Status:** Yes. In fact this holds for every skeletally small exact category.

  See [Enomoto–Saito, Proposition 6.2](https://arxiv.org/html/2208.02928v2#S6): the exact-category case has no invertible element other than zero.

- <a id="q55"></a>**Q55. Extriangulated computations.** How can Grothendieck monoids of extriangulated categories be computed, especially for extension-closed subcategories of triangulated categories?

  **Status:** **Partial.** For the intermediate subcategory $\mathcal F[1]*\mathcal A$ associated to a torsion-free class $\mathcal F$ of an abelian category $\mathcal A$, [Enomoto–Saito, Theorem 5.4](https://arxiv.org/html/2208.02928v2#S5) computes its monoid by inverting the classes of objects of $\mathcal F$ in $\mathsf M(\mathcal A)$. Further cases are known here; their details will appear separately.

- <a id="q56"></a>**Q56. Invertible classes.** Which objects of an extriangulated category represent invertible elements of its Grothendieck monoid?

  **Status:** **Answered in the literature.** [Enomoto–Saito, Proposition 6.1](https://arxiv.org/html/2208.02928v2#S6) identifies the objects representing units as precisely those of the smallest Serre subcategory.

- <a id="q57"></a>**Q57. Realizing the group and reduced parts.** Can the quotient of an extriangulated category’s Grothendieck monoid by its group of units be realized categorically by localization or a decomposition into exact and triangulated parts?

  **Status:** **Partial; the existence of such a quotient for an arbitrary given category remains open here.** [Enomoto–Saito, §6](https://arxiv.org/html/2208.02928v2#S6) discusses the general question. Some additional cases and limitations of a decomposition are known here; details will appear separately.

## Lean Theorem Prover

**Teaching Auslander-Reiten theory to computer** using [Lean](https://leanprover.github.io/), see also [Lean community](https://leanprover-community.github.io/), and a very good introductory material [Formalising Mathematics](https://github.com/ImperialCollegeLondon/formalising-mathematics)

## SageMath

- Create a system which can deal with the Auslander-Reiten quivers as translation quivers. In particular, compute the dimension of Hom spaces using AR quiver.
- Create or modify programs which enables us to deal with string and band modules over special biserial (or string) algebras.
- More concretely, develop a SageMath version of [String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/)!

I know that [QPA](https://folk.ntnu.no/oyvinso/QPA/) are useful, but I think there's no special functions which can applied to special biserial, string, gentle algebras. Since SageMath can deal with other materials including posets, polytopes, lattices, root system, and so on (and since it's written in Python), I hope that special computational experiments on e.g. string algebras can be done inside SageMath.
