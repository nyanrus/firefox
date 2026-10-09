# browser/components/preferences/config/languages.mjs

source: browser/components/preferences/config/languages.mjs
source-hash: 7dd8ff65d59e4b3fc997d44594dbdcb5a1659d8c
lines: 988

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `Preferences.addAll()`, `Preferences.addSetting()`, `Preferences.getSetting()`, `Promise.resolve()`, `Services.urlFormatter.formatURLPref()`, `SettingGroupManager.registerGroups()`

## installedLocales()
- 位置: async L54-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LangPackMatcher.getAvailableLocales()`, `this.localizeArray()`

## localizeArray()
- 位置: L75-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a[0].localeCompare()`, `list .map()`, `list.map()`, `this.getLocaleDisplayNames()`, `transform()`

## getLocaleDisplayNames()
- 位置: L94-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.intl.getLocaleDisplayNames()`
- XPCOM: `Services.intl`

## getTransitionType()
- 位置: L107-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `appLocalesAsBCP47.join()`, `newLocales.join()`
- 条件付き依存: `if (Services.prefs.getBoolPref("intl.multilingual.liveReload"))` → `Services.intl.getScriptDirection()`
- 条件付き依存: `if (Services.prefs.getBoolPref("intl.multilingual.liveReload"))` → `Services.prefs.getBoolPref()`
- 参照: `Multilingual.TransitionType.LiveReload`, `Multilingual.TransitionType.LocalesMatch`, `Multilingual.TransitionType.RestartRequired`, `Services.locale`
- XPCOM: `Services.intl` / `Services.locale` / `Services.prefs`

## recordTelemetry()
- 位置: L135-153
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (method == "apply")` → `Glean.intlUiBrowserLanguage.applyMain.record()`
- 条件付き依存: `if (method == "reorder")` → `Glean.intlUiBrowserLanguage.reorderMain.record()`
- 条件付き依存: `if (method == "add")` → `Glean.intlUiBrowserLanguage.addDialog.record()`
- 条件付き依存: `if (method == "add")` → `String()`
- 条件付き依存: `if (method == "search")` → `Glean.intlUiBrowserLanguage.searchMain.record()`
- 条件付き依存: `if (method == "manage")` → `Glean.intlUiBrowserLanguage.manageMain.record()`

## applyAndRestart()
- 位置: L158-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`, `this.recordTelemetry()`
- 条件付き依存: `if (!cancelQuit.data)` → `Services.startup.quit()`
- 参照: `Ci.nsISupportsPRBool`, `Services.locale.requestedLocales`, `Services.startup.eAttemptQuit`, `Services.startup.eRestart`, `cancelQuit.data`
- XPCOM: [`nsISupportsPRBool`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.locale` / `Services.obs` / `Services.startup`

## ensureLangPackInstalled()
- 位置: async L183-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LangPackMatcher.ensureLangPackInstalled()`, `this.recordTelemetry()`

## makeBrowserLanguageOption()
- 位置: L211-218
- 役割: (未記入)
- 触るとき: (未記入)

## BrowserLanguagesSetting.currentLocale()
- 位置: L232-234
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## BrowserLanguagesSetting.pendingLocale()
- 位置: L236-238
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#pendingLocales`

## BrowserLanguagesSetting.restartRequired()
- 位置: L240-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `this.#pendingLocales?.length`

## BrowserLanguagesSetting.installing()
- 位置: L244-246
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#installing`

## BrowserLanguagesSetting.installError()
- 位置: L248-250
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#installError`

## BrowserLanguagesSetting.#updateLocales()
- 位置: L255-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Multilingual.getTransitionType()`, `this.emitChange()`
- 参照: `Multilingual.TransitionType.LiveReload`, `Multilingual.TransitionType.LocalesMatch`, `Multilingual.TransitionType.RestartRequired`, `Services.locale.requestedLocales`, `this.#pendingLocales`
- XPCOM: `Services.locale`

## BrowserLanguagesSetting.#ensureLocaleInstalled()
- 位置: async L278-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this.installedLocales).find()`, `remoteLocales.find()`
- 条件付き依存: `if (remote)` → `this.emitChange()`
- 条件付き依存: `if (remote)` → `Multilingual.ensureLangPackInstalled()`
- 参照: `locale.code`, `remote.langpack`, `this.#installing`, `this.installedLocales`

## BrowserLanguagesSetting.setup()
- 位置: L301-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `this.multilingualEnabled.off()`, `this.multilingualEnabled.on()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs`

## BrowserLanguagesSetting.beforeRefresh()
- 位置: L310-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Multilingual.installedLocales()`
- 参照: `this.installedLocales`

## BrowserLanguagesSetting.get()
- 位置: async L315-319
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.locale.appLocalesAsBCP47`, `this.#pendingLocales`
- XPCOM: `Services.locale`

## BrowserLanguagesSetting.visible()
- 位置: async L321-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `this.multilingualEnabled.value`

## BrowserLanguagesSetting.getPreferred()
- 位置: async L325-327
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.currentLocale`, `this.pendingLocale`

## BrowserLanguagesSetting.setPreferred()
- 位置: async L333-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `new Set([code, ...Services.locale.requestedLocales]).values()`, `this.#ensureLocaleInstalled()`, `this.#updateLocales()`
- 条件付き依存: `if (code == this.currentLocale)` → `this.emitChange()`
- 条件付き依存: `if (!locale)` → `this.emitChange()`
- 条件付き依存: `if (!locale.langpack)` → `Multilingual.recordTelemetry()`
- 参照: `Services.locale.requestedLocales`, `locale.langpack`, `this.#installError`, `this.#pendingLocales`, `this.currentLocale`
- XPCOM: `Services.locale`

## BrowserLanguagesSetting.getFallback()
- 位置: async L357-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.get()`

## BrowserLanguagesSetting.setFallback()
- 位置: async L368-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Multilingual.recordTelemetry()`, `this.#updateLocales()`, `this.get()`

## BrowserLanguagesSetting.applyAndRestart()
- 位置: L374-378
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.restartRequired)` → `Multilingual.applyAndRestart()`
- 参照: `this.#pendingLocales`, `this.restartRequired`

## BrowserLanguageRemoteLocalesSetting.setup()
- 位置: L394-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#multilingualDownloadEnabled.off()`, `this.#multilingualDownloadEnabled.on()`, `window.addEventListener()`
- 参照: `this.emitChange`

## onPaneshown()
- 位置: L397-403
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.detail.category == "paneLanguages")` → `this.emitChange()`
- 条件付き依存: `if (e.detail.category == "paneLanguages")` → `window.removeEventListener()`
- 参照: `e.detail.category`, `this.#languagesLoaded`

## BrowserLanguageRemoteLocalesSetting.get()
- 位置: async L415-423
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#cache)` → `this.#fetch()`
- 参照: `this.#cache`, `this.#languagesLoaded`, `this.#multilingualDownloadEnabled.value`

## BrowserLanguageRemoteLocalesSetting.#fetch()
- 位置: async L425-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LangPackMatcher.mockable.getAvailableLangpacks()`, `Multilingual.localizeArray()`, `console.error()`
- 参照: `langpack.target_locale`

## BrowserLanguagePreferredSetting.#browserLanguages()
- 位置: L459-467
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `( this.#browserLanguagesSetting.config ).asyncSetting`, `this.#browserLanguagesSetting.config`

## BrowserLanguagePreferredSetting.setup()
- 位置: L469-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserLanguagesSetting.off()`, `this.#browserLanguagesSetting.on()`, `this.#remoteLocalesSetting.off()`, `this.#remoteLocalesSetting.on()`
- 参照: `this.emitChange`

## BrowserLanguagePreferredSetting.#remoteLocales()
- 位置: L478-484
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#remoteLocalesSetting.value`

## BrowserLanguagePreferredSetting.get()
- 位置: async L486-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserLanguages.getPreferred()`

## BrowserLanguagePreferredSetting.set()
- 位置: async L493-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserLanguages.setPreferred()`
- 参照: `this.#remoteLocales`

## BrowserLanguagePreferredSetting.disabled()
- 位置: async L497-499
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#browserLanguages.installing`

## BrowserLanguagePreferredSetting.visible()
- 位置: async L501-503
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#browserLanguagesSetting.visible`

## BrowserLanguagePreferredSetting.getControlConfig()
- 位置: async L505-517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `installed.map()`, `installed.some()`, `remote.map()`, `this.#remoteLocales.filter()`
- 参照: `i.code`, `r.code`, `remote.length`, `this.#browserLanguages.installedLocales`

## BrowserLanguageFallbackSetting.#languages()
- 位置: L527-534
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `(this.#browserLanguages.config) .asyncSetting`, `this.#browserLanguages.config`

## BrowserLanguageFallbackSetting.setup()
- 位置: L536-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserLanguages.off()`, `this.#browserLanguages.on()`
- 参照: `this.emitChange`

## BrowserLanguageFallbackSetting.get()
- 位置: async L541-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#languages.getFallback()`

## BrowserLanguageFallbackSetting.set()
- 位置: async L548-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#languages.setFallback()`

## BrowserLanguageFallbackSetting.disabled()
- 位置: async L552-554
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#languages.installing`

## BrowserLanguageFallbackSetting.visible()
- 位置: async L556-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#languages.getPreferred()`
- 参照: `Services.locale.defaultLocale`, `installed.length`, `this.#browserLanguages.visible`, `this.#languages.installedLocales`
- XPCOM: `Services.locale`

## BrowserLanguageFallbackSetting.getControlConfig()
- 位置: async L569-577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `installed.map()`, `makeBrowserLanguageOption()`, `this.#languages.get()`
- 参照: `locale.code`, `this.#languages.installedLocales`

## visible()
- 位置: L584-592
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.browserLanguages.config`, `handler.asyncSetting`, `setting.installError`, `setting.restartRequired`

## visible()
- 位置: L598-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `appLocale.split()`, `systemLocale.split()`
- 参照: `Services.locale.appLocaleAsBCP47`, `Services.locale.regionalPrefsLocales`, `regionalPrefsLocales.length`
- XPCOM: `Services.locale`

## get()
- 位置: L612-616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.locale.acceptLanguages.toLowerCase()`, `prefVal.toLowerCase()`
- 参照: `setting.pref.defaultValue`
- XPCOM: `Services.locale`

## get()
- 位置: L621-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.intl.getLocaleDisplayNames()`, `Services.strings.createBundle()`, `_acceptLanguages.includes()`, `acceptLanguages.value.split()`, `availableLanguages.push()`, `bundle.getSimpleEnumeration()`, `currString.key.split()`
- 条件付き依存: `if (property[1] == "accept")` → `localeCodes.push()`
- 条件付き依存: `if (property[1] == "accept")` → `localeValues.push()`
- 参照: `currString.value`
- XPCOM: `Services.intl` / `Services.strings`

## onUserReorder()
- 位置: L664-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(deps.acceptLanguages.value) .split()`, `(deps.acceptLanguages.value) .split(re) .filter()`, `(event.target).reorderArrayFromEvent()`, `languages.join()`
- 参照: `deps.acceptLanguages.value`, `event.target`

## getControlConfig()
- 位置: L675-718
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.intl.getLocaleDisplayNames()`, `availableLanguages.push()`, `languagePref .toLowerCase()`, `languagePref .toLowerCase() .split()`, `languagePref .toLowerCase() .split(/\s*,\s*/) .filter()`
- 参照: `code.length`, `config.options`, `deps.acceptLanguages.value`, `localeCodes.length`
- XPCOM: `Services.intl`

## onUserClick()
- 位置: L719-736
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.getAttribute()`
- 条件付き依存: `if (action === "remove")` → `deps.acceptLanguages.value.split()`
- 条件付き依存: `if (action === "remove")` → `acceptedLanguages.filter()`
- 条件付き依存: `if (action === "remove")` → `filteredLanguages.join()`
- 条件付き依存: `if (action === "remove")` → `e.target.closest()`
- 条件付き依存: `if (action === "remove")` → `closestBoxItem.nextElementSibling.focus()`
- 条件付き依存: `if (action === "remove")` → `closestBoxItem.previousElementSibling.focus()`
- 参照: `closestBoxItem.nextElementSibling`, `deps.acceptLanguages.value`

## onUserClick()
- 位置: L742-758
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentLanguages.includes()`, `currentLanguages.join()`, `currentLanguages.unshift()`, `deps.acceptLanguages.value.split()`
- 参照: `deps.acceptLanguages.value`, `deps.websiteLanguagePicker.value`

## getControlConfig()
- 位置: L766-797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(deps.acceptLanguages.value).split()`, `acceptLanguages.has()`, `availableLanguages.map()`, `comp.compare()`, `sortedOptions.sort()`
- 参照: `Services.intl.Collator`, `a.l10nArgs.locale`, `b.l10nArgs.locale`, `config.options`, `deps.acceptLanguages.value`, `deps.availableLanguages.value`, `locale.code`, `locale.displayName`, `locale.isVisible`
- XPCOM: `Services.intl`

## get()
- 位置: L798-806
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deps.acceptLanguages.value.split()`, `deps.acceptLanguages.value.split(",").includes()`
- 参照: `this.inputValue`

## set()
- 位置: L807-809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`
- 参照: `this.inputValue`

## visible()
- 位置: L817-818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `canShowAiFeature()`

## get()
- 位置: L824-824
- 役割: (未記入)
- 触るとき: (未記入)

## set()
- 位置: L825-825
- 役割: (未記入)
- 触るとき: (未記入)

## onUserClick()
- 位置: L839-842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `gotoPref()`

## visible()
- 位置: L843-844
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `canShowAiFeature()`

## l10nArgs()
- 位置: L867-879
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.intl.getLocaleDisplayNames()`
- 参照: `Services.locale.regionalPrefsLocales`, `regionalPrefsLocales.length`
- XPCOM: `Services.intl` / `Services.locale`
