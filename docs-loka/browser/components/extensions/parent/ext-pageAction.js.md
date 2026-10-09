# browser/components/extensions/parent/ext-pageAction.js

source: browser/components/extensions/parent/ext-pageAction.js
source-hash: 72c1b3fd63d94648f6015b584a27a83e033a0658
lines: 417

## <module>
- 役割: pageAction WebExtension API の実装。ツールバーのページアクション (ボタン) の表示、クリック処理、ポップアップの開閉を扱う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## PageAction.constructor()
- 位置: L28-32
- 役割: タブコンテキストを作って PageActionBase を初期化し、ボタン側の delegate を保持する。
- 触るとき: ページアクションのタブごとの状態 (タイトル、アイコン、有効かどうか) がタブ切り替えで正しく変わらないときに見る。
- 呼び出し先: `super()`, `this.getContextData()`
- 参照: `this.buttonDelegate`

## PageAction.updateOnChange()
- 位置: L34-36
- 役割: 状態が変わったタブのウィンドウについて、ボタンの表示を更新する。
- 触るとき: タブの状態変化でボタンが古いままになるときに、どの状態変化から呼ばれるか確認する。
- 呼び出し先: `this.buttonDelegate.updateButton()`
- 参照: `target.documentGlobal`

## PageAction.dispatchClick()
- 位置: L38-40
- 役割: ボタンの click イベントをタブと clickInfo 付きで発火させる。
- 触るとき: 拡張の onClicked に渡る引数や、ボタン押下時の経路を確認するとき。
- 呼び出し先: `this.buttonDelegate.emit()`

## PageAction.getTab()
- 位置: L42-47
- 役割: tabId が null でなければタブを解決し、null なら null を返す。
- 触るとき: tabId を省略したページアクションの呼び出しで、対象タブが誤って解決されるとき。
- 条件付き依存: `if (tabId !== null)` → `tabTracker.getTab()`

## PageAction.isPanelShownBlockingOpenPopup()
- 位置: L49-55
- 役割: グローバルなポップアップ抑止があるか、または同じウィンドウでパネルが開いているかを判定する。
- 触るとき: pageAction.openPopup が開けないとき、またはポップアップを抑止する条件を変えるときに見る。
- 呼び出し先: `isGloballyBlockingOpenPopup()`
- 参照: `panel.documentGlobal`, `panel.state`, `this.buttonDelegate.popupNode?.panel`

## for()
- 位置: L59-61
- 役割: 拡張に紐づく pageAction のインスタンスを pageActionMap から返す。
- 触るとき: 他モジュールが拡張の pageAction を参照する経路 (global.pageActionFor) を辿るとき。
- 呼び出し先: `pageActionMap.get()`

## onUpdate()
- 位置: L63-70
- 役割: 新バージョンの manifest に page_action が無ければ、テレメトリ上のウィジェットを非表示として記録する。
- 触るとき: 拡張更新後に page_action を外した拡張のボタンが残るときや、テレメトリの記録が合わないとき。
- 条件付き依存: `if (!("page_action" in manifest))` → `BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (!("page_action" in manifest))` → `makeWidgetId()`

## onDisable()
- 位置: L72-74
- 役割: 拡張の無効化時に、テレメトリ上のウィジェットを非表示として記録する。
- 触るとき: 無効化された拡張のボタンがテレメトリに残るときに見る。
- 呼び出し先: `BrowserUsageTelemetry.recordWidgetChange()`, `makeWidgetId()`

## onUninstall()
- 位置: L76-80
- 役割: アンインストール時に、テレメトリ上のウィジェットを非表示として記録する。
- 触るとき: アンインストール後にテレメトリのウィジェット記録が残るとき。既に非表示なら何もしない。
- 呼び出し先: `BrowserUsageTelemetry.recordWidgetChange()`, `makeWidgetId()`

## onManifestEntry()
- 位置: async L82-177
- 役割: PageAction を作り、アイコンを読み込み、ブラウザの PageActions にボタンを登録する。アイコン、タイトル、有効状態、イベントのハンドラを設定する。
- 触るとき: ページアクションがツールバーに出ない、クリックが届かない、またはテレメトリ上の配置が合わないときに見る。enabled が未定義なら、アクティブなタブにパターン一致で表示を合わせる。
- 呼び出し先: `makeWidgetId()`, `pageActionMap.set()`, `this.action.loadIconData()`
- 条件付き依存: `if (!this.browserPageAction)` → `PageActions.addAction()`
- 条件付き依存: `if (!this.browserPageAction)` → `this.action.getProperty()`
- 条件付き依存: `if (!this.browserPageAction)` → `this.action.getPinned()`
- 条件付き依存: `if (this.extension.startupReason != "APP_STARTUP")` → `ExtensionParent.browserStartupPromise.then()`
- 条件付き依存: `if (this.extension.startupReason != "APP_STARTUP")` → `BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (this.action.getProperty(null, "enabled") === undefined)` → `windowTracker.browserWindows()`
- 条件付き依存: `if (this.action.getProperty(null, "enabled") === undefined)` → `this.action.isShownForTab()`
- 条件付き依存: `if (this.action.isShownForTab(tab))` → `this.updateButton()`
- 参照: `PageActions.Action`, `extension.id`, `extension.manifest.page_action`, `extension.tabManager`, `options.browser_style`, `this.action`, `this.browserPageAction`, `this.browserPageAction.pinnedToUrlbar`, `this.browserStyle`, `this.extension.startupReason`, `this.id`, `this.lastValues`, `this.tabManager`, `window.gBrowser.selectedTab`

## onPlacedHandler()
- 位置: L101-120
- 役割: ボタンが配置されたとき、中クリック (auxclick) で拡張のクリックを発火させる。パネル内ならポップアップを閉じる。
- 触るとき: 中クリックで拡張のクリックが呼ばれない、またはパネル内で閉じない挙動を調べるとき。
- 呼び出し先: `buttonNode.addEventListener()`, `clickModifiersFromEvent()`, `this.action.dispatchClick()`, `this.tabManager.addActiveTabPermission()`
- 条件付き依存: `if (isPanel)` → `buttonNode.closest("#pageActionPanel").hidePopup()`
- 条件付き依存: `if (isPanel)` → `buttonNode.closest()`
- 参照: `event.button`, `event.target.disabled`, `event.target.documentGlobal`, `window.gBrowser.selectedTab`

## onCommand()
- 位置: L130-135
- 役割: ボタンのコマンドを、押されたボタンとモディファイアキー付きで handleClick に渡す。
- 触るとき: 通常のクリックや、キーボード操作の呼び出し内容を確認するとき。
- 呼び出し先: `clickModifiersFromEvent()`, `this.handleClick()`
- 参照: `event.button`, `event.target.documentGlobal`

## onBeforePlacedInWindow()
- 位置: L136-143
- 役割: menus か contextMenus の権限があるとき、ウィンドウの popupshowing をこのインスタンスに監視させる。
- 触るとき: ページアクションの右クリックメニューが出ない、または権限が無いのに出るときに見る。
- 呼び出し先: `this.extension.hasPermission()`
- 条件付き依存: `if ( this.extension.hasPermission("menus") || this.extension.hasPermission("contextMenus") )` → `browserWindow.document.addEventListener()`

## onPlacedInPanel()
- 位置: L144-144
- 役割: パネルに配置されたボタンに、中クリック用のハンドラを付ける。
- 触るとき: パネル内ボタンの中クリック処理を変えるときに見る。
- 呼び出し先: `onPlacedHandler()`

## onPlacedInUrlbar()
- 位置: L145-145
- 役割: URL バーに配置されたボタンに、中クリック用のハンドラを付ける。
- 触るとき: URL バー内ボタンの中クリック処理を変えるときに見る。
- 呼び出し先: `onPlacedHandler()`

## onRemovedFromWindow()
- 位置: L146-148
- 役割: ウィンドウからボタンが外れるとき、popupshowing の監視を解除する。
- 触るとき: ウィンドウを閉じた後に popupshowing が残って例外になるときに見る。
- 呼び出し先: `browserWindow.document.removeEventListener()`

## onShutdown()
- 位置: L179-191
- 役割: 拡張の終了時に pageActionMap から外し、アプリ終了以外では browserPageAction を削除する。
- 触るとき: 拡張を無効化した後もボタンが残るとき、またはアプリ再起動後に配置が保持されるかを確認するとき。アプリ終了時は削除しないので、次回起動で配置が残る。
- 呼び出し先: `pageActionMap.delete()`, `this.action.onShutdown()`
- 条件付き依存: `if (!isAppShutdown && this.browserPageAction)` → `this.browserPageAction.remove()`
- 参照: `this.browserPageAction`, `this.extension`

## updateButton()
- 位置: L199-230
- 役割: 選択中タブの状態からタイトル、有効状態、アイコンを求め、前回と異なる項目だけ requestAnimationFrame で反映する。
- 触るとき: タブ切り替えでボタンの表示が変わらない、または前回値の比較で更新が抜けるときに見る。enabled が null なら patternMatching の値を使う。
- 呼び出し先: `this.action.getContextData()`, `this.lastValues.get()`, `window.requestAnimationFrame()`
- 条件付き依存: `if (last.title !== title)` → `this.browserPageAction.setTitle()`
- 条件付き依存: `if (last.enabled !== enabled)` → `this.browserPageAction.setDisabled()`
- 条件付き依存: `if (last.icon !== icon)` → `this.browserPageAction.setIconURL()`
- 参照: `last.enabled`, `last.icon`, `last.title`, `tabData.enabled`, `tabData.icon`, `tabData.patternMatching`, `tabData.title`, `this.browserPageAction`, `this.extension.name`, `window.gBrowser.selectedTab`

## triggerAction()
- 位置: L240-242
- 役割: ユーザーのクリックと同じ扱いで handleClick を呼び出す。
- 触るとき: 拡張がプログラム的にページアクションを押す経路を変えるとき。表示されていないタブでは効かない。
- 呼び出し先: `this.handleClick()`

## handleEvent()
- 位置: L244-286
- 役割: popupshowing を受け、ページアクションのコンテキストメニューなら actionContextMenu を開く。
- 触るとき: ページアクションの右クリックメニューに拡張のメニュー項目が出ないときに見る。
- 呼び出し先: `getActionId()`, `this.browserPageAction.getDisabled()`, `this.extension.hasPermission()`
- 条件付き依存: `if ( menu.id === "pageActionContextMenu" && trigger && getActionId() === this.browserPageAction.id && !this.browserPageAction.getDisabled(trigger.documentGlobal)...)` → `global.actionContextMenu()`
- 参照: `event.target`, `event.type`, `menu.id`, `menu.triggerNode`, `this.browserPageAction.id`, `this.extension`, `trigger.documentGlobal`

## getActionId()
- 位置: L249-268
- 役割: メニューのトリガーノードから祖先をたどり、actionid 属性を持つ要素のアクション ID を探す。
- 触るとき: キーボード操作と右クリックでトリガーノードが違い、メニューが正しいボタンに紐づかないときに見る。
- 呼び出し先: `n.getAttribute()`, `trigger.getAttribute()`
- 参照: `n.id`, `n.localName`, `n.parentElement`

## handleClick()
- 位置: async L293-360
- 役割: ポップアップ URL があればパネルを開閉し、無ければクリックイベントだけを発火させる。テレメトリの計測も行う。
- 触るとき: ページアクションのクリック時にポップアップが開かない、または開いたまま閉じないときに見る。拡張の終了中にポップアップが壊れた場合は破棄して例外を投げる。
- 呼び出し先: `ExtensionTelemetry.pageActionPopupOpen.stopwatchStart()`, `this.action.triggerClickOrPopup()`
- 条件付き依存: `if (this.popupNode && this.popupNode.panel.state !== "closed")` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchCancel()`
- 条件付き依存: `if (this.popupNode && this.popupNode.panel.state !== "closed")` → `window.BrowserPageActions.togglePanelForAction()`
- 条件付き依存: `if (popupURL)` → `popup.panel.addEventListener()`
- 条件付き依存: `if (popup.destroyed)` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchCancel()`
- 条件付き依存: `if (popupURL)` → `window.BrowserPageActions.togglePanelForAction()`
- 条件付き依存: `if (popupURL)` → `popup.destroy()`
- 条件付き依存: `if (popupURL)` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchCancel()`
- 条件付き依存: `if (popupURL)` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchFinish()`
- 条件付き依存: `if (!(popupURL))` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchCancel()`
- 参照: `popup.contentReady`, `popup.destroyed`, `popup.panel`, `this.browserPageAction`, `this.browserStyle`, `this.popupNode`, `this.popupNode.panel`, `this.popupNode.panel.state`, `window.document`, `window.gBrowser.selectedTab`

## onClicked()
- 位置: L363-388
- 役割: click イベントを受けて、タブを変換し clickInfo と共に拡張へ fire.sync する。
- 触るとき: pageAction.onClicked の引数や、初回起動前のリスナー復帰の挙動を確認するとき。
- 呼び出し先: `this.on()`

## listener()
- 位置: async L367-376
- 役割: click を受けて、必要なら fire.wakeup() を待ち、保留中のブラウザ内で fire.sync を呼ぶ。
- 触るとき: バックグラウンドが停止していた状態からクリックされたときに、イベントが届かないとき。
- 呼び出し先: `context?.withPendingBrowser()`, `fire.sync()`, `tabManager.convert()`
- 条件付き依存: `if (fire.wakeup)` → `fire.wakeup()`
- 参照: `fire.wakeup`, `tab.linkedBrowser`

## unregister()
- 位置: L380-382
- 役割: onClicked の click リスナーを外す。
- 触るとき: 拡張の無効化後も onClicked が発火するときに解除を確認する。
- 呼び出し先: `this.off()`

## convert()
- 位置: L383-386
- 役割: 永続イベントの再接続時に fire と context を差し替える。
- 触るとき: 再起動後に onClicked が古い fire や context へ送られるときに見る。

## getAPI()
- 位置: L391-413
- 役割: action.api() の結果に onClicked と openPopup を加えて pageAction API を返す。
- 触るとき: 拡張から見える pageAction API を増減するとき。
- 呼び出し先: `action.api()`, `new EventManager({ context, module: "pageAction", event: "onClicked", inputHandling: true, extensionApi: this, }).api()`

## openPopup()
- 位置: L406-410
- 役割: トップウィンドウでポップアップが開けるかを確認してから、triggerAction でページアクションを開く。
- 触るとき: pageAction.openPopup が blocked で失敗するとき、または開く対象のウィンドウを変えるとき。
- 呼び出し先: `action.throwIfOpenPopupIsBlockedByAnyAction()`, `this.triggerAction()`
- 参照: `windowTracker.topWindow`
