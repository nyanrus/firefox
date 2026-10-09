# browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs

source: browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs
source-hash: 838512efba972e47fb90d301081416d1ce3cbde1
lines: 415

## <module>
- 役割: urlbar のクイックアクション（設定を開く、履歴の消去、再起動など）の既定の定義と、それを ActionsProviderQuickActions に登録する読み込み処理。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `openAddonsUrl()`, `openUrlFun()`

## openUrlFun()
- 位置: L32-33
- 役割: 指定 URL を開くアクション関数を作る。選ぶと openUrl を呼ぶ。
- 触るとき: 新しいクイックアクションを URL を開くだけの形で足すとき。
- 呼び出し先: `openUrl()`
- 参照: `controller.browserWindow`

## openUrl()
- 位置: L34-47
- 役割: about: の URL は既存のタブを探して切り替え（フラグメントの扱いは URL 次第）、それ以外は背景でないタブとして開く。コンテンツへのフォーカス移動を返す。
- 触るとき: クイックアクションで開くページが既存タブに移らない、または重複して開く問題を調べるとき。
- 呼び出し先: `url.startsWith()`
- 条件付き依存: `if (url.startsWith("about:"))` → `Services.io.newURI()`
- 条件付き依存: `if (url.startsWith("about:"))` → `window.switchToTabHavingURI()`
- 条件付き依存: `if (!(url.startsWith("about:")))` → `window.gBrowser.addTab()`
- 条件付き依存: `if (!(url.startsWith("about:")))` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `uri.hasRef`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## openAddonsUrl()
- 位置: L49-55
- 役割: アドオン管理画面を指定の addons:// URL で開き、該当タブを選択する。
- 触るとき: 拡張機能・テーマ関連のクイックアクションの遷移先を変えるとき。
- 呼び出し先: `controller.browserWindow.BrowserAddonUI.openAddonsMgr()`

## currentWindow()
- 位置: L57-57
- 役割: 最前面のブラウザウィンドウを返す。
- 触るとき: アクションの状態判定で使う現在ウィンドウの取り方を変えるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`

## currentBrowser()
- 位置: L58-58
- 役割: 最前面ウィンドウで選択中のブラウザ要素を返す。
- 触るとき: 現在のページを見て有効・無効を判定するアクションを足すとき。
- 呼び出し先: `currentWindow()`
- 参照: `currentWindow().gBrowser.selectedBrowser`

## unmutedAudioTabs()
- 位置: L60-68
- 役割: 全ウィンドウで、音を出している（または一時的にその扱いの）タブのうち消音されていないものを集める。
- 触るとき: ミュートのクイックアクションの対象範囲を変えるとき。
- 呼び出し先: `Array.from()`, `Array.from(win.gBrowser.tabs).filter()`, `lazy.BrowserWindowTracker.orderedWindows.flatMap()`, `tab.hasAttribute()`
- 参照: `tab.muted`, `tab.soundPlaying`, `win.gBrowser.tabs`

## onPick()
- 位置: L92-96
- 役割: ブックマーク（ツールバー）のライブラリ画面を開く。
- 触るとき: ブックマーク系の動作を変えるとき。
- 呼び出し先: `controller.browserWindow.top.PlacesCommandHook.showPlacesOrganizer()`

## onPick()
- 位置: L105-109
- 役割: 最近の履歴を消去する Tools:Sanitize コマンドを実行する。
- 触るとき: 履歴消去のクイックアクションの動作を変えるとき。
- 呼び出し先: `controller.browserWindow.document .getElementById()`, `controller.browserWindow.document .getElementById("Tools:Sanitize") .doCommand()`

## isUnsupported()
- 位置: L116-117
- 役割: browser.preferences.aiControls が無効のとき、AI 管理のアクションを非対応にする。
- 触るとき: AI 管理の項目を出す条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onPick()
- 位置: L149-151
- 役割: Firefox View のタブを開く。
- 触るとき: Firefox View への遷移を変えるとき。
- 呼び出し先: `controller.browserWindow.FirefoxViewHandler.openTab()`

## isUnsupported()
- 位置: L160-161
- 役割: DevTools が無効、またはこの利用者が DevTools の利用者でなければ、インスペクターを非対応にする。
- 触るとき: インスペクターを出す条件を変えるとき。
- 呼び出し先: `lazy.DevToolsShim.isDevToolsUser()`, `lazy.DevToolsShim.isEnabled()`

## isInactive()
- 位置: L165-171
- 役割: about:devtools-toolbox を開いているか、このタブにツールボックスがあれば、インスペクターを無効にし、全項目の一覧では無効状態で表示する。
- 触るとき: インスペクターが既に開いているときの表示を変えるとき。
- 呼び出し先: `currentWindow()`, `lazy.DevToolsShim.hasToolboxForTab()`, `win.gBrowser.currentURI.spec.startsWith()`
- 参照: `win.gBrowser.selectedTab`

## onPick()
- 位置: L172-174
- 役割: インスペクターのツールボックスを開く（openInspector を呼ぶ）。
- 触るとき: インスペクターを開く経路を変えるとき。
- 呼び出し先: `openInspector()`
- 参照: `controller.browserWindow`

## isUnsupported()
- 位置: L180-180
- 役割: DevTools が無効なら、スポイト（カラーピッカー）を非対応にする。
- 触るとき: カラーピッカーを出す条件を変えるとき。
- 呼び出し先: `lazy.DevToolsShim.isEnabled()`

## isInactive()
- 位置: L181-182
- 役割: 現在のページが about:devtools-toolbox なら、カラーピッカーを無効にする。
- 触るとき: ツールボックスのページでカラーピッカーの表示を変えるとき。
- 呼び出し先: `currentBrowser()`, `currentBrowser().currentURI.spec.startsWith()`

## onPick()
- 位置: L183-185
- 役割: カラーピッカーを開く（openColorPicker を呼ぶ）。
- 触るとき: カラーピッカーの起動経路を変えるとき。
- 呼び出し先: `openColorPicker()`
- 参照: `controller.browserWindow`

## onPick()
- 位置: L191-193
- 役割: ライブラリ（履歴・ブックマークの管理画面）を開く。
- 触るとき: ライブラリ画面の開き方を変えるとき。
- 呼び出し先: `controller.browserWindow.top.PlacesCommandHook.showPlacesOrganizer()`

## isInactive()
- 位置: L205-205
- 役割: 消音できる再生中のタブがなければ、ミュートを無効にする。
- 触るとき: ミュートの有効・無効の判定を変えるとき。
- 呼び出し先: `unmutedAudioTabs()`
- 参照: `unmutedAudioTabs().length`

## onPick()
- 位置: L206-210
- 役割: 音を出している未消音のタブすべてを消音（トグル）する。
- 触るとき: ミュートの対象や切り替え方を変えるとき。
- 呼び出し先: `tab.toggleMuteAudio()`, `unmutedAudioTabs()`

## isUnsupported()
- 位置: L216-218
- 役割: print.enabled が無効なら、印刷を非対応にする。
- 触るとき: 印刷の項目を出す条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onPick()
- 位置: L219-221
- 役割: 選択中のブラウザで cmd_print コマンドを実行して印刷ダイアログを開く。
- 触るとき: 印刷の起動経路を変えるとき。
- 呼び出し先: `controller.browserWindow.document.getElementById()`, `controller.browserWindow.document.getElementById("cmd_print").doCommand()`

## onPick()
- 位置: L227-229
- 役割: プライベートブラウジングのウィンドウを新しく開く。
- 触るとき: プライベートウィンドウを開く経路を変えるとき。
- 呼び出し先: `controller.browserWindow.OpenBrowserWindow()`

## isUnsupported()
- 位置: L235-235
- 役割: プロファイルのリセットが使えなければ、リフレッシュを非対応にする。
- 触るとき: リフレッシュの項目を出す条件を変えるとき。
- 呼び出し先: `lazy.ResetProfile.resetSupported()`

## onPick()
- 位置: L236-238
- 役割: プロファイルのリセットの確認ダイアログを開く。
- 触るとき: リフレッシュの確認画面の開き方を変えるとき。
- 呼び出し先: `lazy.ResetProfile.openConfirmationDialog()`
- 参照: `controller.browserWindow`

## isUnsupported()
- 位置: L250-252
- 役割: print.enabled が無効なら、PDF として保存を非対応にする。
- 触るとき: PDF 保存の項目を出す条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onPick()
- 位置: L253-266
- 役割: 「PDF に保存」プリンターを最後に使ったプリンターとして保存し、印刷ウィンドウを開く。ソースのコメントにもあるとおり、ユーザーの最後のプリンター設定を上書きする。
- 触るとき: PDF 保存で既存の印刷設定が変わる問題を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/gfx/printsettings-service;1"] .getService()`, `controller.browserWindow.PrintUtils.startPrintWindow()`
- 参照: `Ci.nsIPrintSettingsService`, `controller.browserWindow.PrintUtils.SAVE_TO_PDF_PRINTER`, `controller.browserWindow.gBrowser.selectedBrowser.browsingContext`
- XPCOM: `nsIPrintSettingsService` / `@mozilla.org/gfx/printsettings-service;1`

## isUnsupported()
- 位置: L272-274
- 役割: スクリーンショット機能が無効なら、スクリーンショットを非対応にする。
- 触るとき: スクリーンショットの項目を出す条件を変えるとき。
- 参照: `lazy.ScreenshotsUtils.screenshotsEnabled`

## onPick()
- 位置: L275-282
- 役割: menuitem-screenshot の通知を QuickActions 由来として送り、コンテンツにフォーカスを移す。
- 触るとき: スクリーンショットの起動経路や由来の記録を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `controller.browserWindow`
- XPCOM: `Services.obs`

## isUnsupported()
- 位置: L300-308
- 役割: AI 機能の翻訳と browser.translations.quickAction.enabled の両方が有効でなければ、翻訳を非対応にする。
- 触るとき: 翻訳の項目を出す条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.TranslationsParent.AIFeature.isEnabled`
- XPCOM: `Services.prefs`

## onPick()
- 位置: async L309-316
- 役割: 翻訳ページを target 言語 derive で開き、コンテンツにフォーカスを移す。
- 触るとき: 翻訳ページの開き方を変えるとき。
- 呼び出し先: `lazy.TranslationsParent.openAboutTranslationsPage()`
- 参照: `controller.browserWindow`

## isUnsupported()
- 位置: L322-323
- 役割: 更新機能がない、または通常の更新確認が使えなければ、更新を非対応にする。
- 触るとき: 更新の項目を出す条件を変えるとき。
- 参照: `AppConstants.MOZ_UPDATER`, `lazy.AUS.canUsuallyCheckForUpdates`

## isInactive()
- 位置: L324-325
- 役割: 更新の状態が保留中（pending）でなければ、更新を無効にする。
- 触るとき: 更新の再起動項目を表示する条件を変えるとき。
- 参照: `Ci.nsIApplicationUpdateService.STATE_PENDING`, `lazy.AUS.currentState`
- XPCOM: [`nsIApplicationUpdateService`](../../../toolkit/mozapps/update/nsIUpdateService.idl.md)

## isInactive()
- 位置: L332-332
- 役割: 現在のページが view-source なら、ソース表示を無効にする。
- 触るとき: ソース表示の有効・無効の判定を変えるとき。
- 呼び出し先: `currentBrowser()`
- 参照: `currentBrowser().currentURI.scheme`

## onPick()
- 位置: L333-337
- 役割: 現在のページの view-source: を開く。
- 触るとき: ソース表示の URL の作り方を変えるとき。
- 呼び出し先: `openUrl()`
- 参照: `controller.browserWindow`, `controller.browserWindow.gBrowser.currentURI.spec`

## isUnsupported()
- 位置: L343-343
- 役割: ラボ機能が有効でなければ、ラボを非対応にする。
- 触るとき: ラボの項目を出す条件を変えるとき。
- 参照: `lazy.ExperimentAPI.labsEnabled`

## openInspector()
- 位置: L348-352
- 役割: 選択中タブでインスペクターのツールボックスを開く。
- 触るとき: インスペクターの起動方法を変えるとき。
- 呼び出し先: `lazy.DevToolsShim.showToolboxForTab()`
- 参照: `window.gBrowser.selectedTab`

## openColorPicker()
- 位置: L354-360
- 役割: DevTools を初期化してから、メニューのスポイト項目を実行する。ツールボックスは開かない。
- 触るとき: カラーピッカーの起動方法を変えるとき。
- 呼び出し先: `lazy.DevToolsShim.initDevTools()`, `window.document.getElementById()`, `window.document.getElementById("menu_eyedropper")?.doCommand()`

## restartBrowser()
- 位置: L364-386
- 役割: 終了要求を通知し、取り消されなければ再起動する（セーフモードなら安全モードで再起動）。
- 触るとき: 再起動の項目が動かない、または確認なしで閉じる問題を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.startup.restartInSafeMode()`
- 条件付き依存: `if (!(Services.appinfo.inSafeMode))` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `Ci.nsISupportsPRBool`, `Services.appinfo.inSafeMode`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.appinfo` / `Services.obs` / `Services.startup`

## QuickActionsLoaderDefault.load()
- 位置: async L395-407
- 役割: 既定のアクションごとに、Fluent の文字列からコマンド語（カンマ区切り、小文字化）を作り、ActionsProviderQuickActions に登録する。
- 触るとき: 既定のクイックアクションの一覧やコマンド語を変えるとき。
- 呼び出し先: `Object.keys()`, `actionData.l10nCommands.map()`, `lazy.ActionsProviderQuickActions.addAction()`, `lazy.gFluentStrings.formatMessages()`, `messages .map()`, `messages .map(({ value }) => value.split(",").map(x => x.trim().toLowerCase())) .flat()`, `value.split()`, `value.split(",").map()`, `x.trim()`, `x.trim().toLowerCase()`
- 参照: `actionData.commands`

## QuickActionsLoaderDefault.ensureLoaded()
- 位置: async L408-413
- 役割: 読み込みを一度だけ行う（Promise をキャッシュ）。呼ぶたびに読み込み完了を待つ。
- 触るとき: クイックアクションが候補に出ない、または二重に登録される問題を調べるとき。
- 条件付き依存: `if (!this.#loadedPromise)` → `this.load()`
- 参照: `this.#loadedPromise`
