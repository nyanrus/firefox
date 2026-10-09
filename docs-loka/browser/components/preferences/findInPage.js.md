# browser/components/preferences/findInPage.js

source: browser/components/preferences/findInPage.js
source-hash: 92cd707bc84000268b7dc508c183b5760a5d3eb1
lines: 995

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`, `customElements.get()`

## HighlightableButton.inheritedAttributes()
- 位置: L16-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 参照: `super.inheritedAttributes`

## init()
- 位置: L58-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._recomputeTooltipPositions()`, `window.addEventListener()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `this.searchInput.addEventListener()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `document .getElementById("search-results-back-button") .addEventListener()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `document .getElementById()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `this.handleSearchResultsBack()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `window.addEventListener()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `this.searchInput.updateComplete.then()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `this.searchInput.focus()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `window.requestIdleCallback()`
- 条件付き依存: `if (!this.searchInput.hidden)` → `this.initializeCategories()`
- 参照: `this.inited`, `this.searchInput`, `this.searchInput.hidden`, `this.searchTooltipContainer`

## handleEvent()
- 位置: async L90-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.initializeCategories()`, `this.searchFunction()`

## handleSearchResultsBack()
- 位置: async L96-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.initializeCategories()`, `this.searchFunction()`
- 参照: `this.query`, `this.searchInput`, `this.searchInput.value`

## queryMatchesContent()
- 位置: L114-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.toLowerCase()`, `content.toLowerCase().includes()`, `query.toLowerCase()`

## initializeCategories()
- 位置: L132-137
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._categoriesInitialized)` → `this.runCategoryInitialization()`
- 参照: `this._categoriesInitialized`

## runCategoryInitialization()
- 位置: async L146-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Services.obs.notifyObservers()`, `[...document.querySelectorAll("setting-pane, setting-group")].map()`, `category.init()`, `document.querySelectorAll()`, `gCategoryInits.values()`, `queueMicrotask()`
- 条件付き依存: `if (document.hasPendingL10nMutations)` → `document.addEventListener()`
- 参照: `document.hasPendingL10nMutations`, `el.updateComplete`
- XPCOM: `Services.obs`

## textNodeDescendants()
- 位置: L177-195
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node.nodeType === node.TEXT_NODE)` → `all.push()`
- 条件付き依存: `if (!node.hidden)` → `all.concat()`
- 条件付き依存: `if (!node.hidden)` → `this.textNodeDescendants()`
- 条件付き依存: `if (originalNode.shadowRoot)` → `all.concat()`
- 条件付き依存: `if (originalNode.shadowRoot)` → `this.textNodeDescendants()`
- 参照: `node.TEXT_NODE`, `node.firstChild`, `node.hidden`, `node.nextSibling`, `node.nodeType`, `originalNode.shadowRoot`

## highlightMatches()
- 位置: L225-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createRange()`, `indices.push()`, `range.setEnd()`, `range.setStart()`, `textSearch.indexOf()`, `this.getFindSelection()`, `this.getFindSelection(startNode.documentGlobal).addRange()`
- 参照: `indices.length`, `nodeSizes.length`, `searchPhrase.length`, `startNode.documentGlobal`, `this.searchResultsHighlighted`

## getFindSelection()
- 位置: L288-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.getSelection()`, `docShell .QueryInterface()`, `docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsISelectionDisplay) .QueryInterface()`, `selection.setColors()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsISelectionController`, `Ci.nsISelectionController.SELECTION_FIND`, `Ci.nsISelectionDisplay`, `win.docShell`
- XPCOM: [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsISelectionController`](../../../dom/base/nsISelectionController.idl.md) / [`nsISelectionDisplay`](../../../dom/base/nsISelectionController.idl.md)

## searchFunction()
- 位置: async L311-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `event.target.value.trim()`, `event.target.value.trim().toLowerCase()`, `query.includes()`, `this.removeAllSearchIndicators()`, `window.dispatchEvent()`
- 条件付き依存: `if (this.searchAbortController)` → `this.searchAbortController.abort()`
- 条件付き依存: `if (this.query)` → `gotoPref()`
- 条件付き依存: `if (this.query)` → `history.replaceState()`
- 条件付き依存: `if (this.query)` → `document.querySelectorAll()`
- 条件付き依存: `if (subQuery)` → `rootPreferencesChildren.filter()`
- 条件付き依存: `if (child.hidden)` → `child.classList.add()`
- 条件付き依存: `if (child.localName === "setting-pane")` → `child.querySelectorAll()`
- 条件付き依存: `if (child.localName === "setting-pane")` → `group.hasAttribute()`
- 条件付き依存: `if (group.hidden || group.hasAttribute("data-hidden-from-search"))` → `group.classList.add()`
- 条件付き依存: `if (this.query)` → `performance.now()`
- 条件付き依存: `if (performance.now() - ts > FRAME_THRESHOLD)` → `this.createSearchTooltip()`
- 条件付き依存: `if (performance.now() - ts > FRAME_THRESHOLD)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (child.localName === "setting-pane")` → `this.searchWithinNode()`
- 条件付き依存: `if (matched)` → `group.classList.remove()`
- 条件付き依存: `if (!(matched))` → `group.classList.add()`
- 条件付き依存: `if (!paneMatched)` → `child.querySelectorAll()`
- 条件付き依存: `if (additionalSearchTargets.length)` → `( await Promise.all( [...additionalSearchTargets].map(target => this.searchWithinNode(target, this.query) ) ) ).some()`
- 条件付き依存: `if (additionalSearchTargets.length)` → `Promise.all()`
- 条件付き依存: `if (additionalSearchTargets.length)` → `[...additionalSearchTargets].map()`
- 条件付き依存: `if (additionalSearchTargets.length)` → `this.searchWithinNode()`
- 条件付き依存: `if (paneMatched)` → `child.querySelectorAll()`
- 条件付き依存: `if (paneMatched)` → `group.classList.remove()`
- 条件付き依存: `if (paneMatched)` → `child.classList.remove()`
- 条件付き依存: `if (!(paneMatched))` → `child.classList.add()`
- 条件付き依存: `if (this.query)` → `child.classList.contains()`
- 条件付き依存: `if ( child.classList.contains("header") || (child.classList.contains("subcategory") && child.localName !== "setting-group") )` → `child.classList.add()`
- 条件付き依存: `if (this.query)` → `this.searchWithinNode()`
- 条件付き依存: `if (childMatched)` → `child.classList.remove()`
- 条件付き依存: `if (childMatched)` → `child.closest()`
- 条件付き依存: `if (childMatched)` → `groupbox.querySelector()`
- 条件付き依存: `if (!(childMatched))` → `child.classList.add()`
- 条件付き依存: `if (this.subItems.size)` → `subItem.classList.toggle()`
- 条件付き依存: `if (this.query)` → `noResultsEl.setAttribute()`
- 条件付き依存: `if (this.query)` → `document.getElementById()`
- 条件付き依存: `if (resultsFound)` → `this.createSearchTooltip()`
- 条件付き依存: `if (resultsFound)` → `requestAnimationFrame()`
- 条件付き依存: `if (resultsFound)` → `this._recomputeTooltipPositions()`
- 条件付き依存: `if (!(this.query))` → `document.getElementById()`
- 条件付き依存: `if (window.navigation?.canGoBack ?? true)` → `document.addEventListener()`
- 条件付き依存: `if (window.navigation?.canGoBack ?? true)` → `window.history.back()`
- 条件付き依存: `if (!(window.navigation?.canGoBack ?? true))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(window.navigation?.canGoBack ?? true))` → `gotoPref()`
- 条件付き依存: `if (!(this.query))` → `document.querySelectorAll()`
- 参照: `additionalSearchTargets.length`, `child.hidden`, `child.localName`, `child.onSearchPane`, `document.getElementById("sorry-message-query").textContent`, `document.title`, `el.hidden`, `element.hidden`, `group.hidden`, `groupHeader.hidden`, `history.state`, `msgQueryElem.textContent`, `noResultsEl.hidden`, `query.length`, `signal.aborted`, `srHeader.hidden`, `this.listSearchTooltips`, `this.query`, `this.searchAbortController`, `this.searchAbortController.signal`, `this.searchCompleted`, `this.subItems`, `this.subItems.size`, `window.navigation?.canGoBack`
- XPCOM: `Services.prefs`

## _isAnchor()
- 位置: L570-572
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `el.localName`, `el.prefix`

## searchWithinNode()
- 位置: async L587-751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.every.call()`, `Element.isInstance()`, `nodeObject.localName?.startsWith()`, `this.searchableNodes.has()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `this.textNodeDescendants()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `this.highlightMatches()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `node.textContent.toLowerCase()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `nodeObject.localName.startsWith()`
- 条件付き依存: `if ( nodeObject.localName == "label" || nodeObject.localName == "description" || nodeObject.localName.startsWith("moz-") )` → `accessKeyTextNodes.push()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `nodeSizes.push()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `allNodeText.toLowerCase()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `this.queryMatchesContent()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `nodeObject.getAttribute()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `nodeObject.hasAttribute()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `this.matchesSearchL10nIDs()`
- 条件付き依存: `if (!keywordsResult && nodeObject.getAttribute("data-load-pane"))` → `document.querySelector()`
- 条件付き依存: `if (!keywordsResult && nodeObject.getAttribute("data-load-pane"))` → `nodeObject.getAttribute()`
- 条件付き依存: `if (subPane)` → `subPane.querySelectorAll()`
- 条件付き依存: `if (subPane)` → `this.searchWithinNode()`
- 条件付き依存: `if (!keywordsResult)` → `nodeObject.hasAttribute()`
- 条件付き依存: `if (!keywordsResult)` → `this.queryMatchesContent()`
- 条件付き依存: `if (!keywordsResult)` → `nodeObject.getAttribute()`
- 条件付き依存: `if ( Element.isInstance(nodeObject) && (nodeObject.childElementCount == 0 || (typeof nodeObject.children !== "undefined" && Array.prototype.every.call(nodeObject...)` → `HTMLElement.isInstance()`
- 条件付き依存: `if ( keywordsResult && (HTMLElement.isInstance(nodeObject) || nodeObject.localName === "button" || nodeObject.localName == "menulist") )` → `this.listSearchTooltips.add()`
- 条件付き依存: `if (keywordsResult && nodeObject.localName === "menuitem")` → `nodeObject.setAttribute()`
- 条件付き依存: `if (keywordsResult && nodeObject.localName === "menuitem")` → `this.listSearchMenuitemIndicators.add()`
- 条件付き依存: `if (keywordsResult && nodeObject.localName === "menuitem")` → `nodeObject.closest()`
- 条件付き依存: `if (keywordsResult && nodeObject.localName === "menuitem")` → `menulist.setAttribute()`
- 条件付き依存: `if ( (nodeObject.localName == "menulist" || nodeObject.localName == "menuitem") && (labelResult || valueResult || keywordsResult) )` → `nodeObject.setAttribute()`
- 条件付き依存: `if (index != -1)` → `this.searchChildNodeIfVisible()`
- 条件付き依存: `if (!(nodeObject.localName == "deck" && nodeObject.id != "historyPane"))` → `this.searchChildNodeIfVisible()`
- 参照: `node.length`, `node.textContent`, `node.textContent.length`, `nodeObject.childElementCount`, `nodeObject.childNodes.length`, `nodeObject.children`, `nodeObject.id`, `nodeObject.localName`, `nodeObject.selectedIndex`, `this._isAnchor`

## searchChildNodeIfVisible()
- 位置: async L764-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nodeObject.getAttribute()`
- 条件付き依存: `if ( !child.hidden && nodeObject.getAttribute("data-hidden-from-search") !== "true" )` → `this.searchWithinNode()`
- 条件付き依存: `if ( result && (nodeObject.localName === "menulist" || nodeObject.localName === "moz-select") )` → `this.listSearchTooltips.add()`
- 条件付き依存: `if ( !child.hidden && nodeObject.getAttribute("data-hidden-from-search") !== "true" )` → `Element.isInstance()`
- 条件付き依存: `if ( !child.hidden && nodeObject.getAttribute("data-hidden-from-search") !== "true" )` → `child.classList.contains()`
- 条件付き依存: `if ( Element.isInstance(child) && (child.classList.contains("featureGate") || child.classList.contains("mozilla-product-item")) )` → `this.subItems.set()`
- 参照: `child.hidden`, `nodeObject.childNodes`, `nodeObject.localName`

## matchesSearchL10nIDs()
- 位置: async L804-864
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.queryMatchesContent()`, `this.searchKeywords.get()`, `this.searchKeywords.has()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `nodeObject .getAttribute("search-l10n-ids") .split(",") .map(s => s.trim().split(".")) .filter()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `nodeObject .getAttribute("search-l10n-ids") .split(",") .map()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `nodeObject .getAttribute("search-l10n-ids") .split()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `nodeObject .getAttribute()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `s.trim().split()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `s.trim()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `document.l10n.formatMessages()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `refs.map()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `messages .map()`
- 条件付き依存: `if (!msg)` → `console.error()`
- 条件付き依存: `if (refAttr)` → `msg.attributes.find()`
- 条件付き依存: `if (!attr)` → `console.error()`
- 条件付き依存: `if (attr.value === "")` → `console.error()`
- 条件付き依存: `if (msg.value === "")` → `console.error()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `this.searchKeywords.set()`
- 条件付き依存: `if (!this.searchKeywords.has(nodeObject))` → `this.queryMatchesContent()`
- 参照: `a.name`, `attr.value`, `msg.attributes`, `msg.value`, `s[0].length`

## createSearchTooltip()
- 位置: L875-894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchorNode.ownerDocument.createElement()`, `anchorNode.parentElement.classList.add()`, `searchTooltip.appendChild()`, `this._applyTooltipPosition()`, `this._computeTooltipPosition()`, `this.searchTooltipContainer.append()`
- 参照: `anchorNode.tooltipNode`, `searchTooltip.className`, `searchTooltipText.textContent`

## _recomputeTooltipPositions()
- 位置: L896-909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `positions.push()`, `this._applyTooltipPosition()`, `this._computeTooltipPosition()`
- 参照: `anchorNode.tooltipNode`, `this.listSearchTooltips`

## _applyTooltipPosition()
- 位置: L911-914
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `position.left`, `position.top`, `searchTooltip.style.left`, `searchTooltip.style.top`

## _computeTooltipPosition()
- 位置: L916-948
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `positioningNode.getBoundingClientRect()`, `searchTooltip.getBoundingClientRect()`, `this.searchTooltipContainer.getBoundingClientRect()`
- 条件付き依存: `if (anchorNode.localName == "moz-select")` → `anchorNode.shadowRoot?.querySelector()`
- 参照: `anchorNode.localName`, `anchorRect.left`, `anchorRect.top`, `anchorRect.width`, `tooltipContainerRect.left`, `tooltipContainerRect.top`, `tooltipRect.width`

## removeAllSearchIndicators()
- 位置: L954-969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeAllSearchMenuitemIndicators()`, `this.removeAllSearchTooltips()`
- 条件付き依存: `if (this.searchResultsHighlighted)` → `this.getFindSelection(window).removeAllRanges()`
- 条件付き依存: `if (this.searchResultsHighlighted)` → `this.getFindSelection()`
- 条件付き依存: `if (showSubItems && this.subItems.size)` → `this.subItems.keys()`
- 条件付き依存: `if (showSubItems && this.subItems.size)` → `subItem.classList.remove()`
- 条件付き依存: `if (showSubItems && this.subItems.size)` → `this.subItems.clear()`
- 参照: `this.searchResultsHighlighted`, `this.subItems.size`

## removeAllSearchTooltips()
- 位置: L974-983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchorNode.parentElement.classList.remove()`, `this.listSearchTooltips.clear()`
- 条件付き依存: `if (anchorNode.tooltipNode)` → `anchorNode.tooltipNode.remove()`
- 参照: `anchorNode.tooltipNode`, `this.listSearchTooltips`

## removeAllSearchMenuitemIndicators()
- 位置: L988-993
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.removeAttribute()`, `this.listSearchMenuitemIndicators.clear()`
- 参照: `this.listSearchMenuitemIndicators`
