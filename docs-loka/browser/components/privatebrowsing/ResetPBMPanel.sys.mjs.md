# browser/components/privatebrowsing/ResetPBMPanel.sys.mjs

source: browser/components/privatebrowsing/ResetPBMPanel.sys.mjs
source-hash: 324ea950595613ae87d642248a67e025d39bf769
lines: 279

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ResetPBMPanel.init.bind()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## init()
- 位置: L36-58
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._enabled)` → `lazy.CustomizableUI.createWidget()`
- 条件付き依存: `if (!(this._enabled))` → `lazy.CustomizableUI.destroyWidget()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `this._enabled`, `this._widgetConfig`, `this._widgetConfig.id`

## onViewShowing()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ResetPBMPanel.onViewShowing()`

## onViewHiding()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ResetPBMPanel.onViewHiding()`

## onViewShowing()
- 位置: async L64-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privateBrowsingResetPbm.confirmPanel.record()`, `panelview.addEventListener()`, `this._rememberCheck()`
- 条件付き依存: `if (!this._shouldConfirmClear)` → `event.preventDefault()`
- 条件付き依存: `if (!this._shouldConfirmClear)` → `lazy.CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (!this._shouldConfirmClear)` → `this._restartPBM()`
- 条件付き依存: `if (!this._shouldConfirmClear)` → `Glean.privateBrowsingResetPbm.resetAction.record()`
- 参照: `event.target`, `panelview.documentGlobal`, `this._rememberCheck(triggeringWindow).checked`, `this._shouldConfirmClear`

## onViewHiding()
- 位置: L95-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelview.removeEventListener()`
- 参照: `event.target`

## handleEvent()
- 位置: L100-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onCancel()`, `this.onConfirm()`
- 参照: `button.id`, `event.target`

## onCancel()
- 位置: L117-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privateBrowsingResetPbm.confirmPanel.record()`, `lazy.CustomizableUI.hidePanelForNode()`
- 参照: `this._enabled`

## onConfirm()
- 位置: async L135-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privateBrowsingResetPbm.confirmPanel.record()`, `Glean.privateBrowsingResetPbm.resetAction.record()`, `Services.prefs.setBoolPref()`, `lazy.CustomizableUI.hidePanelForNode()`, `this._rememberCheck()`, `this._restartPBM()`
- 参照: `button.documentGlobal`, `this._enabled`, `this._rememberCheck(triggeringWindow).checked`
- XPCOM: `Services.prefs`

## _restartPBM()
- 位置: async L172-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clearData.clearPrivateBrowsingData()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `Services.ww.getWindowEnumerator()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SessionStore.purgeDataForPrivateWindow()`, `this._toolbarButton()`, `toolbarButton.getAttribute()`, `triggeringWindow.ConfirmationHint.show()`, `triggeringWindow.SidebarController?.hide()`, `triggeringWindow.gBrowser.addTab()`, `triggeringWindow.gBrowser.removeAllTabsBut()`
- 条件付き依存: `if ( w != triggeringWindow && lazy.PrivateBrowsingUtils.isWindowPrivate(w) )` → `w.closeWindow()`
- 条件付き依存: `if (anchorID)` → `triggeringWindow.document.getElementById()`
- 参照: `triggeringWindow.BROWSER_NEW_TAB_URL`
- XPCOM: `Services.clearData` / `Services.scriptSecurityManager` / `Services.ww`

## onDataDeleted()
- 位置: L227-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`
- 条件付き依存: `if (aFailedFlags)` → `console.error()`

## _toolbarButton()
- 位置: L255-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getWidget()`, `lazy.CustomizableUI.getWidget(this._widgetConfig.id).forWindow()`
- 参照: `lazy.CustomizableUI.getWidget(this._widgetConfig.id).forWindow(win) .node`, `this._widgetConfig.id`

## _rememberCheck()
- 位置: L260-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.document.getElementById()`
