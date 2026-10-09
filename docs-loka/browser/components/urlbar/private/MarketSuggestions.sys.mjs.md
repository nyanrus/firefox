# browser/components/urlbar/private/MarketSuggestions.sys.mjs

source: browser/components/urlbar/private/MarketSuggestions.sys.mjs
source-hash: a8fff62fb25ad91d229784aeefba6ad2a4b6dba8
lines: 139

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## MarketSuggestions.realtimeType()
- 位置: L19-21
- 役割: (未記入)
- 触るとき: (未記入)

## MarketSuggestions.isSponsored()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)

## MarketSuggestions.merinoProvider()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)

## MarketSuggestions.getViewTemplateForDescriptionTop()
- 位置: L31-47
- 役割: (未記入)
- 触るとき: (未記入)

## MarketSuggestions.getViewTemplateForDescriptionBottom()
- 位置: L49-75
- 役割: (未記入)
- 触るとき: (未記入)

## MarketSuggestions.getViewUpdateForPayloadItem()
- 位置: L77-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseFloat()`
- 条件付き依存: `if (item.image_url)` → `UrlbarUtils.getRemoteImageUrl()`
- 参照: `item.exchange`, `item.image_url`, `item.last_price`, `item.name`, `item.ticker`, `item.todays_change_perc`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`
