# browser/base/content/webext-panels.js

source: browser/base/content/webext-panels.js
source-hash: 2b0b40a636f352bcb131e0030d0aef53f2784744
lines: 212

## <module>
- 役割: webext-panels.xhtml のスクリプト。拡張機能のサイドバーやパネル用の browser 要素を作成・読み込みし、タブ用 gBrowser のスタブを提供する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## getBrowser()
- 位置: L19-145
- 役割: webext-panels-browser が無ければ作成して返す。サイドバーならヘッダーを設定し、remote なら XULFrameLoaderCreated を待ってから初期化する。
- 触るとき: 拡張のパネルを表示する際の browser 生成が失敗する、ズームや閉じる挙動がずれる、リモートプロセスの割り当てを変えるときに見る。
- 呼び出し先: `browser.addEventListener()`, `browser.setAttribute()`, `document.createXULElement()`, `document.getElementById()`, `event.stopPropagation()`, `readyPromise.then()`, `stack.appendChild()`
- 条件付き依存: `if (browser)` → `Promise.resolve()`
- 条件付き依存: `if (panel.viewType === "sidebar" && gSidebarRevampEnabled)` → `customElements.get()`
- 条件付き依存: `if (!customElements.get("sidebar-panel-header"))` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (panel.viewType === "sidebar" && gSidebarRevampEnabled)` → `document.getElementById()`
- 条件付き依存: `if (!stack)` → `document.createXULElement()`
- 条件付き依存: `if (!stack)` → `stack.setAttribute()`
- 条件付き依存: `if (!stack)` → `document.documentElement.appendChild()`
- 条件付き依存: `if (gAllowTransparentBrowser)` → `browser.setAttribute()`
- 条件付き依存: `if (panel.extension.remote)` → `browser.setAttribute()`
- 条件付き依存: `if (panel.extension.remote)` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (panel.extension.remote)` → `promiseEvent()`
- 条件付き依存: `if (!(panel.extension.remote))` → `Promise.resolve()`
- 条件付き依存: `if (panel.viewType == "sidebar")` → `windowRoot.window.SidebarController.hide()`
- 参照: `ZoomManager.MAX`, `ZoomManager.MIN`, `browser.documentGlobal`, `browser.fullZoom`, `document.getElementById("sidebar-panel-header").heading`, `panel.extension.manifest.sidebar_action.default_title`, `panel.extension.name`, `panel.extension.policy.browsingContextGroupId`, `panel.extension.remote`, `panel.uri`, `panel.viewType`

## initBrowser()
- 位置: L122-141
- 役割: 拡張 API に extension-browser-inserted を通知し、コンテンツ側のフレームスクリプトを読み込み、Extension:InitBrowser を送る。
- 触るとき: パネル内の拡張コンテンツに API が届かない、スタイルシートが適用されないときに見る。プロセスが切り替わって再初期化される経路を変えるときも見る。
- 呼び出し先: `ExtensionParent.apiManager.emit()`, `browser.messageManager.loadFrameScript()`, `browser.messageManager.sendAsyncMessage()`
- 参照: `options.stylesheets`, `panel.browserInsertedData`, `panel.browserStyle`

## selectedBrowser()
- 位置: L150-152
- 役割: gBrowser スタブの getter。webext-panels-browser 要素を返す。
- 触るとき: パネル内のリンクや拡張コードが gBrowser.selectedBrowser を参照して失敗するときに見る。
- 呼び出し先: `document.getElementById()`

## getTabForBrowser()
- 位置: L154-156
- 役割: gBrowser スタブのメソッド。常に null を返し、パネルの browser がタブに属さないことを示す。
- 触るとき: リンクを新しいタブで開く処理が呼び出し元で null をどう扱うかを確認するとき、またはパネルを通常のタブ扱いにするときに見る。

## updatePosition()
- 位置: L159-170
- 役割: 次のフレームの後に webext-panels-browser がリモートなら frameLoader の位置更新を要求する。
- 触るとき: サイドバーのリサイズや表示切り替えで、リモート browser の描画位置がずれるときに見る。
- 呼び出し先: `document.getElementById()`, `requestAnimationFrame()`, `setTimeout()`
- 条件付き依存: `if (browser && browser.isRemoteBrowser)` → `browser.frameLoader.requestUpdatePosition()`
- 参照: `browser.isRemoteBrowser`

## loadPanel()
- 位置: L172-197
- 役割: 拡張 ID から WebExtensionPolicy を引き、URL が同じでなければ既存の browser を削除して新しい URL を読み込む。
- 触るとき: サイドバー拡張を切り替えたときに古い接続が残る、同じ URL を二重に読み込むといった問題を調べるときに見る。
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`, `WebExtensionPolicy.getByID()`, `browser.fixupAndLoadURIString()`, `document.getElementById()`, `getBrowser()`, `getBrowser(sidebar).then()`, `policy.getURL()`
- 条件付き依存: `if (browserEl)` → `browserEl.parentNode.remove()`
- 参照: `browserEl.currentURI.spec`, `policy.extension`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`
