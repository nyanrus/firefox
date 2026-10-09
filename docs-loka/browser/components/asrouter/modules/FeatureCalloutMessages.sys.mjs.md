# browser/components/asrouter/modules/FeatureCalloutMessages.sys.mjs

source: browser/components/asrouter/modules/FeatureCalloutMessages.sys.mjs
source-hash: 8ef2025712210bd8e16f92052b3cbec2a7526fc9
lines: 1323

## <module>
- 役割: (未記入)

## matchIncompleteTargeting()
- 位置: L15-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`

## matchCurrentScreenTargeting()
- 位置: L29-37
- 役割: (未記入)
- 触るとき: (未記入)

## add24HourImpressionJEXLTargeting()
- 位置: L49-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `message.id.startsWith()`, `messageIds.includes()`, `uneditedMessages .filter()`, `uneditedMessages .filter(message => message.id.startsWith(prefix)) .map()`, `uneditedMessages.map()`
- 参照: `message.id`, `message.targeting`

## MESSAGES()
- 位置: L84-1316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `add24HourImpressionJEXLTargeting()`, `matchCurrentScreenTargeting()`, `matchIncompleteTargeting()`

## getMessages()
- 位置: L1319-1321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MESSAGES()`
