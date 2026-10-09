# browser/components/downloads/DownloadsCommon.sys.mjs

source: browser/components/downloads/DownloadsCommon.sys.mjs
source-hash: 24bcd55f748277b583a9039d1d2ca227904756e5
lines: 1717

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `Object.setPrototypeOf()`, `PrefObserver.register()`, `Services.prefs.getBranch()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `lazy.DownloadsLogger.error.bind()`, `lazy.DownloadsLogger.log.bind()`

## getPref()
- 位置: L107-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `kPrefBranch.getBoolPref()`
- 参照: `this.prefs`

## observe()
- 位置: L116-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.prefs.hasOwnProperty()`
- 条件付き依存: `if (this.prefs.hasOwnProperty(aData))` → `this.getPref()`

## register()
- 位置: L122-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `PrefObserver.getPref()`, `kPrefBranch.addObserver()`
- 参照: `this.prefs`

## strings()
- 位置: L178-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.strings.createBundle()`, `sb.getSimpleEnumeration()`
- 参照: `string.key`, `string.value`, `this.strings`
- XPCOM: `Services.strings`

## strings[stringName]()
- 位置: L184-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `sb.formatStringFromName()`

## openInSystemViewerItemEnabled()
- 位置: L199-201
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PrefObserver.openInSystemViewerContextMenuItem`

## alwaysOpenInSystemViewerItemEnabled()
- 位置: L206-208
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PrefObserver.alwaysOpenInSystemViewerContextMenuItem`

## getData()
- 位置: L227-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 参照: `lazy.DownloadsData`, `lazy.HistoryDownloadsData`, `lazy.LimitedHistoryDownloadsData`, `lazy.LimitedPrivateHistoryDownloadData`, `lazy.PrivateDownloadsData`

## initializeAllDataLinks()
- 位置: L248-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsData.initializeDataLink()`, `lazy.PrivateDownloadsData.initializeDataLink()`

## initializeForWindow()
- 位置: L264-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsTaskbar.registerIndicator()`, `lazy.DownloadsTaskbar.registerIndicator(window).catch()`, `this.initializeAllDataLinks()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `lazy.DownloadsMacFinderProgress.register()`
- 参照: `AppConstants.platform`, `console.error`

## getIndicatorData()
- 位置: L277-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 参照: `lazy.DownloadsIndicatorData`, `lazy.PrivateDownloadsIndicatorData`

## getSummary()
- 位置: L294-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 参照: `this._privateSummary`, `this._summary`

## stateOfDownload()
- 位置: L315-351
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `DownloadsCommon.DOWNLOAD_BLOCKED_CONTENT_ANALYSIS`, `DownloadsCommon.DOWNLOAD_BLOCKED_PARENTAL`, `DownloadsCommon.DOWNLOAD_CANCELED`, `DownloadsCommon.DOWNLOAD_DIRTY`, `DownloadsCommon.DOWNLOAD_DOWNLOADING`, `DownloadsCommon.DOWNLOAD_FAILED`, `DownloadsCommon.DOWNLOAD_FINISHED`, `DownloadsCommon.DOWNLOAD_NOTSTARTED`, `DownloadsCommon.DOWNLOAD_PAUSED`, `download.canceled`, `download.error`, `download.error.becauseBlockedByContentAnalysis`, `download.error.becauseBlockedByParentalControls`, `download.error.becauseBlockedByReputationCheck`, `download.error.reputationCheckVerdict`, `download.hasPartialData`, `download.stopped`, `download.succeeded`, `lazy.Downloads.Error.BLOCK_VERDICT_MALWARE`

## deleteDownload()
- 位置: async L356-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `download.finalize()`, `lazy.Downloads.getList()`, `lazy.PlacesUtils.history.canAddURI()`, `list.remove()`
- 条件付き依存: `if (sourceURI && lazy.PlacesUtils.history.canAddURI(sourceURI))` → `lazy.PlacesUtils.history.remove(sourceURI).catch()`
- 条件付き依存: `if (sourceURI && lazy.PlacesUtils.history.canAddURI(sourceURI))` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (download.hasBlockedData)` → `download.confirmBlock()`
- 条件付き依存: `if (download.error?.becauseBlockedByContentAnalysis)` → `download.respondToContentAnalysisWarnWithBlock()`
- 参照: `URL.parse(download.source.url)?.URI`, `console.error`, `download.error?.becauseBlockedByContentAnalysis`, `download.hasBlockedData`, `download.source.url`, `lazy.Downloads.ALL`

## deleteDownloadFiles()
- 位置: async L388-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `download.manuallyRemoveData()`
- 条件付き依存: `if (clearHistoryOnDelete > 1)` → `URL.parse()`
- 条件付き依存: `if (clearHistoryOnDelete > 1)` → `lazy.PlacesUtils.history.canAddURI()`
- 条件付き依存: `if (sourceURI && lazy.PlacesUtils.history.canAddURI(sourceURI))` → `lazy.PlacesUtils.history.remove(sourceURI).catch()`
- 条件付き依存: `if (sourceURI && lazy.PlacesUtils.history.canAddURI(sourceURI))` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (clearHistoryOnDelete > 0)` → `lazy.Downloads.getList()`
- 条件付き依存: `if (clearHistoryOnDelete > 0)` → `list.remove()`
- 条件付き依存: `if (download.error?.becauseBlockedByContentAnalysis)` → `download.respondToContentAnalysisWarnWithBlock()`
- 条件付き依存: `if (clearHistoryOnDelete < 2)` → `lazy.DownloadHistory.updateMetaData(download).catch()`
- 条件付き依存: `if (clearHistoryOnDelete < 2)` → `lazy.DownloadHistory.updateMetaData()`
- 参照: `URL.parse(download.source.url)?.URI`, `console.error`, `download.error?.becauseBlockedByContentAnalysis`, `download.source.url`, `lazy.Downloads.ALL`

## getMimeInfo()
- 位置: L411-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/network/standard-url-mutator;1"] .createInstance()`, `Cc["@mozilla.org/network/standard-url-mutator;1"] .createInstance(Ci.nsIURIMutator) .setSpec()`, `DownloadsCommon.log()`, `kGenericContentTypes.includes()`, `lazy.gMIMEService.getFromTypeAndExtension()`
- 条件付き依存: `if (!contentType || kGenericContentTypes.includes(contentType))` → `lazy.gMIMEService.getTypeFromExtension()`
- 条件付き依存: `if (!contentType || kGenericContentTypes.includes(contentType))` → `DownloadsCommon.log()`
- 参照: `Ci.nsIURIMutator`, `Ci.nsIURL`, `download.contentType`, `download.succeeded`, `download.target.path`, `url.fileExtension`
- XPCOM: [`nsIURIMutator`](../../../netwerk/base/nsIFileURL.idl.md) / [`nsIURL`](../../../netwerk/base/nsIURL.idl.md) / `@mozilla.org/network/standard-url-mutator;1`

## isFileOfType()
- 位置: L458-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getMimeInfo()`, `mimeType.toLowerCase()`
- 条件付き依存: `if (!(download.succeeded && download.target?.exists))` → `DownloadsCommon.log()`
- 参照: `download.succeeded`, `download.target?.exists`, `mimeInfo?.type`

## copyDownloadLink()
- 位置: L472-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gClipboardHelper.copyString()`
- 参照: `download.source.originalUrl`, `download.source.url`

## summarizeDownloads()
- 位置: L498-552
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (download.hasProgress && download.speed > 0)` → `Math.max()`
- 条件付き依存: `if (download.hasProgress && download.speed > 0)` → `Math.min()`
- 条件付き依存: `if (summary.totalSize != 0)` → `Math.floor()`
- 参照: `download.canceled`, `download.currentBytes`, `download.hasPartialData`, `download.hasProgress`, `download.speed`, `download.stopped`, `download.succeeded`, `download.target.size`, `download.totalBytes`, `summary.numActive`, `summary.numDownloading`, `summary.numPaused`, `summary.percentComplete`, `summary.rawTimeLeft`, `summary.slowestSpeed`, `summary.totalSize`, `summary.totalTransferred`

## smoothSeconds()
- 位置: L563-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`
- 条件付き依存: `if (shouldApplySmoothing)` → `Math.abs()`

## openDownload()
- 位置: async L606-612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `download.launch()`, `download.launch(options).catch()`
- 条件付き依存: `if (typeof download.launch !== "function")` → `lazy.Downloads.createDownload()`
- 参照: `download.launch`

## showDownloadedFile()
- 位置: L620-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aFile.reveal()`
- 条件付き依存: `if (parent)` → `this.showDirectory()`
- 参照: `Ci.nsIFile`, `aFile.parent`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md)

## showDirectory()
- 位置: L643-659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/uriloader/external-protocol-service;1"] .getService()`, `Cc["@mozilla.org/uriloader/external-protocol-service;1"] .getService(Ci.nsIExternalProtocolService) .loadURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `aDirectory.launch()`, `lazy.NetUtil.newURI()`
- 参照: `Ci.nsIExternalProtocolService`, `Ci.nsIFile`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / [`nsIFile`](../shell/nsIShellService.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1` / `Services.scriptSecurityManager`

## confirmUnblockDownload()
- 位置: async L691-795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmEx()`, `Services.ww.registerNotification()`, `console.error()`
- 参照: `Ci.nsIPrompt.BUTTON_POS_0`, `Ci.nsIPrompt.BUTTON_POS_0_DEFAULT`, `Ci.nsIPrompt.BUTTON_POS_1`, `Ci.nsIPrompt.BUTTON_POS_1_DEFAULT`, `Ci.nsIPrompt.BUTTON_POS_2`, `Ci.nsIPrompt.BUTTON_POS_2_DEFAULT`, `Ci.nsIPrompt.BUTTON_TITLE_CANCEL`, `Ci.nsIPrompt.BUTTON_TITLE_IS_STRING`, `DownloadsCommon.strings`, `lazy.Downloads.Error.BLOCK_VERDICT_INSECURE`, `lazy.Downloads.Error.BLOCK_VERDICT_POTENTIALLY_UNWANTED`, `lazy.Downloads.Error.BLOCK_VERDICT_UNCOMMON`, `s.unblockButtonConfirmBlock`, `s.unblockButtonOpen`, `s.unblockButtonUnblock`, `s.unblockContentAnalysisTip`, `s.unblockHeaderOpen`, `s.unblockHeaderUnblock`, `s.unblockInsecure2`, `s.unblockTip2`, `s.unblockTypeContentAnalysisWarn`, `s.unblockTypeMalware`, `s.unblockTypePotentiallyUnwanted2`, `s.unblockTypeUncommon2`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / `Services.prompt` / `Services.ww`

## onOpen()
- 位置: L759-781
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "domwindowopened" && subj instanceof Ci.nsIDOMWindow)` → `subj.addEventListener()`
- 条件付き依存: `if ( subj.document.documentURI == "chrome://global/content/commonDialog.xhtml" )` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if ( subj.document.documentURI == "chrome://global/content/commonDialog.xhtml" )` → `subj.document.getElementById()`
- 条件付き依存: `if (dialog)` → `dialog.classList.add()`
- 参照: `Ci.nsIDOMWindow`, `subj.document.documentURI`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md) / `Services.ww`

## DownloadsDataCtor()
- 位置: L819-857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Downloads.getList()`, `list.addView()`
- 条件付き依存: `if (isPrivate)` → `lazy.PrivateDownloadsData.initializeDataLink()`
- 条件付き依存: `if (isHistory)` → `lazy.DownloadsData.initializeDataLink()`
- 条件付き依存: `if (isHistory)` → `lazy.DownloadsData._promiseList.then()`
- 条件付き依存: `if (isHistory)` → `lazy.DownloadHistory.getList()`
- 参照: `lazy.Downloads.ALL`, `lazy.Downloads.PRIVATE`, `lazy.Downloads.PUBLIC`, `this._isPrivate`, `this._oldDownloadStates`, `this._promiseList`, `this.initializeDataLink`

## initializeDataLink()
- 位置: L863-863
- 役割: (未記入)
- 触るとき: (未記入)

## _downloads()
- 位置: L875-877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 参照: `this._oldDownloadStates`

## canRemoveFinished()
- 位置: L882-890
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `download.canceled`, `download.hasPartialData`, `download.stopped`, `this._downloads`

## removeFinished()
- 位置: L896-902
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Downloads.getList()`, `lazy.Downloads.getList( this._isPrivate ? lazy.Downloads.PRIVATE : lazy.Downloads.PUBLIC ) .then()`, `list.removeFinished()`
- 参照: `console.error`, `lazy.Downloads.PRIVATE`, `lazy.Downloads.PUBLIC`, `this._isPrivate`

## onDownloadAdded()
- 位置: L906-923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `DownloadsCommon.stateOfDownload()`, `this._oldDownloadStates.set()`
- 条件付き依存: `if ( download.error?.becauseBlockedByReputationCheck || download.error?.becauseBlockedByContentAnalysis )` → `this._notifyDownloadEvent()`
- 参照: `download.endTime`, `download.error?.becauseBlockedByContentAnalysis`, `download.error?.becauseBlockedByReputationCheck`

## onDownloadChanged()
- 位置: L925-972
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.stateOfDownload()`, `this._oldDownloadStates.get()`, `this._oldDownloadStates.set()`
- 条件付き依存: `if ( download.succeeded || (download.canceled && !download.hasPartialData) || download.error )` → `Date.now()`
- 条件付き依存: `if ( download.succeeded || (download.canceled && !download.hasPartialData) || download.error )` → `lazy.DownloadHistory.updateMetaData(download).catch()`
- 条件付き依存: `if ( download.succeeded || (download.canceled && !download.hasPartialData) || download.error )` → `lazy.DownloadHistory.updateMetaData()`
- 条件付き依存: `if ( download.succeeded || (download.canceled && !download.hasPartialData) || download.error )` → `download.source.url?.startsWith()`
- 条件付き依存: `if ( download.succeeded && download.source.url?.startsWith("data:") && download.source.url.length > kLargeDataUriLengthThreshold )` → `download.source.url.indexOf()`
- 条件付き依存: `if ( download.succeeded && download.source.url?.startsWith("data:") && download.source.url.length > kLargeDataUriLengthThreshold )` → `download.source.url.slice()`
- 条件付き依存: `if ( download.succeeded || (download.error && download.error.becauseBlocked) )` → `this._notifyDownloadEvent()`
- 条件付き依存: `if (!download.newDownloadNotified)` → `this._notifyDownloadEvent()`
- 参照: `console.error`, `download.canceled`, `download.endTime`, `download.error`, `download.error.becauseBlocked`, `download.hasPartialData`, `download.newDownloadNotified`, `download.openDownloadsListOnStart`, `download.source.isDataURICleared`, `download.source.url`, `download.source.url.length`, `download.succeeded`

## onDownloadRemoved()
- 位置: L974-976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._oldDownloadStates.delete()`

## addView()
- 位置: L988-990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.addView()`, `this._promiseList.then()`, `this._promiseList.then(list => list.addView(aView)).catch()`
- 参照: `console.error`

## removeView()
- 位置: L998-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.removeView()`, `this._promiseList.then()`, `this._promiseList.then(list => list.removeView(aView)).catch()`
- 参照: `console.error`

## panelHasShownBefore()
- 位置: L1008-1013
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## panelHasShownBefore()
- 位置: L1015-1017
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## _notifyDownloadEvent()
- 位置: L1031-1069
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`, `DownloadsCommon.summarizeDownloads()`, `browserWin.DownloadsPanel.showPanel()`, `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if ( aType != "error" && ((this.panelHasShownBefore && !shouldOpenDownloadsPanel) || !openDownloadsListOnStart || browserWin != Services.focus.activeWindow) )` → `DownloadsCommon.log()`
- 条件付き依存: `if ( aType != "error" && ((this.panelHasShownBefore && !shouldOpenDownloadsPanel) || !openDownloadsListOnStart || browserWin != Services.focus.activeWindow) )` → `browserWin.DownloadsIndicatorView.showEventNotification()`
- 参照: `DownloadsCommon.summarizeDownloads(this._downloads).numDownloading`, `Services.focus.activeWindow`, `lazy.gAlwaysOpenPanel`, `this._downloads`, `this._isPrivate`, `this.panelHasShownBefore`
- XPCOM: `Services.focus`

## addView()
- 位置: L1143-1155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._views.push()`, `this.refreshView()`
- 条件付き依存: `if (this._isPrivate)` → `lazy.PrivateDownloadsData.addView()`
- 条件付き依存: `if (!(this._isPrivate))` → `lazy.DownloadsData.addView()`
- 参照: `this._isPrivate`, `this._views.length`

## refreshView()
- 位置: L1163-1168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._refreshProperties()`, `this._updateView()`

## removeView()
- 位置: L1176-1190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._views.indexOf()`
- 条件付き依存: `if (index != -1)` → `this._views.splice()`
- 条件付き依存: `if (this._isPrivate)` → `lazy.PrivateDownloadsData.removeView()`
- 条件付き依存: `if (!(this._isPrivate))` → `lazy.DownloadsData.removeView()`
- 参照: `this._isPrivate`, `this._views.length`

## onDownloadBatchStarting()
- 位置: L1202-1204
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._loading`

## onDownloadBatchEnded()
- 位置: L1209-1212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateViews()`
- 参照: `this._loading`

## onDownloadAdded()
- 位置: L1223-1228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.stateOfDownload()`, `this._oldDownloadStates.set()`

## onDownloadStateChanged()
- 位置: L1239-1241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## onDownloadChanged()
- 位置: L1252-1260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.stateOfDownload()`, `this._oldDownloadStates.get()`, `this._oldDownloadStates.set()`
- 条件付き依存: `if (oldState != newState)` → `this.onDownloadStateChanged()`

## onDownloadRemoved()
- 位置: L1271-1273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._oldDownloadStates.delete()`

## _refreshProperties()
- 位置: L1281-1283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## _updateView()
- 位置: L1290-1292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## _updateViews()
- 位置: L1297-1305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._refreshProperties()`, `this._views.forEach()`
- 参照: `this._loading`, `this._updateView`

## DownloadsIndicatorDataCtor()
- 位置: L1320-1324
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isPrivate`, `this._oldDownloadStates`, `this._views`

## _downloads()
- 位置: L1343-1345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 参照: `this._oldDownloadStates`

## removeView()
- 位置: L1353-1359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewPrototype.removeView.call()`
- 参照: `this._itemCount`, `this._views.length`

## onDownloadAdded()
- 位置: L1361-1365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewPrototype.onDownloadAdded.call()`, `this._updateViews()`
- 参照: `this._itemCount`

## onDownloadStateChanged()
- 位置: L1367-1403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateAttention()`
- 条件付き依存: `if ( !download.succeeded && download.error && download.error.reputationCheckVerdict )` → `console.error()`
- 参照: `DownloadsCommon.ATTENTION_INFO`, `DownloadsCommon.ATTENTION_SEVERE`, `DownloadsCommon.ATTENTION_SUCCESS`, `DownloadsCommon.ATTENTION_WARNING`, `DownloadsCommon.SUPPRESS_NONE`, `download.attention`, `download.error`, `download.error.reputationCheckVerdict`, `download.succeeded`, `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`, `lazy.Downloads.Error.BLOCK_VERDICT_INSECURE`, `lazy.Downloads.Error.BLOCK_VERDICT_MALWARE`, `lazy.Downloads.Error.BLOCK_VERDICT_POTENTIALLY_UNWANTED`, `lazy.Downloads.Error.BLOCK_VERDICT_UNCOMMON`, `this._attentionSuppressed`

## onDownloadChanged()
- 位置: L1405-1408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewPrototype.onDownloadChanged.call()`, `this._updateViews()`

## onDownloadRemoved()
- 位置: L1410-1415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewPrototype.onDownloadRemoved.call()`, `this._updateViews()`, `this.updateAttention()`
- 参照: `this._itemCount`

## attention()
- 位置: L1427-1430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateViews()`
- 参照: `this._attention`

## attentionSuppressed()
- 位置: L1437-1445
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `DownloadsCommon.ATTENTION_NONE`, `DownloadsCommon.SUPPRESS_NONE`, `download.attention`, `this._attentionSuppressed`, `this._downloads`, `this.attention`

## attentionSuppressed()
- 位置: L1446-1448
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._attentionSuppressed`

## updateAttention()
- 位置: L1455-1467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._attentionPriority.get()`
- 参照: `DownloadsCommon.ATTENTION_NONE`, `this._downloads`, `this.attention`

## _updateView()
- 位置: L1475-1482
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `DownloadsCommon.ATTENTION_NONE`, `DownloadsCommon.SUPPRESS_NONE`, `aView.attention`, `aView.hasDownloads`, `aView.percentComplete`, `this._attention`, `this._hasDownloads`, `this._percentComplete`, `this.attentionSuppressed`

## _activeDownloads()
- 位置: L1497-1509
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `download.canceled`, `download.hasPartialData`, `download.isInCurrentBatch`, `lazy.DownloadsData._downloads`, `lazy.PrivateDownloadsData._downloads`, `this._isPrivate`

## _refreshProperties()
- 位置: L1514-1528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.summarizeDownloads()`, `this._activeDownloads()`
- 参照: `summary.numDownloading`, `summary.percentComplete`, `this._hasDownloads`, `this._itemCount`, `this._percentComplete`

## DownloadsSummaryData()
- 位置: L1563-1595
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._description`, `this._details`, `this._downloads`, `this._isPrivate`, `this._lastRawTimeLeft`, `this._lastTimeLeft`, `this._loading`, `this._numActive`, `this._numToExclude`, `this._oldDownloadStates`, `this._percentComplete`, `this._showingProgress`, `this._views`

## removeView()
- 位置: L1604-1612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewPrototype.removeView.call()`
- 参照: `this._downloads`, `this._views.length`

## onDownloadAdded()
- 位置: L1614-1618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewPrototype.onDownloadAdded.call()`, `this._downloads.unshift()`, `this._updateViews()`

## onDownloadStateChanged()
- 位置: L1620-1624
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lastRawTimeLeft`, `this._lastTimeLeft`

## onDownloadChanged()
- 位置: L1626-1629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewPrototype.onDownloadChanged.call()`, `this._updateViews()`

## onDownloadRemoved()
- 位置: L1631-1636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewPrototype.onDownloadRemoved.call()`, `this._downloads.indexOf()`, `this._downloads.splice()`, `this._updateViews()`

## _updateView()
- 位置: L1646-1651
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aView.description`, `aView.details`, `aView.percentComplete`, `aView.showingProgress`, `this._description`, `this._details`, `this._percentComplete`, `this._showingProgress`

## _downloadsForSummary()
- 位置: L1662-1668
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._downloads`, `this._downloads.length`, `this._numToExclude`

## _refreshProperties()
- 位置: L1673-1714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.summarizeDownloads()`, `kDownloadsFluentStrings.formatValueSync()`, `this._downloadsForSummary()`
- 条件付き依存: `if (this._lastRawTimeLeft != summary.rawTimeLeft)` → `DownloadsCommon.smoothSeconds()`
- 条件付き依存: `if (!(summary.rawTimeLeft == -1))` → `lazy.DownloadUtils.getDownloadStatusNoRate()`
- 参照: `summary.numDownloading`, `summary.percentComplete`, `summary.rawTimeLeft`, `summary.slowestSpeed`, `summary.totalSize`, `summary.totalTransferred`, `this._description`, `this._details`, `this._lastRawTimeLeft`, `this._lastTimeLeft`, `this._percentComplete`, `this._showingProgress`
