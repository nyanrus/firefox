# browser/actors/ContentSearchParent.sys.mjs

source: browser/actors/ContentSearchParent.sys.mjs
source-hash: 60758375a7e938f75745a1270c228a6040e8bf22
lines: 759

## <module>
- 役割: 検索 UI（ContentSearch）の親側。子からの検索・候補取得・検索履歴・エンジン変更の要求を直列に処理し、状態の変化を各ページへ配信する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## init()
- 位置: L112-120
- 役割: 検索サービス・Urlbar 設定の監視を登録し、一度だけ初期化する。
- 触るとき: 検索 UI が状態変化を受け取らない問題を調べるときに見る。
- 条件付き依存: `if (!this.initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this.initialized)` → `lazy.UrlbarPrefs.addObserver()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## searchSuggestionUIStrings()
- 位置: L122-142
- 役割: search.properties から候補欄の見出し文字列を読み込み、一度だけキャッシュして返す。
- 触るとき: 検索候補欄の文言を追加・変更するときに見る。
- 呼び出し先: `Services.strings.createBundle()`, `searchBundle.GetStringFromName()`
- 参照: `this._searchSuggestionUIStrings`
- XPCOM: `Services.strings`

## destroy()
- 位置: L144-159
- 役割: オブザーバーを外し、待ちのイベント処理が終わるまで待つ Promise を返す。
- 触るとき: 終了時に検索処理が残る、または終了がブロックされる問題を調べるときに見る。
- 呼び出し先: `Promise.resolve()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (!this.initialized)` → `Promise.resolve()`
- 参照: `this._currentEventPromise`, `this._destroyedPromise`, `this._eventQueue.length`, `this.initialized`
- XPCOM: `Services.obs`

## observe()
- 位置: L161-177
- 役割: 検索エンジンの変更通知をイベントキューへ積み、終了前にはブロッカーを登録する。
- 触るとき: 既定エンジン変更の反映タイミングを調べるときに見る。
- 呼び出し先: `subj.wrappedJSObject.client.addBlocker()`, `this._eventQueue.push()`, `this._processEventQueue()`, `this.destroy()`

## onPrefChanged()
- 位置: L186-194
- 役割: 検索モードへの引き継ぎに関わる pref が変わったときに、キューへ Observe を積む。
- 触るとき: 検索モード引き継ぎ設定の変更が画面に反映されないときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.shouldHandOffToSearchModePrefs.includes()`
- 条件付き依存: `if (lazy.UrlbarPrefs.shouldHandOffToSearchModePrefs.includes(pref))` → `this._eventQueue.push()`
- 条件付き依存: `if (lazy.UrlbarPrefs.shouldHandOffToSearchModePrefs.includes(pref))` → `this._processEventQueue()`

## removeFormHistoryEntry()
- 位置: L196-211
- 役割: 直前の候補結果から該当の入力履歴を探し、フォーム履歴から削除する。
- 触るとき: 検索履歴の削除ボタンが効かない問題を調べるときに見る。
- 呼び出し先: `this._suggestionDataForBrowser()`
- 条件付き依存: `if (browserData?.previousFormHistoryResults)` → `browserData.previousFormHistoryResults.find()`
- 条件付き依存: `if (browserData?.previousFormHistoryResults)` → `lazy.FormHistory.update()`
- 条件付き依存: `if (browserData?.previousFormHistoryResults)` → `console.error()`
- 参照: `browserData?.previousFormHistoryResults`, `e.text`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `result.guid`

## performSearch()
- 位置: L213-265
- 役割: エンジンの検索 URL を作り、現在のタブ・新規タブ等の設定に応じて開き、検索テレメトリを記録する。
- 触るとき: 検索結果を開く先やテレメトリの記録条件を変えるときに見る。
- 呼び出し先: `engine.getSubmission()`, `lazy.BrowserSearchTelemetry.recordSearch()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.SearchService.getEngineByName()`, `this._ensureDataHasProperties()`
- 条件付き依存: `if (where === "current")` → `this._reply()`
- 条件付き依存: `if (where === "current")` → `browser.loadURI()`
- 条件付き依存: `if (where === "current")` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (where === "current")` → `win.gBrowser.selectedBrowser.getAttribute()`
- 条件付き依存: `if (!(where === "current"))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(where === "current"))` → `win.openTrustedLinkIn()`
- 参照: `browser.documentGlobal`, `data.engineName`, `data.healthReportKey`, `data.originalEvent`, `data.searchString`, `data.selection`, `submission.postData`, `submission.uri`, `submission.uri.spec`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## getSuggestions()
- 位置: async L267-318
- 役割: エンジンの候補取得コントローラーで候補を集め、ローカル履歴とリモート候補に整形して返す。
- 触るとき: 検索候補の件数、取得方法、プライベート判定を変えるときに見る。
- 呼び出し先: `controller.fetch()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `lazy.SearchService.getEngineByName()`, `lazy.SearchSuggestionController.engineOffersSuggestions()`, `nonTailEntries.map()`, `suggestions.local.map()`, `suggestions.remote.filter()`, `this._suggestionDataForBrowser()`
- 参照: `browserData.previousFormHistoryResults`, `e.matchPrefix`, `e.tail`, `e.value`, `suggestions.formHistoryResults`, `suggestions.local`, `suggestions.remote`, `suggestions.term`, `this._currentSuggestion`

## addFormHistoryEntry()
- 位置: async L320-345
- 役割: プライベートでなく長さの範囲内なら、検索語を検索履歴に加える（bump）。
- 触るとき: 検索履歴の保存条件や文字数上限を変えるときに見る。
- 呼び出し先: `console.error()`, `lazy.FormHistory.update()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `entry.engineName`, `entry.value`, `entry.value.length`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VALUE_LENGTH`

## currentStateObj()
- 位置: async L352-369
- 役割: 通常・プライベートの既定エンジンと、表示中エンジンの一覧（アイコン含む）をまとめた状態を作る。
- 触るとき: 検索 UI に渡すエンジン状態の形式を変えるときに見る。
- 呼び出し先: `lazy.SearchService.getVisibleEngines()`, `state.engines.push()`, `this._currentEngineObj()`, `this._getEngineIconURL()`
- 参照: `engine.hideOneOffButton`, `engine.name`, `lazy.ConfigSearchEngine`

## _processEventQueue()
- 位置: L371-389
- 役割: キューの先頭から 1 件ずつ _on<種類> を実行し、完了後に次を処理する。
- 触るとき: 検索メッセージの順序やまとめ処理を調べるときに見る。
- 呼び出し先: `console.error()`, `this._eventQueue.shift()`, `this._processEventQueue()`, `this["_on" + event.type]()`
- 参照: `event.type`, `this._currentEventPromise`, `this._eventQueue.length`

## _cancelSuggestions()
- 位置: L391-413
- 役割: 同じブラウザの進行中・待ちの候補取得を止め、取り消し通知を返す。
- 触るとき: 検索実行時に古い候補が残る問題を調べるときに見る。
- 条件付き依存: `if ( this._currentSuggestion && this._currentSuggestion.browser === browser )` → `this._currentSuggestion.controller.stop()`
- 条件付き依存: `if (actor === m.actor && m.name === "GetSuggestions")` → `this._eventQueue.splice()`
- 条件付き依存: `if (cancelled)` → `this._reply()`
- 参照: `m.actor`, `m.name`, `this._currentSuggestion`, `this._currentSuggestion.browser`, `this._eventQueue`, `this._eventQueue.length`

## _onMessage()
- 位置: async L415-422
- 役割: メッセージ名に対応する _onMessage<名前> を、サービス初期化後に呼ぶ。
- 触るとき: 新しい検索メッセージを追加するときに、ディスパッチの仕組みを確かめるときに見る。
- 条件付き依存: `if (methodName in this)` → `this._initService()`
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 条件付き依存: `if (methodName in this)` → `eventItem.browser.removeEventListener()`
- 参照: `eventItem.name`

## _onMessageGetState()
- 位置: async L424-427
- 役割: GetState に対し、現在の検索状態を State として返す。
- 触るとき: 検索 UI の初期状態の取得経路を変えるときに見る。
- 呼び出し先: `this._reply()`, `this.currentStateObj()`

## _onMessageGetEngine()
- 位置: async L429-438
- 役割: GetEngine に対し、そのブラウザがプライベートかで既定エンジンを選んで返す。
- 触るとき: プライベートウィンドウでの既定エンジン表示を調べるときに見る。
- 呼び出し先: `this._reply()`, `this.currentStateObj()`
- 参照: `actor.browsingContext`, `state.currentEngine`, `state.currentPrivateEngine`

## _onMessageGetHandoffSearchModePrefs()
- 位置: L440-446
- 役割: 検索モードへの引き継ぎ設定を HandoffSearchModePrefs として返す。
- 触るとき: 検索モード引き継ぎの初期値を調べるときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._reply()`

## _onMessageGetStrings()
- 位置: L448-450
- 役割: 候補欄の文言を Strings として返す。
- 触るとき: 検索 UI の表示文言の受け渡しを変えるときに見る。
- 呼び出し先: `this._reply()`
- 参照: `this.searchSuggestionUIStrings`

## _onMessageSearch()
- 位置: L452-454
- 役割: Search を performSearch に渡す。
- 触るとき: 検索実行の入口を追うときに見る。
- 呼び出し先: `this.performSearch()`

## _onMessageSetCurrentEngine()
- 位置: L456-461
- 役割: 検索バーから選ばれたエンジンを、ユーザー操作として既定に設定する。
- 触るとき: 検索バーからの既定エンジン変更の理由や通知を変えるときに見る。
- 呼び出し先: `lazy.SearchService.getEngineByName()`, `lazy.SearchService.setDefault()`
- 参照: `lazy.SearchService.CHANGE_REASON.USER_SEARCHBAR`

## _onMessageManageEngines()
- 位置: L463-465
- 役割: ブラウザの設定画面の検索パネルを開く。
- 触るとき: 検索エンジンの管理画面への導線を変えるときに見る。
- 呼び出し先: `browser.documentGlobal.openPreferences()`

## _onMessageGetSuggestions()
- 位置: async L467-482
- 役割: 候補取得を実行し、結果の整形済みデータを Suggestions として返す。
- 触るとき: 候補の返却形式や項目を変えるときに見る。
- 呼び出し先: `this._ensureDataHasProperties()`, `this._reply()`, `this.getSuggestions()`
- 参照: `data.engineName`, `suggestions.local`, `suggestions.remote`, `suggestions.term`

## _onMessageAddFormHistoryEntry()
- 位置: async L484-486
- 役割: AddFormHistoryEntry を addFormHistoryEntry に渡す。
- 触るとき: 検索語の履歴登録の入口を追うときに見る。
- 呼び出し先: `this.addFormHistoryEntry()`

## _onMessageRemoveFormHistoryEntry()
- 位置: L488-490
- 役割: RemoveFormHistoryEntry を removeFormHistoryEntry に渡す。
- 触るとき: 検索履歴の削除要求の入口を追うときに見る。
- 呼び出し先: `this.removeFormHistoryEntry()`

## _onMessageSpeculativeConnect()
- 位置: L492-503
- 役割: エンジンのサーバーへ先行接続を張る。エンジンが無ければ例外。
- 触るとき: 検索結果の表示を速くする先行接続の条件を変えるときに見る。
- 呼び出し先: `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (browser.contentWindow)` → `engine.speculativeConnect()`
- 参照: `browser.contentPrincipal.originAttributes`, `browser.contentWindow`

## _onMessageSearchHandoff()
- 位置: L505-575
- 役割: ページ内検索からアドレスバーへ入力を引き継ぎ、初回入力・Esc・フォーカス外れで元に戻すリスナーを付ける。
- 触るとき: ページ内の検索欄からアドレスバーへの引き継ぎ動作を変えるときに見る。
- 呼び出し先: `lazy.AboutNewTab.getVisitId()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `urlBar.inputField.addEventListener()`
- 条件付き依存: `if (!text)` → `urlBar.setHiddenFocus()`
- 条件付き依存: `if (!(!text))` → `urlBar.handoff()`
- 参照: `browser.documentGlobal`, `data.text`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `win.gURLBar`

## checkFirstChange()
- 位置: L528-540
- 役割: 引き継ぎ後の最初の入力・貼り付けを検知して、非表示フォーカスを外しページ内検索を隠す。
- 触るとき: 引き継ぎ直後の見た目や入力の切り替わりを調べるときに見る。
- 条件付き依存: `if (isFirstChange)` → `urlBar.removeHiddenFocus()`
- 条件付き依存: `if (isFirstChange)` → `urlBar.handoff()`
- 条件付き依存: `if (isFirstChange)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (isFirstChange)` → `urlBar.removeEventListener()`

## onKeydown()
- 位置: L542-551
- 役割: 値が変わるキー入力なら checkFirstChange を呼び、Esc なら onDone で後始末する。
- 触るとき: 引き継ぎ中のキー操作の扱いを変えるときに見る。
- 条件付き依存: `if (ev.key.length === 1 && !ev.altKey && !ev.ctrlKey && !ev.metaKey)` → `checkFirstChange()`
- 条件付き依存: `if (ev.key === "Escape")` → `onDone()`
- 参照: `ev.altKey`, `ev.ctrlKey`, `ev.key`, `ev.key.length`, `ev.metaKey`

## onDone()
- 位置: L553-568
- 役割: 引き継ぎを終え、アドレスバーのリスナーを外してページ内検索を再表示する。
- 触るとき: 引き継ぎ終了後にフォーカスやリスナーが残る問題を調べるときに見る。
- 呼び出し先: `actor.sendAsyncMessage()`, `urlBar.inputField.removeEventListener()`, `urlBar.removeHiddenFocus()`
- 参照: `ev?.type`

## _onObserve()
- 位置: async L577-600
- 役割: 既定エンジンや引き継ぎ設定の変更を見て、該当する状態を全ページへ配信する。
- 触るとき: 変更通知が各ページに届く種類を追加・変更するときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._broadcast()`, `this._currentEngineObj()`, `this.currentStateObj()`
- 参照: `eventItem.data`

## _suggestionDataForBrowser()
- 位置: L602-614
- 役割: ブラウザごとの候補コントローラーと前回の履歴結果を返し、必要なら作る。
- 触るとき: 候補の状態をブラウザごとに持つ仕組みを変えるときに見る。
- 呼び出し先: `this._suggestionMap.get()`
- 条件付き依存: `if (!data && create)` → `this._suggestionMap.set()`
- 参照: `lazy.SearchSuggestionController`

## _reply()
- 位置: L616-618
- 役割: 指定したアクターへ、種類とデータを sendAsyncMessage で返す。
- 触るとき: 応答メッセージの送り先を調べるときに見る。
- 呼び出し先: `actor.sendAsyncMessage()`

## _broadcast()
- 位置: L620-624
- 役割: 登録されている全 ContentSearch アクターへ、同じメッセージを送る。
- 触るとき: 全ページへ状態を配る処理を変えるときに見る。
- 呼び出し先: `actor.sendAsyncMessage()`

## _currentEngineObj()
- 位置: async L626-635
- 役割: 通常またはプライベートの既定エンジンの名前・アイコン・設定エンジンかを返す。
- 触るとき: 既定エンジンの表示項目を変えるときに見る。
- 呼び出し先: `lazy.SearchService.getDefault()`, `lazy.SearchService.getDefaultPrivate()`, `this._getEngineIconURL()`
- 参照: `engine.name`, `lazy.ConfigSearchEngine`

## _getEngineIconURL()
- 位置: async L656-690
- 役割: エンジンのアイコンを、そのまま渡せる URL または data/blob をバッファに変換したもの（取得失敗時は代替画像）で返す。
- 触るとき: 検索エンジンのアイコンが表示されない問題を調べるときに見る。
- 呼び出し先: `console.error()`, `engine.getIconURL()`, `fetch()`, `response.arrayBuffer()`, `response.headers.get()`, `url.startsWith()`

## _ensureDataHasProperties()
- 位置: L692-698
- 役割: メッセージデータに必要なキーが無ければ例外を投げる。
- 触るとき: 子から届くデータの必須項目を増やすときに見る。

## _initService()
- 位置: L700-705
- 役割: 検索サービスの初期化を一度だけ開始し、その Promise を返す。
- 触るとき: 検索サービス初期化前の要求が失敗する問題を調べるときに見る。
- 条件付き依存: `if (!this._initServicePromise)` → `lazy.SearchService.init()`
- 参照: `this._initServicePromise`

## ContentSearchParent.constructor()
- 位置: L709-713
- 役割: 検索 UI を初期化し、自分のアクターを全体の一覧に加える。
- 触るとき: ページごとのアクター生成時の登録を変えるときに見る。
- 呼び出し先: `ContentSearch.init()`, `gContentSearchActors.add()`, `super()`

## ContentSearchParent.didDestroy()
- 位置: L715-717
- 役割: アクターを全体の一覧から外す。
- 触るとき: 破棄済みのアクターへ送って失敗する問題を調べるときに見る。
- 呼び出し先: `gContentSearchActors.delete()`

## ContentSearchParent.receiveMessage()
- 位置: L719-757
- 役割: メッセージを一時的なイベント項目にしてキューへ積み、Search なら同じブラウザの候補取得を取り消す。
- 触るとき: 子からの要求の受付・順序を変えるときに見る。
- 呼び出し先: `ContentSearch._eventQueue.push()`, `ContentSearch._processEventQueue()`, `browser.addEventListener()`
- 条件付き依存: `if (msg.name === "Search")` → `ContentSearch._cancelSuggestions()`
- 参照: `msg.data`, `msg.name`, `this.browsingContext.top.embedderElement`

## handleEvent()
- 位置: L736-745
- 役割: ドキュメントの入れ替えでブラウザが変わったとき、候補データと監視対象を新しいブラウザへ付け替える。
- 触るとき: タブの入れ替え後に検索の候補や応答が届かない問題を調べるときに見る。要確認: 外すリスナーが最初の browser を指しており、2 回目以降の入れ替えで古い要素に登録が残る可能性がある。
- 呼び出し先: `ContentSearch._suggestionMap.get()`, `browser.removeEventListener()`, `eventItem.browser.addEventListener()`
- 条件付き依存: `if (browserData)` → `ContentSearch._suggestionMap.delete()`
- 条件付き依存: `if (browserData)` → `ContentSearch._suggestionMap.set()`
- 参照: `event.detail`, `eventItem.browser`
