---
layout: archive
title: "Notes and programs"
permalink: /others/
author_profile: true
---

{% include base_path %}

## Notes

### Theses
- Bachelor thesis: [On categories of modules over locular categories (in Japanese)](/files/sotsuron.pdf).

  Contents:
  - Most of contents are probaly folklore. I considered the correspondence between semiperfect ring, Krull-Schmidt categories and their indecomposable parts in a functorial way, and studied a  **perfect** additive category, a category such that every module over it has a projective cover.

- Master thesis: [Relative Auslander correspondence via exact categories](/files/master_thesis.pdf), [Talk video in VR](https://youtu.be/ENQNdLAF_NE), [Talk slide](/files/mt0130.pdf).

  Contents: just a combination of the following papers, together with an introductory chapter.
  - [Classifying exact categories via Wakamatsu tilting](/papers/wakamatsu/)
  - [Classifications of exact structures and Cohen-Macaulay-finite algebras](/papers/exact-str/)

- Doctoral thesis: [Categorical Properties and Classifications of Several Subcategories of Module Categories](/files/phd_thesis.pdf)

  Contents: just a combination of the following papers, together with an introductory chapter.
  - [Relations for Grothendieck groups and representation-finiteness](/papers/relations/)
  - [The Jordan-H&ouml;lder property and Grothendieck monoids of exact categories](/papers/JHP/)
  - [Bruhat inversions in Weyl groups and torsion-free classes over preprojective algebras](/papers/binv/)
  - [Monobrick, a uniform approach to torsion-free classes and wide subcategories](/papers/mbrick/)
  - [Rigid modules and ICE-closed subcategories in quiver representations](/papers/rigidICE/)

## Notes (in Japanese)
I do NOT guarantee the rigorousness of the following notes.

- [Grothendieckアーベル圏の基礎事項(未完), (Basics on Grothendieck abelian categories)](/files/GrothendieckAbelian0205.pdf), last modified: 2019-02-05.

  Grothendieckアーベル圏やアーベル圏一般論についての自分用の昔に書いたまとめ（書きかけ）です。アーベル圏の局所化やAb条件や、関連する束論（モジュラー束とか）についてフランクに書いてます。気が向いたらせめてGabriel-Popescuくらいまではやりたいですが気力がないので誰か続きを書いてください。

- [可換環上の（非可換）代数上の加群のメモ（未完）, (Notes on modules over non-commutative algebras over a commutative ring)](/files/comm-order1205.pdf), last modified: 2019-12-05.

  可換環上の加群やそれ上のネーター代数について、自分なりに整理してまとめようとしたメモ（書きかけ）です。可換環の次元についてやら、Bass数についてやら、可換環上のCM整環やらについて。中途半端に終っています。

## Programs
I'm a beginner in Python and Sage math. Some programs will be available in the near future...

### In preparation

#### Nakayama algebras
A Python code which focuses on the representation theory of **Nakayama algebras** such that we can deal with various subcategories and their properties.

#### Preprojective algebras of Dynkin type
A Sage math code which can deal with torsion classes, torsion-free classes, bricks and brick labeling, and simple objects of torsion(-free) classes, the validity of (JHP), and so on.

#### From torsion class to ICE-closed subcategories
A Sage math code which can compute the number of ICE-closed subcategories over a $\tau$-tilting finite algebra when the poset of torsion classes are given. Maybe I expect that we can also determine the poset structure.
