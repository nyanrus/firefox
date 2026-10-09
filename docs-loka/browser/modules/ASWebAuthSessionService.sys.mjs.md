# browser/modules/ASWebAuthSessionService.sys.mjs

source: browser/modules/ASWebAuthSessionService.sys.mjs
source-hash: c63282b72a61bd67a4457e7283e3fa46039c0d9f
lines: 677

## <module>
- 役割: アプリからの Web 認証要求を、専用のクロムレス窓で開き、コールバックや取消を仲介するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `Components.ID()`

## ASWebAuthSession.constructor()
- 位置: L20-46
- 役割: 1 件の認証セッションの要求情報・窓・タブ・コンテナを保持し、追跡中のタブ集合を初期化する。
- 触るとき: セッションに持たせる情報を増やすとき、追跡するタブの初期状態を変えるとき。
- 参照: `this.browser`, `this.callbackScheme`, `this.completed`, `this.hasCallback`, `this.headers`, `this.observingHeaders`, `this.request`, `this.service`, `this.trackedBrowsers`, `this.userContextId`, `this.uuid`, `this.window`

## ASWebAuthSession.start()
- 位置: L48-53
- 役割: セッションを有効一覧に登録し、タブ閉じ・窓の unload を監視し、ヘッダー監視を始める。
- 触るとき: セッション開始時の監視対象を増やすとき、開始直後に要求が消えてしまう問題を追うとき。
- 呼び出し先: `this.addHeaderObserver()`, `this.service.activeSessions.set()`, `this.window.addEventListener()`, `this.window.gBrowser.tabContainer.addEventListener()`
- 参照: `this.uuid`

## ASWebAuthSession.cleanup()
- 位置: L55-69
- 役割: ヘッダー監視、タブ・窓のイベント監視、ephemeral 用のコンテナを後始末する。
- 触るとき: 終了時に残るリスナーやコンテナを確かめるとき。窓が閉じていない場合は unload の監視を外さない。
- 呼び出し先: `this.removeHeaderObserver()`
- 条件付き依存: `if (this.window?.gBrowser)` → `this.window.gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (this.window && !this.window.closed)` → `this.window.removeEventListener()`
- 条件付き依存: `if (this.userContextId)` → `lazy.ContextualIdentityService.remove()`
- 参照: `this.userContextId`, `this.window`, `this.window.closed`, `this.window?.gBrowser`

## ASWebAuthSession.finish()
- 位置: L72-81
- 役割: 有効一覧から外して後始末し、必要なら認証窓を閉じる。
- 触るとき: 正常終了と取消のどちらでも窓を閉じる条件を変えるとき。closeWindow が false の時は窓を閉じない。
- 呼び出し先: `this.cleanup()`, `this.service.activeSessions.delete()`
- 条件付き依存: `if (closeWindow && this.window && !this.window.closed)` → `this.window.close()`
- 参照: `this.uuid`, `this.window`, `this.window.closed`

## ASWebAuthSession.complete()
- 位置: L84-92
- 役割: コールバック URL を要求元に返して 1 回だけ完了させ、後始末する。
- 触るとき: 成功時の応答の流れを変えるとき。completed フラグで二重完了を防いでいる点に注意する。
- 呼び出し先: `this.finish()`, `this.request.complete()`
- 参照: `this.completed`

## ASWebAuthSession.cancel()
- 位置: L97-105
- 役割: 要求元に取消を返して 1 回だけ後始末する。options を finish に渡す。
- 触るとき: 取消時の応答や窓を閉じるかどうかの扱いを変えるとき。タブを閉じた時や窓の unload からも呼ばれる。
- 呼び出し先: `this.finish()`, `this.request.cancel()`
- 参照: `this.completed`

## ASWebAuthSession.handleEvent()
- 位置: L107-116
- 役割: タブの TabClose と窓の unload を、それぞれの処理に振り分ける。
- 触るとき: 監視するイベントを増やすとき。
- 呼び出し先: `this.onTabClose()`, `this.onWindowUnload()`
- 参照: `event.type`

## ASWebAuthSession.observe()
- 位置: L118-148
- 役割: セッションのタブが読み込む最上位の文書に、アプリ指定の追加ヘッダーを付ける。既存のヘッダーは上書きしない。
- 触るとき: 認証要求に付けるヘッダーの扱いを変えるとき。ヘッダーの付与は最初の最上位読み込み 1 回だけで、その後は監視を外す。
- 呼び出し先: `Object.entries()`, `channel.getRequestHeader()`, `channel.setRequestHeader()`, `subject.QueryInterface()`, `this.hasBrowser()`, `this.removeHeaderObserver()`
- 参照: `Ci.nsIHttpChannel`, `bc.top`, `bc?.top?.embedderElement`, `channel.isDocument`, `channel.loadInfo?.browsingContext`, `this.headers`
- XPCOM: [`nsIHttpChannel`](../../netwerk/protocol/http/nsIHttpChannel.idl.md)

## ASWebAuthSession.onTabClose()
- 位置: L150-162
- 役割: 追跡中のタブが閉じられたとき、そのタブを外し、必要なら認証を取り消す。
- 触るとき: 認証タブを閉じたときの挙動(取消になる条件)を変えるとき。
- 呼び出し先: `this.hasOpenTrackedBrowser()`, `this.trackedBrowsers.delete()`
- 条件付き依存: `if ( !this.completed && (browser === this.browser || !this.hasOpenTrackedBrowser()) )` → `this.cancel()`
- 参照: `event.target.linkedBrowser`, `this.browser`, `this.completed`

## ASWebAuthSession.onWindowUnload()
- 位置: L164-168
- 役割: 窓が閉じられた時、まだ有効なセッションなら窓を閉じない形で取り消す。
- 触るとき: 窓が閉じた後に二重処理や残留が起きないか確かめるとき。
- 呼び出し先: `this.service.activeSessions.get()`
- 条件付き依存: `if (this.service.activeSessions.get(this.uuid) === this)` → `this.cancel()`
- 参照: `this.uuid`

## ASWebAuthSession.addHeaderObserver()
- 位置: L170-177
- 役割: 追加ヘッダーがある場合だけ http-on-modify-request の監視を始める。
- 触るとき: ヘッダー監視の開始条件を変えるとき。
- 呼び出し先: `Object.keys()`, `Services.obs.addObserver()`
- 参照: `Object.keys(this.headers).length`, `this.headers`, `this.observingHeaders`
- XPCOM: `Services.obs`

## ASWebAuthSession.removeHeaderObserver()
- 位置: L179-186
- 役割: ヘッダー監視が有効なら、その監視を外す。
- 触るとき: ヘッダー監視の解除漏れを確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this.observingHeaders`
- XPCOM: `Services.obs`

## ASWebAuthSession.trackBrowserIfInSessionWindow()
- 位置: L188-192
- 役割: そのブラウザがこのセッションの窓のタブなら追跡対象に加える。
- 触るとき: コールバックを扱うタブの追跡条件を変えるとき。
- 呼び出し先: `this.hasBrowser()`
- 条件付き依存: `if (this.hasBrowser(browser))` → `this.trackedBrowsers.add()`

## ASWebAuthSession.hasOpenTrackedBrowser()
- 位置: L194-202
- 役割: 追跡中のブラウザのうち、閉じられていないタブが一つでもあるかを返す。
- 触るとき: タブを閉じた時に取消すべきかの判定を変えるとき。
- 呼び出し先: `this.window?.gBrowser?.getTabForBrowser()`
- 参照: `tab.closing`, `this.trackedBrowsers`

## ASWebAuthSession.hasBrowser()
- 位置: L204-209
- 役割: そのブラウザが、このセッションの窓に属するタブかを返す。
- 触るとき: どのタブを認証用とみなすかを変えるとき。
- 呼び出し先: `this.window?.gBrowser?.getTabForBrowser()`
- 参照: `browser?.documentGlobal`, `this.window`

## ASWebAuthSession.ownsBrowsingContext()
- 位置: L211-223
- 役割: 文脈の最上位から opener をたどり、このセッションの窓のタブに属するかを返す。
- 触るとき: 別ウィンドウや別プロセスから開かれた認証ページの帰属判定を変えるとき。循環はループ検出で止める。
- 呼び出し先: `this.hasBrowser()`, `visited.add()`, `visited.has()`
- 参照: `bc?.top`, `opener?.top`, `top.crossGroupOpener`, `top.embedderElement`, `top.opener`

## ASWebAuthSessionService.constructor()
- 位置: L227-236
- 役割: 有効・保留中のセッション集合、初期化状態、読み込み進行の監視器を用意する。
- 触るとき: サービスの状態として持つ項目を増やすとき。
- 参照: `this.activeSessions`, `this.initialized`, `this.pendingSetups`, `this.progressListener`

## onLocationChange()
- 位置: L233-234
- 役割: タブ読み込みの場所変化を、サービスの onLocationChange に渡す。
- 触るとき: タブの場所変化を受ける経路を確かめるとき。
- 呼び出し先: `this.onLocationChange()`

## ASWebAuthSessionService.init()
- 位置: L238-258
- 役割: HTTP 応答と要求の通知を登録し、各窓のタブ進行監視を入れ、ネイティブ側に準備完了を知らせる。
- 触るとき: 起動時に登録する通知や監視を変えるとき。二重初期化は無視される。
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `lazy.EveryWindow.registerCallback()`, `win?.gBrowser?.addTabsProgressListener()`, `win?.gBrowser?.removeTabsProgressListener()`
- 参照: `this.initialized`, `this.progressListener`
- XPCOM: `Services.obs`

## ASWebAuthSessionService.uninit()
- 位置: L260-288
- 役割: 登録した通知や監視を外し、残っているセッションと保留中の要求を取り消す。
- 触るとき: 終了処理で要求が残る問題を調べるとき。
- 呼び出し先: `Array.from()`, `Services.obs.notifyObservers()`, `Services.obs.removeObserver()`, `lazy.EveryWindow.unregisterCallback()`, `session.cancel()`, `this.activeSessions.values()`, `this.pendingSetups.clear()`, `this.pendingSetups.values()`
- 条件付き依存: `if (!pending.cancelled)` → `pending.request.cancel()`
- 参照: `pending.cancelled`, `this.initialized`
- XPCOM: `Services.obs`

## ASWebAuthSessionService.removeLeftoverEphemeralContainers()
- 位置: async L294-308
- 役割: 前回の終了時に消し忘れた ephemeral 用コンテナを、使用中のものを除いて削除する。
- 触るとき: 一時コンテナが残り続ける問題を調べるとき。起動時の同期読み込みを避けるため init からは呼ばない。
- 呼び出し先: `identity.name.slice()`, `identity.name?.startsWith()`, `lazy.ContextualIdentityService.getPublicIdentities()`, `lazy.ContextualIdentityService.load()`, `lazy.ContextualIdentityService.remove()`, `this.activeSessions.has()`, `this.pendingSetups.has()`
- 参照: `EPHEMERAL_CONTAINER_PREFIX.length`, `identity.userContextId`

## ASWebAuthSessionService.observe()
- 位置: L312-327
- 役割: 通知の種類ごとに、HTTP 応答、要求の開始、要求の取消、ネイティブ準備完了に振り分ける。
- 触るとき: 新しい通知を受けるとき、通知名を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `this.onBegin()`, `this.onCancel()`, `this.onExamineResponse()`
- XPCOM: `Services.obs`

## ASWebAuthSessionService.shouldLoadCallback()
- 位置: L329-367
- 役割: カスタムスキームへの読み込みを、対応するセッションのコールバックとして受けて完了させ、読み込みを拒否する。
- 触るとき: アプリ独自のスキーム(myapp:// など)のコールバックを変えるとき。HTTP/HTTPS や文書以外は通す。
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `contentLocation.scheme?.toLowerCase()`, `this.activeSessions.get()`, `this.findSessionForCallbackScheme()`
- 条件付き依存: `if (this.activeSessions.get(session.uuid) === session)` → `session.complete()`
- 参照: `Ci.nsIContentPolicy.ACCEPT`, `Ci.nsIContentPolicy.REJECT_POLICY`, `Ci.nsIContentPolicy.TYPE_DOCUMENT`, `Ci.nsIContentPolicy.TYPE_SUBDOCUMENT`, `contentLocation.spec`, `loadInfo.browsingContext`, `loadInfo.externalContentPolicyType`, `session.uuid`, `this.activeSessions.size`
- XPCOM: [`nsIContentPolicy`](../../dom/base/nsIContentPolicy.idl.md) / `Services.tm`

## ASWebAuthSessionService.onExamineResponse()
- 位置: L369-418
- 役割: 最上位文書の 3xx 応答が Location でコールバックに一致する時、通信を打ち切ってセッションを完了させる。
- 触るとき: リダイレクト型のコールバックの判定や打ち切り方を変えるとき。例外はすべて無視する。
- 呼び出し先: `Services.io.newURI()`, `Services.tm.dispatchToMainThread()`, `channel.cancel()`, `channel.getResponseHeader()`, `subject.QueryInterface()`, `this.activeSessions.get()`, `this.findSessionForCallbackScheme()`
- 条件付き依存: `if (this.activeSessions.get(session.uuid) === session)` → `session.complete()`
- 参照: `Ci.nsIHttpChannel`, `Cr.NS_BINDING_ABORTED`, `bc.top`, `channel.isDocument`, `channel.loadInfo?.browsingContext`, `channel.responseStatus`, `locationUri.scheme`, `session.uuid`, `this.activeSessions.size`
- XPCOM: [`nsIHttpChannel`](../../netwerk/protocol/http/nsIHttpChannel.idl.md) / `Services.io` / `Services.tm`

## ASWebAuthSessionService.onLocationChange()
- 位置: L420-462
- 役割: HTTP(S) の場所変化は要求のコールバック URL と照合し、カスタムスキームは対応するセッションを完了させる。
- 触るとき: タブが場所を変えた時にコールバックとして扱う条件を変えるとき。
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `location.scheme?.toLowerCase()`, `session.trackBrowserIfInSessionWindow()`, `this.activeSessions.get()`, `this.findSessionForCallbackScheme()`
- 条件付き依存: `if (scheme === "https" || scheme === "http")` → `this.activeSessions.values()`
- 条件付き依存: `if (scheme === "https" || scheme === "http")` → `session.ownsBrowsingContext()`
- 条件付き依存: `if (session.hasCallback && session.ownsBrowsingContext(bc))` → `session.trackBrowserIfInSessionWindow()`
- 条件付き依存: `if (session.hasCallback && session.ownsBrowsingContext(bc))` → `session.request.matchesCallbackURL()`
- 条件付き依存: `if (session.request.matchesCallbackURL(location.spec))` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (session.request.matchesCallbackURL(location.spec))` → `this.activeSessions.get()`
- 条件付き依存: `if (this.activeSessions.get(session.uuid) === session)` → `session.complete()`
- 参照: `location.spec`, `session.hasCallback`, `session.uuid`, `this.activeSessions.size`, `webProgress.browsingContext`, `webProgress?.isTopLevel`
- XPCOM: `Services.tm`

## ASWebAuthSessionService.findSessionForCallbackScheme()
- 位置: L464-474
- 役割: スキームが一致し、かつ文脈がそのセッションに属する有効なセッションを探す。
- 触るとき: どのセッションにコールバックを渡すかの判定を変えるとき。
- 呼び出し先: `session.ownsBrowsingContext()`, `this.activeSessions.values()`
- 参照: `session.callbackScheme`

## ASWebAuthSessionService.waitForWindowClosed()
- 位置: L476-495
- 役割: 窓が閉じるまで待つ Promise を返す。すでに閉じていれば即座に解決する。
- 触るとき: 認証窓を開いた後に閉じられた場合の待ち方を変えるとき。
- 呼び出し先: `Services.ww.registerNotification()`
- 条件付き依存: `if (!win || win.closed)` → `Promise.resolve()`
- 条件付き依存: `if (win.closed)` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if (win.closed)` → `resolve()`
- 参照: `win.closed`
- XPCOM: `Services.ww`

## windowCloseObserver()
- 位置: L482-487
- 役割: 対象の窓の domwindowclosed を受けて通知を外し、待ちを解決する。
- 触るとき: 窓の閉じ検知の仕組みを変えるとき。
- 条件付き依存: `if (topic === "domwindowclosed" && subject === win)` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if (topic === "domwindowclosed" && subject === win)` → `resolve()`
- XPCOM: `Services.ww`

## ASWebAuthSessionService.observeNextWindowOpen()
- 位置: L497-513
- 役割: 次に開かれる窓を一度だけ待つ Promise と、監視を外す関数を返す。
- 触るとき: 認証窓の開き待ちのタイミングを変えるとき。
- 呼び出し先: `Promise.withResolvers()`, `Services.ww.registerNotification()`
- XPCOM: `Services.ww`

## windowOpenObserver()
- 位置: L499-504
- 役割: domwindowopened を受けて監視を外し、開かれた窓で待ちを解決する。
- 触るとき: 窓の開き検知の仕組みを変えるとき。
- 条件付き依存: `if (topic === "domwindowopened")` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if (topic === "domwindowopened")` → `resolve()`
- XPCOM: `Services.ww`

## ASWebAuthSessionService.unregister()
- 位置: L509-511
- 役割: 窓の開き待ちの監視を外す。
- 触るとき: 窓を開けなかった場合に監視が残る問題を確かめるとき。
- 呼び出し先: `Services.ww.unregisterNotification()`
- XPCOM: `Services.ww`

## ASWebAuthSessionService.openAuthWindow()
- 位置: async L515-553
- 役割: クロムレスの窓で認証 URL を開き、窓とタブが作られるまで待つ。窓が先に閉じたら browser は null。
- 触るとき: 認証窓の開き方(私用モード、コンテナ、窓の種類)を変えるとき。
- 呼び出し先: `Promise.race()`, `Promise.withResolvers()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.URILoadingHelper.openWebLinkIn()`, `openedWindow.unregister()`, `this.observeNextWindowOpen()`, `this.waitForWindowClosed()`, `this.waitForWindowClosed(win).then()`
- 参照: `Services.appShell.hiddenDOMWindow`, `browser?.documentGlobal`, `openedWindow.promise`
- XPCOM: `Services.appShell`

## ASWebAuthSessionService.cleanupFailedSetup()
- 位置: L555-565
- 役割: セットアップに失敗した時、コンテナと窓を片付け、要求を取り消す。
- 触るとき: 開始失敗時に残るものを確かめるとき。取り消し済みの要求は二重に取り消さない。
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.remove()`
- 条件付き依存: `if (win && !win.closed)` → `win.close()`
- 条件付き依存: `if (!pending.cancelled)` → `pending.request.cancel()`
- 参照: `pending.cancelled`, `win.closed`

## ASWebAuthSessionService.onBegin()
- 位置: async L567-638
- 役割: https の要求を受け、起動後に必要なら一時コンテナを作って認証窓を開き、セッションを開始する。
- 触るとき: 認証要求の受け付け条件、窓を開く順番、一時コンテナの扱いを変えるとき。https 以外や uuid の無い要求はその場で取り消す。
- 呼び出し先: `URL.parse()`, `console.error()`, `request.QueryInterface()`, `request.callbackScheme.toLowerCase()`, `request.getAdditionalHeader()`, `session.start()`, `this.cleanupFailedSetup()`, `this.openAuthWindow()`, `this.pendingSetups.delete()`, `this.pendingSetups.set()`, `win.focus()`
- 条件付き依存: `if (!uuid || parsedURL?.protocol !== "https:")` → `request.cancel()`
- 条件付き依存: `if (ephemeral)` → `lazy.ContextualIdentityService.create()`
- 条件付き依存: `if (!result.browser || win.closed || pending.cancelled)` → `this.cleanupFailedSetup()`
- 参照: `Ci.nsIASWebAuthSessionRequest`, `container.userContextId`, `lazy.SessionStore.promiseAllWindowsRestored`, `parsedURL.href`, `parsedURL?.protocol`, `pending.cancelled`, `request.additionalHeaderNames`, `request.hasCallback`, `request.url`, `request.useEphemeralSession`, `request.uuid`, `result.browser`, `result.win`, `win.closed`
- XPCOM: [`nsIASWebAuthSessionRequest`](../../toolkit/xre/nsIASWebAuthSessionRequest.idl.md)

## ASWebAuthSessionService.onCancel()
- 位置: L640-652
- 役割: uuid の要求を、有効なセッションか保留中のセットアップの順に取り消す。
- 触るとき: アプリ側からの取消要求の扱いを変えるとき。
- 呼び出し先: `this.activeSessions.get()`, `this.pendingSetups.get()`
- 条件付き依存: `if (session)` → `session.cancel()`
- 条件付き依存: `if (pending && !pending.cancelled)` → `pending.request.cancel()`
- 参照: `pending.cancelled`

## ASWebAuthSessionCallbackContentPolicy()
- 位置: L657-657
- 役割: カスタムスキームのコールバックを捕まえる content policy コンポーネントの実体。
- 触るとき: components.conf の登録や、このポリシーの契約 ID を変えるとき。

## shouldLoad()
- 位置: L666-671
- 役割: content policy の判定をサービスの shouldLoadCallback に委ねる。
- 触るとき: コールバック判定の入口を変えるとき。
- 呼び出し先: `ASWebAuthSessionService.shouldLoadCallback()`

## shouldProcess()
- 位置: L673-675
- 役割: content policy の処理段階では常に ACCEPT を返し、何もしない。
- 触るとき: 処理段階でも判定が必要になったとき。
- 参照: `Ci.nsIContentPolicy.ACCEPT`
- XPCOM: [`nsIContentPolicy`](../../dom/base/nsIContentPolicy.idl.md)
