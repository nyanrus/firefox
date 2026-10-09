# browser/components/preferences/dialogs/languages.js

source: browser/components/preferences/dialogs/languages.js
source-hash: 9e1b4608a5d21106603724eeaf3bd19f05e89ad1
lines: 440

## <module>
- 役割: (未記入)
- 呼び出し先: `Preferences.addAll()`, `Preferences.addSetting()`, `window.addEventListener()`

## get()
- 位置: L17-21
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.locale.acceptLanguages`, `setting.pref.defaultValue`
- XPCOM: `Services.locale`

## onLoad()
- 位置: L30-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.addSyncFromPrefListener()`, `Preferences.addSyncToPrefListener()`, `Preferences.getSetting()`, `Preferences.getSetting("acceptLanguages").on()`, `addListener()`, `document.getElementById()`, `gLanguagesDialog.readSpoofEnglish()`, `gLanguagesDialog.writeSpoofEnglish()`, `this._readAcceptLanguages()`, `this._readAcceptLanguages().catch()`
- 条件付き依存: `if (!this._availableLanguagesList.length)` → `this._loadAvailableLanguages()`
- 参照: `console.error`, `document.mozSubdialogReady`, `this._availableLanguagesList.length`

## addListener()
- 位置: L43-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById(id).addEventListener()`

## _activeLanguages()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## _availableLanguages()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## _loadAvailableLanguages()
- 位置: async L63-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.intl.getLocaleDisplayNames()`, `currString.key.split()`, `document.getElementById()`, `this._availableLanguagesList.push()`, `this._buildAvailableLanguageList()`, `this._readAcceptLanguages()`
- 条件付き依存: `if (property[1] == "accept")` → `localeCodes.push()`
- 条件付き依存: `if (property[1] == "accept")` → `localeValues.push()`
- 参照: `bundleAccepted.strings`, `currString.value`, `this._acceptLanguages`
- XPCOM: `Services.intl`

## LocaleInfo()
- 位置: L71-75
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.code`, `this.isVisible`, `this.name`

## _buildAvailableLanguageList()
- 位置: async L108-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `a.getAttribute()`, `availableLanguagesPopup.appendChild()`, `availableLanguagesPopup.firstChild.remove()`, `availableLanguagesPopup.hasChildNodes()`, `b.getAttribute()`, `comp.compare()`, `document.createDocumentFragment()`, `document.getElementById()`, `document.l10n.translateFragment()`, `frag.appendChild()`, `items.forEach()`, `items.sort()`, `this._availableLanguages.getAttribute()`, `this._availableLanguages.setAttribute()`
- 条件付き依存: `if ( locale.isVisible && (!(localeCode in this._acceptLanguages) || !this._acceptLanguages[localeCode]) )` → `document.createXULElement()`
- 条件付き依存: `if ( locale.isVisible && (!(localeCode in this._acceptLanguages) || !this._acceptLanguages[localeCode]) )` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( locale.isVisible && (!(localeCode in this._acceptLanguages) || !this._acceptLanguages[localeCode]) )` → `frag.appendChild()`
- 参照: `Services.intl.Collator`, `frag.children`, `locale.code`, `locale.isVisible`, `locale.name`, `menuitem.id`, `this._acceptLanguages`, `this._availableLanguagesList`, `this._availableLanguagesList.length`
- XPCOM: `Services.intl`

## _readAcceptLanguages()
- 位置: async L161-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `document.l10n.translateFragment()`, `listitem.appendChild()`, `preference.value.toLowerCase()`, `preference.value.toLowerCase().split()`, `this._activeLanguages.appendChild()`, `this._activeLanguages.firstChild.remove()`, `this._activeLanguages.hasChildNodes()`, `this._getLocaleName()`, `this.readSpoofEnglish()`
- 条件付き依存: `if (preference.value == "")` → `this.onLanguageSelect()`
- 条件付き依存: `if (this._activeLanguages.childNodes.length)` → `this._activeLanguages.ensureIndexIsVisible()`
- 参照: `languages.length`, `listitem.id`, `preference.value`, `this._acceptLanguages`, `this._activeLanguages`, `this._activeLanguages.childNodes.length`, `this._activeLanguages.selectedIndex`, `this._selectedItemID`

## handleEvent()
- 位置: L209-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.close()`, `this.addLanguage()`, `this.moveDown()`, `this.moveUp()`, `this.onLanguageSelect()`, `this.onLoad()`, `this.removeLanguage()`, `window.top.openPrefsHelp()`
- 条件付き依存: `if (event.currentTarget.id == "availableLanguages")` → `this.onAvailableLanguageSelect()`
- 参照: `event.currentTarget.id`, `event.target.id`, `event.type`

## onAvailableLanguageSelect()
- 位置: L248-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._availableLanguages.removeAttribute()`
- 参照: `addButton.disabled`, `availableLanguages.disabled`, `availableLanguages.selectedIndex`, `this._availableLanguages`

## addLanguage()
- 位置: L257-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`, `preference.value.toLowerCase()`, `preference.value.toLowerCase().split()`, `this._buildAvailableLanguageList()`, `this._buildAvailableLanguageList().catch()`, `this.onAvailableLanguageSelect()`
- 条件付き依存: `if (!(preference.value == ""))` → `arrayOfPrefs.unshift()`
- 条件付き依存: `if (!(preference.value == ""))` → `arrayOfPrefs.join()`
- 参照: `arrayOfPrefs.length`, `console.error`, `preference.value`, `this._acceptLanguages`, `this._availableLanguages.selectedItem`, `this._availableLanguages.selectedItem.id`, `this._selectedItemID`

## removeLanguage()
- 位置: L284-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`, `languagesArray.join()`, `this._buildAvailableLanguageList()`, `this._buildAvailableLanguageList().catch()`
- 条件付き依存: `if (!item.selected)` → `languagesArray.push()`
- 参照: `console.error`, `item.id`, `item.selected`, `lastSelected.nextSibling`, `lastSelected.previousSibling`, `preference.value`, `selectItem.id`, `selection.length`, `this._acceptLanguages`, `this._activeLanguages.childNodes`, `this._activeLanguages.childNodes.length`, `this._activeLanguages.selectedItems`, `this._selectedItemID`

## _getLocaleName()
- 位置: L312-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `localeCode.split()`
- 条件付き依存: `if (!this._availableLanguagesList.length)` → `this._loadAvailableLanguages()`
- 参照: `this._availableLanguagesList`, `this._availableLanguagesList.length`, `this._availableLanguagesList[i].code`, `this._availableLanguagesList[i].name`

## moveUp()
- 位置: L331-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`
- 参照: `item.id`, `preference.value`, `previousItem.id`, `selectedItem.id`, `selectedItem.previousSibling`, `this._activeLanguages.childNodes`, `this._activeLanguages.childNodes.length`, `this._activeLanguages.selectedItems`, `this._selectedItemID`

## moveDown()
- 位置: L355-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`
- 参照: `item.id`, `nextItem.id`, `preference.value`, `selectedItem.id`, `selectedItem.nextSibling`, `this._activeLanguages.childNodes`, `this._activeLanguages.childNodes.length`, `this._activeLanguages.selectedItems`, `this._selectedItemID`

## onLanguageSelect()
- 位置: L379-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `downButton.disabled`, `removeButton.disabled`, `this._activeLanguages.childNodes.length`, `this._activeLanguages.selectedCount`, `this._activeLanguages.selectedIndex`, `upButton.disabled`

## readSpoofEnglish()
- 位置: L401-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Services.prefs.getBoolPref()`, `activeLanguages.clearSelection()`, `activeLanguages.selectItem()`, `document.getElementById()`, `this.onAvailableLanguageSelect()`
- 参照: `Preferences.get("privacy.spoof_english").value`, `activeLanguages.disabled`, `activeLanguages.firstChild`, `availableLanguages.disabled`, `checkbox.hidden`, `this._activeLanguages`, `this._availableLanguages`
- XPCOM: `Services.prefs`

## writeSpoofEnglish()
- 位置: L434-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `document.getElementById("spoofEnglish").checked`
