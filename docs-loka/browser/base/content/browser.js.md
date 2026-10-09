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
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (topWindow)` → `topWindow.focus()`
- 条件付き依存: `if (features)` → `window.open()`
- 条件付き依存: `if (!(features))` → `window.open()`
- XPCOM: `Services.wm`

## OpenBrowserWindow()
- 位置: L1756-1772
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.openWindow()`, `Glean.browserTimings.newWindow.start()`, `Glean.browserTimings.newWindow.stopAndAccumulate()`, `win.addEventListener()`
- 参照: `options.openerWindow`

## updateEditUIVisibility()
- 位置: L1794-1872
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `document.getElementById()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `menu.setAttribute()`
- 参照: `menu.hidden`
- XPCOM: `Services.prefs`

## updateImportCommandEnabledState()
- 位置: L1895-1901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document .getElementById("cmd_file_importFromAnotherBrowser") .setAttribute()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document .getElementById()`
- XPCOM: `Services.policies`

## updateTabCloseCountState()
- 位置: L1907-1916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (document.getElementById("menu_closeWindow").hidden)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(document.getElementById("menu_closeWindow").hidden))` → `document.l10n.setAttributes()`
- 参照: `document.getElementById("menu_closeWindow").hidden`, `gBrowser.selectedTabs.length`

## onPopupShowing()
- 位置: L1918-1946
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.isAIWindowActive()`, `AIWindow.isAIWindowEnabled()`, `PrintUtils.updatePrintSetupMenuHiddenState()`, `event.target.querySelector()`, `this.updateImportCommandEnabledState()`, `this.updateUserContextUIVisibility()`
- 条件付き依存: `if (typeof gBrowser != "undefined")` → `this.updateTabCloseCountState()`
- 条件付き依存: `if (typeof gBrowser != "undefined")` → `SharingUtils.ensureShareMenu()`
- 条件付き依存: `if (typeof gBrowser != "undefined")` → `gBrowser.selectedTabs.map()`
- 条件付き依存: `if (typeof gBrowser != "undefined")` → `document.getElementById()`
- 参照: `aiWindowMenu.hidden`, `classicWindowMenu.hidden`, `event.target.id`, `gBrowser.selectedBrowser`, `gBrowser.selectedTabs.length`, `t.linkedBrowser`

## openNewUserContextTab()
- 位置: L1957-1964
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.getAttribute()`, `openTrustedLinkIn()`, `parseInt()`
- 参照: `event.target.dataset.containerEntrypoint`

## stopCommand()
- 位置: L1982-1985
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.stopCommand`

## reloadCommand()
- 位置: L1986-1989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.reloadCommand`

## _elementsForTextBasedTypes()
- 位置: L1990-1997
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._elementsForTextBasedTypes`

## _elementsForFind()
- 位置: L1998-2005
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._elementsForFind`

## _elementsForViewSource()
- 位置: L2006-2012
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._elementsForViewSource`

## _menuItemForRepairTextEncoding()
- 位置: L2013-2018
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._menuItemForRepairTextEncoding`

## _menuItemForTranslations()
- 位置: L2019-2023
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._menuItemForTranslations`

## _moreToolsTranslateMenuItem()
- 位置: L2024-2029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._moreToolsTranslateMenuItem`

## setDefaultStatus()
- 位置: L2031-2034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `StatusPanel.update()`
- 参照: `this.defaultStatus`

## setOverLink()
- 位置: L2045-2073
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LinkTargetDisplay.update()`, `window.dispatchEvent()`
- 条件付き依存: `if (url)` → `Services.textToSubURI.unEscapeURIForUI()`
- 条件付き依存: `if (url)` → `url.replace()`
- 条件付き依存: `if (url)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("trimURLs"))` → `BrowserUIUtils.trimURL()`
- 参照: `this.overLink`
- XPCOM: `Services.textToSubURI`

## onEnterDOMFullscreen()
- 位置: L2075-2080
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setDefaultStatus()`, `this.setOverLink()`
- 参照: `this.status`

## showTooltip()
- 位置: L2082-2104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/dragservice;1"] .getService()`, `Cc["@mozilla.org/widget/dragservice;1"] .getService(Ci.nsIDragService) .getCurrentSession()`, `document.getElementById()`, `document.hasFocus()`, `elt.openPopupAtScreen()`
- 参照: `Ci.nsIDragService`, `elt.label`, `elt.style.direction`, `window.devicePixelRatio`
- XPCOM: `nsIDragService` / `@mozilla.org/widget/dragservice;1`

## hideTooltip()
- 位置: L2106-2109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `elt.hidePopup()`

## getTabCount()
- 位置: L2111-2113
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gBrowser.tabs.length`

## onProgressChange()
- 位置: L2115-2117
- 役割: (未記入)
- 触るとき: (未記入)

## onProgressChange64()
- 位置: L2119-2135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onProgressChange()`

## onStateChange()
- 位置: L2138-2259
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelectorAll()`
- 条件付き依存: `if (panel.state != "closed")` → `panel.hidePopup()`
- 参照: `panel.state`

## _updateElementsForContentType()
- 位置: L2441-2480
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MacUserActivityUpdater.updateLocation()`, `PrivateBrowsingUtils.isWindowPrivate()`, `win.docShell.treeOwner.QueryInterface()`
- 参照: `AppConstants.platform`, `Ci.nsIBaseWindow`, `uri.spec`, `webProgress.isTopLevel`, `win.gBrowser.contentTitle`
- XPCOM: `nsIBaseWindow`

## _securityURIOverride()
- 位置: L2525-2559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doGetProtocolFlags()`
- 参照: `Ci.nsIProtocolHandler`, `browser.contentPrincipal`, `browser.currentURI`, `principal.URI`, `principal.isNullPrincipal`, `principal.originNoSuffix`, `principal.precursorPrincipal`, `uri.filePath`, `uri.scheme`
- XPCOM: [`nsIProtocolHandler`](../../../netwerk/base/nsIIOService.idl.md)

## asyncUpdateUI()
- 位置: L2561-2563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OpenSearchManager.updateOpenSearchBadge()`

## onStatusChange()
- 位置: L2565-2568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `StatusPanel.update()`
- 参照: `this.status`

## onContentBlockingEvent()
- 位置: L2582-2618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gProtectionsHandler.onContentBlockingEvent()`, `gTrustPanelHandler.onContentBlockingEvent()`
- 参照: `gBrowser.currentURI`, `this._event`, `this._lastLocationForEvent`, `uri.spec`

## onSecurityChange()
- 位置: L2625-2651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.createExposableURI()`, `gIdentityHandler.updateIdentity()`, `gTrustPanelHandler.updateIdentity()`, `gURLBar.formatValue()`, `this._securityURIOverride()`
- 条件付き依存: `if (window.browsingContext.isDocumentPiP)` → `gURLBar.setURI()`
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_ASSOCIATED`, `gBrowser.currentURI`, `gBrowser.selectedBrowser`, `window.browsingContext.isDocumentPiP`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.io`

## XWB_onUpdateCurrentBrowser()
- 位置: L2654-2689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById("aHTMLTooltip").hidePopup()`, `this.hideTooltip()`, `this.onStateChange()`, `this.onStatusChange()`
- 条件付き依存: `if (FullZoom.updateBackgroundTabs)` → `FullZoom.onLocationChange()`
- 参照: `Ci.nsIWebProgressListener`, `FullZoom.updateBackgroundTabs`, `gBrowser.currentURI`, `gBrowser.webProgress`, `nsIWebProgressListener.STATE_START`, `nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## DELAY_SHOW()
- 位置: L2706-2711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 参照: `this.DELAY_SHOW`
- XPCOM: `Services.prefs`

## _contextMenu()
- 位置: L2716-2721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._contextMenu`

## update()
- 位置: L2723-2753
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `this._showDelayed()`
- 参照: `event.type`, `this._timer`

## _showDelayed()
- 位置: L2765-2774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `StatusPanel.update()`, `setTimeout()`, `window.removeEventListener()`
- 参照: `this.DELAY_SHOW`, `this._timer`

## _hide()
- 位置: L2776-2780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `StatusPanel.update()`, `clearTimeout()`
- 参照: `this._timer`

## ensureInitialized()
- 位置: L2786-2824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XULBrowserWindow.stopCommand.hasAttribute()`, `button.hasAttribute()`, `document.getElementById()`, `stop.addEventListener()`
- 条件付き依存: `if (!XULBrowserWindow.stopCommand.hasAttribute("disabled"))` → `reload.setAttribute()`
- 条件付き依存: `if (button.hasAttribute("disabled"))` → `document.getElementById()`
- 条件付き依存: `if (button.hasAttribute("disabled"))` → `button.getAttribute()`
- 条件付き依存: `if (button.hasAttribute("disabled"))` → `command.hasAttribute()`
- 条件付き依存: `if (!command.hasAttribute("disabled"))` → `button.removeAttribute()`
- 参照: `this._destroyed`, `this._initialized`, `this.reload`, `this.stop`

## uninit()
- 位置: L2826-2837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cancelTransition()`, `this.stop.removeEventListener()`
- 参照: `this._destroyed`, `this._initialized`, `this.reload`, `this.stop`

## handleEvent()
- 位置: L2839-2847
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `event.button`, `event.type`, `this._stopClicked`, `this.stop.disabled`

## switchToStop()
- 位置: L2849-2858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._shouldSwitch()`, `this.ensureInitialized()`, `this.reload.setAttribute()`

## switchToReload()
- 位置: L2860-2890
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XULBrowserWindow.reloadCommand.hasAttribute()`, `setTimeout()`, `this.ensureInitialized()`, `this.reload.hasAttribute()`, `this.reload.removeAttribute()`
- 条件付き依存: `if (this._stopClicked)` → `XULBrowserWindow.reloadCommand.hasAttribute()`
- 参照: `self._timer`, `self.reload.disabled`, `this._stopClicked`, `this._timer`, `this.reload.disabled`

## _shouldSwitch()
- 位置: L2892-2905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aRequest.originalURI.schemeIs()`, `aRequest.originalURI.spec.startsWith()`
- 参照: `aRequest.originalURI`, `aWebProgress.isTopLevel`

## _cancelTransition()
- 位置: L2907-2912
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._timer)` → `clearTimeout()`
- 参照: `this._timer`

## onStateChange()
- 位置: L2916-2971
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CaptivePortalWatcher.onLocationChange()`, `FullZoom.onLocationChange()`, `Object.getOwnPropertyDescriptor()`, `Services.obs.notifyObservers()`, `gBrowser.readNotificationBox()`, `gBrowser.readNotificationBox(aBrowser)?.removeTransientNotifications()`
- 条件付き依存: `if (aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT)` → `aBrowser.sendMessageToActor()`
- 条件付き依存: `if (!Object.getOwnPropertyDescriptor(window, "PopupNotifications").get)` → `PopupNotifications.locationChange()`
- 条件付き依存: `if (aBrowser._sharingState)` → `gBrowser.resetBrowserSharing()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `Object.getOwnPropertyDescriptor(window, "PopupNotifications").get`, `aBrowser._sharingState`, `aBrowser.isArticle`, `aWebProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.obs`

## onLinkIconAvailable()
- 位置: L3015-3024
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (browser == gBrowser.selectedBrowser)` → `OpenSearchManager.updateOpenSearchBadge()`
- 参照: `gBrowser.selectedBrowser`

## showFullScreenViewContextMenuItems()
- 位置: L3027-3035
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popup.querySelector()`, `popup.querySelectorAll()`
- 条件付き依存: `if (autoHide)` → `FullScreen.updateAutohideMenuitem()`
- 参照: `node.hidden`, `window.fullScreen`

## onViewToolbarCommand()
- 位置: L3037-3057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUsageTelemetry.recordToolbarVisibility()`, `CustomizableUI.setToolbarVisibility()`
- 条件付き依存: `if (node.dataset.bookmarksToolbarVisibility)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (!(node.dataset.bookmarksToolbarVisibility))` → `node.getAttribute()`
- 条件付き依存: `if (!(node.dataset.bookmarksToolbarVisibility))` → `node.hasAttribute()`
- 参照: `aEvent.originalTarget`, `node.dataset.bookmarksToolbarVisibility`, `node.dataset.visibilityEnum`, `node.parentNode.id`, `node.parentNode.parentNode.parentNode.id`
- XPCOM: `Services.prefs`

## setToolbarVisibility()
- 位置: L3059-3149
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `control.getAttribute()`, `control.hasAttribute()`, `control.setAttribute()`
- 条件付き依存: `if (!control.hasAttribute("label-unchecked"))` → `control.setAttribute()`
- 条件付き依存: `if (!control.hasAttribute("label-unchecked"))` → `control.getAttribute()`

## init()
- 位置: L3166-3171
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.update()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.obs.addObserver()`
- 参照: `AppConstants.platform`, `WindowsUIUtils.inWin10TabletMode`
- XPCOM: `Services.obs`

## uninit()
- 位置: L3173-3177
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.obs.removeObserver()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.obs`

## observe()
- 位置: L3179-3181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.update()`

## update()
- 位置: L3183-3189
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isInTabletMode)` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (!(isInTabletMode))` → `document.documentElement.removeAttribute()`

## displaySecurityInfo()
- 位置: L3192-3194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserCommands.pageInfo()`

## init()
- 位置: L3235-3263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `UIDensityTelemetry.init()`, `document.getElementById()`, `this.update()`, `window.addEventListener()`
- 条件付き依存: `if (sidebarContainer)` → `this.update()`
- 条件付き依存: `if (sidebarContainer)` → `this._sidebarStateObserver.observe()`
- 参照: `this._sidebarShownHandler`, `this._sidebarStateObserver`, `this.autoCompactThresholdPref`, `this.autoTouchModePref`, `this.rfpWindowSizingPrefs`, `this.uiDensityPref`
- XPCOM: `Services.obs` / `Services.prefs`

## this._sidebarShownHandler()
- 位置: L3247-3247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.update()`

## uninit()
- 位置: L3265-3282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `window.removeEventListener()`
- 条件付き依存: `if (this._sidebarShownHandler)` → `window.removeEventListener()`
- 条件付き依存: `if (this._sidebarStateObserver)` → `this._sidebarStateObserver.disconnect()`
- 参照: `this._sidebarShownHandler`, `this._sidebarStateObserver`, `this.autoCompactThresholdPref`, `this.autoTouchModePref`, `this.rfpWindowSizingPrefs`, `this.uiDensityPref`
- XPCOM: `Services.obs` / `Services.prefs`

## handleEvent()
- 位置: L3284-3300
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "resize")` → `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (event.type == "resize")` → `this.update()`
- 参照: `event.type`, `this.novaEnabled`, `this.uiDensityPref`
- XPCOM: `Services.prefs`

## observe()
- 位置: L3302-3317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.knownPrefs.has()`, `this.update()`

## _shouldAutoCompact()
- 位置: L3319-3362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`, `parseFloat()`, `this._densityReferenceSize()`, `this._isSidebarLauncherCollapsed()`, `this.rfpWindowSizingPrefs.some()`
- 参照: `this.AUTO_COMPACT_REFERENCE_SIDEBAR_LAUNCHER_WIDTH`, `this.AUTO_COMPACT_REFERENCE_TABSTRIP_HEIGHT`, `this.autoCompactThresholdPref`, `window.toolbar.visible`
- XPCOM: `Services.prefs`

## _densityReferenceSize()
- 位置: L3370-3378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.getAttribute()`
- 条件付き依存: `if (document.documentElement.getAttribute("sizemode") == "maximized")` → `Math.max()`
- 参照: `window.innerHeight`, `window.innerWidth`, `window.screen.availHeight`, `window.screen.availWidth`

## _isSidebarLauncherCollapsed()
- 位置: L3382-3402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `SidebarController._state`, `SidebarController.initialized`, `SidebarController.sidebarRevampVisibility`, `state.launcherExpanded`, `state?.launcherVisible`
- XPCOM: `Services.prefs`

## _inTabletMode()
- 位置: L3406-3411
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`, `WindowsUIUtils.inWin10TabletMode`, `WindowsUIUtils.inWin11TabletMode`

## getCurrentDensity()
- 位置: L3413-3445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`, `this._inTabletMode()`, `this._shouldAutoCompact()`
- 条件付き依存: `if (this._inTabletMode())` → `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (this._inTabletMode())` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (this._inTabletMode())` → `Services.prefs.getBoolPref()`
- 参照: `this.MODE_COMPACT`, `this.MODE_NORMAL`, `this.MODE_TOUCH`, `this.autoTouchModePref`, `this.novaEnabled`, `this.uiDensityPref`
- XPCOM: `Services.prefs`

## update()
- 位置: L3447-3508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.removeAttribute()`, `doc.setAttribute()`, `window.dispatchEvent()`
- 条件付き依存: `if (mode == null)` → `this.getCurrentDensity()`
- 条件付き依存: `if (sidebarContentDoc?.documentElement)` → `docs.push()`
- 条件付き依存: `if (sidebarContentDoc)` → `sidebarContentDoc.querySelector()`
- 条件付き依存: `if (!isInitialUpdate)` → `UIDensityTelemetry.onDensityChanged()`
- 参照: `SidebarController.browser.contentDocument`, `SidebarController.initialized`, `SidebarController.isOpen`, `document.documentElement`, `sidebarContentDoc.documentElement`, `sidebarContentDoc?.documentElement`, `this.MODE_COMPACT`, `this.MODE_TOUCH`, `this._appliedMode`, `this.getCurrentDensity().mode`, `tree.style.border`

## getText()
- 位置: L3561-3584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`, `this.cache.has()`
- 条件付き依存: `if (nodeId in this.nodeToShortcutMap)` → `document.getElementById()`
- 条件付き依存: `if (shortcut)` → `ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (shortcut)` → `args.push()`
- 条件付き依存: `if (!this.cache.has(nodeId) && nodeId in this.nodeToTooltipMap)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (shouldCache)` → `this.cache.set()`
- 参照: `this.nodeToShortcutMap`, `this.nodeToTooltipMap`

## updateText()
- 位置: L3586-3589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTooltip.setAttribute()`, `this.getText()`
- 参照: `aTooltip.triggerNode.id`

## contentAreaClick()
- 位置: L3610-3683
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.whereToOpenLink()`, `Event.isInstance()`, `UrlbarShared.stripUnsafeProtocolOnPaste()`, `UrlbarUtils.addToUrlbarHistory()`, `UrlbarUtils.getShortcutOrURIAndPostData()`, `UrlbarUtils.getShortcutOrURIAndPostData(clipboard).then()`, `clipboard.replace()`, `console.error()`, `makeURI()`, `readFromClipboard()`
- 条件付き依存: `if ( where != "current" || lastLocationChange == gBrowser.selectedBrowser.lastLocationChange )` → `openUILink()`
- 条件付き依存: `if (Event.isInstance(event))` → `event.stopPropagation()`
- 参照: `data.mayInheritPrincipal`, `data.url`, `gBrowser.selectedBrowser.contentPrincipal`, `gBrowser.selectedBrowser.lastLocationChange`, `gBrowser.selectedBrowser.policyContainer`

## init()
- 位置: L3815-3825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `this._updateOfflineUI()`
- 条件付き依存: `if (!this._uiElement)` → `document.getElementById()`
- 参照: `Services.io.offline`, `this._inited`, `this._uiElement`
- XPCOM: `Services.io` / `Services.obs`

## uninit()
- 位置: L3827-3831
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._inited)` → `Services.obs.removeObserver()`
- 参照: `this._inited`
- XPCOM: `Services.obs`

## toggleOfflineStatus()
- 位置: L3833-3842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._canGoOffline()`
- 条件付き依存: `if (!ioService.offline && !this._canGoOffline())` → `this._updateOfflineUI()`
- 参照: `Services.io`, `ioService.offline`
- XPCOM: `Services.io`

## observe()
- 位置: L3845-3853
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateOfflineUI()`
- 参照: `Services.io.offline`
- XPCOM: `Services.io`

## _canGoOffline()
- 位置: L3856-3870
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`
- 参照: `Ci.nsISupportsPRBool`, `cancelGoOffline.data`
- XPCOM: [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.obs`

## _updateOfflineUI()
- 位置: L3873-3877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`, `this._uiElement.toggleAttribute()`
- XPCOM: `Services.prefs`

## CanCloseWindow()
- 位置: L3880-3899
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.permitUnload()`
- 参照: `Services.startup.shuttingDown`, `browser.isConnected`, `gBrowser.browsers`, `window.skipNextCanClose`
- XPCOM: `Services.startup`

## WindowIsClosing()
- 位置: L3906-4022
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gURLBar.makeURIReadable()`, `this.sendMessage()`
- 参照: `aBrowser.contentTitle`, `aBrowser.currentURI`, `gURLBar.makeURIReadable(aBrowser.currentURI).displaySpec`

## sendMessage()
- 位置: L4117-4129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeURI()`, `this._launchExternalUrl()`
- 条件付き依存: `if (aBody)` → `encodeURIComponent()`

## _launchExternalUrl()
- 位置: L4134-4144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/external-protocol-service;1" ].getService()`
- 条件付き依存: `if (extProtocolSvc)` → `extProtocolSvc.loadURI()`
- 条件付き依存: `if (extProtocolSvc)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `Ci.nsIExternalProtocolService`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1` / `Services.scriptSecurityManager`

## observe()
- 位置: L4157-4159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gRemoteControl.updateVisualCue()`

## updateVisualCue()
- 位置: L4161-4185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.getRemoteControlComponent()`
- 条件付き依存: `if (remoteControlComponent)` → `mainWindow.setAttribute()`
- 条件付き依存: `if (remoteControlComponent)` → `document.getElementById()`
- 条件付き依存: `if (remoteControlComponent)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(remoteControlComponent))` → `mainWindow.removeAttribute()`
- 参照: `Cu.isInAutomation`, `document.documentElement`
- XPCOM: `Services.prefs`

## getRemoteControlComponent()
- 位置: L4187-4207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DevToolsSocketStatus.hasSocketOpened()`
- 参照: `Marionette.running`, `RemoteAgent.running`

## switchToTabHavingURI()
- 位置: L4214-4229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URILoadingHelper.switchToTabHavingURI()`

## safeModeRestart()
- 位置: L4232-4254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `Ci.nsISupportsPRBool`, `Services.appinfo.inSafeMode`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.appinfo` / `Services.obs` / `Services.startup`

## duplicateTabIn()
- 位置: L4266-4304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OpenBrowserWindow()`, `PrivateBrowsingUtils.isBrowserPrivate()`, `Services.obs.addObserver()`, `SessionStore.duplicateTab()`
- 条件付き依存: `if (aTab.group)` → `Glean.tabgroup.tabInteractions.duplicate.add()`
- 参照: `aTab.group`, `aTab.linkedBrowser`
- XPCOM: `Services.obs`

## delayedStartupFinished()
- 位置: L4272-4283
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( topic == "browser-delayed-startup-finished" && subject == otherWin )` → `Services.obs.removeObserver()`
- 条件付き依存: `if ( topic == "browser-delayed-startup-finished" && subject == otherWin )` → `SessionStore.duplicateTab()`
- 条件付き依存: `if ( topic == "browser-delayed-startup-finished" && subject == otherWin )` → `otherGBrowser.removeTab()`
- 参照: `otherGBrowser.selectedTab`, `otherWin.gBrowser`
- XPCOM: `Services.obs`

## addListener()
- 位置: L4333-4342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callListener()`, `this._listeners.add()`, `this._listeners.has()`
- 参照: `listener._hover`

## removeListener()
- 位置: L4344-4346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._listeners.delete()`

## handleEvent()
- 位置: L4348-4371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._callListener()`, `this._listeners.forEach()`
- 参照: `event.currentTarget`, `event.screenX`, `event.screenY`, `event.target.documentGlobal`, `event.type`, `sourceWin.devicePixelRatio`, `this._x`, `this._y`, `window.devicePixelRatio`, `window.mozInnerScreenX`, `window.mozInnerScreenY`

## _callListener()
- 位置: L4373-4394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listener.getMouseTargetRect()`
- 条件付き依存: `if (listener.onMouseEnter)` → `listener.onMouseEnter()`
- 条件付き依存: `if (listener.onMouseLeave)` → `listener.onMouseLeave()`
- 参照: `listener._hover`, `listener.onMouseEnter`, `listener.onMouseLeave`, `rect.bottom`, `rect.left`, `rect.right`, `rect.top`, `this._x`, `this._y`

## init()
- 位置: L4398-4404
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (window.PanicButtonNotifierShouldNotify)` → `this.notify()`
- 参照: `this._initialized`, `window.PanicButtonNotifierShouldNotify`

## createPanelIfNeeded()
- 位置: L4405-4411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("panic-button-success-notification"))` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("panic-button-success-notification"))` → `template.replaceWith()`
- 参照: `template.content`

## notify()
- 位置: L4412-4459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidget("panic-button").forWindow()`, `closeButton.addEventListener()`, `console.error()`, `document.getElementById()`, `popup.addEventListener()`, `popup.getAttribute()`, `popup.openPopup()`, `setTimeout()`, `this.createPanelIfNeeded()`, `window.addEventListener()`
- 参照: `PanicButtonNotifier.timer`, `popup.hidden`, `this._initialized`, `widget.anchor.icon`, `window.PanicButtonNotifierShouldNotify`

## closePopup()
- 位置: L4424-4426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popup.hidePopup()`

## onUserInteractsWithPopup()
- 位置: L4438-4440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`
- 参照: `PanicButtonNotifier.timer`

## removeListeners()
- 位置: L4444-4450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `closeButton.removeEventListener()`, `popup.removeEventListener()`, `window.removeEventListener()`
- 参照: `PanicButtonNotifier.timer`

## TabDialogBox._containerFor()
- 位置: L4471-4475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.closest()`

## TabDialogBox.constructor()
- 位置: L4477-4500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `TabDialogBox._containerFor()`, `TabDialogBox._containerFor(browser).appendChild()`, `dialogStack.classList.add()`, `document.getElementById()`, `template.content.cloneNode()`
- 参照: `SubDialogManager.ORDER_QUEUE`, `dialogStack.firstElementChild`, `template.content.cloneNode(true).firstElementChild`, `this._tabDialogManager`, `this._weakBrowserRef`

## TabDialogBox.open()
- 位置: L4530-4595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialogManager.open()`, `hasDialogs()`, `this.getContentDialogManager()`
- 条件付き依存: `if (!hasDialogs())` → `this._onFirstDialogOpen()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_CONTENT`, `dialog._keepOpenSameOriginNav`, `this._tabDialogManager`, `this.browser.webProgress`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md)

## hasDialogs()
- 位置: L4552-4554
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._contentDialogManager?.hasDialogs`, `this._tabDialogManager.hasDialogs`

## closingCallback()
- 位置: L4560-4568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hasDialogs()`
- 条件付き依存: `if (!hasDialogs())` → `this._onLastDialogClose()`
- 条件付き依存: `if (allowFocusCheckbox && !event.detail?.abort)` → `this.maybeSetAllowTabSwitchPermission()`
- 参照: `event.detail?.abort`, `event.target`, `this.browser.webProgress`

## TabDialogBox._onFirstDialogOpen()
- 位置: L4597-4607
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdatePopupNotificationsVisibility()`, `this.browser.setAttribute()`, `this.tab?.addEventListener()`, `webProgress.addProgressListener()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `this._lastPrincipal`, `this.browser.contentPrincipal`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## TabDialogBox._onLastDialogClose()
- 位置: L4609-4619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdatePopupNotificationsVisibility()`, `this.browser.removeAttribute()`, `this.tab?.removeEventListener()`, `webProgress.removeProgressListener()`
- 参照: `this._lastPrincipal`

## TabDialogBox._buildContentPromptDialog()
- 位置: L4621-4641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabDialogBox._containerFor()`, `browserContainer.insertBefore()`, `browserContainer.querySelector()`, `contentDialogStack.classList.add()`, `document.getElementById()`, `template.content.cloneNode()`
- 参照: `SubDialogManager.ORDER_QUEUE`, `contentDialogStack.firstElementChild`, `template.content.cloneNode(true).firstElementChild`, `this._contentDialogManager`, `this.browser`

## TabDialogBox.handleEvent()
- 位置: L4643-4648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.abortAllDialogs()`
- 参照: `event.type`

## TabDialogBox.abortAllDialogs()
- 位置: L4650-4653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentDialogManager?.abortDialogs()`, `this._tabDialogManager.abortDialogs()`

## TabDialogBox.focus()
- 位置: L4655-4662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentDialogManager?.focusTopDialog()`
- 条件付き依存: `if (this._tabDialogManager._dialogs.length)` → `this._tabDialogManager.focusTopDialog()`
- 参照: `this._tabDialogManager._dialogs.length`

## TabDialogBox.onLocationChange()
- 位置: L4668-4693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentDialogManager?.abortDialogs()`, `this._lastPrincipal?.isSameOrigin()`, `this._tabDialogManager.abortDialogs()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aWebProgress.isTopLevel`, `this._lastPrincipal`, `this.browser.browsingContext.usePrivateBrowsing`, `this.browser.contentPrincipal`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## filterFn()
- 位置: L4686-4686
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dialog._keepOpenSameOriginNav`

## TabDialogBox.tab()
- 位置: L4695-4697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.getTabForBrowser()`
- 参照: `this.browser`

## TabDialogBox.browser()
- 位置: L4699-4705
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._weakBrowserRef.get()`

## TabDialogBox.getTabDialogManager()
- 位置: L4707-4709
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._tabDialogManager`

## TabDialogBox.getContentDialogManager()
- 位置: L4711-4716
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._contentDialogManager)` → `this._buildContentPromptDialog()`
- 参照: `this._contentDialogManager`

## TabDialogBox.onNextPromptShowAllowFocusCheckboxFor()
- 位置: L4718-4720
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._allowTabFocusByPromptPrincipal`

## TabDialogBox.maybeSetAllowTabSwitchPermission()
- 位置: L4725-4738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialog.querySelector()`
- 条件付き依存: `if (checkbox.checked)` → `Services.perms.addFromPrincipal()`
- 参照: `Services.perms.ALLOW_ACTION`, `checkbox.checked`, `this._allowTabFocusByPromptPrincipal`
- XPCOM: `Services.perms`

## dialog()
- 位置: L4771-4773
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._dialog`

## isOpen()
- 位置: L4775-4777
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._dialog`

## replaceDialogIfOpen()
- 位置: L4779-4782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dialog?.close()`
- 参照: `this._nextOpenJumpsQueue`

## open()
- 位置: async L4784-4849
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdatePopupNotificationsVisibility()`, `args.getProperty()`, `console.error()`, `dialog.removeEventListener()`, `document.documentElement.removeAttribute()`, `document.getElementById()`, `document.querySelectorAll()`, `this._open()`, `this._updateMenuAndCommandState()`, `urlbar.view?.close()`, `window.focus()`, `window.windowUtils.isInModalState()`
- 条件付き依存: `if (this.isOpen)` → `this._queued[queueMethod]()`
- 条件付き依存: `if (window.windowUtils.isInModalState() && !args.getProperty("async"))` → `Components.Exception()`
- 条件付き依存: `if (dialog.open)` → `dialog.close()`
- 条件付き依存: `if (this._queued.length)` → `setTimeout()`
- 条件付き依存: `if (this._queued.length)` → `this._openNextDialog()`
- 参照: `Cr.NS_ERROR_NOT_AVAILABLE`, `dialog.open`, `dialog.style.height`, `dialog.style.visibility`, `dialog.style.width`, `this._dialog`, `this._didCloseHTMLDialog`, `this._didOpenHTMLDialog`, `this._nextOpenJumpsQueue`, `this._queued`, `this._queued.length`, `this.isOpen`

## _openNextDialog()
- 位置: L4851-4856
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.isOpen)` → `this._queued.shift()`
- 条件付き依存: `if (!this.isOpen)` → `this.open(uri, args).then()`
- 条件付き依存: `if (!this.isOpen)` → `this.open()`
- 参照: `this.isOpen`

## handleEvent()
- 位置: L4858-4868
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dialog.close()`, `this._dialog.focus()`, `this._didCloseHTMLDialog()`
- 参照: `event.type`

## _open()
- 位置: L4870-4922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdatePopupNotificationsVisibility()`, `document.documentElement.setAttribute()`, `document.getElementById()`, `parentElement.addEventListener()`, `parentElement.showModal()`, `parentElement.style.removeProperty()`, `parentElement.style.setProperty()`, `this._dialog.open()`, `this._updateMenuAndCommandState()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_INTERNAL_WINDOW`, `document.getElementById("window-modal-dialog-template") .content.firstElementChild`, `gBrowser.selectedBrowser`, `this._closedCallback`, `this._dialog`, `this._didOpenHTMLDialog`, `window.windowUtils.getBoundsWithoutFlushing( gBrowser.selectedBrowser ).top`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md)

## this._closedCallback()
- 位置: L4904-4907
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PromptUtils.fireDialogEvent()`, `resolve()`

## closedCallback()
- 位置: L4914-4916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._closedCallback()`

## _updateMenuAndCommandState()
- 位置: L4940-4970
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this._animationBox.setAttribute()`, `this._panel.hidePopup()`
- 参照: `this._timerID`

## _reset()
- 位置: L5081-5091
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._timerID)` → `clearTimeout()`
- 条件付き依存: `if (this.__panel)` → `this._animationBox.removeAttribute()`
- 条件付き依存: `if (this.__panel)` → `this._panel.removeAttribute()`
- 条件付き依存: `if (this.__panel)` → `this._panel.classList.remove()`
- 参照: `this.__panel`, `this._timerID`

## _panel()
- 位置: L5093-5096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensurePanel()`
- 参照: `this.__panel`

## _animationBox()
- 位置: L5098-5104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._ensurePanel()`
- 参照: `this._animationBox`

## _message()
- 位置: L5106-5112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._ensurePanel()`
- 参照: `this._message`

## _description()
- 位置: L5114-5120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._ensurePanel()`
- 参照: `this._description`

## _ensurePanel()
- 位置: L5122-5128
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.__panel)` → `document.getElementById()`
- 条件付き依存: `if (!this.__panel)` → `wrapper.replaceWith()`
- 参照: `this.__panel`, `wrapper.content`

## button()
- 位置: L5134-5136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.BUTTON_ID`

## init()
- 位置: L5137-5143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `CustomizableUI.addListener()`

## uninit()
- 位置: L5144-5146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`

## onWidgetRemoved()
- 位置: L5147-5151
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId == this.BUTTON_ID && this.tab)` → `gBrowser.removeTab()`
- 参照: `this.BUTTON_ID`, `this.tab`

## onWidgetAdded()
- 位置: L5152-5156
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId === this.BUTTON_ID)` → `this.button.removeAttribute()`
- 参照: `this.BUTTON_ID`

## openTab()
- 位置: L5157-5186
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openTab()`
- 参照: `event?.button`, `event?.type`

## handleEvent()
- 位置: L5193-5216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabContainer.removeEventListener()`, `this._onTabForegrounded()`, `this._recordViewIfTabSelected()`, `this.button?.removeAttribute()`, `this.button?.setAttribute()`, `this.button?.toggleAttribute()`
- 参照: `e.target`, `e.type`, `gBrowser.visibleTabs`, `gBrowser.visibleTabs[0].style.MozUserFocus`, `this.tab`

## _closeDeviceConnectedTab()
- 位置: L5217-5243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`, `gBrowser.removeTab()`, `gBrowser.tabs.find()`, `tab.linkedBrowser.currentURI.displaySpec.startsWith()`
- 条件付き依存: `if (gBrowser.tabs.length <= 2)` → `gBrowser.addTrustedTab()`
- 参照: `TabsSetupFlowManager.didFxaTabOpen`, `gBrowser.tabs.length`
- XPCOM: `Services.prefs`

## _onTabForegrounded()
- 位置: L5244-5248
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.tab?.selected)` → `this.SyncedTabs.syncTabs()`
- 参照: `this.tab?.selected`

## _recordViewIfTabSelected()
- 位置: L5249-5273
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.tab?.selected)` → `JSON.parse()`
- 条件付き依存: `if (this.tab?.selected)` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (this.tab?.selected)` → `Glean.firefoxviewNext.tabSelectedToolbarbutton.record()`
- 条件付き依存: `if (this.tab?.selected)` → `Math.round()`
- 条件付き依存: `if (this.tab?.selected)` → `Date.now()`
- 条件付き依存: `if (this.tab?.selected)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (this.tab?.selected)` → `JSON.stringify()`
- 参照: `buttonClicksData.count`, `buttonClicksData.lastCountTime`, `this.tab?.selected`
- XPCOM: `Services.prefs`
