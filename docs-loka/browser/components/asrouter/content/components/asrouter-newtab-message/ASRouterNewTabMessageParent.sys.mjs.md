# browser/components/asrouter/content/components/asrouter-newtab-message/ASRouterNewTabMessageParent.sys.mjs

source: browser/components/asrouter/content/components/asrouter-newtab-message/ASRouterNewTabMessageParent.sys.mjs
source-hash: 14c91eac62dd5af51a0b3c919ca69cb007201130
lines: 63

## <module>
- 役割: asrouter-newtab-message 要素の特権側の JSWindowActor 親で、アクション実行と JEXL 状態評価を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ASRouterNewTabMessageParent.receiveMessage()
- 位置: L16-34
- 役割: 特権 about ページの remoteType でなければ null を返す。SpecialMessageAction はアクションを実行し、EvaluateTargeting は評価結果を返す。
- 触るとき: 新しいメッセージ名を追加するとき、または特権以外からの要求を弾く条件を変えるとき。
- 呼び出し先: `lazy.SpecialMessageActions.handleAction()`, `this.#evaluateTargetings()`
- 参照: `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `message.data.action`, `message.data.targetings`, `message.name`, `this.browsingContext.top.embedderElement`, `this.manager.remoteType`

## ASRouterNewTabMessageParent.#evaluateTargetings()
- 位置: L44-61
- 役割: 各 JEXL 式を ASRouter の環境で評価し、成功して真のものだけ true にする。評価に失敗した式は false として扱いエラーを出す。
- 触るとき: Newtab メッセージの状態判定の結果が想定と違う、または評価の失敗を追うとき。
- 呼び出し先: `Promise.all()`, `lazy.ASRouter.evaluateExpression()`, `targetings.map()`
- 条件付き依存: `if (!result.evaluationStatus.success)` → `console.error()`
- 参照: `lazy.ASRouterTargeting.Environment`, `result.evaluationStatus.result`, `result.evaluationStatus.success`
