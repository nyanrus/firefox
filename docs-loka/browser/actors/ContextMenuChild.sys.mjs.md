# browser/actors/ContextMenuChild.sys.mjs

source: browser/actors/ContextMenuChild.sys.mjs
source-hash: bdb925257894ad76f7eaab179f41847e3f1d7d33
lines: 1303

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ContextMenuChild.constructor()
- 位置: L22-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.context`, `this.lastMenuTarget`, `this.target`

## ContextMenuChild.getTarget()
- 位置: L30-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.getTarget()`, `contextMenus.get()`
- 参照: `browsingContext.id`

## ContextMenuChild.getLastTarget()
- 位置: L42-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contextMenus.get()`
- 参照: `contextMenu.lastMenuTarget`

## ContextMenuChild.receiveMessage()
- 位置: L47-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Promise.resolve()`, `Services.io.newURI()`, `canvas.getContext()`, `canvas.toDataURL()`, `ctxDraw.drawImage()`, `formData.set()`, `formData.values()`, `formData.values().some()`, `img.recognizeCurrentImageText()`, `img.recognizeCurrentImageText().then()`, `input.setUserInput()`, `lazy.ContentDOMReference.resolve()`, `lazy.E10SUtils.wrapHandlingUserInput()`, `media.pause()`, `media.play()`, `media.removeAttribute()`, `media.setAttribute()`, `node.form.getAttribute()`, `node.form.method.toUpperCase()`, `resolve()`, `sel.getRangeAt()`, `target.ownerDocument.location.reload()`, `target.toBlob()`, `this._disableSetDesktopBackground()`, `this.contentWindow.URL.createObjectURL()`, `this.contentWindow.getComputedStyle()`, `this.contentWindow.getSelection()`, `this.contentWindow.history.replaceState()`, `this.contentWindow.windowUtils.dispatchEventToChromeOnly()`, `this.document.createElementNS()`, `this.document.fragmentDirective .createTextDirectiveForRanges()`, `this.document.fragmentDirective .createTextDirectiveForRanges(ranges) .then()`, `this.document.fragmentDirective.getTextDirectiveRanges()`, `this.document.fragmentDirective.removeAllTextDirectives()`
- 条件付き依存: `if (this.document.fullscreenEnabled)` → `media.requestFullscreen()`
- 条件付き依存: `if (image instanceof Ci.nsIImageLoadingContent)` → `image.forceReload()`
- 条件付き依存: `if ( !node.name || (method != "POST" && method != "GET") || node.form.enctype != "application/x-www-form-urlencoded" || formData.values().some(v => typeof v != "...)` → `Promise.reject()`
- 条件付き依存: `if (!disable)` → `this.contentWindow.HTMLCanvasElement.isInstance()`
- 条件付き依存: `if (!(this.contentWindow.HTMLCanvasElement.isInstance(target)))` → `Services.scriptSecurityManager.checkLoadURIWithPrincipal()`
- 条件付き依存: `if (!(this.contentWindow.HTMLCanvasElement.isInstance(target)))` → `this.document.createElement()`
- 条件付き依存: `if (!(this.contentWindow.HTMLCanvasElement.isInstance(target)))` → `canvas.getContext()`
- 条件付き依存: `if (!(this.contentWindow.HTMLCanvasElement.isInstance(target)))` → `ctx.drawImage()`
- 条件付き依存: `if (!disable)` → `canvas.toDataURL()`
- 条件付き依存: `if (!disable)` → `url.pathname.substr()`
- 条件付き依存: `if (!disable)` → `url.pathname.lastIndexOf()`
- 条件付き依存: `if (!disable)` → `Promise.resolve()`
- 条件付き依存: `if (!disable)` → `console.error()`
- 条件付き依存: `if (textFragment)` → `URL.fromURI()`
- 参照: `Ci.nsIImageLoadingContent`, `Services.io.newURI( node.form.getAttribute("action"), charset, formBaseURI ).spec`, `canvas.height`, `canvas.width`, `media.loop`, `media.muted`, `media.playbackRate`, `message.data.command`, `message.data.data`, `message.data.emailMask`, `message.data.forceReload`, `message.data.handlingUserInput`, `message.data.targetIdentifier`, `message.name`, `node.form`, `node.form.baseURI`, `node.form.enctype`, `node.name`, `node.ownerDocument.characterSet`, `sel.isCollapsed`, `sel.rangeCount`, `target.currentURI`, `target.naturalHeight`, `target.naturalWidth`, `target.ownerDocument.location`, `target.ownerDocument.nodePrincipal`, `target.ownerDocument.title`, `target.revealPassword`, `this.contentWindow`, `this.contentWindow.CustomEvent`, `this.contentWindow.history.state`, `this.contentWindow.location.href`, `this.context`, `this.document.fullscreenEnabled`, `this.document?.documentURIObject`, `this.target`, `url.hash`, `url.href`, `video.videoHeight`, `video.videoWidth`
- XPCOM: [`nsIImageLoadingContent`](../../dom/base/nsIImageLoadingContent.idl.md) / `Services.io` / `Services.scriptSecurityManager`

## ContextMenuChild.getTarget()
- 位置: L322-324
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aMessage.objects`, `this.target`

## ContextMenuChild._isXULTextLinkLabel()
- 位置: L327-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.classList.contains()`
- 参照: `aNode.href`, `aNode.namespaceURI`, `aNode.tagName`

## ContextMenuChild._getLinkURL()
- 位置: L339-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `href.match()`, `this.context.link.getAttribute()`, `this.context.link.getAttributeNS()`
- 参照: `href.animVal`, `new URL(href, this.context.link.baseURI).href`, `new URL(href.animVal, this.context.link.baseURI).href`, `this.context.link.baseURI`, `this.context.link.href`

## ContextMenuChild._getLinkURI()
- 位置: L364-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- 参照: `this.context.linkURL`
- XPCOM: `Services.io`

## ContextMenuChild._getLinkText()
- 位置: L375-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `text.match()`, `this._gatherTextUnder()`
- 条件付き依存: `if (!text || !text.match(/\S/))` → `this.context.link.getAttribute()`
- 条件付き依存: `if (!text || !text.match(/\S/))` → `text.match()`
- 参照: `this.context.link`, `this.context.linkURL`

## ContextMenuChild._getLinkProtocol()
- 位置: L391-397
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.context.linkURI`, `this.context.linkURI.scheme`

## ContextMenuChild._isLinkSaveable()
- 位置: L400-413
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.context.linkProtocol`

## ContextMenuChild._gatherTextUnder()
- 位置: L418-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.createDocumentEncoder()`, `encoder.encodeToString()`, `encoder.encodeToString().trim()`, `encoder.init()`, `encoder.setContainerNode()`
- 参照: `root.ownerDocument`

## ContextMenuChild._getComputedURL()
- 位置: L426-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aElem.documentGlobal .getComputedStyle()`, `aElem.documentGlobal .getComputedStyle(aElem) .getCSSImageURLs()`
- 参照: `urls.length`

## ContextMenuChild._isProprietaryDRM()
- 位置: L442-448
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.context.target.isEncrypted`, `this.context.target.mediaKeys`, `this.context.target.mediaKeys.keySystem`

## ContextMenuChild._isMediaURLReusable()
- 位置: L450-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aURL.startsWith()`
- 条件付き依存: `if (aURL.startsWith("blob:"))` → `URL.isBoundToBlob()`

## ContextMenuChild._maybeGetVideoElementAtPoint()
- 位置: L466-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.contentWindow.HTMLVideoElement.isInstance()`, `this.contentWindow.windowUtils.nodesFromRect()`
- XPCOM: `Services.prefs`

## ContextMenuChild._isTargetATextBox()
- 位置: L496-502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contentWindow.HTMLInputElement.isInstance()`, `this.contentWindow.HTMLTextAreaElement.isInstance()`
- 条件付き依存: `if (this.contentWindow.HTMLInputElement.isInstance(node))` → `node.mozIsTextField()`

## ContextMenuChild._isSpellCheckEnabled()
- 位置: L504-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isTargetATextBox()`
- 参照: `aNode.isContentEditable`, `aNode.ownerDocument`, `aNode.ownerDocument.designMode`, `aNode.spellcheck`

## ContextMenuChild._disableSetDesktopBackground()
- 位置: L525-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTarget.currentURI.schemeIs()`, `aTarget.getRequest()`, `this.contentWindow.HTMLCanvasElement.isInstance()`
- 参照: `Ci.nsIImageLoadingContent`, `Ci.nsIImageLoadingContent.CURRENT_REQUEST`, `aTarget.complete`
- XPCOM: [`nsIImageLoadingContent`](../../dom/base/nsIImageLoadingContent.idl.md)

## ContextMenuChild.handleEvent()
- 位置: async L553-746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/referrer-info;1"].createInstance()`, `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `aEvent.composedTarget.documentGlobal.updateCommands()`, `aEvent.stopPropagation()`, `contextMenus.set()`, `docState.getFieldContext()`, `lazy.E10SUtils.serializeReferrerInfo()`, `lazy.LoginManagerChild.forWindow()`, `lazy.SelectionUtils.getSelectionDetails()`, `lazy.SpellCheckHelper.isEditable()`, `loginManagerChild.stateForDocument()`, `referrerInfo.initWithElement()`, `this._setContext()`, `this.docShell.docViewer .QueryInterface()`, `this.docShell.docViewer .QueryInterface(Ci.nsIDocumentViewerEdit) .setCommandNode()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!doc && Cu.isInAutomation)` → `dump()`
- 条件付き依存: `if (composedTarget.nodeType == composedTarget.ELEMENT_NODE)` → `this.contentWindow.HTMLCanvasElement.isInstance()`
- 条件付き依存: `if ( isImage || this.contentWindow.HTMLCanvasElement.isInstance(composedTarget) )` → `this._disableSetDesktopBackground()`
- 条件付き依存: `if (isImage)` → `Cc["@mozilla.org/image/tools;1"] .getService(Ci.imgITools) .getImgCacheForDocument()`
- 条件付き依存: `if (isImage)` → `Cc["@mozilla.org/image/tools;1"] .getService()`
- 条件付き依存: `if (isImage)` → `imageCache.findEntryProperties()`
- 条件付き依存: `if (isImage)` → `props.get()`
- 条件付き依存: `if (context.onLink)` → `Cc["@mozilla.org/referrer-info;1"].createInstance()`
- 条件付き依存: `if (context.onLink)` → `linkReferrerInfo.initWithElement()`
- 条件付き依存: `if (target)` → `this._cleanContext()`
- 条件付き依存: `if (editFlags & lazy.SpellCheckHelper.SPELLCHECKABLE)` → `lazy.InlineSpellCheckerContent.initContextMenu()`
- 条件付き依存: `if (context.inFrame && !context.inSrcdocFrame)` → `lazy.E10SUtils.serializeReferrerInfo()`
- 条件付き依存: `if (linkReferrerInfo)` → `lazy.E10SUtils.serializeReferrerInfo()`
- 条件付き依存: `if (!spellInfo)` → `this.sendAsyncMessage()`
- 参照: `Ci.imgITools`, `Ci.nsIDocumentViewerEdit`, `Ci.nsIImageLoadingContent`, `Ci.nsIReferrerInfo`, `Ci.nsISupportsCString`, `Cu.isInAutomation`, `aEvent.composedTarget`, `aEvent.composedTarget.currentURI`, `aEvent.composedTarget.nodePrincipal.isSystemPrincipal`, `aEvent.composedTarget.ownerDocument`, `aEvent.defaultPrevented`, `aEvent[k]?.ownerDocument`, `composedTarget.ELEMENT_NODE`, `composedTarget.currentURI`, `composedTarget.nodeType`, `context.inFrame`, `context.inSrcdocFrame`, `context.link`, `context.onLink`, `context.target`, `data.frameReferrerInfo`, `data.linkReferrerInfo`, `data.spellInfo`, `doc.defaultView`, `doc.nodePrincipal`, `doc.referrerInfo`, `docLocation.spec`, `lazy.SpellCheckHelper.SPELLCHECKABLE`, `props.get( "content-disposition", Ci.nsISupportsCString ).data`, `props.get("type", Ci.nsISupportsCString).data`, `this.browsingContext`, `this.contentWindow`, `this.context`, `this.target`
- XPCOM: [`nsIDocumentViewerEdit`](../../docshell/base/nsIDocumentViewerEdit.idl.md) / [`nsIImageLoadingContent`](../../dom/base/nsIImageLoadingContent.idl.md) / [`nsIReferrerInfo`](../../docshell/shistory/nsISHEntry.idl.md) / [`nsISupportsCString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/image/tools;1` → `mozilla::image::imgTools` (image/build/components.conf) / `@mozilla.org/referrer-info;1` / `Services.obs` / `Services.prefs`

## ContextMenuChild.setWebExtContextData()
- 位置: L724-726
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `data.webExtContextData`

## ContextMenuChild._cleanContext()
- 位置: L755-803
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Object.create()`
- 条件付き依存: `if (onMedia)` → `Object.assign()`
- 条件付き依存: `if (context.onVideo)` → `Object.assign()`
- 参照: `cleanTarget.ownerDocument`, `context.link`, `context.linkURI`, `context.linkURL`, `context.onAudio`, `context.onVideo`, `context.target`, `context.target.HAVE_CURRENT_DATA`, `context.target.NETWORK_NO_SOURCE`, `context.target.controls`, `context.target.duration`, `context.target.ended`, `context.target.error`, `context.target.loop`, `context.target.muted`, `context.target.networkState`, `context.target.ownerDocument.contentType`, `context.target.ownerDocument.fullscreen`, `context.target.paused`, `context.target.playbackRate`, `context.target.readyState`, `this.context`

## ContextMenuChild._setContext()
- 位置: L805-955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `Object.create()`, `lazy.ContentDOMReference.get()`, `lazy.E10SUtils.serializePolicyContainer()`, `lazy.SpellCheckHelper.isEditable()`, `node.containingShadowRoot?.isUAWidget()`, `this._isXULTextLinkLabel()`, `this._setContextForNodesNoChildren()`, `this._setContextForNodesWithChildren()`, `this.document.documentURI.startsWith()`, `this.document.fragmentDirective?.getTextDirectiveRanges()`
- 条件付き依存: `if (node.containingShadowRoot?.isUAWidget())` → `this.contentWindow.HTMLMediaElement.isInstance()`
- 条件付き依存: `if (node.containingShadowRoot?.isUAWidget())` → `this.contentWindow.HTMLEmbedElement.isInstance()`
- 条件付き依存: `if (node.containingShadowRoot?.isUAWidget())` → `this.contentWindow.HTMLObjectElement.isInstance()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.composedTarget`, `aEvent.inputSource`, `aEvent.screenX`, `aEvent.screenY`, `aEvent.timeStamp`, `context.bgImageURL`, `context.canSpellCheck`, `context.clientX`, `context.clientY`, `context.hasBGImage`, `context.hasMultipleBGImages`, `context.hasTextFragments`, `context.imageDescURL`, `context.imageInfo`, `context.inAboutDevtoolsToolbox`, `context.inFrame`, `context.inPDFViewer`, `context.inSrcdocFrame`, `context.inSyntheticDoc`, `context.inTabBrowser`, `context.inWebExtBrowser`, `context.inputSource`, `context.isDesignMode`, `context.link`, `context.linkDownload`, `context.linkProtocol`, `context.linkTextStr`, `context.linkURI`, `context.linkURL`, `context.mediaURL`, `context.onAudio`, `context.onCanvas`, `context.onCompletedImage`, `context.onDRMMedia`, `context.onEditable`, `context.onImage`, `context.onLink`, `context.onLoadedImage`, `context.onMailtoLink`, `context.onMozExtLink`, `context.onNumeric`, `context.onPassword`, `context.onPiPVideo`, `context.onSaveableLink`, `context.onSpellcheckable`, `context.onTelLink`, `context.onTextInput`, `context.onVideo`, `context.passwordRevealed`, `context.pdfStates`, `context.policyContainer`, `context.screenXDevPx`, `context.screenYDevPx`, `context.shouldDisplay`, `context.shouldInitInlineSpellCheckerUINoChildren`, `context.shouldInitInlineSpellCheckerUIWithChildren`, `context.target`, `context.target.ownerDocument.mozSyntheticDocument`, `context.target.ownerDocument.nodePrincipal.originNoSuffix`, `context.target.ownerDocument.pdfStates`, `context.target.ownerDocument.policyContainer`, `context.targetIdentifier`, `context.timeStamp`, `context.webExtBrowserType`, `lazy.SpellCheckHelper.TEXTINPUT`, `node.DOCUMENT_NODE`, `node.containingShadowRoot.host`, `node.namespaceURI`, `node.nodeType`, `textDirectiveRanges.length`, `this.contentWindow`, `this.contentWindow.devicePixelRatio`, `this.context`, `this.lastMenuTarget`

## ContextMenuChild._setContextForNodesNoChildren()
- 位置: L963-1162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isSpellCheckEnabled()`
- 条件付き依存: `if (context.target.nodeType == context.target.TEXT_NODE)` → `this._isSpellCheckEnabled()`
- 条件付き依存: `if ( context.target instanceof Ci.nsIImageLoadingContent && (context.target.currentRequestFinalURI || context.target.currentURI) )` → `this.contentWindow.ImageDocument.isInstance()`
- 条件付き依存: `if ( context.target instanceof Ci.nsIImageLoadingContent && (context.target.currentRequestFinalURI || context.target.currentURI) )` → `SVGAnimatedLength.isInstance()`
- 条件付き依存: `if ( context.target instanceof Ci.nsIImageLoadingContent && (context.target.currentRequestFinalURI || context.target.currentURI) )` → `context.target.getRequest()`
- 条件付き依存: `if ( context.target instanceof Ci.nsIImageLoadingContent && (context.target.currentRequestFinalURI || context.target.currentURI) )` → `this._isMediaURLReusable()`
- 条件付き依存: `if ( context.target instanceof Ci.nsIImageLoadingContent && (context.target.currentRequestFinalURI || context.target.currentURI) )` → `context.target.getAttribute()`
- 条件付き依存: `if (!( context.target instanceof Ci.nsIImageLoadingContent && (context.target.currentRequestFinalURI || context.target.currentURI) ))` → `this.contentWindow.HTMLCanvasElement.isInstance()`
- 条件付き依存: `if (!( this.contentWindow.HTMLCanvasElement.isInstance(context.target) ))` → `this.contentWindow.HTMLVideoElement.isInstance()`
- 条件付き依存: `if (!( this.contentWindow.HTMLCanvasElement.isInstance(context.target) ))` → `this._maybeGetVideoElementAtPoint()`
- 条件付き依存: `if ( (videoElement = this.contentWindow.HTMLVideoElement.isInstance( context.target ) ? context.target : this._maybeGetVideoElementAtPoint(context.clientX, conte...)` → `lazy.ContentDOMReference.get()`
- 条件付き依存: `if ( (videoElement = this.contentWindow.HTMLVideoElement.isInstance( context.target ) ? context.target : this._maybeGetVideoElementAtPoint(context.clientX, conte...)` → `this._isMediaURLReusable()`
- 条件付き依存: `if ( (videoElement = this.contentWindow.HTMLVideoElement.isInstance( context.target ) ? context.target : this._maybeGetVideoElementAtPoint(context.clientX, conte...)` → `this._isProprietaryDRM()`
- 条件付き依存: `if (!( (videoElement = this.contentWindow.HTMLVideoElement.isInstance( context.target ) ? context.target : this._maybeGetVideoElementAtPoint(context.clientX, conte...))` → `this.contentWindow.HTMLAudioElement.isInstance()`
- 条件付き依存: `if (this.contentWindow.HTMLAudioElement.isInstance(context.target))` → `this._isMediaURLReusable()`
- 条件付き依存: `if (this.contentWindow.HTMLAudioElement.isInstance(context.target))` → `this._isProprietaryDRM()`
- 条件付き依存: `if ( editFlags & (lazy.SpellCheckHelper.INPUT | lazy.SpellCheckHelper.TEXTAREA) )` → `HTMLInputElement.isInstance()`
- 条件付き依存: `if ( editFlags & (lazy.SpellCheckHelper.INPUT | lazy.SpellCheckHelper.TEXTAREA) )` → `lazy.LoginHelper.isInferredEmailField()`
- 条件付き依存: `if ( editFlags & (lazy.SpellCheckHelper.INPUT | lazy.SpellCheckHelper.TEXTAREA) )` → `lazy.LoginHelper.isInferredUsernameField()`
- 条件付き依存: `if (!( editFlags & (lazy.SpellCheckHelper.INPUT | lazy.SpellCheckHelper.TEXTAREA) ))` → `this.contentWindow.HTMLHtmlElement.isInstance()`
- 条件付き依存: `if (bodyElt)` → `this._getComputedURL()`
- 参照: `Ci.nsIImageLoadingContent`, `Ci.nsIImageLoadingContent.CURRENT_REQUEST`, `bodyElt.baseURI`, `context.bgImageURL`, `context.canSpellCheck`, `context.clientX`, `context.clientY`, `context.hasBGImage`, `context.hasMultipleBGImages`, `context.imageDescURL`, `context.imageInfo`, `context.imageInfo.height`, `context.imageInfo.height.animVal.value`, `context.imageInfo.width`, `context.imageInfo.width.animVal.value`, `context.isDesignMode`, `context.mediaURL`, `context.onAudio`, `context.onCanvas`, `context.onCompletedImage`, `context.onDRMMedia`, `context.onEditable`, `context.onImage`, `context.onLoadedImage`, `context.onNumeric`, `context.onPassword`, `context.onPiPVideo`, `context.onSearchField`, `context.onSpellcheckable`, `context.onTextInput`, `context.onVideo`, `context.originalMediaURL`, `context.passwordRevealed`, `context.shouldInitInlineSpellCheckerUINoChildren`, `context.showRelay`, `context.target`, `context.target.ELEMENT_NODE`, `context.target.HAVE_METADATA`, `context.target.TEXT_NODE`, `context.target.alt`, `context.target.currentRequestFinalURI`, `context.target.currentRequestFinalURI?.spec`, `context.target.currentSrc`, `context.target.currentURI`, `context.target.currentURI?.spec`, `context.target.disabled`, `context.target.height`, `context.target.isCloningElementVisually`, `context.target.nodeType`, `context.target.ownerDocument`, `context.target.ownerDocument.body`, `context.target.ownerDocument.body.baseURI`, `context.target.parentNode`, `context.target.readOnly`, `context.target.readyState`, `context.target.revealPassword`, `context.target.src`, `context.target.title`, `context.target.videoHeight`, `context.target.videoWidth`, `context.target.width`, `context.targetIdentifier`, `lazy.SpellCheckHelper.CONTENTEDITABLE`, `lazy.SpellCheckHelper.EDITABLE`, `lazy.SpellCheckHelper.INPUT`, `lazy.SpellCheckHelper.NUMERIC`, `lazy.SpellCheckHelper.PASSWORD`, `lazy.SpellCheckHelper.SEARCHENGINE`, `lazy.SpellCheckHelper.SPELLCHECKABLE`, `lazy.SpellCheckHelper.TEXTAREA`, `lazy.SpellCheckHelper.TEXTINPUT`, `new URL( descURL, context.target.ownerDocument.body.baseURI ).href`, `new URL(computedURL, bodyElt.baseURI).href`, `request.STATUS_ERROR`, `request.STATUS_LOAD_COMPLETE`, `request.STATUS_SIZE_AVAILABLE`, `request.imageStatus`, `this.context`
- XPCOM: [`nsIImageLoadingContent`](../../dom/base/nsIImageLoadingContent.idl.md)

## ContextMenuChild._setContextForNodesWithChildren()
- 位置: L1170-1285
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `this.contentWindow.HTMLAnchorElement.isInstance()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `this.contentWindow.HTMLAreaElement.isInstance()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `this.contentWindow.HTMLLinkElement.isInstance()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `this.contentWindow.SVGAElement.isInstance()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `elem.hasAttributeNS()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `this.contentWindow.MathMLElement.isInstance()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `elem.hasAttribute()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `elem.getAttributeNS()`
- 条件付き依存: `if (elem.nodeType == elem.ELEMENT_NODE)` → `this._isXULTextLinkLabel()`
- 条件付き依存: `if ( !context.onLink && // Be consistent with what hrefAndLinkNodeForClickEvent // does in BrowserUtils.sys.msj ((this.contentWindow.HTMLAnchorElement.isInstance...)` → `this._getLinkURL()`
- 条件付き依存: `if ( !context.onLink && // Be consistent with what hrefAndLinkNodeForClickEvent // does in BrowserUtils.sys.msj ((this.contentWindow.HTMLAnchorElement.isInstance...)` → `this._getLinkURI()`
- 条件付き依存: `if ( !context.onLink && // Be consistent with what hrefAndLinkNodeForClickEvent // does in BrowserUtils.sys.msj ((this.contentWindow.HTMLAnchorElement.isInstance...)` → `this._getLinkText()`
- 条件付き依存: `if ( !context.onLink && // Be consistent with what hrefAndLinkNodeForClickEvent // does in BrowserUtils.sys.msj ((this.contentWindow.HTMLAnchorElement.isInstance...)` → `this._getLinkProtocol()`
- 条件付き依存: `if ( !context.onLink && // Be consistent with what hrefAndLinkNodeForClickEvent // does in BrowserUtils.sys.msj ((this.contentWindow.HTMLAnchorElement.isInstance...)` → `this._isLinkSaveable()`
- 条件付き依存: `if (elem.download)` → `context.target.ownerDocument.nodePrincipal.checkMayLoad()`
- 条件付き依存: `if (!context.hasBGImage && !context.hasMultipleBGImages)` → `this._getComputedURL()`
- 参照: `context.bgImageURL`, `context.hasBGImage`, `context.hasMultipleBGImages`, `context.inFrame`, `context.inSrcdocFrame`, `context.isDesignMode`, `context.isSponsoredLink`, `context.link`, `context.linkDownload`, `context.linkProtocol`, `context.linkTextStr`, `context.linkURI`, `context.linkURL`, `context.onCompletedImage`, `context.onEditable`, `context.onImage`, `context.onLink`, `context.onLoadedImage`, `context.onMailtoLink`, `context.onMozExtLink`, `context.onSaveableLink`, `context.onSpellcheckable`, `context.onTelLink`, `context.onTextInput`, `context.shouldInitInlineSpellCheckerUIWithChildren`, `context.target`, `context.target.documentGlobal`, `context.target.ownerDocument.isSrcdocDocument`, `docDefaultView.top`, `elem.ELEMENT_NODE`, `elem.baseURI`, `elem.dataset.isSponsoredLink`, `elem.download`, `elem.flattenedTreeParentNode`, `elem.href`, `elem.localName`, `elem.nodeType`, `elem.ownerDocument.URL`, `lazy.SpellCheckHelper.CONTENTEDITABLE`, `new URL(bgImgUrl, elem.baseURI).href`, `this.context`
- XPCOM: `Services.prefs`

## ContextMenuChild.registerDestructionObserver()
- 位置: L1288-1290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._destructionObservers.add()`

## ContextMenuChild.unregisterDestructionObserver()
- 位置: L1292-1294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._destructionObservers.delete()`

## ContextMenuChild.didDestroy()
- 位置: L1296-1301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `obs.actorDestroyed()`
- 参照: `this._destructionObservers`
