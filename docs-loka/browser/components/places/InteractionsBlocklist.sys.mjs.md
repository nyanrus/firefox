# browser/components/places/InteractionsBlocklist.sys.mjs

source: browser/components/places/InteractionsBlocklist.sys.mjs
source-hash: 172141f195a23558a7ac66dafae7216efe2d2b66
lines: 278

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## get()
- 位置: L75-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 参照: `regexes.length`

## _InteractionsBlocklist.constructor()
- 位置: L101-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Services.prefs.getStringPref()`, `customBlocklist.map()`, `lazy.logConsole.warn()`
- XPCOM: `Services.prefs`

## _InteractionsBlocklist.urlRequirements()
- 位置: L129-135
- 役割: (未記入)
- 触るとき: (未記入)

## _InteractionsBlocklist.canRecordUrl()
- 位置: L144-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InteractionsBlocklist.urlRequirements.get()`, `pathname.endsWith()`
- 参照: `Ci.nsIURI`, `requirements.extension`, `url.filePath`, `url.pathname`, `url.protocol`, `url.scheme`
- XPCOM: [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md)

## _InteractionsBlocklist.isUrlBlocklisted()
- 位置: L172-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `baseHost.toLocaleLowerCase()`, `hostWithSubdomains.lastIndexOf()`, `hostWithSubdomains.substring()`, `lazy.FilterAdult.isAdultUrl()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `lazy.UrlbarUtils.stripPublicSuffixFromHost()`, `r.test()`, `regexes.push()`, `regexes.some()`, `this.canRecordUrl()`
- 条件付き依存: `if (!url)` → `lazy.logConsole.warn()`
- 参照: `url.host`, `url.href`, `url.protocol`

## _InteractionsBlocklist.addRegexToBlocklist()
- 位置: L228-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HOST_BLOCKLIST["*"].map()`, `HOST_BLOCKLIST["*"].push()`, `JSON.stringify()`, `Services.prefs.setStringPref()`, `lazy.logConsole.warn()`, `reg.toString()`
- XPCOM: `Services.prefs`

## _InteractionsBlocklist.removeRegexFromBlocklist()
- 位置: L255-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `HOST_BLOCKLIST["*"].filter()`, `HOST_BLOCKLIST["*"].map()`, `JSON.stringify()`, `Services.prefs.setStringPref()`, `lazy.logConsole.warn()`, `reg.toString()`
- 参照: `curr.source`, `regex.source`
- XPCOM: `Services.prefs`
