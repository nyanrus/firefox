# browser/actors/LinkHandlerChild.sys.mjs

source: browser/actors/LinkHandlerChild.sys.mjs
source-hash: 387edd75a3accd9270ec02caa87c19f909b2096c
lines: 169

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## LinkHandlerChild.constructor()
- 位置: L12-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._iconLoader`, `this.seenTabIcon`

## LinkHandlerChild.iconLoader()
- 位置: L19-24
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.FaviconLoader`, `this._iconLoader`

## LinkHandlerChild.addRootIcon()
- 位置: L26-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !this.seenTabIcon && Services.prefs.getBoolPref("browser.chrome.guess_favicon", true) && Services.prefs.getBoolPref("browser.chrome.site_icons", true) )` → `["http", "https"].includes()`
- 条件付き依存: `if (["http", "https"].includes(pageURI.scheme))` → `this.iconLoader.addDefaultIcon()`
- 参照: `pageURI.scheme`, `this.document.documentURIObject`, `this.seenTabIcon`
- XPCOM: `Services.prefs`

## LinkHandlerChild.onHeadParsed()
- 位置: L42-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addRootIcon()`
- 条件付き依存: `if (this._iconLoader)` → `this._iconLoader.onPageShow()`
- 参照: `event.target.ownerDocument`, `this._iconLoader`, `this.document`

## LinkHandlerChild.onPageShow()
- 位置: L58-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addRootIcon()`
- 条件付き依存: `if (this._iconLoader)` → `this._iconLoader.onPageShow()`
- 参照: `event.target`, `this._iconLoader`, `this.document`

## LinkHandlerChild.onPageHide()
- 位置: L70-80
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._iconLoader)` → `this._iconLoader.onPageHide()`
- 参照: `event.target`, `this._iconLoader`, `this.document`, `this.seenTabIcon`

## LinkHandlerChild.onLinkEvent()
- 位置: L82-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `link.getAttribute()`, `link.hasAttribute()`, `link.rel.toLowerCase()`, `rel.includes()`, `rel.split()`, `this.iconLoader.addIconFromLink()`
- 条件付き依存: `if (!searchAdded && event.type == "DOMLinkAdded")` → `link.type.toLowerCase()`
- 条件付き依存: `if (!searchAdded && event.type == "DOMLinkAdded")` → `type.replace()`
- 条件付き依存: `if (!searchAdded && event.type == "DOMLinkAdded")` → `re.test()`
- 条件付き依存: `if ( type == "application/opensearchdescription+xml" && link.title && re.test(link.href) )` → `this.sendAsyncMessage()`
- 参照: `event.target`, `event.type`, `link.documentGlobal`, `link.href`, `link.rel`, `link.title`, `link.type`, `this.contentWindow`, `this.seenTabIcon`
- XPCOM: `Services.prefs`

## LinkHandlerChild.handleEvent()
- 位置: L156-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onHeadParsed()`, `this.onLinkEvent()`, `this.onPageHide()`, `this.onPageShow()`
- 参照: `event.type`
