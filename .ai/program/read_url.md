# read_url.py 使用方法

## 概要
`read_url.py` は、指定されたURLのウェブページからテキストコンテンツを抽出し、整形して標準出力に表示するPythonスクリプトです。
`requests` と `BeautifulSoup4` ライブラリを使用しています。

## 実行方法
ターミナルから以下のコマンドを実行します。

```bash
python read_url.py <URL>
```

- `<URL>`: テキストコンテンツを抽出したいウェブページのURLを指定します。

## 引数
- `<URL>` (必須): ウェブページのURL。

## 機能
1. **ウェブページの取得**: 指定されたURLにHTTPリクエストを送信し、ウェブページのHTMLコンテンツを取得します。
2. **HTML解析**: `BeautifulSoup4` を使用してHTMLコンテンツを解析します。
3. **テキスト抽出と整形**: HTMLからテキストコンテンツを抽出し、以下の要素に基づいて整形します。
    - `<br>` タグ: 空行に変換
    - `<h1>` ~ `<h6>` タグ: 前後に空行を挿入
    - `<li>` タグ: 行頭に `  * ` を付与
    - `<p>` タグ: 行末に改行を付与
    - その他のテキスト要素: 前後の空白を削除
4. **標準出力**: 整形されたテキストコンテンツを標準出力に表示します。
5. **エラー処理**:
    - URLが指定されていない場合、または引数の数が正しくない場合は、Usageメッセージを表示して終了します。
    - URLの取得に失敗した場合（HTTPエラーなど）、エラーメッセージを標準エラー出力に出力して終了します。

## 例

### 例1: 特定のURLのテキストコンテンツを表示する
```bash
python read_url.py https://www.example.com
```
このコマンドは、`https://www.example.com` のウェブページのテキストコンテンツを整形して表示します。

### 例2: エラーが発生した場合
URLが正しくない場合や、ウェブページが存在しない場合は、エラーメッセージが表示されます。
```bash
python read_url.py invalid-url
```
```
Error fetching URL: Invalid URL 'invalid-url': No schema supplied. Perhaps you meant http://invalid-url?
```

## 依存ライブラリ
- requests
- beautifulsoup4

これらのライブラリがインストールされていない場合は、以下のコマンドでインストールしてください。
```bash
pip install requests beautifulsoup4
