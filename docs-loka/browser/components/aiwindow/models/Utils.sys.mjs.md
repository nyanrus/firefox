# browser/components/aiwindow/models/Utils.sys.mjs

source: browser/components/aiwindow/models/Utils.sys.mjs
source-hash: 1a697c87e67806a0f03dfcd61150805be4479082
lines: 841

## <module>
- 役割: AI Window のモデル設定(Remote Settings のレコードと、表示用のフォールバック値)を解決し、プロンプト描画や JSON 応答の解析を助けるユーティリティ群。
- 呼び出し先: `Object.freeze()`, `Services.prefs.addObserver()`, `XPCOMUtils.declareLazy()`

## dropRecordsCache()
- 位置: L38-44
- 役割: Remote Settings レコードのメモ化キャッシュと、その無操作タイマーを破棄する。
- 触るとき: レコードの再取得を強制したいとき、またはキャッシュが古いまま残っている不具合を調べるとき。
- 条件付き依存: `if (_recordsIdleTimer)` → `clearTimeout()`

## touchRecordsCache()
- 位置: L48-53
- 役割: 無操作タイマーを張り直す。読み出しのたびに呼ばれ、一定時間読まれなければキャッシュを捨てる。
- 触るとき: キャッシュの解放タイミング(15 秒の無操作)を変えるとき。
- 呼び出し先: `setTimeout()`
- 条件付き依存: `if (_recordsIdleTimer)` → `clearTimeout()`

## getRemoteClient()
- 位置: L62-80
- 役割: AI Window 用の Remote Settings クライアントを初回だけ作って返す。sync を受けたらキャッシュを捨ててモデル情報を再読み込みする。
- 触るとき: Remote Settings のコレクション名や sync 時の再読み込みの扱いを変えるとき。
- 呼び出し先: `client.on()`, `console.error()`, `dropRecordsCache()`, `lazy.RemoteSettings()`, `refreshModelsDataCache()`

## getRemoteRecords()
- 位置: L91-110
- 役割: コレクション全レコードを取り、短時間のあいだメモ化して返す。失敗したら結果を残さない。
- 触るとき: チャットの 1 ターンで同じレコードが何度も読まれて遅くなる問題や、古いレコードが使われる問題を調べるとき。
- 呼び出し先: `getRemoteClient()`, `getRemoteClient() .get()`, `getRemoteClient() .get() .catch()`, `touchRecordsCache()`
- 条件付き依存: `if (_recordsPromise)` → `touchRecordsCache()`
- 条件付き依存: `if (_recordsPromise === promise)` → `dropRecordsCache()`

## _setRemoteClientForTesting()
- 位置: L118-121
- 役割: テスト用に偽のクライアントを差し込み、レコードのキャッシュも破棄する。
- 触るとき: Remote Settings の応答をテストで差し替えるとき。
- 呼び出し先: `dropRecordsCache()`

## _clearRemoteClientForTesting()
- 位置: L126-129
- 役割: テスト用にクライアントのキャッシュを消し、レコードのキャッシュも破棄する。
- 触るとき: テストごとに状態を初期化するとき。
- 呼び出し先: `dropRecordsCache()`

## _clearRecordsCacheForTesting()
- 位置: L135-137
- 役割: テスト用にレコードのメモ化だけを破棄し、クライアントは残す。
- 触るとき: テスト中にフェイククライアントのデータを書き換えたあと、再読み込みさせたいとき。
- 呼び出し先: `dropRecordsCache()`

## _setRecordsIdleMsForTesting()
- 位置: L145-148
- 役割: テスト用に無操作の待ち時間を差し替える。null で既定値に戻す。
- 触るとき: キャッシュ解放をテストで待たずに確認したいとき。
- 呼び出し先: `dropRecordsCache()`

## observe()
- 位置: L151-159
- 役割: モデル設定の pref が変わったら、クライアントとレコードのキャッシュを捨てる。
- 触るとき: モデル選択を変えたのに古い設定が使われ続ける問題を調べるとき。
- 条件付き依存: `if (topic === "nsPref:changed" && data === MODEL_PREF)` → `console.warn()`
- 条件付き依存: `if (topic === "nsPref:changed" && data === MODEL_PREF)` → `dropRecordsCache()`

## [MODEL_FEATURES.CHAT]()
- 位置: L255-257
- 役割: チャット機能のメジャーバージョンを返す。mistral リリース pref が有効なら 12、そうでなければ 10。
- 触るとき: チャットが参照する Remote Settings のメジャー版を変えるとき。Bug 2053495 の pref と合わせて外す予定がある。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `MODEL_FEATURES.CHAT`
- XPCOM: `Services.prefs`

## parseVersion()
- 位置: L335-345
- 役割: 「v1.2」形式の版文字列を major と minor に分けて返す。形式が合わなければ null。
- 触るとき: Remote Settings のレコード版の書式を変えるとき、または版が合わずに設定が選ばれない原因を調べるとき。
- 呼び出し先: `/^v?(\d+)\.(\d+)$/.exec()`, `Number()`

## checkMajorVersion()
- 位置: L354-357
- 役割: レコード版の major が、このビルドの要求する major と一致するか判定する。
- 触るとき: 対応するメジャー版の判定基準を変えるとき。
- 呼び出し先: `parseVersion()`
- 参照: `parsed.major`

## isCustomModelChoice()
- 位置: L416-418
- 役割: モデル選択 ID が「0」または空なら、ユーザーの自由入力モデル(カスタム)とみなす。
- 触るとき: カスタムモデルの判定条件を変えるとき。

## selectMainConfig()
- 位置: L438-515
- 役割: メジャー版で絞った設定から、機能に合うものを選ぶ。チャットはモデル選択 ID か自由入力モデル名で探し、見つからなければ generic を使う。他の機能は既定の設定を使う。
- 触るとき: どの設定レコードが使われるかを変えるとき、またはモデルを選んだのに generic になる理由を調べるとき。
- 呼び出し先: `checkMajorVersion()`, `console.warn()`, `featureConfigs.filter()`, `sameMajor.find()`
- 条件付き依存: `if (sameMajor.length === 0)` → `console.warn()`
- 条件付き依存: `if (feature === MODEL_FEATURES.CHAT)` → `isCustomModelChoice()`
- 条件付き依存: `if (!isCustomModelChoice(modelChoiceId))` → `sameMajor.find()`
- 条件付き依存: `if (!isCustomModelChoice(modelChoiceId))` → `console.warn()`
- 条件付き依存: `if (!(!isCustomModelChoice(modelChoiceId)))` → `sameMajor.find()`
- 条件付き依存: `if (!(!isCustomModelChoice(modelChoiceId)))` → `console.warn()`
- 条件付き依存: `if (feature === MODEL_FEATURES.CHAT)` → `sameMajor.find()`
- 条件付き依存: `if (defaultConfig)` → `isCustomModelChoice()`
- 参照: `MODEL_FEATURES.CHAT`, `config.is_default`, `config.model`, `config.model_choice_id`, `config.version`, `sameMajor.length`

## parseModelDetails()
- 位置: L525-544
- 役割: レコードの model_details を、オブジェクトでも JSON 文字列でも読み、表示用の名前やラベルを返す。無ければ null。
- 触るとき: モデル表示名の取り出し方を変えるとき、または model_details の形式が崩れて表示が空になるとき。
- 呼び出し先: `JSON.parse()`, `console.warn()`
- 参照: `details.brandName`, `details.labelId`, `details.ownerName`, `details.shortName`, `record?.model_details`

## resolveChatModelChoice()
- 位置: async L558-601
- 役割: モデル選択 ID から Remote Settings のチャット用 params レコードを選び、モデル名と表示情報を返す。ID 0 はフォールバック表から返す。取得失敗時は null。
- 触るとき: チャットのモデル選択を Remote Settings から解決する経路を変えるとき。
- 呼び出し先: `allRecords.filter()`, `console.warn()`, `getRemoteRecords()`, `parseModelDetails()`, `selectMainConfig()`
- 条件付き依存: `if (choiceId === "0")` → `getActiveFallbackModels()`
- 参照: `MODEL_FEATURES.CHAT`, `details?.brandName`, `details?.labelId`, `details?.ownerName`, `details?.shortName`, `r.feature`, `r.kind`, `record.model`, `record.owner_name`

## getActiveFallbackModels()
- 位置: L608-613
- 役割: mistral リリース pref に応じて、使うフォールバックのモデル表(V2 か旧版)を返す。
- 触るとき: Remote Settings が使えないときに表示されるモデル一覧を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## getModelDisplayOrder()
- 位置: L623-628
- 役割: モデル選択肢の表示順を返す。pref に応じて 1,2,3 か 3,1,2。
- 触るとき: スマートバーや設定画面のモデル並び順を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## getModelForChoice()
- 位置: async L636-652
- 役割: 選択 ID のモデル情報を、Remote Settings、フォールバック表、「unknown」の順に探して返す。
- 触るとき: 特定のモデル選択について推論に使うモデル名が決まらない問題を調べるとき。
- 呼び出し先: `getActiveFallbackModels()`, `getCurrentModelChoiceId()`, `resolveChatModelChoice()`

## refreshModelsDataCache()
- 位置: async L678-681
- 役割: モデル情報のキャッシュを捨て、全件を取り直す。
- 触るとき: Remote Settings の同期後や pref 変更後に表示を更新させたいとき。
- 呼び出し先: `getAllModelsData()`

## getAllModelsData()
- 位置: async L688-709
- 役割: 全選択肢のモデル情報を並列に解決し、フォールバック表に上書きして一度だけキャッシュする。
- 触るとき: モデル一覧の値の組み立て方(どこまでフォールバックするか)を変えるとき。
- 呼び出し先: `Promise.all()`, `getActiveFallbackModels()`, `getModelDisplayOrder()`, `getModelDisplayOrder().map()`, `getModelForChoice()`

## getCachedModelsData()
- 位置: L716-718
- 役割: 取得済みのモデル情報を同期的に返す。未取得ならフォールバック表を返す。
- 触るとき: 非同期にできない場所で表示用のモデル名を読むとき。
- 呼び出し先: `getActiveFallbackModels()`

## getCurrentModelName()
- 位置: L720-722
- 役割: 現在選ばれているモデル選択の、推論用のモデル名を返す。無ければ空文字。
- 触るとき: 推論リクエストに載せるモデル名の決まり方を追うとき。
- 呼び出し先: `getCachedModelsData()`, `getCurrentModelChoiceId()`
- 参照: `getCachedModelsData()[getCurrentModelChoiceId()]?.model`

## getCurrentModelChoiceId()
- 位置: L724-726
- 役割: モデル選択 ID を firstrun の pref から読んで返す。未設定なら空文字。
- 触るとき: モデル選択の保存先の pref を変えるとき。
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## _clearModelsDataCacheForTesting()
- 位置: L731-733
- 役割: テスト用にモデル情報のキャッシュを消す。
- 触るとき: テストごとにモデル情報の状態を初期化するとき。

## renderPrompt()
- 位置: L742-751
- 役割: プロンプト文字列の {キー} を対応する値で置き換えて返す。
- 触るとき: プロンプトのプレースホルダの書式を変えるとき、または置換されずに残った {キー} を調べるとき。
- 呼び出し先: `Object.entries()`, `finalPromptContent.replace()`

## parseAndExtractJSON()
- 位置: L761-779
- 役割: LLM 応答の finalOutput から、コードブロックがあればその中の JSON を読む。構文エラーなら fallback を返し、それ以外の例外は投げ直す。
- 触るとき: モデル応答の JSON 抽出に失敗したときの挙動を変えるとき、または応答が fallback になって結果が空になる原因を調べるとき。
- 呼び出し先: `JSON.parse()`, `rawContent.match()`
- 条件付き依存: `if (e instanceof SyntaxError)` → `console.warn()`
- 参照: `e.message`, `response?.finalOutput`

## toIntegerId()
- 位置: L788-797
- 役割: 数値または数字の文字列を整数の id に直す。整数でなければ null。
- 触るとき: 推論結果の id が文字列で返る場合の扱いを変えるとき。
- 呼び出し先: `value.trim()`
- 条件付き依存: `if (typeof value === "number")` → `Number.isInteger()`
- 条件付き依存: `if (typeof value === "string" && value.trim() !== "")` → `Number()`
- 条件付き依存: `if (typeof value === "string" && value.trim() !== "")` → `Number.isInteger()`

## indexInferenceResultsById()
- 位置: L807-816
- 役割: 推論結果を id ごとの Map にまとめる。id が無効な結果は無視し、同じ id が複数あれば最初のものを残す。
- 触るとき: 入力と出力の対応づけを、出力順に頼らず id で行うよう変えるとき。
- 呼び出し先: `resultsById.has()`, `toIntegerId()`
- 条件付き依存: `if (id !== null && !resultsById.has(id))` → `resultsById.set()`
- 参照: `result?.id`

## makeJSONSchemaBlob()
- 位置: L831-840
- 役割: OpenAI 形式の response_format(json_schema)オブジェクトを組み立てる。strict が true なら厳密な適合を要求する。
- 触るとき: 構造化出力の JSON スキーマを推論パラメータに載せるとき。strict にはスキーマの制約があるので注意する。
