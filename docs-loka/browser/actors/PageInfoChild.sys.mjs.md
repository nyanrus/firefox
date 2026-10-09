# browser/actors/PageInfoChild.sys.mjs

source: browser/actors/PageInfoChild.sys.mjs
source-hash: 18060c54d7b89a00da3cc072b858c77ea281acb5
lines: 399

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## PageInfoChild.receiveMessage()
- 位置: async L14-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `this.getDocumentInfo()`, `this.getDocumentMedia()`, `this.getMetaInfo()`, `this.getPartitionKey()`, `this.getWindowInfo()`
- 参照: `message.name`, `this.contentWindow`, `window.document`

## PageInfoChild.getPartitionKey()
- 位置: L43-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `document.cookieJarSettings.partitionKey`

## PageInfoChild.getMetaInfo()
- 位置: L48-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementsByTagName()`, `metaNode.getAttribute()`, `metaViewRows.push()`
- 参照: `metaNode.content`, `metaNode.httpEquiv`, `metaNode.name`

## PageInfoChild.getWindowInfo()
- 位置: L66-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- 参照: `Services.io.newURI(window.location.href).displayHost`, `window.location.href`, `window.top`, `windowInfo.hostName`, `windowInfo.isTopWindow`
- XPCOM: `Services.io`

## PageInfoChild.getDocumentInfo()
- 位置: L79-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `document.location.toString()`, `lazy.E10SUtils.serializeCookieJarSettings()`, `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 条件付き依存: `if (document.referrer)` → `Services.io.newURI()`
- 参照: `Services.io.newURI( document.location.toString() ).displaySpec`, `Services.io.newURI(document.referrer).displaySpec`, `docInfo.characterSet`, `docInfo.compatMode`, `docInfo.contentType`, `docInfo.cookieJarSettings`, `docInfo.documentURIObject`, `docInfo.isContentWindowPrivate`, `docInfo.lastModified`, `docInfo.location`, `docInfo.principal`, `docInfo.referrer`, `docInfo.title`, `document.characterSet`, `document.compatMode`, `document.contentType`, `document.cookieJarSettings`, `document.documentGlobal`, `document.documentURIObject.spec`, `document.lastModified`, `document.nodePrincipal`, `document.referrer`, `document.title`, `documentURIObject.spec`
- XPCOM: `Services.io`

## PageInfoChild.getDocumentMedia()
- 位置: async L118-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createTreeWalker()`, `iterator.nextNode()`, `this.getMediaItems()`, `totalMediaItems.push()`
- 条件付き依存: `if (++nodeCount % 500 == 0)` → `lazy.setTimeout()`
- 参照: `content.NodeFilter.SHOW_ELEMENT`, `document.documentGlobal`, `iterator.currentNode`

## PageInfoChild.getMediaItems()
- 位置: L141-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.HTMLImageElement.isInstance()`, `elem.documentGlobal.getComputedStyle()`
- 条件付き依存: `if (computedStyle)` → `addImgFunc()`
- 条件付き依存: `if (computedStyle)` → `computedStyle.getCSSImageURLs()`
- 条件付き依存: `if (content.HTMLImageElement.isInstance(elem))` → `addMedia()`
- 条件付き依存: `if (content.HTMLImageElement.isInstance(elem))` → `elem.getAttribute()`
- 条件付き依存: `if (content.HTMLImageElement.isInstance(elem))` → `elem.hasAttribute()`
- 条件付き依存: `if (!(content.HTMLImageElement.isInstance(elem)))` → `content.SVGImageElement.isInstance()`
- 条件付き依存: `if (elem.href.baseVal)` → `URL.parse()`
- 条件付き依存: `if (href)` → `addMedia()`
- 条件付き依存: `if (!(content.SVGImageElement.isInstance(elem)))` → `content.HTMLVideoElement.isInstance()`
- 条件付き依存: `if (content.HTMLVideoElement.isInstance(elem))` → `addMedia()`
- 条件付き依存: `if (!(content.HTMLVideoElement.isInstance(elem)))` → `content.HTMLAudioElement.isInstance()`
- 条件付き依存: `if (content.HTMLAudioElement.isInstance(elem))` → `addMedia()`
- 条件付き依存: `if (!(content.HTMLAudioElement.isInstance(elem)))` → `content.HTMLLinkElement.isInstance()`
- 条件付き依存: `if (content.HTMLLinkElement.isInstance(elem))` → `/\bicon\b/i.test()`
- 条件付き依存: `if (elem.rel && /\bicon\b/i.test(elem.rel))` → `addMedia()`
- 条件付き依存: `if (!(content.HTMLLinkElement.isInstance(elem)))` → `content.HTMLInputElement.isInstance()`
- 条件付き依存: `if (!(content.HTMLLinkElement.isInstance(elem)))` → `content.HTMLButtonElement.isInstance()`
- 条件付き依存: `if ( content.HTMLInputElement.isInstance(elem) || content.HTMLButtonElement.isInstance(elem) )` → `elem.type.toLowerCase()`
- 条件付き依存: `if (elem.type.toLowerCase() == "image")` → `addMedia()`
- 条件付き依存: `if (elem.type.toLowerCase() == "image")` → `elem.getAttribute()`
- 条件付き依存: `if (elem.type.toLowerCase() == "image")` → `elem.hasAttribute()`
- 条件付き依存: `if (!( content.HTMLInputElement.isInstance(elem) || content.HTMLButtonElement.isInstance(elem) ))` → `content.HTMLObjectElement.isInstance()`
- 条件付き依存: `if (content.HTMLObjectElement.isInstance(elem))` → `addMedia()`
- 条件付き依存: `if (content.HTMLObjectElement.isInstance(elem))` → `this.getValueText()`
- 条件付き依存: `if (!(content.HTMLObjectElement.isInstance(elem)))` → `content.HTMLEmbedElement.isInstance()`
- 条件付き依存: `if (content.HTMLEmbedElement.isInstance(elem))` → `addMedia()`
- 参照: `URL.parse(elem.href.baseVal, elem.baseURI)?.href`, `document.documentGlobal`, `elem.baseURI`, `elem.currentSrc`, `elem.data`, `elem.href`, `elem.href.baseVal`, `elem.rel`, `elem.src`

## addMedia()
- 位置: L149-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mediaItems.push()`, `this.serializeElementInfo()`

## addImgFunc()
- 位置: L162-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addMedia()`

## PageInfoChild.serializeElementInfo()
- 位置: L236-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.HTMLAudioElement.isInstance()`, `content.HTMLEmbedElement.isInstance()`, `content.HTMLImageElement.isInstance()`, `content.HTMLInputElement.isInstance()`, `content.HTMLLinkElement.isInstance()`, `content.HTMLObjectElement.isInstance()`, `content.HTMLVideoElement.isInstance()`, `content.ImageDocument.isInstance()`, `content.SVGImageElement.isInstance()`, `url.startsWith()`
- 条件付き依存: `if ( !isBG && !content.SVGImageElement.isInstance(item) && !content.ImageDocument.isInstance(document) )` → `content.HTMLImageElement.isInstance()`
- 条件付き依存: `if (!imageText && !content.HTMLImageElement.isInstance(item))` → `this.getValueText()`
- 条件付き依存: `if ( !result.mimeType && !isBG && item instanceof Ci.nsIImageLoadingContent )` → `item.getRequest()`
- 条件付き依存: `if (!result.mimeType && url.startsWith("data:"))` → `/^data:(image\/[^;,]+)/i.exec()`
- 条件付き依存: `if (dataMimeType)` → `dataMimeType[1].toLowerCase()`
- 条件付き依存: `if (isBG)` → `content.document.createElement()`
- 条件付き依存: `if (!(isBG))` → `content.SVGImageElement.isInstance()`
- 参照: `Ci.nsIImageLoadingContent`, `Ci.nsIImageLoadingContent.CURRENT_REQUEST`, `document.documentGlobal`, `image.numFrames`, `imageRequest.STATUS_ERROR`, `imageRequest.image`, `imageRequest.imageStatus`, `imageRequest.mimeType`, `img.naturalHeight`, `img.naturalWidth`, `img.src`, `item.alt`, `item.baseURI`, `item.height`, `item.height.baseVal.value`, `item.longDesc`, `item.title`, `item.type`, `item.width`, `item.width.baseVal.value`, `result.HTMLAudioElement`, `result.HTMLImageElement`, `result.HTMLInputElement`, `result.HTMLLinkElement`, `result.HTMLObjectElement`, `result.HTMLVideoElement`, `result.SVGImageElement`, `result.SVGImageElementHeight`, `result.SVGImageElementWidth`, `result.baseURI`, `result.height`, `result.imageText`, `result.longDesc`, `result.mimeType`, `result.naturalHeight`, `result.naturalWidth`, `result.numFrames`, `result.width`
- XPCOM: [`nsIImageLoadingContent`](../../dom/base/nsIImageLoadingContent.idl.md)

## PageInfoChild.getValueText()
- 位置: L334-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.HTMLInputElement.isInstance()`, `content.HTMLSelectElement.isInstance()`, `content.HTMLTextAreaElement.isInstance()`, `this.stripWS()`
- 条件付き依存: `if (nodeType == content.Node.ELEMENT_NODE)` → `content.HTMLImageElement.isInstance()`
- 条件付き依存: `if (content.HTMLImageElement.isInstance(childNode))` → `this.getAltText()`
- 条件付き依存: `if (!(content.HTMLImageElement.isInstance(childNode)))` → `this.getValueText()`
- 参照: `childNode.nodeType`, `childNode.nodeValue`, `content.Node.ELEMENT_NODE`, `content.Node.TEXT_NODE`, `node.childNodes`, `node.childNodes.length`, `node.documentGlobal`

## PageInfoChild.getAltText()
- 位置: L373-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAltText()`
- 参照: `node.alt`, `node.childNodes`, `node.childNodes.length`

## PageInfoChild.stripWS()
- 位置: L391-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `text.replace()`
