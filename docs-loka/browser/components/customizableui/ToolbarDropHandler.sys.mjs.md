# browser/components/customizableui/ToolbarDropHandler.sys.mjs

source: browser/components/customizableui/ToolbarDropHandler.sys.mjs
source-hash: e5f6b735044557a19d9a16251304d029b3bc9a2b
lines: 158

## <module>
- 役割: ツールバーのホーム・新規タブ・新規ウィンドウボタンへのリンクのドロップを処理する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## _canDropLink()
- 位置: L20-20
- 役割: ドラッグ中のイベントがリンクとしてドロップ可能かを droppedLinkHandler に問い合わせる。
- 触るとき: どのドラッグを受け付けるかの判定を変えるとき。
- 呼び出し先: `Services.droppedLinkHandler.canDropLink()`
- XPCOM: `Services.droppedLinkHandler`

## onDragOver()
- 位置: L22-26
- 役割: ドロップ可能なリンクなら preventDefault して、ドロップを受け付ける状態にする。
- 触るとき: ツールバーボタン上でドロップカーソルが出ない不具合を調べるとき。
- 呼び出し先: `this._canDropLink()`
- 条件付き依存: `if (this._canDropLink(aEvent))` → `aEvent.preventDefault()`

## _openHomeDialog()
- 位置: async L28-58
- 役割: ホームページを置き換えるかを確認するダイアログを出し、『はい』なら HomePage.set で設定する。
- 触るとき: ホーム設定の確認文言や、確認後の保存処理を変えるとき。
- 呼び出し先: `Services.prompt.confirmEx()`, `aURL.includes()`, `lazy.FluentStrings.formatValues()`
- 条件付き依存: `if (pressedVal == 0)` → `lazy.HomePage.set(aURL).catch()`
- 条件付き依存: `if (pressedVal == 0)` → `lazy.HomePage.set()`
- 参照: `Services.prompt.STD_YES_NO_BUTTONS`, `console.error`
- XPCOM: `Services.prompt`

## onDropHomeButtonObserver()
- 位置: L60-82
- 役割: ドロップされたリンクを検証し、有効なら確認ダイアログを次のタスクで開く。URL が複数なら『|』で連結する。
- 触るとき: ホームボタンへのドロップで複数 URL をどう扱うか、または検証で弾かれる条件を調べるとき。
- 呼び出し先: `Services.droppedLinkHandler.dropLinks()`
- 条件付き依存: `if (links.length)` → `link.url.includes()`
- 条件付き依存: `if (link.url.includes("|"))` → `urls.push()`
- 条件付き依存: `if (link.url.includes("|"))` → `link.url.split()`
- 条件付き依存: `if (!(link.url.includes("|")))` → `urls.push()`
- 条件付き依存: `if (links.length)` → `Services.droppedLinkHandler.validateURIsForDrop()`
- 条件付き依存: `if (links.length)` → `win.setTimeout()`
- 条件付き依存: `if (links.length)` → `urls.join()`
- 参照: `aEvent.target.documentGlobal`, `link.url`, `links.length`, `this._openHomeDialog`
- XPCOM: `Services.droppedLinkHandler`

## onDropNewTabButtonObserver()
- 位置: async L84-118
- 役割: リンク数が browser.tabs.maxOpenBeforeWarn 以上なら確認を取り、各リンクを新しいタブで開く（Shift で tabshifted）。
- 触るとき: 新規タブボタンへのドロップ時の警告条件や開き方を変えるとき。
- 呼び出し先: `Services.droppedLinkHandler.dropLinks()`, `Services.droppedLinkHandler.getPolicyContainer()`, `Services.droppedLinkHandler.getTriggeringPrincipal()`, `Services.prefs.getIntPref()`
- 条件付き依存: `if ( links.length >= Services.prefs.getIntPref("browser.tabs.maxOpenBeforeWarn") )` → `lazy.OpenInTabsUtils.promiseConfirmOpenInTabs()`
- 条件付き依存: `if (link.url)` → `lazy.UrlbarUtils.getShortcutOrURIAndPostData()`
- 条件付き依存: `if (link.url)` → `lazy.URILoadingHelper.openLinkIn()`
- 参照: `aEvent.shiftKey`, `aEvent.target.documentGlobal`, `data.postData`, `data.url`, `link.url`, `links.length`
- XPCOM: `Services.droppedLinkHandler` / `Services.prefs`

## onDropNewWindowButtonObserver()
- 位置: async L120-156
- 役割: 同様に確認したうえで、各リンクを新しいウィンドウで開く。allowInheritPrincipal を true にしている。
- 触るとき: 新規ウィンドウへのドロップ挙動や、javascript: リンクの扱い（Bug 1475201 の TODO）を調べるとき。
- 呼び出し先: `Services.droppedLinkHandler.dropLinks()`, `Services.droppedLinkHandler.getPolicyContainer()`, `Services.droppedLinkHandler.getTriggeringPrincipal()`, `Services.prefs.getIntPref()`
- 条件付き依存: `if ( links.length >= Services.prefs.getIntPref("browser.tabs.maxOpenBeforeWarn") )` → `lazy.OpenInTabsUtils.promiseConfirmOpenInTabs()`
- 条件付き依存: `if (link.url)` → `lazy.UrlbarUtils.getShortcutOrURIAndPostData()`
- 条件付き依存: `if (link.url)` → `lazy.URILoadingHelper.openLinkIn()`
- 参照: `aEvent.target.documentGlobal`, `data.postData`, `data.url`, `link.url`, `links.length`
- XPCOM: `Services.droppedLinkHandler` / `Services.prefs`
