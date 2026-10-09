# browser/modules/ExtensionsUI.sys.mjs

source: browser/modules/ExtensionsUI.sys.mjs
source-hash: 73ef024602cb4554a024de4ddef83f492adc33ef
lines: 890

## <module>
- 役割: WebExtension のインストール・権限・更新・サイドロード・既定検索などの確認を、ポップアップや通知で表示する ExtensionsUI を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `EventEmitter.decorate()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## getTabBrowser()
- 位置: L48-63
- 役割: 拡張のビューの browser から chrome 側の browser とウィンドウを求める。ビューがポップアップかサイドバーなら、そのウィンドウの選択中のタブの browser を返す。
- 触るとき: 拡張のポップアップやサイドバーから出た確認がどのタブに出るかを調べるときに見る。
- 呼び出し先: `browser.getAttribute()`
- 参照: `Ci.nsIDocShell.typeChrome`, `browser.documentGlobal`, `browser.documentGlobal.docShell.chromeEventHandler`, `browser.documentGlobal.docShell.itemType`, `window.browsingContext.topChromeWindow`, `window.gBrowser.selectedBrowser`
- XPCOM: [`nsIDocShell`](../../docshell/base/nsIDocShell.idl.md)

## init()
- 位置: async L72-86
- 役割: 拡張の確認・通知に関する 8 種類のオブザーバーを登録し、最初のブラウザーウィンドウの起動完了後にサイドロードの確認を始める。
- 触るとき: 新しい通知トピックを追加するとき、または起動時にサイドロードの確認が走らないときに見る。
- 呼び出し先: `Services.obs.addObserver()`, `Services.wm.getMostRecentWindow()`, `this._checkForSideloaded()`
- 参照: `Services.wm.getMostRecentWindow("navigator:browser") .delayedStartupPromise`
- XPCOM: `Services.obs` / `Services.wm`

## _checkForSideloaded()
- 位置: async L88-123
- 役割: 新しくサイドロードされたアドオンを取得し、ID 順に並べて未承認の一覧へ入れる。有効化を監視するリスナーを張り、通知を更新する。新規がなければ何もしない。
- 触るとき: サイドロードの確認通知が出ない、または並び順を変えるときに見る。
- 呼び出し先: `a.id.localeCompare()`, `lazy.AddonManagerPrivate.getNewSideloads()`, `sideloaded.sort()`, `this._updateNotifications()`, `this.sideloaded.add()`
- 条件付き依存: `if (!this.sideloadListener)` → `lazy.AddonManager.addAddonListener()`
- 参照: `b.id`, `sideloaded.length`, `this.sideloadListener`

## onEnabled()
- 位置: L102-114
- 役割: 未承認の一覧にあるアドオンが有効化されたら一覧から外して通知を更新する。一覧が空になったらリスナーを外す。
- 触るとき: サイドロードを承認した後も通知が消えないときに見る。
- 呼び出し先: `this._updateNotifications()`, `this.sideloaded.delete()`, `this.sideloaded.has()`
- 条件付き依存: `if (this.sideloaded.size == 0)` → `lazy.AddonManager.removeAddonListener()`
- 参照: `this.sideloadListener`, `this.sideloaded.size`

## _updateNotifications()
- 位置: L125-135
- 役割: 取り込み待ち・サイドロード待ち・更新待ちが 0 件なら addon-alert 通知を消し、1 件でもあればバッジ通知を出す。最後に change イベントを発火する。
- 触るとき: アドオン通知のバッジが出る・消える条件を変えるときに見る。
- 呼び出し先: `this.emit()`
- 条件付き依存: `if (importedAddonIDs.length + sideloaded.size + updates.size == 0)` → `lazy.AppMenuNotifications.removeNotification()`
- 条件付き依存: `if (!(importedAddonIDs.length + sideloaded.size + updates.size == 0))` → `lazy.AppMenuNotifications.showBadgeOnlyNotification()`
- 参照: `importedAddonIDs.length`, `lazy.AMBrowserExtensionsImport`, `sideloaded.size`, `updates.size`

## showAddonsManager()
- 位置: L137-158
- 役割: アドオン管理画面を開き、その browser 上で権限確認(showPermissionsPrompt)を出す。
- 触るとき: 権限確認をアドオン管理画面の中で表示する経路を追うときに見る。
- 呼び出し先: `global.BrowserAddonUI.openAddonsMgr()`, `global.BrowserAddonUI.openAddonsMgr("addons://list/extension").then()`, `this.showPermissionsPrompt()`
- 参照: `aomWin.docShell.chromeEventHandler`, `tabbrowser.selectedBrowser.documentGlobal`

## showSideloaded()
- 位置: L160-188
- 役割: サイドロードのアドオンを既読にして未承認の一覧から外し、権限確認を出す。承認されたら有効化して通知を更新し、sideload-response を発火する。
- 触るとき: サイドロードの承認の流れや計測の項目を変えるときに見る。
- 呼び出し先: `addon.markAsSeen()`, `lazy.AMTelemetry.recordManageEvent()`, `this._buildStrings()`, `this._updateNotifications()`, `this.emit()`, `this.showAddonsManager()`, `this.sideloaded.delete()`
- 条件付き依存: `if (answer)` → `addon.enable()`
- 条件付き依存: `if (answer)` → `this._updateNotifications()`
- 参照: `addon.iconURL`, `addon.installPermissions`, `lazy.dataCollectionPermissionsEnabled`, `strings.msgs.length`

## showUpdate()
- 位置: L190-209
- 役割: アップデートの権限確認を出す。承認なら resolve、拒否なら reject し、更新待ちの一覧から外して通知を更新する。
- 触るとき: アップデートの権限確認の結果をどう扱うかを変えるときに見る。(次回の更新確認で再び出る点に注意)
- 呼び出し先: `lazy.AMTelemetry.recordInstallEvent()`, `this._updateNotifications()`, `this.showAddonsManager()`, `this.showAddonsManager(browser, info.strings, info.addon.iconURL).then()`, `this.updates.delete()`
- 条件付き依存: `if (answer)` → `info.resolve()`
- 条件付き依存: `if (!(answer))` → `info.reject()`
- 参照: `info.addon.iconURL`, `info.install`, `info.strings`, `info.strings.msgs.length`

## observe()
- 位置: L211-404
- 役割: 拡張の通知トピックごとに振り分ける。権限要求では進行中の通知を消し、未署名なら警告アイコンにし、文言を作って確認を出す。更新は表示する権限がなければそのまま適用し、あれば待ち一覧に入れる。インストール通知、任意権限、既定検索の確認、インポート関連の変化もそれぞれ処理する。
- 触るとき: 拡張のインストール・更新・任意権限・既定検索の確認のどれかが出ないときに、対応するトピックの分岐を見る。
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `getTabBrowser()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `window.PopupNotifications.getNotification()`
- 条件付き依存: `if (progressNotification)` → `progressNotification.remove()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( info.unsigned && (Cu.isInAutomation || !AppConstants.MOZILLA_OFFICIAL) && Services.prefs.getBoolPref( "extensions.ui.disableUnsignedWarnings", false ) )` → `lazy.logConsole.warn()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `this._buildStrings()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `console.error()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `info.reject()`
- 条件付き依存: `if ( info.type == "update" && !strings.msgs.length && !strings.dataCollectionPermissions?.msg )` → `info.resolve()`
- 条件付き依存: `if (info.type == "sideload")` → `lazy.AMTelemetry.recordManageEvent()`
- 条件付き依存: `if (!(info.type == "sideload"))` → `lazy.AMTelemetry.recordInstallEvent()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `this.showPermissionsPrompt()`
- 条件付き依存: `if (answer)` → `info.resolve()`
- 条件付き依存: `if (!(answer))` → `info.reject()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `this._buildStrings()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `console.error()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `info.reject()`
- 条件付き依存: `if (!strings.msgs.length && !strings.dataCollectionPermissions?.msg)` → `info.resolve()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `this.updates.add()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `this._updateNotifications()`
- 条件付き依存: `if (topic == "webextension-install-notify")` → `this.showInstallNotification(target, addon).then()`
- 条件付き依存: `if (topic == "webextension-install-notify")` → `this.showInstallNotification()`
- 条件付き依存: `if (callback)` → `callback()`
- 条件付き依存: `if (topic == "webextension-optional-permission-prompt")` → `this._buildStrings()`
- 条件付き依存: `if (!strings.msgs.length && !strings.dataCollectionPermissions?.msg)` → `resolve()`
- 条件付き依存: `if (topic == "webextension-optional-permission-prompt")` → `resolve()`
- 条件付き依存: `if (topic == "webextension-optional-permission-prompt")` → `this.showPermissionsPrompt()`
- 条件付き依存: `if (topic == "webextension-defaultsearch-prompt")` → `lazy.l10n.formatMessagesSync()`
- 条件付き依存: `if (topic == "webextension-defaultsearch-prompt")` → `this.showDefaultSearchPrompt(browser, strings, icon).then()`
- 条件付き依存: `if (topic == "webextension-defaultsearch-prompt")` → `this.showDefaultSearchPrompt()`
- 条件付き依存: `if ( [ "webextension-imported-addons-cancelled", "webextension-imported-addons-complete", "webextension-imported-addons-pending", ].includes(topic) )` → `this._updateNotifications()`
- 参照: `AppConstants.MOZILLA_OFFICIAL`, `Cu.isInAutomation`, `attr.name`, `attr.value`, `info.addon`, `info.addon.id`, `info.addon.signedState`, `info.icon`, `info.install`, `info.permissions`, `info.reject`, `info.resolve`, `info.type`, `info.unsigned`, `lazy.AddonManager.SIGNEDSTATE_MISSING`, `lazy.dataCollectionPermissionsEnabled`, `permissions.permissions`, `permissions.permissions.length`, `searchDesc.value`, `searchNo.attributes`, `searchYes.attributes`, `strings.acceptKey`, `strings.acceptText`, `strings.cancelKey`, `strings.cancelText`, `strings.dataCollectionPermissions?.msg`, `strings.msgs.length`, `subject.wrappedJSObject`
- XPCOM: `Services.prefs`

## _buildStrings()
- 位置: L407-418
- 役割: ExtensionData.formatPermissionStrings で権限の文言を作り、アドオン名を加える。文言が作れなければ例外を投げる。
- 触るとき: 権限ダイアログの文言やアドオン名の表示がずれるときに見る。
- 呼び出し先: `lazy.ExtensionData.formatPermissionStrings()`
- 参照: `info.addon.name`, `strings.addonName`

## showPermissionsPrompt()
- 位置: async L420-630
- 役割: 権限確認のポップアップを出す。プライベートブラウズ許可とデータ収集のチェックボックスの既定値を既存設定から決め、承認か拒否で resolve する。チェックボックスの値は承認後に ExtensionPermissions へ add または remove で反映する。同じ browser の先行する確認が終わるまで待つ。
- 触るとき: 権限確認の表示内容、チェックボックスの既定値、または承認後の権限の書き込みを変えるときに見る。
- 呼び出し先: `Promise.all()`, `Promise.all(promises).then()`, `Services.urlFormatter.formatURLPref()`, `browser.documentGlobal.gUnifiedExtensions.getPopupAnchorID()`, `getTabBrowser()`, `lazy.AddonManager.getAddonByID()`, `lazy.ExtensionPermissions.remove()`, `lazy.ExtensionPermissions.remove(addon.id, perms).catch()`, `lazy.logConsole.warn()`, `permsToUpdate.map()`, `promise.finally()`, `promise.then()`, `strings.header.includes()`, `this.pendingNotifications.delete()`, `this.pendingNotifications.get()`, `this.pendingNotifications.set()`, `window.PopupNotifications.show()`
- 条件付き依存: `if ( showIncognitoCheckbox && // Usually false, unless the user tries to install a XPI file whose ID // matches an already-installed add-on. (await lazy.AddonMan...)` → `lazy.ExtensionPermissions.get()`
- 条件付き依存: `if ( showIncognitoCheckbox && // Usually false, unless the user tries to install a XPI file whose ID // matches an already-installed add-on. (await lazy.AddonMan...)` → `permissions.includes()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `permsToUpdate.push()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `permsToUpdate.push()`
- 条件付き依存: `if (value)` → `lazy.ExtensionPermissions.add(addon.id, perms).catch()`
- 条件付き依存: `if (value)` → `lazy.ExtensionPermissions.add()`
- 条件付き依存: `if (value)` → `lazy.logConsole.warn()`
- 参照: `addon.id`, `addon.permissions`, `lazy.AddonManager.PERM_CAN_CHANGE_PRIVATEBROWSING_ACCESS`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `options.name`, `strings.acceptKey`, `strings.acceptText`, `strings.addonName`, `strings.cancelKey`, `strings.cancelText`, `strings.dataCollectionPermissions?.collectsTechnicalAndInteractionData`, `strings.dataCollectionPermissions?.msg`, `strings.header`, `strings.msgs.length`
- XPCOM: `Services.urlFormatter`

## eventCallback()
- 位置: L471-481
- 役割: swapping の間は通知を残し、removed になったら非同期に拒否として resolve する。
- 触るとき: タブの入れ替え時に確認が消える、または残る理由を追うときに見る。
- 条件付き依存: `if (topic == "removed")` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (topic == "removed")` → `resolve()`
- XPCOM: `Services.tm`

## onPrivateBrowsingAllowedChanged()
- 位置: L519-521
- 役割: プライベートブラウズ許可のチェックボックスの値を保持する。
- 触るとき: プライベートブラウズ許可の選択が承認時に反映されない原因を調べるときに見る。

## onTechnicalAndInteractionDataChanged()
- 位置: L524-526
- 役割: データ収集(技術・操作データ)のチェックボックスの値を保持する。
- 触るとき: データ収集の選択が承認時に反映されない原因を調べるときに見る。

## callback()
- 位置: L548-550
- 役割: 承認ボタンで resolve(true) する。
- 触るとき: 権限確認の承認ボタンの扱いを変えるときに見る。
- 呼び出し先: `resolve()`

## callback()
- 位置: L556-558
- 役割: 拒否ボタンで resolve(false) する。
- 触るとき: 権限確認の拒否ボタンの扱いを変えるときに見る。
- 呼び出し先: `resolve()`

## showDefaultSearchPrompt()
- 位置: L632-676
- 役割: 既定検索エンジンを変える確認を出す。承認なら true、閉じられたら false で resolve する。
- 触るとき: 既定検索の変更確認の表示や結果の扱いを変えるときに見る。
- 呼び出し先: `getTabBrowser()`, `window.PopupNotifications.show()`
- 参照: `strings.acceptKey`, `strings.acceptText`, `strings.addonName`, `strings.cancelKey`, `strings.cancelText`, `strings.text`

## eventCallback()
- 位置: L639-643
- 役割: 通知が removed になったら false で resolve する。
- 触るとき: 既定検索の確認を閉じた後に変更が行われないことを確かめるときに見る。
- 条件付き依存: `if (topic == "removed")` → `resolve()`

## callback()
- 位置: L650-652
- 役割: 承認ボタンで resolve(true) する。
- 触るとき: 既定検索の承認ボタンの動作を変えるときに見る。
- 呼び出し先: `resolve()`

## callback()
- 位置: L658-660
- 役割: 拒否ボタンで resolve(false) する。
- 触るとき: 既定検索の拒否ボタンの動作を変えるときに見る。
- 呼び出し先: `resolve()`

## showInstallNotification()
- 位置: async L678-760
- 役割: インストール完了の通知を出す。テーマは直前のテーマへ戻す取り消しボタン付きで出し、それ以外は addonId を渡して出す。閉じられたら resolve する。
- 触るとき: インストール後の通知の表示内容やテーマの取り消しの挙動を変えるときに見る。
- 呼び出し先: `getTabBrowser()`, `lazy.AddonManager.getPreferredIconURL()`, `lazy.l10n.formatValue()`
- 条件付き依存: `if (addon.type == "theme")` → `lazy.AppMenuNotifications.showNotification()`
- 条件付き依存: `if (!(addon.type == "theme"))` → `lazy.AppMenuNotifications.showNotification()`
- 参照: `addon.id`, `addon.isWebExtension`, `addon.name`, `addon.type`

## themeActionUndo()
- 位置: async L694-711
- 役割: 直前に有効だったテーマを有効化し、今インストールしたテーマを削除する。終わったら resolve する。
- 触るとき: テーマ導入の取り消しで元のテーマに戻らないときに見る。
- 呼び出し先: `addon.uninstall()`, `lazy.AddonManager.getAddonByID()`, `resolve()`
- 条件付き依存: `if (theme)` → `theme.enable()`

## onDismissed()
- 位置: L724-727
- 役割: テーマの通知が閉じられたら通知を消して resolve する。
- 触るとき: テーマ通知を閉じた後の後始末を変えるときに見る。
- 呼び出し先: `lazy.AppMenuNotifications.removeNotification()`, `resolve()`

## onDismissed()
- 位置: L744-747
- 役割: インストールの通知が閉じられたら通知を消して resolve する。
- 触るとき: インストール通知を閉じた後の後始末を変えるときに見る。
- 呼び出し先: `lazy.AppMenuNotifications.removeNotification()`, `resolve()`

## showQuarantineConfirmation()
- 位置: async L762-792
- 役割: 隔離された拡張を許可するかの確認を出し、承認なら許可の pref を立てる。
- 触るとき: 隔離された拡張の許可がどこに保存されるかを追うときに見る。
- 呼び出し先: `ExtensionsUI.showPermissionsPrompt()`, `attr()`, `lazy.l10n.formatMessages()`, `policy.extension?.getPreferredIcon()`
- 条件付き依存: `if (await ExtensionsUI.showPermissionsPrompt(browser, strings, icon))` → `lazy.QuarantinedDomains.setUserAllowedAddonIdPref()`
- 参照: `line1.value`, `line2.value`, `policy.id`, `policy.name`, `title.value`

## attr()
- 位置: L774-774
- 役割: Fluent メッセージから指定した名前の属性の値を取り出す小さな関数。
- 触るとき: 確認文言の label や accesskey が空になるときに見る。
- 呼び出し先: `msg.attributes.find()`
- 参照: `a.name`, `msg.attributes.find(a => a.name === name)?.value`

## originControlsMenu()
- 位置: L795-886
- 役割: 拡張のツールバーのメニューに、サイトへのアクセス設定の項目を挿入する。隔離されておらず origin controls もない拡張では何もしない。
- 触るとき: 拡張のサイトアクセス設定の項目を追加・変更するとき、または項目が出ない理由を調べるときに見る。
- 呼び出し先: `WebExtensionPolicy.getByID()`, `doc.createXULElement()`, `headerItem.setAttribute()`, `items.forEach()`, `items.push()`, `lazy.OriginControls.getState()`, `popup.addEventListener()`, `popup.insertBefore()`, `popup.querySelector()`
- 条件付き依存: `if (state.noAccess)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(state.noAccess))` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.quarantined)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.quarantined)` → `doc.createXULElement()`
- 条件付き依存: `if (state.quarantined)` → `allowQuarantined.addEventListener()`
- 条件付き依存: `if (state.quarantined)` → `this.showQuarantineConfirmation()`
- 条件付き依存: `if (state.quarantined)` → `items.push()`
- 条件付き依存: `if (state.allDomains)` → `doc.createXULElement()`
- 条件付き依存: `if (state.allDomains)` → `allDomains.setAttribute()`
- 条件付き依存: `if (state.allDomains)` → `allDomains.toggleAttribute()`
- 条件付き依存: `if (state.allDomains)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.allDomains)` → `items.push()`
- 条件付き依存: `if (state.whenClicked)` → `doc.createXULElement()`
- 条件付き依存: `if (state.whenClicked)` → `whenClicked.setAttribute()`
- 条件付き依存: `if (state.whenClicked)` → `whenClicked.toggleAttribute()`
- 条件付き依存: `if (state.whenClicked)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.whenClicked)` → `whenClicked.addEventListener()`
- 条件付き依存: `if (state.whenClicked)` → `lazy.OriginControls.setWhenClicked()`
- 条件付き依存: `if (state.whenClicked)` → `win.gUnifiedExtensions.updateAttention()`
- 条件付き依存: `if (state.whenClicked)` → `items.push()`
- 条件付き依存: `if (state.alwaysOn)` → `doc.createXULElement()`
- 条件付き依存: `if (state.alwaysOn)` → `alwaysOn.setAttribute()`
- 条件付き依存: `if (state.alwaysOn)` → `alwaysOn.toggleAttribute()`
- 条件付き依存: `if (state.alwaysOn)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.alwaysOn)` → `alwaysOn.addEventListener()`
- 条件付き依存: `if (state.alwaysOn)` → `lazy.OriginControls.setAlwaysOn()`
- 条件付き依存: `if (state.alwaysOn)` → `win.gUnifiedExtensions.updateAttention()`
- 条件付き依存: `if (state.alwaysOn)` → `items.push()`
- 参照: `policy?.extension.originControls`, `popup.documentGlobal`, `popup.ownerDocument`, `state.allDomains`, `state.alwaysOn`, `state.hasAccess`, `state.noAccess`, `state.quarantined`, `state.whenClicked`, `tab.linkedBrowser`, `tab.linkedBrowser?.currentURI`, `uri.host`, `win.gBrowser.selectedTab`

## cleanup()
- 位置: L879-884
- 役割: メニューが閉じたとき、挿入した項目を取り除き、自身の popuphidden リスナーを外す。
- 触るとき: メニューに同じ項目が重複して残るときに見る。
- 条件付き依存: `if (e.target === popup)` → `items.forEach()`
- 条件付き依存: `if (e.target === popup)` → `item?.remove()`
- 条件付き依存: `if (e.target === popup)` → `popup.removeEventListener()`
- 参照: `e.target`
