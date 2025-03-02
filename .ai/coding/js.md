<!--
  このファイルは、JavaScriptのコーディング規約を記述します。
  Airbnbスタイルガイドに準拠し、コーディングスタイル、命名規則、
  エラーハンドリング、モジュール管理、コメントの書き方などを網羅しています。
-->

# JavaScript コーディング規約（Airbnbスタイルガイド準拠）

このドキュメントは、JavaScriptのコーディング規約を提供します。
Airbnb JavaScript Style Guideに準拠したスタイルガイドラインを基本とし、
プロジェクト固有のルールや推奨事項を追加しています。
以下の項目について説明します。

## 1. コーディングスタイル

- **Airbnbスタイルガイド:**
  - Airbnb JavaScript Style Guideに可能な限り準拠します。
  - Airbnbスタイルガイドは、JavaScriptコードの可読性と保守性を向上させるためのスタイルガイドラインです。
  - [https://github.com/airbnb/javascript](https://github.com/airbnb/javascript)
  - [https://github.com/mitsuruog/javascript-style-guide](https://github.com/mitsuruog/javascript-style-guide)（日本語訳）
- **インデント:**
  - スペース2つを使用します。
  - タブ文字は使用しません。
- **セミコロン:**
  - 行末にセミコロンを記述しません（ASI: Automatic Semicolon Insertionに依存します）。
- **クォート:**
  - 文字列リテラルには、シングルクォート(')を使用します。
- **オブジェクトと配列:**
  - オブジェクトと配列の定義は、末尾にカンマを付与します（trailing commas）。

## 2. 命名規則

- **変数名:**
  - ローワーキャメルケース(lowerCamelCase)を使用します。
  - 例：`firstName`、`lastName`、`userAge`
- **関数名:**
  - ローワーキャメルケース(lowerCamelCase)を使用します。
  - 例：`getUserName`、`calculateTotal`、`isValidInput`
- **クラス名:**
  - アッパーキャメルケース/パスカルケース（UpperCamelCase/PascalCase）を使用します。
  - 例：`UserAccount`、`ShoppingCart`、`OrderService`
- **メソッド名:**
  - ローワーキャメルケース（lowerCamelCase）を使用します。
  - 例：`getName`、`addItem`、`validateOrder`
- **定数名:**
  - スネークケース（SNAKE_CASE）の大文字を使用します。
  - 例：`MAX_USERS`、`API_ENDPOINT`、`DEFAULT_TIMEOUT`
- **コンポーネント名（React）:**
  - パスカルケース（PascalCase）を使用します。
  - 例：`UserProfile`、`ProductList`、`OrderForm`

## 3. エラーハンドリング

- **例外処理:**
  - `try...catch`文を使用して、例外を適切に処理します。
  - 例外をthrowする場合は、Errorオブジェクトをthrowします。

## 4. モジュール管理

- **ES Modules (ESM):**
  - ES Modules（ESM）を使用して、モジュールを管理します。
  - `import`および`export`構文を使用します。
- **相対パス:**
  - モジュールをimportする際は、相対パスを基本とします。
  - 例：`import { UserService } from '../services/user-service';`

## 5. コメントの書き方

- **行コメント:**
  - `//`を使用します。
  - コードの意図や処理内容を簡潔に説明するために使用します。
- **ブロックコメント:**
  - 複数行にわたるコメントは、`/** ... */`を使用します。
  - 関数、クラス、コンポーネントなどのドキュメントを記述するために使用します。
  - JSDoc形式で記述することを推奨します。

## 6. その他

- コーディング規約に関する疑問や問題点があれば、プロジェクトのリーダーまたはコーディング規約担当者に相談してください。
  - このガイドラインは、必要に応じて更新されます。定期的に内容を確認し、最新の情報を把握するようにしてください。
