# browser/base/content/utilityOverlay.js

source: browser/base/content/utilityOverlay.js
source-hash: 3b8782f6fc3a2ad1b40aa17af34db482b998691b
lines: 605

## <module>
- 役割: ブラウザ全体で使うグローバル関数を置くスクリプト。リンクを開く処理、コンテナーメニューの構築、設定画面やヘルプの起動などを含む。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Components.Constructor()`, `Object.defineProperty()`

## get()
- 位置: L42-74
- 役割: BROWSER_NEW_TAB_URL の getter。プライベートウィンドウなら about:privatebrowsing、AI ウィンドウなら AIWindow.newTabURL、それ以外は AboutNewTab.newTabURL を返す。
- 触るとき: 新しいタブの URL が想定と違うとき、またはプライベートウィンドウや AI ウィンドウでの新規タブの扱いを変えるときに見る。
- 呼び出し先: `AIWindow.isAIWindowActive()`, `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `ExtensionUtils.isExtensionUrl()`
- 参照: `AIWindow.newTabURL`, `AboutNewTab.newTabURL`, `AboutNewTab.newTabURLOverridden`, `PrivateBrowsingUtils.permanentPrivateBrowsing`
- XPCOM: `Services.prefs`

## isBlankPageURL()
- 位置: L84-91
- 役割: about:blank、about:home、新規タブ URL、blanktab.html のいずれかなら true を返す。
- 触るとき: 空白ページ扱いで分岐する処理(起動時のタブ置き換えなど)の条件を確かめるときに見る。

## doGetProtocolFlags()
- 位置: L93-95
- 役割: Services.io.getDynamicProtocolFlags に URI を渡して、その動的なプロトコルのフラグを返す。
- 触るとき: URI のプロトコル性質による判定がずれるときに見る。
- 呼び出し先: `Services.io.getDynamicProtocolFlags()`
- XPCOM: `Services.io`

## openUILink()
- 位置: L97-116
- 役割: 引数を URILoadingHelper.openUILink に渡し、現在のウィンドウでリンクを開く。
- 触るとき: ボタンやメニューのクリックで URL を開く挙動(中クリック、修飾キー、POST データ)を調べるときに見る。
- 呼び出し先: `URILoadingHelper.openUILink()`

## openTrustedLinkIn()
- 位置: L118-120
- 役割: URILoadingHelper.openTrustedLinkIn に委譲する。信頼された URL を指定の場所(タブやウィンドウ)で開く。
- 触るとき: 内部ページのリンクが別タブで開かない、または開き方がずれるときに見る。
- 呼び出し先: `URILoadingHelper.openTrustedLinkIn()`

## openWebLinkIn()
- 位置: L122-124
- 役割: URILoadingHelper.openWebLinkIn に委譲し、Web ページの URL を指定の場所で開く。
- 触るとき: Web の URL を新規タブや新規ウィンドウで開く処理を変えるときに見る。
- 呼び出し先: `URILoadingHelper.openWebLinkIn()`

## openLinkIn()
- 位置: L126-128
- 役割: URILoadingHelper.openLinkIn に委譲し、指定の場所で URL を開いてその結果を返す。
- 触るとき: 呼び出し元が戻り値を使うケースで、開く結果が正しく返るかを確かめるときに見る。
- 呼び出し先: `URILoadingHelper.openLinkIn()`

## checkForMiddleClick()
- 位置: L133-177
- 役割: 中クリックなら node の command イベントを発火し、クリックを止めてから、含まれるメニューを閉じる。disabled のときは何もしない。
- 触るとき: リンク風の要素で中クリックが二重に動く、またはメニューが閉じないといった問題を調べるときに見る。
- 呼び出し先: `node.hasAttribute()`
- 条件付き依存: `if (event.button == 1)` → `document.createEvent()`
- 条件付き依存: `if (event.button == 1)` → `cmdEvent.initCommandEvent()`
- 条件付き依存: `if (event.button == 1)` → `node.dispatchEvent()`
- 条件付き依存: `if (event.button == 1)` → `event.stopPropagation()`
- 条件付き依存: `if (event.button == 1)` → `event.preventDefault()`
- 条件付き依存: `if (event.button == 1)` → `closeMenus()`
- 参照: `event.altKey`, `event.button`, `event.ctrlKey`, `event.inputSource`, `event.metaKey`, `event.shiftKey`, `event.target`, `event.target.tagName`

## createUserContextMenu()
- 位置: L181-318
- 役割: 既存の子要素を消し、コンテナーの一覧と「新しいタブ」「コンテナーを追加」「コンテナーを管理」の項目を作って target に入れる。パネルリストかメニューかで部品を変える。
- 触るとき: コンテナーメニューの項目や並び、無効化される項目を変えるとき、またはメニューに表示されない項目があると報告されたときに見る。
- 呼び出し先: `ContextualIdentityService.getPublicIdentities()`, `ContextualIdentityService.getPublicIdentities().forEach()`, `ContextualIdentityService.getUserContextLabel()`, `MozXULElement.insertFTLIfNeeded()`, `createMenuItem()`, `docfrag.appendChild()`, `document.createDocumentFragment()`, `document.createElement()`, `document.createXULElement()`, `menuitem.setAttribute()`, `target.appendChild()`, `target.firstChild.remove()`, `target.hasChildNodes()`
- 条件付き依存: `if (excludeUserContextId || showDefaultTab)` → `createMenuItem()`
- 条件付き依存: `if (excludeUserContextId || showDefaultTab)` → `menuitem.setAttribute()`
- 条件付き依存: `if (!isContextMenu)` → `menuitem.setAttribute()`
- 条件付き依存: `if (excludeUserContextId || showDefaultTab)` → `docfrag.appendChild()`
- 条件付き依存: `if (excludeUserContextId || showDefaultTab)` → `createSeparator()`
- 条件付き依存: `if (isPanelList)` → `ContextualIdentityService.getContainerIconURL()`
- 条件付き依存: `if (isPanelList)` → `menuitem.style.setProperty()`
- 条件付き依存: `if (isPanelList)` → `ContextualIdentityService.getContainerColorCode()`
- 条件付き依存: `if (!(isPanelList))` → `menuitem.classList.add()`
- 条件付き依存: `if (showAddContainer || showManageContainers)` → `docfrag.appendChild()`
- 条件付き依存: `if (showAddContainer || showManageContainers)` → `createSeparator()`
- 条件付き依存: `if (showAddContainer)` → `createMenuItem()`
- 条件付き依存: `if (showAddContainer)` → `onActivate()`
- 条件付き依存: `if (showAddContainer)` → `ContainerCreationPanel.open()`
- 条件付き依存: `if (showAddContainer)` → `docfrag.appendChild()`
- 条件付き依存: `if (showManageContainers)` → `createMenuItem()`
- 条件付き依存: `if (showManageContainers)` → `onActivate()`
- 条件付き依存: `if (showManageContainers)` → `openPreferences()`
- 条件付き依存: `if (showManageContainers)` → `docfrag.appendChild()`
- 参照: `event.target`, `identity.color`, `identity.icon`, `identity.userContextId`

## onActivate()
- 位置: L204-210
- 役割: 項目のイベントを、パネルリストなら click、メニューなら command に登録し、メニューでは伝播を止めてから callback を呼ぶ。
- 触るとき: コンテナーメニューの項目を押しても反応しない、または二重に反応するときに見る。
- 呼び出し先: `callback()`, `item.addEventListener()`
- 条件付き依存: `if (!isPanelList)` → `activateEvent.stopPropagation()`

## panelListReplacements()
- 位置: L220-221
- 役割: パネルリストのときだけ、通常の l10n ID を panel-item 用の ID に置き換える。
- 触るとき: パネルリストの文言が通常メニューと違う、または古いままになるときに見る。

## createMenuItem()
- 位置: L223-242
- 役割: パネルリストなら panel-item、メニューなら menuitem を作り、名前か l10n ID でラベルを設定する。
- 触るとき: コンテナーメニューの項目の作り方を変えるとき、または名前と l10n ID の使い分けを確かめるときに見る。
- 呼び出し先: `document.createElement()`, `document.createXULElement()`
- 条件付き依存: `if (name)` → `setLabel()`
- 条件付き依存: `if (!(name))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(name))` → `panelListReplacements()`

## setLabel()
- 位置: L227-233
- 役割: パネルリストなら textContent に、メニューなら label 属性にラベルを書く。
- 触るとき: メニューの表示ラベルが空になる、またはパネルで文字が出ないときに見る。
- 条件付き依存: `if (!(isPanelList))` → `item.setAttribute()`
- 参照: `item.textContent`

## closeMenus()
- 位置: L321-333
- 役割: node から親をたどり、XUL の menupopup と popup を hidePopup で閉じる。
- 触るとき: メニューの項目を操作した後にメニューが閉じない、または閉じすぎるときに見る。
- 条件付き依存: `if ( node.namespaceURI == "http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul" && (node.tagName == "menupopup" || node.tagName == "popup") )` → `node.hidePopup()`
- 条件付き依存: `if ("tagName" in node)` → `closeMenus()`
- 参照: `node.namespaceURI`, `node.parentNode`, `node.tagName`

## eventMatchesKey()
- 位置: L346-379
- 役割: キーイベントの key と、キー要素の key と modifiers 属性が一致するかを判定する。accel は macOS では Meta、それ以外では Control として扱う。
- 触るとき: 新しいショートカットを追加するとき、または修飾キーの判定が想定と違うときに見る。
- 呼び出し先: `(aKey.getAttribute("key") || "").toLowerCase()`, `aEvent.getModifierState()`, `aKey.getAttribute()`, `modifiers.filter()`
- 条件付き依存: `if (keyModifiers)` → `keyModifiers.split()`
- 条件付き依存: `if (keyModifiers)` → `keyModifiers.forEach()`
- 条件付き依存: `if (!(modifier == "accel"))` → `modifier[0].toUpperCase()`
- 条件付き依存: `if (!(modifier == "accel"))` → `modifier.slice()`
- 条件付き依存: `if (keyModifiers)` → `modifiers.every()`
- 条件付き依存: `if (keyModifiers)` → `keyModifiers.includes()`
- 条件付き依存: `if (keyModifiers)` → `aEvent.getModifierState()`
- 参照: `AppConstants.platform`, `aEvent.key`, `eventModifiers.length`, `keyModifiers.length`

## gatherTextUnder()
- 位置: L384-389
- 役割: text/plain のドキュメントエンコーダーで root 以下のテキストを取り出し、前後の空白を除いて返す。
- 触るとき: 右クリックでのテキスト取得結果が変わったとき、または ContextMenuChild 側の同等処理と差が出たときに見る。
- 呼び出し先: `Cu.createDocumentEncoder()`, `encoder.encodeToString()`, `encoder.encodeToString().trim()`, `encoder.init()`, `encoder.setContainerNode()`
- 参照: `root.ownerDocument`

## getShellService()
- 位置: L392-394
- 役割: 互換のために ShellService を返す。
- 触るとき: 既定ブラウザ関連の呼び出しで ShellService が取れないときに見る。

## isBidiEnabled()
- 位置: L396-409
- 役割: bidi.browser.ui が真ならそれを返し、そうでなければアプリのロケールが RTL かを返す。RTL のときは bidi.browser.ui を立てる。
- 触るとき: 右から左へのレイアウトの切り替え条件を変えるとき、または RTL 言語での表示が崩れるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (isRTL)` → `Services.prefs.setBoolPref()`
- 参照: `Services.locale.isAppLocaleRTL`
- XPCOM: `Services.locale` / `Services.prefs`

## openAboutDialog()
- 位置: L411-432
- 役割: 既に開いている about ウィンドウがあればフォーカスし、無ければ aboutDialog.xhtml を開く。
- 触るとき: バージョン情報の画面が二重に開く、または開かないときに見る。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `Services.wm.getEnumerator()`, `win.focus()`, `win.openDialog()`
- 参照: `AppConstants.platform`, `win.closed`
- XPCOM: `Services.wm`

## openReferralsPage()
- 位置: L434-436
- 役割: Referrals.openReferralsTab を help_menu として呼ぶ。
- 触るとき: ヘルプメニューの紹介ページの導線を変えるときに見る。
- 呼び出し先: `Referrals.openReferralsTab()`

## openPreferences()
- 位置: async L438-520
- 役割: 設定画面(about:settings / about:preferences)を開くか既存タブを前面にし、ペイン ID とURL パラメーターに従ってページを移動する。
- 触るとき: 設定の特定のペインが開かない、同じタブが重複するといった問題を調べるとき、または URL パラメーターを追加するときに見る。
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `internalPrefCategoryNameToFriendlyName()`
- 条件付き依存: `if (urlParams[name] !== undefined)` → `params.set()`
- 条件付き依存: `if (!win)` → `Cc["@mozilla.org/array;1"].createInstance()`
- 条件付き依存: `if (!win)` → `Cc[ "@mozilla.org/supports-string;1" ].createInstance()`
- 条件付き依存: `if (!win)` → `windowArguments.appendElement()`
- 条件付き依存: `if (!win)` → `Services.ww.openWindow()`
- 条件付き依存: `if (!(!win))` → `win.switchToTabHavingURI()`
- 条件付き依存: `if (!(!win))` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (newLoad)` → `win.switchToTabHavingURI()`
- 条件付き依存: `if (newLoad)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (browser.contentDocument?.readyState != "complete")` → `browser.addEventListener()`
- 条件付き依存: `if (!newLoad && paneID)` → `browser.contentWindow.gotoPref()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIMutableArray`, `Ci.nsISupportsString`, `browser.contentDocument?.readyState`, `extraArgs.urlParams`, `supportsStringPrefURL.data`, `win.gBrowser.selectedBrowser`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/supports-string;1` / `Services.scriptSecurityManager` / `Services.wm` / `Services.ww`

## internalPrefCategoryNameToFriendlyName()
- 位置: L440-444
- 役割: pane で始まるカテゴリー名から先頭の pane を除き、先頭文字を小文字にして URL のフラグメント名を返す。
- 触るとき: 設定の URL の末尾(#)がペイン名と合わないときに見る。preferences.js 側の同じ処理と揃えるべき点に注意する。
- 呼び出し先: `(aName || "").replace()`, `toReplace[4].toLowerCase()`

## openTroubleshootingPage()
- 位置: L526-528
- 役割: about:support を新しいタブで開く。
- 触るとき: トラブルシューティングのメニューがポリシーで無効化されたときなどに、開く先を確かめるときに見る。
- 呼び出し先: `openTrustedLinkIn()`

## openFeedbackPage()
- 位置: L533-536
- 役割: app.feedback.baseURL から URL を作り、新しいタブで開く。
- 触るとき: フィードバックのリンク先を変えるとき、または開く場所が違うと報告されたときに見る。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `openTrustedLinkIn()`
- XPCOM: `Services.urlFormatter`

## openSwitchingDevicesPage()
- 位置: L541-549
- 役割: switching-devices のヘルプ URL に、help-menu 由来の utm_* パラメーターを付けて新しいタブで開く。
- 触るとき: 端末移行ページの計測用パラメーターを変えるときに見る。
- 呼び出し先: `getHelpLinkURL()`, `openTrustedLinkIn()`, `parsedUrl.searchParams.set()`
- 参照: `parsedUrl.href`

## buildHelpMenu()
- 位置: L551-579
- 役割: ポリシーと pref に従ってヘルプメニューの項目の有効・非表示を決め、サポートメニューの表示と Safe Browsing の偽サイト報告項目を更新する。
- 触るとき: ヘルプメニューの項目が出ない、または無効なのに押せるといったときに見る。
- 呼び出し先: `Services.policies.getSupportMenu()`, `Services.policies.isAllowed()`, `Services.prefs.getBoolPref()`, `document.getElementById()`
- 条件付き依存: `if (supportMenu)` → `document.getElementById()`
- 条件付き依存: `if (supportMenu)` → `menuitem.setAttribute()`
- 条件付き依存: `if ("AccessKey" in supportMenu)` → `menuitem.setAttribute()`
- 条件付き依存: `if (typeof gSafeBrowsing != "undefined")` → `gSafeBrowsing.setReportPhishingMenu()`
- 参照: `document.getElementById("feedbackPage").disabled`, `document.getElementById("helpPolicySeparator").hidden`, `document.getElementById("helpSafeMode").disabled`, `document.getElementById("menu_referralsPage").hidden`, `document.getElementById("troubleShooting").disabled`, `menuitem.hidden`, `supportMenu.AccessKey`, `supportMenu.Title`
- XPCOM: `Services.policies` / `Services.prefs`

## isElementVisible()
- 位置: L581-590
- 役割: 要素が null でなく、表示上の高さと幅がどちらも正なら true を返す。
- 触るとき: 非表示の要素を対象にしてしまう処理や、表示の判定がずれるときに見る。
- 呼び出し先: `aElement.getBoundingClientRect()`
- 参照: `rect.height`, `rect.width`

## makeURLAbsolute()
- 位置: L592-595
- 役割: base を基準に相対 URL を絶対 URL にし、その spec を返す。不正な URL では例外になる。
- 触るとき: 相対リンクが解決されない、または不正な URL で例外が出るときに見る。
- 呼び出し先: `makeURI()`
- 参照: `makeURI(aUrl, null, makeURI(aBase)).spec`

## getHelpLinkURL()
- 位置: L597-600
- 役割: app.support.baseURL に aHelpTopic を連結した URL を返す。
- 触るとき: ヘルプのトピックを増やすとき、または URL の組み立てがずれるときに見る。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## openHelpLink()
- 位置: L602-604
- 役割: getHelpLinkURL で作った URL を新しいタブで開く。
- 触るとき: ヘルプリンクのクリックで開くページが違うときに見る。
- 呼び出し先: `getHelpLinkURL()`, `openTrustedLinkIn()`
