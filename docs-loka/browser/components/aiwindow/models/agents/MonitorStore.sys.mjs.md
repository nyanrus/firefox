# browser/components/aiwindow/models/agents/MonitorStore.sys.mjs

source: browser/components/aiwindow/models/agents/MonitorStore.sys.mjs
source-hash: e6002228b0e0e8c5bcf55180738c0547b8ad77c7
lines: 615

## <module>
- 役割: 監視エージェントの定義と実行履歴を IndexedDB に保存・読み出しする層。保存前の検証、古い形式からの補完、DB のバージョン管理と終了時の待ち合わせを担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.values()`, `Promise.resolve()`, `console.createInstance()`

## invalidField()
- 位置: L34-36
- 役割: 項目名を入れた「Monitor ... is invalid.」の例外を作る。
- 触るとき: 検証エラーのメッセージ文言を変えるとき。

## stringField()
- 位置: L38-47
- 役割: 値が文字列で、空でなく、前後に空白が無いことを確かめる。allowEmpty で空を許す。
- 触るとき: ID やプロンプトなどの文字列項目の検証条件を変えるとき。
- 呼び出し先: `value.trim()`
- 条件付き依存: `if ( typeof value !== "string" || (!allowEmpty && !value.trim()) || value !== value.trim() )` → `invalidField()`

## timestampField()
- 位置: L49-61
- 役割: 値が ISO 8601 形式の日時として正規化されているかを確かめる。nullable なら null を許す。
- 触るとき: 保存する日時の形式を変えるとき、または日時の不正で保存が失敗する原因を調べるとき。
- 呼び出し先: `Number.isNaN()`, `date.getTime()`, `date.toISOString()`
- 条件付き依存: `if (typeof value !== "string")` → `invalidField()`
- 条件付き依存: `if (Number.isNaN(date.getTime()) || date.toISOString() !== value)` → `invalidField()`

## runCountField()
- 位置: L63-72
- 役割: 実行回数が 0 以上の整数か確かめる。復元モードでは不正な値を捨てて 0 にする。
- 触るとき: 実行回数の扱いを変えるとき、または古いデータの回数が 0 に戻る理由を調べるとき。
- 呼び出し先: `Number.isInteger()`, `lazy.log.warn()`
- 条件付き依存: `if (!recoverInvalid)` → `invalidField()`

## scheduleRecord()
- 位置: L74-124
- 役割: スケジュールの種類ごとに値を検証し、保存用の平らなレコードにする。不正なら例外を投げる。
- 触るとき: 新しいスケジュール種別を足すとき、または時刻や曜日の範囲を変えるとき。
- 呼び出し先: `Array.isArray()`, `Number.isFinite()`, `Number.isInteger()`, `invalidField()`
- 条件付き依存: `if (!schedule || typeof schedule !== "object" || Array.isArray(schedule))` → `invalidField()`
- 条件付き依存: `if (!Number.isFinite(schedule.hours) || schedule.hours <= 0)` → `invalidField()`
- 条件付き依存: `if ( !Number.isInteger(schedule.hour) || schedule.hour < 0 || schedule.hour > 23 || !Number.isInteger(schedule.minute) || schedule.minute < 0 || schedule.minute ...)` → `invalidField()`
- 条件付き依存: `if ( !Number.isInteger(schedule.weekday) || schedule.weekday < 0 || schedule.weekday > 6 || !Number.isInteger(schedule.hour) || schedule.hour < 0 || schedule.hou...)` → `invalidField()`
- 参照: `schedule.hour`, `schedule.hours`, `schedule.minute`, `schedule.type`, `schedule.weekday`

## watchUrlRecords()
- 位置: L126-132
- 役割: URL を正規化し、残りが空なら例外を投げる。
- 触るとき: 監視できる URL の条件を保存時にも適用するとき。
- 呼び出し先: `trimAndFilterWatchUrls()`
- 条件付き依存: `if (!normalizedUrls.length)` → `invalidField()`
- 参照: `normalizedUrls.length`

## initialSnapshotRecord()
- 位置: L134-160
- 役割: 初期スナップショットを検証して保存形式にする。復元モードでは不正なら null にする。
- 触るとき: スナップショットの保存形式を変えるとき。
- 呼び出し先: `Array.isArray()`, `lazy.log.warn()`, `timestampField()`
- 条件付き依存: `if ( typeof snapshot !== "object" || Array.isArray(snapshot) || typeof snapshot.pageContent !== "string" )` → `invalidField()`
- 参照: `snapshot.capturedAt`, `snapshot.pageContent`

## expiryRecord()
- 位置: L162-185
- 役割: 自動停止の記録(理由と時刻)を検証する。理由が未知なら例外、復元モードでは null にする。
- 触るとき: 自動停止の理由の種類を増やすとき。
- 呼び出し先: `Array.isArray()`, `EXPIRY_REASONS.has()`, `lazy.log.warn()`, `timestampField()`
- 条件付き依存: `if ( typeof expiry !== "object" || Array.isArray(expiry) || !EXPIRY_REASONS.has(expiry.reason) )` → `invalidField()`
- 参照: `expiry.expiredAt`, `expiry.reason`

## historyRecord()
- 位置: L187-215
- 役割: 履歴 1 件の状態、説明、一致結果、エラーコードを検証して保存用レコードにする。
- 触るとき: 履歴の項目や許可するエラーコードを変えるとき。
- 呼び出し先: `Array.isArray()`, `HISTORY_STATUSES.has()`, `stringField()`, `timestampField()`
- 条件付き依存: `if (!entry || typeof entry !== "object" || Array.isArray(entry))` → `invalidField()`
- 条件付き依存: `if (!HISTORY_STATUSES.has(entry.status))` → `invalidField()`
- 条件付き依存: `if (typeof entry.resultExplanation !== "string")` → `invalidField()`
- 条件付き依存: `if (typeof entry.conditionMet !== "boolean")` → `invalidField()`
- 条件付き依存: `if (entry.errorCode != null)` → `HISTORY_ERROR_CODES.has()`
- 条件付き依存: `if (!HISTORY_ERROR_CODES.has(entry.errorCode))` → `invalidField()`
- 参照: `entry.checkedAt`, `entry.conditionMet`, `entry.errorCode`, `entry.id`, `entry.resultExplanation`, `entry.status`, `record.errorCode`

## sanitizeHistoryRecords()
- 位置: L217-244
- 役割: 履歴配列を 1 件ずつ検証する。復元モードでは不正な件を飛ばし、件数が上限を超えたら新しい方を残す。
- 触るとき: 履歴の保持件数や、不正な履歴の扱いを変えるとき。
- 呼び出し先: `Array.isArray()`, `historyRecord()`, `lazy.log.warn()`, `records.push()`
- 条件付き依存: `if (recoverInvalid)` → `lazy.log.warn()`
- 条件付き依存: `if (!Array.isArray(history))` → `invalidField()`
- 条件付き依存: `if (!recoverInvalid)` → `invalidField()`
- 条件付き依存: `if (records.length > MAX_HISTORY_ENTRIES)` → `records.slice()`
- 参照: `records.length`

## sanitizeMonitorRecord()
- 位置: L246-294
- 役割: 監視 1 件を保存形式に整える。古いデータは作成時刻や履歴の件数から補い、復元モードでは壊れた部分だけ捨てる。
- 触るとき: 監視の保存項目を追加や削除するとき、または古い保存データの移行方法を変えるとき。
- 呼び出し先: `Array.isArray()`, `expiryRecord()`, `initialSnapshotRecord()`, `runCountField()`, `sanitizeHistoryRecords()`, `scheduleRecord()`, `stringField()`, `timestampField()`, `watchUrlRecords()`
- 条件付き依存: `if (!monitor || typeof monitor !== "object" || Array.isArray(monitor))` → `invalidField()`
- 条件付き依存: `if (typeof monitor.enabled !== "boolean")` → `invalidField()`
- 参照: `monitor.activeSince`, `monitor.createdAt`, `monitor.enabled`, `monitor.expiry`, `monitor.history`, `monitor.history.length`, `monitor.id`, `monitor.initialSnapshot`, `monitor.lastMatchAt`, `monitor.lastRunTime`, `monitor.monitorPrompt`, `monitor.nextRunTime`, `monitor.runCount`, `monitor.schedule`, `monitor.title`, `monitor.updatedAt`, `monitor.watchUrls`

## wrapRequest()
- 位置: L296-301
- 役割: IndexedDB のリクエストを promise に変換し、成功なら結果、失敗ならエラーで決まる。
- 触るとき: IndexedDB の操作を新しく書くとき、またはエラーがどこで伝わるかを追うとき。
- 参照: `request.onerror`, `request.onsuccess`

## request.onsuccess()
- 位置: L298-298
- 役割: リクエストが成功したとき、結果で promise を解決する。
- 触るとき: 成功時の戻り値の取り方を変えるとき。
- 呼び出し先: `resolve()`
- 参照: `request.result`

## request.onerror()
- 位置: L299-299
- 役割: リクエストが失敗したとき、そのエラーで promise を拒否する。
- 触るとき: 失敗時に送るエラーの内容を変えるとき。
- 呼び出し先: `reject()`
- 参照: `request.error`

## isNewerSchemaError()
- 位置: L303-305
- 役割: DB のバージョンエラー(VersionError)かを判定する。
- 触るとき: 新しすぎるスキーマを検出する条件を変えるとき。
- 参照: `error?.name`

## MonitorStoreImpl.constructor()
- 位置: L320-331
- 役割: シャットダウン時に保存の完了を待って DB を閉じるブロッカーを用意する。
- 触るとき: 終了時の保存の待ち方を変えるとき。
- 参照: `lazy.AsyncShutdown.profileBeforeChange`, `this.#asyncShutdownBlocker`, `this.#shutdownClient`

## this.#asyncShutdownBlocker()
- 位置: async L322-330
- 役割: 終了時に、進行中の書き込みを待ってから DB を閉じる。
- 触るとき: 終了処理で保存が失われないよう待つ条件を変えるとき。
- 呼び出し先: `this.#closeDatabase()`
- 参照: `this.#promiseWrite`, `this.#shutdownBlockerAdded`, `this.#shuttingDown`

## MonitorStoreImpl.listMonitors()
- 位置: async L333-360
- 役割: 全監視を読み出し、壊れたレコードは飛ばして作成時刻順に返す。
- 触るとき: 起動時の読み込みや一覧の並び順を変えるとき。
- 呼び出し先: `Date.parse()`, `db.transaction()`, `first.id.localeCompare()`, `lazy.log.warn()`, `monitors.push()`, `monitors.sort()`, `sanitizeMonitorRecord()`, `this.#ensureDatabase()`, `this.#prepareForOperation()`, `transaction.objectStore()`, `transaction.objectStore(MONITOR_STORE_NAME).getAll()`, `transaction.promiseComplete()`, `transactionComplete.catch()`
- 参照: `first.createdAt`, `second.createdAt`, `second.id`

## MonitorStoreImpl.saveMonitor()
- 位置: async L362-367
- 役割: 監視 1 件を検証して書き込みキューに入れ、put で保存する。
- 触るとき: 1 件保存の検証や書き込み方法を変えるとき。
- 呼び出し先: `sanitizeMonitorRecord()`, `store.put()`, `this.#queueWrite()`, `this.#withWriteStore()`

## MonitorStoreImpl.saveMonitors()
- 位置: async L369-382
- 役割: 監視の配列を検証し、1 つの transaction で全件を置き換えて保存する。
- 触るとき: 全件保存の方法(全消去してから書く)を変えるとき。
- 呼び出し先: `Array.isArray()`, `monitors.map()`, `store.clear()`, `store.put()`, `this.#queueWrite()`, `this.#withWriteStore()`
- 条件付き依存: `if (!Array.isArray(monitors))` → `invalidField()`

## MonitorStoreImpl.deleteMonitor()
- 位置: async L384-389
- 役割: 指定 ID の監視を書き込みキュー経由で削除する。
- 触るとき: 監視の削除の経路を変えるとき。
- 呼び出し先: `store.delete()`, `stringField()`, `this.#queueWrite()`, `this.#withWriteStore()`

## MonitorStoreImpl.destroyDatabase()
- 位置: async L391-397
- 役割: DB の接続を閉じ、DB を削除して、保持している接続参照も消す。
- 触るとき: テストのリセットや保存データの全消去の方法を変えるとき。
- 呼び出し先: `this.#closeDatabaseConnection()`, `this.#deleteDatabase()`, `this.#queueWrite()`
- 参照: `this.#promiseDb`

## MonitorStoreImpl.close()
- 位置: async L399-404
- 役割: DB 接続を閉じ、終了中でなければシャットダウンブロッカーも外す。
- 触るとき: 保存層を停止する順序を変えるとき。
- 呼び出し先: `this.#closeDatabaseConnection()`
- 条件付き依存: `if (!this.#shuttingDown)` → `this.#removeShutdownBlocker()`
- 参照: `this.#shuttingDown`

## MonitorStoreImpl.#closeDatabaseConnection()
- 位置: async L406-413
- 役割: 開いている途中の接続を待ってから閉じ、参照を消す。
- 触るとき: DB を開く処理と閉じる処理が競合する問題を調べるとき。
- 呼び出し先: `this.#closeDatabase()`
- 条件付き依存: `if (!this.#db && this.#promiseDb)` → `this.#promiseDb.catch()`
- 参照: `this.#db`, `this.#promiseDb`

## MonitorStoreImpl.#withWriteStore()
- 位置: async L415-429
- 役割: readwrite の transaction を開き、コールバックで書き込んでから完了を待つ。失敗時は transaction を中止する。
- 触るとき: 書き込みの共通処理や失敗時の中止の仕方を変えるとき。
- 呼び出し先: `callback()`, `db.transaction()`, `this.#ensureDatabase()`, `transaction.abort()`, `transaction.objectStore()`, `transaction.promiseComplete()`, `transactionComplete.catch()`

## MonitorStoreImpl.#queueWrite()
- 位置: L431-450
- 役割: 書き込みを直前の書き込みの完了後に 1 件ずつ実行する。待機中と実行中の状態を記録する。
- 触るとき: 書き込みの順序を保つ仕組みや、終了時に待つ対象を変えるとき。
- 呼び出し先: `Date.now()`, `promise .finally()`, `promise .finally(() => { this.#pendingWrites.delete(pendingWrite); }) .catch()`, `this.#pendingWrites.add()`, `this.#pendingWrites.delete()`, `this.#prepareForOperation()`, `this.#promiseWrite.then()`
- 参照: `this.#promiseWrite`

## runTask()
- 位置: L439-442
- 役割: 書き込み処理を開始した時刻を記録してから実行する。
- 触るとき: 書き込みの待ち時間の計測を変えるとき。
- 呼び出し先: `Date.now()`, `task()`
- 参照: `pendingWrite.startedAt`

## MonitorStoreImpl.#prepareForOperation()
- 位置: L452-457
- 役割: 終了中なら例外を投げ、そうでなければシャットダウンブロッカーを登録する。
- 触るとき: 終了処理の後に保存操作を受け付けない条件を変えるとき。
- 呼び出し先: `this.#addShutdownBlocker()`
- 参照: `this.#shuttingDown`

## MonitorStoreImpl.#openDatabase()
- 位置: async L459-498
- 役割: IndexedDB を開き、無ければ monitors のストアと createdAt の索引を作る。終了中で書き込みが無ければ閉じて例外を投げる。
- 触るとき: スキーマの変更や索引の追加をするとき。ここでスキーマを上げる。
- 呼び出し先: `db.objectStoreNames.contains()`, `event.target.transaction.objectStore()`, `lazy.IndexedDB.open()`, `store.indexNames.contains()`
- 条件付き依存: `if (!db.objectStoreNames.contains(MONITOR_STORE_NAME))` → `db.createObjectStore()`
- 条件付き依存: `if (!db.objectStoreNames.contains(MONITOR_STORE_NAME))` → `store.createIndex()`
- 条件付き依存: `if (!store.indexNames.contains(CREATED_AT_INDEX))` → `store.createIndex()`
- 条件付き依存: `if (this.#shuttingDown && !this.#pendingWrites.size)` → `database.close()`
- 条件付き依存: `if (this.#shuttingDown && !this.#pendingWrites.size)` → `lazy.log.warn()`
- 参照: `error.message`, `this.#db`, `this.#db.onclose`, `this.#db.onversionchange`, `this.#pendingWrites.size`, `this.#shuttingDown`

## this.#db.onversionchange()
- 位置: L489-492
- 役割: 別の場所で DB のバージョンが変わったとき、接続を閉じて次回に開き直す。
- 触るとき: 複数の接続が競合したときの挙動を変えるとき。
- 呼び出し先: `this.#closeDatabase()`
- 参照: `this.#promiseDb`

## this.#db.onclose()
- 位置: L493-496
- 役割: DB が閉じられたとき、保持している参照を消す。
- 触るとき: 予期せず閉じられた接続の扱いを変えるとき。
- 参照: `this.#db`, `this.#promiseDb`

## MonitorStoreImpl.#ensureDatabase()
- 位置: async L500-529
- 役割: DB の接続を 1 つにまとめて用意する。必要なら起動時の削除フラグを見て DB を消してから開く。新しすぎるスキーマなら分かりやすい例外にする。
- 触るとき: DB を開く経路や、スキーマが新しすぎるときのエラーを変えるとき。
- 呼び出し先: `isNewerSchemaError()`, `lazy.log.warn()`, `this.#closeDatabase()`, `this.#openDatabase()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.#closeDatabase()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.#deleteDatabase()`
- 参照: `this.#promiseDb`, `this.#removeDatabaseOnStartup`

## MonitorStoreImpl.#deleteDatabase()
- 位置: async L531-539
- 役割: DB を削除する。失敗したら次回起動時に削除するよう pref を立てる。
- 触るとき: DB の削除に失敗したときの後始末を変えるとき。
- 呼び出し先: `lazy.IndexedDB.deleteDatabase()`, `wrapRequest()`
- 参照: `this.#removeDatabaseOnStartup`

## MonitorStoreImpl.#closeDatabase()
- 位置: L541-555
- 役割: 開いている DB 接続のイベント参照を外してから閉じ、参照を消す。
- 触るとき: DB を閉じる手順を変えるとき。
- 呼び出し先: `db.close()`, `lazy.log.warn()`
- 参照: `db.onclose`, `db.onversionchange`, `error.message`, `this.#db`

## MonitorStoreImpl.#addShutdownBlocker()
- 位置: L557-578
- 役割: 終了時に保存の完了を待つブロッカーを 1 回だけ登録し、状態を調べる関数も渡す。
- 触るとき: 終了時にブロッカーで待つ対象を増やすとき。
- 呼び出し先: `this.#shutdownClient.addBlocker()`
- 参照: `this.#asyncShutdownBlocker`, `this.#shutdownBlockerAdded`

## fetchState()
- 位置: L566-574
- 役割: 終了時のブロッカーが表示する状態(DB が開いているか、待機中の書き込み)を返す。
- 触るとき: 終了が遅れたときに何を表示するかを変えるとき。
- 呼び出し先: `Array.from()`, `Date.now()`
- 参照: `pendingWrite.operation`, `pendingWrite.queuedAt`, `pendingWrite.startedAt`, `this.#db`, `this.#pendingWrites`, `this.#shuttingDown`

## MonitorStoreImpl.#removeShutdownBlocker()
- 位置: L580-587
- 役割: 登録済みのシャットダウンブロッカーを外す。
- 触るとき: 終了処理の登録解除の条件を変えるとき。
- 呼び出し先: `this.#shutdownClient.removeBlocker()`
- 参照: `this.#asyncShutdownBlocker`, `this.#shutdownBlockerAdded`

## MonitorStoreImpl.#removeDatabaseOnStartup()
- 位置: L589-594
- 役割: 起動時に DB を削除するかどうかの pref を読む。
- 触るとき: 次回起動時に保存データを消す仕組みを確認するとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## MonitorStoreImpl.#removeDatabaseOnStartup()
- 位置: L596-598
- 役割: 起動時に DB を削除するかどうかの pref を書く。
- 触るとき: DB の削除を次回起動に予約する経路を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## MonitorStoreImpl.databaseName()
- 位置: L600-602
- 役割: DB の名前(monitor-store)を返す。
- 触るとき: DB の名前を変えるとき。変えると既存データは読めなくなる。

## MonitorStoreImpl.databaseVersion()
- 位置: L604-606
- 役割: 現在のスキーマのバージョン番号を返す。
- 触るとき: スキーマを上げるとき。

## MonitorStoreImpl.objectStoreName()
- 位置: L608-610
- 役割: 監視を保存するオブジェクトストアの名前(monitors)を返す。
- 触るとき: 保存先のストア名を変えるとき。
