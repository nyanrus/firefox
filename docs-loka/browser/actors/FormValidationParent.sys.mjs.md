# browser/actors/FormValidationParent.sys.mjs

source: browser/actors/FormValidationParent.sys.mjs
source-hash: 2eca818bc761b4a0a83e2458768a4dfca938617b
lines: 211

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## PopupShownObserver.constructor()
- 位置: L18-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`
- 参照: `this._weakContext`

## PopupShownObserver.observe()
- 位置: L22-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctxt.currentWindowGlobal?.getExistingActor()`, `this._weakContext.get()`
- 条件付き依存: `if (!actor)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (topic == "popup-shown" && subject != actor._panel)` → `actor._hidePopup()`
- 参照: `actor._panel`
- XPCOM: `Services.obs`

## FormValidationParent.constructor()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._obs`, `this._panel`

## FormValidationParent.hasOpenPopups()
- 位置: L49-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.document.querySelectorAll()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`

## FormValidationParent.uninit()
- 位置: L69-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._obs`, `this._panel`

## FormValidationParent.hidePopup()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hidePopup()`

## FormValidationParent.receiveMessage()
- 位置: L82-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormValidationParent.hasOpenPopups()`, `this._hidePopup()`, `this._showPopup()`
- 参照: `aMessage.data`, `aMessage.name`, `browser.documentGlobal`, `tabBrowser.selectedBrowser`, `this._panel`, `this.browsingContext.top.embedderElement`, `window.gBrowser`

## FormValidationParent.handleEvent()
- 位置: L113-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hidePopup()`, `this._onPopupHidden()`
- 参照: `aEvent.type`

## FormValidationParent._onPopupHidden()
- 位置: L130-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `aEvent.originalTarget.removeEventListener()`, `tabBrowser.selectedBrowser.removeEventListener()`
- 参照: `aEvent.originalTarget.documentGlobal.gBrowser`, `this._obs`, `this._panel`
- XPCOM: `Services.obs`

## FormValidationParent._showPopup()
- 位置: L153-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `aBrowser.addEventListener()`, `aBrowser.constrainPopup()`, `this._getAndMaybeCreatePanel()`, `this._panel.addEventListener()`, `this._panel.openPopupAtScreenRect()`
- 参照: `aPanelData.message`, `aPanelData.position`, `aPanelData.screenRect`, `rect.height`, `rect.left`, `rect.top`, `rect.width`, `this._obs`, `this._panel`, `this._panel.firstChild.textContent`, `this.browsingContext`
- XPCOM: `Services.obs`

## FormValidationParent._hidePopup()
- 位置: L192-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._panel?.hidePopup()`

## FormValidationParent._getAndMaybeCreatePanel()
- 位置: L196-209
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._panel)` → `window.document.getElementById()`
- 条件付き依存: `if (template)` → `template.replaceWith()`
- 参照: `browser.documentGlobal`, `template.content`, `this._panel`, `this.browsingContext.top.embedderElement`
