# browser/components/asrouter/actors/ASRouterParent.sys.mjs

source: browser/components/asrouter/actors/ASRouterParent.sys.mjs
source-hash: 779bb026caf98a56605def0a0893f2c8198aac1b
lines: 98

## <module>
- 役割: about:newtab などのページごとの ASRouter 親側アクターと、それらをまとめる ASRouterTabs を定義する。
- 呼び出し先: `ChromeUtils.importESModule()`

## ASRouterTabs.constructor()
- 位置: L17-36
- 役割: ASRouterNewTabHook のインスタンスを作って初期化し、接続時にメッセージ転送用の関数を渡す。切断用の destroy も登録する。
- 触るとき: ASRouter の初期化順やページ間の共有状態を変えるとき。
- 呼び出し先: `ASRouterDefaultConfig()`, `asRouterNewTabHook .getInstance()`, `asRouterNewTabHook .getInstance() .then()`, `asRouterNewTabHook.createInstance()`, `initializer.connect()`
- 参照: `this.actors`, `this.destroy`, `this.loadingMessageHandler`

## this.destroy()
- 位置: L19-19
- 役割: 初期化前に呼ばれても何もしない空の destroy。
- 触るとき: 初期化完了前の破棄で例外が出る問題を調べるとき。

## clearChildMessages()
- 位置: L27-27
- 役割: 接続中の全ページに ClearMessages を送る。
- 触るとき: メッセージのクリアがページに届かないと調べるとき。
- 呼び出し先: `this.messageAll()`

## clearChildProviders()
- 位置: L28-28
- 役割: 接続中の全ページに ClearProviders を送る。
- 触るとき: プロバイダ単位のクリアを追うとき。
- 呼び出し先: `this.messageAll()`

## updateAdminState()
- 位置: L29-29
- 役割: 接続中の全ページに UpdateAdminState を送る。
- 触るとき: 管理者設定の変更をページへ反映させるとき。
- 呼び出し先: `this.messageAll()`

## this.destroy()
- 位置: L31-33
- 役割: ハンドラの切断を行い、接続済みの initializer を解放する。
- 触るとき: ASRouter を終了する経路で解放漏れがないか確認するとき。
- 呼び出し先: `initializer.disconnect()`

## ASRouterTabs.size()
- 位置: L38-40
- 役割: 登録されている親アクターの数を返す。
- 触るとき: 最後のページが閉じたときに共有状態を破棄する条件を変えるとき。
- 参照: `this.actors.size`

## ASRouterTabs.messageAll()
- 位置: L42-46
- 役割: 登録済みの全アクターに同じメッセージを送り、全部の完了を待つ Promise を返す。
- 触るとき: 全ページへの一斉通知が一部だけ届く問題を調べるとき。
- 呼び出し先: `Promise.all()`, `[...this.actors].map()`, `a.sendAsyncMessage()`
- 参照: `this.actors`

## ASRouterTabs.registerActor()
- 位置: L48-50
- 役割: 新しい親アクターを actors に追加する。
- 触るとき: ページ生成時の登録処理を変えるとき。
- 呼び出し先: `this.actors.add()`

## ASRouterTabs.unregisterActor()
- 位置: L52-54
- 役割: 親アクターを actors から削除する。
- 触るとき: ページ破棄後も通知が飛ぶ問題を調べるとき。
- 呼び出し先: `this.actors.delete()`

## defaultTabsFactory()
- 位置: L57-58
- 役割: 既定の ASRouterNewTabHook を渡して ASRouterTabs を作る。
- 触るとき: テストで別の tabs 実装を差し込む経路を変えるとき。

## ASRouterParent.constructor()
- 位置: L65-68
- 役割: tabsFactory を受け取り保持する。省略時は defaultTabsFactory を使う。
- 触るとき: テストや別環境で tabsFactory を差し替えるとき。
- 呼び出し先: `super()`
- 参照: `this.tabsFactory`

## ASRouterParent.actorCreated()
- 位置: L70-75
- 役割: 共有の ASRouterParent.tabs を未作成なら作り、このアクターに一意の tabId を振って登録する。
- 触るとき: タブごとの ID 採番やアクターの登録タイミングを変えるとき。
- 呼び出し先: `ASRouterParent.tabs.registerActor()`, `this.tabsFactory()`
- 参照: `ASRouterParent.nextTabId`, `ASRouterParent.tabs`, `this.tabId`, `this.tabsFactory`

## ASRouterParent.didDestroy()
- 位置: L77-83
- 役割: アクターを解除し、残りが 0 になったら tabs を破棄して null に戻す。
- 触るとき: 最後のタブを閉じた後にリソースが残る問題を調べるとき。
- 呼び出し先: `ASRouterParent.tabs.unregisterActor()`
- 条件付き依存: `if (ASRouterParent.tabs.size < 1)` → `ASRouterParent.tabs.destroy()`
- 参照: `ASRouterParent.tabs`, `ASRouterParent.tabs.size`

## ASRouterParent.getTab()
- 位置: L85-90
- 役割: tabId と埋め込み要素(embedderElement)を持つタブ情報を返す。
- 触るとき: メッセージ処理にタブ情報が正しく渡らないと調べるとき。
- 参照: `this.browsingContext.embedderElement`, `this.tabId`

## ASRouterParent.receiveMessage()
- 位置: L92-96
- 役割: ページからのメッセージを、接続済みハンドラの handleMessage にタブ情報付きで渡す。
- 触るとき: ページからの要求がハンドラに届かない、またはタブ情報が欠けると調べるとき。
- 呼び出し先: `ASRouterParent.tabs.loadingMessageHandler.then()`, `handler.handleMessage()`, `this.getTab()`
