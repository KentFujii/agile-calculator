## インセプションデッキ

### 我々はなぜここにいるのか？
あなたは、開発組織のアジャイルコーチです。
また、Pythonに長けたDevOpsエンジニアです。
あなたは、チームの生産性を向上させるために、JiraやGitHubのデータを分析します。
Pythonを利用しJiraやGitHubのデータをJupyter Notebookで可視化することで、開発サイクル改善の施策を推進します。

### エレベーターピッチ
[ 潜在的なニーズを満たしたり、潜在的な課題を解決したり ]したい
[ JiraやGitHubユーザーのITエンジニア ]向けの
[ agile-calculator ]というプロダクトは
[ Jupyter Notebookで利用する、JiraやGitHub向けのPythonクライアント ]です。
これは[ Four Keysといった各種開発サイクルの指標計測 ]ができ、
[ Findy Team+ ]とは違って
[ JiraやGitHubのクレデンシャルさえあれば、無料で利用できるという特徴 ]が備わっている。

### やらないことリスト
- 本プロジェクトの、早すぎる最適化
  - 本プロジェクトの、過度なドキュメント化
  - 本プロジェクトの、過度なテストカバレッジの追求
  - 本プロジェクトの、過度なコードのリファクタリング
  - 本プロジェクトの、過度な機能追加

### 「ご近所さん」を探せ
- このリポジトリで開発ツールを開発する、GEMINI、つまりあなたです。
- このリポジトリを管理して、ツールを利用する人、つまり私です。
- 開発チームのメンバー、つまり分析対象の人たちです。

## 解決案を描く
### システム構成
[ユーザーストーリーマッピング](https://www.canva.com/design/DAGc0-KJrLg/_1o6i9n5LO1YdSLCs_IXFA/view?utm_content=DAGc0-KJrLg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h3a1ac8b254)

#### データを取得する(Extract)
分析対象となるサービスのAPIからデータを取得するためのモジュールを実装します。
- src/extractors
#### データを加工する(Transform)
取得したデータを用途に沿って加工するためのモジュールを実装します。
- src/transformers
#### データを出力する(Load)
加工したデータを用途に則した各形式に出力するためのモジュールを実装します。
- src/loaders
### データの形式を保持する(Record)
各工程間でデータの形式を保持するためのモジュールを実装します。
- src/records
#### データの流れを管理する(Workflow)
データを取得し、加工し、出力するためのワークフローを管理するモジュールを実装します。
- src/workflows
#### アプリケーション
このシステムを利用するためのインターフェースアプリケーション向けのモジュールを実装します。
- src/pandas
- src/cli

### 開発手順
#### 開発環境のセットアップ手順
ビルドの実行
```bash
docker compose build
```
#### 開発コマンド
本プロジェクトのコマンドは、以下のように`docker compose run --rm jupyter`を先頭につけて実行します。
```bash
docker compose run --rm jupyter <command>
```

例えば、テストの実行は以下です
```sh
docker compose run --rm jupyter pytest
```

静的解析は以下です
```sh
docker compose run --rm jupyter ruff check --fix
```

型検査は以下です
```sh
docker compose run --rm jupyter ty check
```
