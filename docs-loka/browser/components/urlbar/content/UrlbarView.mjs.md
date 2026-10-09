# browser/components/urlbar/content/UrlbarView.mjs

source: browser/components/urlbar/content/UrlbarView.mjs
source-hash: 625b58d963cfb10fd00ba44941433fb3c054f506
lines: 5058

## <module>
- 役割: (未記入)

## getUniqueId()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarView.constructor()
- 位置: L88-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#rows.addEventListener()`, `this.#updateOverflowState.bind()`, `this.controller.addListener()`, `this.controller.setView()`, `this.input.addEventListener()`, `this.input.toggleAttribute()`, `this.panel.querySelector()`, `this.resultMenu.addEventListener()`
- 参照: `input.controller`, `input.panel`, `this.#l10nCache`, `this.#overflowObserver`, `this.#rows`, `this.controller`, `this.input`, `this.panel`, `this.queryContextCache`, `this.resultMenu`

## UrlbarView.oneOffSearchButtons()
- 位置: L122-134
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#oneOffSearchButtons)` → `this.#oneOffSearchButtons.addEventListener()`
- 参照: `lazy.UrlbarSearchOneOffs`, `this.#oneOffSearchButtons`, `this.input.sapName`

## UrlbarView.chromeWindow()
- 位置: L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.window`

## UrlbarView.#currentPage()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.chromeWindow.gBrowser?.currentURI?.spec`

## UrlbarView.#canReuseResults()
- 位置: L166-171
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `queryContext.currentPage`, `queryContext.searchString`, `this.#currentPage`, `this.input.value`

## UrlbarView.isOpen()
- 位置: L178-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.hasAttribute()`

## UrlbarView.queryContext()
- 位置: L185-187
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#queryContext`

## UrlbarView.allowEmptySelection()
- 位置: L189-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#shouldShowHeuristic()`
- 参照: `this.#queryContext`

## UrlbarView.selectedRowIndex()
- 位置: L194-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSelectedRow()`
- 参照: `selectedRow.result.rowIndex`, `this.isOpen`

## UrlbarView.selectedRowIndex()
- 位置: L208-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.#rows.children).filter()`, `this.#getNextSelectableElement()`, `this.#getRowFromElement()`, `this.#isElementVisible()`, `this.#selectElement()`
- 条件付き依存: `if (val < 0)` → `this.#selectElement()`
- 参照: `items.length`, `this.#rows.children`, `this.isOpen`

## UrlbarView.selectedElementIndex()
- 位置: L238-244
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#selectedElement`, `this.#selectedElement.elementIndex`, `this.isOpen`

## UrlbarView.selectedResult()
- 位置: L250-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSelectedRow()`
- 参照: `this.#getSelectedRow()?.result`, `this.isOpen`

## UrlbarView.selectedElement()
- 位置: L262-268
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#selectedElement`, `this.isOpen`

## UrlbarView.shouldSpaceActivateSelectedElement()
- 位置: L275-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedElement?.getAttribute()`
- 参照: `this.input.value`, `this.selectedElement?.dataset.name`

## UrlbarView.clearSelection()
- 位置: L298-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#selectElement()`

## UrlbarView.visibleRowCount()
- 位置: L308-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `this.#isElementVisible()`
- 参照: `this.#rows.children`

## UrlbarView.getResultFromElement()
- 位置: L325-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element?.classList.contains()`, `this.#getRowFromElement()`
- 参照: `this.#getRowFromElement(element)?.result`, `this.#resultMenuResult`

## UrlbarView.telemetryTypeFromElement()
- 位置: L339-356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.classList?.contains()`, `this.telemetryTypeFromResult()`
- 参照: `element.dataset.command`, `element.dataset.l10nName`

## UrlbarView.telemetryTypeFromResult()
- 位置: L364-459
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!type)` → `console.error()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.ACTION`, `UrlbarShared.RESTRICT_TOKENS.BOOKMARK`, `UrlbarShared.RESTRICT_TOKENS.HISTORY`, `UrlbarShared.RESTRICT_TOKENS.OPENPAGE`, `UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `result.autofill`, `result.autofill.type`, `result.heuristic`, `result.isRichSuggestion`, `result.payload.keyword`, `result.payload.suggestion`, `result.payload.trending`, `result.providerName`, `result.source`, `result.type`

## UrlbarView.getResultAtIndex()
- 位置: L468-478
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#rows.children`, `this.#rows.children.length`, `this.#rows.children[index].result`, `this.isOpen`

## UrlbarView.resultIsSelected()
- 位置: L484-490
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.rowIndex`, `this.selectedRowIndex`

## UrlbarView.selectBy()
- 位置: L504-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSkippableTabToSearchAnnounce()`, `this.#getNextSelectableElement()`, `this.#getPreviousSelectableElement()`, `this.#selectElement()`, `this.getFirstSelectableElement()`, `this.getLastSelectableElement()`
- 条件付き依存: `if (!this.input.eventBufferer.isDeferringEvents)` → `this.controller.cancelQuery()`
- 条件付き依存: `if (this.allowEmptySelection)` → `this.#selectElement()`
- 条件付き依存: `if (selectedRowIndex != -1)` → `Math.min()`
- 条件付き依存: `if (selectedRowIndex != -1)` → `Math.max()`
- 条件付き依存: `if (!userPressedTab)` → `this.#isRowArrowSelectable()`
- 条件付き依存: `if (!selectedElement)` → `this.#selectElement()`
- 条件付き依存: `if (!selectedElement)` → `isSkippableTabToSearchAnnounce()`
- 条件付き依存: `if (endReached)` → `this.#selectElement()`
- 条件付き依存: `if (endReached)` → `isSkippableTabToSearchAnnounce()`
- 参照: `this.#selectedElement`, `this.allowEmptySelection`, `this.input.eventBufferer.isDeferringEvents`, `this.isOpen`, `this.selectedRowIndex`, `this.visibleRowCount`

## isSkippableTabToSearchAnnounce()
- 位置: L552-564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.getResultFromElement()`
- 参照: `result?.providerName`, `this.#announceTabToSearchOnSelection`

## UrlbarView.acknowledgeFeedback()
- 位置: async L618-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row._content.closest()`, `row._content.closest("[role=option]").ariaNotify()`, `row.setAttribute()`, `this.#getRowByResultId()`, `this.#l10nCache.ensure()`, `this.#l10nCache.get()`
- 参照: `row.result?.id`

## UrlbarView.#acknowledgeDismissal()
- 位置: L645-684
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getRowByResultId()`, `this.#getSelectedRow()`, `this.#rowLabel()`, `this.#setRowSelectable()`, `this.#updateIndices()`, `this.#updateRow()`
- 条件付き依存: `if (isSelected)` → `this.#selectElement()`
- 条件付き依存: `if (isSelected)` → `this.#getNextSelectableElement()`
- 参照: `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.TIP`, `result.hideRowLabel`, `result.id`

## UrlbarView.removeAccessibleFocus()
- 位置: L686-688
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setAccessibleFocus()`

## UrlbarView.clear()
- 位置: L690-696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#rows.toggleAttribute()`, `this.clearSelection()`, `this.input.toggleAttribute()`
- 参照: `this.#rows.textContent`, `this.visibleResults`

## UrlbarView.close()
- 位置: L707-770
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getBoundsWithoutFlushing()`, `this.#stopTail150()`, `this.controller.cancelQuery()`, `this.controller.notify()`, `this.input.inputField.setAttribute()`, `this.input.toggleAttribute()`, `this.removeAccessibleFocus()`, `this.resultMenu.hide()`, `window.removeEventListener()`
- 条件付き依存: `if (!elementPicked && showFocusBorder)` → `this.input.removeAttribute()`
- 条件付き依存: `if (!this.isOpen)` → `this.input.updatePopover()`
- 条件付き依存: `if (!this.input.focused && !elementPicked)` → `this.controller.engagementEvent.discard()`
- 条件付き依存: `if (this.#blobUrlsByResultUrl)` → `this.#blobUrlsByResultUrl.values()`
- 条件付き依存: `if (this.#blobUrlsByResultUrl)` → `URL.revokeObjectURL()`
- 条件付き依存: `if (this.#blobUrlsByResultUrl)` → `this.#blobUrlsByResultUrl.clear()`
- 条件付き依存: `if (isShowingZeroPrefix)` → `this.controller.parentController.recordZeroPrefix()`
- 参照: `UrlbarShared.NOTIFICATIONS.VIEW_CLOSE`, `getBoundsWithoutFlushing( this.input.parentElement ).width`, `this.#blobUrlsByResultUrl`, `this.#containerWidthOnLastClose`, `this.#openPanelInstance`, `this.#previousTabToSearchEngine`, `this.#queryContext`, `this.#queryContext.searchString`, `this.input.focused`, `this.input.parentElement`, `this.input.searchMode`, `this.input.searchMode?.isPreview`, `this.input.userTypedValue`, `this.isOpen`

## UrlbarView.startTail150()
- 位置: L772-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `canvas.getContext()`, `closeBtn.addEventListener()`, `closeBtn.setAttribute()`, `ctx.scale()`, `document.createElement()`, `overlay.append()`, `overlay.setAttribute()`, `overlay.showPopover()`, `this.#runTail150()`, `this.close()`, `this.input.appendChild()`
- 参照: `canvas.className`, `canvas.height`, `canvas.width`, `closeBtn.className`, `overlay.className`, `this.#tail150`, `window.devicePixelRatio`

## UrlbarView.#stopTail150()
- 位置: L801-810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tail150.overlay.remove()`
- 条件付き依存: `if (this.#tail150.keyHandler)` → `window.removeEventListener()`
- 参照: `this.#tail150`, `this.#tail150.keyHandler`

## UrlbarView.#runTail150()
- 位置: L812-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `S.getPropertyValue()`, `W.addEventListener()`, `X.fillText()`, `c.getContext()`, `window.getComputedStyle()`
- 参照: `SP.src`, `X.fillStyle`, `X.font`, `X.textAlign`, `this.#tail150.keyHandler`, `window.Image`

## A()
- 位置: L819-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `W.requestAnimationFrame()`

## CA()
- 位置: L819-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `X.arc()`, `X.beginPath()`, `X.fill()`

## g()
- 位置: L819-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.random()`

## GO()
- 位置: L819-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `X.fillText()`
- 参照: `X.fillStyle`, `X.shadowBlur`, `X.shadowColor`

## PF()
- 位置: L819-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GO()`, `Math.random()`, `a.push()`, `s.every()`
- 参照: `$.x`, `$.y`, `a.length`

## I()
- 位置: L819-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `A()`, `Array()`, `[...Array(8)].map()`

## L()
- 位置: L819-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `A()`, `CA()`, `Math.max()`, `Math.min()`, `X.clearRect()`, `X.restore()`, `X.save()`, `X.translate()`, `s.map()`
- 条件付き依存: `if (p>=1)` → `s.some()`
- 条件付き依存: `if (t.x<0||t.x>19||t.y<0||t.y>19||s.some($=>$.x==t.x&&$.y==t.y))` → `GO()`
- 条件付き依存: `if (p>=1)` → `s.unshift()`
- 条件付き依存: `if (p>=1)` → `PF()`
- 条件付き依存: `if (p>=1)` → `s.pop()`
- 条件付き依存: `if (X.save(),X.translate(Math.min(390,Math.max(10,20*($.x+(!t&&d[0]*p))+10)),Math.min(390,Math.max(10,20*($.y+(!t&&d[1]*p))+10))),t)` → `CA()`
- 条件付き依存: `if (!(X.save(),X.translate(Math.min(390,Math.max(10,20*($.x+(!t&&d[0]*p))+10)),Math.min(390,Math.max(10,20*($.y+(!t&&d[1]*p))+10))),t))` → `X.drawImage()`
- 参照: `$.x`, `$.y`, `SP.complete`, `X.fillStyle`, `f.x`, `f.y`, `s.length`, `s[0].x`, `s[0].y`, `t.x`, `t.y`, `this.#tail150`

## this.#tail150.keyHandler()
- 位置: L819-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `$.preventDefault()`, `$.stopPropagation()`, `I()`
- 参照: `$.keyCode`

## UrlbarView.autoOpen()
- 位置: L837-950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getBoundsWithoutFlushing()`, `this.#canReuseResults()`, `this.#pickSearchTipIfPresent()`, `this.controller.engagementEvent.discard()`, `this.input.getAttribute()`, `this.input.startQuery()`
- 条件付き依存: `if ( !this.input.value || this.input.getAttribute("pageproxystate") == "valid" )` → `["mousedown", "command"].includes()`
- 条件付き依存: `if (!this.input.searchMode && this.queryContextCache.topSitesContext)` → `this.onQueryResults()`
- 条件付き依存: `if (!this.isOpen && ["mousedown", "command"].includes(event.type))` → `this.input.startQuery()`
- 条件付き依存: `if (suppressFocusBorder)` → `this.input.toggleAttribute()`
- 条件付き依存: `if (!( this.#rows.firstElementChild && this.#canReuseResults(this.#queryContext) && this.#containerWidthOnLastClose == getBoundsWithoutFlushing(this.input.parentEl...))` → `this.queryContextCache.get()`
- 条件付き依存: `if (cachedQueryContext)` → `this.onQueryResults()`
- 条件付き依存: `if (this.input.sapName == "urlbar")` → `this.input.getBrowserState()`
- 条件付き依存: `if ( this.#queryContext?.results?.length && this.#canReuseResults(this.#queryContext) && this.#queryContext.results[0].type != UrlbarShared.RESULT_TYPE.TIP )` → `this.#openPanel()`
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `event.type`, `getBoundsWithoutFlushing(this.input.parentElement).width`, `queryOptions.allowAutofill`, `queryOptions.autofillIgnoresSelection`, `queryOptions.interactionType`, `queryOptions.searchString`, `state.persist?.shouldPersist`, `this.#containerWidthOnLastClose`, `this.#currentPage`, `this.#queryContext`, `this.#queryContext.allowAutofill`, `this.#queryContext.results`, `this.#queryContext.results[0].type`, `this.#queryContext?.results?.length`, `this.#rows.firstElementChild`, `this.chromeWindow.gBrowser.selectedBrowser`, `this.input.focused`, `this.input.inOverflowPanel`, `this.input.parentElement`, `this.input.readOnly`, `this.input.sapName`, `this.input.searchMode`, `this.input.value`, `this.isOpen`, `this.queryContextCache.topSitesContext`

## UrlbarView.onQueryStarted()
- 位置: L960-975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cacheL10nStrings()`, `this.#startRemoveStaleRowsTimer()`
- 参照: `queryContext.searchString`, `this.#openPanelInstance`, `this.#previousTabToSearchEngine`, `this.#queryUpdatedResults`, `this.#queryWasCancelled`

## UrlbarView.onQueryCancelled()
- 位置: L980-983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cancelRemoveStaleRowsTimer()`
- 参照: `this.#queryWasCancelled`

## UrlbarView.onQueryFinished()
- 位置: L991-1039
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(oneOffs?.willHide() ?? Promise.resolve(true)).then()`, `Promise.resolve()`, `oneOffs.enable()`, `oneOffs?.willHide()`, `this.#cancelRemoveStaleRowsTimer()`, `this.#openPanel()`
- 条件付き依存: `if (this.#queryUpdatedResults)` → `this.#removeStaleRows()`
- 条件付き依存: `if (!(this.#queryUpdatedResults))` → `this.clear()`
- 条件付き依存: `if (!queryContext.searchString)` → `this.controller.parentController.recordZeroPrefix()`
- 条件付き依存: `if (!this.input.searchMode)` → `this.close()`
- 条件付き依存: `if (this.isOpen)` → `this.close()`
- 参照: `queryContext.searchString`, `this.#openPanelInstance`, `this.#queryUpdatedResults`, `this.#queryWasCancelled`, `this.input.searchMode`, `this.isOpen`, `this.oneOffSearchButtons`

## UrlbarView.onQueryResults()
- 位置: L1047-1169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.#openPanel()`, `this.#updateResults()`, `this.queryContextCache.put()`
- 条件付き依存: `if (!this.isOpen)` → `this.clear()`
- 条件付き依存: `if (this.input.searchMode?.source == UrlbarShared.RESULT_SOURCE.ACTIONS)` → `this.#rows.toggleAttribute()`
- 条件付き依存: `if (queryContext.lastResultCount == 0)` → `this.#selectElement()`
- 条件付き依存: `if (queryContext.lastResultCount == 0)` → `this.oneOffSearchButtons?.enable()`
- 条件付き依存: `if (firstResult.heuristic)` → `this.#shouldShowHeuristic()`
- 条件付き依存: `if (this.#shouldShowHeuristic(firstResult))` → `this.#selectElement()`
- 条件付き依存: `if (this.#shouldShowHeuristic(firstResult))` → `this.getFirstSelectableElement()`
- 条件付き依存: `if (!(this.#shouldShowHeuristic(firstResult)))` → `this.input.setResultForCurrentValue()`
- 条件付き依存: `if ( firstResult.payload.providesSearchMode && queryContext.trimmedSearchString != "@" )` → `this.input.setResultForCurrentValue()`
- 条件付き依存: `if ( secondResult?.providerName == "UrlbarProviderTabToSearch" && UrlbarPrefs.get("accessibility.tabToSearch.announceResults") && this.#previousTabToSearchEngine...)` → `this.#ariaNotifyLocalizedString()`
- 条件付き依存: `if (this.#selectedElement && !this.oneOffSearchButtons?.selectedButton)` → `this.input.inputField.getAttribute()`
- 条件付き依存: `if (this.#selectedElement && !this.oneOffSearchButtons?.selectedButton)` → `document.getElementById()`
- 条件付き依存: `if (aadID && !document.getElementById(aadID))` → `this.#setAccessibleFocus()`
- 条件付き依存: `if (firstResult.heuristic)` → `this.input.formatValue()`
- 条件付き依存: `if (queryContext.deferUserSelectionProviders.size)` → `queryContext.results.forEach()`
- 条件付き依存: `if (queryContext.deferUserSelectionProviders.size)` → `queryContext.deferUserSelectionProviders.delete()`
- 条件付き依存: `if (UrlbarPrefs.get("unifiedSearchButton.always"))` → `this.input.searchModeSwitcher?.updateSearchIcon()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.SEARCH`, `UrlbarShared.RESULT_SOURCE.ACTIONS`, `firstResult.heuristic`, `firstResult.payload.providesSearchMode`, `firstResult.providerName`, `queryContext.deferUserSelectionProviders.size`, `queryContext.lastResultCount`, `queryContext.results`, `queryContext.trimmedSearchString`, `queryContext.trimmedSearchString.length`, `r.providerName`, `secondResult.payload.engine`, `secondResult.payload.isGeneralPurposeEngine`, `secondResult?.providerName`, `this.#announceTabToSearchOnSelection`, `this.#previousTabToSearchEngine`, `this.#queryContext`, `this.#queryUpdatedResults`, `this.#rows.children`, `this.#selectedElement`, `this.controller.userSelectionBehavior`, `this.input.searchMode?.source`, `this.isOpen`, `this.oneOffSearchButtons?.selectedButton`

## UrlbarView.onQueryResultRemoved()
- 位置: L1183-1225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rowToRemove.remove()`, `this.#getSelectedRow()`, `this.#updateIndices()`
- 条件付き依存: `if (acknowledgeDismissalL10n)` → `this.#acknowledgeDismissal()`
- 条件付き依存: `if (updateSelection)` → `Math.min()`
- 条件付き依存: `if (!this.#rows.children.length)` → `this.close()`
- 参照: `this.#rows.children`, `this.#rows.children.length`, `this.#rows.children[i].result?.id`, `this.selectedRowIndex`

## UrlbarView.openResultMenu()
- 位置: L1227-1233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resultMenu.toggle()`
- 参照: `this.#resultMenuResult`

## UrlbarView.updateResultMenuCommands()
- 位置: L1247-1254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getRowByResultId()`, `this.#resultMenuCommands.delete()`
- 参照: `row.result`, `row.result.commands`

## UrlbarView.handleEvent()
- 位置: L1262-1269
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.type`

## UrlbarView.isResultMenuOpen()
- 位置: L1271-1273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resultMenu.hasAttribute()`

## UrlbarView.#selectedElement()
- 位置: L1313-1317
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#rawSelectedElement`, `this.#rawSelectedElement?.isConnected`

## UrlbarView.#showsActionLabels()
- 位置: L1325-1327
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.sapName`

## UrlbarView.#openPanel()
- 位置: L1329-1357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#enableOrDisableRowWrap()`, `this.controller.notify()`, `this.input.inputField.setAttribute()`, `this.input.toggleAttribute()`, `this.maybeRollupPopups()`, `this.panel.removeAttribute()`, `window.addEventListener()`
- 条件付き依存: `if (this.isOpen)` → `this.input.updatePopover()`
- 参照: `UrlbarShared.NOTIFICATIONS.VIEW_OPEN`, `this.controller.userSelectionBehavior`, `this.input.isSidebarMode`, `this.isOpen`

## UrlbarView.maybeRollupPopups()
- 位置: L1364-1378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if ( UrlbarPrefs.get("closeOtherPanelsOnOpen") && !this.input.inOverflowPanel )` → `window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsIAppWindow) .rollupAllPopups()`
- 条件付き依存: `if ( UrlbarPrefs.get("closeOtherPanelsOnOpen") && !this.input.inOverflowPanel )` → `window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if ( UrlbarPrefs.get("closeOtherPanelsOnOpen") && !this.input.inOverflowPanel )` → `window.docShell.treeOwner .QueryInterface()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `this.input.inOverflowPanel`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../../netwerk/base/nsIChannel.idl.md)

## UrlbarView.#shouldShowHeuristic()
- 位置: L1380-1388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `result.type`, `result?.heuristic`

## UrlbarView.#resultIsSearchSuggestion()
- 位置: L1396-1402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `result.payload.suggestion`, `result.type`

## UrlbarView.#rowCanUpdateToResult()
- 位置: L1415-1458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resultIsSearchSuggestion()`
- 参照: `result.hasSuggestedIndex`, `result.heuristic`, `result.providerName`, `result.suggestedIndex`, `row.result`, `row.result.hasSuggestedIndex`, `row.result.providerName`, `row.result.suggestedIndex`, `this.#rows.children`

## UrlbarView.#updateResults()
- 位置: L1460-1614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getSpanForResult()`, `results.slice()`, `row.setAttribute()`, `this.#createRow()`, `this.#isElementVisible()`, `this.#rows.appendChild()`, `this.#shouldShowHeuristic()`, `this.#updateIndices()`, `this.#updateRow()`, `this.controller.engagementEvent.discardTentativeExposures()`
- 条件付き依存: `if (results[0]?.heuristic && !this.#shouldShowHeuristic(results[0]))` → `results.slice()`
- 条件付き依存: `if (this.#isElementVisible(row))` → `UrlbarShared.getSpanForResult()`
- 条件付き依存: `if (!seenMisplacedResult)` → `this.#resultIsSearchSuggestion()`
- 条件付き依存: `if (!seenMisplacedResult)` → `this.#rowCanUpdateToResult()`
- 条件付き依存: `if ( this.#rowCanUpdateToResult(rowIndex, result, seenSearchSuggestion) )` → `resultsToInsert.shift()`
- 条件付き依存: `if (result.isHiddenExposure)` → `this.controller.engagementEvent.addExposure()`
- 条件付き依存: `if ( this.#rowCanUpdateToResult(rowIndex, result, seenSearchSuggestion) )` → `this.#updateRow()`
- 条件付き依存: `if (!(result.isSuggestedIndexRelativeToGroup))` → `Math.min()`
- 条件付き依存: `if (!(result.isSuggestedIndexRelativeToGroup))` → `Math.max()`
- 条件付き依存: `if (canBeVisible)` → `this.controller.engagementEvent.addExposure()`
- 条件付き依存: `if (!(canBeVisible))` → `this.controller.engagementEvent.addTentativeExposure()`
- 条件付き依存: `if (!(canBeVisible))` → `this.#setRowVisibility()`
- 参照: `result.hasSuggestedIndex`, `result.isHiddenExposure`, `result.isSuggestedIndexRelativeToGroup`, `result.suggestedIndex`, `results.length`, `resultsToInsert.length`, `results[0]?.heuristic`, `row.result`, `row.result.hasSuggestedIndex`, `row.result.heuristic`, `this.#queryContext`, `this.#queryContext.maxResults`, `this.#queryContext.results`, `this.#rows.children`, `this.#rows.children.length`

## UrlbarView.#createRow()
- 位置: L1616-1644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...item.attributes].map()`, `[...item.attributes].map(v => v.name).concat()`, `document.createElement()`, `item.setAttribute()`
- 参照: `item._buttons`, `item._elements`, `item._sharedAttributes`, `item._sharedClassList`, `item.attributes`, `item.classList`, `item.className`, `v.name`

## UrlbarView.#createRowContent()
- 位置: L1649-1709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `item._content.appendChild()`, `item._elements.set()`, `noWrap.appendChild()`, `tagsContainer.classList.add()`, `tailPrefix.appendChild()`, `tailPrefix.toggleAttribute()`, `this.#createExplanation()`, `title.classList.add()`
- 参照: `action.className`, `favicon.className`, `item._content`, `noWrap.className`, `tailPrefix.className`, `tailPrefixChar.className`, `tailPrefixStr.className`, `titleSeparator.className`, `typeIcon.className`, `url.className`

## UrlbarView.#createExplanation()
- 位置: L1715-1734
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `document.createElement()`, `explanation.appendChild()`, `explanation.classList.add()`, `item._elements.set()`, `parentNode.appendChild()`
- 参照: `bookmarked.className`, `lastVisited.className`

## UrlbarView.#updateExplanation()
- 位置: L1746-1797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item._elements.get()`, `item.toggleAttribute()`
- 条件付き依存: `if (hasBookmark)` → `UrlbarShared.formatDate()`
- 条件付き依存: `if (hasBookmark)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(hasBookmark))` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (hasLastVisit)` → `UrlbarShared.formatDate()`
- 条件付き依存: `if (hasLastVisit)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(hasLastVisit))` → `this.#l10nCache.removeElementL10n()`
- 参照: `UrlbarShared.DATE_FORMAT_TYPE.ABSOLUTE`, `UrlbarShared.DATE_FORMAT_TYPE.DAYS_WEEKS_MONTHS_AGO`, `UrlbarShared.DATE_FORMAT_TYPE.YESTERDAY_TODAY_TOMORROW`, `result.payload.bookmarkDateMs`, `result.payload.lastVisit`

## UrlbarView.#updateElementForDynamicType()
- 位置: L1831-1901
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (update.attributes)` → `Object.entries()`
- 条件付き依存: `if (key == "id")` → `console.error()`
- 条件付き依存: `if (value === null)` → `element.removeAttribute()`
- 条件付き依存: `if (typeof value == "boolean")` → `element.toggleAttribute()`
- 条件付き依存: `if (!(typeof value == "boolean"))` → `UrlbarShared.isInstance()`
- 条件付き依存: `if (UrlbarShared.isInstance(value, Blob) && result)` → `element.setAttribute()`
- 条件付き依存: `if (UrlbarShared.isInstance(value, Blob) && result)` → `this.#getBlobUrlForResult()`
- 条件付き依存: `if (!(UrlbarShared.isInstance(value, Blob) && result))` → `element.setAttribute()`
- 条件付き依存: `if (update.style)` → `Object.entries()`
- 条件付き依存: `if (update.style)` → `styleName.includes()`
- 条件付き依存: `if (value === null)` → `element.style.removeProperty()`
- 条件付き依存: `if (!(value === null))` → `element.style.setProperty()`
- 条件付き依存: `if (update.dataset)` → `Object.entries()`
- 条件付き依存: `if (typeof value != "string")` → `console.error()`
- 条件付き依存: `if (update.classList)` → `element.classList.add()`
- 参照: `element.className`, `element.dataset`, `element.style`, `item._content`, `update.attributes`, `update.classList`, `update.dataset`, `update.style`

## UrlbarView.#createRowContentForDynamicType()
- 位置: L1907-1926
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classes.has()`, `item._content.hasAttribute()`, `item.toggleAttribute()`, `this.#buildViewForDynamicType()`, `this.#setRowSelectable()`
- 条件付き依存: `if (!viewTemplate)` → `console.error()`
- 参照: `item._content`, `item._elements`, `result.payload`, `result.providerName`, `this.#showsActionLabels`

## UrlbarView.#buildViewForDynamicType()
- 位置: L1951-1991
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `parentNode.appendChild()`, `this.#buildViewForDynamicType()`, `this.#updateElementForDynamicType()`
- 条件付き依存: `if (template.classList)` → `classes.add()`
- 条件付き依存: `if (template.overflowable)` → `parentNode.classList.add()`
- 条件付き依存: `if (template.name)` → `parentNode.setAttribute()`
- 条件付き依存: `if (template.name)` → `parentNode.classList.add()`
- 条件付き依存: `if (template.name)` → `elementsByName.set()`
- 参照: `childTemplate.tag`, `template.children`, `template.classList`, `template.name`, `template.overflowable`

## UrlbarView.#createRowContentForRichSuggestion()
- 位置: L1997-2110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `body.appendChild()`, `bodyTop.appendChild()`, `description.classList.add()`, `document.createElement()`, `item._content.appendChild()`, `item._content.toggleAttribute()`, `item._elements.set()`, `noWrap.appendChild()`, `tagsContainer.classList.add()`, `tailPrefix.appendChild()`, `tailPrefix.toggleAttribute()`, `this.#createExplanation()`, `title.classList.add()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `document.createElement()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `userContext.classList.add()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `noWrap.appendChild()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `item._elements.set()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `tabGroupContainer.classList.add()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `tabGroupLabelFull.classList.add()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `tabGroupContainer.appendChild()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `tabGroupLabelShort.classList.add()`
- 条件付き依存: `if (result.payload.descriptionLearnMoreTopic)` → `document.createElement()`
- 条件付き依存: `if (result.payload.descriptionLearnMoreTopic)` → `learnMoreLink.setAttribute()`
- 条件付き依存: `if (result.payload.descriptionLearnMoreTopic)` → `description.appendChild()`
- 参照: `action.className`, `body.className`, `bodyTop.className`, `bottom.className`, `favicon.className`, `noWrap.className`, `result.payload.descriptionLearnMoreTopic`, `tailPrefix.className`, `tailPrefixChar.className`, `tailPrefixStr.className`, `titleSeparator.className`, `typeIcon.className`, `url.className`

## UrlbarView.#createRowContentForBottomUrl()
- 位置: L2116-2175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `body.appendChild()`, `bodyTop.appendChild()`, `bottom.appendChild()`, `description.classList.add()`, `document.createElement()`, `item._content.appendChild()`, `item._content.toggleAttribute()`, `item._elements.set()`, `noWrap.appendChild()`, `title.classList.add()`
- 参照: `body.className`, `bodyTop.className`, `bottom.className`, `bottomLabel.className`, `bottomSeparator.className`, `favicon.className`, `noWrap.className`, `subtitle.className`, `subtitleSeparator.className`, `url.className`

## UrlbarView.#needsNewButtons()
- 位置: L2183-2207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.deepEqual()`, `item._buttons.has()`, `this.#hasMenuButton()`
- 参照: `newResult.payload.buttons`, `newResult.payload.buttons?.length`, `newResult.showFeedbackMenu`, `newResult.testForceNewContent`, `oldResult.payload.buttons`, `oldResult.payload.buttons?.length`, `oldResult.showFeedbackMenu`

## UrlbarView.#updateRowButtons()
- 位置: L2214-2271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `i.toString()`, `item._buttons.clear()`, `item._elements.get()`, `item.toggleAttribute()`, `this.#hasMenuButton()`, `this.#needsNewButtons()`
- 条件付き依存: `if (!(container))` → `document.createElement()`
- 条件付き依存: `if (!(container))` → `item.appendChild()`
- 条件付き依存: `if (!(container))` → `item._elements.set()`
- 条件付き依存: `if (result.payload.buttons)` → `this.#addRowButton()`
- 条件付き依存: `if (result.payload.buttonText)` → `this.#addRowButton()`
- 条件付き依存: `if (result.payload.buttonText)` → `item._buttons.get()`
- 条件付き依存: `if (hasResultMenu)` → `this.#addRowButton()`
- 条件付き依存: `if (hasResultMenu)` → `UrlbarPrefs.get()`
- 参照: `button.name`, `container.className`, `container.innerHTML`, `item._buttons.get("tip").textContent`, `result.payload.buttonText`, `result.payload.buttonUrl`, `result.payload.buttons`, `result.payload.buttons?.length`, `result.showFeedbackMenu`

## UrlbarView.#addRowButton()
- 位置: L2286-2354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.classList.add()`, `container.appendChild()`, `container.classList.add()`, `document.createElement()`, `dropmarker.classList.add()`, `dropmarker.setAttribute()`, `item._buttons.set()`, `item._elements.get()`, `item._elements.get("buttons").appendChild()`, `this.#l10nCache.setElementL10n()`, `this.#updateElementForDynamicType()`
- 条件付き依存: `if (l10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!menu)` → `item._elements.get("buttons").appendChild()`
- 条件付き依存: `if (!menu)` → `item._elements.get()`
- 参照: `button.id`, `item.id`

## UrlbarView.#createSecondaryAction()
- 位置: L2356-2392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actionContainer.appendChild()`, `actionContainer.classList.add()`, `button.appendChild()`, `button.classList.add()`, `button.setAttribute()`, `document.createElement()`
- 条件付き依存: `if (global)` → `button.classList.add()`
- 条件付き依存: `if (action.classList)` → `button.classList.add()`
- 条件付き依存: `if (action.icon)` → `document.createElement()`
- 条件付き依存: `if (action.icon)` → `button.appendChild()`
- 条件付き依存: `if (action.l10nId)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(action.l10nId))` → `document.l10n.setAttributes()`
- 参照: `action.classList`, `action.dataset`, `action.icon`, `action.key`, `action.l10nArgs`, `action.l10nId`, `action.label`, `action.providerName`, `button.dataset`, `button.dataset.action`, `button.dataset.providerName`, `icon.src`

## UrlbarView.#needsNewContent()
- 位置: L2394-2467
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (newResult.type == UrlbarShared.RESULT_TYPE.DYNAMIC)` → `UrlbarShared.deepEqual()`
- 参照: `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `newResult.heuristic`, `newResult.isBottomUrlSuggestion`, `newResult.isRichSuggestion`, `newResult.payload.dynamicType`, `newResult.payload.items?.length`, `newResult.payload.suggestionType`, `newResult.payload.viewTemplate`, `newResult.providerName`, `newResult.testForceNewContent`, `newResult.type`, `oldResult.heuristic`, `oldResult.isBottomUrlSuggestion`, `oldResult.isRichSuggestion`, `oldResult.payload.dynamicType`, `oldResult.payload.items?.length`, `oldResult.payload.suggestionType`, `oldResult.payload.viewTemplate`, `oldResult.providerName`, `oldResult.type`

## UrlbarView.#updateRow()
- 位置: L2470-2865
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `action?.toggleAttribute()`, `getUniqueId()`, `item._elements.get()`, `item.querySelector()`, `item.removeAttribute()`, `item.toggleAttribute()`, `result.getDisplayableValueAndHighlights()`, `result.payload.input.trim()`, `this.#iconForResult()`, `this.#needsNewContent()`, `this.#setResultTitle()`, `this.#setRowSelectable()`, `this.#updateExplanation()`, `this.#updateOverflowTooltip()`, `this.#updateRowButtons()`, `title.hasAttribute()`, `title.toggleAttribute()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item._elements.get()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item.lastChild.remove()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item._elements.clear()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `document.createElement()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item.appendChild()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item._sharedAttributes.has()`
- 条件付き依存: `if (!item._sharedAttributes.has(attribute.name))` → `item.removeAttribute()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item._sharedClassList.has()`
- 条件付き依存: `if (!item._sharedClassList.has(className))` → `item.classList.remove()`
- 条件付き依存: `if (item.result.type == UrlbarShared.RESULT_TYPE.DYNAMIC)` → `this.#createRowContentForDynamicType()`
- 条件付き依存: `if (result.isBottomUrlSuggestion)` → `this.#createRowContentForBottomUrl()`
- 条件付き依存: `if (!(result.isBottomUrlSuggestion))` → `UrlbarPrefs.get()`
- 条件付き依存: `if ( result.isRichSuggestion || UrlbarPrefs.get("browser.nova.enabled") )` → `this.#createRowContentForRichSuggestion()`
- 条件付き依存: `if (!( result.isRichSuggestion || UrlbarPrefs.get("browser.nova.enabled") ))` → `this.#createRowContent()`
- 条件付き依存: `if (buttons)` → `item.appendChild()`
- 条件付き依存: `if (buttons)` → `item._elements.set()`
- 条件付き依存: `if (result.isBottomUrlSuggestion)` → `this.#updateRowContentForBottomUrl()`
- 条件付き依存: `if (secAction && !actionsContainer)` → `item.appendChild()`
- 条件付き依存: `if (secAction && !actionsContainer)` → `this.#createSecondaryAction()`
- 条件付き依存: `if ( secAction && secAction.key != actionsContainer.firstChild.dataset.action )` → `item.replaceChild()`
- 条件付き依存: `if ( secAction && secAction.key != actionsContainer.firstChild.dataset.action )` → `this.#createSecondaryAction()`
- 条件付き依存: `if (!secAction && actionsContainer)` → `item.removeChild()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.SEARCH && !result.payload.providesSearchMode && !result.payload.inPrivateWindow && result.providerName != "UrlbarPro...)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.REMOTE_TAB)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.TIP)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.TIP)` → `item.addEventListener()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.TIP)` → `this.input.focus()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderSearchTips" || result.payload.type == "dismissalAcknowledgment" )` → `this.#ariaNotifyLocalizedString()`
- 条件付き依存: `if (result.source == UrlbarShared.RESULT_SOURCE.BOOKMARKS)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.DYNAMIC)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.DYNAMIC)` → `this.#updateRowForDynamicType()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderTabToSearch")` → `item.setAttribute()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderSemanticHistorySearch")` → `item.setAttribute()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderInputHistory")` → `item.setAttribute()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderTopSites" && result.source == UrlbarShared.RESULT_SOURCE.HISTORY )` → `item.setAttribute()`
- 条件付き依存: `if (!( result.providerName == "UrlbarProviderTopSites" && result.source == UrlbarShared.RESULT_SOURCE.HISTORY ))` → `item.setAttribute()`
- 条件付き依存: `if (!( result.providerName == "UrlbarProviderTopSites" && result.source == UrlbarShared.RESULT_SOURCE.HISTORY ))` → `UrlbarShared.searchEngagementTelemetryType()`
- 条件付き依存: `if (result.payload.tail && result.payload.tailOffsetIndex > 0)` → `this.#fillTailSuggestionPrefix()`
- 条件付き依存: `if (result.payload.tail && result.payload.tailOffsetIndex > 0)` → `title.setAttribute()`
- 条件付き依存: `if (result.payload.tail && result.payload.tailOffsetIndex > 0)` → `item.toggleAttribute()`
- 条件付き依存: `if (!(result.payload.tail && result.payload.tailOffsetIndex > 0))` → `item.removeAttribute()`
- 条件付き依存: `if (!(result.payload.tail && result.payload.tailOffsetIndex > 0))` → `title.removeAttribute()`
- 条件付き依存: `if (tagsContainer)` → `result.getDisplayableValueAndHighlights()`
- 条件付き依存: `if (tags?.length)` → `tagsContainer.append()`
- 条件付き依存: `if (tags?.length)` → `tags.map()`
- 条件付き依存: `if (tags?.length)` → `document.createElement()`
- 条件付き依存: `if (tags?.length)` → `UrlbarShared.addTextContentWithHighlights()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `title.toggleAttribute()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `this.#l10nCache.ensure(label).then()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `this.#l10nCache.ensure()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `this.#l10nCache.get()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `title.setAttribute()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `action.setAttribute()`
- 条件付き依存: `if (result.isRichSuggestion || UrlbarPrefs.get("browser.nova.enabled"))` → `this.#updateRowForRichSuggestion()`
- 条件付き依存: `if (setURL)` → `result.getDisplayableValueAndHighlights()`
- 条件付き依存: `if (setURL)` → `this.#updateOverflowTooltip()`
- 条件付き依存: `if (setURL)` → `UrlbarContentUtils.isTextDirectionRTL()`
- 条件付き依存: `if (UrlbarContentUtils.isTextDirectionRTL(displayedUrl, window))` → `this.#offsetHighlights()`
- 条件付き依存: `if (setURL)` → `UrlbarShared.addTextContentWithHighlights()`
- 条件付き依存: `if (!(setURL))` → `this.#updateOverflowTooltip()`
- 条件付き依存: `if (this.#showsActionLabels)` → `item.toggleAttribute()`
- 条件付き依存: `if (actionSetter)` → `actionSetter()`
- 条件付き依存: `if (!(actionSetter))` → `item._originalActionSetter()`
- 条件付き依存: `if (!title.hasAttribute("is-url"))` → `title.setAttribute()`
- 条件付き依存: `if (!(!title.hasAttribute("is-url")))` → `title.removeAttribute()`
- 参照: `UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `actionsContainer.firstChild.dataset.action`, `attribute.name`, `element.className`, `favicon.src`, `item._content`, `item._content.className`, `item._content.id`, `item._originalActionSetter`, `item.attributes`, `item.classList`, `item.id`, `item.lastChild`, `item.result`, `item.result.type`, `result.autofill?.noVisitAction`, `result.getDisplayableValueAndHighlights("title").value`, `result.heuristic`, `result.isBestMatch`, `result.isBottomUrlSuggestion`, `result.isRichSuggestion`, `result.payload.action`, `result.payload.inPrivateWindow`, `result.payload.isPinned`, `result.payload.isPrivateEngine`, `result.payload.isSponsored`, `result.payload.keyword`, `result.payload.providesSearchMode`, `result.payload.shouldShowUrl`, `result.payload.suggestion`, `result.payload.suggestionObject?.suggestionType`, `result.payload.tail`, `result.payload.tailOffsetIndex`, `result.payload.titleL10n.args`, `result.payload.titleL10n.id`, `result.payload.type`, `result.payload.url`, `result.providerName`, `result.source`, `result.type`, `secAction.key`, `tags?.length`, `tagsContainer.textContent`, `this.#queryContext.tokens`, `this.#rows.children`, `this.#showsActionLabels`, `title.innerText`, `url.textContent`

## actionSetter()
- 位置: L2672-2674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setSwitchTabActionChiclet()`

## actionSetter()
- 位置: L2679-2682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.removeElementL10n()`
- 参照: `action.textContent`, `result.payload.device`

## actionSetter()
- 位置: L2686-2690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## actionSetter()
- 位置: L2703-2708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.setElementL10n()`
- 参照: `result.payload.engine`

## actionSetter()
- 位置: L2710-2714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## actionSetter()
- 位置: L2717-2724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.setElementL10n()`
- 参照: `result.payload.engine`, `result.payload.isGeneralPurposeEngine`

## actionSetter()
- 位置: L2726-2731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.setElementL10n()`
- 参照: `result.payload.engine`

## actionSetter()
- 位置: L2738-2741
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.removeElementL10n()`
- 参照: `action.textContent`, `result.payload.content`

## actionSetter()
- 位置: L2748-2752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## actionSetter()
- 位置: L2801-2805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## actionSetter()
- 位置: L2839-2843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## item._originalActionSetter()
- 位置: L2852-2855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.removeElementL10n()`
- 参照: `action.textContent`

## UrlbarView.#setRowSelectable()
- 位置: L2867-2879
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item._content.toggleAttribute()`, `item.toggleAttribute()`
- 条件付き依存: `if (isRowSelectable)` → `item._content.setAttribute()`
- 条件付き依存: `if (!(isRowSelectable))` → `item._content.getAttribute()`
- 条件付き依存: `if (item._content.getAttribute("role") == "option")` → `item._content.removeAttribute()`

## UrlbarView.#iconForResult()
- 位置: L2881-2919
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (result.payload.iconBlob)` → `this.#getBlobUrlForResult()`
- 参照: `UrlbarShared.ICON.DEFAULT`, `UrlbarShared.ICON.HISTORY`, `UrlbarShared.ICON.SEARCH_GLASS`, `UrlbarShared.ICON.TRENDING`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.SEARCH`, `result.payload.icon`, `result.payload.iconBlob`, `result.payload.trending`, `result.source`, `result.type`

## UrlbarView.#getBlobUrlForResult()
- 位置: L2921-2940
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (resultUrl)` → `this.#blobUrlsByResultUrl?.get()`
- 条件付き依存: `if (!blobUrl)` → `URL.createObjectURL()`
- 条件付き依存: `if (!blobUrl)` → `this.#blobUrlsByResultUrl.set()`
- 参照: `result.payload.originalUrl`, `result.payload.url`, `this.#blobUrlsByResultUrl`

## UrlbarView.#updateRowForDynamicType()
- 位置: L2946-2978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `item.querySelector()`, `item.setAttribute()`, `this.#updateElementForDynamicType()`
- 条件付き依存: `if (update.l10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(update.l10n))` → `update.hasOwnProperty()`
- 条件付き依存: `if (update.hasOwnProperty("textContent"))` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (update.hasOwnProperty("textContent"))` → `UrlbarShared.addTextContentWithHighlights()`
- 参照: `item._elements`, `item.id`, `node.id`, `result.payload`, `result.payload.dynamicType`, `update.highlights`, `update.l10n`, `update.textContent`

## UrlbarView.#updateRowForRichSuggestion()
- 位置: L2984-3044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `item._elements.get()`, `item.toggleAttribute()`, `this.#setRowSelectable()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `String()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `item.setAttribute()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `favicon.setAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconSize))` → `item.removeAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconSize))` → `favicon.removeAttribute()`
- 条件付き依存: `if (result.richSuggestionIconVariation)` → `favicon.setAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconVariation))` → `favicon.removeAttribute()`
- 条件付き依存: `if (result.payload.descriptionL10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (result.payload.descriptionLearnMoreTopic)` → `description.querySelector()`
- 条件付き依存: `if (learnMoreLink)` → `window.getHelpLinkURL()`
- 条件付き依存: `if (!(learnMoreLink))` → `console.warn()`
- 条件付き依存: `if (!(result.payload.descriptionL10n))` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (result.payload.bottomTextL10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(result.payload.bottomTextL10n))` → `this.#l10nCache.removeElementL10n()`
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `description.textContent`, `learnMoreLink.dataset.url`, `result.payload.bottomTextL10n`, `result.payload.description`, `result.payload.descriptionL10n`, `result.payload.descriptionLearnMoreTopic`, `result.richSuggestionIconSize`, `result.richSuggestionIconVariation`, `result.type`

## UrlbarView.#updateRowContentForBottomUrl()
- 位置: L3050-3102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.prepareUrlForDisplay()`, `UrlbarShared.searchEngagementTelemetryType()`, `item._elements.get()`, `item.classList.add()`, `item.setAttribute()`, `item.toggleAttribute()`, `this.#iconForResult()`, `this.#l10nCache.setElementL10n()`, `this.#setResultTitle()`, `this.#setRowSelectable()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `String()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `item.setAttribute()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `favicon.setAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconSize))` → `item.removeAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconSize))` → `favicon.removeAttribute()`
- 条件付き依存: `if (result.payload.subtitleL10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(result.payload.subtitleL10n))` → `this.#l10nCache.removeElementL10n()`
- 参照: `description.textContent`, `favicon.src`, `result.payload.bottomTextL10n`, `result.payload.description`, `result.payload.isSponsored`, `result.payload.subtitle`, `result.payload.subtitleL10n`, `result.payload.url`, `result.richSuggestionIconSize`, `subtitle.textContent`, `url.textContent`

## UrlbarView.#updateIndices()
- 位置: L3110-3168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getNextSelectableElement()`, `this.#isElementVisible()`, `this.#overflowObserver.disconnect()`, `this.#updateRowLabel()`, `this.getFirstSelectableElement()`, `this.input.toggleAttribute()`
- 条件付き依存: `if (visible)` → `this.visibleResults.push()`
- 条件付き依存: `if (result.exposureTelemetry)` → `this.controller.engagementEvent.addExposure()`
- 条件付き依存: `if (visible)` → `item.querySelectorAll()`
- 条件付き依存: `if (visible)` → `this.#overflowObserver.observe()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `result.exposureTelemetry`, `result.heuristic`, `result.payload.suggestion`, `result.rowIndex`, `result.type`, `selectableElement.elementIndex`, `this.#queryContext`, `this.#rows.children`, `this.#rows.children.length`, `this.visibleResults`, `this.visibleResults.length`

## UrlbarView.#updateRowLabel()
- 位置: L3190-3252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.deepEqual()`, `groupAriaLabel.setAttribute()`, `item._elements.get()`, `this.#l10nCache.ensure()`, `this.#l10nCache.ensure(label).then()`, `this.#l10nCache.get()`, `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if ( isItemVisible && // Show the search suggestions label only if there are other visible // results before this one that aren't the heuristic or suggestions. !...)` → `this.#rowLabel()`
- 条件付き依存: `if ( !label || item.result.hideRowLabel || UrlbarShared.deepEqual(label, lastVisibleLabel) )` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (groupAriaLabel)` → `groupAriaLabel.remove()`
- 条件付き依存: `if (groupAriaLabel)` → `item._elements.delete()`
- 条件付き依存: `if (!groupAriaLabel)` → `document.createElement()`
- 条件付き依存: `if (!groupAriaLabel)` → `item._content.insertBefore()`
- 条件付き依存: `if (!groupAriaLabel)` → `item._elements.set()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `groupAriaLabel.className`, `item._content.firstChild`, `item.result.hideRowLabel`, `item.result.payload.suggestion`, `item.result.type`, `label.args`, `label.id`, `message?.attributes.label`

## UrlbarView.#rowLabel()
- 位置: L3264-3328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.URL`, `row.result.heuristic`, `row.result.isBestMatch`, `row.result.payload.engine`, `row.result.payload.trending`, `row.result.providerName`, `row.result.rowLabel`, `row.result.type`, `this.#queryContext.results`, `this.#queryContext.results[0].providerName`, `this.#queryContext?.searchString`, `this.controller.engineStore.default?.name`

## UrlbarView.#setRowVisibility()
- 位置: L3334-3336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.toggleAttribute()`

## UrlbarView.#ariaNotifyLocalizedString()
- 位置: async L3338-3341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatValue()`, `element.ariaNotify()`

## UrlbarView.#isElementVisible()
- 位置: L3351-3357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.hasAttribute()`, `this.#getRowFromElement()`
- 参照: `element.style.display`

## UrlbarView.#removeStaleRows()
- 位置: L3359-3389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.hasAttribute()`, `this.#updateIndices()`, `this.controller.engagementEvent.acceptTentativeExposures()`
- 条件付き依存: `if (row.hasAttribute("stale"))` → `row.remove()`
- 条件付き依存: `if (!(row.hasAttribute("stale")))` → `this.#setRowVisibility()`
- 条件付き依存: `if ( this.input.searchMode?.source != UrlbarShared.RESULT_SOURCE.ACTIONS && this.visibleResults[0]?.source != UrlbarShared.RESULT_SOURCE.ACTIONS )` → `this.#rows.toggleAttribute()`
- 参照: `UrlbarShared.RESULT_SOURCE.ACTIONS`, `row.previousElementSibling`, `this.#rows.lastElementChild`, `this.input.searchMode?.source`, `this.visibleResults`, `this.visibleResults[0]?.source`

## UrlbarView.#startRemoveStaleRowsTimer()
- 位置: L3391-3400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.#cancelRemoveStaleRowsTimer()`, `this.#removeStaleRows()`, `window.setTimeout()`
- 参照: `this.#removeStaleRowsTimer`

## UrlbarView.#cancelRemoveStaleRowsTimer()
- 位置: L3402-3407
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#removeStaleRowsTimer)` → `window.clearTimeout()`
- 参照: `this.#removeStaleRowsTimer`

## UrlbarView.#selectElement()
- 位置: L3409-3464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.matches()`, `this.#getRowFromElement()`, `this.#setAccessibleFocus()`
- 条件付き依存: `if (this.#selectedElement)` → `this.#selectedElement.toggleAttribute()`
- 条件付き依存: `if (this.#selectedElement)` → `this.#selectedElement.removeAttribute()`
- 条件付き依存: `if (this.#selectedElement)` → `this.#getSelectedRow()`
- 条件付き依存: `if (this.#selectedElement)` → `row?.toggleAttribute()`
- 条件付き依存: `if (element)` → `element.toggleAttribute()`
- 条件付き依存: `if (element)` → `element.setAttribute()`
- 条件付き依存: `if (element)` → `row?.hasAttribute()`
- 条件付き依存: `if (row?.hasAttribute("row-selectable"))` → `row?.toggleAttribute()`
- 条件付き依存: `if (element != row)` → `row?.toggleAttribute()`
- 条件付き依存: `if (element)` → `["smartbar", "newtab_searchbar"].includes()`
- 条件付き依存: `if (["smartbar", "newtab_searchbar"].includes(this.input.sapName))` → `(row ?? element).scrollIntoView()`
- 条件付き依存: `if (result)` → `this.controller.parentController.onBeforeSelection()`
- 条件付き依存: `if (updateInput)` → `element?.classList?.contains()`
- 条件付き依存: `if (updateInput)` → `this.input.setValueFromResult()`
- 条件付き依存: `if (!(updateInput))` → `this.input.setResultForCurrentValue()`
- 条件付き依存: `if (result)` → `this.controller.parentController.onSelection()`
- 参照: `row?.result`, `this.#rawSelectedElement`, `this.#selectedElement`, `this.input.sapName`

## UrlbarView.#getClosestSelectableElement()
- 位置: L3481-3501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.classList.contains()`, `element.closest()`, `element.hasAttribute()`, `this.#isElementVisible()`
- 参照: `(element)._content`

## UrlbarView.#isSelectableElement()
- 位置: L3511-3513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getClosestSelectableElement()`

## UrlbarView.#isRowArrowSelectable()
- 位置: L3524-3534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getNextSelectableElement()`, `this.#getRowFromElement()`
- 参照: `row.result?.providerName`, `this.#rows.children`, `this.#rows.children.length`

## UrlbarView.getFirstSelectableElement()
- 位置: L3542-3549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isSelectableElement()`
- 条件付き依存: `if (element && !this.#isSelectableElement(element))` → `this.#getNextSelectableElement()`
- 参照: `this.#rows.firstElementChild`

## UrlbarView.getLastSelectableElement()
- 位置: L3557-3564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isSelectableElement()`
- 条件付き依存: `if (element && !this.#isSelectableElement(element))` → `this.#getPreviousSelectableElement()`
- 参照: `this.#rows.lastElementChild`

## UrlbarView.#getNextSelectableElement()
- 位置: L3576-3596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getKeyboardSelectablesInRow()`, `this.#getRowFromElement()`, `this.#isSelectableElement()`
- 条件付き依存: `if (selectables.length)` → `selectables.indexOf()`
- 条件付き依存: `if (next && !this.#isSelectableElement(next))` → `this.#getNextSelectableElement()`
- 参照: `row.nextElementSibling`, `selectables.length`

## UrlbarView.#getPreviousSelectableElement()
- 位置: L3608-3631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getKeyboardSelectablesInRow()`, `this.#getRowFromElement()`, `this.#isSelectableElement()`
- 条件付き依存: `if (selectables.length)` → `selectables.indexOf()`
- 条件付き依存: `if (previous && !this.#isSelectableElement(previous))` → `this.#getPreviousSelectableElement()`
- 参照: `row.previousElementSibling`, `selectables.length`

## UrlbarView.#getKeyboardSelectablesInRow()
- 位置: L3637-3650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `row.querySelectorAll()`, `selectables.sort()`
- 参照: `a.localName`, `b.localName`

## UrlbarView.#getSelectedRow()
- 位置: L3660-3662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getRowFromElement()`
- 参照: `this.#selectedElement`

## UrlbarView.#getRowFromElement()
- 位置: L3670-3672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element?.closest()`

## UrlbarView.#getRowByResultId()
- 位置: L3681-3688
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `row.result?.id`, `this.#rows.children`

## UrlbarView.#setAccessibleFocus()
- 位置: L3690-3700
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!item.id)` → `getUniqueId()`
- 条件付き依存: `if (item)` → `this.input.inputField.setAttribute()`
- 条件付き依存: `if (!(item))` → `this.input.inputField.removeAttribute()`
- 参照: `item.id`

## UrlbarView.#setResultTitle()
- 位置: L3710-3773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.addTextContentWithHighlights()`, `result.getDisplayableValueAndHighlights()`, `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (result.payload.titleL10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `result.payload.l10nRestrictKeywords[0].toLowerCase()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `result.payload.l10nRestrictKeywords .map(keyword => `@${keyword.toLowerCase()}`) .join()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `result.payload.l10nRestrictKeywords .map()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `keyword.toLowerCase()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(result.type == UrlbarShared.RESULT_TYPE.RESTRICT))` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderTokenAliasEngines" && UrlbarPrefs.getScotchBonnetPref("searchRestrictKeywords.featureGate") )` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!( result.providerName == "UrlbarProviderTokenAliasEngines" && UrlbarPrefs.getScotchBonnetPref("searchRestrictKeywords.featureGate") ))` → `this.#l10nCache.setElementL10n()`
- 参照: `UrlbarShared.RESULT_TYPE.RESTRICT`, `result.payload.engine`, `result.payload.keywords`, `result.payload.l10nRestrictKeywords`, `result.payload.providesSearchMode`, `result.payload.text`, `result.payload.titleL10n`, `result.providerName`, `result.type`, `this.#queryContext.tokens`, `titleAndHighlights.highlights`, `titleAndHighlights.value`, `titleNode.textContent`

## UrlbarView.#offsetHighlights()
- 位置: L3783-3791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `highlights.map()`

## UrlbarView.#setSwitchTabActionChiclet()
- 位置: L3804-3826
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `actionNode.classList.add()`, `splitview.tabs.some()`, `this.#l10nCache.setElementL10n()`, `this.#updateTabGroupAction()`, `this.#updateUserContextAction()`
- 条件付き依存: `if (!UrlbarPrefs.get("browser.nova.enabled"))` → `this.#updateOtherActionChicletsProton()`
- 参照: `result.payload.url`, `tab.linkedBrowser.currentURI.spec`, `this.chromeWindow.gBrowser.selectedTab.splitview`

## UrlbarView.#updateOtherActionChicletsProton()
- 位置: L3829-3874
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.isContainerUserContextId()`, `actionNode.parentNode.querySelector()`
- 条件付き依存: `if (!contextualIdentityAction)` → `actionNode.cloneNode()`
- 条件付き依存: `if (!contextualIdentityAction)` → `contextualIdentityAction.classList.add()`
- 条件付き依存: `if (!contextualIdentityAction)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (!contextualIdentityAction)` → `actionNode.parentNode.insertBefore()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && UrlbarShared.isContainerUserContextId(result.payload.userContext?.id) )` → `this.#addContextualIdentityToSwitchTabChiclet()`
- 条件付き依存: `if (!( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && UrlbarShared.isContainerUserContextId(result.payload.userContext?.id) ))` → `contextualIdentityAction?.remove()`
- 条件付き依存: `if (!tabGroupAction)` → `actionNode.cloneNode()`
- 条件付き依存: `if (!tabGroupAction)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (!tabGroupAction)` → `actionNode.parentNode.insertBefore()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && result.payload.tabGroup )` → `this.#addGroupToSwitchTabChiclet()`
- 条件付き依存: `if (!( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && result.payload.tabGroup ))` → `tabGroupAction?.remove()`
- 参照: `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.payload.tabGroup`, `result.payload.userContext?.id`, `result.type`

## UrlbarView.#addContextualIdentityToSwitchTabChiclet()
- 位置: L3877-3916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actionNode.classList.contains()`
- 条件付き依存: `if (label)` → `actionNode.classList.add()`
- 条件付き依存: `if (label)` → `actionNode.classList.remove()`
- 条件付き依存: `if (color)` → `actionNode.className.replace()`
- 条件付き依存: `if (color)` → `actionNode.classList.add()`
- 条件付き依存: `if (label)` → `document.createElement()`
- 条件付き依存: `if (label)` → `textModeLabel.classList.add()`
- 条件付き依存: `if (label)` → `actionNode.appendChild()`
- 条件付き依存: `if (label)` → `iconModeLabel.classList.add()`
- 条件付き依存: `if (iconUrl)` → `document.createElement()`
- 条件付き依存: `if (iconUrl)` → `userContextIcon.classList.add()`
- 条件付き依存: `if (iconUrl)` → `userContextIcon.setAttribute()`
- 条件付き依存: `if (iconUrl)` → `iconModeLabel.appendChild()`
- 条件付き依存: `if (label)` → `actionNode.setAttribute()`
- 参照: `actionNode.className`, `actionNode.innerHTML`, `result.payload.userContext`, `textModeLabel.innerText`, `userContextIcon.src`

## UrlbarView.#addGroupToSwitchTabChiclet()
- 位置: L3919-3970
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actionNode.appendChild()`, `actionNode.classList.add()`, `actionNode.classList.remove()`, `actionNode.style.setProperty()`, `document.createElement()`, `fullWidthModeLabel.classList.add()`, `group.style.getPropertyValue()`, `narrowWidthModeLabel.classList.add()`, `this.chromeWindow.gBrowser.getTabGroupById()`
- 条件付き依存: `if (!group)` → `actionNode.remove()`
- 条件付き依存: `if (!(group.label))` → `this.#l10nCache.setElementL10n()`
- 参照: `actionNode.innerHTML`, `fullWidthModeLabel.textContent`, `group.label`, `narrowWidthModeLabel.textContent`, `result.payload.tabGroup`

## UrlbarView.#updateUserContextAction()
- 位置: L3972-4017
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.isContainerUserContextId()`, `contextNode.toggleAttribute()`, `item._elements.get()`, `n.startsWith()`
- 条件付き依存: `if (!iconUrl && !label)` → `contextNode.toggleAttribute()`
- 条件付き依存: `if (!iconUrl && !label)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (iconUrl)` → `contextNode.style.setProperty()`
- 条件付き依存: `if (!(iconUrl))` → `contextNode.style.removeProperty()`
- 条件付き依存: `if (n.startsWith("identity-color-"))` → `contextNode.classList.remove()`
- 条件付き依存: `if (color)` → `contextNode.classList.add()`
- 条件付き依存: `if (label)` → `contextNode.setAttribute()`
- 条件付き依存: `if (!(label))` → `contextNode.removeAttribute()`
- 参照: `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `contextNode.classList`, `contextNode.textContent`, `result.payload.userContext`, `result.payload.userContext?.id`, `result.type`

## UrlbarView.#updateTabGroupAction()
- 位置: L4019-4083
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `containerNode.style.setProperty()`, `containerNode.toggleAttribute()`, `group.label.trim()`, `group.style.getPropertyValue()`, `item._elements.get()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && result.payload.tabGroup )` → `this.chromeWindow.gBrowser.getTabGroupById()`
- 条件付き依存: `if (!group)` → `containerNode.toggleAttribute()`
- 条件付き依存: `if (!group)` → `containerNode.removeAttribute()`
- 条件付き依存: `if (!group)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (label)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (label)` → `containerNode.setAttribute()`
- 条件付き依存: `if (!(label))` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(label))` → `containerNode.removeAttribute()`
- 参照: `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `fullLabelNode.textContent`, `result.payload.tabGroup`, `result.type`, `shortLabelNode.textContent`

## UrlbarView.#fillTailSuggestionPrefix()
- 位置: L4093-4103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item._elements.get()`, `result.payload.suggestion.substring()`
- 参照: `result.payload.tailOffsetIndex`, `result.payload.tailPrefix`, `tailPrefixCharNode.textContent`, `tailPrefixStrNode.textContent`

## UrlbarView.#enableOrDisableRowWrap()
- 位置: L4105-4109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getBoundsWithoutFlushing()`, `this.#rows.toggleAttribute()`, `this.oneOffSearchButtons?.container.toggleAttribute()`
- 参照: `getBoundsWithoutFlushing(this.input).width`, `this.input`

## UrlbarView.#setElementOverflowing()
- 位置: L4119-4122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.toggleAttribute()`, `this.#updateOverflowTooltip()`

## UrlbarView.#updateOverflowTooltip()
- 位置: L4135-4147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.hasAttribute()`
- 条件付き依存: `if (typeof tooltip == "string")` → `this.#tooltips.set()`
- 条件付き依存: `if (!(typeof tooltip == "string"))` → `this.#tooltips.get()`
- 条件付き依存: `if (element.hasAttribute("overflow") && tooltip)` → `element.setAttribute()`
- 条件付き依存: `if (!(element.hasAttribute("overflow") && tooltip))` → `element.removeAttribute()`

## UrlbarView.#updateOverflowState()
- 位置: L4149-4157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entries.map()`, `this.#setElementOverflowing()`
- 参照: `target.clientWidth`, `target.scrollWidth`

## UrlbarView.#pickSearchTipIfPresent()
- 位置: L4169-4188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buttons.get()`, `this.input.pickElement()`
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `result.type`, `this.#queryContext`, `this.#queryContext.results`, `this.#queryContext.results.length`, `this.#rows.firstElementChild._buttons`, `this.isOpen`

## UrlbarView.#cacheL10nStrings()
- 位置: async L4201-4227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.#cacheL10nIDArgsForSearchService()`, `this.#l10nCache.ensureAll()`
- 条件付き依存: `if (UrlbarPrefs.get("groupLabels.enabled"))` → `idArgs.push()`
- 条件付き依存: `if (suggestSponsoredEnabled)` → `idArgs.push()`

## UrlbarView.#cacheL10nIDArgsForSearchService()
- 位置: L4236-4274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `idArgs.push()`
- 条件付き依存: `if (UrlbarPrefs.get("groupLabels.enabled"))` → `idArgs.push()`
- 参照: `this.controller.engineStore.default.name`, `this.controller.engineStore.initialized`

## UrlbarView.#openInCommands()
- 位置: L4282-4311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `commands.push()`
- 条件付き依存: `if ( !this.input.isPrivate && UrlbarPrefs.get("privacy.userContext.enabled") )` → `commands.push()`
- 参照: `this.input.isPrivate`

## UrlbarView.#hasMenuButton()
- 位置: L4321-4326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#canOpenInNewTarget()`, `this.#getResultMenuCommands()`
- 参照: `result.heuristic`

## UrlbarView.#updateMenuButtonKeyboardAccessibility()
- 位置: L4333-4340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `button.toggleAttribute()`, `this.#rows.querySelectorAll()`

## UrlbarView.#canOpenInNewTarget()
- 位置: L4348-4355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.getLoadRequestFromResult()`
- 参照: `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.type`, `this.input.handlesOpenInCommands`

## UrlbarView.#getMenuCommands()
- 位置: L4367-4388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.#canOpenInNewTarget()`, `this.#getResultMenuCommands()`
- 参照: `RESULT_MENU_COMMANDS.TOGGLE_KEYBOARD_ACCESSIBLE`, `this.#openInCommands`

## UrlbarView.#getResultMenuCommands()
- 位置: L4396-4439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resultMenuCommands.has()`, `this.#resultMenuCommands.set()`
- 条件付き依存: `if (this.#resultMenuCommands.has(result))` → `this.#resultMenuCommands.get()`
- 条件付き依存: `if (commands)` → `this.#resultMenuCommands.set()`
- 条件付き依存: `if (result.payload.isBlockable)` → `commands.push()`
- 条件付き依存: `if (result.payload.helpUrl)` → `commands.push()`
- 条件付き依存: `if (result.payload.isManageable)` → `commands.push()`
- 参照: `RESULT_MENU_COMMANDS.DISMISS`, `RESULT_MENU_COMMANDS.HELP`, `RESULT_MENU_COMMANDS.MANAGE`, `commands.length`, `result.commands`, `result.payload.blockL10n`, `result.payload.helpL10n`, `result.payload.helpUrl`, `result.payload.isBlockable`, `result.payload.isManageable`

## UrlbarView.#populateResultMenu()
- 位置: async L4448-4490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.map()`, `commands.map(e => e.l10n).filter()`, `document.createElement()`, `menuitem.classList.add()`, `panel.appendChild()`, `this.#l10nCache.ensureAll()`
- 条件付き依存: `if (data.name == "separator")` → `panel.appendChild()`
- 条件付き依存: `if (data.name == "separator")` → `document.createElement()`
- 条件付き依存: `if (data.submenu)` → `menuitem.toggleAttribute()`
- 条件付き依存: `if (data.submenu)` → `document.createElement()`
- 条件付き依存: `if (data.submenu)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (data.submenu)` → `label.hasAttribute()`
- 条件付き依存: `if (label.hasAttribute("accesskey"))` → `menuitem.setAttribute()`
- 条件付き依存: `if (label.hasAttribute("accesskey"))` → `label.getAttribute()`
- 条件付き依存: `if (label.hasAttribute("accesskey"))` → `label.removeAttribute()`
- 条件付き依存: `if (data.submenu)` → `menuitem.appendChild()`
- 条件付き依存: `if (!(data.submenu))` → `this.#l10nCache.setElementL10n()`
- 参照: `data.checked`, `data.l10n`, `data.name`, `data.openIn`, `data.submenu`, `data.type`, `e.l10n`, `menuitem.checked`, `menuitem.dataset.command`, `menuitem.dataset.openIn`, `menuitem.type`, `panel.textContent`, `submenu.slot`, `this.resultMenu`

## UrlbarView.#populateContainerSubmenu()
- 位置: async L4499-4534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `UrlbarContentUtils.getContainers()`, `document.createElement()`, `menuitem.style.setProperty()`, `panel.appendChild()`, `this.#createContainerMenuItem()`, `this.controller.parentController.openContainerCreationPanel()`, `this.controller.parentController.openPreferences()`
- 参照: `container.colorCode`, `container.iconURL`, `container.name`, `container.userContextId`, `menuitem.dataset.usercontextid`, `menuitem.textContent`, `panel.textContent`

## UrlbarView.#createContainerMenuItem()
- 位置: L4546-4551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.l10n.setAttributes()`, `menuitem.addEventListener()`

## UrlbarView.on_SelectedOneOffButtonChanged()
- 位置: L4555-4721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item._elements.get()`
- 条件付き依存: `if (source)` → `UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 条件付き依存: `if ( result.heuristic && !this.selectedElement && (localSearchMode || engine) )` → `item.setAttribute()`
- 条件付き依存: `if (!( result.heuristic && !this.selectedElement && (localSearchMode || engine) ))` → `item.removeAttribute()`
- 条件付き依存: `if (result.heuristic)` → `result.getDisplayableValueAndHighlights()`
- 条件付き依存: `if (localSearchMode || engine)` → `item.setAttribute()`
- 条件付き依存: `if (!(localSearchMode || engine))` → `item.removeAttribute()`
- 条件付き依存: `if (localSearchMode)` → `UrlbarShared.getResultSourceName()`
- 条件付き依存: `if (localSearchMode)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (result.heuristic)` → `item.setAttribute()`
- 条件付き依存: `if (engine && !result.payload.inPrivateWindow)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (item._originalActionSetter)` → `item._originalActionSetter()`
- 条件付き依存: `if (!(item._originalActionSetter))` → `console.error()`
- 条件付き依存: `if (!(engine && !result.payload.inPrivateWindow))` → `item.removeAttribute()`
- 条件付き依存: `if ( result.heuristic || (result.payload.inPrivateWindow && !result.payload.isPrivateEngine) )` → `this.#iconForResult()`
- 参照: `UrlbarShared.ICON.DEFAULT`, `UrlbarShared.ICON.SEARCH_GLASS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.SEARCH`, `engine.name`, `favicon.src`, `item._originalActionSetter`, `item.result`, `localSearchMode.source`, `localSearchMode?.icon`, `m.source`, `result.getDisplayableValueAndHighlights("title").value`, `result.heuristic`, `result.payload.engine`, `result.payload.icon`, `result.payload.inPrivateWindow`, `result.payload.isPrivateEngine`, `result.payload.originalEngine`, `result.payload.suggestion`, `result.source`, `result.type`, `this.#queryContext`, `this.#queryContext.searchString`, `this.#rows.children`, `this.input.searchMode`, `this.input.searchMode.isPreview`, `this.isOpen`, `this.oneOffSearchButtons.selectedButton?.engine`, `this.oneOffSearchButtons.selectedButton?.image`, `this.oneOffSearchButtons.selectedButton?.source`, `this.selectedElement`, `title.textContent`

## UrlbarView.on_blur()
- 位置: L4723-4730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.close()`

## UrlbarView.on_mousedown()
- 位置: L4732-4782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.classList.contains()`, `element.getAttribute()`, `this.#getClosestSelectableElement()`, `window.addEventListener()`
- 条件付き依存: `if (!element.classList.contains("urlbarView-button"))` → `this.#selectElement()`
- 条件付き依存: `if (!element.classList.contains("urlbarView-button"))` → `this.controller.parentController.speculativeConnect()`
- 参照: `event.button`, `event.target`, `this.#mousedownSelectedElement`, `this.#queryContext`, `this.selectedResult`

## UrlbarView.on_mouseup()
- 位置: L4784-4823
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.getAttribute()`, `event.composedPath()`, `this.#getClosestSelectableElement()`, `window.removeEventListener()`
- 条件付き依存: `if (element && element.getAttribute("aria-disabled") != "true")` → `this.input.pickElement()`
- 条件付き依存: `if (this.#mousedownSelectedElement?.isConnected)` → `this.clearSelection()`
- 参照: `event.button`, `eventTarget.ELEMENT_NODE`, `eventTarget.nodeType`, `this.#mousedownSelectedElement`, `this.#mousedownSelectedElement?.isConnected`

## UrlbarView.on_resize()
- 位置: L4825-4827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#enableOrDisableRowWrap()`

## UrlbarView.on_click()
- 位置: L4829-4863
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event .composedPath()`, `event .composedPath() .find()`, `this.input.pickResult()`
- 条件付き依存: `if ( menuitem.dataset.command == RESULT_MENU_COMMANDS.TOGGLE_KEYBOARD_ACCESSIBLE )` → `UrlbarPrefs.toggleResultMenuKeyboardAccessible()`
- 条件付き依存: `if ( menuitem.dataset.command == RESULT_MENU_COMMANDS.TOGGLE_KEYBOARD_ACCESSIBLE )` → `this.#updateMenuButtonKeyboardAccessibility()`
- 条件付き依存: `if (menuitem.dataset.command == RESULT_MENU_COMMANDS.HELP)` → `UrlbarContentUtils.getSupportUrl()`
- 参照: `RESULT_MENU_COMMANDS.HELP`, `RESULT_MENU_COMMANDS.TOGGLE_KEYBOARD_ACCESSIBLE`, `menuitem.dataset.command`, `menuitem.dataset.openIn`, `menuitem.dataset.url`, `menuitem.dataset.usercontextid`, `menuitem.hasSubmenu`, `node.localName`, `result.payload.helpUrl`, `this.#resultMenuResult`

## UrlbarView.on_showing()
- 位置: L4865-4894
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this.resultMenu)` → `this.resultMenu.lastAnchorNode .closest(".urlbarView-row") .toggleAttribute()`
- 条件付き依存: `if (event.target == this.resultMenu)` → `this.resultMenu.lastAnchorNode .closest()`
- 条件付き依存: `if (event.target == this.resultMenu)` → `triggeringEvent.detail.target.closest()`
- 条件付き依存: `if (splitButton)` → `this.#resultMenuResult.payload.buttons.find()`
- 条件付き依存: `if (!(splitButton))` → `this.#getMenuCommands()`
- 条件付き依存: `if (event.target == this.resultMenu)` → `this.#populateResultMenu()`
- 条件付き依存: `if (event.target.dataset.openIn == "container-tab")` → `this.#populateContainerSubmenu()`
- 参照: `b.name`, `event.target`, `event.target.dataset.openIn`, `event.target.submenuPanel`, `mainButton.dataset.name`, `splitButton.firstElementChild`, `this.#resultMenuResult`, `this.#resultMenuResult.payload.buttons.find( b => b.name == buttonName ).menu`, `this.resultMenu`, `this.resultMenu.triggeringEvent`, `triggeringEvent.type`

## UrlbarView.on_hidden()
- 位置: L4896-4903
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.currentTarget.lastAnchorNode ?.closest()`, `event.currentTarget.lastAnchorNode ?.closest(".urlbarView-row") ?.toggleAttribute()`
- 参照: `event.currentTarget`, `event.target`

## UrlbarView.on_contextmenu()
- 位置: L4905-4929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `event.preventDefault()`, `event.target.closest()`, `this.#getMenuCommands()`, `this.resultMenu.toggle()`
- 参照: `row.result`, `this.#resultMenuResult`

## UrlbarView.clearTopSitesCache()
- 位置: L4931-4933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.queryContextCache.clearTopSitesCache()`

## UrlbarView.clearL10nCache()
- 位置: L4935-4937
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#l10nCache.clear()`

## QueryContextCache.constructor()
- 位置: L4965-4967
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#size`

## QueryContextCache.size()
- 位置: L4972-4974
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#size`

## QueryContextCache.topSitesContext()
- 位置: L4977-4979
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#topSitesContext`

## QueryContextCache.clearTopSitesCache()
- 位置: L4981-4983
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#topSitesContext`

## QueryContextCache.clear()
- 位置: L4988-4991
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearTopSitesCache()`
- 参照: `this.#cache`

## QueryContextCache.put()
- 位置: L5001-5042
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cache.findIndex()`, `this.#cache.unshift()`
- 条件付き依存: `if (!searchString)` → `queryContext.results?.some()`
- 条件付き依存: `if (!searchString)` → `queryContext.results.some()`
- 条件付き依存: `if (index != -1)` → `this.#cache.splice()`
- 参照: `e.currentPage`, `e.searchString`, `queryContext.currentPage`, `queryContext.results.length`, `queryContext.searchString`, `r.providerName`, `this.#cache`, `this.#cache.length`, `this.#topSitesContext`, `this.size`

## QueryContextCache.get()
- 位置: L5052-5056
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cache.find()`
- 参照: `e.currentPage`, `e.searchString`
