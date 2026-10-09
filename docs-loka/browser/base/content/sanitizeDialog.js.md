# browser/base/content/sanitizeDialog.js

source: browser/base/content/sanitizeDialog.js
source-hash: 04d2253bb998827f1bb2f2201b4e9b178c39fe10
lines: 578

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Preferences.addAll()`, `gSanitizePromptDialog.init()`, `gSanitizePromptDialog.init().then()`, `window.addEventListener()`

## selectedTimespan()
- 位置: L64-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `parseInt()`
- 参照: `durList.value`

## warningBox()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## init()
- 位置: async L73-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Intl.DateTimeFormat()`, `Intl.DateTimeFormat(navigator.language, { hour: "numeric", minute: "numeric", }).format()`, `document .getElementById()`, `document .getElementById("sanitizeDurationChoice") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `document.l10n.setAttributes()`, `document.querySelector()`, `document.querySelectorAll()`, `new Date().setHours()`, `this._dialog.getButton()`, `this.getAndUpdateDataSizes()`, `this.registerSyncFromPrefListeners()`, `this.selectByTimespan()`, `this.showLoadingSpinners()`
- 条件付き依存: `if (arg.inBrowserWindow)` → `this._dialog.setAttribute()`
- 条件付き依存: `if (arg.inBrowserWindow)` → `this._observeTitleForChanges()`
- 条件付き依存: `if (arg.wrappedJSObject?.needNativeUI)` → `document .getElementById("sanitizeDurationChoice") .setAttribute()`
- 条件付き依存: `if (arg.wrappedJSObject?.needNativeUI)` → `document .getElementById()`
- 条件付き依存: `if (arg.wrappedJSObject?.needNativeUI)` → `document.querySelectorAll()`
- 条件付き依存: `if (arg.wrappedJSObject?.needNativeUI)` → `cb.setAttribute()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `this._dialog.setAttribute()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `clearPrivateDataGroupbox.remove()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `clearSiteDataGroupbox.remove()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `Sanitizer.maybeMigratePrefs()`
- 条件付き依存: `if (!(this._inClearOnShutdownNewDialog))` → `clearOnShutdownGroupbox.remove()`
- 条件付き依存: `if (this._inClearSiteDataNewDialog)` → `clearPrivateDataGroupbox.remove()`
- 条件付き依存: `if (!(this._inClearSiteDataNewDialog))` → `clearSiteDataGroupbox.remove()`
- 条件付き依存: `if (!(this._inClearSiteDataNewDialog))` → `Sanitizer.maybeMigratePrefs()`
- 条件付き依存: `if (lazy.AIWindow.isEnabled)` → `document.querySelectorAll()`
- 条件付き依存: `if (lazy.AIWindow.isEnabled)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `this.updatePrefs()`
- 条件付き依存: `if (!(this._inClearOnShutdownNewDialog))` → `this.sanitize()`
- 条件付き依存: `if (typeof onAccept === "function")` → `document.addEventListener()`
- 条件付き依存: `if (typeof onCancel === "function")` → `document.addEventListener()`
- 条件付き依存: `if ( this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING && !this._inClearOnShutdownNewDialog )` → `this.prepareWarning()`
- 条件付き依存: `if ( this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING && !this._inClearOnShutdownNewDialog )` → `document.getElementById()`
- 条件付き依存: `if ( this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING && !this._inClearOnShutdownNewDialog )` → `document.l10n.translateFragment()`
- 条件付き依存: `if ( this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING && !this._inClearOnShutdownNewDialog )` → `rootWin.promiseDocumentFlushed()`
- 参照: `Sanitizer.TIMESPAN_EVERYTHING`, `arg.inBrowserWindow`, `arg.mode`, `arg.wrappedJSObject`, `arg.wrappedJSObject?.needNativeUI`, `lazy.AIWindow.isEnabled`, `navigator.language`, `this._allCheckboxes`, `this._cacheCheckbox`, `this._cacheLoading`, `this._cookiesAndSiteDataCheckbox`, `this._cookiesLoading`, `this._dataSizesUpdated`, `this._dialog`, `this._inBrowserWindow`, `this._inClearOnShutdownNewDialog`, `this._inClearSiteDataNewDialog`, `this._inited`, `this._sinceMidnightSanitizeDurationOption`, `this.cacheSize`, `this.dataSizesFinishedUpdatingPromise`, `this.selectedTimespan`, `this.siteDataSizes`, `this.warningBox.hidden`, `window.arguments`, `window.browsingContext.topChromeWindow`

## updateAcceptButtonState()
- 位置: L232-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this._allCheckboxes).every()`, `this._dialog.getButton()`
- 参照: `acceptButton.disabled`, `cb.checked`, `this._allCheckboxes`

## selectByTimespan()
- 位置: async L240-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `this.updateDataSizesInUI()`
- 条件付き依存: `if (this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING)` → `this.prepareWarning()`
- 条件付き依存: `if (warningBox.hidden)` → `warningBox.nextElementSibling.getBoundingClientRect()`
- 条件付き依存: `if (warningBox.hidden)` → `warningBox.previousElementSibling.getBoundingClientRect()`
- 条件付き依存: `if (warningBox.hidden)` → `window.resizeBy()`
- 条件付き依存: `if (this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING)` → `this.updateDataSizesInUI()`
- 条件付き依存: `if (!warningBox.hidden)` → `warningBox.nextElementSibling.getBoundingClientRect()`
- 条件付き依存: `if (!warningBox.hidden)` → `warningBox.previousElementSibling.getBoundingClientRect()`
- 条件付き依存: `if (!warningBox.hidden)` → `window.resizeBy()`
- 参照: `Sanitizer.TIMESPAN_EVERYTHING`, `document.documentElement`, `this._inited`, `this.selectedTimespan`, `this.warningBox`, `warningBox.hidden`, `warningBox.nextElementSibling.getBoundingClientRect().top`, `warningBox.previousElementSibling.getBoundingClientRect().bottom`

## sanitize()
- 位置: L282-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Sanitizer.getClearRange()`, `Sanitizer.sanitize()`, `Sanitizer.sanitize(itemsToClear, options) .catch()`, `Sanitizer.sanitize(itemsToClear, options) .catch(console.error) .then()`, `console.error()`, `document.l10n.setAttributes()`, `event.preventDefault()`, `this._dialog.getButton()`, `this.getItemsToClear()`, `this.updatePrefs()`, `window.close()`
- 条件付き依存: `if (!this._inBrowserWindow)` → `lazy.SiteDataManager.updateSites()`
- 参照: `acceptButton.disabled`, `console.error`, `this._dialog.getButton("cancel").disabled`, `this._inBrowserWindow`, `this.selectedTimespan`

## prepareWarning()
- 位置: L326-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.hasNonSelectedItems()`
- 条件付き依存: `if (this.hasNonSelectedItems())` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this.hasNonSelectedItems()))` → `document.l10n.setAttributes()`

## _getItemPrefs()
- 位置: L342-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this._allCheckboxes).map()`, `checkbox.getAttribute()`
- 参照: `this._allCheckboxes`

## onReadGeneric()
- 位置: L352-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `this._dialog.getButton()`, `this._getItemPrefs()`, `this._getItemPrefs().some()`, `this.prepareWarning()`
- 参照: `Preferences.get(pref).value`, `this._dialog.getButton("accept").disabled`

## showLoadingSpinners()
- 位置: L374-381
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._cacheLoading`, `this._cacheLoading.hidden`, `this._cookiesLoading`, `this._cookiesLoading.hidden`

## hideLoadingSpinners()
- 位置: L386-393
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._cacheLoading`, `this._cacheLoading.hidden`, `this._cookiesLoading`, `this._cookiesLoading.hidden`

## getAndUpdateDataSizes()
- 位置: async L400-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.DownloadUtils.convertByteUnits()`, `lazy.SiteDataManager.getCacheSize()`, `lazy.SiteDataManager.getQuotaUsageForTimeRanges()`, `this.hideLoadingSpinners()`, `this.updateDataSizesInUI()`
- 条件付き依存: `if (this._inBrowserWindow)` → `lazy.SiteDataManager.updateSites()`
- 参照: `this._dataSizesUpdated`, `this._inBrowserWindow`, `this.cacheSize`, `this.siteDataSizes`

## updatePrefs()
- 位置: L443-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Services.prefs.setBoolPref()`, `Services.prefs.setIntPref()`, `this._getItemPrefs()`
- 参照: `Sanitizer.PREF_TIMESPAN`, `p.id`, `p.value`, `prefs.length`, `this.selectedTimespan`
- XPCOM: `Services.prefs`

## hasNonSelectedItems()
- 位置: L458-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `checkboxes[i].getAttribute()`, `document.querySelectorAll()`
- 参照: `checkboxes.length`, `pref.value`

## registerSyncFromPrefListeners()
- 位置: L472-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.addSyncFromPrefListener()`, `document.querySelectorAll()`, `this.onReadGeneric()`

## _titleChanged()
- 位置: L479-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.getAttribute()`
- 条件付き依存: `if (title)` → `document.getElementById()`
- 参照: `document.getElementById("titleText").textContent`

## _observeTitleForChanges()
- 位置: L486-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._mutObs.observe()`, `this._titleChanged()`
- 参照: `document.documentElement`, `this._mutObs`

## updateDataSizesInUI()
- 位置: async L500-544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.pauseObserving()`, `document.l10n.resumeObserving()`, `document.l10n.setAttributes()`, `document.l10n.translateElements()`, `window.resizeDialog()`
- 参照: `this._cacheCheckbox`, `this._cookiesAndSiteDataCheckbox`, `this._dataSizesUpdated`, `this._sinceMidnightSanitizeDurationOption`, `this.cacheSize`, `this.selectedTimespan`, `this.siteDataSizes`

## getItemsToClear()
- 位置: L551-559
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (cb.checked)` → `items.push()`
- 参照: `cb.checked`, `cb.id`, `this._allCheckboxes`
