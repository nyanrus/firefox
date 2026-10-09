# browser/components/aiwindow/ui/components/smartwindow-prompts/smartwindow-prompts.mjs

source: browser/components/aiwindow/ui/components/smartwindow-prompts/smartwindow-prompts.mjs
source-hash: ce519bfa4239587390a858935ae4fb212b4b1777
lines: 330

## <module>
- 役割: 会話の出だしに出す提案ピル(スターター)を横一列に並べて描く smartwindow-prompts を定義するモジュール。
- 呼び出し先: `customElements.define()`

## SmartWindowPrompts.constructor()
- 位置: L35-41
- 役割: prompts を空、mode を fullpage、両方向のスクロール可否を false にして初期化する。
- 触るとき: 初期値を変えるとき、または矢印がいつ出るかの初期条件を調べるとき。
- 呼び出し先: `super()`
- 参照: `this.canScrollEnd`, `this.canScrollStart`, `this.mode`, `this.prompts`

## SmartWindowPrompts.disconnectedCallback()
- 位置: L43-48
- 役割: 切断時にサイズ監視を止め、監視中の要素の記録を消す。
- 触るとき: 要素を外したあとの監視の後始末を変えるとき。
- 呼び出し先: `super.disconnectedCallback()`, `this.#resizeObserver?.disconnect()`
- 参照: `this.#observedContainer`, `this.#resizeObserver`

## SmartWindowPrompts.updated()
- 位置: L50-67
- 役割: コンテナが作り直されたら幅の監視先を付け替え、prompts か mode が変わったらスクロール状態を更新する。
- 触るとき: スクロール矢印の更新タイミングや監視先の扱いを変えるとき。
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (container && container !== this.#observedContainer)` → `this.#resizeObserver?.disconnect()`
- 条件付き依存: `if (container && container !== this.#observedContainer)` → `this.#updateScrollState()`
- 条件付き依存: `if (container && container !== this.#observedContainer)` → `this.#resizeObserver.observe()`
- 条件付き依存: `if (changedProperties.has("prompts") || changedProperties.has("mode"))` → `this.#updateScrollState()`
- 参照: `this.#observedContainer`, `this.#resizeObserver`, `this.#scrollContainer`

## SmartWindowPrompts.#scrollContainer()
- 位置: L69-71
- 役割: shadow DOM 内の .sw-prompts-container を取得する。
- 触るとき: スクロールするコンテナの参照先を変えるとき。
- 呼び出し先: `this.renderRoot.querySelector()`

## SmartWindowPrompts.#updateScrollState()
- 位置: L76-96
- 役割: fullpage で溢れがあるときだけ前後へのスクロール可否を計算し、canScrollStart と canScrollEnd に入れる。
- 触るとき: 矢印が出る条件や、RTL を含む向きの判定を変えるとき。
- 呼び出し先: `Math.abs()`
- 参照: `container.clientWidth`, `container.scrollLeft`, `container.scrollWidth`, `this.#scrollContainer`, `this.canScrollEnd`, `this.canScrollStart`, `this.mode`

## SmartWindowPrompts.#scrollToAdjacentPill()
- 位置: L103-130
- 役割: 先頭に最も近いピルを基準に、一つ前か次のピルへ scrollIntoView する。端では止まる。
- 触るとき: 矢印ボタンを押したときの移動量や RTL の扱いを変えるとき。
- 呼び出し先: `Array.from()`, `Math.max()`, `Math.min()`, `container.getBoundingClientRect()`, `isAtOrPastStart()`, `pill.getBoundingClientRect()`, `pills.findIndex()`, `pills[targetIndex].scrollIntoView()`, `this.matches()`
- 参照: `container.children`, `containerRect.left`, `containerRect.right`, `pills.length`, `this.#scrollContainer`

## isAtOrPastStart()
- 位置: L116-117
- 役割: ピルの矩形が先頭の端に達しているかを判定する。RTL では右端を基準にする。
- 触るとき: 先頭判定の許容誤差や向きの判定を変えるとき。
- 参照: `rect.left`, `rect.right`

## SmartWindowPrompts.#promptSelected()
- 位置: L132-150
- 役割: resume 種別なら memory と content を含め、それ以外は text と type だけで prompt-selected を発火する。
- 触るとき: スターターを選んだときに親へ渡す情報を変えるとき。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `swPrompt.content`, `swPrompt.memory`

## SmartWindowPrompts.#hasInteracted()
- 位置: L152-154
- 役割: マウスやフォーカスが来たピルに has-interacted クラスを付ける。
- 触るとき: 一度触れたピルの見た目の状態を変えるとき。
- 呼び出し先: `e.currentTarget.classList.add()`

## SmartWindowPrompts.#promptDismissed()
- 位置: L156-165
- 役割: 伝播を止め、resume ピルの memory を入れた prompt-dismissed を発火する。
- 触るとき: resume 項目を閉じたときの通知内容を変えるとき。
- 呼び出し先: `e.stopPropagation()`, `this.dispatchEvent()`
- 参照: `swPrompt.memory`

## SmartWindowPrompts.#renderFavicons()
- 位置: L174-207
- 役割: previewIcons を最大3つまで並べ、超える分は最後に +N の表示にまとめる。
- 触るとき: ピルのアイコンの数や +N の表示を変えるとき。
- 呼び出し先: `html()`, `previewIcons.slice()`, `visibleIcons.map()`
- 参照: `e.target.src`, `icon.iconSrc`, `previewIcons.length`, `previewIcons?.length`, `visibleIcons.length`

## SmartWindowPrompts.#renderSkeletonPrompt()
- 位置: L213-219
- 役割: 内容の読み込み中に、操作できない仮のピルを描く。
- 触るとき: 読み込み中の見た目を変えるとき。
- 呼び出し先: `html()`

## SmartWindowPrompts.#renderScrollButtons()
- 位置: L222-253
- 役割: fullpage で、スクロールできる方向にだけ前後の moz-button を描く。
- 触るとき: スクロール用ボタンの出し分けや見た目を変えるとき。
- 呼び出し先: `html()`, `this.#scrollToAdjacentPill()`
- 参照: `this.canScrollEnd`, `this.canScrollStart`, `this.mode`

## SmartWindowPrompts.#renderPrompt()
- 位置: L260-294
- 役割: スターターのボタンを描き、resume かつ fullpage のときだけ閉じるボタンを横に添える。
- 触るとき: 個々のピルの構成や閉じるボタンの有無を変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#promptDismissed()`, `this.#promptSelected()`, `this.#renderFavicons()`
- 参照: `swPrompt.previewIcons`, `swPrompt.text`, `swPrompt.type`, `this.#hasInteracted`, `this.mode`

## SmartWindowPrompts.render()
- 位置: L296-326
- 役割: prompts が空なら何も描かず、無ければスクロール用のコンテナに各ピルを並べる。skeleton 種別は仮表示にする。
- 触るとき: スターター全体の構成やスクロール枠の作りを変えるとき。
- 呼び出し先: `classMap()`, `html()`, `this.#renderPrompt()`, `this.#renderScrollButtons()`, `this.#renderSkeletonPrompt()`, `this.#updateScrollState()`, `this.prompts.map()`
- 条件付き依存: `if (!this.prompts.length)` → `html()`
- 参照: `swPrompt.type`, `this.canScrollEnd`, `this.canScrollStart`, `this.prompts.length`
