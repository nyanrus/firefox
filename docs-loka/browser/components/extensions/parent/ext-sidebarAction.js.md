# browser/components/extensions/parent/ext-sidebarAction.js

source: browser/components/extensions/parent/ext-sidebarAction.js
source-hash: ec0676688769674c9caab7e34f621c2dede5e7d8
lines: 485

## <module>
- 役割: sidebar_action manifest の処理と、サイドバーのメニュー項目・パネル・API の実装。ウィンドウごとのサイドバー表示を SidebarController に委ねる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## for()
- 位置: L27-29
- 役割: 拡張に紐づく sidebarAction インスタンスを sidebarActionMap から返す。
- 触るとき: 他モジュールが拡張のサイドバーを参照する経路 (global.sidebarActionFor) を辿るとき。
- 呼び出し先: `sidebarActionMap.get()`

## onManifestEntry()
- 位置: L31-68
- 役割: ID と既定値 (title、icon、panel) を用意し、ready 後の build と、新しいウィンドウ向けのメニュー項目作成を登録する。
- 触るとき: サイドバーの既定タイトルや既定 panel が反映されないとき、またはセッション復元前にメニュー項目が無いときに見る。
- 呼び出し先: `ChromeUtils.getClassName()`, `IconDetails.normalize()`, `Object.create()`, `extension.once()`, `makeWidgetId()`, `sidebarActionMap.set()`, `this.onReady.bind()`, `this.tabContext.get()`, `windowTracker.addOpenListener()`
- 参照: `extension.id`, `extension.manifest.sidebar_action`, `extension.name`, `options.browser_style`, `options.default_icon`, `options.default_panel`, `options.default_title`, `target.documentGlobal`, `this.browserStyle`, `this.defaults`, `this.globals`, `this.id`, `this.menuId`, `this.tabContext`, `this.windowOpenListener`

## this.windowOpenListener()
- 位置: L62-64
- 役割: 新しく開かれたウィンドウに、このサイドバーのメニュー項目を作る。
- 触るとき: ウィンドウを新しく開いたときにサイドバーのメニューに項目が出ないときに見る。セッション復元より前に要素を用意するために存在する。
- 呼び出し先: `this.createMenuItem()`
- 参照: `this.globals`

## onReady()
- 位置: L70-72
- 役割: 拡張の起動完了 (ready) 時に build を呼ぶ。
- 触るとき: 起動が完了した後にサイドバーの初期化が始まるタイミングを変えるとき。
- 呼び出し先: `this.build()`

## onShutdown()
- 位置: L83-103
- 役割: 拡張の終了時にタブ用コンテキストを止め、アプリ終了以外では各ウィンドウからサイドバーを外す。
- 触るとき: 拡張を無効化した後もサイドバーが残るときに見る。アプリ終了時は削除しないので、次回起動でサイドバーの復元が効く。
- 呼び出し先: `SidebarController.removeExtension()`, `sidebarActionMap.delete()`, `this.tabContext.shutdown()`, `windowTracker.browserWindows()`, `windowTracker.removeOpenListener()`
- 参照: `this.extension`, `this.id`, `this.windowOpenListener`

## onUninstall()
- 位置: L105-122
- 役割: アンインストール時に sidebar.installed.extensions の設定を消し、最後に開いたサイドバーの ID をウィンドウごとにクリアする。
- 触るとき: アンインストール後に、拡張のサイドバーが次回起動で再び開くときに見る。
- 呼び出し先: `Services.prefs .getStringPref()`, `Services.prefs .getStringPref("sidebar.installed.extensions", "") .split()`, `installedExtensions.indexOf()`, `makeWidgetId()`, `windowTracker.browserWindows()`
- 条件付き依存: `if (index != -1)` → `SidebarManager.cleanupPrefs()`
- 参照: `SidebarController.lastOpenedId`
- XPCOM: `Services.prefs`

## build()
- 位置: L124-141
- 役割: タブ選択時の更新を登録し、各ウィンドウを更新する。インストール直後か前回開いていた場合は open_at_install に従ってサイドバーを表示する。
- 触るとき: 拡張のインストール直後にサイドバーが開かない、または再起動後に前回の開き方が再現されないときに見る。
- 呼び出し先: `this.tabContext.on()`, `this.updateWindow()`, `windowTracker.browserWindows()`
- 条件付き依存: `if ( (install || SidebarController.lastOpenedId == this.id) && this.extension.manifest.sidebar_action.open_at_install )` → `SidebarController.show()`
- 参照: `SidebarController.lastOpenedId`, `tab.documentGlobal`, `this.extension.manifest.sidebar_action.open_at_install`, `this.extension.startupReason`, `this.id`

## createMenuItem()
- 位置: L143-161
- 役割: アクセス可能なウィンドウの SidebarController に、拡張のアイコン、メニュー ID、タイトル、読み込み時の処理を登録する。
- 触るとき: サイドバーのメニュー項目が出ない、または読み込んだパネルが違うときに見る。
- 呼び出し先: `SidebarController.registerExtension()`, `this.extension.canAccessWindow()`, `this.getMenuIcon()`
- 参照: `details.panel`, `details.title`, `this.extension.id`, `this.id`, `this.menuId`, `this.panel`

## onload()
- 位置: L154-159
- 役割: サイドバーが読み込まれたとき、拡張 ID と現在の panel URL で loadPanel を呼ぶ。
- 触るとき: サイドバーを開いた時にパネルの内容が出ないときに見る。
- 呼び出し先: `SidebarController.browser.contentWindow.loadPanel()`
- 参照: `this.browserStyle`, `this.extension.id`, `this.panel`

## getMenuIcon()
- 位置: L173-177
- 役割: 表示倍率に合わせて 16px に相当するアイコンを選び、URL をエスケープして返す。
- 触るとき: サイドバーのメニューアイコンの大きさや表示がずれるとき。
- 呼び出し先: `IconDetails.escapeUrl()`, `IconDetails.getPreferredIcon()`
- 参照: `IconDetails.getPreferredIcon(icon, this.extension, 16 * scale).icon`, `this.extension`

## updateButton()
- 位置: L187-208
- 役割: タブのデータを使ってメニュー項目のアイコンとラベルを更新し、panel が変わったかを伝える。メニュー項目が無ければ作り直す。
- 触るとき: 拡張がタイトルやアイコンを変えてもサイドバーのメニューに反映されないときに見る。
- 呼び出し先: `SidebarController.setExtensionAttributes()`, `document.getElementById()`, `this.getMenuIcon()`
- 条件付き依存: `if (!document.getElementById(this.menuId))` → `this.createMenuItem()`
- 参照: `tabData.panel`, `tabData.title`, `this.extension.name`, `this.id`, `this.menuId`, `this.panel`

## updateWindow()
- 位置: L216-222
- 役割: アクセス可能なウィンドウで、選択中タブのデータを使って updateButton を呼ぶ。
- 触るとき: タブを切り替えてもサイドバーの表示が切り替わらないときに見る。
- 呼び出し先: `this.extension.canAccessWindow()`, `this.tabContext.get()`, `this.updateButton()`
- 参照: `window.gBrowser.selectedTab`

## updateOnChange()
- 位置: L233-245
- 役割: 変化の対象がウィンドウ、選択中のタブ、または null (全体) かで、必要なウィンドウだけ更新する。
- 触るとき: 拡張がプロパティを変えたときに、対象外のウィンドウまで更新されるなど範囲がずれるとき。
- 条件付き依存: `if (target)` → `ChromeUtils.getClassName()`
- 条件付き依存: `if (ChromeUtils.getClassName(target) == "Window")` → `this.updateWindow()`
- 条件付き依存: `if (target.selected)` → `this.updateWindow()`
- 条件付き依存: `if (!(target))` → `windowTracker.browserWindows()`
- 条件付き依存: `if (!(target))` → `this.updateWindow()`
- 参照: `target.documentGlobal`, `target.selected`

## getTargetFromDetails()
- 位置: L263-282
- 役割: tabId か windowId から対象 (タブ、ウィンドウ、または null) を解決し、両方の指定やアクセス不可の ID を例外にする。
- 触るとき: setTitle や getTitle などの details で『Invalid tab ID』や『Only one of』が出るとき。
- 条件付き依存: `if (tabId != null)` → `tabTracker.getTab()`
- 条件付き依存: `if (tabId != null)` → `this.extension.canAccessWindow()`
- 条件付き依存: `if (windowId != null)` → `windowTracker.getWindow()`
- 条件付き依存: `if (windowId != null)` → `this.extension.canAccessWindow()`
- 参照: `target.documentGlobal`

## getContextData()
- 位置: L292-297
- 役割: 対象がタブならタブのデータ、null なら全体のデータを返す。
- 触るとき: タブごと・ウィンドウごと・全体の値の優先順位を変えるときに見る。
- 条件付き依存: `if (target)` → `this.tabContext.get()`
- 参照: `this.globals`

## setProperty()
- 位置: L309-318
- 役割: 対象のデータの prop を値で設定する。null なら削除し、最後に updateOnChange で反映する。
- 触るとき: title、icon、panel の設定が効かないとき、または値の削除の扱いを確認するとき。
- 呼び出し先: `this.getContextData()`, `this.updateOnChange()`

## getProperty()
- 位置: L330-332
- 役割: 対象のデータから prop を読み出す。
- 触るとき: タブ単位の値が取れず全体の値が返るなど、値の解決先を調べるとき。
- 呼び出し先: `this.getContextData()`

## setPropertyFromDetails()
- 位置: L334-336
- 役割: details から対象を解決して setProperty を呼ぶ。
- 触るとき: setTitle、setIcon、setPanel の API が対象を正しく指定できないとき。
- 呼び出し先: `this.getTargetFromDetails()`, `this.setProperty()`

## getPropertyFromDetails()
- 位置: L338-340
- 役割: details から対象を解決して getProperty を呼ぶ。
- 触るとき: getTitle、getPanel の API が対象を正しく指定できないとき。
- 呼び出し先: `this.getProperty()`, `this.getTargetFromDetails()`

## triggerAction()
- 位置: L348-353
- 役割: ユーザーのメニュー操作と同じく、アクセス可能なウィンドウでサイドバーを toggle する。
- 触るとき: 拡張からサイドバーを開閉する経路を変えるとき。
- 呼び出し先: `this.extension.canAccessWindow()`
- 条件付き依存: `if (SidebarController && this.extension.canAccessWindow(window))` → `SidebarController.toggle()`
- 参照: `this.id`

## open()
- 位置: L360-365
- 役割: アクセス可能なウィンドウで SidebarController.show を呼ぶ。
- 触るとき: 拡張の sidebarAction.open が開かないときに見る。
- 呼び出し先: `this.extension.canAccessWindow()`
- 条件付き依存: `if (SidebarController && this.extension.canAccessWindow(window))` → `SidebarController.show()`
- 参照: `this.id`

## close()
- 位置: L372-376
- 役割: このサイドバーが開いていれば、そのウィンドウで hide する。
- 触るとき: sidebarAction.close が効かないときに見る。
- 呼び出し先: `this.isOpen()`
- 条件付き依存: `if (this.isOpen(window))` → `window.SidebarController.hide()`

## toggle()
- 位置: L383-394
- 役割: このサイドバーが開いていなければ show、開いていれば hide する。
- 触るとき: sidebarAction.toggle が期待と逆に動くとき。
- 呼び出し先: `this.extension.canAccessWindow()`, `this.isOpen()`
- 条件付き依存: `if (!this.isOpen(window))` → `SidebarController.show()`
- 条件付き依存: `if (!(!this.isOpen(window)))` → `SidebarController.hide()`
- 参照: `this.id`

## isOpen()
- 位置: L402-405
- 役割: そのウィンドウのサイドバーが開いていて、現在のサイドバーが自分の ID かを判定する。
- 触るとき: 別の拡張のサイドバーが開いているときに、isOpen が true を返してしまうなどの判定を調べるとき。
- 参照: `SidebarController.currentID`, `SidebarController.isOpen`, `this.id`

## getAPI()
- 位置: L407-481
- 役割: sidebarAction の API オブジェクトを組み立て、title、icon、panel の取得と設定、開閉の操作を返す。
- 触るとき: 拡張から見える sidebarAction API を増減するとき。

## setTitle()
- 位置: async L413-415
- 役割: details の title を対象のタイトルとして設定する。
- 触るとき: sidebarAction.setTitle が反映されないときに見る。
- 呼び出し先: `sidebarAction.setPropertyFromDetails()`
- 参照: `details.title`

## getTitle()
- 位置: L417-419
- 役割: details で指定された対象のタイトルを返す。
- 触るとき: sidebarAction.getTitle が想定と違う値を返すとき。
- 呼び出し先: `sidebarAction.getPropertyFromDetails()`

## setIcon()
- 位置: async L421-427
- 役割: details のアイコンを正規化して設定する。空なら null として既定に戻す。
- 触るとき: sidebarAction.setIcon が効かない、または空指定で既定に戻らないときに見る。
- 呼び出し先: `IconDetails.normalize()`, `Object.keys()`, `sidebarAction.setPropertyFromDetails()`
- 参照: `Object.keys(icon).length`

## setPanel()
- 位置: async L429-444
- 役割: panel の URL を拡張の URI で解決し、読み込み可能か確認してから設定する。空なら null を入れる。
- 触るとき: sidebarAction.setPanel で『Access denied for URL』が出るとき、または相対 URL の解決を確認するとき。
- 呼び出し先: `sidebarAction.setPropertyFromDetails()`
- 条件付き依存: `if (!(!details.panel))` → `context.uri.resolve()`
- 条件付き依存: `if (!(!details.panel))` → `context.checkLoadURL()`
- 条件付き依存: `if (!context.checkLoadURL(url))` → `Promise.reject()`
- 参照: `details.panel`

## getPanel()
- 位置: L446-448
- 役割: details で指定された対象の panel URL を返す。
- 触るとき: sidebarAction.getPanel が想定と違う値を返すとき。
- 呼び出し先: `sidebarAction.getPropertyFromDetails()`

## open()
- 位置: L450-455
- 役割: トップウィンドウでアクセス可能な場合に sidebarAction.open を呼ぶ。
- 触るとき: sidebarAction.open API が別のウィンドウで開いてしまうときに見る。
- 呼び出し先: `context.canAccessWindow()`
- 条件付き依存: `if (context.canAccessWindow(window))` → `sidebarAction.open()`
- 参照: `windowTracker.topWindow`

## close()
- 位置: L457-462
- 役割: トップウィンドウでアクセス可能な場合に sidebarAction.close を呼ぶ。
- 触るとき: sidebarAction.close API が効かないときに見る。
- 呼び出し先: `context.canAccessWindow()`
- 条件付き依存: `if (context.canAccessWindow(window))` → `sidebarAction.close()`
- 参照: `windowTracker.topWindow`

## toggle()
- 位置: L464-469
- 役割: トップウィンドウでアクセス可能な場合に sidebarAction.toggle を呼ぶ。
- 触るとき: sidebarAction.toggle API が効かないときに見る。
- 呼び出し先: `context.canAccessWindow()`
- 条件付き依存: `if (context.canAccessWindow(window))` → `sidebarAction.toggle()`
- 参照: `windowTracker.topWindow`

## isOpen()
- 位置: L471-478
- 役割: windowId で対象ウィンドウを解決し (省略時は現在のウィンドウ)、そのサイドバーが開いているかを返す。
- 触るとき: sidebarAction.isOpen が別ウィンドウの状態を返すときに見る。
- 呼び出し先: `sidebarAction.isOpen()`, `windowTracker.getWindow()`
- 参照: `Window.WINDOW_ID_CURRENT`
