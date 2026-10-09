# browser/components/urlbar/content/UrlbarResult.mjs

source: browser/components/urlbar/content/UrlbarResult.mjs
source-hash: febdaae5818d21b142ba1d5968875133b6f3adb9
lines: 709

## <module>
- 役割: 検索候補 1 件を表す UrlbarResult クラス。型・データ源・表示の属性を管理し、親子間で送る形式も持つ。

## UrlbarResult.constructor()
- 位置: L82-161
- 役割: 型・データ源・payload を検査して非公開フィールドに保存する。TIP 型はリッチ表示でアイコンサイズ 24 に固定する。
- 触るとき: 新しい結果型や属性を足す時、またはコンストラクタ引数の既定値を変える時。
- 呼び出し先: `Object.entries()`, `Object.entries(payload).filter()`, `Object.fromEntries()`, `Object.values()`, `Object.values(UrlbarShared.RESULT_SOURCE).includes()`, `Object.values(UrlbarShared.RESULT_TYPE).includes()`, `this.#validatePayload()`
- 条件付き依存: `if (highlights)` → `Object.freeze()`
- 参照: `UrlbarShared.EXPOSURE_TELEMETRY.NONE`, `UrlbarShared.RESULT_SOURCE`, `UrlbarShared.RESULT_TYPE`, `UrlbarShared.RESULT_TYPE.TIP`, `this.#autofill`, `this.#exposureTelemetry`, `this.#group`, `this.#heuristic`, `this.#hideRowLabel`, `this.#highlights`, `this.#isBestMatch`, `this.#isBottomUrlSuggestion`, `this.#isRichSuggestion`, `this.#isSuggestedIndexRelativeToGroup`, `this.#payload`, `this.#providerName`, `this.#resultSpan`, `this.#richSuggestionIconSize`, `this.#richSuggestionIconVariation`, `this.#rowLabel`, `this.#showFeedbackMenu`, `this.#source`, `this.#suggestedIndex`, `this.#testForceNewContent`, `this.#type`

## UrlbarResult.type()
- 位置: L203-205
- 役割: 結果の種類 (UrlbarShared.RESULT_TYPE) を返す。
- 触るとき: 表示や選択の処理が結果の種類によって分かれている箇所を調べる時。
- 参照: `this.#type`

## UrlbarResult.source()
- 位置: L212-214
- 役割: 結果のデータ源 (RESULT_SOURCE) を返す。複数の源が混ざる時はプライバシー上より厳しい方。
- 触るとき: 結果がどのデータから来たかで計測や表示が変わる時。
- 参照: `this.#source`

## UrlbarResult.autofill()
- 位置: L221-223
- 役割: 選択時に入力欄へ補完する文字列のデータを返す。無ければ undefined。
- 触るとき: オートフィル候補の補完内容が期待と違う時。
- 参照: `this.#autofill`

## UrlbarResult.exposureTelemetry()
- 位置: L231-233
- 役割: 露出テレメトリを記録するか、また結果を表示するか隠すかの値 (EXPOSURE_TELEMETRY) を返す。
- 触るとき: 露出の計測が出ない時や、隠すべき露出が表示されてしまう時。
- 参照: `this.#exposureTelemetry`

## UrlbarResult.exposureTelemetry()
- 位置: L234-236
- 役割: 露出テレメトリの値を設定する。
- 触るとき: プロバイダーが結果ごとに露出の扱いを切り替える箇所を調べる時。
- 参照: `this.#exposureTelemetry`

## UrlbarResult.group()
- 位置: L242-244
- 役割: マクサーが結果を置くグループ (RESULT_GROUP) を返す。未設定ならマクサーが決める。
- 触るとき: 候補の並び順やグループ分けを調べる時。
- 参照: `this.#group`

## UrlbarResult.heuristic()
- 位置: L252-254
- 役割: この結果が、Enter だけで選ばれる heuristic 結果かを返す。
- 触るとき: Enter で何が選ばれるかの不具合を調べる時。
- 参照: `this.#heuristic`

## UrlbarResult.hideRowLabel()
- 位置: L261-263
- 役割: 結果の行の上にグループ見出しを表示しないかを返す。
- 触るとき: 見出しが出ない、または重複して出る表示を直す時。
- 参照: `this.#hideRowLabel`

## UrlbarResult.isBestMatch()
- 位置: L270-272
- 役割: ベストマッチ (上位の候補として表示される) かを返す。
- 触るとき: 上位表示になる条件を変える時。
- 参照: `this.#isBestMatch`

## UrlbarResult.isBottomUrlSuggestion()
- 位置: L280-282
- 役割: URL 候補を結果の下部に表示するかを返す。
- 触るとき: 下部に出る URL 候補が期待とずれる時。
- 参照: `this.#isBottomUrlSuggestion`

## UrlbarResult.isRichSuggestion()
- 位置: L290-292
- 役割: リッチ表示 (大きなアイコンと説明付き) かを返す。TIP は常に true。
- 触るとき: 候補の見た目が通常と違う原因を調べる時。
- 参照: `this.#isRichSuggestion`

## UrlbarResult.isRichSuggestion()
- 位置: L293-295
- 役割: リッチ表示かどうかを設定する。
- 触るとき: プロバイダーが結果の表示形式を後から切り替える箇所を見る時。
- 参照: `this.#isRichSuggestion`

## UrlbarResult.isSuggestedIndexRelativeToGroup()
- 位置: L303-305
- 役割: suggestedIndex がグループ内の位置か、結果全体の位置かを返す。
- 触るとき: 位置指定の候補がグループ内で正しく並ばない時。
- 参照: `this.#isSuggestedIndexRelativeToGroup`

## UrlbarResult.isSuggestedIndexRelativeToGroup()
- 位置: L306-308
- 役割: suggestedIndex をグループ基準にするかを設定する。
- 触るとき: 位置指定の基準をグループ基準に切り替えるプロバイダーを作る時。
- 参照: `this.#isSuggestedIndexRelativeToGroup`

## UrlbarResult.providerName()
- 位置: L315-317
- 役割: 結果を作ったプロバイダーの名前を返す。
- 触るとき: プロバイダー名でグループや計測を分けている箇所を調べる時。
- 参照: `this.#providerName`

## UrlbarResult.providerName()
- 位置: L318-320
- 役割: プロバイダー名を設定する。
- 触るとき: 結果の出所名が途中で書き換えられる経路を調べる時。
- 参照: `this.#providerName`

## UrlbarResult.providerType()
- 位置: L327-329
- 役割: プロバイダーの種類 (HEURISTIC、PROFILE、NETWORK、EXTENSION) を返す。
- 触るとき: プロバイダーの種類によって結果の扱いが変わる時。
- 参照: `this.#providerType`

## UrlbarResult.providerType()
- 位置: L330-332
- 役割: プロバイダーの種類を設定する。
- 触るとき: 結果の登録時にプロバイダーの種類を決める箇所を変える時。
- 参照: `this.#providerType`

## UrlbarResult.resultSpan()
- 位置: L341-343
- 役割: 結果が表で占める行数を返す。未設定なら種類ごとの既定値 (getSpanForResult) を使う。
- 触るとき: 結果の高さが想定と違う時。
- 参照: `this.#resultSpan`

## UrlbarResult.richSuggestionIconSize()
- 位置: L350-352
- 役割: リッチ候補のアイコンサイズ (px) を返す。TIP は 24。
- 触るとき: アイコンの大きさが崩れる時。
- 参照: `this.#richSuggestionIconSize`

## UrlbarResult.richSuggestionIconVariation()
- 位置: L360-362
- 役割: リッチ候補のアイコンの種類を返す。表示側が行の icon-variation 属性として使う。
- 触るとき: アイコンの見た目の種類を新しく足す時や、スタイルが当たらない時。
- 参照: `this.#richSuggestionIconVariation`

## UrlbarResult.richSuggestionIconSize()
- 位置: L363-365
- 役割: リッチ候補のアイコンサイズを設定する。
- 触るとき: TIP 以外の結果でアイコンサイズを変えたい時。
- 参照: `this.#richSuggestionIconSize`

## UrlbarResult.rowLabel()
- 位置: L373-375
- 役割: 行の上に出すグループ見出しを、l10n の id と args の組として返す。
- 触るとき: 結果ごとに見出しの文言を変えたい時。
- 参照: `this.#rowLabel`

## UrlbarResult.showFeedbackMenu()
- 位置: L382-384
- 役割: メニューボタンをフィードバックメニューとして表示するかを返す。
- 触るとき: フィードバック用メニューの表示条件を調べる時。
- 参照: `this.#showFeedbackMenu`

## UrlbarResult.suggestedIndex()
- 位置: L393-395
- 役割: 結果の希望位置を返す。負の値は末尾から数える。未設定は undefined。
- 触るとき: 位置を指定した候補が期待どおりの順に並ばない時。
- 参照: `this.#suggestedIndex`

## UrlbarResult.suggestedIndex()
- 位置: L396-398
- 役割: 希望位置を設定する。
- 触るとき: プロバイダーが並び位置を後から変える箇所を調べる時。
- 参照: `this.#suggestedIndex`

## UrlbarResult.payload()
- 位置: L404-406
- 役割: 結果のデータを返す。持つ項目は種類によって変わる。
- 触るとき: 表示や選択で payload のどの項目を使うかを確かめる時。
- 参照: `this.#payload`

## UrlbarResult.testForceNewContent()
- 位置: L408-410
- 役割: テスト用に、内容を強制的に新しく描画させるフラグを返す。
- 触るとき: 同じ結果の再描画をテストで強制する時。
- 参照: `this.#testForceNewContent`

## UrlbarResult.testHighlights()
- 位置: L413-415
- 役割: テスト用に、ハイライト情報を返す。
- 触るとき: ハイライトの期待値をテストで確かめる時。
- 参照: `this.#highlights`

## UrlbarResult.icon()
- 位置: L422-424
- 役割: payload の icon を返す。
- 触るとき: 結果のアイコンが表示されない時。
- 参照: `this.payload.icon`

## UrlbarResult.hasSuggestedIndex()
- 位置: L433-435
- 役割: suggestedIndex が数値として設定されているかを返す。
- 触るとき: 位置指定の有無でグループ分けが変わる箇所を調べる時。
- 参照: `this.suggestedIndex`

## UrlbarResult.isHiddenExposure()
- 位置: L444-446
- 役割: 露出テレメトリの値が HIDDEN (表示しない) かを返す。
- 触るとき: 非表示の露出が行数に数えられてしまうかを確かめる時。
- 参照: `UrlbarShared.EXPOSURE_TELEMETRY.HIDDEN`, `this.exposureTelemetry`

## UrlbarResult.getDisplayableValueAndHighlights()
- 位置: L460-539
- 役割: payload の項目を表示用に整え、入力との一致範囲を求めて結果をキャッシュする。title が無ければドメインか URL で代用する。
- 触るとき: 候補のタイトルや URL の表示文字列、強調位置が違う時や、表示の整形規則を変える時。
- 呼び出し先: `Array.isArray()`, `UrlbarShared.getTokenMatches()`, `structuredClone()`, `this.#displayValuesCache.has()`, `this.#displayValuesCache.set()`, `value.map()`
- 条件付き依存: `if (this.#displayValuesCache.has(payloadName))` → `this.#displayValuesCache.get()`
- 条件付き依存: `if (this.#displayValuesCache.has(payloadName))` → `UrlbarShared.deepEqual()`
- 条件付き依存: `if ( options.isURL == cached.options.isURL && (options.tokens == undefined || UrlbarShared.deepEqual(options.tokens, cached.options.tokens)) )` → `this.#displayValuesCache.get()`
- 条件付き依存: `if (isURL)` → `UrlbarShared.prepareUrlForDisplay()`
- 条件付き依存: `if (typeof value == "string")` → `value.substring()`
- 条件付き依存: `if (!options.tokens?.length || !highlightType)` → `this.#displayValuesCache.set()`
- 参照: `UrlbarShared.HIGHLIGHT.TYPED`, `UrlbarShared.MAX_TEXT_LENGTH`, `cached.options.isURL`, `cached.options.tokens`, `new URL(this.payload.url).URI.displayHostPort`, `options.isURL`, `options.tokens`, `options.tokens?.length`, `this.#displayValuesCache`, `this.#highlights`, `this.payload`, `this.payload.url`

## UrlbarResult.#validatePayload()
- 位置: L553-575
- 役割: 型ごとのスキーマで payload を検査する。content 側はスキーマが読めないため検査を省く。
- 触るとき: 新しい結果型がスキーマ検査で弾かれる時や、content 側で検査されない前提を確かめる時。
- 呼び出し先: `lazy.JsonSchemaValidator.validate()`, `lazy.UrlbarUtils.getPayloadSchema()`
- 参照: `UrlbarShared.RESULT_TYPE.DYNAMIC`, `result.error`, `result.valid`, `this.type`

## UrlbarResult.toString()
- 位置: L583-597
- 役割: ログ向けに結果を短い文字列にする。url、keyword、suggestion、engine の順に判定し、どれも無ければ JSON を返す。
- 触るとき: ログに出す結果の概要表示を変える時。
- 呼び出し先: `JSON.stringify()`
- 条件付き依存: `if (this.payload.url)` → `this.payload.url.substr()`
- 参照: `this.payload.engine`, `this.payload.keyword`, `this.payload.query`, `this.payload.suggestion`, `this.payload.title`, `this.payload.url`

## UrlbarResult.toWire()
- 位置: L607-636
- 役割: 非公開フィールドを含めて、actor 越しに送れる素のオブジェクトにする。
- 触るとき: 結果に新しいフィールドを足し、それが wire に含まれるかを確かめる時。
- 参照: `this.#autofill`, `this.#exposureTelemetry`, `this.#group`, `this.#heuristic`, `this.#hideRowLabel`, `this.#highlights`, `this.#isBestMatch`, `this.#isBottomUrlSuggestion`, `this.#isRichSuggestion`, `this.#isSuggestedIndexRelativeToGroup`, `this.#payload`, `this.#providerName`, `this.#providerType`, `this.#resultSpan`, `this.#richSuggestionIconSize`, `this.#richSuggestionIconVariation`, `this.#rowLabel`, `this.#showFeedbackMenu`, `this.#source`, `this.#suggestedIndex`, `this.#testForceNewContent`, `this.#type`, `this.commands`, `this.id`, `this.isSERP`, `this.rowIndex`

## UrlbarResult.fromWire()
- 位置: L655-672
- 役割: wire から UrlbarResult を復元する。liveResults に同じ id があれば元の結果を返し、rowIndex だけ更新する。
- 触るとき: 親が受け取った結果が子で別物になり、選択や露出の対応がずれる時。
- 呼び出し先: `liveResults?.find()`
- 参照: `liveResult.rowIndex`, `r.id`, `result.commands`, `result.id`, `result.isSERP`, `result.providerType`, `result.rowIndex`, `wire.commands`, `wire.id`, `wire.isSERP`, `wire.providerType`, `wire.rowIndex`
