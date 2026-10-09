# browser/components/preferences/dialogs/siteDataSettings.js

source: browser/components/preferences/dialogs/siteDataSettings.js
source-hash: 07bbb54e233d1c6981bb1a2a1456ae5a6f6f90eb
lines: 334

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `gSiteDataSettings.init()`, `window.addEventListener()`

## _createSiteListItem()
- 位置: L28-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addColumnItem()`, `document.createXULElement()`, `item.appendChild()`, `item.setAttribute()`, `this._absoluteTimeFormat.format()`, `this._relativeTimeFormat.formatBestUnit()`
- 条件付き依存: `if (site.usage > 0 || site.persisted)` → `DownloadUtils.convertByteUnits()`
- 条件付き依存: `if (site.usage > 0 || site.persisted)` → `addColumnItem()`
- 条件付き依存: `if (!(site.usage > 0 || site.persisted))` → `addColumnItem()`
- 参照: `site.baseDomain`, `site.cookies.length`, `site.lastAccessed`, `site.persisted`, `site.usage`

## addColumnItem()
- 位置: L34-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `box.appendChild()`, `box.setAttribute()`, `container.appendChild()`, `document.createXULElement()`, `label.setAttribute()`
- 条件付き依存: `if (l10n)` → `l10n.hasOwnProperty()`
- 条件付き依存: `if (l10n.hasOwnProperty("raw"))` → `box.setAttribute()`
- 条件付き依存: `if (l10n.hasOwnProperty("raw"))` → `label.setAttribute()`
- 条件付き依存: `if (!(l10n.hasOwnProperty("raw")))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (tooltipText)` → `box.setAttribute()`
- 参照: `box.className`, `l10n.args`, `l10n.id`, `l10n.raw`

## init()
- 位置: L101-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `SiteDataManager.getSites()`, `SiteDataManager.getSites().then()`, `document.addEventListener()`, `document.getElementById()`, `document.querySelector()`, `setEventListener()`, `this._buildSitesList()`, `this._sortSites()`, `this.onKeyPress()`, `this.saveChanges()`, `window.addEventListener()`
- 参照: `Services.intl.DateTimeFormat`, `Services.intl.RelativeTimeFormat`, `this._absoluteTimeFormat`, `this._list`, `this._relativeTimeFormat`, `this._searchBox`, `this._sites`, `this.onClickRemoveAll`, `this.onClickTreeCol`, `this.onInputSearch`, `this.onSelect`, `this.removeSelected`
- XPCOM: `Services.intl` / `Services.obs`

## setEventListener()
- 位置: L102-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback.bind()`, `document .getElementById()`, `document .getElementById(id) .addEventListener()`

## _updateButtonsState()
- 位置: L143-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`, `this._list.getElementsByTagName()`
- 参照: `items.length`, `removeAllBtn.disabled`, `removeSelectedBtn.disabled`, `this._list.selectedItems.length`, `this._searchBox.value`

## _sortSites()
- 位置: L160-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `c.removeAttribute()`, `col.getAttribute()`, `col.setAttribute()`, `cols.forEach()`, `this._list.previousElementSibling.querySelectorAll()`
- 条件付き依存: `if (sortDirection === "descending")` → `sites.sort()`
- 条件付き依存: `if (sortDirection === "descending")` → `sortFunc()`
- 条件付き依存: `if (!(sortDirection === "descending"))` → `sites.sort()`
- 参照: `col.id`

## sortFunc()
- 位置: L173-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.baseDomain.toLowerCase()`, `aHost.localeCompare()`, `b.baseDomain.toLowerCase()`

## sortFunc()
- 位置: L181-181
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.cookies.length`, `b.cookies.length`

## sortFunc()
- 位置: L185-185
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.usage`, `b.usage`

## sortFunc()
- 位置: L189-189
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.lastAccessed`, `b.lastAccessed`

## _buildSitesList()
- 位置: L211-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createDocumentFragment()`, `fragment.appendChild()`, `item.remove()`, `site.baseDomain.includes()`, `this._createSiteListItem()`, `this._list.appendChild()`, `this._list.querySelectorAll()`, `this._searchBox.value.toLowerCase()`, `this._searchBox.value.toLowerCase().trim()`, `this._updateButtonsState()`
- 参照: `site.userAction`

## _removeSiteItems()
- 位置: L236-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.getAttribute()`, `item.remove()`, `this._sites.find()`, `this._updateButtonsState()`
- 参照: `items.length`, `site.baseDomain`, `siteForBaseDomain.userAction`

## saveChanges()
- 位置: async L251-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sites .filter()`, `this._sites .filter(site => site.userAction == "remove") .map()`
- 条件付き依存: `if (removals.length)` → `SiteDataManager.promptSiteDataRemoval()`
- 条件付き依存: `if (!SiteDataManager.promptSiteDataRemoval(window, promptArg))` → `event.preventDefault()`
- 条件付き依存: `if (removeAll)` → `SiteDataManager.removeAll()`
- 条件付き依存: `if (!(removeAll))` → `SiteDataManager.remove()`
- 条件付き依存: `if (removals.length)` → `console.error()`
- 参照: `removals.length`, `site.baseDomain`, `site.userAction`, `this._sites.length`

## removeSelected()
- 位置: L277-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._list.clearSelection()`, `this._list.getIndexOfItem()`, `this._list.getItemAtIndex()`, `this._removeSiteItems()`
- 参照: `this._list.itemCount`, `this._list.selectedIndex`, `this._list.selectedItem`, `this._list.selectedItems`, `this._list.selectedItems.length`

## onClickTreeCol()
- 位置: L295-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._buildSitesList()`, `this._list.clearSelection()`, `this._sortSites()`
- 参照: `e.target`, `this._sites`

## onInputSearch()
- 位置: L301-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._buildSitesList()`, `this._list.clearSelection()`
- 参照: `this._sites`

## onClickRemoveAll()
- 位置: L306-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._list.getElementsByTagName()`
- 条件付き依存: `if (siteItems.length)` → `this._removeSiteItems()`
- 参照: `siteItems.length`

## onKeyPress()
- 位置: L313-326
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( e.keyCode == KeyEvent.DOM_VK_DELETE || (AppConstants.platform == "macosx" && e.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `e.target.closest()`
- 条件付き依存: `if ( e.keyCode == KeyEvent.DOM_VK_DELETE || (AppConstants.platform == "macosx" && e.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `this.removeSelected()`
- 参照: `AppConstants.platform`, `KeyEvent.DOM_VK_BACK_SPACE`, `KeyEvent.DOM_VK_DELETE`, `e.keyCode`

## onSelect()
- 位置: L328-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateButtonsState()`
