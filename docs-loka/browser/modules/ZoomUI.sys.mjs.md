# browser/modules/ZoomUI.sys.mjs

source: browser/modules/ZoomUI.sys.mjs
source-hash: 667ee95940f1fc17521aecddbefb2bab299f73cc
lines: 206

## <module>
- 役割: ツールバーとアプリケーションメニューのズームボタン・リセットボタンのラベルと表示を、現在のズーム値に合わせて更新するモジュール。
- 呼び出し先: `Cc["@mozilla.org/content-pref/service;1"].getService()`, `Cu.createLoadContext()`, `CustomizableUI.addListener()`, `Services.obs.addObserver()`

## init()
- 位置: L12-29
- 役割: ウィンドウにDocShell入れ替えとズーム変更のイベントを登録し、unloadで外す。
- 触るとき: ズーム関連のイベントを新しく購読させたり、ウィンドウ単位の後始末を変えたりするとき。
- 呼び出し先: `aWindow.addEventListener()`, `aWindow.removeEventListener()`

## getGlobalValue()
- 位置: L37-68
- 役割: browser.content.full-zoomの全体既定値を、キャッシュを先に見てからPromiseで返す。取得できなければ1.0。
- 触るとき: 既定のズーム倍率の取得元やフォールバック値を変えるとき。
- 呼び出し先: `gContentPrefs.getCachedGlobal()`, `gContentPrefs.getGlobal()`
- 条件付き依存: `if (cachedVal)` → `resolve()`
- 条件付き依存: `if (cachedVal)` → `parseFloat()`
- 参照: `cachedVal.value`

## handleResult()
- 位置: L55-59
- 役割: 全体既定値のprefを受け取り、値があればparseFloatで数値にする。
- 触るとき: コンテンツprefの取得結果をズーム値として読む箇所を調べるとき。
- 条件付き依存: `if (pref.value)` → `parseFloat()`
- 参照: `pref.value`

## handleCompletion()
- 位置: L60-62
- 役割: 取得完了時に、受け取った既定値でPromiseを解決する。
- 触るとき: 既定値の取得が完了したあとの後続処理のタイミングを調べるとき。
- 呼び出し先: `resolve()`

## handleError()
- 位置: L63-65
- 役割: 取得エラーをconsole.errorに記録する。
- 触るとき: ズーム既定値の取得失敗時の扱いを変えるとき。
- 呼び出し先: `console.error()`

## fullZoomLocationChangeObserver()
- 位置: L71-79
- 役割: browser-fullZoom:location-changeを受け、ウィンドウが無効なら無視し、有効ならupdateZoomUIを呼ぶ。
- 触るとき: ページ遷移時にズームボタンが更新されない問題や、タブをウィンドウ間で移動したときの挙動を調べるとき。
- 呼び出し先: `updateZoomUI()`
- 参照: `aSubject.documentGlobal`

## onEndSwapDocShells()
- 位置: L85-87
- 役割: DocShellの入れ替え後に、入れ替え元ブラウザでupdateZoomUIを呼ぶ。
- 触るとき: タブのドラッグ移動や遅延読み込みでズーム表示がずれる問題を調べるとき。
- 呼び出し先: `updateZoomUI()`
- 参照: `event.originalTarget`

## onZoomChange()
- 位置: L89-106
- 役割: FullZoomChange・TextZoomChangeを受け、ドキュメントからブラウザ要素を求めてupdateZoomUIを呼ぶ(アニメーションあり)。
- 触るとき: ズーム変更時の表示更新の対象や、アニメーションの有無を変えるとき。
- 呼び出し先: `updateZoomUI()`
- 参照: `event.originalTarget`, `event.target.DOCUMENT_NODE`, `event.target.defaultView.top.document`, `event.target.nodeType`, `topDoc.documentElement`, `topDoc.documentGlobal.docShell.chromeEventHandler`

## updateZoomUI()
- 位置: async L115-184
- 役割: 選択中ブラウザのズーム率を取り、既定値と異なるとき等に応じてズームボタンの表示・ラベル・アニメーションを更新する。
- 触るとき: ズームボタンの表示条件(既定値、about:blank、PDFビューア、ツールバー配置)やラベルを変えるとき。
- 呼び出し先: `Math.round()`, `ZoomUI.getGlobalValue()`, `customizableZoomControls.getAttribute()`, `win.FullZoom.updateCommands()`, `win.document.getElementById()`, `win.gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (appMenuZoomReset)` → `appMenuZoomReset.setAttribute()`
- 条件付き依存: `if (customizableZoomReset)` → `customizableZoomReset.setAttribute()`
- 条件付き依存: `if (aAnimate && !win.gReduceMotion)` → `urlbarZoomButton.setAttribute()`
- 条件付き依存: `if (!(aAnimate && !win.gReduceMotion))` → `urlbarZoomButton.removeAttribute()`
- 条件付き依存: `if (!urlbarZoomButton.hidden)` → `urlbarZoomButton.setAttribute()`
- 参照: `aBrowser.browsingContext?.topChromeWindow`, `aBrowser.contentPrincipal`, `aBrowser.contentPrincipal.isNullPrincipal`, `aBrowser.contentPrincipal.spec`, `aBrowser.currentURI.spec`, `aBrowser.documentGlobal`, `urlbarZoomButton.hidden`, `win.ZoomManager.zoom`, `win.gBrowser`, `win.gBrowser.selectedBrowser`, `win.gReduceMotion`

## customizationListener.onWidgetMoved()
- 位置: L192-198
- 役割: zoom-controlsが追加・削除・移動されたときに、全ウィンドウのズーム表示を更新する。
- 触るとき: ツールバーのカスタマイズでズームボタンを動かしたあとに表示が合わなくなる問題を調べるとき。
- 条件付き依存: `if (aWidgetId == "zoom-controls")` → `updateZoomUI()`
- 参照: `CustomizableUI.windows`, `window.gBrowser.selectedBrowser`

## customizationListener.onWidgetUndoMove()
- 位置: L200-204
- 役割: zoom-controlsのリセット・移動の取り消しで、そのウィンドウのズーム表示を更新する。
- 触るとき: カスタマイズの初期化や移動の取り消し後のズーム表示を調べるとき。
- 条件付き依存: `if (aWidgetNode.id == "zoom-controls")` → `updateZoomUI()`
- 参照: `aWidgetNode.documentGlobal.gBrowser.selectedBrowser`, `aWidgetNode.id`
