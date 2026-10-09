# browser/components/aiwindow/ui/components/ai-chat-grid/ai-chat-grid.stories.mjs

source: browser/components/aiwindow/ui/components/ai-chat-grid/ai-chat-grid.stories.mjs
source-hash: 3ca295a1aadfe5b4d02c166969f219011b5a4f93
lines: 162

## <module>
- 役割: ai-chat-grid の Storybook 定義。履歴 URL 風の項目を使い、切り替えの有無を組み合わせる。
- 呼び出し先: `Template.bind()`, `window.MozXULElement.insertFTLIfNeeded()`

## Template()
- 位置: L21-29
- 役割: view、showSwitch、items、描画関数を ai-chat-grid に渡す共通テンプレート。
- 触るとき: ストーリーで渡す項目や描画関数の形を変えるとき、ここで受け渡しを確認する。
- 呼び出し先: `html()`

## gridItem()
- 位置: L86-94
- 役割: 項目 1 件を ai-chat-card で描く関数（切り替えあり、grid 初期表示）。
- 触るとき: グリッドの見た目を試すために ai-chat-card に渡す属性を変えるときに見る。
- 呼び出し先: `html()`
- 参照: `item.favicon`, `item.thumbnail`, `item.timestamp`, `item.title`, `item.url`

## rowItem()
- 位置: L95-115
- 役割: 項目 1 件を favicon、タイトル、日時の 1 行で描く関数（切り替えあり）。
- 触るとき: 一覧の行の見た目を変えるときに見る。
- 呼び出し先: `html()`
- 参照: `item.favicon`, `item.timestamp`, `item.title`

## gridItem()
- 位置: L123-131
- 役割: 項目 1 件を ai-chat-card で描く関数（切り替えなし、grid 表示）。
- 触るとき: 切り替えなしの grid ストーリーを変えるときに見る。
- 呼び出し先: `html()`
- 参照: `item.favicon`, `item.thumbnail`, `item.timestamp`, `item.title`, `item.url`

## rowItem()
- 位置: L139-159
- 役割: 項目 1 件を 1 行で描く関数（切り替えなし、list 表示）。
- 触るとき: 切り替えなしの一覧ストーリーを変えるときに見る。
- 呼び出し先: `html()`
- 参照: `item.favicon`, `item.timestamp`, `item.title`
