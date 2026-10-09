# browser/components/aiwindow/ui/modules/AITabStore.sys.mjs

source: browser/components/aiwindow/ui/modules/AITabStore.sys.mjs
source-hash: bc786a20a5892d44bd4ded1fbf7ff4887c497e90
lines: 387

## <module>
- 役割: AI タブページを SQLite に版ごとに保存・取得・削除するシングルトンのストアを定義する

## AITabStore.logPrefix()
- 位置: L41-43
- 役割: ログに付ける接頭辞 AITabStore を返す
- 触るとき: ログの出どころを識別する名前を変えるとき

## AITabStore.logLevelPref()
- 位置: L45-47
- 役割: ログレベルを決める pref 名 browser.smartwindow.aiTabStore.logLevel を返す
- 触るとき: このストアのログを有効にする方法を調べるとき

## AITabStore.shutdownBlockerName()
- 位置: L49-51
- 役割: 終了時に待つブロッカーの名前を返す
- 触るとき: 終了時の書き込み待ちが効かない問題を調べるとき

## AITabStore.CURRENT_SCHEMA_VERSION()
- 位置: L53-55
- 役割: 基盤に渡す現在のスキーマ版(AITabConstants の値)を返す
- 触るとき: スキーマ版を上げたときに移行が走るかを確認するとき

## AITabStore.databaseFileName()
- 位置: L57-59
- 役割: DB ファイル名を返す
- 触るとき: 保存先のファイル名を変えるとき

## AITabStore.prefBranch()
- 位置: L61-63
- 役割: 保存先の pref の枝を返す
- 触るとき: 保存先の pref を参照している箇所を探すとき

## AITabStore.createEntityStatements()
- 位置: L65-67
- 役割: 新規作成時に実行するテーブル定義と slug・版の一意インデックスの SQL を返す
- 触るとき: 初期スキーマに列やインデックスを足すとき

## AITabStore.migrations()
- 位置: L69-71
- 役割: AITabMigrations の移行配列をそのまま返す
- 触るとき: 移行を追加したときに基盤へ届くかを確認するとき

## AITabStore.create()
- 位置: async L86-88
- 役割: 新規タブを版 1 で保存し、確定したスラッグを返す
- 触るとき: 新しい AI タブを作る処理の保存部分を調べるとき、スラッグが変わる理由を追うとき
- 呼び出し先: `this.#insertNextVersion()`

## AITabStore.edit()
- 位置: async L99-101
- 役割: 既存タブの次の版として保存する(該当スラッグが無ければ例外)
- 触るとき: ページ編集の保存と版番号の付け方を調べるとき
- 呼び出し先: `this.#insertNextVersion()`

## AITabStore.getBySlug()
- 位置: async L110-118
- 役割: スラッグの最新版を 1 件返す。無ければ null
- 触るとき: スラッグだけの URL からページを読み込む処理を変えるとき
- 呼び出し先: `this.#ensureConnection()`, `this.#parseRow()`, `this.connection.executeCached()`
- 参照: `rows.length`

## AITabStore.getBySlugAndVersion()
- 位置: async L127-136
- 役割: スラッグと版を指定して 1 件返す。無ければ null
- 触るとき: 過去の版を開く、または版指定で読み直すとき
- 呼び出し先: `this.#ensureConnection()`, `this.#parseRow()`, `this.connection.executeCached()`
- 参照: `rows.length`

## AITabStore.getVersionsBySlug()
- 位置: async L146-155
- 役割: スラッグの版番号一覧を新しい順に返す
- 触るとき: 履歴や元に戻す操作が使える版があるかを判定するとき
- 呼び出し先: `row.getResultByName()`, `rows.map()`, `this.#ensureConnection()`, `this.connection.executeCached()`

## AITabStore.getAITabPagesByConvId()
- 位置: async L164-173
- 役割: 会話 ID に属する全版を古い順に返す
- 触るとき: 会話単位でページを集めるとき、会話の削除に伴う影響を調べるとき
- 呼び出し先: `rows.map()`, `this.#ensureConnection()`, `this.#parseRow()`, `this.connection.executeCached()`

## AITabStore.deleteVersionsBefore()
- 位置: async L185-192
- 役割: 指定版より古い版を削除する。残った版の番号は変えない
- 触るとき: 履歴の刈り込みの挙動や、番号が巻き戻らない理由を確認するとき
- 呼び出し先: `this.#ensureConnection()`, `this.connection.execute()`

## AITabStore.deleteBySlug()
- 位置: async L210-214
- 役割: スラッグの全版を削除する。会話側の削除は呼び出し元が別途行う
- 触るとき: ページ削除の範囲や削除順を変えるとき、会話が残る問題を調べるとき
- 呼び出し先: `this.#ensureConnection()`, `this.connection.execute()`

## AITabStore.#parseRow()
- 位置: L222-236
- 役割: DB の 1 行を page オブジェクトに変換し、JSON 列を parse して渡す
- 触るとき: 返されるページの項目名や JSON の扱いを変えるとき
- 呼び出し先: `parseJSONOrNull()`, `row.getResultByName()`

## AITabStore.#insertNextVersion()
- 位置: async L264-340
- 役割: 作成ならスラッグを確保して版 1 を、編集なら最大版+1 を一つのトランザクションで挿入する
- 触るとき: 保存時の版番号・スラッグの決まり方や競合対策を変えるとき、保存失敗の原因を追うとき
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`, `this.#ensureConnection()`, `this.connection .executeTransaction()`, `this.connection.executeCached()`, `this.log.error()`, `toJSONOrNull()`
- 条件付き依存: `if (expectNew)` → `this.#mintSlug()`
- 条件付き依存: `if (!(expectNew))` → `this.connection.execute()`
- 条件付き依存: `if (!(expectNew))` → `rows[0].getResultByName()`
- 参照: `e.message`, `e.stack`

## AITabStore.#mintSlug()
- 位置: async L357-371
- 役割: 基になるスラッグが空いていれば使い、埋まっていれば _2, _3 と番号を付けて空きを探す(上限後はランダム 8 文字)
- 触るとき: 同じタイトルのページが多いときのスラッグの付け方を変えるとき
- 呼び出し先: `crypto.randomUUID()`, `crypto.randomUUID().slice()`, `rows[0].getResultByName()`, `this.connection.execute()`

## AITabStore.#ensureConnection()
- 位置: async L373-382
- 役割: DB の準備を待ち、失敗時はエラーをログに出して再送出する
- 触るとき: DB が開けない場合のログや振る舞いを変えるとき
- 呼び出し先: `this.ensureDatabase()`, `this.ensureDatabase().catch()`, `this.log.error()`
- 参照: `e.message`, `e.stack`
