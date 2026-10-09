# browser/components/ipprotection/IPPL10nHelper.sys.mjs

source: browser/components/ipprotection/IPPL10nHelper.sys.mjs
source-hash: fc6670193f7ecd9128ca8c17f38a4e0e5a218d10
lines: 85

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## IPPL10nHelperSingleton.init()
- 位置: L33-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPProtectionService.addEventListener()`

## IPPL10nHelperSingleton.initOnStartupCompleted()
- 位置: L40-40
- 役割: (未記入)
- 触るとき: (未記入)

## IPPL10nHelperSingleton.uninit()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPProtectionService.removeEventListener()`

## IPPL10nHelperSingleton.handleEvent()
- 位置: L49-57
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( state !== lazy.IPProtectionStates.UNINITIALIZED && state !== lazy.IPProtectionStates.UNAVAILABLE )` → `Services.prefs.setBoolPref()`
- 参照: `lazy.IPProtectionService.state`, `lazy.IPProtectionStates.UNAVAILABLE`, `lazy.IPProtectionStates.UNINITIALIZED`
- XPCOM: `Services.prefs`

## IPPL10nHelperSingleton.hidesFeature()
- 位置: L59-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.locale.isLocalizedEnough()`, `Services.prefs.getIntPref()`, `parseInt()`
- 条件付き依存: `if (!gateVersion)` → `Services.prefs.setIntPref()`
- 参照: `AppConstants.MOZ_APP_VERSION`
- XPCOM: `Services.locale` / `Services.prefs`
