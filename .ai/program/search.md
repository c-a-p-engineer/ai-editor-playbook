# search.py スクリプト使用説明

## スクリプト概要

`search.py` スクリプトは、指定されたキーワードでウェブ検索を行い、上位URLからテキスト情報を抽出するPythonスクリプトです。

DuckDuckGo または Google 検索エンジンを利用して検索を行い、上位 N 件の検索結果からウェブページをダウンロードし、テキストコンテンツを抽出します。

トークン削減のため、以下の機能が追加されています。

- **テキスト長制限**: 各URLから抽出するテキストの最大文字数を制限するオプション (`-c/--max_chars`)
- **不要タグ削除**:  ヘッダー、フッター、ナビゲーションなどの不要なHTMLタグを削除するオプション (`--keep_tags` で無効化可能)

## 実行方法

```bash
python .ai/program/search.py [キーワード] [オプション]
```

### 必須引数

- `キーワード`: 検索キーワード

### オプション引数

- `-n`, `--num_results`:  取得する検索結果の数 (デフォルト: 5件)
- `-e`, `--search_engine`: 検索エンジン (`google` または `duckduckgo`, デフォルト: `google`)
- `-ss`, `--search_sites`: Google検索時に考慮するサイト数 (デフォルト: 5, `google` 検索エンジンでのみ有効)
- `-c`, `--max_chars`: 各URLから抽出するテキストの最大文字数 (デフォルト: 1000文字)
- `--keep_tags`:  ヘッダー、フッター、ナビゲーション、aside タグを削除しない (デフォルト: 削除)

### 使用例

- デフォルト設定 (タグ削除あり、文字数制限 1000文字) で実行:
  ```bash
  python .ai/program/search.py wikipedia
  ```

- ヘッダー、フッターなどのタグを削除せずに実行:
  ```bash
  python .ai/program/search.py wikipedia --keep_tags
  ```

- テキスト抽出数を 500 文字に制限して実行:
  ```bash
  python .ai/program/search.py wikipedia -c 500
  ```

- タグを削除せず、テキスト抽出数を 500 文字に制限して実行:
  ```bash
  python .ai/program/search.py wikipedia --keep_tags -c 500
　```
