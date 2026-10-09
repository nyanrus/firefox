# browser/components/extensions/parent/ext-devtools-panels.js

source: browser/components/extensions/parent/ext-devtools-panels.js
source-hash: a4d13753d30e52c4da62c9f3ee43226628c1d44c
lines: 739

## <module>
- 役割: devtools.panels API を実装し、拡張の devtools パネルとインスペクターサイドバーを、ツールボックス上への読み込みと表示状態の通知で管理する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## BaseDevToolsPanel.constructor()
- 位置: L20-41
- 役割: ツールボックスを取り出して拡張の文脈・パネル ID・オプションを保持し、ツールボックスが無ければ例外を投げる。
- 触るとき: パネル生成時にツールボックスが渡らない不具合や、保持する項目を増やすときに見る。
- 条件付き依存: `if (!toolbox)` → `Error()`
- 参照: `context.devToolsToolbox`, `context.extension`, `panelOptions.id`, `this.browser`, `this.browserContainerWindow`, `this.context`, `this.extension`, `this.id`, `this.panelOptions`, `this.toolbox`, `this.unwatchExtensionProxyContextLoad`, `this.viewType`

## BaseDevToolsPanel.createBrowserElement()
- 位置: async L43-91
- 役割: パネル用の browser 要素を作り、拡張コンテキストの読み込みを監視し、ズームを同期してパネルの URL を読み込む。
- 触るとき: パネルの読み込み先や toolbox 情報の渡し方、トップレベルコンテキストの取得を変えるとき。
- 呼び出し先: `getTargetTabIdForToolbox()`, `this.browser.fixupAndLoadURIString()`, `this.syncToolboxZoom()`, `this.toolbox.win.browsingContext.embedderElement.addEventListener()`, `watchExtensionProxyContextLoad()`, `window.getBrowser()`
- 条件付き依存: `if (this._resolveTopLevelContext)` → `this._resolveTopLevelContext()`
- 参照: `context.devToolsToolbox`, `this._resolveTopLevelContext`, `this.browser`, `this.context`, `this.context.principal`, `this.id`, `this.panelOptions`, `this.unwatchExtensionProxyContextLoad`

## BaseDevToolsPanel.handleEvent()
- 位置: L93-100
- 役割: FullZoomChange を受けてツールボックスのズームをパネルに同期する。
- 触るとき: ズームを変えてもパネルの拡大率が追従しないときに調べる。
- 呼び出し先: `this.syncToolboxZoom()`
- 参照: `event.type`

## BaseDevToolsPanel.syncToolboxZoom()
- 位置: L113-119
- 役割: ツールボックスのズーム値をパネルの browser に設定する。リモート browser がズームを継承しないための回避策。
- 触るとき: パネルの拡大率がツールボックスとずれる問題を調べるとき。
- 参照: `this.browser`, `this.browser.fullZoom`, `this.toolbox.win.browsingContext.fullZoom`

## BaseDevToolsPanel.destroyBrowserElement()
- 位置: L121-139
- 役割: コンテキスト読み込みの監視を解除し、ズームの購読を外して、パネルの browser 要素を削除する。
- 触るとき: パネル削除後にリスナーや browser 要素が残るときに確認する。
- 条件付き依存: `if (unwatchExtensionProxyContextLoad)` → `unwatchExtensionProxyContextLoad()`
- 条件付き依存: `if (this.toolbox)` → `this.toolbox.win.browsingContext.embedderElement.removeEventListener()`
- 条件付き依存: `if (browser)` → `browser.remove()`
- 参照: `this.browser`, `this.toolbox`, `this.unwatchExtensionProxyContextLoad`

## ParentDevToolsPanel.constructor()
- 位置: L159-182
- 役割: 表示状態を初期化し、可視性通知用の conduit を作り、トップレベルコンテキストの待ち Promise を用意してから addPanel でツールに登録する。
- 触るとき: 拡張のパネル生成時に表示イベントが届かない、または登録が遅れる問題を調べるとき。
- 呼び出し先: `super()`, `this.addPanel()`, `this.context.callOnClose()`, `this.onToolboxHostChanged.bind()`, `this.onToolboxHostWillChange.bind()`, `this.onToolboxPanelSelect.bind()`
- 参照: `this._resolveTopLevelContext`, `this.conduit`, `this.destroyed`, `this.id`, `this.onToolboxHostChanged`, `this.onToolboxHostWillChange`, `this.onToolboxPanelSelect`, `this.panelAdded`, `this.visible`, `this.waitTopLevelContext`

## ParentDevToolsPanel.addPanel()
- 位置: L184-212
- 役割: アイコン・タイトル・ローカルタブ限定の対応判定・build 関数を付けて、ツールボックスに追加ツールとして登録する。
- 触るとき: devtools パネルの表示名、アイコン、対応するツールボックスの条件を変えるとき。
- 呼び出し先: `this.toolbox.addAdditionalTool()`
- 参照: `this.context.extension.id`, `this.context.extension.name`, `this.id`, `this.panelAdded`, `this.panelOptions`

## isToolSupported()
- 位置: L197-197
- 役割: ツールボックスがローカルタブの場合にだけ、パネルを対応ツールとして扱う。
- 触るとき: リモートのツールボックスにもパネルを出すかどうかを変えるとき。
- 参照: `toolbox.commands.descriptorFront.isLocalTab`

## build()
- 位置: L198-208
- 役割: ツールボックスの一致を確かめてからパネルを構築し、ツールボックスと破棄関数を返す。一致しなければ例外を投げる。
- 触るとき: パネルの構築先の検証や、破棄処理の戻し方を変えるとき。
- 呼び出し先: `this.buildPanel()`
- 参照: `this.toolbox`

## ParentDevToolsPanel.buildPanel()
- 位置: L214-240
- 役割: パネルの browser を作り、select・host 変更のイベントを購読する。返す関数で破棄時にそれらを外す。
- 触るとき: パネルの非表示・再表示やドック切り替え時の購読の扱いを見直すとき。
- 呼び出し先: `this.createBrowserElement()`, `this.destroyBrowserElement()`, `toolbox.off()`, `toolbox.on()`
- 参照: `this.browserContainerWindow`, `this.onToolboxHostChanged`, `this.onToolboxHostWillChange`, `this.onToolboxPanelSelect`

## ParentDevToolsPanel.onToolboxHostWillChange()
- 位置: L242-258
- 役割: ホスト変更の前に、表示中なら hidden を送り、browser 要素を破棄する。
- 触るとき: ドックとアンドックを切り替えた際にパネルの表示が崩れる問題を調べるとき。
- 条件付き依存: `if (this.visible)` → `this.conduit.sendPanelHidden()`
- 条件付き依存: `if (this.browser)` → `this.destroyBrowserElement()`
- 参照: `this.browser`, `this.id`, `this.visible`

## ParentDevToolsPanel.onToolboxHostChanged()
- 位置: async L260-272
- 役割: ホスト変更後に browser 要素を作り直し、表示中だった場合はコンテキストの準備を待ってから shown を送る。
- 触るとき: ホスト切り替え後にパネルが再表示されない問題を調べるとき。
- 条件付き依存: `if (this.browserContainerWindow)` → `this.createBrowserElement()`
- 条件付き依存: `if (this.visible)` → `this.conduit.sendPanelShown()`
- 参照: `this.browserContainerWindow`, `this.id`, `this.visible`, `this.waitTopLevelContext`

## ParentDevToolsPanel.onToolboxPanelSelect()
- 位置: async L274-289
- 役割: 選択されたツールが自分かどうかで表示状態を判定し、変わったときだけ shown か hidden を送る。
- 触るとき: パネルの表示・非表示イベントが拡張に正しく届かないときに確認する。
- 条件付き依存: `if (!this.visible && id === this.id)` → `this.conduit.sendPanelShown()`
- 条件付き依存: `if (this.visible && id !== this.id)` → `this.conduit.sendPanelHidden()`
- 参照: `this.id`, `this.panelAdded`, `this.visible`, `this.waitTopLevelContext`

## ParentDevToolsPanel.close()
- 位置: L291-313
- 役割: conduit を閉じ、登録済みならパネルを破棄してツールから外し、参照を null に戻す。
- 触るとき: 拡張の終了後にパネルが残る、またはツールボックスに二重登録されるときに確認する。
- 呼び出し先: `this.conduit.close()`, `toolbox.isToolRegistered()`
- 条件付き依存: `if (this.panelAdded && toolbox.isToolRegistered(this.id))` → `this.destroyBrowserElement()`
- 条件付き依存: `if (this.panelAdded && toolbox.isToolRegistered(this.id))` → `toolbox.removeAdditionalTool()`
- 参照: `this._resolveTopLevelContext`, `this.browser`, `this.browserContainerWindow`, `this.context`, `this.id`, `this.panelAdded`, `this.toolbox`, `this.waitTopLevelContext`

## ParentDevToolsPanel.destroyBrowserElement()
- 位置: L315-324
- 役割: 基底の破棄処理を呼んだうえで、トップレベルコンテキストの待ち Promise を作り直す。
- 触るとき: パネルを再表示した後に拡張側の待ちが解決されない問題を調べるとき。
- 呼び出し先: `super.destroyBrowserElement()`
- 参照: `this._resolveTopLevelContext`, `this.waitTopLevelContext`

## DevToolsSelectionObserver.constructor()
- 位置: L328-341
- 役割: ツールボックスを保持し、コンテキストの終了時に閉じられるよう登録する。ツールボックスが無ければ例外を投げる。
- 触るとき: 要素選択の監視を始める前提が崩れたときに調べる。
- 呼び出し先: `context.callOnClose()`, `super()`, `this.onSelected.bind()`
- 条件付き依存: `if (!context.devToolsToolbox)` → `Error()`
- 参照: `context.devToolsToolbox`, `this.initialized`, `this.onSelected`, `this.toolbox`

## DevToolsSelectionObserver.on()
- 位置: L343-346
- 役割: 購読の前に遅延初期化を行い、その後で通常の on 購読を登録する。
- 触るとき: 選択変更イベントの購読順や初期化の契機を変えるとき。
- 呼び出し先: `super.on.apply()`, `this.lazyInit()`

## DevToolsSelectionObserver.once()
- 位置: L348-351
- 役割: 一回限りの購読の前にも遅延初期化を行い、その後で once を登録する。
- 触るとき: once 購読で選択変更の通知が来ない問題を調べるとき。
- 呼び出し先: `super.once.apply()`, `this.lazyInit()`

## DevToolsSelectionObserver.lazyInit()
- 位置: async L353-358
- 役割: 初回だけツールボックスの selection-changed に onSelected を登録する。
- 触るとき: 選択変更の通知がいつから届き始めるかを変えるとき。
- 条件付き依存: `if (!this.initialized)` → `this.toolbox.on()`
- 参照: `this.initialized`, `this.onSelected`

## DevToolsSelectionObserver.close()
- 位置: L360-371
- 役割: 初期化済みなら selection-changed の購読を外し、ツールボックスの参照を消して破棄済みにする。
- 触るとき: 要素選択の監視を解放した後も通知が来る問題を調べるとき。
- 条件付き依存: `if (this.initialized)` → `this.toolbox.off()`
- 参照: `this.destroyed`, `this.initialized`, `this.onSelected`, `this.toolbox`

## DevToolsSelectionObserver.onSelected()
- 位置: L373-375
- 役割: ツールボックスの選択変更を受けて、内部の selectionChanged イベントを発火する。
- 触るとき: 拡張に届く要素選択イベントの発火条件を変えるとき。
- 呼び出し先: `this.emit()`

## ParentDevToolsInspectorSidebar.constructor()
- 位置: L391-430
- 役割: サイドバー用の状態と conduit を用意し、ツールボックスのイベントを購読して、インスペクターのサイドバーを登録する。
- 触るとき: 拡張のインスペクターサイドバーの生成時の初期化順を変えるとき。
- 呼び出し先: `super()`, `this.context.callOnClose()`, `this.onExtensionPageMount.bind()`, `this.onExtensionPageUnmount.bind()`, `this.onSidebarCreated.bind()`, `this.onSidebarSelect.bind()`, `this.onToolboxHostChanged.bind()`, `this.onToolboxHostWillChange.bind()`, `this.toolbox.on()`, `this.toolbox.once()`, `this.toolbox.registerInspectorExtensionSidebar()`
- 参照: `panelOptions.title`, `this._initializeSidebar`, `this._lastExpressionResult`, `this.conduit`, `this.destroyed`, `this.id`, `this.onExtensionPageMount`, `this.onExtensionPageUnmount`, `this.onSidebarCreated`, `this.onSidebarSelect`, `this.onToolboxHostChanged`, `this.onToolboxHostWillChange`, `this.visible`

## ParentDevToolsInspectorSidebar.close()
- 位置: L432-469
- 役割: 購読と conduit を解除し、browser 要素を破棄してサイドバーの登録を外す。
- 触るとき: サイドバーを閉じた後にリスナーやサイドバーが残る問題を調べるとき。
- 呼び出し先: `this.conduit.close()`, `this.toolbox.off()`, `this.toolbox.unregisterInspectorExtensionSidebar()`
- 条件付き依存: `if (this.extensionSidebar)` → `this.extensionSidebar.off()`
- 条件付き依存: `if (this.browser)` → `this.destroyBrowserElement()`
- 参照: `this._lazySidebarInit`, `this.browser`, `this.containerEl`, `this.destroyed`, `this.extensionSidebar`, `this.id`, `this.onExtensionPageMount`, `this.onExtensionPageUnmount`, `this.onSidebarCreated`, `this.onSidebarSelect`, `this.onToolboxHostChanged`, `this.onToolboxHostWillChange`

## ParentDevToolsInspectorSidebar.onToolboxHostWillChange()
- 位置: L471-475
- 役割: ホスト変更の前に browser 要素を破棄する。
- 触るとき: インスペクターサイドバーがドック切り替え時に崩れる問題を調べるとき。
- 条件付き依存: `if (this.browser)` → `this.destroyBrowserElement()`
- 参照: `this.browser`

## ParentDevToolsInspectorSidebar.onToolboxHostChanged()
- 位置: L477-481
- 役割: ホスト変更後、コンテナとページ URL があれば browser 要素を作り直す。
- 触るとき: ドック切り替え後にサイドバーのページが表示されないときに見る。
- 条件付き依存: `if (this.containerEl && this.panelOptions.url)` → `this.createBrowserElement()`
- 参照: `this.containerEl`, `this.containerEl.contentWindow`, `this.panelOptions.url`

## ParentDevToolsInspectorSidebar.onExtensionPageMount()
- 位置: L483-499
- 役割: サイドバーのページがマウントされたら、そのコンテナで browser 要素を作る。読み込み済みなら即座に作る。
- 触るとき: 拡張ページのマウント後の待ち方(読み込み完了の判定)を変えるとき。
- 条件付き依存: `if (doc.readyState == "complete" && doc.location.href != "about:blank")` → `onLoaded()`
- 条件付き依存: `if (!(doc.readyState == "complete" && doc.location.href != "about:blank"))` → `containerEl.addEventListener()`
- 参照: `containerEl.contentDocument`, `doc.location.href`, `doc.readyState`, `this.containerEl`

## onLoaded()
- 位置: L488-490
- 役割: コンテナの content window に対して browser 要素を作成する。
- 触るとき: マウント後にサイドバーのページが表示されない問題を調べるとき。
- 呼び出し先: `this.createBrowserElement()`
- 参照: `containerEl.contentWindow`

## ParentDevToolsInspectorSidebar.onExtensionPageUnmount()
- 位置: L501-504
- 役割: コンテナの参照を消し、browser 要素を破棄する。
- 触るとき: サイドバーのページが外れた後に要素が残るときに見る。
- 呼び出し先: `this.destroyBrowserElement()`
- 参照: `this.containerEl`

## ParentDevToolsInspectorSidebar.onSidebarCreated()
- 位置: L506-518
- 役割: 作成されたサイドバーに mount と unmount を購読させ、保留していた初期化処理があれば実行する。
- 触るとき: サイドバー作成前に行った setObject や setPage が反映されないときに見る。
- 呼び出し先: `sidebar.on()`
- 条件付き依存: `if (typeof _lazySidebarInit === "function")` → `_lazySidebarInit()`
- 参照: `this._lazySidebarInit`, `this.extensionSidebar`, `this.onExtensionPageMount`, `this.onExtensionPageUnmount`

## ParentDevToolsInspectorSidebar.onSidebarSelect()
- 位置: L520-532
- 役割: サイドバーの選択が変わったときに表示状態を判定し、shown か hidden を送る。
- 触るとき: サイドバーの表示・非表示イベントが届かないときに確認する。
- 条件付き依存: `if (!this.visible && id === this.id)` → `this.conduit.sendInspectorSidebarShown()`
- 条件付き依存: `if (this.visible && id !== this.id)` → `this.conduit.sendInspectorSidebarHidden()`
- 参照: `this.extensionSidebar`, `this.id`, `this.visible`

## ParentDevToolsInspectorSidebar.setPage()
- 位置: L534-556
- 役割: 表示ページの URL を保存する。サイドバーと browser が既にあれば URL を読み込み直し、サイドバーだけならページ設定を行い、無ければ後に予約する。
- 触るとき: 拡張がサイドバーのページを切り替える処理を変えるとき。
- 条件付き依存: `if (this.browser)` → `this.browser.fixupAndLoadURIString()`
- 条件付き依存: `if (!(this.browser))` → `this.extensionSidebar.setExtensionPage()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this._setLazySidebarInit()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this.extensionSidebar.setExtensionPage()`
- 参照: `this.browser`, `this.context.extension.principal`, `this.extensionSidebar`, `this.panelOptions.url`

## ParentDevToolsInspectorSidebar.setObject()
- 位置: L558-574
- 役割: 表示する JSON オブジェクトを設定する。rootTitle があれば包み、サイドバーが未作成なら作成後に予約する。
- 触るとき: サイドバーに値を表示する形式や遅延設定を変えるとき。
- 呼び出し先: `this._updateLastExpressionResult()`
- 条件付き依存: `if (this.extensionSidebar)` → `this.extensionSidebar.setObject()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this._setLazySidebarInit()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this.extensionSidebar.setObject()`
- 参照: `this.extensionSidebar`, `this.panelOptions.url`

## ParentDevToolsInspectorSidebar._setLazySidebarInit()
- 位置: L576-578
- 役割: サイドバー作成後に実行する初期化処理を1つだけ保持する。
- 触るとき: 作成前に呼ばれた設定が次の設定で上書きされる問題を調べるとき。
- 参照: `this._lazySidebarInit`

## ParentDevToolsInspectorSidebar.setExpressionResult()
- 位置: L580-593
- 役割: 式の評価結果をサイドバーに設定する。未作成なら作成後に予約し、直前の結果の解放も行う。
- 触るとき: 式の評価結果の表示や、リモートの参照解放の手順を変えるとき。
- 呼び出し先: `this._updateLastExpressionResult()`
- 条件付き依存: `if (this.extensionSidebar)` → `this.extensionSidebar.setExpressionResult()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this._setLazySidebarInit()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this.extensionSidebar.setExpressionResult()`
- 参照: `this.extensionSidebar`, `this.panelOptions.url`

## ParentDevToolsInspectorSidebar._updateLastExpressionResult()
- 位置: L595-611
- 役割: 最新の式評価結果を保持し、アクターが変わったときは直前のアクターを release する。
- 触るとき: 評価結果のアクターが残ってリモート側のメモリが解放されない問題を調べるとき。
- 条件付き依存: `if ( oldActor && oldActor !== newActor && typeof _lastExpressionResult.release === "function" )` → `_lastExpressionResult.release()`
- 参照: `_lastExpressionResult.actorID`, `_lastExpressionResult.release`, `newExpressionResult.actorID`, `this._lastExpressionResult`

## getAPI()
- 位置: L617-737
- 役割: devtools.panels の API を組み立て、要素選択イベント、サイドバーの作成、パネルの作成と内部用の Sidebar 操作を公開する。
- 触るとき: devtools.panels の公開 API を追加・変更するとき。
- 参照: `context.extension.baseURI.spec`, `context.extension.id`

## newBasePanelId()
- 位置: L631-633
- 役割: 拡張 ID・コンテキスト ID・連番からパネル用の基底 ID を作る。
- 触るとき: パネル ID の形式や重複を調べるとき。
- 参照: `context.contextId`, `context.extension.id`

## register()
- 位置: L642-650
- 役割: 要素選択イベントの購読を登録し、解除時に listener を外す関数を返す。
- 触るとき: onSelectionChanged が届かない、または解除されないときに見る。
- 呼び出し先: `toolboxSelectionObserver.off()`, `toolboxSelectionObserver.on()`

## listener()
- 位置: L643-645
- 役割: 要素選択が変わるたびに、引数なしで fire.async を送る。
- 触るとき: onSelectionChanged の通知内容を変えるとき。
- 呼び出し先: `fire.async()`

## createSidebarPane()
- 位置: L652-673
- 役割: ID 付きのインスペクターサイドバーを作って Map に保持し、コンテキスト終了時に Map から外す。作成した ID を返す。
- 触るとき: createSidebarPane の ID の作り方やサイドバーの後始末を変えるとき。
- 呼び出し先: `Promise.resolve()`, `context.callOnClose()`, `makeWidgetId()`, `newBasePanelId()`, `sidebarsById.set()`

## close()
- 位置: L664-666
- 役割: コンテキスト終了時に、そのサイドバー ID を Map から削除する。
- 触るとき: 終了後の古いサイドバーへ操作が届いてしまう問題を調べるとき。
- 呼び出し先: `sidebarsById.delete()`

## setPage()
- 位置: L678-681
- 役割: 子プロセスからの依頼を受け、指定 ID のサイドバーにページ URL を設定する。
- 触るとき: サイドバーの setPage の呼び出し経路を変えるとき。
- 呼び出し先: `sidebar.setPage()`, `sidebarsById.get()`

## setObject()
- 位置: L682-685
- 役割: 子プロセスからの依頼を受け、指定 ID のサイドバーに JSON オブジェクトを設定する。
- 触るとき: サイドバーの setObject の呼び出し経路を変えるとき。
- 呼び出し先: `sidebar.setObject()`, `sidebarsById.get()`

## setExpression()
- 位置: async L686-711
- 役割: 子プロセスから受けた式をツールボックスの評価オプションで評価し、例外ならその内容を、成功なら結果をサイドバーに表示する。
- 触るとき: サイドバーでの式評価や例外の表示の仕方を変えるとき。
- 呼び出し先: `commands.inspectedWindowCommand.eval()`, `context.getDevToolsCommands()`, `getToolboxEvalOptions()`, `sidebar.setExpressionResult()`, `sidebarsById.get()`, `target.getFront()`
- 条件付き依存: `if (evalResult.exceptionInfo)` → `sidebar.setObject()`
- 参照: `commands.targetCommand.targetFront`, `evalResult.exceptionInfo`, `toolboxEvalOptions.consoleFront`

## create()
- 位置: L714-733
- 役割: 表示名・アイコン・URL を拡張のベース URL から解決し、ID を付けて ParentDevToolsPanel を作る。
- 触るとき: devtools.panels.create の引数の扱い(アイコンの既定値など)を変えるとき。
- 呼び出し先: `Promise.resolve()`, `context.extension.baseURI.resolve()`, `makeWidgetId()`, `newBasePanelId()`
- 条件付き依存: `if (icon === "")` → `context.extension.getPreferredIcon()`
