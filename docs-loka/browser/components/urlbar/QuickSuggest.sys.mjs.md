# browser/components/urlbar/QuickSuggest.sys.mjs

source: browser/components/urlbar/QuickSuggest.sys.mjs
source-hash: ce4dc0f5e3af6b8a4efbb54031b1e6321e0b6b05
lines: 1331

## <module>
- 役割: Firefox Suggest(旧 Quick Suggest)の全体を管理する _QuickSuggest シングルトンと、地域・ロケールごとの既定 pref、設定 UI の値、user pref の移行処理を定義するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.entries()`, `Object.entries(REGION_LOCALE_DEFAULTS_EU_157_BOOLEAN).map()`, `Object.freeze()`, `Object.fromEntries()`, `Promise.withResolvers()`, `shouldOnlineBeAvailable()`

## _QuickSuggest.HELP_URL()
- 位置: L313-318
- 役割: app.support.baseURL に firefox-suggest を連結したヘルプ URL を返す。
- 触るとき: Suggest の設定画面や案内からヘルプへのリンク先が古い、または別トピックを指しているとき。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- 参照: `this.HELP_TOPIC`
- XPCOM: `Services.urlFormatter`

## _QuickSuggest.HELP_TOPIC()
- 位置: L324-326
- 役割: ヘルプのトピック名として固定値 firefox-suggest を返す。
- 触るとき: ヘルプのトピック名を変更する、または HELP_URL の行き先を確かめるとき。

## _QuickSuggest.SETTINGS_UI()
- 位置: L335-337
- 役割: モジュール内の SETTINGS_UI 定数(FULL=0、NONE=1、OFFLINE_ONLY=2)を返す。
- 触るとき: 設定画面に出す項目を変えたい、または quickSuggestSettingsUi の値の意味を確かめるとき。

## _QuickSuggest.SUGGEST_TOU_TIMESTAMP()
- 位置: L344-346
- 役割: Suggest の利用規約(ToU)の時刻(ミリ秒)を返す。
- 触るとき: ToU を承諾済みかの判定が想定より早く、または遅く切り替わるときに、基準時刻の値を確かめるとき。

## _QuickSuggest.initPromise()
- 位置: L352-354
- 役割: init() の完了で解決される Promise を返す。
- 触るとき: Suggest の初期化完了を待つ呼び出し元で、初期化前に読まれてしまうとき。
- 参照: `this.#initResolvers.promise`

## _QuickSuggest.enabledBackends()
- 位置: L360-368
- 役割: Rust、Merino、ML の各バックエンドのうち、isEnabled が真のものだけを配列で返す。
- 触るとき: どのバックエンドで候補を取得しているか、または init 前に呼ばれたときの null 扱いを調べるとき。
- 呼び出し先: `this.#featuresByName.get()`
- 参照: `b?.isEnabled`, `this.rustBackend`

## _QuickSuggest.rustBackend()
- 位置: L374-376
- 役割: SuggestBackendRust の機能インスタンスを返す。
- 触るとき: Rust コンポーネントへの問い合わせ先を探すとき、rustBackend が未登録の時点で null が返る点を確かめるとき。
- 呼び出し先: `this.#featuresByName.get()`

## _QuickSuggest.config()
- 位置: L384-386
- 役割: Rust バックエンドが取り込んだ remote settings の設定を返す。無ければ空オブジェクト。
- 触るとき: Suggest のグローバル設定(remote settings 由来)の値を読みたいとき。
- 参照: `this.rustBackend?.config`

## _QuickSuggest.impressionCaps()
- 位置: L392-394
- 役割: ImpressionCaps 機能のインスタンスを返す。
- 触るとき: 表示回数の上限(impression caps)の判定にアクセスするとき。
- 呼び出し先: `this.#featuresByName.get()`

## _QuickSuggest.rustFeatures()
- 位置: L401-406
- 役割: rustSuggestionType を持つ機能と、動的な rust 種別を持つ機能を合わせた Set を返す。
- 触るとき: Rust が扱う候補種別をすべて洗い出すとき、新しい Rust 種別を登録した後に漏れがないか確かめるとき。
- 呼び出し先: `this.#featuresByDynamicRustSuggestionType.values()`, `this.#featuresByRustSuggestionType.values()`

## _QuickSuggest.mlFeatures()
- 位置: L413-415
- 役割: mlIntent を持つ機能の Set を返す。
- 触るとき: ML による候補の意図(intent)に対応する機能を一覧したいとき。
- 呼び出し先: `this.#featuresByMlIntent.values()`

## _QuickSuggest.logger()
- 位置: L417-422
- 役割: QuickSuggest 接頭辞付きのロガーを初回だけ作って返す。
- 触るとき: Suggest のログ出力を追いたい、またはログ接頭辞を変えるとき。
- 条件付き依存: `if (!this._logger)` → `lazy.UrlbarShared.getLogger()`
- 参照: `this._logger`

## _QuickSuggest.init()
- 位置: async L430-495
- 役割: Region、Nimbus、TelemetryEnvironment の準備を待ってから prefs を初期化し、FEATURES の各機能を生成して登録する。最後に updateAll と pref オブザーバーの登録を行う。2回目以降の呼び出しは完了を待つだけ。
- 触るとき: Suggest の起動順序(地域、Nimbus、テレメトリの待ち合わせ)が原因で候補が出ない、または機能の登録漏れを調べるとき。
- 呼び出し先: `ChromeUtils.importESModule()`, `Object.entries()`, `lazy.NimbusFeatures.urlbar.ready()`, `lazy.Region.init()`, `lazy.UrlbarPrefs.addObserver()`, `this.#featuresByName.set()`, `this.#initPrefs()`, `this.#initResolvers.resolve()`, `this.#updateAll()`
- 条件付き依存: `if (!this._testSkipTelemetryEnvironmentInit)` → `lazy.TelemetryEnvironment.onInitialized()`
- 条件付き依存: `if (feature.merinoProvider)` → `this.#featuresByMerinoProvider.set()`
- 条件付き依存: `if (feature.dynamicRustSuggestionTypes?.length)` → `this.#featuresByDynamicRustSuggestionType.set()`
- 条件付き依存: `if (!(feature.dynamicRustSuggestionTypes?.length))` → `this.#featuresByRustSuggestionType.set()`
- 条件付き依存: `if (feature.mlIntent)` → `this.#featuresByMlIntent.set()`
- 条件付き依存: `if (prefs)` → `this.#featuresByEnablingPrefs.get()`
- 条件付き依存: `if (!features)` → `this.#featuresByEnablingPrefs.set()`
- 条件付き依存: `if (prefs)` → `features.add()`
- 参照: `feature.dynamicRustSuggestionTypes`, `feature.dynamicRustSuggestionTypes?.length`, `feature.enablingPreferences`, `feature.merinoProvider`, `feature.mlIntent`, `feature.rustSuggestionType`, `this.#initStarted`, `this._testSkipTelemetryEnvironmentInit`, `this.initPromise`

## _QuickSuggest.getFeature()
- 位置: L505-507
- 役割: クラス名を指定して機能インスタンスを取り出す。
- 触るとき: 特定の Suggest 機能(例 AmpSuggestions)の状態や設定に、名前から直接アクセスしたいとき。
- 呼び出し先: `this.#featuresByName.get()`

## _QuickSuggest.getFeatureByMlIntent()
- 位置: L519-521
- 役割: ML の intent 名から対応する機能を返す。見つからなければ undefined。
- 触るとき: ML が返した intent がどの機能に届くかを確かめるとき。
- 呼び出し先: `this.#featuresByMlIntent.get()`

## _QuickSuggest.getFeatureByResult()
- 位置: L531-533
- 役割: 結果の payload を使って、その結果を管理する機能を返す。
- 触るとき: ある urlbar 結果がどの Suggest 機能に属するかを特定して、その挙動を確かめたいとき。
- 呼び出し先: `this.getFeatureBySource()`
- 参照: `result.payload`

## _QuickSuggest.getFeatureBySource()
- 位置: L560-577
- 役割: source(merino、rust、ml)ごとに、対応する機能を引く。rust の Dynamic 種別は動的な種別表を先に見る。該当がなければ null。
- 触るとき: 候補の source や provider 名から機能が見つからず、結果の扱いが決まらないとき。
- 呼び出し先: `this.#featuresByMerinoProvider.get()`, `this.#featuresByRustSuggestionType.get()`, `this.getFeatureByMlIntent()`
- 条件付き依存: `if (provider == "Dynamic" && suggestionType)` → `this.#featuresByDynamicRustSuggestionType.get()`

## _QuickSuggest.dismissResult()
- 位置: async L586-599
- 役割: rust 由来の結果は Rust の dismissRustSuggestion、その他は dismissalKey で dismissByKey を呼び、最後に dismissals-changed を通知する。
- 触るとき: 候補を非表示にしても再表示される、または非表示の登録先が合わないとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (result.payload.source == "rust")` → `this.rustBackend?.dismissRustSuggestion()`
- 条件付き依存: `if (!(result.payload.source == "rust"))` → `getDismissalKey()`
- 条件付き依存: `if (key)` → `this.rustBackend?.dismissByKey()`
- 参照: `result.payload.source`, `result.payload.suggestionObject`
- XPCOM: `Services.obs`

## _QuickSuggest.isResultDismissed()
- 位置: async L609-633
- 役割: 旧方式の URL ダイジェストと、新方式(rust の個別判定またはキー判定)の両方を調べ、どれか一つでも真なら非表示とみなす。
- 触るとき: 非表示にした候補がまだ出る、または旧方式の URL 判定が新方式と食い違うときに調べるとき。
- 呼び出し先: `Promise.all()`, `getDigest()`, `getDigest(result.payload.originalUrl || result.payload.url).then()`, `this.rustBackend?.isDismissedByKey()`, `values.some()`
- 条件付き依存: `if (result.payload.source == "rust")` → `promises.push()`
- 条件付き依存: `if (result.payload.source == "rust")` → `this.rustBackend?.isRustSuggestionDismissed()`
- 条件付き依存: `if (!(result.payload.source == "rust"))` → `getDismissalKey()`
- 条件付き依存: `if (key)` → `promises.push()`
- 条件付き依存: `if (key)` → `this.rustBackend?.isDismissedByKey()`
- 参照: `result.payload.originalUrl`, `result.payload.source`, `result.payload.suggestionObject`, `result.payload.url`

## _QuickSuggest.clearDismissedSuggestions()
- 位置: async L645-672
- 役割: 各機能の primaryUserControlledPreferences のうち false のものの user 値を消し、Rust 側の個別の非表示もまとめて消して、通知を2つ送る。
- 触るとき: 「非表示をすべて元に戻す」の動作が一部の種別だけ戻らないとき、消す対象の pref を確かめるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.UrlbarPrefs.get()`, `this.logger.error()`, `this.rustBackend?.clearDismissedSuggestions()`
- 条件付き依存: `if (pref && !lazy.UrlbarPrefs.get(pref))` → `lazy.UrlbarPrefs.clear()`
- 参照: `feature.primaryUserControlledPreferences`, `this.#featuresByName`
- XPCOM: `Services.obs`

## _QuickSuggest.canClearDismissedSuggestions()
- 位置: async L681-715
- 役割: primaryUserControlledPreferences のいずれかが false かつ user 値を持つか、Rust に個別の非表示があれば真を返す。
- 触るとき: 「非表示をクリア」ボタンが有効にならない、または逆に常に有効なままになるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.hasUserValue()`, `this.logger.error()`, `this.rustBackend?.anyDismissedSuggestions()`
- 参照: `feature.primaryUserControlledPreferences`, `this.#featuresByName`

## _QuickSuggest.intendedDefaultPrefs()
- 位置: L728-749
- 役割: SUGGEST_PREFS の defaultValues から、指定の地域とロケールに当てはまる既定値を求め、firefox.js 由来の既定値に上書きした結果を返す。
- 触るとき: 特定の地域やロケールで Suggest の既定値が想定と違うとき、地域・ロケール表のどの行が効くかを調べるとき。
- 呼び出し先: `Object.entries()`, `Object.entries(SUGGEST_PREFS) .map()`, `Object.fromEntries()`, `defaultValues?.hasOwnProperty()`
- 条件付き依存: `if (defaultValues?.hasOwnProperty(region))` → `enablingLocales.includes()`
- 条件付き依存: `if (typeof prefValue == "function")` → `prefValue()`
- 参照: `this.#unmodifiedDefaultPrefs`

## _QuickSuggest.onPrefChanged()
- 位置: L757-782
- 役割: ToU の承諾日の pref が変わったら prefs を再初期化する。さらに、その pref を有効化条件に持つ機能の update を呼び、主要な設定 pref なら非表示の変更通知を送る。
- 触るとき: Suggest の pref を変えても対応する機能が再評価されない、または ToU 承諾直後に既定値が切り替わらないとき。
- 呼び出し先: `f.primaryUserControlledPreferences.includes()`, `f.update()`, `this.#featuresByEnablingPrefs.get()`
- 条件付き依存: `if (pref == lazy.TelemetryReportingPolicy.TOU_ACCEPTED_DATE_PREF)` → `this.#initPrefs()`
- 条件付き依存: `if (isPrimaryUserControlledPref)` → `Services.obs.notifyObservers()`
- 参照: `lazy.TelemetryReportingPolicy.TOU_ACCEPTED_DATE_PREF`
- XPCOM: `Services.obs`

## _QuickSuggest.onNimbusChanged()
- 位置: L790-797
- 役割: 変わった Nimbus 変数に対応する UI pref の既定値を同期してから、全機能を更新する。
- 触るとき: Nimbus の実験値を変えたのに Suggest の設定が反映されないとき。
- 呼び出し先: `this.#syncNimbusVariablesToUiPrefs()`, `this.#updateAll()`

## _QuickSuggest.isUrlEquivalentToResultUrl()
- 位置: L817-822
- 役割: 結果の機能が判定を持つならそれに任せ、なければ URL が結果の URL と完全一致するかを返す。
- 触るとき: 履歴の URL と候補の URL を同じ提案とみなす条件(クエリ付き URL など)を変えたいとき。
- 呼び出し先: `feature.isUrlEquivalentToResultUrl()`, `this.getFeatureByResult()`
- 参照: `result.payload.url`

## _QuickSuggest.getFullKeywordTitleAndHighlights()
- 位置: L846-858
- 役割: fullKeyword があれば「キーワード — タイトル」の形の表示文字列と、キーワード部分だけのハイライトを返す。なければタイトルをそのまま使い、ハイライトは付けない。
- 触るとき: 完全キーワードを表示する候補の文字列や強調の範囲がずれるとき。
- 呼び出し先: `lazy.UrlbarShared.getTokenMatches()`

## _QuickSuggest.#uiPrefsByNimbusVariable()
- 位置: L866-876
- 役割: SUGGEST_PREFS のうち nimbusVariableIfExposedInUi を持つものを、変数名から pref 名への対応表にする。
- 触るとき: 設定 UI に出ている pref と Nimbus 変数の対応関係を確かめるとき。
- 呼び出し先: `Object.entries()`, `Object.entries(SUGGEST_PREFS) .map()`, `Object.fromEntries()`

## _QuickSuggest.#initPrefs()
- 位置: L886-992
- 役割: 地域とロケールに応じて既定値を既定ブランチに設定し、UI 用の pref は Nimbus の値で上書きし、最後にユーザー設定の移行を実行する。テスト用の上書きも受け付ける。
- 触るとき: Suggest の既定値の決まり方や、ユーザー設定が移行で消えないかを確かめるとき。
- 呼び出し先: `Object.entries()`, `defaults.set()`, `this.#ensureUserPrefsMigrated()`, `this.#syncNimbusVariablesToUiPrefs()`
- 条件付き依存: `if (!this.#unmodifiedDefaultPrefs)` → `Object.fromEntries()`
- 条件付き依存: `if (!this.#unmodifiedDefaultPrefs)` → `Object.keys(SUGGEST_PREFS).map()`
- 条件付き依存: `if (!this.#unmodifiedDefaultPrefs)` → `Object.keys()`
- 条件付き依存: `if (!this.#unmodifiedDefaultPrefs)` → `defaults.get()`
- 条件付き依存: `if (!(testOverrides?.defaultPrefs))` → `this.intendedDefaultPrefs()`
- 参照: `Services.locale.appLocaleAsBCP47`, `lazy.Preferences`, `lazy.Region.home`, `testOverrides.defaultPrefs`, `testOverrides?.defaultPrefs`, `testOverrides?.locale`, `testOverrides?.region`, `this.#intendedDefaultPrefs`, `this.#unmodifiedDefaultPrefs`
- XPCOM: `Services.locale`

## _QuickSuggest.#syncNimbusVariablesToUiPrefs()
- 位置: L1002-1026
- 役割: UI 用の pref の既定値を、Nimbus の値(未定義なら既定の値)で既定ブランチに設定する。変数名を渡すとその一件だけを対象にする。
- 触るとき: Nimbus で設定を変えた結果が、設定画面の既定の表示に反映されないとき。
- 呼び出し先: `Object.entries()`, `defaults.set()`, `lazy.NimbusFeatures.urlbar.getVariable()`
- 条件付き依存: `if (variable)` → `prefsByVariable.hasOwnProperty()`
- 参照: `lazy.Preferences`, `this.#intendedDefaultPrefs`, `this.#uiPrefsByNimbusVariable`

## _QuickSuggest.#updateAll()
- 位置: L1031-1040
- 役割: 登録されている全機能の update を呼ぶ。Nimbus の fallback pref が変わるたびに呼ばれる。
- 触るとき: pref の変更後に機能の有効・無効が更新されないとき、呼び出しの頻度を見直すとき。
- 呼び出し先: `feature.update()`, `this.#featuresByName.values()`

## _QuickSuggest.MIGRATION_VERSION()
- 位置: L1047-1049
- 役割: 現在の pref 移行バージョン(7)を返す。
- 触るとき: 新しい移行を追加するときに、この値をいくつに上げるかを確かめるとき。

## _QuickSuggest.#ensureUserPrefsMigrated()
- 位置: L1061-1094
- 役割: 記録済みの移行バージョンから現在のバージョンまで、_migrateUserPrefsTo_N を順に呼ぶ。途中で例外が出たら止めて、そこまでのバージョンを記録する。
- 触るとき: アップデート後にユーザーの Suggest 設定が想定通りに移らないとき、どの移行が走ったかを追うとき。
- 呼び出し先: `Math.max()`, `Services.prefs.getBranch()`, `console.error()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`, `this[methodName]()`
- 参照: `testOverrides.migrationVersion`, `testOverrides?.migrationVersion`, `this.MIGRATION_VERSION`
- XPCOM: `Services.prefs`

## _QuickSuggest._migrateUserPrefsTo_1()
- 位置: L1096-1134
- 役割: suggest.quicksuggest を nonsponsored に移す。Suggest が有効な地域で nonsponsored の user 値が false なら、sponsored の user 値を false にする。
- 触るとき: 旧 suggest.quicksuggest の値が引き継がれず、スポンサー候補の表示が変わってしまったとき。
- 呼び出し先: `userBranch.getBoolPref()`, `userBranch.prefHasUserValue()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest"))` → `userBranch.setBoolPref()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest"))` → `userBranch.getBoolPref()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest"))` → `userBranch.clearUserPref()`
- 条件付き依存: `if ( shouldEnableSuggest && userBranch.prefHasUserValue("suggest.quicksuggest.nonsponsored") && !userBranch.getBoolPref("suggest.quicksuggest.nonsponsored") )` → `userBranch.setBoolPref()`

## _QuickSuggest._migrateUserPrefsTo_2()
- 位置: L1136-1156
- 役割: scenario が online のユーザーで nonsponsored と sponsored の user 値が無ければ false を入れて、既定の有効化で勝手に有効にならないようにする。
- 触るとき: online の既存ユーザーにだけ候補が増えた、または逆に消えたように見えるとき。
- 呼び出し先: `userBranch.getCharPref()`
- 条件付き依存: `if (scenario == "online")` → `userBranch.prefHasUserValue()`
- 条件付き依存: `if (!userBranch.prefHasUserValue("suggest.quicksuggest.nonsponsored"))` → `userBranch.setBoolPref()`
- 条件付き依存: `if (!userBranch.prefHasUserValue("suggest.quicksuggest.sponsored"))` → `userBranch.setBoolPref()`

## _QuickSuggest._migrateUserPrefsTo_3()
- 位置: L1158-1163
- 役割: 処理は無い。旧版で settingsUi を設定していたが、v4 で全員クリアされるため何もしない。
- 触るとき: バージョン 3 の移行で何かを変えたい、または欠番の理由を確かめるとき。

## _QuickSuggest._migrateUserPrefsTo_4()
- 位置: L1165-1170
- 役割: quicksuggest.settingsUi の user 値を消して既定値に戻す。
- 触るとき: 設定画面の Suggest 項目の表示が既定と違うユーザーがいるとき、この移行で既定に戻された経緯を確かめるとき。
- 呼び出し先: `userBranch.clearUserPref()`

## _QuickSuggest._migrateUserPrefsTo_5()
- 位置: L1172-1195
- 役割: DE、FR、IT の en ロケールで、誤って false になった sponsored の user 値を消す。
- 触るとき: その地域の en ユーザーで sponsored が無効のままになっているとき。
- 呼び出し先: `EN_LOCALES.includes()`, `["DE", "FR", "IT"].includes()`
- 条件付き依存: `if ( ["DE", "FR", "IT"].includes(lazy.Region.home) && EN_LOCALES.includes(Services.locale.appLocaleAsBCP47) )` → `userBranch.clearUserPref()`
- 参照: `Services.locale.appLocaleAsBCP47`, `lazy.Region.home`
- XPCOM: `Services.locale`

## _QuickSuggest._migrateUserPrefsTo_6()
- 位置: L1197-1214
- 役割: nonsponsored の user 値を新しい suggest.quicksuggest.all にコピーする。nonsponsored の値は残す。
- 触るとき: 非スポンサー候補の表示が Firefox 146 以降で変わったとき、all への引き継ぎを確かめるとき。
- 呼び出し先: `userBranch.prefHasUserValue()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest.nonsponsored"))` → `userBranch.setBoolPref()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest.nonsponsored"))` → `userBranch.getBoolPref()`

## _QuickSuggest._migrateUserPrefsTo_7()
- 位置: L1216-1240
- 役割: addons.minKeywordLength と showLessFrequentlyCount の片方だけに user 値があるとき、もう片方を補って「少なく表示」の挙動を揃える。
- 触るとき: アドオン候補の「表示を減らす」の結果が、ユーザーごとに違って見えるとき。
- 呼び出し先: `userBranch.prefHasUserValue()`
- 条件付き依存: `if ( userBranch.prefHasUserValue("addons.minKeywordLength") && !userBranch.prefHasUserValue("addons.showLessFrequentlyCount") )` → `userBranch.setIntPref()`
- 条件付き依存: `if (!( userBranch.prefHasUserValue("addons.minKeywordLength") && !userBranch.prefHasUserValue("addons.showLessFrequentlyCount") ))` → `userBranch.prefHasUserValue()`
- 条件付き依存: `if ( !userBranch.prefHasUserValue("addons.minKeywordLength") && userBranch.prefHasUserValue("addons.showLessFrequentlyCount") )` → `userBranch.setIntPref()`

## _QuickSuggest._test_reset()
- 位置: async L1242-1257
- 役割: テスト用に、初期化済みなら待ってから、prefs の再初期化と全機能の更新を行い、Rust の取り込み完了まで待つ。
- 触るとき: テストで Suggest の状態を初期化し直すとき、取り込み待ちが足りずテストが不安定になるとき。
- 呼び出し先: `this.#initPrefs()`, `this.#updateAll()`
- 参照: `this.#initStarted`, `this.initPromise`, `this.rustBackend`, `this.rustBackend.ingestPromise`

## userAcceptedSuggestToU()
- 位置: L1298-1301
- 役割: ToU の承諾日が Suggest の ToU 時刻以降かを返す。
- 触るとき: ToU 承諾の判定で、オンライン機能が有効にならないとき。
- 呼び出し先: `date.getTime()`
- 参照: `lazy.TelemetryReportingPolicy.termsOfUseAcceptedDate`

## shouldOnlineBeAvailable()
- 位置: L1311-1313
- 役割: 地域や言語を除いて、オンライン機能が利用可能かを ToU 承諾の有無だけで返す。
- 触るとき: オンライン向けの既定値(US の online 系 pref)が切り替わる条件を確かめるとき。
- 呼び出し先: `userAcceptedSuggestToU()`

## getDismissalKey()
- 位置: L1315-1321
- 役割: 結果の dismissalKey、originalUrl、url の順に最初にある値を返す。
- 触るとき: 同じ候補の非表示キーがずれて、非表示が効かないとき。
- 参照: `result.payload.dismissalKey`, `result.payload.originalUrl`, `result.payload.url`

## getDigest()
- 位置: async L1323-1328
- 役割: 文字列を UTF-8 にして SHA-1 を計算し、16進数の文字列にして返す。
- 触るとき: 旧方式の URL ダイジェストによる非表示判定の値が合わないとき。
- 呼び出し先: `Array.from()`, `Array.from(hashArray, b => b.toString(16).padStart(2, "0")).join()`, `b.toString()`, `b.toString(16).padStart()`, `crypto.subtle.digest()`, `new TextEncoder().encode()`
