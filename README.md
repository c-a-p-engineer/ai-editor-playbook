# AIエディター プレイブック リポジトリテンプレート　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　

[![GitHub stars](https://img.shields.io/github/stars/c-a-p-engineer/ai-editor-playbook?style=social)](https://github.com/c-a-p-engineer/ai-editor-playbook/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 推奨環境

-   Python 3.10+ がインストールされている環境 (一部 Cline のプログラミング機能で使用)

---

## リポジトリの説明

このリポジトリテンプレートは、最新のAIエディター（例: Cline、Cursorなど）を活用した開発環境のための統一ルールと設定ファイルを集約したプレイブックのテンプレートです。
各プログラミング言語ごとのコーディング規約、コードレベルのテストルール、インテグレーションテストやCI/CD連携ルール、
セキュリティ、パフォーマンス、エラーハンドリング、静的解析、依存関係管理など、
生成コードの品質向上を目的とした実践的なガイドラインと設定例を含んでいます。

## ディレクトリ構成

```
/.ai
├─ guidelines/
│    ├─ ai_editor.md         // AIエディター全体の基本ガイドライン
│    ├─ security.md          // セキュリティルール
│    ├─ performance.md       // パフォーマンス・最適化ルール
│    ├─ review_feedback.md   // レビュー・フィードバックルール
│    └─ ci_cd.md             // CI/CD連携ルール（インテグレーションテスト等含む）
├─ coding/
│    ├─ css.md                // CSS向けコーディング規約
│    ├─ docker.md             // Dockerfile向けコーディング規約
│    ├─ html.md               // HTML向けコーディング規約
│    ├─ javascript.md         // JavaScript向けコーディング規約
│    ├─ php.md                // PHP向けコーディング規約
│    ├─ python.md             // Python向けコーディング規約
│    ├─ scss.md               // SCSS向けコーディング規約
│    ├─ typescript.md         // TypeScript向けコーディング規約
│    └─ ...                   // 必要に応じたその他言語のルール
├─ configs/
│    └─ ai_config.json       // AIエディターの動作設定ファイル
└─ prompts/
     └─ default_prompts.md   // プロンプトテンプレート集
```

## 各ファイルの説明

- **.ai/guidelines/**: AIエディターの利用に関するガイドラインを記述したMarkdownファイル群です。
  - `ai_editor.md`: AIエディター全体の基本ガイドライン
  - `security.md`: セキュリティルール
  - `performance.md`: パフォーマンス・最適化ルール
  - `review_feedback.md`: レビュー・フィードバックルール
  - `ci_cd.md`: CI/CD連携ルール（インテグレーションテスト等含む）
- **.ai/guidelines/**: AIエディターの利用に関するガイドラインを記述したMarkdownファイル群です。
  - `ai_editor.md`: AIエディター全体の基本ガイドライン
  - `security.md`: セキュリティルール
  - `performance.md`: パフォーマンス・最適化ルール
  - `review_feedback.md`: レビュー・フィードバックルール
  - `ci_cd.md`: CI/CD連携ルール（インテグレーションテスト等含む）
- **.ai/coding/**: 各プログラミング言語のコーディング規約を記述したMarkdownファイル群です。
  - `css.md`: CSS向けコーディング規約
  - `docker.md`: Dockerfile向けコーディング規約
  - `html.md`: HTML向けコーディング規約
  - `javascript.md`: JavaScript向けコーディング規約
  - `php.md`: PHP向けコーディング規約
  - `python.md`: Python向けコーディング規約
  - `scss.md`: SCSS向けコーディング規約
  - `typescript.md`: TypeScript向けコーディング規約
  - `...`: 必要に応じたその他言語のルール
- **.ai/configs/**: AIエディターの設定ファイルを格納するディレクトリです。
  - `ai_config.json`: AIエディターの動作設定ファイル
- **.ai/prompts/**: AIエディターで使用するプロンプトテンプレートを格納するディレクトリです。
  - `default_prompts.md`: デフォルトのプロンプトテンプレート集

## 利用方法

1. このリポジトリテンプレートを元に、新しいリポジトリを作成します。
2. 各Markdownファイルを編集し、プロジェクトに合わせたガイドラインを記述します。
3. `ai_config.json` を編集し、AIエディターの設定をカスタマイズします。
4. `default_prompts.md` を参考に、プロンプトテンプレートを必要に応じて追加・編集します。
5. 作成したリポジトリをチームメンバーと共有し、AIエディターを活用した開発をスタートします。

## その他

- このリポジトリテンプレートは、継続的に改善します。
- フィードバックや改善提案は大歓迎です。

## プロジェクトの使い方

このプロジェクトは、以下の3つの方法で使用できます。

### 1. ファイルをダウンロードして既存プロジェクトに導入する場合

1.  このプロジェクトのリポジトリからファイルをダウンロードします。
2.  ダウンロードしたファイルの中から、必要なファイル (例: `.ai/` ディレクトリ, 特定のスクリプトファイルなど) を既存のプロジェクトの適切なディレクトリにコピーします。
3.  コピーしたファイルを既存のプロジェクトのコードから利用します。
    -   必要に応じて、ファイルパスやモジュールimport文を調整してください。

### 2. このワークスペースをベースにこのまま開発を行う場合

1.  このワークスペース ( `/workspaces/ai-editor-playbook` ) をそのまま開発環境として使用します。
2.  VS Codeなどのエディタでワークスペースを開き、コードの編集や実行を行います。
3.  必要に応じて、DevContainer環境のカスタマイズや、追加のライブラリのインストールなどを行ってください。

### 3. Gitモジュールとして組み込んで使用する場合

1.  既存のGitリポジトリのルートディレクトリで、以下のコマンドを実行し、このプロジェクトをサブモジュールとして追加します。
    ```bash
    git submodule add https://github.com/c-a-p-engineer/ai-editor-playbook .ai
    ```
    -   `.ai` はサブモジュールを配置するディレクトリ名です。必要に応じて変更してください。
2.  サブモジュールとして追加されたコードを、既存のプロジェクトのコードから利用します。
    -   必要に応じて、ファイルパスやモジュールimport文を調整してください。
    3.  サブモジュールの初期化と更新を行う場合は、以下のコマンドを実行します。
    ```bash
    git submodule init
    git submodule update
    ```

## 注意事項

-   各利用方法において、ファイルパスや設定、依存関係などは、プロジェクトの構成や目的に応じて適宜調整してください。
-   Gitモジュールとして組み込む場合は、サブモジュールの管理方法 (初期化、更新、コミットなど) について、Gitのドキュメントをご確認ください。

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
