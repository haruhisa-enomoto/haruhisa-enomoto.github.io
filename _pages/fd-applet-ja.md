---
layout: single
classes: wide-no-author
title: "FD Applet - an applet for Finite-Dimensional algebras"
permalink: /fd-applet-ja/
author_profile: false
toc: true
toc_sticky: true
---

[(English version)](/fd-applet/)

## FD Applet 使用例

![FD Applet 1](/assets/images/fd-applet/fd-applet1.jpg)

255,364 個の τ-rigid modules たち

![FD Applet 2](/assets/images/fd-applet/fd-applet2.jpg)

Rresolving subcategories の Hasse 図

![FD Applet 3](/assets/images/fd-applet/fd-applet3.jpg)

ある cotorsion pair

![FD Applet 4](/assets/images/fd-applet/fd-applet4.jpg)

ある IE-closed subcategories の Ext-injectives

## FD Applet について

FD Applet は、多元環を入力すると、その加群に関する様々な計算や、特定の加群や加群圏の部分圏を列挙し、AR quiver や 各種 Hasse quiver などが計算できる PC アプリケーションです。
このガイドでは、Windows、Mac、Linux などの他のシステムでの FD Applet のインストール方法と使用方法について説明します。

### 実装について

Kotlin を用いたサーバー・バックエンドと、React を用いたフロントエンド、およびアップデート確認・自動更新や起動補助のためのスクリプトで構成されています。ソースコードは今後公開予定です。アプリの開発やドキュメント作成において、ChatGPT のサポートを受けています。

**ソースコード**

- [フロントエンド（React）](https://github.com/haruhisa-enomoto/fd-applet-front)

- バックエンド：in preparation

## 更新履歴

- 2023-04-06: バージョン 0.1.1 をリリース。UI と挙動を修正：
  - Quiver に「Zoom」オプションを追加（デフォルト：無効）。Quiver 内でのスクロールでズームするかどうかを選択できるようになりました。
  - ブラウザまたはタブが閉じられたときに、サーバーが自動的にシャットダウンされるようになりました。
- 2023-04-04: 2023-04-04: 初期バージョン 0.1.0 をリリースしました。

## インストール

### システム要件

- JDK 17: まず Java 環境（JDK 17）をインストールしてください。こだわりがなければ、<https://adoptium.net/> から「Latest LTS Release」をダウンロードしてインストールするのが簡単です（インストールは特にどこも変更せずデフォルトのままで大丈夫です）。

### ダウンロード・解凍

1. **システムに適した zip ファイルをダウンロードしてください:**

   - Windows: [Windows 用 zip をダウンロード](/files/fd-applet-win.zip)
   - Mac: [Mac 用 zip をダウンロード](/files/fd-applet-mac.zip)
   - 他 OS (や詳しい人向け): [zip をダウンロード](/files/fd-applet-others.zip)
   - Fat Jar のみ: [fd-applet-fat.jar](/files/fd-applet-fat.jar)

2. **ダウンロードした zip ファイルを解凍します。**

### ディレクトリ構成

解凍したディレクトリには、以下のファイルとフォルダが含まれています：

- `lib`フォルダ: `fd-applet-fat.jar`という Java ファイルがあります。**決してダブルクリックして開こうとしないでください**。
- `examples`フォルダ: 多元環の例が含まれています。使い方は[Open と Save](#open-と-save)をご覧ください。
- Windows: `fd-applet.bat`
- Mac: `fd-applet.command`, `initial-setup.scpt`

## FD Applet の起動

{% capture notice-text %}

### 重要な注意

- **`fd-applet-fat.jar`をダブルクリックしないでください**。起動はできないか、できたとしても終了することができなくなります。必ず、`fd-applet.bat`（Windows）または `fd-applet.command`（Mac）をダブルクリックする（か[その他](#その他の-os-や詳しいユーザー)に従う）ようお願いします。
- ブラウザで「サイトにアクセスできません」「サーバーに接続できません」等のエラーが出た場合、数秒待ってからブラウザを更新してみてください。
- （バージョン 0.1.0 の場合のみ）アプリを使用し終わったら、ターミナルウィンドウ（Windows の場合はコマンドプロンプト、Mac の場合はターミナル）を確実に閉じるようにしてください。

{% endcapture %}

<div class="notice--danger">
  {{ notice-text | markdownify }}
</div>

### Windows ユーザー

1. `fd-applet.bat`をダブルクリックしてアプリを起動します。
   （このファイルは、アップデートを確認し、`fd-applet-fat.jar`を実行して、ブラウザで<http://localhost:8080>を開く処理を自動的に行います。）

### Mac ユーザー

1. 初回のみ、`initial-setup.scpt`を開いてスクリプトエディタの実行ボタン（三角のアイコン）をクリックして実行します（これは`fd-applet.command`に実行権限を付与します）。
2. `fd-applet.command`をダブルクリックしてアプリを起動します。
   （このファイルは、アップデートを確認し、`fd-applet-fat.jar`を実行して、ブラウザで<http://localhost:8080>を開く処理を自動的に行います。）

3. 初回起動時には、おそらく以下の手順でアプリを実行できるようにする必要があります：
   - システム環境設定 > セキュリティとプライバシーに移動します。
   - 「開発元を確認できないため」のようなメッセージの横にある「このまま開く」ボタンをクリック

### その他の OS や詳しいユーザー

1. `lib/fd-applet-fat.jar`が FD Applet の本体です。Java 環境をインストールした後、`java -jar fd-applet-fat.jar`というコマンドを（`lib` 内から）実行することで、サーバーが立ち上がります。**ファイルをダブルクリックしないでください。サーバーが起動しても、終了できない可能性があります。**
2. サーバーが立ち上がった後、ブラウザで<http://localhost:8080>にアクセスすると、FD Applet が利用できます。
3. この場合、アップデートは自動で行われませんので、画面に最新版が利用可能というメッセージが表示されたら、手動で[fd-applet-fat.jar](/files/fd-applet-fat.jar)をダウンロードし、`lib`フォルダ内のものと置き換えてください。

### アプリの終了

アプリを閉じるには、ブラウザ（またはタブ）を閉じるだけです。バージョン 0.1.1 から、ブラウザを閉じるとバックグラウンドのサーバーが自動的にシャットダウンされるため、ターミナルを手動で閉じる必要はありません。

## 使用方法

概略

1. 左の入力欄に多元環（quiver、単項および可換関係）を入力します。
2. Update ボタンをクリックし、右のタブ（Basic Info、Calculator、Enumerator、Quivers）を使用します。
3. ほとんどの機能は有限次元 special biserial algebra（例えば gentle や string algebra）が必要で、Enumerator と Quivers ではさらに有限表現型なことが必要です。

### 多元環の入力

左の入力欄に多元環を入力します。
中山多元環は"File"メニューから Kupisch series を使って入力もできます。

#### Quiver

- 頂点の追加：キャンバスをクリックします。
- 矢印の追加：始点の頂点をクリックし、次に終点の頂点をクリック（または空いてる場所をクリックして終点を追加）します。
- 頂点/矢印の削除：Delete または Backspace キー、または中央の"Delete selected item"ボタンを使用します。
- キャンバスを quiver に合わせる：左の"Fit"ボタンを使用します。
- すべて消す：右の"Clear all"ボタンを使用します。

#### Relation

*単項および可換関係式のみ*に対応しています。

- 単項関係式：path `-a-> -b->`は、`ab`、`a b`、または`a*b`のように書きます。
- 可換関係式：`ab-cd`や`a * b - c * d`のように書きます。

#### Update

Update ボタンをクリックして完了します。

#### Open と Save

"File"メニューの"Save"から多元環を保存でき、また"Open"から保存した多元環を読み込む事ができます。

例えば"Open"で`examples`フォルダの中のファイルを選ぶと、quiver と関係式が自動で読み込まれます。

### 右のタブ

多元環を入力し、"Get Data"ボタンを押して各タブを使用します。

直既約加群の記法：

- `1`、`2`：`1`および`2`での単純加群。
- `a*b*!c`：string 加群`1 -a-> 2 -b-> 3 <-c- 4`。
- `a*b=d*e`：可換正方形`-a->-b-> = -d->-e->`の biserial 加群。

#### Basic Info

各種ホモロジー次元、射影/移入加群など、多元環の基本情報を表示します。

（ほとんどの機能は有限次元 special biserial algebra でのみ動きます。）

#### Calculator

入力に基づいて Hom や Ext の次元や射影分解などを計算します（例：`dim Ext^2(a*b + c*d*e, f*g)`）。

（ほとんどの機能は有限次元 special biserial algebra でのみ動きます。）

#### Enumerator

- 加群/部分圏を数え上げて列挙します（例：各種 tilting や semibrick など）。"Show Distribution"ボタンで直既約の個数ごとの分布を表示します。
- AR quiver を表示すると、加群/部分圏を選択すると、頂点が色付けされます。部分圏を選んだ場合は Ext-projective/injective をハイライト表示できます。

（有限表現型 special biserial algebra でのみ動きます。）

#### Quivers

- 多元環に関連する quiver を表示します（例：τ-tilting quiver、部分圏の Hasse quiver など）。
- AR quiver を表示すると、右側の quiver の頂点を選ぶと、対応する加群・部分圏が AR quiver 上で色付けされます。

（有限表現型 special biserial algebra でのみ動きます。）

## サポート

質問や問題や機能追加の要望（こんな計算をする機能をつけて欲しい・これは計算できるのか）等がある場合は、メニューの Files → "Send Feedback or report issues"を使用するか、
`henomoto [at] omu.ac.jp` にメールを送ってください。
