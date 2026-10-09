# browser/components/extensions/child/ext-devtools-panels.js

source: browser/components/extensions/child/ext-devtools-panels.js
source-hash: 4b38bd50517794fcd20bdc433ae4978967d43b6e
lines: 325

## <module>
- 役割: devtools.panels の子側 API を定義する。拡張のパネルとインスペクターのサイドバーを親プロセスと連携して作り、テーマ名と変更通知を公開する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyGlobalGetters()`

## ChildDevToolsPanel.constructor()
- 位置: L30-42
- 役割: 拡張コンテキストに自身を登録し、親とパネル表示や非表示のメッセージを送受信する conduit を開く。
- 触るとき: パネルを作ったときに必要な購読や終了時の後始末を変えるとき。
- 呼び出し先: `context.openConduit()`, `super()`, `this.context.callOnClose()`
- 参照: `this._panelContext`, `this.conduit`, `this.context`, `this.id`

## ChildDevToolsPanel.panelContext()
- 位置: L44-67
- 役割: 拡張のビューから、このパネルの toolbox panel ID に一致する devtools_panel を探して保持する。見つからなければ null を返す。
- 触るとき: パネルの文書を見つける条件を変えるとき。閉じられたら保持を解除する。
- 条件付き依存: `if ( view.viewType === "devtools_panel" && view.devtoolsToolboxInfo.toolboxPanelId === this.id )` → `view.callOnClose()`
- 参照: `this._panelContext`, `this.context.extension.devtoolsViews`, `this.id`, `view.devtoolsToolboxInfo.toolboxPanelId`, `view.viewType`

## close()
- 位置: L58-60
- 役割: パネルのビューが閉じられたとき、保持していたパネルの文脈を外す。
- 触るとき: パネルを閉じた後に古い参照が残らないかを確かめるとき。
- 参照: `this._panelContext`

## ChildDevToolsPanel.recvPanelShown()
- 位置: L69-81
- 役割: 文書が読み込まれてから、shown イベントを発火させる。文書がまだ無ければ何もしない。
- 触るとき: パネルが表示されたときに拡張へ届くタイミングを変えるとき。
- 呼び出し先: `promiseDocumentLoaded()`, `promiseDocumentLoaded(document).then()`, `this.emit()`
- 参照: `this.panelContext`, `this.panelContext.contentWindow`

## ChildDevToolsPanel.recvPanelHidden()
- 位置: L83-85
- 役割: 親からパネル非表示の通知を受けて、hidden イベントを発火させる。
- 触るとき: 非表示の通知の扱いを変えるとき。
- 呼び出し先: `this.emit()`

## ChildDevToolsPanel.api()
- 位置: L87-119
- 役割: onShown と onHidden の EventManager を作り、拡張に公開する。
- 触るとき: 拡張に公開するパネルのイベントを増やすとき。onSearch やステータスバーのボタンは TODO のまま未実装。
- 参照: `this.context`

## register()
- 位置: L92-100
- 役割: shown イベントの購読を登録し、解除関数を返す。拡張にはパネルの content window を渡す。
- 触るとき: onShown の登録と解除の仕組みを変えるとき。
- 呼び出し先: `this.off()`, `this.on()`

## listener()
- 位置: L93-95
- 役割: shown イベントを受けて、content window を拡張へ発火させる。
- 触るとき: 拡張へ渡す onShown の引数を変えるとき。
- 呼び出し先: `fire.asyncWithoutClone()`

## register()
- 位置: L106-114
- 役割: hidden イベントの購読を登録し、解除関数を返す。
- 触るとき: onHidden の登録と解除の仕組みを変えるとき。
- 呼び出し先: `this.off()`, `this.on()`

## listener()
- 位置: L107-109
- 役割: hidden イベントを受けて、拡張へ引数なしで発火させる。
- 触るとき: onHidden の発火の仕方を変えるとき。
- 呼び出し先: `fire.async()`

## ChildDevToolsPanel.close()
- 位置: L121-124
- 役割: パネルの文脈と拡張の参照を外す。
- 触るとき: 拡張が閉じられた後の後始末を確かめるとき。
- 参照: `this._panelContext`, `this.context`

## ChildDevToolsInspectorSidebar.constructor()
- 位置: L137-148
- 役割: 拡張コンテキストに自身を登録し、親とサイドバー表示や非表示の通知を受け取る conduit を開く。
- 触るとき: サイドバーを作った時の購読や後始末を変えるとき。
- 呼び出し先: `context.openConduit()`, `super()`, `this.context.callOnClose()`
- 参照: `this.conduit`, `this.context`, `this.id`

## ChildDevToolsInspectorSidebar.close()
- 位置: L150-152
- 役割: 拡張コンテキストの参照を外す。
- 触るとき: サイドバーの後始末を確かめるとき。
- 参照: `this.context`

## ChildDevToolsInspectorSidebar.recvInspectorSidebarShown()
- 位置: L154-157
- 役割: 親からサイドバー表示の通知を受けて、shown を発火させる。TODO のとおり content window は渡していない。
- 触るとき: サイドバーの表示通知の扱いを変えるとき。
- 呼び出し先: `this.emit()`

## ChildDevToolsInspectorSidebar.recvInspectorSidebarHidden()
- 位置: L159-161
- 役割: 親からサイドバー非表示の通知を受けて、hidden を発火させる。
- 触るとき: 非表示の通知の扱いを変えるとき。
- 呼び出し先: `this.emit()`

## ChildDevToolsInspectorSidebar.api()
- 位置: L163-242
- 役割: onShown、onHidden、setPage、setObject、setExpression を持つ API を作る。setPage の URL は拡張内の URL に限って解決する。
- 触るとき: サイドバーに拡張が使える操作を増やすか、その検証を変えるとき。
- 参照: `context.uri.spec`

## resolveExtensionURL()
- 位置: L171-184
- 役割: 渡された URL を拡張の URL に対して解決し、プロトコルかホストが違えばエラーにする。
- 触るとき: サイドバーに表示できる URL の範囲を変えるとき。
- 参照: `context.cloneScope.Error`, `context.uri.spec`, `extensionURL.host`, `extensionURL.protocol`, `sidebarPageURL.host`, `sidebarPageURL.href`, `sidebarPageURL.protocol`

## register()
- 位置: L190-198
- 役割: サイドバーの shown イベントの購読を登録し、解除関数を返す。
- 触るとき: サイドバーの onShown の仕組みを変えるとき。
- 呼び出し先: `this.off()`, `this.on()`

## listener()
- 位置: L191-193
- 役割: shown イベントを受けて、拡張へ発火させる。
- 触るとき: サイドバーの onShown の引数を変えるとき。
- 呼び出し先: `fire.asyncWithoutClone()`

## register()
- 位置: L204-212
- 役割: サイドバーの hidden イベントの購読を登録し、解除関数を返す。
- 触るとき: サイドバーの onHidden の仕組みを変えるとき。
- 呼び出し先: `this.off()`, `this.on()`

## listener()
- 位置: L205-207
- 役割: hidden イベントを受けて、拡張へ発火させる。
- 触るとき: サイドバーの onHidden の発火の仕方を変えるとき。
- 呼び出し先: `fire.async()`

## ChildDevToolsInspectorSidebar.setPage()
- 位置: L215-222
- 役割: 検証した URL を親の devtools.panels.elements.Sidebar.setPage に渡す。
- 触るとき: サイドバーに表示するページの受け渡しを変えるとき。
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `resolveExtensionURL()`

## ChildDevToolsInspectorSidebar.setObject()
- 位置: L224-231
- 役割: 次の tick で、JSON オブジェクトとタイトルを親の setObject に渡す。
- 触るとき: サイドバーに JSON を表示する経路を変えるとき。
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `context.cloneScope.Promise.resolve()`, `context.cloneScope.Promise.resolve().then()`

## ChildDevToolsInspectorSidebar.setExpression()
- 位置: L233-240
- 役割: 次の tick で、評価式とタイトルを親の setExpression に渡す。
- 触るとき: サイドバーに式の結果を表示する経路を変えるとき。
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `context.cloneScope.Promise.resolve()`, `context.cloneScope.Promise.resolve().then()`

## getAPI()
- 位置: L246-323
- 役割: devtools.panels の API を組み立てる。テーマ監視を取得し、createSidebarPane、create、themeName、onThemeChanged を公開する。
- 触るとき: devtools.panels の公開範囲を増やすとき。
- 呼び出し先: `ExtensionChildDevToolsUtils.getThemeChangeObserver()`

## createSidebarPane()
- 位置: L254-278
- 役割: 親でサイドバーを作って ID を受け取り、それを使う ChildDevToolsInspectorSidebar の API を拡張側へ複製して返す。
- 触るとき: サイドバーを作る流れや、返すオブジェクトの複製の仕方を変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `context.childManager.callParentAsyncFunction()`, `context.cloneScope.Promise.resolve()`, `context.cloneScope.Promise.resolve().then()`, `sidebar.api()`
- 参照: `context.cloneScope`

## create()
- 位置: L280-303
- 役割: 親でパネルを作って ID を受け取り、ChildDevToolsPanel の API を拡張側へ複製して返す。
- 触るとき: パネルを作る流れや、返すオブジェクトの複製の仕方を変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `context.childManager.callParentAsyncFunction()`, `context.cloneScope.Promise.resolve()`, `context.cloneScope.Promise.resolve().then()`, `devtoolsPanel.api()`
- 参照: `context.cloneScope`

## themeName()
- 位置: L304-306
- 役割: テーマ変更の監視が持つ現在のテーマ名を返す。
- 触るとき: 拡張がテーマ名を読む経路を変えるとき。
- 参照: `themeChangeObserver.themeName`

## register()
- 位置: L310-318
- 役割: テーマ変更の監視で themeChanged を購読し、解除関数を返す。
- 触るとき: onThemeChanged の登録と解除の仕組みを変えるとき。
- 呼び出し先: `themeChangeObserver.off()`, `themeChangeObserver.on()`

## listener()
- 位置: L311-313
- 役割: テーマ名を受けて、拡張へ非同期に発火させる。
- 触るとき: onThemeChanged の引数を変えるとき。
- 呼び出し先: `fire.async()`
