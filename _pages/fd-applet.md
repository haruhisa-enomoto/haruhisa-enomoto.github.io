---
layout: single
classes: wide-no-author
title: "FD Applet - an applet for Finite-Dimensional algebras"
permalink: /fd-applet/
author_profile: false
toc: true
toc_sticky: true
---

[(日本語版)](/fd-applet-ja/)

## Online Version

You can use FD Applet from your browser [here](https://fd-applet.dt.r.appspot.com/):
- <https://fd-applet.dt.r.appspot.com/>

Our online version might be a bit slow sometimes and you might run into some connection issues.

For an optimized experience, consider installing our local version from this page.

## FD Applet Usage Examples

![FD Applet 1](/assets/images/fd-applet/fd-applet1.jpg)

**Info Tab**: Basic Info (and AR quiver) of this algebra

![FD Applet 2](/assets/images/fd-applet/fd-applet2.jpg)

**Calculator Tab**: Calculation of Ext^1 between modules

![FD Applet 3](/assets/images/fd-applet/fd-applet3.jpg)

**Enumerator Tab**: There are 255,364 τ-rigid modules!

![FD Applet 4](/assets/images/fd-applet/fd-applet4.jpg)

**Converter Tab**: Convert a support τ-tilting module to the corresponding semibrick

![FD Applet 5](/assets/images/fd-applet/fd-applet5.jpg)

**Quivers Tab**: The Hasse quiver of resolving subcategories

## About FD Applet

FD Applet is a PC application that, from your inputted algebra, performs various calculations related to modules, enumerates specific modules and subcategories of module categories, and generates the AR quiver and various Hasse quivers and so on.

This guide covers the installation and usage instructions for FD Applet on Windows, Mac, and other systems.

### Implementation

The implementation consists of a server backend using Kotlin, a frontend using React, and scripts for update verification, automatic updating, and startup assistance. The source code will be published in the future. The development of the app and the creation of this documentation have greatly benefited from the support of ChatGPT.

**Source codes**

- [GitHub Repository](https://github.com/haruhisa-enomoto/fd-applet)

## Changelog

- 2023-06-27: Released version 0.3.2. Add the computation of wide τ-tilting modules and its Hasse quiver (via the corresponding Hasse quiver of ICE-closed subcategories). Also for possibly heavy calculation, show the actual computation time.

- 2023-06-05: Released version 0.3.0.
  - New Tab: **Converter**, which computes various modules/subcategories from a given modules/subcategories (the smallest torsion class containing a module, Ext-projs of subcategories, various bijections in τ-tilting theory, etc)
  - Some UI improvements. Add physics settings to the AR quiver.

- 2023-04-15: Released version 0.2.1. Minor UI fixes, and add online demo.

- 2023-04-14: Released version 0.2.0. UI updates (mainly for the AR quiver), and added "projectively/injectiely stable Hom" calculator.

- 2023-04-07: Released version 0.1.2. Minor UI fixes.

- 2023-04-06: Released version 0.1.1. Fixed UI and behavior:

  - Added "Zoom" options for quivers (default: disabled), allowing users to choose whether scrolling in a quiver will zoom or not.
  - When the browser or the tab is closed, the server will now shut down automatically.

- 2023-04-04: Released the initial version 0.1.0.

## Installation

0. **Install the Java environment (JDK 17):**
   If you have no preference, it's easy to download and install the "Latest LTS Release" from <https://adoptium.net/>. (Then you can install it with the default settings without changing anything during the installation process.)

1. **Download the appropriate zip file for your system:**

   - Windows: [Download Windows zip](/files/fd-applet-win.zip)
   - Mac: [Download Mac zip](/files/fd-applet-mac.zip)
   - Others (and Expert Users): [Download zip](/files/fd-applet-others.zip)
   - Fat Jar file only: [fd-applet-fat.jar](/files/fd-applet-fat.jar)

2. **Extract the downloaded zip file.**

### Directory Structure

The extracted directory contains the following files and folders:

- Windows: `fd-applet.bat`
- Mac: `fd-applet.command`, `initial-setup.scpt`
- `examples` folder: contains examples of algebras. See [Open and Save](#open-and-save) for how to use them.
- `lib` folder: contains a java file `fd-applet-fat.jar`. **Do not double-click it.**

## Launching FD Applet

{% capture notice-text %}

### Important Notes

- **Do not double-click `fd-applet-fat.jar`.** Launching it either won't work or, if it does, you won't be able to close it. Always double-click `fd-applet.bat` (Windows) or `fd-applet.command` (Mac) instead, or follow the instructions for [other operating systems](#other-os-or-advanced-users).
- If you encounter errors in your browser such as "Unable to access the site" or "Cannot connect to the server," please wait a few seconds before refreshing your browser.

{% endcapture %}

<div class="notice--danger">
  {{ notice-text | markdownify }}
</div>

### Windows Users

1. Double-click `fd-applet.bat` to launch the app.
   (This file automatically checks for updates, runs `fd-applet-fat.jar`, and opens <http://localhost:8080> in your browser.)

### Mac Users

1. For the first time only, open `initial-setup.scpt` and click the Run button (the triangle icon) in the Script Editor (to grant `fd-applet.command` execute permissions).
2. Double-click `fd-applet.command` to launch the app.
   (This file automatically checks for updates, runs `fd-applet-fat.jar`, and opens <http://localhost:8080> in your browser.)

3. On the first launch, you may need to allow the app to run by following these steps:
   - Go to System Preferences > Security & Privacy.
   - Click the "Open Anyway" button next to the message about the app being from an unidentified developer.

### Other OS or Advanced Users

1. `lib/fd-applet-fat.jar` is the main body of FD Applet. After installing the Java environment, execute the command `java -jar fd-applet-fat.jar` (from `lib` directory) to start the server.
   **Do not double-click the jar file. You won't be able to close the server.**
2. Once the server is up and running, access <http://localhost:8080> in your browser to use FD Applet.
3. Note that in this case, the app will not be updated automatically. If a message appears on the screen indicating that a newer version is available, manually download [fd-applet-fat.jar](/files/fd-applet-fat.jar) and replace the one in the `lib` folder.

### Closing FD Applet

To close the app, simply close the browser (or the tab). Starting from version 0.1.1, the background server will shut down automatically when the browser is closed, so you no longer need to close the terminal manually.

## Usage

([日本語版](/fd-applet-ja/#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95))

TL;DR:

1. Input your algebra (quiver, monomial/commutative relations) in the left input area.
2. Click Update button, then use right tabs (Info, Calculator, Enumerator, Converter, Quivers).
3. Most features only work for a finite-dimensional special biserial algebra (e.g. a gentle or string algebra); In addition, Enumerator, Converter, and Quiver tabs only work for a representation-finite algebra.

### Input Your Algebra

Enter your algebra in the left input area.
Input Nakayama algebra from Kupisch series via "File" menu if needed.

#### Quiver

- Add vertices: click canvas.
- Add arrows: click source vertex, then target vertex (or empty space for a new target vertex).
- Delete vertices/arrows: use Delete or Backspace key, or middle "Delete selected item" button.
- Fit canvas: left "Fit" button.
- Clear all: right "Clear all" button.

#### Relation

_Supported: monomial and commutative relations only._

- Monomial relation: write `ab`, `a b`, or `a*b` for the path `-a-> -b->`.
- Commutative relation: write expressions like `ab-cd` or `a * b - c * d`.

#### Update

Click Update button to finish.

#### Open and Save

You can save your algebra by selecting "File" > "Save" menu, and load a saved algebra using "Open."

For example, when you choose a file from within the `examples` folder using "Open," a quiver and relations will be loaded automatically.

### Right Tabs

- Input algebra, press "Get Data" button to use each tab.

- Toggle the "Show AR Quiver" switch to determine whether the AR quiver should be displayed (for all tabs) or not. Click on "Compute AR Quiver" to actually show the AR quiver.

Indecomposable module notation:

- `1`, `2`: the simple modules at `1` and `2`.
- `a*b*!c`: the string module `1 -a-> 2 -b-> 3 <-c- 4`.
- `a*b=d*e`: the biserial module with commutative square `-a->-b-> = -d->-e->`.

#### Info

Displays basic info: homological dimensions, projective/injective modules, etc.

(Most features only work for finite-dimensional special biserial algebras.)

#### Calculator

Calculates things like dimensions of Hom or Ext and projective resolutions based on input (e.g. `dim Ext^2(a*b + c*d*e, f*g)`).

(Most features only work for finite-dimensional special biserial algebras.)

#### Enumerator

- Enumerates modules/subcategories (e.g. tilting modules, semibricks). Show distribution with "Show Distribution" button.
- When the AR quiver is diaplayed, if a module/subcategory is selected, it is colored. Highlight Ext-projectives/injectives in the chosen subcategory.

(Only Works for representation-finite special biserial algebras.)

#### Converter

From a given module or subcategories, you can compute another module or subcategory by various operations. For example:
- Given a subcategory, compute the smallest torsion class containing it (or torsion-free class, ICE-closed subcategory, wide subcategory, etc).
- Given a torsion class, compute the corresponding wide subcategory (under Marks-Stovicek) (and various other bijections in τ-tilting theory).
- Given an extension-closed subcategory, compute the Ext-projectives of it.
- and lots of other operations!

#### Quivers

- Displays quivers related to algebra (e.g. τ-tilting quiver, Hasse quivers of various subcategories).
- When the AR quiver is diaplayed, the selected module/subcategory in the quiver is colored in the AR quiver.

(Only Works for representation-finite special biserial algebras.)

## Support

If you have any questions or issues or feature requests (e.g., a function to perform a specific calculation or a question about whether a certain calculation is possible), please use the menu's Files > "Send Feedback or report issues" option, or send an email to `henomoto [at] omu.ac.jp`.
