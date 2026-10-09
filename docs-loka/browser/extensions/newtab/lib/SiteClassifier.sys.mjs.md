# browser/extensions/newtab/lib/SiteClassifier.sys.mjs

source: browser/extensions/newtab/lib/SiteClassifier.sys.mjs
source-hash: 64c7309bf54cad3af196edab50eac25de37037e8
lines: 104

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## _hasParams()
- 位置: L19-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `params.get()`, `val.startsWith()`
- 参照: `param.key`, `param.prefix`, `param.value`

## classifySite()
- 位置: async L62-103
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (parsedURL)` → `parsedURL.hostname.replace()`
- 条件付き依存: `if (parsedURL)` → `RS("sites-classification").get()`
- 条件付き依存: `if (parsedURL)` → `RS()`
- 条件付き依存: `if (parsedURL)` → `siteTypes.sort()`
- 条件付き依存: `if (parsedURL)` → `hostname.split()`
- 条件付き依存: `if (parsedURL)` → `_hasParams()`
- 参照: `criteria.hostname`, `criteria.params`, `criteria.sld`, `criteria.url`, `parsedURL.searchParams`, `type.criteria`, `type.type`, `x.weight`, `y.weight`
