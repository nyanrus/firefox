# browser/modules/WindowsPreviewPerTab.sys.mjs

source: browser/modules/WindowsPreviewPerTab.sys.mjs
source-hash: 3e9ffc410fef92bc682dc94b949f20ce7f009822
lines: 891

## <module>
- 役割: Windowsのタスクバーに出すタブ単位・ウィンドウ単位のプレビュー(AeroPeek)を管理し、サムネイル・ファビコン・タイトルを返すモジュール。
- 呼び出し先: `AeroPeek.initialize()`, `Cc["@mozilla.org/timer;1"].createInstance()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `XPCOMUtils.defineLazyServiceGetter()`

## _imageFromURI()
- 位置: L71-122
- 役割: URIから画像を非同期取得してデコードし、callbackに渡す。失敗時は既定ファビコンで取り直す。
- 触るとき: ファビコン取得の失敗時の挙動や、プライベートブラウズ時のチャンネル設定を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/thread-manager;1"].getService()`, `Components.isSuccessCode()`, `NetUtil.asyncFetch()`, `NetUtil.newChannel()`, `channel.QueryInterface()`, `channel.setPrivate()`, `defaultURI.equals()`, `lazy.imgTools.decodeImageAsync()`
- 条件付き依存: `if (!defaultURI.equals(uri))` → `_imageFromURI()`
- 参照: `Ci.nsIContentPolicy.TYPE_INTERNAL_IMAGE`, `Ci.nsIPrivateBrowsingChannel`, `PlacesUtils.favicons.defaultFavicon`, `channel.contentType`, `threadManager.currentThread`
- XPCOM: [`nsIContentPolicy`](../../dom/base/nsIContentPolicy.idl.md) / [`nsIPrivateBrowsingChannel`](../../netwerk/base/nsIPrivateBrowsingChannel.idl.md) / `@mozilla.org/thread-manager;1`

## onImageReady()
- 位置: L90-102
- 役割: デコード結果が空なら既定ファビコンで再度取得し、それ以外はそのままcallbackへ渡す。
- 触るとき: ファビコンのデコードに失敗したときに既定アイコンへ戻る条件を調べるとき。
- 呼び出し先: `callback()`
- 条件付き依存: `if (!image)` → `defaultURI.equals()`
- 条件付き依存: `if (!defaultURI.equals(uri))` → `_imageFromURI()`
- 参照: `PlacesUtils.favicons.defaultFavicon`

## getFaviconAsImage()
- 位置: L125-131
- 役割: アイコンURLがあればそのURIから、無ければ既定ファビコンから画像を取得する。
- 触るとき: タスクバーに表示するタブアイコンの取得元を変えるとき。
- 条件付き依存: `if (iconurl)` → `_imageFromURI()`
- 条件付き依存: `if (iconurl)` → `NetUtil.newURI()`
- 条件付き依存: `if (!(iconurl))` → `_imageFromURI()`
- 参照: `PlacesUtils.favicons.defaultFavicon`

## PreviewController()
- 位置: L150-163
- 役割: 1タブ分のタスクバープレビューを作り、TabAttrModifiedを購読して遅延生成のキャンバスを用意する。
- 触るとき: タブごとのプレビュー生成や、表示名更新のトリガーを追加・変更するとき。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `lazy.PageThumbs.createCanvas()`, `this.tab.addEventListener()`, `this.win.createTabPreview()`
- 参照: `canvas.mozOpaque`, `tab.linkedBrowser`, `this.linkedBrowser`, `this.preview`, `this.tab`, `this.win`, `this.win.win`

## destroy()
- 位置: L168-175
- 役割: タブの購読を外し、winとpreviewの参照を消して循環参照を断つ。
- 触るとき: タブを閉じたあとにウィンドウがメモリに残る問題を調べるとき。
- 呼び出し先: `this.tab.removeEventListener()`
- 参照: `this.preview`, `this.win`

## wrappedJSObject()
- 位置: L177-179
- 役割: nsITaskbarPreviewControllerの取り出しに使い、自身のJSオブジェクトを返す。
- 触るとき: TabWindow側からcontrollerの内部メソッドを直接呼ぶ箇所を追うとき。

## resetCanvasPreview()
- 位置: L182-185
- 役割: キャンバスの幅と高さを0にして、保持している描画メモリを解放する。
- 触るとき: サムネイルのキャッシュを手放すタイミング(キャッシュタイマーなど)を変えるとき。
- 参照: `this.canvasPreview.height`, `this.canvasPreview.width`

## resizeCanvasPreview()
- 位置: L190-193
- 役割: Windowsが要求したサイズに合わせてキャンバスの寸法を設定する。
- 触るとき: タブサムネイルの要求サイズへの対応を変えるとき。
- 参照: `this.canvasPreview.height`, `this.canvasPreview.width`

## browserDims()
- 位置: L195-197
- 役割: リンクされたブラウザ要素の矩形を返す。
- 触るとき: サムネイルに貼る内容領域の位置や大きさの計算を調べるとき。
- 呼び出し先: `this.tab.linkedBrowser.getBoundingClientRect()`

## cacheBrowserDims()
- 位置: L199-203
- 役割: 現在のブラウザの幅と高さを_cachedWidth/_cachedHeightに保存する。
- 触るとき: リサイズ後に無効化を入れるかの基準値を更新する箇所を追うとき。
- 参照: `dims.height`, `dims.width`, `this._cachedHeight`, `this._cachedWidth`, `this.browserDims`

## testCacheBrowserDims()
- 位置: L205-208
- 役割: 保存したブラウザの幅と高さが現在値と一致するかを返す。
- 触るとき: ブラウザ領域の寸法変化を検出する条件を変えるとき。
- 参照: `dims.height`, `dims.width`, `this._cachedHeight`, `this._cachedWidth`, `this.browserDims`

## updateCanvasPreview()
- 位置: L214-228
- 役割: キャッシュ寸法を更新し、PageThumbsでブラウザ内容をキャンバスに描画する。
- 触るとき: タブ内容のキャプチャ方法やフルスケール指定を変えるとき。
- 呼び出し先: `AeroPeek.resetCacheTimer()`, `lazy.PageThumbs.captureToCanvas()`, `lazy.PageThumbs.captureToCanvas( this.linkedBrowser, this.canvasPreview, { fullScale: aFullScale, } ).catch()`, `this.cacheBrowserDims()`
- 参照: `console.error`, `this.canvasPreview`, `this.linkedBrowser`

## updateTitleAndTooltip()
- 位置: L230-236
- 役割: ブラウザのウィンドウタイトルを取得し、プレビューのtitleとtooltipに設定する。
- 触るとき: タスクバーのプレビューに出る名前の決め方を変えるとき。
- 呼び出し先: `this.win.tabbrowser.getWindowTitleForBrowser()`
- 参照: `this.linkedBrowser`, `this.preview.title`, `this.preview.tooltip`

## width()
- 位置: L241-243
- 役割: プレビューの基準として親ウィンドウの幅を返す。
- 触るとき: プレビュー画像の全体サイズの元になる値を調べるとき。
- 参照: `this.win.width`

## height()
- 位置: L246-248
- 役割: プレビューの基準として親ウィンドウの高さを返す。
- 触るとき: プレビュー画像の全体サイズの元になる値を調べるとき。
- 参照: `this.win.height`

## thumbnailAspectRatio()
- 位置: L250-257
- 役割: タブ領域の幅と高さの比を返す。ゼロ除算と0値を1に置き換えて防ぐ。
- 触るとき: タブサムネイルの縦横比をWindowsに伝える値を変えるとき。
- 参照: `browserDims.height`, `browserDims.width`, `this.browserDims`

## requestPreview()
- 位置: L265-305
- 役割: キャンバスに高解像度のタブ内容を取り、ウィンドウ全体の画像に重ねてWindowsへ返す。
- 触るとき: ホバー時のウィンドウプレビューの見た目や描画順を変えるとき。
- 呼び出し先: `aTaskbarCallback.done()`, `composite.getContext()`, `ctx.drawImage()`, `ctx.drawWindow()`, `ctx.restore()`, `ctx.save()`, `ctx.scale()`, `lazy.PageThumbs.createCanvas()`, `this.resetCanvasPreview()`, `this.updateCanvasPreview()`, `this.updateCanvasPreview(true).then()`, `this.win.tabbrowser.previewTab()`
- 参照: `aPreviewCanvas.height`, `aPreviewCanvas.width`, `composite.height`, `composite.mozOpaque`, `composite.width`, `this.browserDims.x`, `this.browserDims.y`, `this.tab`, `this.win.height`, `this.win.width`, `this.win.win`, `this.win.win.devicePixelRatio`

## requestThumbnail()
- 位置: L318-323
- 役割: 要求サイズにキャンバスを合わせ、タブのサムネイルをWindowsへ返す。
- 触るとき: Windowsのサムネイル要求サイズと応答の流れを変えるとき。
- 呼び出し先: `aTaskbarCallback.done()`, `this.resizeCanvasPreview()`, `this.updateCanvasPreview()`, `this.updateCanvasPreview(false).then()`

## onClose()
- 位置: L327-329
- 役割: タスクバーの閉じるボタンからタブを閉じる。
- 触るとき: プレビューの閉じる操作でタブがどう閉じるかを変えるとき。
- 呼び出し先: `this.win.tabbrowser.removeTab()`
- 参照: `this.tab`

## onActivate()
- 位置: L331-337
- 役割: 対象タブを選択し、trueを返して最小化されたウィンドウを前面に戻す。
- 触るとき: プレビューをクリックしたときの前面化の挙動を調べるとき。
- 参照: `this.tab`, `this.win.tabbrowser.selectedTab`

## handleEvent()
- 位置: L340-346
- 役割: TabAttrModifiedを受けてタイトルとツールチップを更新する。
- 触るとき: タブ属性の変化でプレビューの表示名が古いままになる問題を調べるとき。
- 呼び出し先: `this.updateTitleAndTooltip()`
- 参照: `evt.type`

## TabWindow()
- 位置: L357-381
- 役割: 1ウィンドウ分のタブ監視を始める。タブとリサイズのイベントを購読し、既存タブのプレビューを作って並べる。
- 触るとき: ウィンドウ単位の初期化や購読するイベントを追加・変更するとき。
- 呼び出し先: `AeroPeek.checkPreviewCount()`, `AeroPeek.windows.push()`, `this.newTab()`, `this.tabbrowser.addTabsProgressListener()`, `this.tabbrowser.tabContainer.addEventListener()`, `this.updateTabOrdering()`, `this.win.addEventListener()`
- 参照: `tabs.length`, `this.previews`, `this.tabEvents`, `this.tabEvents.length`, `this.tabbrowser`, `this.tabbrowser.tabs`, `this.win`, `this.winEvents`, `this.winEvents.length`, `win.gBrowser`

## destroy()
- 位置: L390-412
- 役割: イベントとタブ進行リスナーを外し、全タブのプレビューを削除してAeroPeekの一覧から外す。
- 触るとき: ウィンドウを閉じたあとにプレビューが残る問題を調べるとき。
- 呼び出し先: `AeroPeek.checkPreviewCount()`, `AeroPeek.windows.indexOf()`, `AeroPeek.windows.splice()`, `this.removeTab()`, `this.tabbrowser.removeTabsProgressListener()`, `this.tabbrowser.tabContainer.removeEventListener()`, `this.win.removeEventListener()`
- 参照: `tabs.length`, `this._destroying`, `this.tabEvents`, `this.tabEvents.length`, `this.tabbrowser.tabs`, `this.win.gTaskbarTabGroup`, `this.winEvents`, `this.winEvents.length`

## width()
- 位置: L414-416
- 役割: ウィンドウの内側の幅(innerWidth)を返す。
- 触るとき: リサイズ判定に使うウィンドウ寸法の基準を調べるとき。
- 参照: `this.win.innerWidth`

## height()
- 位置: L417-419
- 役割: ウィンドウの内側の高さ(innerHeight)を返す。
- 触るとき: リサイズ判定に使うウィンドウ寸法の基準を調べるとき。
- 参照: `this.win.innerHeight`

## cacheDims()
- 位置: L421-424
- 役割: 現在のウィンドウ寸法を_cachedWidth/_cachedHeightに保存する。
- 触るとき: リサイズ時の重複した無効化を抑える基準値を更新するとき。
- 参照: `this._cachedHeight`, `this._cachedWidth`, `this.height`, `this.width`

## testCacheDims()
- 位置: L426-428
- 役割: 保存したウィンドウ寸法と現在値が一致するかを返す。
- 触るとき: ウィンドウのリサイズ時に無効化を省くかの判定条件を変えるとき。
- 参照: `this._cachedHeight`, `this._cachedWidth`, `this.height`, `this.width`

## newTab()
- 位置: L431-439
- 役割: タブ用のPreviewControllerを作り、プレビューを登録してタイトルを設定する。
- 触るとき: タブ追加時にプレビューが作られない、またはタイトルが空になる問題を調べるとき。
- 呼び出し先: `AeroPeek.addPreview()`, `controller.updateTitleAndTooltip()`, `this.previews.set()`
- 参照: `controller.preview`

## createTabPreview()
- 位置: L441-452
- 役割: タスクバーのタブプレビューを作り、表示・選択状態とファビコンを設定する。
- 触るとき: タブプレビューの初期表示やアクティブ判定を変えるとき。
- 呼び出し先: `AeroPeek.taskbar.createTaskbarTabPreview()`, `tab.getAttribute()`, `this.updateFavicon()`
- 参照: `AeroPeek.enabled`, `preview.active`, `preview.visible`, `this.tabbrowser.selectedTab`, `this.win.docShell`

## removeTab()
- 位置: L455-464
- 役割: タブのプレビューを非表示・非アクティブにして破棄し、一覧から外す。
- 触るとき: タブを閉じたときのプレビューの後始末を変えるとき。
- 呼び出し先: `AeroPeek.removePreview()`, `preview.controller.wrappedJSObject.destroy()`, `preview.move()`, `this.previewFromTab()`, `this.previews.delete()`
- 参照: `preview.active`, `preview.visible`

## enabled()
- 位置: L466-468
- 役割: ウィンドウ単位のプレビューの有効フラグを返す。
- 触るとき: プレビューが有効かどうかの状態を追うとき。
- 参照: `this._enabled`

## enabled()
- 位置: L470-480
- 役割: 有効フラグを設定し、全プレビューの配置を解除して表示状態を切り替えたあと、並び順を更新する。
- 触るとき: AeroPeekの有効・無効切り替えをウィンドウごとに反映させる処理を変えるとき。
- 呼び出し先: `preview.move()`, `this.updateTabOrdering()`
- 参照: `preview.visible`, `this._enabled`, `this.previews`

## previewFromTab()
- 位置: L482-484
- 役割: タブに対応するプレビューをMapから取得する。
- 触るとき: タブからプレビューを引く箇所の挙動を追うとき。
- 呼び出し先: `this.previews.get()`

## updateTabOrdering()
- 位置: L486-506
- 役割: タブの並び順どおりに各プレビューをmoveで並べ替える。後ろから順に指定する。
- 触るとき: タスクバー上のタブ順がずれる問題を調べるとき。
- 呼び出し先: `inorder[i].move()`, `previews.has()`
- 条件付き依存: `if (previews.has(t))` → `inorder.push()`
- 条件付き依存: `if (previews.has(t))` → `previews.get()`
- 参照: `inorder.length`, `this.previews`, `this.tabbrowser.tabs`

## handleEvent()
- 位置: L509-533
- 役割: TabOpen・TabClose・TabSelect・TabMove・resizeを振り分け、追加・削除・選択・並べ替え・リサイズ処理を呼ぶ。
- 触るとき: タブ操作やウィンドウのリサイズでプレビューが更新されない問題を調べるとき。
- 呼び出し先: `this.newTab()`, `this.onResize()`, `this.previewFromTab()`, `this.removeTab()`, `this.updateTabOrdering()`
- 参照: `AeroPeek._prefenabled`, `evt.originalTarget`, `evt.type`, `this.previewFromTab(tab).active`

## setInvalidationTimer()
- 位置: L536-560
- 役割: 1秒の一回限りタイマーを張り直し、満了時に寸法が変わったプレビューを無効化する。
- 触るとき: リサイズ中の再描画の遅延時間や対象を変えるとき。
- 呼び出し先: `controller.testCacheBrowserDims()`, `this.invalidateTimer.cancel()`, `this.invalidateTimer.initWithCallback()`, `this.previews.forEach()`
- 条件付き依存: `if (!this.invalidateTimer)` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 条件付き依存: `if (!controller.testCacheBrowserDims())` → `controller.cacheBrowserDims()`
- 条件付き依存: `if (!controller.testCacheBrowserDims())` → `aPreview.invalidate()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `aPreview.controller.wrappedJSObject`, `this.invalidateTimer`
- XPCOM: [`nsITimer`](../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## onResize()
- 位置: L562-578
- 役割: 寸法が変わっていれば寸法を保存し、無効化タイマーを張る。
- 触るとき: ウィンドウ境界のドラッグ中にサムネイル更新が重なる問題を調べるとき。
- 呼び出し先: `this.cacheDims()`, `this.setInvalidationTimer()`, `this.testCacheDims()`

## invalidateTabPreview()
- 位置: L580-587
- 役割: 指定したブラウザに対応するタブのプレビューを無効化する。
- 触るとき: 読み込みが終わってもサムネイルが古いままになる問題を調べるとき。
- 条件付き依存: `if (aBrowser == tab.linkedBrowser)` → `preview.invalidate()`
- 参照: `tab.linkedBrowser`, `this.previews`

## onLocationChange()
- 位置: L591-595
- 役割: 何もしない空の処理。ページ遷移ではプレビューを無効化しない。
- 触るとき: ページ遷移でサムネイルを更新する要件が出て、onStateChangeとの役割分担を確認するとき。

## onStateChange()
- 位置: L597-604
- 役割: ネットワーク読み込みの完了(STATE_STOPかつSTATE_IS_NETWORK)でタブのプレビューを無効化する。
- 触るとき: 読み込み完了時にサムネイルを更新するタイミングを変えるとき。
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_STOP && aStateFlags & Ci.nsIWebProgressListener.STATE_IS_NETWORK )` → `this.invalidateTabPreview()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_NETWORK`, `Ci.nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLinkIconAvailable()
- 位置: L606-609
- 役割: ファビコンの通知を受けてブラウザからタブを特定し、updateFaviconを呼ぶ。
- 触るとき: ファビコン更新の経路を調べるとき。
- 呼び出し先: `this.updateFavicon()`, `this.win.gBrowser.getTabForBrowser()`

## updateFavicon()
- 位置: L610-647
- 役割: アイコンURLからfavicon linkを解決して画像を取得し、プレビューのiconに設定する。既定ファビコンのときはアイコン未設定の場合だけ反映する。
- 触るとき: タスクバーのタブアイコンが古い・違う問題を調べるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `aTab.getAttribute()`, `getFaviconAsImage()`, `this.previews.get()`
- 条件付き依存: `if (aIconURL)` → `PlacesUtils.favicons.getFaviconLinkForIcon()`
- 条件付き依存: `if (aIconURL)` → `Services.io.newURI()`
- 参照: `PlacesUtils.favicons.getFaviconLinkForIcon( Services.io.newURI(aIconURL) ).spec`, `aTab.closing`, `aTab.linkedBrowser`, `preview.icon`, `this.win`, `this.win.closed`
- XPCOM: `Services.io`

## initialize()
- 位置: L680-694
- 役割: WINTASKBARサービスの利用可否を確認し、トグルpref(browser.taskbar.previews.enable)を監視して初期の有効状態を決める。
- 触るとき: Windowsのタスクバー機能が使えない環境での起動挙動や、pref初期化を変えるとき。
- 呼び出し先: `Cc[WINTASKBAR_CONTRACTID].getService()`, `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`
- 参照: `Ci.nsIWinTaskbar`, `this._prefenabled`, `this.available`, `this.enabled`, `this.initialized`, `this.taskbar`, `this.taskbar.available`
- XPCOM: `nsIWinTaskbar` / `Services.prefs`

## destroy()
- 位置: L696-702
- 役割: 全体の有効フラグを下げ、キャッシュ用タイマーを止める。
- 触るとき: 機能を終了させるときの後始末を調べるとき。
- 条件付き依存: `if (this.cacheTimer)` → `this.cacheTimer.cancel()`
- 参照: `this._enabled`, `this.cacheTimer`

## enabled()
- 位置: L704-706
- 役割: 全体の有効フラグを返す。
- 触るとき: プレビュー機能が今有効かどうかを判定する箇所を追うとき。
- 参照: `this._enabled`

## enabled()
- 位置: L708-718
- 役割: 値が変わったときだけ、登録済みの全ウィンドウに有効状態を伝える。
- 触るとき: プレビュー件数の上限超過などで機能全体を切り替える処理を追うとき。
- 呼び出し先: `this.windows.forEach()`
- 参照: `this._enabled`, `win.enabled`

## _prefenabled()
- 位置: L720-722
- 役割: トグルprefの現在値を返す。
- 触るとき: プレビュー機能のon/offの判定元を調べるとき。
- 参照: `this.__prefenabled`

## _prefenabled()
- 位置: L724-735
- 役割: 値が変わったときに有効化(enable)か無効化(disable)を実行する。
- 触るとき: browser.taskbar.previews.enableの切り替えが反映されない問題を調べるとき。
- 条件付き依存: `if (enable)` → `this.enable()`
- 条件付き依存: `if (!(enable))` → `this.disable()`
- 参照: `this.__prefenabled`

## enable()
- 位置: L739-767
- 役割: 上限(max)とキャッシュ時間(cachetime)のprefを読み、places監視を登録する。初期化済みならオープン中の全ウィンドウを処理する。
- 触るとき: 上限やキャッシュ時間の読み込み、またはプレビューを途中で有効化したときの既存ウィンドウ処理を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (!this._observersAdded)` → `Services.prefs.addObserver()`
- 条件付き依存: `if (!this._observersAdded)` → `this.handlePlacesEvents.bind()`
- 条件付き依存: `if (!this._observersAdded)` → `PlacesUtils.observers.addListener()`
- 条件付き依存: `if (this.initialized)` → `Services.wm.getEnumerator()`
- 条件付き依存: `if (!win.closed)` → `this.onOpenWindow()`
- 参照: `this._observersAdded`, `this._placesListener`, `this.cacheLifespan`, `this.initialized`, `this.maxpreviews`, `win.closed`
- XPCOM: `Services.prefs` / `Services.wm`

## disable()
- 位置: L769-781
- 役割: 全ウィンドウのTabWindowを破棄し、places監視を外す。
- 触るとき: プレビュー機能を無効にしたときの後始末を変えるとき。
- 呼び出し先: `PlacesUtils.observers.removeListener()`, `tabWinObject.destroy()`
- 参照: `tabWinObject.win.gTaskbarTabGroup`, `this._placesListener`, `this.windows`, `this.windows.length`

## addPreview()
- 位置: L783-786
- 役割: プレビューを一覧に追加し、件数を確認する。
- 触るとき: 上限判定に使うプレビュー件数の増え方を追うとき。
- 呼び出し先: `this.checkPreviewCount()`, `this.previews.push()`

## removePreview()
- 位置: L788-792
- 役割: プレビューを一覧から取り除き、件数を確認する。
- 触るとき: タブを閉じた後の件数と上限判定のずれを調べるとき。一覧に無いプレビューが渡るとindexOfが-1になり、spliceが末尾の要素を消す点に注意。
- 呼び出し先: `this.checkPreviewCount()`, `this.previews.indexOf()`, `this.previews.splice()`

## checkPreviewCount()
- 位置: L794-799
- 役割: プレビュー件数が上限(maxpreviews)以下なら有効、超えたら無効にする。
- 触るとき: タブ数が多いときにプレビューが自動で無効化される閾値を変えるとき。
- 参照: `this._prefenabled`, `this.enabled`, `this.maxpreviews`, `this.previews.length`

## onOpenWindow()
- 位置: L801-808
- 役割: 機能が使えて有効なら、新しいウィンドウ用のTabWindowを作ってgTaskbarTabGroupに登録する。
- 触るとき: 新しいウィンドウを開いたときにプレビューが付かない問題を調べるとき。
- 参照: `this._prefenabled`, `this.available`, `win.gTaskbarTabGroup`

## onCloseWindow()
- 位置: L810-822
- 役割: ウィンドウのTabWindowを破棄して外し、ウィンドウが残らなければ機能を終了する。
- 触るとき: ウィンドウを閉じた後の後始末や終了条件を変えるとき。
- 呼び出し先: `win.gTaskbarTabGroup.destroy()`
- 条件付き依存: `if (!this.windows.length)` → `this.destroy()`
- 参照: `this._prefenabled`, `this.available`, `this.windows.length`, `win.gTaskbarTabGroup`

## resetCacheTimer()
- 位置: L824-831
- 役割: キャッシュ用の一回限りタイマーを、cacheLifespan秒後に満了するよう張り直す。
- 触るとき: サムネイルをキャッシュし続ける時間の扱いを変えるとき。
- 呼び出し先: `this.cacheTimer.cancel()`, `this.cacheTimer.init()`
- 参照: `Ci.nsITimer.TYPE_ONE_SHOT`, `this.cacheLifespan`
- XPCOM: [`nsITimer`](../../xpcom/threads/nsITimer.idl.md)

## observe()
- 位置: L834-862
- 役割: トグルpref変更で有効状態を切り替え、上限pref変更で上限を更新して件数を確認する。タイマー満了時は全プレビューのキャンバスを解放する。
- 触るとき: 設定変更の反映やキャンバスの解放タイミングを変えるとき。
- 呼び出し先: `controller.resetCanvasPreview()`, `this.checkPreviewCount()`, `this.previews.forEach()`
- 条件付き依存: `if (aTopic == "nsPref:changed" && aData == TOGGLE_PREF_NAME)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (aData == DISABLE_THRESHOLD_PREF_NAME)` → `Services.prefs.getIntPref()`
- 参照: `preview.controller.wrappedJSObject`, `this._prefenabled`, `this.maxpreviews`
- XPCOM: `Services.prefs`

## handlePlacesEvents()
- 位置: L864-878
- 役割: favicon-changedを受け、対象URLのタブのファビコンを更新する。
- 触るとき: 履歴側でファビコンが変わったときにタスクバーの表示が追従しない問題を調べるとき。
- 呼び出し先: `tab.getAttribute()`
- 条件付き依存: `if (tab.getAttribute("image") == event.faviconUrl)` → `win.updateFavicon()`
- 参照: `event.faviconUrl`, `event.type`, `this.windows`, `win.previews`
