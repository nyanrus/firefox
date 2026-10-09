# browser/components/customizableui/DragPositionManager.sys.mjs

source: browser/components/customizableui/DragPositionManager.sys.mjs
source-hash: e40a321055d9fb8fb8016e9140c9b273d209f715
lines: 477

## <module>
- 役割: カスタマイズモードで、パレットのグリッド状ドラッグ&ドロップの位置計算と挿入位置のアニメーションを担う AreaPositionManager と、その管理用 DragPositionManager を定義する。
- 呼び出し先: `Object.freeze()`

## AreaPositionManager.constructor()
- 位置: L61-68
- 役割: エリアのコンテナの向き(RTL)と外接矩形を保存し、update で子要素の寸法を計測する。
- 触るとき: ドラッグ開始時にエリアの配置情報がどこで作られるか、またはパレットの RTL 対応を見直すときに見る。
- 呼び出し先: `DOMRectReadOnly.fromRect()`, `aContainer.getBoundingClientRect()`, `this.update()`
- 参照: `aContainer.documentGlobal.RTL_UI`, `this.#containerInfo`, `this.#rtl`

## AreaPositionManager.update()
- 位置: L96-116
- 役割: 表示中の子要素の位置を読み、子要素の水平間隔と高さから列の幅比を求める。
- 触るとき: パレットの要素を増減させた後にドロップ位置の判定がずれるとき、または計測のタイミングを変えるときに見る。
- 呼び出し先: `this.#lazyStoreGet()`
- 参照: `aContainer.children`, `child.hidden`, `coordinates.height`, `coordinates.left`, `last.left`, `this.#containerInfo.width`, `this.#heightToWidthFactor`, `this.#horizontalDistance`

## AreaPositionManager.find()
- 位置: L141-184
- 役割: 座標に最も近い子要素を、行の違いを重く見る重み付き距離で選び、右端寄りなら次の兄弟を返す。
- 触るとき: ドラッグ中にどの位置へ落ちるかが期待と違うとき、特に行をまたぐ場合の判定を調べるときに見る。
- 呼び出し先: `this.#lazyStoreGet()`
- 条件付き依存: `if (closest)` → `this.#lazyStoreGet()`
- 参照: `Number.MAX_VALUE`, `aContainer.children`, `closest.nextElementSibling`, `coordinates.x`, `coordinates.y`, `targetBounds.bottom`, `targetBounds.top`, `this.#containerInfo.left`, `this.#containerInfo.top`, `this.#heightToWidthFactor`, `this.#rtl`

## AreaPositionManager.insertPlaceholder()
- 位置: L203-246
- 役割: 挿入位置より後ろの子要素を CSS transform で押しずらし、同じエリア内からの移動では初回のみ transition を抑える。
- 触るとき: ドラッグ中に要素がぎこちなく動く、または挿入位置の隙間が正しく空かないときに見る。
- 条件付き依存: `if (aIsFromThisArea && !this.#lastPlaceholderInsertion)` → `child.setAttribute()`
- 条件付き依存: `if (isShifted)` → `this.#diffWithNext()`
- 条件付き依存: `if ( aContainer.lastElementChild && aIsFromThisArea && !this.#lastPlaceholderInsertion )` → `aContainer.lastElementChild.getBoundingClientRect()`
- 条件付き依存: `if ( aContainer.lastElementChild && aIsFromThisArea && !this.#lastPlaceholderInsertion )` → `child.removeAttribute()`
- 参照: `aContainer.children`, `aContainer.lastElementChild`, `child.hidden`, `child.style.transform`, `this.#lastPlaceholderInsertion`

## AreaPositionManager.clearPlaceholders()
- 位置: L259-276
- 役割: 全子要素の transform を消し、noTransition 指定時は transition なしで戻して挿入位置の記録も消す。
- 触るとき: ドラッグを取り消した後に要素が元の位置へ戻らないとき、または戻るときのアニメーションを変えたいときに見る。
- 条件付き依存: `if (aNoTransition)` → `child.setAttribute()`
- 条件付き依存: `if (aNoTransition)` → `child.getBoundingClientRect()`
- 条件付き依存: `if (aNoTransition)` → `child.removeAttribute()`
- 参照: `aContainer.children`, `child.style.transform`, `this.#lastPlaceholderInsertion`

## AreaPositionManager.#diffWithNext()
- 位置: L290-333
- 役割: ノードごとに、挿入分だけずらす translate 量を計算する。次の兄弟があればその位置差を使い、なければ行の先頭か前の要素から推定する。
- 触るとき: ドラッグ中に後続の要素が正しい量ずれないとき、または行末や行頭での挙動を調べるときに見る。
- 呼び出し先: `this.#getVisibleSiblingForDirection()`, `this.#lazyStoreGet()`
- 条件付き依存: `if (next)` → `this.#lazyStoreGet()`
- 条件付き依存: `if (!(next))` → `this.#firstInRow()`
- 条件付き依存: `if (!(aNode == firstNode))` → `this.#moveNextBasedOnPrevious()`
- 参照: `aSize.height`, `aSize.width`, `nodeBounds.top`, `otherBounds.top`, `this.#horizontalDistance`, `this.#rtl`

## AreaPositionManager.#moveNextBasedOnPrevious()
- 位置: L348-364
- 役割: 次の兄弟がないとき前の兄弟との差を使ってずらし、行が溢れる場合は次の行の先頭に合わせる。
- 触るとき: 行の末尾にあるアイテムが行の折り返しを越えて飛ぶように見えるときに見る。
- 呼び出し先: `this.#getVisibleSiblingForDirection()`, `this.#lazyStoreGet()`
- 条件付き依存: `if ( (!this.#rtl && xDiff + aNodeBounds.right > bound) || (this.#rtl && xDiff + aNodeBounds.left < bound) )` → `this.#lazyStoreGet()`
- 参照: `aNodeBounds.left`, `aNodeBounds.right`, `this.#containerInfo`, `this.#rtl`

## AreaPositionManager.#lazyStoreGet()
- 位置: L377-389
- 役割: ノードの矩形を初めて要求されたときに DOMRectReadOnly として取得して保持し、以降は同じ値を返す。
- 触るとき: ドラッグ中に古い位置を使って判定がずれるとき、またはキャッシュの寿命を変えるときに見る。
- 呼び出し先: `this.#nodePositionStore.get()`
- 条件付き依存: `if (!rect)` → `DOMRectReadOnly.fromRect()`
- 条件付き依存: `if (!rect)` → `aNode.getBoundingClientRect()`
- 条件付き依存: `if (!rect)` → `this.#nodePositionStore.set()`

## AreaPositionManager.#firstInRow()
- 位置: L398-412
- 役割: 前の兄弟をたどり、ノードと同じ行の先頭を探す。行の判定には top と bottom の床関数を使う。
- 触るとき: 行の先頭を基準にした位置計算が外れるとき、または折り返しの判定を変えるときに見る。
- 呼び出し先: `Math.floor()`, `this.#getVisibleSiblingForDirection()`, `this.#lazyStoreGet()`
- 参照: `this.#lazyStoreGet(aNode).top`, `this.#lazyStoreGet(prev).bottom`

## AreaPositionManager.#getVisibleSiblingForDirection()
- 位置: L424-430
- 役割: 指定方向(previous か next)の兄弟要素を、hidden のものを飛ばして返す。
- 触るとき: 非表示の要素がドラッグ位置の計算に混ざるとき、またはより多くの兄弟の扱いを変えるときに見る。
- 参照: `rv.hidden`

## start()
- 位置: L445-455
- 役割: パレットの AreaPositionManager を作り、既にあれば update で計測し直す。
- 触るとき: カスタマイズモードに入ったときの位置管理の初期化や、再計測のタイミングを調べるときに見る。
- 呼び出し先: `aWindow.document.getElementById()`, `gManagers.get()`
- 条件付き依存: `if (positionManager)` → `positionManager.update()`
- 条件付き依存: `if (!(positionManager))` → `gManagers.set()`

## stop()
- 位置: L460-462
- 役割: キャッシュ済みの AreaPositionManager を全て捨てるため、WeakMap を作り直す。
- 触るとき: カスタマイズモードを抜けた後も古い計測値が残るように見えるときに見る。

## getManagerForArea()
- 位置: L471-473
- 役割: 指定エリア DOM ノードに対応する AreaPositionManager を WeakMap から返す。未作成なら undefined を返す。
- 触るとき: ドラッグ処理が特定エリアの位置管理にアクセスするときや、そのエリアが未初期化かを確かめるときに見る。
- 呼び出し先: `gManagers.get()`
