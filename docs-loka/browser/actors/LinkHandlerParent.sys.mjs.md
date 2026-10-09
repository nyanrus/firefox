# browser/actors/LinkHandlerParent.sys.mjs

source: browser/actors/LinkHandlerParent.sys.mjs
source-hash: 695fa5abf9b95720e15cca546a944baed87b9a53
lines: 272

## <module>
- 役割: 子プロセスから届いたページのアイコン情報を、タブのアイコンや検索エンジン追加として反映する親側アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## drawImageOnCanvas()
- 位置: async L22-35
- 役割: 画像データを VideoFrame に変換し、キャンバスのサイズに合わせて描画する。
- 触るとき: アイコン画像の変換で画質やサイズが崩れるとき。
- 呼び出し先: `canvas.getContext()`, `ctx.drawImage()`, `image.blob.bytes()`
- 参照: `canvas.height`, `canvas.width`, `frame.displayHeight`, `frame.displayWidth`, `image.displayHeight`, `image.displayWidth`, `image.format`

## createICO()
- 位置: L39-77
- 役割: 複数の PNG を 1 つの ICO ファイルのバイト列にまとめる。各エントリの幅と高さは 0 にして PNG 側の情報に任せる。
- 触るとき: 複数サイズのファビコンを扱う処理を変えるとき。
- 呼び出し先: `images.reduce()`, `u8.set()`, `view.setUint16()`, `view.setUint32()`, `view.setUint8()`
- 参照: `image.byteLength`, `images.length`, `images[i].byteLength`

## LinkHandlerParent.addListenerForTests()
- 位置: L80-82
- 役割: テスト用の通知リスナーを登録する。
- 触るとき: テストからアイコン処理の経過を観測する方法を変えるとき。
- 呼び出し先: `gTestListeners.add()`

## LinkHandlerParent.removeListenerForTests()
- 位置: L84-86
- 役割: テスト用の通知リスナーを外す。
- 触るとき: テストの後始末を変えるとき。
- 呼び出し先: `gTestListeners.delete()`

## LinkHandlerParent.receiveMessage()
- 位置: L88-156
- 役割: 読み込み中、アイコン設定、アイコン失敗、検索追加の各メッセージを処理し、タブの表示状態を変える。テスト用リスナーにも通知する。
- 触るとき: アイコンや検索追加のメッセージの扱いを変えるとき。
- 呼び出し先: `gBrowser.getTabForBrowser()`, `lazy.OpenSearchManager.addEngine()`, `lazy.PlacesUtils.favicons .expireFaviconsForPage()`, `lazy.PlacesUtils.favicons .expireFaviconsForPage(this.manager.documentURI) .catch()`, `this.notifyTestListeners()`, `this.setIconFromLink()`
- 条件付き依存: `if (!aMsg.data.isRichIcon)` → `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (!aMsg.data.isRichIcon)` → `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("busy"))` → `tab.setAttribute()`
- 条件付き依存: `if (!aMsg.data.isRichIcon)` → `this.clearPendingIcon()`
- 参照: `aMsg.data`, `aMsg.data.engine`, `aMsg.data.isRichIcon`, `aMsg.name`, `browser.documentGlobal`, `console.error`, `this.browsingContext.top.embedderElement`, `this.manager.documentURI`, `win.gBrowser`

## LinkHandlerParent.notifyTestListeners()
- 位置: L158-162
- 役割: 登録済みのテスト用リスナーに、名前とデータを渡す。
- 触るとき: テストの観測点を増やすとき。
- 呼び出し先: `listener()`

## LinkHandlerParent.clearPendingIcon()
- 位置: L164-167
- 役割: タブの pendingicon 属性を外し、読み込み中のアイコン表示を戻す。
- 触るとき: アイコンの読み込み中表示が残る不具合を調べるとき。
- 呼び出し先: `gBrowser.getTabForBrowser()`, `tab.removeAttribute()`

## LinkHandlerParent.setIconFromLink()
- 位置: async L169-270
- 役割: 画像があれば data URL に変換し、許可されたスキームか確かめてから、サイトアイコンとして保存し、タブのアイコンを設定する。途中でタブが消えたら止める。
- 触るとき: アイコンの許可条件や保存先、タブへの設定を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `TRUSTED_FAVICON_SCHEMES.includes()`, `console.error()`, `gBrowser.getBrowserForTab()`, `gBrowser.getTabForBrowser()`, `iconURI.schemeIs()`, `iconURL.startsWith()`
- 条件付き依存: `if (images)` → `tab.ownerDocument.createElement()`
- 条件付き依存: `if (images.length > 1)` → `drawImageOnCanvas()`
- 条件付き依存: `if (images.length > 1)` → `blobs.push()`
- 条件付き依存: `if (images.length > 1)` → `canvas.toBlob()`
- 条件付き依存: `if (images.length > 1)` → `Promise.all()`
- 条件付き依存: `if (images.length > 1)` → `blobs.map()`
- 条件付き依存: `if (images.length > 1)` → `blob.bytes()`
- 条件付き依存: `if (images.length > 1)` → `createICO()`
- 条件付き依存: `if (images.length > 1)` → `blobAsDataURL()`
- 条件付き依存: `if (!(images.length > 1))` → `drawImageOnCanvas()`
- 条件付き依存: `if (!(images.length > 1))` → `canvas.toDataURL()`
- 条件付き依存: `if (!isRichIcon)` → `this.clearPendingIcon()`
- 条件付き依存: `if ( !images && !TRUSTED_FAVICON_SCHEMES.includes(iconURI.scheme) && !iconURL.startsWith(SVG_DATA_URI_PREFIX) )` → `console.error()`
- 条件付き依存: `if (!iconURI.schemeIs("data"))` → `Services.scriptSecurityManager.checkLoadURIWithPrincipal()`
- 条件付き依存: `if (canStoreIcon)` → `lazy.PlacesUtils.favicons .setFaviconForPage()`
- 条件付き依存: `if (canStoreIcon)` → `Services.io.newURI()`
- 条件付き依存: `if (canStoreIcon)` → `lazy.PlacesUtils.toPRTime()`
- 条件付き依存: `if (canStoreIcon)` → `console.error()`
- 条件付き依存: `if (!isRichIcon)` → `gBrowser.setIcon()`
- 参照: `Services.scriptSecurityManager.ALLOW_CHROME`, `browser.contentPrincipal`, `console.error`, `iconURI.scheme`, `images.length`, `this.manager.documentURI`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`
