# browser/components/ipprotection/IPPUsageHelper.sys.mjs

source: browser/components/ipprotection/IPPUsageHelper.sys.mjs
source-hash: 5d4200372de5c0d70aab180abdb20b5b0d87bd97
lines: 218

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## IPPUsageHelperSingleton.constructor()
- 位置: L60-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.#handleEvent.bind()`
- 参照: `this.handleEvent`

## IPPUsageHelperSingleton.state()
- 位置: L68-70
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#state`

## IPPUsageHelperSingleton.init()
- 位置: L72-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IPPProxyManager.addEventListener()`, `lazy.IPProtectionService.addEventListener()`, `lazy.IPProtectionService.authProvider.addEventListener()`
- 参照: `this.handleEvent`

## IPPUsageHelperSingleton.initOnStartupCompleted()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#checkEntitlement()`

## IPPUsageHelperSingleton.uninit()
- 位置: L91-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IPPProxyManager.removeEventListener()`, `lazy.IPProtectionService.authProvider.removeEventListener()`, `lazy.IPProtectionService.removeEventListener()`, `this.#setState()`
- 参照: `UsageStates.NONE`, `this.handleEvent`

## IPPUsageHelperSingleton.#handleEvent()
- 位置: L107-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `this.#setBandwidthEnabled()`, `this.#setState()`
- 条件付き依存: `if (event.type === "IPPAuthProvider:StateChanged")` → `this.#checkEntitlement()`
- 条件付き依存: `if (lazy.IPProtectionService.state !== lazy.IPProtectionStates.READY)` → `this.#setState()`
- 条件付き依存: `if (usage.unlimited)` → `this.#setState()`
- 条件付き依存: `if (usage.max == null || usage.remaining == null)` → `this.#setState()`
- 参照: `BANDWIDTH.SECOND_THRESHOLD`, `BANDWIDTH.THIRD_THRESHOLD`, `UsageStates.NONE`, `UsageStates.UNLIMITED`, `UsageStates.WARNING_75_PERCENT`, `UsageStates.WARNING_90_PERCENT`, `event.detail`, `event.type`, `lazy.IPProtectionService.state`, `lazy.IPProtectionStates.READY`, `usage.max`, `usage.remaining`, `usage.unlimited`

## IPPUsageHelperSingleton.getDismissedThresholds()
- 位置: L156-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`
- 参照: `obj.infobar`, `obj.panel`
- XPCOM: `Services.prefs`

## IPPUsageHelperSingleton.setDismissedThresholds()
- 位置: L175-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## IPPUsageHelperSingleton.#checkEntitlement()
- 位置: L182-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setBandwidthEnabled()`
- 条件付き依存: `if (!limitedBandwidth)` → `this.#setState()`
- 条件付き依存: `if (this.#state === UsageStates.UNLIMITED)` → `this.#setState()`
- 参照: `UsageStates.NONE`, `UsageStates.UNLIMITED`, `lazy.IPProtectionService.authProvider.entitlement?.limitedBandwidth`, `this.#state`

## IPPUsageHelperSingleton.#setBandwidthEnabled()
- 位置: L194-198
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.BANDWIDTH_USAGE_ENABLED !== enabled)` → `Services.prefs.setBoolPref()`
- 参照: `lazy.BANDWIDTH_USAGE_ENABLED`
- XPCOM: `Services.prefs`

## IPPUsageHelperSingleton.#setState()
- 位置: L200-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.#state`
