# browser/actors/AboutReaderParent.sys.mjs

source: browser/actors/AboutReaderParent.sys.mjs
source-hash: 4a7bac56a273dbb6efcab7e9763768d63879da11
lines: 261

## <module>
- 役割: リーダーモードの親側アクター。記事データの一時キャッシュ、リーダー切り替えの履歴遷移、ツールバーのリーダーボタン更新、リスナーへのメッセージ中継を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutReaderParent.didDestroy()
- 位置: L27-35
- 役割: アクター一覧から外し、リーダー画面なら対応する記事キャッシュを削除する。
- 触るとき: リーダー画面を閉じた後にキャッシュや一覧に古い項目が残る問題を調べるときに見る。
- 呼び出し先: `gAllActors.delete()`, `this.isReaderMode()`
- 条件付き依存: `if (this.isReaderMode())` → `decodeURIComponent()`
- 条件付き依存: `if (this.isReaderMode())` → `url.substr()`
- 条件付き依存: `if (this.isReaderMode())` → `gCachedArticles.delete()`
- 参照: `"about:reader?url=".length`, `this.manager.documentURI.spec`

## AboutReaderParent.isReaderMode()
- 位置: L37-39
- 役割: 管理対象の文書 URI が about:reader で始まるかを返す。
- 触るとき: リーダー画面かどうかの判定を使う箇所を変えるときに見る。
- 呼び出し先: `this.manager.documentURI.spec.startsWith()`

## AboutReaderParent.addMessageListener()
- 位置: L41-47
- 役割: 指定したメッセージ名のリスナー集合へ、リスナーを追加する。
- 触るとき: リーダーの外部リスナーの登録経路を追うときに見る。
- 呼び出し先: `gListeners.has()`
- 条件付き依存: `if (!gListeners.has(name))` → `gListeners.set()`
- 条件付き依存: `if (!(!gListeners.has(name)))` → `gListeners.get(name).add()`
- 条件付き依存: `if (!(!gListeners.has(name)))` → `gListeners.get()`

## AboutReaderParent.removeMessageListener()
- 位置: L49-55
- 役割: 指定したメッセージ名のリスナー集合から、リスナーを取り除く。
- 触るとき: リスナーが解除されず呼ばれ続ける問題を調べるときに見る。
- 呼び出し先: `gListeners.get()`, `gListeners.get(name).delete()`, `gListeners.has()`

## AboutReaderParent.broadcastAsyncMessage()
- 位置: L57-64
- 役割: 管理中の全 AboutReader actor にメッセージを送り、送信失敗は無視する。
- 触るとき: 全リーダー画面へ一斉に通知を送る処理を変えるときに見る。
- 呼び出し先: `actor.sendAsyncMessage()`

## AboutReaderParent.callListeners()
- 位置: L66-80
- 役割: メッセージ名に登録されたリスナーへ、対象タブ付きでメッセージを渡す。例外は console に出して続ける。
- 触るとき: リーダーのメッセージを購読している側（ReaderMode など）の動作を確かめるときに見る。
- 呼び出し先: `console.error()`, `gListeners.get()`, `listener.receiveMessage()`, `listeners.values()`
- 参照: `message.name`, `message.target`, `this.browsingContext.embedderElement`

## AboutReaderParent.receiveMessage()
- 位置: async L82-147
- 役割: 子からの EnterReaderMode、GetCachedArticle、FaviconRequest、UpdateReaderButton などを処理し、記事キャッシュや遷移を行う。
- 触るとき: リーダーモードの入退場や記事データの受け渡しを変えるときに見る。
- 呼び出し先: `Services.io.newURI()`, `console.error()`, `gCachedArticles.delete()`, `gCachedArticles.get()`, `gCachedArticles.set()`, `lazy.PlacesUtils.favicons.getFaviconForPage()`, `this.callListeners()`, `this.enterReaderMode()`, `this.leaveReaderMode()`, `this.updateReaderButton()`
- 参照: `browser.isArticle`, `message.data`, `message.data.article`, `message.data.isArticle`, `message.data.newURL`, `message.data.preferredWidth`, `message.data.url`, `message.name`, `result.uri.spec`, `this.browsingContext.embedderElement`, `uri.spec`
- XPCOM: `Services.io`

## AboutReaderParent.onLocationChange()
- 位置: L149-155
- 役割: ロケーション変更時に、そのブラウザのリーダーボタンを更新する。
- 触るとき: ページ遷移時にリーダーボタンの表示が古いままになる問題を調べるときに見る。
- 呼び出し先: `AboutReaderParent.updateReaderButton()`
- 参照: `webProgress.browsingContext.embedderElement`

## AboutReaderParent.updateReaderButton()
- 位置: L157-161
- 役割: ブラウザの子アクターに、リーダーボタン更新を依頼する静的な入口。
- 触るとき: ボタン更新をどの経路で呼ぶかを追うときに見る。
- 呼び出し先: `actor.updateReaderButton()`, `windowGlobal.getActor()`
- 参照: `browser.browsingContext.currentWindowGlobal`

## AboutReaderParent.updateReaderButton()
- 位置: L163-204
- 役割: 選択中のタブならリーダー画面かどうかに応じてボタン・メニュー・キーの表示を切り替え、必要なら通知を出す。
- 触るとき: リーダーボタンやメニュー項目の表示条件、ローカライズ属性を変えるときに見る。
- 呼び出し先: `browser.getTabBrowser()`, `doc.getElementById()`, `this.isReaderMode()`
- 条件付き依存: `if (this.isReaderMode())` → `gAllActors.add()`
- 条件付き依存: `if (this.isReaderMode())` → `button.setAttribute()`
- 条件付き依存: `if (this.isReaderMode())` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (this.isReaderMode())` → `key.removeAttribute()`
- 条件付き依存: `if (this.isReaderMode())` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(this.isReaderMode()))` → `button.removeAttribute()`
- 条件付き依存: `if (!(this.isReaderMode()))` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(this.isReaderMode()))` → `key.toggleAttribute()`
- 条件付き依存: `if (browser.isArticle)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!button.hidden)` → `lazy.PageActions.sendPlacedInUrlbarTrigger()`
- 参照: `browser.documentGlobal.document`, `browser.isArticle`, `button.hidden`, `menuitem.hidden`, `tabBrowser.selectedBrowser`
- XPCOM: `Services.obs`

## AboutReaderParent.forceShowReaderIcon()
- 位置: L206-209
- 役割: ブラウザを記事扱いにして、リーダーボタンを強制的に表示する。
- 触るとき: 記事判定に関係なくリーダーアイコンを出す条件を変えるときに見る。
- 呼び出し先: `AboutReaderParent.updateReaderButton()`
- 参照: `browser.isArticle`

## AboutReaderParent.toggleReaderMode()
- 位置: L211-225
- 役割: 選択中ブラウザの AboutReader actor に、リーダーの切り替え要求を送る。
- 触るとき: リーダーボタンやショートカットからの切り替え経路を変えるときに見る。要確認: static 内の gAllActors.delete(this) は this がクラスを指すため、意図した actor が一覧から消えていない可能性がある。
- 条件付き依存: `if (win.gBrowser)` → `windowGlobal.getActor()`
- 条件付き依存: `if (actor)` → `actor.isReaderMode()`
- 条件付き依存: `if (actor.isReaderMode())` → `gAllActors.delete()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `browser.browsingContext.currentWindowGlobal`, `event.target.documentGlobal`, `win.gBrowser`, `win.gBrowser.selectedBrowser`

## AboutReaderParent.hasReaderModeEntryAtOffset()
- 位置: L227-236
- 役割: 指定オフセットの履歴に、対象 URL のエントリがあるかを子セッション履歴で確かめる。
- 触るとき: リーダーの入退場で履歴の前後移動を使うか判断する条件を見るときに見る。
- 呼び出し先: `browsingContext.childSessionHistory.canGo()`
- 条件付き依存: `if (browsingContext.childSessionHistory.canGo(offset))` → `shistory.getEntryAtIndex()`
- 参照: `browsingContext.sessionHistory`, `nextEntry.URI.spec`, `shistory.index`, `this.browsingContext`

## AboutReaderParent.enterReaderMode()
- 位置: L238-247
- 役割: 次の履歴にリーダー用エントリがあればそこへ進み、なければ子へリーダー表示を指示する。
- 触るとき: リーダー表示への移行で履歴を再利用する挙動を変えるときに見る。
- 呼び出し先: `encodeURIComponent()`, `this.hasReaderModeEntryAtOffset()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (this.hasReaderModeEntryAtOffset(readerURL, +1))` → `browsingContext.childSessionHistory.go()`
- 参照: `this.browsingContext`

## AboutReaderParent.leaveReaderMode()
- 位置: L249-259
- 役割: 元 URL の履歴が前にあればそこへ戻り、なければ子へリーダー終了を指示する。
- 触るとき: リーダーから元のページへ戻るときの履歴の扱いを変えるときに見る。
- 呼び出し先: `lazy.ReaderMode.getOriginalUrl()`, `this.hasReaderModeEntryAtOffset()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (this.hasReaderModeEntryAtOffset(originalURL, -1))` → `browsingContext.childSessionHistory.go()`
- 参照: `browsingContext.currentWindowGlobal.documentURI.spec`, `this.browsingContext`
