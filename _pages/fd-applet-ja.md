---
layout: single
classes: wide
title: "FD Applet - インストールと使用ガイド"
permalink: /fd-applet-ja/
author_profile: false
---

{% include base_path %}

[(English version)](/fd-applet/)

このガイドでは、Windows、Mac、Linux などの他のシステムでの FD Applet のインストール方法と使用方法について説明します。

## 使い方

TODO

## システム要件

- JDK 17: 最新の Java 環境（JDK 17）をインストールしていることを確認してください。わからない場合は、https://adoptium.net/ から「Latest LTS Release」をダウンロードしてインストールしてください。

## インストール

1. **システムに適した zip ファイルをダウンロードしてください:**

   - Windows: [Windows 用 zip をダウンロード](https://example.com/windows_download)
   - Mac: [Mac 用 zip をダウンロード](https://example.com/mac_download)
   - 他 OS (や詳しい人向け): [zip をダウンロード](/files/fd-applet-others.zip)
   - Fat Jar のみ: [fd-applet-fat.jar](/files/fd-applet-fat.jar)

2. **ダウンロードした zip ファイルを解凍します。**

## ディレクトリ構成

解凍したディレクトリには、以下のファイルとフォルダが含まれています：

- `lib`フォルダ: `fd-applet-fat.jar`を含む
- `examples`フォルダ: 多元環の例が含まれています
- Windows: `fd-applet.bat`
- Mac: `fd-applet.command`, `initial-setup.scpt`

## FD Applet の実行

### Windows ユーザー

1. `fd-applet.bat`をダブルクリックしてアプリを起動します。
   (このファイルは、アップデートを確認し、`fd-applet-fat.jar`を実行して、ブラウザで<https://localhost:8080>を開く処理を自動的に行います。)

### Mac ユーザー

1. 初回のみ、`initial-setup.scpt`を開いてスクリプトエディタの実行ボタンをクリックし、`fd-applet.command`に実行権限を付与します。
2. `fd-applet.command`をダブルクリックしてアプリを起動します。
   (このファイルは、アップデートを確認し、`fd-applet-fat.jar`を実行して、ブラウザで<https://localhost:8080>を開く処理を自動的に行います。)

3. 初回起動時には、以下の手順でアプリを実行できるようにする必要があります：
   - システム環境設定 > セキュリティとプライバシーに移動します。
   - 確認されていない開発者からのアプリに関するメッセージの横にある「とにかく開く」ボタ

### Linux やその他の OS のユーザー、または詳しい方へ

1. `lib/fd-applet-fat.jar`が FD Applet の本体です。Java 環境をインストールした後、`java -jar fd-applet-fat.jar`というコマンドを(`lib` 内から)実行することで、サーバーが立ち上がります。
2. サーバーが立ち上がった後、ブラウザで<http://localhost:8080>にアクセスすると、FD Applet が利用できます。
3. この場合、アップデートは自動で行われませんので、画面に最新版が利用可能というメッセージが表示されたら、手動で提供されているリンクから最新の[fd-applet-fat.jar](/files/fd-applet-fat.jar)をダウンロードし、`lib`フォルダ内のものと置き換えてください。

## アプリの終了

アプレットを終了するには、ターミナルウィンドウ(Windows の場合はコマンドプロンプト、Mac の場合はターミナル)とブラウザを閉じてください。

## サポート

質問や問題がある場合は、メニューの Files → "Send Feedback or report issues"を使用するか、
henomoto [at] omu.ac.jp にメールを送ってください。
