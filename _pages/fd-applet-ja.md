---
layout: single
classes: wide
title: "FD Applet"
permalink: /fd-applet-ja/
author_profile: false
---

{% include base_path %}

[(English version)](/fd-applet/)

# FD Applet について

最新バージョンは`0.1.0`です。

## FD Applet の説明

TODO

## インストール方法

1. **JDK 17 をインストール:**  
   まずシステムに Java 環境（JDK 17）をインストールします。
   特にこだわりがない場合は、<https://adoptium.net/> から「Latest LTS Release」をダウンロードしてインストールしてください。

2. **ダウンロードと解凍:**  
   OS に応じて zip ファイルをダウンロードします:

   - [Windows 版ダウンロードリンク](/files/fd-applet-win.zip)
   - [Mac 版ダウンロードリンク](/files/fd-applet-mac.zip)

   zip ファイルを解凍します。

3. **FD Applet を実行:**  
   OS に応じたリンクを参照してアプリを起動してください（同じ手順は、zip 内の Readme ファイルにも記載されています）:
   - [Windows 版の手順](https://example.com/windows_instructions)
   - [Mac 版の手順](https://example.com/mac_instructions)

## 詳しい人へ・向け・Linux などのその他 OS 向け

FD Applet のメイン部分は[fd-applet-fat.jar](/files/fd-applet-fat.jar)ファイルです。
Java 環境をインストールした後、`java -jar fd-applet-fat.jar`コマンドを実行することで、サーバーが立ち上がります。その後、ブラウザで<http://localhost:8080/>にアクセスすると FD Applet が利用できます。
