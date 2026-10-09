# browser/components/urlbar/private/SportsSuggestions.sys.mjs

source: browser/components/urlbar/private/SportsSuggestions.sys.mjs
source-hash: b52fc22c0a52187bac199d8d262922eef238748b
lines: 344

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SportsSuggestions.realtimeType()
- 位置: L20-22
- 役割: (未記入)
- 触るとき: (未記入)

## SportsSuggestions.isSponsored()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)

## SportsSuggestions.merinoProvider()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)

## SportsSuggestions.getViewTemplateForImageContainer()
- 位置: L32-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["home", "away"].map()`

## SportsSuggestions.getViewTemplateForDescriptionTop()
- 位置: L71-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `stringifiedScore()`, `this.#viewTemplateTopWithScores()`, `this.#viewTemplateTopWithoutScores()`
- 参照: `item.away_team.score`, `item.home_team.score`

## SportsSuggestions.#viewTemplateTopWithScores()
- 位置: L78-103
- 役割: (未記入)
- 触るとき: (未記入)

## SportsSuggestions.#viewTemplateTopWithoutScores()
- 位置: L105-113
- 役割: (未記入)
- 触るとき: (未記入)

## SportsSuggestions.getViewTemplateForDescriptionBottom()
- 位置: L115-139
- 役割: (未記入)
- 触るとき: (未記入)

## SportsSuggestions.getViewUpdateForPayloadItem()
- 位置: L141-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `stringifiedScore()`, `this.#viewUpdateImageAndBottom()`, `this.#viewUpdateTopWithScores()`, `this.#viewUpdateTopWithoutScores()`
- 参照: `item.away_team.score`, `item.home_team.score`, `item.sport_category`, `item.status_type`

## SportsSuggestions.#viewUpdateTopWithScores()
- 位置: L160-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `stringifiedScore()`
- 参照: `item.away_team.name`, `item.away_team.score`, `item.home_team.name`, `item.home_team.score`

## SportsSuggestions.#viewUpdateTopWithoutScores()
- 位置: L177-189
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `item.away_team.name`, `item.home_team.name`

## SportsSuggestions.#viewUpdateImageAndBottom()
- 位置: L191-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(imageUpdatesByTeam).reduce()`, `Object.fromEntries()`, `["home", "away"].reduce()`, `lazy.ObjectUtils.deepEqual()`, `lazy.UrlbarShared.formatDate()`, `new Intl.DateTimeFormat(undefined, { month: "short", day: "numeric", timeZone: zonedNow.timeZoneId, }).formatToParts()`, `partsArray.map()`
- 条件付き依存: `if (item[itemKey]?.icon)` → `UrlbarUtils.getRemoteImageUrl()`
- 参照: `Intl.DateTimeFormat`, `imageUpdatesByTeam.away`, `imageUpdatesByTeam.away[`image-container-${i}`].attributes.hidden`, `imageUpdatesByTeam.home`, `item.away_team?.icon`, `item.date`, `item.home_team?.icon`, `item.sport`, `item.status_type`, `item[itemKey].icon`, `item[itemKey]?.icon`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`, `partsMap.day`, `partsMap.month`, `zonedNow.timeZoneId`

## stringifiedScore()
- 位置: L337-343
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof s == "number")` → `String()`
