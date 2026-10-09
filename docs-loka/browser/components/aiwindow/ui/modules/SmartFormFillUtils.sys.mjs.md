# browser/components/aiwindow/ui/modules/SmartFormFillUtils.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillUtils.sys.mjs
source-hash: a2af5c8ddf9338bc889622d6a766e204d5307895
lines: 169

## <module>
- 役割: フォーム入力欄の近傍にあるテキスト(ラベル代わり)を DOM 走査で探す補助クラスを提供する。

## SmartFormFillUtils.iterateNodes()
- 位置: L38-70
- 役割: 要素の前後の兄弟と親を辿り、フィルタが false 以外を返すか、打ち切り対象の要素に当たるまで走査する。
- 触るとき: 近傍テキストの探索範囲や順序を変えるとき、または探索が途中で止まる原因を調べるとき。
- 条件付き依存: `if (!next)` → `this.shouldStopIterating()`
- 条件付き依存: `if (filter)` → `filter()`
- 条件付き依存: `if (!(!next))` → `this.shouldStopIterating()`
- 参照: `Node.ELEMENT_NODE`, `child.firstChild`, `child.lastChild`, `child.nodeType`, `element.nextSibling`, `element.parentNode`, `element.previousSibling`

## SmartFormFillUtils.shouldStopIterating()
- 位置: L80-95
- 役割: button, input, label, select などの要素名かを判定し、走査を打ち切るべきかを返す。
- 触るとき: 近傍テキストの探索を止める部品の種類を増やす、または減らすとき。
- 参照: `element.localName`

## SmartFormFillUtils.clearCache()
- 位置: L100-103
- 役割: 近傍テキストの逆方向・順方向の WeakMap キャッシュを作り直して空にする。
- 触るとき: DOM が変わった後に古いラベル結果が残るとき、キャッシュを消すタイミングを確認する。
- 参照: `this.#mappedTextForward`, `this.#mappedTextReverse`

## SmartFormFillUtils.findNearbyText()
- 位置: L114-167
- 役割: 方向ごとにキャッシュを使いつつ、テキストノードを最大 10 個まで集め、空白を詰めて返す。
- 触るとき: 入力欄の近傍テキストが切れたり余計なものが混ざったりするとき、取得の上限や結合方法を調べる。
- 呼び出し先: `cache.has()`, `cache.set()`, `this.iterateNodes()`, `txt.replace()`, `txt.replace(/\s{2,}/g, " ").trim()`
- 条件付き依存: `if (cache.has(element))` → `cache.get()`
- 参照: `current.nodeValue`, `this.#mappedTextForward`, `this.#mappedTextReverse`

## returnTextNode()
- 位置: L135-148
- 役割: 走査中のノードを見て、テキストノードなら採用する。上限を超えた場合や、文字を得た後の div に当たった場合は探索を止める。
- 触るとき: 近傍テキストがどこで切れるかを変えるとき。
- 参照: `Node.ELEMENT_NODE`, `Node.TEXT_NODE`, `node.localName`, `node.nodeType`, `txt.length`
