# browser/components/aiwindow/ui/actors/AIChatContentParent.sys.mjs

source: browser/components/aiwindow/ui/actors/AIChatContentParent.sys.mjs
source-hash: ef9b2cdc672976bdb291adb028da2a0c1ee6df5b
lines: 371

## <module>
- 役割: AI Window のチャット(AIChatContent)と、ページ側の内部ページ・親ウィンドウの UI をつなぐ親アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AIChatContentParent.isTrustedInternalURI()
- 位置: L45-49
- 役割: URI が設定・タスク・スマートページのいずれかの内部 URL なら true を返す。
- 触るとき: チャットからの内部リンクを開いてよいか判定する条件を変えるとき、または新しい内部ページを開けるようにするときに見る。判定の根拠は TrustedInternalURLs.mjs 側にある。
- 呼び出し先: `URL.parse()`, `isSettingsURL()`, `isSmartPageURL()`, `isTasksURL()`
- 参照: `uri.spec`

## AIChatContentParent.dispatchMessageToChatContent()
- 位置: L51-61
- 役割: メッセージを浅くコピーして pageUrl を外し、子プロセスへ AIChatContent:DispatchMessage として送る。URL オブジェクトは IPC で送れないため pageUrl を消す。
- 触るとき: チャットへ新しいメッセージを送る経路を変えるとき、または送ったメッセージに URL 型の値が残ってエラーになるときに見る。
- 呼び出し先: `Object.assign()`, `this.sendAsyncMessage()`
- 参照: `message.pageUrl`

## AIChatContentParent.dispatchTruncateToChatContent()
- 位置: L63-65
- 役割: 会話の切り詰めを AIChatContent:TruncateConversation として子へ送る。
- 触るとき: 会話を途中から打ち切る操作が表示に反映されないときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## AIChatContentParent.dispatchRemoveAppliedMemoryToChatContent()
- 位置: L67-69
- 役割: 適用済みの記憶の削除要求を AIChatContent:RemoveAppliedMemory として子へ送る。
- 触るとき: 記憶の削除がチャット側に反映されないときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## AIChatContentParent.dispatchSeenUrlsToChatContent()
- 位置: L79-81
- 役割: 会話の既読 URL の集合(全件または差分)を AIChatContent:SeenUrls として子へ送る。
- 触るとき: 生成ページの表示可否が既読 URL に依存して変わらないときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## AIChatContentParent.setGeneratingOnChatContent()
- 位置: L83-85
- 役割: 生成中かどうかの状態を AIChatContent:SetGenerating として子へ送る。
- 触るとき: 生成中の表示(停止ボタンなど)がずれるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## AIChatContentParent.receiveMessage()
- 位置: L87-139
- 役割: 子からの AIChatContent:* メッセージを名前で振り分ける。履歴グリッドのイベントは telemetry に記録し、未知の名前は警告を出す。
- 触るとき: 子プロセスから新しいメッセージを追加するとき、または子からの要求が処理されないときに見る。新しい名前は switch に足す必要がある。
- 呼び出し先: `console.warn()`, `lazy.AIWindowTelemetry.recordHistoryGridEvent()`, `this.#getAIWindowElement()`, `this.#handleAccountSignIn()`, `this.#handleClientError()`, `this.#handleFollowUpFromChild()`, `this.#handleFooterActionFromChild()`, `this.#handleNewChat()`, `this.#handleOpenLink()`, `this.#handleRequestAssets()`, `this.#handleToolUIUpdate()`, `this.#notifyContentReady()`

## AIChatContentParent.#notifyContentReady()
- 位置: L141-150
- 役割: AI Window に読み込み完了を伝え、そのモード(サイドバーか全画面)を AIChatContent:SetMode で子へ送る。
- 触るとき: チャットの初回表示でモード別のスタイルが当たらないときに見る。モードは URL ではなくこの経路で渡す。
- 呼び出し先: `aiWindow?.onContentReady()`, `this.#getAIWindowElement()`
- 条件付き依存: `if (aiWindow?.mode)` → `this.sendAsyncMessage()`
- 参照: `aiWindow.mode`, `aiWindow?.mode`

## AIChatContentParent.#handleFooterActionFromChild()
- 位置: L152-159
- 役割: 子からのフッター操作を AI Window の handleFooterAction に渡す。失敗は警告にとどめる。
- 触るとき: フッターのボタン操作が効かないときに見る。
- 呼び出し先: `aiWindow.handleFooterAction()`, `console.warn()`, `this.#getAIWindowElement()`

## AIChatContentParent.#handleOpenLink()
- 位置: L161-244
- 役割: チャット内のリンクを開く。http と https、および内部ページだけを通す。同じ URL なら同一リンク扱いにし、内部ページは既存タブへ切り替え、それ以外は設定に従って既存タブへの切り替えか新規タブで開く。
- 触るとき: チャットのリンクが開かない、または開き先(現在のタブか新規タブか)がおかしいときに見る。リンク計測(recordUriLoad)もこの関数で記録される。
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createNullPrincipal()`, `aiWindow?.onOpenLink()`, `console.warn()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.SmartWindowTelemetry.recordUriLoad()`, `lazy.URILoadingHelper.openWebLinkIn()`, `this.#getAIWindowElement()`, `this.isTrustedInternalURI()`
- 条件付き依存: `if (url === currentPageURL)` → `lazy.AIWindowUI.handleSameLinkClick()`
- 条件付き依存: `if (this.isTrustedInternalURI(uri))` → `lazy.URILoadingHelper.switchToTabHavingURI()`
- 条件付き依存: `if (preferSwitchToTab)` → `lazy.URILoadingHelper.switchToTabHavingURI()`
- 条件付き依存: `if (preferSwitchToTab)` → `lazy.URILoadingHelper.openWebLinkIn()`
- 条件付き依存: `if (where === "current")` → `lazy.URILoadingHelper.switchToTabHavingURI()`
- 参照: `this.browsingContext.topChromeWindow`, `uri.scheme`, `window.gBrowser.selectedBrowser.browsingContext.originAttributes`, `window.gBrowser.selectedBrowser.currentURI.spec`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## AIChatContentParent.#handleAccountSignIn()
- 位置: async L246-252
- 役割: サインインフローを起動し、成功したら直前のエラーからの再試行を行う。
- 触るとき: サインイン後にエラー表示が残る、または再試行が走らないときに見る。
- 呼び出し先: `lazy.AIWindow.launchSignInFlow()`
- 条件付き依存: `if (success)` → `this.#handleRetryAfterError()`
- 参照: `this.browsingContext.topChromeWindow.gBrowser`

## AIChatContentParent.#handleRetryAfterError()
- 位置: L254-261
- 役割: AI Window のフッター操作として retry-after-error を渡し、直前のエラーから再試行させる。
- 触るとき: エラー後の再試行ボタンが効かないときに見る。
- 呼び出し先: `aiWindow.handleFooterAction()`, `console.warn()`, `this.#getAIWindowElement()`

## AIChatContentParent.#handleNewChat()
- 位置: L263-270
- 役割: AI Window の新規チャット処理(onCreateNewChatClick)を呼ぶ。
- 触るとき: 新規チャットボタンが反応しないときに見る。
- 呼び出し先: `aiWindow.onCreateNewChatClick()`, `console.warn()`, `this.#getAIWindowElement()`

## AIChatContentParent.#getAIWindowElement()
- 位置: L272-279
- 役割: 埋め込み元要素のルートがシャドウルートで、そのホストが ai-window ならそれを返す。そうでなければ所属文書から ai-window を探し、無ければ null を返す。
- 触るとき: チャットがどの AI Window に属するか判定する経路を変えるとき、または要素が見つからず処理が黙って止まるときに見る。
- 呼び出し先: `browser?.getRootNode()`, `browser?.ownerDocument?.querySelector()`
- 参照: `root.host`, `root?.host?.localName`, `this.browsingContext.embedderElement`

## AIChatContentParent.#handleFollowUpFromChild()
- 位置: L281-288
- 役割: フォローアップの文面を onQuickPromptClicked に渡して送信する。
- 触るとき: フォローアップ質問が送信されないときに見る。
- 呼び出し先: `aiWindow.onQuickPromptClicked()`, `console.warn()`, `this.#getAIWindowElement()`
- 参照: `data.text`

## AIChatContentParent.#handleToolUIUpdate()
- 位置: L290-297
- 役割: ツールの UI 更新を AI Window の handleToolUIUpdate に渡す。
- 触るとき: ツール実行の表示が更新されないときに見る。
- 呼び出し先: `aiWindow.handleToolUIUpdate()`, `console.warn()`, `this.#getAIWindowElement()`

## AIChatContentParent.#handleRequestAssets()
- 位置: async L313-338
- 役割: 各 URL のサムネイルと、Places に保存済みのファビコンの有無を解決する。結果を AI Window の会話キャッシュに入れ、同じ messageId で AIChatContent:AssetsReady として子へ返す。
- 触るとき: 履歴グリッドや引用のサムネイル・ファビコンが出ないときに見る。サムネイルを取れない場合も images には項目が残る。
- 呼び出し先: `Promise.all()`, `console.warn()`, `items.map()`, `lazy.captureThumbnail()`, `this.#getAIWindowElement()`, `this.#pageHasFavicon()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (aiWindowElement)` → `aiWindowElement.applyHistoryAssets()`

## AIChatContentParent.#pageHasFavicon()
- 位置: async L348-357
- 役割: Places に url のファビコンが保存されているかを返す。取得に失敗した場合は false を返す。
- 触るとき: ファビコンの代わりにデフォルトのアイコンが出るとき、または UI 側のフォールバック判定を変えるときに見る。
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons.getFaviconForPage()`
- XPCOM: `Services.io`

## AIChatContentParent.#handleClientError()
- 位置: L359-369
- 役割: 子から届いたクライアント側エラーを、AI Window の文脈つきで telemetry に記録する。
- 触るとき: チャット側のエラーが telemetry に出ないとき、または記録する文脈情報を増やすときに見る。
- 呼び出し先: `aiWindow?.getClientErrorContext()`, `console.warn()`, `lazy.SmartWindowTelemetry.recordClientErrorDetail()`, `this.#getAIWindowElement()`
