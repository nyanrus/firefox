# browser/components/downloads/DownloadsViewUI.sys.mjs

source: browser/components/downloads/DownloadsViewUI.sys.mjs
source-hash: 10b9e6ef4943fcea65da61130103d51c587dd512
lines: 1293

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Integration.downloads.defineESModuleGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## isCommandName()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `name.startsWith()`

## getStrippedUrl()
- 位置: L132-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.stripPrefixAndTrim()`
- 参照: `download?.source?.url`

## getDisplayName()
- 位置: L145-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.filename()`
- 条件付き依存: `if ( download.error?.reputationCheckVerdict == lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM )` → `DownloadsViewUI.getStrippedUrl()`
- 参照: `download.error?.reputationCheckVerdict`, `download.source.url`, `download.target.path`, `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`

## getSizeWithUnits()
- 位置: L166-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadUtils.convertByteUnits()`, `lazy.DownloadsCommon.strings.sizeWithUnits()`
- 参照: `download.target.size`

## updateContextMenuForElement()
- 位置: L182-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.filename()`, `Services.policies.isExemptExecutableExtension()`, `[ DOWNLOAD_NOTSTARTED, DOWNLOAD_DOWNLOADING, DOWNLOAD_FINISHED, DOWNLOAD_PAUSED, ].includes()`, `contextMenu.querySelector()`, `document.l10n.pauseObserving()`, `document.l10n.resumeObserving()`, `document.l10n.translateElements()`, `element.classList.contains()`, `element.getAttribute()`, `element.hasAttribute()`, `filename?.split()`, `filename?.split(".").at()`, `lazy.DownloadsCommon.getMimeInfo()`, `lazy.gReputationService.isBinary()`, `lazy.gReputationService.isExecutable()`, `parseInt()`
- 条件付き依存: `if (defaultDescription && defaultDescription.length < 40)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(defaultDescription && defaultDescription.length < 40))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (preferredAction === useSystemDefault)` → `alwaysUseSystemViewerItem.setAttribute()`
- 条件付き依存: `if (preferredAction === useSystemDefault)` → `alwaysOpenSimilarFilesItem.setAttribute()`
- 条件付き依存: `if (!(preferredAction === useSystemDefault))` → `alwaysUseSystemViewerItem.removeAttribute()`
- 条件付き依存: `if (!(preferredAction === useSystemDefault))` → `alwaysOpenSimilarFilesItem.removeAttribute()`
- 参照: `alwaysOpenSimilarFilesItem.hidden`, `alwaysUseSystemViewerItem.hidden`, `contextMenu.ownerDocument`, `contextMenu.querySelector(".downloadCommandsSeparator").hidden`, `contextMenu.querySelector(".downloadDeleteFileMenuItem").hidden`, `contextMenu.querySelector(".downloadOpenReferrerMenuItem").hidden`, `contextMenu.querySelector(".downloadPauseMenuItem").hidden`, `contextMenu.querySelector(".downloadRemoveFromHistoryMenuItem").hidden`, `contextMenu.querySelector(".downloadResumeMenuItem").hidden`, `contextMenu.querySelector(".downloadShowMenuItem").hidden`, `contextMenu.querySelector(".downloadUnblockMenuItem").hidden`, `defaultDescription.length`, `download.deleted`, `download.source.originalUrl`, `download.source.referrerInfo?.originalReferrer`, `download.source.url`, `download.target.path`, `download.target?.exists`, `download.target?.partFileExists`, `element._shell.download`, `lazy.DownloadsCommon`, `lazy.DownloadsCommon.alwaysOpenInSystemViewerItemEnabled`, `lazy.DownloadsCommon.openInSystemViewerItemEnabled`, `lazy.safeBrowsingAllowOverride`, `mimeInfo.type`, `mimeInfo?.type`, `useSystemViewerItem.hidden`
- XPCOM: `Services.policies`

## canClearDownloads()
- 位置: L377-390
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `download.canceled`, `download.hasPartialData`, `download.stopped`, `elt._shell.download`, `elt.previousSibling`, `nodeContainer.lastChild`

## DownloadsViewUI.DownloadElementShell()
- 位置: L406-406
- 役割: (未記入)
- 触るとき: (未記入)

## ensureActive()
- 位置: L419-425
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._active)` → `this.connect()`
- 条件付き依存: `if (!this._active)` → `this.onChanged()`
- 参照: `this._active`

## active()
- 位置: L426-428
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._active`

## connect()
- 位置: L430-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElementNS()`, `document.importNode()`, `downloadButton.addEventListener()`, `ev.target.documentGlobal.DownloadsView.onDownloadClick()`, `event.target.documentGlobal.DownloadsView.onDownloadButton()`, `gDownloadListItemFragments.get()`, `progress.setAttribute()`, `this._downloadTarget.insertAdjacentElement()`, `this.element.addEventListener()`, `this.element.appendChild()`, `this.element.querySelector()`, `this.element.setAttribute()`
- 条件付き依存: `if (!downloadListItemFragment)` → `MozXULElement.parseXULToFragment()`
- 条件付き依存: `if (!downloadListItemFragment)` → `gDownloadListItemFragments.set()`
- 参照: `document.defaultView.MozXULElement`, `progress.className`, `this._downloadProgress`, `this.element.ownerDocument`

## image()
- 位置: L491-509
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.download.succeeded`, `this.download.target.path`

## browserWindow()
- 位置: L511-515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`

## showDisplayNameAndIcon()
- 位置: L525-538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._downloadTypeIcon.setAttribute()`
- 条件付き依存: `if (displayName.l10n)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(displayName.l10n))` → `this._downloadTarget.setAttribute()`
- 参照: `displayName.l10n`, `displayName.l10n.args`, `displayName.l10n.id`, `this._downloadTarget`, `this.element.ownerDocument`

## showProgress()
- 位置: L550-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._downloadProgress.toggleAttribute()`
- 条件付き依存: `if (mode == "undetermined")` → `this._downloadProgress.removeAttribute()`
- 条件付き依存: `if (!(mode == "undetermined"))` → `this._downloadProgress.setAttribute()`

## showStatus()
- 位置: L570-594
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (status?.l10n)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(status?.l10n))` → `this._downloadDetailsNormal.removeAttribute()`
- 条件付き依存: `if (!(status?.l10n))` → `this._downloadDetailsNormal.setAttribute()`
- 条件付き依存: `if (hoverStatus?.l10n)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(hoverStatus?.l10n))` → `this._downloadDetailsHover.removeAttribute()`
- 条件付き依存: `if (!(hoverStatus?.l10n))` → `this._downloadDetailsHover.setAttribute()`
- 参照: `hoverStatus.l10n.args`, `hoverStatus.l10n.id`, `hoverStatus?.l10n`, `status.l10n.args`, `status.l10n.id`, `status?.l10n`, `this._downloadDetailsHover`, `this._downloadDetailsNormal`, `this.element.ownerDocument`

## showStatusWithDetails()
- 位置: L611-641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `lazy.BrowserUtils.formatURIForDisplay()`, `lazy.DownloadUtils.getReadableDates()`, `lazy.DownloadsCommon.strings.statusSeparator()`
- 条件付き依存: `if (stateLabel.l10n)` → `this.showStatus()`
- 条件付き依存: `if (!this.isPanel)` → `this.showStatus()`
- 条件付き依存: `if (!(!this.isPanel))` → `this.showStatus()`
- 参照: `URL.parse(this.download.source.url)?.URI`, `stateLabel.l10n`, `this.download.endTime`, `this.download.source.url`, `this.isPanel`

## showButton()
- 位置: L649-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `this._downloadButton.removeAttribute()`, `this._downloadButton.setAttribute()`
- 条件付き依存: `if (this.isPanel && descriptionL10nId)` → `document.l10n.setAttributes()`
- 参照: `this._downloadButton`, `this._downloadDetailsButtonHover`, `this.buttonCommandName`, `this.element.ownerDocument`, `this.isPanel`

## hideButton()
- 位置: L667-669
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._downloadButton.hidden`

## _updateState()
- 位置: L677-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.getDisplayName()`, `lazy.DownloadsCommon.stateOfDownload()`, `this._updateStateInner()`, `this.element.setAttribute()`, `this.showDisplayNameAndIcon()`
- 条件付き依存: `if (!this.download.stopped)` → `this.showButton()`
- 条件付き依存: `if (!this.download.stopped)` → `this.element.removeAttribute()`
- 参照: `this.download`, `this.download.stopped`, `this.image`, `this.lastEstimatedSecondsLeft`

## _updateStateInner()
- 位置: L710-904
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.element.classList.toggle()`
- 条件付き依存: `if (!this.download.stopped)` → `lazy.DownloadUtils.getDownloadStatus()`
- 条件付き依存: `if (this.download.launchWhenSucceeded)` → `lazy.DownloadUtils.getFormattedTimeStatus()`
- 条件付き依存: `if (!this.download.stopped)` → `this.showStatus()`
- 条件付き依存: `if (this.download.deleted)` → `this.showDeletedOrMissing()`
- 条件付き依存: `if (this.download.succeeded)` → `lazy.DownloadsCommon.log()`
- 条件付き依存: `if (this.download.target.exists)` → `this.element.setAttribute()`
- 条件付き依存: `if (this.download.target.exists)` → `this.element.toggleAttribute()`
- 条件付き依存: `if (this.download.target.exists)` → `lazy.DownloadIntegration.shouldViewDownloadInternally()`
- 条件付き依存: `if (this.download.target.exists)` → `lazy.DownloadsCommon.getMimeInfo()`
- 条件付き依存: `if (this.download.target.exists)` → `DownloadsViewUI.getSizeWithUnits()`
- 条件付き依存: `if (sizeWithUnits)` → `lazy.DownloadsCommon.strings.statusSeparator()`
- 条件付き依存: `if (this.isPanel)` → `this.showStatus()`
- 条件付き依存: `if (!(this.isPanel))` → `this.showStatusWithDetails()`
- 条件付き依存: `if (this.download.target.exists)` → `this.showButton()`
- 条件付き依存: `if (!(this.download.target.exists))` → `this.showDeletedOrMissing()`
- 条件付き依存: `if (this.download.error.becauseBlockedByParentalControls)` → `this.showStatusWithDetails()`
- 条件付き依存: `if (this.download.error.becauseBlockedByParentalControls)` → `this.hideButton()`
- 条件付き依存: `if (!this.download.hasBlockedData)` → `this.hideButton()`
- 条件付き依存: `if (this.isPanel)` → `this.showButton()`
- 条件付き依存: `if (this.download.launchWhenSucceeded)` → `this.showButton()`
- 条件付き依存: `if (!(this.download.launchWhenSucceeded))` → `this.showButton()`
- 条件付き依存: `if (!(this.isPanel))` → `this.showButton()`
- 条件付き依存: `if ( this.download.error.becauseBlockedByReputationCheck || this.download.error.becauseBlockedByContentAnalysis )` → `this.showStatusWithDetails()`
- 条件付き依存: `if (!( this.download.error.becauseBlockedByReputationCheck || this.download.error.becauseBlockedByContentAnalysis ))` → `this.showStatusWithDetails()`
- 条件付き依存: `if (!( this.download.error.becauseBlockedByReputationCheck || this.download.error.becauseBlockedByContentAnalysis ))` → `this.showButton()`
- 条件付き依存: `if (this.download.hasPartialData)` → `lazy.DownloadUtils.getTransferTotal()`
- 条件付き依存: `if (this.download.hasPartialData)` → `this.showStatus()`
- 条件付き依存: `if (this.download.hasPartialData)` → `lazy.DownloadsCommon.strings.statusSeparatorBeforeNumber()`
- 条件付き依存: `if (this.download.hasPartialData)` → `this.showButton()`
- 条件付き依存: `if (!(this.download.hasPartialData))` → `this.showStatusWithDetails()`
- 条件付き依存: `if (!(this.download.hasPartialData))` → `this.showButton()`
- 条件付き依存: `if (!(this.download.canceled))` → `this.showStatus()`
- 条件付き依存: `if (!(this.download.canceled))` → `this.showButton()`
- 条件付き依存: `if (verdict)` → `this.element.setAttribute()`
- 条件付き依存: `if (!(verdict))` → `this.element.removeAttribute()`
- 条件付き依存: `if (!(!this.download.stopped))` → `this.element.classList.toggle()`
- 条件付き依存: `if (this.download.hasProgress)` → `this.showProgress()`
- 条件付き依存: `if (!(this.download.hasProgress))` → `this.showProgress()`
- 参照: `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`, `lazy.Downloads.Error.BLOCK_VERDICT_INSECURE`, `lazy.Downloads.Error.BLOCK_VERDICT_POTENTIALLY_UNWANTED`, `lazy.Downloads.Error.BLOCK_VERDICT_UNCOMMON`, `lazy.DownloadsCommon.getMimeInfo(this.download)?.type`, `lazy.DownloadsCommon.strings.sizeUnknown`, `lazy.DownloadsCommon.strings.stateBlockedParentalControls`, `lazy.DownloadsCommon.strings.stateCanceled`, `lazy.DownloadsCommon.strings.stateCompleted`, `lazy.DownloadsCommon.strings.stateFailed`, `lazy.DownloadsCommon.strings.statePaused`, `lazy.DownloadsCommon.strings.stateStarting`, `this.download`, `this.download.canceled`, `this.download.currentBytes`, `this.download.deleted`, `this.download.error`, `this.download.error.becauseBlockedByContentAnalysis`, `this.download.error.becauseBlockedByParentalControls`, `this.download.error.becauseBlockedByReputationCheck`, `this.download.error.localizedReason`, `this.download.error.reputationCheckVerdict`, `this.download.hasBlockedData`, `this.download.hasPartialData`, `this.download.hasProgress`, `this.download.launchWhenSucceeded`, `this.download.progress`, `this.download.speed`, `this.download.stopped`, `this.download.succeeded`, `this.download.target.exists`, `this.download.target.path`, `this.download.totalBytes`, `this.isPanel`, `this.lastEstimatedSecondsLeft`, `this.rawBlockedTitleAndDetails`

## getContentAnalysisErrorTitle()
- 位置: L906-929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `strings.contentAnalysisInvalidAgentSignatureError()`, `strings.contentAnalysisNoAgentError()`, `strings.contentAnalysisTimeoutError()`, `strings.contentAnalysisUnspecifiedError()`
- 参照: `Ci.nsIContentAnalysisResponse.eErrorOther`, `Ci.nsIContentAnalysisResponse.eInvalidAgentSignature`, `Ci.nsIContentAnalysisResponse.eNoAgent`, `Ci.nsIContentAnalysisResponse.eTimeout`, `lazy.contentAnalysisAgentName`, `strings.blockedByContentAnalysis`
- XPCOM: [`nsIContentAnalysisResponse`](../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md)

## rawBlockedTitleAndDetails()
- 位置: L935-1004
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.getStrippedUrl()`, `this.getContentAnalysisErrorTitle()`
- 参照: `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`, `lazy.Downloads.Error.BLOCK_VERDICT_INSECURE`, `lazy.Downloads.Error.BLOCK_VERDICT_MALWARE`, `lazy.Downloads.Error.BLOCK_VERDICT_POTENTIALLY_UNWANTED`, `lazy.Downloads.Error.BLOCK_VERDICT_UNCOMMON`, `lazy.DownloadsCommon.strings`, `s.blockedMalware`, `s.blockedPotentiallyInsecure`, `s.blockedPotentiallyUnwanted`, `s.blockedUncommon2`, `s.unblockContentAnalysis1`, `s.unblockContentAnalysis2`, `s.unblockContentAnalysisWarnTip`, `s.unblockInsecure2`, `s.unblockTip2`, `s.unblockTypeContentAnalysisWarn`, `s.unblockTypeMalware`, `s.unblockTypePotentiallyUnwanted2`, `s.unblockTypeUncommon2`, `s.warnedByContentAnalysis`, `this.download`, `this.download.blockedDownloadsCount`, `this.download.error`, `this.download.error.becauseBlockedByContentAnalysis`, `this.download.error.becauseBlockedByReputationCheck`, `this.download.error.contentAnalysisCancelError`, `this.download.error.reputationCheckVerdict`

## showDeletedOrMissing()
- 位置: L1006-1019
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.element.removeAttribute()`, `this.hideButton()`, `this.showStatusWithDetails()`
- 参照: `lazy.DownloadsCommon.strings`, `this.download.deleted`, `this.download.error?.becauseBlocked`

## confirmUnblock()
- 位置: L1031-1050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `lazy.DownloadsCommon.confirmUnblockDownload()`
- 条件付き依存: `if (action == "open")` → `this.unblockAndOpenDownload()`
- 条件付き依存: `if (action == "unblock")` → `this.download.unblock()`
- 条件付き依存: `if (action == "confirmBlock")` → `this.download.confirmBlock()`
- 参照: `console.error`, `this.download.error.becauseBlockedByReputationCheck`, `this.download.error.reputationCheckVerdict`

## unblockAndOpenDownload()
- 位置: L1057-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.download.unblock()`, `this.download.unblock().then()`, `this.downloadsCmd_open()`

## unblockAndSave()
- 位置: L1061-1063
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.download.unblock()`

## currentDefaultCommandName()
- 位置: L1070-1088
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.stateOfDownload()`
- 参照: `lazy.DownloadsCommon.DOWNLOAD_BLOCKED_CONTENT_ANALYSIS`, `lazy.DownloadsCommon.DOWNLOAD_BLOCKED_PARENTAL`, `lazy.DownloadsCommon.DOWNLOAD_CANCELED`, `lazy.DownloadsCommon.DOWNLOAD_DIRTY`, `lazy.DownloadsCommon.DOWNLOAD_FAILED`, `lazy.DownloadsCommon.DOWNLOAD_FINISHED`, `lazy.DownloadsCommon.DOWNLOAD_NOTSTARTED`, `lazy.DownloadsCommon.DOWNLOAD_PAUSED`, `this.download`

## isCommandEnabled()
- 位置: L1097-1144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.isCommandName()`, `lazy.DownloadIntegration.shouldViewDownloadInternally()`, `lazy.DownloadsCommon.getMimeInfo()`
- 参照: `lazy.DownloadsCommon.getMimeInfo(this.download)?.type`, `lazy.safeBrowsingAllowOverride`, `referrer.asciiSpec`, `target.exists`, `target.partFileExists`, `this.download`, `this.download.canceled`, `this.download.deleted`, `this.download.error`, `this.download.hasBlockedData`, `this.download.hasPartialData`, `this.download.source.referrerInfo?.originalReferrer`, `this.download.stopped`, `this.download.target.exists`

## doCommand()
- 位置: L1146-1153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.isCommandName()`, `aCommand.split()`
- 条件付き依存: `if (DownloadsViewUI.isCommandName(command))` → `this[command]()`

## onButton()
- 位置: L1155-1157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.doCommand()`
- 参照: `this.buttonCommandName`

## downloadsCmd_cancel()
- 位置: L1159-1166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.download .removePartialData()`, `this.download .removePartialData() .catch()`, `this.download .removePartialData() .catch(console.error) .finally()`, `this.download.cancel()`, `this.download.cancel().catch()`, `this.download.target.refresh()`
- 参照: `console.error`

## downloadsCmd_confirmBlock()
- 位置: L1168-1170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.download.confirmBlock()`, `this.download.confirmBlock().catch()`
- 参照: `console.error`

## downloadsCmd_open()
- 位置: L1172-1176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.openDownload()`
- 参照: `this.download`

## downloadsCmd_openReferrer()
- 位置: L1178-1182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.element.documentGlobal.openURL()`
- 参照: `this.download.source.referrerInfo.originalReferrer`

## downloadsCmd_pauseResume()
- 位置: L1184-1190
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.download.stopped)` → `this.download.start()`
- 条件付き依存: `if (!(this.download.stopped))` → `this.download.cancel()`
- 参照: `this.download.stopped`

## downloadsCmd_show()
- 位置: L1192-1195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.showDownloadedFile()`
- 参照: `lazy.FileUtils.File`, `this.download.target.path`

## downloadsCmd_retry()
- 位置: L1197-1212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.filename()`, `window.DownloadURL()`
- 条件付き依存: `if (this.download.start)` → `this.download.start().catch()`
- 条件付き依存: `if (this.download.start)` → `this.download.start()`
- 参照: `this.browserWindow`, `this.download.source.url`, `this.download.start`, `this.download.target.path`, `this.element.documentGlobal`, `window.document`

## downloadsCmd_delete()
- 位置: L1214-1219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cmd_delete()`

## cmd_delete()
- 位置: L1221-1223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.deleteDownload()`, `lazy.DownloadsCommon.deleteDownload(this.download).catch()`
- 参照: `console.error`, `this.download`

## downloadsCmd_deleteFile()
- 位置: async L1225-1231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.deleteDownloadFiles()`
- 参照: `DownloadsViewUI.clearHistoryOnDelete`, `this.download`

## downloadsCmd_openInSystemViewer()
- 位置: L1233-1239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.openDownload()`, `lazy.DownloadsCommon.openDownload(this.download, { useSystemDefault: true, }).catch()`
- 参照: `console.error`, `this.download`

## downloadsCmd_alwaysOpenInSystemViewer()
- 位置: L1241-1270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.getMimeInfo()`, `lazy.DownloadsCommon.openDownload()`, `lazy.DownloadsCommon.openDownload(this.download).catch()`, `lazy.handlerSvc.store()`
- 条件付き依存: `if (mimeInfo.preferredAction !== mimeInfo.useSystemDefault)` → `lazy.DownloadsCommon.log()`
- 条件付き依存: `if (!(mimeInfo.preferredAction !== mimeInfo.useSystemDefault))` → `lazy.DownloadsCommon.log()`
- 参照: `console.error`, `mimeInfo.alwaysAskBeforeHandling`, `mimeInfo.handleInternally`, `mimeInfo.preferredAction`, `mimeInfo.type`, `mimeInfo.useSystemDefault`, `this.download`

## downloadsCmd_alwaysOpenSimilarFiles()
- 位置: L1272-1291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.getMimeInfo()`
- 条件付き依存: `if (mimeInfo.preferredAction !== mimeInfo.useSystemDefault)` → `lazy.handlerSvc.store()`
- 条件付き依存: `if (mimeInfo.preferredAction !== mimeInfo.useSystemDefault)` → `lazy.DownloadsCommon.openDownload(this.download).catch()`
- 条件付き依存: `if (mimeInfo.preferredAction !== mimeInfo.useSystemDefault)` → `lazy.DownloadsCommon.openDownload()`
- 条件付き依存: `if (!(mimeInfo.preferredAction !== mimeInfo.useSystemDefault))` → `lazy.handlerSvc.store()`
- 参照: `console.error`, `mimeInfo.preferredAction`, `mimeInfo.saveToDisk`, `mimeInfo.useSystemDefault`, `this.download`
