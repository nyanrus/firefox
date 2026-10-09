# browser/modules/FilePickerCrashed.sys.mjs

source: browser/modules/FilePickerCrashed.sys.mjs
source-hash: 7e82e9d4b201d3fc5315dd8bdbd3904984aa4d39
lines: 128

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## observe()
- 位置: async L23-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bag.getPropertyAsBool()`, `bag.getPropertyAsInterface()`, `bag.getPropertyAsUint32()`, `console.error()`, `file_error.toString()`, `file_error.toString(16).padLeft()`, `nbox.appendNotification()`, `subject.QueryInterface()`, `window.gBrowser.getNotificationBox()`
- 条件付き依存: `if (!window?.gBrowser)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!window)` → `console.error()`
- 条件付き依存: `if (file)` → `buttons.push()`
- 参照: `Ci.nsIFile`, `Ci.nsIFilePicker.modeSave`, `Ci.nsILoadContext`, `Ci.nsIPropertyBag2`, `ctx.topChromeWindow`, `file.path`, `nbox.PRIORITY_CRITICAL_LOW`, `notification.persistence`, `window?.gBrowser`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `nsIFilePicker` / [`nsILoadContext`](../../docshell/base/nsILoadContext.idl.md) / [`nsIPropertyBag2`](../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## callback()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.showDownloadedFile()`
