# browser/extensions/webcompat/shims/facebook-sdk.js

source: browser/extensions/webcompat/shims/facebook-sdk.js
source-hash: 47a4396d4a56164fafc9ee4d896cd23c64f94b1e
lines: 591

## <module>
- 役割: (未記入)

## getGUID()
- 位置: L55-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(v, c => c.toString(16)).join()`, `c.toString()`, `crypto.getRandomValues()`

## channel.port1.onmessage()
- 位置: L65-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pendingMessages.get()`
- 条件付き依存: `if (resolve)` → `pendingMessages.delete()`
- 条件付き依存: `if (resolve)` → `resolve()`
- 参照: `event.data`

## reconnect()
- 位置: L73-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pendingMessages.values()`, `window.dispatchEvent()`
- 参照: `channel.port2`

## makeLoginPlaceholder()
- 位置: L97-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `parseFloat()`, `target.addEventListener()`, `target.appendChild()`, `target.getAttribute()`, `target.hasAttribute()`, `target.setAttribute()`
- 参照: `button.style`, `button.textContent`, `target.textContent`

## makeVideoPlaceholder()
- 位置: async L175-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowFacebookSDK()`, `document.createElement()`, `p.remove()`, `parseInt()`, `placeholder.addEventListener()`, `placeholdersToRemoveOnUnshim.add()`, `placeholdersToRemoveOnUnshim.forEach()`, `target.appendChild()`, `target.getAttribute()`, `target.hasAttribute()`, `target.setAttribute()`
- 参照: `evt.isTrusted`, `placeholder.style`, `placeholder.textContent`, `target.innerHTML`

## window.open()
- 位置: L265-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `oldWindowOpen.call()`, `url.pathname.endsWith()`
- 参照: `url.hostname`, `url.protocol`, `window.location.href`

## allowFacebookSDK()
- 位置: async L285-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activePopup?.close()`, `alert()`, `console.error()`, `document.createElement()`, `document.head.appendChild()`, `reject()`, `script.addEventListener()`, `script.remove()`, `sendMessageToAddon()`, `window.FB.XFBML.parse()`, `window.FB.api.apply()`, `xfbmlObserver.disconnect()`
- 参照: `document.body`, `script.src`, `window.FB`, `window.fbAsyncInit`

## window.fbAsyncInit()
- 位置: L307-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `eventHandlers.entries()`, `postInitCallback()`, `window.FB.Event.subscribe()`
- 条件付き依存: `if (typeof initInfo !== "undefined")` → `window.FB.init()`
- 条件付き依存: `if (oldInit)` → `oldInit()`

## buildPopupParams()
- 位置: L365-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `ua.includes()`
- 参照: `navigator.userAgent`, `window.screen`

## ensureProxiedToUnshimmed()
- 位置: L387-418
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(typeof value !== "object" || value === null))` → `ensureProxiedToUnshimmed()`

## unshimmedTarget()
- 位置: L388-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `path.reduce()`
- 参照: `window.FB`

## shim[key]()
- 位置: L396-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `unshimmedTarget()`, `value.apply()`
- 条件付き依存: `if (typeof target?.[key] === "function")` → `target[key].apply()`

## get()
- 位置: L410-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `unshimmedTarget()`

## set()
- 位置: L411-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Reflect.set()`, `unshimmedTarget()`

## api()
- 位置: L421-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loggedGraphApiCalls.push()`

## activateApp()
- 位置: L425-425
- 役割: (未記入)
- 触るとき: (未記入)

## clearAppVersion()
- 位置: L426-426
- 役割: (未記入)
- 触るとき: (未記入)

## clearUserID()
- 位置: L427-427
- 役割: (未記入)
- 触るとき: (未記入)

## getAppVersion()
- 位置: L443-443
- 役割: (未記入)
- 触るとき: (未記入)

## getUserID()
- 位置: L444-444
- 役割: (未記入)
- 触るとき: (未記入)

## logEvent()
- 位置: L445-445
- 役割: (未記入)
- 触るとき: (未記入)

## logPageView()
- 位置: L446-446
- 役割: (未記入)
- 触るとき: (未記入)

## logPurchase()
- 位置: L447-447
- 役割: (未記入)
- 触るとき: (未記入)

## setAppVersion()
- 位置: L463-463
- 役割: (未記入)
- 触るとき: (未記入)

## setUserID()
- 位置: L464-464
- 役割: (未記入)
- 触るとき: (未記入)

## updateUserProperties()
- 位置: L465-465
- 役割: (未記入)
- 触るとき: (未記入)

## getHash()
- 位置: L468-468
- 役割: (未記入)
- 触るとき: (未記入)

## getPageInfo()
- 位置: L469-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb?.call()`

## hidePluginElement()
- 位置: L480-480
- 役割: (未記入)
- 触るとき: (未記入)

## showPluginElement()
- 位置: L481-481
- 役割: (未記入)
- 触るとき: (未記入)

## addStaticResource()
- 位置: L486-486
- 役割: (未記入)
- 触るとき: (未記入)

## setCollectionMode()
- 位置: L487-487
- 役割: (未記入)
- 触るとき: (未記入)

## scrollTo()
- 位置: L489-489
- 役割: (未記入)
- 触るとき: (未記入)

## setAutoGrow()
- 位置: L490-490
- 役割: (未記入)
- 触るとき: (未記入)

## setDoneLoading()
- 位置: L491-491
- 役割: (未記入)
- 触るとき: (未記入)

## setHash()
- 位置: L492-492
- 役割: (未記入)
- 触るとき: (未記入)

## setSize()
- 位置: L493-493
- 役割: (未記入)
- 触るとき: (未記入)

## setUrlHandler()
- 位置: L494-494
- 役割: (未記入)
- 触るとき: (未記入)

## startTimer()
- 位置: L495-495
- 役割: (未記入)
- 触るとき: (未記入)

## stopTimer()
- 位置: L496-496
- 役割: (未記入)
- 触るとき: (未記入)

## subscribe()
- 位置: L499-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eventHandlers.get()`, `eventHandlers.get(e).add()`, `eventHandlers.has()`
- 条件付き依存: `if (!eventHandlers.has(e))` → `eventHandlers.set()`

## unsubscribe()
- 位置: L505-507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eventHandlers.get()`, `eventHandlers.get(e)?.delete()`

## init()
- 位置: L510-510
- 役割: (未記入)
- 触るとき: (未記入)

## isAllowed()
- 位置: L511-511
- 役割: (未記入)
- 触るとき: (未記入)

## friendFinder()
- 位置: L514-514
- 役割: (未記入)
- 触るとき: (未記入)

## uploadImageToMediaLibrary()
- 位置: L515-515
- 役割: (未記入)
- 触るとき: (未記入)

## getAccessToken()
- 位置: L517-517
- 役割: (未記入)
- 触るとき: (未記入)

## getAuthResponse()
- 位置: L518-520
- 役割: (未記入)
- 触るとき: (未記入)

## getLoginStatus()
- 位置: L521-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb?.call()`

## getUserID()
- 位置: L524-524
- 役割: (未記入)
- 触るとき: (未記入)

## init()
- 位置: L525-527
- 役割: (未記入)
- 触るとき: (未記入)

## login()
- 位置: L528-559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowFacebookSDK()`, `cb()`, `console.error()`, `window.FB.login()`
- 条件付き依存: `if (needPopup)` → `window.open()`
- 条件付き依存: `if (needPopup)` → `buildPopupParams()`

## runPostLoginCallbacks()
- 位置: L538-548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb?.apply()`, `console.error()`
- 条件付き依存: `if (activeOnloginAttribute)` → `setTimeout()`

## logout()
- 位置: L560-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb?.call()`

## ui()
- 位置: L563-567
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (params.method === "permissions.oauth")` → `window.FB.login()`
- 参照: `params.method`

## parse()
- 位置: L569-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb?.call()`, `console.error()`, `node.querySelectorAll()`, `node.querySelectorAll(".fb-login-button").forEach()`, `node.querySelectorAll(".fb-video").forEach()`
