# browser/components/sessionstore/SessionCookies.sys.mjs

source: browser/components/sessionstore/SessionCookies.sys.mjs
source-hash: c3ad241d57d6e5eba66727243349c9b225bda280
lines: 325

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.declareLazy()`

## collect()
- 位置: L17-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionCookiesInternal.collect()`

## restore()
- 位置: L21-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionCookiesInternal.restore()`

## collect()
- 位置: L38-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CookieStore.toArray()`, `this._ensureInitialized()`

## restore()
- 位置: L46-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.cookies.cookieExists()`, `console.error()`
- 条件付き依存: `if (!exists)` → `Services.cookies.add()`
- 条件付き依存: `if (cv.result !== Ci.nsICookieValidation.eOK)` → `console.error()`
- 条件付き依存: `if (cv.result !== Ci.nsICookieValidation.eOK)` → `JSON.stringify()`
- 条件付き依存: `if (!exists)` → `console.error()`
- 条件付き依存: `if (!exists)` → `JSON.stringify()`
- 参照: `Ci.nsICookie.SAMESITE_NONE`, `Ci.nsICookie.SCHEME_HTTPS`, `Ci.nsICookieValidation.eOK`, `cookie.expiry`, `cookie.host`, `cookie.httponly`, `cookie.isPartitioned`, `cookie.name`, `cookie.originAttributes`, `cookie.originAttributes?.partitionKey?.length`, `cookie.path`, `cookie.sameSite`, `cookie.schemeMap`, `cookie.secure`, `cookie.value`, `cv.result`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md) / [`nsICookieValidation`](../../../netwerk/cookie/nsICookieManager.idl.md) / `Services.cookies`

## observe()
- 位置: L113-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CookieStore.clear()`, `subject.QueryInterface()`, `this._addCookie()`, `this._removeCookie()`, `this._removeCookies()`, `this._updateCookie()`
- 参照: `Ci.nsICookieNotification`, `notification.action`, `notification.batchDeletedCookies`, `notification.cookie`
- XPCOM: [`nsICookieNotification`](../../../netwerk/cookie/nsICookieNotification.idl.md)

## _ensureInitialized()
- 位置: L149-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `this._reloadCookies()`
- 参照: `this._initialized`
- XPCOM: `Services.obs` / `Services.prefs`

## _addCookie()
- 位置: L166-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cookie.QueryInterface()`, `lazy.PrivacyLevel.canSave()`
- 条件付き依存: `if (cookie.isSession && lazy.PrivacyLevel.canSave(cookie.isSecure))` → `CookieStore.add()`
- 参照: `Ci.nsICookie`, `cookie.isSecure`, `cookie.isSession`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md)

## _updateCookie()
- 位置: L178-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cookie.QueryInterface()`, `lazy.PrivacyLevel.canSave()`
- 条件付き依存: `if (cookie.isSession && lazy.PrivacyLevel.canSave(cookie.isSecure))` → `CookieStore.add()`
- 条件付き依存: `if (!(cookie.isSession && lazy.PrivacyLevel.canSave(cookie.isSecure)))` → `CookieStore.delete()`
- 参照: `Ci.nsICookie`, `cookie.isSecure`, `cookie.isSession`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md)

## _removeCookie()
- 位置: L192-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cookie.QueryInterface()`
- 条件付き依存: `if (cookie.isSession)` → `CookieStore.delete()`
- 参照: `Ci.nsICookie`, `cookie.isSession`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md)

## _removeCookies()
- 位置: L203-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cookies.queryElementAt()`, `this._removeCookie()`
- 参照: `Ci.nsICookie`, `cookies.length`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md)

## _reloadCookies()
- 位置: L213-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CookieStore.clear()`, `lazy.PrivacyLevel.canSave()`, `this._addCookie()`
- 参照: `Services.cookies.sessionCookies`
- XPCOM: `Services.cookies`

## add()
- 位置: L242-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._entries.set()`, `this._getKeyForCookie()`
- 参照: `cookie.expiry`, `cookie.host`, `cookie.isHttpOnly`, `cookie.isPartitioned`, `cookie.isSecure`, `cookie.name`, `cookie.originAttributes`, `cookie.path`, `cookie.sameSite`, `cookie.schemeMap`, `cookie.value`, `jscookie.expiry`, `jscookie.httponly`, `jscookie.isPartitioned`, `jscookie.name`, `jscookie.originAttributes`, `jscookie.path`, `jscookie.sameSite`, `jscookie.schemeMap`, `jscookie.secure`

## delete()
- 位置: L289-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._entries.delete()`, `this._getKeyForCookie()`

## clear()
- 位置: L296-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._entries.clear()`

## toArray()
- 位置: L303-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._entries.values()`

## _getKeyForCookie()
- 位置: L316-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.originAttributesToSuffix()`, `JSON.stringify()`
- 参照: `cookie.host`, `cookie.name`, `cookie.originAttributes`, `cookie.path`
