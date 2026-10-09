# browser/components/aboutlogins/content/components/login-list-item.mjs

source: browser/components/aboutlogins/content/components/login-list-item.mjs
source-hash: 32c8dec98f081c59ce3303c8cd62c28e4f32512d
lines: 35

## <module>
- 役割: ログイン一覧の行要素を作る/更新するファクトリ。新規作成行とログイン行の振り分けを担う

## LoginListItemFactory.create()
- 位置: L11-21
- 役割: GUID がなければ新規作成行を、あればログイン行を作り、ログイン情報を流し込んで返す
- 触るとき: 一覧に行を追加する経路を変えるとき、または新規作成行が出ない問題を調べるとき
- 呼び出し先: `LoginListItemFactory.update()`, `loginListItem.classList.add()`
- 条件付き依存: `if (!login.guid)` → `newListItem.classList.add()`
- 参照: `login.guid`

## LoginListItemFactory.update()
- 位置: L23-33
- 役割: タイトル、ユーザー名、favicon を更新し、id と dataset.guid は未設定のときだけ設定する
- 触るとき: 一覧行に表示する項目を増やすとき。id は数字始まりを避けるため lli- を前置する
- 参照: `listItem.dataset.guid`, `listItem.favicon`, `listItem.id`, `listItem.title`, `listItem.username`, `login.guid`, `login.origin`, `login.title`, `login.username`
