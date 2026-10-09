# browser/modules/BrowserDOMWindow.sys.mjs

source: browser/modules/BrowserDOMWindow.sys.mjs
source-hash: 2cbf419680e8b2943786aeeda290c70af16e6c4a
lines: 557

## <module>
- 役割: 各ウィンドウの nsIBrowserDOMWindow 実装。外部リンクや window.open などの開き先(窓・タブ・現在のタブ・フレーム)を振り分ける。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Components.Constructor()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## BrowserDOMWindow.constructor()
- 位置: L53-55
- 役割: 対象のウィンドウを保持する。ウィンドウごとに 1 つ作られる。
- 触るとき: ウィンドウ単位の状態をこのクラスに持たせるとき。
- 参照: `this.win`

## BrowserDOMWindow.setupInWindow()
- 位置: L60-62
- 役割: ウィンドウの browserDOMWindow にこのインスタンスを取り付ける。
- 触るとき: ウィンドウ生成時の取り付け方を変えるとき。Fenix など別実装との入れ替えを考えるとき。
- 参照: `win.browserDOMWindow`

## BrowserDOMWindow.teardownInWindow()
- 位置: L67-69
- 役割: ウィンドウの browserDOMWindow を null にして参照を外す。
- 触るとき: ウィンドウを閉じた後も参照が残る問題を確かめるとき。
- 参照: `win.browserDOMWindow`

## BrowserDOMWindow.#openURIInNewTab()
- 位置: L88-178
- 役割: 最適な窓(ポップアップ・タスクバータブ・ミニ窓では最近の通常窓)に新しいタブを開く。外部起動で URL が無いか about:blank なら空のタブを開く。
- 触るとき: 新しいタブの開き先の窓の選び方、背景での読み込み、タブの位置(現在のタブの隣)を変えるとき。窓が無ければ null を返す。
- 呼び出し先: `lazy.TaskbarTabsUtils.isTaskbarTabWindow()`, `this.win.document.documentElement.hasAttribute()`, `win.gBrowser.getBrowserForTab()`
- 条件付き依存: `if (!( this.win.toolbar.visible && !lazy.TaskbarTabsUtils.isTaskbarTabWindow(this.win) && !this.win.document.documentElement.hasAttribute("mini-window") ))` → `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (aIsExternal && (!aURI || aURI.spec == "about:blank"))` → `win.BrowserCommands.openTab()`
- 条件付き依存: `if (aIsExternal && (!aURI || aURI.spec == "about:blank"))` → `win.focus()`
- 条件付き依存: `if (aWhere == Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT)` → `win.gBrowser.addAdjacentTab()`
- 条件付き依存: `if (!(aWhere == Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT))` → `win.gBrowser.addTab()`
- 条件付き依存: `if (needToFocusWin || (!loadInBackground && aIsExternal))` → `win.focus()`
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_BACKGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_FOREGROUND`, `Ci.nsIScriptSecurityManager.DEFAULT_USER_CONTEXT_ID`, `aURI.spec`, `lazy.loadDivertedInBackground`, `this.win`, `this.win.toolbar.visible`, `win.gBrowser.selectedBrowser`, `win.gBrowser.selectedTab`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / `nsIScriptSecurityManager`

## BrowserDOMWindow.createContentWindow()
- 位置: L183-200
- 役割: 読み込みなしで内容用の窓を作る。#getContentWindowOrOpenURI を null の URL で呼ぶ。
- 触るとき: window.open などで内容窓を先に作る経路を変えるとき。
- 呼び出し先: `this.#getContentWindowOrOpenURI()`

## BrowserDOMWindow.openURI()
- 位置: L205-226
- 役割: URL を指定の場所(新しい窓、新しいタブ、現在のタブ)で開く。URL が無ければ例外を投げる。
- 触るとき: リンクの開き方や外部起動の扱いを変えるとき。
- 呼び出し先: `this.#getContentWindowOrOpenURI()`
- 条件付き依存: `if (!aURI)` → `console.error()`
- 条件付き依存: `if (!aURI)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_FAILURE`

## BrowserDOMWindow.#getContentWindowOrOpenURI()
- 位置: L238-445
- 役割: 開く場所とフラグで分岐し、新しい窓・新しいタブ・印刷用・現在のタブへの読み込みを実行して、ブラウジングコンテキストを返す。
- 触るとき: リンクの開き方の決定(外部起動の既定動作を Nimbus の openBehavior で上書きする部分を含む)や、参照元ポリシー、ユーザーコンテキストを変えるとき。最も分岐が多い箇所。
- 呼び出し先: `Cc[ "@mozilla.org/hash-property-bag;1" ].createInstance()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `aURI.schemeIs()`, `console.error()`, `extraOptions.setPropertyAsBool()`, `lazy.URILoadingHelper.guessUserContextId()`, `this.#openURIInNewTab()`, `this.win.PrintUtils.handleStaticCloneCreatedForPrint()`, `this.win.openDialog()`
- 条件付き依存: `if (aOpenWindowInfo && isExternal)` → `console.error()`
- 条件付き依存: `if (aOpenWindowInfo && isExternal)` → `Components.Exception()`
- 条件付き依存: `if (isExternal && aURI && aURI.schemeIs("chrome"))` → `dump()`
- 条件付き依存: `if (isExternal)` → `lazy.NimbusFeatures.externalLinkHandling.recordExposureEvent()`
- 条件付き依存: `if (aWhere == Ci.nsIBrowserDOMWindow.OPEN_DEFAULTWINDOW)` → `lazy.NimbusFeatures.externalLinkHandling.getVariable()`
- 条件付き依存: `if (!(isExternal && externalLinkOpeningBehavior != -1))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if ( aOpenWindowInfo && aOpenWindowInfo.parent && aOpenWindowInfo.parent.window )` → `Services.io.newURI()`
- 条件付き依存: `if (forceAllowDataURI)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (aURI)` → `this.win.gBrowser.fixupAndLoadURIString()`
- 条件付き依存: `if (!lazy.loadDivertedInBackground)` → `this.win.focus()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIBrowserDOMWindow.OPEN_DEFAULTWINDOW`, `Ci.nsIBrowserDOMWindow.OPEN_EXTERNAL`, `Ci.nsIBrowserDOMWindow.OPEN_FORCE_ALLOW_DATA_URI`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_BACKGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_FOREGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_NEWWINDOW`, `Ci.nsIBrowserDOMWindow.OPEN_NO_REFERRER`, `Ci.nsIBrowserDOMWindow.OPEN_PRINT_BROWSER`, `Ci.nsIReferrerInfo.EMPTY`, `Ci.nsIScriptSecurityManager.DEFAULT_USER_CONTEXT_ID`, `Ci.nsIWebNavigation.LOAD_FLAGS_FIRST_LOAD`, `Ci.nsIWebNavigation.LOAD_FLAGS_FORCE_ALLOW_DATA_URI`, `Ci.nsIWebNavigation.LOAD_FLAGS_FROM_EXTERNAL`, `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`, `Ci.nsIWritablePropertyBag2`, `Cr.NS_ERROR_FAILURE`, `aOpenWindowInfo.isRemote`, `aOpenWindowInfo.originAttributes.privateBrowsingId`, `aOpenWindowInfo.originAttributes.userContextId`, `aOpenWindowInfo.parent`, `aOpenWindowInfo.parent.window`, `aOpenWindowInfo.parent.window.document.referrerInfo.referrerPolicy`, `aOpenWindowInfo.parent.window.location.href`, `aOpenWindowInfo?.parent?.top.embedderElement`, `aTriggeringPrincipal.isSystemPrincipal`, `aURI.spec`, `browser.browsingContext`, `lazy.ReferrerInfo`, `lazy.loadDivertedInBackground`, `this.win`, `this.win.gBrowser.selectedBrowser.browsingContext`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / [`nsIReferrerInfo`](../../docshell/shistory/nsISHEntry.idl.md) / `nsIScriptSecurityManager` / [`nsIWebNavigation`](../../docshell/base/nsIWebNavigation.idl.md) / [`nsIWritablePropertyBag2`](../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/hash-property-bag;1` / `Services.io` / `Services.prefs`

## BrowserDOMWindow.createContentWindowInFrame()
- 位置: L450-462
- 役割: 読み込みなしでフレーム向けの内容窓を作る。
- 触るとき: フレームからの窓作成の経路を変えるとき。
- 呼び出し先: `this.#getContentWindowOrOpenURIInFrame()`

## BrowserDOMWindow.openURIInFrame()
- 位置: L467-476
- 役割: フレームからの URL 読み込みを、新しいタブとして開く。
- 触るとき: フレーム内のリンクの扱いを変えるとき。
- 呼び出し先: `this.#getContentWindowOrOpenURIInFrame()`

## BrowserDOMWindow.#getContentWindowOrOpenURIInFrame()
- 位置: L487-537
- 役割: 印刷用と新しいタブ(通常・背景・前面)だけを受け付け、ユーザーコンテキストを決めて #openURIInNewTab に渡す。
- 触るとき: フレームからのタブ開きで受け付ける種類や、ユーザーコンテキストの引き継ぎを変えるとき。受け付けない種類は null を返す。
- 呼び出し先: `this.#openURIInNewTab()`
- 条件付き依存: `if (aWhere == Ci.nsIBrowserDOMWindow.OPEN_PRINT_BROWSER)` → `this.win.PrintUtils.handleStaticCloneCreatedForPrint()`
- 条件付き依存: `if ( aWhere != Ci.nsIBrowserDOMWindow.OPEN_NEWTAB && aWhere != Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_BACKGROUND && aWhere != Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_FORE...)` → `dump()`
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_EXTERNAL`, `Ci.nsIBrowserDOMWindow.OPEN_FORCE_ALLOW_DATA_URI`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_BACKGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_FOREGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_PRINT_BROWSER`, `Ci.nsIScriptSecurityManager.DEFAULT_USER_CONTEXT_ID`, `aParams.isPrivate`, `aParams.openWindowInfo`, `aParams.openerBrowser`, `aParams.openerOriginAttributes`, `aParams.openerOriginAttributes.userContextId`, `aParams.policyContainer`, `aParams.referrerInfo`, `aParams.triggeringPrincipal`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / `nsIScriptSecurityManager`

## BrowserDOMWindow.canClose()
- 位置: L542-544
- 役割: ウィンドウを閉じてよいかを CanCloseWindow に問い合わせて返す。
- 触るとき: ウィンドウを閉じる前の確認条件を変えるとき。
- 呼び出し先: `this.win.CanCloseWindow()`

## BrowserDOMWindow.tabCount()
- 位置: L549-551
- 役割: ウィンドウのタブ数を返す。
- 触るとき: 外部からタブ数を読む処理の結果を確かめるとき。
- 参照: `this.win.gBrowser.tabs.length`
