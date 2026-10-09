# browser/components/ipprotection/IPProtectionToolbarButton.sys.mjs

source: browser/components/ipprotection/IPProtectionToolbarButton.sys.mjs
source-hash: af6f35dd4ec42b0380d07c64554d1d583aa04953
lines: 540

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## IPProtectionToolbarButton.gBrowser()
- 位置: L86-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.get()`
- 参照: `win?.gBrowser`

## IPProtectionToolbarButton.isExceptionsFeatureEnabled()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.siteExceptionsFeaturePref`

## IPProtectionToolbarButton.isInclusionsFeatureEnabled()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.siteInclusionsFeaturePref`

## IPProtectionToolbarButton.isExceptionsHintsEnabled()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.siteExceptionsHintsPref`

## IPProtectionToolbarButton.toolbaritem()
- 位置: L130-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getWidget()`, `lazy.CustomizableUI.getWidget(this.#widgetId)?.forWindow()`, `this.#window.get()`
- 参照: `lazy.CustomizableUI.getWidget(this.#widgetId)?.forWindow(win).node`, `this.#widgetId`

## IPProtectionToolbarButton.constructor()
- 位置: L139-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `lazy.IPPProxyManager.addEventListener()`, `lazy.IPPSiteRuleManager.addEventListener()`, `lazy.IPProtectionService.addEventListener()`, `this.#addProgressListener()`, `this.#handleEvent.bind()`
- 条件付き依存: `if (this.gBrowser?.tabContainer)` → `this.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (toolbaritem)` → `toolbaritem.classList.add()`
- 条件付き依存: `if (toolbaritem)` → `this.updateState()`
- 参照: `this.#widgetId`, `this.#window`, `this.gBrowser?.tabContainer`, `this.handleEvent`

## IPProtectionToolbarButton.#addProgressListener()
- 位置: L171-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.gBrowser.addTabsProgressListener()`
- 参照: `this.#progressListener`, `this.gBrowser`

## onLocationChange()
- 位置: L177-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateState()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD`, `aWebProgress.isTopLevel`, `this.gBrowser?.selectedBrowser`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## IPProtectionToolbarButton.#handleEvent()
- 位置: L213-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateState()`
- 条件付き依存: `if ( event.type === "IPPProxyManager:StateChanged" && lazy.IPPProxyManager.state !== lazy.IPPProxyStates.ACTIVE )` → `this.#visitedExcludedSites.clear()`
- 参照: `event.type`, `lazy.IPPProxyManager.state`, `lazy.IPPProxyStates.ACTIVE`

## IPProtectionToolbarButton.updateState()
- 位置: L259-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSitePrincipal()`, `lazy.IPPSiteRuleManager.canManage()`, `lazy.IPPSiteRuleManager.getRule()`, `this.#updateBadge()`, `this.#window.get()`, `this.updateIconStatus()`
- 条件付き依存: `if (showConfirmationHint)` → `this.updateConfirmationHint()`
- 参照: `lazy.ERRORS.NETWORK`, `lazy.IPPPrincipalRules.EXCLUDED`, `lazy.IPPPrincipalRules.INCLUDED`, `lazy.IPPProxyManager.errorType`, `lazy.IPPProxyManager.state`, `lazy.IPPProxyStates.ACTIVE`, `lazy.IPPProxyStates.ERROR`, `lazy.IPPProxyStates.PAUSED`, `options.error`, `options.showConfirmationHint`, `options?.error`, `principal.isNullPrincipal`, `this.#previousIsExcluded`, `this.gBrowser`, `this.toolbaritem`, `win.ConfirmationHint`

## IPProtectionToolbarButton.#updateBadge()
- 位置: L336-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`, `toolbaritem.querySelector()`
- 条件付き依存: `if (!newFeatureRelease || inPalette)` → `toolbaritem.removeAttribute()`
- 条件付き依存: `if (!newFeatureRelease || inPalette)` → `badge?.classList.remove()`
- 条件付き依存: `if (!(!newFeatureRelease || inPalette))` → `toolbaritem.setAttribute()`
- 条件付き依存: `if (!(!newFeatureRelease || inPalette))` → `badge?.classList.add()`
- 参照: `this.#widgetId`, `this.toolbaritem`

## IPProtectionToolbarButton.updateConfirmationHint()
- 位置: L373-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `confirmationHint.show()`, `getSitePrincipal()`, `this.#visitedExcludedSites.add()`, `this.#visitedExcludedSites.has()`
- 参照: `IPProtectionToolbarButton.CONFIRMATION_HINT_MESSAGE_ID`, `getSitePrincipal(this.gBrowser)?.origin`, `status.isActive`, `status.isError`, `status.isExcluded`, `this.#previousIsExcluded`, `this.gBrowser`, `this.isExceptionsFeatureEnabled`, `this.isExceptionsHintsEnabled`

## IPProtectionToolbarButton.updateIconStatus()
- 位置: L420-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#buildIconLayers()`, `toolbaritem.classList.remove()`, `toolbaritem.setAttribute()`
- 条件付き依存: `if (isNetworkError)` → `toolbaritem.classList.add()`
- 条件付き依存: `if (isError)` → `toolbaritem.classList.add()`
- 条件付き依存: `if (isPaused)` → `toolbaritem.classList.add()`
- 条件付き依存: `if (isExcluded && isActive)` → `toolbaritem.classList.add()`
- 条件付き依存: `if (isIncluded && !isActive)` → `toolbaritem.classList.add()`
- 条件付き依存: `if (isActive)` → `toolbaritem.classList.add()`
- 参照: `status.isActive`, `status.isError`, `status.isExcluded`, `status.isIncluded`, `status.isNetworkError`, `status.isPaused`, `this.isExceptionsFeatureEnabled`, `this.isInclusionsFeatureEnabled`

## IPProtectionToolbarButton.#buildIconLayers()
- 位置: L484-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `icon.replaceWith()`, `layer.classList.add()`, `layer.setAttribute()`, `stack.appendChild()`, `stack.classList.add()`, `toolbaritem.querySelector()`
- 参照: `IPProtectionToolbarButton.ICON_LAYER_STATES`, `toolbaritem.ownerDocument`

## IPProtectionToolbarButton.uninit()
- 位置: L516-538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.removeEventListener()`, `lazy.IPPSiteRuleManager.removeEventListener()`, `lazy.IPProtectionService.removeEventListener()`
- 条件付き依存: `if (this.gBrowser && this.#progressListener)` → `this.gBrowser.removeTabsProgressListener()`
- 条件付き依存: `if (this.gBrowser?.tabContainer)` → `this.gBrowser.tabContainer.removeEventListener()`
- 参照: `this.#progressListener`, `this.gBrowser`, `this.gBrowser?.tabContainer`, `this.handleEvent`
