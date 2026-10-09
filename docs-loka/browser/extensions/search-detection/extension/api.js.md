# browser/extensions/search-detection/extension/api.js

source: browser/extensions/search-detection/extension/api.js
source-hash: ad97dedbde86fbd2f91b31942bafe677ca338ef2
lines: 306

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyGlobalGetters()`

## getAPI()
- 位置: L34-304
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ExtensionCommon.EventManager`, `this.firstMatchedUrls`

## getEngines()
- 位置: async L51-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.isESModuleLoaded()`, `console.error()`, `engine.getSubmission()`, `lazy.SearchService.getEngines()`
- 条件付き依存: `if (submission)` → `results.push()`
- 参照: `ExtensionParent.browserPaintedPromise`, `Services.startup.shuttingDown`, `engine.extensionID`, `engine.partnerCode`, `extension.hasShutdown`, `lazy.AddonSearchEngine`, `lazy.ConfigSearchEngine`, `lazy.SearchService.promiseInitialized`, `submission.uri`, `uri.filePath`, `uri.prePath`, `uri.query`
- XPCOM: `Services.startup`

## getAddonVersion()
- 位置: async L111-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`
- 参照: `addon.version`

## getPublicSuffix()
- 位置: async L119-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `console.error()`
- XPCOM: `Services.eTLD` / `Services.io`

## reportSameSiteRedirect()
- 位置: L128-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.addonsSearchDetection.sameSiteRedirect.record()`

## reportETLDChangeOther()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.addonsSearchDetection.etldChangeOther.record()`

## reportETLDChangeWebrequest()
- 位置: L136-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.addonsSearchDetection.etldChangeWebrequest.record()`

## register()
- 位置: L148-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## onSearchEngineModifiedObserver()
- 位置: L149-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["engine-added", "engine-removed", "engine-changed"].includes()`, `fire.async()`

## register()
- 位置: L193-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionUtils.parseMatchPatterns()`, `WebRequest.onBeforeRedirect.addListener()`, `WebRequest.onBeforeRedirect.removeListener()`, `WebRequest.onBeforeRequest.addListener()`, `WebRequest.onBeforeRequest.removeListener()`
- 参照: `context.xulBrowser.frameLoader.remoteTab`, `extension.id`, `extension.policy`, `filter.urls`

## stopListener()
- 位置: L194-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `channel ?.QueryInterface()`, `channel ?.QueryInterface(Ci.nsIPropertyBag) ?.getProperty()`, `console.error()`, `fire.sync()`
- 参照: `Ci.nsIPropertyBag`, `event.currentTarget`, `event.type`, `this.firstMatchedUrls`, `wrapper.finalURL`
- XPCOM: [`nsIPropertyBag`](../../../../toolkit/components/passwordmgr/nsILoginManager.idl.md)

## listener()
- 位置: L233-253
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.firstMatchedUrls[requestId])` → `ChannelWrapper.getRegisteredChannel()`
- 条件付き依存: `if (!this.firstMatchedUrls[requestId])` → `wrapper.addEventListener()`
- 参照: `context.extension.policy`, `this.firstMatchedUrls`

## ensureRegisterChannel()
- 位置: L255-265
- 役割: (未記入)
- 触るとき: (未記入)
