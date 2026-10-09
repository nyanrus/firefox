# browser/components/urlbar/ActionsProvider.sys.mjs

source: browser/components/urlbar/ActionsProvider.sys.mjs
source-hash: 521df2627fa4e459dc793a74139a1eb178d382b3
lines: 76

## <module>
- 役割: urlbar の入力に対して組み込みアクション（ボタン行）を返すプロバイダの基底クラスと、結果オブジェクトの型を定義する。

## ActionsProvider.name()
- 位置: L15-17
- 役割: プロバイダ固有の名前を返す基底実装（"ActionsProviderBase"）。
- 触るとき: 新しいアクションプロバイダを作るとき、名前を派生クラスで上書きする必要を確かめるとき。

## ActionsProvider.isActive()
- 位置: L28-30
- 役割: 基底では例外を投げる抽象メソッド。派生クラスが、この入力で問い合わせをするかを返す。
- 触るとき: 新しいプロバイダの起動条件を決めるとき。

## ActionsProvider.queryActions()
- 位置: async L39-41
- 役割: 基底では例外を投げる抽象メソッド。入力に応じた ActionsResult の配列を Promise で返す。
- 触るとき: 新しいプロバイダが結果をどう返すかを決めるとき。

## ActionsProvider.onPick()
- 位置: L49-49
- 役割: 基底では何もしない。アクションボタンが選ばれたときの処理を派生クラスで実装する。
- 触るとき: アクションを選んだときの動作を追加するとき。
