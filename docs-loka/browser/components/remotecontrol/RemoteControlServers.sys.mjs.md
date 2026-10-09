# browser/components/remotecontrol/RemoteControlServers.sys.mjs

source: browser/components/remotecontrol/RemoteControlServers.sys.mjs
source-hash: fb100590232b9deb98ea40ca632c8efa85031a6e
lines: 208

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## RemoteControlServersImpl.constructor()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#listeners`

## RemoteControlServersImpl.enabled()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.ENABLE_WEBDRIVER`, `lazy.Marionette.enabled`, `lazy.RemoteAgent.enabled`

## RemoteControlServersImpl.hasActiveSession()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.hasActiveWebDriverSession()`
- 参照: `AppConstants.ENABLE_WEBDRIVER`

## RemoteControlServersImpl.runningDynamically()
- 位置: L61-67
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.ENABLE_WEBDRIVER`, `lazy.Marionette.isDynamicStartRunning`, `lazy.RemoteAgent.isDynamicStartRunning`

## RemoteControlServersImpl.addListener()
- 位置: L76-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.add()`
- 条件付き依存: `if (!this.#listeners.size)` → `Services.obs.addObserver()`
- 参照: `this.#listeners.size`
- XPCOM: `Services.obs`

## RemoteControlServersImpl.removeListener()
- 位置: L92-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.delete()`
- 条件付き依存: `if (!this.#listeners.size)` → `Services.obs.removeObserver()`
- 参照: `this.#listeners.size`
- XPCOM: `Services.obs`

## RemoteControlServersImpl.observe()
- 位置: L104-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listener()`
- 参照: `this.#listeners`

## RemoteControlServersImpl.#createPortFilePath()
- 位置: async L118-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.makeDirectory()`, `PathUtils.join()`, `Services.dirsvc.get()`, `console.error()`
- 参照: `Ci.nsIFile`, `Services.appinfo.processID`, `Services.dirsvc.get("Home", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.appinfo` / `Services.dirsvc`

## RemoteControlServersImpl.start()
- 位置: async L141-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Marionette.startAtRuntime()`, `lazy.RemoteAgent.startAtRuntime()`, `this.#createPortFilePath()`
- 参照: `AppConstants.ENABLE_WEBDRIVER`

## RemoteControlServersImpl.stop()
- 位置: async L157-168
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.Marionette.isDynamicStartRunning)` → `lazy.Marionette.stopAtRuntime()`
- 条件付き依存: `if (lazy.RemoteAgent.isDynamicStartRunning)` → `lazy.RemoteAgent.stopAtRuntime()`
- 参照: `AppConstants.ENABLE_WEBDRIVER`, `lazy.Marionette.isDynamicStartRunning`, `lazy.RemoteAgent.isDynamicStartRunning`

## setRemoteControlServers()
- 位置: L182-188
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Cu.isInAutomation`

## enabled()
- 位置: L191-193
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `servers.enabled`

## hasActiveSession()
- 位置: L195-197
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `servers.hasActiveSession`

## runningDynamically()
- 位置: L199-201
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `servers.runningDynamically`

## addListener()
- 位置: L203-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `servers.addListener()`

## removeListener()
- 位置: L204-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `servers.removeListener()`

## start()
- 位置: L205-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `servers.start()`

## stop()
- 位置: L206-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `servers.stop()`
