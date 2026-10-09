# browser/components/asrouter/modules/MomentsPageHub.sys.mjs

source: browser/components/asrouter/modules/MomentsPageHub.sys.mjs
source-hash: 7c9ce32a05bdb9647ace78b4e2a3a861682c4801
lines: 158

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _MomentsPageHub.constructor()
- 位置: L17-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.checkHomepageOverridePref.bind()`
- 参照: `this._initialized`, `this.checkHomepageOverridePref`, `this.id`, `this.state`

## _MomentsPageHub.init()
- 位置: async L24-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setInterval()`, `this.checkHomepageOverridePref()`, `this.messageRequest()`
- 参照: `this._addImpression`, `this._blockMessageById`, `this._handleMessageRequest`, `this._initialized`, `this._sendTelemetry`, `this.state`

## _MomentsPageHub._sendPing()
- 位置: L53-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendTelemetry()`

## _MomentsPageHub.sendUserEventTelemetry()
- 位置: L60-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendPing()`
- 参照: `message.id`

## _MomentsPageHub.getExpirationDate()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`

## _MomentsPageHub.executeAction()
- 位置: L80-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `this._addImpression()`, `this._blockMessageById()`, `this.sendUserEventTelemetry()`
- 条件付き依存: `if (!expire)` → `this.getExpirationDate()`
- 参照: `message.content.action`, `message.id`
- XPCOM: `Services.prefs`

## _MomentsPageHub.messageRequest()
- 位置: async L110-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.messagingSystem.messageRequestTime.start()`, `Glean.messagingSystem.messageRequestTime.stopAndAccumulate()`, `this._handleMessageRequest()`
- 条件付き依存: `if (!message.recordReach && !message._reachId)` → `nonReachMessages.push()`
- 条件付き依存: `if (message)` → `this.executeAction()`
- 参照: `message._reachId`, `message.recordReach`

## _MomentsPageHub.checkHomepageOverridePref()
- 位置: L139-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.messageRequest()`

## _MomentsPageHub.uninit()
- 位置: L146-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.clearInterval()`
- 参照: `this._initialized`, `this.state`, `this.state._intervalId`
