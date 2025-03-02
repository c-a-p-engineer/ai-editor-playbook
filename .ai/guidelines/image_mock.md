# 画像モック使用時のガイドライン

このドキュメントは、プロジェクト内で画像モック生成に [Placehold.jp](https://placehold.jp/) を利用するための設定と利用方法を記載しています。

## 基本設定

- **Base URL**: `https://placehold.jp`
- **デフォルトサイズ**: `300x200`
- **画像フォーマット**: `png`
- **デフォルトテキスト**: `Placeholder`
- **背景色**: `cccccc`（16進数表記）
- **テキスト色**: `ffffff`（16進数表記）

## URL パターン

Placehold.jp は以下の URL 形式で画像を生成します：

```
https://placehold.jp/{サイズ}.{フォーマット}?text={テキスト}&bg={背景色}&fg={テキスト色}
```

### 例
- デフォルト設定の場合：
  ```
  https://placehold.jp/300x200.png?text=Placeholder&bg=cccccc&fg=ffffff
  ```
- カスタマイズ例（サイズ変更、テキスト変更）：
  ```
  https://placehold.jp/500x300.png?text=My+Image&bg=cccccc&fg=ffffff
  ```

## 利用方法

1. **画像モックの生成**  
   各モック画像が必要な箇所では、上記の URL パターンに従い、必要なサイズやテキスト、色を指定して URL を生成してください。

2. **テンプレートとの連携**  
   - AIエディタのテンプレート内で画像モックが必要な場合、ここで定義した設定を参照して自動的に URL を組み立てるようにしてください。
   - 例えば、HTML テンプレート内で `<img src="https://placehold.jp/300x200.png?text=Placeholder&bg=cccccc&fg=ffffff" alt="モック画像">` のように利用します。

## JSON 形式の設定例

プロジェクト全体で利用する場合、JSON 形式で設定を管理することも可能です。以下はその一例です：

```json
{
  "imageMock": {
    "baseUrl": "https://placehold.jp",
    "defaultSize": "300x200",
    "format": "png",
    "defaultText": "Placeholder",
    "bgColor": "cccccc",
    "fgColor": "ffffff"
  }
}
```

この設定ファイルをもとに、AIエディタや自動化スクリプトが画像モック URL を生成する際に、上記パラメータを適用してください。
