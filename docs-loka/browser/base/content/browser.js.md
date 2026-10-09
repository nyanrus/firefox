# browser/base/content/browser.js

source: browser/base/content/browser.js
source-hash: 7ce8e235dd4dafde6ed1bfa8c81c4dc1409141f1
lines: 5275

## <module>
- 役割: 最上位の browser.xhtml 用ウィンドウ制御を担う。遅延ゲッターで urlbar、通知、PopupNotifications、カスタマイズモードなどを初めて参照時に生成し、pref 監視でツールバー・FxA・印刷などの表示を切り替え、履歴メニュー、アプリコマンド、ロケーション入力、ダイアログ、Shutdown・オフラインなど、ウィンドウ全体の振る舞いを定義する。
- 呼び出し先: `Cc["@mozilla.org/widget/macuseractivityupdater;1"].getService()`, `Cc[WINTASKBAR_CONTRACTID].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Object.defineProperty()`, `Services.prefs.getIntPref()`, `Services.scriptloader.loadSubScript()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyScriptGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `console.error()`, `customElements.setElementCreationCallback()`, `document.getElementById()`, `document.getElementById("notifications-toolbar").prepend()`, `element.classList.add()`, `element.setAttribute()`, `updateFxaToolbarMenu()`, `updatePrintCommands()`, `urlbar.addEventListener()`, `window.docShell.QueryInterface()`

## gLocaleChangeObserver()
- 位置: L352-355
- 役割: アプリのロケールが変わったとき、window.RTL_UI を現在のロケールの RTL 判定で作り直す。
- 触るとき: 言語切替後にレイアウト方向(RTL)が追従しないとき、または RTL_UI を参照する箇所を調べるとき。
- 参照: `Services.locale.isAppLocaleRTL`, `window.RTL_UI`
- XPCOM: `Services.locale`

## beforeFocusOrSelect()
- 位置: L383-413
- 役割: urlbar の beforefocus・beforeselect で、カスタマイズ中または終了直後ならカスタマイズ終了後に focus や select を予約して既定動作を止め、フルスクリーン中ならナビゲーションツールボックスを表示する。
- 触るとき: カスタマイズモード中にアドレスバーへ移動するとフォーカスが効かない、またはフルスクリーンでアドレスバーを選択しても見えないとき。
- 呼び出し先: `CustomizationHandler.isCustomizing()`
- 条件付き依存: `if ( CustomizationHandler.isCustomizing() || CustomizationHandler.isExitingCustomizeMode )` → `gNavToolbox.addEventListener()`
- 条件付き依存: `if (event.type == "beforeselect")` → `gURLBar.select()`
- 条件付き依存: `if (!(event.type == "beforeselect"))` → `gURLBar.focus()`
- 条件付き依存: `if ( CustomizationHandler.isCustomizing() || CustomizationHandler.isExitingCustomizeMode )` → `event.preventDefault()`
- 条件付き依存: `if (window.fullScreen)` → `FullScreen.showNavToolbox()`
- 参照: `CustomizationHandler.isExitingCustomizeMode`, `event.type`, `window.fullScreen`

## shouldSuppress()
- 位置: L451-466
- 役割: PopupNotifications を抑止すべきか判定する。urlbar を編集中でフォーカスがある場合、読み込み中で pageproxystate が valid でない場合、shouldSuppressPopupNotifications が真の場合に true を返す。
- 触るとき: アドレスバー操作中に通知ポップアップが出ない、または出るべき通知が隠れるとき。
- 呼び出し先: `gURLBar.getAttribute()`, `gURLBar.hasAttribute()`, `isBlankPageURL()`, `shouldSuppressPopupNotifications()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser._awaitingSetURI`, `gURLBar.focused`

## getVisibleAnchorElement()
- 位置: L471-496
- 役割: 通知ポップアップの anchor を決める。urlbar 側の revert 処理を挟み、anchor が見えていればそれを返し、見えなければ信頼パネル・検索切替・ID アイコンなどの fallback の最初の可視要素を返す。どれも無ければ null を返す。
- 触るとき: 通知ポップアップが意図しない位置に出る、または anchor が隠れた状態で通知が消えるとき。
- 呼び出し先: `anchorElement?.checkVisibility()`, `anchorElement?.dispatchEvent()`, `document.getElementById()`, `element?.checkVisibility()`, `fallback.find()`, `gURLBar.maybeHandleRevertFromPopup()`, `gURLBar.querySelector()`
- 参照: `PopupNotifications.CHECK_VISIBILITY_OPTIONS`

## onOpenWindow()
- 位置: L536-541
- 役割: Windows の AeroPeek が利用可能なとき、新しいウィンドウを通知して handledOpening を立てる。
- 触るとき: Windows のタスクバーのプレビューに新しいウィンドウを出す条件を変えるとき。
- 条件付き依存: `if (aeroPeek)` → `aeroPeek.onOpenWindow()`
- 参照: `this.handledOpening`

## onCloseWindow()
- 位置: L542-546
- 役割: handledOpening が立っている場合だけ、AeroPeek にウィンドウが閉じたことを伝える。
- 触るとき: Windows でウィンドウを閉じたあとにタスクバープレビューが残るとき。
- 条件付き依存: `if (this.handledOpening)` → `aeroPeek.onCloseWindow()`
- 参照: `this.handledOpening`

## get()
- 位置: L703-707
- 役割: gReduceMotion の値を返す。テストが設定した gReduceMotionOverride が boolean ならそれを、そうでなければ gReduceMotionManager.setting を返す。
- 触るとき: アニメーションを減らすかどうかの判定元を変えるとき、またはテストで動きを止めたいとき。
- 参照: `gReduceMotionManager.setting`

## init()
- 位置: L717-726
- 役割: prefers-reduced-motion のメディアクエリに listener を付け、現在値を読み込んで setting に反映する。
- 触るとき: OS の視覚効果設定に合わせた動作抑制の初期化順序を変えるとき。
- 呼び出し先: `readSetting()`, `reduceMotionQuery.addListener()`, `window.matchMedia()`

## readSetting()
- 位置: L721-723
- 役割: メディアクエリの matches を gReduceMotionManager.setting に書き込む。
- 触るとき: reduce motion の値が古いまま残るとき。
- 参照: `reduceMotionQuery.matches`, `this.setting`

## get()
- 位置: L734-736
- 役割: gFindBar のゲッター。gBrowser.getCachedFindBar() でキャッシュ済みの検索バーを返し、未作成なら null を返す。
- 触るとき: 検索バーを強制的に作らずに参照したいとき、または検索バーの有無を確認したいとき。
- 呼び出し先: `gBrowser.getCachedFindBar()`

## get()
- 位置: L741-743
- 役割: gFindBarInitialized のゲッター。検索バーが初期化済みかを gBrowser.isFindBarInitialized() で返す。
- 触るとき: 検索バーを作らずに初期化状態だけ確認したいとき。
- 呼び出し先: `gBrowser.isFindBarInitialized()`

## get()
- 位置: L748-750
- 役割: gFindBarPromise のゲッター。gBrowser.getFindBar() で検索バーの取得を Promise として返し、必要なら作成する。
- 触るとき: 検索バーが作られた後に処理したいコードを書くとき。
- 呼び出し先: `gBrowser.getFindBar()`

## shouldSuppressPopupNotifications()
- 位置: L753-764
- 役割: 最小化中、選択中のブラウザでタブダイアログが表示中、または gDialogBox が開いているときに true を返し、通知ポップアップを抑止させる。
- 触るとき: 最小化やタブダイアログの表示時に通知が前面に出る問題を調べるとき。
- 呼び出し先: `gBrowser?.selectedBrowser.hasAttribute()`
- 参照: `gDialogBox?.isOpen`, `window.STATE_MINIMIZED`, `window.windowState`

## gLazyFindCommand()
- 位置: async L766-772
- 役割: 検索バーの Promise を待ち、検索バーに指定の関数があれば引数を渡して呼ぶ。待機中にウィンドウが閉じた場合は何もしない。
- 触るとき: キーボード操作などから検索バーのコマンドを遅延実行したいとき。
- 条件付き依存: `if (fb && fb[cmd])` → `fb[cmd].apply()`

## isInitialPage()
- 位置: L795-806
- 役割: URL を nsIURI に変換し、プレフィックスとパスが初期ページ一覧か新しいタブの URL と一致するかを返す。変換に失敗すると false を返す。
- 触るとき: about:newtab や about:home など初期ページの判定基準を増やすとき、またはそのページで特別な処理が効かないとき。
- 呼び出し先: `gInitialPages.includes()`
- 条件付き依存: `if (!(url instanceof Ci.nsIURI))` → `Services.io.newURI()`
- 参照: `Ci.nsIURI`, `url.filePath`, `url.prePath`
- XPCOM: [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## browserWindows()
- 位置: L808-810
- 役割: navigator:browser のウィンドウ列挙子を返す。
- 触るとき: 開いているブラウザウィンドウを順に調べる処理を書くとき。
- 呼び出し先: `Services.wm.getEnumerator()`
- XPCOM: `Services.wm`

## updateBookmarkToolbarVisibility()
- 位置: L812-820
- 役割: ブックマークツールバーの空メッセージを更新し、gBookmarksToolbarVisibility の設定に合わせてツールバーの表示を切り替える。
- 触るとき: ブックマークツールバーの表示設定が変わっても表示が追従しないとき。
- 呼び出し先: `BookmarkingUI.updateEmptyToolbarMessage()`, `setToolbarVisibility()`
- 参照: `BookmarkingUI.toolbar`

## getString()
- 位置: L825-827
- 役割: gBrowserBundle から指定キーの文字列を取り出す。
- 触るとき: browser.properties の文字列を JS から読むとき。
- 呼び出し先: `gBrowserBundle.GetStringFromName()`

## getFormattedString()
- 位置: L828-830
- 役割: gBrowserBundle から指定キーの文字列を引数で埋めて返す。
- 触るとき: browser.properties の書式付き文字列を JS から読むとき。
- 呼び出し先: `gBrowserBundle.formatStringFromName()`

## updateFxaToolbarMenu()
- 位置: L833-873
- 役割: アカウント(FxA)の状態を fxastatus に推測して設定する。sync と FxA が有効でタスクバータブでなければ fxatoolbarmenu を visible にし、初回以外は sync の UI を更新する。条件に合わなければ属性を外す。
- 触るとき: FxA ツールバーメニューが出ない・消えないとき、またはサインイン状態の初期表示を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `mainWindowEl.hasAttribute()`, `mainWindowEl.setAttribute()`
- 条件付き依存: `if (enable && syncEnabled && !taskbarTab)` → `mainWindowEl.setAttribute()`
- 条件付き依存: `if (!isInitialUpdate)` → `gSync.maybeUpdateUIState()`
- 条件付き依存: `if (!(enable && syncEnabled && !taskbarTab))` → `mainWindowEl.removeAttribute()`
- 参照: `document.documentElement`
- XPCOM: `Services.prefs`

## UpdateBackForwardCommands()
- 位置: L875-901
- 役割: 渡された webNavigation の canGoBack と canGoForward に合わせて、Browser:Back と Browser:Forward の disabled 属性を変化したときだけ更新する。
- 触るとき: 戻る・進むボタンの有効無効が履歴と合わないとき。
- 呼び出し先: `backCommand.hasAttribute()`, `document.getElementById()`, `forwardCommand.hasAttribute()`
- 条件付き依存: `if (backDisabled)` → `backCommand.removeAttribute()`
- 条件付き依存: `if (!(backDisabled))` → `backCommand.setAttribute()`
- 条件付き依存: `if (forwardDisabled)` → `forwardCommand.removeAttribute()`
- 条件付き依存: `if (!(forwardDisabled))` → `forwardCommand.setAttribute()`
- 参照: `aWebNavigation.canGoBack`, `aWebNavigation.canGoForward`

## updatePrintCommands()
- 位置: L903-914
- 役割: 印刷と印刷プレビューのコマンドの disabled 属性を、enabled の値に合わせて設定する。
- 触るとき: print.enabled 設定で印刷メニューが切り替わらないとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (enabled)` → `printCommand.removeAttribute()`
- 条件付き依存: `if (enabled)` → `printPreviewCommand.removeAttribute()`
- 条件付き依存: `if (!(enabled))` → `printCommand.setAttribute()`
- 条件付き依存: `if (!(enabled))` → `printPreviewCommand.setAttribute()`

## SetClickAndHoldHandlers()
- 位置: L920-949
- 役割: 戻ると進むのボタンに履歴メニューのクローンを差し込み、command で gotoHistoryIndex を、popupshowing で FillHistoryMenu を呼ぶよう設定し、長押しハンドラーの対象に登録する。
- 触るとき: 戻る・進むボタンの長押しメニューの項目や動作を変えるとき。
- 呼び出し先: `backButton.prepend()`, `backButton.setAttribute()`, `document.getElementById()`, `document.getElementById("backForwardMenu").cloneNode()`, `forwardButton.prepend()`, `forwardButton.setAttribute()`, `gClickAndHoldListenersOnElement.add()`, `popup.addEventListener()`, `popup.cloneNode()`, `popup.removeAttribute()`, `popup.setAttribute()`

## backForwardMenuCommand()
- 位置: L927-933
- 役割: 選ばれた履歴項目で gotoHistoryIndex を呼び、クリックがボタン側へ伝播しないよう stopPropagation する。
- 触るとき: 履歴メニューの項目を選んだときに別のボタン動作が走ってしまうとき。
- 呼び出し先: `BrowserCommands.gotoHistoryIndex()`, `event.stopPropagation()`

## _mousedownHandler()
- 位置: L954-972
- 役割: 左ボタンで押され、メニューが開いておらず無効でもなければ、メニューを一時的に隠して 500ms 後に開くタイマーを予約し、mouseout と mouseup を監視する。
- 触るとき: 戻る・進むボタンを押し続けたときに履歴メニューが開くタイミングを変えるとき。
- 呼び出し先: `aEvent.currentTarget.addEventListener()`, `setTimeout()`, `this._openMenu()`, `this._timers.set()`
- 参照: `aEvent.button`, `aEvent.currentTarget`, `aEvent.currentTarget.disabled`, `aEvent.currentTarget.menupopup.hidden`, `aEvent.currentTarget.open`

## _clickHandler()
- 位置: L974-1010
- 役割: 左クリックで、ボタン自身がターゲットで、メニューが開いておらず隠れたままのとき、command イベントを発火させて既定の click を打ち消す。長押しで開いたメニューの mouseup と二重処理しないよう除外する。
- 触るとき: 戻る・進むボタンのクリックで command が二重に飛ぶ、または一度も飛ばないとき。
- 条件付き依存: `if ( aEvent.button == 0 && aEvent.target == aEvent.currentTarget && !aEvent.currentTarget.open && !aEvent.currentTarget.disabled && // When menupopup is not hidd...)` → `document.createEvent()`
- 条件付き依存: `if ( aEvent.button == 0 && aEvent.target == aEvent.currentTarget && !aEvent.currentTarget.open && !aEvent.currentTarget.disabled && // When menupopup is not hidd...)` → `cmdEvent.initCommandEvent()`
- 条件付き依存: `if ( aEvent.button == 0 && aEvent.target == aEvent.currentTarget && !aEvent.currentTarget.open && !aEvent.currentTarget.disabled && // When menupopup is not hidd...)` → `aEvent.currentTarget.dispatchEvent()`
- 条件付き依存: `if ( aEvent.button == 0 && aEvent.target == aEvent.currentTarget && !aEvent.currentTarget.open && !aEvent.currentTarget.disabled && // When menupopup is not hidd...)` → `aEvent.preventDefault()`
- 参照: `aEvent.altKey`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.currentTarget`, `aEvent.currentTarget.disabled`, `aEvent.currentTarget.menupopup.hidden`, `aEvent.currentTarget.open`, `aEvent.inputSource`, `aEvent.metaKey`, `aEvent.shiftKey`, `aEvent.target`

## _openMenu()
- 位置: L1012-1016
- 役割: 保留中のタイマーを取り消し、メニューを表示して open 状態にする。
- 触るとき: 長押しで開く履歴メニューの表示処理を変えるとき。
- 呼び出し先: `this._cancelHold()`
- 参照: `aButton.firstElementChild.hidden`, `aButton.open`

## _mouseoutHandler()
- 位置: L1018-1029
- 役割: ボタンの矩形の下端より下へマウスが出たときは _openMenu でメニューを開き、それ以外は保留を取り消す。
- 触るとき: 押したままドラッグして履歴メニューを開く操作の判定を調整するとき。
- 呼び出し先: `aEvent.currentTarget.getBoundingClientRect()`
- 条件付き依存: `if ( aEvent.clientX >= buttonRect.left && aEvent.clientX <= buttonRect.right && aEvent.clientY >= buttonRect.bottom )` → `this._openMenu()`
- 条件付き依存: `if (!( aEvent.clientX >= buttonRect.left && aEvent.clientX <= buttonRect.right && aEvent.clientY >= buttonRect.bottom ))` → `this._cancelHold()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.currentTarget`, `buttonRect.bottom`, `buttonRect.left`, `buttonRect.right`

## _mouseupHandler()
- 位置: L1031-1033
- 役割: mouseup で保留中の長押しを取り消す。
- 触るとき: ボタンを離した後にメニューが開く不具合を調べるとき。
- 呼び出し先: `this._cancelHold()`
- 参照: `aEvent.currentTarget`

## _cancelHold()
- 位置: L1035-1039
- 役割: 保留中のタイマーを消し、mouseout と mouseup の監視を外す。
- 触るとき: 長押しの後始末が漏れてメニューが勝手に開くとき。
- 呼び出し先: `aButton.removeEventListener()`, `clearTimeout()`, `this._timers.get()`

## _keypressHandler()
- 位置: L1041-1049
- 役割: Space か Enter で既定動作を止め、target の click を呼ぶ。type=menu では command が飛ばないため、クリックと同じ経路で処理する。
- 触るとき: キーボードで戻る・進むのメニューを開閉できないとき。
- 条件付き依存: `if (aEvent.key == " " || aEvent.key == "Enter")` → `aEvent.preventDefault()`
- 条件付き依存: `if (aEvent.key == " " || aEvent.key == "Enter")` → `aEvent.target.click()`
- 参照: `aEvent.key`

## handleEvent()
- 位置: L1051-1073
- 役割: mouseout、mousedown、click、mouseup、keypress の各イベントを対応する内部ハンドラーへ振り分ける。keypress は既定動作が止められていないときだけ処理する。
- 触るとき: 長押しハンドラーにイベント種類を追加するとき。
- 呼び出し先: `this._clickHandler()`, `this._mousedownHandler()`, `this._mouseoutHandler()`, `this._mouseupHandler()`
- 条件付き依存: `if (!e.defaultPrevented)` → `this._keypressHandler()`
- 参照: `e.defaultPrevented`, `e.type`

## remove()
- 位置: L1075-1079
- 役割: ボタンからキャプチャ付きの mousedown、click、keypress リスナーを外す。
- 触るとき: 長押し機能を要素から外す処理を変えるとき。
- 呼び出し先: `aButton.removeEventListener()`

## add()
- 位置: L1081-1087
- 役割: 保留中のタイマーを消し、ボタンにキャプチャ付きで mousedown、click、keypress の監視を付ける。
- 触るとき: 長押し機能を新しいボタンに付けるとき。
- 呼び出し先: `aElm.addEventListener()`, `this._timers.delete()`

## observe()
- 位置: L1091-1103
- 役割: browser:purge-session-history を受けて、戻る・進むを disabled にし、URL バーの undo 履歴を消す。
- 触るとき: 履歴の消去後にも戻る・進むが有効に見える、または URL バーの undo が残るとき。
- 呼び出し先: `backCommand.setAttribute()`, `document.getElementById()`, `fwdCommand.setAttribute()`, `gURLBar.editor.clearUndoRedo()`

## observe()
- 位置: async L1109-1181
- 役割: QuotaManager の StoragePressure 通知を受け、既に通知が出ていたり最小間隔内なら何もしない。そうでなければ使用量が閾値未満か以上かでメッセージを選び、設定ボタン付きの storage-permissions 通知を出す。
- 触るとき: ストレージ不足の警告の文言、表示間隔、閾値を変えるとき。
- 呼び出し先: `Date.now()`, `MozXULElement.insertFTLIfNeeded()`, `Services.prefs.getIntPref()`, `document.createDocumentFragment()`, `document.createElement()`, `document.l10n.translateFragment()`, `gNotificationBox.appendNotification()`, `gNotificationBox.getNotificationWithValue()`, `messageFragment.appendChild()`, `subject.QueryInterface()`
- 条件付き依存: `if (usage < USAGE_THRESHOLD_BYTES)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(usage < USAGE_THRESHOLD_BYTES))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(usage < USAGE_THRESHOLD_BYTES))` → `buttons.push()`
- 参照: `Ci.nsISupportsPRUint64`, `gNotificationBox.PRIORITY_WARNING_HIGH`, `gNotificationBox.currentNotification`, `subject.QueryInterface(Ci.nsISupportsPRUint64).data`, `this._lastNotificationTime`
- XPCOM: [`nsISupportsPRUint64`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `Services.prefs`

## callback()
- 位置: L1160-1164
- 役割: ストレージ通知の設定ボタンが押されたとき、サイトデータのプライバシー設定を開く。
- 触るとき: ストレージ警告からの設定画面の遷移先を変えるとき。
- 呼び出し先: `openPreferences()`

## check()
- 位置: L1185-1298
- 役割: キーワード検索になった URL を非同期の DNS 照会にかけ、ホストとして解決できる可能性があれば infobar での移動提案を準備する。既定の DNS 優先設定などで条件を満たさないときは何もしない。
- 触るとき: アドレスバーの検索語がホストとして解決される場合の案内を変えるとき、または誤って検索に切り替わるとき。
- 呼び出し先: `Cu.getWeakReference()`, `Services.uriFixup.checkHost()`, `UrlbarPrefs.get()`
- 参照: `browser.contentPrincipal`, `browser.currentURI`, `contentPrincipal.originAttributes`, `fixedURI.asciiHost`, `fixedURI.displayHost`, `fixedURI.host`
- XPCOM: `Services.uriFixup`

## onLookupComplete()
- 位置: async L1222-1286
- 役割: DNS 照会が成功し、ブラウザがまだ元のページか検索先にいる場合に限り、keyword-uri-fixup の infobar を追加する。別ページへ移動済みなら表示しない。
- 触るとき: ホスト移動の案内が古いタブに出る、または出るべき場面で出ないとき。
- 呼び出し先: `Components.isSuccessCode()`, `currentURI.equals()`, `gBrowser.getNotificationBox()`, `gNavigatorBundle.getFormattedString()`, `gNavigatorBundle.getString()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `weakBrowser.get()`
- 参照: `browserRef.currentURI`, `notification.persistence`, `notificationBox.PRIORITY_INFO_HIGH`

## callback()
- 位置: L1259-1274
- 役割: infobar の移動ボタンが押されたら、非プライベートなら browser.fixup.domainwhitelist.<ホスト> を true にして、修正後の URL を現在のタブで開く。
- 触るとき: ホストの許可リストの保存条件や移動先を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `openTrustedLinkIn()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(window))` → `prefHost.indexOf()`
- 条件付き依存: `if (prefHost.indexOf(".") == prefHost.length - 1)` → `prefHost.slice()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(window))` → `Services.prefs.setBoolPref()`
- 参照: `fixedURI.spec`, `prefHost.length`
- XPCOM: `Services.prefs`

## observe()
- 位置: L1300-1309
- 役割: fixupInfo の consumer から、このウィンドウのブラウザ要素を取り出せた場合だけ check を呼ぶ。
- 触るとき: 別ウィンドウ向けの URL 修正通知が混ざるとき。
- 呼び出し先: `fixupInfo.QueryInterface()`, `this.check()`
- 参照: `Ci.nsIURIFixupInfo`, `browser.documentGlobal`, `fixupInfo.consumer?.top?.embedderElement`
- XPCOM: [`nsIURIFixupInfo`](../../../docshell/base/nsIURIFixup.idl.md)

## HandleAppCommandEvent()
- 位置: L1312-1366
- 役割: アプリコマンド(戻る、進む、再読込、検索、ブックマーク、印刷、保存など)を、対応するブラウザコマンドへ振り分け、処理したら伝播と既定動作を止める。
- 触るとき: マウスや多機能キーのアプリコマンドに新しい動作を追加するとき、または対応しないコマンドが無視されるとき。
- 呼び出し先: `BrowserCommands.back()`, `BrowserCommands.closeTabOrWindow()`, `BrowserCommands.forward()`, `BrowserCommands.home()`, `BrowserCommands.openFileWindow()`, `BrowserCommands.openTab()`, `BrowserCommands.reloadSkipCache()`, `MailIntegration.sendLinkForBrowser()`, `PrintUtils.startPrintWindow()`, `SearchUIUtils.webSearch()`, `SidebarController.toggle()`, `XULBrowserWindow.stopCommand.hasAttribute()`, `evt.preventDefault()`, `evt.stopPropagation()`, `gLazyFindCommand()`, `openHelpLink()`, `saveBrowser()`
- 条件付き依存: `if (XULBrowserWindow.stopCommand.hasAttribute("disabled"))` → `BrowserCommands.stop()`
- 参照: `evt.command`, `gBrowser.selectedBrowser`, `gBrowser.selectedBrowser.browsingContext`

## loadOneOrMoreURIs()
- 位置: L1368-1396
- 役割: ブラウザウィンドウ以外では URI を新しいブラウザウィンドウへ渡す。ブラウザウィンドウでは | 区切りの URI を gBrowser.loadTabs で読み込み、例外は握りつぶして起動を妨げない。
- 触るとき: コマンドライン引数や起動時の URL 読み込みで、複数 URL の扱いを変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `aURIString.split()`, `gBrowser.loadTabs()`
- 条件付き依存: `if (window.location.href != AppConstants.BROWSER_CHROME_URL)` → `window.openDialog()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `window.location.href`
- XPCOM: `Services.scriptSecurityManager`

## openLocation()
- 位置: L1398-1421
- 役割: ブラウザウィンドウならアドレスバーを選択して候補を開く。そうでなければ既存のブラウザウィンドウへ転送し、無ければ新しいウィンドウを新規タブで開く。
- 触るとき: Ctrl+L などの場所を開く操作の挙動を変えるとき。
- 呼び出し先: `URILoadingHelper.getTargetWindow()`, `window.openDialog()`
- 条件付き依存: `if (window.location.href == AppConstants.BROWSER_CHROME_URL)` → `UrlbarUtils.getURLBarForFocus()`
- 条件付き依存: `if (window.location.href == AppConstants.BROWSER_CHROME_URL)` → `focusTarget.select()`
- 条件付き依存: `if (window.location.href == AppConstants.BROWSER_CHROME_URL)` → `focusTarget.view.autoOpen()`
- 条件付き依存: `if (win)` → `win.focus()`
- 条件付き依存: `if (win)` → `win.openLocation()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `window.location.href`

## path()
- 位置: L1425-1438
- 役割: 最後に開いたディレクトリを返す。キャッシュが無効なら browser.open.lastDir から読み直し、存在しなければ null を返す。
- 触るとき: ファイルを開くダイアログの初期ディレクトリが保存されないとき。
- 呼び出し先: `this._lastDir.exists()`
- 条件付き依存: `if (!this._lastDir || !this._lastDir.exists())` → `Services.prefs.getComplexValue()`
- 条件付き依存: `if (!this._lastDir || !this._lastDir.exists())` → `this._lastDir.exists()`
- 参照: `Ci.nsIFile`, `this._lastDir`
- XPCOM: [`nsIFile`](../../components/shell/nsIShellService.idl.md) / `Services.prefs`

## path()
- 位置: L1439-1457
- 役割: 有効なディレクトリだけを最後に開いたディレクトリとして保存し、プライベートウィンドウでなければ browser.open.lastDir に書き出す。
- 触るとき: 最後に開いたディレクトリの保存条件を変えるとき、またはプライベートウィンドウで保存されてしまうとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `val.clone()`, `val.isDirectory()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(window))` → `Services.prefs.setComplexValue()`
- 参照: `Ci.nsIFile`, `this._lastDir`
- XPCOM: [`nsIFile`](../../components/shell/nsIShellService.idl.md) / `Services.prefs`

## reset()
- 位置: L1458-1460
- 役割: 保持している最後に開いたディレクトリを破棄する。
- 触るとき: ディレクトリの記憶を消す処理を追加するとき。
- 参照: `this._lastDir`

## readFromClipboard()
- 位置: L1463-1493
- 役割: 選択クリップボード(対応時)またはグローバルクリップボードから text/plain を読み、文字列を返す。取得に失敗したら空文字を返す。
- 触るとき: 中クリックやドロップで貼り付ける内容の取得元を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `clipboard.isClipboardTypeSupported()`, `trans.addDataFlavor()`, `trans.getTransferData()`, `trans.init()`, `window.docShell.QueryInterface()`
- 条件付き依存: `if (clipboard.isClipboardTypeSupported(clipboard.kSelectionClipboard))` → `clipboard.getData()`
- 条件付き依存: `if (!(clipboard.isClipboardTypeSupported(clipboard.kSelectionClipboard)))` → `clipboard.getData()`
- 条件付き依存: `if (data)` → `data.value.QueryInterface()`
- 参照: `Ci.nsILoadContext`, `Ci.nsISupportsString`, `Ci.nsITransferable`, `Services.clipboard`, `clipboard.kGlobalClipboard`, `clipboard.kSelectionClipboard`, `data.data`
- XPCOM: [`nsILoadContext`](../../../docshell/base/nsILoadContext.idl.md) / [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## UpdateUrlbarSearchSplitterState()
- 位置: L1495-1545
- 役割: アドレスバーと検索バーの間にリサイズ用のスプリッターを、並びに応じて挿入・移動・削除する。カスタマイズ中はスプリッターを削除する。
- 触るとき: ツールバーの並びを変えたあとにスプリッターの位置が合わないとき、またはカスタマイズ中の表示を変えるとき。
- 呼び出し先: `document.documentElement.hasAttribute()`, `document.getElementById()`
- 条件付き依存: `if (splitter)` → `splitter.remove()`
- 条件付き依存: `if (!splitter)` → `document.createXULElement()`
- 条件付き依存: `if (!splitter)` → `splitter.setAttribute()`
- 条件付き依存: `if (ibefore)` → `urlbar.parentNode.insertBefore()`
- 参照: `searchbar.nextElementSibling`, `splitter.className`, `splitter.id`, `splitter.nextElementSibling`, `splitter.previousElementSibling`, `urlbar.nextElementSibling`

## UpdatePopupNotificationsVisibility()
- 位置: L1547-1561
- 役割: PopupNotifications が初期化済みなら anchor の可視性を再評価させ、PanelUI の通知表示も更新する。
- 触るとき: ツールバー等の表示が変わったあとに通知の位置や表示が古いままのとき。
- 呼び出し先: `Object.getOwnPropertyDescriptor()`, `PanelUI?.updateNotifications()`
- 条件付き依存: `if (!Object.getOwnPropertyDescriptor(window, "PopupNotifications").get)` → `PopupNotifications.anchorVisibilityChange()`
- 参照: `Object.getOwnPropertyDescriptor(window, "PopupNotifications").get`

## PageProxyClickHandler()
- 位置: L1563-1567
- 役割: 中ボタンで、middlemouse.paste が有効なら middleMousePaste を呼ぶ。
- 触るとき: ページアイコンなどを中クリックしたときの貼り付け動作を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (aEvent.button == 1 && Services.prefs.getBoolPref("middlemouse.paste"))` → `middleMousePaste()`
- 参照: `aEvent.button`
- XPCOM: `Services.prefs`

## CreateContainerTabMenu()
- 位置: L1569-1580
- 役割: メニュー内から開かれた場合は既定動作を止めて何もしない。それ以外は new_tab_button 向けのコンテナタブ用メニューを作成する。
- 触るとき: 新規タブボタンのコンテナメニューの表示条件を変えるとき。
- 呼び出し先: `createUserContextMenu()`, `event.target.triggerNode?.closest()`
- 条件付き依存: `if (event.target.triggerNode?.closest("menupopup"))` → `event.preventDefault()`

## FillHistoryMenu()
- 位置: L1582-1737
- 役割: 戻る・進むの履歴メニューの中身を作る。初回表示時に項目へ状態表示のリスナーを付け、既存の項目を消してから updateSessionHistory で作り直す。履歴が 1 件以下なら既定動作を止めて表示しない。
- 触るとき: 戻る・進むの長押しや右クリックで出る履歴メニューの項目数や並びを変えるとき、または履歴が 1 件のときにメニューが出ない原因を調べるとき。
- 呼び出し先: `children[i].hasAttribute()`, `gNavigatorBundle.getString()`
- 条件付き依存: `if (!parent.hasStatusListener)` → `parent.addEventListener()`
- 条件付き依存: `if (!parent.hasStatusListener)` → `aEvent.target.hasAttribute()`
- 条件付き依存: `if (!aEvent.target.hasAttribute("checked"))` → `XULBrowserWindow.setOverLink()`
- 条件付き依存: `if (!aEvent.target.hasAttribute("checked"))` → `aEvent.target.getAttribute()`
- 条件付き依存: `if (!parent.hasStatusListener)` → `XULBrowserWindow.setOverLink()`
- 条件付き依存: `if (children[i].hasAttribute("index"))` → `parent.removeChild()`
- 条件付き依存: `if (sessionHistory.count <= 1)` → `event.preventDefault()`
- 条件付き依存: `if (sessionHistory?.count)` → `updateSessionHistory()`
- 条件付き依存: `if (!(sessionHistory?.count))` → `SessionStore.getSessionHistory()`
- 条件付き依存: `if (!(sessionHistory?.count))` → `updateSessionHistory()`
- 参照: `children.length`, `event.target`, `gBrowser.selectedBrowser.browsingContext.sessionHistory`, `gBrowser.selectedTab`, `parent.children`, `parent.hasStatusListener`, `sessionHistory.count`, `sessionHistory?.count`

## updateSessionHistory()
- 位置: L1615-1717
- 役割: 履歴の現在位置を中心に最大 15 件を選び、ユーザー操作を伴わないエントリーは除いて menuitem を再利用または追加する。現在位置は checked にし、前は back、後ろは forward のクラスとツールチップを付ける。初回以外は余った項目を削除し、件数が 1 以下なら閉じる。
- 触るとき: 履歴メニューの表示件数、並び、現在項目の表示、またはユーザー操作のない履歴の扱いを変えるとき。
- 呼び出し先: `Math.floor()`, `Math.max()`, `Math.min()`, `document.createXULElement()`, `item.setAttribute()`, `sessionHistory.getEntryAtIndex()`
- 条件付き依存: `if (count <= 1)` → `parent.hidePopup()`
- 条件付き依存: `if (end == count)` → `Math.max()`
- 条件付き依存: `if (j != index)` → `item.style.setProperty()`
- 条件付き依存: `if (j != index)` → `CSS.escape()`
- 条件付き依存: `if (j < index)` → `item.setAttribute()`
- 条件付き依存: `if (j == index)` → `item.setAttribute()`
- 条件付き依存: `if (!(j == index))` → `item.setAttribute()`
- 条件付き依存: `if (!item.parentNode)` → `parent.appendChild()`
- 条件付き依存: `if (!initial)` → `parent.removeChild()`
- 参照: `BrowserUtils.navigationRequireUserInteraction`, `children.length`, `entry.URI.spec`, `entry.hasUserInteraction`, `entry.title`, `entry.url`, `item.className`, `item.parentNode`, `parent.id`, `parent.lastElementChild`, `parent.parentNode.open`, `sessionHistory.count`, `sessionHistory.entries`, `sessionHistory.entries.length`, `sessionHistory.index`

## toOpenWindowByType()
- 位置: L1739-1749
- 役割: 指定した種類の最新ウィンドウがあれば前面に出し、無ければ features 付きで新しいウィンドウを開く。features が無ければ chrome,resizable,toolbar で開く。
- 触るとき: 既存の特定種別のウィンドウを再利用する経路を追加または変えるとき。
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (topWindow)` → `topWindow.focus()`
- 条件付き依存: `if (features)` → `window.open()`
- 条件付き依存: `if (!(features))` → `window.open()`
- XPCOM: `Services.wm`

## OpenBrowserWindow()
- 位置: L1756-1772
- 役割: BrowserWindowTracker.openWindow で新しいブラウザウィンドウを開き、MozAfterPaint までの時間を Glean の newWindow 計測に記録する。opener が未指定なら現在のウィンドウを使う。
- 触るとき: 新しいウィンドウを開く経路を追加するとき、またはウィンドウ作成の性能計測を見直すとき。
- 呼び出し先: `BrowserWindowTracker.openWindow()`, `Glean.browserTimings.newWindow.start()`, `Glean.browserTimings.newWindow.stopAndAccumulate()`, `win.addEventListener()`
- 参照: `options.openerWindow`

## updateEditUIVisibility()
- 位置: L1794-1872
- 役割: 編集 UI(編集メニュー、コンテキストメニュー、ツールバーの切り取り・コピー・貼り付け、メインメニュー)が見えているかを判定し、見えていれば編集コマンドの有効状態を更新、見えていなければ全ての編集コマンドを有効のままにして既存の遅延判定に任せる。macOS では何もしない。
- 触るとき: フォーカス変更時の編集コマンド更新を減らす仕組みを変えるとき、または編集ショートカットが効かない・Cut などが無効表示のままのとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!gEditUIVisible)` → `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (!gEditUIVisible)` → `CustomizableUI.getAreaType()`
- 条件付き依存: `if (areaType == CustomizableUI.TYPE_PANEL)` → `kOpenPopupStates.includes()`
- 条件付き依存: `if (placement.area == "nav-bar")` → `document.getElementById()`
- 条件付き依存: `if (placement.area == "nav-bar")` → `editControls.hasAttribute()`
- 条件付き依存: `if (placement.area == "nav-bar")` → `kOpenPopupStates.includes()`
- 条件付き依存: `if (!gEditUIVisible)` → `kOpenPopupStates.includes()`
- 条件付き依存: `if (gEditUIVisible)` → `goUpdateGlobalEditMenuItems()`
- 条件付き依存: `if (!(gEditUIVisible))` → `goSetCommandEnabled()`
- 参照: `AppConstants.platform`, `CustomizableUI.TYPE_PANEL`, `CustomizableUI.TYPE_TOOLBAR`, `PanelUI.overflowPanel`, `PanelUI.panel.state`, `customizablePanel.state`, `document.getElementById( "contentAreaContextMenu" ).state`, `document.getElementById("menu_EditPopup").state`, `document.getElementById("placesContext").state`, `document.getElementById("widget-overflow").state`, `placement.area`, `window.toolbar.visible`

## updateUserContextUIVisibility()
- 位置: L1879-1889
- 役割: privacy.userContext.enabled に応じてコンテナの新規メニューを表示または非表示にし、プライベートウィンドウでは無効化する。
- 触るとき: コンテナ機能の有効条件やプライベートウィンドウでのメニュー扱いを変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `document.getElementById()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `menu.setAttribute()`
- 参照: `menu.hidden`
- XPCOM: `Services.prefs`

## updateImportCommandEnabledState()
- 位置: L1895-1901
- 役割: profileImport のポリシーが許可されていなければ、『他のブラウザからインポート』コマンドを無効化する。
- 触るとき: エンタープライズポリシーでインポートを止める挙動を変えるとき。
- 呼び出し先: `Services.policies.isAllowed()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document .getElementById("cmd_file_importFromAnotherBrowser") .setAttribute()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document .getElementById()`
- XPCOM: `Services.policies`

## updateTabCloseCountState()
- 位置: L1907-1916
- 役割: ウィンドウを閉じる項目が隠れていれば『閉じる』の文言を通常にし、そうでなければ選択中のタブ数を含む文言に切り替える。
- 触るとき: ファイルメニューの『閉じる』の表示文言を変えるとき、または複数選択時のラベルがおかしいとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (document.getElementById("menu_closeWindow").hidden)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(document.getElementById("menu_closeWindow").hidden))` → `document.l10n.setAttributes()`
- 参照: `document.getElementById("menu_closeWindow").hidden`, `gBrowser.selectedTabs.length`

## onPopupShowing()
- 位置: L1918-1946
- 役割: ファイルメニューの表示時に、コンテナ・インポート・タブ数の文言・共有メニュー・印刷設定を更新し、AI ウィンドウとクラシックウィンドウの新規メニューの表示を切り替える。サブメニューの表示は対象外。
- 触るとき: ファイルメニューの項目を追加・削除するとき、または AI ウィンドウとクラシックウィンドウの新規メニューの出し分けを変えるとき。
- 呼び出し先: `AIWindow.isAIWindowActive()`, `AIWindow.isAIWindowEnabled()`, `PrintUtils.updatePrintSetupMenuHiddenState()`, `event.target.querySelector()`, `this.updateImportCommandEnabledState()`, `this.updateUserContextUIVisibility()`
- 条件付き依存: `if (typeof gBrowser != "undefined")` → `this.updateTabCloseCountState()`
- 条件付き依存: `if (typeof gBrowser != "undefined")` → `SharingUtils.ensureShareMenu()`
- 条件付き依存: `if (typeof gBrowser != "undefined")` → `gBrowser.selectedTabs.map()`
- 条件付き依存: `if (typeof gBrowser != "undefined")` → `document.getElementById()`
- 参照: `aiWindowMenu.hidden`, `classicWindowMenu.hidden`, `event.target.id`, `gBrowser.selectedBrowser`, `gBrowser.selectedTabs.length`, `t.linkedBrowser`

## openNewUserContextTab()
- 位置: L1957-1964
- 役割: コンテナ(userContext)メニュー項目の data-usercontextid を読み、そのコンテナで新規タブを開く。
- 触るとき: コンテナタブのメニューから開くタブの属性やソースを変えるとき。
- 呼び出し先: `event.target.getAttribute()`, `openTrustedLinkIn()`, `parseInt()`
- 参照: `event.target.dataset.containerEntrypoint`

## stopCommand()
- 位置: L1982-1985
- 役割: Browser:Stop 要素を初回参照時に取り出し、以後はキャッシュする(遅延ゲッター)。
- 触るとき: 読み込み停止ボタンの状態を更新する箇所を追加するとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.stopCommand`

## reloadCommand()
- 位置: L1986-1989
- 役割: Browser:Reload 要素を初回参照時に取り出し、以後はキャッシュする(遅延ゲッター)。
- 触るとき: 再読み込みボタンの有効無効を切り替える箇所を追加するとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.reloadCommand`

## _elementsForTextBasedTypes()
- 位置: L1990-1997
- 役割: テキスト系の文書のときだけ表示する項目(ページのスタイル、選択範囲のソース表示、選択範囲の印刷)を遅延で集める。
- 触るとき: テキスト表示時にだけ有効な項目を増やすとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._elementsForTextBasedTypes`

## _elementsForFind()
- 位置: L1998-2005
- 役割: 検索系のコマンド(検索、次を検索、前を検索)を遅延で集める。
- 触るとき: ページ内検索の項目を増やすとき、またはテキストでない文書で検索が有効になるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._elementsForFind`

## _elementsForViewSource()
- 位置: L2006-2012
- 役割: ソース表示の項目(コンテキストメニューと View:PageSource)を遅延で集める。
- 触るとき: ソース表示を無効化する条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._elementsForViewSource`

## _menuItemForRepairTextEncoding()
- 位置: L2013-2018
- 役割: 文字エンコーディングの修復メニュー項目を遅延で取り出す。
- 触るとき: 文字コードの修復項目の有効条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._menuItemForRepairTextEncoding`

## _menuItemForTranslations()
- 位置: L2019-2023
- 役割: 翻訳コマンド(cmd_translate)を遅延で取り出す。
- 触るとき: 翻訳コマンドの有効無効を切り替えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._menuItemForTranslations`

## _moreToolsTranslateMenuItem()
- 位置: L2024-2029
- 役割: その他のツール内の翻訳項目(cmd_openAboutTranslations)を遅延で取り出す。
- 触るとき: 翻訳の設定画面を開く項目を追加または変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._moreToolsTranslateMenuItem`

## setDefaultStatus()
- 位置: L2031-2034
- 役割: 既定のステータス文字列を保存し、ステータスパネルを更新する。
- 触るとき: 読み込み中や停止時の既定ステータス表示を変えるとき。
- 呼び出し先: `StatusPanel.update()`
- 参照: `this.defaultStatus`

## setOverLink()
- 位置: L2045-2073
- 役割: マウスを重ねたリンクの URL を、OverLink イベントで通知し、表示用に unescape と双方向制御文字の符号化、trimURLs 設定による短縮を施してから保持し、LinkTargetDisplay を更新する。
- 触るとき: リンクにカーソルを重ねたときのステータス表示の文字列や通知を変えるとき。
- 呼び出し先: `LinkTargetDisplay.update()`, `window.dispatchEvent()`
- 条件付き依存: `if (url)` → `Services.textToSubURI.unEscapeURIForUI()`
- 条件付き依存: `if (url)` → `url.replace()`
- 条件付き依存: `if (url)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("trimURLs"))` → `BrowserUIUtils.trimURL()`
- 参照: `this.overLink`
- XPCOM: `Services.textToSubURI`

## onEnterDOMFullscreen()
- 位置: L2075-2080
- 役割: DOM フルスクリーンに入ったとき、ステータス文字列を空にし、既定ステータスを消して、リンク表示を即座に隠す。
- 触るとき: フルスクリーン時にステータスパネルが残るとき。
- 呼び出し先: `this.setDefaultStatus()`, `this.setOverLink()`
- 参照: `this.status`

## showTooltip()
- 位置: L2082-2104
- 役割: ドラッグ中、またはウィンドウにフォーカスが無いときは表示せず、それ以外はリモートブラウザ用のツールチップを画面座標で表示する。
- 触るとき: リモートコンテンツのツールチップの表示条件や位置を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/widget/dragservice;1"] .getService()`, `Cc["@mozilla.org/widget/dragservice;1"] .getService(Ci.nsIDragService) .getCurrentSession()`, `document.getElementById()`, `document.hasFocus()`, `elt.openPopupAtScreen()`
- 参照: `Ci.nsIDragService`, `elt.label`, `elt.style.direction`, `window.devicePixelRatio`
- XPCOM: `nsIDragService` / `@mozilla.org/widget/dragservice;1`

## hideTooltip()
- 位置: L2106-2109
- 役割: リモートブラウザ用のツールチップを閉じる。
- 触るとき: ツールチップが残るときの後始末を調べるとき。
- 呼び出し先: `document.getElementById()`, `elt.hidePopup()`

## getTabCount()
- 位置: L2111-2113
- 役割: 現在のウィンドウのタブ数を返す。
- 触るとき: タブ数に応じた処理を書くとき。
- 参照: `gBrowser.tabs.length`

## onProgressChange()
- 位置: L2115-2117
- 役割: 進捗変化の通知を受けるが何もしない。
- 触るとき: 進捗表示を追加するときの入口として使う。

## onProgressChange64()
- 位置: L2119-2135
- 役割: 64 ビット版の進捗通知を、そのまま onProgressChange へ渡す。
- 触るとき: 進捗通知の引数を変えるとき。
- 呼び出し先: `this.onProgressChange()`

## onStateChange()
- 位置: L2138-2259
- 役割: 選択中タブの読み込み状態を処理する。開始時は通信中フラグ、停止ボタン、保護アイコンの初期化、Stop/Reload の切替を行う。停止時はステータスを戻し、表示 ソース項目と文字コード項目を更新し、停止ボタンを無効にして Reload に切り替える。
- 触るとき: 読み込み開始・終了時の UI(停止ボタン、スピナー、保護アイコン、ステータス)の挙動を変えるとき、または読み込みが終わっても Stop が残るとき。
- 呼び出し先: `gProtectionsHandler.onStateChange()`
- 条件付き依存: `if (aRequest && aWebProgress.isTopLevel)` → `OpenSearchManager.clearEngines()`
- 条件付き依存: `if ( !(aStateFlags & nsIWebProgressListener.STATE_RESTORING) && aWebProgress.isTopLevel )` → `StatusPanel.update()`
- 条件付き依存: `if ( !(aStateFlags & nsIWebProgressListener.STATE_RESTORING) && aWebProgress.isTopLevel )` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if ( !Object.getOwnPropertyDescriptor(window, "gTrustPanelHandler").get )` → `gTrustPanelHandler.resetIconForNavigation()`
- 条件付き依存: `if (this.spinCursorWhileBusy)` → `window.setCursor()`
- 条件付き依存: `if ( !(aStateFlags & nsIWebProgressListener.STATE_RESTORING) && aWebProgress.isTopLevel )` → `this.stopCommand.removeAttribute()`
- 条件付き依存: `if ( !(aStateFlags & nsIWebProgressListener.STATE_RESTORING) && aWebProgress.isTopLevel )` → `CombinedStopReload.switchToStop()`
- 条件付き依存: `if (location.spec != "about:blank")` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (aRequest)` → `this.setDefaultStatus()`
- 条件付き依存: `if (aRequest)` → `BrowserUtils.mimeTypeIsTextBased()`
- 条件付き依存: `if (canViewSource && isText)` → `element.removeAttribute()`
- 条件付き依存: `if (!(canViewSource && isText))` → `element.setAttribute()`
- 条件付き依存: `if (aRequest)` → `this._updateElementsForContentType()`
- 条件付き依存: `if (aRequest)` → `document.getElementById()`
- 条件付き依存: `if (browser.mayEnableCharacterEncodingMenu)` → `this._menuItemForRepairTextEncoding.removeAttribute()`
- 条件付き依存: `if (browser.mayEnableCharacterEncodingMenu)` → `button?.removeAttribute()`
- 条件付き依存: `if (!(browser.mayEnableCharacterEncodingMenu))` → `this._menuItemForRepairTextEncoding.setAttribute()`
- 条件付き依存: `if (!(browser.mayEnableCharacterEncodingMenu))` → `button?.setAttribute()`
- 条件付き依存: `if (this.busyUI && aWebProgress.isTopLevel)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if ( !Object.getOwnPropertyDescriptor(window, "gTrustPanelHandler").get )` → `gTrustPanelHandler.onNavigationComplete()`
- 条件付き依存: `if (this.busyUI && aWebProgress.isTopLevel)` → `this.stopCommand.setAttribute()`
- 条件付き依存: `if (this.busyUI && aWebProgress.isTopLevel)` → `CombinedStopReload.switchToReload()`
- 参照: `Ci.nsIChannel`, `Ci.nsIWebProgressListener`, `Cr.NS_ERROR_NET_TIMEOUT`, `Object.getOwnPropertyDescriptor(window, "gTrustPanelHandler").get`, `aRequest.URI`, `aWebProgress.isTopLevel`, `browser.documentContentType`, `browser.mayEnableCharacterEncodingMenu`, `gBrowser.selectedBrowser`, `gBrowser.userTypedValue`, `location.scheme`, `location.spec`, `nsIWebProgressListener.STATE_IS_NETWORK`, `nsIWebProgressListener.STATE_RESTORING`, `nsIWebProgressListener.STATE_START`, `nsIWebProgressListener.STATE_STOP`, `this._elementsForViewSource`, `this.busyUI`, `this.isBusy`, `this.spinCursorWhileBusy`, `this.status`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLocationChange()
- 位置: L2280-2439
- 役割: 選択中のタブの URL が変わったときに UI を更新する。戻る・進むの有効化、再読み込みボタン、URL バーの表示、ブックマークツールバー、AI の没入表示、タブ固有・場所固有のポップアップを閉じる処理、文字コード項目、カスタマイズモードの入退場、クラッシュレポートへの URL 注記まで行う。サブフレームの移動は無視する。
- 触るとき: ページ移動時にアドレスバーやツールバーが古い状態のままになるとき、または URL 変化に伴う新しい UI 処理を足すとき。
- 呼び出し先: `BrowserUIUtils.checkEmptyPageOrigin()`, `BrowserUtils.callModulesFromCategory()`, `Object.getOwnPropertyDescriptor()`, `Services.obs.notifyObservers()`, `UpdateBackForwardCommands()`, `button?.setAttribute()`, `document.getElementById()`, `gBrowser.selectedTab.hasAttribute()`, `this._menuItemForRepairTextEncoding.setAttribute()`, `this._updateElementsForContentType()`, `this._updateMacUserActivity()`, `this.setOverLink()`
- 条件付き依存: `if ( !isSameDocument && !aIsSimulated && !Object.getOwnPropertyDescriptor(window, "gTrustPanelHandler").get )` → `gTrustPanelHandler.resetIconForNavigation()`
- 条件付き依存: `if ( (location == "about:blank" && BrowserUIUtils.checkEmptyPageOrigin(gBrowser.selectedBrowser)) || location == "" || (location == "about:newtab" && !this.newTa...)` → `this.reloadCommand.setAttribute()`
- 条件付き依存: `if (!( (location == "about:blank" && BrowserUIUtils.checkEmptyPageOrigin(gBrowser.selectedBrowser)) || location == "" || (location == "about:newtab" && !this.newTa...))` → `this.reloadCommand.removeAttribute()`
- 条件付き依存: `if (!window.browsingContext.isDocumentPiP)` → `gURLBar.setURI()`
- 条件付き依存: `if (!isSameDocument)` → `updateBookmarkToolbarVisibility()`
- 条件付き依存: `if (!isSameDocument)` → `AIWindow.updateImmersiveView()`
- 条件付き依存: `if (aIsSimulated)` → `closeOpenPanels()`
- 条件付き依存: `if (!isSameDocument)` → `closeOpenPanels()`
- 条件付き依存: `if ( location == "about:blank" && gBrowser.selectedTab.hasAttribute("customizemode") )` → `gCustomizeMode.enter()`
- 条件付き依存: `if (!( location == "about:blank" && gBrowser.selectedTab.hasAttribute("customizemode") ))` → `CustomizationHandler.isCustomizing()`
- 条件付き依存: `if ( CustomizationHandler.isEnteringCustomizeMode || CustomizationHandler.isCustomizing() )` → `gCustomizeMode.exit()`
- 条件付き依存: `if (!gMultiProcessBrowser)` → `gGestureSupport.restoreRotationState()`
- 条件付き依存: `if (aRequest)` → `setTimeout()`
- 条件付き依存: `if (aRequest)` → `XULBrowserWindow.asyncUpdateUI()`
- 条件付き依存: `if (!(aRequest))` → `this.asyncUpdateUI()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER && aLocationURI)` → `aLocationURI.mutate().setUserPass("").finalize()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER && aLocationURI)` → `aLocationURI.mutate().setUserPass()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER && aLocationURI)` → `aLocationURI.mutate()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER && aLocationURI)` → `Services.appinfo.annotateCrashReport()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SESSION_STORE`, `Cr.NS_ERROR_NOT_INITIALIZED`, `CustomizationHandler.isEnteringCustomizeMode`, `Object.getOwnPropertyDescriptor(window, "gTrustPanelHandler").get`, `aLocationURI.spec`, `aWebProgress.isTopLevel`, `ex.result`, `gBrowser.currentURI`, `gBrowser.selectedBrowser`, `gBrowser.webNavigation`, `this.newTabPageEnabled`, `uri.spec`, `window.browsingContext.isDocumentPiP`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.appinfo` / `Services.obs`

## closeOpenPanels()
- 位置: L2352-2358
- 役割: 渡されたセレクターに一致するパネルのうち、閉じていないものを hidePopup で閉じる。
- 触るとき: タブ切り替えや場所移動の際に閉じるべきパネルの種類(tabspecific や locationspecific)を変えるとき。
- 呼び出し先: `document.querySelectorAll()`
- 条件付き依存: `if (panel.state != "closed")` → `panel.hidePopup()`
- 参照: `panel.state`

## _updateElementsForContentType()
- 位置: L2441-2480
- 役割: 選択中ブラウザの MIME 種別に応じて、テキスト系の項目と検索系の項目の disabled を切り替え、PDF では検索を常に有効にする。翻訳項目は制限ページと翻訳エンジンの対応状況で表示と無効化を決める。
- 触るとき: テキスト以外のページ(画像や PDF など)で検索・ソース表示・翻訳メニューの有効無効がおかしいとき。
- 呼び出し先: `BrowserUtils.canFindInPage()`, `BrowserUtils.mimeTypeIsTextBased()`, `TranslationsParent.getIsTranslationsEngineSupported()`, `TranslationsParent.isFullPageTranslationsRestrictedForPage()`
- 条件付き依存: `if (isText)` → `element.removeAttribute()`
- 条件付き依存: `if (!(isText))` → `element.setAttribute()`
- 条件付き依存: `if (enableFind)` → `element.removeAttribute()`
- 条件付き依存: `if (!(enableFind))` → `element.setAttribute()`
- 条件付き依存: `if (TranslationsParent.isFullPageTranslationsRestrictedForPage(gBrowser))` → `this._menuItemForTranslations.setAttribute()`
- 条件付き依存: `if (!(TranslationsParent.isFullPageTranslationsRestrictedForPage(gBrowser)))` → `this._menuItemForTranslations.removeAttribute()`
- 参照: `TranslationsParent.AIFeature.isEnabled`, `browser.contentPrincipal?.spec`, `browser.documentContentType`, `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser`, `this._elementsForFind`, `this._elementsForTextBasedTypes`, `this._menuItemForTranslations.hidden`, `this._moreToolsTranslateMenuItem.hidden`

## _updateMacUserActivity()
- 位置: L2494-2511
- 役割: macOS でトップレベルの移動があったとき、MacUserActivityUpdater に URL とタイトルを渡して Handoff 用の NSUserActivity を更新する。プライベートウィンドウでは URL を空にして無効化する。
- 触るとき: Handoff で他の Apple 機器に渡すページ情報を変えるとき、またはプライベートウィンドウの URL が漏れていないか確認するとき。
- 呼び出し先: `MacUserActivityUpdater.updateLocation()`, `PrivateBrowsingUtils.isWindowPrivate()`, `win.docShell.treeOwner.QueryInterface()`
- 参照: `AppConstants.platform`, `Ci.nsIBaseWindow`, `uri.spec`, `webProgress.isTopLevel`, `win.gBrowser.contentTitle`
- XPCOM: `nsIBaseWindow`

## _securityURIOverride()
- 位置: L2525-2559
- 役割: currentURI がサンドボックスや about:blank の場合に、親となる principal の URI を返して ID パネルで表示する URL を差し替える。pdf.js の場合は元の URI が得られないので null を返す。
- 触るとき: about:blank や srcdoc のページで ID パネルに出る URL が空や誤りになるとき。
- 呼び出し先: `doGetProtocolFlags()`
- 参照: `Ci.nsIProtocolHandler`, `browser.contentPrincipal`, `browser.currentURI`, `principal.URI`, `principal.isNullPrincipal`, `principal.originNoSuffix`, `principal.precursorPrincipal`, `uri.filePath`, `uri.scheme`
- XPCOM: [`nsIProtocolHandler`](../../../netwerk/base/nsIIOService.idl.md)

## asyncUpdateUI()
- 位置: L2561-2563
- 役割: 非同期に OpenSearch のバッジ表示を更新する。
- 触るとき: 検索エンジン追加ボタンの表示条件を変えるとき。
- 呼び出し先: `OpenSearchManager.updateOpenSearchBadge()`

## onStatusChange()
- 位置: L2565-2568
- 役割: ステータスメッセージを保存し、ステータスパネルを更新する。
- 触るとき: ステータスパネルに出る文字列の流れを調べるとき。
- 呼び出し先: `StatusPanel.update()`
- 参照: `this.status`

## onContentBlockingEvent()
- 位置: L2582-2618
- 役割: 現在の URI と直前のイベントが同じなら何もせず、そうでなければ保護パネルと信頼パネルへイベントを渡し、今回のイベントを直前の値として保存する。aIsSimulated が boolean か undefined 以外なら例外を投げる。
- 触るとき: トラッキング防止などのコンテンツブロックイベントが保護アイコンに反映されないとき、またはイベントの処理先を増やすとき。
- 呼び出し先: `gProtectionsHandler.onContentBlockingEvent()`, `gTrustPanelHandler.onContentBlockingEvent()`
- 参照: `gBrowser.currentURI`, `this._event`, `this._lastLocationForEvent`, `uri.spec`

## onSecurityChange()
- 位置: L2625-2651
- 役割: URL バーの https 表示を更新し、必要ならセキュリティ上の URI の上書きを適用して ID 情報を作り直す。PiP ウィンドウでは URL バーの URI も設定する。
- 触るとき: 鍵アイコンや接続保護の表示が実際の状態と合わないとき、または混在コンテンツの表示を変えるとき。
- 呼び出し先: `Services.io.createExposableURI()`, `gIdentityHandler.updateIdentity()`, `gTrustPanelHandler.updateIdentity()`, `gURLBar.formatValue()`, `this._securityURIOverride()`
- 条件付き依存: `if (window.browsingContext.isDocumentPiP)` → `gURLBar.setURI()`
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_ASSOCIATED`, `gBrowser.currentURI`, `gBrowser.selectedBrowser`, `window.browsingContext.isDocumentPiP`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.io`

## XWB_onUpdateCurrentBrowser()
- 位置: L2654-2689
- 役割: タブ切り替え時に、ズームの背景タブ更新、ツールチップの非表示を行い、現在の読み込み状態を onStateChange に疑似的に渡し、読み込み中なら onStatusChange でメッセージを流す。
- 触るとき: タブを切り替えたときに停止ボタンやステータス表示が古いまま残るとき。
- 呼び出し先: `document.getElementById()`, `document.getElementById("aHTMLTooltip").hidePopup()`, `this.hideTooltip()`, `this.onStateChange()`, `this.onStatusChange()`
- 条件付き依存: `if (FullZoom.updateBackgroundTabs)` → `FullZoom.onLocationChange()`
- 参照: `Ci.nsIWebProgressListener`, `FullZoom.updateBackgroundTabs`, `gBrowser.currentURI`, `gBrowser.webProgress`, `nsIWebProgressListener.STATE_START`, `nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## DELAY_SHOW()
- 位置: L2706-2711
- 役割: リンク先表示を出すまでの遅延を browser.overlink-delay から一度だけ読み、以後は値をキャッシュする(遅延ゲッター)。
- 触るとき: リンク先の表示遅延を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`
- 参照: `this.DELAY_SHOW`
- XPCOM: `Services.prefs`

## _contextMenu()
- 位置: L2716-2721
- 役割: コンテキストメニュー要素(contentAreaContextMenu)を初回参照時に取り出し、以後キャッシュする(遅延ゲッター)。
- 触るとき: リンク表示とコンテキストメニューの連携を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._contextMenu`

## update()
- 位置: L2723-2753
- 役割: コンテキストメニューが開いている間は popuphidden を待つ。リンク上になければ即時または遅延で非表示にし、ステータスパネルが見えていれば更新、見えていなければマウス移動の止まりを待って表示する。
- 触るとき: リンクにカーソルを置いたときのステータス表示のタイミングを変えるとき。
- 呼び出し先: `clearTimeout()`, `window.removeEventListener()`
- 条件付き依存: `if ( this._contextMenu.state == "open" || this._contextMenu.state == "showing" )` → `this._contextMenu.addEventListener()`
- 条件付き依存: `if ( this._contextMenu.state == "open" || this._contextMenu.state == "showing" )` → `this.update()`
- 条件付き依存: `if (hideStatusPanelImmediately)` → `this._hide()`
- 条件付き依存: `if (!(hideStatusPanelImmediately))` → `setTimeout()`
- 条件付き依存: `if (!(hideStatusPanelImmediately))` → `this._hide.bind()`
- 条件付き依存: `if (StatusPanel.isVisible)` → `StatusPanel.update()`
- 条件付き依存: `if (!(StatusPanel.isVisible))` → `this._showDelayed()`
- 条件付き依存: `if (!(StatusPanel.isVisible))` → `window.addEventListener()`
- 参照: `StatusPanel.isVisible`, `XULBrowserWindow.overLink`, `this.DELAY_HIDE`, `this._contextMenu.state`, `this._timer`

## handleEvent()
- 位置: L2755-2763
- 役割: mousemove のたびに表示遅延をやり直す。
- 触るとき: マウスを動かしている間は表示を出さない挙動を変えるとき。
- 呼び出し先: `clearTimeout()`, `this._showDelayed()`
- 参照: `event.type`, `this._timer`

## _showDelayed()
- 位置: L2765-2774
- 役割: DELAY_SHOW ミリ秒後にステータスパネルを更新し、mousemove の監視を外す。
- 触るとき: リンク先表示の出る遅れを調べるとき。
- 呼び出し先: `StatusPanel.update()`, `setTimeout()`, `window.removeEventListener()`
- 参照: `this.DELAY_SHOW`, `this._timer`

## _hide()
- 位置: L2776-2780
- 役割: 保留中のタイマーを消し、ステータスパネルを更新して隠す。
- 触るとき: リンク先表示が残るときの後始末を調べるとき。
- 呼び出し先: `StatusPanel.update()`, `clearTimeout()`
- 参照: `this._timer`

## ensureInitialized()
- 位置: L2786-2824
- 役割: reload-button と stop-button が DOM にあるときだけ初期化し、停止中なら displaystop を付け、停止ボタンのクリックを監視し、無効化された状態を解消する。どちらか無いか破棄済みなら false を返す。
- 触るとき: 再読み込みと停止を1つのボタンにまとめる仕組みが、ボタンのパレット移動後に動かないとき。
- 呼び出し先: `XULBrowserWindow.stopCommand.hasAttribute()`, `button.hasAttribute()`, `document.getElementById()`, `stop.addEventListener()`
- 条件付き依存: `if (!XULBrowserWindow.stopCommand.hasAttribute("disabled"))` → `reload.setAttribute()`
- 条件付き依存: `if (button.hasAttribute("disabled"))` → `document.getElementById()`
- 条件付き依存: `if (button.hasAttribute("disabled"))` → `button.getAttribute()`
- 条件付き依存: `if (button.hasAttribute("disabled"))` → `command.hasAttribute()`
- 条件付き依存: `if (!command.hasAttribute("disabled"))` → `button.removeAttribute()`
- 参照: `this._destroyed`, `this._initialized`, `this.reload`, `this.stop`

## uninit()
- 位置: L2826-2837
- 役割: 破棄済みにし、初期化済みなら遷移タイマーを止めて停止ボタンのクリック監視と参照を外す。
- 触るとき: ウィンドウ終了時の後始末に項目を足すとき。
- 呼び出し先: `this._cancelTransition()`, `this.stop.removeEventListener()`
- 参照: `this._destroyed`, `this._initialized`, `this.reload`, `this.stop`

## handleEvent()
- 位置: L2839-2847
- 役割: 停止ボタンを左クリックしたときに、停止の要求済みフラグを立てる。
- 触るとき: 停止の押下後に再読み込みへ戻すタイミングを変えるとき。
- 参照: `event.button`, `event.type`, `this._stopClicked`, `this.stop.disabled`

## switchToStop()
- 位置: L2849-2858
- 役割: 初期化できて切り替えが妥当なら、再読み込みボタンに displaystop を付けて停止表示にする。
- 触るとき: 読み込み開始時に停止ボタンへ切り替わらないとき。
- 呼び出し先: `this._shouldSwitch()`, `this.ensureInitialized()`, `this.reload.setAttribute()`

## switchToReload()
- 位置: L2860-2890
- 役割: displaystop があれば外して再読み込みに戻す。停止を押した直後なら再読み込みの有効状態を戻す。そうでなければ 650ms の間だけ再読み込みを無効にして、停止の押し間違いを防ぐ。
- 触るとき: 読み込み後に再読み込みボタンが一時的に押せない挙動を変えるとき、または停止直後に再読み込みが有効にならないとき。
- 呼び出し先: `XULBrowserWindow.reloadCommand.hasAttribute()`, `setTimeout()`, `this.ensureInitialized()`, `this.reload.hasAttribute()`, `this.reload.removeAttribute()`
- 条件付き依存: `if (this._stopClicked)` → `XULBrowserWindow.reloadCommand.hasAttribute()`
- 参照: `self._timer`, `self.reload.disabled`, `this._stopClicked`, `this._timer`, `this.reload.disabled`

## _shouldSwitch()
- 位置: L2892-2905
- 役割: chrome: の要求や、トップレベルの about: の要求(about:reader を除く)では切り替えないよう false を返す。それ以外は true を返す。
- 触るとき: 内部ページの読み込みで停止と再読み込みの表示が切り替わらないようにしたいとき。
- 呼び出し先: `aRequest.originalURI.schemeIs()`, `aRequest.originalURI.spec.startsWith()`
- 参照: `aRequest.originalURI`, `aWebProgress.isTopLevel`

## _cancelTransition()
- 位置: L2907-2912
- 役割: 保留中の 650ms タイマーがあれば取り消す。
- 触るとき: 再読み込みボタンの一時無効化を途中で解除する必要があるとき。
- 条件付き依存: `if (this._timer)` → `clearTimeout()`
- 参照: `this._timer`

## onStateChange()
- 位置: L2916-2971
- 役割: トップレベルのページ読み込みの計測を行う。読み込み種別で pageLoad・pageReloadNormal・pageReloadSkipCache を選び、開始時に計測を始め、停止時に記録し、サイト単位の計測を送る。中断時は計測を取り消す。about: の要求は計測しない。
- 触るとき: ページ読み込みの性能計測の対象や区分を変えるとき。
- 条件付き依存: `if (aBrowser[timerIdField])` → `Glean.browserTimings[metricName].cancel()`
- 条件付き依存: `if (metricName)` → `Glean.browserTimings[metricName].start()`
- 条件付き依存: `if (aStateFlags & Ci.nsIWebProgressListener.STATE_START)` → `Glean.browserEngagement.totalTopVisits.true.add()`
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_STOP && /* we won't see STATE_START events for pre-rendered tabs */ metricName && aBrowser[timerIdField] )` → `Glean.browserTimings[metricName].stopAndAccumulate()`
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_STOP && /* we won't see STATE_START events for pre-rendered tabs */ metricName && aBrowser[timerIdField] )` → `BrowserTelemetryUtils.recordSiteOriginTelemetry()`
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_STOP && /* we won't see STATE_START events for pre-rendered tabs */ metricName && aBrowser[timerIdField] )` → `browserWindows()`
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_STOP && /* we won't see STATE_START events for pre-rendered tabs */ aStatus == Cr.NS_BINDING_ABORTED && metric...)` → `Glean.browserTimings[metricName].cancel()`
- 参照: `Ci.nsIDocShell.LOAD_CMD_RELOAD`, `Ci.nsIWebProgressListener.STATE_IS_WINDOW`, `Ci.nsIWebProgressListener.STATE_START`, `Ci.nsIWebProgressListener.STATE_STOP`, `Cr.NS_BINDING_ABORTED`, `Glean.browserTimings`, `aRequest.originalURI`, `aRequest.originalURI.scheme`, `aWebProgress.isTopLevel`, `aWebProgress.loadType`
- XPCOM: [`nsIDocShell`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLocationChange()
- 位置: L2973-3013
- 役割: トップレベルの移動で、同一ドキュメントの移動なら Reader モードに pushState を通知して終わる。それ以外は通知の一時表示を消し、mailto の通知、ズーム、キャプティブポータルの確認を行う。
- 触るとき: ページ移動時のリーダーモードやズームの追従がずれるとき、または移動時に行う処理を追加するとき。
- 呼び出し先: `CaptivePortalWatcher.onLocationChange()`, `FullZoom.onLocationChange()`, `Object.getOwnPropertyDescriptor()`, `Services.obs.notifyObservers()`, `gBrowser.readNotificationBox()`, `gBrowser.readNotificationBox(aBrowser)?.removeTransientNotifications()`
- 条件付き依存: `if (aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT)` → `aBrowser.sendMessageToActor()`
- 条件付き依存: `if (!Object.getOwnPropertyDescriptor(window, "PopupNotifications").get)` → `PopupNotifications.locationChange()`
- 条件付き依存: `if (aBrowser._sharingState)` → `gBrowser.resetBrowserSharing()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `Object.getOwnPropertyDescriptor(window, "PopupNotifications").get`, `aBrowser._sharingState`, `aBrowser.isArticle`, `aWebProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.obs`

## onLinkIconAvailable()
- 位置: L3015-3024
- 役割: アイコン URI があり、選択中のブラウザのとき OpenSearch のバッジを更新する。
- 触るとき: リンクのアイコンが検索エンジン追加ボタンに反映されないとき。
- 条件付き依存: `if (browser == gBrowser.selectedBrowser)` → `OpenSearchManager.updateOpenSearchBadge()`
- 参照: `gBrowser.selectedBrowser`

## showFullScreenViewContextMenuItems()
- 位置: L3027-3035
- 役割: fullscreen 用の項目をフルスクリーン中だけ表示し、自動的に隠す項目があれば FullScreen の表示を更新する。
- 触るとき: フルスクリーン時にだけ出すメニュー項目を追加するとき。
- 呼び出し先: `popup.querySelector()`, `popup.querySelectorAll()`
- 条件付き依存: `if (autoHide)` → `FullScreen.updateAutohideMenuitem()`
- 参照: `node.hidden`, `window.fullScreen`

## onViewToolbarCommand()
- 位置: L3037-3057
- 役割: ツールバー表示メニューの項目から呼ばれ、ブックマークツールバーなら bookmarks.visibility の pref を設定し、それ以外は toolbarId と checked 属性から表示を決めて CustomizableUI で切り替え、表示の変更を telemetry に記録する。
- 触るとき: 表示メニュー(ツールバー、ブックマークツールバーの表示切替)の項目を追加したり、その切替の記録を変えたりするとき。
- 呼び出し先: `BrowserUsageTelemetry.recordToolbarVisibility()`, `CustomizableUI.setToolbarVisibility()`
- 条件付き依存: `if (node.dataset.bookmarksToolbarVisibility)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (!(node.dataset.bookmarksToolbarVisibility))` → `node.getAttribute()`
- 条件付き依存: `if (!(node.dataset.bookmarksToolbarVisibility))` → `node.hasAttribute()`
- 参照: `aEvent.originalTarget`, `node.dataset.bookmarksToolbarVisibility`, `node.dataset.visibilityEnum`, `node.parentNode.id`, `node.parentNode.parentNode.parentNode.id`
- XPCOM: `Services.prefs`

## setToolbarVisibility()
- 位置: L3059-3149
- 役割: ツールバーの表示・非表示を切り替える。メニューバーは autohide、それ以外は collapsed 属性を使い、ブックマークツールバーでは true・false・always・never・newtab を実際の表示に直して pref にも保存する。変化がなければ何もせず、変化時は xulstore に保存して toolbarvisibilitychange を発火する。
- 触るとき: ツールバーの表示状態が保存されない、または変化しても通知や再描画が起きないとき、またはブックマークツールバーの newtab 表示の条件を変えるとき。
- 呼び出し先: `toolbar.classList.toggle()`, `toolbar.dispatchEvent()`, `toolbar.getAttribute()`, `toolbar.hasAttribute()`, `toolbar.toggleAttribute()`
- 条件付き依存: `if (AppConstants.platform == "linux")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (persist)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (uriToLoad)` → `Array.isArray()`
- 条件付き依存: `if (uriToLoad)` → `URL.parse()`
- 条件付き依存: `if (toolbar == BookmarkingUI.toolbar)` → `BookmarkingUI.isOnNewTabPage()`
- 条件付き依存: `if (persist && toolbar.id != "PersonalToolbar")` → `Services.xulStore.persist()`
- 参照: `AppConstants.platform`, `BookmarkingUI.toolbar`, `URL.parse(uriToLoad)?.URI`, `gBrowser.currentURI`, `gBrowser?.currentURI`, `gBrowserInit.domContentLoaded`, `gBrowserInit.uriToLoadPromise`, `toolbar.id`
- XPCOM: `Services.prefs` / `Services.xulStore`

## updateToggleControlLabel()
- 位置: L3151-3161
- 役割: label-checked を持つ切替コントロールの label を、checked 属性の有無で label-checked または label-unchecked に差し替える。初回は元の label を label-unchecked として保存する。
- 触るとき: チェックボックス風のメニュー項目の表示文言が切替に追従しないとき。
- 呼び出し先: `control.getAttribute()`, `control.hasAttribute()`, `control.setAttribute()`
- 条件付き依存: `if (!control.hasAttribute("label-unchecked"))` → `control.setAttribute()`
- 条件付き依存: `if (!control.hasAttribute("label-unchecked"))` → `control.getAttribute()`

## init()
- 位置: L3166-3171
- 役割: Windows の場合だけ、タブレットモードの現在値を反映し、変化の通知を監視する。
- 触るとき: Windows のタブレットモードに応じた見た目の制御を変えるとき。
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.update()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.obs.addObserver()`
- 参照: `AppConstants.platform`, `WindowsUIUtils.inWin10TabletMode`
- XPCOM: `Services.obs`

## uninit()
- 位置: L3173-3177
- 役割: Windows の場合だけ、タブレットモード変化の監視を外す。
- 触るとき: ウィンドウ終了時の監視解除漏れを調べるとき。
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.obs.removeObserver()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.obs`

## observe()
- 位置: L3179-3181
- 役割: tablet-mode-change を受け取り、データが win10-tablet-mode かどうかで update を呼ぶ。
- 触るとき: タブレットモードの通知の解釈を変えるとき。
- 呼び出し先: `this.update()`

## update()
- 位置: L3183-3189
- 役割: タブレットモードなら win10-tablet-mode 属性を付け、そうでなければ外す。
- 触るとき: Windows 10 のタブレットモードの見た目が切り替わらないとき。
- 条件付き依存: `if (isInTabletMode)` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (!(isInTabletMode))` → `document.documentElement.removeAttribute()`

## displaySecurityInfo()
- 位置: L3192-3194
- 役割: ページ情報ダイアログをセキュリティタブを指定して開く。
- 触るとき: 鍵アイコンなどからページのセキュリティ情報を開く導線を変えるとき。
- 呼び出し先: `BrowserCommands.pageInfo()`

## init()
- 位置: L3235-3263
- 役割: 初期の密度を反映し、テレメトリを初期化して、ウィンドウ・サイドバー・テレメトリの各監視と、uidensity 系と RFP 系の pref 監視を登録する。サイドバー launcher の属性変化も MutationObserver で監視する。
- 触るとき: UI 密度(標準、コンパクト、タッチ)の自動切替の契機を追加または変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `UIDensityTelemetry.init()`, `document.getElementById()`, `this.update()`, `window.addEventListener()`
- 条件付き依存: `if (sidebarContainer)` → `this.update()`
- 条件付き依存: `if (sidebarContainer)` → `this._sidebarStateObserver.observe()`
- 参照: `this._sidebarShownHandler`, `this._sidebarStateObserver`, `this.autoCompactThresholdPref`, `this.autoTouchModePref`, `this.rfpWindowSizingPrefs`, `this.uiDensityPref`
- XPCOM: `Services.obs` / `Services.prefs`

## this._sidebarShownHandler()
- 位置: L3247-3247
- 役割: SidebarShown のたびに密度の再評価を行う。
- 触るとき: サイドバーを開いたときに密度が変わらない、または頻繁に再計算されているとき。
- 呼び出し先: `this.update()`

## uninit()
- 位置: L3265-3282
- 役割: init で登録した pref・オブザーバー・リスナーと MutationObserver をすべて外す。
- 触るとき: UI 密度の監視を追加・削除したときに解除漏れがないか確認するとき。
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `window.removeEventListener()`
- 条件付き依存: `if (this._sidebarShownHandler)` → `window.removeEventListener()`
- 条件付き依存: `if (this._sidebarStateObserver)` → `this._sidebarStateObserver.disconnect()`
- 参照: `this._sidebarShownHandler`, `this._sidebarStateObserver`, `this.autoCompactThresholdPref`, `this.autoTouchModePref`, `this.rfpWindowSizingPrefs`, `this.uiDensityPref`
- XPCOM: `Services.obs` / `Services.prefs`

## handleEvent()
- 位置: L3284-3300
- 役割: resize のうち、nova が有効で uidensity が明示指定されていない場合だけ update を呼ぶ。それ以外はリサイズごとの再計算を省く(性能上の理由)。
- 触るとき: ウィンドウのリサイズ時に密度が追従しない、またはリサイズ中に重くなるとき。
- 条件付き依存: `if (event.type == "resize")` → `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (event.type == "resize")` → `this.update()`
- 参照: `event.type`, `this.novaEnabled`, `this.uiDensityPref`
- XPCOM: `Services.prefs`

## observe()
- 位置: L3302-3317
- 役割: tablet-mode-change と既知の pref 変更のときだけ update を呼ぶ。
- 触るとき: 密度に影響する新しい pref を監視対象に足すとき。
- 呼び出し先: `this.knownPrefs.has()`, `this.update()`

## _shouldAutoCompact()
- 位置: L3319-3362
- 役割: ツールバーが無いポップアップでは false を返し、RFP のウィンドウサイズ保護が有効なら false を返す。閾値が正のとき、タブストリップの高さ(36px)か、サイドバーの折りたたみ launcher の幅(56px)の比率が閾値を超えたら true を返す。
- 触るとき: 小さいウィンドウでコンパクト表示へ自動で切り替わる条件を変えるとき、またはウィンドウが小さいのにコンパクトにならないとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`, `parseFloat()`, `this._densityReferenceSize()`, `this._isSidebarLauncherCollapsed()`, `this.rfpWindowSizingPrefs.some()`
- 参照: `this.AUTO_COMPACT_REFERENCE_SIDEBAR_LAUNCHER_WIDTH`, `this.AUTO_COMPACT_REFERENCE_TABSTRIP_HEIGHT`, `this.autoCompactThresholdPref`, `window.toolbar.visible`
- XPCOM: `Services.prefs`

## _densityReferenceSize()
- 位置: L3370-3378
- 役割: 自動コンパクト判定に使うウィンドウサイズを返す。最大化時は画面サイズと内側サイズの大きい方を使い、そうでなければ内側サイズを使う。
- 触るとき: 起動直後の最大化ウィンドウで自動コンパクトの判定がぶれるとき。
- 呼び出し先: `document.documentElement.getAttribute()`
- 条件付き依存: `if (document.documentElement.getAttribute("sizemode") == "maximized")` → `Math.max()`
- 参照: `window.innerHeight`, `window.innerWidth`, `window.screen.availHeight`, `window.screen.availWidth`

## _isSidebarLauncherCollapsed()
- 位置: L3382-3402
- 役割: sidebar.revamp が有効で launcher が表示中かつ折りたたみ中のとき true を返す。展開がホバーで行われる設定では、ホバーで展開されても折りたたみ扱いのままにする。
- 触るとき: サイドバーの launcher 表示状態によって自動コンパクトの判定が変わる問題を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `SidebarController._state`, `SidebarController.initialized`, `SidebarController.sidebarRevampVisibility`, `state.launcherExpanded`, `state?.launcherVisible`
- XPCOM: `Services.prefs`

## _inTabletMode()
- 位置: L3406-3411
- 役割: Windows の Win10 または Win11 のタブレットモードかを返す。それ以外の OS は false。
- 触るとき: タブレットモードを密度の判定に使う条件を変えるとき。
- 参照: `AppConstants.platform`, `WindowsUIUtils.inWin10TabletMode`, `WindowsUIUtils.inWin11TabletMode`

## getCurrentDensity()
- 位置: L3413-3445
- 役割: 実際に適用する密度を決める。Windows のタブレットモードで自動、または touchmode.auto と通常密度の組み合わせならタッチを返し、nova で明示指定が無ければ自動コンパクトを、それ以外は uidensity の pref 値を返す。
- 触るとき: 密度の優先順位(タブレット、自動コンパクト、ユーザー設定)を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`, `this._inTabletMode()`, `this._shouldAutoCompact()`
- 条件付き依存: `if (this._inTabletMode())` → `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (this._inTabletMode())` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (this._inTabletMode())` → `Services.prefs.getBoolPref()`
- 参照: `this.MODE_COMPACT`, `this.MODE_NORMAL`, `this.MODE_TOUCH`, `this.autoTouchModePref`, `this.novaEnabled`, `this.uiDensityPref`
- XPCOM: `Services.prefs`

## update()
- 位置: L3447-3508
- 役割: 密度の属性を文書とサイドバーの文書へ設定し、前回と異なるときだけ選択中のツリーを再描画させて uidensitychanged を発火し、初回以外はテレメトリに記録する。
- 触るとき: 密度変更後にタブやツリーの見た目が古いままになるとき、または密度変化の通知やテレメトリを増やすとき。
- 呼び出し先: `doc.removeAttribute()`, `doc.setAttribute()`, `window.dispatchEvent()`
- 条件付き依存: `if (mode == null)` → `this.getCurrentDensity()`
- 条件付き依存: `if (sidebarContentDoc?.documentElement)` → `docs.push()`
- 条件付き依存: `if (sidebarContentDoc)` → `sidebarContentDoc.querySelector()`
- 条件付き依存: `if (!isInitialUpdate)` → `UIDensityTelemetry.onDensityChanged()`
- 参照: `SidebarController.browser.contentDocument`, `SidebarController.initialized`, `SidebarController.isOpen`, `document.documentElement`, `sidebarContentDoc.documentElement`, `sidebarContentDoc?.documentElement`, `this.MODE_COMPACT`, `this.MODE_TOUCH`, `this._appliedMode`, `this.getCurrentDensity().mode`, `tree.style.border`

## getText()
- 位置: L3561-3584
- 役割: ツールチップ用の文字列を、ノード ID に対応する文言と、対応するショートカットの表示で作る。ショートカットが空の結果は保存せず、それ以外は cache に保存して返す。
- 触るとき: ツールバーボタンのツールチップに出るショートカット表記を変えるとき。
- 呼び出し先: `this.cache.get()`, `this.cache.has()`
- 条件付き依存: `if (nodeId in this.nodeToShortcutMap)` → `document.getElementById()`
- 条件付き依存: `if (shortcut)` → `ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (shortcut)` → `args.push()`
- 条件付き依存: `if (!this.cache.has(nodeId) && nodeId in this.nodeToTooltipMap)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (shouldCache)` → `this.cache.set()`
- 参照: `this.nodeToShortcutMap`, `this.nodeToTooltipMap`

## updateText()
- 位置: L3586-3589
- 役割: ツールチップの triggerNode の ID から文字列を取り、label として設定する。
- 触るとき: ツールチップの表示内容を別のボタンに広げるとき。
- 呼び出し先: `aTooltip.setAttribute()`, `this.getText()`
- 参照: `aTooltip.triggerNode.id`

## contentAreaClick()
- 位置: L3610-3683
- 役割: コンテンツ領域の左クリックを処理する。信頼されていない、既に処理済み、左以外のクリックは無視する。リンクでなければ、中クリックの貼り付け(設定が有効なとき)を行う。拡張パネルからの通常リンクは現在のタブで開き、そうでなければ handleLinkClick に任せ、最後に Places で訪問を利用者操作として記録する。
- 触るとき: ページ内リンクのクリックや中クリックの動作を変えるとき、または拡張パネルのリンクが新しいタブで開いてしまうとき。
- 呼び出し先: `BrowserUtils.hrefAndLinkNodeForClickEvent()`, `PrivateBrowsingUtils.isWindowPrivate()`, `handleLinkClick()`
- 条件付き依存: `if (!href)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( event.button == 1 && Services.prefs.getBoolPref("middlemouse.contentLoadURL") && !Services.prefs.getBoolPref("general.autoScroll") )` → `middleMousePaste()`
- 条件付き依存: `if ( event.button == 1 && Services.prefs.getBoolPref("middlemouse.contentLoadURL") && !Services.prefs.getBoolPref("general.autoScroll") )` → `event.preventDefault()`
- 条件付き依存: `if (isPanelClick && mainTarget)` → `linkNode.getAttribute()`
- 条件付き依存: `if (isPanelClick && mainTarget)` → `href.startsWith()`
- 条件付き依存: `if (isPanelClick && mainTarget)` → `urlSecurityCheck()`
- 条件付き依存: `if (isPanelClick && mainTarget)` → `event.preventDefault()`
- 条件付き依存: `if (isPanelClick && mainTarget)` → `openLinkIn()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(window))` → `PlacesUIUtils.markPageAsFollowedLink()`
- 参照: `event.altKey`, `event.button`, `event.ctrlKey`, `event.defaultPrevented`, `event.isTrusted`, `event.metaKey`, `event.shiftKey`, `linkNode.ownerDocument.nodePrincipal`, `linkNode.target`
- XPCOM: `Services.prefs`

## handleLinkClick()
- 位置: L3690-3748
- 役割: リンクの開き先を BrowserUtils で決め、現在のタブならそのまま既定動作に任せる。保存の場合は saveURL を呼び、それ以外は参照元情報、文字コード、プリンシパル、フレーム ID を付けて openLinkIn で開く。コンテナのユーザーコンテキスト ID も引き継ぐ。右クリックは扱わない。
- 触るとき: リンクを新しいタブ・ウィンドウ・保存で開く経路を変えるとき、またはコンテナ内のリンクが別コンテナで開くとき。
- 呼び出し先: `BrowserUtils.whereToOpenLink()`, `Cc["@mozilla.org/referrer-info;1"].createInstance()`, `WebNavigationFrames.getFrameId()`, `event.preventDefault()`, `openLinkIn()`, `urlSecurityCheck()`
- 条件付き依存: `if (linkNode)` → `referrerInfo.initWithElement()`
- 条件付き依存: `if (!(linkNode))` → `referrerInfo.initWithDocument()`
- 条件付き依存: `if (where == "save")` → `saveURL()`
- 条件付き依存: `if (where == "save")` → `gatherTextUnder()`
- 条件付き依存: `if (where == "save")` → `event.preventDefault()`
- 参照: `Ci.nsIReferrerInfo`, `doc.characterSet`, `doc.cookieJarSettings`, `doc.defaultView`, `doc.effectiveStoragePrincipal`, `doc.nodePrincipal`, `doc.nodePrincipal.originAttributes.userContextId`, `doc.policyContainer`, `event.button`, `event.target.ownerDocument`, `params.userContextId`
- XPCOM: [`nsIReferrerInfo`](../../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/referrer-info;1`

## middleMousePaste()
- 位置: L3755-3807
- 役割: クリップボードの文字列から改行と前後の空白を取り除き、安全でないプロトコルを除く。URL として有効なら履歴へ追加し、移動先が変わっていない場合だけ開く。イベントの伝播は止める。
- 触るとき: 中クリックで貼り付けて開く URL の扱いを変えるとき、または貼り付けたのに開かないとき。
- 呼び出し先: `BrowserUtils.whereToOpenLink()`, `Event.isInstance()`, `UrlbarShared.stripUnsafeProtocolOnPaste()`, `UrlbarUtils.addToUrlbarHistory()`, `UrlbarUtils.getShortcutOrURIAndPostData()`, `UrlbarUtils.getShortcutOrURIAndPostData(clipboard).then()`, `clipboard.replace()`, `console.error()`, `makeURI()`, `readFromClipboard()`
- 条件付き依存: `if ( where != "current" || lastLocationChange == gBrowser.selectedBrowser.lastLocationChange )` → `openUILink()`
- 条件付き依存: `if (Event.isInstance(event))` → `event.stopPropagation()`
- 参照: `data.mayInheritPrincipal`, `data.url`, `gBrowser.selectedBrowser.contentPrincipal`, `gBrowser.selectedBrowser.lastLocationChange`, `gBrowser.selectedBrowser.policyContainer`

## init()
- 位置: L3815-3825
- 役割: オフライン切替コマンドを取り出し、network:offline-status-changed を監視し、現在のオフライン状態で UI を更新する。
- 触るとき: オフライン表示の初期化を変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `this._updateOfflineUI()`
- 条件付き依存: `if (!this._uiElement)` → `document.getElementById()`
- 参照: `Services.io.offline`, `this._inited`, `this._uiElement`
- XPCOM: `Services.io` / `Services.obs`

## uninit()
- 位置: L3827-3831
- 役割: 初期化済みなら network:offline-status-changed の監視を外す。
- 触るとき: オフライン監視の解除を調べるとき。
- 条件付き依存: `if (this._inited)` → `Services.obs.removeObserver()`
- 参照: `this._inited`
- XPCOM: `Services.obs`

## toggleOfflineStatus()
- 位置: L3833-3842
- 役割: オフライン切替を行う。オフラインへ変える際は、他の処理に止められなければ(canGoOffline)のみ io.offline を反転し、止められたら UI を戻す。
- 触るとき: オフライン切替ボタンの動作や、オフラインに入る前の確認を変えるとき。
- 呼び出し先: `this._canGoOffline()`
- 条件付き依存: `if (!ioService.offline && !this._canGoOffline())` → `this._updateOfflineUI()`
- 参照: `Services.io`, `ioService.offline`
- XPCOM: `Services.io`

## observe()
- 位置: L3845-3853
- 役割: network:offline-status-changed を受けたら、現在の io.offline の値で UI を更新する。通信の切断による通知も含めて現在値を反映する。
- 触るとき: オフライン表示が実際の状態と合わないとき。
- 呼び出し先: `this._updateOfflineUI()`
- 参照: `Services.io.offline`
- XPCOM: `Services.io`

## _canGoOffline()
- 位置: L3856-3870
- 役割: offline-requested を通知し、誰かが取り消せば false を返す。通知の処理で例外が出ても握りつぶして true を返す。
- 触るとき: オフラインに入る前に止めたい処理を追加するとき。
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`
- 参照: `Ci.nsISupportsPRBool`, `cancelGoOffline.data`
- XPCOM: [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.obs`

## _updateOfflineUI()
- 位置: L3873-3877
- 役割: network.online が管理者などにロックされていれば切替を無効化し、オフライン状態に応じて checked 属性を設定する。
- 触るとき: オフライン切替メニューの有効無効や check の表示を変えるとき。
- 呼び出し先: `Services.prefs.prefIsLocked()`, `this._uiElement.toggleAttribute()`
- XPCOM: `Services.prefs`

## CanCloseWindow()
- 位置: L3880-3899
- 役割: 終了中か skipNextCanClose が立っていれば true を返す。それ以外は、読み込み済みの各タブについて permitUnload を確認し、一つでも拒否されたら false を返す。
- 触るとき: ウィンドウを閉じる前の beforeunload 確認の対象や回数を変えるとき、または閉じられないタブの原因を調べるとき。
- 呼び出し先: `browser.permitUnload()`
- 参照: `Services.startup.shuttingDown`, `browser.isConnected`, `gBrowser.browsers`, `window.skipNextCanClose`
- XPCOM: `Services.startup`

## WindowIsClosing()
- 位置: L3906-4022
- 役割: ウィンドウを閉じる要求を処理する。閉じ方(メニュー、閉じるボタン、ショートカット、OS)を判別し、警告で中断されれば false を返す。閉じる前に Spotlight を閉じ、permitUnload を確認し、最後のウィンドウで lastWindowClose のメッセージがあれば表示して閉じるのを一旦止め、解決後に window.close() を再度呼ぶ。
- 触るとき: ウィンドウ閉じ時の警告、メッセージ表示、閉じ方の計測を変えるとき、または閉じられない・閉じた後に余計なメッセージが出るとき。
- 呼び出し先: `Array.from()`, `Array.from(browserWindows()).some()`, `CanCloseWindow()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`, `Spotlight.close()`, `browserWindows()`, `closeWindow()`
- 条件付き依存: `if (event)` → `target?.id?.startsWith()`
- 条件付き依存: `if (gLastWindowCloseTriggerHandled)` → `Glean.messagingSystem.lastWindowCloseTriggerBypassed.add()`
- 条件付き依存: `if (!(gLastWindowCloseTriggerHandled))` → `TaskbarTabsUtils.isTaskbarTabWindow()`
- 条件付き依存: `if (!(gLastWindowCloseTriggerHandled))` → `document.documentElement.hasAttribute()`
- 条件付き依存: `if (!(gLastWindowCloseTriggerHandled))` → `ASRouter.hasMessageForTrigger()`
- 条件付き依存: `if ( isLastWindow && // Web app (Taskbar Tabs) and mini windows aren't a normal browsing window // this trigger targets, even though they keep the toolbar visibl...)` → `ASRouter.sendTriggerMessage()`
- 条件付き依存: `if ( isLastWindow && // Web app (Taskbar Tabs) and mini windows aren't a normal browsing window // this trigger targets, even though they keep the toolbar visibl...)` → `console.error()`
- 条件付き依存: `if ( isLastWindow && // Web app (Taskbar Tabs) and mini windows aren't a normal browsing window // this trigger targets, even though they keep the toolbar visibl...)` → `window.close()`
- 参照: `ASRouter.initialized`, `AppConstants.platform`, `event.sourceEvent?.target`, `gBrowser.openTabs.length`, `gBrowser.pinnedTabCount`, `gBrowser.selectedBrowser`, `gBrowser.visibleTabs.length`, `target?.nodeName`, `w.closed`, `window.skipNextCanClose`
- XPCOM: `Services.prefs`

## warnAboutClosingWindow()
- 位置: L4030-4107
- 役割: 最後のブラウザウィンドウなら終了扱いの通知(browser-lastwindow-close-requested)を出し、そうでなければタブ数の警告を出す。プライベートウィンドウは通常と別に扱い、最後のプライベートウィンドウでは終了前の通知を出す。キャンセルされれば false を返す。
- 触るとき: ウィンドウを閉じるときのタブ数警告や、最後のウィンドウの扱い(Windows と macOS の違い)を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `PrivateBrowsingUtils.isWindowPrivate()`, `browserWindows()`, `gBrowser.warnAboutClosingTabs()`, `os.notifyObservers()`
- 条件付き依存: `if (!isPBWindow && !toolbar.visible)` → `gBrowser.warnAboutClosingTabs()`
- 条件付き依存: `if (!win.closed && win != window)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (isPBWindow && !otherPBWindowExists)` → `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`
- 条件付き依存: `if (isPBWindow && !otherPBWindowExists)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (otherWindowExists)` → `gBrowser.warnAboutClosingTabs()`
- 参照: `AppConstants.platform`, `Ci.nsISupportsPRBool`, `PrivateBrowsingUtils.permanentPrivateBrowsing`, `Services.obs`, `Tabbrowser.closingTabsEnum.ALL`, `closingCanceled.data`, `exitingCanceled.data`, `gBrowser.openTabs.length`, `toolbar.visible`, `win.closed`
- XPCOM: [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.obs`

## sendLinkForBrowser()
- 位置: L4110-4115
- 役割: 現在のページの読みやすい URL とタイトルを取り、メール送信へ渡す。
- 触るとき: ページのリンクをメールで送る際の本文や件名を変えるとき。
- 呼び出し先: `gURLBar.makeURIReadable()`, `this.sendMessage()`
- 参照: `aBrowser.contentTitle`, `aBrowser.currentURI`, `gURLBar.makeURIReadable(aBrowser.currentURI).displaySpec`

## sendMessage()
- 位置: L4117-4129
- 役割: 本文と件名を含む mailto の URL を作り、外部のプロトコルハンドラーで開く。本文が空なら mailto: だけを開く。
- 触るとき: メールの作成の仕方(件名や本文のエンコード)を変えるとき。
- 呼び出し先: `makeURI()`, `this._launchExternalUrl()`
- 条件付き依存: `if (aBody)` → `encodeURIComponent()`

## _launchExternalUrl()
- 位置: L4134-4144
- 役割: 外部プロトコルサービスを使い、渡された URI をシステム権限で開く。
- 触るとき: mailto などを外部アプリで開く経路を変えるとき。
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/external-protocol-service;1" ].getService()`
- 条件付き依存: `if (extProtocolSvc)` → `extProtocolSvc.loadURI()`
- 条件付き依存: `if (extProtocolSvc)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `Ci.nsIExternalProtocolService`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1` / `Services.scriptSecurityManager`

## observe()
- 位置: L4157-4159
- 役割: remote-listening の通知を受け、リモート制御のアイコンを更新する。
- 触るとき: リモート制御の表示が出るタイミングを変えるとき。
- 呼び出し先: `gRemoteControl.updateVisualCue()`

## updateVisualCue()
- 位置: L4161-4185
- 役割: リモート制御が有効なら remotecontrol 属性を付けてアンカーのアイコンに原因(DevTools か Marionette か RemoteAgent)を表示し、無ければ属性を外す。自動テストで設定されていれば何もしない。
- 触るとき: リモート制御中の表示を変えるとき、またはテストで表示が邪魔になるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.getRemoteControlComponent()`
- 条件付き依存: `if (remoteControlComponent)` → `mainWindow.setAttribute()`
- 条件付き依存: `if (remoteControlComponent)` → `document.getElementById()`
- 条件付き依存: `if (remoteControlComponent)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(remoteControlComponent))` → `mainWindow.removeAttribute()`
- 参照: `Cu.isInAutomation`, `document.documentElement`
- XPCOM: `Services.prefs`

## getRemoteControlComponent()
- 位置: L4187-4207
- 役割: DevTools の接続(ブラウザツールボックス以外)、Marionette、RemoteAgent の順に調べ、該当する名前を返す。どれも無ければ null を返す。
- 触るとき: リモート制御の種類に新しい接続を足すとき。
- 呼び出し先: `DevToolsSocketStatus.hasSocketOpened()`
- 参照: `Marionette.running`, `RemoteAgent.running`

## switchToTabHavingURI()
- 位置: L4214-4229
- 役割: 引数をそのまま URILoadingHelper.switchToTabHavingURI へ渡す。
- 触るとき: URL を持つタブへの切替の入口を探すとき。
- 呼び出し先: `URILoadingHelper.switchToTabHavingURI()`

## safeModeRestart()
- 位置: L4232-4254
- 役割: セーフモードの再起動を行う。すでにセーフモードなら quit-application-requested を通知し、拒否されなければ再起動する。そうでなければ restart-in-safe-mode を通知する。
- 触るとき: セーフモードで再起動する導線の挙動を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `Ci.nsISupportsPRBool`, `Services.appinfo.inSafeMode`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.appinfo` / `Services.obs` / `Services.startup`

## duplicateTabIn()
- 位置: L4266-4304
- 役割: タブを複製する。where が window なら新しいウィンドウを開き、起動後に SessionStore で複製して初期タブを閉じる。tabshifted は背景で、tab は前面で複製する。タブグループのタブなら、重複計測を記録する。
- 触るとき: タブの複製先(新規タブ、背景タブ、新規ウィンドウ)の挙動を変えるとき。
- 呼び出し先: `OpenBrowserWindow()`, `PrivateBrowsingUtils.isBrowserPrivate()`, `Services.obs.addObserver()`, `SessionStore.duplicateTab()`
- 条件付き依存: `if (aTab.group)` → `Glean.tabgroup.tabInteractions.duplicate.add()`
- 参照: `aTab.group`, `aTab.linkedBrowser`
- XPCOM: `Services.obs`

## delayedStartupFinished()
- 位置: L4272-4283
- 役割: 新しいウィンドウの遅延起動が終わったとき、そのウィンドウの初期タブを閉じ、元のタブを SessionStore で複製する。監視は一度で外す。
- 触るとき: 新規ウィンドウへの複製で初期タブが残ったり、複製が失敗したりするとき。
- 条件付き依存: `if ( topic == "browser-delayed-startup-finished" && subject == otherWin )` → `Services.obs.removeObserver()`
- 条件付き依存: `if ( topic == "browser-delayed-startup-finished" && subject == otherWin )` → `SessionStore.duplicateTab()`
- 条件付き依存: `if ( topic == "browser-delayed-startup-finished" && subject == otherWin )` → `otherGBrowser.removeTab()`
- 参照: `otherGBrowser.selectedTab`, `otherWin.gBrowser`
- XPCOM: `Services.obs`

## addListener()
- 位置: L4333-4342
- 役割: 未登録なら hover 状態を false にして監視対象に加え、直ちに現在位置との判定を一度行う。
- 触るとき: マウスの位置で表示を切り替える新しい要素を追加するとき。
- 呼び出し先: `this._callListener()`, `this._listeners.add()`, `this._listeners.has()`
- 参照: `listener._hover`

## removeListener()
- 位置: L4344-4346
- 役割: マウス位置の監視対象から外す。
- 触るとき: 監視を止めた要素がまだ反応してしまうとき。
- 呼び出し先: `this._listeners.delete()`

## handleEvent()
- 位置: L4348-4371
- 役割: mouseout はウィンドウ自身に対するものだけ処理し、それ以外は画面座標を、ズームの違う文書の場合は比率を合わせてウィンドウ内の座標に直し、登録済みの全リスナーを判定する。
- 触るとき: マウス位置の判定がズームやデベロッパーツールで狂うとき。
- 呼び出し先: `console.error()`, `this._callListener()`, `this._listeners.forEach()`
- 参照: `event.currentTarget`, `event.screenX`, `event.screenY`, `event.target.documentGlobal`, `event.type`, `sourceWin.devicePixelRatio`, `this._x`, `this._y`, `window.devicePixelRatio`, `window.mozInnerScreenX`, `window.mozInnerScreenY`

## _callListener()
- 位置: L4373-4394
- 役割: リスナーの矩形を取得し、マウス位置がその内側かどうかを判定する。状態が変わったときだけ onMouseEnter または onMouseLeave を呼ぶ。
- 触るとき: マウスの入退場の通知条件を変えるとき。
- 呼び出し先: `listener.getMouseTargetRect()`
- 条件付き依存: `if (listener.onMouseEnter)` → `listener.onMouseEnter()`
- 条件付き依存: `if (listener.onMouseLeave)` → `listener.onMouseLeave()`
- 参照: `listener._hover`, `listener.onMouseEnter`, `listener.onMouseLeave`, `rect.bottom`, `rect.left`, `rect.right`, `rect.top`, `this._x`, `this._y`

## init()
- 位置: L4398-4404
- 役割: 初期化済みにし、通知保留のフラグがあれば通知を出す。
- 触るとき: パニックボタンの通知の初期化順序を変えるとき。
- 条件付き依存: `if (window.PanicButtonNotifierShouldNotify)` → `this.notify()`
- 参照: `this._initialized`, `window.PanicButtonNotifierShouldNotify`

## createPanelIfNeeded()
- 位置: L4405-4411
- 役割: 成功通知のパネルがまだ DOM に無ければテンプレートを差し込む(遅延読み込み)。
- 触るとき: パニックボタンの通知パネルの作成を変えるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("panic-button-success-notification"))` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("panic-button-success-notification"))` → `template.replaceWith()`
- 参照: `template.content`

## notify()
- 位置: L4412-4459
- 役割: パニックボタン成功の通知を、未初期化なら保留にし、初期化済みならパネルを作って表示する。3 秒後に閉じるタイマーを設定し、マウスやキー操作があれば閉じるタイマーを止め、閉じたらリスナーを外す。
- 触るとき: パニックボタン押下後の通知の表示時間や閉じ方を変えるとき。
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidget("panic-button").forWindow()`, `closeButton.addEventListener()`, `console.error()`, `document.getElementById()`, `popup.addEventListener()`, `popup.getAttribute()`, `popup.openPopup()`, `setTimeout()`, `this.createPanelIfNeeded()`, `window.addEventListener()`
- 参照: `PanicButtonNotifier.timer`, `popup.hidden`, `this._initialized`, `widget.anchor.icon`, `window.PanicButtonNotifierShouldNotify`

## closePopup()
- 位置: L4424-4426
- 役割: 通知パネルを閉じる。
- 触るとき: 通知の閉じ方を変えるとき。
- 呼び出し先: `popup.hidePopup()`

## onUserInteractsWithPopup()
- 位置: L4438-4440
- 役割: マウスやキーの操作があったら自動で閉じるタイマーを止める。
- 触るとき: 通知を操作中に勝手に閉じないようにする条件を変えるとき。
- 呼び出し先: `clearTimeout()`
- 参照: `PanicButtonNotifier.timer`

## removeListeners()
- 位置: L4444-4450
- 役割: 通知パネルに付けた監視と閉じるタイマーをすべて外す。
- 触るとき: 通知を閉じた後のリスナーの解除漏れを調べるとき。
- 呼び出し先: `clearTimeout()`, `closeButton.removeEventListener()`, `popup.removeEventListener()`, `window.removeEventListener()`
- 参照: `PanicButtonNotifier.timer`

## TabDialogBox._containerFor()
- 位置: L4471-4475
- 役割: ブラウザを包む、タブのサイドバーや拡張ポップアップなどのコンテナ要素を探す。
- 触るとき: ダイアログを載せるコンテナの種類を増やすとき。
- 呼び出し先: `browser.closest()`

## TabDialogBox.constructor()
- 位置: L4477-4500
- 役割: ダイアログ用のスタック要素をテンプレートから作ってコンテナに追加し、タブレベルのダイアログ管理(キュー順)を作る。
- 触るとき: タブのダイアログの構成や初期オプションを変えるとき。
- 呼び出し先: `Cu.getWeakReference()`, `TabDialogBox._containerFor()`, `TabDialogBox._containerFor(browser).appendChild()`, `dialogStack.classList.add()`, `document.getElementById()`, `template.content.cloneNode()`
- 参照: `SubDialogManager.ORDER_QUEUE`, `dialogStack.firstElementChild`, `template.content.cloneNode(true).firstElementChild`, `this._tabDialogManager`, `this._weakBrowserRef`

## TabDialogBox.open()
- 位置: L4530-4595
- 役割: ダイアログを開く。modalType がコンテンツ用なら内容用のマネージャーを使い、最初のダイアログ開始時に通知の抑止と進捗監視を始める。閉じたときは最後のダイアログなら後始末する。開いたダイアログと、閉じるまで解決しない Promise を返す。
- 触るとき: タブ内のプロンプトの開き方や同一サイトの移動での閉じ方を変えるとき、または新しいダイアログの種類を追加するとき。
- 呼び出し先: `dialogManager.open()`, `hasDialogs()`, `this.getContentDialogManager()`
- 条件付き依存: `if (!hasDialogs())` → `this._onFirstDialogOpen()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_CONTENT`, `dialog._keepOpenSameOriginNav`, `this._tabDialogManager`, `this.browser.webProgress`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md)

## hasDialogs()
- 位置: L4552-4554
- 役割: タブとコンテンツのどちらかにダイアログがあるかを返す。
- 触るとき: ダイアログの開閉の判定を見直すとき。
- 参照: `this._contentDialogManager?.hasDialogs`, `this._tabDialogManager.hasDialogs`

## closingCallback()
- 位置: L4560-4568
- 役割: ダイアログが閉じたとき、最後のダイアログなら後始末し、許可チェックが有効なら許可を設定する。
- 触るとき: ダイアログを閉じた後の後始末(通知の再表示、タブ切替の許可)を変えるとき。
- 呼び出し先: `hasDialogs()`
- 条件付き依存: `if (!hasDialogs())` → `this._onLastDialogClose()`
- 条件付き依存: `if (allowFocusCheckbox && !event.detail?.abort)` → `this.maybeSetAllowTabSwitchPermission()`
- 参照: `event.detail?.abort`, `event.target`, `this.browser.webProgress`

## TabDialogBox._onFirstDialogOpen()
- 位置: L4597-4607
- 役割: 最初のダイアログが開いたとき、ブラウザに tabDialogShowing を付けて通知の表示を更新し、場所の変化とタブの終了を監視する。
- 触るとき: ダイアログ表示中に通知が隠れる仕組みを変えるとき。
- 呼び出し先: `UpdatePopupNotificationsVisibility()`, `this.browser.setAttribute()`, `this.tab?.addEventListener()`, `webProgress.addProgressListener()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `this._lastPrincipal`, `this.browser.contentPrincipal`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## TabDialogBox._onLastDialogClose()
- 位置: L4609-4619
- 役割: 最後のダイアログが閉じたとき、tabDialogShowing を外して通知の表示を戻し、監視を外す。
- 触るとき: ダイアログを閉じた後に通知が戻らないとき。
- 呼び出し先: `UpdatePopupNotificationsVisibility()`, `this.browser.removeAttribute()`, `this.tab?.removeEventListener()`, `webProgress.removeProgressListener()`
- 参照: `this._lastPrincipal`

## TabDialogBox._buildContentPromptDialog()
- 位置: L4621-4641
- 役割: コンテンツレベルのプロンプト用スタックを作り、タブ用スタックの前に挿入して、専用のマネージャーを用意する。
- 触るとき: コンテンツプロンプト(ページ由来の認証など)の表示位置を変えるとき。
- 呼び出し先: `TabDialogBox._containerFor()`, `browserContainer.insertBefore()`, `browserContainer.querySelector()`, `contentDialogStack.classList.add()`, `document.getElementById()`, `template.content.cloneNode()`
- 参照: `SubDialogManager.ORDER_QUEUE`, `contentDialogStack.firstElementChild`, `template.content.cloneNode(true).firstElementChild`, `this._contentDialogManager`, `this.browser`

## TabDialogBox.handleEvent()
- 位置: L4643-4648
- 役割: タブが閉じられたとき、全てのダイアログを中止する。
- 触るとき: タブ終了時にダイアログが残るとき。
- 呼び出し先: `this.abortAllDialogs()`
- 参照: `event.type`

## TabDialogBox.abortAllDialogs()
- 位置: L4650-4653
- 役割: タブとコンテンツの両方のダイアログを中止させる。
- 触るとき: ダイアログを一括で閉じる必要がある処理を書くとき。
- 呼び出し先: `this._contentDialogManager?.abortDialogs()`, `this._tabDialogManager.abortDialogs()`

## TabDialogBox.focus()
- 位置: L4655-4662
- 役割: タブ用のダイアログがあれば最前面に、無ければコンテンツ用の最前面にフォーカスを移す。
- 触るとき: ダイアログの表示後にフォーカスが背景に残るとき。
- 呼び出し先: `this._contentDialogManager?.focusTopDialog()`
- 条件付き依存: `if (this._tabDialogManager._dialogs.length)` → `this._tabDialogManager.focusTopDialog()`
- 参照: `this._tabDialogManager._dialogs.length`

## TabDialogBox.onLocationChange()
- 位置: L4668-4693
- 役割: トップレベルの別文書への移動で、同一オリジンでなければ全てのダイアログを中止する。同一オリジン移動でも、keepOpenSameOriginNav が無いダイアログは中止する。
- 触るとき: ページ移動時にダイアログを残すか閉じるかの条件を変えるとき。
- 呼び出し先: `this._contentDialogManager?.abortDialogs()`, `this._lastPrincipal?.isSameOrigin()`, `this._tabDialogManager.abortDialogs()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aWebProgress.isTopLevel`, `this._lastPrincipal`, `this.browser.browsingContext.usePrivateBrowsing`, `this.browser.contentPrincipal`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## filterFn()
- 位置: L4686-4686
- 役割: 同一オリジンへの移動時に、keepOpenSameOriginNav が立っていないダイアログだけを中止対象にする。
- 触るとき: 同一オリジン移動でダイアログを残す条件を変えるとき。
- 参照: `dialog._keepOpenSameOriginNav`

## TabDialogBox.tab()
- 位置: L4695-4697
- 役割: このブラウザを持つタブを gBrowser から取り出す。
- 触るとき: ダイアログからタブを参照する処理を書くとき。
- 呼び出し先: `gBrowser.getTabForBrowser()`
- 参照: `this.browser`

## TabDialogBox.browser()
- 位置: L4699-4705
- 役割: 弱参照からブラウザを取り出す。すでに消えていれば例外を投げる。
- 触るとき: 破棄済みのブラウザへのダイアログ参照で例外が出るとき。
- 呼び出し先: `this._weakBrowserRef.get()`

## TabDialogBox.getTabDialogManager()
- 位置: L4707-4709
- 役割: タブレベルのダイアログ管理オブジェクトを返す。
- 触るとき: タブのダイアログを外部から操作するとき。
- 参照: `this._tabDialogManager`

## TabDialogBox.getContentDialogManager()
- 位置: L4711-4716
- 役割: コンテンツレベルのダイアログ管理を返す。まだ無ければ作成してから返す。
- 触るとき: コンテンツプロンプトを表示する経路を調べるとき、またはコンテンツ用マネージャーが必要な初期化の順序を変えるとき。
- 条件付き依存: `if (!this._contentDialogManager)` → `this._buildContentPromptDialog()`
- 参照: `this._contentDialogManager`

## TabDialogBox.onNextPromptShowAllowFocusCheckboxFor()
- 位置: L4718-4720
- 役割: 次に表示するプロンプトについて、タブ切替を許可するチェックボックスを出す対象のプリンシパルを保存する。
- 触るとき: タブ切替の許可チェックボックスを出す対象を変えるとき。
- 参照: `this._allowTabFocusByPromptPrincipal`

## TabDialogBox.maybeSetAllowTabSwitchPermission()
- 位置: L4725-4738
- 役割: チェックボックスがオンなら、保存した対象のプリンシパルに focus-tab-by-prompt の許可を付与し、次回以降はチェックボックスを出さないよう対象を消す。
- 触るとき: プロンプトからタブを前面にする権限の保存条件を変えるとき。
- 呼び出し先: `dialog.querySelector()`
- 条件付き依存: `if (checkbox.checked)` → `Services.perms.addFromPrincipal()`
- 参照: `Services.perms.ALLOW_ACTION`, `checkbox.checked`, `this._allowTabFocusByPromptPrincipal`
- XPCOM: `Services.perms`

## dialog()
- 位置: L4771-4773
- 役割: 開いている window モーダルのダイアログ(SubDialog)を返す。
- 触るとき: 開いているダイアログを外部から操作するとき。
- 参照: `this._dialog`

## isOpen()
- 位置: L4775-4777
- 役割: ダイアログが開いているかを返す。
- 触るとき: ダイアログを開く前に空いているか確認したいとき。
- 参照: `this._dialog`

## replaceDialogIfOpen()
- 位置: L4779-4782
- 役割: 開いているダイアログを閉じ、次に開くダイアログをキューの先頭へ回す指示を立てる。
- 触るとき: 既存のダイアログを新しいものに置き換えるとき。
- 呼び出し先: `this._dialog?.close()`
- 参照: `this._nextOpenJumpsQueue`

## open()
- 位置: async L4784-4849
- 役割: window モーダルのダイアログを開く。すでに開いていれば待ち行列に入れる。モーダル中の同期プロンプトは例外を投げる。開いた後は HTML の close を待ち、後始末でメニューと編集コマンドを戻し、キューに残りがあれば次を開く。
- 触るとき: ウィンドウ単位のプロンプトの表示順や閉じた後の後始末を変えるとき。
- 呼び出し先: `UpdatePopupNotificationsVisibility()`, `args.getProperty()`, `console.error()`, `dialog.removeEventListener()`, `document.documentElement.removeAttribute()`, `document.getElementById()`, `document.querySelectorAll()`, `this._open()`, `this._updateMenuAndCommandState()`, `urlbar.view?.close()`, `window.focus()`, `window.windowUtils.isInModalState()`
- 条件付き依存: `if (this.isOpen)` → `this._queued[queueMethod]()`
- 条件付き依存: `if (window.windowUtils.isInModalState() && !args.getProperty("async"))` → `Components.Exception()`
- 条件付き依存: `if (dialog.open)` → `dialog.close()`
- 条件付き依存: `if (this._queued.length)` → `setTimeout()`
- 条件付き依存: `if (this._queued.length)` → `this._openNextDialog()`
- 参照: `Cr.NS_ERROR_NOT_AVAILABLE`, `dialog.open`, `dialog.style.height`, `dialog.style.visibility`, `dialog.style.width`, `this._dialog`, `this._didCloseHTMLDialog`, `this._didOpenHTMLDialog`, `this._nextOpenJumpsQueue`, `this._queued`, `this._queued.length`, `this.isOpen`

## _openNextDialog()
- 位置: L4851-4856
- 役割: ダイアログが開いていなければ待ち行列の先頭を取り出して open する。
- 触るとき: 待ち行列からダイアログを順に開く処理を変えるとき。
- 条件付き依存: `if (!this.isOpen)` → `this._queued.shift()`
- 条件付き依存: `if (!this.isOpen)` → `this.open(uri, args).then()`
- 条件付き依存: `if (!this.isOpen)` → `this.open()`
- 参照: `this.isOpen`

## handleEvent()
- 位置: L4858-4868
- 役割: dialogopen でダイアログにフォーカスを移し、close で完了の待ちを解除してダイアログを閉じる。
- 触るとき: ダイアログを閉じた後に次のダイアログが開かないとき。
- 呼び出し先: `this._dialog.close()`, `this._dialog.focus()`, `this._didCloseHTMLDialog()`
- 参照: `event.type`

## _open()
- 位置: L4870-4922
- 役割: ウィンドウ内のダイアログ用要素を、ブラウザの位置に合わせて表示し showModal で開く。メニューとショートカットを無効化し、SubDialog を作ってその中に URI を読み込む。閉じたときは DOMModalDialogClosed を発火する。
- 触るとき: ウィンドウモーダルの見た目や開き方を変えるとき。
- 呼び出し先: `UpdatePopupNotificationsVisibility()`, `document.documentElement.setAttribute()`, `document.getElementById()`, `parentElement.addEventListener()`, `parentElement.showModal()`, `parentElement.style.removeProperty()`, `parentElement.style.setProperty()`, `this._dialog.open()`, `this._updateMenuAndCommandState()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_INTERNAL_WINDOW`, `document.getElementById("window-modal-dialog-template") .content.firstElementChild`, `gBrowser.selectedBrowser`, `this._closedCallback`, `this._dialog`, `this._didOpenHTMLDialog`, `window.windowUtils.getBoundsWithoutFlushing( gBrowser.selectedBrowser ).top`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md)

## this._closedCallback()
- 位置: L4904-4907
- 役割: 閉じたときの後始末(DOMModalDialogClosed の発火と完了の解決)を保持する関数を作る。
- 触るとき: ダイアログを閉じたときの通知の流れを変えるとき。
- 呼び出し先: `PromptUtils.fireDialogEvent()`, `resolve()`

## closedCallback()
- 位置: L4914-4916
- 役割: SubDialog が閉じたとき、保存しておいた閉じた後の処理を呼ぶ。
- 触るとき: ダイアログを閉じたあとの処理が呼ばれないとき。
- 呼び出し先: `this._closedCallback()`

## _updateMenuAndCommandState()
- 位置: L4940-4970
- 役割: メニューバーのトップ項目、コマンド、ショートカットの disabled を切り替える。編集系と、デベロッパーツール系のショートカットは対象外。無効化前の状態は wasdisabled に残して、戻すときに復元する。
- 触るとき: ダイアログ表示中にメニューを止める範囲を変えるとき、または閉じた後にメニューが無効のまま残るとき。
- 呼び出し先: `document.getElementById()`, `document.querySelectorAll()`, `editorCommands?.contains()`, `this._nonUpdatableElements.has()`
- 条件付き依存: `if (!shouldBeEnabled)` → `element.hasAttribute()`
- 条件付き依存: `if (!element.hasAttribute("disabled"))` → `element.setAttribute()`
- 条件付き依存: `if (!(!element.hasAttribute("disabled")))` → `element.setAttribute()`
- 条件付き依存: `if (!(!shouldBeEnabled))` → `element.getAttribute()`
- 条件付き依存: `if (element.getAttribute("wasdisabled") != "true")` → `element.removeAttribute()`
- 条件付き依存: `if (!(element.getAttribute("wasdisabled") != "true"))` → `element.removeAttribute()`
- 参照: `element.command`, `element.id`, `element.nodeName`

## show()
- 位置: L5003-5079
- 役割: ツールチップ風の確認ヒントを、アンカーの近くに出す。メッセージ、説明、チェックマーク、位置を設定して開き、表示中なら自動で閉じるタイマーだけを再設定する。表示は 3 秒、説明付きは 6 秒。
- 触るとき: 保存完了などの一時的な確認ヒントの文言や表示時間を変えるとき、または新しいヒントを追加するとき。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `document.l10n.setAttributes()`, `this._panel.addEventListener()`, `this._panel.openPopup()`, `this._panel.setAttribute()`, `this._reset()`
- 条件付き依存: `if ( messageId === "confirmation-hint-ipprotection-navigated-to-excluded-site" )` → `MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (descriptionId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (descriptionId)` → `this._panel.classList.add()`
- 条件付き依存: `if (!(descriptionId))` → `this._panel.classList.remove()`
- 条件付き依存: `if (!hideCheckmark)` → `this._panel.classList.add()`
- 条件付き依存: `if (this._panel.state == "open")` → `startAutoHideTimer()`
- 参照: `this._description`, `this._description.hidden`, `this._message`, `this._panel.state`

## startAutoHideTimer()
- 位置: L5048-5053
- 役割: チェックマークのアニメーションを始め、表示時間の後にパネルを閉じるタイマーを設定する。
- 触るとき: 確認ヒントの自動で閉じる時間を調整するとき。
- 呼び出し先: `setTimeout()`, `this._animationBox.setAttribute()`, `this._panel.hidePopup()`
- 参照: `this._timerID`

## _reset()
- 位置: L5081-5091
- 役割: 閉じるタイマーを止め、表示中の要素の属性とチェックマークのクラスを外す。
- 触るとき: 新しいヒントに切り替えたときに前の状態が残るとき。
- 条件付き依存: `if (this._timerID)` → `clearTimeout()`
- 条件付き依存: `if (this.__panel)` → `this._animationBox.removeAttribute()`
- 条件付き依存: `if (this.__panel)` → `this._panel.removeAttribute()`
- 条件付き依存: `if (this.__panel)` → `this._panel.classList.remove()`
- 参照: `this.__panel`, `this._timerID`

## _panel()
- 位置: L5093-5096
- 役割: 確認ヒントのパネル要素を返す。未作成なら作る。
- 触るとき: 確認ヒントのパネルを参照する処理を書くとき。
- 呼び出し先: `this._ensurePanel()`
- 参照: `this.__panel`

## _animationBox()
- 位置: L5098-5104
- 役割: チェックマーク用のアニメーション箱を遅延で取り出す。
- 触るとき: チェックマークの見た目を変えるとき。
- 呼び出し先: `document.getElementById()`, `this._ensurePanel()`
- 参照: `this._animationBox`

## _message()
- 位置: L5106-5112
- 役割: メッセージ要素を遅延で取り出す。
- 触るとき: ヒントのメッセージ表示先を変えるとき。
- 呼び出し先: `document.getElementById()`, `this._ensurePanel()`
- 参照: `this._message`

## _description()
- 位置: L5114-5120
- 役割: 説明文の要素を遅延で取り出す。
- 触るとき: ヒントの説明文を変えるとき。
- 呼び出し先: `document.getElementById()`, `this._ensurePanel()`
- 参照: `this._description`

## _ensurePanel()
- 位置: L5122-5128
- 役割: 確認ヒントのテンプレートをまだ DOM に入れていなければ差し込み、パネル要素を保持する。
- 触るとき: 確認ヒントの読み込みタイミングを変えるとき。
- 条件付き依存: `if (!this.__panel)` → `document.getElementById()`
- 条件付き依存: `if (!this.__panel)` → `wrapper.replaceWith()`
- 参照: `this.__panel`, `wrapper.content`

## button()
- 位置: L5134-5136
- 役割: Firefox View のボタン要素を返す。
- 触るとき: Firefox View のボタンを参照するとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.BUTTON_ID`

## init()
- 位置: L5137-5143
- 役割: カスタマイズモードの変化を監視し、同期タブの読み込みを用意する。
- 触るとき: Firefox View の初期化時に登録する監視を増やすとき。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `CustomizableUI.addListener()`

## uninit()
- 位置: L5144-5146
- 役割: カスタマイズモードの監視を外す。
- 触るとき: Firefox View の後始末を変えるとき。
- 呼び出し先: `CustomizableUI.removeListener()`

## onWidgetRemoved()
- 位置: L5147-5151
- 役割: Firefox View のボタンがツールバーから外されたとき、開いている Firefox View のタブを閉じる。
- 触るとき: ボタンを外したときに Firefox View のタブが残るとき。
- 条件付き依存: `if (aWidgetId == this.BUTTON_ID && this.tab)` → `gBrowser.removeTab()`
- 参照: `this.BUTTON_ID`, `this.tab`

## onWidgetAdded()
- 位置: L5152-5156
- 役割: Firefox View のボタンが追加されたとき、open 属性を外す。
- 触るとき: ボタンを追加した後に開いた状態が残るとき。
- 条件付き依存: `if (aWidgetId === this.BUTTON_ID)` → `this.button.removeAttribute()`
- 参照: `this.BUTTON_ID`

## openTab()
- 位置: L5157-5186
- 役割: Firefox View のタブを前面に開く。指定の節がある場合は about:firefoxview の末尾に付ける。古い未確定の読み込み以外で別ページに移っていたタブは閉じて作り直す。タブが無ければ隠しタブとして追加して監視を付ける。最後に、ペアリング後の不要なタブを閉じてからタブを選択する。
- 触るとき: Firefox View の開き方、節の指定、タブの作り直しの条件を変えるとき。
- 呼び出し先: `this._closeDeviceConnectedTab()`, `this.tab.linkedBrowser.currentURI.spec.split()`
- 条件付き依存: `if ( this.tab && !this.tab.linkedBrowser.browsingContext.currentWindowGlobal .isInitialDocument && this.tab.linkedBrowser.currentURI.spec.split("#")[0] != viewURL )` → `gBrowser.removeTab()`
- 条件付き依存: `if (!this.tab)` → `gBrowser.addTrustedTab()`
- 条件付き依存: `if (!this.tab)` → `this.tab.addEventListener()`
- 条件付き依存: `if (!this.tab)` → `gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (!this.tab)` → `window.addEventListener()`
- 条件付き依存: `if (!this.tab)` → `gBrowser.hideTab()`
- 条件付き依存: `if (!this.tab)` → `this.button?.setAttribute()`
- 参照: `gBrowser.selectedTab`, `this.tab`, `this.tab.linkedBrowser.browsingContext.currentWindowGlobal .isInitialDocument`, `this.tab.linkedPanel`

## openToolbarMouseEvent()
- 位置: L5187-5192
- 役割: マウスのイベントが左ボタン以外の mousedown なら何もせず、それ以外は openTab を呼ぶ。
- 触るとき: ツールバーの Firefox View ボタンを右クリックなどで開かないようにするとき。
- 呼び出し先: `this.openTab()`
- 参照: `event?.button`, `event?.type`

## handleEvent()
- 位置: L5193-5216
- 役割: タブ選択時はボタンの open と aria-pressed を更新し、閲覧を記録し、同期タブを更新し、先頭タブのフォーカスを切り替える。タブが閉じたら参照を消し、ウィンドウが有効化されたときは同期を更新する。
- 触るとき: Firefox View のタブ選択時の表示やフォーカスの扱いを変えるとき。
- 呼び出し先: `gBrowser.tabContainer.removeEventListener()`, `this._onTabForegrounded()`, `this._recordViewIfTabSelected()`, `this.button?.removeAttribute()`, `this.button?.setAttribute()`, `this.button?.toggleAttribute()`
- 参照: `e.target`, `e.type`, `gBrowser.visibleTabs`, `gBrowser.visibleTabs[0].style.MozUserFocus`, `this.tab`

## _closeDeviceConnectedTab()
- 位置: L5217-5243
- 役割: 端末ペアリングの完了ページ(fxa の pair/auth/complete)のタブが残っていれば閉じる。他にタブが無い場合は先に新しいタブを開き、フラグを戻す。
- 触るとき: 端末ペアリング後にタブが残る問題を調べるとき。
- 呼び出し先: `Services.prefs.getCharPref()`, `gBrowser.removeTab()`, `gBrowser.tabs.find()`, `tab.linkedBrowser.currentURI.displaySpec.startsWith()`
- 条件付き依存: `if (gBrowser.tabs.length <= 2)` → `gBrowser.addTrustedTab()`
- 参照: `TabsSetupFlowManager.didFxaTabOpen`, `gBrowser.tabs.length`
- XPCOM: `Services.prefs`

## _onTabForegrounded()
- 位置: L5244-5248
- 役割: Firefox View のタブが選択中なら、同期タブの情報を更新する。
- 触るとき: Firefox View を前面にしたときの同期更新の条件を変えるとき。
- 条件付き依存: `if (this.tab?.selected)` → `this.SyncedTabs.syncTabs()`
- 参照: `this.tab?.selected`

## _recordViewIfTabSelected()
- 位置: L5249-5273
- 役割: Firefox View のタブが選択中なら、ボタン押下の回数を Glean に記録し、30 日ごとに回数を戻して pref に保存する。
- 触るとき: Firefox View のボタン利用の計測項目や集計期間を変えるとき。
- 条件付き依存: `if (this.tab?.selected)` → `JSON.parse()`
- 条件付き依存: `if (this.tab?.selected)` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (this.tab?.selected)` → `Glean.firefoxviewNext.tabSelectedToolbarbutton.record()`
- 条件付き依存: `if (this.tab?.selected)` → `Math.round()`
- 条件付き依存: `if (this.tab?.selected)` → `Date.now()`
- 条件付き依存: `if (this.tab?.selected)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (this.tab?.selected)` → `JSON.stringify()`
- 参照: `buttonClicksData.count`, `buttonClicksData.lastCountTime`, `this.tab?.selected`
- XPCOM: `Services.prefs`
