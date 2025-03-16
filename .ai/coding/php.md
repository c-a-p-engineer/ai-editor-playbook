# PHP コーディング規約

このプロジェクトでは、PHPコードの品質と保守性を高めるため、以下のコーディング規約に従います。

## 基本規約

- **PSR-12** に準拠します。
- **PHP 7.4** 以上を対象とします。
- **UTF-8** エンコーディングを使用します。
- **インデント** はスペース4文字とします。
- **行末** は改行コード（LF）とします。
- **名前空間** を使用します。
- **クラス名** は `StudlyCaps` 形式とします。
- **メソッド名** と **変数名** は `camelCase` 形式とします。
- **定数名** は `UPPER_SNAKE_CASE` 形式とします。
- **コメント** は英語で記述します。

## 詳細規約

### ファイル

- ファイルの先頭には、ライセンス情報を記述します。
- ファイルの末尾には、空行を入れます。
- 1ファイル1クラス（またはtrait、interface）とします。

### 名前空間とuse

- 名前空間は、プロジェクトのディレクトリ構造に対応させます。
- use文は、クラスの先頭にまとめて記述します。
- グローバル名前空間のクラスは、use文で明示的にインポートします。

### クラス、メソッド、変数

- クラス、メソッド、変数には、適切なアクセス修飾子（public, protected, private）を付与します。
- メソッドの引数と返り値の型宣言を積極的に行います。
- 変数のスコープを最小限にします。
- マジックメソッドの使用は必要最小限に留めます。

### 制御構造

- 制御構造（if, for, while, switchなど）のブロックは、常に波括弧 `{}` で囲みます。
- `elseif` ではなく `else if` を使用します。
- `switch` 文では、`break` を忘れずに記述します。

### 関数とメソッド

- 関数とメソッドは、単一の責務を持つように小さく分割します。
- 関数の引数の数は、できるだけ少なくします。
- 副作用のある関数やメソッドは、ドキュメントで明示的に記述します。

### エラー処理

- 例外処理を積極的に行います。
- エラーメッセージは、ユーザーに分かりやすいように記述します。
- エラーログを適切に出力します。

### コメントとドキュメンテーション

- コードの意図や処理内容を明確にするために、適切なコメントを記述します。
- PHPDoc形式で、クラス、メソッド、関数にドキュメントを記述します。
- 複雑な処理やロジックには、詳細なコメントを記述します。

### その他

- 可読性の高いコードを心がけます。
- コードの重複を避けます。
- マジックナンバーの使用を避けます。定数を定義して使用します。
- パフォーマンスを考慮したコードを記述します。
- セキュリティを考慮したコードを記述します。

## 例

```php
<?php

namespace App\Controller;

use App\Model\User;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

class UserController
{
    /**
     * @var UserRepository
     */
    private $userRepository;

    public function __construct(UserRepository $userRepository)
    {
        $this->userRepository = $userRepository;
    }

    /**
     * ユーザー一覧を表示する
     *
     * @param Request $request
     * @return Response
     */
    public function index(Request $request): Response
    {
        $users = $this->userRepository->findAll();

        return new Response(
            'users/index.html.php',
            ['users' => $users]
        );
    }

    /**
     * ユーザーを登録する
     *
     * @param Request $request
     * @return Response
     */
    public function create(Request $request): Response
    {
        $name = $request->get('name');
        $email = $request->get('email');

        $user = new User($name, $email);
        $this->userRepository->save($user);

        return new Response(
            'users/create.html.php',
            ['user' => $user]
        );
    }
}
```

この規約は、プロジェクトの成長や変化に合わせて、適宜見直していきます。
