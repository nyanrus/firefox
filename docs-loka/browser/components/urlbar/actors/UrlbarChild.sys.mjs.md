# browser/components/urlbar/actors/UrlbarChild.sys.mjs

source: browser/components/urlbar/actors/UrlbarChild.sys.mjs
source-hash: 7a1929d5c43c0e56fe48f68213746a504c5ed21b
lines: 304

## <module>
- 役割: urlbar のメッセージパス用アクターの子側。content に公開するポートを作り、親側からの操作要求を許可リストの範囲で実行する。
- 呼び出し先: `XPCOMUtils.declareLazy()`, `this.#childControllers.delete()`, `this.#maybeSendAsyncMessage()`

## UrlbarChild.#maybeSendAsyncMessage()
- 位置: L60-70
- 役割: アクターが破棄されていなければ sendAsyncMessage を送る。破棄による InvalidStateError は無視する。
- 触るとき: 破棄済みの入力から通知が飛んでエラーになる問題を調べるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `ex.name`

## UrlbarChild.#maybeSendQuery()
- 位置: async L80-92
- 役割: sendQuery を送る。送信前に破棄された(InvalidStateError)か、送信中に破棄された(AbortError)場合は、解決しない Promise を返す。
- 触るとき: 入力を閉じた直後のクエリの扱いや、待ち続けるプロミスを調べるときに見る。
- 呼び出し先: `this.sendQuery()`
- 参照: `ex.name`

## UrlbarChild.#wrapPromise()
- 位置: L106-121
- 役割: 特権側の Promise を content のレルムで扱える Promise に変換する。結果は cloneInto で複製し、拒否時は message だけを持つ content 側の Error に作り直す。
- 触るとき: content に渡る値やエラーに特権オブジェクトやスタックが混ざらないようにする箇所を変えるときに見る。
- 呼び出し先: `Cu.cloneInto()`, `String()`, `promise.then()`, `reject()`, `resolve()`
- 参照: `ex?.message`, `win.Error`, `win.Promise`

## UrlbarChild.#forContent()
- 位置: L133-137
- 役割: 非特権の content ウィンドウ向けに引数を cloneInto で content レルムへ複製する。親プロセスでは何もせず返す。
- 触るとき: 親から受けた引数を content のスクリプトが読めない(Xray で拒否される)ときに見る。
- 呼び出し先: `Cu.cloneInto()`, `Cu.waiveXrays()`
- 参照: `this.contentWindow`, `this.manager.parentActor`

## UrlbarChild.exposePort()
- 位置: L153-162
- 役割: createPort で作ったポートを window.UrlbarActorPort として公開する。非特権の window では Xray を外し、cloneInto で複製する。
- 触るとき: メッセージパスの <moz-urlbar> が公開 API を取得できない問題を調べるときに見る。content に新しい機能を渡すときもここに追加する。
- 呼び出し先: `Cu.cloneInto()`, `Cu.waiveXrays()`, `this.createPort()`
- 参照: `this.contentWindow`, `this.manager.parentActor`, `win.UrlbarActorPort`

## UrlbarChild.createPort()
- 位置: L170-207
- 役割: content に見せるポートのオブジェクトを作る。メッセージ送信、クエリ、入力の登録、リンクの開き方、fixup、pref の取得と監視などを含む。
- 触るとき: content から使える API を増減させるときに見る。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.UrlbarPrefs.addObserver.bind()`, `lazy.UrlbarPrefs.removeObserver.bind()`, `lazy.UrlbarPrefs.toggleResultMenuKeyboardAccessible.bind()`, `this.#maybeSendAsyncMessage.bind()`, `this.registerChildController.bind()`, `this.registerMessagePathInput.bind()`
- 参照: `UrlbarContentUtils.getDisplaySpec`, `UrlbarContentUtils.getPlatform`, `UrlbarContentUtils.getSupportUrl`, `UrlbarContentUtils.isTextDirectionRTL`, `UrlbarContentUtils.unEscapeURIForUI`, `UrlbarContentUtils.whereToOpenLink`, `UrlbarContentUtils.willLoadInBackground`, `lazy.UrlbarPrefs`, `this.contentWindow`

## sendQuery()
- 位置: L174-177
- 役割: 非特権の window では #wrapPromise で包んだ sendQuery を、特権側では直接 sendQuery を呼ぶ。
- 触るとき: content からのクエリの戻り値の型が期待と違うときに見る。
- 呼び出し先: `this.#maybeSendQuery()`, `this.#wrapPromise()`, `this.sendQuery()`

## getFixupPrimitives()
- 位置: L183-187
- 役割: UrlbarContentUtils.getFixupPrimitives の結果を #forWindow で渡す。
- 触るとき: content 側で fixup 結果が読めないときに見る。
- 呼び出し先: `UrlbarContentUtils.getFixupPrimitives()`, `this.#forWindow()`

## getPref()
- 位置: L197-197
- 役割: UrlbarPrefs.get の値を #forWindow で window に渡す。
- 触るとき: content の urlbar が pref の値を正しく読めないときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.#forWindow()`

## UrlbarChild.#forWindow()
- 位置: L218-220
- 役割: 親プロセスならそのまま、content プロセスなら値を cloneInto で window に複製して返す。
- 触るとき: ポート経由で返す値が content で読めないときに見る。
- 呼び出し先: `Cu.cloneInto()`
- 参照: `this.manager.parentActor`

## UrlbarChild.handleEvent()
- 位置: L227-234
- 役割: DOMDocElementInserted で呼ばれ、メッセージパスを使う場合に exposePort を実行する。
- 触るとき: ページ読込み直後に UrlbarActorPort が無い問題を調べるときに見る。
- 呼び出し先: `UrlbarContentUtils.usesMessagePath()`
- 条件付き依存: `if (UrlbarContentUtils.usesMessagePath())` → `this.exposePort()`

## UrlbarChild.registerMessagePathInput()
- 位置: L245-249
- 役割: 入力に ID を振り、入力が GC されたときに Destroy を送る登録をして、その ID を返す。
- 触るとき: 入力の破棄時に親側のコントローラーが残ってしまう問題を調べるときに見る。
- 呼び出し先: `this.#destroyRegistry.register()`
- 参照: `this.#nextInstanceId`

## UrlbarChild.registerChildController()
- 位置: L261-263
- 役割: ID ごとに子側コントローラーを WeakRef で保持し、親からの通知を届けられるようにする。
- 触るとき: 親からの通知が子のコントローラーに届かない問題を調べるときに見る。
- 呼び出し先: `this.#childControllers.set()`

## UrlbarChild.receiveMessage()
- 位置: L265-271
- 役割: InvokeContentAction のメッセージを #invokeContentAction に渡す。
- 触るとき: 親から content の操作を呼ぶ経路を追うときに見る。
- 呼び出し先: `this.#invokeContentAction()`
- 参照: `message.data`, `message.name`

## UrlbarChild.#invokeContentAction()
- 位置: L284-302
- 役割: 親が指定したコントローラー、入力、ビューのメソッドを呼ぶ。INVOKABLE_CONTENT_ACTIONS の許可リストにないメソッドは例外にする。content では Xray を外して呼ぶ。
- 触るとき: 親から呼べる操作を増やすとき、または「disallowed content action」の例外が出るときに見る。
- 呼び出し先: `allowlist?.includes()`, `receiver?.[method]()`, `this.#childControllers.get()`, `this.#childControllers.get(instanceId)?.deref()`, `this.#forContent()`
- 条件付き依存: `if (!child)` → `this.#childControllers.delete()`
- 条件付き依存: `if (!this.manager.parentActor)` → `Cu.waiveXrays()`
- 参照: `lazy.UrlbarShared.INVOKABLE_CONTENT_ACTIONS`, `this.manager.parentActor`
