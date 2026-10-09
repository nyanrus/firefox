# browser/components/sessionstore/PageWireframes.sys.mjs

source: browser/components/sessionstore/PageWireframes.sys.mjs
source-hash: ed59f8637d970ee4232030ca844b7f3b476b2ded
lines: 126

## <module>
- 役割: セッション履歴のエントリに保存されたワイヤーフレーム(ページ上の矩形情報)を取り出し、履歴プレビュー用の SVG に変換する。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## getWireframeState()
- 位置: L21-27
- 役割: タブの現在の履歴インデックスにあるエントリのワイヤーフレームを返す。タブが無ければ null を返し、履歴やワイヤーフレームが無ければ undefined になる。
- 触るとき: 履歴プレビューでワイヤーフレームが無い場合にどの値が返るかを確認するとき。収集は browser.history.collectWireframes が有効なときだけ行われる。
- 呼び出し先: `lazy.SessionStore.getSessionHistory()`
- 参照: `sessionHistory.index`, `sessionHistory?.entries`, `sessionHistory?.entries[sessionHistory.index]?.wireframe`

## getWireframeElementForTab()
- 位置: L36-39
- 役割: タブの現在のワイヤーフレームを、そのタブの ownerDocument で SVG 要素にする。ワイヤーフレームが無ければ undefined を返す。
- 触るとき: 戻る・進むのプレビュー画像を作る箇所で、ワイヤーフレームが無い履歴のときに呼び出し側が何を受け取るかを調べるとき。
- 呼び出し先: `this.getWireframeElement()`, `this.getWireframeState()`
- 参照: `tab.ownerDocument`

## nscolorToRGB()
- 位置: L50-55
- 役割: nscolor 形式の 32bit 整数の下位バイトを赤、次を緑、次を青として rgb() 文字列にする。アルファ値は使わない。
- 触るとき: ワイヤーフレームの色の解釈を直すとき、またはプレビューの色が想定と違うときにバイト順を確認する。

## getWireframeElement()
- 位置: L68-124
- 役割: 矩形群から viewBox を決め、背景色と各矩形を載せた SVG 要素を作る。type が unknown の矩形は描かない。
- 触るとき: 履歴プレビューの見た目を変えるとき。幅と高さは保存値ではなく矩形の右下端の最大値から推定しているので、ずれが出たらこの計算を疑う。画像と文字は色が無いとき既定の半透明グレーで塗る。
- 呼び出し先: `Math.max()`, `document.createElementNS()`, `rectEl.setAttribute()`, `svg.appendChild()`, `svg.setAttributeNS()`, `this.nscolorToRGB()`, `wireframe.rects.reduce()`
- 参照: `rect.height`, `rect.width`, `rect.x`, `rect.y`, `rectObj.color`, `rectObj.height`, `rectObj.type`, `rectObj.width`, `rectObj.x`, `rectObj.y`, `svg.style.backgroundColor`, `wireframe.canvasBackground`, `wireframe.rects`
