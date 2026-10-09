# browser/components/AccountsGlue.sys.mjs

source: browser/components/AccountsGlue.sys.mjs
source-hash: fe44c8924c1ba510091ef875787b1d5f2341efc5
lines: 490

## <module>
- 役割: Mozilla アカウントと Sync の起動時イベント(端末接続、受信タブ、遠隔のタブ閉じ、バッジ)を扱う AccountsGlue を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Components.Constructor()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## init()
- 位置: L66-77
- 役割: fxaccounts 系、sync-ui-state:update、idle-daily の通知を Services.obs で監視登録する。
- 触るとき: アカウント関連の通知がどの処理に届くかを確かめるとき、または新しい通知を扱うときに見る。
- 呼び出し先: `os.addObserver()`
- 参照: `Services.obs`
- XPCOM: `Services.obs`

## observe()
- 位置: L79-134
- 役割: 通知の種類ごとに、端末接続・切断、受信タブ、タブのクローズ、バッジ更新、テスト用のアラートの差し替え、日次の client info ping を振り分ける。
- 触るとき: アカウント関連の通知に応じた処理が出ない、または二重に出るときに見る。
- 呼び出し先: `JSON.parse()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.UIState.get()`, `this._onDeviceConnected()`, `this._onDisplaySyncURIs()`, `this._onIncomingCloseTabCommand()`, `this._onThisDeviceConnected()`, `this._updateFxaBadges()`
- 条件付き依存: `if (data.isLocalDevice)` → `this._onDeviceDisconnected()`
- 条件付き依存: `if (lazy.CLIENT_ASSOCIATION_PING_ENABLED)` → `lazy.UIState.get()`
- 条件付き依存: `if (fxaState.status == lazy.UIState.STATUS_SIGNED_IN)` → `Glean.clientAssociation.uid.set()`
- 条件付き依存: `if (fxaState.status == lazy.UIState.STATUS_SIGNED_IN)` → `Glean.clientAssociation.legacyClientId.set()`
- 条件付き依存: `if (fxaState.status == lazy.UIState.STATUS_SIGNED_IN)` → `lazy.ClientID.getCachedClientID()`
- 条件付き依存: `if (data == "mock-alerts-service")` → `Object.defineProperty()`
- 条件付き依存: `if ( lazy.CLIENT_INFO_PING_ENABLED && lazy.UIState.get().status == lazy.UIState.STATUS_SIGNED_IN )` → `GleanPings.fxAccountsClientInfo.submit()`
- 参照: `data.isLocalDevice`, `fxaState.status`, `fxaState.uid`, `lazy.CLIENT_ASSOCIATION_PING_ENABLED`, `lazy.CLIENT_INFO_PING_ENABLED`, `lazy.UIState.STATUS_SIGNED_IN`, `lazy.UIState.get().status`, `subject.wrappedJSObject`

## _onThisDeviceConnected()
- 位置: L136-154
- 役割: このデバイスがアカウントに接続されたとき、通知を出す。クリックで Sync の設定画面を開く。
- 触るとき: 接続完了の通知の文言や、クリック時の遷移先を変えるときに見る。
- 呼び出し先: `lazy.AlertsService.showAlert()`, `lazy.accountsL10n.formatValuesSync()`

## clickCallback()
- 位置: L142-147
- 役割: アラートがクリックされたら、Sync の設定画面を開く。
- 触るとき: 接続完了通知を押しても設定が開かないときに見る。
- 呼び出し先: `this._openPreferences()`

## _openURLInNewWindow()
- 位置: L156-181
- 役割: 新しいブラウザウィンドウを開き、その load を待って返す。private が真ならプライベートで開く。
- 触るとき: 受信タブを開く先のウィンドウが作られない、またはプライベートで開かないときに見る。
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`, `Services.ww.openWindow()`, `resolve()`, `win.addEventListener()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsISupportsString`, `urlString.data`
- XPCOM: [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1` / `Services.ww`

## _onDisplaySyncURIs()
- 位置: async L191-296
- 役割: Sync から届いた URI を、個人用またはプライベート用のウィンドウのタブとして開き、件数と送信元に応じた通知を出す。通知をクリックすると最初のタブを前面にする。
- 触るとき: 受信タブの通知の文言や、開くタブの扱いを変えるとき、または受信タブが開かないときに見る。
- 呼び出し先: `Promise.all()`, `URIs.slice()`, `URIs.slice(1).map()`, `console.error()`, `lazy.AlertsService.showAlert()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.accountsL10n.formatValue()`, `openTab()`
- 条件付き依存: `if (URIs.length == 1)` → `URIs[0].uri.replace()`
- 条件付き依存: `if (URIs.length == 1)` → `lazy.BrowserUIUtils.trimURL()`
- 条件付き依存: `if (wasTruncated)` → `lazy.accountsL10n.formatValue()`
- 条件付き依存: `if (!(URIs.length == 1))` → `URIs.every()`
- 条件付き依存: `if (!(URIs.length == 1))` → `lazy.accountsL10n.formatValue()`
- 参照: `URI.sender`, `URI.sender.id`, `URIs.length`, `URIs[0].sender`, `URIs[0].sender.id`, `URIs[0].sender.name`, `URIs[0].uri.length`, `data.wrappedJSObject.object`, `titleL10nId.args`, `titleL10nId.id`, `url.length`

## openTab()
- 位置: async L204-222
- 役割: URI に対応するウィンドウがあればそこに Web タブを追加し、無ければ新しいウィンドウを開く。どちらの場合も attention を立てる。
- 触るとき: 受信タブが別のウィンドウに開く、または注目表示が付かないときに見る。
- 条件付き依存: `if (!win)` → `this._openURLInNewWindow()`
- 条件付き依存: `if (!(!win))` → `win.gBrowser.addWebTab()`
- 参照: `URI.private`, `URI.uri`, `tab.attention`, `tabs.length`, `win.gBrowser.tabs`

## clickCallback()
- 位置: L278-285
- 役割: 受信タブ通知がクリックされたら、最初のタブのウィンドウを前面にしてそのタブを選択する。
- 触るとき: 受信タブ通知を押しても正しいタブが選ばれないときに見る。
- 条件付き依存: `if (obsTopic == "alertclickcallback")` → `firstTab.documentGlobal.window.focus()`
- 参照: `firstTab.documentGlobal.gBrowser.selectedTab`

## _onIncomingCloseTabCommand()
- 位置: async L298-382
- 役割: Sync から届いた URL を各ウィンドウで閉じ、閉じた件数を累積して通知する。通知をクリックすると最近閉じたタブを開く。
- 触るとき: 遠隔からのタブ閉じ命令が効かない、または件数の表示がずれるときに見る。
- 呼び出し先: `Services.io.newURI()`, `closeTabsInWindows()`, `console.error()`, `lazy.AlertsService.showAlert()`, `lazy.accountsL10n.formatValues()`, `urisToClose.push()`, `urls.forEach()`
- 参照: `data.wrappedJSObject.object`, `lazy.BrowserWindowTracker.orderedWindows`, `lazy.CloseRemoteTab.closeTabNotificationCount`, `lazy.CloseRemoteTab.hasPendingCloseTabNotification`
- XPCOM: `Services.io`

## closeTabsInWindows()
- 位置: async L316-328
- 役割: 全ウィンドウを順に見て、URI に一致するタブを closeTabsByURI で閉じ、閉じた数を totalClosedTabs に足す。
- 触るとき: 一部のウィンドウだけタブが閉じない、またはエラーが記録されるときに見る。(要確認: 内部で this.log.error を呼ぶが、AccountsGlue には log が無く、this も関数の中では AccountsGlue を指さないため、この経路ではエラー処理そのものが例外になる可能性がある。)
- 呼び出し先: `this.log.error()`, `win.gBrowser.closeTabsByURI()`
- 参照: `win.gBrowser`

## clickCallback()
- 位置: async L332-356
- 役割: 通知の表示・終了の段階に応じて hasPendingCloseTabNotification を更新し、クリックされたら最近閉じたタブ画面を開く。
- 触るとき: 閉じたタブの通知が残り続ける、またはクリックで最近閉じたタブが開かないときに見る。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (win)` → `win.FirefoxViewHandler.openTab()`
- 参照: `lazy.CloseRemoteTab.hasPendingCloseTabNotification`

## _onDeviceConnected()
- 位置: L384-417
- 役割: 新しい Sync 端末の接続を通知する。端末名の有無で文言を変え、クリックでデバイス管理画面を開く。
- 触るとき: 端末接続の通知文言や、管理画面の URL を変えるときに見る。
- 呼び出し先: `console.error()`, `lazy.AlertsService.showAlert()`, `lazy.accountsL10n.formatValuesSync()`

## clickCallback()
- 位置: async L392-405
- 役割: 端末接続通知がクリックされたら、デバイス管理の URI を取得し、ウィンドウがあれば新しいタブで、無ければ新しいウィンドウで開く。
- 触るとき: 端末接続通知から管理画面が開かないときに見る。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.FxAccounts.config.promiseManageDevicesURI()`
- 条件付き依存: `if (!win)` → `this._openURLInNewWindow()`
- 条件付き依存: `if (!(!win))` → `win.gBrowser.addWebTab()`

## _onDeviceDisconnected()
- 位置: L419-438
- 役割: このデバイスが切断されたことを通知する。クリックで Sync の設定画面を開く。
- 触るとき: 切断通知の文言や、クリックの遷移先を変えるときに見る。
- 呼び出し先: `lazy.AlertsService.showAlert()`, `lazy.accountsL10n.formatValuesSync()`

## clickCallback()
- 位置: L425-430
- 役割: 切断通知がクリックされたら Sync の設定画面を開く。
- 触るとき: 切断通知から設定画面が開かないときに見る。
- 呼び出し先: `this._openPreferences()`

## _updateFxaBadges()
- 位置: L440-467
- 役割: FxA の状態が未検証またはログイン失敗のとき、ツールバーのボタンに表示するか、アプリメニューのバッジを出す。それ以外では両方を消す。
- 触るとき: アカウントのエラー表示が出ない、または消えないときに見る。
- 呼び出し先: `fxaButton?.querySelector()`, `lazy.UIState.get()`, `win.document.getElementById()`
- 条件付き依存: `if ( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED )` → `win.document.getElementById()`
- 条件付き依存: `if ( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED )` → `navToolbox.contains()`
- 条件付き依存: `if (isFxAButtonShown)` → `fxaButton?.setAttribute()`
- 条件付き依存: `if (isFxAButtonShown)` → `badge?.classList.add()`
- 条件付き依存: `if (!(isFxAButtonShown))` → `lazy.AppMenuNotifications.showBadgeOnlyNotification()`
- 条件付き依存: `if (!( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED ))` → `fxaButton?.removeAttribute()`
- 条件付き依存: `if (!( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED ))` → `badge?.classList.remove()`
- 条件付き依存: `if (!( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED ))` → `lazy.AppMenuNotifications.removeNotification()`
- 参照: `lazy.UIState.STATUS_LOGIN_FAILED`, `lazy.UIState.STATUS_NOT_VERIFIED`, `state.status`

## _openPreferences()
- 位置: async L470-488
- 役割: 最上位のウィンドウがなければ(macOS 以外は)新しいウィンドウを開き、設定画面を開く。macOS でウィンドウが無ければ hiddenDOMWindow を使う。
- 触るとき: ウィンドウが無い状態で Sync の設定が開かないときに見る。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!chromeWindow && AppConstants.platform !== "macosx")` → `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (chromeWindow)` → `chromeWindow.openPreferences()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `Services.appShell.hiddenDOMWindow.openPreferences()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.appShell`
