# browser/components/referrals/Referrals.sys.mjs

source: browser/components/referrals/Referrals.sys.mjs
source-hash: a79477f37602cfbfc080820e913e3ce6a1592bce
lines: 108

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## ReferralsClass.maybeLockPref()
- 位置: L24-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (code.length)` → `Services.prefs.lockPref()`
- 参照: `code.length`
- XPCOM: `Services.prefs`

## ReferralsClass.isEnabled()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.REFERRALS_ENABLED`

## ReferralsClass.getReferralCode()
- 位置: L49-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `Services.prefs.lockPref()`, `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (Services.prefs.prefIsLocked(REFERRAL_CODE_PREF))` → `Services.prefs.unlockPref()`
- 条件付き依存: `if (!code)` → `this.#generateCode()`
- 条件付き依存: `if (!code)` → `Services.prefs.setStringPref()`
- 参照: `this.isEnabled`
- XPCOM: `Services.prefs`

## ReferralsClass.openReferralsTab()
- 位置: L77-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.referrals.entrypointClicked.record()`, `aboutPageURL.searchParams.set()`, `aboutPageURL.toString()`, `this.getReferralCode()`, `window.openTrustedLinkIn()`
- 参照: `this.isEnabled`

## ReferralsClass.#generateCode()
- 位置: L95-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.getRandomValues()`
- 参照: `REFERRAL_CODE_CHARSET.length`
