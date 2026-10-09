# browser/components/genai/LinkPreview.sys.mjs

source: browser/components/genai/LinkPreview.sys.mjs
source-hash: deaead5da0781ec3fe74cfdc3d37d6db38290858
lines: 1242

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/ml-utils;1"].getService()`, `Cc["@mozilla.org/ml-utils;1"].getService(Ci.nsIMLUtils).canUseLlamaCpp()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `LinkPreview.onCollapsedPref()`, `LinkPreview.onEnabledPref()`, `LinkPreview.onLongPressPrefChange()`, `LinkPreview.onOptinPref()`, `LinkPreview.onShiftAltPrefChange()`, `LinkPreview.onShiftPrefChange()`, `Object.freeze()`, `Object.setPrototypeOf()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `rawValue.split()`, `rawValue.split(",").map()`

## id()
- 位置: L156-158
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.LinkPreviewModel.id`

## hasDistinctEnabledState()
- 位置: L160-165
- 役割: (未記入)
- 触るとき: (未記入)

## enable()
- 位置: async L167-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## block()
- 位置: async L172-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `console.error()`, `this.uninstallModel()`
- XPCOM: `Services.prefs`

## makeAvailable()
- 位置: async L185-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `Services.prefs.setBoolPref()`, `Services.prefs.setStringPref()`, `console.error()`, `this.uninstallModel()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(pref))` → `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## isEnabled()
- 位置: L219-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## isAllowed()
- 位置: L232-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isLocaleSupported()`, `this._isRegionSupported()`

## canRunOnDevice()
- 位置: L236-239
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.canUseLlamaCpp`

## isBlocked()
- 位置: L241-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## isManagedByPolicy()
- 位置: L245-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`, `this._isDisabledByPolicy()`
- XPCOM: `Services.prefs`

## _getTabContextValue()
- 位置: L261-268
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `uri.filePath`, `uri?.scheme`, `win.gBrowser.selectedBrowser.currentURI`

## canShowKeyPoints()
- 位置: L270-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isDisabledByPolicy()`, `this._isLocaleSupported()`, `this._isRegionSupported()`
- 参照: `this.canRunOnDevice`

## canShowLegacy()
- 位置: L279-281
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `LABS_STATE.NOT_ENROLLED`, `lazy.labs`

## canShowPreferences()
- 位置: L283-286
- 役割: (未記入)
- 触るとき: (未記入)

## showOnboarding()
- 位置: L288-290
- 役割: (未記入)
- 触るとき: (未記入)

## shouldShowContextMenu()
- 位置: L292-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isRegionSupported()`
- 参照: `lazy.enabled`, `nsContextMenu.onLink`, `nsContextMenu.onMailtoLink`, `nsContextMenu.onMozExtLink`, `nsContextMenu.onPlainTextLink`, `nsContextMenu.onTelLink`

## onShiftPrefChange()
- 位置: L313-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.prefChanged.record()`, `this._updateShortcutMetric()`

## onShiftAltPrefChange()
- 位置: L323-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.prefChanged.record()`, `this._updateShortcutMetric()`

## onLongPressPrefChange()
- 位置: L336-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.prefChanged.record()`, `this._updateShortcutMetric()`

## onEnabledPref()
- 位置: L350-368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.enabled.set()`, `Glean.genaiLinkpreview.prefChanged.record()`, `this._windowStates.keys()`, `this.handleNimbusPrefs()`, `this[method]()`
- 条件付き依存: `if (enabled && lazy.prefetchOnEnable && this.canShowKeyPoints)` → `this.generateKeyPoints()`
- 参照: `lazy.prefetchOnEnable`, `this.canShowKeyPoints`

## updateCardProperty()
- 位置: L376-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.querySelector()`, `win.document.getElementById()`
- 参照: `this._windowStates`, `this.linkPreviewPanelId`

## onOptinPref()
- 位置: L396-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.aiOptin.set()`, `Glean.genaiLinkpreview.cardAiConsent.record()`, `Glean.genaiLinkpreview.prefChanged.record()`, `this.updateCardProperty()`

## onCollapsedPref()
- 位置: L414-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.keyPoints.set()`, `Glean.genaiLinkpreview.keyPointsToggle.record()`, `this.updateCardProperty()`
- 条件付き依存: `if (collapsed && this.progress >= 0)` → `this.updateCardProperty()`
- 参照: `this.progress`

## handleNimbusPrefs()
- 位置: L431-481
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries( lazy.NimbusFeatures[featureId].getVariable("prefs") ?? [] ).forEach()`, `lazy.NimbusFeatures.linkPreviews.getVariable()`, `lazy.NimbusFeatures[featureId].getEnrollmentMetadata()`, `lazy.NimbusFeatures[featureId].getVariable()`, `lazy.NimbusFeatures[featureId].onUpdate()`, `setPref()`
- 条件付き依存: `if ( lazy.NimbusFeatures.linkPreviews.getVariable("enabled") && lazy.labs == LABS_STATE.NOT_ENROLLED )` → `Services.prefs.setIntPref()`
- 条件付き依存: `if ( lazy.NimbusFeatures.linkPreviews.getVariable("enabled") && lazy.labs == LABS_STATE.NOT_ENROLLED )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!lazy.enabled && lazy.labs == LABS_STATE.ENROLLED)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!lazy.enabled && lazy.labs == LABS_STATE.ENROLLED)` → `Services.prefs.setBoolPref()`
- 参照: `LABS_STATE.ENROLLED`, `LABS_STATE.NOT_ENROLLED`, `LABS_STATE.ROLLOUT_ENDED`, `enrollment.branch`, `enrollment.slug`, `lazy.NimbusFeatures`, `lazy.enabled`, `lazy.labs`, `lazy.nimbus`, `this._nimbusRegistered`
- XPCOM: `Services.prefs`

## setPref()
- 位置: L469-475
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (anyBranch || branch == "default")` → `lazy.PrefUtils.setPref()`

## init()
- 位置: L488-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.aiOptin.set()`, `Glean.genaiLinkpreview.enabled.set()`, `Glean.genaiLinkpreview.keyPoints.set()`, `this._updateShortcutMetric()`, `this._windowStates.set()`, `this.handleNimbusPrefs()`, `win.customElements.get()`
- 条件付き依存: `if (!win.customElements.get("link-preview-card"))` → `win.ChromeUtils.importESModule()`
- 条件付き依存: `if (!win.customElements.get("link-preview-card-onboarding"))` → `win.ChromeUtils.importESModule()`
- 条件付き依存: `if (lazy.enabled)` → `this._addEventListeners()`
- 参照: `lazy.collapsed`, `lazy.enabled`, `lazy.longPress`, `lazy.optin`, `lazy.shift`, `lazy.shiftAlt`

## teardown()
- 位置: L529-541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `doc.getElementById(this.linkPreviewPanelId)?.remove()`, `this._windowStates.delete()`
- 条件付き依存: `if (lazy.enabled)` → `this._removeEventListeners()`
- 参照: `lazy.enabled`, `this.linkPreviewPanelId`, `win.document`

## _addEventListeners()
- 位置: L548-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.addEventListener()`

## _removeEventListeners()
- 位置: L560-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cancelLongPress()`, `win.removeEventListener()`

## handleEvent()
- 位置: L576-593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onKeyEvent()`, `this._onLinkPreview()`, `this._onPressEvent()`
- 参照: `event.type`

## _onKeyEvent()
- 位置: L600-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["Enter", "Tab"].includes()`, `this._maybeLinkPreview()`
- 条件付き依存: `if (event.key.length == 1 || ["Enter", "Tab"].includes(event.key))` → `Date.now()`
- 参照: `event.altKey`, `event.ctrlKey`, `event.currentTarget`, `event.key`, `event.key.length`, `event.metaKey`, `event.shiftKey`, `lazy.shift`, `lazy.shiftAlt`, `this.keyboardComboActive`, `this.recentTyping`

## _onLinkPreview()
- 位置: L633-651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this._windowStates.get()`, `url.endsWith()`, `url.startsWith()`
- 条件付き依存: `if (this.keyboardComboActive)` → `this._maybeLinkPreview()`
- 条件付き依存: `if (this.showOnboarding)` → `this._maybeOnboard()`
- 参照: `event.currentTarget`, `event.detail.url`, `stateObject.overLink`, `this.keyboardComboActive`, `this.overLinkTime`, `this.showOnboarding`

## _maybeOnboard()
- 位置: L653-683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.document.getElementById()`, `win.setTimeout()`
- 条件付き依存: `if (stateObject.hoverTimerId)` → `win.clearTimeout()`
- 条件付き依存: `if (stateObject.overLink === url)` → `this.renderOnboardingPanel()`
- 参照: `lazy.onboardingHoverLinkMs`, `panel.state`, `stateObject.hoverTimerId`, `stateObject.lastHoveredUrl`, `stateObject.overLink`, `this.linkPreviewPanelId`

## renderOnboardingPanel()
- 位置: async L692-735
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.genaiLinkpreview.onboardingCard.record()`, `Services.prefs.setStringPref()`, `doc.createElement()`, `onboardingCard.addEventListener()`, `panel.append()`, `panel.hidePopup()`, `panel.openPopupNearMouse()`, `this.initOrResetPreviewPanel()`, `this.renderLinkPreviewPanel()`
- 参照: `lazy.onboardingTimes`, `onboardingCard.onboardingType`, `onboardingCard.style.width`, `panel.onboardingType`, `this.showOnboarding`, `win.document`
- XPCOM: `Services.prefs`

## initOrResetPreviewPanel()
- 位置: L745-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`
- 条件付き依存: `if (panel.cardType == "linkpreview")` → `panel.hidePopup()`
- 条件付き依存: `if (panel)` → `panel.replaceChildren()`
- 条件付き依存: `if (!(panel))` → `doc .getElementById("mainPopupSet") .appendChild()`
- 条件付き依存: `if (!(panel))` → `doc .getElementById()`
- 条件付き依存: `if (!(panel))` → `doc.createXULElement()`
- 条件付き依存: `if (!(panel))` → `panel.setAttribute()`
- 条件付き依存: `if (!(panel))` → `panel.style.setProperty()`
- 条件付き依存: `if (!(panel))` → `panel.addEventListener()`
- 条件付き依存: `if (panel.cardType === "onboarding")` → `Glean.genaiLinkpreview.onboardingCard.record()`
- 条件付き依存: `if (panel.cardType === "linkpreview")` → `this._getTabContextValue()`
- 条件付き依存: `if (panel.cardType === "linkpreview")` → `Glean.genaiLinkpreview.cardClose.record()`
- 条件付き依存: `if (panel.cardType === "linkpreview")` → `Date.now()`
- 参照: `panel.cardType`, `panel.className`, `panel.id`, `panel.onboardingType`, `panel.openPopupNearMouse`, `panel.openTime`, `panel.style.width`, `this.linkPreviewPanelId`, `win.document`

## openPopup()
- 位置: L772-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `panel.openPopup()`
- 参照: `doc.documentElement`, `panel.openTime`, `win.MousePosTracker`

## _onPressEvent()
- 位置: L806-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._windowStates.get()`
- 条件付き依存: `if ( event.type == "mousedown" && !event.button && event.buttons & 1 && !event.altKey && !event.ctrlKey && !event.metaKey && !event.shiftKey && stateObject.overL...)` → `win.addEventListener()`
- 条件付き依存: `if ( event.type == "mousedown" && !event.button && event.buttons & 1 && !event.altKey && !event.ctrlKey && !event.metaKey && !event.shiftKey && stateObject.overL...)` → `win.setTimeout()`
- 条件付き依存: `if ( event.type == "mousedown" && !event.button && event.buttons & 1 && !event.altKey && !event.ctrlKey && !event.metaKey && !event.shiftKey && stateObject.overL...)` → `this.cancelLongPress()`
- 条件付き依存: `if ( event.type == "mousedown" && !event.button && event.buttons & 1 && !event.altKey && !event.ctrlKey && !event.metaKey && !event.shiftKey && stateObject.overL...)` → `this.renderLinkPreviewPanel()`
- 条件付き依存: `if (!( event.type == "mousedown" && !event.button && event.buttons & 1 && !event.altKey && !event.ctrlKey && !event.metaKey && !event.shiftKey && stateObject.overL...))` → `this.cancelLongPress()`
- 参照: `event.altKey`, `event.button`, `event.buttons`, `event.ctrlKey`, `event.currentTarget`, `event.metaKey`, `event.shiftKey`, `event.type`, `lazy.longPress`, `lazy.longPressMs`, `stateObject.overLink`, `this.cancelLongPress`

## this.cancelLongPress()
- 位置: L838-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.clearTimeout()`, `win.removeEventListener()`
- 参照: `this.cancelLongPress`

## _isRegionSupported()
- 位置: L854-861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `disallowedRegions.includes()`, `lazy.Region.home?.toUpperCase()`, `lazy.noKeyPointsRegions .split()`, `lazy.noKeyPointsRegions .split(",") .map()`, `region.trim()`, `region.trim().toUpperCase()`

## _isLocaleSupported()
- 位置: L868-875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.locale.appLocaleAsBCP47.toLowerCase()`, `lazy.supportedLocales .split()`, `lazy.supportedLocales .split(",") .map()`, `locale.trim()`, `locale.trim().toLowerCase()`, `supportedLocales.some()`, `userLocale.startsWith()`
- XPCOM: `Services.locale`

## _isDisabledByPolicy()
- 位置: L882-886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- 参照: `lazy.optin`
- XPCOM: `Services.prefs`

## createOGCard()
- 位置: L899-942
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `doc.createElement()`, `lazy.allowedLanguages .split()`, `lazy.allowedLanguages .split(",") .includes()`, `ogCard.addEventListener()`, `this._abortController?.abort()`, `updateProgress()`
- 条件付き依存: `if ( this.canShowKeyPoints && pageData.article.textContent && pageData.article.detectedLanguage && (!lazy.allowedLanguages || lazy.allowedLanguages .split(",") ....)` → `this.generateKeyPoints()`
- 参照: `lazy.allowedLanguages`, `lazy.collapsed`, `lazy.optin`, `ogCard.canShowKeyPoints`, `ogCard.collapsed`, `ogCard.isMissingDataErrorState`, `ogCard.optin`, `ogCard.pageData`, `ogCard.style.width`, `pageData.article.detectedLanguage`, `pageData.article.textContent`, `this.canShowKeyPoints`
- XPCOM: `Services.prefs`

## updateProgress()
- 位置: L914-923
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.progress >= 0)` → `doc.documentGlobal.setTimeout()`
- 条件付き依存: `if (this.progress >= 0)` → `updateProgress()`
- 参照: `ogCard.isConnected`, `ogCard.progress`, `this.progress`

## generateKeyPoints()
- 位置: async L950-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.genaiLinkpreview.generate.record()`, `Promise.allSettled()`, `Promise.withResolvers()`, `lazy.LinkPreviewModel.generateTextAI()`, `resolve()`
- 条件付き依存: `if (!ogCard.isConnected)` → `resolve()`
- 条件付き依存: `if (!ogCard.isConnected)` → `Glean.genaiLinkpreview.generate.record()`
- 参照: `lazy.collapsed`, `lazy.optin`, `ogCard.generating`, `ogCard.isConnected`, `ogCard.keyPoints.length`, `ogCard.pageData?.article.textContent`, `this._abortController`, `this._abortController.signal`, `this.lastRequest`

## addKeyPoint()
- 位置: L961-961
- 役割: (未記入)
- 触るとき: (未記入)

## onDownload()
- 位置: L991-998
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `isNaN()`
- 参照: `ogCard.progress`, `this.progress`

## onError()
- 位置: L999-1013
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `error.message?.includes()`
- 条件付き依存: `if ( error.name === "AbortError" || error.message?.includes("AbortError") )` → `Promise.resolve()`
- 参照: `error.name`, `ogCard.generationError`, `this.lastRequest`

## onText()
- 位置: L1014-1019
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `ogCard.addKeyPoint()`
- 参照: `ogCard.showWait`

## _handleKeyPointsGenerationEvent()
- 位置: L1044-1050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.generateKeyPoints()`
- 参照: `ogCard.isGenerationErrorState`, `ogCard.isMissingDataErrorState`

## renderLinkPreviewPanel()
- 位置: async L1059-1157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.genaiLinkpreview.cardLink.record()`, `Glean.genaiLinkpreview.fetch.record()`, `Glean.genaiLinkpreview.start.record()`, `Math.round()`, `actor.fetchPageData()`, `browsingContext.currentWindowGlobal.getActor()`, `doc.getElementById()`, `ogCard.addEventListener()`, `panel.append()`, `panel.hidePopup()`, `panel.style.setProperty()`, `this._getTabContextValue()`, `this._handleKeyPointsGenerationEvent()`, `this.createOGCard()`, `this.initOrResetPreviewPanel()`
- 条件付き依存: `if (source !== "onboarding")` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (source !== "onboarding")` → `[...lazy.onboardingTimes, ...Array(maxFreq).fill("0")].slice()`
- 条件付き依存: `if (source !== "onboarding")` → `Array(maxFreq).fill()`
- 条件付き依存: `if (source !== "onboarding")` → `Array()`
- 条件付き依存: `if (source == "onboarding")` → `panel.style.setProperty()`
- 条件付き依存: `if (panel.state == "closed")` → `panel.openPopupNearMouse()`
- 条件付き依存: `if (panel.state == "closed")` → `Glean.genaiLinkpreview.start.record()`
- 条件付き依存: `if (source !== "onboarding")` → `panel.openPopupNearMouse()`
- 参照: `event.detail`, `lazy.collapsed`, `lazy.onboardingMaxShowFreq`, `lazy.onboardingTimes`, `ogCard.generating`, `ogCard.keyPoints?.length`, `pageData.article.siteName`, `pageData.article.textContent?.length`, `pageData.error?.result`, `pageData.meta.description`, `pageData.meta.imageUrl`, `pageData.meta.title`, `pageData.url`, `panel.previewUrl`, `panel.state`, `this.linkPreviewPanelId`, `win.browsingContext`, `win.document`
- XPCOM: `Services.prefs`

## _maybeLinkPreview()
- 位置: L1166-1181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this._windowStates.get()`
- 条件付き依存: `if ( url && this.keyboardComboActive && Date.now() - this.overLinkTime <= lazy.ignoreMs && Date.now() - this.recentTyping >= lazy.recentTypingMs )` → `this.renderLinkPreviewPanel()`
- 参照: `lazy.ignoreMs`, `lazy.recentTypingMs`, `stateObject.overLink`, `this.keyboardComboActive`, `this.overLinkTime`, `this.recentTyping`

## handleContextMenuClick()
- 位置: async L1190-1193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderLinkPreviewPanel()`
- 参照: `nsContextMenu.browser.documentGlobal`

## _updateShortcutMetric()
- 位置: L1201-1213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.shortcut.set()`, `activeShortcuts.join()`
- 条件付き依存: `if (lazy.shift)` → `activeShortcuts.push()`
- 条件付き依存: `if (lazy.shiftAlt)` → `activeShortcuts.push()`
- 条件付き依存: `if (lazy.longPress)` → `activeShortcuts.push()`
- 参照: `lazy.longPress`, `lazy.shift`, `lazy.shiftAlt`

## uninstallModel()
- 位置: async L1224-1238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MLUninstallService.uninstall()`
- 参照: `lazy.LinkPreviewModel.engineId`
