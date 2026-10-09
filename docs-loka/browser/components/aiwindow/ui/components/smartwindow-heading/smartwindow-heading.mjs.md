# browser/components/aiwindow/ui/components/smartwindow-heading/smartwindow-heading.mjs

source: browser/components/aiwindow/ui/components/smartwindow-heading/smartwindow-heading.mjs
source-hash: 2656ce90cf7cc9e663a2f65336493805ee8fae1e
lines: 40

## <module>
- 役割: スマートウィンドウのフルページの見出し(ロゴ・タイトル・ベータバッジ)を定義するモジュール。
- 呼び出し先: `customElements.define()`

## SmartwindowHeading.render()
- 位置: L14-36
- 役割: 装飾用のロゴ画像と、ベータバッジを aria-describedby で結んだ h1 の見出しを描く。
- 触るとき: 見出しの表示文言の取得元やバッジの表示を変えるとき。
- 呼び出し先: `html()`
