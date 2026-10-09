# browser/base/content/safeMode.js

source: browser/base/content/safeMode.js
source-hash: 48d4ddb299c96dad7314d1a4fd13357b0854b06a
lines: 75

## <module>
- 役割: セーフモード確認ダイアログ(safeMode.xhtml)のスクリプト。自動セーフモードかどうかでボタンの表示を切り替え、既定・キャンセル・extra1 の各ダイアログイベントを対応するハンドラに結びつける。
- 呼び出し先: `ChromeUtils.importESModule()`, `document.addEventListener()`, `document.getElementById()`, `window.addEventListener()`

## showResetDialog()
- 位置: L13-29
- 役割: resetProfile.xhtml をモーダルで開き、利用者がリセットを確定した場合のみ ResetProfile.doReset() を呼ぶ。
- 触るとき: リセット確認画面の開き方や、リセットを実行する条件を変えるとき。extra1 ボタンからも呼ばれる。
- 呼び出し先: `ResetProfile.doReset()`, `window.openDialog()`
- 参照: `retVals.reset`

## onDefaultButton()
- 位置: L31-40
- 役割: 既定ボタンの処理。defaultToReset が真ならイベントを止めて ResetProfile.doReset() でリセットを始め、偽ならそのままセーフモードで続行する。
- 触るとき: 既定ボタンでセーフモードに入るか、リセットへ進むかの判定を変えるとき。現在 defaultToReset は false のまま変更されない(要確認)。
- 条件付き依存: `if (defaultToReset)` → `event.preventDefault()`
- 条件付き依存: `if (defaultToReset)` → `ResetProfile.doReset()`

## onCancel()
- 位置: L42-44
- 役割: キャンセル時に appStartup.quit(eForceQuit) で本体を終了する。
- 触るとき: セーフモード確認ダイアログを閉じたときの終了動作を変えるとき。
- 呼び出し先: `appStartup.quit()`
- 参照: `appStartup.eForceQuit`

## onExtra1()
- 位置: L46-53
- 役割: extra1 ボタンの処理。defaultToReset が真ならウィンドウを閉じてセーフモードで続行し、そのうえで showResetDialog() を呼ぶ。
- 触るとき: extra1 ボタン(リセットの入口)の振る舞いを変えるとき。defaultToReset の値によって分岐が変わる点に注意する。
- 呼び出し先: `showResetDialog()`
- 条件付き依存: `if (defaultToReset)` → `window.close()`
