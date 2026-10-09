# browser/components/translations/content/fullPageTranslationsPanel.js

source: browser/components/translations/content/fullPageTranslationsPanel.js
source-hash: 6eac00e607c0638dce158b3d3285b1c01b2d181c
lines: 1737

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`

## CheckboxPageAction.constructor()
- 位置: L75-85
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#alwaysTranslateLanguage`, `this.#neverTranslateLanguage`, `this.#neverTranslateSite`, `this.#translationsActive`

## CheckboxPageAction.#computeState()
- 位置: L99-111
- 役割: (未記入)
- 触るとき: (未記入)

## CheckboxPageAction.#state()
- 位置: L118-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CheckboxPageAction.#computeState()`, `Number()`
- 参照: `this.#alwaysTranslateLanguage`, `this.#neverTranslateLanguage`, `this.#neverTranslateSite`, `this.#translationsActive`

## CheckboxPageAction.alwaysTranslateLanguage()
- 位置: L133-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CheckboxPageAction.#computeState()`, `this.#state()`
- 参照: `PageAction.NO_CHANGE`, `PageAction.RESTORE_PAGE`, `PageAction.TRANSLATE_PAGE`

## CheckboxPageAction.neverTranslateLanguage()
- 位置: L151-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CheckboxPageAction.#computeState()`, `this.#state()`
- 参照: `PageAction.CLOSE_PANEL`, `PageAction.NO_CHANGE`, `PageAction.RESTORE_PAGE`

## CheckboxPageAction.neverTranslateSite()
- 位置: L173-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CheckboxPageAction.#computeState()`, `this.#state()`
- 参照: `PageAction.CLOSE_PANEL`, `PageAction.NO_CHANGE`, `PageAction.RESTORE_PAGE`, `PageAction.TRANSLATE_PAGE`

## console()
- 位置: L223-235
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#console)` → `console.createInstance()`
- 参照: `this.#console`

## elements()
- 位置: L256-326
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#lazyElements)` → `document.getElementById()`
- 条件付き依存: `if (!this.#lazyElements)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this.#lazyElements)` → `panel.addEventListener()`
- 条件付き依存: `if (!this.#lazyElements)` → `panel.querySelectorAll()`
- 条件付き依存: `if (!this.#lazyElements)` → `header.contains()`
- 条件付き依存: `if (!this.#lazyElements)` → `settingsButton.cloneNode()`
- 条件付き依存: `if (!this.#lazyElements)` → `settingsButtonClone.removeAttribute()`
- 条件付き依存: `if (!this.#lazyElements)` → `header.appendChild()`
- 条件付き依存: `if (!this.#lazyElements)` → `TranslationsPanelShared.defineLazyElements()`
- 参照: `this.#lazyElements`, `wrapper.content`, `wrapper.content.firstElementChild`

## buttonElements()
- 位置: L335-346
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#lazyButtonElements)` → `document.getElementById()`
- 参照: `this.#lazyButtonElements`

## #showError()
- 位置: L360-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`
- 条件付き依存: `if (hint)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (hintCommand && hintCommandText)` → `errorHintAction.removeEventListener()`
- 条件付き依存: `if (hintCommand && hintCommandText)` → `errorHintAction.addEventListener()`
- 条件付き依存: `if (hintCommand && hintCommandText)` → `document.l10n.setAttributes()`
- 参照: `error.hidden`, `errorHintAction.hidden`, `errorMessageHint.hidden`, `intro.hidden`, `this.#lastHintCommand`, `this.elements`

## #fetchDetectedLanguages()
- 位置: async L397-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTranslationsActor()`, `TranslationsParent.getTranslationsActor( gBrowser.selectedBrowser ).getLangTags()`
- 参照: `gBrowser.selectedBrowser`, `this.detectedLanguages`

## #getCachedDetectedLanguages()
- 位置: async L410-415
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.detectedLanguages)` → `this.#fetchDetectedLanguages()`
- 参照: `this.detectedLanguages`

## #ensureLangListsBuilt()
- 位置: async L422-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsPanelShared.ensureLangListsBuilt()`, `this.console?.error()`

## #updateViewFromTranslationStatus()
- 位置: L436-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsPanelShared.getLangListsInitState()`, `TranslationsParent.getTranslationsActor()`, `TranslationsUtils.langTagsMatch()`, `fromMenuList.value.split()`, `toMenuList.value.split()`
- 条件付き依存: `if ( requestedLanguagePair && !isEngineReady && TranslationsUtils.langTagsMatch( selectedFrom, requestedLanguagePair.sourceLanguage ) && TranslationsUtils.langTa...)` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( requestedLanguagePair && !isEngineReady && TranslationsUtils.langTagsMatch( selectedFrom, requestedLanguagePair.sourceLanguage ) && TranslationsUtils.langTa...)` → `this.updateUIForReTranslation()`
- 条件付き依存: `if (!( requestedLanguagePair && !isEngineReady && TranslationsUtils.langTagsMatch( selectedFrom, requestedLanguagePair.sourceLanguage ) && TranslationsUtils.langTa...))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!( requestedLanguagePair && !isEngineReady && TranslationsUtils.langTagsMatch( selectedFrom, requestedLanguagePair.sourceLanguage ) && TranslationsUtils.langTa...))` → `TranslationsUtils.langTagsMatch()`
- 条件付き依存: `if (requestedLanguagePair && isEngineReady)` → `TranslationsParent.createLanguageDisplayNames()`
- 条件付き依存: `if (requestedLanguagePair && isEngineReady)` → `this.updateUIForReTranslation()`
- 条件付き依存: `if (requestedLanguagePair && isEngineReady)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (requestedLanguagePair && isEngineReady)` → `languageDisplayNames.of()`
- 条件付き依存: `if (!(requestedLanguagePair && isEngineReady))` → `TranslationsParent.hasUserEverTranslated()`
- 条件付き依存: `if ( !requestedLanguagePair && !intro.hidden && !TranslationsParent.hasUserEverTranslated() )` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!( !requestedLanguagePair && !intro.hidden && !TranslationsParent.hasUserEverTranslated() ))` → `document.l10n.setAttributes()`
- 参照: `TranslationsParent.getTranslationsActor( gBrowser.selectedBrowser ).languageState`, `cancelButton.hidden`, `fromMenuList.value`, `gBrowser.selectedBrowser`, `intro.hidden`, `requestedLanguagePair.sourceLanguage`, `requestedLanguagePair.targetLanguage`, `this.elements`, `toMenuList.value`, `translateButton.disabled`

## updateUIForReTranslation()
- 位置: L529-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `fromLabel.hidden`, `fromLabel.style.marginBlockStart`, `fromMenuList.hidden`, `restoreButton.hidden`, `this.elements`, `toLabel.style.marginBlockStart`

## #isShowingDefaultView()
- 位置: L556-566
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `multiview.getAttribute()`
- 参照: `this.#lazyElements`, `this.elements`

## #showDefaultView()
- 位置: async L574-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsPanelShared.getLangListsInitState()`, `fromMenuList.value.split()`, `panel.addEventListener()`, `this.#fetchDetectedLanguages()`, `this.#fetchDetectedLanguages().then()`, `this.#updateViewFromTranslationStatus()`
- 条件付き依存: `if (TranslationsPanelShared.getLangListsInitState(this) === "error")` → `this.#showError()`
- 条件付き依存: `if (TranslationsPanelShared.getLangListsInitState(this) === "error")` → `this.updateUIForReTranslation()`
- 条件付き依存: `if (TranslationsPanelShared.getLangListsInitState(this) === "error")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (isDocLangTagSupported || force)` → `TranslationsUtils.langTagsMatch()`
- 条件付き依存: `if (!( this.#manuallySelectedToLanguage && !TranslationsUtils.langTagsMatch( docLangTag, this.#manuallySelectedToLanguage ) ))` → `TranslationsUtils.langTagsMatch()`
- 条件付き依存: `if (!( userLangTag && !TranslationsUtils.langTagsMatch(userLangTag, docLangTag) ))` → `TranslationsParent.getTopPreferredSupportedToLang()`
- 条件付き依存: `if (isDocLangTagSupported || force)` → `fromMenuList.value.split()`
- 条件付き依存: `if (isDocLangTagSupported || force)` → `toMenuList.value.split()`
- 条件付き依存: `if (isDocLangTagSupported || force)` → `this.onChangeLanguages()`
- 条件付き依存: `if (isDocLangTagSupported || force)` → `this.updateUIForReTranslation()`
- 条件付き依存: `if (isDocLangTagSupported || force)` → `multiview.setAttribute()`
- 条件付き依存: `if (isDocLangTagSupported || force)` → `TranslationsParent.hasUserEverTranslated()`
- 条件付き依存: `if (TranslationsParent.hasUserEverTranslated())` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(TranslationsParent.hasUserEverTranslated()))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(isDocLangTagSupported || force))` → `multiview.setAttribute()`
- 条件付き依存: `if (docLangTag)` → `TranslationsParent.createLanguageDisplayNames()`
- 条件付き依存: `if (docLangTag)` → `languageDisplayNames.of()`
- 条件付き依存: `if (language)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(language))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!fromMenuList.value)` → `fromMenuList.focus()`
- 条件付き依存: `if (!toMenuList.value)` → `toMenuList.focus()`
- 参照: `cancelButton.hidden`, `error.hidden`, `errorHintAction.disabled`, `fromMenuList.value`, `intro.hidden`, `langSelection.hidden`, `this.#manuallySelectedToLanguage`, `this.elements`, `toMenuList.value`, `translateButton.disabled`

## actionCommand()
- 位置: L601-601
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#reloadLangList()`

## #updateSettingsMenuLanguageCheckboxStates()
- 位置: async L737-776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTopPreferredSupportedToLang()`, `TranslationsParent.shouldAlwaysOfferTranslations()`, `TranslationsParent.shouldAlwaysTranslateLanguage()`, `TranslationsParent.shouldNeverTranslateLanguage()`, `menuitem.toggleAttribute()`, `panel.ownerDocument.querySelectorAll()`, `this.#getCachedDetectedLanguages()`
- 参照: `menuitem.disabled`, `this.elements`

## #updateSettingsMenuSiteCheckboxStates()
- 位置: async L782-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTranslationsActor()`, `TranslationsParent.getTranslationsActor( gBrowser.selectedBrowser ).shouldNeverTranslateSite()`, `menuitem.toggleAttribute()`, `panel.ownerDocument.querySelectorAll()`
- 参照: `gBrowser.selectedBrowser`, `this.elements`

## #populateSettingsMenuItems()
- 位置: async L800-857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `panel.ownerDocument.querySelectorAll()`, `this.#getCachedDetectedLanguages()`, `this.#updateSettingsMenuLanguageCheckboxStates()`, `this.#updateSettingsMenuSiteCheckboxStates()`
- 条件付き依存: `if (docLangTag)` → `TranslationsParent.createLanguageDisplayNames()`
- 条件付き依存: `if (docLangTag)` → `languageDisplayNames.of()`
- 条件付き依存: `if (docLangDisplayName)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(docLangDisplayName))` → `document.l10n.setAttributes()`
- 参照: `this.elements`

## #showRevisitView()
- 位置: async L864-886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTopPreferredSupportedToLang()`, `this.#isShowingDefaultView()`, `this.onChangeLanguages()`
- 条件付き依存: `if (!this.#isShowingDefaultView())` → `this.#showDefaultView()`
- 条件付き依存: `if (!this.#isShowingDefaultView())` → `TranslationsParent.getTranslationsActor()`
- 参照: `fromMenuList.value`, `gBrowser.selectedBrowser`, `intro.hidden`, `this.elements`, `toMenuList.value`

## onChangeRevisitTo()
- 位置: L892-895
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `revisitMenuList.value`, `revisitTranslate.disabled`, `this.elements`

## onChangeFromLanguage()
- 位置: async L902-940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTopPreferredSupportedToLang()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .fullPagePanel()`, `TranslationsParent.telemetry() .fullPagePanel() .onChangeFromLanguage()`, `TranslationsUtils.langTagsMatch()`, `this.console?.error()`, `this.onChangeLanguages()`
- 参照: `target.value`, `target?.value`, `this.elements.toMenuList.value`

## onChangeToLanguage()
- 位置: L947-957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onChangeLanguages()`
- 条件付き依存: `if (target?.value)` → `TranslationsParent.telemetry() .fullPagePanel() .onChangeToLanguage()`
- 条件付き依存: `if (target?.value)` → `TranslationsParent.telemetry() .fullPagePanel()`
- 条件付き依存: `if (target?.value)` → `TranslationsParent.telemetry()`
- 参照: `target.value`, `target?.value`, `this.#manuallySelectedToLanguage`

## onChangeLanguages()
- 位置: L962-964
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateViewFromTranslationStatus()`

## close()
- 位置: L969-971
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`
- 参照: `this.elements.panel`

## onLearnMoreLink()
- 位置: L977-980
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FullPageTranslationsPanel.close()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onLearnMoreLink()`

## onAboutTranslations()
- 位置: L985-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onAboutTranslations()`, `window.openTrustedLinkIn()`
- 参照: `gBrowser.selectedBrowser.browsingContext.top.embedderElement .documentGlobal`, `this.elements.panel`
- XPCOM: `Services.scriptSecurityManager`

## onChangeSourceLanguage()
- 位置: async L1008-1022
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `TranslationsParent.getTranslationsActor()`, `this.#openPanelPopup()`, `this.#showDefaultView()`
- 参照: `gBrowser.selectedBrowser`, `this.elements`, `this.elements.appMenuButton`

## #reloadLangList()
- 位置: async L1027-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureLangListsBuilt()`, `this.#showDefaultView()`
- 参照: `this.elements.errorHintAction.disabled`

## handlePanelButtonEvent()
- 位置: L1041-1073
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .fullPagePanel()`, `TranslationsParent.telemetry() .fullPagePanel() .onChangeSourceLanguageButton()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onCancelButton()`, `TranslationsParent.telemetry().fullPagePanel().onDismissErrorButton()`, `TranslationsParent.telemetry().fullPagePanel().onRestorePageButton()`, `TranslationsParent.telemetry().fullPagePanel().onTranslateButton()`
- 参照: `cancelButton.id`, `changeSourceLanguageButton.id`, `dismissErrorButton.id`, `event.target.id`, `restoreButton.id`, `this.elements`, `translateButton.id`

## handlePanelPopupShownEvent()
- 位置: L1080-1098
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onOpenFromLanguageMenu()`, `TranslationsParent.telemetry().fullPagePanel().onOpenToLanguageMenu()`
- 参照: `event.target.id`, `fromMenuList.firstChild.id`, `panel.id`, `this.elements`, `toMenuList.firstChild.id`

## handlePanelPopupHiddenEvent()
- 位置: L1105-1125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .fullPagePanel()`, `TranslationsParent.telemetry() .fullPagePanel() .onCloseFromLanguageMenu()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onClose()`, `TranslationsParent.telemetry().fullPagePanel().onCloseToLanguageMenu()`
- 参照: `event.target.id`, `fromMenuList.firstChild.id`, `panel.id`, `this.#isPopupOpen`, `this.elements`, `this.elements.error.hidden`, `toMenuList.firstChild.id`

## handleSettingsPopupShownEvent()
- 位置: L1130-1132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onOpenSettingsMenu()`

## handleSettingsPopupHiddenEvent()
- 位置: L1137-1139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onCloseSettingsMenu()`

## #openPanelPopup()
- 位置: async L1155-1177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.openPopup()`, `PanelMultiView.openPopup(panel, target, { position: "bottomright topright", triggerEvent: event, }).catch()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onOpen()`, `this.#getCachedDetectedLanguages()`, `this.console?.error()`
- 参照: `appMenuButton.id`, `target.id`, `this.#isPopupOpen`, `this.elements`

## open()
- 位置: async L1193-1203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openImpl()`, `this.#openPromise.finally()`
- 参照: `this.#openPromise`

## #openImpl()
- 位置: async L1218-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTranslationsActor()`, `button.contains()`, `event.stopPropagation()`, `this.#ensureLangListsBuilt()`, `this.#openPanelPopup()`, `this.#populateSettingsMenuItems()`, `this.console?.log()`
- 条件付き依存: `if (requestedLanguagePair)` → `this.#showRevisitView(requestedLanguagePair).catch()`
- 条件付き依存: `if (requestedLanguagePair)` → `this.#showRevisitView()`
- 条件付き依存: `if (requestedLanguagePair)` → `this.console?.error()`
- 条件付き依存: `if (!(requestedLanguagePair))` → `this.#showDefaultView( TranslationsParent.getTranslationsActor(gBrowser.selectedBrowser) ).catch()`
- 条件付き依存: `if (!(requestedLanguagePair))` → `this.#showDefaultView()`
- 条件付き依存: `if (!(requestedLanguagePair))` → `TranslationsParent.getTranslationsActor()`
- 条件付き依存: `if (!(requestedLanguagePair))` → `this.console?.error()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `TranslationsParent.getTranslationsActor( gBrowser.selectedBrowser ).languageState`, `event.button`, `event.charCode`, `event.keyCode`, `event.target`, `event.type`, `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser`, `this.buttonElements`, `this.elements.appMenuButton`

## #isTranslationsActive()
- 位置: L1273-1278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTranslationsActor()`
- 参照: `TranslationsParent.getTranslationsActor( gBrowser.selectedBrowser ).languageState`, `gBrowser.selectedBrowser`

## onTranslate()
- 位置: async L1283-1299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `TranslationsParent.getTranslationsActor()`, `actor.translate()`, `this.elements.fromMenuList.value.split()`, `this.elements.toMenuList.value.split()`
- 参照: `gBrowser.selectedBrowser`, `this.#manuallySelectedToLanguage`, `this.elements.panel`

## onCancel()
- 位置: L1304-1306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`
- 参照: `this.elements.panel`

## openSettingsPopup()
- 位置: async L1311-1320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `button.ownerDocument.getElementById()`, `popup.openPopup()`, `this.#updateSettingsMenuLanguageCheckboxStates()`, `this.#updateSettingsMenuSiteCheckboxStates()`

## getCheckboxPageActionFor()
- 位置: L1329-1349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `alwaysTranslateLanguageMenuItem.hasAttribute()`, `neverTranslateLanguageMenuItem.hasAttribute()`, `neverTranslateSiteMenuItem.hasAttribute()`, `this.#isTranslationsActive()`
- 参照: `this.elements`

## openManageLanguages()
- 位置: L1354-1360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().fullPagePanel()`, `TranslationsParent.telemetry().fullPagePanel().onManageLanguages()`, `window.openTrustedLinkIn()`
- 参照: `gBrowser.selectedBrowser.browsingContext.top.embedderElement .documentGlobal`

## #doPageAction()
- 位置: async L1367-1385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `this.onRestore()`, `this.onTranslate()`
- 参照: `PageAction.CLOSE_PANEL`, `PageAction.NO_CHANGE`, `PageAction.RESTORE_PAGE`, `PageAction.TRANSLATE_PAGE`, `this.elements.panel`

## onAlwaysTranslateLanguage()
- 位置: async L1392-1407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .fullPagePanel()`, `TranslationsParent.telemetry() .fullPagePanel() .onAlwaysTranslateLanguage()`, `TranslationsParent.toggleAlwaysTranslateLanguagePref()`, `this.#doPageAction()`, `this.#getCachedDetectedLanguages()`, `this.#updateSettingsMenuLanguageCheckboxStates()`, `this.getCheckboxPageActionFor()`, `this.getCheckboxPageActionFor().alwaysTranslateLanguage()`

## onAlwaysOfferTranslations()
- 位置: async L1412-1417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .fullPagePanel()`, `TranslationsParent.telemetry() .fullPagePanel() .onAlwaysOfferTranslations()`, `TranslationsParent.toggleAutomaticallyPopupPref()`

## onNeverTranslateLanguage()
- 位置: async L1424-1437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .fullPagePanel()`, `TranslationsParent.telemetry() .fullPagePanel() .onNeverTranslateLanguage()`, `TranslationsParent.toggleNeverTranslateLanguagePref()`, `this.#doPageAction()`, `this.#getCachedDetectedLanguages()`, `this.#updateSettingsMenuLanguageCheckboxStates()`, `this.getCheckboxPageActionFor()`, `this.getCheckboxPageActionFor().neverTranslateLanguage()`

## onNeverTranslateSite()
- 位置: async L1444-1454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTranslationsActor()`, `TranslationsParent.getTranslationsActor( gBrowser.selectedBrowser ).toggleNeverTranslateSitePermissions()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .fullPagePanel()`, `TranslationsParent.telemetry() .fullPagePanel() .onNeverTranslateSite()`, `this.#doPageAction()`, `this.#updateSettingsMenuSiteCheckboxStates()`, `this.getCheckboxPageActionFor()`, `this.getCheckboxPageActionFor().neverTranslateSite()`
- 参照: `gBrowser.selectedBrowser`

## onRestore()
- 位置: async L1459-1470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `TranslationsParent.getTranslationsActor()`, `TranslationsParent.getTranslationsActor( gBrowser.selectedBrowser ).restorePage()`, `this.#getCachedDetectedLanguages()`
- 参照: `gBrowser.selectedBrowser`, `this.elements`

## onLocationChange()
- 位置: L1478-1492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.isFullPageTranslationsRestrictedForPage()`
- 参照: `TranslationsFeature.isEnabled`, `gBrowser.selectedBrowser`, `this.buttonElements.button.hidden`

## #showEngineError()
- 位置: async L1499-1517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureLangListsBuilt()`, `this.#openPanelPopup()`, `this.#showDefaultView()`, `this.#showDefaultView(actor).catch()`, `this.#showError()`, `this.console?.error()`
- 参照: `button.hidden`, `this.buttonElements`, `this.elements.appMenuButton`, `this.elements.error.hidden`

## handleEvent()
- 位置: L1524-1735
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `TranslationsParent.getIsTranslationsEngineSupported()`, `console.error()`, `this.#showEngineError()`, `this.#showEngineError(actor).catch()`, `this.console?.debug()`, `this.console?.error()`, `this.handlePanelButtonEvent()`, `this.handlePanelPopupHiddenEvent()`, `this.handlePanelPopupShownEvent()`, `this.onCancel()`, `this.onChangeFromLanguage()`, `this.onChangeSourceLanguage()`, `this.onChangeToLanguage()`, `this.onLearnMoreLink()`, `this.onRestore()`, `this.onTranslate()`, `this.openSettingsPopup()`
- 条件付き依存: `if (!id)` → `target.closest()`
- 条件付き依存: `if (Services.wm.getMostRecentBrowserWindow()?.gBrowser === gBrowser)` → `this.open()`
- 条件付き依存: `if (this.#isPopupOpen)` → `this.#updateViewFromTranslationStatus()`
- 条件付き依存: `if (requestedLanguagePair)` → `button.setAttribute()`
- 条件付き依存: `if (isEngineReady)` → `TranslationsParent.createLanguageDisplayNames()`
- 条件付き依存: `if (isEngineReady)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (isEngineReady)` → `languageDisplayNames.of()`
- 条件付き依存: `if (isEngineReady)` → `requestedLanguagePair.targetLanguage.split()`
- 条件付き依存: `if (!(isEngineReady))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(requestedLanguagePair))` → `button.removeAttribute()`
- 条件付き依存: `if (!(requestedLanguagePair))` → `TranslationsParent.hasUserEverTranslated()`
- 条件付き依存: `if (TranslationsParent.hasUserEverTranslated())` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(TranslationsParent.hasUserEverTranslated()))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (wasButtonHidden)` → `PageActions.sendPlacedInUrlbarTrigger()`
- 参照: `FullPageTranslationsPanel.detectedLanguages`, `Services.wm.getMostRecentBrowserWindow()?.gBrowser`, `TranslationsFeature.isEnabled`, `actor.innerWindowId`, `actor.languageState`, `button.hidden`, `buttonCircleArrows.hidden`, `buttonLocale.hidden`, `buttonLocale.innerText`, `detectedLanguages?.docLangTag`, `detectedLanguages?.isDocLangTagSupported`, `detectedLanguages?.userLangTag`, `event.detail`, `event.target`, `event.type`, `gBrowser.selectedBrowser.browsingContext.top.embedderElement .innerWindowID`, `requestedLanguagePair.sourceLanguage`, `requestedLanguagePair.targetLanguage`, `target.closest("[id]")?.id`, `this.#isPopupOpen`, `this.#manuallySelectedToLanguage`, `this.buttonElements`
- XPCOM: `Services.wm`
