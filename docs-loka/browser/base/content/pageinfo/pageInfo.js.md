# browser/base/content/pageinfo/pageInfo.js

source: browser/base/content/pageinfo/pageInfo.js
source-hash: 1ba2ac6861b409a4afb898220d67a0a40d220484
lines: 1330

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/netwerk/cache-storage-service;1" ].getService()`, `ChromeUtils.defineESModuleGetters()`, `getClipboardHelper()`, `window.addEventListener()`

## pageInfoTreeView()
- 位置: L17-28
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.copycol`, `this.data`, `this.rows`, `this.selection`, `this.sortcol`, `this.sortdir`, `this.tree`, `this.treeid`

## rowCount()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)

## rowCount()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.rows`

## setTree()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.tree`

## getCellText()
- 位置: L42-48
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `column.index`, `this.data`

## setCellValue()
- 位置: L50-50
- 役割: (未記入)
- 触るとき: (未記入)

## setCellText()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `column.index`, `this.data`

## addRow()
- 位置: L56-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.data.push()`, `this.rowCountChanged()`
- 条件付き依存: `if (this.selection.count == 0 && this.rowCount && !gImageElement)` → `this.selection.select()`
- 参照: `this.rowCount`, `this.rows`, `this.selection.count`

## addRows()
- 位置: L64-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addRow()`

## rowCountChanged()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tree.rowCountChanged()`

## invalidate()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tree.invalidate()`

## clear()
- 位置: L78-84
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.tree)` → `this.tree.rowCountChanged()`
- 参照: `this.data`, `this.rows`, `this.tree`

## onPageMediaSort()
- 位置: L86-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `col.element.removeAttribute()`, `document.getElementById()`, `gTreeUtils.sort()`, `tree.columns.getNamedColumn()`, `treecol.element.setAttribute()`
- 参照: `this.data`, `this.sortcol`, `this.sortdir`, `this.treeid`, `tree.columns`, `treecol.index`

## textComparator()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(a || "").toLowerCase()`, `(a || "").toLowerCase().localeCompare()`, `(b || "").toLowerCase()`

## getRowProperties()
- 位置: L115-117
- 役割: (未記入)
- 触るとき: (未記入)

## getCellProperties()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)

## getColumnProperties()
- 位置: L121-123
- 役割: (未記入)
- 触るとき: (未記入)

## isContainer()
- 位置: L124-126
- 役割: (未記入)
- 触るとき: (未記入)

## isContainerOpen()
- 位置: L127-129
- 役割: (未記入)
- 触るとき: (未記入)

## isSeparator()
- 位置: L130-132
- 役割: (未記入)
- 触るとき: (未記入)

## isSorted()
- 位置: L133-135
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.sortcol`

## canDrop()
- 位置: L136-138
- 役割: (未記入)
- 触るとき: (未記入)

## drop()
- 位置: L139-141
- 役割: (未記入)
- 触るとき: (未記入)

## getParentIndex()
- 位置: L142-144
- 役割: (未記入)
- 触るとき: (未記入)

## hasNextSibling()
- 位置: L145-147
- 役割: (未記入)
- 触るとき: (未記入)

## getLevel()
- 位置: L148-150
- 役割: (未記入)
- 触るとき: (未記入)

## getImageSrc()
- 位置: L151-151
- 役割: (未記入)
- 触るとき: (未記入)

## getCellValue()
- 位置: L152-155
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.copycol`, `this.data`

## toggleOpenState()
- 位置: L156-156
- 役割: (未記入)
- 触るとき: (未記入)

## cycleHeader()
- 位置: L157-157
- 役割: (未記入)
- 触るとき: (未記入)

## selectionChanged()
- 位置: L158-158
- 役割: (未記入)
- 触るとき: (未記入)

## cycleCell()
- 位置: L159-159
- 役割: (未記入)
- 触るとき: (未記入)

## isEditable()
- 位置: L160-162
- 役割: (未記入)
- 触るとき: (未記入)

## gImageView.getCellProperties()
- 位置: L188-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HTMLEmbedElement.isInstance()`, `HTMLObjectElement.isInstance()`, `checkProtocol()`, `item.type.startsWith()`
- 参照: `col.element.id`, `gImageView.data`

## gImageView.onPageMediaSort()
- 位置: L207-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `col.element.removeAttribute()`, `document.getElementById()`, `gTreeUtils.sort()`, `tree.columns.getNamedColumn()`, `treecol.element.setAttribute()`
- 参照: `this.data`, `this.sortcol`, `this.sortdir`, `this.treeid`, `tree.columns`, `treecol.index`

## numComparator()
- 位置: L214-216
- 役割: (未記入)
- 触るとき: (未記入)

## textComparator()
- 位置: L223-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(a || "").toLowerCase()`, `(a || "").toLowerCase().localeCompare()`, `(b || "").toLowerCase()`

## getClipboardHelper()
- 位置: L274-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/clipboardhelper;1"].getService()`
- 参照: `Ci.nsIClipboardHelper`
- XPCOM: `nsIClipboardHelper` / `@mozilla.org/widget/clipboardhelper;1`

## onLoadPageInfo()
- 位置: async L294-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doHelpButton()`, `doSelectAllMedia()`, `document .getElementById()`, `document .getElementById("metatree") .controllers.appendController()`, `document .querySelector()`, `document .querySelector("#imagetree > treecols") .addEventListener()`, `document .querySelector("#metatree > treecols") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `document.l10n.formatValues()`, `event.target.id.slice()`, `gImageView.onPageMediaSort()`, `gMetaView.onPageMediaSort()`, `imageTree.controllers.appendController()`, `imagetree.addEventListener()`, `loadTab()`, `onBeginLinkDrag()`, `saveMedia()`, `security.clearSiteData()`, `security.viewCert()`, `security.viewPasswords()`, `security.viewQWAC()`, `showTab()`, `window.close()`, `window.dispatchEvent()`
- 参照: `MEDIA_STRINGS.audio`, `MEDIA_STRINGS.cursor`, `MEDIA_STRINGS.embed`, `MEDIA_STRINGS.img`, `MEDIA_STRINGS.input`, `MEDIA_STRINGS.link`, `MEDIA_STRINGS.object`, `MEDIA_STRINGS.video`, `event.target.id`, `imageTree.view`, `window.arguments`, `window.arguments.length`

## loadPageInfo()
- 位置: async L422-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendQuery()`, `addImage()`, `browsingContext.currentWindowGlobal.getActor()`, `contextsToVisit.pop()`, `contextsToVisit.push()`, `global.getActor()`, `onNonMediaPageInfoLoad()`, `selectImage()`, `subframeActor.sendQuery()`
- 参照: `browser.browsingContext`, `contextsToVisit.length`, `currContext.children`, `currContext.currentWindowGlobal`, `mediaResult.mediaItems`, `window.opener.gBrowser.selectedBrowser`

## createPreviewBrowserElement()
- 位置: L453-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `document.getElementById()`, `document.getElementById("mediaBrowser").replaceWith()`, `previewBrowser.setAttribute()`
- 条件付き依存: `if (userContextId)` → `previewBrowser.setAttribute()`
- 参照: `browser.browsingContext.group.id`, `browser.remoteType`, `docInfo.principal.originAttributes`

## onNonMediaPageInfoLoad()
- 位置: async L480-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `createPreviewBrowserElement()`, `document .getElementById()`, `document .getElementById("main-window") .setAttribute()`, `document.l10n.setAttributes()`, `makeGeneralTab()`, `onLoadPermission()`, `securityOnLoad()`, `uri.spec.startsWith()`
- 条件付き依存: `if ( uri.spec.startsWith("about:neterror") || uri.spec.startsWith("about:certerror") || uri.spec.startsWith("about:httpsonlyerror") )` → `Services.scriptSecurityManager.createContentPrincipal()`
- 参照: `browser.contentPrincipal.originAttributes`, `browser.currentURI`, `browsingContext.top.embedderElement`, `docInfo.documentURIObject.spec`, `docInfo.location`, `docInfo.principal`, `document.documentElement`, `pageInfoData.metaViewRows`, `windowInfo.isTopWindow`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## resetPageInfo()
- 位置: L521-535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `gImageView.clear()`, `gMetaView.clear()`, `loadTab()`
- 参照: `mediaTab.hidden`

## doHelpButton()
- 位置: L537-548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `openHelpLink()`
- 参照: `deck.selectedPanel.id`

## showTab()
- 位置: L550-554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `deck.selectedPanel`

## loadTab()
- 位置: async L556-588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `loadPageInfo()`, `radioGroup.focus()`, `radioGroup.selectedItem.doCommand()`
- 条件付き依存: `if (!diskStorage)` → `getOaWithPartitionKey()`
- 条件付き依存: `if (!diskStorage)` → `Services.loadContextInfo.custom()`
- 条件付き依存: `if (!diskStorage)` → `cacheService.diskCacheStorage()`
- 参照: `args?.browser`, `args?.browsingContext`, `args?.imageElement`, `args?.initialTab`, `radioGroup.selectedItem`
- XPCOM: `Services.loadContextInfo`

## openCacheEntry()
- 位置: L590-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `diskStorage.asyncOpenURI()`
- 参照: `nsICacheStorage.OPEN_READONLY`
- XPCOM: `Services.io`

## onCacheEntryCheck()
- 位置: L592-594
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICacheEntryOpenCallback.ENTRY_WANTED`
- XPCOM: [`nsICacheEntryOpenCallback`](../../../../netwerk/cache2/nsICacheEntryOpenCallback.idl.md)

## onCacheEntryAvailable()
- 位置: L595-597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb()`

## makeGeneralTab()
- 位置: async L607-678
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.l10n.formatValue()`, `document.l10n.setAttributes()`, `formatDate()`, `openCacheEntry()`, `setItemValue()`, `url.replace()`
- 条件付き依存: `if (docInfo.title)` → `document.getElementById()`
- 条件付き依存: `if (!(docInfo.title))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(docInfo.title))` → `document.getElementById()`
- 条件付き依存: `if (!(!length))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(!length))` → `document.getElementById()`
- 条件付き依存: `if (!(!length))` → `gMetaView.addRows()`
- 条件付き依存: `if (!(!length))` → `metaGroup.style.removeProperty()`
- 条件付き依存: `if (cacheEntry)` → `formatNumber()`
- 条件付き依存: `if (cacheEntry)` → `Math.round()`
- 条件付き依存: `if (cacheEntry)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (cacheEntry)` → `document.getElementById()`
- 条件付き依存: `if (!(cacheEntry))` → `setItemValue()`
- 参照: `cacheEntry.dataSize`, `docInfo.characterSet`, `docInfo.compatMode`, `docInfo.contentType`, `docInfo.lastModified`, `docInfo.location`, `docInfo.referrer`, `docInfo.title`, `document.getElementById("encodingtext").value`, `document.getElementById("metatree").view`, `document.getElementById("modifiedtext").value`, `document.getElementById("titletext").value`, `metaGroup.style.visibility`, `metaViewRows.length`

## addImage()
- 位置: async L680-748
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gImageHash.hasOwnProperty()`, `gImageHash[url].hasOwnProperty()`, `gImageHash[url][type].hasOwnProperty()`
- 条件付き依存: `if (!gImageHash[url][type].hasOwnProperty(alt))` → `gImageView.addRow()`
- 条件付き依存: `if (!gImageHash[url][type].hasOwnProperty(alt))` → `openCacheEntry()`
- 条件付き依存: `if (value != -1)` → `Number()`
- 条件付き依存: `if (value != -1)` → `Math.round()`
- 条件付き依存: `if (value != -1)` → `document.l10n .formatValue("media-file-size", { size: kbSize }) .then()`
- 条件付き依存: `if (value != -1)` → `document.l10n .formatValue()`
- 条件付き依存: `if (value != -1)` → `gImageView.tree.invalidateRow()`
- 条件付き依存: `if (value != -1)` → `gImageView.data.indexOf()`
- 条件付き依存: `if (gImageView.data.length == 1)` → `document.getElementById()`
- 参照: `cacheEntry.dataSize`, `document.getElementById("mediaTab").hidden`, `element.height`, `element.imageText`, `element.width`, `gImageElement.currentSrc`, `gImageElement.height`, `gImageElement.imageText`, `gImageElement.width`, `gImageView.data`, `gImageView.data.length`

## onBeginLinkDrag()
- 位置: L751-776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dt.setData()`, `tree.getRowAt()`, `tree.view.getCellText()`
- 参照: `event.clientX`, `event.clientY`, `event.dataTransfer`, `event.originalTarget.localName`, `event.target`, `tree.columns`, `tree.localName`, `tree.parentNode`

## getSelectedRows()
- 位置: L779-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rowArray.push()`, `tree.view.selection.getRangeAt()`, `tree.view.selection.getRangeCount()`
- 参照: `end.value`, `start.value`

## getSelectedRow()
- 位置: L795-798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSelectedRows()`
- 参照: `rows.length`

## selectSaveFolder()
- 位置: async L800-824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `Services.prefs.getComplexValue()`, `document.l10n.formatValue()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`
- 参照: `fp.displayDirectory`, `nsIFilePicker.filterAll`, `nsIFilePicker.modeGetFolder`, `window.browsingContext`
- XPCOM: `@mozilla.org/filepicker;1` / `Services.prefs`

## fpCallback_done()
- 位置: L804-810
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aResult == nsIFilePicker.returnOK)` → `aCallback()`
- 条件付き依存: `if (aResult == nsIFilePicker.returnOK)` → `fp.file.QueryInterface()`
- 条件付き依存: `if (!(aResult == nsIFilePicker.returnOK))` → `aCallback()`
- 参照: `nsIFilePicker.returnOK`

## saveMedia()
- 位置: L826-949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Constructor()`, `document.getElementById()`, `getSelectedRows()`
- 条件付き依存: `if (url)` → `HTMLVideoElement.isInstance()`
- 条件付き依存: `if (!(HTMLVideoElement.isInstance(item)))` → `HTMLAudioElement.isInstance()`
- 条件付き依存: `if (url)` → `Services.io.newURI()`
- 条件付き依存: `if (url)` → `E10SUtils.deserializeCookieJarSettings()`
- 条件付き依存: `if (url)` → `internalSave()`
- 条件付き依存: `if (!(rowArray.length == 1))` → `selectSaveFolder()`
- 条件付き依存: `if (aDirectory)` → `aDirectory.clone()`
- 条件付き依存: `if (aDirectory)` → `Services.io.newURI()`
- 条件付き依存: `if (aDirectory)` → `uri.QueryInterface()`
- 条件付き依存: `if (aDirectory)` → `dir.append()`
- 条件付き依存: `if (aDirectory)` → `decodeURIComponent()`
- 条件付き依存: `if (i == 0)` → `saveAnImage()`
- 条件付き依存: `if (i == 0)` → `Services.io.newURI()`
- 条件付き依存: `if (!(i == 0))` → `setTimeout()`
- 条件付き依存: `if (!(i == 0))` → `Services.io.newURI()`
- 参照: `Ci.nsIReferrerInfo.EMPTY`, `Ci.nsIURL`, `gDocInfo.cookieJarSettings`, `gDocInfo.isContentWindowPrivate`, `gDocInfo.principal`, `gImageView.data`, `item.baseURI`, `item.mimeType`, `rowArray.length`, `uri.fileName`
- XPCOM: [`nsIReferrerInfo`](../../../../docshell/shistory/nsISHEntry.idl.md) / [`nsIURL`](../../../../netwerk/base/nsIURL.idl.md) / `Services.io`

## saveAnImage()
- 位置: L880-909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `E10SUtils.deserializeCookieJarSettings()`, `internalSave()`, `uniqueFile()`
- 参照: `Ci.nsIReferrerInfo.EMPTY`, `aChosenData.file`, `gDocInfo.cookieJarSettings`, `gDocInfo.isContentWindowPrivate`, `gDocInfo.principal`
- XPCOM: [`nsIReferrerInfo`](../../../../docshell/shistory/nsISHEntry.idl.md)

## onImageSelect()
- 位置: L951-974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (count == 0)` → `tree.setAttribute()`
- 条件付き依存: `if (count > 1)` → `tree.setAttribute()`
- 条件付き依存: `if (!(count > 1))` → `tree.setAttribute()`
- 条件付き依存: `if (!(count > 1))` → `makePreview()`
- 条件付き依存: `if (!(count > 1))` → `getSelectedRows()`
- 参照: `mediaSaveBox.collapsed`, `previewBox.collapsed`, `splitter.collapsed`, `tree.view.selection.count`

## makePreview()
- 位置: L977-1189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.io.newURI()`, `actor.sendQuery()`, `checkProtocol()`, `console.error()`, `document.getElementById()`, `getSelectedRows()`, `mediaBrowser.addProgressListener()`, `mediaBrowser.browsingContext.currentWindowGlobal.getActor()`, `mediaBrowser.loadURI()`, `mimeType.startsWith()`, `openCacheEntry()`, `setItemValue()`, `this.getContentTypeFromHeaders()`, `url.replace()`, `window.dispatchEvent()`
- 条件付き依存: `if (cacheEntry)` → `Math.round()`
- 条件付き依存: `if (cacheEntry)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (cacheEntry)` → `document.getElementById()`
- 条件付き依存: `if (cacheEntry)` → `formatNumber()`
- 条件付き依存: `if (!(cacheEntry))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(cacheEntry))` → `document.getElementById()`
- 条件付き依存: `if (mimeType)` → `/^image\/(.*)/i.exec()`
- 条件付き依存: `if (imageMimeType)` → `imageMimeType[1].toUpperCase()`
- 条件付き依存: `if (numFrames > 1)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(numFrames > 1))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(imageMimeType))` → `element.setAttribute()`
- 条件付き依存: `if (!(imageMimeType))` → `element.removeAttribute()`
- 条件付き依存: `if (!(mimeType))` → `element.setAttribute()`
- 条件付き依存: `if (!(mimeType))` → `element.removeAttribute()`
- 条件付き依存: `if (isAllowed)` → `Services.scriptSecurityManager.checkLoadURIWithPrincipal()`
- 条件付き依存: `if (isAllowed)` → `Services.io.newURI()`
- 条件付き依存: `if ( (item.HTMLLinkElement || item.HTMLInputElement || item.HTMLImageElement || item.SVGImageElement || (item.HTMLObjectElement && mimeType && mimeType.startsWit...)` → `document.getElementById()`
- 条件付き依存: `if (item.HTMLVideoElement && isAllowed)` → `document.getElementById()`
- 条件付き依存: `if (item.HTMLVideoElement && isAllowed)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (item.HTMLVideoElement && isAllowed)` → `formatNumber()`
- 条件付き依存: `if (item.HTMLAudioElement && isAllowed)` → `document.getElementById()`
- 条件付き依存: `if (!(item.HTMLAudioElement && isAllowed))` → `document.getElementById()`
- 条件付き依存: `if ( data.width != data.naturalWidth || data.height != data.naturalHeight )` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( data.width != data.naturalWidth || data.height != data.naturalHeight )` → `document.getElementById()`
- 条件付き依存: `if ( data.width != data.naturalWidth || data.height != data.naturalHeight )` → `formatNumber()`
- 条件付き依存: `if (!( data.width != data.naturalWidth || data.height != data.naturalHeight ))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!( data.width != data.naturalWidth || data.height != data.naturalHeight ))` → `document.getElementById()`
- 条件付き依存: `if (!( data.width != data.naturalWidth || data.height != data.naturalHeight ))` → `formatNumber()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `cacheEntry.dataSize`, `data.height`, `data.naturalHeight`, `data.naturalWidth`, `data.width`, `document.getElementById("brokenimagecontainer").collapsed`, `document.getElementById("theimagecontainer").collapsed`, `gDocInfo.principal`, `gImageView.data`, `item.HTMLAudioElement`, `item.HTMLImageElement`, `item.HTMLInputElement`, `item.HTMLLinkElement`, `item.HTMLObjectElement`, `item.HTMLVideoElement`, `item.SVGImageElement`, `item.SVGImageElementHeight`, `item.SVGImageElementWidth`, `item.height`, `item.imageText`, `item.longDesc`, `item.mimeType`, `item.numFrames`, `item.videoHeight`, `item.videoWidth`, `item.width`, `message.height`, `message.width`
- XPCOM: [`nsIWebProgress`](../../../../dom/interfaces/base/nsIBrowser.idl.md) / `Services.io` / `Services.scriptSecurityManager`

## onStateChange()
- 位置: L1117-1124
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aStateFlags & Ci.nsIWebProgressListener.STATE_STOP)` → `mediaBrowser.webProgress?.removeProgressListener()`
- 条件付き依存: `if (aStateFlags & Ci.nsIWebProgressListener.STATE_STOP)` → `resolve()`
- 参照: `Ci.nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## getContentTypeFromHeaders()
- 位置: L1191-1199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^Content-Type:\s*(.*?)\s*(?:\;|$)/im.exec()`, `cacheEntryDescriptor.getMetaDataElement()`

## setItemValue()
- 位置: L1201-1207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `item.closest()`
- 参照: `item.closest("tr").hidden`, `item.value`

## formatNumber()
- 位置: L1209-1211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(+number).toLocaleString()`

## formatDate()
- 位置: L1213-1224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `date.valueOf()`, `dateTimeFormatter.format()`
- 参照: `Services.intl.DateTimeFormat`
- XPCOM: `Services.intl`

## supportsCommand()
- 位置: L1227-1229
- 役割: (未記入)
- 触るとき: (未記入)

## isCommandEnabled()
- 位置: L1231-1233
- 役割: (未記入)
- 触るとき: (未記入)

## doCommand()
- 位置: L1235-1244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doCopy()`, `document.activeElement.view.selection.selectAll()`

## doCopy()
- 位置: L1247-1276
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (elem && elem.localName == "tree")` → `selection.getRangeCount()`
- 条件付き依存: `if (elem && elem.localName == "tree")` → `selection.getRangeAt()`
- 条件付き依存: `if (elem && elem.localName == "tree")` → `view.getCellValue()`
- 条件付き依存: `if (tmp)` → `text.push()`
- 条件付き依存: `if (elem && elem.localName == "tree")` → `gClipboardHelper.copyString()`
- 条件付き依存: `if (elem && elem.localName == "tree")` → `text.join()`
- 参照: `document.commandDispatcher.focusedElement`, `elem.localName`, `elem.view`, `max.value`, `min.value`, `view.selection`

## doSelectAllMedia()
- 位置: L1278-1284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (tree)` → `tree.view.selection.selectAll()`

## selectImage()
- 位置: L1286-1308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if ( !gImageView.data[i][COL_IMAGE_BG] && gImageElement.currentSrc == gImageView.data[i][COL_IMAGE_ADDRESS] && gImageElement.width == image.width && gImageElemen...)` → `tree.view.selection.select()`
- 条件付き依存: `if ( !gImageView.data[i][COL_IMAGE_BG] && gImageElement.currentSrc == gImageView.data[i][COL_IMAGE_ADDRESS] && gImageElement.width == image.width && gImageElemen...)` → `tree.ensureRowIsVisible()`
- 条件付き依存: `if ( !gImageView.data[i][COL_IMAGE_BG] && gImageElement.currentSrc == gImageView.data[i][COL_IMAGE_ADDRESS] && gImageElement.width == image.width && gImageElemen...)` → `tree.focus()`
- 参照: `gImageElement.currentSrc`, `gImageElement.height`, `gImageElement.imageText`, `gImageElement.width`, `gImageView.data`, `image.height`, `image.imageText`, `image.width`, `tree.view.rowCount`

## checkProtocol()
- 位置: L1310-1316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^(https?|file|about|chrome|resource):/.test()`, `/^data:image\//i.test()`

## getOaWithPartitionKey()
- 位置: async L1318-1329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendQuery()`, `browsingContext.currentWindowGlobal.getActor()`
- 参照: `browser.browsingContext`, `browser.contentPrincipal.originAttributes`, `oa.partitionKey`, `partitionKeyFromChild.partitionKey`, `window.opener.gBrowser.selectedBrowser`
