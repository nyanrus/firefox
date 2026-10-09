# browser/components/extensions/ExtensionControlledPopup.sys.mjs

source: browser/components/extensions/ExtensionControlledPopup.sys.mjs
source-hash: 13f2bb2fb5019eba3305d168669bb581f63568ac
lines: 453

## <module>
- 役割: 拡張機能が新規タブやホームページを変えたときに、確認用のドアハンガーを出す仕組みを定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs .getChildList()`, `Services.prefs .getChildList(PREF_BRANCH_INSTALLED_ADDON) .map()`, `Services.strings.createBundle()`, `id.replace()`

## ExtensionControlledPopup.constructor()
- 位置: L102-118
- 役割: ポップアップのオプション(確認の種類、監視トピック、説明文、設定の種類とキー、副ボタンの動作など)を保持する。
- 触るとき: 同種の確認ポップアップを新しく作るとき、渡すオプションの意味を確かめるとき。
- 参照: `opts.beforeDisableAddon`, `opts.confirmedType`, `opts.descriptionId`, `opts.descriptionMessageId`, `opts.getLocalizedDescription`, `opts.learnMoreLink`, `opts.observerTopic`, `opts.onObserverAdded`, `opts.onObserverRemoved`, `opts.popupnotificationId`, `opts.preferencesEntrypoint`, `opts.preferencesLocation`, `opts.settingKey`, `opts.settingType`, `this.beforeDisableAddon`, `this.confirmedType`, `this.descriptionId`, `this.descriptionMessageId`, `this.getLocalizedDescription`, `this.learnMoreLink`, `this.observerRegistered`, `this.observerTopic`, `this.onObserverAdded`, `this.onObserverRemoved`, `this.popupnotificationId`, `this.preferencesEntrypoint`, `this.preferencesLocation`, `this.settingKey`, `this.settingType`

## ExtensionControlledPopup.topWindow()
- 位置: L120-122
- 役割: 最後に前面にあった navigator:browser のウィンドウを返す。
- 触るとき: ポップアップを出す先のウィンドウの決め方を変えるとき。
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- XPCOM: `Services.wm`

## ExtensionControlledPopup.userHasConfirmed()
- 位置: L124-143
- 役割: 配布版アドオンなら true、副ボタンでの無効化がポリシーで禁じられていれば true を返し、それ以外は確認済みの設定値を返す。
- 触るとき: ポップアップを再び出すかどうかの判定を変えるとき。
- 呼び出し先: `Services.policies.isAllowed()`, `lazy.ExtensionSettingsStore.getSetting()`, `lazy.distributionAddonsList.has()`
- 参照: `Services.policies`, `setting.value`, `this.confirmedType`, `this.preferencesLocation`
- XPCOM: `Services.policies`

## ExtensionControlledPopup.setConfirmation()
- 位置: async L145-154
- 役割: ExtensionSettingsStore に、そのアドオンの確認済みの設定を追加する。
- 触るとき: 確認済みの保存の仕方や保存先の種類を変えるとき。
- 呼び出し先: `lazy.ExtensionSettingsStore.addSetting()`, `lazy.ExtensionSettingsStore.initialize()`
- 参照: `this.confirmedType`

## ExtensionControlledPopup.clearConfirmation()
- 位置: async L156-163
- 役割: ExtensionSettingsStore から、そのアドオンの確認済みの設定を削除する。
- 触るとき: 確認を取り消す経路を追うとき。
- 呼び出し先: `lazy.ExtensionSettingsStore.initialize()`, `lazy.ExtensionSettingsStore.removeSetting()`
- 参照: `this.confirmedType`

## ExtensionControlledPopup.observe()
- 位置: L165-178
- 役割: 監視トピックを受けると、まず監視を外してから、アイドル時に open を呼ぶ。対象が文書を持つウィンドウなら、そのウィンドウを渡す。
- 触るとき: ポップアップが開くきっかけや、同じ通知で二重に開かない仕組みを変えるとき。
- 呼び出し先: `this.open()`, `this.removeObserver()`, `this.topWindow.requestIdleCallback()`
- 参照: `subject.document`

## ExtensionControlledPopup.removeObserver()
- 位置: L180-188
- 役割: 登録中の監視を外し、onObserverRemoved があれば呼ぶ。
- 触るとき: 監視の登録と解除の対応を確かめるとき。
- 条件付き依存: `if (this.observerRegistered)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.onObserverRemoved)` → `this.onObserverRemoved()`
- 参照: `this.observerRegistered`, `this.observerTopic`, `this.onObserverRemoved`
- XPCOM: `Services.obs`

## ExtensionControlledPopup.addObserver()
- 位置: async L190-200
- 役割: まだ確認されていなければ、監視トピックへ登録し、onObserverAdded を呼ぶ。
- 触るとき: ポップアップの監視をいつ始めるかを変えるとき。
- 呼び出し先: `lazy.ExtensionSettingsStore.initialize()`, `this.userHasConfirmed()`
- 条件付き依存: `if (!this.observerRegistered && !this.userHasConfirmed(extensionId))` → `Services.obs.addObserver()`
- 条件付き依存: `if (this.onObserverAdded)` → `this.onObserverAdded()`
- 参照: `this.observerRegistered`, `this.observerTopic`, `this.onObserverAdded`
- XPCOM: `Services.obs`

## ExtensionControlledPopup.open()
- 位置: async L204-359
- 役割: 条件を満たせばポップアップを表示する。非公開ウィンドウで許可されていない拡張、確認済み、ウィンドウが閉じた場合は何もしない。ボタンの処理を登録し、ツールバーのボタンか拡張ボタンにアンカーして開く。
- 触るとき: 表示条件、ボタンの動作、アンカーの位置のどれかを変えるとき。
- 呼び出し先: `ExtensionControlledPopup._getAndMaybeCreatePanel()`, `WebExtensionPolicy.getByID()`, `doc.getElementById()`, `lazy.AddonManager.getAddonByID()`, `lazy.CustomizableUI.getWidget()`, `lazy.ExtensionSettingsStore.initialize()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `makeWidgetId()`, `panel.addEventListener()`, `panel.openPopup()`, `panel.querySelectorAll()`, `panel.removeEventListener()`, `popupnotification.show()`, `this._ensureWindowReady()`, `this.populateDescription()`, `this.removeObserver()`, `this.userHasConfirmed()`
- 条件付き依存: `if (!extensionId)` → `lazy.ExtensionSettingsStore.getSetting()`
- 条件付き依存: `if (elementsToTranslate.length)` → `win.MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (elementsToTranslate.length)` → `el.setAttribute()`
- 条件付き依存: `if (elementsToTranslate.length)` → `el.getAttribute()`
- 条件付き依存: `if (elementsToTranslate.length)` → `el.removeAttribute()`
- 条件付き依存: `if (elementsToTranslate.length)` → `win.document.l10n.translateFragment()`
- 条件付き依存: `if (action)` → `action .forWindow(win) .node.querySelector()`
- 条件付き依存: `if (action)` → `action .forWindow()`
- 条件付き依存: `if (this.learnMoreLink)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (this.learnMoreLink)` → `popupnotification.setAttribute()`
- 条件付き依存: `if (!(this.learnMoreLink))` → `popupnotification.removeAttribute()`
- 条件付き依存: `if (anchor?.id == "unified-extensions-button")` → `gUnifiedExtensions.recordButtonTelemetry()`
- 条件付き依存: `if (anchor?.id == "unified-extensions-button")` → `gUnifiedExtensions.ensureButtonShownBeforeAttachingPanel()`
- 参照: `WebExtensionPolicy.getByID(extensionId).privateBrowsingAllowed`, `action.areaType`, `anchor.documentGlobal`, `anchor?.id`, `elementsToTranslate.length`, `item.id`, `popupnotification.hidden`, `this.learnMoreLink`, `this.popupnotificationId`, `this.settingKey`, `this.settingType`, `this.topWindow`, `win.document`, `win.gURLBar.focused`
- XPCOM: `Services.urlFormatter`

## handleButtonCommand()
- 位置: async L270-284
- 役割: 主ボタンでポップアップを閉じ、確認を保存する。URL バーにフォーカスがあったなら、そこへ戻す。
- 触るとき: 主ボタンを押した後の確認の保存やフォーカスの戻し方を変えるとき。
- 呼び出し先: `event.preventDefault()`, `panel.hidePopup()`, `this.setConfirmation()`
- 条件付き依存: `if (urlBarWasFocused)` → `win.gURLBar.focus()`

## handleSecondaryButtonCommand()
- 位置: async L285-306
- 役割: 副ボタンで設定画面を開く。設定の場所がなければ beforeDisableAddon を待ってからアドオンを無効化する。
- 触るとき: 副ボタンの動作(設定を開く、無効化)を変えるとき。
- 呼び出し先: `event.preventDefault()`, `panel.hidePopup()`
- 条件付き依存: `if (this.preferencesLocation)` → `win.openPreferences()`
- 条件付き依存: `if (this.beforeDisableAddon)` → `this.beforeDisableAddon()`
- 条件付き依存: `if (!(this.preferencesLocation))` → `addon.disable()`
- 条件付き依存: `if (urlBarWasFocused)` → `win.gURLBar.focus()`
- 参照: `this.Entrypoint`, `this.beforeDisableAddon`, `this.preferencesLocation`

## ExtensionControlledPopup.getAddonDetails()
- 位置: L361-373
- 役割: アドオンのアイコンと名前を並べた文書断片を作り、説明文へ差し込めるようにする。
- 触るとき: 説明文に出すアドオンの情報の見た目を変えるとき。
- 呼び出し先: `addonDetails.appendChild()`, `doc.createDocumentFragment()`, `doc.createTextNode()`, `doc.createXULElement()`, `image.classList.add()`, `image.setAttribute()`
- 参照: `addon.iconURL`, `addon.name`

## ExtensionControlledPopup.populateDescription()
- 位置: L375-390
- 役割: 説明要素を空にし、説明メッセージにアドオン情報を入れて追加する。独自の描画関数があればそれを使う。
- 触るとき: 説明文の組み立て(メッセージの取得、独自の描画)を変えるとき。
- 呼び出し先: `doc.getElementById()`, `lazy.strBundle.GetStringFromName()`, `this.getAddonDetails()`
- 条件付き依存: `if (this.getLocalizedDescription)` → `description.appendChild()`
- 条件付き依存: `if (this.getLocalizedDescription)` → `this.getLocalizedDescription()`
- 条件付き依存: `if (!(this.getLocalizedDescription))` → `description.appendChild()`
- 条件付き依存: `if (!(this.getLocalizedDescription))` → `lazy.BrowserUIUtils.getLocalizedFragment()`
- 参照: `description.textContent`, `this.descriptionId`, `this.descriptionMessageId`, `this.getLocalizedDescription`

## ExtensionControlledPopup._ensureWindowReady()
- 位置: async L392-441
- 役割: ウィンドウが閉じていなければ、アクティブ化とフォーカスのイベントを待つ。待機中にアンロードされたら失敗させる。
- 触るとき: ポップアップを出すタイミングを、ウィンドウのフォーカス取得後に変えるとき。
- 条件付き依存: `if (activeWindow != win)` → `promiseEvent()`
- 条件付き依存: `if (focusedWindow)` → `rootTreeItem.QueryInterface()`
- 条件付き依存: `if (focusedWindow != win)` → `promiseEvent()`
- 条件付き依存: `if (promises.length)` → `win.addEventListener()`
- 条件付き依存: `if (promises.length)` → `Promise.all()`
- 条件付き依存: `if (promises.length)` → `Promise.race()`
- 条件付き依存: `if (promises.length)` → `win.removeEventListener()`
- 参照: `Ci.nsIDocShell`, `Services.focus`, `focusedWindow.docShell`, `promises.length`, `rootTreeItem.docViewer.DOMDocument.defaultView`, `win.closed`
- XPCOM: [`nsIDocShell`](../../../docshell/base/nsIDocShell.idl.md) / `Services.focus`

## promiseEvent()
- 位置: L398-409
- 役割: 指定したイベントを一度だけ受ける Promise を作り、後で外せるようにリスナを記録する。
- 触るとき: _ensureWindowReady が待つイベントの種類を増やすとき。
- 呼び出し先: `listenersToRemove.push()`, `promises.push()`, `win.addEventListener()`

## listener()
- 位置: L401-404
- 役割: 受け取ったイベントのリスナを外して、Promise を解決する。
- 触るとき: イベント待ちの後始末を変えるとき。
- 呼び出し先: `resolve()`, `win.removeEventListener()`

## unloadListener()
- 位置: L426-431
- 役割: アンロード時に、待っていたリスナをすべて外し、Promise をウィンドウが閉じた扱いで失敗させる。
- 触るとき: ウィンドウが閉じたときの待機の中断条件を変えるとき。
- 呼び出し先: `reject()`, `win.removeEventListener()`

## ExtensionControlledPopup._getAndMaybeCreatePanel()
- 位置: L443-451
- 役割: 遅延読み込み用のテンプレートがあれば展開し、extension-notification-panel を返す。
- 触るとき: 拡張通知のパネルを作るタイミングを変えるとき。
- 呼び出し先: `doc.getElementById()`
- 条件付き依存: `if (template)` → `template.replaceWith()`
- 参照: `template.content`
