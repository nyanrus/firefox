# browser/components/newtab/AboutHomeStartupCache.sys.mjs

source: browser/components/newtab/AboutHomeStartupCache.sys.mjs
source-hash: 51608caa69651a906bc33220747f192633c51eda
lines: 939

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## init()
- 位置: L107-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cache2.diskCacheStorage()`, `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.startup.isInOrBeyondShutdownPhase()`, `console.createInstance()`, `lazy.AsyncShutdown.appShutdownConfirmed.addBlocker()`, `storage.asyncOpenURI()`, `this.cacheNow()`, `this.log.error()`, `this.log.trace()`, `this.makePipe()`, `this.setDeferredResult()`
- 条件付き依存: `if (!this._enabled)` → `this.recordResult()`
- 条件付き依存: `if (!willLoadAboutHome)` → `this.log.trace()`
- 条件付き依存: `if (!willLoadAboutHome)` → `this.recordResult()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(this.PRELOADED_NEWTAB_PREF, false))` → `this.log.trace()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(this.PRELOADED_NEWTAB_PREF, false))` → `this.recordResult()`
- 参照: `Ci.nsIAppStartup.SHUTDOWN_PHASE_APPSHUTDOWNCONFIRMED`, `Ci.nsICacheStorage.OPEN_PRIORITY`, `Services.loadContextInfo.default`, `lazy.DeferredTask`, `lazy.HomePage.overridden`, `this.CACHE_DEBOUNCE_RATE_MS`, `this.CACHE_RESULT_SCALARS.DISABLED`, `this.CACHE_RESULT_SCALARS.NOT_LOADING_ABOUTHOME`, `this.CACHE_RESULT_SCALARS.PRELOADING_DISABLED`, `this.CACHE_RESULT_SCALARS.UNSET`, `this.LOG_LEVEL_PREF`, `this.LOG_NAME`, `this.PRELOADED_NEWTAB_PREF`, `this._cacheDeferred`, `this._cacheEntryPromise`, `this._cacheEntryResolver`, `this._cacheProgress`, `this._cacheTask`, `this._enabled`, `this._initted`, `this._pagePipe`, `this._scriptPipe`, `this._shutdownBlocker`, `this.aboutHomeURI`, `this.log`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsICacheStorage`](../../../netwerk/cache2/nsICacheStorage.idl.md) / `Services.cache2` / `Services.loadContextInfo` / `Services.obs` / `Services.prefs` / `Services.startup`

## this._shutdownBlocker()
- 位置: async L188-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onShutdown()`

## initted()
- 位置: L203-205
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._initted`

## uninit()
- 位置: L207-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.AsyncShutdown.appShutdownConfirmed.removeBlocker()`
- 条件付き依存: `if (this._cacheTask)` → `this._cacheTask.disarm()`
- 条件付き依存: `if (this.log)` → `this.log.trace()`
- 参照: `this._appender`, `this._cacheDeferred`, `this._cacheDeferredResultScalar`, `this._cacheEntry`, `this._cacheEntryPromise`, `this._cacheEntryResolver`, `this._cacheTask`, `this._enabled`, `this._finalized`, `this._firstPrivilegedProcessCreated`, `this._hasWrittenThisSession`, `this._initted`, `this._pagePipe`, `this._procManager`, `this._procManagerID`, `this._scriptPipe`, `this._shutdownBlocker`, `this.log`
- XPCOM: `Services.obs`

## aboutHomeURI()
- 位置: L257-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- 参照: `this.ABOUT_HOME_URI_STRING`, `this._aboutHomeURI`
- XPCOM: `Services.io`

## onShutdown()
- 位置: async L286-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserStartup.abouthomeCacheShutdownwrite.set()`, `this.log.trace()`
- 条件付き依存: `if (!this._hasWrittenThisSession)` → `this.log.trace()`
- 条件付き依存: `if (!this._hasWrittenThisSession)` → `this._cacheTask.arm()`
- 条件付き依存: `if (this._cacheTask.isArmed)` → `this.log.trace()`
- 条件付き依存: `if (this._cacheTask.isArmed)` → `Symbol()`
- 条件付き依存: `if (this._cacheTask.isArmed)` → `lazy.setTimeout()`
- 条件付き依存: `if (this._cacheTask.isArmed)` → `resolve()`
- 条件付き依存: `if (this._cacheTask.isArmed)` → `this._cacheTask.finalize()`
- 条件付き依存: `if (withTimeout)` → `this.log.trace()`
- 条件付き依存: `if (withTimeout)` → `promises.push()`
- 条件付き依存: `if (!(withTimeout))` → `this.log.trace()`
- 条件付き依存: `if (this._cacheTask.isArmed)` → `Promise.race()`
- 条件付き依存: `if (this._cacheTask.isArmed)` → `lazy.clearTimeout()`
- 条件付き依存: `if (result === TIMED_OUT)` → `this.log.error()`
- 参照: `this.SHUTDOWN_CACHE_WRITE_TIMEOUT_MS`, `this._cacheTask.isArmed`, `this._finalized`, `this._hasWrittenThisSession`

## cacheNow()
- 位置: async L341-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.log.error()`, `this.log.trace()`, `this.populateCache()`, `this.requestCache()`
- 条件付き依存: `if (!pageInputStream || !scriptInputStream)` → `this.log.trace()`
- 参照: `this._cacheProgress`, `this._hasWrittenThisSession`

## requestCache()
- 位置: L386-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTab.activityStream.store.getState()`, `this._procManager.sendAsyncMessage()`, `this.log.trace()`
- 条件付き依存: `if (!this._initted)` → `this.log.error()`
- 条件付き依存: `if (!this._procManager)` → `this.log.error()`
- 条件付き依存: `if ( this._procManager.remoteType != lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `this.log.error()`
- 参照: `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `this.CACHE_REQUEST_MESSAGE`, `this._cacheDeferred`, `this._initted`, `this._procManager`, `this._procManager.remoteType`

## makePipe()
- 位置: L419-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/pipe;1"].createInstance()`, `pipe.init()`
- 参照: `Ci.nsIPipe`
- XPCOM: [`nsIPipe`](../../../xpcom/io/nsIPipe.idl.md) / `@mozilla.org/pipe;1`

## pagePipe()
- 位置: L430-432
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._pagePipe`

## scriptPipe()
- 位置: L434-436
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._scriptPipe`

## connectToPipes()
- 位置: L447-531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NetUtil.asyncCopy()`, `this._cacheEntry.getMetaDataElement()`, `this._cacheEntry.openAlternativeInputStream()`, `this._cacheEntry.openInputStream()`, `this.log.error()`, `this.log.info()`, `this.log.trace()`, `this.pagePipe.outputStream.close()`, `this.scriptPipe.outputStream.close()`, `this.setDeferredResult()`
- 条件付き依存: `if (e.result == Cr.NS_ERROR_NOT_AVAILABLE)` → `this.log.debug()`
- 条件付き依存: `if (e.result == Cr.NS_ERROR_NOT_AVAILABLE)` → `this.pagePipe.outputStream.close()`
- 条件付き依存: `if (e.result == Cr.NS_ERROR_NOT_AVAILABLE)` → `this.scriptPipe.outputStream.close()`
- 条件付き依存: `if (e.result == Cr.NS_ERROR_NOT_AVAILABLE)` → `this.setDeferredResult()`
- 条件付き依存: `if (version != Services.appinfo.appBuildID)` → `this.log.info()`
- 条件付き依存: `if (version != Services.appinfo.appBuildID)` → `this.clearCache()`
- 条件付き依存: `if (version != Services.appinfo.appBuildID)` → `this.pagePipe.outputStream.close()`
- 条件付き依存: `if (version != Services.appinfo.appBuildID)` → `this.scriptPipe.outputStream.close()`
- 条件付き依存: `if (version != Services.appinfo.appBuildID)` → `this.setDeferredResult()`
- 条件付き依存: `if (e.result == Cr.NS_ERROR_NOT_AVAILABLE)` → `this.log.error()`
- 参照: `Cr.NS_ERROR_NOT_AVAILABLE`, `Services.appinfo.appBuildID`, `e.result`, `this.CACHE_RESULT_SCALARS.CORRUPT_PAGE`, `this.CACHE_RESULT_SCALARS.CORRUPT_SCRIPT`, `this.CACHE_RESULT_SCALARS.DOES_NOT_EXIST`, `this.CACHE_RESULT_SCALARS.INVALIDATED`, `this.CACHE_RESULT_SCALARS.VALID_AND_USED`, `this.CACHE_VERSION_META_KEY`, `this.pagePipe.outputStream`, `this.scriptPipe.outputStream`
- XPCOM: `Services.appinfo`

## populateCache()
- 位置: async L552-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`, `lazy.NetUtil.asyncCopy()`, `reject()`, `resolve()`, `this._cacheEntry.openAlternativeOutputStream()`, `this._cacheEntry.openOutputStream()`, `this._cacheEntry.setMetaDataElement()`, `this.clearCache()`, `this.ensureCacheEntry()`, `this.log.error()`, `this.log.info()`, `this.log.trace()`
- 条件付き依存: `if (!Components.isSuccessCode(pageResult))` → `this.log.error()`
- 条件付き依存: `if (!Components.isSuccessCode(pageResult))` → `reject()`
- 条件付き依存: `if (!Components.isSuccessCode(scriptResult))` → `this.log.error()`
- 条件付き依存: `if (!Components.isSuccessCode(scriptResult))` → `reject()`
- 参照: `Services.appinfo.appBuildID`
- XPCOM: `Services.appinfo`

## ensureCacheEntry()
- 位置: L638-646
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initted)` → `Promise.reject()`
- 参照: `this._cacheEntryPromise`, `this._initted`

## clearCache()
- 位置: L651-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `this._cacheEntry.recreate()`, `this.log.trace()`
- 参照: `this._cacheEntry`, `this._cacheEntryPromise`, `this._hasWrittenThisSession`

## clearCacheAndUninit()
- 位置: L666-672
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._enabled && this.initted)` → `this.log.trace()`
- 条件付き依存: `if (this._enabled && this.initted)` → `this.clearCache()`
- 条件付き依存: `if (this._enabled && this.initted)` → `this.uninit()`
- 参照: `this._enabled`, `this.initted`

## onContentProcessCreated()
- 位置: L686-719
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._finalized)` → `this.log.trace()`
- 条件付き依存: `if (this._firstPrivilegedProcessCreated)` → `this.log.trace()`
- 条件付き依存: `if (procManager.remoteType == lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE)` → `this.log.trace()`
- 条件付き依存: `if (procManager.remoteType == lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE)` → `this.log.info()`
- 条件付き依存: `if (procManager.remoteType == lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE)` → `processParent.getActor()`
- 条件付き依存: `if (procManager.remoteType == lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (procManager.remoteType == lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE)` → `procManager.addMessageListener()`
- 参照: `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `procManager.remoteType`, `this.CACHE_RESPONSE_MESSAGE`, `this.CACHE_USAGE_RESULT_MESSAGE`, `this.SEND_STREAMS_MESSAGE`, `this._finalized`, `this._firstPrivilegedProcessCreated`, `this._procManager`, `this._procManagerID`, `this.pagePipe.inputStream`, `this.scriptPipe.inputStream`

## onContentProcessShutdown()
- 位置: L730-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.log.info()`
- 条件付き依存: `if (this._procManagerID == childID)` → `this.log.info()`
- 条件付き依存: `if (this._cacheDeferred)` → `this.log.error()`
- 条件付き依存: `if (this._cacheDeferred)` → `this._cacheDeferred()`
- 条件付き依存: `if (this._procManagerID == childID)` → `this._procManager.removeMessageListener()`
- 参照: `this.CACHE_RESPONSE_MESSAGE`, `this.CACHE_USAGE_RESULT_MESSAGE`, `this._cacheDeferred`, `this._procManager`, `this._procManagerID`

## onPreloadedNewTabMessage()
- 位置: L764-778
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cacheTask.arm()`, `this._cacheTask.disarm()`, `this.log.trace()`
- 条件付き依存: `if (this._finalized)` → `this.log.trace()`
- 参照: `this._enabled`, `this._finalized`, `this._initted`

## setDeferredResult()
- 位置: L799-803
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._cacheDeferredResultScalar`

## recordResult()
- 位置: L812-816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserStartup.abouthomeCacheResult.set()`

## onUsageResult()
- 位置: L826-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.log.trace()`
- 条件付き依存: `if ( this._cacheDeferredResultScalar != this.CACHE_RESULT_SCALARS.VALID_AND_USED )` → `this.log.error()`
- 条件付き依存: `if ( this._cacheDeferredResultScalar != this.CACHE_RESULT_SCALARS.VALID_AND_USED )` → `this.recordResult()`
- 条件付き依存: `if (!( this._cacheDeferredResultScalar != this.CACHE_RESULT_SCALARS.VALID_AND_USED ))` → `this.recordResult()`
- 条件付き依存: `if ( this._cacheDeferredResultScalar == this.CACHE_RESULT_SCALARS.VALID_AND_USED )` → `this.recordResult()`
- 条件付き依存: `if (!( this._cacheDeferredResultScalar == this.CACHE_RESULT_SCALARS.VALID_AND_USED ))` → `this.recordResult()`
- 参照: `this.CACHE_RESULT_SCALARS.LATE`, `this.CACHE_RESULT_SCALARS.VALID_AND_USED`, `this._cacheDeferredResultScalar`

## receiveMessage()
- 位置: L867-895
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cacheDeferred()`, `this.log.trace()`, `this.onUsageResult()`
- 条件付き依存: `if ( message.target.remoteType != lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `this.log.error()`
- 条件付き依存: `if (!this._cacheDeferred)` → `this.log.error()`
- 参照: `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `message.data`, `message.data.success`, `message.name`, `message.target.remoteType`, `this.CACHE_RESPONSE_MESSAGE`, `this.CACHE_USAGE_RESULT_MESSAGE`, `this._cacheDeferred`

## observe()
- 位置: L899-923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aSubject .QueryInterface()`, `aSubject .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `aSubject.QueryInterface()`, `this.clearCache()`, `this.onContentProcessCreated()`, `this.onContentProcessShutdown()`
- 参照: `Ci.nsIDOMProcessParent`, `Ci.nsIInterfaceRequestor`, `Ci.nsIMessageSender`
- XPCOM: [`nsIDOMProcessParent`](../../../dom/ipc/nsIDOMProcessParent.idl.md) / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIMessageSender`](../../../dom/base/nsIMessageManager.idl.md)

## onCacheEntryCheck()
- 位置: L927-929
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICacheEntryOpenCallback.ENTRY_WANTED`
- XPCOM: [`nsICacheEntryOpenCallback`](../../../netwerk/cache2/nsICacheEntryOpenCallback.idl.md)

## onCacheEntryAvailable()
- 位置: L931-937
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cacheEntryResolver()`, `this.connectToPipes()`, `this.log.trace()`
- 参照: `this._cacheEntry`
