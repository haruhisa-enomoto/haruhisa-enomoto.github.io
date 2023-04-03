---
layout: single
classes: wide
title: "FD Applet - Installation and Usage Guide"
permalink: /fd-applet/
author_profile: false
---

{% include base_path %}

[(日本語版)](/fd-applet-ja/)

This guide covers the installation and usage instructions for FD Applet on Windows, Mac, and other systems.

## Usage

TODO

## System Requirements

- JDK 17: Install the latest Java environment (JDK 17). If unsure, download and install the "Latest LTS Release" from <https://adoptium.net/>.

## Installation

1. **Download the appropriate zip file for your system:**

   - Windows: [Download Windows zip](/files/fd-applet-win.zip)
   - Mac: [Download Mac zip](/files/fd-applet-mac.zip)
   - Others (and Expert Users): [Download zip](/files/fd-applet-others.zip)
   - Fat Jar file only: [fd-applet-fat.jar](/files/fd-applet-fat.jar)

2. **Extract the downloaded zip file.**

## Directory Structure

The extracted directory contains the following files and folders:

- `lib` folder: contains `fd-applet-fat.jar`
- `examples` folder: contains algebra examples
- Windows: `fd-applet.bat`
- Mac: `fd-applet.command`, `initial-setup.scpt`

## Running FD Applet

### Windows Users

1. Double-click `fd-applet.bat` to launch the app.
   (This file automatically checks for updates, runs `fd-applet-fat.jar`, and opens <https://localhost:8080> in your browser.)

### Mac Users

1. For the first time only, open `initial-setup.scpt` and click the Run button (the triangle icon) in the Script Editor to grant `fd-applet.command` execute permissions.
2. Double-click `fd-applet.command` to launch the app.
   (This file automatically checks for updates, runs `fd-applet-fat.jar`, and opens <https://localhost:8080> in your browser.)

3. On the first launch, you may need to allow the app to run by following these steps:
   - Go to System Preferences > Security & Privacy.
   - Click the "Open Anyway" button next to the message about the app being from an unidentified developer.

### For Linux and Other OS Users or Advanced Users

1. `lib/fd-applet-fat.jar` is the main body of FD Applet. After installing the Java environment, execute the command `java -jar fd-applet-fat.jar` (from `lib` directory) to start the server.
2. Once the server is up and running, access <https://localhost:8080> in your browser to use FD Applet.
3. Note that in this case, the app will not be updated automatically. If a message appears on the screen indicating that a newer version is available, manually download [fd-applet-fat.jar](/files/fd-applet-fat.jar) and replace the one in the `lib` folder.

## Closing FD Applet

To close the app, close the terminal window (Command Prompt on Windows, Terminal on Mac) and the browser.

## Support

If you have any questions or issues, please use the menu's FILES > Send Feedback or report issues option or send an email to henomoto [at] omu.ac.jp.
