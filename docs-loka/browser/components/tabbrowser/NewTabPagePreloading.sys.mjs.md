# browser/components/tabbrowser/NewTabPagePreloading.sys.mjs

source: browser/components/tabbrowser/NewTabPagePreloading.sys.mjs
source-hash: 09b8c8d57f917c079fae7209826f14c1218c5cb8
lines: 198

## <module>
- 役割: 新規タブ用ページ(about:newtab など)を事前に読み込んでおき、タブを開く際に使い回す NewTabPagePreloading を公開する。
- 呼び出し先: `XPCOMUtils.declareLazy()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## enabled()
- 位置: L33-39
- 役割: 先読み設定と新規タブ有効設定が真で、新規タブ URL が上書きされていない場合に true を返す。
- 触るとき: 先読みが動かない原因や有効条件を調べるとき。
- 参照: `lazy.AboutNewTab.newTabURLOverridden`, `this.newTabEnabled`, `this.prefEnabled`

## _createBrowser()
- 位置: L44-60
- 役割: 新規タブ URL に合うプロセス種別を予測して先読み用ブラウザを作り、gBrowser に登録してパネルを追加する。
- 触るとき: 先読みブラウザの生成方法やプロセス種別の決定を変えるとき。
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`, `gBrowser.createBrowser()`, `gBrowser.getPanel()`, `gBrowser.tabpanels.appendChild()`
- 参照: `gBrowser.preloadedBrowser`

## _adoptBrowserFromOtherWindow()
- 位置: L65-94
- 役割: プライベート状態と AI ウィンドウ状態が同じ別ウィンドウの先読みブラウザを、新しく作ったブラウザへ swapBrowsers で移して返す(無ければ null)。
- 触るとき: 先読み数の上限到達時に別ウィンドウから引き継ぐ処理を調べるとき。
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `lazy.BrowserWindowTracker.orderedWindows .filter()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `oldBrowser.swapBrowsers()`, `oldWin.gBrowser.getPanel()`, `oldWin.gBrowser.getPanel(oldBrowser).remove()`, `this._createBrowser()`
- 参照: `newBrowser.permanentKey`, `oldBrowser.permanentKey`, `oldWin.gBrowser.preloadedBrowser`, `w.gBrowser`, `w.gBrowser.preloadedBrowser`

## maybeCreatePreloadedBrowser()
- 位置: L96-147
- 役割: 条件を満たすウィンドウで先読みブラウザを作って新規タブ URL を読み込み、上限超過時は他ウィンドウから引き継ぐ。
- 触るとき: 先読みを作る条件(ウィンドウ順位、最大数、非表示時の抑止)や初期状態を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `browser.loadURI()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.BrowserWindowTracker.orderedWindows.filter()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this._createBrowser()`, `topWindows.indexOf()`, `window.FullZoom.onLocationChange()`, `window.gURLBar.getBrowserState()`
- 条件付き依存: `if (this.browserCounts[countKey] >= this.MAX_COUNT)` → `this._adoptBrowserFromOtherWindow()`
- 参照: `browser.docShellIsActive`, `this.MAX_COUNT`, `this.browserCounts`, `this.enabled`, `window.BROWSER_NEW_TAB_URL`, `window.document.hidden`, `window.gBrowser.preloadedBrowser`, `window.gURLBar.getBrowserState(browser).urlbarFocused`, `window.toolbar.visible`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## getPreloadedBrowser()
- 位置: L149-176
- 役割: ウィンドウの先読みブラウザを取り出して消費し、カウントを減らして属性を整え返す(無効時や無ければ null)。
- 触るとき: 新規タブを開く時に先読みブラウザが使われない、またはカウントが合わない問題を調べるとき。
- 条件付き依存: `if (browser)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (browser)` → `browser.removeAttribute()`
- 条件付き依存: `if (browser)` → `browser.setAttribute()`
- 参照: `this.browserCounts`, `this.enabled`, `window.gBrowser.preloadedBrowser`

## removePreloadedBrowser()
- 位置: L178-183
- 役割: 先読みブラウザを取り出して破棄し、そのパネルを DOM から外す。
- 触るとき: 先読みブラウザを明示的に捨てる契機や後始末を調べるとき。
- 呼び出し先: `this.getPreloadedBrowser()`
- 条件付き依存: `if (browser)` → `window.gBrowser.getPanel(browser).remove()`
- 条件付き依存: `if (browser)` → `window.gBrowser.getPanel()`
