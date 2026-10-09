# browser/components/aiwindow/ui/components/smartwindow-smartbar-glow/smartwindow-smartbar-glow.mjs

source: browser/components/aiwindow/ui/components/smartwindow-smartbar-glow/smartwindow-smartbar-glow.mjs
source-hash: c38ec4760dd49c395003a919a1ff004c5007a4a9
lines: 645

## <module>
- 役割: スマートバー周囲のカーソル追従グロー(SVG 多角形)を描く custom element を定義する
- 呼び出し先: `customElements.define()`

## clamp()
- 位置: L113-115
- 役割: 値を min と max の範囲に収める
- 触るとき: 補間の入力や割合を 0 から 1 などの範囲に丸めたいとき
- 呼び出し先: `Math.max()`, `Math.min()`

## lerp()
- 位置: L123-125
- 役割: from と to を fraction の割合で線形補間する
- 触るとき: キーフレーム間の混合やアニメーション値の移動量を計算しているとき

## samplePolyline()
- 位置: L136-153
- 役割: 折れ線上で 0 から 1 の割合に当たる点を求める
- 触るとき: 上辺・下辺に等間隔のサンプル点を置く計算を調べるとき、多角形の辺の形を変えるとき
- 呼び出し先: `Math.floor()`, `Math.min()`, `clamp()`, `lerp()`
- 参照: `points.length`, `points[segmentIndex + 1].x`, `points[segmentIndex + 1].y`, `points[segmentIndex].x`, `points[segmentIndex].y`

## SmartwindowSmartbarGlow.constructor()
- 位置: L235-242
- 役割: マウス移動とアニメーションのハンドラを作り、参照を固定する
- 触るとき: コンストラクタで初期化する内部状態を増やすとき
- 呼び出し先: `super()`
- 参照: `this.#boundMouseMove`, `this.#boundTick`

## this.#boundMouseMove()
- 位置: L239-240
- 役割: mousemove のハンドラを一度だけ束縛し、追加と削除で同じ参照を使えるようにする
- 触るとき: マウス移動の購読が外れない不具合を調べるとき
- 呼び出し先: `this.#onMouseMove()`

## this.#boundTick()
- 位置: L241-241
- 役割: requestAnimationFrame に渡す tick を一度だけ束縛する
- 触るとき: フレーム予約が重複する、または効かない問題を調べるとき
- 呼び出し先: `this.#tick()`

## SmartwindowSmartbarGlow.connectedCallback()
- 位置: L244-260
- 役割: window の mousemove を購読し、親の属性を監視する MutationObserver を張る
- 触るとき: 親要素の focused や open 属性による表示切り替えを変えるとき、接続時の初期化を調べるとき
- 呼び出し先: `super.connectedCallback()`, `this.#scheduleTick()`, `window.addEventListener()`
- 条件付き依存: `if (this.parentElement)` → `this.#syncStateFromParent()`
- 条件付き依存: `if (this.parentElement)` → `this.#attributeObserver.observe()`
- 参照: `SmartwindowSmartbarGlow.OBSERVED_PARENT_ATTRIBUTES`, `this.#attributeObserver`, `this.#boundMouseMove`, `this.parentElement`

## SmartwindowSmartbarGlow.disconnectedCallback()
- 位置: L262-271
- 役割: mousemove の購読、フレーム予約、監視を解除し、cached な windowUtils を捨てる
- 触るとき: 要素が別の document に移った後に古い windowUtils を使ってしまう問題を調べるとき
- 呼び出し先: `cancelAnimationFrame()`, `super.disconnectedCallback()`, `this.#attributeObserver?.disconnect()`, `window.removeEventListener()`
- 参照: `this.#animationFrameId`, `this.#attributeObserver`, `this.#boundMouseMove`, `this.#winUtils`

## SmartwindowSmartbarGlow.firstUpdated()
- 位置: L273-281
- 役割: SVG の要素参照を取得し、親状態を同期してから最初の tick を予約する
- 触るとき: 初回描画で表示が一瞬ずれる、または描画されないときに調べる
- 呼び出し先: `this.#scheduleTick()`, `this.#syncStateFromParent()`, `this.renderRoot.querySelector()`
- 参照: `this.#pathElement`, `this.#svgElement`

## SmartwindowSmartbarGlow.referenceElement()
- 位置: L289-291
- 役割: グローの幾何を決める基準要素(入力欄)を返す getter
- 触るとき: どの要素の矩形を基準にするかを追うとき
- 参照: `this.#referenceElement`

## SmartwindowSmartbarGlow.referenceElement()
- 位置: L293-296
- 役割: 基準要素を設定し、次の tick を予約する setter
- 触るとき: 親コンポーネントが基準要素を差し替えたときの再描画を調べるとき
- 呼び出し先: `this.#scheduleTick()`
- 参照: `this.#referenceElement`

## SmartwindowSmartbarGlow.#syncStateFromParent()
- 位置: L308-327
- 役割: 親の focused と open を読み、closing 時に cornerSpread を 0 に戻して mousemove の購読を切り替える
- 触るとき: フォーカス時に静止状態へ戻す挙動や、開閉時の角の出現アニメーションを変えるとき
- 呼び出し先: `parentEl.hasAttribute()`, `this.#scheduleTick()`
- 条件付き依存: `if (isOpen)` → `window.removeEventListener()`
- 条件付き依存: `if (!(isOpen))` → `window.addEventListener()`
- 参照: `this.#boundMouseMove`, `this.#cornerSpread`, `this.#isFocused`, `this.#parentWasOpen`, `this.parentElement`

## SmartwindowSmartbarGlow.#onMouseMove()
- 位置: L330-334
- 役割: マウス座標を保存して tick を予約する
- 触るとき: カーソル座標の取り方(clientX/Y)を変えるとき
- 呼び出し先: `this.#scheduleTick()`
- 参照: `event.clientX`, `event.clientY`, `this.#cursorX`, `this.#cursorY`

## SmartwindowSmartbarGlow.#scheduleTick()
- 位置: L337-341
- 役割: 未予約なら requestAnimationFrame で tick を 1 回だけ予約する
- 触るとき: アニメーションが始まらない、または多重に走るときに調べる
- 条件付き依存: `if (!this.#animationFrameId)` → `requestAnimationFrame()`
- 参照: `this.#animationFrameId`, `this.#boundTick`

## SmartwindowSmartbarGlow.#tick()
- 位置: L353-506
- 役割: 毎フレーム、矩形とカーソル距離から目標値を求めて平滑化し、path を書き込み、値が動く間だけ再予約する
- 触るとき: グローの反応速度や到達範囲を変えるとき、アニメーションが止まらない(または早く止まる)ときに調べる
- 呼び出し先: `Math.max()`, `Math.min()`, `Math.sqrt()`, `adjustForFrameTime()`, `clamp()`, `hostHeight.toFixed()`, `hostWidth.toFixed()`, `lerp()`, `this.#bias.toFixed()`, `this.#bottomBumpX.toFixed()`, `this.#buildPath()`, `this.#cornerSpread.toFixed()`, `this.#engagement.toFixed()`, `this.#pathElement.setAttribute()`, `this.#topBumpX.toFixed()`, `winUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (hostWidth !== this.#hostWidth || hostHeight !== this.#hostHeight)` → `this.#svgElement.setAttribute()`
- 条件付き依存: `if (snapshot !== this.#lastTickSnapshot)` → `this.#scheduleTick()`
- 参照: `POLYGON_REST[0].x`, `POLYGON_REST[3].x`, `hostRect.height`, `hostRect.left`, `hostRect.top`, `hostRect.width`, `referenceRect.height`, `referenceRect.left`, `referenceRect.top`, `referenceRect.width`, `this.#animationFrameId`, `this.#bias`, `this.#bottomBumpX`, `this.#cornerSpread`, `this.#cursorX`, `this.#cursorY`, `this.#engagement`, `this.#hostHeight`, `this.#hostWidth`, `this.#isFocused`, `this.#lastTickSnapshot`, `this.#lastTickTime`, `this.#pathElement`, `this.#svgElement`, `this.#topBumpX`, `this.#winUtils`, `this.documentGlobal.windowUtils`, `this.referenceElement`

## adjustForFrameTime()
- 位置: L371-372
- 役割: 平滑化係数を経過時間で補正し、60Hz 以外の画面でも同じ速さに保つ
- 触るとき: 高リフレッシュレートの画面で動きが速すぎる、または遅すぎるときに調べる

## SmartwindowSmartbarGlow.#buildPath()
- 位置: L523-604
- 役割: 現在の状態から six 点の多角形と上下のこぶ(ベル曲線)を求め、SVG の path 文字列を作る
- 触るとき: グローの形そのもの(角の張り出し、こぶの高さや幅)を変えるとき
- 呼び出し先: `Math.max()`, `Math.min()`, `POLYGON_REST.map()`, `clamp()`, `lerp()`, `pathSegments.join()`, `pathSegments.push()`, `traceEdge()`
- 参照: `POLYGON_LEFT[anchorIndex].x`, `POLYGON_LEFT[anchorIndex].y`, `POLYGON_RIGHT[anchorIndex].x`, `POLYGON_RIGHT[anchorIndex].y`, `anchors[0].x`, `anchors[0].y`, `anchors[3].x`, `anchors[3].y`, `restAnchor.x`, `restAnchor.y`, `this.#bias`, `this.#bottomBumpX`, `this.#cornerSpread`, `this.#engagement`, `this.#topBumpX`

## traceEdge()
- 位置: L583-598
- 役割: 一辺を EDGE_SAMPLES 点でたどり、こぶ位置に応じて y 座標を押し出して path の区間を積む
- 触るとき: こぶの向きや曲線の滑らかさ(サンプル数)を変えるとき
- 呼び出し先: `(samplePoint.y + bumpDirection * bumpHeight).toFixed()`, `Math.exp()`, `pathSegments.push()`, `samplePoint.x.toFixed()`, `samplePolyline()`
- 参照: `pathSegments.length`, `samplePoint.x`, `samplePoint.y`

## SmartwindowSmartbarGlow.render()
- 位置: L609-641
- 役割: SVG の枠と線形グラデーション(3 色の停止点)と glow-path を描く
- 触るとき: グローの配色やグラデーションの向きを変えるとき、CSS 変数との対応を確認するとき
- 呼び出し先: `html()`, `svg()`
