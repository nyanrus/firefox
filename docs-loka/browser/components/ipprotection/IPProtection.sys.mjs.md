# browser/components/ipprotection/IPProtection.sys.mjs

source: browser/components/ipprotection/IPProtection.sys.mjs
source-hash: 50948e3c7e826fdafe222ada4a8f826076795440
lines: 368

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## IPProtectionWidget.constructor()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sendReadyTrigger.bind()`
- 参照: `this.sendReadyTrigger`

## IPProtectionWidget.init()
- 位置: L54-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.addListener()`
- 条件付き依存: `if (!this.created)` → `this.#createWidget()`
- 参照: `this.#inited`, `this.created`

## IPProtectionWidget.uninit()
- 位置: L70-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.removeListener()`, `this.#destroyWidget()`, `this.#uninitPanels()`
- 参照: `this.#inited`

## IPProtectionWidget.isInitialized()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#inited`

## IPProtectionWidget.#createWidget()
- 位置: L92-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.createWidget()`, `this.#onBeforeCreated.bind()`, `this.#onCreated.bind()`, `this.#onDestroyed.bind()`, `this.#onViewHiding.bind()`, `this.#onViewShowing.bind()`, `this.#placeWidget()`
- 参照: `IPProtectionWidget.PANEL_ID`, `IPProtectionWidget.WIDGET_ID`, `this.created`

## IPProtectionWidget.#placeWidget()
- 位置: L120-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`, `lazy.CustomizableUI.addWidgetToArea()`, `lazy.CustomizableUI.getPlacementOfWidget()`
- 参照: `IPProtectionWidget.ADDED_PREF`, `IPProtectionWidget.WIDGET_ID`, `lazy.CustomizableUI.AREA_NAVBAR`, `prevWidget.position`
- XPCOM: `Services.prefs`

## IPProtectionWidget.#destroyWidget()
- 位置: L153-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.destroyWidget()`, `this.#destroyPanels()`
- 条件付き依存: `if (this.readyTriggerIdleCallback)` → `lazy.cancelIdleCallback()`
- 参照: `IPProtectionWidget.WIDGET_ID`, `this.created`, `this.readyTriggerIdleCallback`

## IPProtectionWidget.getPanel()
- 位置: L171-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panels.get()`, `this.#panels.has()`
- 条件付き依存: `if (!this.#panels.has(window))` → `this.#panels.set()`
- 参照: `lazy.IPProtectionPanel`, `this.created`, `window?.PanelUI`

## IPProtectionWidget.getToolbarButton()
- 位置: L195-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#toolbarButtons.get()`
- 参照: `this.created`

## IPProtectionWidget.#destroyPanels()
- 位置: L209-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`, `this.#panels.get()`, `this.#panels.get(panel).destroy()`
- 参照: `this.#panels`

## IPProtectionWidget.#uninitPanels()
- 位置: L219-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`, `this.#panels.get()`, `this.#panels.get(panel).uninit()`, `this.#toolbarButtons.get()`, `this.#toolbarButtons.get(toolbarButton).uninit()`
- 参照: `this.#panels`, `this.#toolbarButtons`

## IPProtectionWidget.#onViewShowing()
- 位置: L241-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panels.has()`
- 条件付き依存: `if (this.#panels.has(documentGlobal))` → `this.#panels.get()`
- 条件付き依存: `if (this.#panels.has(documentGlobal))` → `panel.showing()`
- 参照: `event.target`

## IPProtectionWidget.#onViewHiding()
- 位置: L254-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panels.has()`
- 条件付き依存: `if (this.#panels.has(documentGlobal))` → `this.#panels.get()`
- 条件付き依存: `if (this.#panels.has(documentGlobal))` → `panel.hiding()`
- 参照: `event.target`

## IPProtectionWidget.#onBeforeCreated()
- 位置: L267-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panels.has()`
- 条件付き依存: `if (documentGlobal && !this.#panels.has(documentGlobal))` → `this.#panels.set()`
- 参照: `lazy.IPProtectionPanel`

## IPProtectionWidget.#onCreated()
- 位置: L281-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.addEventListener()`, `lazy.IPProtectionService.addEventListener()`, `lazy.requestIdleCallback()`, `this.#toolbarButtons.has()`
- 条件付き依存: `if (window && !this.#toolbarButtons.has(window))` → `this.#toolbarButtons.set()`
- 参照: `IPProtectionWidget.WIDGET_ID`, `lazy.IPProtectionToolbarButton`, `this.handleEvent`, `this.readyTriggerIdleCallback`, `this.sendReadyTrigger`, `toolbaritem.documentGlobal`

## IPProtectionWidget.#onDestroyed()
- 位置: L306-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.removeEventListener()`, `lazy.IPProtectionService.removeEventListener()`
- 参照: `this.handleEvent`

## IPProtectionWidget.onWindowClosed()
- 位置: L322-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panels.has()`, `this.#toolbarButtons.has()`
- 条件付き依存: `if (this.#panels.has(window))` → `this.#panels.get(window).uninit()`
- 条件付き依存: `if (this.#panels.has(window))` → `this.#panels.get()`
- 条件付き依存: `if (this.#panels.has(window))` → `this.#panels.delete()`
- 条件付き依存: `if (this.#toolbarButtons.has(window))` → `this.#toolbarButtons.get(window).uninit()`
- 条件付き依存: `if (this.#toolbarButtons.has(window))` → `this.#toolbarButtons.get()`
- 条件付き依存: `if (this.#toolbarButtons.has(window))` → `this.#toolbarButtons.delete()`

## IPProtectionWidget.onWidgetRemoved()
- 位置: async L333-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (!moved)` → `Glean.ipprotection.removedFromToolbar.record()`
- 条件付き依存: `if (!moved)` → `lazy.IPPProxyManager.stop()`
- 条件付き依存: `if (!moved)` → `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 条件付き依存: `if (!moved)` → `this.#toolbarButtons.get(win)?.updateState()`
- 条件付き依存: `if (!moved)` → `this.#toolbarButtons.get()`
- 参照: `IPProtectionWidget.WIDGET_ID`, `this.#toolbarButtons`

## IPProtectionWidget.#sendReadyTrigger()
- 位置: async L354-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `lazy.ASRouter.sendTriggerMessage()`
- 参照: `lazy.ASRouter.waitForInitialized`, `win?.gBrowser?.selectedBrowser`
- XPCOM: `Services.wm`
