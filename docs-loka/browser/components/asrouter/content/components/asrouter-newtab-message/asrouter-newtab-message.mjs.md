# browser/components/asrouter/content/components/asrouter-newtab-message/asrouter-newtab-message.mjs

source: browser/components/asrouter/content/components/asrouter-newtab-message/asrouter-newtab-message.mjs
source-hash: a1528ad680b0f8c3e88ad366f9b1d33fc335fb8c
lines: 461

## <module>
- 役割: New Tab ページに表示される ASRouter メッセージ(asrouter-newtab-message 要素)の表示、状態切り替え、ボタン操作を担う Lit の Web Component。
- 呼び出し先: `customElements.define()`

## ASRouterNewTabMessage.connectedCallback()
- 位置: L65-77
- 役割: states があれば visibilitychange の監視を登録し、状態の再評価ポーリングを開始する。
- 触るとき: 状態の再評価が始まらない、またはタブ切り替えで評価が止まると調べるとき。
- 呼び出し先: `super.connectedCallback()`, `this.#startPolling()`, `this.ownerDocument.addEventListener()`
- 参照: `this.#onVisibilityChange`, `this.messageData?.content?.states?.length`

## this.#onVisibilityChange()
- 位置: L71-71
- 役割: タブが表示状態になったとき、状態を再評価するためのハンドラ。
- 触るとき: 表示切り替え時の再評価タイミングを変えるとき。
- 呼び出し先: `this.#evaluateStates()`

## ASRouterNewTabMessage.disconnectedCallback()
- 位置: L79-82
- 役割: 親の切断処理を呼んだ後、ポーリングと visibilitychange の監視を解除する。
- 触るとき: 要素を外した後もタイマーが動き続けるといった問題を調べるとき。
- 呼び出し先: `super.disconnectedCallback()`, `this.#teardownTriggers()`

## ASRouterNewTabMessage.updated()
- 位置: L92-96
- 役割: isIntersecting が真になった時に初めて状態を評価する。
- 触るとき: 表示領域に入ってからの最初の状態判定の順序を変えるとき。
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (changedProperties.has("isIntersecting") && this.isIntersecting)` → `this.#evaluateStates()`
- 参照: `this.isIntersecting`

## ASRouterNewTabMessage.#teardownTriggers()
- 位置: L98-107
- 役割: ポーリングを止め、visibilitychange の監視を外す。
- 触るとき: 最終状態到達後や切断時に監視が残らないことを確かめるとき。
- 呼び出し先: `this.#stopPolling()`
- 条件付き依存: `if (this.#onVisibilityChange)` → `this.ownerDocument.removeEventListener()`
- 参照: `this.#onVisibilityChange`

## ASRouterNewTabMessage.#startPolling()
- 位置: L109-117
- 役割: POLL_INTERVAL_MS ごとに状態を再評価するタイマーを作る。既に動いていれば何もしない。
- 触るとき: ポーリング間隔を変えるとき、または評価頻度が多すぎる・少なすぎると調べるとき。
- 呼び出し先: `globalThis.setInterval()`, `this.#evaluateStates()`
- 参照: `this.#pollTimer`

## ASRouterNewTabMessage.#stopPolling()
- 位置: L119-124
- 役割: ポーリング用のタイマーを解除する。
- 触るとき: ポーリングの停止条件を増やすとき。
- 条件付き依存: `if (this.#pollTimer)` → `globalThis.clearInterval()`
- 参照: `this.#pollTimer`

## ASRouterNewTabMessage.#evaluateStates()
- 位置: L134-154
- 役割: 最終状態に達しておらず表示中で交差している時だけ、全 states の targeting を親に依頼する。
- 触るとき: 状態判定の依頼条件(表示中、可視、最終状態)を変えるとき。
- 呼び出し先: `states.map()`, `this.dispatchEvent()`
- 参照: `state.targeting`, `states?.length`, `this.#reachedFinalState`, `this.isIntersecting`, `this.messageData?.content?.states`, `this.ownerDocument.visibilityState`

## ASRouterNewTabMessage.setMatchedState()
- 位置: L163-179
- 役割: 親から届いた一致番号の content を _matchedContent に入れ、final の状態なら以後の評価とトリガーを止める。
- 触るとき: 状態に応じて表示内容が切り替わらない、または最終状態で止まらない問題を調べるとき。
- 条件付き依存: `if (matched?.final)` → `this.#teardownTriggers()`
- 参照: `matched?.content`, `matched?.final`, `this.#reachedFinalState`, `this._matchedContent`, `this.messageData?.content?.states`

## ASRouterNewTabMessage.#currentContent()
- 位置: L188-193
- 役割: 基本の content に一致した状態の content を重ねた、表示と操作の両方で使う内容を返す。
- 触るとき: 状態ごとに表示やボタンの動作を変える項目を増やすとき。
- 参照: `this._matchedContent`, `this.messageData?.content`

## ASRouterNewTabMessage.specialMessageAction()
- 位置: L210-227
- 役割: 許可された型(WIDGETS_OPT_IN)は dispatch で直接 New Tab の store へ送り、それ以外は親の SpecialMessageActions へイベントで渡す。
- 触るとき: New Tab 内で処理するアクションの型を追加するとき、またはボタンの操作が親に届かないと調べるとき。
- 呼び出し先: `NEWTAB_DISPATCH_ACTION_TYPES.has()`, `this.dispatchEvent()`
- 条件付き依存: `if (NEWTAB_DISPATCH_ACTION_TYPES.has(action?.type) && this.dispatch)` → `this.dispatch()`
- 参照: `action?.type`, `this.dispatch`

## ASRouterNewTabMessage.#handleXButton()
- 位置: L229-232
- 役割: 閉じるボタンで、ブロックを要求してから閉じる処理を行う。
- 触るとき: 閉じるボタンの振る舞い(ブロックするかどうか)を変えるとき。
- 呼び出し先: `this.#handleDismiss()`, `this.handleBlock()`

## ASRouterNewTabMessage.#handleDismiss()
- 位置: L234-236
- 役割: 注入された handleDismiss を呼んでメッセージを閉じる。
- 触るとき: 閉じた後のテレメトリや処理を変えるとき。
- 呼び出し先: `this.handleDismiss()`

## ASRouterNewTabMessage.#handlePrimaryButton()
- 位置: L238-247
- 役割: プライマリボタンのクリックを記録し、アクションを実行し、dismiss 指定があれば閉じる。
- 触るとき: プライマリボタンの押下時の順序(記録、アクション、閉じる)を変えるとき。
- 呼び出し先: `this.#currentContent()`, `this.handleClick()`
- 条件付き依存: `if (primaryButton?.action?.type)` → `this.specialMessageAction()`
- 条件付き依存: `if (primaryButton?.action?.dismiss)` → `this.#handleDismiss()`
- 参照: `primaryButton.action`, `primaryButton?.action?.dismiss`, `primaryButton?.action?.type`

## ASRouterNewTabMessage.#handleSecondaryButton()
- 位置: L249-258
- 役割: セカンダリボタンのクリックを記録し、アクションを実行し、dismiss 指定があれば閉じる。
- 触るとき: セカンダリボタンの押下時の動作を変えるとき。
- 呼び出し先: `this.#currentContent()`, `this.handleClick()`
- 条件付き依存: `if (secondaryButton?.action?.type)` → `this.specialMessageAction()`
- 条件付き依存: `if (secondaryButton?.action?.dismiss)` → `this.#handleDismiss()`
- 参照: `secondaryButton.action`, `secondaryButton?.action?.dismiss`, `secondaryButton?.action?.type`

## ASRouterNewTabMessage.#renderHeading()
- 位置: L260-271
- 役割: 見出しを、文字列ならそのまま、ローカライズ ID ならその data-l10n-id を付けて描画する。
- 触るとき: 見出しの文字列とローカライズの扱いを変えるとき。
- 呼び出し先: `html()`
- 条件付き依存: `if (typeof value === "string")` → `html()`
- 参照: `value.string_id`

## ASRouterNewTabMessage.#renderBody()
- 位置: L273-281
- 役割: 本文を、文字列またはローカライズ ID で段落として描画する。
- 触るとき: 本文の描画形式を変えるとき。
- 呼び出し先: `html()`
- 条件付き依存: `if (typeof value === "string")` → `html()`
- 参照: `value.string_id`

## ASRouterNewTabMessage.#renderSecondaryButton()
- 位置: L283-302
- 役割: セカンダリボタンを、ラベルの種類に応じて描画する。type は content から上書きできる。
- 触るとき: セカンダリボタンのラベルや種類の扱いを変えるとき。
- 呼び出し先: `html()`, `this.#handleSecondaryButton.bind()`
- 参照: `secondaryButton.label`, `secondaryButton.label.string_id`, `secondaryButton.type`

## ASRouterNewTabMessage.#renderPrimaryButtonContent()
- 位置: L304-323
- 役割: プライマリボタンを、ラベルの種類とアイコンに応じて描画する。
- 触るとき: プライマリボタンの見た目やラベルの扱いを変えるとき。
- 呼び出し先: `html()`, `this.#handlePrimaryButton.bind()`
- 条件付き依存: `if (typeof primaryButton.label === "string")` → `html()`
- 条件付き依存: `if (typeof primaryButton.label === "string")` → `this.#handlePrimaryButton.bind()`
- 参照: `primaryButton.iconSrc`, `primaryButton.label`, `primaryButton.label.string_id`, `primaryButton.type`

## ASRouterNewTabMessage.#hasResponsiveImage()
- 位置: L334-341
- 役割: レスポンシブ用の画像指定が一つでもあれば真を返す。
- 触るとき: 全幅バナーの扱いを判定する条件を変えるとき。
- 呼び出し先: `Boolean()`
- 参照: `content?.imageSrcDarkNarrow`, `content?.imageSrcDarkResponsive`, `content?.imageSrcNarrow`, `content?.imageSrcResponsive`

## ASRouterNewTabMessage.#renderImage()
- 位置: L359-404
- 役割: imageSrc があれば、ダーク配色と幅ごとの <source> を並べた picture を描画する。
- 触るとき: 画像の切り替え条件(配色や画面幅の境界 724px、1072px)を変えるとき。
- 呼び出し先: `html()`
- 参照: `content?.imageSrc`

## ASRouterNewTabMessage.#renderPrimaryButton()
- 位置: L406-414
- 役割: プライマリとセカンダリのボタンをボタングループにまとめて描画する。どちらも無ければ何も描かない。
- 触るとき: ボタン領域の並び方を変えるとき。
- 呼び出し先: `html()`, `this.#renderPrimaryButtonContent()`, `this.#renderSecondaryButton()`

## ASRouterNewTabMessage.render()
- 位置: L416-457
- 役割: 現在の内容から、閉じるボタン、画像、見出し、本文、ボタンを組み立てる。
- 触るとき: メッセージ全体のレイアウトや CSS の読み込み先を変えるとき。
- 呼び出し先: `html()`, `this.#currentContent()`, `this.#handleXButton.bind()`, `this.#hasResponsiveImage()`, `this.#renderBody()`, `this.#renderHeading()`, `this.#renderImage()`, `this.#renderPrimaryButton()`
- 参照: `content?.body`, `content?.heading`, `content?.hideDismissButton`, `content?.primaryButton`, `content?.secondaryButton`, `this.cssOverride`
