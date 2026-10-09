# browser/tools/mozscreenshots/mozscreenshots/extension/Screenshot.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/Screenshot.sys.mjs
source-hash: 23d9a36758d0c07984588a2562c35001d704187e
lines: 162

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## init()
- 位置: L31-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/file/local;1"].createInstance()`, `dir.exists()`, `dir.initWithPath()`
- 条件付き依存: `if (!dir.exists())` → `dir.create()`
- 参照: `Ci.nsIFile`, `Ci.nsIFile.DIRECTORY_TYPE`, `Services.appinfo.OS`, `this._extensionPath`, `this._imagePrefix`, `this._path`, `this._screenshotFunction`, `this._screenshotLinux`, `this._screenshotOSX`, `this._screenshotWindows`
- XPCOM: [`nsIFile`](../../../../components/shell/nsIShellService.idl.md) / `@mozilla.org/file/local;1` / `Services.appinfo`

## _buildImagePath()
- 位置: L57-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`
- 参照: `this._imageExtension`, `this._imagePrefix`, `this._path`

## captureExternal()
- 位置: async L65-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this._buildImagePath()`, `this._screenshotFunction()`

## _screenshotWindows()
- 位置: L74-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/process/util;1"].createInstance()`, `Services.dirsvc.get()`, `exe.append()`, `exe.exists()`, `process.init()`, `process.runAsync()`, `this._processObserver()`
- 条件付き依存: `if (!exe.exists())` → `Services.dirsvc.get()`
- 条件付き依存: `if (!exe.exists())` → `exe.append()`
- 参照: `Ci.nsIFile`, `Ci.nsIProcess`, `Services.dirsvc.get("CurWorkD", Ci.nsIFile).parent`, `args.length`
- XPCOM: [`nsIFile`](../../../../components/shell/nsIShellService.idl.md) / [`nsIProcess`](../../../../../xpcom/threads/nsIProcess.idl.md) / `@mozilla.org/process/util;1` / `Services.dirsvc`

## _screenshotOSX()
- 位置: L97-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/file/local;1"].createInstance()`, `Cc["@mozilla.org/process/util;1"].createInstance()`, `file.initWithPath()`, `process.init()`, `process.runAsync()`, `this._processObserver()`
- 参照: `Ci.nsIFile`, `Ci.nsIProcess`, `args.length`
- XPCOM: [`nsIFile`](../../../../components/shell/nsIShellService.idl.md) / [`nsIProcess`](../../../../../xpcom/threads/nsIProcess.idl.md) / `@mozilla.org/file/local;1` / `@mozilla.org/process/util;1`

## _screenshotLinux()
- 位置: L119-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/process/util;1"].createInstance()`, `Services.dirsvc.get()`, `exe.append()`, `exe.exists()`, `process.init()`, `process.runAsync()`, `this._processObserver()`
- 条件付き依存: `if (!exe.exists())` → `Services.dirsvc.get()`
- 条件付き依存: `if (!exe.exists())` → `exe.append()`
- 参照: `Ci.nsIFile`, `Ci.nsIProcess`, `Services.dirsvc.get("CurWorkD", Ci.nsIFile).parent`, `args.length`
- XPCOM: [`nsIFile`](../../../../components/shell/nsIShellService.idl.md) / [`nsIProcess`](../../../../../xpcom/threads/nsIProcess.idl.md) / `@mozilla.org/process/util;1` / `Services.dirsvc`

## _processObserver()
- 位置: L142-160
- 役割: (未記入)
- 触るとき: (未記入)

## observe()
- 位置: L144-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`, `setTimeout()`
