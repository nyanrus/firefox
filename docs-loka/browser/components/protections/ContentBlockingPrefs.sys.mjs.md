# browser/components/protections/ContentBlockingPrefs.sys.mjs

source: browser/components/protections/ContentBlockingPrefs.sys.mjs
source-hash: 4b709b747631e586e5516b06532b20bcdb08effd
lines: 547

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## applyCategoryPref()
- 位置: L42-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `console.error()`
- 参照: `Ci.nsIBounceTrackingProtection.MODE_ENABLED`, `Ci.nsIBounceTrackingProtection.MODE_ENABLED_DRY_RUN`, `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `this.CATEGORY_PREFS`, `this.PREF_LNA_ETP_ENABLED`
- XPCOM: [`nsIBounceTrackingProtection`](../../../toolkit/components/antitracking/bouncetrackingprotection/nsIBounceTrackingProtection.idl.md) / [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / `Services.prefs`

## setPrefExpectations()
- 位置: L272-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs .getStringPref()`, `Services.prefs .getStringPref(this.PREF_STRICT_DEF) .split()`, `this.applyCategoryPref()`
- 参照: `this.CATEGORY_PREFS`, `this.PREF_ALLOW_LIST_BASELINE`, `this.PREF_ALLOW_LIST_CONVENIENCE`, `this.PREF_STRICT_DEF`
- XPCOM: `Services.prefs`

## prefsMatch()
- 位置: L346-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (value == null)` → `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (!(value == null))` → `Services.prefs.getPrefType()`
- 条件付き依存: `if (!(value == null))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(value == null))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (!(value == null))` → `Services.prefs.getStringPref()`
- 参照: `Services.prefs.PREF_BOOL`, `Services.prefs.PREF_INT`, `Services.prefs.PREF_STRING`, `this.CATEGORY_PREFS`, `this.PREF_ALLOW_LIST_BASELINE`, `this.PREF_ALLOW_LIST_CONVENIENCE`, `this.PREF_CB_CATEGORY`
- XPCOM: `Services.prefs`

## matchCBCategory()
- 位置: L384-411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`, `this.prefsMatch()`
- 条件付き依存: `if (this.prefsMatch("standard"))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(this.prefsMatch("standard")))` → `this.prefsMatch()`
- 条件付き依存: `if (this.prefsMatch("strict"))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(this.prefsMatch("strict")))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if ( policy && ((policy.EnableTrackingProtection && !policy.EnableTrackingProtection.Category) || policy.Cookies) )` → `Services.prefs.setStringPref()`
- 参照: `policy.Cookies`, `policy.EnableTrackingProtection`, `policy.EnableTrackingProtection.Category`, `this.PREF_CB_CATEGORY`, `this.switchingCategory`
- XPCOM: `Services.policies` / `Services.prefs`

## updateCBCategory()
- 位置: L413-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `Services.prefs.prefHasUserValue()`, `this.setPrefsToCategory()`
- 参照: `this.PREF_CB_CATEGORY`, `this.switchingCategory`
- XPCOM: `Services.prefs`

## setPrefsToCategory()
- 位置: L436-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBranch()`, `Services.prefs.getDefaultBranch()`, `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (value == null)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!(value == null))` → `Services.prefs.getPrefType()`
- 条件付き依存: `if (!(value == null))` → `prefBranch.setBoolPref()`
- 条件付き依存: `if (!(value == null))` → `prefBranch.setIntPref()`
- 条件付き依存: `if (!(value == null))` → `prefBranch.setStringPref()`
- 条件付き依存: `if (lockPrefs)` → `Services.prefs.lockPref()`
- 参照: `Services.prefs.PREF_BOOL`, `Services.prefs.PREF_INT`, `Services.prefs.PREF_STRING`, `this.CATEGORY_PREFS`, `this.PREF_ALLOW_LIST_BASELINE`, `this.PREF_ALLOW_LIST_CONVENIENCE`
- XPCOM: `Services.prefs`

## setPrefExpectationsAndUpdate()
- 位置: L480-483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setPrefExpectations()`, `this.updateCBCategory()`

## observe()
- 位置: L485-517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PREFS_CHANGING_CATEGORY.has()`, `data.startsWith()`
- 条件付き依存: `if ( data.startsWith("privacy.trackingprotection") || PREFS_CHANGING_CATEGORY.has(data) )` → `this.matchCBCategory()`
- 条件付き依存: `if (data.startsWith("privacy.trackingprotection"))` → `this.setPrefExpectations()`
- 条件付き依存: `if (data == this.PREF_CB_CATEGORY)` → `this.updateCBCategory()`
- 条件付き依存: `if (data == "browser.contentblocking.features.strict")` → `this.setPrefExpectationsAndUpdate()`
- 条件付き依存: `if (data == this.PREF_LNA_ETP_ENABLED)` → `this.setPrefExpectationsAndUpdate()`
- 参照: `this.PREF_CB_CATEGORY`, `this.PREF_LNA_ETP_ENABLED`

## init()
- 位置: L519-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `this.matchCBCategory()`, `this.setPrefExpectationsAndUpdate()`
- XPCOM: `Services.prefs`

## uninit()
- 位置: L528-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`
