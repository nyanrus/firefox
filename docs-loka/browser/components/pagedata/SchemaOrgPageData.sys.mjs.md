# browser/components/pagedata/SchemaOrgPageData.sys.mjs

source: browser/components/pagedata/SchemaOrgPageData.sys.mjs
source-hash: ec300ecd1fc16e83085b7295cd6e67f6b8f17a19
lines: 438

## <module>
- 役割: (未記入)

## Item.constructor()
- 位置: L29-31
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.type`

## Item.has()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.properties.has()`

## Item.all()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.properties.get()`

## Item.get()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.properties.get()`

## Item.set()
- 位置: L75-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `props.push()`, `this.properties.get()`
- 条件付き依存: `if (props === undefined)` → `this.properties.set()`

## Item.toJsonLD()
- 位置: L92-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Object.fromEntries()`, `value.map()`
- 条件付き依存: `if (value.length == 1)` → `toLD()`
- 参照: `this.properties`, `this.type`, `value.length`

## toLD()
- 位置: L100-105
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (val instanceof Item)` → `val.toJsonLD()`

## parseMicrodataProp()
- 位置: L131-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseUrl()`, `propElement.getAttribute()`, `propElement.hasAtribute()`, `propElement.hasAttribute()`
- 条件付き依存: `if (propElement.hasAtribute("datetime"))` → `propElement.getAttribute()`
- 条件付き依存: `if (propElement.hasAttribute("content"))` → `propElement.getAttribute()`
- 参照: `propElement.localName`, `propElement.textContent`

## parseUrl()
- 位置: L138-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `url.toString()`, `urlElement.getAttribute()`, `urlElement.hasAttribute()`
- 参照: `urlElement.ownerDocument.documentURI`

## collectProduct()
- 位置: L203-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNaN()`, `item.all()`, `item.get()`, `item.has()`, `offer.get()`, `parseFloat()`
- 条件付き依存: `if (item.has("image"))` → `item.get()`
- 条件付き依存: `if (item.has("image"))` → `url.toString()`
- 条件付き依存: `if (item.has("description"))` → `item.get()`
- 条件付き依存: `if (!isNaN(price))` → `offer.get()`
- 参照: `PageDataSchema.DATA_TYPE.PRODUCT`, `document.documentURI`, `offer.type`, `pageData.data`, `pageData.data[PageDataSchema.DATA_TYPE.PRODUCT].price`, `pageData.description`, `pageData.image`

## collectMicrodataItems()
- 位置: L241-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelectorAll()`, `element.getAttribute()`, `item.set()`, `itemFor()`, `itemType.startsWith()`, `items.get()`, `items.set()`, `items.values()`, `parseMicrodataProp()`
- 条件付き依存: `if (itemType.startsWith("https://"))` → `itemType.substring()`
- 条件付き依存: `if (!(itemType.startsWith("https://")))` → `itemType.substring()`
- 条件付き依存: `if (propValue instanceof Item)` → `roots.delete()`
- 参照: `element.parentElement`

## itemFor()
- 位置: L262-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `itemFor()`, `items.get()`, `items.set()`
- 参照: `element.parentElement`

## collectJsonLDItems()
- 位置: L321-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `document.querySelectorAll()`, `fromLD()`
- 条件付き依存: `if (item instanceof Item)` → `items.push()`
- 参照: `script.textContent`

## fromLD()
- 位置: L336-357
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof val == "object" && "@type" in val)` → `Object.entries()`
- 条件付き依存: `if (typeof val == "object" && "@type" in val)` → `prop.startsWith()`
- 条件付き依存: `if (typeof val == "object" && "@type" in val)` → `Array.isArray()`
- 条件付き依存: `if (typeof val == "object" && "@type" in val)` → `item.properties.set()`
- 条件付き依存: `if (typeof val == "object" && "@type" in val)` → `value.map()`

## collectItems()
- 位置: L406-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `collectJsonLDItems()`, `collectMicrodataItems()`, `collectMicrodataItems(document).concat()`

## collect()
- 位置: L417-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.get()`, `this.collectItems()`
- 条件付き依存: `if (!(PageDataSchema.DATA_TYPE.PRODUCT in pageData.data))` → `collectProduct()`
- 参照: `PageDataSchema.DATA_TYPE.PRODUCT`, `item.type`, `pageData.data`, `pageData.siteName`
