# browser/extensions/newtab/lib/actors/NewTabAttributionParent.sys.mjs

source: browser/extensions/newtab/lib/actors/NewTabAttributionParent.sys.mjs
source-hash: e94e99c1fc09e971dee3f808055bc12bf548b817
lines: 254

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `console.createInstance()`

## isPlainObject()
- 位置: L43-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.prototype.toString.call()`

## AttributionParent.constructor()
- 位置: L65-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.onSync.bind()`
- 参照: `this._onSync`

## AttributionParent.setAllowListForTest()
- 位置: L75-77
- 役割: (未記入)
- 触るとき: (未記入)

## AttributionParent.resetRemoteSettingsClientForTest()
- 位置: L82-84
- 役割: (未記入)
- 触るとき: (未記入)

## AttributionParent.RemoteSettings()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteSettings()`

## AttributionParent.updateAllowList()
- 位置: L99-106
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (records?.length)` → `records.map()`
- 参照: `record.domain`, `records?.length`

## AttributionParent.retrieveAllowList()
- 位置: async L112-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.error()`
- 条件付き依存: `if (!gAllowListClient)` → `this.RemoteSettings()`
- 条件付き依存: `if (!gAllowListClient)` → `gAllowListClient.on()`
- 条件付き依存: `if (!gAllowListClient)` → `gAllowListClient.get()`
- 条件付き依存: `if (!gAllowListClient)` → `this.updateAllowList()`
- 参照: `this._onSync`

## AttributionParent.onSync()
- 位置: L137-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateAllowList()`

## AttributionParent.didDestroy()
- 位置: L141-145
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (gAllowListClient)` → `gAllowListClient.off()`
- 参照: `this._onSync`

## AttributionParent.validateConversion()
- 位置: L161-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CONVERSION_KEYS.has()`, `Object.keys()`, `isPlainObject()`
- 参照: `data.impressionType`, `data.lookbackDays`, `data.partnerId`

## AttributionParent.receiveMessage()
- 位置: async L210-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAllowList.has()`
- 条件付き依存: `if (!principal.isOriginPotentiallyTrustworthy)` → `lazy.logConsole.error()`
- 条件付き依存: `if (!gAllowList.size)` → `this.retrieveAllowList()`
- 条件付き依存: `if (!gAllowList.has(principal.originNoSuffix))` → `lazy.logConsole.error()`
- 条件付き依存: `if (detail)` → `this.validateConversion()`
- 条件付き依存: `if (!validatedConversion)` → `lazy.logConsole.error()`
- 条件付き依存: `if (detail)` → `newTabAttributionService.onAttributionConversion()`
- 参照: `gAllowList.size`, `message.data`, `principal.isOriginPotentiallyTrustworthy`, `principal.originNoSuffix`, `this.manager.documentPrincipal`
