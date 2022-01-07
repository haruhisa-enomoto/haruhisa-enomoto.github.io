---
layout: single
title: "Problems"
permalink: /problems/
author_profile: true
toc: true
toc_label: "My Table of Contents"
---

{% include base_path %}

In this page, I raise some problems in the representation theory of algebras, which are interesting to me, but which seem so difficult that I can't answer by myself. I hope someone will solve (or at least consider) them.

**I DO NOT claim the originality of the problems below**, hence you're free to solve and write papers about them. But I'm happy if you contact me if you have some ideas to approach these problems.

## Torsion classes

- Is there an analogue of $\tau$-tilting theory for exact categories?
More precisely, can we classify torsion classes of exact categories using projective objects?

- Is there a purely poset-theoretical characterization of torsion classes in the poset of torsion classes which are
  - functorially finite?
  - faithful?
  - functorially finite and faithful (thus corresponds to a tilting module)? In particular, can we construct the simplicial complex of tilting modules only using the poset structure?

- Is there a categorical characterization of the heart of intervals in the poset of torsion classes (Tattar's twin torsion heart)?

- If we consider $\tau$-tilting finite algebras, then the Hasse quiver of the poset of torsion classes is a regular graph by the theory of mutation (Adachi-Iyama-Reiten). On the other hand, if we consider an arbitrary abelian length category, some properties of torsion classes of artin algebras are also satisfied (mainly those about bricks), e.g. DIRRT's brick labeling and bijection between join-irreducible torsion classes and bricks, Asai-Pfeifer's characterization of wide intervals, and a bijection between torsion classes and wide subcategories provided that there are only finitely many torsion classes (see [my paper](/papers/mbrick/)). Thus,
  - Is the Hasse quiver of torsion classes of an abelian length category a regular graph if there are only finitely many torsion classes?
  - To what extent can we generalize many papers on the poset of torsion classes over artin algebras?
  - It is interesting to investigate torsion classes in the category of modules with finite length over non-artinian ring (e.g. commutative Cohen-Macaulay ring, etc.).

## Wide subcategories

- Is there any wide subcategory $\mathcal{W}$ in the module category of an artin algebra such that $\mathcal{W}$ has enough projectives and there are **infinitely many indecomposable projective objects** in $\mathcal{W}$?

- Suppose that there is a common upper bound on the cardinality of semibricks. Then is this algebra necessarily $\tau$-tilting finite? (The converse of course holds by the result of e.g. Asai.)

- By computer computation, I conjecture that for $\tau$-tilting finite case, the lattice of wide subcategory
  - is strongly Sperner, or more strongly,
  - has a symmetric Boolean decomposition
Since the non-crossing partition lattice and the shard intersection lattice are realized as lattices of wide subcategories, this will unify several known results by combinatorialists.
- Or are there more properties such that the lattice of wide subcategory has? Especially, what can be said if we consider $\tau$-tilting infinite case, or we only consider left finite wide subcategories?
- For the hereditary case, there is a self-duality on the lattice of wide subcategories. For a general algebra $\Lambda$, is there any algebra $\Gamma$ such that the lattices of wide subcategories over $\Lambda$ and $\Gamma$ are dual to each other? This will make things easier to deal with.
- Is there a combinatorial (or surface) model for the lattice of wide subcategories over gentle algebras?

## ICE-closed subcategories

- Characterize the number of Hasse arrows starting at an ICE-closed subcategory in the poset of ICE-closed subcategories, or characterize a Hasse arrow (minimal inclusion of ICE-closed subcategories). In the poset of torsion classes, the number of arrows starting at a torsion class is equal to the number of indecomposable split projective objects (for $\tau$-tilting finite case). I and Sakai conjectured that the number of Hasse arrows is equal to the number of indecomposable projective objects in the case of ICE-closed subcategories, which are true for Dynkin path algebras (by [our paper](/papers/ice/)) and Nakayama algebras (in preparation), but the computer experiment shows that this conjecture is not true in general. Thus
  - Is there any class of algebras such that this conjecture is true?

- Is there a combinatorial (or surface) model for the lattice of wide subcategories over gentle algebras?
- How many ICE-closed subcategories the preprojective algebras of Dynkin type have? Is there any Lie-theoretic interpretation of ICE-closed subcategories?

## Extension-closed subcategories

- Is there any extension-closed subcategory (closed under summands) $\mathcal{E}$ in the module category of an artin algebra such that $\mathcal{E}$ has enough projectives and there are **infinitely many indecomposable projective objects** in $\mathcal{E}$?

- Let $\mathcal{E}$ be a functorially finite extension-closed subcategory of the module category of an artin algebra. Then it's known that $\mathcal{E}$ has both enough projectives and enough injectives. Are the numbers of indecomposable projectives and injectives finite in this case? And do the numbers coincide?

- Are there any classes of subcategories which we can classify?

- Suppose that we are given the Auslander-Reiten quiver of the module category. Can we compute all subcategories which are closed under extensions and direct summands only using the combinatorial data?

## Higher homological algebra
Can we classify all the possible structure of $n$-exact categories on a given additive category like [my paper on exact structures](/papers/exact-str/)?
In particular, does the unique maximum $n$-exact structure always exists?

## Grothendieck monoid

- Compute the Grothendieck monoids of a special class of exact categories, for example, torsion(-free) classes over path algebras of Dynkin type, or even type A. In particular, are these monoids reduced?

- We can define the Grothendieck monoids of extriangulated categories. It seems that triangulated categories behave in contrast to exact categories with respect to the Grothendieck monoid, e.g. the Grothendieck monoid of exact categories is always reduced (invertible element is only 0), but every element is invertible in the Grothendieck monoid of triangulated category. Therefore,
  - Is there any way to compute the Grothendieck monoids of extriangulated categories (at least those embedded in some triangulated categories)?
  - Is there any characterization of objects whose images in the Grothendieck monoid are invertible?
  - Since the Grothendieck monoid is a commutative monoid, it is a direct sum of an abelian group and a reduced group uniquely. It would be very nice if such a factorization can be realized categorically (e.g. describe an extriangulated category as a some kind of semi-direct product of a triangulated category and an exact category).

## Lean Theorem Prover
**Teaching Auslander-Reiten theory to computer** using [Lean](https://leanprover.github.io/), see also [Lean community](https://leanprover-community.github.io/), and a very good introductory material [Formalising Mathematics](https://github.com/ImperialCollegeLondon/formalising-mathematics)

## SageMath
- Create a system which can deal with the Auslander-Reiten quivers as translation quivers. In particular, compute the dimension of Hom spaces using AR quiver.
- Create or modify programs which enables us to deal with string and band modules over special biserial (or string) algebras.
- More concretely, develop a SageMath version of [String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/)!

I know that [QPA](https://folk.ntnu.no/oyvinso/QPA/) are useful, but I think there's no special functions which can applied to special biserial, string, gentle algebras. Since SageMath can deal with other materials including posets, polytopes, lattices, root system, and so on (and since it's written in Python), I hope that special computational experiments on e.g. string algebras can be done inside SageMath.
