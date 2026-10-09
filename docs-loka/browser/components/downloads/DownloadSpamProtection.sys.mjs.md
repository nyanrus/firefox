# browser/components/downloads/DownloadSpamProtection.sys.mjs

source: browser/components/downloads/DownloadSpamProtection.sys.mjs
source-hash: d12cd2f1321d8d7208316e2dcb59fa03d23d2dd3
lines: 313

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## WindowSpamProtection.constructor()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._window`

## WindowSpamProtection.spamList()
- 位置: L70-78
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.DownloadList`, `this._blocking`, `this._spamList`

## WindowSpamProtection.indicator()
- 位置: L87-92
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._indicator)` → `lazy.DownloadsCommon.getIndicatorData()`
- 参照: `this._indicator`, `this._window`

## WindowSpamProtection.addDownloadSpam()
- 位置: L100-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._downloadSpamForUrl.has()`, `this._downloadSpamForUrl.set()`, `this._maybeAddViews()`, `this._notifyDownloadSpamAdded()`, `this.spamList.add()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this._downloadSpamForUrl.get()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this.indicator.onDownloadStateChanged()`
- 参照: `downloadSpam.blockedDownloadsCount`, `this._blocking`

## WindowSpamProtection._notifyDownloadSpamAdded()
- 位置: L126-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.DownloadsCommon.summarizeDownloads()`, `this.indicator._activeDownloads()`, `this.indicator.onDownloadAdded()`
- 条件付き依存: `if ( !hasActiveDownloads && this._window === lazy.BrowserWindowTracker.getTopWindow() )` → `this._window.DownloadsPanel.showPanel()`
- 条件付き依存: `if (!( !hasActiveDownloads && this._window === lazy.BrowserWindowTracker.getTopWindow() ))` → `this._window.getAttention()`
- 参照: `lazy.DownloadsCommon.summarizeDownloads( this.indicator._activeDownloads() ).numDownloading`, `this._window`

## WindowSpamProtection.removeDownloadSpamForUrl()
- 位置: L148-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._downloadSpamForUrl.has()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this._downloadSpamForUrl.get()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this.spamList.remove()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this.indicator.onDownloadRemoved()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this._downloadSpamForUrl.delete()`

## WindowSpamProtection.registerView()
- 位置: L164-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeAddViews()`, `this._pendingViews.add()`, `this.spamList?._views.has()`

## WindowSpamProtection._maybeAddViews()
- 位置: L176-185
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.spamList)` → `this.spamList._views.has()`
- 条件付き依存: `if (!this.spamList._views.has(view))` → `this.spamList.addView()`
- 条件付き依存: `if (this.spamList)` → `this._pendingViews.clear()`
- 参照: `this._pendingViews`, `this.spamList`

## WindowSpamProtection.removeAllViews()
- 位置: L191-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._pendingViews.clear()`
- 条件付き依存: `if (this.spamList)` → `this.spamList.removeView()`
- 参照: `this.spamList`, `this.spamList._views`

## DownloadSpamProtection.update()
- 位置: L222-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._forWindowMap.get()`, `this._forWindowMap.set()`, `wsp.addDownloadSpam()`
- 条件付き依存: `if (window == null)` → `lazy.DownloadsCommon.log()`

## DownloadSpamProtection.getSpamListForWindow()
- 位置: L245-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._forWindowMap.get()`
- 参照: `this._forWindowMap.get(window)?.spamList`

## DownloadSpamProtection.removeDownloadSpamForWindow()
- 位置: L256-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._forWindowMap.get()`, `wsp?.removeDownloadSpamForUrl()`

## DownloadSpamProtection.register()
- 位置: L271-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._forWindowMap.get()`, `this._forWindowMap.set()`, `wsp.registerView()`

## DownloadSpamProtection.unregister()
- 位置: L284-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._forWindowMap.get()`
- 条件付き依存: `if (wsp)` → `wsp.removeAllViews()`
- 条件付き依存: `if (wsp)` → `this._forWindowMap.delete()`

## DownloadSpam.constructor()
- 位置: L300-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`, `this.blockedDownloadsCount`, `this.error`, `this.hasBlockedData`, `this.source`, `this.stopped`, `this.target`
