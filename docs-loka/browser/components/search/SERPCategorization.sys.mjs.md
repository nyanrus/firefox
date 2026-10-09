# browser/components/search/SERPCategorization.sys.mjs

source: browser/components/search/SERPCategorization.sys.mjs
source-hash: c29fe45ab3aa42aadf4f76d635ceb652b1e41e84
lines: 1752

## <module>
- 役割: SERP のドメインを カテゴリに分類し、SERP categorization のテレメトリを Glean に送る仕組みを定義する。
- 呼び出し先: `Cc["@mozilla.org/security/hash;1"].createInstance()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## Categorizer.init()
- 位置: async L126-133
- 役割: categorization が有効なときだけ、ドメインマップ、イベント予約、テレメトリ記録の各初期化を順に行う。
- 触るとき: categorization の有効化時に初期化される対象を増やすとき、または有効にしても記録されないときの起動順を調べるとき。
- 条件付き依存: `if (this.enabled)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.enabled)` → `SERPDomainToCategoriesMap.init()`
- 条件付き依存: `if (this.enabled)` → `SERPCategorizationEventScheduler.init()`
- 条件付き依存: `if (this.enabled)` → `SERPCategorizationRecorder.init()`
- 参照: `this.enabled`

## Categorizer.uninit()
- 位置: async L135-140
- 役割: ドメインマップ(deleteMap が真なら保存データも削除)、イベント予約、テレメトリ記録を順に終了する。
- 触るとき: categorization を無効にしたときに残るデータや終了処理を変えるとき。
- 呼び出し先: `SERPCategorizationEventScheduler.uninit()`, `SERPCategorizationRecorder.uninit()`, `SERPDomainToCategoriesMap.uninit()`, `lazy.logConsole.debug()`

## Categorizer.enabled()
- 位置: L142-144
- 役割: serpEventTelemetryCategorization の pref の値を返す。
- 触るとき: categorization の有効条件に別の判定を足すとき。
- 参照: `lazy.serpEventTelemetryCategorization`

## Categorizer.maybeCategorizeSERP()
- 位置: async L158-185
- 役割: ドメインマップが空なら欠損として記録して null を返す。そうでなければ organic と広告それぞれを分類し、マップのバージョンと合わせた結果を返す。
- 触るとき: SERP のカテゴリ結果の項目を増やすとき、またはマップが空のとき記録されない理由を調べるとき。
- 呼び出し先: `SERPDomainToCategoriesMap.version.toString()`, `this.applyCategorizationLogic()`
- 条件付き依存: `if (SERPDomainToCategoriesMap.empty)` → `SERPCategorizationRecorder.recordMissingImpressionTelemetry()`
- 参照: `SERPDomainToCategoriesMap.empty`, `results.category`, `results.num_domains`, `results.num_inconclusive`, `results.num_unknown`, `resultsToReport.mappings_version`, `resultsToReport.organic_category`, `resultsToReport.organic_num_domains`, `resultsToReport.organic_num_inconclusive`, `resultsToReport.organic_num_unknown`, `resultsToReport.sponsored_category`, `resultsToReport.sponsored_num_domains`, `resultsToReport.sponsored_num_inconclusive`, `resultsToReport.sponsored_num_unknown`

## Categorizer.applyCategorizationLogic()
- 位置: async L197-256
- 役割: 各ドメインのカテゴリ候補を引き、未知と inconclusive の数を数える。残りの候補は score を log2(rank) で割った値が最大のカテゴリを選ぶ(同点は乱択)。
- 触るとき: カテゴリの決め方(スコアの重みや同点の扱い)を変えるとき、または分類結果が想定と違うとき。
- 呼び出し先: `SERPDomainToCategoriesMap.get()`, `domainsCount.toString()`, `finalCategory.toString()`, `inconclusivesCount.toString()`, `unknownsCount.toString()`
- 条件付き依存: `if (!(unknownsCount + inconclusivesCount == domainsCount))` → `Object.values()`
- 条件付き依存: `if (!(unknownsCount + inconclusivesCount == domainsCount))` → `Math.log2()`
- 条件付き依存: `if (adjustedScore == maxScore)` → `topCategories.push()`
- 条件付き依存: `if (adjustedScore == maxScore)` → `Number()`
- 条件付き依存: `if (!(unknownsCount + inconclusivesCount == domainsCount))` → `this.#chooseRandomlyFrom()`
- 参照: `CATEGORIZATION_SETTINGS.INCONCLUSIVE`, `CATEGORIZATION_SETTINGS.MINIMUM_SCORE`, `CATEGORIZATION_SETTINGS.STARTING_RANK`, `categoryCandidates.length`, `categoryCandidates[0].category`, `topCategories.length`

## Categorizer.#chooseRandomlyFrom()
- 位置: L258-261
- 役割: 同点のカテゴリ候補から一つをランダムに選んで返す。
- 触るとき: 同点時の選び方を固定するなど、乱択の挙動を変えるとき。
- 呼び出し先: `Math.floor()`, `Math.random()`
- 参照: `categories.length`

## CategorizationEventScheduler.init()
- 位置: L302-329
- 役割: アイドル監視(IDLE_TIMEOUT_SECONDS)と quit-application、wake_notification を登録する。
- 触るとき: カテゴリの送信タイミングを決めるアイドルや復帰の通知を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/widget/useridleservice;1"].getService()`, `Services.obs.addObserver()`, `lazy.logConsole.debug()`, `this.#idleService.addIdleObserver()`
- 参照: `CATEGORIZATION_SETTINGS.IDLE_TIMEOUT_SECONDS`, `Ci.nsIUserIdleService`, `this.#browserToCallbackMap`, `this.#idleService`, `this.#init`
- XPCOM: `nsIUserIdleService` / `@mozilla.org/widget/useridleservice;1` / `Services.obs`

## CategorizationEventScheduler.uninit()
- 位置: L331-349
- 役割: アイドル監視と通知の登録を外し、browser と callback の対応表を捨てる。
- 触るとき: 終了時に残る予約済みの送信がないか確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.logConsole.debug()`, `this.#idleService.removeIdleObserver()`
- 参照: `CATEGORIZATION_SETTINGS.IDLE_TIMEOUT_SECONDS`, `this.#browserToCallbackMap`, `this.#idleService`, `this.#init`
- XPCOM: `Services.obs`

## CategorizationEventScheduler.observe()
- 位置: L351-373
- 役割: idle では全予約を送り、quit-application では終了し、wake では最後の登録から WAKE_TIMEOUT_MS(1 時間)以上経っていれば全予約を送る。
- 触るとき: 予約の送信タイミング(アイドル、スリープ復帰、終了)を変えるとき。
- 呼び出し先: `Date.now()`, `lazy.logConsole.debug()`, `this.#sendAllCallbacks()`, `this.uninit()`
- 条件付き依存: `if ( this.#mostRecentMs && Date.now() - this.#mostRecentMs >= CATEGORIZATION_SETTINGS.WAKE_TIMEOUT_MS )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( this.#mostRecentMs && Date.now() - this.#mostRecentMs >= CATEGORIZATION_SETTINGS.WAKE_TIMEOUT_MS )` → `this.#sendAllCallbacks()`
- 参照: `CATEGORIZATION_SETTINGS.WAKE_TIMEOUT_MS`, `this.#mostRecentMs`

## CategorizationEventScheduler.addCallback()
- 位置: L375-379
- 役割: browser に対応する送信用 callback を登録し、最終登録時刻を今にする。
- 触るとき: どの SERP の結果がどのタブに紐づけられるかを調べるとき。
- 呼び出し先: `Date.now()`, `lazy.logConsole.debug()`, `this.#browserToCallbackMap?.set()`
- 参照: `this.#mostRecentMs`

## CategorizationEventScheduler.sendCallback()
- 位置: L381-392
- 役割: browser に登録された callback を実行し、recorded-single-categorization-event を通知してから対応表から消す。
- 触るとき: 1 件ごとの送信後の通知や後片付けを変えるとき。
- 呼び出し先: `this.#browserToCallbackMap?.get()`
- 条件付き依存: `if (callback)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (callback)` → `callback()`
- 条件付き依存: `if (callback)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (callback)` → `this.#browserToCallbackMap.delete()`
- XPCOM: `Services.obs`

## CategorizationEventScheduler.#sendAllCallbacks()
- 位置: L394-406
- 役割: 全 browser の callback を送り、最終登録時刻をリセットして recorded-all-categorization-events を通知する。
- 触るとき: アイドルや復帰で一括送信する仕組みを直すとき。
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`, `Services.obs.notifyObservers()`
- 条件付き依存: `if (browsers)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (browsers)` → `this.sendCallback()`
- 参照: `this.#browserToCallbackMap`, `this.#mostRecentMs`
- XPCOM: `Services.obs`

## CategorizationRecorder.init()
- 位置: async L422-437
- 役割: ユーザー操作の開始と終了を監視し、保存済みの件数を読み込んでカウンターを 0 にし、startup の ping を送る。
- 触るとき: 起動時に未送信の件数を引き継ぐ仕組みを変えるとき、または起動直後の ping の扱いを調べるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`, `this.submitPing()`
- 参照: `this.#init`, `this.#serpCategorizationsCount`
- XPCOM: `Services.obs` / `Services.prefs`

## CategorizationRecorder.uninit()
- 位置: L439-451
- 役割: 監視を外し、未送信件数を pref serpMetricsRecordedCounter に保存してデータを初期化する。
- 触るとき: 終了時に件数が次回起動へ正しく引き継がれるか確かめるとき。
- 条件付き依存: `if (this.#init)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#init)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (this.#init)` → `this.#resetCategorizationRecorderData()`
- 参照: `this.#init`, `this.#serpCategorizationsCount`
- XPCOM: `Services.obs` / `Services.prefs`

## CategorizationRecorder.observe()
- 位置: L453-476
- 役割: ユーザー操作の開始時刻を記録し、操作終了時に activity_limit(既定 120 秒)以上続いていたら inactivity の ping を送る。
- 触るとき: inactivity の ping を送る条件を変えるとき。
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (this.#userInteractionStartTime == null)` → `Date.now()`
- 条件付き依存: `if ( this.#userInteractionStartTime && currentTime - this.#userInteractionStartTime >= activityLimitInMs )` → `this.submitPing()`
- 参照: `lazy.activityLimit`, `this.#userInteractionStartTime`

## CategorizationRecorder.recordCategorizationTelemetry()
- 位置: L484-492
- 役割: 分類結果を Glean の serp.categorization に記録し、件数を増やす。
- 触るとき: 記録するテレメトリの項目を変えるとき、または記録件数が増えない理由を調べるとき。
- 呼び出し先: `Glean.serp.categorization.record()`, `lazy.logConsole.debug()`, `this.#incrementCategorizationsCount()`

## CategorizationRecorder.recordMissingImpressionTelemetry()
- 位置: L499-505
- 役割: マップが無い場合に categorizationNoMapFound を 1 件加算し、件数を増やす。
- 触るとき: マップ欠損時の計測の仕方を変えるとき。
- 呼び出し先: `Glean.serp.categorizationNoMapFound.add()`, `lazy.logConsole.debug()`, `this.#incrementCategorizationsCount()`

## CategorizationRecorder.maybeExtractAndRecordExperimentInfo()
- 位置: L511-543
- 役割: Nimbus の targetExperiment と一致する実験か rollout があれば、そのスラッグとブランチを Glean の experimentInfo に設定する。
- 触るとき: ping に載せる実験情報の決め方を変えるとき、または実験の情報が ping に出ないとき。
- 呼び出し先: `Glean.serp.experimentInfo.set()`, `lazy.NimbusFeatures.search.getEnrollmentMetadata()`, `lazy.NimbusFeatures.search.getVariable()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (!targetExperiment)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (metadata?.slug !== targetExperiment)` → `lazy.NimbusFeatures.search.getEnrollmentMetadata()`
- 条件付き依存: `if (metadata?.slug !== targetExperiment)` → `lazy.logConsole.debug()`
- 参照: `lazy.EnrollmentType.EXPERIMENT`, `lazy.EnrollmentType.ROLLOUT`, `metadata.branch`, `metadata.slug`, `metadata?.slug`

## CategorizationRecorder.submitPing()
- 位置: L545-557
- 役割: 件数が 0 なら何もせず、そうでなければ実験情報を記録してから ping を送り、件数を 0 にする。
- 触るとき: ping の送信理由や送信条件を変えるとき。
- 呼び出し先: `GleanPings.serpCategorization.submit()`, `lazy.logConsole.debug()`, `this.maybeExtractAndRecordExperimentInfo()`
- 参照: `this.#serpCategorizationsCount`

## CategorizationRecorder.testReset()
- 位置: L564-568
- 役割: 自動テスト中だけ、記録済みの件数と操作開始時刻をリセットする。
- 触るとき: テストの間で件数が残らないようにするとき。
- 条件付き依存: `if (Cu.isInAutomation)` → `this.#resetCategorizationRecorderData()`
- 参照: `Cu.isInAutomation`

## CategorizationRecorder.#incrementCategorizationsCount()
- 位置: L570-579
- 役割: 件数を 1 増やし、PING_SUBMISSION_THRESHOLD(10 件)に達したら threshold_reached の ping を送る。
- 触るとき: ping を送る件数の閾値を変えるとき。
- 条件付き依存: `if ( this.#serpCategorizationsCount >= CATEGORIZATION_SETTINGS.PING_SUBMISSION_THRESHOLD )` → `this.submitPing()`
- 参照: `CATEGORIZATION_SETTINGS.PING_SUBMISSION_THRESHOLD`, `this.#serpCategorizationsCount`

## CategorizationRecorder.#resetCategorizationRecorderData()
- 位置: L581-584
- 役割: 件数と操作開始時刻を初期値に戻す。
- 触るとき: 記録の状態を初期化する新しい箇所を足すとき。
- 参照: `this.#serpCategorizationsCount`, `this.#userInteractionStartTime`

## DomainToCategoriesMap.init()
- 位置: async L669-692
- 役割: 初期化フラグを立ててから Remote Settings とストアを準備する。失敗時は後始末し、成功時は map 初期化の通知を出す。
- 触るとき: 起動時にドメインマップが読み込まれない原因を調べるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#setupClientAndStore()`, `this.uninit()`
- 条件付き依存: `if (this.#client && this.#store)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#client && this.#store)` → `Services.obs.notifyObservers()`
- 参照: `this.#client`, `this.#init`, `this.#store`
- XPCOM: `Services.obs`

## DomainToCategoriesMap.uninit()
- 位置: async L694-716
- 役割: Remote Settings の登録、再試行タイマー、ストアを解放する。shouldDeleteStore が真ならデータも消す。
- 触るとき: 無効化時に保存データを消すかどうかの扱いを変えるとき。
- 条件付き依存: `if (this.#init)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#init)` → `this.#clearClient()`
- 条件付き依存: `if (this.#init)` → `this.#cancelAndNullifyTimer()`
- 条件付き依存: `if (shouldDeleteStore)` → `this.#store.dropData()`
- 条件付き依存: `if (shouldDeleteStore)` → `lazy.logConsole.error()`
- 条件付き依存: `if (this.#store)` → `this.#store.uninit()`
- 条件付き依存: `if (this.#init)` → `Services.obs.notifyObservers()`
- 参照: `this.#init`, `this.#store`
- XPCOM: `Services.obs`

## DomainToCategoriesMap.get()
- 位置: async L726-745
- 役割: ストアが使えないときは空を返す。ドメインを SHA256 でハッシュし、[カテゴリ, スコア] の並びを {category, score} の配列に変えて返す。
- 触るとき: ドメインのカテゴリ検索の仕組みやハッシュ方式を変えるとき。
- 呼び出し先: `lazy.gCryptoHash.finish()`, `lazy.gCryptoHash.init()`, `lazy.gCryptoHash.update()`, `new TextEncoder().encode()`, `this.#store.getCategories()`
- 条件付き依存: `if (rawValues?.length)` → `output.push()`
- 参照: `bytes.length`, `lazy.gCryptoHash.SHA256`, `rawValues.length`, `rawValues?.length`, `this.#store`, `this.#store.empty`, `this.#store.ready`

## DomainToCategoriesMap.version()
- 位置: L756-758
- 役割: 読み込んだマップのバージョン番号を返す。未初期化なら null。
- 触るとき: テレメトリの mappings_version の値の由来を調べるとき。
- 参照: `this.#version`

## DomainToCategoriesMap.empty()
- 位置: L765-770
- 役割: ストアが無ければ真、あればストアの空判定を返す。
- 触るとき: マップが空のときに分類を行わない条件を変えるとき。
- 参照: `this.#store`, `this.#store.empty`

## DomainToCategoriesMap.overrideMapForTests()
- 位置: async L784-794
- 役割: 自動テストでだけ、ストアに渡したオブジェクトを入れ直す。
- 触るとき: 分類のテストで任意のマップを使いたいとき。
- 呼び出し先: `Services.env.exists()`
- 条件付き依存: `if (Cu.isInAutomation || Services.env.exists("XPCSHELL_TEST_PROFILE_DIR"))` → `this.#store.init()`
- 条件付き依存: `if (Cu.isInAutomation || Services.env.exists("XPCSHELL_TEST_PROFILE_DIR"))` → `this.#store.dropData()`
- 条件付き依存: `if (Cu.isInAutomation || Services.env.exists("XPCSHELL_TEST_PROFILE_DIR"))` → `this.#store.insertObject()`
- 参照: `Cu.isInAutomation`
- XPCOM: `Services.env`

## DomainToCategoriesMap.findRecordsForRegion()
- 位置: L814-840
- 役割: 地域に合う特定レコードを優先し、無ければ既定(isDefault)のレコードを返す。どちらも無ければ null。
- 触るとき: 地域ごとのマップの選び方を変えるとき。
- 呼び出し先: `this.recordMatchesRegion()`
- 条件付き依存: `if (record.isDefault)` → `defaultRecords.push()`
- 条件付き依存: `if (!(record.isDefault))` → `regionSpecificRecords.push()`
- 参照: `defaultRecords.length`, `record.isDefault`, `records?.length`, `regionSpecificRecords.length`

## DomainToCategoriesMap.recordMatchesRegion()
- 位置: L851-869
- 役割: 除外地域に含まれれば偽、既定レコードなら真、それ以外は対象地域に含まれるかで判定する。
- 触るとき: 地域の包含や除外の規則を変えるとき。
- 呼び出し先: `record.excludeRegions?.includes()`, `record.includeRegions?.includes()`
- 参照: `record.isDefault`

## DomainToCategoriesMap.syncMayModifyStore()
- 位置: async L871-905
- 役割: 同期の内容が自分の地域のレコードに影響し、ストアを更新する必要があるかを判定する。
- 触るとき: 同期のたびにストアを作り直す無駄を減らすとき、または同期後にマップが更新されないとき。
- 呼び出し先: `recordsDifferFromStore()`, `syncData.updated.map()`, `this.#store.isDefault()`, `this.findRecordsForRegion()`
- 条件付き依存: `if (this.#store.empty && !currentResult)` → `lazy.logConsole.debug()`
- 参照: `currentResult.isDefault`, `obj.new`, `syncData.created`, `syncData.deleted`, `syncData?.current`, `this.#store.empty`

## recordsDifferFromStore()
- 位置: L891-894
- 役割: 渡されたレコードのうち、地域に合い既定の種別がストアと同じものが一つでもあれば真を返す。
- 触るとき: 同期で追加や削除されたレコードがストアに影響するかを判定する条件を変えるとき。
- 呼び出し先: `this.findRecordsForRegion()`
- 参照: `result.isDefault`, `result?.records.length`

## DomainToCategoriesMap.#setupClientAndStore()
- 位置: async L915-977
- 役割: Remote Settings のクライアントとストアを作り、地域に合うレコードがあれば地域の pref を更新する。バージョンが同じなら再利用し、違えば作り直す。
- 触るとき: 起動時にマップを読み直す条件や、地域の pref の値の決まり方を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `lazy.RemoteSettings()`, `lazy.logConsole.debug()`, `this.#clearAndPopulateStore()`, `this.#client.get()`, `this.#client.on()`, `this.#retrieveLatestVersion()`, `this.#store.getVersion()`, `this.#store.init()`, `this.#store.isDefault()`, `this.findRecordsForRegion()`
- 条件付き依存: `if (!records.length)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!hasMatchingRecords)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#store.empty)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#store.empty)` → `this.#store.dropData()`
- 条件付き依存: `if ( storeVersion == this.#version && !this.#store.empty && storeIsDefault == matchingRecordsAreDefault )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( storeVersion == this.#version && !this.#store.empty && storeIsDefault == matchingRecordsAreDefault )` → `Services.obs.notifyObservers()`
- 参照: `lazy.Region.home`, `matchingRecords?.length`, `records.length`, `result?.isDefault`, `result?.records`, `this.#client`, `this.#onSettingsSync`, `this.#store`, `this.#store.empty`, `this.#version`, `this.empty`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#onSettingsSync()
- 位置: L922-922
- 役割: Remote Settings の sync イベントの data を #sync に渡す。
- 触るとき: sync イベントの受け取り方を変えるとき。
- 呼び出し先: `this.#sync()`
- 参照: `event.data`

## DomainToCategoriesMap.#clearClient()
- 位置: L979-987
- 役割: クライアントの sync 登録を外し、ダウンロードの再試行回数を 0 にする。
- 触るとき: クライアントを作り直すときに再試行の回数が引き継がれないか確かめるとき。
- 条件付き依存: `if (this.#client)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#client)` → `this.#client.off()`
- 参照: `this.#client`, `this.#downloadRetries`, `this.#onSettingsSync`

## DomainToCategoriesMap.#retrieveLatestVersion()
- 位置: L999-1006
- 役割: レコード群の中で最大の version を返す。
- 触るとき: マップのバージョンの決め方を変えるとき。
- 呼び出し先: `records.reduce()`
- 参照: `record.version`

## DomainToCategoriesMap.#sync()
- 位置: async L1017-1042
- 役割: 削除されたレコードの添付を消し、地域に影響する変更があればストアを作り直す。失敗時は後始末する。
- 触るとき: Remote Settings の同期でマップが更新される流れを追うとき。
- 呼び出し先: `Promise.all()`, `data?.deleted.filter()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#clearAndPopulateStore()`, `this.#client.attachments.deleteDownloaded()`, `this.syncMayModifyStore()`, `this.uninit()`, `toDelete.map()`
- 条件付き依存: `if (!couldModify)` → `lazy.logConsole.debug()`
- 参照: `d.attachment`, `data?.current`, `lazy.Region.home`, `this.#downloadRetries`

## DomainToCategoriesMap.#clearAndPopulateStore()
- 位置: async L1055-1136
- 役割: ストアを空にしてから、地域に合うレコードの添付をすべてダウンロードして挿入する。ダウンロードに失敗したら再試行タイマーを作って戻る。
- 触るとき: マップの中身を入れ替える処理や、ダウンロードの失敗時の扱いを変えるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `Services.obs.notifyObservers()`, `Services.prefs.setBoolPref()`, `fileContents.push()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#cancelAndNullifyTimer()`, `this.#client.attachments.download()`, `this.#createTimerToPopulateMap()`, `this.#retrieveLatestVersion()`, `this.#store.dropData()`, `this.#store.insertFileContents()`, `this.findRecordsForRegion()`
- 条件付き依存: `if (!this.#store)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#store.ready)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!records?.length)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!hasMatchingRecords)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#version)` → `lazy.logConsole.debug()`
- 参照: `fetchedAttachment.buffer`, `lazy.Region.home`, `records?.length`, `recordsMatchingRegion?.length`, `result?.isDefault`, `result?.records`, `this.#store`, `this.#store.ready`, `this.#version`
- XPCOM: `Services.obs` / `Services.prefs`

## DomainToCategoriesMap.#cancelAndNullifyTimer()
- 位置: L1138-1144
- 役割: 再試行タイマーが動いていれば止めて捨てる。
- 触るとき: タイマーが残って二重にダウンロードされないか確かめるとき。
- 条件付き依存: `if (this.#downloadTimer)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#downloadTimer)` → `this.#downloadTimer.cancel()`
- 参照: `this.#downloadTimer`

## DomainToCategoriesMap.#createTimerToPopulateMap()
- 位置: L1146-1180
- 役割: 再試行回数が maxTriesPerSession(2)未満なら、1 時間に 1〜10 分の揺らぎを足した遅延の後に再度マップを作る。
- 触るとき: ダウンロード再試行の回数や遅延の計算を変えるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `randomInteger()`, `this.#clearAndPopulateStore()`, `this.#client.get()`, `this.#downloadTimer.initWithCallback()`, `this.uninit()`
- 条件付き依存: `if (!this.#downloadTimer)` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `TELEMETRY_CATEGORIZATION_DOWNLOAD_SETTINGS.base`, `TELEMETRY_CATEGORIZATION_DOWNLOAD_SETTINGS.maxAdjust`, `TELEMETRY_CATEGORIZATION_DOWNLOAD_SETTINGS.maxTriesPerSession`, `TELEMETRY_CATEGORIZATION_DOWNLOAD_SETTINGS.minAdjust`, `this.#client`, `this.#downloadRetries`, `this.#downloadTimer`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## DomainToCategoriesStore.init()
- 位置: async L1221-1270
- 役割: 接続を開く。破損時は rebuildableErrors に当たるとストアを作り直す。接続が無ければ戻り、無ければスキーマを作る。
- 触るとき: ストアが壊れたときの復旧の仕方を変えるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#initConnection()`, `this.#rebuildableErrors.includes()`
- 条件付き依存: `if (this.#rebuildableErrors.includes(ex1.name))` → `this.#rebuildStore()`
- 条件付き依存: `if (this.#rebuildableErrors.includes(ex1.name))` → `this.#closeConnection()`
- 条件付き依存: `if (this.#rebuildableErrors.includes(ex1.name))` → `lazy.logConsole.error()`
- 条件付き依存: `if (!this.#connection)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!rebuiltStore)` → `this.#initSchema()`
- 条件付き依存: `if (!rebuiltStore)` → `lazy.logConsole.error()`
- 条件付き依存: `if (!rebuiltStore)` → `this.#closeConnection()`
- 参照: `ex1.name`, `this.#connection`, `this.#init`

## DomainToCategoriesStore.uninit()
- 位置: async L1272-1278
- 役割: 初期化済みなら接続を閉じる。
- 触るとき: ストアの終了処理を変えるとき。
- 条件付き依存: `if (this.#init)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#init)` → `this.#closeConnection()`
- 参照: `this.#init`

## DomainToCategoriesStore.ready()
- 位置: L1285-1287
- 役割: 接続が開いて使えるかを返す。
- 触るとき: ストアを読み書きする前の準備完了の判定を変えるとき。
- 参照: `this.#init`

## DomainToCategoriesStore.empty()
- 位置: L1294-1296
- 役割: ストアにデータが無いかを返す。
- 触るとき: 空のストアを検索しないようにする条件を調べるとき。
- 参照: `this.#empty`

## DomainToCategoriesStore.dropData()
- 位置: async L1305-1343
- 役割: テーブルがあれば作り直して空にし、バージョンを 0 に戻す。
- 触るとき: データの消し方(テーブルの作り直し、バージョン)を変えるとき。
- 呼び出し先: `this.#connection.tableExists()`
- 条件付き依存: `if (tableExists)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (tableExists)` → `this.#connection.executeTransaction()`
- 条件付き依存: `if (tableExists)` → `this.#connection.execute()`
- 条件付き依存: `if (tableExists)` → `this.#connection.executeCached()`
- 参照: `CATEGORIZATION_SETTINGS.STORE_NAME`, `this.#connection`, `this.#empty`

## DomainToCategoriesStore.insertFileContents()
- 位置: async L1360-1371
- 役割: 初期化済みでバージョンがあるとき、添付の内容をストアに挿入する。失敗時は既存データを消す。
- 触るとき: ダウンロードした添付をストアに入れる処理の失敗時の扱いを変えるとき。
- 呼び出し先: `lazy.logConsole.error()`, `this.#insert()`, `this.dropData()`
- 参照: `fileContents?.length`, `this.#init`

## DomainToCategoriesStore.insertObject()
- 位置: async L1387-1396
- 役割: 自動テスト中だけ、オブジェクトを JSON にして挿入する。
- 触るとき: テストで手書きのマップを入れるとき。
- 呼び出し先: `JSON.stringify()`, `new TextEncoder().encode()`, `this.insertFileContents()`
- 参照: `Cu.isInAutomation`, `new TextEncoder().encode( JSON.stringify(domainToCategoriesMap) ).buffer`, `this.#init`

## DomainToCategoriesStore.getCategories()
- 位置: async L1408-1437
- 役割: ハッシュ化したドメインをキーに categories 列を引き、JSON として返す。失敗や無ければ空配列。
- 触るとき: カテゴリを引く SQL を変えるとき、または検索結果が空になる原因を調べるとき。
- 呼び出し先: `JSON.parse()`, `lazy.logConsole.error()`, `rows[0].getResultByName()`, `this.#connection.executeCached()`
- 参照: `rows.length`, `this.#init`

## DomainToCategoriesStore.getVersion()
- 位置: async L1446-1469
- 役割: moz_meta の version を返す。無い、または失敗のときは 0。
- 触るとき: ストアのバージョン判定や再作成の条件を変えるとき。
- 条件付き依存: `if (this.#connection)` → `this.#connection.executeCached()`
- 条件付き依存: `if (this.#connection)` → `lazy.logConsole.error()`
- 条件付き依存: `if (rows.length)` → `parseInt()`
- 条件付き依存: `if (rows.length)` → `rows[0].getResultByName()`
- 参照: `rows.length`, `this.#connection`

## DomainToCategoriesStore.isDefault()
- 位置: async L1477-1502
- 役割: moz_meta の is_default が 1 なら真を返す。
- 触るとき: 既定のレコードから作られたストアかどうかの判定を変えるとき。
- 条件付き依存: `if (this.#connection)` → `this.#connection.executeCached()`
- 条件付き依存: `if (this.#connection)` → `lazy.logConsole.error()`
- 条件付き依存: `if (this.#connection)` → `parseInt()`
- 条件付き依存: `if (this.#connection)` → `rows[0].getResultByName()`
- 参照: `rows.length`, `this.#connection`

## DomainToCategoriesStore.testDelete()
- 位置: async L1507-1512
- 役割: 自動テスト中だけ、接続を閉じてストアのファイルを消す。
- 触るとき: テストでストアを消してから作り直したいとき。
- 条件付き依存: `if (Cu.isInAutomation)` → `this.#closeConnection()`
- 条件付き依存: `if (Cu.isInAutomation)` → `this.#delete()`
- 参照: `Cu.isInAutomation`

## DomainToCategoriesStore.#closeConnection()
- 位置: async L1517-1537
- 役割: 初期化状態を戻し、接続を閉じて、シャットダウン時のブロッカーを外す。
- 触るとき: 接続を閉じる際の後始末の順序を変えるとき。
- 条件付き依存: `if (this.#connection)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#connection)` → `this.#connection.close()`
- 条件付き依存: `if (this.#connection)` → `lazy.logConsole.error()`
- 条件付き依存: `if (this.#asyncShutdownBlocker)` → `lazy.Sqlite.shutdown.removeBlocker()`
- 参照: `this.#asyncShutdownBlocker`, `this.#connection`, `this.#empty`, `this.#init`

## DomainToCategoriesStore.#initSchema()
- 位置: async L1545-1582
- 役割: domain_to_categories と moz_meta のテーブルを作り、スキーマのバージョンを設定し、空かどうかを判定する。
- 触るとき: テーブル構造や保存する meta の項目を変えるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `rows[0].getResultByIndex()`, `this.#connection.execute()`, `this.#connection.executeCached()`, `this.#connection.executeTransaction()`, `this.#connection.setSchemaVersion()`
- 参照: `CATEGORIZATION_SETTINGS.STORE_SCHEMA`, `this.#connection`, `this.#empty`

## DomainToCategoriesStore.#delete()
- 位置: async L1590-1605
- 役割: ストアのファイルを削除し、空の状態にする。
- 触るとき: ストアを作り直す際の削除手順を変えるとき。
- 呼び出し先: `IOUtils.remove()`, `PathUtils.join()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`
- 参照: `CATEGORIZATION_SETTINGS.STORE_FILE`, `PathUtils.profileDir`, `this.#empty`

## DomainToCategoriesStore.#initConnection()
- 位置: async L1614-1645
- 役割: プロファイル内の SQLite を開き、journal_mode を TRUNCATE にして、終了時のブロッカーを登録する。
- 触るとき: DB の接続方法や終了時の閉じ方を変えるとき。
- 呼び出し先: `PathUtils.join()`, `lazy.Sqlite.openConnection()`, `lazy.Sqlite.shutdown.addBlocker()`, `lazy.logConsole.error()`, `this.#closeConnection()`, `this.#connection.execute()`
- 参照: `CATEGORIZATION_SETTINGS.STORE_FILE`, `PathUtils.profileDir`, `this.#asyncShutdownBlocker`, `this.#connection`

## this.#asyncShutdownBlocker()
- 位置: async L1629-1632
- 役割: 終了時に接続を閉じ、接続を null にする。
- 触るとき: 終了時の接続の閉じ方を変えるとき。
- 呼び出し先: `this.#connection.close()`
- 参照: `this.#connection`

## DomainToCategoriesStore.#insert()
- 位置: async L1661-1716
- 役割: 添付の JSON を1トランザクションで domain_to_categories に流し込み、version と is_default を moz_meta に書く。
- 触るとき: マップの取り込み形式やトランザクションの範囲を変えるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `lazy.logConsole.debug()`, `new TextDecoder().decode()`, `this.#connection.executeCached()`, `this.#connection.executeTransaction()`
- 条件付き依存: `if (isDefault)` → `this.#connection.executeCached()`
- 参照: `fileContents?.length`, `this.#empty`

## DomainToCategoriesStore.#rebuildStore()
- 位置: async L1727-1740
- 役割: 接続を閉じ、ファイルを消し、接続を開き直して、スキーマを作り直す。
- 触るとき: ストアの復旧手順を変えるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `this.#closeConnection()`, `this.#delete()`, `this.#initConnection()`, `this.#initSchema()`

## randomInteger()
- 位置: L1743-1745
- 役割: min から max までの整数を一様乱数で返す。
- 触るとき: 再試行の遅延などに使う乱数の範囲を変えるとき。
- 呼び出し先: `Math.floor()`, `Math.random()`
