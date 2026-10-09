# browser/components/contentanalysis/content/ContentAnalysis.sys.mjs

source: browser/components/contentanalysis/content/ContentAnalysis.sys.mjs
source-hash: 2d45f07861f916dd1b06a97c7a6677f2da161031
lines: 1131

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## contentAnalysis()
- 位置: L125-135
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!internalContentAnalysisService)` → `Cc[ "@mozilla.org/contentanalysis;1" ].getService()`
- 参照: `Ci.nsIContentAnalysis`, `this.mockContentAnalysisForTest`
- XPCOM: [`nsIContentAnalysis`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md) / `@mozilla.org/contentanalysis;1` → `mozilla::contentanalysis::ContentAnalysis` (toolkit/components/contentanalysis/components.conf)

## setMockContentAnalysisForTest()
- 位置: L142-144
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.mockContentAnalysisForTest`

## initialize()
- 位置: L152-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.documentElement.setAttribute()`, `doc.getElementsByClassName()`, `doc.l10n.setAttributes()`
- 条件付き依存: `if (!this.contentAnalysis.isActive)` → `this.uninitialize()`
- 条件付き依存: `if (!this.isInitialized)` → `this.initializeObservers()`
- 条件付き依存: `if (!this.isInitialized)` → `ChromeUtils.defineLazyGetter()`
- 参照: `lazy.agentName`, `this.contentAnalysis.isActive`, `this.isInitialized`, `window.document`

## uninitialize()
- 位置: async L182-189
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isInitialized)` → `this.requestTokenToRequestInfo.clear()`
- 条件付き依存: `if (this.isInitialized)` → `this.userActionToBusyDialogMap.clear()`
- 条件付き依存: `if (this.isInitialized)` → `this.uninitializeObservers()`
- 参照: `this.isInitialized`

## initializeObservers()
- 位置: L194-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## uninitializeObservers()
- 位置: L205-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## observe()
- 位置: async L214-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Services.prompt.confirmEx()`, `aSubj.QueryInterface()`, `pendingRequestInfos.flatMap()`, `requestDescriptions.join()`, `this._getAllSlowCARequestInfos()`, `this._getResourceNameFromNameOrOperationType()`, `this._getResourceNameOrOperationTypeFromRequest()`, `this._queueSlowCAMessage()`, `this._removeSlowCAMessage()`, `this.contentAnalysis.respondToWarnDialog()`, `this.l10n.formatValueSync()`, `this.requestTokenToRequestInfo.delete()`, `this.requestTokenToRequestInfo.get()`, `this.requestTokenToRequestInfo.set()`, `this.uninitialize()`
- 条件付き依存: `if (!(buttonSelected === 1))` → `this.contentAnalysis.cancelAllRequests()`
- 条件付き依存: `if (!request)` → `console.error()`
- 条件付き依存: `if (!windowAndResourceNameOrOperationType)` → `console.warn()`
- 条件付き依存: `if (!response?.isCachedResponse)` → `this._showCAResult()`
- 参照: `Ci.nsIContentAnalysisRequest`, `Ci.nsIContentAnalysisRequest.eDownload`, `Ci.nsIContentAnalysisResponse`, `Ci.nsIContentAnalysisResponse.eUnspecified`, `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_0_DEFAULT`, `Ci.nsIPromptService.BUTTON_POS_1`, `Ci.nsIPromptService.BUTTON_TITLE_CANCEL`, `Ci.nsIPromptService.BUTTON_TITLE_IS_STRING`, `aSubj.data`, `info.resourceNameOrOperationType`, `request.operationTypeForDisplay`, `request.requestToken`, `request.windowGlobalParent?.browsingContext`, `requestDescriptions.length`, `response.action`, `response.cancelError`, `response.isSyntheticResponse`, `response.requestToken`, `response.userActionId`, `response?.action`, `response?.isCachedResponse`, `this.warnDialogRequestTokens`, `windowAndResourceNameOrOperationType.browsingContext`, `windowAndResourceNameOrOperationType.resourceNameOrOperationType`, `windowAndResourceNameOrOperationType.resourceNameOrOperationType ?.operationType`
- XPCOM: [`nsIContentAnalysisRequest`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md) / [`nsIContentAnalysisResponse`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md) / [`nsIPromptService`](../../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / `Services.prompt`

## showPanel()
- 位置: async L383-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.ownerDocument.l10n.setAttributes()`, `lazy.PanelMultiView.getViewNode()`, `panelUI.showSubView()`
- 参照: `element.ownerDocument`, `lazy.agentName`

## _disconnectFromView()
- 位置: L400-439
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (caView.timer)` → `lazy.clearTimeout()`
- 条件付き依存: `if (caView.notification.close)` → `caView.notification.close()`
- 条件付き依存: `if (win)` → `win.gBrowser.getTabDialogBox()`
- 条件付き依存: `if (win)` → `dialogBox.getTabDialogManager().abortDialogs()`
- 条件付き依存: `if (win)` → `dialogBox.getTabDialogManager()`
- 条件付き依存: `if (!(caView.notification.dialogBrowsingContext))` → `console.error()`
- 参照: `browser.documentGlobal.browsingContext.embedderElement`, `browser?.documentGlobal`, `browser?.documentGlobal?.browsingContext?.embedderElement?.id`, `caView.notification`, `caView.notification.close`, `caView.notification.dialogBrowsingContext`, `caView.notification.dialogBrowsingContext.top.embedderElement`, `caView.timer`, `caView.userActionId`, `dialog.promptID`, `this.PROMPTID_PREFIX`

## _showMessage()
- 位置: L452-492
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._SHOW_DIALOGS)` → `Services.prompt.asyncAlert()`
- 条件付き依存: `if (this._SHOW_DIALOGS)` → `this.l10n.formatValueSync()`
- 条件付き依存: `if (this._SHOW_NOTIFICATIONS)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!topWindow)` → `console.error()`
- 条件付き依存: `if (this._SHOW_NOTIFICATIONS)` → `this.l10n.formatValueSync()`
- 条件付き依存: `if (aTimeout != 0)` → `lazy.setTimeout()`
- 条件付き依存: `if (aTimeout != 0)` → `notification.close()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_WINDOW`, `aBrowsingContext?.embedderWindowGlobal.browsingContext .topChromeWindow`, `aBrowsingContext?.topChromeWindow`, `lazy.silentNotifications`, `this._SHOW_DIALOGS`, `this._SHOW_NOTIFICATIONS`, `topWindow.Notification`
- XPCOM: [`nsIPrompt`](../../../../netwerk/base/nsIAuthPrompt.idl.md) / `Services.prompt`

## _shouldShowBlockingNotification()
- 位置: L500-505
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIContentAnalysisRequest.eFileDownloaded`, `Ci.nsIContentAnalysisRequest.ePrint`
- XPCOM: [`nsIContentAnalysisRequest`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md)

## _getResourceNameFromNameOrOperationType()
- 位置: L514-541
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!l10nId)` → `console.error()`
- 条件付き依存: `if (!nameOrOperationType.name)` → `this.l10n.formatValueSync()`
- 参照: `Ci.nsIContentAnalysisRequest.eCopyClipboard`, `Ci.nsIContentAnalysisRequest.eDroppedText`, `Ci.nsIContentAnalysisRequest.eOperationPrint`, `Ci.nsIContentAnalysisRequest.ePasteClipboard`, `nameOrOperationType.name`, `nameOrOperationType.operationType`
- XPCOM: [`nsIContentAnalysisRequest`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md)

## _getResourceNameOrOperationTypeFromRequest()
- 位置: L553-584
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aStandalone)` → `this.l10n.formatValueSync()`
- 参照: `Ci.nsIContentAnalysisRequest.eDownload`, `Ci.nsIContentAnalysisRequest.eUpload`, `aRequest.fileNameForDisplay`, `aRequest.operationTypeForDisplay`, `nameOrOperationType.name`
- XPCOM: [`nsIContentAnalysisRequest`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md)

## _queueSlowCAMessage()
- 位置: L594-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setTimeout()`, `this._getSlowDialogMessage()`, `this._shouldShowBlockingNotification()`, `this._showSlowCAMessage()`, `this.userActionToBusyDialogMap.get()`, `this.userActionToBusyDialogMap.set()`
- 条件付き依存: `if (entry)` → `entry.requestTokenSet.add()`
- 参照: `aRequest.analysisType`, `aRequest.requestToken`, `aRequest.userActionId`, `aRequest.userActionRequestsCount`, `entry.notification`, `entry.timer`, `this._SLOW_DLP_NOTIFICATION_BLOCKING_TIMEOUT_MS`, `this._SLOW_DLP_NOTIFICATION_NONBLOCKING_TIMEOUT_MS`

## _removeSlowCAMessage()
- 位置: L638-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entry.requestTokenSet.delete()`, `this._disconnectFromView()`, `this.userActionToBusyDialogMap.delete()`, `this.userActionToBusyDialogMap.get()`
- 条件付き依存: `if (!entry)` → `console.error()`
- 条件付き依存: `if (!entry.requestTokenSet.delete(aRequestToken))` → `console.warn()`
- 参照: `entry.requestTokenSet.size`

## _getAllSlowCARequestInfos()
- 位置: L665-670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestTokenToRequestInfo.get()`, `this.userActionToBusyDialogMap .values()`, `this.userActionToBusyDialogMap .values() .flatMap()`, `this.userActionToBusyDialogMap .values() .flatMap(val => val.requestTokenSet) .map()`
- 参照: `val.requestTokenSet`

## _showSlowCAMessage()
- 位置: L681-698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._shouldShowBlockingNotification()`, `this._showSlowCABlockingMessage()`
- 条件付き依存: `if (!this._shouldShowBlockingNotification(aOperation))` → `this._showMessage()`
- 参照: `aRequest.requestToken`, `aRequest.userActionId`

## _getSlowDialogMessage()
- 位置: L707-743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.l10n.formatValueSync()`
- 条件付き依存: `if (aResourceNameOrOperationType.name)` → `this.l10n.formatValueSync()`
- 条件付き依存: `if (!l10nId)` → `console.error()`
- 参照: `Ci.nsIContentAnalysisRequest.eCopyClipboard`, `Ci.nsIContentAnalysisRequest.eDroppedText`, `Ci.nsIContentAnalysisRequest.eOperationPrint`, `Ci.nsIContentAnalysisRequest.ePasteClipboard`, `aResourceNameOrOperationType.name`, `aResourceNameOrOperationType.operationType`, `lazy.agentName`
- XPCOM: [`nsIContentAnalysisRequest`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md)

## _getErrorDialogMessage()
- 位置: L751-781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.l10n.formatValueSync()`
- 条件付き依存: `if (aResourceNameOrOperationType.name)` → `this.l10n.formatValueSync()`
- 条件付き依存: `if (!l10nId)` → `console.error()`
- 参照: `Ci.nsIContentAnalysisRequest.eCopyClipboard`, `Ci.nsIContentAnalysisRequest.eDroppedText`, `Ci.nsIContentAnalysisRequest.eOperationPrint`, `Ci.nsIContentAnalysisRequest.ePasteClipboard`, `aResourceNameOrOperationType.name`, `aResourceNameOrOperationType.operationType`
- XPCOM: [`nsIContentAnalysisRequest`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md)

## _showSlowCABlockingMessage()
- 位置: L792-846
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.asyncConfirmEx()`, `promise .catch()`, `this.l10n.formatValueSync()`, `this.requestTokenToRequestInfo.delete()`, `this.userActionToBusyDialogMap.has()`
- 条件付き依存: `if (this.userActionToBusyDialogMap.has(aUserActionId))` → `this.contentAnalysis.cancelAllRequestsAssociatedWithUserAction()`
- 条件付き依存: `if (this.requestTokenToRequestInfo.delete(aRequestToken))` → `this._removeSlowCAMessage()`
- 参照: `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_1_DEFAULT`, `Ci.nsIPromptService.BUTTON_TITLE_CANCEL`, `Ci.nsIPromptService.MODAL_TYPE_TAB`, `Ci.nsIPromptService.SHOW_SPINNER`, `this.PROMPTID_PREFIX`
- XPCOM: [`nsIPromptService`](../../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / `Services.prompt`

## _showCAResult()
- 位置: async L860-1109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.asyncAlert()`, `Services.prompt.asyncConfirmEx()`, `aBrowsingContext.embedderElement?.getAttribute()`, `console.error()`, `result.get()`, `this._getErrorDialogMessage()`, `this._getResourceNameFromNameOrOperationType()`, `this._showMessage()`, `this._warnDialogText()`, `this.l10n.formatValue()`, `this.l10n.formatValueSync()`, `this.userActionToBusyDialogMap.get()`, `this.warnDialogRequestTokens.add()`, `this.warnDialogRequestTokens.delete()`
- 条件付き依存: `if (this.warnDialogRequestTokens.delete(aRequestToken))` → `this.contentAnalysis.respondToWarnDialog()`
- 条件付き依存: `if (aResourceNameOrOperationType.name)` → `this.l10n.formatValueSync()`
- 条件付き依存: `if (!(aResourceNameOrOperationType.name))` → `this.contentAnalysis.getDiagnosticInfo()`
- 条件付き依存: `if (!titleId || !bodyId)` → `console.error()`
- 条件付き依存: `if (bodyHasContent)` → `this.l10n.formatValueSync()`
- 条件付き依存: `if (!(bodyHasContent))` → `this.l10n.formatValueSync()`
- 条件付き依存: `if (aBrowsingContext.embedderElement?.getAttribute("printpreview"))` → `win.PrintUtils.getPreviewBrowser()`
- 条件付き依存: `if (busyDialogInfo)` → `busyDialogInfo.requestTokenSet.forEach()`
- 条件付き依存: `if (busyDialogInfo)` → `this.requestTokenToRequestInfo.delete()`
- 条件付き依存: `if (busyDialogInfo)` → `this._removeSlowCAMessage()`
- 条件付き依存: `if (!message)` → `console.error()`
- 参照: `Ci.nsIContentAnalysisRequest.eCopyClipboard`, `Ci.nsIContentAnalysisRequest.eDroppedText`, `Ci.nsIContentAnalysisRequest.eOperationPrint`, `Ci.nsIContentAnalysisRequest.ePasteClipboard`, `Ci.nsIContentAnalysisRequest.eUpload`, `Ci.nsIContentAnalysisResponse.eAllow`, `Ci.nsIContentAnalysisResponse.eBlock`, `Ci.nsIContentAnalysisResponse.eCanceled`, `Ci.nsIContentAnalysisResponse.eErrorOther`, `Ci.nsIContentAnalysisResponse.eInvalidAgentSignature`, `Ci.nsIContentAnalysisResponse.eNoAgent`, `Ci.nsIContentAnalysisResponse.eOtherRequestInGroupCancelled`, `Ci.nsIContentAnalysisResponse.eReportOnly`, `Ci.nsIContentAnalysisResponse.eShutdown`, `Ci.nsIContentAnalysisResponse.eTimeout`, `Ci.nsIContentAnalysisResponse.eUnspecified`, `Ci.nsIContentAnalysisResponse.eUserInitiated`, `Ci.nsIContentAnalysisResponse.eWarn`, `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_1`, `Ci.nsIPromptService.BUTTON_POS_2_DEFAULT`, `Ci.nsIPromptService.BUTTON_TITLE_IS_STRING`, `Ci.nsIPromptService.MODAL_TYPE_TAB`, `aBrowsingContext.embedderElement`, `aResourceNameOrOperationType.name`, `aResourceNameOrOperationType.operationType`, `browser.browsingContext`, `caInfo.connectedToAgent`, `lazy.agentName`, `lazy.showBlockedResult`, `printPreviewBrowser.browserId`, `printPreviewBrowser.documentGlobal`, `this._RESULT_NOTIFICATION_FAST_TIMEOUT_MS`, `this._RESULT_NOTIFICATION_TIMEOUT_MS`, `win.PrintUtils.getPreviewBrowser(browser)?.browserId`, `win.gBrowser.browsers`
- XPCOM: [`nsIContentAnalysisRequest`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md) / [`nsIContentAnalysisResponse`](../../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md) / [`nsIPromptService`](../../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / `Services.prompt`

## _warnDialogText()
- 位置: async L1116-1129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contentAnalysis.getDiagnosticInfo()`, `this.l10n.formatValue()`
- 条件付き依存: `if (caInfo.connectedToAgent)` → `this.l10n.formatValue()`
- 条件付き依存: `if (caInfo.connectedToAgent)` → `this._getResourceNameFromNameOrOperationType()`
- 参照: `caInfo.connectedToAgent`, `lazy.agentName`
