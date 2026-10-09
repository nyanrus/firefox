# browser/components/downloads/DownloadSpamProtection.sys.mjs

source: browser/components/downloads/DownloadSpamProtection.sys.mjs
source-hash: d12cd2f1321d8d7208316e2dcb59fa03d23d2dd3
lines: 313

## <module>
- 役割: 自動ダウンロードの連続発生（スパム）を検出して、ウィンドウごとにブロック分を一覧化し UI に通知する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## WindowSpamProtection.constructor()
- 位置: L30-32
- 役割: 担当ウィンドウを保持する。ウィンドウごとに1つ作られる。
- 触るとき: ウィンドウ単位の状態管理の前提を確かめるとき。
- 参照: `this._window`

## WindowSpamProtection.spamList()
- 位置: L70-78
- 役割: ブロックが一度でも起きたときだけ DownloadList を遅延生成して返す。未ブロックなら undefined。
- 触るとき: スパム一覧の生成タイミングを変えるとき、または一覧が空で返る原因を調べるとき。
- 参照: `lazy.DownloadList`, `this._blocking`, `this._spamList`

## WindowSpamProtection.indicator()
- 位置: L87-92
- 役割: ウィンドウのダウンロード表示状態（ツールバーボタン等）のデータを初回アクセス時に取得してキャッシュする。
- 触るとき: ダウンロードボタンの状態表示がブロック時に更新されない問題を調べるとき。
- 条件付き依存: `if (!this._indicator)` → `lazy.DownloadsCommon.getIndicatorData()`
- 参照: `this._indicator`, `this._window`

## WindowSpamProtection.addDownloadSpam()
- 位置: L100-118
- 役割: 同じ URL なら件数を1増やして表示を更新し、新規なら DownloadSpam を作って一覧に追加し、パネルを開く通知を出す。
- 触るとき: 同一 URL の連続ブロック時の件数表示や、新規ブロック時の通知動作を変えるとき。
- 呼び出し先: `this._downloadSpamForUrl.has()`, `this._downloadSpamForUrl.set()`, `this._maybeAddViews()`, `this._notifyDownloadSpamAdded()`, `this.spamList.add()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this._downloadSpamForUrl.get()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this.indicator.onDownloadStateChanged()`
- 参照: `downloadSpam.blockedDownloadsCount`, `this._blocking`

## WindowSpamProtection._notifyDownloadSpamAdded()
- 位置: L126-141
- 役割: 進行中のダウンロードがなく最前面のウィンドウなら、ダウンロードパネルを開く。それ以外はウィンドウの注意喚起（getAttention）を出す。
- 触るとき: スパム検出時にパネルを勝手に開く条件を変えるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.DownloadsCommon.summarizeDownloads()`, `this.indicator._activeDownloads()`, `this.indicator.onDownloadAdded()`
- 条件付き依存: `if ( !hasActiveDownloads && this._window === lazy.BrowserWindowTracker.getTopWindow() )` → `this._window.DownloadsPanel.showPanel()`
- 条件付き依存: `if (!( !hasActiveDownloads && this._window === lazy.BrowserWindowTracker.getTopWindow() ))` → `this._window.getAttention()`
- 参照: `lazy.DownloadsCommon.summarizeDownloads( this.indicator._activeDownloads() ).numDownloading`, `this._window`

## WindowSpamProtection.removeDownloadSpamForUrl()
- 位置: L148-155
- 役割: URL に対応するブロック記録を一覧と表示から取り除く。
- 触るとき: ブロック済みダウンロードを消去する操作の後始末を調べるとき。
- 呼び出し先: `this._downloadSpamForUrl.has()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this._downloadSpamForUrl.get()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this.spamList.remove()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this.indicator.onDownloadRemoved()`
- 条件付き依存: `if (this._downloadSpamForUrl.has(url))` → `this._downloadSpamForUrl.delete()`

## WindowSpamProtection.registerView()
- 位置: L164-170
- 役割: 表示先（ダウンロードパネル等）を保留リストに入れ、既に一覧があれば直ちに通知対象に加える。
- 触るとき: パネルがスパム通知を受け取れない問題を調べるとき。
- 呼び出し先: `this._maybeAddViews()`, `this._pendingViews.add()`, `this.spamList?._views.has()`

## WindowSpamProtection._maybeAddViews()
- 位置: L176-185
- 役割: 一覧が存在するとき、保留中の表示先をすべて一覧に登録して保留を空にする。
- 触るとき: 表示先の登録タイミングを変えるとき。
- 条件付き依存: `if (this.spamList)` → `this.spamList._views.has()`
- 条件付き依存: `if (!this.spamList._views.has(view))` → `this.spamList.addView()`
- 条件付き依存: `if (this.spamList)` → `this._pendingViews.clear()`
- 参照: `this._pendingViews`, `this.spamList`

## WindowSpamProtection.removeAllViews()
- 位置: L191-198
- 役割: ウィンドウを閉じるとき、一覧に登録済みの表示先をすべて外し、保留も消す。
- 触るとき: ウィンドウ終了時のリスナー解除漏れを調べるとき。
- 呼び出し先: `this._pendingViews.clear()`
- 条件付き依存: `if (this.spamList)` → `this.spamList.removeView()`
- 参照: `this.spamList`, `this.spamList._views`

## DownloadSpamProtection.update()
- 位置: L222-237
- 役割: ブロックされた URL を、ウィンドウの WindowSpamProtection（なければ作成）に渡す。ウィンドウ null なら記録せずログだけ出す。
- 触るとき: nsExternalAppHandler 側からのスパム通知を受けた後の振り分けを変えるとき。
- 呼び出し先: `this._forWindowMap.get()`, `this._forWindowMap.set()`, `wsp.addDownloadSpam()`
- 条件付き依存: `if (window == null)` → `lazy.DownloadsCommon.log()`

## DownloadSpamProtection.getSpamListForWindow()
- 位置: L245-247
- 役割: 指定ウィンドウのスパム一覧を返す。ウィンドウ未登録なら undefined。
- 触るとき: ダウンロードパネルがスパム一覧を取得する経路を調べるとき。
- 呼び出し先: `this._forWindowMap.get()`
- 参照: `this._forWindowMap.get(window)?.spamList`

## DownloadSpamProtection.removeDownloadSpamForWindow()
- 位置: L256-259
- 役割: 指定ウィンドウで、URL に対応するブロック記録を取り除く。
- 触るとき: ウィンドウ単位での記録削除の呼び出し元を調べるとき。
- 呼び出し先: `this._forWindowMap.get()`, `wsp?.removeDownloadSpamForUrl()`

## DownloadSpamProtection.register()
- 位置: L271-277
- 役割: ウィンドウの管理オブジェクトを作成（または取得）し、表示先を登録する。
- 触るとき: ダウンロードパネルを開いたときにスパム通知の購読を設定する箇所を変えるとき。
- 呼び出し先: `this._forWindowMap.get()`, `this._forWindowMap.set()`, `wsp.registerView()`

## DownloadSpamProtection.unregister()
- 位置: L284-291
- 役割: ウィンドウが閉じられたとき、表示先の登録を解除して管理オブジェクトを捨てる。
- 触るとき: ウィンドウ終了時の後始末を変えるとき。
- 呼び出し先: `this._forWindowMap.get()`
- 条件付き依存: `if (wsp)` → `wsp.removeAllViews()`
- 条件付き依存: `if (wsp)` → `this._forWindowMap.delete()`

## DownloadSpam.constructor()
- 位置: L300-311
- 役割: ブロックされたダウンロードを表す Download 派生オブジェクトを作る。レピュテーション検査による遮断エラーを持ち、件数は1から始まる。
- 触るとき: ブロック項目の表示内容（エラー種別や URL）を変えるとき。
- 呼び出し先: `super()`
- 参照: `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`, `this.blockedDownloadsCount`, `this.error`, `this.hasBlockedData`, `this.source`, `this.stopped`, `this.target`
