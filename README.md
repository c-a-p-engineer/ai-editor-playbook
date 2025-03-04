# AIエディター プレイブック リポジトリテンプレート

このリポジトリは、最新のAIエディター（例: Cline、Cursorなど）を活用した開発環境のための統一ルールと設定ファイルを集約したプレイブックのテンプレートです。

## リポジトリの説明

このリポジトリテンプレートは、AIエディターを活用した開発チームが、生成コードの品質を向上させ、開発効率を最大化するための基盤を提供します。
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
│    ├─ ts.md                // TypeScript向けコーディング規約
│    ├─ py.md                // Python向けコーディング規約
│    ├─ js.md                // JavaScript向けコーディング規約
│    └─ ...                  // 必要に応じたその他言語のルール
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
- **.ai/coding/**: 各プログラミング言語のコーディング規約を記述したMarkdownファイル群です。
  - `ts.md`: TypeScript向けコーディング規約
  - `py.md`: Python向けコーディング規約
  - `js.md`: JavaScript向けコーディング規約
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
