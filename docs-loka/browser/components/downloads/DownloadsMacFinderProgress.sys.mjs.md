# browser/components/downloads/DownloadsMacFinderProgress.sys.mjs

source: browser/components/downloads/DownloadsMacFinderProgress.sys.mjs
source-hash: 6ae7d3fa6b37a1ad44601f8cad85c1af8c6ba687
lines: 83

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## register()
- 位置: L25-33
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._finderProgresses)` → `lazy.Downloads.getList(lazy.Downloads.ALL).then()`
- 条件付き依存: `if (!this._finderProgresses)` → `lazy.Downloads.getList()`
- 条件付き依存: `if (!this._finderProgresses)` → `list.addView()`
- 参照: `lazy.Downloads.ALL`, `this._finderProgresses`

## onDownloadAdded()
- 位置: L35-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/widget/macfinderprogress;1" ].createInstance()`, `download.cancel()`, `download.cancel().catch()`, `download.removePartialData()`, `download.removePartialData().catch()`, `finderProgress.init()`, `this._finderProgresses.set()`
- 条件付き依存: `if (download.hasProgress)` → `finderProgress.updateProgress()`
- 条件付き依存: `if (!(download.hasProgress))` → `finderProgress.updateProgress()`
- 参照: `Ci.nsIMacFinderProgress`, `console.error`, `download.currentBytes`, `download.hasProgress`, `download.stopped`, `download.target.path`, `download.totalBytes`
- XPCOM: `nsIMacFinderProgress` / `@mozilla.org/widget/macfinderprogress;1`

## onDownloadChanged()
- 位置: L59-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._finderProgresses.get()`
- 条件付き依存: `if (!finderProgress)` → `this.onDownloadAdded()`
- 条件付き依存: `if (download.stopped)` → `finderProgress.end()`
- 条件付き依存: `if (download.stopped)` → `this._finderProgresses.delete()`
- 条件付き依存: `if (!(download.stopped))` → `finderProgress.updateProgress()`
- 参照: `download.currentBytes`, `download.stopped`, `download.target.path`, `download.totalBytes`

## onDownloadRemoved()
- 位置: L74-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._finderProgresses.get()`
- 条件付き依存: `if (finderProgress)` → `finderProgress.end()`
- 条件付き依存: `if (finderProgress)` → `this._finderProgresses.delete()`
- 参照: `download.target.path`
