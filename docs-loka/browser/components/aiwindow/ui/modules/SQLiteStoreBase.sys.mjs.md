# browser/components/aiwindow/ui/modules/SQLiteStoreBase.sys.mjs

source: browser/components/aiwindow/ui/modules/SQLiteStoreBase.sys.mjs
source-hash: 92f1929e38b70bebd2a0ffae2490ffebc1ef8aac
lines: 566

## <module>
- 役割: AI Window の SQLite 保存ストアの共通基盤。接続の開閉、スキーマ作成と移行、破損時の作り直し、サイズ上限による古いレコードの削除を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SQLiteStoreBase.constructor()
- 位置: L39-43
- 役割: アプリ終了時に接続を閉じるブロッカー関数を作って保持する。
- 触るとき: 終了時に DB 接続が閉じられない問題を追うとき。
- 参照: `this.#asyncShutdownBlocker`

## this.#asyncShutdownBlocker()
- 位置: async L40-42
- 役割: アプリ終了時に呼ばれ、開いている接続を閉じる非同期関数。
- 触るとき: 終了処理で接続が残る、または終了の順序を変えたいとき。
- 呼び出し先: `this.#closeConnection()`

## SQLiteStoreBase.logPrefix()
- 位置: L47-49
- 役割: ログ行の接頭辞を返す。サブクラスが必ず上書きする。
- 触るとき: 新しいストアを作るときにログ接頭辞の設定を忘れていないか確認する。

## SQLiteStoreBase.logLevelPref()
- 位置: L51-53
- 役割: ログ出力レベルを決めるプリファレンス名を返す。サブクラスが上書きする。
- 触るとき: ストアごとにログの詳細度を分けたいとき。

## SQLiteStoreBase.shutdownBlockerName()
- 位置: L55-57
- 役割: 終了ブロッカーの名前を返す。サブクラスが必ず上書きする。
- 触るとき: 終了ブロッカーの名前が重複して登録に失敗するとき。

## SQLiteStoreBase.CURRENT_SCHEMA_VERSION()
- 位置: L59-61
- 役割: 現在のスキーマ版数を返す。サブクラスが必ず上書きする。
- 触るとき: テーブル構造を変えて版数を上げるとき。移行 (migrations) と合わせて見る。

## SQLiteStoreBase.databaseFileName()
- 位置: L63-65
- 役割: プロファイル直下の DB ファイル名を返す。サブクラスが必ず上書きする。
- 触るとき: 新しいストアの保存先ファイル名を決めるとき。

## SQLiteStoreBase.prefBranch()
- 位置: L67-69
- 役割: 起動時の DB 削除フラグを読み書きするプリファレンスの枝を返す。サブクラスが必ず上書きする。
- 触るとき: 次回起動時の DB 削除フラグの名前空間を調べるとき。

## SQLiteStoreBase.createEntityStatements()
- 位置: L75-77
- 役割: 新規 DB を作るときに実行する SQL 文の配列を返す。既定では例外を投げる。
- 触るとき: テーブルや索引を追加して、初期化 SQL の一覧に加えるとき。

## SQLiteStoreBase.migrations()
- 位置: L83-85
- 役割: 版数移行の関数の配列を返す。各関数は (conn, version) を受け取る。
- 触るとき: 既存 DB の版数が上がるときに、列の追加や値の変換を書くとき。

## SQLiteStoreBase.findOldestPrunableRecords()
- 位置: async L95-97
- 役割: 剪定の対象となる古いレコードを、指定件数まで返す。サブクラスが必ず実装する。
- 触るとき: 容量上限で消される対象の条件や並び順を決めるとき。

## SQLiteStoreBase.deletePrunableRecord()
- 位置: async L104-106
- 役割: id で指定された剪定対象のレコードを一件削除する。
- 触るとき: 剪定で消す単位を変えるとき、例えば関連するテーブルも一緒に消したいとき。

## SQLiteStoreBase.log()
- 位置: L115-123
- 役割: logPrefix と logLevelPref を使ったコンソールのインスタンスを、初回にだけ作って返す。
- 触るとき: ストアのログを追加するとき、またはログが出ない原因を調べるとき。
- 条件付き依存: `if (!this.#log)` → `console.createInstance()`
- 参照: `this.#log`, `this.logLevelPref`, `this.logPrefix`

## SQLiteStoreBase.connection()
- 位置: L130-132
- 役割: 保持している SQLite 接続を返す。接続前は undefined、閉じた後は null になる。
- 触るとき: サブクラスが接続を直接使う前に、接続が確立しているかを確認するとき。
- 参照: `this.#conn`

## SQLiteStoreBase.databaseFilePath()
- 位置: L139-141
- 役割: プロファイル直下の DB ファイルの絶対パスを組み立てて返す。
- 触るとき: DB ファイルの場所を変えるとき、またはサイズ取得や削除の対象を調べるとき。
- 呼び出し先: `PathUtils.join()`
- 参照: `PathUtils.profileDir`, `this.databaseFileName`

## SQLiteStoreBase.maxDatabaseSizeBytes()
- 位置: L148-150
- 役割: 剪定を始める上限サイズとして、75 MiB を返す。
- 触るとき: ストアごとに上限を変えたいとき、この getter を上書きする。

## SQLiteStoreBase.profilerMarkerCategory()
- 位置: L158-160
- 役割: 接続時のプロファイラマーカーの分類名として SmartWindow を返す。
- 触るとき: 接続マーカーをプロファイラで別のカテゴリに分けたいとき。

## SQLiteStoreBase.ensureDatabase()
- 位置: async L175-231
- 役割: 接続の Promise を一度だけ作って共有する。必要なら削除フラグに従って DB を消し、破損していれば作り直してから接続を返す。
- 触るとき: DB の初期化が失敗する、または破損 DB の扱いを変えるとき。すべての操作の入口なので、起動時の不具合を追うときに最初に見る。
- 呼び出し先: `Promise.withResolvers()`, `deferred.resolve()`, `e.errors?.some()`, `this.#initializeSchema()`, `this.#openConnection()`, `this.#removeDatabaseFiles()`, `this.log.warn()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.log.debug()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.#removeDatabaseFiles()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `deferred.reject()`
- 条件付き依存: `if ( e.result == Cr.NS_ERROR_FILE_CORRUPTED || e.errors?.some(error => error.result == Ci.mozIStorageError.NOTADB) )` → `this.log.warn()`
- 条件付き依存: `if ( e.result == Cr.NS_ERROR_FILE_CORRUPTED || e.errors?.some(error => error.result == Ci.mozIStorageError.NOTADB) )` → `this.#removeDatabaseFiles()`
- 条件付き依存: `if (!this.#conn)` → `this.#openConnection()`
- 条件付き依存: `if (!this.#conn)` → `this.log.error()`
- 条件付き依存: `if (!this.#conn)` → `deferred.reject()`
- 参照: `Ci.mozIStorageError.NOTADB`, `Cr.NS_ERROR_FILE_CORRUPTED`, `deferred.promise`, `e.message`, `e.result`, `e.stack`, `error.result`, `this.#conn`, `this.#promiseConn`, `this.#removeDatabaseOnStartup`

## SQLiteStoreBase.getDatabaseSchemaVersion()
- 位置: async L238-244
- 役割: 接続が無ければ ensureDatabase を呼んでから、DB に保存された版数を返す。
- 触るとき: 版数で分岐する移行や検証の処理を追うとき。
- 呼び出し先: `this.#conn.getSchemaVersion()`
- 条件付き依存: `if (!this.#conn)` → `this.ensureDatabase()`
- 参照: `this.#conn`

## SQLiteStoreBase.setSchemaVersion()
- 位置: async L251-253
- 役割: DB の版数を指定の値に書き換える。
- 触るとき: 移行の最後に版数を進める処理を変えるとき。
- 呼び出し先: `this.#conn.setSchemaVersion()`

## SQLiteStoreBase.getDatabaseSize()
- 位置: async L260-272
- 役割: 接続を確保してから、DB ファイルのディスク上のサイズをバイトで返す。
- 触るとき: DB の大きさを計測や表示に使うとき。実使用量が必要なら getDbBytesInUse を見る。
- 呼び出し先: `IOUtils.stat()`, `this.ensureDatabase()`, `this.ensureDatabase().catch()`, `this.log.error()`
- 参照: `e.message`, `e.stack`, `stats.size`, `this.databaseFilePath`

## SQLiteStoreBase.destroyDatabase()
- 位置: async L277-280
- 役割: DB ファイル群を削除し、接続の Promise を null に戻す。
- 触るとき: 保存データを全消去する機能を作るとき、またはリセット後に再接続されるかを確かめるとき。
- 呼び出し先: `this.#removeDatabaseFiles()`
- 参照: `this.#promiseConn`

## SQLiteStoreBase.applyMigrations()
- 位置: async L287-295
- 役割: migrations の関数を順に、接続と現在の版数を渡して実行する。関数でない要素は飛ばす。
- 触るとき: 移行の実行順や失敗時の扱いを変えるとき。
- 呼び出し先: `migration()`
- 参照: `this.#conn`, `this.migrations`

## SQLiteStoreBase.getDbBytesInUse()
- 位置: async L303-309
- 役割: dbstat から各ページのサイズを合計し、DB が実際に使っているバイト数を返す。
- 触るとき: 剪定の判定に使う実使用量を調べるとき、またはディスク上のサイズとの差を確かめるとき。
- 呼び出し先: `rows[0].getResultByName()`, `this.#conn.execute()`

## SQLiteStoreBase.pruneDatabase()
- 位置: async L321-384
- 役割: 実使用量が上限を超えていれば古いレコードを 50 件ずつ消し、目標量まで縮むか打ち切りに当たるまで繰り返し、最後に空き領域を回収する。
- 触るとき: 容量上限の挙動 (削除量、打ち切り条件、空き領域の回収) を変えるとき、または DB が縮まないと感じるとき。
- 呼び出し先: `IOUtils.exists()`, `Math.max()`, `this.#conn.execute()`, `this.deletePrunableRecord()`, `this.ensureDatabase()`, `this.ensureDatabase().catch()`, `this.findOldestPrunableRecords()`, `this.getDbBytesInUse()`, `this.log.error()`
- 参照: `e.message`, `e.stack`, `oldestRecords.length`, `record.id`, `this.databaseFilePath`, `this.maxDatabaseSizeBytes`

## SQLiteStoreBase.#openConnection()
- 位置: async L393-440
- 役割: SQLite 接続を開き、WAL などの PRAGMA を設定して終了ブロッカーを登録する。PRAGMA の失敗は警告に留める。
- 触るとき: 接続時の PRAGMA 設定を変えるとき、または接続が開けない、遅いと感じるとき。
- 呼び出し先: `Services.profiler.IsActive()`, `lazy.Sqlite.openConnection()`, `lazy.Sqlite.shutdown.addBlocker()`, `this.#conn.execute()`, `this.log.debug()`, `this.log.error()`, `this.log.warn()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `IOUtils.stat()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `(stat.size / 1048576).toFixed()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `ChromeUtils.now()`
- 条件付き依存: `if (markerData)` → `ChromeUtils.addProfilerMarker()`
- 参照: `e.message`, `e.stack`, `markerData.sizeLabel`, `markerData.startTime`, `stat.size`, `this.#asyncShutdownBlocker`, `this.#conn`, `this.databaseFilePath`, `this.logPrefix`, `this.profilerMarkerCategory`, `this.shutdownBlockerName`
- XPCOM: `Services.profiler`

## SQLiteStoreBase.#closeConnection()
- 位置: async L447-460
- 役割: 終了ブロッカーを外してから接続を閉じ、接続の参照を null にする。接続が無ければ何もしない。
- 触るとき: 接続の終了処理を変えるとき、または閉じた後の接続が使われる問題を追うとき。
- 呼び出し先: `lazy.Sqlite.shutdown.removeBlocker()`, `this.#conn.close()`, `this.log.debug()`, `this.log.warn()`
- 参照: `e.message`, `this.#asyncShutdownBlocker`, `this.#conn`

## SQLiteStoreBase.#initializeSchema()
- 位置: async L469-495
- 役割: DB の版数を見て、新規なら表を作り、古ければ移行を実行し、新しすぎれば版数だけを書き換える。
- 触るとき: スキーマ版数を上げたのに移行が走らない、または失敗するとき。
- 呼び出し先: `this.#conn.executeTransaction()`, `this.applyMigrations()`, `this.getDatabaseSchemaVersion()`, `this.setSchemaVersion()`
- 条件付き依存: `if (version > this.CURRENT_SCHEMA_VERSION)` → `this.setSchemaVersion()`
- 条件付き依存: `if (version == 0)` → `this.#createDatabaseEntities()`
- 条件付き依存: `if (version == 0)` → `this.#conn.setSchemaVersion()`
- 参照: `this.CURRENT_SCHEMA_VERSION`

## SQLiteStoreBase.#createDatabaseEntities()
- 位置: async L502-506
- 役割: createEntityStatements の SQL を順に実行して、表や索引を作る。
- 触るとき: 新しい表や索引の初期化 SQL を足して、その実行を確かめるとき。
- 呼び出し先: `this.#conn.execute()`
- 参照: `this.createEntityStatements`

## SQLiteStoreBase.#removeDatabaseFiles()
- 位置: async L513-537
- 役割: 接続を閉じ、DB 本体と -wal, -shm を削除する。失敗時は次回起動で削除するよう印を付け、例外を再送出する。
- 触るとき: DB の削除が失敗して残る問題を追うとき、または削除対象のファイルを増やすとき。
- 呼び出し先: `IOUtils.remove()`, `PathUtils.join()`, `this.#closeConnection()`, `this.log.debug()`, `this.log.warn()`
- 参照: `PathUtils.profileDir`, `this.#removeDatabaseOnStartup`, `this.databaseFileName`, `this.databaseFilePath`

## SQLiteStoreBase.#removeDatabaseOnStartup()
- 位置: L544-549
- 役割: 次回起動時に DB を削除するかを示す、プリファレンスの値を読む。
- 触るとき: 起動時削除フラグの参照元をたどるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.prefBranch`
- XPCOM: `Services.prefs`

## SQLiteStoreBase.#removeDatabaseOnStartup()
- 位置: L558-564
- 役割: 次回起動時に DB を削除するよう、プリファレンスの値を書き込む。
- 触るとき: DB の削除を次回起動に持ち越す経路を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.log.debug()`
- 参照: `this.prefBranch`
- XPCOM: `Services.prefs`
