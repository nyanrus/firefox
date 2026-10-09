# browser/components/downloads/DownloadsMacFinderProgress.sys.mjs

source: browser/components/downloads/DownloadsMacFinderProgress.sys.mjs
source-hash: 6ae7d3fa6b37a1ad44601f8cad85c1af8c6ba687
lines: 83

## <module>
- 役割: macOS の Finder に表示するダウンロード進捗を、ダウンロード一覧のイベントから nsIMacFinderProgress へ橋渡しする。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## register()
- 位置: L25-33
- 役割: ダウンロード一覧に自身を view として一度だけ登録する。2 回目以降の呼び出しは何もしない。
- 触るとき: macOS でウィンドウが複数開かれても Finder 進捗の監視が二重登録されないことを確認したいとき、登録の契機を変えるとき。
- 条件付き依存: `if (!this._finderProgresses)` → `lazy.Downloads.getList(lazy.Downloads.ALL).then()`
- 条件付き依存: `if (!this._finderProgresses)` → `lazy.Downloads.getList()`
- 条件付き依存: `if (!this._finderProgresses)` → `list.addView()`
- 参照: `lazy.Downloads.ALL`, `this._finderProgresses`

## onDownloadAdded()
- 位置: L35-57
- 役割: 停止していないダウンロードごとに Finder 進捗オブジェクトを作り、パスをキーに保持する。
- 触るとき: 新規ダウンロードが Finder に表示されない、キャンセル操作が効かない、といった開始時の不具合を調べるとき。
- 呼び出し先: `Cc[ "@mozilla.org/widget/macfinderprogress;1" ].createInstance()`, `download.cancel()`, `download.cancel().catch()`, `download.removePartialData()`, `download.removePartialData().catch()`, `finderProgress.init()`, `this._finderProgresses.set()`
- 条件付き依存: `if (download.hasProgress)` → `finderProgress.updateProgress()`
- 条件付き依存: `if (!(download.hasProgress))` → `finderProgress.updateProgress()`
- 参照: `Ci.nsIMacFinderProgress`, `console.error`, `download.currentBytes`, `download.hasProgress`, `download.stopped`, `download.target.path`, `download.totalBytes`
- XPCOM: `nsIMacFinderProgress` / `@mozilla.org/widget/macfinderprogress;1`

## onDownloadChanged()
- 位置: L59-72
- 役割: 進捗を更新し、停止したダウンロードは終了させて追跡から外す。未追跡なら onDownloadAdded に回す。
- 触るとき: 再開されたダウンロードが Finder 進捗に出てこない、または完了後も進捗が残るといった問題を調べるとき。
- 呼び出し先: `this._finderProgresses.get()`
- 条件付き依存: `if (!finderProgress)` → `this.onDownloadAdded()`
- 条件付き依存: `if (download.stopped)` → `finderProgress.end()`
- 条件付き依存: `if (download.stopped)` → `this._finderProgresses.delete()`
- 条件付き依存: `if (!(download.stopped))` → `finderProgress.updateProgress()`
- 参照: `download.currentBytes`, `download.stopped`, `download.target.path`, `download.totalBytes`

## onDownloadRemoved()
- 位置: L74-81
- 役割: ダウンロードが一覧から消えたとき、対応する Finder 進捗を終了して追跡表から削除する。
- 触るとき: 履歴からダウンロードを削除した後に Finder の進捗表示が残るときに見る。
- 呼び出し先: `this._finderProgresses.get()`
- 条件付き依存: `if (finderProgress)` → `finderProgress.end()`
- 条件付き依存: `if (finderProgress)` → `this._finderProgresses.delete()`
- 参照: `download.target.path`
