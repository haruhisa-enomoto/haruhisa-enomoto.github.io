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

Of the **57 numbered questions**, **37 have complete answers** in the scopes stated below and **20 do not yet have a complete answer**. This count includes subquestions and answers already in the literature; it is not a count of new results. **Unpublished** marks an answer recorded here without its proof or construction. **Open** means that no complete answer is recorded here, not a claim about the entire literature.

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

  **Status:** No (unpublished).

- <a id="q2"></a>**Q2. Proj=Inj.** If an extension- and summand-closed subcategory has an Ext-progenerator $P$ and an Ext-injective cogenerator $I$, must $\lvert P\rvert=\lvert I\rvert$? Equivalently, must every Wakamatsu tilting module $T$ satisfy $\lvert T\rvert=\lvert A\rvert$?

  **Status:** No (unpublished).

- <a id="q3"></a>**Q3. Maximal self-orthogonality.** Is every Wakamatsu tilting module $T$ maximal self-orthogonal: does self-orthogonality of $T\oplus M$ imply $M\in\mathsf{add}\,T$?

  **Status:** No (unpublished).

- <a id="q4"></a>**Q4. Finiteness of Ext-injectives.** If an extension- and summand-closed E has an Ext-progenerator and enough Ext-injectives, must it have a finite Ext-injective cogenerator? What if E is functorially finite?

  **Status:** Partial: yes in the functorially finite case; the general question remains open.

- <a id="q5"></a>**Q5. Equality in the preceding setting.** Under the hypotheses of [Q4](#q4), if a finite Ext-injective cogenerator exists, must its summand count equal that of the Ext-progenerator?

  **Status:** No (unpublished).

- <a id="q6"></a>**Q6. Self-orthogonality over Gorenstein algebras.** Over an Iwanaga–Gorenstein Artin algebra, must every self-orthogonal finite module have finite projective dimension?

  **Status:** No. Published preprint.

  [A counterexample to Tachikawa's second conjecture](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf) gives a nonprojective self-orthogonal module over a finite-dimensional symmetric algebra. Over a self-injective algebra a finite module of finite projective dimension is projective, so it also answers Q6.

- <a id="q7"></a>**Q7. Wakamatsu tilting over Gorenstein algebras.** Over an Iwanaga–Gorenstein Artin algebra, must every Wakamatsu tilting module be a tilting module of finite projective dimension?

  **Status:** No (unpublished).

- <a id="q8"></a>**Q8. Covariant finiteness.** If $T$ is an Ext-progenerator of $T^\perp$, must $T^\perp$ be covariantly finite in $\mathsf{mod}\,A$? Here $T^\perp$ is defined using all positive Ext degrees.

  **Status:** No (unpublished).

- <a id="q9"></a>**Q9. A partial order on Wakamatsu tilting modules.** For which algebras is the relation $\operatorname{Ext}^{>0}(T,U)=0$ a partial order on basic Wakamatsu tilting modules? Is there a combinatorial criterion for Nakayama algebras?

  **Status:** Open: a general criterion is not known here.

  The relation is not transitive in general, even in finite representation type: see [Maximal self-orthogonal modules and a new generalization of tilting modules, Example 6.6](https://arxiv.org/html/2301.13498v2).

- <a id="q10"></a>**Q10. Mutation.** Is there a mutation theory computing all Wakamatsu tilting modules from the regular module, allowing two summands to change along a Hasse arrow?

  **Status:** Open.

  For a related result, [Liu–Feng–Gao, Theorem 3.5](https://arxiv.org/html/2604.10118#S3) shows that one-point extensions preserve certain mutations of projectively Wakamatsu tilting modules. It does not give a general enumeration of Wakamatsu tilting modules.

## Combinatorics of Auslander-Reiten quivers

Throughout Q11–Q18, $A$ is a representation-finite Artin algebra. The input is the valued Auslander–Reiten quiver with translation and with projective and injective vertices marked. The results are for this finite-type setting, not arbitrary representation type.

- <a id="q11"></a>**Q11. Extension-closed subcategories.** For a representation-finite algebra A, can the AR quiver determine the extension- and summand-closed subcategories, viewed as subsets of its indecomposable vertices?

  **Status:** Yes (unpublished).

- <a id="q12"></a>**Q12. Syzygies.** For a representation-finite algebra A, can the AR quiver determine the syzygy of an indecomposable module, including summand multiplicities?

  **Status:** Yes (unpublished).

- <a id="q13"></a>**Q13. Projective dimension.** For a representation-finite algebra A, can the AR quiver determine each indecomposable module’s projective dimension?

  **Status:** Yes (unpublished).

- <a id="q14"></a>**Q14. Injective dimension.** For a representation-finite algebra A, can the AR quiver determine each indecomposable module’s injective dimension?

  **Status:** Yes (unpublished).

- <a id="q15"></a>**Q15. Global dimension.** For a representation-finite algebra A, can the AR quiver determine the global dimension of the algebra?

  **Status:** Yes (unpublished).

- <a id="q16"></a>**Q16. Factor modules.** For a given finite module $M$, can the AR quiver determine $\mathsf{Fac}\,M$, the quotients of finite direct sums of $M$?

  **Status:** Yes (unpublished).

  For finite-dimensional algebras over a field, the factor-ladder test in [Theorem 5.8(1) of the equidistribution preprint](https://arxiv.org/html/2608.18024v2#S5) reconstructs quotient-closed subcategories from the marked valued AR quiver. Taking the smallest one containing the summands of $M$ gives $\mathsf{Fac}\,M$.

- <a id="q17"></a>**Q17. Submodules.** For a given finite module $M$, can the AR quiver determine $\mathsf{Sub}\,M$, the submodules of finite direct sums of $M$?

  **Status:** Yes (unpublished).

  In the same published setting, the dual reverse factor-ladder test in [Theorem 5.8(2) of the same preprint](https://arxiv.org/html/2608.18024v2#S5) reconstructs submodule-closed subcategories. Taking the smallest one containing the summands of $M$ gives $\mathsf{Sub}\,M$.

- <a id="q18"></a>**Q18. Approximation kernels.** Can the AR quiver determine the kernel of a minimal right $\mathsf{add}\,M$-approximation of an indecomposable module $X$?

  **Status:** Yes (unpublished).

## Torsion classes

- <a id="q19"></a>**Q19. Realizing finite lattices.** Which finite lattices occur as $\mathsf{tors}\,A$ for a $\tau$-tilting finite Artin algebra A?

  **Status:** Open.

- <a id="q20"></a>**Q20. Two proposed necessary conditions.** Does congruence-uniformity together with regularity of the undirected Hasse graph characterize finite torsion lattices? Does semidistributivity together with that regularity suffice?

  **Status:** No. A counterexample was already recorded on this page.

  The obstruction uses the fact that the core-label order of a finite torsion lattice gives the wide-subcategory lattice; see [From the lattice of torsion classes to the posets of wide subcategories and ICE-closed subcategories](https://arxiv.org/abs/2201.00595). The general realization problem is [Q19](#q19).

- <a id="q21"></a>**Q21. Join-irreducibles and infinite bricks.** Can join-irreducible torsion classes that need not be completely join-irreducible be described using appropriate infinitely generated bricks, perhaps pure-injective ones?

  **Status:** Open.

- <a id="q22"></a>**Q22. Exact categories.** Is there an analogue of $\tau$-tilting theory classifying torsion classes of exact categories through projective objects?

  **Status:** Open.

- <a id="q23"></a>**Q23. Recognizing functorial finiteness.** Can functorially finite torsion classes be recognized from the abstract unlabelled poset $\mathsf{tors}\,A$?

  **Status:** Yes for finite-dimensional algebras over arbitrary fields (unpublished).

- <a id="q24"></a>**Q24. Recognizing faithfulness.** Can faithful torsion classes be recognized from the abstract unlabelled poset $\mathsf{tors}\,A$?

  **Status:** No (unpublished).

- <a id="q25"></a>**Q25. Recognizing faithful functorially finite classes.** Can faithful functorially finite torsion classes be recognized from the abstract unlabelled poset $\mathsf{tors}\,A$?

  **Status:** No (unpublished).

- <a id="q26"></a>**Q26. The tilting complex.** Does the abstract torsion poset determine the simplicial complex of classical tilting modules, with basic partial tilting modules of projective dimension at most one as faces?

  **Status:** No (unpublished).

- <a id="q27"></a>**Q27. Hearts of intervals.** Can one characterize the hearts $\mathcal T\cap\mathcal U^{\perp_0}$ of torsion intervals $\mathcal U\subseteq\mathcal T$ categorically, without specifying the endpoints? Here $\perp_0$ denotes Hom-orthogonality.

  **Status:** Yes (unpublished).

- <a id="q28"></a>**Q28. Regularity in length categories.** If an essentially small abelian length category has finitely many torsion classes, is its undirected torsion Hasse graph regular?

  **Status:** Yes. Published preprint.

  By [Sentieri, Theorem 2.27 and Corollary 5.2](https://arxiv.org/html/2607.15991v1#S5), finiteness of the torsion lattice implies brick-finiteness, and its Hasse graph is regular. Its degree is the number of simple objects up to isomorphism, as seen at the zero torsion class.

- <a id="q29"></a>**Q29. Beyond module categories.** Which results about torsion classes over Artin algebras extend to arbitrary abelian length categories?

  **Status:** Partial; this is a broader research direction.

- <a id="q30"></a>**Q30. Finite length over non-artinian rings.** What is the structure of torsion classes of finite-length modules over non-Artinian rings, for example commutative Cohen–Macaulay rings?

  **Status:** Open-ended.

## Wide subcategories

- <a id="q31"></a>**Q31. Infinitely many projectives.** Can $\mathsf{mod}\,A$ contain a wide subcategory with enough projectives and infinitely many nonisomorphic indecomposable internal projectives?

  **Status:** Yes (unpublished).

- <a id="q32"></a>**Q32. A bound on semibricks.** Does a common finite bound on the cardinalities of semibricks force $\tau$-tilting finiteness?

  **Status:** Open.

- <a id="q33"></a>**Q33. The strong Sperner property.** For a $\tau$-tilting finite algebra A, is $\mathsf{wide}\,A$ strongly Sperner (with the rank properties of a Peck poset)?

  **Status:** Partial; the general conjecture remains open.

  For the special case of finite Coxeter noncrossing partition lattices, see [Mühle](https://arxiv.org/abs/1509.06942); the corresponding wide-subcategory realization is discussed in [From the lattice of torsion classes …](https://arxiv.org/abs/2201.00595).

- <a id="q34"></a>**Q34. Symmetric Boolean decompositions.** For a $\tau$-tilting finite algebra A, does $\mathsf{wide}\,A$ admit a symmetric Boolean decomposition?

  **Status:** Partial; the general conjecture remains open.

  For published noncrossing-partition cases, see [Mühle](https://arxiv.org/abs/1509.06942) and [Petersen](https://arxiv.org/abs/1108.5761).

- <a id="q35"></a>**Q35. Other lattice properties.** What other order properties do wide-subcategory lattices have, especially in the $\tau$-tilting infinite case?

  **Status:** Open-ended.

- <a id="q36"></a>**Q36. Left finite wide subcategories.** What order properties hold for the left finite wide subcategories, those whose generated torsion class is functorially finite?

  **Status:** Open-ended.

- <a id="q37"></a>**Q37. Realizing the dual lattice.** For every Artin algebra $A$, is there an Artin algebra $B$ whose poset of all wide subcategories is dual to that of $A$?

  **Status:** No (unpublished).

- <a id="q38"></a>**Q38. Gentle algebras.** Is there a combinatorial or surface model for the lattice of all wide subcategories of a gentle algebra?

  **Status:** Open.

## ICE-closed subcategories

Hasse arrows here point from larger to smaller subcategories. The gentle-algebra question appearing in both sections of the original page is listed once, as [Q38](#q38).

- <a id="q39"></a>**Q39. The number of outgoing arrows.** Can one characterize the number of outgoing Hasse arrows at an ICE-closed subcategory, with arrows oriented from larger to smaller subcategories?

  **Status:** Yes (unpublished).

- <a id="q40"></a>**Q40. Cover relations.** Can one characterize the minimal strict inclusions between ICE-closed subcategories?

  **Status:** Yes (unpublished).

- <a id="q41"></a>**Q41. Arrows and Ext-projectives.** For which classes of algebras does every ICE-closed subcategory have as many outgoing arrows as indecomposable Ext-projectives?

  **Status:** Partial; a general classification is not known here.

- <a id="q42"></a>**Q42. Dynkin preprojective algebras.** How many ICE-closed subcategories does an ordinary Dynkin preprojective algebra have?

  **Status:** Computed for ordinary Dynkin preprojective algebras of types A, D and E over algebraically closed fields (unpublished).

- <a id="q43"></a>**Q43. A Lie-theoretic interpretation.** Is there a Lie-theoretic interpretation of the ICE-closed subcategories of ordinary Dynkin preprojective algebras?

  **Status:** Yes in the same Dynkin setting as Q42 (unpublished).

## Extension-closed subcategories

- <a id="q44"></a>**Q44. Infinitely many Ext-projectives.** Can an extension- and summand-closed subcategory have enough Ext-projectives and infinitely many nonisomorphic indecomposable Ext-projectives?

  **Status:** Yes. Published example.

  For $n>1$, the subcategory of $n$-preprojective modules over an $n$-representation-infinite algebra has infinitely many indecomposables with pairwise vanishing $\operatorname{Ext}^1$, including self-extensions. Thus it is extension-closed with the split exact structure and all its objects are relatively projective and injective. See [Herschend–Iyama–Oppermann, Question 1.2 and §4](https://arxiv.org/abs/1205.1272). Thanks to Sondre Kvamme for pointing out this example.

- <a id="q45"></a>**Q45. Finiteness of Ext-projectives.** Does every functorially finite extension- and summand-closed subcategory of $\mathsf{mod}\,A$ have only finitely many indecomposable Ext-projectives?

  **Status:** No (unpublished).

- <a id="q46"></a>**Q46. Finiteness of Ext-injectives.** Does every functorially finite extension- and summand-closed subcategory of $\mathsf{mod}\,A$ have only finitely many indecomposable Ext-injectives?

  **Status:** No (unpublished).

- <a id="q47"></a>**Q47. Equality of the two numbers.** In such a functorially finite extension- and summand-closed subcategory, do the numbers of indecomposable Ext-projectives and Ext-injectives coincide?

  **Status:** Open.

- <a id="q48"></a>**Q48. Further classifications.** Which additional classes of subcategories of module categories admit useful classifications?

  **Status:** Partial; this is a broader classification program.

- <a id="q49"></a>**Q49. Images and extensions.** Can one classify image- and extension-closed subcategories over nonhereditary algebras?

  **Status:** A general categorical characterization is published; a finer classification remains open.

  [Enomoto–Sakai, Proposition 2.3](https://arxiv.org/html/2208.13937#S2) characterizes IE-closed subcategories as intersections of a torsion class and a torsion-free class, without assuming heredity. The two classes need not form a torsion pair.

## Higher homological algebra

- <a id="q50"></a>**Q50. Classifying higher exact structures.** Can all $n$-exact structures on a given additive category be classified, for every $n\geq 1$?

  **Status:** Yes; the higher case is unpublished.

  For $n=1$, see the classification by Serre subcategories of the defect category in [Classifying substructures of extriangulated categories via Serre subcategories](https://arxiv.org/abs/2005.13381), for skeletally small additive categories.

- <a id="q51"></a>**Q51. A maximum exact structure.** Does every additive category admit a greatest $n$-exact structure for every $n\geq 1$?

  **Status:** Yes; the full generality beyond the published cases below is unpublished.

  See [Rump](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/214/1/89069/on-the-maximal-exact-structure-of-an-additive-category) for $n=1$ and [Klapproth](https://arxiv.org/abs/2410.05242) for idempotent-complete additive categories in higher degrees.

## Grothendieck monoid

- <a id="q52"></a>**Q52. Torsion classes in Dynkin type.** Can one compute the Grothendieck monoid of every torsion class over a Dynkin path algebra?

  **Status:** Yes (unpublished).

- <a id="q53"></a>**Q53. Torsion-free classes in Dynkin type.** Can one compute the Grothendieck monoid of every torsion-free class over a Dynkin path algebra?

  **Status:** Yes (unpublished).

- <a id="q54"></a>**Q54. Reducedness.** Are the Grothendieck monoids in [Q52–Q53](#q52) reduced, meaning that their only additive unit is zero?

  **Status:** Yes. In fact this holds for every skeletally small exact category.

  See [Enomoto–Saito, Proposition 6.2](https://arxiv.org/html/2208.02928v2#S6): the exact-category case has no invertible element other than zero.

- <a id="q55"></a>**Q55. Extriangulated computations.** How can Grothendieck monoids of extriangulated categories be computed, especially for extension-closed subcategories of triangulated categories?

  **Status:** Partial. Some cases have a published formula.

  For the intermediate subcategory $\mathcal F[1]*\mathcal A$ associated to a torsion-free class $\mathcal F$ of an abelian category $\mathcal A$, [Enomoto–Saito, Theorem 5.4](https://arxiv.org/html/2208.02928v2#S5) computes its monoid by inverting the classes of the objects of $\mathcal F$ in $\mathsf M(\mathcal A)$.

- <a id="q56"></a>**Q56. Invertible classes.** Which objects of an extriangulated category represent invertible elements of its Grothendieck monoid?

  **Status:** Yes, there is a categorical characterization. Published preprint.

  [Enomoto–Saito, Proposition 6.1](https://arxiv.org/html/2208.02928v2#S6) identifies the objects representing units as precisely those of the smallest Serre subcategory.

- <a id="q57"></a>**Q57. Realizing the group and reduced parts.** Can the quotient of an extriangulated category’s Grothendieck monoid by its group of units be realized categorically by localization or a decomposition into exact and triangulated parts?

  **Status:** Partial; the general question remains open.

  [Enomoto–Saito, §6](https://arxiv.org/html/2208.02928v2#S6) discusses the general problem. The characterization of units in [Q56](#q56) is not a general categorical quotient construction.

## Lean Theorem Prover

**Teaching Auslander-Reiten theory to computer** using [Lean](https://leanprover.github.io/), see also [Lean community](https://leanprover-community.github.io/), and a very good introductory material [Formalising Mathematics](https://github.com/ImperialCollegeLondon/formalising-mathematics)

## SageMath

- Create a system which can deal with the Auslander-Reiten quivers as translation quivers. In particular, compute the dimension of Hom spaces using AR quiver.
- Create or modify programs which enables us to deal with string and band modules over special biserial (or string) algebras.
- More concretely, develop a SageMath version of [String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/)!

I know that [QPA](https://folk.ntnu.no/oyvinso/QPA/) are useful, but I think there's no special functions which can applied to special biserial, string, gentle algebras. Since SageMath can deal with other materials including posets, polytopes, lattices, root system, and so on (and since it's written in Python), I hope that special computational experiments on e.g. string algebras can be done inside SageMath.
