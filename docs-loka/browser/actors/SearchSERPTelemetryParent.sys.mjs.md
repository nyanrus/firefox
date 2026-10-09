# browser/actors/SearchSERPTelemetryParent.sys.mjs

source: browser/actors/SearchSERPTelemetryParent.sys.mjs
source-hash: 74fc5fd164bc91758abd172d65382adc58516caf
lines: 40

## <module>
- 役割: 検索結果ページ(SERP)のテレメトリ情報を子から受け、SearchSERPTelemetry に振り分ける親側アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SearchSERPTelemetryParent.receiveMessage()
- 位置: L13-38
- 役割: メッセージ名ごとに、広告・インプレッション・操作・ドメインの各報告関数へデータを渡す。
- 触るとき: 新しい SERP テレメトリの種類を追加するとき。
- 呼び出し先: `lazy.SearchSERPTelemetry.reportPageAction()`, `lazy.SearchSERPTelemetry.reportPageDomains()`, `lazy.SearchSERPTelemetry.reportPageImpression()`, `lazy.SearchSERPTelemetry.reportPageWithAdImpressions()`, `lazy.SearchSERPTelemetry.reportPageWithAds()`
- 参照: `msg.data`, `msg.name`, `this.browsingContext.top.embedderElement`
