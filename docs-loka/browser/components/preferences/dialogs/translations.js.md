# browser/components/preferences/dialogs/translations.js

source: browser/components/preferences/dialogs/translations.js
source-hash: d44d306b2f919f5de152e578fc8122cb1bb41c93
lines: 530

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `gTranslationsSettings.onLoad()`, `window.addEventListener()`

## Tree()
- 位置: L26-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._data`, `this._tree`, `this._tree.view`

## tree()
- 位置: L33-35
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._tree`

## isEmpty()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._data.length`

## hasSelection()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selection.count`

## getSelectedItems()
- 位置: L42-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `result.push()`, `this.selection.getRangeAt()`, `this.selection.getRangeCount()`
- 参照: `max.value`, `min.value`, `this._data`

## rowCount()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._data.length`

## getCellText()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._data`

## isSeparator()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)

## isSorted()
- 位置: L68-70
- 役割: (未記入)
- 触るとき: (未記入)

## isContainer()
- 位置: L71-73
- 役割: (未記入)
- 触るとき: (未記入)

## setTree()
- 位置: L74-74
- 役割: (未記入)
- 触るとき: (未記入)

## getImageSrc()
- 位置: L75-75
- 役割: (未記入)
- 触るとき: (未記入)

## getCellValue()
- 位置: L76-76
- 役割: (未記入)
- 触るとき: (未記入)

## cycleHeader()
- 位置: L77-77
- 役割: (未記入)
- 触るとき: (未記入)

## getRowProperties()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)

## getColumnProperties()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)

## getCellProperties()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)

## Lang()
- 位置: L90-93
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._label`, `this.langCode`

## toString()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._label`

## onLoad()
- 位置: L102-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `TranslationsParent.listNeverTranslateSites()`, `document.addEventListener()`, `this.getAlwaysTranslateLanguages()`, `this.getNeverTranslateLanguages()`, `this.onSelectAlwaysTranslateLanguage()`, `this.onSelectNeverTranslateLanguage()`, `this.onSelectNeverTranslateSite()`, `tree.addEventListener()`, `window.addEventListener()`
- 条件付き依存: `if (this._neverTranslateSiteTree)` → `this.removeObservers()`
- 参照: `this._alwaysTranslateLangs`, `this._alwaysTranslateLangsTree`, `this._neverTranslateLangs`, `this._neverTranslateLangsTree`, `this._neverTranslateSiteTree`, `this._neverTranslateSites`
- XPCOM: `Services.obs` / `Services.prefs`

## getLangsFromPref()
- 位置: L162-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.intl.getLanguageDisplayNames()`, `Services.prefs.getCharPref()`, `langArr.map()`, `langs.sort()`, `rawLangs.split()`
- XPCOM: `Services.intl` / `Services.prefs`

## getAlwaysTranslateLanguages()
- 位置: L184-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getLangsFromPref()`

## getNeverTranslateLanguages()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getLangsFromPref()`

## observe()
- 位置: L200-293
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aData === "cleared")` → `this._neverTranslateSites.splice()`
- 条件付き依存: `if (aData === "cleared")` → `this._neverTranslateSiteTree.tree.rowCountChanged()`
- 条件付き依存: `if (!(aData === "cleared"))` → `aSubject.QueryInterface()`
- 条件付き依存: `if (aData === "added")` → `this._neverTranslateSites.push()`
- 条件付き依存: `if (aData === "added")` → `this._neverTranslateSites.sort()`
- 条件付き依存: `if (aData === "added")` → `tree.rowCountChanged()`
- 条件付き依存: `if (aData === "added")` → `tree.invalidate()`
- 条件付き依存: `if (aData == "deleted")` → `this._neverTranslateSites.indexOf()`
- 条件付き依存: `if (aData == "deleted")` → `this._neverTranslateSites.splice()`
- 条件付き依存: `if (aData == "deleted")` → `this._neverTranslateSiteTree.tree.rowCountChanged()`
- 条件付き依存: `if (aTopic === "perm-changed")` → `this.onSelectNeverTranslateSite()`
- 条件付き依存: `if (aTopic === "nsPref:changed")` → `this.getAlwaysTranslateLanguages()`
- 条件付き依存: `if (alwaysTranslateLangsChange)` → `alwaysTranslateLangsTree.rowCountChanged()`
- 条件付き依存: `if (aTopic === "nsPref:changed")` → `alwaysTranslateLangsTree.invalidate()`
- 条件付き依存: `if (aTopic === "nsPref:changed")` → `this.onSelectAlwaysTranslateLanguage()`
- 条件付き依存: `if (aTopic === "nsPref:changed")` → `this.getNeverTranslateLanguages()`
- 条件付き依存: `if (neverTranslateLangsChange)` → `neverTranslateLangsTree.rowCountChanged()`
- 条件付き依存: `if (aTopic === "nsPref:changed")` → `neverTranslateLangsTree.invalidate()`
- 条件付き依存: `if (aTopic === "nsPref:changed")` → `this.onSelectNeverTranslateLanguage()`
- 参照: `Ci.nsIPermission`, `Services.perms.DENY_ACTION`, `perm.capability`, `perm.principal.origin`, `perm.type`, `removed.length`, `this._alwaysTranslateLangs`, `this._alwaysTranslateLangs.length`, `this._alwaysTranslateLangsTree._data`, `this._alwaysTranslateLangsTree.rowCount`, `this._alwaysTranslateLangsTree.tree`, `this._neverTranslateLangs`, `this._neverTranslateLangs.length`, `this._neverTranslateLangsTree._data`, `this._neverTranslateLangsTree.rowCount`, `this._neverTranslateLangsTree.tree`, `this._neverTranslateSiteTree.tree`, `this._neverTranslateSites.length`
- XPCOM: [`nsIPermission`](../../../../netwerk/base/nsIPermission.idl.md) / `Services.perms`

## handleEvent()
- 位置: L295-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onAlwaysTranslateLanguageKeyPress()`, `this.onNeverTranslateLanguageKeyPress()`, `this.onNeverTranslateSiteKeyPress()`, `this.onRemoveAllAlwaysTranslateLanguages()`, `this.onRemoveAllNeverTranslateLanguages()`, `this.onRemoveAllNeverTranslateSites()`, `this.onRemoveAlwaysTranslateLanguage()`, `this.onRemoveNeverTranslateLanguage()`, `this.onRemoveNeverTranslateSite()`, `this.onSelectAlwaysTranslateLanguage()`, `this.onSelectNeverTranslateLanguage()`, `this.onSelectNeverTranslateSite()`, `this.removeObservers()`, `window.close()`
- 参照: `event.currentTarget.id`, `event.target.id`, `event.type`

## _handleButtonDisabling()
- 位置: L365-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `aTree.hasSelection`, `aTree.isEmpty`, `document.getElementById("remove" + aIdPart).disabled`, `document.getElementById("removeAll" + aIdPart + "s").disabled`

## onSelectAlwaysTranslateLanguage()
- 位置: L375-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleButtonDisabling()`
- 参照: `this._alwaysTranslateLangsTree`

## onSelectNeverTranslateLanguage()
- 位置: L385-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleButtonDisabling()`
- 参照: `this._neverTranslateLangsTree`

## onSelectNeverTranslateSite()
- 位置: L395-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleButtonDisabling()`
- 参照: `this._neverTranslateSiteTree`

## _onRemoveLanguage()
- 位置: L409-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`, `Services.prefs.setCharPref()`, `langs.join()`, `langs.split()`, `langs.split(",").filter()`, `removed.includes()`, `tree.getSelectedItems()`, `tree.getSelectedItems().map()`
- 参照: `l.langCode`
- XPCOM: `Services.prefs`

## onRemoveAlwaysTranslateLanguage()
- 位置: L425-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onRemoveLanguage()`
- 参照: `this._alwaysTranslateLangsTree`

## onRemoveNeverTranslateLanguage()
- 位置: L436-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onRemoveLanguage()`
- 参照: `this._neverTranslateLangsTree`

## onRemoveNeverTranslateSite()
- 位置: L446-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.setNeverTranslateSiteByOrigin()`, `this._neverTranslateSiteTree.getSelectedItems()`

## onRemoveAllAlwaysTranslateLanguages()
- 位置: L457-459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setCharPref()`
- XPCOM: `Services.prefs`

## onRemoveAllNeverTranslateLanguages()
- 位置: L464-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setCharPref()`
- XPCOM: `Services.prefs`

## onRemoveAllNeverTranslateSites()
- 位置: L471-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.setNeverTranslateSiteByOrigin()`, `this._neverTranslateSiteTree.tree.rowCountChanged()`, `this._neverTranslateSites.splice()`, `this.onSelectNeverTranslateSite()`
- 参照: `removedNeverTranslateSites.length`, `this._neverTranslateSiteTree.isEmpty`, `this._neverTranslateSites.length`

## onAlwaysTranslateLanguageKeyPress()
- 位置: L495-499
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aEvent.keyCode == KeyEvent.DOM_VK_DELETE)` → `this.onRemoveAlwaysTranslateLanguage()`
- 参照: `KeyEvent.DOM_VK_DELETE`, `aEvent.keyCode`

## onNeverTranslateLanguageKeyPress()
- 位置: L504-508
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aEvent.keyCode == KeyEvent.DOM_VK_DELETE)` → `this.onRemoveNeverTranslateLanguage()`
- 参照: `KeyEvent.DOM_VK_DELETE`, `aEvent.keyCode`

## onNeverTranslateSiteKeyPress()
- 位置: L513-517
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aEvent.keyCode == KeyEvent.DOM_VK_DELETE)` → `this.onRemoveNeverTranslateSite()`
- 参照: `KeyEvent.DOM_VK_DELETE`, `aEvent.keyCode`

## removeObservers()
- 位置: L522-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`
- XPCOM: `Services.obs` / `Services.prefs`
