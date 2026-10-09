# browser/components/asrouter/content/components/asrouter-newtab-message/ASRouterNewTabMessageChild.sys.mjs

source: browser/components/asrouter/content/components/asrouter-newtab-message/ASRouterNewTabMessageChild.sys.mjs
source-hash: a9d264edf76d3726a890fe8288da3fe77f4604ee
lines: 51

## <module>
- 役割: asrouter-newtab-message 要素のページ側(コンテンツ)で、イベントを親へ中継し、状態の判定結果を要素へ戻す JSWindowActor の子側。

## ASRouterNewTabMessageChild.handleEvent()
- 位置: L6-17
- 役割: SpecialMessageAction は親へそのまま送り、EvaluateTargeting は targeting 評価の要求キューに入れる。
- 触るとき: 新しいカスタムイベントをページから親へ渡すとき。
- 呼び出し先: `this.#enqueueTargetingEvaluation()`, `this.sendAsyncMessage()`
- 参照: `event.detail`, `event.target`, `event.type`

## ASRouterNewTabMessageChild.#enqueueTargetingEvaluation()
- 位置: async L29-49
- 役割: targetings を親に問い合わせ、要素が接続中なら最初に一致した状態の番号を setMatchedState で要素へ設定する。問い合わせが途中で切れた場合は何もしない。
- 触るとき: ポーリングで状態が切り替わらない、または切断時の例外が出るとき。
- 呼び出し先: `Array.from()`, `Cu.waiveXrays()`, `Cu.waiveXrays(el).setMatchedState()`, `results.findIndex()`, `this.sendQuery()`
- 参照: `Cu.waiveXrays(detail).targetings`, `el.isConnected`
