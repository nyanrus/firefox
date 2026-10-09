# browser/components/sessionstore/SessionLogger.sys.mjs

source: browser/components/sessionstore/SessionLogger.sys.mjs
source-hash: 1659e9b6153536051df19b21decf73ab4bc0f6f5
lines: 136

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Log.repository.getLogger()`, `XPCOMUtils.declareLazy()`, `sessionStoreLogger.manageLevelFromPref()`

## SessionLogManager.constructor()
- 位置: L34-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.AsyncShutdown.profileBeforeChange.addBlocker()`, `super()`, `this.#observers.add()`, `this.stop()`
- 条件付き依存: `if (this._fileAppenderChangeTopic)` → `Services.obs.addObserver()`
- 条件付き依存: `if (this._fileAppenderChangeTopic)` → `this.#observers.add()`
- 参照: `this._fileAppenderChangeTopic`
- XPCOM: `Services.obs`

## SessionLogManager.getLogFilename()
- 位置: L53-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.getLogFilename()`
- 条件付き依存: `if (!this.#startupTime)` → `Services.startup.getStartupInfo().main.getTime()`
- 条件付き依存: `if (!this.#startupTime)` → `Services.startup.getStartupInfo()`
- 参照: `this.#startupTime`
- XPCOM: `Services.startup`

## SessionLogManager.stop()
- 位置: async L61-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observers.has()`, `this.finalize()`, `this.requestLogFlush()`
- 条件付き依存: `if (this.#observers.has("sessionstore-windows-restored"))` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#observers.has("sessionstore-windows-restored"))` → `this.#observers.delete()`
- 条件付き依存: `if ( this._fileAppenderChangeTopic && this.#observers.has(this._fileAppenderChangeTopic) )` → `Services.obs.removeObserver()`
- 条件付き依存: `if ( this._fileAppenderChangeTopic && this.#observers.has(this._fileAppenderChangeTopic) )` → `this.#observers.delete()`
- 参照: `this.#isStartingUp`, `this._fileAppenderChangeTopic`
- XPCOM: `Services.obs`

## SessionLogManager.observe()
- 位置: L78-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Services.obs.removeObserver()`, `this.#observers.delete()`, `this.requestLogFlush()`
- 条件付き依存: `if (shouldFlush)` → `this.requestLogFlush()`
- 参照: `lazy.logFlushIntervalSeconds`, `this.#isStartingUp`, `this._fileAppender.lastFlushTime`, `this._fileAppender.sawError`, `this._fileAppenderChangeTopic`
- XPCOM: `Services.obs`

## SessionLogManager.requestLogFlush()
- 位置: async L109-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetFileLog()`
- 条件付き依存: `if (this.#idleCallbackId)` → `lazy.cancelIdleCallback()`
- 条件付き依存: `if (!immediate)` → `lazy.requestIdleCallback()`
- 参照: `this.#idleCallbackId`
