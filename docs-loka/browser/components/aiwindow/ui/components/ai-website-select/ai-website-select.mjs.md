# browser/components/aiwindow/ui/components/ai-website-select/ai-website-select.mjs

source: browser/components/aiwindow/ui/components/ai-website-select/ai-website-select.mjs
source-hash: 024905b7209d8d20fc4602890c681c67c0a30432
lines: 130

## <module>
- 役割: サイト1件分のチェックボックス行 ai-website-select を定義する。
- 呼び出し先: `customElements.define()`

## AIWebsiteSelect.constructor()
- 位置: L32-40
- 役割: token、linkedPanel、label、iconSrc、url を空文字、checked を false にする。
- 触るとき: 行の既定値を変えるとき、または行が初期化されない原因を調べるとき。
- 呼び出し先: `super()`
- 参照: `this.checked`, `this.iconSrc`, `this.label`, `this.linkedPanel`, `this.token`, `this.url`

## AIWebsiteSelect.handleCheckboxChange()
- 位置: L48-74
- 役割: チェックボックスの変更を止め、token などを載せた ai-website-select:change を発火する。親が preventDefault しなかった時だけ checked を更新する。
- 触るとき: 親が選択を拒否する仕組みを使うとき、または行の状態が親とずれるとき。
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `changeEvent.defaultPrevented`, `event.target.checked`, `this.checked`, `this.iconSrc`, `this.label`, `this.linkedPanel`, `this.token`, `this.url`

## AIWebsiteSelect.setChecked()
- 位置: L81-105
- 役割: checked が同じなら何もしない。違えば change イベントを発火し、親が止めなければ checked を変える。
- 触るとき: 親からの一括選択や解除で行の状態を変えるときに経路を追う。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `changeEvent.defaultPrevented`, `this.checked`, `this.iconSrc`, `this.label`, `this.linkedPanel`, `this.token`, `this.url`

## AIWebsiteSelect.render()
- 位置: L107-126
- 役割: moz-checkbox を描画し、name と value に linkedPanel、ラベルと aria-label に label、アイコンに iconSrc(無ければ既定の favicon)を使う。
- 触るとき: 行の表示項目やアイコンの既定値を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.checked`, `this.handleCheckboxChange`, `this.iconSrc`, `this.label`, `this.linkedPanel`
