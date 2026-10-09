# browser/components/aiwindow/ui/modules/AIWindowAccountAuth.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowAccountAuth.sys.mjs
source-hash: 48965846125c33dd3d9b848964d20f45d3f9e0f6
lines: 158

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## hasToSConsent()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.hasAIWindowToSConsent`

## hasToSConsent()
- 位置: L52-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## isSignedIn()
- 位置: async L61-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.fxAccounts.getSignedInUser()`, `lazy.log.error()`

## canAccessAIWindow()
- 位置: async L71-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isSignedIn()`
- 参照: `this.hasToSConsent`

## denialReason()
- 位置: L85-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.hasToSConsent`

## promptSignIn()
- 位置: async L102-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.signinFlowCompleted.record()`, `Glean.smartWindow.signinFlowStarted.record()`, `lazy.FxAccounts.canConnectAccount()`, `lazy.SpecialMessageActions.fxaSignInFlow()`, `lazy.log.error()`, `this.denialReason()`, `this.isSignedIn()`
- 参照: `lazy.hasFirstrunCompleted`, `this.hasToSConsent`

## ensureAIWindowAccess()
- 位置: async L142-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isSignedIn()`, `this.promptSignIn()`
- 条件付き依存: `if (!(await this.promptSignIn(browser, signedIn)))` → `lazy.log.error()`
- 参照: `this.hasToSConsent`
