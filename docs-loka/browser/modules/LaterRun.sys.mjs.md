# browser/modules/LaterRun.sys.mjs

source: browser/modules/LaterRun.sys.mjs
source-hash: 1ea3483149b1ba83e0736c2153fc20496564c8cb
lines: 208

## <module>
- 役割: (未記入)
- 呼び出し先: `LaterRun.init()`

## Page.constructor()
- 位置: L20-32
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.minimumHoursSinceInstall`, `this.minimumSessionCount`, `this.pref`, `this.requireBoth`, `this.url`

## Page.hasRun()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.pref`
- XPCOM: `Services.prefs`

## Page.applies()
- 位置: L38-52
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `sessionInfo.hoursSinceInstall`, `sessionInfo.sessionCount`, `this.hasRun`, `this.minimumHoursSinceInstall`, `this.minimumSessionCount`, `this.requireBoth`

## ENABLE_REASON_NEW_PROFILE()
- 位置: L56-58
- 役割: (未記入)
- 触るとき: (未記入)

## ENABLE_REASON_UPDATE_APPLIED()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)

## init()
- 位置: L63-94
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (reason == this.ENABLE_REASON_NEW_PROFILE)` → `Services.prefs.getPrefType()`
- 条件付き依存: `if ( Services.prefs.getPrefType(kProfileCreationTime) == Ci.nsIPrefBranch.PREF_INVALID )` → `Services.prefs.setIntPref()`
- 条件付き依存: `if ( Services.prefs.getPrefType(kProfileCreationTime) == Ci.nsIPrefBranch.PREF_INVALID )` → `Math.floor()`
- 条件付き依存: `if ( Services.prefs.getPrefType(kProfileCreationTime) == Ci.nsIPrefBranch.PREF_INVALID )` → `Date.now()`
- 条件付き依存: `if (reason == this.ENABLE_REASON_UPDATE_APPLIED)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (reason == this.ENABLE_REASON_UPDATE_APPLIED)` → `Math.floor()`
- 条件付き依存: `if (reason == this.ENABLE_REASON_UPDATE_APPLIED)` → `Services.startup.getStartupInfo().start.getTime()`
- 条件付き依存: `if (reason == this.ENABLE_REASON_UPDATE_APPLIED)` → `Services.startup.getStartupInfo()`
- 条件付き依存: `if ( this.hoursSinceInstall > kSelfDestructHoursLimit || this.sessionCount > kSelfDestructSessionLimit )` → `this.selfDestruct()`
- 参照: `Ci.nsIPrefBranch.PREF_INVALID`, `this.ENABLE_REASON_NEW_PROFILE`, `this.ENABLE_REASON_UPDATE_APPLIED`, `this.enabled`, `this.hoursSinceInstall`, `this.sessionCount`
- XPCOM: [`nsIPrefBranch`](../../netwerk/base/nsINetUtil.idl.md) / `Services.prefs` / `Services.startup`

## enabled()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## enable()
- 位置: L102-107
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.enabled)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!this.enabled)` → `this.init()`
- 参照: `this.enabled`
- XPCOM: `Services.prefs`

## hoursSinceInstall()
- 位置: L109-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## hoursSinceUpdate()
- 位置: L117-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## sessionCount()
- 位置: L122-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 参照: `this._sessionCount`
- XPCOM: `Services.prefs`

## sessionCount()
- 位置: L132-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`
- 参照: `this._sessionCount`
- XPCOM: `Services.prefs`

## selfDestruct()
- 位置: L140-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## readPages()
- 位置: L145-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getChildList()`, `pageDataStore.has()`, `pref.substring()`, `pref.substring(kPagePrefRoot.length).split()`
- 条件付き依存: `if (!pageDataStore.has(slug))` → `pageDataStore.set()`
- 条件付き依存: `if (!pageDataStore.has(slug))` → `pref.substring()`
- 条件付き依存: `if (prop == "requireBoth" || prop == "hasRun")` → `pageDataStore.get()`
- 条件付き依存: `if (prop == "requireBoth" || prop == "hasRun")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (prop == "url")` → `pageDataStore.get()`
- 条件付き依存: `if (prop == "url")` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (!(prop == "url"))` → `pageDataStore.get()`
- 条件付き依存: `if (!(prop == "url"))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (pageData.url)` → `Services.urlFormatter.formatURL()`
- 条件付き依存: `if (pageData.url)` → `pageData.url.trim()`
- 条件付き依存: `if (pageData.url)` → `URL.parse()`
- 条件付き依存: `if (!uri)` → `console.error()`
- 条件付き依存: `if (pageData.url)` → `uri.schemeIs()`
- 条件付き依存: `if (!uri.schemeIs("https"))` → `console.error()`
- 条件付き依存: `if (!(!uri.schemeIs("https")))` → `rv.push()`
- 参照: `URL.parse(urlString)?.URI`, `kPagePrefRoot.length`, `pageData.url`, `pref.length`, `prop.length`, `uri.spec`
- XPCOM: `Services.prefs` / `Services.urlFormatter`

## getURL()
- 位置: L193-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `p.applies()`, `pages.find()`, `this.readPages()`
- 条件付き依存: `if (page)` → `Services.prefs.setBoolPref()`
- 参照: `page.pref`, `page.url`, `this.enabled`
- XPCOM: `Services.prefs`
