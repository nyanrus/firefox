# browser/modules/AboutNewTab.sys.mjs

source: browser/modules/AboutNewTab.sys.mjs
source-hash: fde4f9eb767211f65ef72e3635775a38f5810aa2
lines: 366

## <module>
- 役割: about:newtab の Activity Stream の初期化・停止と、新しいタブの URL 設定を管理するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## init()
- 位置: L54-113
- 役割: 終了時と TOU 同意の通知を登録し、設定の既定値を入れて、Activity Stream の初期化を始める。
- 触るとき: 起動時に行う初期化の順序や既定値を変えるとき。二重に呼ばれた時は何もしない。
- 呼び出し先: `Promise.withResolvers()`, `Services.obs.addObserver()`, `Services.prefs.getPrefType()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.AboutNewTabResourceMapping.init()`, `this.notifyChange()`, `this.toggleActivityStream()`
- 条件付き依存: `if (!AppConstants.RELEASE_OR_BETA)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (!AppConstants.RELEASE_OR_BETA)` → `this.notifyChange()`
- 条件付き依存: `if ( Services.prefs.getPrefType(AStelemetryPref) === Services.prefs.PREF_INVALID )` → `Services.prefs .getDefaultBranch("") .setBoolPref()`
- 条件付き依存: `if ( Services.prefs.getPrefType(AStelemetryPref) === Services.prefs.PREF_INVALID )` → `Services.prefs .getDefaultBranch()`
- 参照: `AppConstants.MOZILLA_OFFICIAL`, `AppConstants.RELEASE_OR_BETA`, `Services.prefs.PREF_INVALID`, `lazy.TelemetryReportingPolicy.TELEMETRY_TOU_ACCEPTED_OR_INELIGIBLE`, `this._activityStreamResolver`, `this.activityStreamPromise`, `this.initialized`
- XPCOM: `Services.obs` / `Services.prefs`

## toggleActivityStream()
- 位置: L125-142
- 役割: Activity Stream の有効状態を切り替え、状態が変わった時だけ newTab の URL を about:newtab に戻す。
- 触るとき: 有効・無効の切り替え条件を変えるとき。URL が上書きされている時は force 指定が無い限り切り替えない。
- 参照: `this._activityStreamEnabled`, `this._newTabURL`, `this._newTabURLOverridden`

## newTabURL()
- 位置: L144-146
- 役割: 現在の新しいタブの URL を返す。
- 触るとき: 新しいタブの URL を読む側の挙動を確かめるとき。
- 参照: `this._newTabURL`

## newTabURL()
- 位置: L148-162
- 役割: 新しいタブの URL を設定する。about:newtab は既定に戻し、空文字は about:blank にする。
- 触るとき: ユーザーが設定した新しいタブ URL の扱い(リダイレクトの防止、空の扱い)を変えるとき。
- 呼び出し先: `aNewTabURL.trim()`, `this.notifyChange()`, `this.toggleActivityStream()`
- 条件付き依存: `if (newTabURL === ABOUT_URL)` → `this.resetNewTabURL()`
- 参照: `this._newTabURL`, `this._newTabURLOverridden`

## newTabURLOverridden()
- 位置: L164-166
- 役割: 新しいタブの URL が既定から上書きされているかを返す。
- 触るとき: 上書き有無で他の処理を分けるとき。
- 参照: `this._newTabURLOverridden`

## activityStreamEnabled()
- 位置: L168-170
- 役割: Activity Stream が有効かを返す。
- 触るとき: 新しいタブが Activity Stream で描画されるかの判定を読むとき。
- 参照: `this._activityStreamEnabled`

## resetNewTabURL()
- 位置: L172-177
- 役割: 上書きを解除して URL を about:newtab に戻し、Activity Stream を有効に戻す。
- 触るとき: 新しいタブの設定を既定に戻す操作の流れを変えるとき。
- 呼び出し先: `this.notifyChange()`, `this.toggleActivityStream()`
- 参照: `this._newTabURL`, `this._newTabURLOverridden`

## notifyChange()
- 位置: L179-181
- 役割: 現在の新しいタブ URL を newtab-url-changed 通知で他に知らせる。
- 触るとき: URL 変更の通知先を増やすとき、通知の引数を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `this._newTabURL`
- XPCOM: `Services.obs`

## onBrowserReady()
- 位置: async L186-248
- 役割: アドオンの初期化、Nimbus の機能、プロファイル作成日時の揃いを待ち、Activity Stream を作って初期化する。
- 触るとき: 新しいタブの起動待ちや初期化の順序を変えるとき。作成に失敗すると telemetry を送って例外を投げる。
- 呼び出し先: `Cc[ "@mozilla.org/network/protocol/about;1?what=newtab" ].getService()`, `Glean.newtab.activityStreamCtorSuccess.set()`, `Promise.all()`, `Temporal.Instant.fromEpochMilliseconds()`, `console.error()`, `lazy .ProfileAge()`, `lazy .ProfileAge() .then()`, `lazy.AboutNewTabResourceMapping.scheduleUpdateTrainhopAddonState()`, `nimbusFeature.ready()`, `this._activityStreamResolver()`, `this._subscribeToActivityStream()`, `this.activityStream.init()`
- 参照: `Cc[ "@mozilla.org/network/protocol/about;1?what=newtab" ].getService(Ci.nsIAboutModule).wrappedJSObject`, `Ci.nsIAboutModule`, `accessor.created`, `lazy.ActivityStream`, `lazy.NimbusFeatures`, `redirector.promiseBuiltInAddonInitialized`, `this.activityStream`, `this.activityStream.initialized`
- XPCOM: [`nsIAboutModule`](../../netwerk/protocol/about/nsIAboutModule.idl.md) / `@mozilla.org/network/protocol/about;1?what=newtab`

## _subscribeToActivityStream()
- 位置: L250-275
- 役割: Redux 風ストアの上位サイト一覧を購読し、スクリーンショットを除いて変わった時だけ newtab-top-sites-changed を通知する。
- 触るとき: 上位サイトの変更通知の条件や内容を変えるとき。スクリーンショットは変化判定から外している。
- 呼び出し先: `lazy.ObjectUtils.deepEqual()`, `store.getState()`, `store.getState().TopSites.rows.map()`, `store.subscribe()`
- 条件付き依存: `if (!lazy.ObjectUtils.deepEqual(topSites, this._cachedTopSites))` → `Services.obs.notifyObservers()`
- 参照: `site.screenshot`, `this._cachedTopSites`, `this._unsubscribeFromActivityStream`, `this.activityStream.store`
- XPCOM: `Services.obs`

## this._unsubscribeFromActivityStream()
- 位置: L268-274
- 役割: 上位サイトの購読を解除する。解除時の例外は記録して握りつぶす。
- 触るとき: 終了時に購読が残る問題を確かめるとき。
- 呼び出し先: `console.error()`, `unsubscribe()`

## uninit()
- 位置: L280-298
- 役割: Activity Stream を止め、登録した通知を外して初期化状態を戻す。
- 触るとき: 終了処理や再初期化の時に残るものを確かめるとき。通知の登録前に失敗した場合の例外は無視する。
- 呼び出し先: `Services.obs.removeObserver()`
- 条件付き依存: `if (this.activityStream)` → `this._unsubscribeFromActivityStream()`
- 条件付き依存: `if (this.activityStream)` → `this.activityStream.uninit()`
- 参照: `lazy.TelemetryReportingPolicy.TELEMETRY_TOU_ACCEPTED_OR_INELIGIBLE`, `this.activityStream`, `this.initialized`
- XPCOM: `Services.obs`

## getTopSites()
- 位置: L300-304
- 役割: ストアから上位サイトの行を返す。Activity Stream が無ければ空配列。
- 触るとき: 上位サイトを他の機能から読むとき。
- 呼び出し先: `this.activityStream.store.getState()`
- 参照: `this.activityStream`, `this.activityStream.store.getState().TopSites.rows`

## getVisitId()
- 位置: L316-323
- 役割: 指定したブラウザが表示中の新しいタブの訪問 ID(newtab_visit_id)を返す。無ければ null。
- 触るとき: newtab ping の訪問 ID を結びつける処理を変えるとき。
- 呼び出し先: `lazy.AboutNewTabParent.loadedTabs.get()`, `telemetryFeed?.sessions.get()`, `this.activityStream?.store.feeds.get()`
- 参照: `lazy.AboutNewTabParent.loadedTabs.get(browser)?.portID`, `telemetryFeed?.sessions.get(portID)?.session_id`

## noteNonDefaultStartup()
- 位置: L328-330
- 役割: 既定以外の起動だったことを記録し、上位サイトの描画計測を止める。
- 触るとき: 起動の種類による計測の除外条件を変えるとき。
- 参照: `this._nonDefaultStartup`

## maybeRecordTopsitesPainted()
- 位置: L332-343
- 役割: 初回の上位サイト描画までの時間を計測し、Glean とプロファイラーに記録する。既定以外の起動や記録済みなら何もしない。
- 触るとき: 起動時間の計測の仕組みや記録先を変えるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Glean.timestamps.aboutHomeTopsitesFirstPaint.set()`, `Math.round()`, `Services.startup.getStartupInfo()`, `startupInfo.process.getTime()`
- 参照: `this._alreadyRecordedTopsitesPainted`, `this._nonDefaultStartup`
- XPCOM: `Services.startup`

## observe()
- 位置: L347-364
- 役割: 終了通知で uninit を呼び、TOU 同意の通知で次のイベントループ以降に onBrowserReady を呼ぶ。
- 触るとき: 新しいタブの初期化の開始タイミングを変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `Services.tm.dispatchToMainThread()`, `this.onBrowserReady()`, `this.uninit()`
- 参照: `lazy.TelemetryReportingPolicy.TELEMETRY_TOU_ACCEPTED_OR_INELIGIBLE`
- XPCOM: `Services.obs` / `Services.tm`
