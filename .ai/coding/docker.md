# DockerfileとDocker Compose 作成時の規約 (ベストプラクティス)

このドキュメントでは、DockerfileとDocker Composeファイルを作成する際のベストプラクティスと規約について説明します。これらの規約に従っていただくことで、より安全で効率的、かつ保守性の高いDocker環境を構築できます。

## Dockerfile 作成規約

Dockerfileは、Dockerイメージを構築するための設計図です。以下のベストプラクティスに従ってDockerfileを作成していただくことで、イメージのサイズを削減し、ビルド時間を短縮し、セキュリティを向上させることができます。

### 1. ベースイメージは 具体的なバージョンを指定してください

- `FROM ubuntu:latest` のように `latest` タグを使用するのではなく、`FROM ubuntu:20.04` のように具体的なバージョンを指定してください。
- `latest` タグは常に最新バージョンを指すため、ビルドの再現性が損なわれる可能性があります。
- 具体的なバージョンを指定していただくことで、ビルドの一貫性を保ち、予期せぬエラーを防ぐことができます。

### 2. マルチステージビルドを利用してください

- ビルドに必要なツールと、最終的なイメージに含める成果物を分離するために、マルチステージビルドを利用してください。
- たとえば、Goのアプリケーションをビルドする場合、ビルドステージではGoのコンパイラやビルドツールを使用し、最終ステージでは実行ファイルのみをコピーします。
- これにより、最終的なイメージサイズを大幅に削減できます。

```dockerfile
# ビルドステージ
FROM golang:1.16 as builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o main .

# 最終ステージ
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/main .
CMD ["./main"]
```

### 3. レイヤー数を削減してください

- Dockerイメージはレイヤー構造で構成されており、レイヤー数が多いほどイメージサイズが大きくなる傾向があります。
- 複数の `RUN` コマンドを `&&` で連結することで、レイヤー数を削減できます。

```dockerfile
# レイヤー数が多い例
RUN apt-get update
RUN apt-get install -y curl

# レイヤー数を削減した例
RUN apt-get update && apt-get install -y curl
```

### 4. キャッシュを有効活用してください

- Dockerビルドはキャッシュを活用してビルド時間を短縮します。
- `COPY` や `ADD` コマンドは、ファイルの内容が変更された場合にのみキャッシュが無効になります。
- 依存関係のインストールなど、変更頻度の低い処理をDockerfileの前の方に記述していただくことで、キャッシュを有効活用できます。

### 5. セキュリティに配慮してください

- 不要なパッケージやツールをインストールしないようにしてください。
- `USER` 命令を使用して、コンテナーを非rootユーザーで実行するようにしてください。
- パスワードやAPIキーなどの機密情報をDockerfileに直接記述しないようにしてください。

### 6. ファイルコピーと追加の最適化

- `COPY` コマンドは必要なファイルのみをコピーするようにしてください。`.dockerignore` ファイルを使用して、不要なファイルをイメージに含めないようにしてください。
- `ADD` コマンドは、tarファイルやリモートURLからのファイル追加など、便利な機能を提供しますが、キャッシュを無効にする可能性が高いため、`COPY` コマンドを優先的に使用してください。

### 7. ユーザーと権限の設定

- `USER` 命令を使用して、コンテナーを特定のユーザーで実行するように設定してください。
- これにより、コンテナーのセキュリティを向上させることができます。
- ファイルの権限設定も適切に行っていただき、コンテナー内で必要な権限のみを付与するようにしてください。

## Docker Compose 作成規約

Docker Composeは、複数のコンテナーからなるアプリケーションを定義し、管理するためのツールです。以下のベストプラクティスに従ってDocker Composeファイルを作成していただくことで、アプリケーションのデプロイと管理を容易にすることができます。

### 1. バージョン指定

- `version: '3.8'` のように、Docker Composeファイルのバージョンを明示的に指定してください。
- バージョンを指定していただくことで、Docker Composeのバージョン間の非互換性による問題を回避できます。

### 2. サービス定義

- `services` セクションで、アプリケーションを構成する各サービスを定義してください。
- 各サービスには、`image`, `build`, `ports`, `volumes`, `environment`, `depends_on` などの設定項目を指定してください。
- サービス名は明確で分かりやすい名前を付けてください。

### 3. ネットワークとボリューム管理

- `networks` セクションで、コンテナー間のネットワークを定義してください。
- `volumes` セクションで、コンテナー間で共有するボリュームを定義してください。
- ネットワークとボリュームを適切に管理していただくことで、コンテナー間の通信とデータ永続化を効率的に行うことができます。

### 4. 環境変数

- 環境変数を活用して、設定値を外部化してください。
- `.env` ファイルや環境変数ファイルを活用して、機密情報や環境依存の設定値を管理してください。
- Docker Composeファイルには、直接機密情報を記述しないようにしてください。

### 5. ヘルスチェック

- `healthcheck` を実装して、コンテナーのヘルス状態を監視してください。
- ヘルスチェックを実装していただくことで、コンテナーの異常を自動的に検出し、再起動などの対応ができます。

### 6. 依存関係の管理

- `depends_on` を使用して、サービス間の依存関係を定義してください。
- 依存関係を定義していただくことで、サービスの起動順序を制御し、アプリケーションの起動時の問題を回避できます。

### 7. ファイル構成

- Docker Composeファイル (`docker-compose.yml`) は、プロジェクトのルートディレクトリに配置してください。
- 環境変数ファイル (`.env`) もプロジェクトのルートディレクトリに配置してください。
- 必要に応じて、Docker Composeの設定ファイルを複数に分割し、`docker-compose.override.yml` などを使用して環境ごとの設定を上書きしてください。

## まとめ

DockerfileとDocker Composeの作成規約に従っていただくことで、より効率的で安全、かつ保守性の高いDocker環境を構築できます。これらの規約を参考に、プロジェクトに最適なDocker環境を構築してください。

このドキュメントは、Dockerのベストプラクティスに基づいて作成されていますが、プロジェクトの要件や環境によって最適な規約は異なる場合があります。必要に応じて、これらの規約を調整し、プロジェクトに最適なものを作成してください。
