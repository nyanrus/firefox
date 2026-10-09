# browser/components/preferences/config/tabs-browsing.mjs

source: browser/components/preferences/config/tabs-browsing.mjs
source-hash: 4f4aa1a0d9a52f2d9bdc29bab71d97f359c1a680
lines: 922

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Preferences.addAll()`, `Preferences.addSetting()`, `Services.prefs.getBoolPref()`, `SettingGroupManager.registerGroups()`, `XPCOMUtils.declareLazy()`

## get()
- 位置: L158-160
- 役割: (未記入)
- 触るとき: (未記入)

## set()
- 位置: L167-169
- 役割: (未記入)
- 触るとき: (未記入)

## get()
- 位置: L189-191
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT`
- XPCOM: [`nsIBrowserDOMWindow`](../../../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md)

## set()
- 位置: L202-206
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT`, `setting.pref.defaultValue`
- XPCOM: [`nsIBrowserDOMWindow`](../../../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md)

## onUserChange()
- 位置: L207-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.linkHandling.openNextToActiveTabSettingsChange.record()`, `Glean.linkHandling.openNextToActiveTabSettingsEnabled.set()`

## visible()
- 位置: L226-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TransientPrefs.prefShouldBeVisible()`

## onUserClick()
- 位置: L237-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## visible()
- 位置: L249-249
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabHoverPreview.value`

## visible()
- 位置: L268-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.locale.appLocaleAsBCP47.startsWith()`, `window.canShowAiFeature()`
- 参照: `smartTabGroups.value`, `tabGroups.value`
- XPCOM: `Services.locale`

## visible()
- 位置: L286-286
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabGroups.value`

## visible()
- 位置: L298-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`, `parseFloat()`
- XPCOM: `Services.sysinfo`

## visible()
- 位置: L309-309
- 役割: (未記入)
- 触るとき: (未記入)

## visible()
- 位置: L320-320
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `privacyUserContextUI.value`

## promptToCloseTabsAndDisable()
- 位置: async L329-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmEx()`, `document.l10n.formatValues()`
- 条件付き依存: `if (rv == 0)` → `lazy.ContextualIdentityService.closeContainerTabs()`
- 参照: `Ci.nsIPrompt.BUTTON_POS_0`, `Ci.nsIPrompt.BUTTON_POS_1`, `Ci.nsIPrompt.BUTTON_TITLE_IS_STRING`, `setting.pref.value`
- XPCOM: [`nsIPrompt`](../../../../netwerk/base/nsIAuthPrompt.idl.md) / `Services.prompt`

## set()
- 位置: L363-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.countContainerTabs()`, `this.promptToCloseTabsAndDisable()`

## onUserClick()
- 位置: L387-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gotoPref()`

## disabled()
- 位置: L390-390
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `browserContainersCheckbox.value`

## setup()
- 位置: L414-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.browsingContext.topChromeWindow.document.getElementById()`
- 条件付き依存: `if (quitKeyElement)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 参照: `this.quitKey`

## visible()
- 位置: L423-425
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AppConstants.platform`, `this.quitKey`

## getControlConfig()
- 位置: L426-431
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.quitKey`

## visible()
- 位置: L449-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.canShowAiFeature()`
- 参照: `lazy.LinkPreview.canShowPreferences`

## visible()
- 位置: L462-462
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.LinkPreview.canShowKeyPoints`

## availableHighlightToSearchActions()
- 位置: L470-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HIGHLIGHT_TO_SEARCH_ACTIONS.map()`, `HIGHLIGHT_TO_SEARCH_ACTIONS.map(id => Preferences.getSetting(id) ).filter()`, `Preferences.getSetting()`
- 参照: `action.visible`

## onHighlightToSearchActionChange()
- 位置: L479-483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `availableHighlightToSearchActions()`, `availableHighlightToSearchActions().some()`
- 条件付き依存: `if (!checked && !availableHighlightToSearchActions().some(a => a.value))` → `Preferences.getSetting()`
- 参照: `Preferences.getSetting("highlightToSearchEnabled").value`, `a.value`

## visible()
- 位置: L493-494
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `highlightToSearchFeatureGate.value`

## onUserChange()
- 位置: L495-502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actions.some()`, `availableHighlightToSearchActions()`
- 参照: `action.value`

## visible()
- 位置: L508-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.canShowAiFeature()`
- 参照: `lazy.GenAI.canOfferChatbot`

## getControlConfig()
- 位置: L512-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.GenAI.chatProviders.get()`
- 参照: `chatbotProvider.value`, `lazy.GenAI.chatProviders.get(chatbotProvider.value)?.name`

## visible()
- 位置: L533-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onUserChange()
- 位置: L537-541
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!checked)` → `Glean.pictureinpictureSettings.disableSettings.record()`

## onUserChange()
- 位置: L547-551
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (checked)` → `Glean.pictureinpictureSettings.enableAutotriggerSettings.record()`

## visible()
- 位置: L556-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (lazy.AppConstants.platform == "win")` → `parseFloat()`
- 条件付き依存: `if (lazy.AppConstants.platform == "win")` → `Services.sysinfo.get()`
- 参照: `lazy.AppConstants.platform`
- XPCOM: `Services.prefs` / `Services.sysinfo`

## visible()
- 位置: L580-582
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `useRecommendedPerformanceSettings.value`

## get()
- 位置: L588-596
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `allowHWAccel.pref.defaultValue`, `allowHWAccel.value`, `contentProcessCount.pref.defaultValue`, `contentProcessCount.value`

## set()
- 位置: L597-603
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `allowHWAccel.pref.defaultValue`, `allowHWAccel.value`, `contentProcessCount.pref.defaultValue`, `contentProcessCount.value`

## get()
- 位置: L620-620
- 役割: (未記入)
- 触るとき: (未記入)

## set()
- 位置: L621-621
- 役割: (未記入)
- 触るとき: (未記入)
