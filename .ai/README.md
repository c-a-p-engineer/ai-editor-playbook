# .ai ディレクトリについて

このディレクトリには、AIエディタに関する各種設定ファイルやガイドラインが格納されています。

## ディレクトリ構成

- **`.ai/guidelines/`**: 開発ガイドラインに関するファイルを格納します。
    - プロジェクト全体に関わるルールや推奨事項を記述したMarkdownファイル (`.md`) を配置します。
    - 例: コーディング規約、テストガイドライン、セキュリティガイドラインなど
- **`.ai/coding/`**: プログラミング言語ごとのコーディング規則に関するファイルを格納します。
    - 各言語のコーディングスタイルやベストプラクティスを記述したMarkdownファイル (`.md`) を配置します。
    - 例: CSSコーディング規則、JavaScriptコーディング規則、Pythonコーディング規則など
- **`.ai/program/`**: AIエディタが実行するプログラム (スクリプト) を格納します。
    - Pythonスクリプト (`.py`) やMarkdownファイル (`.md`) などを配置します。
    - 例: ウェブ検索スクリプト (`search.py`)、URL読み込みスクリプト (`read_url.py`)、スクリプト使用説明 (`search.md`, `read_url.md`) など
- **`.ai/prompts/`**: プロンプトテンプレートに関するファイルを格納します。
    - AIエディタで使用するプロンプトの例やテンプレートを記述したMarkdownファイル (`.md`) を配置します。
    - 例: 各シナリオに対するプロンプト例 (`sample_prompts.md`) など

## ファイル配置のルール

- 新しいガイドラインファイルを作成する場合は、内容に応じて `.ai/guidelines/` または `.ai/coding/` ディレクトリに配置してください。
- 新しいプログラム (スクリプト) を作成する場合は、`.ai/program/` ディレクトリに配置してください。
- 新しいプロンプトテンプレートを作成する場合は、`.ai/prompts/` ディレクトリに配置してください。

この README.md を参考に、適切な場所にファイルを作成・配置してください。
