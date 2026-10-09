# browser/components/reportbrokensite/ReportBrokenSite.sys.mjs

source: browser/components/reportbrokensite/ReportBrokenSite.sys.mjs
source-hash: df6efd09a80b47517a7a58a212bf81a8d5649278
lines: 1228

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ViewState.constructor()
- 位置: L27-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.#cache.set()`, `doc.documentGlobal.PanelMultiView.getViewNode()`
- 参照: `this.#detailsView`, `this.#doc`, `this.#mainView`, `this.#previewView`, `this.#reportSentView`

## ViewState.get()
- 位置: L49-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.#cache.get()`

## ViewState.mainPanelview()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#mainView`

## ViewState.detailsPanelview()
- 位置: L57-59
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#detailsView`

## ViewState.previewPanelview()
- 位置: L61-63
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#previewView`

## ViewState.reportSentPanelview()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#reportSentView`

## ViewState.#setCSSClass()
- 位置: L79-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `view.classList.toggle()`
- 参照: `this.#detailsView`, `this.#mainView`, `this.#previewView`

## ViewState.wrongTabInfo()
- 位置: L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#wrongTabInfo`

## ViewState.wrongTabInfo()
- 位置: L97-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `this.#setCSSClass()`
- 参照: `this.#wrongTabInfo`

## ViewState.screenshotsDisabled()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#screenshotsDisabled`

## ViewState.screenshotsDisabled()
- 位置: L112-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `this.#setCSSClass()`
- 参照: `this.#screenshotsDisabled`

## ViewState.screenshotOptOut()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#screenshotOptOut`

## ViewState.screenshotOptOut()
- 位置: L128-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `this.#setCSSClass()`
- 参照: `this.#screenshotOptOut`, `this.screenshotToggle.pressed`

## ViewState.noBlockedTrackers()
- 位置: L142-144
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#noBlockedTrackers`

## ViewState.noBlockedTrackers()
- 位置: L145-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `this.#setCSSClass()`
- 参照: `this.#noBlockedTrackers`

## ViewState.blockedTrackersOptOut()
- 位置: L158-160
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#blockedTrackersOptOut`

## ViewState.blockedTrackersOptOut()
- 位置: L161-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `this.#setCSSClass()`
- 参照: `this.#blockedTrackersOptOut`, `this.blockedTrackersToggle.pressed`

## ViewState.shouldSendBlockedTrackers()
- 位置: L168-174
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.blockedTrackersOptOut`, `this.blockedTrackersToggle.pressed`, `this.noBlockedTrackers`

## ViewState.url()
- 位置: L176-178
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#reportURL`

## ViewState.url()
- 位置: L182-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `this.updateProgressDisabledState()`
- 参照: `input.url`, `this.#isURLValid`, `this.#reportURL`, `this.currentTabURL.hostname`, `this.urlInputs`, `this.wrongTabInfo`, `url.hostname`

## ViewState.resetURLToCurrentTab()
- 位置: L197-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.fromURI()`
- 参照: `this.#doc.documentGlobal.gBrowser.selectedBrowser`, `this.currentTabURL`, `this.url`

## ViewState.focusInput()
- 位置: L202-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `input.addEventListener()`, `panelview.focusSelectedElement()`, `this.#doc.documentGlobal.PanelView.forNode()`
- 参照: `panelview.ignoreMouseMove`, `panelview.selectedElement`

## ViewState.focusFirstInvalidInputOnView()
- 位置: L216-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelview.querySelector()`, `target.closest()`
- 条件付き依存: `if (urlInput && !this.isURLValid)` → `this.focusInput()`
- 条件付き依存: `if (this.lastBlurredURLInputSelection)` → `urlInput.input.setSelectionRange()`
- 条件付き依存: `if (description && !this.isDescriptionValid)` → `this.focusInput()`
- 参照: `this.isDescriptionValid`, `this.isURLValid`, `this.lastBlurredURLInputSelection`, `urlInput.input`

## ViewState.updateProgressDisabledState()
- 位置: L233-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `btn.toggleAttribute()`, `this.#mainView.querySelectorAll()`, `view.querySelectorAll()`
- 参照: `this.#detailsView`, `this.#previewView`

## ViewState.descriptionTextArea()
- 位置: L245-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`

## ViewState.description()
- 位置: L251-253
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.descriptionTextArea.value`

## ViewState.description()
- 位置: L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value.trim()`
- 参照: `this.descriptionTextArea.value`

## ViewState.blockedTrackersToggle()
- 位置: L259-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`

## ViewState.screenshotToggle()
- 位置: L265-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`

## ViewState.screenshot()
- 位置: L271-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`, `this.#setCSSClass()`
- 参照: `this.#detailsView.querySelector( "#report-broken-site-popup-screenshot" ).src`

## ViewState.detailsViewTitle()
- 位置: L278-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.setAttribute()`

## ViewState.detailsViewInstructions()
- 位置: L282-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`

## ViewState.detailsViewDescriptionError()
- 位置: L288-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`

## ViewState.reset()
- 位置: L294-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetURLToCurrentTab()`
- 参照: `this.blockedTrackersOptOut`, `this.cachedPreviewData`, `this.currentTabWebcompatDetailsPromise`, `this.description`, `this.lastBlurredURLInputSelection`, `this.noBlockedTrackers`, `this.reason`, `this.screenshot`, `this.screenshotOptOut`, `this.wrongTabInfo`

## ViewState.isURLValid()
- 位置: L312-314
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isURLValid`

## ViewState.descriptionIsOptional()
- 位置: L316-318
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.reason`

## ViewState.isDescriptionValid()
- 位置: L320-326
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `value.trim()`
- 参照: `this.descriptionIsOptional`, `this.descriptionTextArea`, `value.trim().length`

## ViewState.createElement()
- 位置: L328-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#doc.createElement()`

## ViewState.learnMoreLink()
- 位置: L332-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#mainView.querySelector()`

## ViewState.sendMoreInfoButton()
- 位置: L338-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`

## ViewState.reasonButtons()
- 位置: L344-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#mainView.querySelectorAll()`

## ViewState.urlInputs()
- 位置: L348-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelectorAll()`, `this.#mainView.querySelectorAll()`

## ViewState.cancelButtons()
- 位置: L355-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelectorAll()`, `this.#previewView.querySelectorAll()`

## ViewState.sendButtons()
- 位置: L362-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`, `this.#previewView.querySelector()`

## ViewState.mainView()
- 位置: L371-373
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#mainView`

## ViewState.reportSentView()
- 位置: L375-377
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#reportSentView`

## ViewState.okayButton()
- 位置: L379-383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#reportSentView.querySelector()`

## ViewState.previewBox()
- 位置: L385-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#previewView.querySelector()`

## ViewState.previewButton()
- 位置: L391-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detailsView.querySelector()`

## ReportBrokenSite.enabled()
- 位置: L420-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `Services.prefs.getBoolPref()`
- 参照: `ReportBrokenSite.DATAREPORTING_PREF`, `ReportBrokenSite.REPORTER_ENABLED_PREF`
- XPCOM: `Services.policies` / `Services.prefs`

## ReportBrokenSite.canReportURI()
- 位置: L428-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `uri.schemeIs()`

## ReportBrokenSite.#recordGleanEvent()
- 位置: L432-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webcompatreporting[name].record()`
- 参照: `Glean.webcompatreporting`

## ReportBrokenSite.updateParentMenu()
- 位置: L436-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.addEventListener()`, `tabbrowser.addTabsProgressListener()`, `tabbrowser.removeTabsProgressListener()`, `this.enableOrDisableMenuitems()`
- 参照: `event.target.documentGlobal.gBrowser`, `tabbrowser.selectedBrowser`

## ReportBrokenSite.constructor()
- 位置: L459-463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Services.prefs.addObserver()`
- 参照: `this.#OBSERVED_PREFS`
- XPCOM: `Services.prefs`

## ReportBrokenSite.#onNewWindow()
- 位置: L467-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `this.#windows.add()`, `this.observe()`
- 条件付き依存: `if (!this.#windows.size)` → `Services.prefs.addObserver()`
- 参照: `this.#OBSERVED_PREFS`, `this.#windows.size`
- XPCOM: `Services.prefs`

## ReportBrokenSite.#onWindowClosed()
- 位置: L477-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windows.delete()`
- 条件付き依存: `if (!this.#windows.size)` → `Object.keys()`
- 条件付き依存: `if (!this.#windows.size)` → `Services.prefs.removeObserver()`
- 参照: `this.#OBSERVED_PREFS`, `this.#windows.size`
- XPCOM: `Services.prefs`

## ReportBrokenSite.observe()
- 位置: L486-493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `ViewState.get()`, `checkFn()`
- 参照: `this.#OBSERVED_PREFS`, `this.#windows`
- XPCOM: `Services.prefs`

## ReportBrokenSite.onScreenshotsPrefChanged()
- 位置: L495-497
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `state.screenshotsDisabled`

## ReportBrokenSite.onShowSendMoreInfoPrefChanged()
- 位置: L499-516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if ( Services.prefs.prefHasUserValue(ReportBrokenSite.SHOW_SEND_MORE_INFO_PREF) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!( Services.prefs.prefHasUserValue(ReportBrokenSite.SHOW_SEND_MORE_INFO_PREF) ))` → `["release", "esr"].includes()`
- 参照: `AppConstants.MOZ_UPDATE_CHANNEL`, `ReportBrokenSite.SHOW_SEND_MORE_INFO_PREF`, `state.sendMoreInfoButton.hidden`
- XPCOM: `Services.prefs`

## ReportBrokenSite.uninit()
- 位置: L518-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onWindowClosed()`

## ReportBrokenSite.#loadCustomElements()
- 位置: L535-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ReportBrokenSite.#hasCustomElements.add()`, `ReportBrokenSite.#hasCustomElements.has()`, `Services.scriptloader.loadSubScriptWithOptions()`
- 参照: `ReportBrokenSite.REGISTER_CUSTOM_ELEMENTS_SCRIPT`
- XPCOM: `Services.scriptloader`

## ReportBrokenSite.init()
- 位置: L551-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `ReportBrokenSite.#loadCustomElements()`, `ViewState.get()`, `btn.addEventListener()`, `document .getElementById()`, `document .getElementById(id) .addEventListener()`, `document.addEventListener()`, `document.l10n .formatMessages()`, `document.l10n.setAttributes()`, `input.addEventListener()`, `sendButton.addEventListener()`, `state.blockedTrackersToggle.addEventListener()`, `state.descriptionTextArea.addEventListener()`, `state.detailsPanelview .querySelector()`, `state.detailsPanelview .querySelector(".subviewbutton-back") .addEventListener()`, `state.detailsPanelview.addEventListener()`, `state.learnMoreLink.addEventListener()`, `state.mainPanelview.addEventListener()`, `state.okayButton.addEventListener()`, `state.previewButton.addEventListener()`, `state.reportSentPanelview.addEventListener()`, `state.screenshotToggle.addEventListener()`, `state.sendMoreInfoButton.addEventListener()`, `state.updateProgressDisabledState()`, `target.documentGlobal.CustomizableUI.hidePanelForNode()`, `this.#cancelButtonHandler()`, `this.#focusFirstInvalidInputOnView()`, `this.#learnMoreLinkHandler()`, `this.#onDetailsViewShowing()`, `this.#onMainViewShowing()`, `this.#onNewWindow()`, `this.#onReportBrokenSiteHandler()`, `this.#onReportSentViewShown()`, `this.#onURLEdited()`, `this.#onURLInputChanged()`, `this.#onURLInputReset()`, `this.#previewButtonHandler()`, `this.#reasonButtonHandler()`, `this.#resetURLInputsOrCloseOnEscapePress()`, `this.#saveURLInputSelectionRange()`, `this.#sendButtonHandler()`, `this.#sendMoreInfoButtonHandler()`, `this.updateDescriptionValidity()`, `this.updateParentMenu()`, `win.document .getElementById()`, `win.document .getElementById("cmd_reportBrokenSite") .addEventListener()`
- 参照: `result[0].value`, `state.blockedTrackersOptOut`, `state.cancelButtons`, `state.detailsViewDescriptionError`, `state.reasonButtons`, `state.screenshotOptOut`, `state.sendButtons`, `state.urlInputs`, `target.pressed`, `this.#descriptionErrorTextPromise`

## ReportBrokenSite.enableOrDisableMenuitems()
- 位置: L676-709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `cmd.toggleAttribute()`, `document.getElementById()`, `this.canReportURI()`
- 条件付き依存: `if (canReportUrl)` → `cmd.removeAttribute()`
- 条件付き依存: `if (canReportUrl)` → `prot?.removeAttribute()`
- 条件付き依存: `if (!(canReportUrl))` → `cmd.setAttribute()`
- 条件付き依存: `if (!(canReportUrl))` → `prot?.setAttribute()`
- 参照: `mainmenuItem.disabled`, `mainmenuItem.hidden`, `selectedbrowser.currentURI`, `selectedbrowser.documentGlobal`
- XPCOM: `Services.policies`

## ReportBrokenSite.updateDescriptionValidity()
- 位置: L711-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `descriptionTextArea.setCustomValidity()`, `state.updateProgressDisabledState()`, `this.#descriptionErrorTextPromise.then()`
- 参照: `target.documentGlobal.document`

## ReportBrokenSite.#focusFirstInvalidInputOnView()
- 位置: L722-725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `state.focusFirstInvalidInputOnView()`
- 参照: `event.target.documentGlobal.document`

## ReportBrokenSite.#onReportBrokenSiteHandler()
- 位置: L727-748
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.enabled)` → `this.open()`
- 条件付き依存: `if (!(this.enabled))` → `ViewState.get()`
- 条件付き依存: `if (!(this.enabled))` → `state.resetURLToCurrentTab()`
- 条件付き依存: `if (!(this.enabled))` → `this.promiseWebCompatInfo()`
- 条件付き依存: `if (!(this.enabled))` → `this.#openWebCompatTab(gBrowser) .catch()`
- 条件付き依存: `if (!(this.enabled))` → `this.#openWebCompatTab()`
- 条件付き依存: `if (!(this.enabled))` → `console.error()`
- 条件付き依存: `if (!(this.enabled))` → `state.reset()`
- 参照: `event.target`, `this.enabled`

## ReportBrokenSite.handleParentMenuButtonCommand()
- 位置: L750-755
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onReportBrokenSiteHandler()`

## ReportBrokenSite.#onURLInputReset()
- 位置: L757-762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `event.preventDefault()`
- 参照: `event.target.documentGlobal`, `state.currentTabURL`, `state.url`

## ReportBrokenSite.#onURLEdited()
- 位置: L764-767
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`
- 参照: `state.url`, `target.documentGlobal.document`, `target.input.value`

## ReportBrokenSite.#onURLInputChanged()
- 位置: L769-772
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`
- 参照: `detail.newValue`, `state.url`, `target.documentGlobal.document`

## ReportBrokenSite.#saveURLInputSelectionRange()
- 位置: L774-780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`
- 参照: `state.lastBlurredURLInputSelection`, `target.documentGlobal.document`, `target.input.selectionEnd`, `target.input.selectionStart`

## ReportBrokenSite.#resetURLInputsOrCloseOnEscapePress()
- 位置: L782-797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `activeElement.requestBlur()`, `event.stopImmediatePropagation()`
- 参照: `activeElement?.nodeName`, `event.key`, `event.target.documentGlobal`, `state.currentTabURL`, `state.url`

## ReportBrokenSite.#reasonButtonHandler()
- 位置: async L799-841
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `multiview.showSubView()`, `state.detailsViewInstructions.setAttribute()`, `state.focusFirstInvalidInputOnView()`, `target.closest()`, `target.id?.replace()`, `target.matches()`
- 条件付き依存: `if (target.matches("#report-broken-site-popup-reason-deceptive"))` → `target.documentGlobal.CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (target.matches("#report-broken-site-popup-reason-deceptive"))` → `URL.parse()`
- 条件付き依存: `if (target.matches("#report-broken-site-popup-reason-deceptive"))` → `lazy.SafeBrowsing.getReportURL()`
- 条件付き依存: `if (target.matches("#report-broken-site-popup-reason-deceptive"))` → `target.documentGlobal.gBrowser.addTab()`
- 条件付き依存: `if (target.matches("#report-broken-site-popup-reason-deceptive"))` → `Services.scriptSecurityManager.createNullPrincipal()`
- 参照: `ReportBrokenSite.DETAILS_PANELVIEW_ID`, `state.descriptionIsOptional`, `state.detailsViewTitle`, `state.reason`, `state.url`, `target.documentGlobal.document`, `target.textContent`, `url.hash`, `url.href`, `url.search`
- XPCOM: `Services.scriptSecurityManager`

## ReportBrokenSite.#sendButtonHandler()
- 位置: async L843-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `multiview.showSubView()`, `state.focusFirstInvalidInputOnView()`, `state.reset()`, `target.closest()`, `this.#recordGleanEvent()`, `this.#sendReportAsGleanPing()`
- 参照: `gBrowser.selectedBrowser`, `state.shouldSendBlockedTrackers`, `target.documentGlobal.document`

## ReportBrokenSite.#learnMoreLinkHandler()
- 位置: L864-869
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.documentGlobal.CustomizableUI.hidePanelForNode()`, `target.documentGlobal.requestAnimationFrame()`, `this.#recordGleanEvent()`

## ReportBrokenSite.#sendMoreInfoButtonHandler()
- 位置: async L871-878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `event.target.documentGlobal.CustomizableUI.hidePanelForNode()`, `this.#openWebCompatTab()`, `this.#recordGleanEvent()`
- 参照: `target.documentGlobal.gBrowser`

## ReportBrokenSite.#previewButtonHandler()
- 位置: L880-911
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `ViewState.get()`, `multiview.showSubView()`, `previewBox.querySelector()`, `state.currentTabWebcompatDetailsPromise ?.catch()`, `state.currentTabWebcompatDetailsPromise ?.catch(_ => {}) .then()`, `state.focusFirstInvalidInputOnView()`, `target.closest()`, `this.#recordGleanEvent()`, `this.generatePreviewMarkup()`
- 参照: `ReportBrokenSite.PREVIEW_PANELVIEW_ID`, `previewBox.querySelector(".preview-description > .value").innerText`, `previewBox.querySelector(".preview-reason > .value").innerText`, `previewBox.querySelector(".preview-url > .value").innerText`, `state.cachedPreviewData`, `state.cachedPreviewData.basic.description`, `state.cachedPreviewData.basic.reason`, `state.cachedPreviewData.basic.url`, `target.documentGlobal.document`

## ReportBrokenSite.#cancelButtonHandler()
- 位置: L913-917
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `state.reset()`, `target.documentGlobal.CustomizableUI.hidePanelForNode()`
- 参照: `target.documentGlobal.document`

## ReportBrokenSite.#onMainViewShowing()
- 位置: async L919-951
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `state.updateProgressDisabledState()`, `target.closest()`, `this.#recordGleanEvent()`
- 条件付き依存: `if (!state.isURLValid)` → `state.reset()`
- 条件付き依存: `if (url != state.currentTabURL)` → `state.reset()`
- 条件付き依存: `if (!state.currentTabURL)` → `state.resetURLToCurrentTab()`
- 条件付き依存: `if (didReset || !state.currentTabWebcompatDetailsPromise)` → `this.promiseWebCompatInfo()`
- 参照: `selectedBrowser.currentURI.spec`, `selectedBrowser.documentGlobal.document`, `state.currentTabURL`, `state.currentTabWebcompatDetailsPromise`, `state.isURLValid`, `target.closest("panelmultiview")?.id`, `target.documentGlobal.gBrowser`

## ReportBrokenSite.#onDetailsViewShowing()
- 位置: L953-965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `state.updateProgressDisabledState()`, `target.closest()`, `this.updateDescriptionValidity()`
- 条件付き依存: `if (!this.updateDescriptionValidity(event))` → `panelview.addEventListener()`
- 条件付き依存: `if (!this.updateDescriptionValidity(event))` → `state.focusInput()`
- 参照: `state.descriptionTextArea`, `target.documentGlobal.document`

## ReportBrokenSite.#onReportSentViewShown()
- 位置: L967-975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ViewState.get()`, `documentGlobal.PanelView.forNode()`, `panelview.focusSelectedElement()`
- 参照: `documentGlobal.document`, `panelview.selectedElement`, `state.okayButton`, `state.reportSentPanelview`

## ReportBrokenSite.promiseWebCompatInfo()
- 位置: L977-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor .getBrokenSiteReport()`, `actor .getBrokenSiteReport() .then()`, `console.error()`, `this.#getActor()`
- 参照: `info.tabInfo?.screenshot?.value`, `info?.antitracking?.blockedOrigins?.value?.length`, `info?.tabInfo?.favicon?.value`, `input.favicon`, `state.currentTabWebcompatDetailsPromise`, `state.noBlockedTrackers`, `state.screenshot`, `state.urlInputs`

## ReportBrokenSite.cachePreviewData()
- 位置: L1002-1029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 条件付き依存: `if (brokenSiteReportData)` → `Object.entries()`
- 条件付き依存: `if (brokenSiteReportData)` → `Object.fromEntries()`
- 条件付き依存: `if (brokenSiteReportData)` → `Object.entries(values) .filter(([_, { doNotPreview }]) => !doNotPreview) .map()`
- 条件付き依存: `if (brokenSiteReportData)` → `Object.entries(values) .filter()`
- 参照: `brokenSiteReportData.tabInfo.screenshot`, `previewData.basic.screenshot`, `state.cachedPreviewData`

## ReportBrokenSite.generatePreviewMarkup()
- 位置: L1031-1087
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `details.appendChild()`, `div.append()`, `div.classList.add()`, `info.appendChild()`, `preview.appendChild()`, `preview.querySelector()`, `state.createElement()`, `this.cachePreviewData()`, `value.startsWith()`
- 条件付き依存: `if (k == "isTabSpecific")` → `details.classList.add()`
- 条件付き依存: `if (isTabSpecific)` → `div.classList.add()`
- 条件付き依存: `if (typeof value === "string" && value.startsWith("data:image/"))` → `state.createElement()`
- 条件付き依存: `if (typeof value === "string" && value.startsWith("data:image/"))` → `span_value.appendChild()`
- 条件付き依存: `if (!(typeof value === "string" && value.startsWith("data:image/")))` → `JSON.stringify(value)?.replace()`
- 条件付き依存: `if (!(typeof value === "string" && value.startsWith("data:image/")))` → `JSON.stringify()`
- 条件付き依存: `if (first)` → `first.setAttribute()`
- 参照: `details.className`, `img.src`, `info.className`, `preview.innerHTML`, `span_name.innerText`, `span_value.className`, `span_value.innerText`, `state.cachedPreviewData`, `state.previewBox`, `summary.innerText`

## ReportBrokenSite.#getActor()
- 位置: L1089-1093
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.browsingContext.currentWindowGlobal.getActor()`

## ReportBrokenSite.#loadTab()
- 位置: async L1095-1116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabbrowser.addTab()`, `tabbrowser.addTabsProgressListener()`, `tabbrowser.getBrowserForTab()`

## ReportBrokenSite.onLocationChange()
- 位置: L1103-1112
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( browser == expectedBrowser && uri.spec == url && webProgress.isTopLevel )` → `resolve()`
- 条件付き依存: `if ( browser == expectedBrowser && uri.spec == url && webProgress.isTopLevel )` → `tabbrowser.removeTabsProgressListener()`
- 参照: `uri.spec`, `webProgress.isTopLevel`

## ReportBrokenSite.#openWebCompatTab()
- 位置: async L1118-1165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `Services.scriptSecurityManager.createNullPrincipal()`, `ViewState.get()`, `actor .sendQuery()`, `console.error()`, `this.#getActor()`, `this.#loadTab()`
- 参照: `ReportBrokenSite.NEW_REPORT_ENDPOINT_PREF`, `ReportBrokenSite.WEBCOMPAT_REPORTER_CONFIG`, `screenshotToggle.pressed`, `tab.linkedBrowser`, `tabbrowser.selectedBrowser`, `tabbrowser.selectedBrowser.documentGlobal`, `webcompatInfo.tabInfo.screenshot.value`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## ReportBrokenSite.#sendReportAsGleanPing()
- 位置: L1167-1190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentTabWebcompatDetailsPromise .catch()`, `currentTabWebcompatDetailsPromise .catch(() => undefined) .then()`, `this.#getActor()`, `this.#getActor(browser).sendBrokenSiteReport()`

## ReportBrokenSite.open()
- 位置: L1192-1226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `appMenuPopup?.hidePopup()`, `document .getElementById()`, `document .getElementById("protections-popup-multiView") .showSubView()`, `document.getElementById()`, `documentGlobal.PanelUI.showSubView()`
- 参照: `ReportBrokenSite.MAIN_PANELVIEW_ID`, `documentGlobal.PanelUI.menuButton`, `event.sourceEvent`, `target.documentGlobal.gBrowser`, `target.id`
