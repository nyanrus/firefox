# browser/modules/PopupAndRedirectBlockerObserver.sys.mjs

source: browser/modules/PopupAndRedirectBlockerObserver.sys.mjs
source-hash: b82d0cbd94a5d8e3055cbf25aaa5f9fa17f38bb0
lines: 416

## <module>
- 役割: ポップアップとリダイレクトのブロック通知、およびそのオプションメニューを管理する
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## handleEvent()
- 位置: L16-34
- 役割: ブロック関連の DOM イベントを種類ごとに対応するハンドラへ振り分ける
- 触るとき: 新しいイベント種別を追加するとき、またはブロック通知が特定の操作に反応しないとき
- 呼び出し先: `this.onCommand()`, `this.onDOMUpdateBlockedPopupsAndRedirect()`, `this.onPopupHiding()`, `this.onPopupShowing()`
- 参照: `aEvent.type`

## onDOMUpdateBlockedPopupsAndRedirect()
- 位置: L42-64
- 役割: 選択中のタブのブロック数とリダイレクト有無を見て、通知を出すか消すかを決める
- 触るとき: ブロック数の更新で通知が出ない・消えないといった問題を調べるとき。privacy.popups.showBrowserMessage が false なら通知を出さない
- 呼び出し先: `Services.prefs.getBoolPref()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.getBlockedPopupCount()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.isRedirectBlocked()`, `gPermissionPanel.refreshPermissionIcons()`
- 条件付き依存: `if (!popupCount && !isRedirectBlocked)` → `this.hideNotification()`
- 条件付き依存: `if (Services.prefs.getBoolPref("privacy.popups.showBrowserMessage"))` → `this.ensureInitializedForWindow()`
- 条件付き依存: `if (Services.prefs.getBoolPref("privacy.popups.showBrowserMessage"))` → `this.showBrowserMessage()`
- 参照: `aEvent.originalTarget`, `aEvent.originalTarget.documentGlobal`, `gBrowser.selectedBrowser`
- XPCOM: `Services.prefs`

## hideNotification()
- 位置: L66-73
- 役割: ブラウザの通知ボックスから popup-blocked 通知を取り除く
- 触るとき: タブを切り替えたときや通知を消すときに、通知が残る問題を直すとき
- 呼び出し先: `aBrowser.getNotificationBox()`, `notificationBox.getNotificationWithValue()`
- 条件付き依存: `if (notification)` → `notificationBox.removeNotification()`

## ensureInitializedForWindow()
- 位置: L75-86
- 役割: blockedPopupOptions メニューに command・popupshowing・popuphiding のリスナーを一度だけ登録する
- 触るとき: オプションメニューの項目が反応しない、または二重に動くときに見る。initialized 属性で二重登録を防いでいる
- 呼び出し先: `aWindow.document.getElementById()`, `popup.addEventListener()`, `popup.getAttribute()`, `popup.setAttribute()`

## showBrowserMessage()
- 位置: async L88-143
- 役割: ブロック数に応じた文言で通知バーを出す。既存の通知があれば文言だけ更新し、閉じられた後は出さない
- 触るとき: 通知の文言、優先度、ボタンを変えるとき、または閉じた通知が再表示される問題を調べるとき。数が maxReportedPopups 以上なら超過用の文言を使う
- 呼び出し先: `aBrowser.getNotificationBox()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `popupAndRedirectBlocker.eventCallback.bind()`, `popupAndRedirectBlocker.hasBeenDismissed()`
- 参照: `aBrowser.selectedBrowser`, `notification.label`, `notificationBox.PRIORITY_INFO_MEDIUM`, `selectedBrowser.popupAndRedirectBlocker`, `this.mNotificationPromise`, `this.maxReportedPopups`

## onPopupShowing()
- 位置: async L151-196
- 役割: オプションメニューを開いたとき、サイト名入りの許可項目を更新し、リダイレクトとポップアップの一覧取得を始める
- 触るとき: メニューのサイト名表示や許可項目の表示条件を変えるとき。dom.disable_open_during_load がロックされていると許可項目は隠れる
- 呼び出し先: `Services.prefs.prefIsLocked()`, `blockedPopupDontShowMessage.removeAttribute()`, `document.getElementById()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker .getBlockedPopups()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker .getBlockedPopups() .then()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker .getBlockedRedirect()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker .getBlockedRedirect() .then()`, `this.onPopupShowingBlockedPopups()`, `this.onPopupShowingBlockedRedirect()`
- 条件付き依存: `if (Services.prefs.prefIsLocked("dom.disable_open_during_load"))` → `blockedPopupAllowSite.setAttribute()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("dom.disable_open_during_load")))` → `blockedPopupAllowSite.removeAttribute()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("dom.disable_open_during_load")))` → `document.l10n.setAttributes()`
- 参照: `aEvent.originalTarget.documentGlobal`, `browser.contentPrincipal`, `browser.currentURI`, `browser.isContentPrincipal`, `gBrowser.selectedBrowser`, `uriOrPrincipal.asciiHost`, `uriOrPrincipal.displayHost`, `uriOrPrincipal.spec`
- XPCOM: `Services.prefs`

## onPopupShowingBlockedRedirect()
- 位置: L198-237
- 役割: ブロックされたリダイレクトがあればメニューに項目を 1 件追加し、なければ区切りを隠す
- 触るとき: リダイレクト項目の表示や重複防止を調べるとき。既に項目があれば追加しない
- 呼び出し先: `blockedRedirectSeparator.after()`, `document.createXULElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `menuitem.setAttribute()`, `nextElement?.hasAttribute()`
- 参照: `aBlockedRedirect.browsingContext`, `aBlockedRedirect.innerWindowId`, `aBlockedRedirect.redirectURISpec`, `blockedRedirectSeparator.hidden`, `blockedRedirectSeparator.nextElementSibling`, `gBrowser.selectedBrowser`, `menuitem.browser`, `menuitem.browsingContext`

## onPopupShowingBlockedPopups()
- 位置: L239-281
- 役割: ブロックされたポップアップごとにメニュー項目を追加し、解除に必要な識別子を持たせる
- 触るとき: ポップアップ一覧の表示内容や、個別に開くための識別子を変えるとき
- 呼び出し先: `blockedPopupsSeparator.after()`, `document.createXULElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `menuitem.setAttribute()`, `nextElement?.hasAttribute()`
- 参照: `aBlockedPopups.length`, `blockedPopup.browsingContext`, `blockedPopup.innerWindowId`, `blockedPopup.popupWindowURISpec`, `blockedPopup.reportIndex`, `blockedPopupsSeparator.hidden`, `blockedPopupsSeparator.nextElementSibling`, `gBrowser.selectedBrowser`, `menuitem.browser`, `menuitem.browsingContext`

## onPopupHiding()
- 位置: L289-315
- 役割: メニューを閉じたとき、追加したリダイレクトとポップアップの項目を削除する
- 触るとき: メニューを閉じた後に項目が残る、または消えすぎるといった問題を見るとき
- 呼び出し先: `document.getElementById()`, `item.remove()`, `item?.hasAttribute()`
- 条件付き依存: `if (item?.hasAttribute("redirectInnerWindowId"))` → `item.remove()`
- 参照: `aEvent.originalTarget.documentGlobal`, `blockedPopupsSeparator.nextElementSibling`, `blockedRedirectSeparator.nextElementSibling`, `item.nextElementSibling`

## onCommand()
- 位置: L323-345
- 役割: オプションメニューの項目クリックを、属性か id に応じて各処理へ振り分ける
- 触るとき: メニューに新しい項目を足す、または項目の id や属性を変えるとき
- 呼び出し先: `aEvent.target.hasAttribute()`, `this.dontShowMessage()`, `this.editPopupSettings()`, `this.toggleAllowPopupsForSite()`
- 条件付き依存: `if (aEvent.target.hasAttribute("popupReportIndex"))` → `this.showBlockedPopup()`
- 条件付き依存: `if (aEvent.target.hasAttribute("redirectURISpec"))` → `this.navigateToBlockedRedirect()`
- 参照: `aEvent.target.id`

## showBlockedPopup()
- 位置: L347-357
- 役割: メニュー項目から、そのブロック済みポップアップの解除を依頼する
- 触るとき: ポップアップを個別に開く動作を変えるとき。報告インデックスと内部ウィンドウ ID の受け渡しを確認する
- 呼び出し先: `aEvent.target.getAttribute()`, `browser.popupAndRedirectBlocker.unblockPopup()`
- 参照: `aEvent.target`

## navigateToBlockedRedirect()
- 位置: L359-369
- 役割: メニュー項目から、ブロックされたリダイレクト先への遷移を解除付きで依頼する
- 触るとき: リダイレクトを許可して遷移する経路を変えるとき
- 呼び出し先: `aEvent.target.getAttribute()`, `browser.popupAndRedirectBlocker.unblockRedirect()`
- 参照: `aEvent.target`

## toggleAllowPopupsForSite()
- 位置: async L371-393
- 役割: 現在のサイトのポップアップを許可に設定し、通知を閉じ、ブロック済みポップアップとリダイレクトを順に解除する
- 触るとき: 「サイトで許可」の動作順序を変えるとき。現ドキュメントのポップアップを先に解除し、その後でリダイレクトを解除する
- 呼び出し先: `Services.perms.addFromPrincipal()`, `Services.prefs.prefIsLocked()`, `gBrowser.getNotificationBox()`, `gBrowser.getNotificationBox().removeCurrentNotification()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.unblockAllPopups()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.unblockFirstRedirect()`
- 参照: `Services.perms.ALLOW_ACTION`, `aEvent.originalTarget.documentGlobal`, `gBrowser.contentPrincipal`
- XPCOM: `Services.perms` / `Services.prefs`

## editPopupSettings()
- 位置: L395-400
- 役割: プライバシー設定のポップアップ関連の項目を開く
- 触るとき: 設定画面の遷移先を変えるとき
- 呼び出し先: `openPreferences()`
- 参照: `aEvent.originalTarget.documentGlobal`

## dontShowMessage()
- 位置: L402-408
- 役割: showBrowserMessage の設定を false にして、現在の通知を閉じる
- 触るとき: 「今後表示しない」ボタンの効果や、対象の設定キーを確認するとき
- 呼び出し先: `Services.prefs.setBoolPref()`, `gBrowser.getNotificationBox()`, `gBrowser.getNotificationBox().removeCurrentNotification()`
- 参照: `aEvent.originalTarget.documentGlobal`
- XPCOM: `Services.prefs`
