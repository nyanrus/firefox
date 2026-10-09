# browser/components/translations/content/selectTranslationsPanel.js

source: browser/components/translations/content/selectTranslationsPanel.js
source-hash: 7f454a216b7264f7812a65ac08ece3e6269a8178
lines: 2411

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## console()
- 位置: L55-67
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#console)` → `console.createInstance()`
- 参照: `this.#console`

## shortTextHeight()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#shortTextHeight`

## longTextHeight()
- 位置: L148-150
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#longTextHeight`

## textLengthThreshold()
- 位置: L165-167
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#textLengthThreshold`

## elements()
- 位置: L240-292
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#lazyElements)` → `document.getElementById()`
- 条件付き依存: `if (!this.#lazyElements)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this.#lazyElements)` → `TranslationsPanelShared.defineLazyElements()`
- 参照: `this.#lazyElements`, `wrapper.content`, `wrapper.content.firstElementChild`

## getTopSupportedDetectedLanguage()
- 位置: async L302-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LanguageDetector.detectLanguage()`, `TranslationsParent.findCompatibleSourceLangTagSync()`, `TranslationsParent.getNonPivotLanguagePairs()`, `this.#getLanguageInfo()`

## #getLanguageInfo()
- 位置: L345-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTranslationsActor()`, `TranslationsParent.isFullPageTranslationsRestrictedForPage()`, `this.#maybeGetActiveFullPageTranslationsTargetLanguage()`
- 条件付き依存: `if ( !TranslationsParent.isFullPageTranslationsRestrictedForPage(gBrowser) )` → `this.console?.warn()`
- 条件付き依存: `if ( !TranslationsParent.isFullPageTranslationsRestrictedForPage(gBrowser) )` → `this.console?.error()`
- 参照: `actor.languageState`, `gBrowser.selectedBrowser`, `this .#isFullPageTranslationsRestrictedForPage`, `this.#activeFullPageTranslationsTargetLanguage`, `this.#isFullPageTranslationsRestrictedForPage`, `this.#languageInfo`, `this.#languageInfo.docLangTag`

## getLangPairPromise()
- 位置: async L408-433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectTranslationsPanel.getTopSupportedDetectedLanguage()`, `TranslationsParent.getTopPreferredSupportedToLang()`, `TranslationsParent.isInAutomation()`, `TranslationsParent.isTranslationsEngineMocked()`

## close()
- 位置: L438-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`
- 参照: `this.#mostRecentUIPhase`, `this.elements.panel`

## #ensureLangListsBuilt()
- 位置: async L450-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsPanelShared.ensureLangListsBuilt()`

## #initializeLanguageMenuList()
- 位置: async L462-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.findCompatibleSourceLangTag()`, `TranslationsParent.findCompatibleTargetLangTag()`
- 条件付き依存: `if (compatibleLangTag)` → `menuList.removeAttribute()`
- 条件付き依存: `if (!(compatibleLangTag))` → `this.#deselectLanguage()`
- 参照: `menuList.id`, `menuList.value`, `this.elements.fromMenuList.id`

## #initializeLanguageMenuLists()
- 位置: async L486-507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `this.#initializeLanguageMenuList()`, `this.#maybeTranslateOnEvents()`
- 参照: `this.elements`

## #initializeEventListeners()
- 位置: L513-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fromMenuList.addEventListener()`, `panel.addEventListener()`, `toMenuList.addEventListener()`, `tryAnotherSourceMenuList.addEventListener()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `panel.addEventListener()`
- 参照: `AppConstants.platform`, `this.#eventListenersInitialized`, `this.elements`

## open()
- 位置: async L552-609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .selectTranslationsPanel()`, `TranslationsParent.telemetry() .selectTranslationsPanel() .onOpen()`, `this.#cachePlaceholderText()`, `this.#changeStateToInitFailure()`, `this.#ensureLangListsBuilt()`, `this.#getLanguageInfo()`, `this.#initializeEventListeners()`, `this.#initializeLanguageMenuLists()`, `this.#isOpen()`, `this.#maybeRequestTranslation()`, `this.#openPopup()`, `this.#registerSourceText()`, `this.console?.error()`
- 条件付き依存: `if (this.#isOpen())` → `this.#forceReopen()`
- 参照: `this.#sourceTextWordCount`

## #maybeGetActiveFullPageTranslationsTargetLanguage()
- 位置: L618-628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTranslationsActor()`, `this.console.warn()`
- 参照: `TranslationsParent.getTranslationsActor( gBrowser.selectedBrowser ).languageState`, `gBrowser.selectedBrowser`, `requestedLanguagePair?.targetLanguage`

## #forceReopen()
- 位置: async L645-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#changeStateToClosed()`, `this.close()`, `this.console?.warn()`, `this.open()`

## #openPopup()
- 位置: L673-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.openPopupAtScreenRect()`, `this.#cacheAlignmentPositionOnOpen()`, `this.console?.log()`
- 参照: `this.elements`

## #cacheAlignmentPositionOnOpen()
- 位置: L696-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.addEventListener()`
- 参照: `popupPositionedEvent.alignmentPosition`, `this.#alignmentPosition`, `this.elements`

## #registerSourceText()
- 位置: async L718-748
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.findCompatibleSourceLangTag()`, `this.#maybeTranslateOnEvents()`
- 条件付き依存: `if (compatibleFromLang)` → `this.#changeStateTo()`
- 条件付き依存: `if (!(compatibleFromLang))` → `this.#changeStateTo()`
- 参照: `SelectTranslationsPanel.longTextHeight`, `SelectTranslationsPanel.shortTextHeight`, `SelectTranslationsPanel.textLengthThreshold`, `sourceText.length`, `textArea.style.height`, `textArea.style.maxHeight`, `textArea.style.resize`, `textArea.value`, `this.elements`

## #cachePlaceholderText()
- 位置: async L753-760
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatValues()`
- 参照: `this.#idlePlaceholderText`, `this.#translatingPlaceholderText`

## #openSettingsPopup()
- 位置: L765-776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .selectTranslationsPanel()`, `TranslationsParent.telemetry() .selectTranslationsPanel() .onOpenSettingsMenu()`, `popup.openPopup()`, `settingsButton.ownerDocument.getElementById()`
- 参照: `this.elements`

## onAboutTranslations()
- 位置: L781-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .selectTranslationsPanel()`, `TranslationsParent.telemetry() .selectTranslationsPanel() .onAboutTranslations()`, `this.close()`, `window.openTrustedLinkIn()`
- 参照: `gBrowser.selectedBrowser.browsingContext.top.embedderElement .documentGlobal`
- XPCOM: `Services.scriptSecurityManager`

## openTranslationsSettingsPage()
- 位置: L804-814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .selectTranslationsPanel()`, `TranslationsParent.telemetry() .selectTranslationsPanel() .onTranslationSettings()`, `this.close()`, `window.openTrustedLinkIn()`
- 参照: `gBrowser.selectedBrowser.browsingContext.top.embedderElement .documentGlobal`

## #handleCommandEvent()
- 位置: L821-884
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openSettingsPopup()`, `this.onChangeFromLanguage()`, `this.onChangeToLanguage()`, `this.onChangeTryAnotherSourceLanguage()`, `this.onClickCancelButton()`, `this.onClickCopyButton()`, `this.onClickDoneButton()`, `this.onClickTranslateButton()`, `this.onClickTranslateFullPageButton()`, `this.onClickTryAgainButton()`
- 参照: `cancelButton.id`, `copyButton.id`, `doneButtonPrimary.id`, `doneButtonSecondary.id`, `fromMenuList.id`, `fromMenuPopup.id`, `settingsButton.id`, `target.id`, `this.elements`, `toMenuList.id`, `toMenuPopup.id`, `translateButton.id`, `translateFullPageButton.id`, `tryAgainButton.id`, `tryAnotherSourceMenuList.id`, `tryAnotherSourceMenuPopup.id`

## #handleEnterKeyPressed()
- 位置: L891-934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openSettingsPopup()`, `this.onClickCancelButton()`, `this.onClickCopyButton()`, `this.onClickDoneButton()`, `this.onClickTranslateButton()`, `this.onClickTranslateFullPageButton()`, `this.onClickTryAgainButton()`
- 参照: `cancelButton.id`, `copyButton.id`, `doneButtonPrimary.id`, `doneButtonSecondary.id`, `settingsButton.id`, `target.id`, `this.elements`, `translateButton.id`, `translateFullPageButton.id`, `tryAgainButton.id`

## #maybeEnableTextAreaResizer()
- 位置: L946-1151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`, `Math.min()`, `Math.trunc()`, `panel.getBoundingClientRect()`, `panel.getOuterScreenRect()`, `this.console?.debug()`
- 条件付き依存: `if (textArea.style.maxHeight)` → `this.console?.debug()`
- 条件付き依存: `if (textAreaScrollHeight <= textAreaClientHeight)` → `this.console?.debug()`
- 条件付き依存: `if (AppConstants.platform === "linux")` → `this.console?.warn()`
- 条件付き依存: `if (AppConstants.platform === "linux")` → `this.console?.debug()`
- 条件付き依存: `if (panelTop < 0)` → `this.console?.debug()`
- 条件付き依存: `if (panelBottom > window.innerHeight)` → `this.console?.debug()`
- 条件付き依存: `if (panelLeft < 0)` → `this.console?.debug()`
- 条件付き依存: `if (panelRight > window.innerWidth)` → `this.console?.debug()`
- 条件付き依存: `if (!panelBottom)` → `this.console?.debug()`
- 条件付き依存: `if (panelBottomToBottomEdge < BOTTOM_EDGE_PIXEL_BUFFER)` → `this.console?.debug()`
- 参照: `AppConstants.platform`, `GfxInfo.windowProtocol`, `gBrowser.selectedBrowser.browsingContext.top.embedderElement .documentGlobal`, `screen.availHeight`, `textArea.clientHeight`, `textArea.scrollHeight`, `textArea.style.maxHeight`, `textArea.style.resize`, `this.#alignmentPosition`, `this.elements`, `window.innerHeight`, `window.innerWidth`

## #handlePopupShownEvent()
- 位置: L1159-1167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePanelUIFromState()`
- 参照: `panel.id`, `target.id`, `this.elements`

## #handlePopupHiddenEvent()
- 位置: L1175-1185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().selectTranslationsPanel()`, `TranslationsParent.telemetry().selectTranslationsPanel().onClose()`, `this.#changeStateToClosed()`, `this.#removeActiveTranslationListeners()`
- 参照: `panel.id`, `target.id`, `this.elements`

## handleEvent()
- 位置: L1192-1221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleCommandEvent()`, `this.#handlePopupHiddenEvent()`, `this.#handlePopupShownEvent()`
- 条件付き依存: `if (event.key === "Enter")` → `this.#handleEnterKeyPressed()`
- 参照: `event.key`, `event.target`, `event.type`, `target.id`, `target.parentElement`

## onChangeFromLanguage()
- 位置: L1226-1229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateConditionalUIEnabledState()`
- 参照: `this.#sourceTextWordCount`

## onChangeToLanguage()
- 位置: L1234-1236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateConditionalUIEnabledState()`

## onChangeTryAnotherSourceLanguage()
- 位置: L1241-1246
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.elements`, `translateButton.disabled`, `tryAnotherSourceMenuList.value`

## onClickCancelButton()
- 位置: L1251-1254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().selectTranslationsPanel()`, `TranslationsParent.telemetry().selectTranslationsPanel().onCancelButton()`, `this.close()`

## onClickCopyButton()
- 位置: L1259-1270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ClipboardHelper.copyString()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().selectTranslationsPanel()`, `TranslationsParent.telemetry().selectTranslationsPanel().onCopyButton()`, `this.#checkCopyButton()`, `this.console?.error()`, `this.getTranslatedText()`

## onClickDoneButton()
- 位置: L1275-1278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().selectTranslationsPanel()`, `TranslationsParent.telemetry().selectTranslationsPanel().onDoneButton()`, `this.close()`

## onClickTranslateButton()
- 位置: L1283-1296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().selectTranslationsPanel()`, `TranslationsParent.telemetry().selectTranslationsPanel().onTranslateButton()`, `this.#maybeRequestTranslation()`
- 参照: `fromMenuList.value`, `this.#translationState`, `this.elements`, `tryAnotherSourceMenuList.value`

## onClickTranslateFullPageButton()
- 位置: L1301-1332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getTranslationsActor()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry() .selectTranslationsPanel()`, `TranslationsParent.telemetry() .selectTranslationsPanel() .onTranslateFullPageButton()`, `actor.translate()`, `panel.addEventListener()`, `this.#getSelectedLanguagePair()`, `this.close()`, `this.console?.error()`
- 参照: `gBrowser.selectedBrowser`, `this.elements`

## onClickTryAgainButton()
- 位置: L1337-1383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().selectTranslationsPanel()`, `TranslationsParent.telemetry().selectTranslationsPanel().onTryAgainButton()`, `panel.addEventListener()`, `this.#maybeRequestTranslation()`, `this.close()`, `this.console?.error()`, `this.open()`, `this.phase()`
- 参照: `this.#translationState`, `this.elements`

## #checkCopyButton()
- 位置: L1388-1395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `copyButton.classList.add()`, `document.l10n.setAttributes()`
- 参照: `this.elements`

## #uncheckCopyButton()
- 位置: L1400-1407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `copyButton.classList.remove()`, `document.l10n.setAttributes()`
- 参照: `this.elements`

## #deselectLanguage()
- 位置: async L1415-1419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `document.l10n.translateElements()`
- 参照: `menuList.value`

## #maybeFocusMenuList()
- 位置: L1427-1439
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (menuList && !menuList.value)` → `menuList.focus()`
- 条件付き依存: `if (!fromMenuList.value)` → `fromMenuList.focus()`
- 条件付き依存: `if (!toMenuList.value)` → `toMenuList.focus()`
- 参照: `fromMenuList.value`, `menuList.value`, `this.elements`, `toMenuList.value`

## #indicateTranslatedTextArea()
- 位置: L1444-1461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestAnimationFrame()`, `textArea.focus()`, `textArea.setSelectionRange()`
- 参照: `textArea.scrollTop`, `textArea.style.overflow`, `this.elements`

## #isSelectedLangPair()
- 位置: L1471-1480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsUtils.langTagsMatch()`, `this.#getSelectedLanguagePair()`
- 参照: `selected.sourceLanguage`, `selected.targetLanguage`

## #getSelectedLanguagePair()
- 位置: L1487-1497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fromMenuList.value.split()`, `toMenuList.value.split()`
- 参照: `this.elements`

## getSourceText()
- 位置: L1505-1507
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#translationState?.sourceText`

## getTranslatedText()
- 位置: L1515-1517
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#translationState?.translatedText`

## phase()
- 位置: L1524-1526
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#translationState.phase`

## #isOpen()
- 位置: L1531-1533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.phase()`

## #isClosed()
- 位置: L1538-1540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.phase()`

## #changeStateTo()
- 位置: L1550-1602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`, `this.#updatePanelUIFromState()`, `this.console?.debug()`, `this.phase()`
- 参照: `this.#translationState`, `this.#translationState.phase`

## #changeStateToClosed()
- 位置: L1607-1609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#changeStateTo()`

## #changeStateToTranslating()
- 位置: L1616-1622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#changeStateTo()`, `this.phase()`

## #changeStateToTranslated()
- 位置: L1629-1637
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#changeStateTo()`, `this.phase()`

## #changeStateToInitFailure()
- 位置: L1649-1665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#changeStateTo()`

## #changeStateToTranslationFailure()
- 位置: L1670-1678
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#changeStateTo()`, `this.phase()`
- 条件付き依存: `if (phase !== "translating")` → `this.console?.error()`

## #maybeChangeStateToTranslatable()
- 位置: L1687-1722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `langSelectionChanged()`, `shouldTranslateEvenIfLangSelectionHasNotChanged()`
- 条件付き依存: `if ( // A valid source language is actively selected. sourceLanguage && // A valid target language is actively selected. targetLanguage && // The language select...)` → `this.#changeStateTo()`
- 参照: `this.#translationState`

## langSelectionChanged()
- 位置: L1690-1695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsUtils.langTagsMatch()`
- 参照: `previous.sourceLanguage`, `previous.targetLanguage`

## shouldTranslateEvenIfLangSelectionHasNotChanged()
- 位置: L1697-1705
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.phase()`

## #handleCopyButtonChanges()
- 位置: L1729-1749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#uncheckCopyButton()`

## #handleTextAreaBackgroundChanges()
- 位置: L1756-1777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `textArea.classList.add()`, `textArea.classList.remove()`
- 参照: `this.elements`

## #handlePrimaryUIChanges()
- 位置: L1784-1819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#displayIdlePlaceholder()`, `this.#displayInitFailureMessage()`, `this.#displayTranslatedText()`, `this.#displayTranslatingPlaceholder()`, `this.#displayTranslationFailureMessage()`, `this.#displayUnsupportedLanguageMessage()`

## #shouldHideTranslateFullPageButton()
- 位置: L1826-1833
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#activeFullPageTranslationsTargetLanguage`, `this.#isFullPageTranslationsRestrictedForPage`

## #shouldContinueTranslation()
- 位置: L1844-1853
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isOpen()`, `this.#isSelectedLangPair()`
- 参照: `this.#translationId`

## #displayIdlePlaceholder()
- 位置: L1858-1866
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeFocusMenuList()`, `this.#showMainContent()`, `this.#updateConditionalUIEnabledState()`, `this.#updateTextDirection()`
- 参照: `SelectTranslationsPanel.elements`, `textArea.value`, `this.#idlePlaceholderText`

## #displayTranslatingPlaceholder()
- 位置: L1871-1879
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#indicateTranslatedTextArea()`, `this.#showMainContent()`, `this.#updateConditionalUIEnabledState()`, `this.#updateTextDirection()`
- 参照: `SelectTranslationsPanel.elements`, `textArea.value`, `this.#translatingPlaceholderText`

## #displayTranslatedText()
- 位置: L1884-1901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSelectedLanguagePair()`, `this.#indicateTranslatedTextArea()`, `this.#maybeEnableTextAreaResizer()`, `this.#showMainContent()`, `this.#updateConditionalUIEnabledState()`, `this.#updateTextDirection()`, `this.getTranslatedText()`, `window.A11yUtils.announce()`
- 参照: `SelectTranslationsPanel.elements`, `gBrowser.selectedBrowser.browsingContext.top.embedderElement .documentGlobal`, `textArea.value`

## #setPanelElementAttributes()
- 位置: L1911-1918
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `element.hidden`

## #updateConditionalUIEnabledState()
- 位置: L1923-1943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsUtils.langTagsMatch()`, `this.#getSelectedLanguagePair()`, `this.#shouldHideTranslateFullPageButton()`, `this.phase()`
- 参照: `copyButton.disabled`, `textArea.disabled`, `this.elements`, `translateButton.disabled`, `translateFullPageButton.disabled`, `tryAnotherSourceMenuList.value`

## #updatePanelUIFromState()
- 位置: L1948-1956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleCopyButtonChanges()`, `this.#handlePrimaryUIChanges()`, `this.#handleTextAreaBackgroundChanges()`, `this.phase()`
- 参照: `this.#mostRecentUIPhase`

## #showMainContent()
- 位置: L1961-1999
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setPanelElementAttributes()`, `this.#shouldHideTranslateFullPageButton()`
- 参照: `this.elements`

## #showUnsupportedLanguageContent()
- 位置: L2004-2033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setPanelElementAttributes()`
- 参照: `this.elements`

## #displayInitFailureMessage()
- 位置: L2038-2074
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setPanelElementAttributes()`, `tryAgainButton.focus()`, `tryAgainButton.setAttribute()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "init-failure")` → `TranslationsParent.telemetry() .selectTranslationsPanel() .onInitializationFailureMessage()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "init-failure")` → `TranslationsParent.telemetry() .selectTranslationsPanel()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "init-failure")` → `TranslationsParent.telemetry()`
- 参照: `this.#mostRecentUIPhase`, `this.elements`

## #displayTranslationFailureMessage()
- 位置: L2079-2125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setPanelElementAttributes()`, `tryAgainButton.focus()`, `tryAgainButton.setAttribute()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "translation-failure")` → `this.#getSelectedLanguagePair()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "translation-failure")` → `TranslationsParent.telemetry() .selectTranslationsPanel() .onTranslationFailureMessage()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "translation-failure")` → `TranslationsParent.telemetry() .selectTranslationsPanel()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "translation-failure")` → `TranslationsParent.telemetry()`
- 参照: `this.#mostRecentUIPhase`, `this.elements`

## #displayUnsupportedLanguageMessage()
- 位置: L2131-2168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.createLanguageDisplayNames()`, `document.l10n.setAttributes()`, `languageDisplayNames.of()`, `this.#maybeFocusMenuList()`, `this.#showUnsupportedLanguageContent()`, `this.#updateConditionalUIEnabledState()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "unsupported")` → `this.#getLanguageInfo()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "unsupported")` → `TranslationsParent.telemetry() .selectTranslationsPanel() .onUnsupportedLanguageMessage()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "unsupported")` → `TranslationsParent.telemetry() .selectTranslationsPanel()`
- 条件付き依存: `if (this.#mostRecentUIPhase !== "unsupported")` → `TranslationsParent.telemetry()`
- 条件付き依存: `if (language)` → `document.l10n.setAttributes()`
- 参照: `this.#mostRecentUIPhase`, `this.#translationState`, `this.elements`

## #updateTextDirection()
- 位置: L2176-2184
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (langTag)` → `Services.intl.getScriptDirection()`
- 条件付き依存: `if (langTag)` → `textArea.setAttribute()`
- 条件付き依存: `if (!(langTag))` → `textArea.removeAttribute()`
- 参照: `this.elements`
- XPCOM: `Services.intl`

## #requestTranslationsPort()
- 位置: async L2192-2194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.requestTranslationsPort()`

## #createTranslator()
- 位置: async L2203-2216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsUtils.serializeLanguagePair()`, `Translator.create()`, `this.console?.log()`
- 参照: `this.#requestTranslationsPort`

## #maybeRequestTranslation()
- 位置: L2222-2299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.storeMostRecentTargetLanguage()`, `TranslationsParent.telemetry()`, `TranslationsParent.telemetry().onTranslate()`, `this.#changeStateToTranslationFailure()`, `this.#createTranslator()`, `this.#createTranslator(languagePair) .then()`, `this.#getLanguageInfo()`, `this.#getSelectedLanguagePair()`, `this.#isClosed()`, `this.#maybeChangeStateToTranslatable()`, `this.#shouldContinueTranslation()`, `this.console?.error()`, `this.console?.warn()`, `this.getSourceText()`, `this.phase()`, `translator.destroy()`
- 条件付き依存: `if ( this.#shouldContinueTranslation( translationId, sourceLanguage, targetLanguage ) )` → `this.#changeStateToTranslating()`
- 条件付き依存: `if ( this.#shouldContinueTranslation( translationId, sourceLanguage, targetLanguage ) )` → `translator.translate()`
- 条件付き依存: `if ( this.#shouldContinueTranslation( translationId, sourceLanguage, targetLanguage ) )` → `this.getSourceText()`
- 条件付き依存: `if ( translatedText && this.#shouldContinueTranslation( translationId, sourceLanguage, targetLanguage ) )` → `this.#changeStateToTranslated()`
- 条件付き依存: `if (!this.#sourceTextWordCount)` → `TranslationsParent.countWords()`
- 参照: `sourceText.length`, `this.#sourceTextWordCount`, `this.#translationId`

## #maybeReportLanguageChangeToTelemetry()
- 位置: L2306-2335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsUtils.langTagsMatch()`, `this.#getSelectedLanguagePair()`
- 条件付き依存: `if ( !TranslationsUtils.langTagsMatch( selected.sourceLanguage, previous.sourceLanguage ) )` → `this.#getLanguageInfo()`
- 条件付き依存: `if ( !TranslationsUtils.langTagsMatch( selected.sourceLanguage, previous.sourceLanguage ) )` → `TranslationsParent.telemetry() .selectTranslationsPanel() .onChangeFromLanguage()`
- 条件付き依存: `if ( !TranslationsUtils.langTagsMatch( selected.sourceLanguage, previous.sourceLanguage ) )` → `TranslationsParent.telemetry() .selectTranslationsPanel()`
- 条件付き依存: `if ( !TranslationsUtils.langTagsMatch( selected.sourceLanguage, previous.sourceLanguage ) )` → `TranslationsParent.telemetry()`
- 条件付き依存: `if ( !TranslationsUtils.langTagsMatch( selected.targetLanguage, previous.targetLanguage ) )` → `TranslationsParent.telemetry() .selectTranslationsPanel() .onChangeToLanguage()`
- 条件付き依存: `if ( !TranslationsUtils.langTagsMatch( selected.targetLanguage, previous.targetLanguage ) )` → `TranslationsParent.telemetry() .selectTranslationsPanel()`
- 条件付き依存: `if ( !TranslationsUtils.langTagsMatch( selected.targetLanguage, previous.targetLanguage ) )` → `TranslationsParent.telemetry()`
- 参照: `previous.sourceLanguage`, `previous.targetLanguage`, `selected.sourceLanguage`, `selected.targetLanguage`, `this.#translationState`

## #maybeTranslateOnEvents()
- 位置: L2344-2379
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (target.translationListenerCallbacks.length === 0)` → `target.addEventListener()`
- 条件付き依存: `if (target.translationListenerCallbacks.length === 0)` → `target.translationListenerCallbacks.push()`
- 参照: `target.translationListenerCallbacks`, `target.translationListenerCallbacks.length`

## callback()
- 位置: L2354-2357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeReportLanguageChangeToTelemetry()`, `this.#maybeRequestTranslation()`

## callback()
- 位置: L2361-2366
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key === "Enter")` → `this.#maybeReportLanguageChangeToTelemetry()`
- 条件付き依存: `if (event.key === "Enter")` → `this.#maybeRequestTranslation()`
- 参照: `event.key`

## #removeActiveTranslationListeners()
- 位置: L2384-2392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removeTranslationListenersFrom()`
- 参照: `SelectTranslationsPanel.elements`

## #removeTranslationListenersFrom()
- 位置: L2399-2409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.removeEventListener()`
- 参照: `target.translationListenerCallbacks`
