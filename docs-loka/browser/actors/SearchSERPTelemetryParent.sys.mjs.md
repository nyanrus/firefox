# browser/actors/SearchSERPTelemetryParent.sys.mjs

source: browser/actors/SearchSERPTelemetryParent.sys.mjs
source-hash: 74fc5fd164bc91758abd172d65382adc58516caf
lines: 40

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SearchSERPTelemetryParent.receiveMessage()
- 位置: L13-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchSERPTelemetry.reportPageAction()`, `lazy.SearchSERPTelemetry.reportPageDomains()`, `lazy.SearchSERPTelemetry.reportPageImpression()`, `lazy.SearchSERPTelemetry.reportPageWithAdImpressions()`, `lazy.SearchSERPTelemetry.reportPageWithAds()`
- 参照: `msg.data`, `msg.name`, `this.browsingContext.top.embedderElement`
