# browser/components/preferences/dialogs/browserLanguages.js

source: browser/components/preferences/dialogs/browserLanguages.js
source-hash: bc5f95d6cf9c46292048d31d2d3184085b0ad25e
lines: 720

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `gBrowserLanguagesDialog.onLoad()`, `window.addEventListener()`

## installFromUrl()
- 位置: async L30-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getInstallForURL()`, `install.install()`
- 条件付き依存: `if (callback)` → `callback()`
- 条件付き依存: `if (callback)` → `install.installId.toString()`
- 参照: `install.addon`

## dictionaryIdsForLocale()
- 位置: async L45-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RemoteSettings()`, `RemoteSettings("language-dictionaries").get()`
- 参照: `entries.length`, `entries[0].dictionaries`

## OrderedListBox.constructor()
- 位置: L56-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.downButton.addEventListener()`, `this.moveDown()`, `this.moveUp()`, `this.removeButton.addEventListener()`, `this.removeItem()`, `this.richlistbox.addEventListener()`, `this.setButtonState()`, `this.upButton.addEventListener()`
- 参照: `this.downButton`, `this.items`, `this.onRemove`, `this.onReorder`, `this.removeButton`, `this.richlistbox`, `this.upButton`

## OrderedListBox.selectedItem()
- 位置: L79-81
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.items`, `this.richlistbox.selectedIndex`

## OrderedListBox.setButtonState()
- 位置: L83-89
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `downButton.disabled`, `removeButton.disabled`, `this.richlistbox`, `this.selectedItem.canRemove`, `upButton.disabled`

## OrderedListBox.moveUp()
- 位置: L91-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.onReorder()`, `this.richlistbox.ensureElementIsVisible()`, `this.richlistbox.insertBefore()`, `this.setButtonState()`
- 参照: `prevItem.id`, `selectedItem.id`, `this.richlistbox`

## OrderedListBox.moveDown()
- 位置: L110-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.onReorder()`, `this.richlistbox.ensureElementIsVisible()`, `this.richlistbox.insertBefore()`, `this.setButtonState()`
- 参照: `nextItem.id`, `selectedItem.id`, `this.items.length`, `this.richlistbox`

## OrderedListBox.removeItem()
- 位置: L129-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `this.items.splice()`, `this.onRemove()`, `this.richlistbox.ensureElementIsVisible()`, `this.richlistbox.selectedItem.remove()`
- 参照: `this.richlistbox`, `this.richlistbox.itemCount`, `this.richlistbox.selectedIndex`, `this.richlistbox.selectedItem`

## OrderedListBox.setItems()
- 位置: L146-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.populate()`, `this.setButtonState()`
- 参照: `this.items`

## OrderedListBox.addItem()
- 位置: L157-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.createItem()`, `this.items.unshift()`, `this.richlistbox.ensureElementIsVisible()`, `this.richlistbox.insertBefore()`
- 参照: `this.richlistbox.firstElementChild`, `this.richlistbox.selectedIndex`, `this.richlistbox.selectedItem`

## OrderedListBox.populate()
- 位置: L167-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createDocumentFragment()`, `frag.appendChild()`, `this.createItem()`, `this.richlistbox.appendChild()`, `this.richlistbox.ensureElementIsVisible()`
- 参照: `this.items`, `this.richlistbox.selectedIndex`, `this.richlistbox.selectedItem`, `this.richlistbox.textContent`

## OrderedListBox.createItem()
- 位置: L180-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `listitem.appendChild()`, `listitem.setAttribute()`
- 参照: `labelEl.textContent`, `listitem.id`

## SortedItemSelectList.constructor()
- 位置: L197-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.addEventListener()`, `menulist.getAttribute()`, `menulist.selectedItem.remove()`, `menulist.setAttribute()`, `onSelect()`, `this.items.splice()`
- 条件付き依存: `if (menulist.selectedItem)` → `onChange()`
- 参照: `button.disabled`, `menulist.disabled`, `menulist.itemCount`, `menulist.menupopup`, `menulist.selectedIndex`, `menulist.selectedItem`, `this.button`, `this.compareFn`, `this.items`, `this.menulist`, `this.popup`

## SortedItemSelectList.setItems()
- 位置: L239-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.sort()`, `this.populate()`
- 参照: `this.compareFn`, `this.items`

## SortedItemSelectList.populate()
- 位置: L244-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createDocumentFragment()`, `frag.appendChild()`, `menulist.getAttribute()`, `menulist.setAttribute()`, `popup.appendChild()`, `this.createItem()`
- 参照: `button.disabled`, `menulist.disabled`, `menulist.itemCount`, `menulist.selectedIndex`, `popup.textContent`

## SortedItemSelectList.addItem()
- 位置: L265-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `compareFn()`, `items.findIndex()`, `items.splice()`, `menulist.getItemAtIndex()`, `popup.insertBefore()`, `this.createItem()`
- 参照: `menulist.disabled`, `menulist.itemCount`

## SortedItemSelectList.createItem()
- 位置: L276-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `item.setAttribute()`
- 条件付き依存: `if (className)` → `item.classList.add()`
- 条件付き依存: `if (disabled)` → `item.setAttribute()`
- 参照: `item.value`

## SortedItemSelectList.disableWithMessageId()
- 位置: L295-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `this.menulist.setAttribute()`
- 参照: `this.button.disabled`, `this.menulist`, `this.menulist.disabled`

## SortedItemSelectList.enableWithMessageId()
- 位置: L309-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `this.menulist.removeAttribute()`
- 参照: `this.button.disabled`, `this.menulist`, `this.menulist.disabled`, `this.menulist.itemCount`, `this.menulist.selectedItem`

## getLocaleDisplayInfo()
- 位置: async L331-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LangPackMatcher.getAvailableLocales()`, `Services.intl.getLocaleDisplayNames()`, `availableLocales.has()`, `localeCodes.map()`
- 参照: `Services.locale.defaultLocale`
- XPCOM: `Services.intl` / `Services.locale`

## compareItems()
- 位置: L354-374
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (a.value && b.value)` → `a.label.localeCompare()`
- 参照: `a.installed`, `a.value`, `b.installed`, `b.label`, `b.value`

## downloadEnabled()
- 位置: L404-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## recordTelemetry()
- 位置: L409-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.intlUiBrowserLanguage[method + "Dialog"].record()`
- 参照: `Glean.intlUiBrowserLanguage`, `extra.value`, `this._telemetryId`

## onLoad()
- 位置: async L414-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LangPackMatcher.getAvailableLocales()`, `available.filter()`, `availableSet.has()`, `document .getElementById()`, `document .getElementById("BrowserLanguagesDialog") .addEventListener()`, `selectedLocaleSet.has()`, `selectedLocales.filter()`, `this._selectedLocalesUI.items.map()`, `this.initAvailableLocales()`, `this.initSelectedLocales()`
- 参照: `Services.locale.appLocalesAsBCP47`, `item.value`, `this._telemetryId`, `this.initialized`, `this.selected`, `window.arguments`
- XPCOM: `Services.locale`

## initSelectedLocales()
- 位置: async L465-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `getLocaleDisplayInfo()`, `this._selectedLocalesUI.setItems()`
- 参照: `this._selectedLocalesUI`

## onRemove()
- 位置: L471-471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedLocaleRemoved()`

## onReorder()
- 位置: L472-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.recordTelemetry()`

## initAvailableLocales()
- 位置: async L484-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.loadLocalesFromInstalled()`
- 条件付き依存: `if (search)` → `this.loadLocalesFromAMO()`
- 参照: `this._availableLocalesUI`

## onSelect()
- 位置: L489-489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.availableLanguageSelected()`

## onChange()
- 位置: L490-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideError()`
- 条件付き依存: `if (item.value == "search")` → `this.recordTelemetry()`
- 条件付き依存: `if (item.value == "search")` → `this.loadLocalesFromAMO()`
- 参照: `item.value`

## loadLocalesFromAMO()
- 位置: async L514-566
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonRepository.getAvailableLangpacks()`, `LangPackMatcher.getAvailableLocales()`, `availableItems.push()`, `availableLangpacks .filter()`, `availableLangpacks .filter(({ target_locale }) => !installedLocales.has(target_locale)) .map()`, `document.l10n.formatValue()`, `getLocaleDisplayInfo()`, `installedLocales.has()`, `items.concat()`, `items.pop()`, `this._availableLocalesUI.disableWithMessageId()`, `this._availableLocalesUI.enableWithMessageId()`, `this._availableLocalesUI.setItems()`, `this.availableLangpacks.set()`, `this.showError()`
- 参照: `lang.target_locale`, `this._availableLocalesUI.items`, `this.availableLangpacks`, `this.downloadEnabled`

## loadLocalesFromInstalled()
- 位置: async L571-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._availableLocalesUI.setItems()`
- 条件付き依存: `if (available.length)` → `getLocaleDisplayInfo()`
- 条件付き依存: `if (available.length)` → `items.push()`
- 条件付き依存: `if (available.length)` → `this.createInstalledLabel()`
- 条件付き依存: `if (this.downloadEnabled)` → `items.push()`
- 条件付き依存: `if (this.downloadEnabled)` → `document.l10n.formatValue()`
- 参照: `available.length`, `this.downloadEnabled`

## availableLanguageSelected()
- 位置: async L591-601
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await LangPackMatcher.getAvailableLocales()).includes()`, `LangPackMatcher.getAvailableLocales()`
- 条件付き依存: `if ((await LangPackMatcher.getAvailableLocales()).includes(item.value))` → `this.recordTelemetry()`
- 条件付き依存: `if ((await LangPackMatcher.getAvailableLocales()).includes(item.value))` → `this.requestLocalLanguage()`
- 条件付き依存: `if (!((await LangPackMatcher.getAvailableLocales()).includes(item.value)))` → `this.availableLangpacks.has()`
- 条件付き依存: `if (this.availableLangpacks.has(item.value))` → `this.requestRemoteLanguage()`
- 条件付き依存: `if (!(this.availableLangpacks.has(item.value)))` → `this.showError()`
- 参照: `item.value`

## requestLocalLanguage()
- 位置: async L606-619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LangPackMatcher.getAvailableLocales()`, `this._availableLocalesUI.enableWithMessageId()`, `this._selectedLocalesUI.addItem()`
- 条件付き依存: `if (selectedCount == availableCount)` → `this._availableLocalesUI.items.shift()`
- 条件付き依存: `if (selectedCount == availableCount)` → `this._availableLocalesUI.setItems()`
- 参照: `(await LangPackMatcher.getAvailableLocales()).length`, `this._availableLocalesUI.items`, `this._selectedLocalesUI.items.length`

## requestRemoteLanguage()
- 位置: async L624-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `installFromUrl()`, `this._availableLocalesUI.disableWithMessageId()`, `this._availableLocalesUI.enableWithMessageId()`, `this._selectedLocalesUI.addItem()`, `this.availableLangpacks.get()`, `this.installDictionariesForLanguage()`, `this.recordTelemetry()`, `this.showError()`
- 条件付き依存: `if (addon.userDisabled)` → `addon.enable()`
- 参照: `addon.userDisabled`, `item.installed`, `item.value`

## installDictionariesForLanguage()
- 位置: async L661-671
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonRepository.getAddonsByIDs()`, `Promise.all()`, `addonInfos.map()`, `console.error()`, `dictionaryIdsForLocale()`, `installFromUrl()`
- 参照: `info.sourceURI.spec`

## showError()
- 位置: L673-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialogs.findIndex()`, `document.getElementById()`, `requestAnimationFrame()`, `this._availableLocalesUI.enableWithMessageId()`
- 条件付き依存: `if (index != -1)` → `dialogs[index].resizeDialog()`
- 参照: `d._frame.contentDocument`, `document.getElementById("warning-message").hidden`, `window.opener.gSubDialog._dialogs`

## hideError()
- 位置: L689-691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `document.getElementById("warning-message").hidden`

## selectedLocaleRemoved()
- 位置: async L696-705
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._availableLocalesUI.addItem()`, `this.recordTelemetry()`
- 条件付き依存: `if (this._availableLocalesUI.items[0] == item)` → `this._availableLocalesUI.addItem()`
- 条件付き依存: `if (this._availableLocalesUI.items[0] == item)` → `this.createInstalledLabel()`
- 参照: `this._availableLocalesUI.items`

## createInstalledLabel()
- 位置: async L707-716
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatValue()`
