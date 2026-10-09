# browser/components/extensions/parent/ext-devtools.js

source: browser/components/extensions/parent/ext-devtools.js
source-hash: 650f58b7a5026d57a4f35a5e101d6fc3acfd66bb
lines: 513

## <module>
- 役割: devtools_page を実装する。ツールボックスごとに拡張のページを作り、devtools 設定 pref による有効・無効の切り替えとテーマ変更の通知を扱う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## getDevToolsPrefBranchName()
- 位置: L23-25
- 役割: 拡張 ID から devtools.webextensions.<id> という pref ブランチ名を作る。
- 触るとき: 拡張ごとの devtools 設定 pref の名前を変えるとき。

## global.getTargetTabIdForToolbox()
- 位置: L36-51
- 役割: ツールボックスのローカルタブを解決し、拡張側で使うタブ ID を返す。ローカルタブ以外は例外にする。
- 触るとき: リモートなど非ローカルのツールボックスで拡張がタブ ID を取れない問題を調べるとき。
- 呼び出し先: `parentWindow.gBrowser.getTabForBrowser()`, `tabTracker.getId()`
- 参照: `descriptorFront.isLocalTab`, `descriptorFront.localTab.linkedBrowser`, `descriptorFront.localTab.linkedBrowser.documentGlobal`, `toolbox.commands`

## global.getToolboxEvalOptions()
- 位置: async L55-71
- 役割: 選択中ノードのアクター ID とコンソールのアクター ID を eval オプションとして組み立てる。$0 と inspect の束縛に使う。
- 触るとき: 拡張の eval で $0 や inspect が使えない問題を調べるとき。
- 呼び出し先: `toolbox.target.getFront()`
- 参照: `consoleFront.actor`, `context.devToolsToolbox`, `options.toolboxConsoleActorID`, `options.toolboxSelectedNodeActorID`, `selectedNode.nodeFront`, `selectedNode.nodeFront.actorID`, `toolbox.selection`

## DevToolsPage.constructor()
- 位置: L93-105
- 役割: 拡張ページの URL を解決し、ツールボックスと定義を保持して、最初のコンテキストを待つ Promise を用意する。
- 触るとき: devtools_page の URL 解決や初期状態を変えるとき。
- 呼び出し先: `extension.baseURI.resolve()`, `super()`
- 参照: `options.devToolsPageDefinition`, `options.toolbox`, `options.url`, `this.devToolsPageDefinition`, `this.resolveTopLevelContext`, `this.toolbox`, `this.unwatchExtensionProxyContextLoad`, `this.url`, `this.waitForTopLevelContext`

## DevToolsPage.build()
- 位置: async L107-142
- 役割: ブラウザ要素を作り、コンテキストの読み込みを監視し、ツールボックス情報を付けて URL を読み込み、トップレベルのコンテキストを待つ。
- 触るとき: devtools_page の読み込み順やツールボックス情報の渡し方を変えるとき。
- 呼び出し先: `DevToolsShim.getTheme()`, `extensions.emit()`, `getTargetTabIdForToolbox()`, `this.browser.fixupAndLoadURIString()`, `this.createBrowserElement()`, `watchExtensionProxyContextLoad()`
- 条件付き依存: `if (!this.topLevelContext)` → `this.topLevelContext.callOnClose()`
- 条件付き依存: `if (!this.topLevelContext)` → `this.resolveTopLevelContext()`
- 参照: `context.devToolsToolbox`, `this.browser`, `this.extension.principal`, `this.toolbox`, `this.topLevelContext`, `this.unwatchExtensionProxyContextLoad`, `this.url`, `this.waitForTopLevelContext`

## DevToolsPage.close()
- 位置: L144-166
- 役割: 定義からこのページを外し、コンテキストの終了登録と読み込み監視を解除してから拡張ページを閉じる。
- 触るとき: ツールボックスを閉じた後も devtools_page が残る問題を調べるとき。
- 呼び出し先: `super.shutdown()`, `this.devToolsPageDefinition.forgetForToolbox()`
- 条件付き依存: `if (this.topLevelContext)` → `this.topLevelContext.forgetOnClose()`
- 条件付き依存: `if (this.unwatchExtensionProxyContextLoad)` → `this.unwatchExtensionProxyContextLoad()`
- 参照: `this.closed`, `this.toolbox`, `this.topLevelContext`, `this.unwatchExtensionProxyContextLoad`

## DevToolsPageDefinition.constructor()
- 位置: L188-194
- 役割: 拡張と URL を保持し、ツールボックスごとの DevToolsPage を入れる Map を用意する。
- 触るとき: ツールボックスごとのページ管理の初期状態を変えるとき。
- 参照: `this.devtoolsPageForToolbox`, `this.extension`, `this.url`

## DevToolsPageDefinition.onThemeChanged()
- 位置: L196-200
- 役割: テーマ変更を全プロセスへ Extension:DevToolsThemeChanged メッセージで通知する。
- 触るとき: devtools 拡張へテーマ変更が伝わらない問題を調べるとき。
- 呼び出し先: `Services.ppmm.broadcastAsyncMessage()`
- XPCOM: `Services.ppmm`

## DevToolsPageDefinition.buildForToolbox()
- 位置: L202-232
- 役割: 拡張がアクセスできる窓なら、そのツールボックス用の DevToolsPage を作って Map に入れ、最初の1件ならテーマ変更を購読してから構築する。
- 触るとき: ツールボックスごとに devtools_page を作る条件(非公開ウィンドウの扱いなど)を変えるとき。
- 呼び出し先: `devtoolsPage.build()`, `this.devtoolsPageForToolbox.has()`, `this.devtoolsPageForToolbox.set()`, `this.extension.canAccessWindow()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `Promise.reject()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.size === 0)` → `DevToolsShim.on()`
- 参照: `this.devtoolsPageForToolbox.size`, `this.extension`, `this.onThemeChanged`, `this.url`, `toolbox.commands.descriptorFront.localTab.documentGlobal`

## DevToolsPageDefinition.shutdownForToolbox()
- 位置: L234-253
- 役割: ツールボックスの DevToolsPage を閉じて Map から消し、残っていれば例外にする。最後の1件ならテーマ購読を外す。
- 触るとき: ツールボックス破棄時に devtools_page のリークが出るのを調べるとき。
- 呼び出し先: `this.devtoolsPageForToolbox.has()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `this.devtoolsPageForToolbox.get()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `devtoolsPage.close()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `this.devtoolsPageForToolbox.has()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.size === 0)` → `DevToolsShim.off()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `this.extension.emit()`
- 参照: `this.devtoolsPageForToolbox.size`, `this.extension.policy.debugName`, `this.onThemeChanged`, `toolbox.commands.descriptorFront.url`

## DevToolsPageDefinition.forgetForToolbox()
- 位置: L255-257
- 役割: ツールボックスに対応するページを Map から外す。
- 触るとき: ページを閉じた後の Map の整合性が崩れる問題を調べるとき。
- 呼び出し先: `this.devtoolsPageForToolbox.delete()`

## DevToolsPageDefinition.build()
- 位置: L263-290
- 役割: 既存のツールボックスのうち、破棄中・リモート・アクセス不可のものを除き、拡張を登録して devtools_page を構築する。
- 触るとき: 拡張の読み込み時に既存のツールボックスへ devtools_page を配る処理を変えるとき。
- 呼び出し先: `DevToolsShim.getToolboxes()`, `getDevToolsPrefBranchName()`, `this.buildForToolbox()`, `this.extension.canAccessWindow()`, `toolbox.isDestroying()`, `toolbox.registerWebExtension()`
- 参照: `this.extension.id`, `this.extension.name`, `this.extension.uuid`, `toolbox.commands.descriptorFront.isLocalTab`, `toolbox.commands.descriptorFront.localTab.documentGlobal`

## DevToolsPageDefinition.shutdown()
- 位置: L295-305
- 役割: 全ツールボックスのページを閉じ、Map が空でなければ例外にする。
- 触るとき: 拡張の無効化や終了時にページが残らないか確認するとき。
- 呼び出し先: `this.devtoolsPageForToolbox.keys()`, `this.shutdownForToolbox()`
- 参照: `this.devtoolsPageForToolbox.size`

## constructor()
- 位置: L309-342
- 役割: devtools の状態を初期化し、devtools 権限の付与・取り消しに応じて設定 pref を書き換えて初期化か解除を行う。
- 触るとき: devtools 権限の付与や取り消しに伴う挙動を変えるとき。
- 呼び出し先: `extension.on()`, `permissions.permissions.includes()`, `super()`, `this.onToolboxDestroy.bind()`, `this.onToolboxReady.bind()`
- 条件付き依存: `if (permissions.permissions.includes("devtools"))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (permissions.permissions.includes("devtools"))` → `getDevToolsPrefBranchName()`
- 条件付き依存: `if (permissions.permissions.includes("devtools"))` → `this._initialize()`
- 条件付き依存: `if (permissions.permissions.includes("devtools"))` → `this._uninitialize()`
- 参照: `extension.id`, `this._initialized`, `this.onToolboxDestroy`, `this.onToolboxReady`, `this.pageDefinition`
- XPCOM: `Services.prefs`

## onManifestEntry()
- 位置: L344-346
- 役割: マニフェストの読み込み時に初期化を行う。
- 触るとき: devtools_page を有効にするタイミングを変えるとき。
- 呼び出し先: `this._initialize()`

## onUninstall()
- 位置: L348-355
- 役割: アンインストール時に、拡張の devtools 設定 pref ブランチを削除する。
- 触るとき: アンインストール後も devtools の pref が残る問題を調べるとき。
- 呼び出し先: `Services.prefs.getBranch()`, `getDevToolsPrefBranchName()`, `prefBranch.deleteBranch()`
- XPCOM: `Services.prefs`

## _initialize()
- 位置: L357-381
- 役割: devtools 権限があり未初期化なら、設定 pref を初期化して定義を作り、既存のツールボックスに構築し、ツールボックスのイベントを購読する。
- 触るとき: ツールボックスを開いても devtools_page が出ない問題を調べるとき。
- 呼び出し先: `DevToolsShim.on()`, `extension.hasPermission()`, `this.initDevToolsPref()`, `this.isDevToolsPageDisabled()`
- 条件付き依存: `if (!this.isDevToolsPageDisabled())` → `this.pageDefinition.build()`
- 参照: `extension.manifest.devtools_page`, `this._initialized`, `this.onToolboxDestroy`, `this.onToolboxReady`, `this.pageDefinition`

## _uninitialize()
- 位置: L383-405
- 役割: 初期化済みなら、イベントの購読を外し、全ページを閉じ、ツールボックスの拡張登録を外して、pref の監視を止める。
- 触るとき: devtools 権限を外した後に残るページや登録を調べるとき。
- 呼び出し先: `DevToolsShim.getToolboxes()`, `DevToolsShim.off()`, `this.pageDefinition.shutdown()`, `this.uninitDevToolsPref()`, `toolbox.unregisterWebExtension()`
- 参照: `this._initialized`, `this.extension.uuid`, `this.onToolboxDestroy`, `this.onToolboxReady`, `this.pageDefinition`

## onShutdown()
- 位置: L407-409
- 役割: 拡張の終了時に _uninitialize を呼ぶ。
- 触るとき: 拡張終了時の後片付けを変えるとき。
- 呼び出し先: `this._uninitialize()`

## getAPI()
- 位置: L411-415
- 役割: devtools 名前空間の API オブジェクトを空で返す。公開メソッドは別のモジュールが追加する。
- 触るとき: devtools 名前空間に新しい API を足す場所を探すとき。

## onToolboxReady()
- 位置: L417-441
- 役割: アクセス可能なローカルタブのツールボックスに拡張を登録し、拡張が有効ならそのツールボックス用の devtools_page を作る。
- 触るとき: ツールボックス起動時に devtools_page が出ない、または出すぎる問題を調べるとき。
- 呼び出し先: `getDevToolsPrefBranchName()`, `this.extension.canAccessWindow()`, `toolbox.isWebExtensionEnabled()`, `toolbox.registerWebExtension()`
- 条件付き依存: `if (toolbox.isWebExtensionEnabled(this.extension.uuid))` → `this.pageDefinition.buildForToolbox()`
- 参照: `this.extension.id`, `this.extension.name`, `this.extension.uuid`, `toolbox.commands.descriptorFront.isLocalTab`, `toolbox.commands.descriptorFront.localTab.documentGlobal`

## onToolboxDestroy()
- 位置: L443-451
- 役割: ローカルタブのツールボックスが破棄されたら、そのツールボックスのページを閉じる。
- 触るとき: ツールボックスを閉じた後に devtools_page が残るときに見る。
- 呼び出し先: `this.pageDefinition.shutdownForToolbox()`
- 参照: `toolbox.commands.descriptorFront.isLocalTab`

## initDevToolsPref()
- 位置: L457-469
- 役割: 拡張の devtools 設定ブランチに enabled が無ければ true で初期化し、そのブランチの監視を始める。
- 触るとき: devtools の有効化設定の既定値や監視先を変えるとき。
- 呼び出し先: `Services.prefs.getBranch()`, `getDevToolsPrefBranchName()`, `prefBranch.getPrefType()`, `this.devtoolsPrefBranch.addObserver()`
- 条件付き依存: `if (prefBranch.getPrefType("enabled") === prefBranch.PREF_INVALID)` → `prefBranch.setBoolPref()`
- 参照: `prefBranch.PREF_INVALID`, `this.devtoolsPrefBranch`, `this.extension.id`
- XPCOM: `Services.prefs`

## uninitDevToolsPref()
- 位置: L474-477
- 役割: devtools 設定ブランチの監視を外し、参照を消す。
- 触るとき: 拡張の終了後も pref 監視が残る問題を調べるとき。
- 呼び出し先: `this.devtoolsPrefBranch.removeObserver()`
- 参照: `this.devtoolsPrefBranch`

## isDevToolsPageDisabled()
- 位置: L486-488
- 役割: devtools 設定の enabled が false なら、devtools_page を無効と判定する。
- 触るとき: 設定で拡張の devtools_page を無効にしたときの判定を変えるとき。
- 呼び出し先: `this.devtoolsPrefBranch.getBoolPref()`

## observe()
- 位置: L498-511
- 役割: devtools 設定の enabled が変わったら、無効化なら全ページを閉じ、有効化なら全ツールボックスに構築する。
- 触るとき: 設定画面でのオンとオフが即時反映されない問題を調べるとき。
- 呼び出し先: `this.isDevToolsPageDisabled()`
- 条件付き依存: `if (this.isDevToolsPageDisabled())` → `this.pageDefinition.shutdown()`
- 条件付き依存: `if (!(this.isDevToolsPageDisabled()))` → `this.pageDefinition.build()`
- 参照: `this.devtoolsPrefBranch`
