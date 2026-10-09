# browser/actors/ClickHandlerParent.sys.mjs

source: browser/actors/ClickHandlerParent.sys.mjs
source-hash: c06993a8f543d7d4587f618b429c7dba59ff9987
lines: 161

## <module>
- 役割: 子プロセスから届いたクリック情報を親側で補完し、リンクを開く処理と登録済みのクリックリスナーへの通知を行うアクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## fillInClickEvent()
- 位置: L19-27
- 役割: 子から届いたクリックデータに、フレーム ID・プリンシパル・属性・プライベート判定を親側の値で補う。
- 触るとき: クリックで開くリンクの権限や分離属性が正しいかを調べるときに見る。
- 呼び出し先: `lazy.WebNavigationFrames.getFrameId()`
- 参照: `actor.manager`, `data.frameID`, `data.isContentWindowPrivate`, `data.originAttributes`, `data.originPrincipal`, `data.originStoragePrincipal`, `data.triggeringPrincipal`, `wgp.browsingContext`, `wgp.browsingContext.usePrivateBrowsing`, `wgp.documentPrincipal`, `wgp.documentPrincipal?.originAttributes`, `wgp.documentStoragePrincipal`

## MiddleMousePasteHandlerParent.receiveMessage()
- 位置: L30-43
- 役割: MiddleClickPaste を受け、補完したデータをウィンドウの middleMousePaste に渡す。
- 触るとき: 中クリック貼り付けの後段処理を変えるときに見る。
- 条件付き依存: `if (message.name == "MiddleClickPaste")` → `fillInClickEvent()`
- 条件付き依存: `if (message.name == "MiddleClickPaste")` → `browser.documentGlobal.middleMousePaste()`
- 参照: `message.data`, `message.name`, `this.manager.browsingContext.top.embedderElement`

## ClickHandlerParent.addContentClickListener()
- 位置: L47-49
- 役割: コンテンツのクリックを受け取るリスナーを登録する。
- 触るとき: クリックを購読する機能を追加するときに見る。
- 呼び出し先: `gContentClickListeners.add()`

## ClickHandlerParent.removeContentClickListener()
- 位置: L51-53
- 役割: 登録済みのクリックリスナーを外す。
- 触るとき: リスナーの解除漏れを調べるときに見る。
- 呼び出し先: `gContentClickListeners.delete()`

## ClickHandlerParent.receiveMessage()
- 位置: L55-63
- 役割: Content:Click を受け、補完・リンクを開く処理・リスナー通知の順に実行する。
- 触るとき: リンククリックの処理順序を変えるときに見る。
- 呼び出し先: `fillInClickEvent()`, `this.contentAreaClick()`, `this.notifyClickListeners()`
- 参照: `message.data`, `message.name`

## ClickHandlerParent.contentAreaClick()
- 位置: L71-147
- 役割: リンクを開く先（新規タブや新規ウィンドウ）を決め、閲覧履歴の印を付けてから、参照元や分離属性を引き継いで開く。
- 触るとき: リンクを新しいタブで開く挙動、履歴の扱い、参照元ポリシーを変えるときに見る。
- 呼び出し先: `lazy.BrowserUtils.whereToOpenLink()`, `lazy.E10SUtils.deserializePolicyContainer()`, `lazy.E10SUtils.deserializeReferrerInfo()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `window.openLinkIn()`
- 条件付き依存: `if (!lazy.PrivateBrowsingUtils.isWindowPrivate(window))` → `lazy.PlacesUIUtils.markPageAsFollowedLink()`
- 条件付き依存: `if (!(data.globalHistoryOptions))` → `browser.getAttribute()`
- 参照: `browser.characterSet`, `browser.documentGlobal`, `data.frameID`, `data.globalHistoryOptions`, `data.href`, `data.isContentWindowPrivate`, `data.originAttributes.userContextId`, `data.originPrincipal`, `data.originStoragePrincipal`, `data.policyContainer`, `data.referrerInfo`, `data.triggeringPrincipal`, `params.allowInheritPrincipal`, `params.globalHistoryOptions`, `params.userContextId`, `this.manager.browsingContext.top.embedderElement`, `this.manager.domProcess?.remoteType`, `window.openLinkIn`

## ClickHandlerParent.notifyClickListeners()
- 位置: L149-159
- 役割: 登録済みの各リスナーの onContentClick を呼び、例外は個別に記録して続ける。
- 触るとき: クリックに反応する外部機能が呼ばれない問題を調べるときに見る。
- 呼び出し先: `console.error()`, `listener.onContentClick()`
- 参照: `this.browsingContext.top.embedderElement`
