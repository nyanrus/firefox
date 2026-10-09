# browser/components/urlbar/content/UrlbarContentUtils.mjs

source: browser/components/urlbar/content/UrlbarContentUtils.mjs
source-hash: 27df028b09dbc0f471569096c41f7538f5ebed65
lines: 259

## <module>
- 役割: (未記入)

## port()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `globalThis.window?.UrlbarActorPort`

## UrlbarContentUtils.getPlatform()
- 位置: L63-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!(!port()))` → `port().getPlatform()`
- 条件付き依存: `if (!(!port()))` → `port()`
- 参照: `ChromeUtils.importESModule( "resource://gre/modules/AppConstants.sys.mjs" ).AppConstants.platform`

## UrlbarContentUtils.isWindowPrivate()
- 位置: L87-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule( "resource://gre/modules/PrivateBrowsingUtils.sys.mjs" ).PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`
- 参照: `port().isWindowPrivate`

## UrlbarContentUtils.getDisplaySpec()
- 位置: L104-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`, `port().getDisplaySpec()`
- 条件付き依存: `if (!port())` → `Services.io.newURI()`
- 参照: `Services.io.newURI(url).displaySpec`
- XPCOM: `Services.io`

## UrlbarContentUtils.unEscapeURIForUI()
- 位置: L123-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`, `port().unEscapeURIForUI()`
- 条件付き依存: `if (!port())` → `Services.textToSubURI.unEscapeURIForUI()`
- XPCOM: `Services.textToSubURI`

## UrlbarContentUtils.getSupportUrl()
- 位置: L137-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`, `port().getSupportUrl()`
- 条件付き依存: `if (!port())` → `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## UrlbarContentUtils.getFixupPrimitives()
- 位置: L155-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`, `port().getFixupPrimitives()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule( "moz-src:///browser/components/urlbar/UrlbarUtils.sys.mjs" ).UrlbarUtils.getFixupPrimitives()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`

## UrlbarContentUtils.isTextDirectionRTL()
- 位置: L174-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`, `port().isTextDirectionRTL()`
- 条件付き依存: `if (!port())` → `win.windowUtils.getDirectionFromText()`
- 参照: `win.windowUtils.DIRECTION_RTL`

## UrlbarContentUtils.whereToOpenLink()
- 位置: L191-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`, `port().whereToOpenLink()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule( "resource://gre/modules/BrowserUtils.sys.mjs" ).BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`

## UrlbarContentUtils.willLoadInBackground()
- 位置: L209-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port()`, `port().willLoadInBackground()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule( "resource://gre/modules/BrowserUtils.sys.mjs" ).BrowserUtils.willLoadInBackground()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`

## UrlbarContentUtils.getContainers()
- 位置: L225-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `ContextualIdentityService.getContainerColorCode()`, `ContextualIdentityService.getContainerIconURL()`, `ContextualIdentityService.getPublicIdentities()`, `ContextualIdentityService.getPublicIdentities().map()`, `ContextualIdentityService.getUserContextLabel()`, `Promise.resolve()`, `port()`
- 条件付き依存: `if (port())` → `port().sendQuery()`
- 条件付き依存: `if (port())` → `port()`
- 参照: `identity.color`, `identity.icon`, `identity.userContextId`

## UrlbarContentUtils.usesMessagePath()
- 位置: L251-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`
- XPCOM: `Services.appinfo`
