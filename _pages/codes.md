---
layout: archive
title: "SageMath codes"
permalink: /codes/
author_profile: true
---

{% include base_path %}

I'm a beginner of Python and [SageMath](https://www.sagemath.org/)...

## StringApplet to SageMath converter
This enables us to import the **lattice of torsion classes** in SageMath from **[String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/)**. [String Applet](https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/) can compute the Hasse quiver of torsion classes for a inputted algebra (which should be representation-finite special biserial).
This module makes a data which we can use to construct and study the lattice of torsion classes in SageMath (e.g. the kappa map below), from the tex file exported by String Applet.

- [GitHub Repository](https://github.com/haruhisa-enomoto/StringApplet-to-SageMath-converter)
- [Manual](https://github.com/haruhisa-enomoto/StringApplet-to-SageMath-converter/blob/main/Manual.ipynb)



## Kappa-maps-for-lattices
This adds methods to
a Sage class [`FiniteLatticePoset`](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/posets/lattices.html#sage.combinat.posets.lattices.FiniteLatticePoset)
which compute the (extended) kappa (dual) map.
Using this, one can compute kappa maps for finite lattices in SageMath.

- [GitHub Repository](https://github.com/haruhisa-enomoto/kappa-map-for-lattices)
- [Manual](https://github.com/haruhisa-enomoto/kappa-map-for-lattices/blob/main/Manual.ipynb)
- [Notes for representation theorists](https://github.com/haruhisa-enomoto/kappa-map-for-lattices/blob/main/for-rep-theorists.ipynb):
I **strongly recommend you to read this** if you are working with representation theory of algebras, not just a lattice theory: this explains how the kappa map arises in the rep-theory, and demonstrates how to use it to study bricks and torsion classes.
