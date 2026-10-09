# browser/components/aiwindow/ui/components/smartwindow-overflow-row/SmartwindowOverflowRow.mjs

source: browser/components/aiwindow/ui/components/smartwindow-overflow-row/SmartwindowOverflowRow.mjs
source-hash: 635e04556769e24c2d247a8cd92cb089256cb135
lines: 209

## <module>
- 役割: 横一列の項目を幅に合わせて入るだけ表示し、残りを省略ボタンに畳む共通ミックスインを定義するモジュール。

## SmartwindowOverflowRowMixin()
- 位置: L11-208
- 役割: 基底の要素クラスに、幅に応じた表示件数(visibleCount)の決定を足すミックスインを作る。
- 触るとき: 表示件数の決め方を複数の要素で共有するとき、またはこのミックスインを使う要素を新しく作るとき。

## constructor()
- 位置: L22-25
- 役割: visibleCount を Infinity(全件表示)で初期化する。
- 触るとき: 初期状態で全件を出すかどうかを変えるとき。
- 呼び出し先: `super()`
- 参照: `this.visibleCount`

## overflowContainerSelector()
- 位置: L30-32
- 役割: 項目を並べる行の要素を探すセレクタ(.smartwindow-overflow-row)を返す。
- 触るとき: 使う側で行のクラス名を変えるとき。

## overflowItemSelector()
- 位置: L37-39
- 役割: 行の直下にある role=listitem の子要素を選ぶセレクタを返す。
- 触るとき: 計測対象の項目の指定方法を変えるとき。

## overflowTriggerSelector()
- 位置: L44-46
- 役割: 「+n more」ボタンのセレクタ(.overflow-more)を返す。
- 触るとき: 省略ボタンのクラス名を変えるとき、またはボタンの幅が計算に入らないと疑うとき。

## maxInlineItems()
- 位置: L51-53
- 役割: 幅に関係なく並べられる件数の上限を返す。既定は無限大。
- 触るとき: 要素ごとに表示件数の上限を設けるとき。

## inlineItemCount()
- 位置: L58-60
- 役割: 固定の表示件数を返す。null の場合は幅から計測する。
- 触るとき: 件数を固定して計測を省きたいとき。

## isWidthAware()
- 位置: L65-67
- 役割: inlineItemCount が有限の数でなければ、幅で計測すると判定して返す。
- 触るとき: 固定件数と幅による計測のどちらで件数を決めるかの判定を変えるとき。
- 呼び出し先: `Number.isFinite()`
- 参照: `this.inlineItemCount`

## overflowItems()
- 位置: L72-74
- 役割: 畳む対象の項目の配列を返す。既定は空配列。
- 触るとき: 使う要素で畳む項目を定義するとき。

## isMeasuring()
- 位置: L81-83
- 役割: 計測の次フレームが予約されているかを返す。テストが完了を待つために公開している。
- 触るとき: 計測完了を待つテストの仕組みを変えるとき。
- 参照: `this.#measureRaf`

## connectedCallback()
- 位置: L85-90
- 役割: 接続時に、描画済みなら表示モードを同期する。
- 触るとき: DOM へ再接続したときに表示件数が古いままにならないか確認するとき。
- 呼び出し先: `super.connectedCallback()`
- 条件付き依存: `if (this.hasUpdated)` → `this.syncOverflowMode()`
- 参照: `this.hasUpdated`

## disconnectedCallback()
- 位置: L92-95
- 役割: 切断時に幅の監視と計測予約を止める。
- 触るとき: 要素を外したときの後始末を変えるとき。
- 呼び出し先: `super.disconnectedCallback()`, `this.#stopMeasuring()`

## updated()
- 位置: L97-102
- 役割: 描画のたびに表示モードを同期する。消費側の getter が変わりうるため、毎回実行する。
- 触るとき: 描画後に件数を計算し直すタイミングを変えるとき。
- 呼び出し先: `super.updated()`, `this.syncOverflowMode()`

## syncOverflowMode()
- 位置: L105-113
- 役割: 幅で計測するなら幅の監視と計測予約を行い、固定件数なら計測を止めて件数を設定する。
- 触るとき: 固定件数と幅計測の切り替えの挙動を変えるとき。
- 呼び出し先: `Math.max()`, `this.#setVisibleCount()`, `this.#stopMeasuring()`
- 条件付き依存: `if (this.isWidthAware)` → `this.#observeWidth()`
- 条件付き依存: `if (this.isWidthAware)` → `this.scheduleOverflowMeasure()`
- 参照: `this.inlineItemCount`, `this.isWidthAware`

## scheduleOverflowMeasure()
- 位置: L116-124
- 役割: 計測が予約されていなければ、次のフレームでの計測を1回だけ予約する。
- 触るとき: 計測がいつ走るかを変えるとき、または計測が繰り返し予約される問題を調べるとき。
- 呼び出し先: `requestAnimationFrame()`, `this.#measureOverflow()`
- 参照: `this.#measureRaf`, `this.isWidthAware`

## #observeWidth()
- 位置: L126-137
- 役割: ResizeObserver で幅を見て、前回と違う幅になったときだけ計測を予約する。
- 触るとき: 幅の変化に反応する条件を変えるとき。
- 呼び出し先: `this.#resizeObserver.observe()`, `this.scheduleOverflowMeasure()`
- 参照: `entries[0]?.contentBoxSize`, `entries[0]?.contentBoxSize?.[0]?.inlineSize`, `this.#lastWidth`, `this.#resizeObserver`, `this.#widthChanged`

## #stopMeasuring()
- 位置: L139-145
- 役割: 幅の監視を外し、予約済みの計測を取り消す。
- 触るとき: 計測の後始末の内容を変えるとき。
- 呼び出し先: `cancelAnimationFrame()`, `this.#resizeObserver?.disconnect()`
- 参照: `this.#lastWidth`, `this.#measureRaf`, `this.#resizeObserver`

## #setVisibleCount()
- 位置: L147-151
- 役割: 値が変わったときだけ visibleCount を更新する。
- 触るとき: 表示件数の更新の仕方を変えるとき。
- 参照: `this.visibleCount`

## #measureOverflow()
- 位置: L153-207
- 役割: 各項目の幅を測って行に収まる件数を求める。収まらなければ省略ボタンの幅を足して件数を減らし、幅が広がったときだけ件数を増やす。
- 触るとき: 溢れの判定や、件数が増えない・減らない問題を調べるとき。
- 呼び出し先: `Math.min()`, `child.getBoundingClientRect()`, `container.querySelector()`, `container.querySelectorAll()`, `cumulativeItemWidths.at()`, `cumulativeItemWidths.push()`, `getComputedStyle()`, `parseFloat()`, `this.#setVisibleCount()`, `this.renderRoot?.querySelector()`, `trigger?.getBoundingClientRect()`
- 条件付き依存: `if ( children.length <= this.maxInlineItems && cumulativeItemWidths.at(-1) - columnGap <= container.clientWidth )` → `this.#setVisibleCount()`
- 参照: `child.getBoundingClientRect().width`, `children.length`, `container.clientWidth`, `getComputedStyle(container).columnGap`, `items.length`, `this.#widthChanged`, `this.maxInlineItems`, `this.overflowContainerSelector`, `this.overflowItemSelector`, `this.overflowItems`, `this.overflowTriggerSelector`, `this.visibleCount`, `trigger?.getBoundingClientRect().width`
