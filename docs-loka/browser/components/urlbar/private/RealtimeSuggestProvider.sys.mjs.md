# browser/components/urlbar/private/RealtimeSuggestProvider.sys.mjs

source: browser/components/urlbar/private/RealtimeSuggestProvider.sys.mjs
source-hash: d8afa268f0f4b9b7ae053e4427e02cde0cc81160
lines: 708

## <module>
- 役割: リアルタイム提案(市況や天気などの種別)の共通基盤。種別ごとのサブクラスが表示と設定を定め、オプトイン tip と Merino のオンライン結果を切り替える。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## RealtimeSuggestProvider.realtimeType()
- 位置: L36-38
- 役割: 種別名を返す。基底では例外を投げるので、サブクラスで必ず上書きする。
- 触るとき: 新しいリアルタイム種別を追加するとき、または種別名が設定 pref や Merino の provider 名に波及する箇所を確かめるとき。

## RealtimeSuggestProvider.getViewTemplateForDescriptionTop()
- 位置: L40-42
- 役割: 説明の上段の要素テンプレートを返す。基底では例外を投げるので、サブクラスで実装する。
- 触るとき: 新しい種別の上段表示を作るとき。

## RealtimeSuggestProvider.getViewTemplateForDescriptionBottom()
- 位置: L44-46
- 役割: 説明の下段の要素テンプレートを返す。基底では例外を投げるので、サブクラスで実装する。
- 触るとき: 新しい種別の下段表示を作るとき。

## RealtimeSuggestProvider.getViewUpdateForPayloadItem()
- 位置: L48-50
- 役割: payload の1項目から要素の更新内容を返す。基底では例外を投げるので、サブクラスで実装する。
- 触るとき: 項目の表示文字列や画像を種別ごとに差し替えるとき。

## RealtimeSuggestProvider.dynamicRustSuggestionTypes()
- 位置: L60-62
- 役割: オプトイン用の Rust 動的提案種別として '{realtimeType}_opt_in' を含む配列を返す。
- 触るとき: オプトイン提案の Rust 側の種別名を変えるとき、または Rust 側の定義と突き合わせるとき。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.merinoProvider()
- 位置: L69-71
- 役割: Merino の provider 名を返す。既定では realtimeType と同じ。
- 触るとき: Merino 側の provider 名が種別名と違う種別を扱うとき。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.baseTelemetryType()
- 位置: L73-75
- 役割: テレメトリに使う基本の種別名として realtimeType を返す。
- 触るとき: テレメトリの種別名が想定と違うとき。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.realtimeTypeForFtl()
- 位置: L77-79
- 役割: realtimeType の大文字の前にハイフンを入れて小文字にし、Fluent の ID に使う形にする。
- 触るとき: 新しい種別の Fluent メッセージ ID が見つからないとき。
- 呼び出し先: `this.realtimeType.replace()`, `this.realtimeType.replace(/([A-Z])/g, "-$1").toLowerCase()`

## RealtimeSuggestProvider.featureGatePref()
- 位置: L81-83
- 役割: 機能ゲートの pref 名 '{realtimeType}FeatureGate' を返す。
- 触るとき: 種別の機能ゲート pref の名前の規則を変えるとき。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.suggestPref()
- 位置: L85-87
- 役割: 利用者が種別ごとに on/off する pref 名 'suggest.{realtimeType}' を返す。
- 触るとき: 種別の表示設定が効かないときに対応する pref を確かめるとき。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.minKeywordLengthPref()
- 位置: L89-91
- 役割: 最小キーワード長の pref 名 '{realtimeType}.minKeywordLength' を返す。
- 触るとき: 最小キーワード長の pref を種別ごとに読み書きする箇所を追うとき。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.showLessFrequentlyCountPref()
- 位置: L93-95
- 役割: 「少なく表示」の回数の pref 名 '{realtimeType}.showLessFrequentlyCount' を返す。
- 触るとき: 「少なく表示」の回数を種別ごとに保存する箇所を追うとき。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.optInIcon()
- 位置: L97-99
- 役割: オプトイン tip のアイコンとして chrome の illustrations 配下の '{realtimeType}-opt-in.svg' の URL を返す。
- 触るとき: オプトインの画像を差し替えるとき、または画像が出ないときに確認するとき。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.optInTitleL10n()
- 位置: L101-105
- 役割: オプトイン tip のタイトルの Fluent ID 'urlbar-result-{ftl名}-opt-in-title' を返す。
- 触るとき: オプトインのタイトル文言を種別ごとに変えるとき。
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.optInDescriptionL10n()
- 位置: L107-112
- 役割: オプトイン tip の説明の Fluent ID 'urlbar-result-{ftl名}-opt-in-description' を、マークアップ解釈ありで返す。
- 触るとき: オプトインの説明文の表示を変えるとき。
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.notInterestedCommandL10n()
- 位置: L114-118
- 役割: 結果メニューの「表示しない」の Fluent ID 'urlbar-result-menu-dont-show-{ftl名}2' を返す。
- 触るとき: 結果メニューの「表示しない」の文言が種別ごとに正しく出るか確かめるとき。
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.acknowledgeDismissalL10n()
- 位置: L120-124
- 役割: 削除時の確認文の Fluent ID 'urlbar-result-dismissal-acknowledgment-{ftl名}' を返す。
- 触るとき: 削除後の確認文が出ない、または違う文言になるときに確かめるとき。
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.ariaGroupL10n()
- 位置: L126-131
- 役割: 項目が複数のときの group の aria-label 用 Fluent ID 'urlbar-result-aria-group-{ftl名}' を返す。
- 触るとき: スクリーンリーダーに読まれるグループ名を種別ごとに変えるとき。
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.isSponsored()
- 位置: L133-135
- 役割: 既定でスポンサーではない false を返す。個々の提案が判定値を持たないときの fallback になる。
- 触るとき: スポンサー扱いの種別を作るとき、またはスポンサー判定の既定値を確かめるとき。

## RealtimeSuggestProvider.dynamicResultType()
- 位置: L147-149
- 役割: payload の dynamicType として 'realtime-{realtimeType}' を返す。
- 触るとき: 動的結果の種別名を変えるとき。CSS がこの 'realtime-' 接頭辞に依存している点に注意する。
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.rustSuggestionType()
- 位置: L153-155
- 役割: Rust の提案種別として 'Dynamic' を返す。
- 触るとき: Rust 側の動的提案をこの種別で受けるかを見直すとき。

## RealtimeSuggestProvider.enablingPreferences()
- 位置: L157-176
- 役割: 提案の有効判定に使う pref の一覧を返す。全体の on/off、オプトイン関係、オンライン可否、オンライン設定、機能ゲート、種別の設定、スポンサー表示の設定を含む。
- 触るとき: 種別が出ないときにどの pref が条件になっているかを調べるとき、または有効条件を増やすとき。
- 参照: `this.featureGatePref`, `this.suggestPref`

## RealtimeSuggestProvider.primaryUserControlledPreferences()
- 位置: L178-186
- 役割: 利用者が設定画面で直接操作する pref を返す。オプトイン関係の pref と種別の設定 pref を含む。
- 触るとき: 設定画面に出す項目を種別ごとに見直すとき。
- 参照: `this.suggestPref`

## RealtimeSuggestProvider.shouldEnable()
- 位置: L188-232
- 役割: 機能ゲート、オンライン可否、全体の on/off のいずれかがオフなら false。オンライン有効時は種別の設定値を返す。未有効時はオプトインの状態を見て、無効化・種別の削除・「あとで」の期間内のいずれかなら false、それ以外は true を返す。
- 触るとき: オプトインの段階から提案を表示し始める条件や、「あとで」の再表示期間の扱いを変えるとき。
- 呼び出し先: `Date.now()`, `dismissTypes.has()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("quicksuggest.online.enabled"))` → `lazy.UrlbarPrefs.get()`
- 参照: `this.featureGatePref`, `this.realtimeType`, `this.suggestPref`

## RealtimeSuggestProvider.isSuggestionSponsored()
- 位置: L234-248
- 役割: 提案の出どころで判定する。Merino は is_sponsored、Rust は payload の isSponsored を見て、どちらも無ければこの種別の isSponsored を返す。
- 触るとき: 個々の提案のスポンサー判定がずれるとき。
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`, `suggestion.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.isSponsored`, `suggestion.is_sponsored`, `suggestion.source`, `this.isSponsored`

## RealtimeSuggestProvider.getSuggestionTelemetryType()
- 位置: L269-283
- 役割: Merino の提案は telemetry_type があればそれを、無ければ基本の種別名を返す。Rust の提案は payload の telemetryType があればそれを、無ければ '_opt_in' を付けた名前を返す。
- 触るとき: オプトインとオンラインの提案のテレメトリ種別が想定と違うとき。
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`, `suggestion.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.telemetryType`, `suggestion.source`, `suggestion.telemetry_type`, `this.baseTelemetryType`

## RealtimeSuggestProvider.filterSuggestions()
- 位置: L285-292
- 役割: オンライン提案が有効なら Merino の提案だけを残し、無効ならすべて残す。
- 触るとき: オプトイン提案とオンライン提案が同時に出てしまう問題を調べるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("quicksuggest.online.enabled"))` → `suggestions.filter()`
- 参照: `s.source`

## RealtimeSuggestProvider.makeResult()
- 位置: L294-312
- 役割: 全体の設定がオフ、またはスポンサー提案を表示しない設定のときは null を返す。source が merino なら makeMerinoResult、rust なら makeOptInResult に振り分ける。
- 触るとき: 提案を結果にするか捨てるかの分岐を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.isSuggestionSponsored()`, `this.makeMerinoResult()`, `this.makeOptInResult()`
- 参照: `suggestion.source`

## RealtimeSuggestProvider.makeMerinoResult()
- 位置: L314-357
- 役割: 機能が無効、または「少なく表示」の最小長に満たなければ null。values が無ければ null。query を含む値があれば既定の検索エンジンを取り、無ければ null。値ごとに makePayloadItem を通して動的結果を作る。
- 触るとき: オンライン提案の結果の作り方や、検索エンジンへの依存を変えるとき。
- 呼び出し先: `this.makePayloadItem()`, `values.map()`, `values.some()`
- 条件付き依存: `if (values.some(v => v.query))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 参照: `engine?.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `queryContext.isPrivate`, `searchString.length`, `suggestion.custom_details`, `suggestion.custom_details?.[this.merinoProvider]?.values`, `this.#minKeywordLength`, `this.dynamicResultType`, `this.isEnabled`, `this.merinoProvider`, `this.showLessFrequentlyCount`, `v.query`, `values?.length`

## RealtimeSuggestProvider.makePayloadItem()
- 位置: L376-378
- 役割: payload の項目として値をそのまま返す。必要なら、サブクラスで表示用の値を事前計算する。
- 触るとき: 表示に使う値を結果作成時に計算して項目に載せたいとき。

## RealtimeSuggestProvider.makeOptInResult()
- 位置: L380-434
- 役割: オプトイン tip の結果を作る。「表示しない」か「あとで」かを notNowTypes から決め、ボタンは「許可」と分割ボタン、メニューに「すべて表示しない」を持つ。
- 触るとき: オプトイン tip のボタン構成や文言の出し方を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `notNowTypes.has()`
- 参照: `lazy.QuickSuggest.HELP_TOPIC`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.TIP`, `queryContext.searchString`, `this.optInDescriptionL10n`, `this.optInIcon`, `this.optInTitleL10n`, `this.realtimeType`

## RealtimeSuggestProvider.getViewTemplate()
- 位置: L436-486
- 役割: 動的結果の表示テンプレートを作る。項目が複数ならグループ、1つなら選択可能な項目とし、各項目に画像と上段・下段の説明を並べる。
- 触るとき: 表示の要素の入れ子や属性(role、selectable など)を変えるとき。
- 呼び出し先: `items.map()`, `this.getViewTemplateForDescriptionBottom()`, `this.getViewTemplateForDescriptionTop()`, `this.getViewTemplateForImageContainer()`
- 参照: `item.query`, `item.url`, `items.length`, `items[0].query`, `items[0].url`, `result.payload`

## RealtimeSuggestProvider.getViewTemplateForImageContainer()
- 位置: L500-520
- 役割: 画像を正方形の枠に収めるための span と img のテンプレートを返す。
- 触るとき: アイコンの大きさや余白を変えるとき。Merino の市況アイコンの大きさがまちまちな理由を確かめるとき。

## RealtimeSuggestProvider.getViewUpdate()
- 位置: L522-541
- 役割: 複数項目のときだけ root の aria-label を設定し、各項目の getViewUpdateForPayloadItem の結果を1つにまとめて返す。
- 触るとき: 表示の更新をまとめる処理を変えるとき。
- 呼び出し先: `Object.assign()`, `this.getViewUpdateForPayloadItem()`
- 参照: `items.length`, `result.payload`, `this.ariaGroupL10n`

## RealtimeSuggestProvider.getResultCommands()
- 位置: L543-582
- 役割: オプトイン結果は null を返す。Merino の結果では、上限内なら「少なく表示」を入れ、続けて「表示しない」、区切り、「管理」、「ヘルプ」を返す。
- 触るとき: 結果メニューに出す項目や順序を種別ごとに変えるとき。
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `result.payload.source`, `this.canShowLessFrequently`, `this.notInterestedCommandL10n`

## RealtimeSuggestProvider.onEngagement()
- 位置: L590-604
- 役割: 結果の payload の source で振り分け、merino なら onMerinoEngagement、rust なら onOptInEngagement を呼ぶ。
- 触るとき: 操作がどちらの処理に渡るかを追うとき。
- 呼び出し先: `this.onMerinoEngagement()`, `this.onOptInEngagement()`
- 参照: `details.result.payload.source`

## RealtimeSuggestProvider.onMerinoEngagement()
- 位置: L606-631
- 役割: 「ヘルプ」と「管理」は UrlbarInput に任せる。「表示しない」は種別の suggest pref を false にして結果を削除する。「少なく表示」は回数を増やし、最小長を入力長+1 に設定する。
- 触るとき: Merino 提案のメニュー操作の結果を変えるとき。
- 呼び出し先: `controller.removeResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 参照: `details.selType`, `searchString.length`, `this.acknowledgeDismissalL10n`, `this.minKeywordLengthPref`, `this.suggestPref`

## RealtimeSuggestProvider.onOptInEngagement()
- 位置: L633-671
- 役割: opt_in はオンラインを有効にして検索を再実行する。not_now は今の時刻を記録して notNowTypes に加え、結果を消す。dismiss は dismissTypes に加えて結果を消す。not_interested は全体のオプトインを off にする。
- 触るとき: オプトイン tip のボタンを押したあとに pref がどう変わるかを追うとき。
- 呼び出し先: `Date.now()`, `controller.input.startQuery()`, `controller.removeResult()`, `lazy.UrlbarPrefs.add()`, `lazy.UrlbarPrefs.set()`
- 参照: `details.result`, `details.selType`, `this.acknowledgeDismissalL10n`, `this.realtimeType`

## RealtimeSuggestProvider.incrementShowLessFrequentlyCount()
- 位置: L673-680
- 役割: 上限内であれば、種別の「少なく表示」回数を1増やして pref に保存する。
- 触るとき: 回数の増やし方や上限の判定を変えるとき。
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`, `this.showLessFrequentlyCountPref`

## RealtimeSuggestProvider.showLessFrequentlyCount()
- 位置: L682-686
- 役割: 種別ごとの回数 pref を読み、0 未満にならないよう丸めて返す。
- 触るとき: 回数が画面の挙動に反映されない問題を調べるとき。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`
- 参照: `this.showLessFrequentlyCountPref`

## RealtimeSuggestProvider.canShowLessFrequently()
- 位置: L688-694
- 役割: 上限は realtimeShowLessFrequentlyCap、無ければ config の showLessFrequentlyCap、どちらも無ければ 0 から求め、上限が 0 か回数が上限未満なら true を返す。
- 触るとき: 「少なく表示」を出し続けるかの判断条件を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## RealtimeSuggestProvider.#minKeywordLength()
- 位置: L696-706
- 役割: 利用者が種別の pref を設定済み、または Nimbus の realtimeMinKeywordLength が null なら種別の pref 値を、それ以外は Nimbus の値を使い、0 以上に丸めて返す。
- 触るとき: 最小キーワード長の優先順位(利用者の設定、Nimbus、既定値)を変えるとき。
- 呼び出し先: `Math.max()`, `Services.prefs.prefHasUserValue()`, `lazy.UrlbarPrefs.get()`
- 参照: `this.minKeywordLengthPref`
- XPCOM: `Services.prefs`
