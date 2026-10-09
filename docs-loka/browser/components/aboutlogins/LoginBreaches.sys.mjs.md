# browser/components/aboutlogins/LoginBreaches.sys.mjs

source: browser/components/aboutlogins/LoginBreaches.sys.mjs
source-hash: f1d79257f8196c2f8430c801e91e5d55e54c5790
lines: 189

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## breachAlertsData()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BreachAlertsData`, `this._cachedBreachAlertsData`

## update()
- 位置: async L37-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.getAllUserFacingLogins()`, `this.getPotentialBreachesByLoginGUID()`

## subscribeToBreachUpdates()
- 位置: L46-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.breachAlertsData.subscribe()`, `this.update()`

## getPotentialBreachesByLoginGUID()
- 位置: async L64-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.pwmgr.potentiallyBreachedPasswords.set()`, `Services.eTLD.hasRootDomain()`, `Services.io.newURI()`, `Services.logins.arePotentiallyVulnerablePasswords()`, `Services.logins.getBreachAlertDismissalsByLoginGUID()`, `Services.prefs.getStringPref()`, `breachAlertURL.searchParams.set()`, `breachesByLoginGUID.set()`, `potentiallyVulnerablePasswords.has()`, `this._breachAlertIsDismissed()`, `this._breachInvolvedPasswords()`, `this._breachWasAfterPasswordLastChanged()`
- 条件付き依存: `if (!breaches)` → `this.breachAlertsData.getAllBreaches()`
- 条件付き依存: `if (!potentiallyVulnerablePasswords.has(login.guid))` → `Services.logins.addPotentiallyVulnerablePassword()`
- 参照: `Services.io.newURI(login.origin).host`, `Services.logins.initializationPromise`, `breach.Domain`, `breach.Name`, `breach.breachAlertURL`, `breachAlertURL.href`, `breaches.length`, `breachesByLoginGUID.size`, `login.guid`, `login.origin`, `logins.length`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.logins` / `Services.prefs`

## getPotentiallyVulnerablePasswordsByLoginGUID()
- 位置: async L146-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.arePotentiallyVulnerablePasswords()`, `vulnerablePasswordsByLoginGUID.set()`
- 参照: `lazy.VULNERABLE_PASSWORDS_ENABLED`
- XPCOM: `Services.logins`

## recordBreachAlertDismissal()
- 位置: async L159-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.recordBreachAlertDismissal()`
- XPCOM: `Services.logins`

## clearAllPotentiallyVulnerablePasswords()
- 位置: async L163-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.clearAllPotentiallyVulnerablePasswords()`
- 参照: `Services.logins.initializationPromise`
- XPCOM: `Services.logins`

## _breachAlertIsDismissed()
- 位置: L168-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date(breach.AddedDate).getTime()`
- 参照: `breach.AddedDate`, `dismissedBreachAlerts[login.guid].timeBreachAlertDismissed`, `login.guid`

## _breachInvolvedPasswords()
- 位置: L177-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `breach.DataClasses.includes()`, `breach.hasOwnProperty()`

## _breachWasAfterPasswordLastChanged()
- 位置: L184-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date(breach.BreachDate).getTime()`
- 参照: `breach.BreachDate`, `login.timePasswordChanged`
