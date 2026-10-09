# browser/actors/AboutProtectionsParent.sys.mjs

source: browser/actors/AboutProtectionsParent.sys.mjs
source-hash: 8933d7cb8544202e322c36e81356d0216cb5a848
lines: 430

## <module>
- 役割: about:protections の親側アクター。保護レポートに出す Monitor の漏えい情報、ログイン数、VPN 契約状況、トラッキング統計を集めてページへ返す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Services.prefs.getStringPref()`, `Services.urlFormatter.formatURLPref()`, `XPCOMUtils.defineLazyServiceGetter()`

## AboutProtectionsParent.constructor()
- 位置: L85-87
- 役割: 親アクターの基底コンストラクタを呼ぶだけで、独自の初期化はしていない。
- 触るとき: アクター生成時に初期化処理を足すときに見る。
- 呼び出し先: `super()`

## AboutProtectionsParent.setTestOverride()
- 位置: L90-92
- 役割: テスト用に、ログイン・Monitor・VPN の取得処理を差し替える関数群を保存する。
- 触るとき: about:protections のテストで実データの代わりにモック値を使う仕組みを変えるときに見る。

## AboutProtectionsParent.fetchUserBreachStats()
- 位置: async L100-158
- 役割: Monitor の API を OAuth トークン付きで呼び、応答を検証して 1 日キャッシュし、失敗時は種別ごとのエラーを投げる。
- 触るとき: 漏えい統計の取得失敗、キャッシュの期限、Monitor の応答形式の変化を調べるときに見る。
- 呼び出し先: `fetch()`, `headers.append()`
- 条件付き依存: `if (monitorResponse && monitorResponse.timestamp)` → `Date.now()`
- 条件付き依存: `if (response.ok)` → `response.json()`
- 条件付き依存: `if (response.ok)` → `MONITOR_RESPONSE_PROPS.includes()`
- 条件付き依存: `if (isValid)` → `Date.now()`
- 参照: `monitorResponse.timestamp`, `response.ok`, `response.status`

## AboutProtectionsParent.getLoginData()
- 位置: async L165-208
- 役割: 保存済みログイン数と漏えいの可能性があるパスワード数、モバイル端末の接続有無をまとめて返す。
- 触るとき: 保護画面のパスワード関連の数字がおかしいときに見る。
- 呼び出し先: `Services.logins.countLoginsAsync()`, `console.error()`, `lazy.fxAccounts.device.recentDeviceList.filter()`, `lazy.fxAccounts.getSignedInUser()`
- 条件付き依存: `if (gTestOverride && "getLoginData" in gTestOverride)` → `gTestOverride.getLoginData()`
- 条件付き依存: `if (await lazy.fxAccounts.getSignedInUser())` → `lazy.fxAccounts.device.refreshDeviceList()`
- 条件付き依存: `if (userFacingLogins && Services.logins.isLoggedIn)` → `lazy.LoginHelper.getAllUserFacingLogins()`
- 条件付き依存: `if (userFacingLogins && Services.logins.isLoggedIn)` → `lazy.LoginBreaches.getPotentialBreachesByLoginGUID()`
- 参照: `Services.logins.isLoggedIn`, `device.type`, `e.message`, `lazy.FXA_PWDMGR_HOST`, `lazy.FXA_PWDMGR_REALM`, `lazy.fxAccounts.device.recentDeviceList`, `lazy.fxAccounts.device.recentDeviceList.filter( device => device.type == "mobile" ).length`, `potentiallyBreachedLogins.size`
- XPCOM: `Services.logins`

## AboutProtectionsParent.getMonitorData()
- 位置: async L224-282
- 役割: Monitor 用の OAuth トークンを取り、漏えい統計とユーザーのメールアドレスを返す。トークン無効時は再取得する。
- 触るとき: Monitor の表示内容、エラー表示、ユーザーの誘導先を変えるときに見る。
- 呼び出し先: `console.error()`, `this.getMonitorScopedOAuthToken()`
- 条件付き依存: `if (gTestOverride && "getMonitorData" in gTestOverride)` → `gTestOverride.getMonitorData()`
- 条件付き依存: `if (gTestOverride && "getMonitorData" in gTestOverride)` → `Date.now()`
- 条件付き依存: `if (gTestOverride && "getMonitorData" in gTestOverride)` → `this.fetchUserBreachStats()`
- 条件付き依存: `if (token)` → `this.fetchUserBreachStats()`
- 条件付き依存: `if (token)` → `lazy.fxAccounts.getSignedInUser()`
- 条件付き依存: `if (e.message === INVALID_OAUTH_TOKEN)` → `lazy.fxAccounts.removeCachedOAuthToken()`
- 条件付き依存: `if (e.message === INVALID_OAUTH_TOKEN)` → `this.getMonitorScopedOAuthToken()`
- 条件付き依存: `if (e.message === INVALID_OAUTH_TOKEN)` → `this.fetchUserBreachStats()`
- 条件付き依存: `if (e.message === INVALID_OAUTH_TOKEN)` → `console.error()`
- 条件付き依存: `if (e.message === USER_UNSUBSCRIBED_TO_MONITOR)` → `lazy.fxAccounts.getSignedInUser()`
- 参照: `e.message`, `monitorData.errorMessage`, `monitorResponse.timestamp`

## AboutProtectionsParent.getMonitorScopedOAuthToken()
- 位置: async L284-297
- 役割: Monitor のスコープで OAuth トークンを取得し、失敗時は null を返す。
- 触るとき: Monitor 連携でトークンが取れない問題を調べるときに見る。
- 呼び出し先: `console.error()`, `lazy.fxAccounts.getOAuthToken()`
- 参照: `e.message`

## AboutProtectionsParent.VPNSubStatus()
- 位置: async L299-331
- 役割: VPN のスコープでトークンを取り、契約一覧に設定の subscription ID があるかで購読を判定する。
- 触るとき: VPN 購読の判定条件や VPN 関連の表示を変えるときに見る。
- 呼び出し先: `console.error()`, `fetch()`, `headers.append()`, `lazy.fxAccounts.getOAuthToken()`
- 条件付き依存: `if (gTestOverride && "vpnOverrides" in gTestOverride)` → `gTestOverride.vpnOverrides()`
- 条件付き依存: `if (res.ok)` → `res.json()`
- 参照: `e.message`, `res.ok`, `sub.subscriptionId`

## AboutProtectionsParent.receiveMessage()
- 位置: async L333-428
- 役割: ページからの設定画面表示、トラッキング統計、Monitor・ログイン・VPN の取得、エントリーポイント記録などのメッセージを処理する。
- 触るとき: about:protections の機能を追加・変更する際に、どのメッセージがどの処理に届くかを確かめるときに見る。
- 呼び出し先: `[7, 1, 2, 3, 4, 5, 6].map()`, `displayNames.of()`, `idToTextMap.get()`, `lazy.BrowserUtils.shouldShowVPNPromo()`, `lazy.LoginHelper.openPasswordManager()`, `lazy.PrivacyMetricsService.getWeeklyStats()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.TrackingDBService.getEarliestRecordedDate()`, `lazy.TrackingDBService.getEventsByDateRange()`, `lazy.TrackingDBService.sumAllEvents()`, `result.getResultByName()`, `this.VPNSubStatus()`, `this.getLoginData()`, `this.getMonitorData()`, `win.openPreferences()`, `win.openTrustedLinkIn()`
- 参照: `Services.intl.DisplayNames`, `aMessage.data.entrypoint`, `aMessage.data.from`, `aMessage.data.to`, `aMessage.name`, `dataToSend.earliestDate`, `dataToSend.isPrivate`, `dataToSend.largest`, `dataToSend.sumEvents`, `dataToSend.weekdays`, `dataToSend[timestamp].total`, `this.browsingContext.top.embedderElement.documentGlobal`
- XPCOM: `Services.intl`
