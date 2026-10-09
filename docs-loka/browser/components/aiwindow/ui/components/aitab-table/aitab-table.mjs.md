# browser/components/aiwindow/ui/components/aitab-table/aitab-table.mjs

source: browser/components/aiwindow/ui/components/aitab-table/aitab-table.mjs
source-hash: a46dd4a56ec82d00235be67ea1a37cf6190b6966
lines: 271

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## formatter()
- 位置: L38-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatters.get()`
- 条件付き依存: `if (!instance)` → `create()`
- 条件付き依存: `if (!instance)` → `formatters.set()`

## numberFormatter()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatter()`
- 参照: `Intl.NumberFormat`

## ratingFormatter()
- 位置: L51-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatter()`
- 参照: `Intl.NumberFormat`

## currencyFormatter()
- 位置: L58-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatter()`
- 参照: `Intl.NumberFormat`

## dateFormatter()
- 位置: L70-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatter()`
- 参照: `Intl.DateTimeFormat`

## formatValue()
- 位置: L86-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DATE_ONLY.test()`, `ISO_DATE_TIME.test()`, `JSON.stringify()`, `Number.isFinite()`, `Number.isNaN()`, `currencyFormatter()`, `currencyFormatter(field.currency ?? "USD").format()`, `date.valueOf()`, `dateFormatter()`, `dateFormatter(timeZone).format()`, `html()`, `numberFormatter()`, `numberFormatter().format()`, `ratingFormatter()`, `ratingFormatter().format()`
- 参照: `field.currency`, `field.key`, `field.max`, `field.prefix`, `field.suffix`, `field.type`

## AITabTable.constructor()
- 位置: L162-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.columns`, `this.description`, `this.heading`, `this.rows`

## AITabTable.#columnsByRole()
- 位置: L176-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.columns.filter()`, `this.columns.find()`
- 参照: `field.role`

## AITabTable.#label()
- 位置: L187-189
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `field.key`, `field.label`

## AITabTable.#renderSourceChip()
- 位置: L191-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `httpUrl()`
- 参照: `row?.href`, `url.hostname`, `url.href`

## AITabTable.#renderRow()
- 位置: L207-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `details.map()`, `formatValue()`, `html()`, `subtitleValues.map()`, `subtitles .map()`, `subtitles .map(field => formatValue(field, row)) .filter()`, `this.#renderSourceChip()`

## AITabTable.render()
- 位置: L225-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `details.map()`, `html()`, `this.#label()`, `this.#renderRow()`, `this.rows.map()`
- 参照: `details.length`, `this.#columnsByRole`, `this.description`, `this.heading`
