# browser/extensions/newtab/lib/NewTabGleanUtils.sys.mjs

source: browser/extensions/newtab/lib/NewTabGleanUtils.sys.mjs
source-hash: a1cb6a0d63a63fa30a4db08579abeb3a51535096
lines: 329

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Promise.withResolvers()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## registrationDone()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._registrationDone.promise`

## readJSON()
- 位置: async L63-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`, `result.json()`

## registerMetricsAndPings()
- 位置: async L79-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this._registrationDone.resolve()`, `this.readJSON()`
- 条件付き依存: `if (!data || (!data.metrics && !data.pings))` → `lazy.logConsole.log()`
- 条件付き依存: `if (data.pings)` → `Object.entries()`
- 条件付き依存: `if (data.pings)` → `this.registerPingIfNeeded()`
- 条件付き依存: `if (data.pings)` → `this.convertToCamelCase()`
- 条件付き依存: `if (data.metrics)` → `Object.entries()`
- 条件付き依存: `if (data.metrics)` → `this.registerMetricIfNeeded()`
- 参照: `data.metrics`, `data.pings`

## registerMetricIfNeeded()
- 位置: L139-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EXTRA_ARGS_TYPES_ALLOWLIST.includes()`, `Object.keys()`, `Services.fog.registerRuntimeMetric()`, `gleanSuccessMetric.set()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.dottedSnakeToCamel()`
- 条件付き依存: `if (categoryName in Glean && metricName in Glean[categoryName])` → `lazy.logConsole.warn()`
- 条件付き依存: `if ( EXTRA_ARGS_TYPES_ALLOWLIST.includes(type) && extraArgs && Object.keys(extraArgs).length )` → `JSON.stringify()`
- 参照: `Glean.newtab.metricRegistered`, `Object.keys(extraArgs).length`
- XPCOM: `Services.fog`

## registerPingIfNeeded()
- 位置: L205-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.fog.registerRuntimePing()`, `gleanSuccessPing.set()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.kebabToCamel()`
- 条件付き依存: `if (pingName in GleanPings)` → `lazy.logConsole.warn()`
- 参照: `Glean.newtab.pingRegistered`
- XPCOM: `Services.fog`

## dottedSnakeToCamel()
- 位置: L260-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `metricNameOrCategory.split()`, `segment.split()`
- 条件付き依存: `if (part.length)` → `part.charAt()`
- 条件付き依存: `if (firstChar >= "a" && firstChar <= "z")` → `firstChar.toUpperCase()`
- 条件付き依存: `if (firstChar >= "a" && firstChar <= "z")` → `part.slice()`
- 参照: `part.length`

## kebabToCamel()
- 位置: L295-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pingName.split()`
- 条件付き依存: `if (segment.length)` → `segment.charAt()`
- 条件付き依存: `if (firstChar >= "a" && firstChar <= "z")` → `firstChar.toUpperCase()`
- 条件付き依存: `if (firstChar >= "a" && firstChar <= "z")` → `segment.slice()`
- 参照: `segment.length`

## convertToCamelCase()
- 位置: L321-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `this.dottedSnakeToCamel()`
