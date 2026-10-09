# browser/components/extensions/parent/ext-menus.js

source: browser/components/extensions/parent/ext-menus.js
source-hash: 4b16b259632854896794702c8a59dff929466522
lines: 1489

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## build()
- 位置: L55-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.afterBuildingMenu()`, `this.createAndInsertTopLevelElements()`, `this.maybeOverrideContextData()`, `xulMenu.addEventListener()`
- 条件付き依存: `if ( contextData.webExtContextData && !contextData.webExtContextData.showDefaults )` → `Promise.resolve().then()`
- 条件付き依存: `if ( contextData.webExtContextData && !contextData.webExtContextData.showDefaults )` → `Promise.resolve()`
- 条件付き依存: `if ( contextData.webExtContextData && !contextData.webExtContextData.showDefaults )` → `this.hideDefaultMenuItems()`
- 参照: `contextData.menu`, `contextData.webExtContextData`, `contextData.webExtContextData.showDefaults`, `this.xulMenu`

## maybeOverrideContextData()
- 位置: L75-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getContextViewType()`
- 条件付き依存: `if (webExtContextData.overrideContext === "tab")` → `tabTracker.getTab()`
- 参照: `contextData.frameUrl`, `contextData.inFrame`, `contextData.menu`, `contextData.pageUrl`, `tab.linkedBrowser.currentURI.spec`, `webExtContextData.bookmarkId`, `webExtContextData.overrideContext`, `webExtContextData.tabId`

## canAccessContext()
- 位置: L111-126
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!extension.privateBrowsingAllowed)` → `PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (!( nativeTab && PrivateBrowsingUtils.isBrowserPrivate(nativeTab.linkedBrowser) ))` → `PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `contextData.menu.documentGlobal`, `contextData.tab`, `extension.privateBrowsingAllowed`, `nativeTab.linkedBrowser`

## createAndInsertTopLevelElements()
- 位置: L128-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.canAccessContext()`, `this.itemsToCleanUp.add()`
- 条件付き依存: `if ( contextData.onAction || contextData.onBrowserAction || contextData.onPageAction )` → `this.buildTopLevelElements()`
- 条件付き依存: `if ( contextData.onAction || contextData.onBrowserAction || contextData.onPageAction )` → `this.itemsToCleanUp.has()`
- 条件付き依存: `if (rootElements.length && !this.itemsToCleanUp.has(nextSibling))` → `rootElements.push()`
- 条件付き依存: `if (rootElements.length && !this.itemsToCleanUp.has(nextSibling))` → `this.xulMenu.ownerDocument.createXULElement()`
- 条件付き依存: `if (extensionId === root.extension.id)` → `this.buildTopLevelElements()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `this.xulMenu.querySelector()`
- 条件付き依存: `if (extensionId === root.extension.id)` → `this.itemsToCleanUp.has()`
- 条件付き依存: `if ( rootElements.length && showDefaults && !this.itemsToCleanUp.has(nextSibling) )` → `rootElements.push()`
- 条件付き依存: `if ( rootElements.length && showDefaults && !this.itemsToCleanUp.has(nextSibling) )` → `this.xulMenu.ownerDocument.createXULElement()`
- 条件付き依存: `if (!rootElements)` → `this.buildTopLevelElements()`
- 条件付き依存: `if (!rootElements)` → `this.itemsToCleanUp.has()`
- 条件付き依存: `if ( rootElements.length && !this.itemsToCleanUp.has(this.xulMenu.lastElementChild) )` → `rootElements.unshift()`
- 条件付き依存: `if ( rootElements.length && !this.itemsToCleanUp.has(this.xulMenu.lastElementChild) )` → `this.xulMenu.ownerDocument.createXULElement()`
- 条件付き依存: `if (nextSibling)` → `nextSibling.before()`
- 条件付き依存: `if (!(nextSibling))` → `this.xulMenu.append()`
- 参照: `AppConstants.platform`, `contextData.extension.id`, `contextData.onAction`, `contextData.onBrowserAction`, `contextData.onPageAction`, `contextData.webExtContextData`, `root.extension`, `root.extension.id`, `rootElements.length`, `this.xulMenu.firstElementChild`, `this.xulMenu.lastElementChild`

## buildElementWithChildren()
- 位置: L221-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buildChildren()`, `this.buildSingleElement()`
- 条件付き依存: `if (children.length)` → `element.firstElementChild.append()`
- 参照: `children.length`

## buildChildren()
- 位置: L230-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.enabledForContext()`
- 条件付き依存: `if (child.enabledForContext(contextData))` → `children.push()`
- 条件付き依存: `if (child.enabledForContext(contextData))` → `this.buildElementWithChildren()`
- 参照: `child.groupName`, `child.type`, `item.children`

## buildTopLevelElements()
- 位置: L250-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `children[0].getAttribute()`, `this.buildChildren()`
- 条件付き依存: `if (children.length > maxCount)` → `this.buildSingleElement()`
- 条件付き依存: `if (children.length > maxCount)` → `rootElement.setAttribute()`
- 条件付き依存: `if (children.length > maxCount)` → `rootElement.firstElementChild.append()`
- 条件付き依存: `if (children.length > maxCount)` → `children.splice()`
- 条件付き依存: `if (children.length > maxCount)` → `children.push()`
- 条件付き依存: `if (forceManifestIcons)` → `rootElement.getAttribute()`
- 条件付き依存: `if ( root.extension.manifest.icons && rootElement.getAttribute("type") !== "checkbox" )` → `this.setMenuItemIcon()`
- 条件付き依存: `if (!( root.extension.manifest.icons && rootElement.getAttribute("type") !== "checkbox" ))` → `this.removeMenuItemIcon()`
- 参照: `AppConstants.platform`, `children.length`, `root.extension`, `root.extension.manifest.icons`

## buildSingleElement()
- 位置: L295-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.customizeElement()`
- 条件付き依存: `if (item.children.length)` → `this.createMenuElement()`
- 条件付き依存: `if (item.type == "separator")` → `doc.createXULElement()`
- 条件付き依存: `if (!(item.type == "separator"))` → `doc.createXULElement()`
- 参照: `contextData.menu.ownerDocument`, `item.children.length`, `item.type`

## createMenuElement()
- 位置: L309-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `element.appendChild()`

## customizeElement()
- 位置: L317-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickModifiersFromEvent()`, `element.addEventListener()`, `element.classList.add()`, `element.setAttribute()`, `item.extension.emit()`, `item.getClickInfo()`
- 条件付き依存: `if (label)` → `label.replace()`
- 条件付き依存: `if (accessKey === undefined)` → `label.charAt()`
- 条件付き依存: `if (label)` → `label.indexOf()`
- 条件付き依存: `if (contextData.isTextSelected && label.indexOf("%s") > -1)` → `contextData.selectionText.trim()`
- 条件付き依存: `if (contextData.isTextSelected && label.indexOf("%s") > -1)` → `Array.from()`
- 条件付き依存: `if (codePointsToRemove)` → `selectionArray.slice(0, -codePointsToRemove).join()`
- 条件付き依存: `if (codePointsToRemove)` → `selectionArray.slice()`
- 条件付き依存: `if (contextData.isTextSelected && label.indexOf("%s") > -1)` → `label.replace()`
- 条件付き依存: `if (label)` → `element.setAttribute()`
- 条件付き依存: `if (accessKey)` → `element.setAttribute()`
- 条件付き依存: `if (accessKey)` → `element.toggleAttribute()`
- 条件付き依存: `if (!(accessKey))` → `element.toggleAttribute()`
- 条件付き依存: `if (item.icons)` → `this.setMenuItemIcon()`
- 条件付き依存: `if (!(item.icons))` → `this.removeMenuItemIcon()`
- 条件付き依存: `if (item.type == "checkbox")` → `element.setAttribute()`
- 条件付き依存: `if (item.checked)` → `element.setAttribute()`
- 条件付き依存: `if (item.type == "radio")` → `element.setAttribute()`
- 条件付き依存: `if (!item.enabled)` → `element.setAttribute()`
- 条件付き依存: `if ( contextData.tab && // If the menu context was overridden by the extension, do not grant // activeTab since the extension also controls the tabId. (!webExtCo...)` → `item.tabManager.addActiveTabPermission()`
- 条件付き依存: `if (actionFor)` → `actionFor(item.extension).triggerAction()`
- 条件付き依存: `if (actionFor)` → `actionFor()`
- 条件付き依存: `if (item.parent)` → `gShownMenuItems.get(item.extension).push()`
- 条件付き依存: `if (item.parent)` → `gShownMenuItems.get()`
- 参照: `Services.locale.ellipsis`, `child.checked`, `child.groupName`, `child.type`, `contextData.isTextSelected`, `contextData.tab`, `event.button`, `event.currentTarget`, `event.target`, `event.target.documentGlobal`, `global.browserActionFor`, `global.pageActionFor`, `global.sidebarActionFor`, `info.button`, `info.modifiers`, `item.checked`, `item.command`, `item.elementId`, `item.enabled`, `item.extension`, `item.extension.id`, `item.extension.manifestVersion`, `item.groupName`, `item.icons`, `item.id`, `item.parent`, `item.parent.children`, `item.title`, `item.type`, `label.length`, `selectionArray.length`, `webExtContextData.extensionId`
- XPCOM: `Services.locale`

## setMenuItemIcon()
- 位置: L469-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.encodeURIForSrcset()`, `IconDetails.getPreferredIcon()`, `element.setAttribute()`, `extension.baseURI.resolve()`
- 条件付き依存: `if (element.localName == "menu")` → `element.classList.add()`
- 条件付き依存: `if (element.localName == "menuitem")` → `element.classList.add()`
- 参照: `contextData.menu.documentGlobal`, `element.localName`, `parentWindow.devicePixelRatio`

## removeMenuItemIcon()
- 位置: L493-496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.classList.remove()`, `element.removeAttribute()`

## rebuildMenu()
- 位置: L498-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `assignAutoAccessKeys()`, `gRootItems.get()`, `item.id.startsWith()`, `makeWidgetId()`, `this.xulMenu.showHideSeparators()`
- 条件付き依存: `if (item.id && item.id.startsWith(elementIdPrefix))` → `item.remove()`
- 条件付き依存: `if (item.id && item.id.startsWith(elementIdPrefix))` → `this.itemsToCleanUp.delete()`
- 条件付き依存: `if (root)` → `this.createAndInsertTopLevelElements()`
- 参照: `extension.id`, `item.id`, `item.nextSibling`, `this.itemsToCleanUp`, `this.xulMenu`

## afterBuildingMenu()
- 位置: L527-554
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( contextData.onAction || contextData.onBrowserAction || contextData.onPageAction )` → `dispatchOnShownEvent()`
- 条件付き依存: `if (!( contextData.onAction || contextData.onBrowserAction || contextData.onPageAction ))` → `gOnShownSubscribers.keys()`
- 条件付き依存: `if (!( contextData.onAction || contextData.onBrowserAction || contextData.onPageAction ))` → `dispatchOnShownEvent()`
- 参照: `contextData.extension`, `contextData.onAction`, `contextData.onBrowserAction`, `contextData.onPageAction`, `this.contextData`

## dispatchOnShownEvent()
- 位置: L528-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.emit()`, `gShownMenuItems.get()`, `this.canAccessContext()`

## hideDefaultMenuItems()
- 位置: L556-566
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.itemsToCleanUp.has()`
- 条件付き依存: `if (this.xulMenu.showHideSeparators)` → `this.xulMenu.showHideSeparators()`
- 参照: `item.hidden`, `this.xulMenu.children`, `this.xulMenu.showHideSeparators`

## handleEvent()
- 位置: L568-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.emit()`, `gShownMenuItems.clear()`, `gShownMenuItems.keys()`, `item.remove()`, `target.removeEventListener()`, `this.itemsToCleanUp.clear()`
- 参照: `event.target`, `event.type`, `this.contextData`, `this.itemsToCleanUp`, `this.xulMenu`

## global.actionContextMenu()
- 位置: L592-596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMenuBuilder.build()`
- 参照: `contextData.pageUrl`, `contextData.tab`, `contextData.tab.linkedBrowser.currentURI.spec`, `tabTracker.activeTab`

## getMenuContexts()
- 位置: L616-639
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 条件付き依存: `if (contextData[key])` → `contexts.add()`
- 条件付き依存: `if (contexts.size === 0)` → `contexts.add()`
- 条件付き依存: `if ( !contextData.onBookmark && !contextData.onTab && !contextData.inToolsMenu )` → `contexts.add()`
- 参照: `contextData.inToolsMenu`, `contextData.onBookmark`, `contextData.onTab`, `contexts.size`

## getContextViewType()
- 位置: L641-655
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `contextData.menu.id`, `contextData.originalViewType`, `contextData.tab`, `contextData.webExtBrowserType`

## addMenuEventInfo()
- 位置: L657-703
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getContextViewType()`
- 条件付き依存: `if (includeSensitiveData)` → `extension.hasPermission()`
- 条件付き依存: `if (contextData.timeStamp && extension.hasPermission("menus"))` → `Math.floor()`
- 参照: `contextData.bookmarkId`, `contextData.frameId`, `contextData.frameUrl`, `contextData.inFrame`, `contextData.isTextSelected`, `contextData.linkText`, `contextData.linkUrl`, `contextData.onAudio`, `contextData.onBookmark`, `contextData.onEditable`, `contextData.onImage`, `contextData.onLink`, `contextData.onVideo`, `contextData.originalViewUrl`, `contextData.pageUrl`, `contextData.selectionText`, `contextData.srcUrl`, `contextData.timeStamp`, `info.bookmarkId`, `info.editable`, `info.frameId`, `info.frameUrl`, `info.linkText`, `info.linkUrl`, `info.mediaType`, `info.pageUrl`, `info.selectionText`, `info.srcUrl`, `info.targetElementId`, `info.viewType`

## MenuItem.constructor()
- 位置: L706-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasOwnProperty()`, `this.setDefaults()`, `this.setProps()`
- 条件付き依存: `if (!isRoot && !this.parent)` → `this.root.addChild()`
- 参照: `extension.tabManager`, `this.children`, `this.extension`, `this.id`, `this.parent`, `this.tabManager`

## MenuItem.setProps()
- 位置: L725-750
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionMenus.mergeMenuProperties()`
- 条件付き依存: `if (createProperties.documentUrlPatterns != null)` → `parseMatchPatterns()`
- 条件付き依存: `if (createProperties.targetUrlPatterns != null)` → `parseMatchPatterns()`
- 参照: `createProperties.contexts`, `createProperties.documentUrlPatterns`, `createProperties.parentId`, `createProperties.targetUrlPatterns`, `this.contexts`, `this.documentUrlMatchPattern`, `this.documentUrlPatterns`, `this.extension.restrictSchemes`, `this.parent.contexts`, `this.targetUrlMatchPattern`, `this.targetUrlPatterns`

## MenuItem.setDefaults()
- 位置: L752-760
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setProps()`

## MenuItem.id()
- 位置: L762-771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMenuMap.get()`, `gMenuMap.get(this.extension).has()`, `this.hasOwnProperty()`
- 参照: `this._id`, `this.extension`

## MenuItem.id()
- 位置: L773-775
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._id`

## MenuItem.elementId()
- 位置: L777-787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeWidgetId()`
- 参照: `this.extension.id`, `this.id`

## MenuItem.ensureValidParentId()
- 位置: L789-804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMenuMap.get()`, `menuMap.get()`, `menuMap.has()`
- 参照: `item.parent`, `this.extension`

## MenuItem.parentId()
- 位置: L806-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureValidParentId()`
- 条件付き依存: `if (this.parent)` → `this.parent.detachChild()`
- 条件付き依存: `if (parentId === undefined)` → `this.root.addChild()`
- 条件付き依存: `if (!(parentId === undefined))` → `gMenuMap.get()`
- 条件付き依存: `if (!(parentId === undefined))` → `menuMap.get(parentId).addChild()`
- 条件付き依存: `if (!(parentId === undefined))` → `menuMap.get()`
- 参照: `this.extension`, `this.parent`

## MenuItem.parentId()
- 位置: L821-823
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.parent`, `this.parent.id`

## MenuItem.addChild()
- 位置: L825-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.children.push()`
- 参照: `child.parent`

## MenuItem.detachChild()
- 位置: L833-840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.children.indexOf()`, `this.children.splice()`
- 参照: `child.parent`

## MenuItem.root()
- 位置: L842-854
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gRootItems.get()`, `gRootItems.has()`
- 条件付き依存: `if (!gRootItems.has(extension))` → `gRootItems.set()`
- 参照: `extension.name`, `this.extension`

## MenuItem.descendantIds()
- 位置: L856-860
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.children.flatMap()`
- 参照: `m.descendantIds`, `m.id`, `this.children`

## MenuItem.remove()
- 位置: L862-876
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.remove()`, `gMenuMap.get()`, `menuMap.delete()`, `this.children.slice()`
- 条件付き依存: `if (this.parent)` → `this.parent.detachChild()`
- 条件付き依存: `if (this.root == this)` → `gRootItems.delete()`
- 参照: `this.extension`, `this.id`, `this.parent`, `this.root`

## MenuItem.getClickInfo()
- 位置: L878-894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addMenuEventInfo()`
- 参照: `info.checked`, `info.parentMenuItemId`, `info.wasChecked`, `this.checked`, `this.extension`, `this.id`, `this.parent`, `this.parentId`, `this.type`

## MenuItem.enabledForContext()
- 位置: L896-956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `contexts.has()`, `docPattern.matches()`, `getContextViewType()`, `getMenuContexts()`, `this.contexts.some()`, `this.viewTypes.includes()`
- 条件付き依存: `if (docPattern && this.viewTypes && contextData.originalViewUrl)` → `docPattern.matches()`
- 条件付き依存: `if (docPattern && this.viewTypes && contextData.originalViewUrl)` → `Services.io.newURI()`
- 条件付き依存: `if (contextData.onBookmark)` → `this.extension.hasPermission()`
- 条件付き依存: `if (contextData.onImage || contextData.onAudio || contextData.onVideo)` → `targetURIs.push()`
- 条件付き依存: `if (contextData.onImage || contextData.onAudio || contextData.onVideo)` → `Services.io.newURI()`
- 条件付き依存: `if (contextData.onLink && contextData.linkURI)` → `targetURIs.push()`
- 条件付き依存: `if (targetPattern)` → `targetURIs.some()`
- 条件付き依存: `if (targetPattern)` → `targetPattern.matches()`
- 参照: `contextData.inFrame`, `contextData.linkURI`, `contextData.onAudio`, `contextData.onBookmark`, `contextData.onImage`, `contextData.onLink`, `contextData.onVideo`, `contextData.originalViewUrl`, `contextData.srcUrl`, `this.documentUrlMatchPattern`, `this.targetUrlMatchPattern`, `this.viewTypes`, `this.visible`
- XPCOM: `Services.io`

## isLibraryWindow()
- 位置: L964-967
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.document.documentElement.getAttribute()`
- 参照: `this.libraryWindowType`

## init()
- 位置: L969-984
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `Services.ww.registerNotification()`, `windowTracker.isBrowserWindowInitialized()`
- 条件付き依存: `if (windowTracker.isBrowserWindowInitialized(window))` → `this.isLibraryWindow()`
- 条件付き依存: `if (this.isLibraryWindow(window))` → `this.notify()`
- 条件付き依存: `if (!(windowTracker.isBrowserWindowInitialized(window)))` → `window.addEventListener()`
- 参照: `this._listener`
- XPCOM: `Services.wm` / `Services.ww`

## uninit()
- 位置: L987-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.reportError()`, `Services.wm.getEnumerator()`, `Services.ww.unregisterNotification()`, `this.isLibraryWindow()`, `window.removeEventListener()`
- 条件付き依存: `if (this.isLibraryWindow(window))` → `cleanupWindow()`
- XPCOM: `Services.wm` / `Services.ww`

## observe()
- 位置: L1004-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "domwindowopened")` → `window.addEventListener()`

## handleEvent()
- 位置: L1011-1016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isLibraryWindow()`
- 条件付き依存: `if (this.isLibraryWindow(window))` → `this.notify()`
- 参照: `event.target.defaultView`

## notify()
- 位置: L1018-1024
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.reportError()`, `this._listener.call()`

## register()
- 位置: L1037-1044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `libraryTracker.init()`, `this.onWindowOpen()`, `windowTracker.addOpenListener()`, `windowTracker.browserWindows()`
- 参照: `this.onLibraryOpen`, `this.onWindowOpen`
- XPCOM: `Services.obs`

## unregister()
- 位置: L1046-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `libraryTracker.uninit()`, `this.cleanupWindow()`, `windowTracker.browserWindows()`, `windowTracker.removeOpenListener()`
- 参照: `this.cleanupLibrary`, `this.onWindowOpen`
- XPCOM: `Services.obs`

## observe()
- 位置: L1055-1058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMenuBuilder.build()`
- 参照: `subject.wrappedJSObject`

## onWindowOpen()
- 位置: async L1060-1079
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.addEventListener()`, `sidebarHeader.addEventListener()`, `window.document.getElementById()`
- 条件付き依存: `if ( !window.closed && window.SidebarController.currentID === "viewBookmarksSidebar" )` → `menuTracker.onSidebarShown()`
- 参照: `menuTracker.menuIds`, `menuTracker.onSidebarShown`, `window.SidebarController.currentID`, `window.SidebarController.promiseInitialized`, `window.closed`

## cleanupWindow()
- 位置: L1081-1105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.removeEventListener()`, `sidebarHeader.removeEventListener()`, `window.document.getElementById()`
- 条件付き依存: `if (window.SidebarController.currentID === "viewBookmarksSidebar")` → `sidebarBrowser.removeEventListener()`
- 条件付き依存: `if (window.SidebarController.currentID === "viewBookmarksSidebar")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("sidebar.updatedBookmarks.enabled", false) )` → `sidebarBrowser.contentDocument.getElementById()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("sidebar.updatedBookmarks.enabled", false) )` → `menu.removeEventListener()`
- 参照: `this.menuIds`, `this.onBookmarksContextMenu`, `this.onSidebarShown`, `window.SidebarController.browser`, `window.SidebarController.currentID`
- XPCOM: `Services.prefs`

## onSidebarShown()
- 位置: L1107-1135
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (sidebarBrowser.contentDocument.readyState !== "complete")` → `sidebarBrowser.addEventListener()`
- 条件付き依存: `if (window.SidebarController.currentID === "viewBookmarksSidebar")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("sidebar.updatedBookmarks.enabled", false) )` → `sidebarBrowser.contentDocument.getElementById()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("sidebar.updatedBookmarks.enabled", false) )` → `menu.addEventListener()`
- 参照: `event.currentTarget.documentGlobal`, `menuTracker.onBookmarksContextMenu`, `menuTracker.onSidebarShown`, `sidebarBrowser.contentDocument.readyState`, `window.SidebarController.browser`, `window.SidebarController.currentID`
- XPCOM: `Services.prefs`

## onLibraryOpen()
- 位置: L1137-1140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.addEventListener()`, `window.document.getElementById()`
- 参照: `menuTracker.onBookmarksContextMenu`

## cleanupLibrary()
- 位置: L1142-1148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.removeEventListener()`, `window.document.getElementById()`
- 参照: `menuTracker.onBookmarksContextMenu`

## handleEvent()
- 位置: L1150-1187
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (menu.id === "placesContext")` → `gMenuBuilder.build()`
- 条件付き依存: `if (menu.id === "sidebar-bookmarks-context-menu")` → `gMenuBuilder.build()`
- 条件付き依存: `if (menu.id === "menu_ToolsPopup")` → `gMenuBuilder.build()`
- 条件付き依存: `if (menu.id === "tabContextMenu")` → `gMenuBuilder.build()`
- 参照: `event.target`, `menu.documentGlobal.TabContextMenu.contextTab`, `menu.id`, `menu.triggerNode`, `menu.triggerNode.triggerNode`, `tab.linkedBrowser.currentURI.spec`, `tabTracker.activeTab`, `trigger._placesNode.bookmarkGuid`, `trigger._placesNode?.bookmarkGuid`, `trigger.guid`, `trigger?.guid`

## onBookmarksContextMenu()
- 位置: L1189-1201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.isVirtualLeftPaneItem()`, `gMenuBuilder.build()`, `tree.getCellAt()`, `tree.view.nodeForTreeIndex()`
- 参照: `cell.row`, `event.target`, `event.x`, `event.y`, `menu.triggerNode.parentElement`

## constructor()
- 位置: L1207-1214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMenuMap.set()`, `super()`
- 条件付き依存: `if (!gMenuMap.size)` → `menuTracker.register()`
- 参照: `gMenuMap.size`

## initExtensionMenus()
- 位置: async L1216-1263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.reportError()`, `ExtensionMenus.asyncInitForExtension()`, `ExtensionMenus.getMenus()`, `ExtensionMenus.shouldPersistMenus()`, `createErrorMenuIds.push()`, `gMenuMap.get()`, `gMenuMap.get(extension).set()`, `menus.values()`, `notifyMenusCreated()`
- 条件付き依存: `if (!menus.size)` → `notifyMenusCreated()`
- 条件付き依存: `if (createErrorMenuIds.length)` → `ExtensionMenus.deleteMenus()`
- 参照: `createErrorMenuIds.length`, `createProperties.id`, `createProperties?.id`, `extension.hasShutdown`, `extension.id`, `menuItem.id`, `menus.size`

## notifyMenusCreated()
- 位置: L1229-1230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.emit()`, `gMenuMap.get()`

## onStartup()
- 位置: L1265-1267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.initExtensionMenus()`
- 参照: `this.#promiseInitialized`

## onShutdown()
- 位置: L1269-1281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMenuMap.has()`
- 条件付き依存: `if (gMenuMap.has(extension))` → `gMenuMap.delete()`
- 条件付き依存: `if (gMenuMap.has(extension))` → `gRootItems.delete()`
- 条件付き依存: `if (gMenuMap.has(extension))` → `gShownMenuItems.delete()`
- 条件付き依存: `if (gMenuMap.has(extension))` → `gOnShownSubscribers.delete()`
- 条件付き依存: `if (!gMenuMap.size)` → `menuTracker.unregister()`
- 参照: `gMenuMap.size`

## onShown()
- 位置: L1284-1325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`, `gOnShownSubscribers.get()`, `gOnShownSubscribers.get(extension).add()`

## listener()
- 位置: L1286-1309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `addMenuEventInfo()`, `extension.allowedOrigins.matches()`, `extension.tabManager.convert()`, `extension.tabManager.hasActiveTabPermission()`, `fire.sync()`, `getMenuContexts()`
- 参照: `contextData.frameUrl`, `contextData.inFrame`, `contextData.pageUrl`, `contextData.tab`

## unregister()
- 位置: L1313-1320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.off()`, `gOnShownSubscribers.get()`, `listeners.delete()`
- 条件付き依存: `if (listeners.size === 0)` → `gOnShownSubscribers.delete()`
- 参照: `listeners.size`

## convert()
- 位置: L1321-1323
- 役割: (未記入)
- 触るとき: (未記入)

## onHidden()
- 位置: L1326-1340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`

## listener()
- 位置: L1328-1330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L1333-1335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.off()`

## convert()
- 位置: L1336-1338
- 役割: (未記入)
- 触るとき: (未記入)

## onClicked()
- 位置: L1341-1374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`

## listener()
- 位置: async L1343-1362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.withPendingBrowser()`, `extension.tabManager.convert()`, `fire.sync()`
- 条件付き依存: `if (fire.wakeup)` → `fire.wakeup()`
- 条件付き依存: `if (fire.wakeup)` → `linkedBrowser.documentGlobal.gBrowser.getTabForBrowser()`
- 条件付き依存: `if ( !linkedBrowser.documentGlobal.gBrowser.getTabForBrowser( linkedBrowser ) )` → `Cu.reportError()`
- 参照: `fire.wakeup`, `tabTracker.activeTab`

## unregister()
- 位置: L1366-1368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.off()`

## convert()
- 位置: L1369-1372
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L1377-1487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module: "menusInternal", event: "onShown", name: "menus.onShown", extensionApi: this, }).api()`

## refresh()
- 位置: L1381-1383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMenuBuilder.rebuildMenu()`

## create()
- 位置: async L1405-1432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionMenus.addMenu()`, `ExtensionMenus.shouldPersistMenus()`, `gMenuMap.get()`, `gMenuMap.get(extension).set()`
- 条件付き依存: `if (ExtensionMenus.shouldPersistMenus(extension))` → `gMenuMap.get(extension).has()`
- 条件付き依存: `if (ExtensionMenus.shouldPersistMenus(extension))` → `gMenuMap.get()`
- 参照: `createProperties.id`, `extension.hasShutdown`, `menuItem.id`, `this.#promiseInitialized`

## update()
- 位置: async L1434-1447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionMenus.updateMenu()`, `gMenuMap.get()`, `gMenuMap.get(extension).get()`, `menuItem.setProps()`
- 参照: `extension.hasShutdown`, `this.#promiseInitialized`

## remove()
- 位置: async L1449-1463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionMenus.deleteMenus()`, `gMenuMap.get()`, `gMenuMap.get(extension).get()`, `menuItem.remove()`
- 参照: `extension.hasShutdown`, `menuItem.descendantIds`, `menuItem.id`, `this.#promiseInitialized`

## removeAll()
- 位置: async L1465-1476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionMenus.deleteAllMenus()`, `gRootItems.get()`
- 条件付き依存: `if (root)` → `root.remove()`
- 参照: `extension.hasShutdown`, `this.#promiseInitialized`
