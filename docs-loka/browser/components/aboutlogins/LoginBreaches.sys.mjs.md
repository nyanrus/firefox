# browser/components/aboutlogins/LoginBreaches.sys.mjs

source: browser/components/aboutlogins/LoginBreaches.sys.mjs
source-hash: f1d79257f8196c2f8430c801e91e5d55e54c5790
lines: 189

## <module>
- 役割: Firefox Monitor の侵害データ(RemoteSettings 経由)を使い、保存済みログインの侵害警告と脆弱パスワードの判定をまとめるモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## breachAlertsData()
- 位置: L30-35
- 役割: BreachAlertsData を初回アクセス時に生成して保持するキャッシュ付きの getter。
- 触るとき: 侵害データの取得元や購読の仕組みを変えるとき。
- 参照: `lazy.BreachAlertsData`, `this._cachedBreachAlertsData`

## update()
- 位置: async L37-40
- 役割: 全ユーザー向けログインを取得し、getPotentialBreachesByLoginGUID を呼ぶ。戻り値は使わず、脆弱パスワードの登録などの副作用だけを残す。
- 触るとき: RemoteSettings の侵害データが更新されたときに判定をやり直す流れを変えるとき。
- 呼び出し先: `lazy.LoginHelper.getAllUserFacingLogins()`, `this.getPotentialBreachesByLoginGUID()`

## subscribeToBreachUpdates()
- 位置: L46-48
- 役割: 侵害データの購読を開始し、データが届くたびに update を呼ぶ。購読解除用の値を返す。
- 触るとき: 侵害データ更新時に判定を再計算するタイミングを変えるとき。
- 呼び出し先: `this.breachAlertsData.subscribe()`, `this.update()`

## getPotentialBreachesByLoginGUID()
- 位置: async L64-134
- 役割: パスワードに関わる侵害のうち、ドメインが一致し、パスワード変更時刻が侵害日より前のログインを見つける。該当すると脆弱パスワードとして登録し、dismiss されていなければ UTM 付きの侵害ページ URL を付けて GUID から侵害への Map に入れる(同じ GUID では後の侵害で上書き)。最後に件数を Glean に送る。
- 触るとき: 侵害警告の出す条件や、どの侵害を表示するかを変えるとき。ユーザー名やパスワードの中身は見ない点に注意が要る。
- 呼び出し先: `Glean.pwmgr.potentiallyBreachedPasswords.set()`, `Services.eTLD.hasRootDomain()`, `Services.io.newURI()`, `Services.logins.arePotentiallyVulnerablePasswords()`, `Services.logins.getBreachAlertDismissalsByLoginGUID()`, `Services.prefs.getStringPref()`, `breachAlertURL.searchParams.set()`, `breachesByLoginGUID.set()`, `potentiallyVulnerablePasswords.has()`, `this._breachAlertIsDismissed()`, `this._breachInvolvedPasswords()`, `this._breachWasAfterPasswordLastChanged()`
- 条件付き依存: `if (!breaches)` → `this.breachAlertsData.getAllBreaches()`
- 条件付き依存: `if (!potentiallyVulnerablePasswords.has(login.guid))` → `Services.logins.addPotentiallyVulnerablePassword()`
- 参照: `Services.io.newURI(login.origin).host`, `Services.logins.initializationPromise`, `breach.Domain`, `breach.Name`, `breach.breachAlertURL`, `breachAlertURL.href`, `breaches.length`, `breachesByLoginGUID.size`, `login.guid`, `login.origin`, `logins.length`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.logins` / `Services.prefs`

## getPotentiallyVulnerablePasswordsByLoginGUID()
- 位置: async L146-157
- 役割: 脆弱パスワード機能が有効なときだけ、Services.logins で脆弱とされたログインの GUID を true の Map にする。
- 触るとき: 脆弱パスワード警告の対象の取得方法や有効化条件を変えるとき。
- 呼び出し先: `Services.logins.arePotentiallyVulnerablePasswords()`, `vulnerablePasswordsByLoginGUID.set()`
- 参照: `lazy.VULNERABLE_PASSWORDS_ENABLED`
- XPCOM: `Services.logins`

## recordBreachAlertDismissal()
- 位置: async L159-161
- 役割: 指定ログインの侵害警告が閉じられたことを Services.logins に記録する。
- 触るとき: 侵害警告を閉じた後の再表示を調べるとき。
- 呼び出し先: `Services.logins.recordBreachAlertDismissal()`
- XPCOM: `Services.logins`

## clearAllPotentiallyVulnerablePasswords()
- 位置: async L163-166
- 役割: 初期化を待ってから、登録済みの脆弱パスワードをすべて消す。
- 触るとき: 脆弱パスワードの記録の消去処理を変えるとき。
- 呼び出し先: `Services.logins.clearAllPotentiallyVulnerablePasswords()`
- 参照: `Services.logins.initializationPromise`
- XPCOM: `Services.logins`

## _breachAlertIsDismissed()
- 位置: L168-175
- 役割: ログインに dismiss の記録があり、その時刻が侵害の追加日より新しければ true を返す。
- 触るとき: 一度閉じた侵害警告を再び出す条件を変えるとき。
- 呼び出し先: `new Date(breach.AddedDate).getTime()`
- 参照: `breach.AddedDate`, `dismissedBreachAlerts[login.guid].timeBreachAlertDismissed`, `login.guid`

## _breachInvolvedPasswords()
- 位置: L177-182
- 役割: 侵害の DataClasses に Passwords が含まれるかを返す。
- 触るとき: パスワード以外の侵害を警告の対象から外す条件を変えるとき。
- 呼び出し先: `breach.DataClasses.includes()`, `breach.hasOwnProperty()`

## _breachWasAfterPasswordLastChanged()
- 位置: L184-187
- 役割: ログインのパスワード変更時刻が侵害日より前なら true を返す。
- 触るとき: パスワードを変えた後の侵害を警告の対象外にする判定を変えるとき。
- 呼び出し先: `new Date(breach.BreachDate).getTime()`
- 参照: `breach.BreachDate`, `login.timePasswordChanged`
