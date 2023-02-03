---
layout: single
title: "Programs"
permalink: /codes/
author_profile: true
toc: true
---

{% include base_path %}

I'm interested in realizing, computing and expressing various objects in the representation theory of algebra using computer, especially using [SageMath](https://www.sagemath.org/) and Theorem prover [Lean](https://leanprover.github.io/).

## Generator of finite congruence-uniform lattices in SageMath
Generate all finite congruence-uniform lattices (with a limitation of the number of join-irreducibles if necessary) in SageMath, by iterating Day's interval doubling construction.
<https://gist.github.com/haruhisa-enomoto/8a16c926c66e0ea5a4f7f9f4744d7c21>

(I used this to find a counterexample of congruence-uniform lattices which are not isomorphic to the lattice of torsion classes.)

## AR quiver calculator

A tool to deal with the Auslander-Reiten quiver of a module category or a triangualted category.

![](https://cdn.discordapp.com/attachments/524877289213788171/1007891731703943168/unknown.png)

(The Auslander-Reiten quiver of mod k(D5), a torsion class of it, and Ext-projectives of it)

You can input your translation quiver by your mouse and keyboard, save and load your translation quiver, and import the AR quiver from [String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/).

Then this computes various things.

- Compute Hom and Ext^1
- For a module category, this computes all torsion(-free) classes, wide subcategories, ICE-closed subcategories (closed under Image, Cokernel, Extensions), IE-closed subcategories (closed under Images, Extensions), etc,
- and its Ext-projective (injective) objects.
- For a triangulated category, this computes a shift functor, and list all maximal Ext-orthogonal objects.

See [GitHub Readme](https://github.com/haruhisa-enomoto/ARquiver#readme) for details and examples.

### Links
- [Follow this link](https://github.com/haruhisa-enomoto/ARquiver#readme) for Windows and Mac.
- [GitHub Repository](https://github.com/haruhisa-enomoto/ARquiver)

## Representation theory of algebra in Lean
I'm trying to formalize representation theory of algebra (especially Auslander-Reiten theory) using a proof assistant [Lean](https://leanprover.github.io/). For those who don't know a proof assistant, it's like a **computer game for proving theorems**, so write a programming code which states and proves theorems.

What I have done so far in [lean-noncommutative-ring](https://github.com/haruhisa-enomoto/lean-noncommutative-ring) is

- The left right symmetry of Jacobson radical of a ring (intersection of maximal left ideals coincides that of maximal right ideals), and a well-known characterization of elements in the Jacobson radical
- The left right symmetry of local ring (ring has a unique maximal left ideal iff it has a unique maximal right ideal), and a well-known characterization of local rings.

Obviously there are lots of things to play with Auslander-Reiten theory in Lean, so if you are interested in this game project, please contact me.

See also:
- [Natural number game](https://www.ma.imperial.ac.uk/~buzzard/xena/natural_number_game/) and [its mirror](https://cbirkbeck.github.io/natural_number_game/). A very funny game for proving basic statements (associativity, commutativity, etc) from Peano's axioms. Very gentle and instructive, so no prerequisite knowledge is needed.
- [Formalising Mathematics](https://github.com/ImperialCollegeLondon/formalising-mathematics), which explains basics of Lean from undergraduate materials like set theory and group theory
- [Lean community](https://leanprover-community.github.io/)

## The lattice of torsion classes in SageMath
`tors_lattice.py` below enables us to compute and construct various objects from the lattice of torsion classes of a &tau;-tilting finite algebra in SageMath. Internally, this defines a class `FiniteTorsLattice`, which is a subclass of a SageMath class for finite lattices: [`FiniteLatticePoset`](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/posets/lattices.html#sage.combinat.posets.lattices.FiniteLatticePoset).

Once you input the lattice of torsion classes (e.g. using my [StringApplet-to-SageMath-converter](https://github.com/haruhisa-enomoto/StringApplet-to-SageMath-converter) below), this program can compute (or construct) various objects which naturally arise in the representation theory of algebras in SageMath, such as the lattice of wide subcategories, the lattice of ICE-closed subcategories, the simplicial complex of support &tau;-tilting modules, and the number of indecomposable Ext-projectives of each torsion class or a heart of each interval, and so on.

- [tors_lattice.py](/files/tors_lattice.py)
- [Manual](https://nbviewer.jupyter.org/github/haruhisa-enomoto/tors-lattice/blob/main/Manual.ipynb)
- [GitHub Repository](https://github.com/haruhisa-enomoto/tors-lattice)
- [An introduction video](https://www.youtube.com/watch?v=2-y1a-_zEEA) based on the second part of [my talk](/talks/2021-07-26/)
- [Slides](/files/OCAMI0726.pdf) used in the above video
- [A Demo Notebook](https://nbviewer.jupyter.org/urls/haruhisa-enomoto.github.io/files/OCAMI_Demo.ipynb) used in the above video, and its [ipynb file](/files/OCAMI_Demo.ipynb)

## StringApplet to SageMath converter
This enables us to import the **lattice of torsion classes** in SageMath from **[String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/)**. [String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/) can compute the Hasse quiver of torsion classes for an inputted algebra (which should be representation-finite special biserial).
This module makes a data which we can use to construct and study the lattice of torsion classes in SageMath (e.g. the kappa map below), from the TeX file exported by String Applet.

- [converter.py](/files/converter.py)
- [Manual](https://nbviewer.jupyter.org/github/haruhisa-enomoto/StringApplet-to-SageMath-converter/blob/main/Manual.ipynb)
- [GitHub Repository](https://github.com/haruhisa-enomoto/StringApplet-to-SageMath-converter)


## Kappa maps for lattices
This adds methods to
a Sage class [`FiniteLatticePoset`](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/posets/lattices.html#sage.combinat.posets.lattices.FiniteLatticePoset)
which compute the (extended) kappa (dual) map.
Using this, one can compute kappa maps for finite lattices in SageMath.

- [GitHub Repository](https://github.com/haruhisa-enomoto/kappa-map-for-lattices)
- [Manual](https://nbviewer.jupyter.org/github/haruhisa-enomoto/kappa-map-for-lattices/blob/main/Manual.ipynb)
- [Notes for representation theorists](https://nbviewer.jupyter.org/github/haruhisa-enomoto/kappa-map-for-lattices/blob/main/for-rep-theorists.ipynb):
I **strongly recommend you to read this** if you are working with representation theory of algebras, not just a lattice theory: this explains how the kappa map arises in the rep-theory, and demonstrates how to use it to study bricks and torsion classes.
