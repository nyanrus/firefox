# browser/components/ipprotection/IPProtectionInfobarManager.sys.mjs

source: browser/components/ipprotection/IPProtectionInfobarManager.sys.mjs
source-hash: e144468cb0e8f16c0704cf88c776a5143143d411
lines: 331

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## IPProtectionInfobarManagerClass.initialized()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#initialized`

## IPProtectionInfobarManagerClass.init()
- 位置: L55-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.wm.addListener()`, `lazy.IPPProxyManager.addEventListener()`, `lazy.IPProtectionService.addEventListener()`, `this.#handlePrefChange.bind()`
- 参照: `lazy.BANDWIDTH_USAGE_ENABLED`, `this.#initialized`, `this.#prefObserver`, `this.#windowListener`
- XPCOM: `Services.prefs` / `Services.wm`

## onOpenWindow()
- 位置: L67-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.addEventListener()`, `win.document.documentElement.getAttribute()`
- 条件付き依存: `if (this.#lastThreshold && this.#lastUsage)` → `this.#showInfobar()`
- 参照: `this.#lastThreshold`, `this.#lastUsage`, `xulWindow.docShell.domWindow`

## IPProtectionInfobarManagerClass.uninit()
- 位置: L97-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `Services.wm.removeListener()`, `lazy.IPPProxyManager.removeEventListener()`, `lazy.IPProtectionService.removeEventListener()`, `this.hideInfobars()`
- 参照: `this.#initialized`, `this.#lastThreshold`, `this.#lastUsage`, `this.#prefObserver`, `this.#windowListener`
- XPCOM: `Services.prefs` / `Services.wm`

## IPProtectionInfobarManagerClass.#handlePrefChange()
- 位置: L127-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPUsageHelper.getDismissedThresholds()`
- 条件付き依存: `if (infobar >= 75)` → `this.#hideInfobar()`
- 条件付き依存: `if (infobar >= 90)` → `this.#hideInfobar()`

## IPProtectionInfobarManagerClass.handleEvent()
- 位置: L140-193
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.type === "IPProtectionService:StateChanged" && lazy.IPProtectionService.state !== lazy.IPProtectionStates.READY )` → `this.#hideInfobar()`
- 条件付き依存: `if (event.type === "IPPProxyManager:UsageChanged")` → `Number()`
- 条件付き依存: `if (remainingPercent === 0 || remainingPercent > 0.25)` → `lazy.IPPUsageHelper.setDismissedThresholds()`
- 条件付き依存: `if (remainingPercent === 0 || remainingPercent > 0.25)` → `this.#hideInfobar()`
- 条件付き依存: `if (remainingPercent <= 0.1)` → `this.#showInfobar()`
- 条件付き依存: `if (remainingPercent > 0.1 && remainingPercent <= 0.25)` → `this.#showInfobar()`
- 参照: `event.detail.usage`, `event.type`, `lazy.IPProtectionService.state`, `lazy.IPProtectionStates.READY`, `this.#lastThreshold`, `this.#lastUsage`, `usage.max`, `usage.remaining`, `usage.reset`

## IPProtectionInfobarManagerClass.hideInfobars()
- 位置: L203-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hideInfobar()`
- 条件付き依存: `if (triggeredByPanel && this.#lastThreshold)` → `lazy.IPPUsageHelper.getDismissedThresholds()`
- 条件付き依存: `if (this.#lastThreshold > current.infobar)` → `lazy.IPPUsageHelper.setDismissedThresholds()`
- 参照: `current.infobar`, `this.#lastThreshold`, `this.#lastUsage`

## IPProtectionInfobarManagerClass.#hideInfobar()
- 位置: L224-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `win.gNotificationBox.getNotificationWithValue()`
- 条件付き依存: `if (notification)` → `win.gNotificationBox.removeNotification()`
- 参照: `win.closed`
- XPCOM: `Services.wm`

## IPProtectionInfobarManagerClass.#showInfobar()
- 位置: L248-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `Services.wm.getEnumerator()`, `Services.wm.getMostRecentWindow()`, `formatRemainingBandwidth()`, `lazy.IPPUsageHelper.getDismissedThresholds()`, `lazy.IPProtection.getPanel()`, `win.gNotificationBox.appendNotification()`, `win.gNotificationBox.getNotificationWithValue()`
- 条件付き依存: `if (!useGB && threshold === 90)` → `String()`
- 条件付き依存: `if (!(!useGB && threshold === 90))` → `String()`
- 参照: `lazy.IPPUsageHelper.getDismissedThresholds().infobar`, `openWin.closed`, `panel.state.bandwidthWarning`, `panel?.active`, `usage.remaining`, `win.closed`, `win.gNotificationBox.PRIORITY_WARNING_HIGH`
- XPCOM: `Services.wm`

## eventCallback()
- 位置: L310-320
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event === "dismissed")` → `lazy.IPPUsageHelper.getDismissedThresholds()`
- 条件付き依存: `if (threshold > current.infobar)` → `lazy.IPPUsageHelper.setDismissedThresholds()`
- 参照: `current.infobar`
