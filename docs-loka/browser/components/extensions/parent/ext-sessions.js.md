# browser/components/extensions/parent/ext-sessions.js

source: browser/components/extensions/parent/ext-sessions.js
source-hash: 408fa09b5ba55612f09f70324115e2825781a077
lines: 301

## <module>
- 役割: sessions WebExtension API の実装。閉じたタブとウィンドウの一覧、復元、拡張ごとのタブ・ウィンドウ値の保存を SessionStore に委ねる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getRecentlyClosed()
- 位置: L17-49
- 役割: 閉じたウィンドウと、アクセス可能なウィンドウの閉じたタブを集め、閉じた時刻の新しい順に maxResults 件まで返す。
- 触るとき: sessions.getRecentlyClosed の件数や並びがおかしいとき。プライベートウィンドウのタブは、そのウィンドウが開いている間だけ含まれる。
- 呼び出し先: `SessionStore.getClosedTabDataForWindow()`, `SessionStore.getClosedWindowData()`, `Tab.convertFromSessionStoreClosedData()`, `Window.convertFromSessionStoreClosedData()`, `extension.canAccessWindow()`, `recentlyClosed.push()`, `recentlyClosed.slice()`, `recentlyClosed.sort()`, `windowTracker.browserWindows()`
- 参照: `a.lastModified`, `b.lastModified`, `tab.closedAt`, `window.closedAt`

## createSession()
- 位置: async L51-74
- 役割: 復元されたオブジェクトを拡張用の session 形式 (window または tab) に変換する。ウィンドウは復元完了の通知を待つ。
- 触るとき: sessions.restore の戻り値が空になる、またはウィンドウの復元後に内容が欠けるときに見る。restored が無ければ例外を投げる。
- 呼び出し先: `Date.now()`, `extension.tabManager.convert()`
- 条件付き依存: `if (restored.isChromeWindow)` → `promiseObserved()`
- 条件付き依存: `if (restored.isChromeWindow)` → `extension.windowManager.convert()`
- 参照: `restored.isChromeWindow`, `sessionObj.tab`, `sessionObj.window`

## getEncodedKey()
- 位置: L76-86
- 役割: 拡張 ID とキーから sessionstore 用の 'extension:ID:key' 形式の文字列を作る。
- 触るとき: 拡張のカスタム値のキー形式を変えるとき、または保存キーの衝突を調べるとき。一時アドオン ID では例外になる。
- 呼び出し先: `AddonManagerPrivate.isTemporaryInstallID()`

## onChanged()
- 位置: L90-104
- 役割: sessionstore-closed-objects-changed を監視し、閉じたオブジェクトの一覧が変わったことを通知する。
- 触るとき: sessions.onChanged が発火しない、または閉じた項目が変わっても通知されないときに見る。
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## observer()
- 位置: L91-93
- 役割: sessionstore の変更通知を受けて fire.async() を呼ぶ。
- 触るとき: onChanged の通知が二重に出るときなど、通知の発火条件を確認するとき。
- 呼び出し先: `fire.async()`

## unregister()
- 位置: L97-99
- 役割: onChanged の sessionstore 変更オブザーバーを外す。
- 触るとき: 拡張の無効化後も onChanged が届くときに解除を確認する。
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## convert()
- 位置: L100-102
- 役割: 永続イベントの再接続時に onChanged の fire を差し替える。
- 触るとき: 再起動後に onChanged が古い fire へ送られるときに見る。

## getAPI()
- 位置: L107-299
- 役割: sessions API のオブジェクトを組み立て、閉じた項目の操作、復元、タブ・ウィンドウのカスタム値、onChanged を返す。
- 触るとき: 拡張から見える sessions API を増減するとき。
- 呼び出し先: `new EventManager({ context, module: "sessions", event: "onChanged", extensionApi: this, }).api()`

## getTabParams()
- 位置: L110-117
- 役割: キーを暗号化済みの形式にし、タブ ID からタブを引く。タブのウィンドウへアクセスできなければ例外を投げる。
- 触るとき: setTabValue や getTabValue などでタブ ID が無効扱いになるとき。
- 呼び出し先: `context.canAccessWindow()`, `getEncodedKey()`, `tabTracker.getTab()`
- 参照: `extension.id`, `tab.documentGlobal`

## getWindowParams()
- 位置: L119-123
- 役割: キーを暗号化済みの形式にし、ウィンドウ ID から対象ウィンドウを引く。
- 触るとき: setWindowValue や getWindowValue などでウィンドウ ID の解決に失敗するとき。
- 呼び出し先: `getEncodedKey()`, `windowTracker.getWindow()`
- 参照: `extension.id`

## getClosedIdFromSessionId()
- 位置: L125-133
- 役割: 文字列の sessionId を整数の closedId に変換する。整数でなければ例外を投げる。
- 触るとき: sessionId の形式を変えるとき、または forgetClosedTab や restore が Invalid sessionId を返すとき。
- 呼び出し先: `Number.isInteger()`, `parseInt()`

## getRecentlyClosed()
- 位置: async L137-142
- 役割: SessionStore の初期化を待ってから、maxResults (省略時は無限) を渡して getRecentlyClosed を呼ぶ。
- 触るとき: sessions.getRecentlyClosed の件数上限を変えるとき。TODO として MAX_SESSION_RESULTS への上限付けが残っている (bug 1764376)。
- 呼び出し先: `getRecentlyClosed()`
- 参照: `SessionStore.promiseInitialized`, `filter.maxResults`

## forgetClosedTab()
- 位置: async L144-159
- 役割: 指定ウィンドウの閉じたタブ一覧に sessionId があれば、SessionStore からその閉じたタブを忘れさせる。無ければ例外を投げる。
- 触るとき: sessions.forgetClosedTab が『Could not find closed tab』を返すとき。対象の探索は指定ウィンドウの閉じたタブ一覧に限られる。
- 呼び出し先: `SessionStore.forgetClosedTabById()`, `SessionStore.getClosedTabDataForWindow()`, `closedTabData.some()`, `getClosedIdFromSessionId()`, `windowTracker.getWindow()`
- 参照: `SessionStore.promiseInitialized`, `closedTab.closedId`

## forgetClosedWindow()
- 位置: async L161-176
- 役割: 閉じたウィンドウ一覧から sessionId の位置を探し、SessionStore からそのウィンドウを忘れさせる。無ければ例外を投げる。
- 触るとき: sessions.forgetClosedWindow で対象が消えない、または見つからないと判定されるときに見る。
- 呼び出し先: `SessionStore.forgetClosedWindow()`, `SessionStore.getClosedWindowData()`, `closedWindowData.findIndex()`, `getClosedIdFromSessionId()`
- 参照: `SessionStore.promiseInitialized`, `closedWindow.closedId`

## restore()
- 位置: async L178-235
- 役割: sessionId があればその閉じた項目を復元し、無ければ最後に閉じたウィンドウまたは最新の閉じたタブを復元する。結果を createSession で変換する。
- 触るとき: sessions.restore の対象の選び方や、タブをどのウィンドウに戻すかを変えるとき。引数なしで最後に閉じたのがタブでも、閉じたタブの closedId を使って復元する。
- 呼び出し先: `createSession()`
- 条件付き依存: `if (sessionId)` → `getClosedIdFromSessionId()`
- 条件付き依存: `if (closedId !== undefined)` → `SessionStore.getObjectTypeForClosedId()`
- 条件付き依存: `if (SessionStore.getObjectTypeForClosedId(closedId) == "tab")` → `SessionStore.getWindowForTabClosedId()`
- 条件付き依存: `if (closedId !== undefined)` → `SessionStore.undoCloseById()`
- 条件付き依存: `if (SessionStore.lastClosedObjectType == "window")` → `SessionStore.undoCloseWindow()`
- 条件付き依存: `if (!(SessionStore.lastClosedObjectType == "window"))` → `windowTracker.browserWindows()`
- 条件付き依存: `if (!(SessionStore.lastClosedObjectType == "window"))` → `SessionStore.getClosedTabDataForWindow()`
- 条件付き依存: `if (!(SessionStore.lastClosedObjectType == "window"))` → `recentlyClosedTabs.push()`
- 条件付き依存: `if (recentlyClosedTabs.length)` → `recentlyClosedTabs.sort()`
- 条件付き依存: `if (recentlyClosedTabs.length)` → `SessionStore.getWindowForTabClosedId()`
- 条件付き依存: `if (recentlyClosedTabs.length)` → `SessionStore.undoCloseById()`
- 参照: `SessionStore.lastClosedObjectType`, `SessionStore.promiseInitialized`, `a.closedAt`, `b.closedAt`, `extension.privateBrowsingAllowed`, `recentlyClosedTabs.length`, `recentlyClosedTabs[0].closedId`

## setTabValue()
- 位置: L237-245
- 役割: タブに拡張のカスタム値を JSON 文字列として保存する。
- 触るとき: sessions.setTabValue で値が保存されない、または JSON に変換できない値を渡したときに見る。
- 呼び出し先: `JSON.stringify()`, `SessionStore.setCustomTabValue()`, `getTabParams()`

## getTabValue()
- 位置: async L247-256
- 役割: タブに保存されたカスタム値を読み出して JSON として戻す。無ければ undefined を返す。
- 触るとき: 保存した値が取り出せないとき。保存値が空文字の場合は undefined になる。
- 呼び出し先: `SessionStore.getCustomTabValue()`, `getTabParams()`
- 条件付き依存: `if (value)` → `JSON.parse()`

## removeTabValue()
- 位置: L258-262
- 役割: タブのカスタム値を削除する。
- 触るとき: sessions.removeTabValue が効かないときに見る。
- 呼び出し先: `SessionStore.deleteCustomTabValue()`, `getTabParams()`

## setWindowValue()
- 位置: L264-272
- 役割: ウィンドウに拡張のカスタム値を JSON 文字列として保存する。
- 触るとき: sessions.setWindowValue で値が保存されない、または JSON に変換できない値を渡したときに見る。
- 呼び出し先: `JSON.stringify()`, `SessionStore.setCustomWindowValue()`, `getWindowParams()`

## getWindowValue()
- 位置: async L274-283
- 役割: ウィンドウに保存されたカスタム値を読み出して JSON として戻す。無ければ undefined を返す。
- 触るとき: 保存したウィンドウ値が取り出せないとき。
- 呼び出し先: `SessionStore.getCustomWindowValue()`, `getWindowParams()`
- 条件付き依存: `if (value)` → `JSON.parse()`

## removeWindowValue()
- 位置: L285-289
- 役割: ウィンドウのカスタム値を削除する。
- 触るとき: sessions.removeWindowValue が効かないときに見る。
- 呼び出し先: `SessionStore.deleteCustomWindowValue()`, `getWindowParams()`
