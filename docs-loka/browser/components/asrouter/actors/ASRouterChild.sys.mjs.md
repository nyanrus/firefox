# browser/components/asrouter/actors/ASRouterChild.sys.mjs

source: browser/components/asrouter/actors/ASRouterChild.sys.mjs
source-hash: 2f3879e93bc5641072e2626e1681d8f2377190c3
lines: 119

## <module>
- 役割: 親プロセスの ASRouter と、コンテンツ側ページの間をつなぐ JSWindowActor の子側。ページに ASRouterMessage などの関数を公開する。
- 呼び出し先: `ChromeUtils.importESModule()`

## ASRouterChild.constructor()
- 位置: L18-21
- 役割: 購読者を保持する observers セットを空で作る。
- 触るとき: 子アクターが持つ状態を増やすとき。
- 呼び出し先: `super()`
- 参照: `this.observers`

## ASRouterChild.didDestroy()
- 位置: L23-25
- 役割: アクターの破棄時に observers を空にして、解放後のリスナー呼び出しを防ぐ。
- 触るとき: ページ遷移で古いリスナーが残る不具合を調べるとき。
- 呼び出し先: `this.observers.clear()`

## ASRouterChild.actorCreated()
- 位置: L27-41
- 役割: contentWindow に ASRouterMessage、ASRouterAddParentListener、ASRouterRemoveParentListener を exportFunction で公開する。
- 触るとき: ページ側から呼べる API 名を追加・改名するとき、または about:blank 再利用時の二重公開を調べるとき。
- 呼び出し先: `Cu.exportFunction()`, `this.addParentListener.bind()`, `this.asRouterMessage.bind()`, `this.removeParentListener.bind()`
- 参照: `this.contentWindow`

## ASRouterChild.handleEvent()
- 位置: L43-45
- 役割: 何もしない。DOMDocElementCreated はアクター生成のためだけに使われる。
- 触るとき: イベントリスナーの登録を増やすとき(ここは空のままでよいか確認する)。

## ASRouterChild.addParentListener()
- 位置: L47-49
- 役割: ページ側から渡されたリスナーを observers に追加する。
- 触るとき: 親からページへの通知を受けるリスナーの登録経路を変えるとき。
- 呼び出し先: `this.observers.add()`

## ASRouterChild.removeParentListener()
- 位置: L51-53
- 役割: 渡されたリスナーを observers から削除する。
- 触るとき: リスナー解除が効かない問題を追うとき。
- 呼び出し先: `this.observers.delete()`

## ASRouterChild.receiveMessage()
- 位置: L55-72
- 役割: 親から UpdateAdminState と ClearProviders を受け、各リスナーにページ側の構造として複製して渡す。
- 触るとき: 親からページへ新しい種類の通知を流す追加をするとき。
- 呼び出し先: `Cu.cloneInto()`, `listener()`, `this.observers.forEach()`
- 参照: `this.contentWindow`

## ASRouterChild.wrapPromise()
- 位置: L74-78
- 役割: 通常の Promise をページの window の Promise に包み直す。
- 触るとき: ページ側に返す Promise の型の問題を調べるとき。
- 呼び出し先: `promise.then()`
- 参照: `this.contentWindow.Promise`

## ASRouterChild.sendQuery()
- 位置: L80-88
- 役割: 親へ問い合わせを送り、応答をページ側の構造に複製して返す。
- 触るとき: 応答が必要なメッセージを増やすとき、または応答の値がページで読めないと調べるとき。
- 呼び出し先: `Cu.cloneInto()`, `resolve()`, `super.sendQuery()`, `super.sendQuery(aName, aData).then()`, `this.wrapPromise()`
- 参照: `this.contentWindow`

## ASRouterChild.asRouterMessage()
- 位置: L90-117
- 役割: ページからのメッセージを型で振り分け、通知系は sendAsyncMessage、応答が要る型は sendQuery で親へ送る。許可されない型は例外にする。
- 触るとき: 新しいメッセージ型を追加するとき、または Unexpected type の例外が出る理由を調べるとき。
- 呼び出し先: `VALID_TYPES.has()`
- 条件付き依存: `if (type === "NEWTAB_MESSAGE_REQUEST")` → `this.wrapPromise()`
- 条件付き依存: `if (type === "NEWTAB_MESSAGE_REQUEST")` → `Promise.resolve()`
- 条件付き依存: `if (VALID_TYPES.has(type))` → `this.sendAsyncMessage()`
- 条件付き依存: `if (VALID_TYPES.has(type))` → `this.sendQuery()`
- 参照: `msg.DISABLE_PROVIDER`, `msg.ENABLE_PROVIDER`, `msg.EXPIRE_QUERY_CACHE`, `msg.FORCE_PRIVATE_BROWSING_WINDOW`, `msg.IMPRESSION`, `msg.RESET_PROVIDER_PREF`, `msg.SET_PROVIDER_USER_PREF`, `msg.USER_ACTION`
