# browser/extensions/newtab/lib/DownloadsManager.sys.mjs

source: browser/extensions/newtab/lib/DownloadsManager.sys.mjs
source-hash: d29bcd59e70df7e2aebfd65ce1571ddbd30a4c21
lines: 191

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## DownloadsManager.constructor()
- 位置: L22-27
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._downloadData`, `this._downloadItems`, `this._downloadTimer`, `this._store`

## DownloadsManager.setTimeout()
- 位置: L29-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`
- XPCOM: [`nsITimer`](../../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## DownloadsManager.formatDownload()
- 位置: L35-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsViewUI.getDisplayName()`, `lazy.DownloadsViewUI.getSizeWithUnits()`
- 参照: `download.endTime`, `download.source.referrerInfo?.originalReferrer?.spec`, `download.source.url`, `download.target.path`, `lazy.DownloadsCommon.strings.sizeUnknown`, `new URL(download.source.url).hostname`

## DownloadsManager.init()
- 位置: L50-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadsCommon.getData()`, `this._downloadData.addView()`
- 参照: `this._downloadData`, `this._store`

## DownloadsManager.onDownloadAdded()
- 位置: L61-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._downloadItems.has()`
- 条件付き依存: `if (!this._downloadItems.has(download.source.url))` → `this._downloadItems.set()`
- 条件付き依存: `if (!(this._downloadTimer))` → `this.setTimeout()`
- 条件付き依存: `if (!(this._downloadTimer))` → `this._store.dispatch()`
- 参照: `at.DOWNLOAD_CHANGED`, `download.source.url`, `this._downloadTimer`, `this._downloadTimer.delay`

## DownloadsManager.onDownloadRemoved()
- 位置: L77-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._downloadItems.has()`
- 条件付き依存: `if (this._downloadItems.has(download.source.url))` → `this._downloadItems.delete()`
- 条件付き依存: `if (this._downloadItems.has(download.source.url))` → `this._store.dispatch()`
- 参照: `at.DOWNLOAD_CHANGED`, `download.source.url`

## DownloadsManager.getDownloads()
- 位置: async L84-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `[...this._downloadItems.values()] .filter()`, `[...this._downloadItems.values()] .filter(download => download.endTime > downloadThreshold) .sort()`, `lazy.NewTabUtils.blockedLinks.isBlocked()`, `results.push()`, `this._downloadItems.values()`, `this.formatDownload()`
- 条件付き依存: `if (onlyExists)` → `download.refresh()`
- 参照: `download.endTime`, `download.source`, `download.source.url.length`, `download.succeeded`, `download.target.exists`, `download1.endTime`, `download2.endTime`, `results.length`, `this._downloadItems.size`

## DownloadsManager.uninit()
- 位置: L135-144
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._downloadData)` → `this._downloadData.removeView()`
- 条件付き依存: `if (this._downloadTimer)` → `this._downloadTimer.cancel()`
- 参照: `this._downloadData`, `this._downloadTimer`

## DownloadsManager.onAction()
- 位置: L146-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["window", "tab", "tabshifted"].includes()`, `doDownloadAction()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.DownloadsCommon.copyDownloadLink()`, `lazy.DownloadsCommon.deleteDownload()`, `lazy.DownloadsCommon.deleteDownload(download).catch()`, `lazy.DownloadsCommon.openDownload()`, `lazy.DownloadsCommon.showDownloadedFile()`, `this.uninit()`
- 参照: `action.data.event`, `action.type`, `at.COPY_DOWNLOAD_LINK`, `at.OPEN_DOWNLOAD_FILE`, `at.REMOVE_DOWNLOAD_FILE`, `at.SHOW_DOWNLOAD_FILE`, `at.UNINIT`, `console.error`, `download.target.path`, `lazy.FileUtils.File`

## doDownloadAction()
- 位置: L147-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._downloadItems.get()`
- 条件付き依存: `if (download)` → `callback()`
- 参照: `action.data.url`
