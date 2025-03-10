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

## オンライン版

FD Applet は、ブラウザ上で下のリンクから気軽に使うことができます：
- <https://fd-applet.dt.r.appspot.com/>

このオンラインデモは、使用可能メモリが制限されており、計算も遅い可能性があります。また、接続が不安定になる可能性があります。
より快適にご利用したい方は、このページからローカル版のインストールをお勧めします。

## FD Applet 使用例

![FD Applet 1](/assets/images/fd-applet/fd-applet1.jpg)

**Info タブ**：この多元環の基本的な情報と AR quiver 

![FD Applet 2](/assets/images/fd-applet/fd-applet2.jpg)

**Calculator タブ**：加群の間の Ext^1 の計算

![FD Applet 3](/assets/images/fd-applet/fd-applet3.jpg)

**Enumerator タブ**: τ-rigid modulesを全て列挙（255,364個！）

![FD Applet 4](/assets/images/fd-applet/fd-applet4.jpg)

**Converter タブ**：support τ-tilting moduleを、対応するsemibrickへ変換

![FD Applet 5](/assets/images/fd-applet/fd-applet5.jpg)

**Quivers Tab**: resolving 部分圏の Hasse 図

## FD Applet について

FD Applet は、多元環を入力すると、その加群に関する様々な計算や、特定の加群や加群圏の部分圏を列挙し、AR quiver や 各種 Hasse quiver などが計算できる PC アプリケーションです。
このガイドでは、Windows、Mac、Linux などの他のシステムでの FD Applet のインストール方法と使用方法について説明します。

### 実装について

Kotlin を用いたサーバー・バックエンドと、React を用いたフロントエンド、およびアップデート確認・自動更新や起動補助のためのスクリプトで構成されています。アプリの開発やドキュメント作成において、ChatGPT のサポートを受けています。

**ソースコード**

- [GitHub Repository](https://github.com/haruhisa-enomoto/fd-applet)

## 更新履歴

- 2023-07-25: バージョン 0.4.0 をリリース。酒井氏によって導入された[ICE sequence](https://arxiv.org/abs/2307.11347)の計算を追加。これは有界導来圏のある$t$-structureを分類しているものです。

- 2023-06-27: バージョン 0.3.2 をリリース。Wide τ-tilting 加群の計算と、そのHasse図（対応するICE閉部分圏の包含によるHasse図）の計算を追加。また負荷がかかりうる計算については実際の計算時間を表示するよう変更。

- 2023-06-05: バージョン 0.3.0 をリリース。
  - 新しい機能：**Converter** を追加。これは、与えられた加群・部分圏から、いろんな操作で別の加群・部分圏を計算します (ある加群を含む最小の torsion class、部分圏の Ext-proj、τ-tilting theory でのさまざまな全単射、などなど)
  - UIの改善。AR quiver の物理演算の調整機能の追加。

- 2023-04-15: バージョン 0.2.1 をリリース。軽微な UI 修正と、オンラインデモの追加。

- 2023-04-14: バージョン 0.2.0 をリリース。UI 修正（AR quiver 周り）、"projectively/injectiely stable Hom"の計算を追加。

- 2023-04-07: バージョン 0.1.2 をリリース。軽微な UI 修正。

- 2023-04-06: バージョン 0.1.1 をリリース。UI と挙動を修正：
  - Quiver に「Zoom」オプションを追加（デフォルト：無効）。Quiver 内でのスクロールでズームするかどうかを選択できるようになりました。
  - ブラウザまたはタブが閉じられたときに、サーバーが自動的にシャットダウンされるようになりました。
- 2023-04-04: 初期バージョン 0.1.0 をリリースしました。

## インストール

0. **Java 環境（JDK 17）をインストールしてください:**
   こだわりがなければ、<https://adoptium.net/> から「Latest LTS Release」をダウンロードしてインストールするのが簡単です（インストールは特にどこも変更せずデフォルトのままで大丈夫です）。

1. **システムに適した zip ファイルをダウンロードしてください:**

   - Windows: [Windows 用 zip をダウンロード](/files/fd-applet-win.zip)
   - Mac: [Mac 用 zip をダウンロード](/files/fd-applet-mac.zip)
   - 他 OS (や詳しい人向け): [zip をダウンロード](/files/fd-applet-others.zip)
   - Fat Jar のみ: [fd-applet-fat.jar](/files/fd-applet-fat.jar)

2. **ダウンロードした zip ファイルを解凍します。**

### ディレクトリ構成

解凍したディレクトリには、以下のファイルとフォルダが含まれています：

- Windows: `fd-applet.bat`
- Mac: `fd-applet.command`, `initial-setup.scpt`
- `examples`フォルダ: 多元環の例が含まれています。使い方は[Open と Save](#open-と-save)をご覧ください。
- `lib`フォルダ: `fd-applet-fat.jar`という Java ファイルがあります。**決してダブルクリックして開こうとしないでください**。

## FD Applet の起動

{% capture notice-text %}

### 重要な注意

- **`fd-applet-fat.jar`をダブルクリックしないでください**。起動はできないか、できたとしても終了することができなくなります。必ず、`fd-applet.bat`（Windows）または `fd-applet.command`（Mac）をダブルクリックする（か[その他](#その他の-os-や詳しいユーザー)に従う）ようお願いします。
- ブラウザで「サイトにアクセスできません」「サーバーに接続できません」等のエラーが出た場合、数秒待ってからブラウザを更新してみてください。

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
2. Update ボタンをクリックし、右のタブ（Info、Calculator、Enumerator、Converter、Quivers）を使用します。
3. ほとんどの機能は有限次元 special biserial algebra（例えば gentle や string algebra）が必要で、Enumerator と Converter と Quivers ではさらに有限表現型なことが必要です。

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

- 多元環を入力し、"Get Data"ボタンを押して各タブを使用します。

- "Show AR Quiver"で、AR quiver を（全てのタブについて）表示するか切り替えられます。実際に AR quiver を表示するには、"Compute AR Quiver"ボタンを押してください。

直既約加群の記法：

- `1`、`2`：`1`および`2`での単純加群。
- `a*b*!c`：string 加群`1 -a-> 2 -b-> 3 <-c- 4`。
- `a*b=d*e`：可換正方形`-a->-b-> = -d->-e->`の biserial 加群。

#### Info

各種ホモロジー次元、射影/移入加群など、多元環の基本情報を表示します。

（ほとんどの機能は有限次元 special biserial algebra でのみ動きます。）

#### Calculator

入力に基づいて Hom や Ext の次元や射影分解などを計算します（例：`dim Ext^2(a*b + c*d*e, f*g)`）。

（ほとんどの機能は有限次元 special biserial algebra でのみ動きます。）

#### Enumerator

- 加群/部分圏を数え上げて列挙します（例：各種 tilting や semibrick など）。"Show Distribution"ボタンで直既約の個数ごとの分布を表示します。
- AR quiver が表示されているとき、加群/部分圏を選択すると、頂点が色付けされます。部分圏を選んだ場合は Ext-projective/injective をハイライト表示できます。

（有限表現型 special biserial algebra でのみ動きます。）

#### Converter

加群や部分圏を入力すると、それからさまざまな操作で別の加群・部分圏を計算できます。例えば：
- 与えられた部分圏に対し、それを含む最小の torsion class (や torsion-free class、ICE-closed subcategory、wide subcategory、などなど)
- Torsion class を与えると、（Marks-Stovicekの対応で）対応する wide 部分圏を計算（や他にも τ-tilting theory でのさまざまな全単射の計算）
- 拡大閉部分圏に対して、その Ext-projectives の計算
- そして他にもたくさんの操作！

#### Quivers

- 多元環に関連する quiver を表示します（例：τ-tilting quiver、部分圏の Hasse quiver など）。
- AR quiver が表示されているとき、quiver の頂点を選ぶと、対応する加群・部分圏が AR quiver 上で色付けされます。

（有限表現型 special biserial algebra でのみ動きます。）

## サポート

質問や問題や機能追加の要望（こんな計算をする機能をつけて欲しい・これは計算できるのか）等がある場合は、メニューの Files → "Send Feedback or report issues"を使用するか、
`henomoto [at] omu.ac.jp` にメールを送ってください。
