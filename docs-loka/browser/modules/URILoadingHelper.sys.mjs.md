# browser/modules/URILoadingHelper.sys.mjs

source: browser/modules/URILoadingHelper.sys.mjs
source-hash: 6f88bf621d9c423954d59deb2798fb37303dd04e
lines: 1134

## <module>
- 役割: リンクや URL を、現在のタブ、新しいタブ、新しいウィンドウ、保存などの指定先で開くための共通の窓口。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Components.Constructor()`

## saveLink()
- 位置: L26-61
- 役割: where が save のときに window.saveURL で保存する。isContentWindowPrivate がある呼び出しと、initiatingDoc が必要な旧形式の2通りに分かれる。
- 触るとき: リンクの名前を付けて保存の挙動や、initiatingDoc が無いときのエラーを調べるとき。
- 条件付き依存: `if ("isContentWindowPrivate" in params)` → `window.saveURL()`
- 条件付き依存: `if (!params.initiatingDoc)` → `console.error()`
- 条件付き依存: `if (!("isContentWindowPrivate" in params))` → `window.saveURL()`
- 参照: `params.initiatingDoc`, `params.isContentWindowPrivate`, `params.originPrincipal`, `params.referrerInfo`

## openInWindow()
- 位置: L63-255
- 役割: 新しいブラウザーウィンドウを、ウィンドウ用の feature 文字列と引数の配列を組み立てて開く。プライベートでは referrer を外し、chromeless では最小限の feature を付ける。
- 触るとき: 新しいウィンドウのオプション(プライベート、chromeless、リファラー)を変えるとき、新規ウィンドウに渡す情報を増やすとき。
- 呼び出し先: `Cc[ "@mozilla.org/supports-PRBool;1" ].createInstance()`, `Cc[ "@mozilla.org/supports-PRUint32;1" ].createInstance()`, `Cc["@mozilla.org/array;1"].createInstance()`, `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`, `Cc["@mozilla.org/supports-string;1"].createInstance()`, `Services.ww.openWindow()`, `sa.appendElement()`
- 条件付き依存: `if (triggeringRemoteType)` → `extraOptions.setPropertyAsACString()`
- 条件付き依存: `if (params.hasValidUserGestureActivation !== undefined)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (params.textDirectiveUserActivation !== undefined)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (forceAllowDataURI)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (params.fromExternal !== undefined)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `extraOptions.setPropertyAsACString()`
- 条件付き依存: `if (globalHistoryOptions.triggeringSponsoredURLVisitTimeMS)` → `extraOptions.setPropertyAsUint64()`
- 条件付き依存: `if (globalHistoryOptions.triggeringSource)` → `extraOptions.setPropertyAsACString()`
- 条件付き依存: `if (params.schemelessInput !== undefined)` → `extraOptions.setPropertyAsUint32()`
- 条件付き依存: `if (params.aiWindow)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (chromeless)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (params.aswebauth)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (params.frameID != undefined && sourceWindow)` → `waitForWindowStartup().then()`
- 条件付き依存: `if (params.frameID != undefined && sourceWindow)` → `waitForWindowStartup()`
- 条件付き依存: `if (params.frameID != undefined && sourceWindow)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (resolveOnContentBrowserCreated)` → `waitForWindowStartup().then()`
- 条件付き依存: `if (resolveOnContentBrowserCreated)` → `waitForWindowStartup()`
- 条件付き依存: `if (resolveOnContentBrowserCreated)` → `resolveOnContentBrowserCreated()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIMutableArray`, `Ci.nsISupportsPRBool`, `Ci.nsISupportsPRUint32`, `Ci.nsISupportsString`, `Ci.nsIWritablePropertyBag2`, `allowThirdPartyFixupSupports.data`, `globalHistoryOptions.triggeringSource`, `globalHistoryOptions.triggeringSponsoredURL`, `globalHistoryOptions.triggeringSponsoredURLVisitTimeMS`, `globalHistoryOptions?.triggeringSponsoredURL`, `lazy.ReferrerInfo`, `params.aiWindow`, `params.aswebauth`, `params.frameID`, `params.fromExternal`, `params.hasValidUserGestureActivation`, `params.private`, `params.schemelessInput`, `params.textDirectiveUserActivation`, `referrerInfo.originalReferrer`, `referrerInfo.referrerPolicy`, `sourceWindow.gBrowser.selectedBrowser`, `userContextIdSupports.data`, `win.gBrowser.selectedBrowser`, `wuri.data`
- XPCOM: [`nsIMutableArray`](../../docshell/shistory/nsISHEntry.idl.md) / [`nsISupportsPRBool`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsISupportsPRUint32`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsIWritablePropertyBag2`](../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `@mozilla.org/supports-PRBool;1` / `@mozilla.org/supports-PRUint32;1` / `@mozilla.org/supports-string;1` / `Services.obs` / `Services.ww`

## waitForWindowStartup()
- 位置: L192-219
- 役割: 新しく開くウィンドウの browser-delayed-startup-finished を待つ Promise を返す。ウィンドウが先に閉じた場合は解決せず、監視だけ外す。
- 触るとき: 新しいウィンドウの起動後に処理を行うタイミングを変えるとき、ウィンドウ起動待ちが終わらない問題を調べるとき。
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## removeObservers()
- 位置: L194-200
- 役割: 起動完了と、ウィンドウ終了の両方の監視を外す。
- 触るとき: 起動待ちの監視解除の漏れを調べるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## delayedStartupObserver()
- 位置: L201-206
- 役割: 対象の新規ウィンドウの起動完了を受けたら監視を外して Promise を解決する。
- 触るとき: 新規ウィンドウの起動完了の判定を変えるとき。
- 条件付き依存: `if (aSubject == win)` → `removeObservers()`
- 条件付き依存: `if (aSubject == win)` → `resolve()`

## closedObserver()
- 位置: L208-212
- 役割: 対象の新規ウィンドウが閉じられたら、起動待ちの監視だけを外す。
- 触るとき: 閉じられたウィンドウの監視が残る問題を調べるとき。
- 条件付き依存: `if (aSubject == win)` → `removeObservers()`

## openInCurrentTab()
- 位置: L257-327
- 役割: 指定のブラウザーで URL を読み込む。third-party fixup、継承しない principal、ポップアップ許可などを load flag に変換して fixupAndLoadURIString を呼ぶ。
- 触るとき: 現在のタブでの読み込みの flag の決め方を変えるとき、読み込みの挙動が変わった原因を調べるとき。
- 呼び出し先: `Services.io.getDynamicProtocolFlags()`, `params.resolveOnContentBrowserCreated()`, `targetBrowser.fixupAndLoadURIString()`
- 条件付き依存: `if ( params.forceAboutBlankViewerInCurrent && (!uriObj || Services.io.getDynamicProtocolFlags(uriObj) & URI_INHERITS_SECURITY_CONTEXT) )` → `targetBrowser.createAboutBlankDocumentViewer()`
- 参照: `Ci.nsIProtocolHandler`, `Ci.nsIWebNavigation.LOAD_FLAGS_ALLOW_POPUPS`, `Ci.nsIWebNavigation.LOAD_FLAGS_ALLOW_THIRD_PARTY_FIXUP`, `Ci.nsIWebNavigation.LOAD_FLAGS_DISALLOW_INHERIT_PRINCIPAL`, `Ci.nsIWebNavigation.LOAD_FLAGS_ERROR_LOAD_CHANGES_RV`, `Ci.nsIWebNavigation.LOAD_FLAGS_FIXUP_SCHEME_TYPOS`, `Ci.nsIWebNavigation.LOAD_FLAGS_FORCE_ALLOW_DATA_URI`, `Ci.nsIWebNavigation.LOAD_FLAGS_FROM_EXTERNAL`, `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`, `params.allowInheritPrincipal`, `params.allowPopups`, `params.allowThirdPartyFixup`, `params.forceAboutBlankViewerInCurrent`, `params.forceAllowDataURI`, `params.fromExternal`, `params.indicateErrorPageLoad`, `params.originPrincipal`, `params.originStoragePrincipal`
- XPCOM: [`nsIProtocolHandler`](../../netwerk/base/nsIIOService.idl.md) / [`nsIWebNavigation`](../../docshell/base/nsIWebNavigation.idl.md) / `Services.io`

## updatePrincipals()
- 位置: L329-355
- 役割: origin、storage、triggering の各 principal に、userContextId とプライベート状態を反映させた OA を付け直す。
- 触るとき: 新しいコンテナータブやプライベートウィンドウで開くときに principal の区切りが合わない問題を調べるとき。
- 呼び出し先: `useOAForPrincipal()`
- 参照: `params.originPrincipal`, `params.originStoragePrincipal`, `params.triggeringPrincipal`

## useOAForPrincipal()
- 位置: L336-349
- 役割: コンテンツ principal に userContextId、privateBrowsingId、firstPartyDomain を付けた principal を返す。システムや null の principal はそのまま返す。
- 触るとき: principal に付ける属性を変えるとき。
- 条件付き依存: `if (principal && principal.isContentPrincipal)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (principal && principal.isContentPrincipal)` → `Services.scriptSecurityManager.principalWithOA()`
- 参照: `params.private`, `principal.isContentPrincipal`, `principal.originAttributes.firstPartyDomain`
- XPCOM: `Services.scriptSecurityManager`

## _createNullPrincipalFromTabUserContextId()
- 位置: L359-372
- 役割: 指定タブ(省略時は選択中のタブ)の userContextId で null principal を作る。
- 触るとき: コンテナーの区切りを守る null principal を作る経路を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `lazy.BrowserWindowTracker.getTopWindow()`, `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("usercontextid"))` → `tab.getAttribute()`
- 参照: `window.gBrowser.selectedTab`
- XPCOM: `Services.scriptSecurityManager`

## openLinkIn()
- 位置: L489-695
- 役割: where の値に応じて、保存、新規ウィンドウ、現在のタブ、新規タブの各経路に振り分けて URL を読み込む。現在のタブは固定タブやコンテナーの違いで新規タブに切り替え、最後にバウンス計測と内容へのフォーカスを行う。
- 触るとき: リンクを開く先の判定や、現在のタブが置き換わる条件を変えるとき、リンクが期待どおりの場所に開かない問題を調べるとき。
- 呼び出し先: `BrowserUtils.willLoadInBackground()`, `Object.assign()`, `openInCurrentTab()`, `resolveOnContentBrowserCreated()`, `resolveOnNewTabCreated()`, `this._resolveInitialTargetWindow()`, `updatePrincipals()`, `w.focus()`, `w.gBrowser.addTab()`, `w.isBlankPageURL()`
- 条件付き依存: `if (where == "save")` → `saveLink()`
- 条件付き依存: `if (!w || where == "window")` → `openInWindow()`
- 条件付き依存: `if (where == "current")` → `URL.parse()`
- 条件付き依存: `if (where == "current")` → `w.gBrowser.getTabForBrowser()`
- 条件付き依存: `if ( !allowPinnedTabHostChange && tab.pinned && url != "about:crashcontent" )` → `uriObj.schemeIs()`
- 条件付き依存: `if (params.frameID != undefined && w)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!params.initiatedByURLBar && targetBrowser)` → `lazy.handleBounceEventTrigger()`
- 条件付き依存: `if ( !params.avoidBrowserFocus && !focusUrlBar && targetBrowser == w.gBrowser.selectedBrowser )` → `targetBrowser.focus()`
- 参照: `Ci.nsIReferrerInfo.EMPTY`, `URL.parse(url)?.URI`, `lazy.AboutNewTab.willNotifyUser`, `lazy.ReferrerInfo`, `params.avoidBrowserFocus`, `params.chromeless`, `params.eventDetail`, `params.frameID`, `params.fromExternal`, `params.initiatedByURLBar`, `params.openerBrowser`, `params.referrerInfo`, `params.relatedToCurrent`, `params.schemelessInput`, `params.targetBrowser`, `params.userContextId`, `tab.pinned`, `tabUsedForLoad.linkedBrowser`, `targetBrowser.browsingContext.originAttributes.userContextId`, `targetBrowser.currentURI.host`, `uriObj.host`, `w.FirefoxViewHandler.tab`, `w.document.activeElement`, `w.gBrowser.selectedBrowser`, `w.gURLBar.inputField`
- XPCOM: [`nsIReferrerInfo`](../../docshell/shistory/nsISHEntry.idl.md) / `Services.obs`

## _resolveInitialTargetWindow()
- 位置: L710-727
- 役割: where に応じて、読み込みに使う最初のウィンドウを決める。新規タブのときはポップアップ等を除いたウィンドウを選び、同じウィンドウでなければ relatedToCurrent を false にする。
- 触るとき: 新規タブをどのウィンドウに開くかを変えるとき。
- 呼び出し先: `this.getTargetWindow()`
- 条件付き依存: `if (where === "tab" || where === "tabshifted")` → `this.getTargetWindow()`
- 参照: `params.relatedToCurrent`, `params.targetBrowser`, `params.targetBrowser.documentGlobal`, `win.top`

## getTargetWindow()
- 位置: L741-766
- 役割: 現在のウィンドウが条件に合えばそれを、合わなければ条件に合う最前面のブラウザーウィンドウを返す。
- 触るとき: リンクを開くウィンドウの選び方(ポップアップ、taskbar tab、プライベート)を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `lazy.BrowserWindowTracker.getTopWindow()`, `top.document.documentElement.getAttribute()`, `top.document.documentElement.hasAttribute()`
- 参照: `top.toolbar.visible`

## openUILink()
- 位置: L793-832
- 役割: UI 要素のクリックから URL を開く。イベントの修飾キーやボタンから開き先を決め、triggeringPrincipal が必須で、forceForeground は既定で true になる。
- 触るとき: UI のクリックやキー操作による開き先の決め方を変えるとき。
- 呼び出し先: `BrowserUtils.getRootEvent()`, `BrowserUtils.whereToOpenLink()`, `this.openLinkIn()`
- 参照: `event.target.ownerDocument`, `params.forceForeground`, `params.ignoreAlt`, `params.ignoreButton`, `params.triggeringPrincipal`

## openTrustedLinkIn()
- 位置: L848-856
- 役割: triggeringPrincipal が無ければシステム principal を使って openLinkIn を呼ぶ。
- 触るとき: 信頼された内部の URL を開く経路の principal の扱いを変えるとき。
- 呼び出し先: `this.openLinkIn()`
- 条件付き依存: `if (!params.triggeringPrincipal)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `params.forceForeground`, `params.triggeringPrincipal`
- XPCOM: `Services.scriptSecurityManager`

## openWebLinkIn()
- 位置: L873-885
- 役割: triggeringPrincipal が無ければ null principal を使う。システム principal が渡されたら例外を投げて openLinkIn を呼ぶ。
- 触るとき: Web コンテンツ由来のリンクを開くときの principal の扱いを変えるとき。
- 呼び出し先: `this.openLinkIn()`
- 条件付き依存: `if (!params.triggeringPrincipal)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 参照: `params.forceForeground`, `params.triggeringPrincipal`, `params.triggeringPrincipal.isSystemPrincipal`
- XPCOM: `Services.scriptSecurityManager`

## guessUserContextId()
- 位置: L897-928
- 役割: ホストが一致する表示中のタブを、開いているウィンドウ全体で数え、最も多いコンテナーの userContextId を返す。無ければ null を返す。
- 触るとき: 外部から開いた文書を、ログイン済みのコンテナーで開く推定を変えるとき。
- 条件付き依存: `if (currentURIHost == host)` → `containerScores.get()`
- 条件付き依存: `if (currentURIHost == host)` → `containerScores.set()`
- 参照: `aURI.host`, `lazy.BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser.currentURI.host`, `win.gBrowser.visibleTabs`

## switchToTabHavingURI()
- 位置: L965-1132
- 役割: 同じ URL のタブを、現在のウィンドウ、次に他のウィンドウから探して選択する。見つからず aOpenNew が真なら、選択中のタブが空ならそのタブで、それ以外は新規タブで開く。見つかったら true を返す。
- 触るとき: 既に開いているタブへ切り替える条件(クエリ、フラグメント、コンテナー、別ウィンドウからの移動)を変えるとき。
- 呼び出し先: `switchIfURIInWindow()`
- 条件付き依存: `if (!(aURI instanceof Ci.nsIURI))` → `Services.io.newURI()`
- 条件付き依存: `if (isBrowserWindow && window.gBrowser.selectedTab.isEmpty)` → `this.openTrustedLinkIn()`
- 条件付き依存: `if (!(isBrowserWindow && window.gBrowser.selectedTab.isEmpty))` → `this.openTrustedLinkIn()`
- 参照: `Ci.nsIURI`, `aOpenParams.adoptIntoActiveWindow`, `aOpenParams.ignoreFragment`, `aOpenParams.ignoreQueryString`, `aOpenParams.replaceQueryString`, `aOpenParams.userContextId`, `aURI.spec`, `browserWin.closed`, `lazy.BrowserWindowTracker.orderedWindows`, `window.gBrowser`, `window.gBrowser.selectedTab.isEmpty`
- XPCOM: [`nsIURI`](../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## switchIfURIInWindow()
- 位置: L992-1096
- 役割: 指定ウィンドウの各タブを、比較用の URL 文字列と突き合わせて一致するタブを選択する。プライベート状態が違えば一致させない。
- 触るとき: タブの一致判定の対象や、一致したときの移動(ウィンドウのフォーカス、分割表示)を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `browser.getAttribute()`, `cleanURL()`, `ignoreFragment.startsWith()`, `kPrivateBrowsingURLs.has()`
- 条件付き依存: `if (doAdopt)` → `window.gBrowser.adoptTab()`
- 条件付き依存: `if (doAdopt)` → `aWindow.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (!doAdopt)` → `aWindow.focus()`
- 条件付き依存: `if ( ignoreFragment == "whenComparingAndReplace" || replaceQueryString )` → `browser.loadURI()`
- 条件付き依存: `if ( ignoreFragment == "whenComparingAndReplace" || replaceQueryString )` → `_createNullPrincipalFromTabUserContextId()`
- 条件付き依存: `if (aSplitView)` → `aSplitView.tabs.includes()`
- 条件付き依存: `if (!(aSplitView.tabs.includes(tabToMove)))` → `aSplitView.tabs.find()`
- 条件付き依存: `if (!(aSplitView.tabs.includes(tabToMove)))` → `aSplitView.replaceTab()`
- 条件付き依存: `if (aSplitView)` → `aSplitView.documentGlobal.focus()`
- 参照: `aOpenParams.triggeringPrincipal`, `aURI.displaySpec`, `aURI.spec`, `aWindow.gBrowser.browsers`, `aWindow.gBrowser.selectedTab`, `aWindow.gBrowser.tabContainer.selectedIndex`, `aWindow.gBrowser.tabs`, `browser.currentURI.displaySpec`, `browsers.length`, `tab.selected`, `window.gBrowser.tabContainer.selectedIndex`

## cleanURL()
- 位置: L1004-1020
- 役割: URL からフラグメント、クエリ、またはその両方を取り除いた文字列を返す。
- 触るとき: URL 比較でクエリやフラグメントを無視する範囲を変えるとき。
- 条件付き依存: `if (removeFragment)` → `ret.split()`
- 条件付き依存: `if (removeQuery)` → `ret.split()`
- 条件付き依存: `if (removeQuery)` → `ret .split("?")[0] .concat()`
- 条件付き依存: `if (removeQuery)` → `ret .split()`
- 条件付き依存: `if (removeQuery)` → `"#".concat()`
