# browser/components/downloads/DownloadsTaskbar.sys.mjs

source: browser/components/downloads/DownloadsTaskbar.sys.mjs
source-hash: dabc7df9b7d9bd9bdaac6d985d5ccd7499c275a8
lines: 342

## <module>
- 役割: Windows のタスクバー、macOS の Dock、GTK のウィンドウで進捗表示を出すため、ダウンロード要約を各 OS のインジケーターへ流す。
- 呼び出し先: `Cc["@mozilla.org/widget/macdocksupport;1"].getService()`, `Cc["@mozilla.org/widget/taskbarprogress/gtk;1"].getService()`, `Cc["@mozilla.org/windows-taskbar;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `defineResettableGetter()`

## defineResettableGetter()
- 位置: L14-33
- 役割: 遅延初期化した値をキャッシュするゲッターを定義し、null を代入するとキャッシュを捨てて次回再計算させる。
- 触るとき: テストでタスクバー用の XPCOM 参照を差し替えたり消したりする仕組みを変えるとき。
- 呼び出し先: `Object.defineProperty()`

## get()
- 位置: L18-24
- 役割: 初回アクセス時に callback を実行して結果をキャッシュし、以降は同じ値を返す。
- 触るとき: gInterfaces のどの OS インターフェースが取得できないのかを調べるとき。
- 条件付き依存: `if (typeof result == "undefined")` → `callback()`

## set()
- 位置: L25-31
- 役割: null の代入でキャッシュを消し、それ以外の値は例外で拒否する。
- 触るとき: resetBetweenTests でキャッシュが消えない、または誤って値が入るといった問題を調べるとき。

## DownloadsTaskbarInstance.constructor()
- 位置: L105-107
- 役割: フィルター (公開・非公開・全体) を受け取って保持する。ウィンドウへの登録はここでは行わない。
- 触るとき: 公開用と非公開用のインスタンスの振り分けを変えるとき。
- 参照: `this.#filter`

## DownloadsTaskbarInstance.registerIndicator()
- 位置: async L125-173
- 役割: プラットフォームに応じて Windows・macOS・GTK のどの進捗インターフェースを使うか決め、DownloadSummary を非同期に取得して自身を view に登録する。
- 触るとき: 新しいウィンドウを開いたときに進捗が出ない、または macOS と Linux でインジケーターの取り合いが起きるときに見る。aForcedBackend はテスト用の強制指定。
- 条件付き依存: `if ( aForcedBackend == "windows" || (!aForcedBackend && gInterfaces.winTaskbar) )` → `this.#windowsAttachIndicator()`
- 条件付き依存: `if ( aForcedBackend == "mac" || (!aForcedBackend && gInterfaces.macTaskbarProgress) )` → `this.#taskbarProgresses.add()`
- 条件付き依存: `if ( aForcedBackend == "mac" || (!aForcedBackend && gInterfaces.macTaskbarProgress) )` → `Services.obs.addObserver()`
- 条件付き依存: `if ( aForcedBackend == "mac" || (!aForcedBackend && gInterfaces.macTaskbarProgress) )` → `this.#taskbarProgresses.clear()`
- 条件付き依存: `if ( aForcedBackend == "linux" || (!aForcedBackend && gInterfaces.gtkTaskbarProgress) )` → `this.#taskbarProgresses.add()`
- 条件付き依存: `if ( aForcedBackend == "linux" || (!aForcedBackend && gInterfaces.gtkTaskbarProgress) )` → `this.#attachGtkTaskbarProgress()`
- 条件付き依存: `if (!this.#summary)` → `lazy.Downloads.getSummary()`
- 条件付き依存: `if (!this.#summary)` → `this.#summary.addView()`
- 条件付き依存: `if (!this.#summary)` → `console.error()`
- 参照: `gInterfaces.gtkTaskbarProgress`, `gInterfaces.macTaskbarProgress`, `gInterfaces.winTaskbar`, `this.#filter`, `this.#summary`, `this.#taskbarProgresses.size`
- XPCOM: `Services.obs`

## DownloadsTaskbarInstance.#windowsAttachIndicator()
- 位置: L178-196
- 役割: Windows で、そのウィンドウのトップ docShell に対応する TaskbarProgress を作って一覧へ追加し、ウィンドウ unload 時に外す。
- 触るとき: Windows で複数ウィンドウを開いたり閉じたりしたときにタスクバーの進捗が正しく出るかを確認するとき。
- 呼び出し先: `aWindow.addEventListener()`, `gInterfaces.winTaskbar.getTaskbarProgress()`, `this.#taskbarProgresses.add()`, `this.#taskbarProgresses.delete()`
- 条件付き依存: `if (this.#summary)` → `this.onSummaryChanged()`
- 参照: `aWindow.browsingContext.topChromeWindow`, `this.#summary`

## DownloadsTaskbarInstance.#attachGtkTaskbarProgress()
- 位置: L201-227
- 役割: GTK では進捗を載せるプライマリウィンドウを設定し、そのウィンドウが閉じられたら別の最上位ウィンドウへ付け替える。最後のウィンドウなら一覧を空にする。
- 触るとき: Linux でウィンドウを閉じた後に進捗表示が消える、または残るといった問題を調べるとき。
- 呼び出し先: `aWindow.addEventListener()`, `taskbarProgress.setPrimaryWindow()`, `this.#determineProgressRepresentative()`, `this.#taskbarProgresses.values()`, `this.#taskbarProgresses.values().next()`
- 条件付き依存: `if (this.#summary)` → `this.onSummaryChanged()`
- 条件付き依存: `if (browserWindow)` → `this.#attachGtkTaskbarProgress()`
- 条件付き依存: `if (!(browserWindow))` → `this.#taskbarProgresses.clear()`
- 参照: `this.#summary`, `this.#taskbarProgresses.values().next().value`

## DownloadsTaskbarInstance.#determineProgressRepresentative()
- 位置: L232-240
- 役割: 進捗表示を引き継ぐ別のトップウィンドウを、フィルターに合わせて公開・非公開を選んで取得する。
- 触るとき: 閉じられたウィンドウの代わりに進捗を出すウィンドウの選び方を変えるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (this.#filter == lazy.Downloads.ALL)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 参照: `lazy.Downloads.ALL`, `lazy.Downloads.PRIVATE`, `this.#filter`

## DownloadsTaskbarInstance.reset()
- 位置: L242-248
- 役割: 要約ビューの登録を解除し、保持している進捗インターフェースの一覧を空にする。
- 触るとき: テストの後始末でタスクバーの状態を戻す処理を追うとき。
- 呼び出し先: `this.#taskbarProgresses.clear()`
- 条件付き依存: `if (this.#summary)` → `this.#summary.removeView()`
- 参照: `this.#summary`

## DownloadsTaskbarInstance.updateProgress()
- 位置: L257-261
- 役割: 保持しているすべての進捗インターフェースに、状態と現在値・最大値を渡す。
- 触るとき: タスクバーの進捗値が実際のダウンロードと合わない問題を、送信側から追うとき。
- 呼び出し先: `progress.setProgressState()`
- 参照: `this.#taskbarProgresses`

## DownloadsTaskbarInstance.onSummaryChanged()
- 位置: L265-289
- 役割: 要約の状態から停止・不確定・通常のどの進捗状態を送るかを決め、現在値は総量を超えないよう丸める。
- 触るとき: 進捗バーが 100% を超える、完了後も残る、または不確定表示にならないといった不具合を調べるとき。
- 条件付き依存: `if (this.#summary.allHaveStopped || this.#summary.progressTotalBytes == 0)` → `this.updateProgress()`
- 条件付き依存: `if (this.#summary.allUnknownSize)` → `this.updateProgress()`
- 条件付き依存: `if (!(this.#summary.allUnknownSize))` → `Math.min()`
- 条件付き依存: `if (!(this.#summary.allUnknownSize))` → `this.updateProgress()`
- 参照: `Ci.nsITaskbarProgress.STATE_INDETERMINATE`, `Ci.nsITaskbarProgress.STATE_NORMAL`, `Ci.nsITaskbarProgress.STATE_NO_PROGRESS`, `this.#summary.allHaveStopped`, `this.#summary.allUnknownSize`, `this.#summary.progressCurrentBytes`, `this.#summary.progressTotalBytes`, `this.#taskbarProgresses.size`
- XPCOM: `nsITaskbarProgress`

## registerIndicator()
- 位置: async L295-305
- 役割: フィルターを決め、対応するインスタンスを作って (なければ) ウィンドウの登録を依頼する。
- 触るとき: ウィンドウ作成時にどのインスタンスへ登録されるかを追うとき。
- 呼び出し先: `gDownloadsTaskbarInstances[filter].registerIndicator()`, `this._selectFilterForWindow()`

## _selectFilterForWindow()
- 位置: L307-329
- 役割: Windows では窓の私用・公開に応じてフィルターを返し、それ以外では全体 (ALL) を返す。
- 触るとき: macOS や Linux で私用ウィンドウのダウンロードも同じ進捗に含めるかを決めるとき。
- 条件付き依存: `if ( aForcedBackend == "windows" || (!aForcedBackend && gInterfaces.winTaskbar) )` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `gInterfaces.winTaskbar`, `lazy.Downloads.ALL`, `lazy.Downloads.PRIVATE`, `lazy.Downloads.PUBLIC`

## resetBetweenTests()
- 位置: L331-340
- 役割: 全インスタンスの状態を消し、OS インターフェースのキャッシュも null に戻す。
- 触るとき: タスクバー関連のテストが前のテストの状態を引きずるときに見る。
- 呼び出し先: `Object.keys()`, `gDownloadsTaskbarInstances[key].reset()`
- 参照: `gInterfaces.gtkTaskbarProgress`, `gInterfaces.macTaskbarProgress`, `gInterfaces.winTaskbar`
