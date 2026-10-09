# browser/components/sessionstore/SessionLogger.sys.mjs

source: browser/components/sessionstore/SessionLogger.sys.mjs
source-hash: 1659e9b6153536051df19b21decf73ab4bc0f6f5
lines: 136

## <module>
- 役割: セッションストアのログを専用のログファイルへ書き出すマネージャー(SessionLogManager)を作り、ログレベルを設定から読み込む。
- 呼び出し先: `ChromeUtils.generateQI()`, `Log.repository.getLogger()`, `XPCOMUtils.declareLazy()`, `sessionStoreLogger.manageLevelFromPref()`

## SessionLogManager.constructor()
- 位置: L34-51
- 役割: 起動完了の通知とログファイル追加の通知を監視し、終了時にログを確定させるシャットダウンブロッカーを登録する。
- 触るとき: 起動直後にログがいつフラッシュされるか、または終了時にログが失われないかを調べるとき。
- 呼び出し先: `Services.obs.addObserver()`, `lazy.AsyncShutdown.profileBeforeChange.addBlocker()`, `super()`, `this.#observers.add()`, `this.stop()`
- 条件付き依存: `if (this._fileAppenderChangeTopic)` → `Services.obs.addObserver()`
- 条件付き依存: `if (this._fileAppenderChangeTopic)` → `this.#observers.add()`
- 参照: `this._fileAppenderChangeTopic`
- XPCOM: `Services.obs`

## SessionLogManager.getLogFilename()
- 位置: L53-59
- 役割: 起動時刻を初回だけ取得し、その起動単位のログファイル名を返す。引数の既定の接頭辞は success。
- 触るとき: 同じ起動中の成功ログと失敗ログが同じファイルに追記されるかを確認するとき。
- 呼び出し先: `super.getLogFilename()`
- 条件付き依存: `if (!this.#startupTime)` → `Services.startup.getStartupInfo().main.getTime()`
- 条件付き依存: `if (!this.#startupTime)` → `Services.startup.getStartupInfo()`
- 参照: `this.#startupTime`
- XPCOM: `Services.startup`

## SessionLogManager.stop()
- 位置: async L61-76
- 役割: 起動完了と追加の通知の監視を外し、ログを強制的にフラッシュしてファイナライズする。
- 触るとき: ブラウザ終了時にログの書き出しが抜けないかを確認するとき、またはシャットダウン処理の順序を変えるとき。
- 呼び出し先: `this.#observers.has()`, `this.finalize()`, `this.requestLogFlush()`
- 条件付き依存: `if (this.#observers.has("sessionstore-windows-restored"))` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#observers.has("sessionstore-windows-restored"))` → `this.#observers.delete()`
- 条件付き依存: `if ( this._fileAppenderChangeTopic && this.#observers.has(this._fileAppenderChangeTopic) )` → `Services.obs.removeObserver()`
- 条件付き依存: `if ( this._fileAppenderChangeTopic && this.#observers.has(this._fileAppenderChangeTopic) )` → `this.#observers.delete()`
- 参照: `this.#isStartingUp`, `this._fileAppenderChangeTopic`
- XPCOM: `Services.obs`

## SessionLogManager.observe()
- 位置: L78-107
- 役割: 起動完了の通知では起動中フラグを下げてフラッシュを予約する。ログ追加の通知では、書き込みエラーがあるか、起動完了後で前回フラッシュから logFlushIntervalSeconds(既定 3600 秒)を超えていればフラッシュを予約する。
- 触るとき: ログファイルへの書き出し頻度を変えるとき。起動中の追加はフラッシュせず、起動完了後まで溜めておく点に注意する。
- 呼び出し先: `Date.now()`, `Services.obs.removeObserver()`, `this.#observers.delete()`, `this.requestLogFlush()`
- 条件付き依存: `if (shouldFlush)` → `this.requestLogFlush()`
- 参照: `lazy.logFlushIntervalSeconds`, `this.#isStartingUp`, `this._fileAppender.lastFlushTime`, `this._fileAppender.sawError`, `this._fileAppenderChangeTopic`
- XPCOM: `Services.obs`

## SessionLogManager.requestLogFlush()
- 位置: async L109-124
- 役割: アイドル時にログファイルを切り替えるよう予約する。予約済みで immediate が偽なら何もせず戻り、immediate が真なら予約を取り消して即座に resetFileLog を呼ぶ。
- 触るとき: 終了時のログ確定や、起動完了時のフラッシュを呼び出す箇所を変えるとき、二重に予約されないかを見る。
- 呼び出し先: `this.resetFileLog()`
- 条件付き依存: `if (this.#idleCallbackId)` → `lazy.cancelIdleCallback()`
- 条件付き依存: `if (!immediate)` → `lazy.requestIdleCallback()`
- 参照: `this.#idleCallbackId`
