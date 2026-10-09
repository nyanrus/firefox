# browser/modules/LaterRun.sys.mjs

source: browser/modules/LaterRun.sys.mjs
source-hash: 1ea3483149b1ba83e0736c2153fc20496564c8cb
lines: 208

## <module>
- 役割: インストール後の数回の起動で、設定されたHTTPSページを一度だけ案内する仕組み。
- 呼び出し先: `LaterRun.init()`

## Page.constructor()
- 位置: L20-32
- 役割: 案内ページ1件の条件(起動回数、インストールからの時間、AND/OR)を受け取る。
- 触るとき: 案内ページごとの表示条件の既定値(起動回数1、時間0)を変えるとき。
- 参照: `this.minimumHoursSinceInstall`, `this.minimumSessionCount`, `this.pref`, `this.requireBoth`, `this.url`

## Page.hasRun()
- 位置: L34-36
- 役割: そのページが既に表示済みかを hasRun の設定から読む。
- 触るとき: 同じページが二度出る、または一度も出ない報告を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.pref`
- XPCOM: `Services.prefs`

## Page.applies()
- 位置: L38-52
- 役割: 表示済みでなく、起動回数と経過時間の条件を満たすかを返す。
- 触るとき: 案内ページの条件判定を変えるとき。requireBoth が真なら両方、偽なら片方を満たせば対象になる。
- 参照: `sessionInfo.hoursSinceInstall`, `sessionInfo.sessionCount`, `this.hasRun`, `this.minimumHoursSinceInstall`, `this.minimumSessionCount`, `this.requireBoth`

## ENABLE_REASON_NEW_PROFILE()
- 位置: L56-58
- 役割: init に渡す理由コード(新規プロファイル)の 1 を返す。
- 触るとき: 有効化の理由を追加・変更するとき。

## ENABLE_REASON_UPDATE_APPLIED()
- 位置: L59-61
- 役割: init に渡す理由コード(アップデート適用)の 2 を返す。
- 触るとき: アップデート適用時の経過時間の記録処理を確かめるとき。

## init()
- 位置: L63-94
- 役割: 有効時に初回の設置時刻や更新時刻を記録し、起動回数を増やす。上限を超えたら自己停止する。
- 触るとき: インストール時刻や起動回数の記録、または自己停止条件を変えるとき。自己停止の上限は 31 日(744 時間)と 50 回の起動。
- 条件付き依存: `if (reason == this.ENABLE_REASON_NEW_PROFILE)` → `Services.prefs.getPrefType()`
- 条件付き依存: `if ( Services.prefs.getPrefType(kProfileCreationTime) == Ci.nsIPrefBranch.PREF_INVALID )` → `Services.prefs.setIntPref()`
- 条件付き依存: `if ( Services.prefs.getPrefType(kProfileCreationTime) == Ci.nsIPrefBranch.PREF_INVALID )` → `Math.floor()`
- 条件付き依存: `if ( Services.prefs.getPrefType(kProfileCreationTime) == Ci.nsIPrefBranch.PREF_INVALID )` → `Date.now()`
- 条件付き依存: `if (reason == this.ENABLE_REASON_UPDATE_APPLIED)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (reason == this.ENABLE_REASON_UPDATE_APPLIED)` → `Math.floor()`
- 条件付き依存: `if (reason == this.ENABLE_REASON_UPDATE_APPLIED)` → `Services.startup.getStartupInfo().start.getTime()`
- 条件付き依存: `if (reason == this.ENABLE_REASON_UPDATE_APPLIED)` → `Services.startup.getStartupInfo()`
- 条件付き依存: `if ( this.hoursSinceInstall > kSelfDestructHoursLimit || this.sessionCount > kSelfDestructSessionLimit )` → `this.selfDestruct()`
- 参照: `Ci.nsIPrefBranch.PREF_INVALID`, `this.ENABLE_REASON_NEW_PROFILE`, `this.ENABLE_REASON_UPDATE_APPLIED`, `this.enabled`, `this.hoursSinceInstall`, `this.sessionCount`
- XPCOM: [`nsIPrefBranch`](../../netwerk/base/nsINetUtil.idl.md) / `Services.prefs` / `Services.startup`

## enabled()
- 位置: L98-100
- 役割: browser.laterrun.enabled の設定値を返す(既定は偽)。
- 触るとき: 機能の有効・無効の判定元を確かめるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## enable()
- 位置: L102-107
- 役割: 未有効なら有効化の設定を立てて init を呼ぶ。
- 触るとき: 外部から機能を有効にする経路を追加・変更するとき。
- 条件付き依存: `if (!this.enabled)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!this.enabled)` → `this.init()`
- 参照: `this.enabled`
- XPCOM: `Services.prefs`

## hoursSinceInstall()
- 位置: L109-115
- 役割: プロファイル作成時刻からの経過時間を時間単位で返す。
- 触るとき: インストール後の時間条件を変えるとき。時刻の記録がなければ 0 時間になる。
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## hoursSinceUpdate()
- 位置: L117-120
- 役割: アップデート適用時刻からの経過時間を時間単位で返す。
- 触るとき: アップデート後の案内条件を変えるとき。記録がない場合は 0 を基準にするため非常に大きな値になる。
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## sessionCount()
- 位置: L122-130
- 役割: 起動回数をキャッシュ付きで読む。キャッシュが無ければ設定から読む。
- 触るとき: 起動回数の参照元を確かめるとき。
- 呼び出し先: `Services.prefs.getIntPref()`
- 参照: `this._sessionCount`
- XPCOM: `Services.prefs`

## sessionCount()
- 位置: L132-135
- 役割: 起動回数をキャッシュと設定の両方に書き込む。
- 触るとき: 起動回数を増やす処理や保存先を変えるとき。
- 呼び出し先: `Services.prefs.setIntPref()`
- 参照: `this._sessionCount`
- XPCOM: `Services.prefs`

## selfDestruct()
- 位置: L140-142
- 役割: 機能を無効にする設定を立てる。
- 触るとき: 自己停止の後に再度有効になる経路を調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## readPages()
- 位置: L145-186
- 役割: browser.laterrun.pages 配下の設定から案内ページを組み立て、HTTPS のものだけ残す。
- 触るとき: 案内ページの設定項目(url、起動回数、時間、hasRun など)を追加・変更するとき。不正な URL は無視し、HTTP は記録だけして除外する。
- 呼び出し先: `Services.prefs.getChildList()`, `pageDataStore.has()`, `pref.substring()`, `pref.substring(kPagePrefRoot.length).split()`
- 条件付き依存: `if (!pageDataStore.has(slug))` → `pageDataStore.set()`
- 条件付き依存: `if (!pageDataStore.has(slug))` → `pref.substring()`
- 条件付き依存: `if (prop == "requireBoth" || prop == "hasRun")` → `pageDataStore.get()`
- 条件付き依存: `if (prop == "requireBoth" || prop == "hasRun")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (prop == "url")` → `pageDataStore.get()`
- 条件付き依存: `if (prop == "url")` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (!(prop == "url"))` → `pageDataStore.get()`
- 条件付き依存: `if (!(prop == "url"))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (pageData.url)` → `Services.urlFormatter.formatURL()`
- 条件付き依存: `if (pageData.url)` → `pageData.url.trim()`
- 条件付き依存: `if (pageData.url)` → `URL.parse()`
- 条件付き依存: `if (!uri)` → `console.error()`
- 条件付き依存: `if (pageData.url)` → `uri.schemeIs()`
- 条件付き依存: `if (!uri.schemeIs("https"))` → `console.error()`
- 条件付き依存: `if (!(!uri.schemeIs("https")))` → `rv.push()`
- 参照: `URL.parse(urlString)?.URI`, `kPagePrefRoot.length`, `pageData.url`, `pref.length`, `prop.length`, `uri.spec`
- XPCOM: `Services.prefs` / `Services.urlFormatter`

## getURL()
- 位置: L193-204
- 役割: 有効なら最初に条件を満たす案内ページを選び、表示済みにして URL を返す。
- 触るとき: 起動時にどの案内ページを開くかを変えるとき。一度に返すのは1件で、残りは次回の起動に回る。
- 呼び出し先: `p.applies()`, `pages.find()`, `this.readPages()`
- 条件付き依存: `if (page)` → `Services.prefs.setBoolPref()`
- 参照: `page.pref`, `page.url`, `this.enabled`
- XPCOM: `Services.prefs`
