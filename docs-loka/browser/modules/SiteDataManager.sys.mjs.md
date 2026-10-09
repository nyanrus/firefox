# browser/modules/SiteDataManager.sys.mjs

source: browser/modules/SiteDataManager.sys.mjs
source-hash: dc2c7d456219ab5b9c3e9ab6c4c8eec1fc745ee8
lines: 665

## <module>
- 役割: サイトごとの Cookie、サイトデータ(quota 使用量)、ディスクキャッシュの容量を集計し、サイトデータの削除を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`

## updateSites()
- 位置: async L60-67
- 役割: サイト情報を空にしてから Cookie とクォータ使用量を集め直し、更新開始と完了の通知を出す。
- 触るとき: サイトデータの一覧が古い、または更新中の通知が出ない問題を調べるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `this._getAllCookies()`, `this._getQuotaUsage()`, `this._sites.clear()`
- XPCOM: `Services.obs`

## getBaseDomainFromHost()
- 位置: L79-97
- 役割: eTLD からベースドメインを求める。IP アドレスやドメイン階層が足りないホストは、そのままホストを返す。
- 触るとき: サイトのグループ化の単位を変えるとき、IP アドレスのホストが別扱いになる問題を調べるとき。
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`
- 参照: `Cr.NS_ERROR_HOST_IS_IP_ADDRESS`, `Cr.NS_ERROR_INSUFFICIENT_DOMAIN_LEVELS`, `e.result`
- XPCOM: `Services.eTLD`

## _getOrInsertSite()
- 位置: L99-113
- 役割: ベースドメインまたはホストに対応するサイト情報を返し、無ければ空の情報を作る。
- 触るとき: サイトごとの集計の受け皿の初期値を変えるとき。
- 呼び出し先: `this._sites.get()`
- 条件付き依存: `if (!site)` → `this._sites.set()`

## _testInsertSite()
- 位置: L123-144
- 役割: テスト用に、指定の Cookie、永続化状態、使用量などを持つサイト情報を直接登録する。
- 触るとき: サイトデータ一覧のテストの前提データを変えるとき。
- 呼び出し先: `this._sites.set()`

## _getOrInsertContainersData()
- 位置: L146-161
- 役割: サイトのコンテナー(userContextId)ごとの集計を返し、無ければ 0 で初期化する。
- 触るとき: コンテナーごとの Cookie 数や最終アクセス時刻の集計を変えるとき。
- 呼び出し先: `site.containersData.get()`
- 条件付き依存: `if (!containerData)` → `site.containersData.set()`
- 参照: `site.containersData`

## getCacheSize()
- 位置: L171-201
- 役割: ディスクキャッシュの使用量を非同期に取得し、取得中は同じ Promise を返す。
- 触るとき: キャッシュ容量の表示が遅い、または更新されない問題を調べるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.cache2.asyncGetDiskConsumption()`, `reject()`
- 参照: `this._getCacheSizeObserver`, `this._getCacheSizePromise`
- XPCOM: `Services.cache2`

## onNetworkCacheDiskConsumption()
- 位置: L179-183
- 役割: キャッシュ使用量の結果を受けて Promise を解決し、保持していた要求を解放する。
- 触るとき: キャッシュ容量の取得結果が戻らない問題を調べるとき。
- 呼び出し先: `resolve()`
- 参照: `this._getCacheSizeObserver`, `this._getCacheSizePromise`

## _getQuotaUsage()
- 位置: L203-273
- 役割: 以前の要求を取り消してから、クォータ使用量の要求を出し、結果の処理が終わったら解決する。
- 触るとき: サイトのクォータ使用量の取得方法や取り消しを変えるとき。
- 呼び出し先: `Services.qms.getUsage()`, `this._cancelGetQuotaUsage()`
- 参照: `this._getQuotaUsagePromise`, `this._quotaUsageRequest`
- XPCOM: `Services.qms`

## onUsageResult()
- 位置: L206-266
- 役割: クォータの結果を受け、非永続で使用量 0 のものを除き、HTTP と HTTPS のサイトをベースドメインごとにまとめて使用量や最終アクセス時刻を加算する。
- 触るとき: サイトごとの使用量の集計ルール(パーティション、コンテナー、永続化の扱い)を変えるとき。
- 呼び出し先: `resolve()`
- 条件付き依存: `if (request.resultCode == Cr.NS_OK)` → `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`
- 条件付き依存: `if (request.resultCode == Cr.NS_OK)` → `principal.schemeIs()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `ChromeUtils.getBaseDomainFromPartitionKey()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `console.error()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `this._getOrInsertSite()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `Number.isInteger()`
- 条件付き依存: `if (Number.isInteger(principal.userContextId))` → `this._getOrInsertContainersData()`
- 条件付き依存: `if (Number.isInteger(principal.userContextId))` → `containerData.lastAccessed.getTime()`
- 条件付き依存: `if (containerData.lastAccessed.getTime() < itemTime)` → `containerData.lastAccessed.setTime()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `site.principals.push()`
- 条件付き依存: `if (entryUpdatedCallback)` → `entryUpdatedCallback()`
- 参照: `Cr.NS_OK`, `containerData.quotaUsage`, `item.lastAccessed`, `item.origin`, `item.persisted`, `item.usage`, `principal.baseDomain`, `principal.originAttributes.partitionKey`, `principal.userContextId`, `request.result`, `request.resultCode`, `site.lastAccessed`, `site.persisted`, `site.quotaUsage`
- XPCOM: `Services.scriptSecurityManager`

## _getAllCookies()
- 位置: L275-310
- 役割: 全 Cookie をパーティションキーまたはホストのベースドメインでまとめ、件数、最終アクセス時刻を集計する。
- 触るとき: Cookie のサイトへのまとめ方を変えるとき、Cookie 数が合わない問題を調べるとき。
- 呼び出し先: `ChromeUtils.getBaseDomainFromPartitionKey()`, `Number.isInteger()`, `console.error()`, `site.cookies.push()`, `this._getOrInsertSite()`, `this.getBaseDomainFromHost()`
- 条件付き依存: `if (entryUpdatedCallback)` → `entryUpdatedCallback()`
- 条件付き依存: `if (Number.isInteger(cookie.originAttributes.userContextId))` → `this._getOrInsertContainersData()`
- 条件付き依存: `if (Number.isInteger(cookie.originAttributes.userContextId))` → `containerData.lastAccessed.getTime()`
- 条件付き依存: `if (containerData.lastAccessed.getTime() < cookieTime)` → `containerData.lastAccessed.setTime()`
- 参照: `Services.cookies.cookies`, `containerData.cookiesBlocked`, `cookie.lastAccessed`, `cookie.originAttributes.partitionKey`, `cookie.originAttributes.userContextId`, `cookie.rawHost`, `site.lastAccessed`
- XPCOM: `Services.cookies`

## _cancelGetQuotaUsage()
- 位置: L312-317
- 役割: 進行中のクォータ使用量の要求があれば取り消す。
- 触るとき: 更新の途中で取り消しが効かない問題を調べるとき。
- 条件付き依存: `if (this._quotaUsageRequest)` → `this._quotaUsageRequest.cancel()`
- 参照: `this._quotaUsageRequest`

## hasSiteData()
- 位置: async L330-373
- 役割: 指定ホストに Cookie があるか(プライベートブラウズを除く)を先に調べ、無ければクォータの一覧に一致するものがあるかを返す。
- 触るとき: サイトにデータが残っているかを素早く判定する条件を変えるとき。
- 呼び出し先: `JSON.stringify()`, `Services.cookies.hasCookiesForSite()`, `Services.qms.getUsage()`, `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`, `resolve()`
- 条件付き依存: `if (request.resultCode != Cr.NS_OK)` → `resolve()`
- 条件付き依存: `if (principal.asciiHost == asciiHost)` → `resolve()`
- 参照: `Cr.NS_OK`, `item.origin`, `item.persisted`, `item.usage`, `principal.asciiHost`, `request.result`, `request.resultCode`
- XPCOM: `Services.cookies` / `Services.qms` / `Services.scriptSecurityManager`

## getTotalUsage()
- 位置: L381-389
- 役割: 更新済みの全サイトのクォータ使用量の合計を返す。
- 触るとき: 合計使用量の表示が 0 や古い値になる問題を調べるとき。
- 呼び出し先: `this._getQuotaUsagePromise.then()`, `this._sites.values()`
- 参照: `site.quotaUsage`

## getQuotaUsageForTimeRanges()
- 位置: async L400-424
- 役割: 時間範囲ごとに、最終アクセスがその範囲内のサイトの使用量を合計する。全期間のときは全サイトを対象にする。
- 触るとき: 消去ダイアログの期間ごとの使用量の表示を変えるとき。
- 呼び出し先: `Date.now()`, `this._sites.values()`
- 参照: `lazy.Sanitizer.timeSpanMsMap`, `site.lastAccessed`, `site.quotaUsage`, `this._getQuotaUsagePromise`

## getSites()
- 位置: async L445-456
- 役割: ベースドメインごとのサイトの一覧を、Cookie、使用量、コンテナー情報などと一緒に返す。
- 触るとき: サイト一覧の画面に出す項目を変えるとき。
- 呼び出し先: `Array.from()`, `Array.from(this._sites.values()).map()`, `this._sites.values()`
- 参照: `site.baseDomainOrHost`, `site.containersData`, `site.cookies`, `site.lastAccessed`, `site.persisted`, `site.quotaUsage`, `this._getQuotaUsagePromise`

## getSite()
- 位置: async L470-485
- 役割: ベースドメインまたはホストで単一のサイトを探して返し、無ければ null を返す。
- 触るとき: 特定サイトの情報の参照方法を変えるとき。
- 呼び出し先: `this._sites.get()`, `this.getBaseDomainFromHost()`
- 参照: `site.baseDomainOrHost`, `site.containersData`, `site.cookies`, `site.lastAccessed`, `site.persisted`, `site.quotaUsage`

## _removePermission()
- 位置: L487-501
- 役割: サイトの各プリンシパルについて永続ストレージの権限を外す。同じ origin はまとめて1回だけ外す。
- 触るとき: サイト削除時に永続ストレージの権限が残る問題を調べるとき。
- 呼び出し先: `Services.perms.removeFromPrincipal()`, `removals.add()`, `removals.has()`
- 参照: `site.principals`
- XPCOM: `Services.perms`

## _removeCookies()
- 位置: L503-513
- 役割: サイトの Cookie を1つずつ削除し、サイトの Cookie 一覧を空にする。
- 触るとき: サイト削除で Cookie が残る問題を調べるとき。
- 呼び出し先: `Services.cookies.remove()`
- 参照: `cookie.host`, `cookie.name`, `cookie.originAttributes`, `cookie.path`, `site.cookies`
- XPCOM: `Services.cookies`

## remove()
- 位置: async L528-568
- 役割: 指定したホストごとに Cookie、サイトデータ、キャッシュを削除し、空の値ならローカルファイルのデータを消す。最後に一覧を更新する。
- 触るとき: サイトデータ削除の対象や範囲(パーティションや他サイトの扱い)を変えるとき。
- 呼び出し先: `Array.isArray()`, `Promise.all()`, `promises.push()`, `this.updateSites()`
- 条件付き依存: `if (domainOrHost)` → `Services.eTLD.getSchemelessSiteFromHost()`
- 条件付き依存: `if (domainOrHost)` → `clearData.deleteDataFromSite()`
- 条件付き依存: `if (!(domainOrHost))` → `clearData.deleteDataFromLocalFiles()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL_CACHES`, `Ci.nsIClearDataService.CLEAR_COOKIES_AND_SITE_DATA`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.eTLD`

## promptSiteDataRemoval()
- 位置: L580-622
- 役割: 削除対象が指定されていれば個別の選択ダイアログを開き、無ければ全削除の確認ダイアログを出して結果を返す。
- 触るとき: 削除前の確認ダイアログの文言やボタンを変えるとき。
- 呼び出し先: `Services.prompt.confirmEx()`, `lazy.gBrandBundle.GetStringFromName()`, `lazy.gStringBundle.GetStringFromName()`, `lazy.gStringBundle.formatStringFromName()`
- 条件付き依存: `if (removals)` → `win.browsingContext.topChromeWindow.openDialog()`
- 参照: `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_0_DEFAULT`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `args.allowed`
- XPCOM: `Services.prompt`

## removeAll()
- 位置: async L629-632
- 役割: キャッシュを消してからサイトデータを消す。
- 触るとき: 全削除の順序を変えるとき。
- 呼び出し先: `this.removeCache()`, `this.removeSiteData()`

## removeCache()
- 位置: L639-646
- 役割: 全キャッシュを消し、完了したら解決する。
- 触るとき: キャッシュだけを消す処理の挙動を調べるとき。
- 呼び出し先: `Services.clearData.deleteData()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL_CACHES`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`

## removeSiteData()
- 位置: async L654-663
- 役割: キャッシュは消さずに Cookie とサイトデータを消し、その後に一覧を更新する。
- 触るとき: サイトデータだけを消す範囲を変えるとき。キャッシュが残る理由を確認するとき。
- 呼び出し先: `Services.clearData.deleteData()`, `this.updateSites()`
- 参照: `Ci.nsIClearDataService.CLEAR_COOKIES_AND_SITE_DATA`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`
