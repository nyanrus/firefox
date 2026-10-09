# browser/components/aiwindow/ui/modules/AIWindowAccountAuth.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowAccountAuth.sys.mjs
source-hash: 48965846125c33dd3d9b848964d20f45d3f9e0f6
lines: 158

## <module>
- 役割: Smart Window のアカウント認証を扱う。利用規約への同意と Firefox Accounts のサインイン状態から、Smart Window を使えるかを判定する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## hasToSConsent()
- 位置: L48-50
- 役割: 利用規約(ToS)に同意済みかを、同意時刻の pref が 0 以外かで返す。
- 触るとき: 同意済みの判定条件を変えるとき、同意状態を参照する画面の表示を調べるとき。
- 参照: `lazy.hasAIWindowToSConsent`

## hasToSConsent()
- 位置: L52-59
- 役割: 同意時刻 pref に現在時刻(秒)を書き込む。false を渡すと 0 にして同意を取り消す。
- 触るとき: 同意の保存方法を変えるとき、サインイン完了後に同意がどこで記録されるかを調べるとき。
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## isSignedIn()
- 位置: async L61-69
- 役割: FxAccounts からサインイン中ユーザーを取得し、有無を返す。取得に失敗したらエラーを記録して false を返す。
- 触るとき: サインイン判定の仕様を変えるとき、サインイン済みなのに利用できない不具合を調べるとき。
- 呼び出し先: `lazy.fxAccounts.getSignedInUser()`, `lazy.log.error()`

## canAccessAIWindow()
- 位置: async L71-76
- 役割: 同意がなければ false を返し、同意があるときだけ isSignedIn の結果を返す。
- 触るとき: Smart Window の利用可否の条件を変えるとき。同意がない場合はサインイン状態を読まない点に注意する。
- 呼び出し先: `this.isSignedIn()`
- 参照: `this.hasToSConsent`

## denialReason()
- 位置: L85-90
- 役割: 同意とサインイン状態の組み合わせから、拒否理由 none, signed_out, no_consent, both のいずれかを返す。
- 触るとき: signin_flow_started の reason の値を変えるとき、テレメトリの集計条件を確認するとき。
- 参照: `this.hasToSConsent`

## promptSignIn()
- 位置: async L102-140
- 役割: サインイン開始と完了の Glean イベントを記録し、FxAccounts のサインイン画面を開く。接続不可なら blocked、成功なら同意を保存する。
- 触るとき: サインイン導線の挙動や計測の値を変えるとき、サインインが途中で失敗または中断した場合の扱いを調べるとき。
- 呼び出し先: `Glean.smartWindow.signinFlowCompleted.record()`, `Glean.smartWindow.signinFlowStarted.record()`, `lazy.FxAccounts.canConnectAccount()`, `lazy.SpecialMessageActions.fxaSignInFlow()`, `lazy.log.error()`, `this.denialReason()`, `this.isSignedIn()`
- 参照: `lazy.hasFirstrunCompleted`, `this.hasToSConsent`

## ensureAIWindowAccess()
- 位置: async L142-156
- 役割: 同意とサインインの両方が揃っていれば true を返し、足りなければ promptSignIn でサインインを促す。
- 触るとき: 同意もサインインも揃っていないときに、どの順で誰に何を見せるかを変えるとき。
- 呼び出し先: `this.isSignedIn()`, `this.promptSignIn()`
- 条件付き依存: `if (!(await this.promptSignIn(browser, signedIn)))` → `lazy.log.error()`
- 参照: `this.hasToSConsent`
