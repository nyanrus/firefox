# browser/components/aiwindow/ui/components/smartwindow-footer/smartwindow-footer.mjs

source: browser/components/aiwindow/ui/components/smartwindow-footer/smartwindow-footer.mjs
source-hash: 0a0928a85019079837c06430176ed18aba6d5a41
lines: 58

## <module>
- 役割: スマートウィンドウのフルページ下部のフッター(履歴とチャット一覧への入口)を定義するモジュール。
- 呼び出し先: `customElements.define()`

## SmartwindowFooter.handleActionClick()
- 位置: L14-22
- 役割: chats か history 以外は警告して止め、許可された場合は上位のクローム窓の FirefoxViewHandler で該当タブを開く。
- 触るとき: フッターから開くタブを増やす・変えるとき、またはボタンを押しても開かない理由を調べるとき。
- 呼び出し先: `ALLOWED_ACTIONS.includes()`, `topWin.FirefoxViewHandler.openTab()`
- 条件付き依存: `if (!ALLOWED_ACTIONS.includes(action))` → `console.warn()`
- 参照: `window.browsingContext.topChromeWindow`

## SmartwindowFooter.render()
- 位置: L24-54
- 役割: 履歴とチャット一覧の2つのゴースト型 moz-button を描き、押すと handleActionClick を呼ぶ。
- 触るとき: フッターのボタン構成、アイコン、ツールチップを変えるとき。
- 呼び出し先: `html()`, `this.handleActionClick()`
