# browser/components/aiwindow/ui/components/ai-action-result/ai-action-result.mjs

source: browser/components/aiwindow/ui/components/ai-action-result/ai-action-result.mjs
source-hash: 2b08f2076c3d8b9ad43cc8e3f0505487e9905544
lines: 394

## <module>
- 役割: アシスタントの自然言語アクション結果（「タブを閉じました」等）を表示する ai-action-result 要素を定義する。
- 呼び出し先: `customElements.define()`

## AIActionResult.constructor()
- 位置: L65-78
- 役割: 全プロパティを既定値（空文字・null・false・空配列）で初期化する。
- 触るとき: 新しい既定値のプロパティを足すとき、または親が属性を渡さなかった時の表示を確認するとき。
- 呼び出し先: `super()`
- 参照: `this.canUndo`, `this.isExpanded`, `this.isLoading`, `this.label`, `this.labelL10nArgs`, `this.labelL10nId`, `this.labelLink`, `this.rows`, `this.summary`, `this.summaryL10nArgs`, `this.summaryL10nId`

## AIActionResult.willUpdate()
- 位置: L91-129
- 役割: 読み込み中はラベルをスナップショットし、読み込み完了時にシマーの最終スイープを予約する。
- 触るとき: 読み込み完了後に完了ラベルへ切り替わるタイミングがずれる、または shimmering 属性が消えないときに見る。
- 呼び出し先: `this.toggleAttribute()`
- 条件付き依存: `if (this.isLoading)` → `this.#cancelSweepAnim()`
- 条件付き依存: `if (this.isLoading)` → `this.removeAttribute()`
- 条件付き依存: `if (this.isLoading)` → `this.#clearSweepTimer()`
- 条件付き依存: `if (!(this.isLoading))` → `changed.has()`
- 条件付き依存: `if (!(this.isLoading))` → `changed.get()`
- 条件付き依存: `if ( changed.has("isLoading") && changed.get("isLoading") && this.#loadingLabelSnapshot )` → `this.#clearSweepTimer()`
- 条件付き依存: `if ( changed.has("isLoading") && changed.get("isLoading") && this.#loadingLabelSnapshot )` → `setTimeout()`
- 条件付き依存: `if ( changed.has("isLoading") && changed.get("isLoading") && this.#loadingLabelSnapshot )` → `this.#finishSweep()`
- 条件付き依存: `if (!shimmering)` → `this.removeAttribute()`
- 条件付き依存: `if (!shimmering)` → `this.#cancelSweepAnim()`
- 参照: `AIActionResult.SWEEP_MAX_MS`, `this.#awaitingSweep`, `this.#loadingLabelSnapshot`, `this.#sweepTimer`, `this.isLoading`, `this.label`, `this.labelL10nArgs`, `this.labelL10nId`, `this.labelLink`

## AIActionResult.updated()
- 位置: L131-135
- 役割: スイープ待ちかつアニメーション未生成なら、最終スイープ開始の #finishCurrentSweep を呼ぶ。
- 触るとき: 読み込み完了時に最後のシマーが途中で切れる、または再描画後に終了処理が走らないときに見る。
- 条件付き依存: `if (this.#awaitingSweep && !this.#sweepAnim)` → `this.#finishCurrentSweep()`
- 参照: `this.#awaitingSweep`, `this.#sweepAnim`

## AIActionResult.#finishCurrentSweep()
- 位置: L142-183
- 役割: 現在のシマー位置から右端までの最終アニメーションを作り、終了時に #finishSweep を呼ぶ。
- 触るとき: シマーの終わり方や速度を変えるとき、または CSS の actionLogShimmer の周期を変えたときに見る。
- 呼び出し先: `Math.floor()`, `Math.max()`, `Math.min()`, `Math.pow()`, `Number()`, `label ?.getAnimations()`, `label ?.getAnimations?.() .find()`, `label.animate()`, `this.#finishSweep()`, `this.#sweepAnim.finished .then()`, `this.#sweepAnim.finished .then(() => this.#finishSweep()) .catch()`, `this.renderRoot?.querySelector()`, `this.setAttribute()`
- 条件付き依存: `if (!label || !loop)` → `this.#finishSweep()`
- 参照: `AIActionResult.SHIMMER_CYCLE_MS`, `a.animationName`, `loop.currentTime`, `this.#sweepAnim`

## AIActionResult.connectedCallback()
- 位置: L185-192
- 役割: 描画ルートにクリックのキャプチャリスナーを付け、ラベルリンクのクリックがトグルに届かないようにする。
- 触るとき: ラベルのリンクを押したときに展開や折りたたみが誤って動く、または逆に動かなくなったときに見る。
- 呼び出し先: `super.connectedCallback()`, `this.renderRoot.addEventListener()`
- 参照: `this.#handleLabelLinkClick`

## AIActionResult.disconnectedCallback()
- 位置: L194-203
- 役割: 切り離し時にタイマーとアニメーションを止め、描画ルートのクリックリスナーを外す。
- 触るとき: 要素が DOM から外れた後にタイマーが残って例外や再描画が起きるときに見る。
- 呼び出し先: `super.disconnectedCallback()`, `this.#cancelSweepAnim()`, `this.#clearSweepTimer()`, `this.renderRoot.removeEventListener()`
- 参照: `this.#handleLabelLinkClick`

## AIActionResult.#clearSweepTimer()
- 位置: L205-210
- 役割: フォールバック用のスイープタイマーがあれば clearTimeout して null に戻す。
- 触るとき: 読み込み完了時の待ち時間を変えるとき、またはタイマーが二重に動く疑いがあるときに見る。
- 条件付き依存: `if (this.#sweepTimer)` → `clearTimeout()`
- 参照: `this.#sweepTimer`

## AIActionResult.#cancelSweepAnim()
- 位置: L212-217
- 役割: 進行中のシマー用アニメーションがあれば cancel して破棄する。
- 触るとき: 読み込み再開時や切り離し時にシマーが残る不具合を調べるときに見る。
- 条件付き依存: `if (this.#sweepAnim)` → `this.#sweepAnim.cancel()`
- 参照: `this.#sweepAnim`

## AIActionResult.#finishSweep()
- 位置: L219-228
- 役割: スイープ待ち中なら待ちを解除してタイマーを消し、再描画を要求して完了ラベルを出す。
- 触るとき: 読み込み完了後に完了テキストへ切り替わらないときや、早すぎる切り替えを直すときに見る。
- 条件付き依存: `if (this.#awaitingSweep)` → `this.#clearSweepTimer()`
- 条件付き依存: `if (this.#awaitingSweep)` → `this.requestUpdate()`
- 参照: `this.#awaitingSweep`

## AIActionResult.#handleUndo()
- 位置: L230-234
- 役割: action-result-undo イベントを発火する。実際の取り消し処理は親が行う。
- 触るとき: 取り消しボタンの動作を変えるとき、または親が undo を受け取れない時に見る。
- 呼び出し先: `this.dispatchEvent()`

## AIActionResult.#handleLabelLinkClick()
- 位置: L236-247
- 役割: クリックされた要素がラベルリンクなら伝播を止め、ヘッダーのトグルを発火させない。
- 触るとき: ラベル内リンクのクリックで展開状態が変わってしまうときに見る。
- 呼び出し先: `el.classList.contains()`, `event .composedPath()`, `event .composedPath() .some()`
- 条件付き依存: `if (onLabelLink)` → `event.stopPropagation()`

## AIActionResult.#handleToggle()
- 位置: L249-258
- 役割: isExpanded を反転させ、action-result-toggle イベントに新しい状態を載せて発火する。
- 触るとき: 展開・折りたたみの通知を親が受け取る仕組みを変えるとき、または展開状態の同期がずれたときに見る。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.isExpanded`

## AIActionResult.#renderLabelContent()
- 位置: L263-277
- 役割: リンク指定があれば空のリンク要素を、l10n ID があれば空文字を、なければ生のラベルを返す。
- 触るとき: ラベルにリンクを埋め込む表示を変えるとき、またはラベルが翻訳されず表示されないときに見る。
- 条件付き依存: `if (link)` → `html()`
- 参照: `link.href`, `link.l10nName`

## AIActionResult.render()
- 位置: L279-324
- 役割: ヘッダーのボタン、ラベル（シマー中はスナップショット）、詳細部分を組み立てて描画する。
- 触るとき: ヘッダーの見た目や aria-expanded、ラベルの l10n 属性を変えるとき、または読み込み中に別のラベルが出るときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`, `keyed()`, `this.#renderDetails()`, `this.#renderLabelContent()`
- 参照: `label.label`, `label.labelL10nArgs`, `label.labelL10nId`, `label.labelLink`, `this.#awaitingSweep`, `this.#handleToggle`, `this.#loadingLabelSnapshot`, `this.isExpanded`, `this.isLoading`, `this.label`, `this.labelL10nArgs`, `this.labelL10nId`, `this.labelLink`

## AIActionResult.#renderDetails()
- 位置: L326-390
- 役割: 展開時の各行とチップ、要約文、取り消しボタンを描画する。
- 触るとき: 展開時の行表示や要約・取り消しボタンの出し分けを変えるとき、または行の items が表示されないときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`, `keyed()`, `this.#renderLabelContent()`, `this.rows.map()`
- 参照: `row.items`, `row.items?.length`, `row.label`, `row.labelL10nArgs`, `row.labelL10nId`, `row.link`, `this.#handleUndo`, `this.canUndo`, `this.isExpanded`, `this.summary`, `this.summaryL10nArgs`, `this.summaryL10nId`
