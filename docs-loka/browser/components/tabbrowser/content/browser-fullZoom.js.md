# browser/components/tabbrowser/content/browser-fullZoom.js

source: browser/components/tabbrowser/content/browser-fullZoom.js
source-hash: 2eeec9066afc8e6a9cdeb7c2f0eb2c629b456faa
lines: 705

## <module>
- 役割: ページのフルズームとサイト別ズーム設定を管理する FullZoom オブジェクトを定義する。
- 呼び出し先: `ChromeUtils.generateQI()`

## siteSpecific()
- 位置: L27-34
- 役割: サイト別ズームの pref を読んでキャッシュして返す。
- 触るとき: サイト別ズームの有効判定を調べるとき。
- 条件付き依存: `if (this._siteSpecificPref === undefined)` → `Services.prefs.getBoolPref()`
- 参照: `this._siteSpecificPref`
- XPCOM: `Services.prefs`

## FullZoom_init()
- 位置: L46-75
- 役割: イベントと content pref・pref の監視を登録し、初期化前に溜めた位置変更を再生する。
- 触るとき: ズーム機能の初期化を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/content-pref/service;1"].getService()`, `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `gBrowser.addEventListener()`, `this._cps2.addObserverForName()`, `this._initialLocations.has()`, `window.addEventListener()`
- 条件付き依存: `if (this._initialLocations.has(browser))` → `this.onLocationChange()`
- 条件付き依存: `if (this._initialLocations.has(browser))` → `this._initialLocations.get()`
- 参照: `Ci.nsIContentPrefService2`, `gBrowser.browsers`, `this._cps2`, `this._initialLocations`, `this.name`, `this.updateBackgroundTabs`
- XPCOM: [`nsIContentPrefService2`](../../../../dom/interfaces/base/nsIContentPrefService2.idl.md) / `@mozilla.org/content-pref/service;1` → `ContentPrefService2` (toolkit/components/contentprefs/components.conf) / `Services.prefs`

## FullZoom_destroy()
- 位置: L77-83
- 役割: init で登録した監視とイベントリスナーを解除する。
- 触るとき: ズーム機能の終了処理を調べるとき。
- 呼び出し先: `Services.prefs.removeObserver()`, `gBrowser.removeEventListener()`, `this._cps2.removeObserverForName()`, `window.removeEventListener()`
- 参照: `this.name`
- XPCOM: `Services.prefs`

## FullZoom_handleEvent()
- 位置: L89-103
- 役割: 拡大・縮小イベントを対象ブラウザに適用し、ピンチ操作の完了でコマンド状態を更新する。
- 触るとき: ズームのイベント経路を調べるとき。
- 呼び出し先: `this._getTargetedBrowser()`, `this.enlarge()`, `this.reduce()`, `this.updateCommands()`
- 参照: `event.detail`, `event.type`

## observe()
- 位置: L107-127
- 役割: browser.zoom 系 pref の変更を受け、キャッシュ無効化や背景タブ更新設定、コマンド更新を行う。
- 触るとき: ズーム関連 pref の変更への追従を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.updateCommands()`
- 参照: `this._siteSpecificPref`, `this.updateBackgroundTabs`
- XPCOM: `Services.prefs`

## FullZoom_onContentPrefSet()
- 位置: L131-138
- 役割: content pref の設定通知を値付きで内部変更処理へ渡す。
- 触るとき: pref 設定時の反映経路を調べるとき。
- 呼び出し先: `this._onContentPrefChanged()`

## FullZoom_onContentPrefRemoved()
- 位置: L140-146
- 役割: content pref の削除通知を値なしで内部変更処理へ渡す。
- 触るとき: pref 削除時の反映経路を調べるとき。
- 呼び出し先: `this._onContentPrefChanged()`

## FullZoom__onContentPrefChanged()
- 位置: L156-202
- 役割: content pref の変更に応じ、現在のページに該当すればズームを更新する(自身の変更は無視)。
- 触るとき: 他ウィンドウでの設定変更が反映されない時や、グローバル値変更時の挙動を調べるとき。
- 呼び出し先: `this._cps2.extractDomain()`, `this._cps2.getByDomainAndName()`, `this._getBrowserToken()`, `this._isPDFViewer()`, `this._loadContextFromBrowser()`
- 条件付き依存: `if (aGroup == domain && ctxt.usePrivateBrowsing == aIsPrivate)` → `this._applyPrefToZoom()`
- 参照: `browser.currentURI`, `browser.currentURI.spec`, `ctxt.usePrivateBrowsing`, `gBrowser.selectedBrowser`, `this._isNextContentPrefChangeInternal`, `this.name`

## handleResult()
- 位置: L193-195
- 役割: 現在のページにサイト別 pref があることを記録する。
- 触るとき: グローバル変更時のサイト別 pref 判定を調べるとき。

## handleCompletion()
- 位置: L196-200
- 役割: サイト別 pref が無く状態が有効なら、グローバル値をズームに適用する。
- 触るとき: グローバル変更時のズーム適用を調べるとき。
- 条件付き依存: `if (!hasPref && token.isCurrent)` → `this._applyPrefToZoom()`
- 参照: `token.isCurrent`

## FullZoom_onLocationChange()
- 位置: L217-319
- 役割: 位置変更時に保存済みサイト別ズームかグローバル値、特殊ページは固定値を取得して適用する。
- 触るとき: ページ遷移・タブ切替時のズーム復元を調べるとき。
- 呼び出し先: `this._cps2.getByDomainAndName()`, `this._cps2.getCachedByDomainAndName()`, `this._getBrowserToken()`, `this._ignorePendingZoomAccesses()`, `this._isPDFViewer()`, `this._loadContextFromBrowser()`
- 条件付き依存: `if (this._initialLocations)` → `this._initialLocations.set()`
- 条件付き依存: `if (!aURI || (aIsTabSwitch && !this.siteSpecific))` → `this._notifyOnLocationChange()`
- 条件付き依存: `if ( !browser.contentPrincipal || browser.contentPrincipal.isNullPrincipal )` → `this._applyPrefToZoom()`
- 条件付き依存: `if ( !browser.contentPrincipal || browser.contentPrincipal.isNullPrincipal )` → `this._notifyOnLocationChange.bind()`
- 条件付き依存: `if (!( !browser.contentPrincipal || browser.contentPrincipal.isNullPrincipal ))` → `this._applyPrefToZoom()`
- 条件付き依存: `if (!( !browser.contentPrincipal || browser.contentPrincipal.isNullPrincipal ))` → `this._notifyOnLocationChange.bind()`
- 条件付き依存: `if (!aIsTabSwitch && browser.isSyntheticDocument)` → `ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (!aIsTabSwitch && browser.isSyntheticDocument)` → `this._notifyOnLocationChange()`
- 条件付き依存: `if (this._isPDFViewer(browser))` → `this._applyPrefToZoom()`
- 条件付き依存: `if (this._isPDFViewer(browser))` → `this._notifyOnLocationChange.bind()`
- 条件付き依存: `if (pref)` → `this._applyPrefToZoom()`
- 条件付き依存: `if (pref)` → `this._notifyOnLocationChange.bind()`
- 参照: `aURI.spec`, `browser.contentPrincipal`, `browser.contentPrincipal.isNullPrincipal`, `browser.isSyntheticDocument`, `gBrowser.selectedBrowser`, `pref.value`, `this._initialLocations`, `this.name`, `this.siteSpecific`

## handleResult()
- 位置: L304-306
- 役割: 取得したサイト別 pref の値を保持する。
- 触るとき: 非同期取得した pref の値の扱いを調べるとき。
- 参照: `resultPref.value`

## handleCompletion()
- 位置: L307-317
- 役割: トークンが有効なら取得値をズームに適用し、完了を通知する。
- 触るとき: 非同期 pref 取得完了後の適用を調べるとき。
- 呼び出し先: `this._applyPrefToZoom()`, `this._notifyOnLocationChange.bind()`
- 条件付き依存: `if (!token.isCurrent)` → `this._notifyOnLocationChange()`
- 参照: `token.isCurrent`

## FullZoom_updateCommands()
- 位置: async L334-362
- 役割: 現在のズーム値に応じて縮小・拡大・リセット・全体ズーム切替コマンドの有効状態を更新する。
- 触るとき: ズームメニュー項目の有効/無効や状態表示を調べるとき。
- 呼び出し先: `ZoomUI.getGlobalValue()`, `document.getElementById()`, `fullZoomCmd.toggleAttribute()`
- 条件付き依存: `if (zoomLevel == ZoomManager.MIN)` → `reduceCmd.setAttribute()`
- 条件付き依存: `if (!(zoomLevel == ZoomManager.MIN))` → `reduceCmd.removeAttribute()`
- 条件付き依存: `if (zoomLevel == ZoomManager.MAX)` → `enlargeCmd.setAttribute()`
- 条件付き依存: `if (!(zoomLevel == ZoomManager.MAX))` → `enlargeCmd.removeAttribute()`
- 条件付き依存: `if (zoomLevel == defaultZoomLevel && !forceResetEnabled)` → `resetCmd.setAttribute()`
- 条件付き依存: `if (!(zoomLevel == defaultZoomLevel && !forceResetEnabled))` → `resetCmd.removeAttribute()`
- 参照: `ZoomManager.MAX`, `ZoomManager.MIN`, `ZoomManager.useFullZoom`, `ZoomManager.zoom`

## sendMessageToPDFViewer()
- 位置: L366-372
- 役割: PDF ビューアのアクターにメッセージを送り、失敗はログに出す。
- 触るとき: PDF ビューアのズーム連携を調べるとき。
- 呼び出し先: `browser.sendMessageToActor()`, `console.error()`

## reduce()
- 位置: async L382-392
- 役割: リーダーや PDF ならそれぞれへ縮小を依頼し、通常ページはズームを縮小して pref に保存する。
- 触るとき: 縮小操作の分岐を調べるとき。
- 呼び出し先: `aBrowser.currentURI.spec.startsWith()`
- 条件付き依存: `if (aBrowser.currentURI.spec.startsWith("about:reader"))` → `aBrowser.sendMessageToActor()`
- 条件付き依存: `if (!(aBrowser.currentURI.spec.startsWith("about:reader")))` → `this._isPDFViewer()`
- 条件付き依存: `if (this._isPDFViewer(aBrowser))` → `this.sendMessageToPDFViewer()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `ZoomManager.reduceForBrowser()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `this._ignorePendingZoomAccesses()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `this._applyZoomToPref()`
- 参照: `gBrowser.selectedBrowser`

## enlarge()
- 位置: async L402-412
- 役割: リーダーや PDF ならそれぞれへ拡大を依頼し、通常ページはズームを拡大して pref に保存する。
- 触るとき: 拡大操作の分岐を調べるとき。
- 呼び出し先: `aBrowser.currentURI.spec.startsWith()`
- 条件付き依存: `if (aBrowser.currentURI.spec.startsWith("about:reader"))` → `aBrowser.sendMessageToActor()`
- 条件付き依存: `if (!(aBrowser.currentURI.spec.startsWith("about:reader")))` → `this._isPDFViewer()`
- 条件付き依存: `if (this._isPDFViewer(aBrowser))` → `this.sendMessageToPDFViewer()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `ZoomManager.enlargeForBrowser()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `this._ignorePendingZoomAccesses()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `this._applyZoomToPref()`
- 参照: `gBrowser.selectedBrowser`

## setZoom()
- 位置: L418-425
- 役割: PDF 以外のブラウザに指定ズーム値を設定して pref に保存する。
- 触るとき: 任意のズーム値を設定する経路を調べるとき。
- 呼び出し先: `ZoomManager.setZoomForBrowser()`, `this._applyZoomToPref()`, `this._ignorePendingZoomAccesses()`, `this._isPDFViewer()`
- 参照: `gBrowser.selectedBrowser`

## FullZoom_reset()
- 位置: L433-452
- 役割: リーダーや PDF に応じたリセットを行い、通常はグローバル値へ戻してサイト別 pref を削除する。
- 触るとき: ズームリセットの挙動を調べるとき。
- 呼び出し先: `ZoomUI.getGlobalValue()`, `ZoomUI.getGlobalValue().then()`, `browser.currentURI.spec.startsWith()`, `this._getBrowserToken()`, `this._removePref()`
- 条件付き依存: `if (browser.currentURI.spec.startsWith("about:reader"))` → `browser.sendMessageToActor()`
- 条件付き依存: `if (!(browser.currentURI.spec.startsWith("about:reader")))` → `this._isPDFViewer()`
- 条件付き依存: `if (this._isPDFViewer(browser))` → `this.sendMessageToPDFViewer()`
- 条件付き依存: `if (token.isCurrent)` → `ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (token.isCurrent)` → `this._ignorePendingZoomAccesses()`
- 参照: `gBrowser.selectedBrowser`, `token.isCurrent`

## resetFromURLBar()
- 位置: L457-460
- 役割: URL バーのリセットボタンから、ズームとピンチ拡大の両方を初期化する。
- 触るとき: URL バーのズーム表示のリセット動作を調べるとき。
- 呼び出し先: `this.reset()`, `this.resetScalingZoom()`

## FullZoom_resetScaling()
- 位置: L462-466
- 役割: ブラウジングコンテキストのピンチ拡大を初期化する。
- 触るとき: ピンチ拡大のリセットを調べるとき。
- 呼び出し先: `browser.browsingContext?.resetScalingZoom()`
- 参照: `gBrowser.selectedBrowser`

## FullZoom__applyPrefToZoom()
- 位置: L491-526
- 役割: pref 値またはグローバル値をブラウザのズームに適用し、完了後にコールバックを呼ぶ。
- 触るとき: 保存値からズームを決める処理を調べるとき。
- 呼び出し先: `ZoomUI.getGlobalValue()`, `ZoomUI.getGlobalValue().then()`, `this._executeSoon()`, `this._getBrowserToken()`
- 条件付き依存: `if ( !aBrowser.mInitialized || aBrowser.isSyntheticDocument || (!this.siteSpecific && aBrowser.tabHasCustomZoom) )` → `this._executeSoon()`
- 条件付き依存: `if (aValue !== undefined && this.siteSpecific)` → `ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (aValue !== undefined && this.siteSpecific)` → `this._ensureValid()`
- 条件付き依存: `if (aValue !== undefined && this.siteSpecific)` → `this._ignorePendingZoomAccesses()`
- 条件付き依存: `if (aValue !== undefined && this.siteSpecific)` → `this._executeSoon()`
- 条件付き依存: `if (token.isCurrent)` → `ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (token.isCurrent)` → `this._ignorePendingZoomAccesses()`
- 参照: `aBrowser.isSyntheticDocument`, `aBrowser.mInitialized`, `aBrowser.tabHasCustomZoom`, `this.siteSpecific`, `token.isCurrent`

## FullZoom__applyZoomToPref()
- 位置: L534-557
- 役割: 現在のズームを content pref に保存し、サイト別無効時はタブ独自ズームとして記録する。
- 触るとき: ズーム値の保存条件を調べるとき。
- 呼び出し先: `ZoomManager.getZoomForBrowser()`, `this._cps2.set()`, `this._loadContextFromBrowser()`
- 参照: `browser.currentURI.spec`, `browser.isSyntheticDocument`, `browser.tabHasCustomZoom`, `this.name`, `this.siteSpecific`

## handleCompletion()
- 位置: L550-553
- 役割: 保存完了後に、次の pref 変更を自身によるものとして印を付けて解決する。
- 触るとき: 自身の保存が再適用されない仕組みを調べるとき。
- 呼び出し先: `resolve()`
- 参照: `this._isNextContentPrefChangeInternal`

## FullZoom__removePref()
- 位置: L564-574
- 役割: 現在ページのズームの content pref を削除する。
- 触るとき: ズーム設定の削除を調べるとき。
- 呼び出し先: `this._cps2.removeByDomainAndName()`, `this._loadContextFromBrowser()`
- 参照: `browser.currentURI.spec`, `browser.isSyntheticDocument`, `this.name`

## handleCompletion()
- 位置: L570-572
- 役割: 削除完了後に、次の pref 変更を自身によるものとして印を付ける。
- 触るとき: 自身の削除が再適用されない仕組みを調べるとき。
- 参照: `this._isNextContentPrefChangeInternal`

## FullZoom__getBrowserToken()
- 位置: L590-606
- 役割: ブラウザごとの変更番号を取り、まだ有効かを判定できるトークンを返す。
- 触るとき: 非同期処理中のズーム競合を防ぐ仕組みを調べるとき。
- 呼び出し先: `map.get()`, `map.has()`
- 条件付き依存: `if (!map.has(browser))` → `map.set()`
- 参照: `this._browserTokenMap`

## isCurrent()
- 位置: L597-604
- 役割: 番号が変わっておらずブラウザが初期化済みなら true を返す。
- 触るとき: トークンの有効判定を調べるとき。
- 呼び出し先: `map.get()`
- 参照: `browser.mInitialized`, `this.token`

## FullZoom__getTargetedBrowser()
- 位置: L614-636
- 役割: ズームイベントの発生元から対象のブラウザ要素を求め、不明なら例外を投げる。
- 触るとき: ズームイベントの対象ブラウザの決定を調べるとき。
- 呼び出し先: `window.XULElement.isInstance()`
- 参照: `Node.DOCUMENT_NODE`, `event.originalTarget`, `target.documentGlobal.docShell.chromeEventHandler`, `target.localName`, `target.namespaceURI`, `target.nodeType`

## FullZoom__ignorePendingZoomAccesses()
- 位置: L645-650
- 役割: ブラウザの変更番号を進め、保留中の非同期処理を無効にする。
- 触るとき: 古い非同期結果が適用される不具合を調べるとき。
- 呼び出し先: `map.get()`, `map.set()`
- 参照: `this._browserTokenMap`

## FullZoom__ensureValid()
- 位置: L652-668
- 役割: ズーム値を有効範囲に収め、数値でなければ 1 を返す。
- 触るとき: 不正なズーム値の補正を調べるとき。
- 呼び出し先: `isNaN()`
- 参照: `ZoomManager.MAX`, `ZoomManager.MIN`

## FullZoom__loadContextFromBrowser()
- 位置: L676-678
- 役割: ブラウザの load context を返す。
- 触るとき: プライベート判定用の context 取得を調べるとき。
- 参照: `browser.loadContext`

## FullZoom__notifyOnLocationChange()
- 位置: L686-690
- 役割: 非同期で browser-fullZoom:location-change を通知する。
- 触るとき: ズーム適用後の通知を受ける側を調べるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `this._executeSoon()`
- XPCOM: `Services.obs`

## FullZoom__executeSoon()
- 位置: L692-697
- 役割: コールバックがあればメインスレッドに投入する。
- 触るとき: 非同期コールバックの実行タイミングを調べるとき。
- 呼び出し先: `Services.tm.dispatchToMainThread()`
- XPCOM: `Services.tm`

## _isPDFViewer()
- 位置: L699-703
- 役割: コンテンツの principal が pdf.js ビューアか判定する。
- 触るとき: PDF ビューアの判定方法を調べるとき。
- 参照: `browser.contentPrincipal.spec`
