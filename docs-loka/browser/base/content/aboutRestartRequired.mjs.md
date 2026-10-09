# browser/base/content/aboutRestartRequired.mjs

source: browser/base/content/aboutRestartRequired.mjs
source-hash: 5a9c5487e2488d9e468c62f2d5f2168f5cc31861
lines: 53

## <module>
- 役割: 再起動が必要になったことを知らせるページの初期化。再起動ボタン、詳細の開閉、テスト用の読み込み完了通知を扱う。
- 呼び出し先: `AboutRestartRequired.init()`, `document.dispatchEvent()`

## addAutofocus()
- 位置: async L13-19
- 役割: トップレベルのフレームでだけ、再起動ボタンに autofocus を付ける。
- 触るとき: 再起動ページの初期フォーカスを変えるとき。
- 呼び出し先: `button.setAttribute()`
- 参照: `button.updateComplete`, `window.top`

## restart()
- 位置: L20-24
- 役割: eRestart と eAttemptQuit を指定してアプリの終了と再起動を要求する。
- 触るとき: 再起動時の終了フラグや挙動を変えるとき。
- 呼び出し先: `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.startup`

## toggleDetails()
- 位置: L25-35
- 役割: 詳細欄の表示を切り替え、トグルの aria-expanded と文言 ID を更新する。
- 触るとき: 詳細の開閉表示や文言を変えるとき。
- 呼び出し先: `toggle.setAttribute()`
- 参照: `details.hidden`

## init()
- 位置: L36-45
- 役割: 再起動ボタンと詳細トグルに click を登録し、ボタンへの autofocus を依頼する。
- 触るとき: ページ初期化時の配線を追加・変更するとき。
- 呼び出し先: `document.getElementById()`, `restartButton.addEventListener()`, `this.addAutofocus()`, `this.restart()`, `this.toggleDetails()`, `toggle.addEventListener()`
