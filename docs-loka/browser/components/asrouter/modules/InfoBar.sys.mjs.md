# browser/components/asrouter/modules/InfoBar.sys.mjs

source: browser/components/asrouter/modules/InfoBar.sys.mjs
source-hash: fe95571d5b11a508939e05bc806e1c975c5c0bf7
lines: 822

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## InfoBarNotification.constructor()
- 位置: L30-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `this.buttonCallback.bind()`, `this.dispatchUserAction.bind()`, `this.infobarCallback.bind()`
- 参照: `message?.content?.dismissOnPrefChange`, `this._browser`, `this._dismissPrefs`, `this._dispatch`, `this._prefObserver`, `this.buttonCallback`, `this.dispatchUserAction`, `this.infobarCallback`, `this.message`, `this.notification`

## InfoBarNotification._ensureLinkTemplatesFor()
- 位置: L54-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `doc.getElementById()`
- 条件付き依存: `if (!container)` → `doc.createElement()`
- 条件付き依存: `if (!container)` → `doc.body.appendChild()`
- 条件付き依存: `if (!container.querySelector(`a[data-l10n-name="${name}"]`))` → `doc.createElement()`
- 条件付き依存: `if (!container.querySelector(`a[data-l10n-name="${name}"]`))` → `container.appendChild()`
- 参照: `a.dataset.l10nName`, `a.href`, `container.hidden`, `container.id`, `this.message.content.linkUrls`

## InfoBarNotification._buildMessageFragment()
- 位置: async L84-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...temp.querySelectorAll("a[data-l10n-name]")].map()`, `doc.createDocumentFragment()`, `doc.importNode()`, `frag.appendChild()`, `html.includes()`, `lazy.RemoteL10n.formatLocalizableText()`, `new DOMParser().parseFromString()`, `temp.querySelectorAll()`, `this._ensureLinkTemplatesFor()`
- 条件付き依存: `if (!html.includes('data-l10n-name="'))` → `lazy.RemoteL10n.createElement()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `importedNode.matches()`
- 条件付き依存: `if (importedNode.matches("a[data-l10n-name]"))` → `anchors.push()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `anchors.push()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `importedNode.querySelectorAll()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `doc .getElementById("infobar-link-templates") .querySelector()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `doc .getElementById()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `a.addEventListener()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `e.preventDefault()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if (importedNode.nodeType === Node.ELEMENT_NODE)` → `console.error()`
- 条件付き依存: `if (linkActions[name])` → `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if (linkActions[name])` → `console.error()`
- 条件付き依存: `if (linkActions[name].dismiss)` → `this.notification?.dismiss()`
- 参照: `Node.ELEMENT_NODE`, `a.dataset.l10nName`, `a.href`, `importedNode.nodeType`, `linkActions[name].dismiss`, `new DOMParser().parseFromString(html, "text/html").body`, `temp.childNodes`, `template.href`, `text.args?.where`, `this.message.content.linkActions`

## InfoBarNotification.showNotification()
- 位置: async L179-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[TYPES.GLOBAL, TYPES.UNIVERSAL].includes()`, `content.buttons.map()`, `doc.createElement()`, `messageSlot.appendChild()`, `messageSlot.setAttribute()`, `notificationContainer.appendNotification()`, `this._maybeAttachPrefObserver()`, `this.formatButtonConfig()`, `this.formatMessageConfig()`, `this.notification.appendChild()`
- 条件付き依存: `if (!([TYPES.GLOBAL, TYPES.UNIVERSAL].includes(content.type)))` → `gBrowser.getNotificationBox()`
- 条件付き依存: `if (InfoBar._activeInfobar?.notification !== this)` → `notificationContainer.removeNotification()`
- 条件付き依存: `if ( content.type !== TYPES.UNIVERSAL || !InfoBar._universalInfobars.length )` → `this.addImpression()`
- 条件付き依存: `if (content.type === TYPES.UNIVERSAL)` → `InfoBar._universalInfobars.push()`
- 参照: `InfoBar._activeInfobar?.notification`, `InfoBar._universalInfobars.length`, `TYPES.GLOBAL`, `TYPES.UNIVERSAL`, `browser.documentGlobal`, `browser.documentGlobal.gNotificationBox`, `content.attributes`, `content.dismissable`, `content.icon`, `content.priority`, `content.style`, `content.text`, `content.type`, `gBrowser.ownerDocument`, `notificationContainer.PRIORITY_SYSTEM`, `this._browser`, `this.infobarCallback`, `this.message`, `this.message.content.dismiss_action`, `this.message.id`, `this.notification`

## InfoBarNotification._createLinkNode()
- 位置: L254-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.addEventListener()`, `doc.createElement()`, `e.preventDefault()`, `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if (string_id)` → `lazy.RemoteL10n.createElement()`
- 条件付き依存: `if (string_id)` → `a.appendChild()`
- 参照: `a.href`, `a.textContent`

## InfoBarNotification.formatMessageConfig()
- 位置: async L289-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `doc.createDocumentFragment()`
- 条件付き依存: `if (part.href)` → `frag.appendChild()`
- 条件付き依存: `if (part.href)` → `this._createLinkNode()`
- 条件付き依存: `if (part.string_id)` → `this._buildMessageFragment()`
- 条件付き依存: `if (part.string_id)` → `frag.appendChild()`
- 条件付き依存: `if (typeof part === "string")` → `frag.appendChild()`
- 条件付き依存: `if (typeof part === "string")` → `doc.createTextNode()`
- 条件付き依存: `if (part.raw && typeof part.raw === "string")` → `frag.appendChild()`
- 条件付き依存: `if (part.raw && typeof part.raw === "string")` → `doc.createTextNode()`
- 参照: `part.args`, `part.href`, `part.raw`, `part.string_id`

## InfoBarNotification.formatButtonConfig()
- 位置: L333-342
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `button.label.string_id`, `this.buttonCallback`

## InfoBarNotification.handleImpressionAction()
- 位置: L344-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_IMPRESSION_ACTIONS.includes()`, `actions.forEach()`, `console.error()`, `lazy.SpecialMessageActions.handleAction()`
- 参照: `data.onImpression`, `impressionAction.data.actions`, `impressionAction.type`, `lazy.ASRouter.state`, `messageImpressions[this.message.id]?.length`, `this.message.content.impression_action`, `this.message.id`

## InfoBarNotification.addImpression()
- 位置: L373-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dispatch()`, `this.sendUserEventTelemetry()`
- 条件付き依存: `if (this.message.content.impression_action)` → `this.handleImpressionAction()`
- 参照: `this.message`, `this.message.content.impression_action`

## InfoBarNotification.buttonCallback()
- 位置: L395-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.classList.contains()`, `this.dispatchUserAction()`, `this.sendUserEventTelemetry()`
- 参照: `btnDescription.action`, `btnDescription.action?.dismiss`, `btnDescription.id`, `btnDescription.index`, `target.documentGlobal.gBrowser.selectedBrowser`

## InfoBarNotification.dispatchUserAction()
- 位置: L412-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dispatch()`

## InfoBarNotification.infobarCallback()
- 位置: L423-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._removePrefObserver()`
- 条件付き依存: `if (this.notification)` → `this.sendUserEventTelemetry()`
- 条件付き依存: `if (eventType === "dismissed" && this.message.content.dismiss_action)` → `this.dispatchUserAction()`
- 条件付き依存: `if (wasUniversal && isActiveMessage && InfoBar._universalInfobars.length)` → `this.removeUniversalInfobars()`
- 参照: `InfoBar._activeInfobar`, `InfoBar._activeInfobar?.notification`, `InfoBar._universalInfobars.length`, `TYPES.UNIVERSAL`, `this._browser`, `this.message.content.dismiss_action`, `this.message.content.type`, `this.notification`

## InfoBarNotification._maybeAttachPrefObserver()
- 位置: L468-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.prefs.addObserver()`, `console.error()`
- 参照: `this._dismissPrefs`, `this._dismissPrefs?.length`, `this._prefObserver`
- XPCOM: `Services.prefs`

## observe()
- 位置: L478-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dismissPrefs.includes()`
- 条件付き依存: `if (topic === "nsPref:changed" && this._dismissPrefs.includes(data))` → `this.notification?.dismiss()`
- 条件付き依存: `if (topic === "nsPref:changed" && this._dismissPrefs.includes(data))` → `console.error()`

## InfoBarNotification._removePrefObserver()
- 位置: L503-515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- 参照: `this._dismissPrefs`, `this._dismissPrefs?.length`, `this._prefObserver`
- XPCOM: `Services.prefs`

## InfoBarNotification.removeUniversalInfobars()
- 位置: L522-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InfoBar._universalInfobars.forEach()`, `console.error()`
- 条件付き依存: `if (InfoBar._observingWindowOpened)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (box && notification)` → `box.removeNotification()`
- 参照: `InfoBar._activeInfobar`, `InfoBar._activeInfobar?.notification`, `InfoBar._observingWindowOpened`, `InfoBar._universalInfobars`
- XPCOM: `Services.obs`

## InfoBarNotification.sendUserEventTelemetry()
- 位置: L551-561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dispatch()`
- 参照: `this.message.id`

## maybeLoadCustomElement()
- 位置: L569-576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.customElements.get()`
- 条件付き依存: `if (!win.customElements.get("remote-text"))` → `Services.scriptloader.loadSubScript()`
- XPCOM: `Services.scriptloader`

## maybeInsertFTL()
- 位置: L578-580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FTL_FILES.forEach()`, `win.MozXULElement.insertFTLIfNeeded()`

## isValidInfobarWindow()
- 位置: L588-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.document.documentElement.hasAttribute()`
- 参照: `win.closed`, `win.toolbar?.visible`

## showNotificationAllWindows()
- 位置: async L614-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `notification.showNotification()`, `this.isValidInfobarWindow()`, `this.maybeInsertFTL()`, `this.maybeLoadCustomElement()`
- 条件付き依存: `if (this._activeInfobar?.notification === notification)` → `this._showWhenLoaded()`
- 参照: `this._activeInfobar`, `this._activeInfobar?.notification`, `win.document?.readyState`, `win.gBrowser`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## _showWhenLoaded()
- 位置: L642-665
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (win.document?.readyState === "complete")` → `onWindowReady()`
- 条件付き依存: `if (!(win.document?.readyState === "complete"))` → `win.addEventListener()`
- 参照: `win.document?.readyState`

## onWindowReady()
- 位置: L643-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showInfoBarMessage()`
- 参照: `InfoBar._activeInfobar?.notification`, `win.closed`, `win.gBrowser`, `win.gBrowser.selectedBrowser`

## _maybeReplaceActiveInfoBar()
- 位置: L667-688
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `replacementEligible.includes()`
- 条件付き依存: `if (activeType === TYPES.UNIVERSAL)` → `this._activeInfobar.notification?.removeUniversalInfobars()`
- 条件付き依存: `if (!(activeType === TYPES.UNIVERSAL))` → `this._activeInfobar.notification?.notification.dismiss()`
- 条件付き依存: `if (!(activeType === TYPES.UNIVERSAL))` → `console.error()`
- 参照: `TYPES.UNIVERSAL`, `nextMessage?.content?.canReplace`, `this._activeInfobar`, `this._activeInfobar.message?.content?.type`, `this._activeInfobar.message?.id`

## showInfoBarMessage()
- 位置: async L702-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isValidInfobarWindow()`, `this.maybeInsertFTL()`, `this.maybeLoadCustomElement()`
- 条件付き依存: `if (this._activeInfobar && !universalInNewWin)` → `this._maybeReplaceActiveInfoBar()`
- 条件付き依存: `if (isFirstUniversal)` → `this.showNotificationAllWindows()`
- 条件付き依存: `if (!this._observingWindowOpened)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!(!this._observingWindowOpened))` → `console.warn()`
- 条件付き依存: `if (!(isFirstUniversal))` → `notification.showNotification()`
- 条件付き依存: `if (isUniversal)` → `notification.removeUniversalInfobars()`
- 条件付き依存: `if (!universalInNewWin)` → `win.addEventListener()`
- 条件付き依存: `if (!universalInNewWin)` → `InfoBar._universalInfobars.filter()`
- 条件付き依存: `if (!universalInNewWin)` → `InfoBar._universalInfobars.some()`
- 参照: `InfoBar._activeInfobar`, `InfoBar._activeInfobar?.notification`, `InfoBar._universalInfobars`, `TYPES.UNIVERSAL`, `browser?.documentGlobal`, `entry.win`, `entry.win.closed`, `message.content.type`, `this._activeInfobar`, `this._activeInfobar?.notification`, `this._observingWindowOpened`
- XPCOM: `Services.obs`

## observe()
- 位置: L804-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._showWhenLoaded()`, `this.isValidInfobarWindow()`
- 参照: `TYPES.UNIVERSAL`, `active?.message?.content.type`, `this._activeInfobar`
