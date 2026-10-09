# browser/components/places/metadataViewer/interactionsViewer.js

source: browser/components/places/metadataViewer/interactionsViewer.js
source-hash: d552ee755af6d631b27b3f00984461374b807c62
lines: 673

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/places/frecency-recalculator;1"].getService()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`

## TableViewer.start()
- 位置: async L102-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setInterval()`, `this.setupUI()`, `this.updateDisplay()`, `this.updateDisplay.bind()`
- 参照: `this.#timer`

## TableViewer.pause()
- 位置: L111-116
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#timer)` → `clearInterval()`
- 参照: `this.#timer`

## TableViewer.setupUI()
- 位置: L122-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columnDiv.classList.add()`, `columnDiv.setAttribute()`, `document.createDocumentFragment()`, `document.createElement()`, `document.getElementById()`, `header.appendChild()`, `row.appendChild()`, `tableBody.appendChild()`, `this.columnMap.entries()`, `viewer.appendChild()`
- 参照: `columnDiv.textContent`, `details.header`, `document.getElementById("title").textContent`, `existingStyle.innerText`, `limit.textContent`, `this.#lastFilledRows`, `this.columnMap.size`, `this.cssGridTemplateColumns`, `this.maxRows`, `this.title`, `viewer.textContent`

## TableViewer.displayData()
- 位置: L194-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `details.modifier()`, `document.getElementById()`, `this.columnMap.entries()`, `this.updateDisplayedSort()`
- 条件付き依存: `if (details.includeTitle)` → `viewer.children[index].setAttribute()`
- 条件付き依存: `if (numRows < this.#lastFilledRows)` → `viewer.children[index].removeAttribute()`
- 参照: `details.includeTitle`, `details.modifier`, `rows.length`, `this.#lastFilledRows`, `this.columnMap.size`, `viewer.children`, `viewer.children[index].textContent`

## TableViewer.updateDisplayedSort()
- 位置: L231-251
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.sortable)` → `document.getElementById()`
- 条件付き依存: `if (this.sortable)` → `viewer.querySelector()`
- 条件付き依存: `if (!symbolHolder)` → `document.createElement()`
- 条件付き依存: `if (this.sortable)` → `element.appendChild()`
- 参照: `SortingType.DESCENDING`, `symbolHolder.id`, `symbolHolder.style.marginLeft`, `symbolHolder.style.pointerEvents`, `symbolHolder.textContent`, `this.sortSetting.column`, `this.sortSetting.order`, `this.sortable`

## TableViewer.changeSort()
- 位置: L253-262
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SortingType.ASCENDING`, `SortingType.DESCENDING`, `this.sortSetting`, `this.sortSetting.column`, `this.sortSetting.order`

## TableViewer.sortable()
- 位置: L264-266
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.sortSetting`

## modifier()
- 位置: L287-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date(updatedAt).toLocaleString()`

## modifier()
- 位置: L294-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(totalViewTime / 1000).toFixed()`

## modifier()
- 位置: L301-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(typingTime / 1000).toFixed()`

## modifier()
- 位置: L309-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(scrollingTime / 1000).toFixed()`

## #getRows()
- 位置: async L325-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `r.getResultByName()`, `rows.map()`, `this.#db.executeCached()`, `this.columnMap.keys()`
- 条件付き依存: `if (!this.#db)` → `PlacesUtils.promiseDBConnection()`
- 参照: `this.#db`

## updateDisplay()
- 位置: async L342-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getRows()`, `this.displayData()`
- 参照: `this.maxRows`, `this.sortSetting.column`, `this.sortSetting.order`

## export()
- 位置: L355-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getRows()`

## modifier()
- 位置: L427-427
- 役割: (未記入)
- 触るとき: (未記入)

## updateDisplay()
- 位置: async L453-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesDBUtils.getEntitiesStatsAndCounts()`, `this.displayData()`

## modifier()
- 位置: L478-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date(lastVisitDate / 1000).toLocaleString()`

## #getRows()
- 位置: async L505-517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `r.getResultByName()`, `rows.map()`, `this.#db.executeCached()`, `this.columnMap.keys()`
- 条件付き依存: `if (!this.#db)` → `PlacesUtils.promiseDBConnection()`
- 参照: `this.#db`

## updateDisplay()
- 位置: async L522-538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getRows()`, `this.displayData()`
- 参照: `this.#maxRows`, `this.sortSetting.column`, `this.sortSetting.order`

## checkPrefs()
- 位置: L541-548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("browser.places.interactions.enabled", false) )` → `document.getElementById()`
- 参照: `warning.hidden`
- XPCOM: `Services.prefs`

## show()
- 位置: L550-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(gCurrentHandler = metadataHandler).start()`, `(gCurrentHandler = placesStatsHandler).start()`, `(gCurrentHandler = placesViewerHandler).start()`, `currentButton.classList.remove()`, `document.querySelector()`, `gCurrentHandler.pause()`, `metadataHandler.start()`, `selectedButton.classList.add()`, `selectedButton.getAttribute()`

## createObjectURL()
- 位置: L573-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.URL.createObjectURL()`
- 条件付き依存: `if (AppConstants.DEBUG)` → `data.replaceAll("'", "\\'").replaceAll()`
- 条件付き依存: `if (AppConstants.DEBUG)` → `data.replaceAll()`
- 条件付き依存: `if (AppConstants.DEBUG)` → `Cu.evalInSandbox()`
- 参照: `AppConstants.DEBUG`, `Cu.Sandbox`

## downloadFile()
- 位置: L596-602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `a.click()`, `a.remove()`, `a.setAttribute()`, `createObjectURL()`, `document.createElement()`

## getData()
- 位置: async L604-608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `metadataHandler.export()`
- 参照: `document.getElementById("include-place-data").checked`

## setupListeners()
- 位置: L610-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Object.keys()`, `data.at()`, `data.map()`, `document .getElementById()`, `document .getElementById("recalc-alt-frecency") .addEventListener()`, `document.getElementById()`, `document.getElementById("export-csv").addEventListener()`, `document.getElementById("export-json").addEventListener()`, `document.getElementById("tableViewer").addEventListener()`, `downloadFile()`, `e.preventDefault()`, `getData()`, `headers.join()`, `headers.map()`, `headers.map(field => JSON.stringify(obj[field] ?? "")).join()`, `lazy.PlacesFrecencyRecalculator.recalculateAnyOutdatedFrecencies()`, `menu.addEventListener()`, `rows.join()`
- 条件付き依存: `if (e.target && e.target.parentNode == menu)` → `show()`
- 条件付き依存: `if (gCurrentHandler.sortable && e.target.dataset.columnTitle)` → `gCurrentHandler.changeSort()`
- 条件付き依存: `if (gCurrentHandler.sortable && e.target.dataset.columnTitle)` → `gCurrentHandler.updateDisplay()`
- 参照: `e.target`, `e.target.dataset.columnTitle`, `e.target.parentNode`, `gCurrentHandler.sortable`
