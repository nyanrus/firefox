# browser/components/ipprotection/IPPOnboardingMessageHelper.sys.mjs

source: browser/components/ipprotection/IPPOnboardingMessageHelper.sys.mjs
source-hash: da4a1f828646ccffb2242c14828dd70bc171071d
lines: 121

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## IPPOnboardingMessageHelper.constructor()
- 位置: L30-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.getAllByTypes()`, `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `this.#handleEvent.bind()`
- 条件付き依存: `if (savedSites.length)` → `this.setOnboardingFlag()`
- 条件付き依存: `if (!(savedSites.length))` → `Services.obs.addObserver()`
- 条件付き依存: `if (autoStartPref)` → `this.setOnboardingFlag()`
- 参照: `ONBOARDING_PREF_FLAGS.EVER_TURNED_ON_AUTOSTART`, `ONBOARDING_PREF_FLAGS.EVER_USED_SITE_EXCEPTIONS`, `savedSites.length`, `this.#autostartPrefObserver`, `this.#observingPermChanges`, `this.handleEvent`
- XPCOM: `Services.obs` / `Services.perms` / `Services.prefs`

## this.#autostartPrefObserver()
- 位置: L42-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setOnboardingFlag()`
- 参照: `ONBOARDING_PREF_FLAGS.EVER_TURNED_ON_AUTOSTART`

## IPPOnboardingMessageHelper.init()
- 位置: L52-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.addEventListener()`
- 参照: `this.handleEvent`

## IPPOnboardingMessageHelper.initOnStartupCompleted()
- 位置: L59-59
- 役割: (未記入)
- 触るとき: (未記入)

## IPPOnboardingMessageHelper.uninit()
- 位置: L61-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.removeEventListener()`
- 条件付き依存: `if (this.#observingPermChanges)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#autostartPrefObserver)` → `Services.prefs.removeObserver()`
- 参照: `this.#autostartPrefObserver`, `this.#observingPermChanges`, `this.handleEvent`
- XPCOM: `Services.obs` / `Services.prefs`

## IPPOnboardingMessageHelper.observe()
- 位置: L81-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `subject.QueryInterface()`
- 条件付き依存: `if ( topic === "perm-changed" && permission.type === PERM_NAME && data === "added" )` → `this.setOnboardingFlag()`
- 参照: `Ci.nsIPermission`, `ONBOARDING_PREF_FLAGS.EVER_USED_SITE_EXCEPTIONS`, `permission.type`
- XPCOM: [`nsIPermission`](../../../netwerk/base/nsIPermission.idl.md)

## IPPOnboardingMessageHelper.readPrefMask()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## IPPOnboardingMessageHelper.writeOnboardingTriggerPref()
- 位置: L99-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## IPPOnboardingMessageHelper.setOnboardingFlag()
- 位置: L103-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.readPrefMask()`, `this.writeOnboardingTriggerPref()`

## IPPOnboardingMessageHelper.#handleEvent()
- 位置: L108-115
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.type == "IPPProxyManager:StateChanged" && lazy.IPPProxyManager.state === lazy.IPPProxyStates.ACTIVE )` → `this.setOnboardingFlag()`
- 参照: `ONBOARDING_PREF_FLAGS.EVER_TURNED_ON_VPN`, `event.type`, `lazy.IPPProxyManager.state`, `lazy.IPPProxyStates.ACTIVE`
