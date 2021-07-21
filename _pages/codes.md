---
layout: archive
title: "SageMath codes"
permalink: /codes/
author_profile: true
---

{% include base_path %}

I'm interested in realizing and expressing various objects in the representation theory of algebra using computer, especially using [SageMath](https://www.sagemath.org/).

## The lattice of torsion classes in SageMath
`tors_lattice.py` below enables us to compute and construct various objects from the lattice of torsion classes of a &tau;-tilting finite algebra in SageMath. Internally, this defines a class `FiniteTorsLattice`, which is a subclass of a SageMath class for finite lattices: [`FiniteLatticePoset`](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/posets/lattices.html#sage.combinat.posets.lattices.FiniteLatticePoset).

Once you input the lattice of torsion classes (e.g. using my [StringApplet-to-SageMath-converter](https://github.com/haruhisa-enomoto/StringApplet-to-SageMath-converter) below), this program can compute (or construct) various objects which naturally arise in the representation theory of algebras in SageMath, such as the lattice of wide subcategories, the lattice of ICE-closed subcategories, the simplicial complex of support &tau;-tilting modules, and the number of indecomposable Ext-projectives of each torsion class or a heart of each interval, and so on.

- [tors_lattice.py](/files/tors_lattice.py)
- [Manual](https://nbviewer.jupyter.org/github/haruhisa-enomoto/tors-lattice/blob/main/Manual.ipynb)
- [GitHub Repository](https://github.com/haruhisa-enomoto/tors-lattice)

*(TO DO: write a user's guide for representation-theorists)*


## StringApplet to SageMath converter
This enables us to import the **lattice of torsion classes** in SageMath from **[String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/)**. [String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/) can compute the Hasse quiver of torsion classes for an inputted algebra (which should be representation-finite special biserial).
This module makes a data which we can use to construct and study the lattice of torsion classes in SageMath (e.g. the kappa map below), from the tex file exported by String Applet.

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
