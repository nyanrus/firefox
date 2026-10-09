# browser/extensions/webcompat/experiment-apis/trackingProtection.js

source: browser/extensions/webcompat/experiment-apis/trackingProtection.js
source-hash: 918c63ce8d5cdd016d537897b96365775f74b670
lines: 357

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyGlobalGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## AllowList.constructor()
- 位置: L13-15
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._id`

## AllowList.setShims()
- 位置: L17-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(matchEntries || []).map()`, `matchEntries?.flatMap()`
- 参照: `e.patterns`, `entry.patterns`, `entry.types`, `this._shimEntries`, `this._shimMatcher`, `this._shimNotHosts`

## AllowList.setAllows()
- 位置: L29-34
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._allowHosts`, `this._allowMatcher`, `this._allowPatterns`

## AllowList.shims()
- 位置: L38-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entry.matcher.matches()`, `entry.types.includes()`, `this._shimEntries.some()`, `this._shimMatcher?.matches()`, `this._shimNotHosts?.includes()`

## AllowList.allows()
- 位置: L50-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._allowHosts?.includes()`, `this._allowMatcher?.matches()`

## Manager.constructor()
- 位置: L58-61
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._PBModeAllowLists`, `this._allowLists`

## Manager._getAllowList()
- 位置: L63-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activeAllowLists.get()`, `activeAllowLists.has()`
- 条件付き依存: `if (!activeAllowLists.has(id))` → `activeAllowLists.set()`
- 参照: `this._PBModeAllowLists`, `this._allowLists`

## Manager._ensureStarted()
- 位置: L74-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/url-classifier/channel-classifier-service;1" ].getService()`, `Services.obs.addObserver()`, `this._channelClassifier.addListener()`
- 参照: `Ci.nsIChannelClassifierService`, `this._PBModeUnblockedChannelIds`, `this._channelClassifier`, `this._classifierObserver`, `this._classifierObserver.observe`, `this._unblockedChannelIds`
- XPCOM: [`nsIChannelClassifierService`](../../../../netwerk/url-classifier/nsIChannelClassifierService.idl.md) / `@mozilla.org/url-classifier/channel-classifier-service;1` → `nsIChannelClassifierService` (netwerk/url-classifier/components.conf) / `Services.obs`

## this._classifierObserver.observe()
- 位置: L85-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChannelWrapper.get()`, `activeAllowLists.values()`, `allowList.shims()`, `subject.QueryInterface()`
- 条件付き依存: `if (isPrivateMode)` → `this._PBModeUnblockedChannelIds.delete()`
- 条件付き依存: `if (!(isPrivateMode))` → `this._unblockedChannelIds.delete()`
- 条件付き依存: `if (Manager.ENABLE_WEBCOMPAT)` → `activeAllowLists.values()`
- 条件付き依存: `if (Manager.ENABLE_WEBCOMPAT)` → `allowList.allows()`
- 条件付き依存: `if (allowList.allows(url, topHost))` → `activeUnblockedChannelIds.add()`
- 条件付き依存: `if (allowList.allows(url, topHost))` → `channel.allow()`
- 条件付き依存: `if (allowList.shims(url, topHost, requestType))` → `activeUnblockedChannelIds.add()`
- 条件付き依存: `if (allowList.shims(url, topHost, requestType))` → `channel.replace()`
- 参照: `ChannelWrapper.get(channel.channel).type`, `Ci.nsIIdentChannel`, `Ci.nsIUrlClassifierBlockedChannel`, `Manager.ENABLE_WEBCOMPAT`, `channel.channel`, `channel.topLevelUrl`, `new URL(channel.topLevelUrl).hostname`, `subject.isPrivateBrowsing`, `subject.loadInfo.browsingContext?.originAttributes ?.privateBrowsingId`, `this._PBModeAllowLists`, `this._PBModeUnblockedChannelIds`, `this._allowLists`, `this._unblockedChannelIds`
- XPCOM: [`nsIIdentChannel`](../../../../netwerk/base/nsIChannel.idl.md) / [`nsIUrlClassifierBlockedChannel`](../../../../netwerk/url-classifier/nsIChannelClassifierService.idl.md)

## Manager.stop()
- 位置: L148-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this._channelClassifier.removeListener()`
- 参照: `this._channelClassifier`, `this._classifierObserver`
- XPCOM: `Services.obs`

## Manager.wasChannelIdUnblocked()
- 位置: L162-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activeUnblockedChannelIds?.has()`
- 参照: `this._PBModeUnblockedChannelIds`, `this._unblockedChannelIds`

## Manager.allow()
- 位置: L169-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensureStarted()`, `this._getAllowList()`, `this._getAllowList(allowListId, isPrivateMode).setAllows()`

## Manager.shim()
- 位置: L174-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensureStarted()`, `this._getAllowList()`, `this._getAllowList(allowListId, isPrivateMode).setShims()`

## Manager.revoke()
- 位置: L182-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._PBModeAllowLists.delete()`, `this._allowLists.delete()`

## getChannelId()
- 位置: L189-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChannelWrapper.getRegisteredChannel()`, `wrapper?.channel?.QueryInterface()`
- 参照: `Ci.nsIIdentChannel`, `context.extension.policy`, `context.xulBrowser.frameLoader.remoteTab`, `wrapper?.channel?.QueryInterface(Ci.nsIIdentChannel)?.channelId`
- XPCOM: [`nsIIdentChannel`](../../../../netwerk/base/nsIChannel.idl.md)

## updateDFPIStatus()
- 位置: L201-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## onShutdown()
- 位置: L209-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- 条件付き依存: `if (manager)` → `manager.stop()`
- XPCOM: `Services.prefs`

## getAPI()
- 位置: L217-348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `updateDFPIStatus()`
- 参照: `ExtensionCommon.EventManager`
- XPCOM: `Services.prefs`

## register()
- 位置: L231-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## callback()
- 位置: L232-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`, `tabManager.convert()`
- 参照: `subject.linkedBrowser.currentURI.host`, `tabManager.convert(subject).id`

## register()
- 位置: L247-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## callback()
- 位置: L248-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`, `tabManager.convert()`
- 参照: `subject.linkedBrowser.currentURI.host`, `tabManager.convert(subject).id`

## register()
- 位置: L263-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## callback()
- 位置: L264-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`

## shim()
- 位置: async L273-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manager.shim()`

## allow()
- 位置: async L278-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manager.allow()`

## revoke()
- 位置: async L281-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manager.revoke()`

## clearResourceCache()
- 位置: async L284-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.clearResourceCache()`

## wasRequestUnblocked()
- 位置: async L287-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getChannelId()`, `manager.wasChannelIdUnblocked()`

## isDFPIActive()
- 位置: async L297-302
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dFPIStatus.nonPbMode`, `dFPIStatus.pbMode`

## openProtectionsPanel()
- 位置: L303-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `tabManager.get()`
- 参照: `tab?.active`, `tab?.window`, `win.gBrowser.selectedBrowser.browsingContext`
- XPCOM: `Services.obs`

## getSmartBlockEmbedFluentString()
- 位置: async L316-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatValues()`, `gProtectionsHandler.smartblockEmbedInfo.find()`, `tabManager.get()`
- 参照: `element.shimId`, `tabManager.get(tabId).window`, `win.document`, `win.gBrowser.documentGlobal`
