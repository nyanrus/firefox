# browser/components/aboutlogins/content/components/login-list-item.stories.mjs

source: browser/components/aboutlogins/content/components/login-list-item.stories.mjs
source-hash: 51a85aa196261635177a57f0f17cbd737b15973b
lines: 62

## <module>
- 役割: login-list-item 系コンポーネントの Storybook 定義。タイトル、コンポーネント名、FTL の読み込みを宣言する
- 呼び出し先: `window.MozXULElement.insertFTLIfNeeded()`

## NewLoginListItem()
- 位置: L16-18
- 役割: 新規作成行(new-list-item)を selected 指定付きで描画するストーリー
- 触るとき: 新規作成行の見た目を確認・変更するとき
- 呼び出し先: `html()`

## LoginListItem()
- 位置: L28-43
- 役割: ログイン行(login-list-item)を title、username、通知アイコン、selected を指定して描画するストーリー
- 触るとき: 通知アイコン(breached や vulnerable)付きの行の見た目を確認するとき。argTypes に選択肢が定義されている
- 呼び出し先: `html()`
