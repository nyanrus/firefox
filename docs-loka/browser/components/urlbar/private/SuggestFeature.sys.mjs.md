# browser/components/urlbar/private/SuggestFeature.sys.mjs

source: browser/components/urlbar/private/SuggestFeature.sys.mjs
source-hash: 7b58b2bb0065a7ae202076ee2be774d2cc0daa90
lines: 472

## <module>
- 役割: Suggest の機能とバックエンドの基底クラス。pref の変化に応じて機能の有効・無効を切り替え、提案の種別ごとの処理(結果作成、メニュー、テレメトリ)は SuggestProvider が受け持つ。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SuggestFeature.enablingPreferences()
- 位置: L39-41
- 役割: 有効判定に使う pref や Nimbus 変数の名前の配列を返す。基底は空配列。
- 触るとき: 機能が有効にならない条件を追加・見直すとき。pref 名は browser.urlbar. からの相対名で書く。

## SuggestFeature.primaryUserControlledPreferences()
- 位置: L62-64
- 役割: 利用者が設定画面で直接切り替える pref の名前の配列を返す。基底は空配列。
- 触るとき: 設定画面に出す項目を機能ごとに追加するとき。

## SuggestFeature.shouldEnable()
- 位置: L74-76
- 役割: enablingPreferences の全てが真なら true を返す。サブクラスで条件を変えられ、Suggest 全体が有効なときだけ呼ばれる。
- 触るとき: 有効条件を単純な AND 以外にしたいとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.enablingPreferences.every()`

## SuggestFeature.enable()
- 位置: L86-86
- 役割: 基底では何もしない。有効状態が変わったときだけ呼ばれ、サブクラスが状態の初期化や後始末を行う。
- 触るとき: 機能の有効化・無効化の時にタイマーや参照を作る、または消す処理を追加するとき。

## SuggestFeature.logger()
- 位置: L94-101
- 役割: 'QuickSuggest.{name}' を接頭辞にしたロガーを初回に作り、以後は同じものを返す。
- 触るとき: 機能のログが出ない、または接頭辞が違うときに確かめるとき。
- 条件付き依存: `if (!this._logger)` → `lazy.UrlbarShared.getLogger()`
- 参照: `this._logger`, `this.name`

## SuggestFeature.isEnabled()
- 位置: L108-110
- 役割: 内部で保持している有効状態を返す。QuickSuggest が管理し、サブクラスは上書きしない。
- 触るとき: 機能が有効かどうかを、処理の前提として判定するとき。
- 参照: `this.#isEnabled`

## SuggestFeature.name()
- 位置: L116-118
- 役割: クラス名を返す。ログの接頭辞やバックエンドの識別に使われる。
- 触るとき: 機能の識別名が必要になるとき、またはクラス名を変えたときに影響範囲を確かめるとき。
- 参照: `this.constructor.name`

## SuggestFeature.update()
- 位置: L125-135
- 役割: quickSuggestEnabled が真で shouldEnable も真なら有効とみなす。現在の状態と違うときだけ状態を更新して enable() を呼ぶ。
- 触るとき: pref の変化で機能が有効・無効に切り替わる流れを追うとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (enable != this.isEnabled)` → `this.logger.info()`
- 条件付き依存: `if (enable != this.isEnabled)` → `this.enable()`
- 参照: `this.#isEnabled`, `this.isEnabled`, `this.shouldEnable`

## SuggestProvider.merinoProvider()
- 位置: L163-165
- 役割: Merino で提供される provider 名を返す。基底は空文字。
- 触るとき: Merino から来る提案をこの機能に結び付けるとき。

## SuggestProvider.rustSuggestionType()
- 位置: L174-176
- 役割: Rust コンポーネントの Suggestion 列挙の種別名を返す。基底は空文字。
- 触るとき: Rust 側の種別名と突き合わせるとき。

## SuggestProvider.dynamicRustSuggestionTypes()
- 位置: L185-187
- 役割: 動的 Rust 提案の suggestion_type の配列を返す。基底は空配列。rustSuggestionType が 'Dynamic' のときに使う。
- 触るとき: リモート設定の動的提案の種別を追加するとき。

## SuggestProvider.rustProviderConstraints()
- 位置: L197-204
- 役割: 動的種別があれば dynamicSuggestionTypes を持つ制約オブジェクトを返し、無ければ null を返す。
- 触るとき: Rust に渡す provider の制約を変えるとき。
- 参照: `this.dynamicRustSuggestionTypes`, `this.dynamicRustSuggestionTypes?.length`

## SuggestProvider.mlIntent()
- 位置: L212-214
- 役割: ML の intent 名(例: yelp_intent)を返す。基底は空文字。
- 触るとき: ML 提案をこの機能に結び付けるとき。

## SuggestProvider.isMlIntentEnabled()
- 位置: L222-224
- 役割: ML 提案を有効にするかを返す。基底は false。
- 触るとき: ML 提案の有効条件を機能ごとに決めるとき。

## SuggestProvider.getSuggestionTelemetryType()
- 位置: L240-242
- 役割: 提案のテレメトリ種別を返す。基底は merinoProvider をそのまま返す。
- 触るとき: テレメトリ種別が提案ごとに違う機能を作るとき、またはサブクラスの上書きを検討するとき。
- 参照: `this.merinoProvider`

## SuggestProvider.getResultCommands()
- 位置: L254-256
- 役割: 結果メニューのコマンドを返す。基底は undefined を返す。
- 触るとき: 結果メニューに項目を出す機能を作るとき。

## SuggestProvider.canShowLessFrequently()
- 位置: L264-266
- 役割: 「少なく表示」を出すかを返す。基底は false。
- 触るとき: 「少なく表示」に対応する機能を作るとき。

## SuggestProvider.incrementShowLessFrequentlyCount()
- 位置: L272-272
- 役割: 基底では何もしない。「少なく表示」の回数を増やす処理はサブクラスで行う。
- 触るとき: 「少なく表示」の回数を機能で数えるとき。

## SuggestProvider.isSuggestionSponsored()
- 位置: L284-286
- 役割: 提案がスポンサーかどうかを返す。基底は false。
- 触るとき: スポンサー提案を扱う機能で判定を書くとき。

## SuggestProvider.filterSuggestions()
- 位置: async L305-307
- 役割: 1クエリ分の提案をまとめて受け取り、表示するものだけを返す。基底は全件をそのまま返す。
- 触るとき: 複数の提案から一部を選ぶ条件がバックエンドの外にあるとき。

## SuggestProvider.makeResult()
- 位置: async L325-327
- 役割: 提案から UrlbarResult を作る。基底は null を返すので、各機能で実装する。
- 触るとき: 提案の表示内容を機能に追加・変更するとき。

## SuggestProvider.onImpression()
- 位置: L346-346
- 役割: 結果が表示されたまま検索セッションが終わったときに呼ばれる。基底は何もしない。
- 触るとき: 表示の計測を機能ごとに行うとき。

## SuggestProvider.onEngagement()
- 位置: L364-364
- 役割: 利用者が結果を操作したときに呼ばれる。基底は何もしない。
- 触るとき: メニュー操作や選択時の処理を機能に追加するとき。

## SuggestProvider.isUrlEquivalentToResultUrl()
- 位置: L382-384
- 役割: 履歴の URL と結果の URL が同じ元の提案を指すかを返す。基底は payload.url との完全一致で判定する。
- 触るとき: クエリごとに URL が変わる提案で、履歴との突き合わせを行うとき。
- 参照: `result.payload.url`

## SuggestProvider.handleShowLessFrequently()
- 位置: L399-408
- 役割: フィードバックの確認を出し、回数を増やす。上限に達していれば結果のメニューを作り直す。サブクラスの onEngagement から呼ぶ。
- 触るとき: 「少なく表示」の後にメニューの項目が消えないときに確かめるとき。
- 呼び出し先: `controller.view.acknowledgeFeedback()`, `this.incrementShowLessFrequentlyCount()`
- 条件付き依存: `if (!this.canShowLessFrequently)` → `controller.view.updateResultMenuCommands()`
- 条件付き依存: `if (!this.canShowLessFrequently)` → `this.getResultCommands()`
- 参照: `result.id`, `this.canShowLessFrequently`

## SuggestProvider.update()
- 位置: L414-417
- 役割: 基底の update の後、Rust バックエンドがあれば ingestEnabledSuggestions() を呼び、有効になった種別のデータを取り込む。
- 触るとき: 機能を有効にしたあとに Rust 側のデータが取り込まれないときに確かめるとき。
- 呼び出し先: `lazy.QuickSuggest.rustBackend?.ingestEnabledSuggestions()`, `super.update()`

## SuggestBackend.query()
- 位置: async L449-451
- 役割: 提案を取得して配列で返す。基底では例外を投げるので、サブクラスで実装する。
- 触るとき: 新しいバックエンドを追加するとき、または問い合わせの引数(queryContext、types)の扱いを変えるとき。

## SuggestBackend.cancelQuery()
- 位置: L457-457
- 役割: 基底は何もしない。問い合わせが取り消されたときの後始末をサブクラスで行う。
- 触るとき: 取り消された問い合わせの後始末が漏れていないか確かめるとき。

## SuggestBackend.onSearchSessionEnd()
- 位置: L470-470
- 役割: 検索セッションが終わったときに呼ばれる。基底は何もしない。
- 触るとき: セッション単位の状態をバックエンドで後始末するとき。
