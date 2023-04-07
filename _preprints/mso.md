---
title: "Maximal self-orthogonal modules and a new generalization of tilting modules"
excerpt: "Study maximal self-orthogonal modules, a new generalization of tilting modules = projectively Wakamatsu tilting modules, and Wakamatsu tilting modules"
date: 2023-02-01
arxiv: "2301.13498"
citation: "H. Enomoto, Maximal self-orthogonal modules and a new generalization of tilting modules, arXiv:2301.13498."
---

## Comment

I study self-orthogonal modules using so-called **projective Wakamatsu tilting modules** and their relation to Wakamatsu tilting modules and maximal self-orthogonal modules.

$T$ is **projectively Wakamatsu tilting** if $T$ is an Ext-progenerator of the category $T^\perp$ consisting of $X$ with $\operatorname{Ext}^{>0}(T, X) = 0$.
Then we have

{tilting} $\subseteq$ {projectively Wakamatsu tilting} $\subseteq$ {Wakamatsu tilting}.

My interest is mainly in the representation-finite case, and I show that the following are equivalent for $T \in \mathsf{mod} \, \Lambda$ if $\Lambda$ is representation-finite.

1. $T$ is projectively Wakamatsu tilting.
1. $T$ is Wakamatsu tilting.
1. $T$ is maximal self-orthogonal module, that is, self-orthogonal, and if $T \oplus M$ is self-orthogonal, then $M \in \mathsf{add} \, T$ holds.
1. $T$ is self-orthogonal with $\|M\| = \|\Lambda\|$.

3rd and 4th conditions are convenient for actual computation. I give many examples in this paper using a computer program (which I developed but in preparation). This was the initial motivation of this paper (I was wondering how to compute all Wakamatsu tilting modules over rep-fin algebras).

Also, this has applications in Gorenstein homological algebra (e.g. this immediately deduces the fact that the category of Gorenstein-projective modules coincide with $^\perp \Lambda$ if $^\perp\Lambda$ has only finitely many indecomposables).

I also study a binary relation on the set of projectively Wakamatsu tilting modules, defined by the vanishing of Ext, so generalizing the poset of tilting modules.
Unfortunately, **this is not a poset even if the algebra is rep-fin**, and I gave such an example.
Using this relation, I prove that any self-orthogonal module over an Iwanaga-Gorenstein algebra $\Lambda$ has finite projective dimension if $\Lambda$ is representation-finite (I think there may be a direct proof, but I cannot find it).

Some conjectures related on self-orthogonal modules are discussed in detail.

## Presentation materials

- [Notes](/files/2023-03-23.pdf) and [talk video](https://youtu.be/_E9nPEs-WV4) from [this talk](/talks/2023-03-23/)

- [Notes](/files/2023-02-27.pdf) from [this talk](/talks/2023-02-27/)
