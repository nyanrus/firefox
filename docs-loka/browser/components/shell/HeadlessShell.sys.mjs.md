# browser/components/shell/HeadlessShell.sys.mjs

source: browser/components/shell/HeadlessShell.sys.mjs
source-hash: f043cc4d47447af574e1491d94cbdc5ef25faffe
lines: 255

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.registerWindowActor()`

## ScreenshotParent.getDimensions()
- 位置: L12-14
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## loadContentWindow()
- 位置: L27-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `URL.parse()`, `browser.loadURI()`, `progressListeners.add()`, `webProgress.addProgressListener()`
- 条件付き依存: `if (!uri)` → `console.error()`
- 条件付き依存: `if (!uri)` → `Promise.reject()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `URL.parse(url)?.URI`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md) / `Services.scriptSecurityManager`

## onLocationChange()
- 位置: L44-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `progressListeners.delete()`, `resolve()`, `webProgress.removeProgressListener()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `progress.browsingContext.currentWindowGlobal ?.isUncommittedInitialDocument`, `progress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## takeScreenshot()
- 位置: async L78-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.write()`, `actor.getDimensions()`, `browser.browsingContext.currentWindowGlobal.drawSnapshot()`, `browser.browsingContext.currentWindowGlobal.getActor()`, `browser.setAttribute()`, `canvas.getContext()`, `canvas.toBlob()`, `context.drawImage()`, `doc.createElementNS()`, `doc.createXULElement()`, `doc.documentElement.appendChild()`, `dump()`, `fr.readAsArrayBuffer()`, `frame.get()`, `loadContentWindow()`, `snapshot.close()`
- 条件付き依存: `if (frame)` → `frame.destroy()`
- 参照: `browser.style.height`, `browser.style.minHeight`, `browser.style.minWidth`, `browser.style.width`, `canvas.height`, `canvas.width`, `dimensions.innerHeight`, `dimensions.innerWidth`, `dimensions.scrollMaxX`, `dimensions.scrollMaxY`, `dimensions.scrollMinX`, `dimensions.scrollMinY`, `fr.onloadend`, `reader.result`, `windowlessBrowser.document`

## fr.onloadend()
- 位置: L141-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## handleCmdLineArgs()
- 位置: async L157-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.startup.enterLastWindowClosingSurvivalArea()`, `Services.startup.exitLastWindowClosingSurvivalArea()`, `Services.startup.quit()`, `argument.startsWith()`, `cmdLine.getArgument()`, `cmdLine.handleFlag()`, `cmdLine.handleFlagWithParam()`, `dump()`
- 条件付き依存: `if (dimensionsStr)` → `dimensionsStr.split()`
- 条件付き依存: `if (!success)` → `dump()`
- 条件付き依存: `if (argument.startsWith("-"))` → `dump()`
- 条件付き依存: `if (!(argument.startsWith("-")))` → `URLlist.push()`
- 条件付き依存: `if (urlOrFileToSave && !URLlist.length)` → `URLlist.push()`
- 条件付き依存: `if (!path)` → `PathUtils.join()`
- 条件付き依存: `if (URLlist.length == 1)` → `takeScreenshot()`
- 条件付き依存: `if (!(URLlist.length == 1))` → `dump()`
- 参照: `Ci.nsIAppStartup.eForceQuit`, `URLlist.length`, `cmdLine.length`, `cmdLine.workingDirectory.path`, `dimensions.length`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.startup`
