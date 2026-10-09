# browser/components/urlbar/private/SuggestBackendRust.sys.mjs

source: browser/components/urlbar/private/SuggestBackendRust.sys.mjs
source-hash: 04b2d57b4cf5dd65d96b78d82909a6ea86a5529c
lines: 983

## <module>
- 役割: Rust 版の Suggest バックエンド。Rust コンポーネントの SuggestStore を作り、種別ごとの取り込み、問い合わせ、却下(dismissal)、地名検索を担当する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## SuggestBackendRust.constructor()
- 位置: L93-122
- 役割: 取り込み用のキューを作る。リモート設定のサービスは、テスト用のダミー URL で動かないよう shouldSkipRemoteActivity が偽のときだけ取得する。
- 触るとき: テストでリモート設定が使われない条件を変えるとき、または Rust 提案がテストで無効になる理由を調べるとき。
- 呼び出し先: `super()`
- 条件付き依存: `if (!lazy.Utils.shouldSkipRemoteActivity)` → `lazy.SharedRemoteSettingsService.rustService()`
- 参照: `lazy.TaskQueue`, `lazy.Utils.shouldSkipRemoteActivity`, `this.#ingestQueue`, `this.#remoteSettingsService`

## SuggestBackendRust.enablingPreferences()
- 位置: L124-126
- 役割: 有効判定に使う pref として quicksuggest.rustEnabled を返す。
- 触るとき: Rust 提案が出ない問題で有効条件を確かめるとき。

## SuggestBackendRust.config()
- 位置: L133-135
- 役割: Rust から取得したグローバル設定を返す。未取得なら空オブジェクトを返す。
- 触るとき: Rust 側のグローバル設定を機能が参照する箇所を追うとき。
- 参照: `this.#config`

## SuggestBackendRust.ingestPromise()
- 位置: L141-143
- 役割: 取り込みキューが空になるまで待つ Promise を返す。
- 触るとき: 取り込みの完了を待ってから確かめるテストを書くとき。
- 参照: `this.#ingestQueue.emptyPromise`

## SuggestBackendRust.enable()
- 位置: L145-151
- 役割: 有効化なら #init()、無効化なら #uninit() を呼ぶ。
- 触るとき: Rust バックエンドの有効化・無効化の流れを追うとき。
- 条件付き依存: `if (enabled)` → `this.#init()`
- 条件付き依存: `if (!(enabled))` → `this.#uninit()`

## SuggestBackendRust.query()
- 位置: async L169-248
- 役割: ストアが無ければ空配列を返す。有効な種別(テストで指定されたものを含む)のプロバイダーを集め、機能の制約を統合して問い合わせる。結果ごとに種別を求め、source を 'rust'、provider を種別名にし、アイコンは Blob に変換する。未知の種別は例外を投げる。
- 触るとき: Rust からの提案の取り方、種別の絞り込み、アイコンの変換を変えるとき。
- 呼び出し先: `Glean.suggest.queryTime[label].accumulateSingleSample()`, `getSuggestionType()`, `liftSuggestion()`, `liftedSuggestions.push()`, `this.#store.queryWithMetrics()`, `this.logger.debug()`, `types.map()`, `uniqueProviders.add()`
- 条件付き依存: `if (!provider)` → `this.#providerFromSuggestionType()`
- 条件付き依存: `if (feature)` → `SuggestBackendRust.mergeProviderConstraints()`
- 参照: `Glean.suggest.queryTime`, `feature.rustProviderConstraints`, `lazy.SuggestionProviderConstraints`, `lazy.SuggestionQuery`, `suggestion.icon`, `suggestion.iconMimetype`, `suggestion.icon_blob`, `suggestion.provider`, `suggestion.source`, `this.#enabledSuggestionTypes`, `this.#store`

## SuggestBackendRust.cancelQuery()
- 位置: L250-252
- 役割: ストアに読み取りの中断を要求する。
- 触るとき: 入力が変わったあとも古い問い合わせが残る問題を調べるとき。
- 呼び出し先: `this.#store?.interrupt()`
- 参照: `lazy.InterruptKind.READ`

## SuggestBackendRust.getConfigForSuggestionType()
- 位置: L264-266
- 役割: 種別ごとの設定データを返す。
- 触るとき: 機能が Rust 側の種別設定を参照するとき。
- 呼び出し先: `this.#configsBySuggestionType.get()`

## SuggestBackendRust.ingestEnabledSuggestions()
- 位置: L283-310
- 役割: 機能の種別名が無ければ何もしない。バックエンドか機能が無効なら、次回のために取り込み済みの記録を消す。有効なら、evenIfFresh が真か、前回の制約と違うときだけ取り込みを予約する。
- 触るとき: 取り込みが必要になる条件や、古い取り込みの判定を変えるとき。
- 条件付き依存: `if (!this.isEnabled || !feature.isEnabled)` → `this.#providerConstraintsOnLastIngestByFeature.delete()`
- 条件付き依存: `if (!(!this.isEnabled || !feature.isEnabled))` → `this.#providerConstraintsOnLastIngestByFeature.has()`
- 条件付き依存: `if (!(!this.isEnabled || !feature.isEnabled))` → `lazy.ObjectUtils.deepEqual()`
- 条件付き依存: `if (!(!this.isEnabled || !feature.isEnabled))` → `this.#providerConstraintsOnLastIngestByFeature.get()`
- 条件付き依存: `if ( evenIfFresh || !this.#providerConstraintsOnLastIngestByFeature.has(feature) || !lazy.ObjectUtils.deepEqual( providerConstraints, this.#providerConstraintsOn...)` → `this.#providerConstraintsOnLastIngestByFeature.set()`
- 条件付き依存: `if ( evenIfFresh || !this.#providerConstraintsOnLastIngestByFeature.has(feature) || !lazy.ObjectUtils.deepEqual( providerConstraints, this.#providerConstraintsOn...)` → `this.#ingestSuggestionType()`
- 参照: `feature.isEnabled`, `feature.rustProviderConstraints`, `feature.rustSuggestionType`, `this.isEnabled`

## SuggestBackendRust.dismissRustSuggestion()
- 位置: async L321-328
- 役割: 提案を Rust 形式に変換し、ストアに却下として登録する。失敗はログに出すだけ。
- 触るとき: Rust 提案を却下しても再び出る問題を調べるとき。
- 呼び出し先: `lowerSuggestion()`, `this.#store?.dismissBySuggestion()`, `this.logger.error()`

## SuggestBackendRust.dismissByKey()
- 位置: async L339-345
- 役割: 却下キーを直接ストアに登録する。Merino など Rust 以外の提案の却下にも使う。
- 触るとき: Merino の提案の却下を記録するとき。
- 呼び出し先: `this.#store?.dismissByKey()`, `this.logger.error()`

## SuggestBackendRust.isRustSuggestionDismissed()
- 位置: async L358-369
- 役割: 提案が却下済みかを返す。失敗時は false を返す。
- 触るとき: 却下済みの提案が表示される問題を調べるとき。
- 呼び出し先: `lowerSuggestion()`, `this.#store?.isDismissedBySuggestion()`, `this.logger.error()`

## SuggestBackendRust.isDismissedByKey()
- 位置: async L382-389
- 役割: 却下キーが登録済みかを返す。失敗時は false を返す。
- 触るとき: キー単位の却下判定を追うとき。
- 呼び出し先: `this.#store?.isDismissedByKey()`, `this.logger.error()`

## SuggestBackendRust.anyDismissedSuggestions()
- 位置: async L397-405
- 役割: 却下の記録が1件でもあるかを返す。失敗時は、あるかもしれないとして true を返す。
- 触るとき: about:preferences の復元ボタンなど、却下の有無で表示が変わる箇所を確かめるとき。
- 呼び出し先: `this.#store?.anyDismissedSuggestions()`, `this.logger.error()`

## SuggestBackendRust.clearDismissedSuggestions()
- 位置: async L410-416
- 役割: 全ての却下の記録を消す。失敗はログに出すだけ。
- 触るとき: 却下の全消去が効かないときに調べるとき。
- 呼び出し先: `this.#store?.clearDismissedSuggestions()`, `this.logger.error()`

## SuggestBackendRust.fetchGeonames()
- 位置: async L437-448
- 役割: ストアが無ければ空配列を返す。検索文字列、前方一致の有無、地名の種類、絞り込みをストアに渡して地名を取得する。
- 触るとき: 地名の候補を取る箇所(天気の都市など)を変えるとき。
- 呼び出し先: `this.#store.fetchGeonames()`
- 参照: `this.#store`

## SuggestBackendRust.fetchGeonameAlternates()
- 位置: async L466-469
- 役割: 地名の別名、行政区画、国の情報をストアから取得して返す。
- 触るとき: 天気の都市名などのローカライズ表記を変えるとき。
- 呼び出し先: `this.#store?.fetchGeonameAlternates()`

## SuggestBackendRust.notify()
- 位置: L474-477
- 役割: 取り込みタイマーの発火時に全体の取り込みを行う。
- 触るとき: 定期的な取り込みの頻度や動作を確かめるとき。
- 呼び出し先: `this.#ingestAll()`, `this.logger.info()`

## SuggestBackendRust.mergeProviderConstraints()
- 位置: L493-519
- 役割: 2つの制約を統合した新しいオブジェクトを返す。dynamicSuggestionTypes は和集合にして並べ替え、片方しか無ければその値を使う。片方が無ければもう片方を返す。
- 触るとき: 複数の機能が動的提案を共有するときの制約の統合を変えるとき。
- 呼び出し先: `a.hasOwnProperty()`, `b.hasOwnProperty()`
- 条件付き依存: `if (!(!a.dynamicSuggestionTypes || !b.dynamicSuggestionTypes))` → `a.dynamicSuggestionTypes.concat(b.dynamicSuggestionTypes).sort()`
- 条件付き依存: `if (!(!a.dynamicSuggestionTypes || !b.dynamicSuggestionTypes))` → `a.dynamicSuggestionTypes.concat()`
- 参照: `a.dynamicSuggestionTypes`, `b.dynamicSuggestionTypes`, `merged.dynamicSuggestionTypes`

## SuggestBackendRust.#storeDataPath()
- 位置: L528-533
- 役割: プロファイルフォルダー直下の suggest.sqlite のパスを返す。
- 触るとき: Rust のデータの保存場所を変えるとき。
- 呼び出し先: `PathUtils.join()`, `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("ProfD", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `Services.dirsvc`

## SuggestBackendRust.#enabledSuggestionTypes()
- 位置: L548-560
- 役割: 有効な Rust 種別の機能を集め、機能・種別名・プロバイダー番号の組の配列を返す。
- 触るとき: 問い合わせや取り込みの対象になる種別の決まり方を変えるとき。
- 条件付き依存: `if (feature.isEnabled)` → `this.#providerFromSuggestionType()`
- 条件付き依存: `if (provider)` → `items.push()`
- 参照: `feature.isEnabled`, `feature.rustSuggestionType`, `lazy.QuickSuggest.rustFeatures`

## SuggestBackendRust.#init()
- 位置: L562-614
- 役割: ストアを作り、終了時のブロッカーを登録し、取り込みタイマーを登録する。続けて全種別の取り込みを行い、旧形式の却下データを移行したあとに通知を出す。
- 触るとき: 有効化時の初期化の順序や、定期取り込みの設定を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.getIntPref()`, `lazy.AsyncShutdown.profileChangeTeardown.addBlocker()`, `lazy.UrlbarPrefs.get()`, `lazy.timerManager.registerTimer()`, `this.#ingestAll()`, `this.#makeStore()`, `this.#migrateBlockedDigests()`, `this.#migrateBlockedDigests().then()`, `this.logger.debug()`
- 参照: `this.#shutdownBlocker`, `this.#store`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#shutdownBlocker()
- 位置: L576-588
- 役割: 終了時に読み書きの中断を要求し、ストアの参照を null にして SQLite を早めに閉じる。
- 触るとき: 終了時の書き込みの遅れで警告が出るなど、終了処理の順序を調べるとき。
- 呼び出し先: `this.#store?.interrupt()`
- 参照: `lazy.InterruptKind.READ_WRITE`, `this.#shutdownBlocker`, `this.#store`

## SuggestBackendRust.#makeStore()
- 位置: L616-645
- 役割: リモート設定のサービスが無ければ null を返す。データパスと FTS5 拡張を指定して SuggestStore を作り、失敗時はログを出して null を返す。
- 触るとき: ストアの作成条件や読み込む拡張を変えるとき。
- 呼び出し先: `builder.build()`, `lazy.SuggestStoreBuilder.init()`, `lazy.SuggestStoreBuilder.init() .dataPath()`, `lazy.SuggestStoreBuilder.init() .dataPath(this.#storeDataPath) .remoteSettingsService()`, `this.logger.error()`, `this.logger.info()`
- 参照: `AppConstants.SQLITE_LIBRARY_FILENAME`, `this.#remoteSettingsService`, `this.#storeDataPath`

## SuggestBackendRust.#uninit()
- 位置: L647-657
- 役割: ストアを捨て、制約と設定のキャッシュを消し、取り込みタイマーを解除し、終了ブロッカーを外す。
- 触るとき: 無効化のあとに状態が残らないかを確かめるとき。
- 呼び出し先: `lazy.AsyncShutdown.profileChangeTeardown.removeBlocker()`, `lazy.timerManager.unregisterTimer()`, `this.#configsBySuggestionType.clear()`, `this.#providerConstraintsOnLastIngestByFeature.clear()`
- 参照: `this.#shutdownBlocker`, `this.#store`

## SuggestBackendRust.#ingestSuggestionType()
- 位置: L670-720
- 役割: 取り込みキューに、種別の取り込みと、その後のプロバイダー設定の取得を予約する。取り込みの所要時間をテレメトリに記録し、エラーはログに出す。
- 触るとき: 取り込みの失敗時の扱いや計測の内容を変えるとき。
- 呼び出し先: `Glean.suggest.ingestDownloadTime[label].accumulateSingleSample()`, `Glean.suggest.ingestTime[label].accumulateSingleSample()`, `this.#configsBySuggestionType.set()`, `this.#ingestQueue.queueIdleCallback()`, `this.#providerFromSuggestionType()`, `this.#store.fetchProviderConfig()`, `this.#store.ingest()`, `this.logger.debug()`, `this.logger.error()`
- 参照: `Glean.suggest.ingestDownloadTime`, `Glean.suggest.ingestTime`, `error.reason`, `lazy.SuggestIngestionConstraints`, `lazy.SuggestionProviderConstraints`, `metrics.downloadTimes`, `metrics.ingestionTimes`, `this.#store`

## SuggestBackendRust.#ingestAll()
- 位置: L722-737
- 役割: 有効な全ての Rust 機能を強制取り込みで予約し、グローバル設定の取得も予約する。
- 触るとき: 起動時や定期の全体取り込みの流れを変えるとき。
- 呼び出し先: `this.#ingestQueue.queueIdleCallback()`, `this.#store.fetchGlobalConfig()`, `this.ingestEnabledSuggestions()`, `this.logger.debug()`
- 参照: `lazy.QuickSuggest.rustFeatures`, `this.#config`, `this.#store`

## SuggestBackendRust.#providerFromSuggestionType()
- 位置: L749-758
- 役割: 種別名を大文字にして SuggestionProvider の値を引く。無ければエラーを記録して null を返す。
- 触るとき: JS 側の種別名と Rust のプロバイダーの対応が合わないとき。
- 呼び出し先: `lazy.SuggestionProvider.hasOwnProperty()`, `type.toUpperCase()`
- 条件付き依存: `if (!lazy.SuggestionProvider.hasOwnProperty(key))` → `this.logger.error()`
- 参照: `lazy.SuggestionProvider`

## SuggestBackendRust.#migrateBlockedDigests()
- 位置: async L766-793
- 役割: 旧形式の blockedDigests の pref を読み、あれば却下キーとして Rust に移行する。移行が成功してから pref を消す。pref が無ければ何もしない。
- 触るとき: 旧版から引き継ぐ却下データの移行を変えるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.getCharPref()`, `this.#migrateBlockedDigestsJson()`, `this.logger.debug()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `error.result`, `this.#store`
- XPCOM: `Services.prefs`

## SuggestBackendRust.#migrateBlockedDigestsJson()
- 位置: async L796-823
- 役割: JSON を解析し、配列の文字列の要素を却下キーとして登録する。解析できない、または配列でない場合は捨てる。
- 触るとき: 旧データの形式の扱いを変えるとき。
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Promise.all()`, `promises.push()`, `this.#store.dismissByKey()`, `this.logger.debug()`
- 条件付き依存: `if (!digests)` → `this.logger.debug()`
- 条件付き依存: `if (!Array.isArray(digests))` → `this.logger.debug()`

## SuggestBackendRust._test_store()
- 位置: L825-827
- 役割: テスト用に SuggestStore を返す。
- 触るとき: テストでストアに直接触るとき。
- 参照: `this.#store`

## SuggestBackendRust._test_enabledSuggestionTypes()
- 位置: L829-831
- 役割: テスト用に有効な種別の一覧を返す。
- 触るとき: テストで対象の種別を確かめるとき。
- 参照: `this.#enabledSuggestionTypes`

## SuggestBackendRust._test_setRemoteSettingsService()
- 位置: async L833-842
- 役割: テスト用にリモート設定のサービスを差し替える。有効なら取り込みの記録を消してストアを作り直し、取り込みの完了まで待つ。
- 触るとき: テストでモックのリモート設定サーバーを使うとき。
- 条件付き依存: `if (this.isEnabled)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (this.isEnabled)` → `this.#uninit()`
- 条件付き依存: `if (this.isEnabled)` → `this.#init()`
- 参照: `this.#remoteSettingsService`, `this.ingestPromise`, `this.isEnabled`
- XPCOM: `Services.prefs`

## SuggestBackendRust._test_ingest()
- 位置: async L844-847
- 役割: テスト用に全体の取り込みを行い、完了まで待つ。
- 触るとき: テストで取り込み後の状態を確かめるとき。
- 呼び出し先: `this.#ingestAll()`
- 参照: `this.ingestPromise`

## getSuggestionType()
- 位置: L876-909
- 役割: 提案のクラスを Suggestion の各サブクラスと照合して種別名を求める。結果はクラスごとにキャッシュする。見つからなければエラーを記録して undefined を返す。
- 触るとき: Rust から新しい提案種別が届いて認識されないときに確かめるとき。
- 呼び出し先: `gSuggestionTypesByCtor.get()`
- 条件付き依存: `if (!type)` → `Object.keys(lazy.Suggestion).find()`
- 条件付き依存: `if (!type)` → `Object.keys()`
- 条件付き依存: `if (type)` → `gSuggestionTypesByCtor.set()`
- 条件付き依存: `if (!(type))` → `console.error()`
- 参照: `lazy.Suggestion`, `suggestion.constructor`

## liftSuggestion()
- 位置: L930-951
- 役割: 動的提案の data が文字列なら JSON として解析し直し、新しい提案を作って返す。解析に失敗したら null を返す。他の提案はそのまま返す。
- 触るとき: 動的提案の payload の扱いを変えるとき。
- 条件付き依存: `if (typeof data == "string")` → `JSON.parse()`
- 参照: `lazy.Suggestion.Dynamic`, `suggestion.dismissalKey`, `suggestion.score`, `suggestion.suggestionType`

## lowerSuggestion()
- 位置: L967-982
- 役割: 動的提案の data を JSON 文字列に戻し、Rust に渡せる形の提案を作る。他の提案はそのまま返す。
- 触るとき: 動的提案を却下の登録で Rust に渡す前の変換を確かめるとき。
- 条件付き依存: `if (data !== null && data !== undefined)` → `JSON.stringify()`
- 参照: `lazy.Suggestion.Dynamic`, `suggestion.dismissalKey`, `suggestion.provider`, `suggestion.score`, `suggestion.suggestionType`
