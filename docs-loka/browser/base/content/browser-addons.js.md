# browser/base/content/browser-addons.js

source: browser/base/content/browser-addons.js
source-hash: d380089ca59a0728e9378503934b4c6c0432b8af
lines: 3406

## <module>
- 役割: 拡張機能まわりの UI(権限・インストール確認と進捗・ブロックリスト表示・拡張ボタンとパネル・about:addons 連携)を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `customElements.define()`, `customElements.get()`

## MozAddonNotificationBlocklistURL.connectedCallback()
- 位置: L108-110
- 役割: ブロックリスト案内リンクに click リスナを付ける。
- 触るとき: ブロックリスト案内リンクの有効化タイミングを変えるとき。
- 呼び出し先: `this.addEventListener()`

## MozAddonNotificationBlocklistURL.disconnectedCallback()
- 位置: L112-114
- 役割: ブロックリスト案内リンクの click リスナを外す。
- 触るとき: 要素が DOM から外れた時の後始末を変えるとき。
- 呼び出し先: `this.removeEventListener()`

## MozAddonNotificationBlocklistURL.handleEvent()
- 位置: L116-125
- 役割: リンクの既定動作を止め、ブロックリストの URL を前面のタブで開く。
- 触るとき: ブロックリスト案内リンクの開き方を変えるとき。
- 条件付き依存: `if (e.type == "click")` → `e.preventDefault()`
- 条件付き依存: `if (e.type == "click")` → `window.openTrustedLinkIn()`
- 参照: `e.type`, `this.href`

## MozAddonPermissionsNotification.show()
- 位置: L135-168
- 役割: 権限要求通知の子要素を取得し、customElementOptions が無ければ例外にして描画する。
- 触るとき: 権限要求通知の初期化や必須オプションを変えるとき。
- 呼び出し先: `super.show()`, `this.querySelector()`, `this.render()`
- 参照: `this.introEl`, `this.notification`, `this.notification.options?.customElementOptions`, `this.permsListDataCollectionEl`, `this.permsListEl`, `this.permsListOptionalEl`, `this.permsTitleDataCollectionEl`, `this.permsTitleEl`, `this.permsTitleOptionalEl`, `this.textEl`

## MozAddonPermissionsNotification.hasNoPermissions()
- 位置: L170-183
- 役割: 表示すべき権限文言もチェックボックスも無いかを判定する。
- 触るとき: 権限一覧を省くべき条件を変えるとき。
- 参照: `strings.msgs.length`, `this.#dataCollectionPermissions?.msg`, `this.notification.options.customElementOptions`

## MozAddonPermissionsNotification.domainsSet()
- 位置: L185-191
- 役割: fullDomainsList が持つドメイン集合を返す。
- 触るとき: ドメイン一覧表示の元データを調べるとき。
- 参照: `strings.fullDomainsList?.domainsSet`, `this.notification.options.customElementOptions`, `this.notification?.options?.customElementOptions`

## MozAddonPermissionsNotification.hasFullDomainsList()
- 位置: L193-195
- 役割: ドメイン集合が空でないかを返す。
- 触るとき: ドメイン一覧を展開して表示するかの判定を変えるとき。
- 参照: `this.domainsSet?.size`

## MozAddonPermissionsNotification.#isFullDomainsListEntryIndex()
- 位置: L197-203
- 役割: 権限文言の idx 番目がドメイン一覧の項目かを判定する。
- 触るとき: どの権限文言をドメイン一覧に置き換えるかを変えるとき。
- 参照: `strings.fullDomainsList.msgIdIndex`, `this.hasFullDomainsList`, `this.notification.options.customElementOptions`

## MozAddonPermissionsNotification.#dataCollectionPermissions()
- 位置: L209-215
- 役割: customElementOptions からデータ収集権限の情報を取り出す。
- 触るとき: データ収集権限の表示データの受け渡しを変えるとき。
- 参照: `strings.dataCollectionPermissions`, `this.notification.options.customElementOptions`, `this.notification?.options?.customElementOptions`

## MozAddonPermissionsNotification.render()
- 位置: L217-354
- 役割: 必須・データ収集・任意の各節に権限文言を並べ、userScripts 要求では許可ボタンを一度無効にする。
- 触るとき: 権限要求ダイアログの内容や並び、userScripts の確認手順を変えるとき。
- 呼び出し先: `this.#clearChildElements()`, `this.#setAllowButtonEnabled()`
- 条件付き依存: `if (strings.text)` → `strings.text.includes()`
- 条件付き依存: `if (strings.text.includes("\n\n"))` → `textEl.classList.add()`
- 条件付き依存: `if (isUserScriptsRequest)` → `this.#createUserScriptsPermissionItems()`
- 条件付き依存: `if (isUserScriptsRequest)` → `this.#setAllowButtonEnabled()`
- 条件付き依存: `if (isUserScriptsRequest)` → `doc.createElementNS()`
- 条件付き依存: `if (isUserScriptsRequest)` → `item.append()`
- 条件付き依存: `if (isUserScriptsRequest)` → `item.classList.add()`
- 条件付き依存: `if (isUserScriptsRequest)` → `permsListEl.append()`
- 条件付き依存: `if (strings.msgs.length)` → `strings.msgs.entries()`
- 条件付き依存: `if (strings.msgs.length)` → `doc.createElementNS()`
- 条件付き依存: `if (strings.msgs.length)` → `item.classList.add()`
- 条件付き依存: `if (strings.msgs.length)` → `this.#isFullDomainsListEntryIndex()`
- 条件付き依存: `if ( this.hasFullDomainsList && this.#isFullDomainsListEntryIndex(idx) )` → `item.append()`
- 条件付き依存: `if ( this.hasFullDomainsList && this.#isFullDomainsListEntryIndex(idx) )` → `this.#createFullDomainsListFragment()`
- 条件付き依存: `if (strings.msgs.length)` → `permsListEl.appendChild()`
- 条件付き依存: `if (this.#dataCollectionPermissions?.msg)` → `doc.createElementNS()`
- 条件付き依存: `if (this.#dataCollectionPermissions?.msg)` → `item.classList.add()`
- 条件付き依存: `if (this.#dataCollectionPermissions?.msg)` → `permsListDataCollectionEl.appendChild()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `doc.createElementNS()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `item.classList.add()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `item.appendChild()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `this.#createTechnicalAndInteractionDataCheckbox()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `permsListOptionalEl.appendChild()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `doc.createElementNS()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `item.classList.add()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `item.appendChild()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `this.#createPrivateBrowsingCheckbox()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `permsListOptionalEl.appendChild()`
- 参照: `introEl.hidden`, `introEl.textContent`, `item.textContent`, `permsListDataCollectionEl.hidden`, `permsListEl.hidden`, `permsListOptionalEl.hidden`, `permsTitleDataCollectionEl.hidden`, `permsTitleDataCollectionEl.textContent`, `permsTitleEl.hidden`, `permsTitleEl.textContent`, `permsTitleOptionalEl.hidden`, `permsTitleOptionalEl.textContent`, `strings.listIntro`, `strings.msgs`, `strings.msgs.length`, `strings.sectionHeaders`, `strings.text`, `textEl.hidden`, `textEl.textContent`, `this.#dataCollectionPermissions.msg`, `this.#dataCollectionPermissions?.msg`, `this.hasFullDomainsList`, `this.hasNoPermissions`, `this.notification.options.customElementOptions`, `this.ownerDocument`

## MozAddonPermissionsNotification.#createFullDomainsListFragment()
- 位置: L356-380
- 役割: ドメイン一覧の ul を作り、5件を超えるとスクロール可能にしてフラグメントで返す。
- 触るとき: ドメイン一覧の見た目や件数の閾値を変えるとき。
- 呼び出し先: `doc.createElementNS()`, `doc.createXULElement()`, `domainsList.appendChild()`, `domainsList.classList.add()`, `fragment.append()`
- 条件付き依存: `if (this.domainsSet.size > 5)` → `domainsList.classList.add()`
- 参照: `domainItem.textContent`, `label.value`, `this.documentGlobal`, `this.domainsSet`, `this.domainsSet.size`, `this.ownerDocument`

## MozAddonPermissionsNotification.#clearChildElements()
- 位置: L382-419
- 役割: 前回の描画で入れた文言と一覧を空にし、見出しと一覧を隠す。
- 触るとき: 同じ通知を描き直す時の初期化内容を変えるとき。
- 呼び出し先: `textEl.classList.remove()`
- 参照: `introEl.hidden`, `introEl.textContent`, `list.hidden`, `list.textContent`, `textEl.hidden`, `textEl.textContent`, `title.hidden`

## MozAddonPermissionsNotification.#createUserScriptsPermissionItems()
- 位置: L421-440
- 役割: userScripts 権限の確認チェックボックスと警告バーを作り、返す。
- 触るとき: userScripts 権限の確認 UI を変えるとき。
- 呼び出し先: `checkboxEl.addEventListener()`, `lazy.PERMISSION_L10N.formatValueSync()`, `this.#setAllowButtonEnabled()`, `this.ownerDocument.createElement()`, `warningEl.setAttribute()`
- 参照: `checkboxEl.checked`, `checkboxEl.label`

## MozAddonPermissionsNotification.#setAllowButtonEnabled()
- 位置: L442-460
- 役割: 許可ボタンの無効状態を mainactiondisabled と invalidselection の両属性で揃える。
- 触るとき: 許可ボタンの有効化条件や PopupNotifications との競合を扱うとき。
- 呼び出し先: `this.toggleAttribute()`

## MozAddonPermissionsNotification.#createPrivateBrowsingCheckbox()
- 位置: L462-482
- 役割: プライベートブラウズ許可のチェックボックスを作り、変更を通知先へ渡す。
- 触るとき: プライベートブラウズ許可の初期値や変更の扱いを変えるとき。
- 呼び出し先: `checkboxEl.addEventListener()`, `onPrivateBrowsingAllowedChanged()`, `this.ownerDocument.createElement()`, `this.ownerDocument.l10n.setAttributes()`
- 参照: `checkboxEl.checked`, `this.notification.options.customElementOptions`

## MozAddonPermissionsNotification.#createTechnicalAndInteractionDataCheckbox()
- 位置: L484-505
- 役割: 技術・操作データ収集の任意許可チェックボックスを作り、変更を通知先へ渡す。
- 触るとき: 技術・操作データ収集の許可 UI を変えるとき。
- 呼び出し先: `checkboxEl.addEventListener()`, `onTechnicalAndInteractionDataChanged()`, `this.ownerDocument.createElement()`, `this.ownerDocument.l10n.setAttributes()`
- 参照: `checkboxEl.checked`, `this.notification.options.customElementOptions`

## MozAddonProgressNotification.show()
- 位置: L515-543
- 役割: 進捗要素を取得し、各インストールに listener を付けて初期進捗と定期更新を始める。
- 触るとき: インストール進捗表示の開始処理を変えるとき。
- 呼び出し先: `aInstall.addListener()`, `document.getElementById()`, `setTimeout()`, `super.show()`, `this.notification.options.installs.forEach()`, `this.setProgress()`, `this.updateProgress.bind()`
- 参照: `this._updateProgressTimeout`, `this.notification`, `this.progressmeter`, `this.progresstext`

## MozAddonProgressNotification.disconnectedCallback()
- 位置: L545-547
- 役割: DOM から外れた時に destroy を呼ぶ。
- 触るとき: 進捗通知の後始末の呼び出し経路を調べるとき。
- 呼び出し先: `this.destroy()`

## MozAddonProgressNotification.destroy()
- 位置: L549-558
- 役割: 各インストールの listener を外し、保留中の更新タイマーを止める。
- 触るとき: 進捗通知を終了する処理を変えるとき。
- 呼び出し先: `aInstall.removeListener()`, `clearTimeout()`, `this.notification.options.installs.forEach()`
- 参照: `this._updateProgressTimeout`, `this.notification`

## MozAddonProgressNotification.setProgress()
- 位置: L560-606
- 役割: 進捗メーターを更新し、400ms 以上の間隔で速度を平滑化して残り時間の文言を出す。
- 触るとき: ダウンロード速度や残り時間の表示計算を変えるとき。
- 呼び出し先: `Date.now()`, `DownloadUtils.getDownloadStatus()`, `Math.max()`, `this.progresstext.setAttribute()`
- 条件付き依存: `if (aMaxProgress == -1)` → `this.progressmeter.removeAttribute()`
- 条件付き依存: `if (!(aMaxProgress == -1))` → `this.progressmeter.setAttribute()`
- 参照: `this.notification.last`, `this.notification.lastProgress`, `this.notification.lastUpdate`, `this.notification.speed`

## MozAddonProgressNotification.cancel()
- 位置: L608-619
- 役割: 全インストールをキャンセルし、進捗通知を削除する。
- 触るとき: 進捗通知のキャンセル操作を変えるとき。
- 呼び出し先: `PopupNotifications.remove()`, `aInstall.cancel()`, `installs.forEach()`
- 参照: `this.notification`, `this.notification.options.installs`

## MozAddonProgressNotification.updateProgress()
- 位置: L621-652
- 役割: 全インストールの進捗と最大値を合算し、全件完了なら検証中の表示に切り替える。
- 触るとき: 複数インストールの進捗集計を変えるとき。
- 呼び出し先: `this.notification.options.installs.forEach()`
- 条件付き依存: `if (downloadingCount == 0)` → `this.destroy()`
- 条件付き依存: `if (downloadingCount == 0)` → `this.progressmeter.removeAttribute()`
- 条件付き依存: `if (downloadingCount == 0)` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if (downloadingCount == 0)` → `this.progresstext.setAttribute()`
- 条件付き依存: `if (!(downloadingCount == 0))` → `this.setProgress()`
- 参照: `AddonManager.STATE_DOWNLOADED`, `aInstall.maxProgress`, `aInstall.progress`, `aInstall.state`, `this.notification`

## MozAddonProgressNotification.onDownloadProgress()
- 位置: L654-656
- 役割: ダウンロード進捗の通知を受けて updateProgress を呼ぶ。
- 触るとき: 進捗の再計算の契機を変えるとき。
- 呼び出し先: `this.updateProgress()`

## MozAddonProgressNotification.onDownloadFailed()
- 位置: L658-660
- 役割: ダウンロード失敗の通知を受けて updateProgress を呼ぶ。
- 触るとき: 失敗時の進捗表示を変えるとき。
- 呼び出し先: `this.updateProgress()`

## MozAddonProgressNotification.onDownloadCancelled()
- 位置: L662-664
- 役割: ダウンロードキャンセルの通知を受けて updateProgress を呼ぶ。
- 触るとき: キャンセル時の進捗表示を変えるとき。
- 呼び出し先: `this.updateProgress()`

## MozAddonProgressNotification.onDownloadEnded()
- 位置: L666-668
- 役割: ダウンロード完了の通知を受けて updateProgress を呼ぶ。
- 触るとき: 完了時の進捗表示を変えるとき。
- 呼び出し先: `this.updateProgress()`

## extensionPolicy()
- 位置: L678-680
- 役割: 要素の拡張 ID から WebExtensionPolicy を引く。
- 触るとき: 拡張のメッセージバーがどの拡張を指すかを調べるとき。
- 呼び出し先: `WebExtensionPolicy.getByID()`
- 参照: `this.extensionId`

## extensionName()
- 位置: L682-684
- 役割: 拡張ポリシーから拡張名を返す。
- 触るとき: 拡張名の表示元を変えるとき。
- 参照: `this.extensionPolicy?.name`

## isSoftBlocked()
- 位置: L686-688
- 役割: 拡張がソフトブロックされているかを返す。
- 触るとき: ソフトブロックの判定元を調べるとき。
- 参照: `this.extensionPolicy?.extension?.isSoftBlocked`

## connectedCallback()
- 位置: L690-695
- 役割: moz-message-bar を作って要素の子に入れ、表示を更新する。
- 触るとき: 拡張パネル内のメッセージバーの生成タイミングを変えるとき。
- 呼び出し先: `document.createElement()`, `this.append()`, `this.messagebar.classList.add()`, `this.refresh()`
- 参照: `this.messagebar`

## disconnectedCallback()
- 位置: L697-699
- 役割: メッセージバーを DOM から取り除く。
- 触るとき: メッセージバーの後始末を変えるとき。
- 呼び出し先: `this.messagebar?.remove()`

## refresh()
- 位置: async L701-738
- 役割: ソフトブロック時は警告文言を設定して表示し、そうでなければ隠す。非同期で moz-message-bar の定義を待つ。
- 触るとき: 拡張のソフトブロック表示の文言や条件を変えるとき。
- 呼び出し先: `customElements.get()`, `messagebar.requestUpdate()`
- 条件付き依存: `if (!customElements.get("moz-message-bar"))` → `document.createElement()`
- 条件付き依存: `if (!customElements.get("moz-message-bar"))` → `customElements.whenDefined()`
- 条件付き依存: `if (this.isSoftBlocked)` → `messagebar.removeAttribute()`
- 条件付き依存: `if (this.isSoftBlocked)` → `messagebar.setAttribute()`
- 条件付き依存: `if (!(this.isSoftBlocked))` → `messagebar.hasAttribute()`
- 条件付き依存: `if (!(this.isSoftBlocked))` → `messagebar.setAttribute()`
- 参照: `messagebar.messageL10nArgs`, `messagebar.messageL10nArgs?.extensionName`, `messagebar.messageL10nId`, `this.extensionName`, `this.isSoftBlocked`, `this.messagebar`

## BrowserActionWidgetObserver.constructor()
- 位置: L750-756
- 役割: 拡張 ID からブラウザアクションのウィジェット ID を作って保持する。
- 触るとき: ブラウザアクションのウィジェット ID の作り方を変えるとき(ext-browserAction.js と揃える必要がある)。
- 呼び出し先: `lazy.ExtensionCommon.makeWidgetId()`
- 参照: `this.addonId`, `this.onButtonAreaChanged`, `this.widgetId`

## BrowserActionWidgetObserver.startObserving()
- 位置: L758-765
- 役割: CustomizableUI のリスナと unload 監視を登録する。二重登録はしない。
- 触るとき: ウィジェット監視の開始条件を変えるとき。
- 呼び出し先: `CustomizableUI.addListener()`, `window.addEventListener()`
- 参照: `this.#connected`

## BrowserActionWidgetObserver.stopObserving()
- 位置: L767-774
- 役割: CustomizableUI のリスナと unload 監視を外す。
- 触るとき: ウィジェット監視の終了処理を変えるとき。
- 呼び出し先: `CustomizableUI.removeListener()`, `window.removeEventListener()`
- 参照: `this.#connected`

## BrowserActionWidgetObserver.hasBrowserActionUI()
- 位置: L776-788
- 役割: この窓で拡張がアクセスでき、ブラウザアクションを持つかを返す。
- 触るとき: ピン留めチェックボックスを出す条件を変えるとき。
- 呼び出し先: `WebExtensionPolicy.getByID()`, `gUnifiedExtensions.browserActionFor()`, `policy?.canAccessWindow()`
- 参照: `this.addonId`

## BrowserActionWidgetObserver.onWidgetCreated()
- 位置: L790-797
- 役割: 対象のウィジェットが生成された時に変化コールバックを呼ぶ。
- 触るとき: ウィジェット生成時にピン留め欄を描き直す挙動を変えるとき。
- 条件付き依存: `if (aWidgetId === this.widgetId)` → `this.onButtonAreaChanged()`
- 参照: `this.widgetId`

## BrowserActionWidgetObserver.onWidgetAdded()
- 位置: L799-803
- 役割: 対象のウィジェットが追加された時に変化コールバックを呼ぶ。
- 触るとき: ウィジェット追加時の再描画を変えるとき。
- 条件付き依存: `if (aWidgetId === this.widgetId)` → `this.onButtonAreaChanged()`
- 参照: `this.widgetId`

## BrowserActionWidgetObserver.onWidgetMoved()
- 位置: L805-809
- 役割: 対象のウィジェットが移動した時に変化コールバックを呼ぶ。
- 触るとき: ウィジェット移動時の再描画を変えるとき。
- 条件付き依存: `if (aWidgetId === this.widgetId)` → `this.onButtonAreaChanged()`
- 参照: `this.widgetId`

## BrowserActionWidgetObserver.handleEvent()
- 位置: L811-815
- 役割: unload 時に監視を止める。
- 触るとき: ウィンドウ終了時の監視解除を変えるとき。
- 条件付き依存: `if (event.type === "unload")` → `this.stopObserving()`
- 参照: `event.type`

## MozAddonInstalledNotification.connectedCallback()
- 位置: L824-833
- 役割: 説明文とピン留めチェックボックスの要素を取り、クリックと command を監視する。
- 触るとき: インストール完了通知の要素の取得と監視を変えるとき。
- 呼び出し先: `this.#browserActionWidgetObserver?.startObserving()`, `this.addEventListener()`, `this.pinExtensionEl.addEventListener()`, `this.querySelector()`
- 参照: `this.descriptionEl`, `this.pinExtensionEl`

## MozAddonInstalledNotification.disconnectedCallback()
- 位置: L835-839
- 役割: クリックと command の監視を外し、ウィジェット監視を止める。
- 触るとき: インストール完了通知の後始末を変えるとき。
- 呼び出し先: `this.#browserActionWidgetObserver?.stopObserving()`, `this.pinExtensionEl.removeEventListener()`, `this.removeEventListener()`

## MozAddonInstalledNotification.#settingsLinkId()
- 位置: L841-843
- 役割: データ収集設定リンクの要素 ID を返す。
- 触るとき: 設定リンクの ID を変えるとき。

## MozAddonInstalledNotification.handleEvent()
- 位置: L845-871
- 役割: 設定リンクのクリックでアドオン詳細を開き、ピン留めチェックの command を処理する。
- 触るとき: インストール完了通知のクリック動作を変えるとき。
- 条件付き依存: `if (target.id === this.#settingsLinkId)` → `BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (target.id === this.#settingsLinkId)` → `encodeURIComponent()`
- 条件付き依存: `if (target.id === this.#settingsLinkId)` → `event.preventDefault()`
- 条件付き依存: `if (target == this.pinExtensionEl)` → `this.#handlePinnedCheckboxStateChange()`
- 参照: `event.type`, `target.id`, `this.#settingsLinkId`, `this.notification.options.customElementOptions`, `this.pinExtensionEl`

## MozAddonInstalledNotification.show()
- 位置: L873-896
- 役割: ウィジェット監視を作り直して描画し、接続中なら監視を始める。
- 触るとき: インストール完了通知の表示時の初期化を変えるとき。
- 呼び出し先: `super.show()`, `this.#browserActionWidgetObserver?.stopObserving()`, `this.#renderPinToolbarButtonCheckbox()`, `this.render()`
- 条件付き依存: `if (this.isConnected)` → `this.#browserActionWidgetObserver.startObserving()`
- 参照: `this.#browserActionWidgetObserver`, `this.isConnected`, `this.notification`, `this.notification.options.customElementOptions.addonId`, `this.notification.options?.customElementOptions`

## MozAddonInstalledNotification.render()
- 位置: L898-918
- 役割: データ収集の有無に応じて説明文と設定リンクを切り替え、ピン留め欄を描画する。
- 触るとき: インストール完了後の説明文の出し分けを変えるとき。
- 呼び出し先: `this.#renderPinToolbarButtonCheckbox()`, `this.ownerDocument.l10n.setAttributes()`, `this.querySelector()`, `this.querySelector(`#${this.#settingsLinkId}`)?.remove()`
- 条件付き依存: `if (this.#dataCollectionPermissionsEnabled)` → `document.createElementNS()`
- 条件付き依存: `if (this.#dataCollectionPermissionsEnabled)` → `link.setAttribute()`
- 条件付き依存: `if (this.#dataCollectionPermissionsEnabled)` → `this.descriptionEl.append()`
- 参照: `link.href`, `this.#dataCollectionPermissionsEnabled`, `this.#settingsLinkId`, `this.descriptionEl`

## MozAddonInstalledNotification.#dataCollectionPermissionsEnabled()
- 位置: L920-925
- 役割: extensions.dataCollectionPermissions.enabled を読む。
- 触るとき: データ収集権限の機能フラグを参照する箇所を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## MozAddonInstalledNotification.#renderPinToolbarButtonCheckbox()
- 位置: L927-952
- 役割: ブラウザアクションがあり、AREA_ADDONS か AREA_NAVBAR にある時だけピン留めチェックを表示し、状態を反映する。
- 触るとき: ツールバーへのピン留めチェックを出す条件を変えるとき。
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `this.#browserActionWidgetObserver.hasBrowserActionUI()`
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.getPlacementOfWidget(widgetId)?.area`, `this.#browserActionWidgetObserver.widgetId`, `this.pinExtensionEl.checked`, `this.pinExtensionEl.hidden`

## MozAddonInstalledNotification.#handlePinnedCheckboxStateChange()
- 位置: L954-967
- 役割: チェックが入ればツールバーへ移し、外せばパネルへ戻す。
- 触るとき: インストール完了通知からのピン留め操作を変えるとき。
- 呼び出し先: `gUnifiedExtensions.pinToToolbar()`, `this.#browserActionWidgetObserver.hasBrowserActionUI()`
- 条件付き依存: `if (shouldPinToToolbar)` → `gUnifiedExtensions._maybeMoveWidgetNodeBack()`
- 参照: `this.#browserActionWidgetObserver.widgetId`, `this.notification.options.customElementOptions`, `this.pinExtensionEl.checked`

## removeNotificationOnEnd()
- 位置: L974-1000
- 役割: 渡された全インストールが終了したら、まだ表示中ならその通知を削除する。
- 触るとき: インストール通知の寿命や自動消去の条件を変えるとき。
- 呼び出し先: `install.addListener()`
- 参照: `installs.length`

## maybeRemove()
- 位置: L977-990
- 役割: インストール終了のたびに残数を減らし、0 になった時に通知を削除する。
- 触るとき: インストール終了時の通知削除の判定を変えるとき。
- 呼び出し先: `install.removeListener()`
- 条件付き依存: `if (--count == 0)` → `PopupNotifications.getNotification()`
- 条件付き依存: `if (current === notification)` → `notification.remove()`
- 参照: `notification.browser`, `notification.id`

## buildNotificationAction()
- 位置: L1002-1020
- 役割: ラベルとアクセスキーから通知ボタンの定義を作る。disableSecurityDelay を指定できる。
- 触るとき: 通知ボタンの作り方や遅延の扱いを変えるとき。
- 参照: `action.disableSecurityDelay`, `msg.attributes`, `options.disableSecurityDelay`

## showInstallConfirmation()
- 位置: L1025-1208
- 役割: インストール確認の通知を表示し、未署名の有無に応じた文言と承認・拒否の動作を付ける。
- 触るとき: インストール確認ダイアログの内容や承認・拒否の処理を変えるとき。
- 呼び出し先: `Glean.securityUi.events.accumulateSingleSample()`, `PopupNotifications.getNotification()`, `PopupNotifications.show()`, `Services.urlFormatter.formatURLPref()`, `buildNotificationAction()`, `document.getElementById()`, `gBrowser.getTabForBrowser()`, `gUnifiedExtensions.getPopupAnchorID()`, `installInfo.installs.every()`, `installInfo.installs.filter()`, `lazy.l10n.formatMessagesSync()`, `lazy.l10n.formatValueSync()`, `removeNotificationOnEnd()`
- 条件付き依存: `if ( PopupNotifications.getNotification("addon-install-confirmation", browser) )` → `this.pendingInstalls.get()`
- 条件付き依存: `if (pending)` → `pending.push()`
- 条件付き依存: `if (!(pending))` → `this.pendingInstalls.set()`
- 条件付き依存: `if ( installInfo.installs.every(i => i.state != AddonManager.STATE_DOWNLOADED) )` → `showNextConfirmation()`
- 条件付き依存: `if (unsigned.length == installInfo.installs.length)` → `notification.setAttribute()`
- 条件付き依存: `if (!unsigned.length)` → `notification.removeAttribute()`
- 条件付き依存: `if (!(!unsigned.length))` → `notification.setAttribute()`
- 参照: `AddonManager.SIGNEDSTATE_MISSING`, `AddonManager.STATE_DOWNLOADED`, `Ci.nsISecurityUITelemetry.WARNING_CONFIRM_ADDON_INSTALL`, `gBrowser.selectedTab`, `i.addon.signedState`, `i.state`, `installInfo.installs`, `installInfo.installs.length`, `installInfo.originatingURI`, `notification.style.minHeight`, `options.eventCallback`, `options.learnMoreURL`, `unsigned.length`
- XPCOM: `nsISecurityUITelemetry` / `Services.urlFormatter`

## showNextConfirmation()
- 位置: L1040-1050
- 役割: 同じブラウザに保留されている次の確認を表示する。ブラウザが閉じていれば何もしない。
- 触るとき: 複数の確認の順番の扱いを変えるとき。
- 呼び出し先: `gBrowser.browsers.includes()`, `this.pendingInstalls.get()`
- 条件付き依存: `if (pending && pending.length)` → `this.showInstallConfirmation()`
- 条件付き依存: `if (pending && pending.length)` → `pending.shift()`
- 参照: `pending.length`

## acceptInstallation()
- 位置: L1071-1080
- 役割: 全インストールを開始し、承認された件数を Glean に記録する。
- 触るとき: 承認時の処理や計測を変えるとき。
- 呼び出し先: `Glean.securityUi.events.accumulateSingleSample()`, `install.install()`
- 参照: `Ci.nsISecurityUITelemetry.WARNING_CONFIRM_ADDON_INSTALL_CLICK_THROUGH`, `installInfo.installs`
- XPCOM: `nsISecurityUITelemetry`

## cancelInstallation()
- 位置: L1082-1095
- 役割: まだ取り消されていないインストールを取り消し、次の確認を表示する。
- 触るとき: 確認の拒否時の処理を変えるとき。
- 呼び出し先: `showNextConfirmation()`
- 条件付き依存: `if (install.state != AddonManager.STATE_CANCELLED)` → `install.cancel()`
- 参照: `AddonManager.STATE_CANCELLED`, `install.state`, `installInfo.installs`

## options.eventCallback()
- 位置: L1103-1145
- 役割: 確認通知が閉じられたら取り消しを行い、表示時には対象アドオン名と未署名の注記を並べる。
- 触るとき: 確認通知の中身や閉じた時の挙動を変えるとき。
- 呼び出し先: `addonList.appendChild()`, `addonList.firstChild.remove()`, `cancelInstallation()`, `container.appendChild()`, `document.createXULElement()`, `document.getElementById()`, `name.setAttribute()`
- 条件付き依存: `if ( someUnsigned && install.addon.signedState <= AddonManager.SIGNEDSTATE_MISSING )` → `document.createXULElement()`
- 条件付き依存: `if ( someUnsigned && install.addon.signedState <= AddonManager.SIGNEDSTATE_MISSING )` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( someUnsigned && install.addon.signedState <= AddonManager.SIGNEDSTATE_MISSING )` → `unsignedLabel.setAttribute()`
- 条件付き依存: `if ( someUnsigned && install.addon.signedState <= AddonManager.SIGNEDSTATE_MISSING )` → `container.appendChild()`
- 参照: `AddonManager.SIGNEDSTATE_MISSING`, `addonList.firstChild`, `install.addon.name`, `install.addon.signedState`, `installInfo.installs`

## removeAllNotifications()
- 位置: L1233-1241
- 役割: インストール関連の通知を全て無応答で取り除き、1件でもあれば true を返す。
- 触るとき: ページ遷移などで関連通知をまとめて消す条件を変えるとき。
- 呼び出し先: `PopupNotifications.getNotification()`, `PopupNotifications.remove()`, `this.NOTIFICATION_IDS.map()`, `this.NOTIFICATION_IDS.map(id => PopupNotifications.getNotification(id, browser) ).filter()`
- 参照: `notifications.length`

## logWarningFullScreenInstallBlocked()
- 位置: L1243-1261
- 役割: 全画面中のインストール禁止をウェブサイトのコンソールに警告として出す。
- 触るとき: 全画面でインストールが止められた時の記録を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/scripterror;1"].createInstance()`, `Services.console.logMessage()`, `consoleMsg.initWithWindowID()`, `lazy.l10n.formatValueSync()`
- 参照: `Ci.nsIScriptError`, `Ci.nsIScriptError.warningFlag`, `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.innerWindowID`
- XPCOM: [`nsIScriptError`](../../../dom/bindings/nsIScriptError.idl.md) / `@mozilla.org/scripterror;1` / `Services.console`

## observe()
- 位置: async L1264-1751
- 役割: addon-install-* の各トピックを、無効化・ブロック・進捗・失敗・確認の各通知に振り分けて表示する。
- 触るとき: インストール時の通知の種類や文言、表示順を変えるとき。
- 呼び出し先: `Date.now()`, `Glean.securityUi.events.accumulateSingleSample()`, `PopupNotifications.getNotification()`, `PopupNotifications.show()`, `Services.policies.mayInstallAddon()`, `Services.prefs.prefIsLocked()`, `[ AddonManager.ERROR_BLOCKLISTED, AddonManager.ERROR_SOFT_BLOCKED, ].includes()`, `buildNotificationAction()`, `gBrowser.browsers.includes()`, `gUnifiedExtensions.getPopupAnchorID()`, `installInfo.install()`, `installInfo.installs.every()`, `lazy.l10n.formatMessages()`, `lazy.l10n.formatMessagesSync()`, `lazy.l10n.formatValue()`, `lazy.l10n.formatValueSync()`, `lazy.l10n.formatValues()`, `removeNotificationOnEnd()`, `showNotification()`, `this._removeProgressNotification()`, `this.logWarningFullScreenInstallBlocked()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("xpinstall.enabled")))` → `lazy.l10n.formatMessages()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("xpinstall.enabled")))` → `buildNotificationAction()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("xpinstall.enabled")))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (Services.policies)` → `Services.policies.getExtensionSettings()`
- 条件付き依存: `if (progressNotification)` → `progressNotification.remove()`
- 条件付き依存: `if (isSitePermissionAddon)` → `lazy.getSitePermsInstallPromptStringIds()`
- 条件付き依存: `if (!(stringIds?.header && stringIds?.message))` → `console.error()`
- 条件付き依存: `if (!(stringIds?.header && stringIds?.message))` → `cancelInstallation()`
- 条件付き依存: `if (isSitePermissionAddon)` → `declineActions.push()`
- 条件付き依存: `if (isSitePermissionAddon)` → `buildNotificationAction()`
- 条件付き依存: `if (isSitePermissionAddon)` → `AMTelemetry.recordSuspiciousSiteEvent()`
- 条件付き依存: `if (isSitePermissionAddon)` → `neverAllowCallback()`
- 条件付き依存: `if (install.state != AddonManager.STATE_CANCELLED)` → `install.cancel()`
- 条件付き依存: `if ( install.addon && !Services.policies.mayInstallAddon({ id: install.addon.id, type: install.addon.type, permissions: install.addon.userPermissions?.permission...)` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if ( install.addon && !Services.policies.mayInstallAddon({ id: install.addon.id, type: install.addon.type, permissions: install.addon.userPermissions?.permission...)` → `Services.policies.getExtensionSettings()`
- 条件付き依存: `if (!( install.addon && !Services.policies.mayInstallAddon({ id: install.addon.id, type: install.addon.type, permissions: install.addon.userPermissions?.permission...))` → `ERROR_L10N_IDS.get()`
- 条件付き依存: `if (!( install.addon && !Services.policies.mayInstallAddon({ id: install.addon.id, type: install.addon.type, permissions: install.addon.userPermissions?.permission...))` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if (install.error == AddonManager.ERROR_SIGNEDSTATE_REQUIRED)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (isBlocklistError)` → `install.addon?.getBlocklistURL()`
- 条件付き依存: `if (progressNotification)` → `Date.now()`
- 条件付き依存: `if (progressNotification)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (securityDelay > 0)` → `setTimeout()`
- 条件付き依存: `if (securityDelay > 0)` → `PopupNotifications.getNotification()`
- 条件付き依存: `if ( PopupNotifications.getNotification("addon-progress", browser) )` → `showNotification()`
- 参照: `AddonManager.ERROR_BLOCKLISTED`, `AddonManager.ERROR_SIGNEDSTATE_REQUIRED`, `AddonManager.ERROR_SOFT_BLOCKED`, `AddonManager.STATE_CANCELLED`, `AddonManager.STATE_DOWNLOADED`, `Ci.nsISecurityUITelemetry .WARNING_ADDON_ASKING_PREVENTED_CLICK_THROUGH`, `Ci.nsISecurityUITelemetry.WARNING_ADDON_ASKING_PREVENTED`, `Ci.nsIStandardURL`, `Services.appinfo.version`, `Services.policies`, `aInstall.state`, `aSubject.wrappedJSObject`, `action.disabled`, `addon?.type`, `browser.contentWindow`, `browser.currentURI`, `extensionSettings.blocked_install_message`, `fluentIds?.length`, `install.addon`, `install.addon.id`, `install.addon.type`, `install.addon.userPermissions?.permissions`, `install.error`, `install.name`, `install.sourceURI`, `install.sourceURI.host`, `install.state`, `installInfo.browser`, `installInfo.installs`, `installInfo.installs.length`, `installInfo.installs[0].addon.sitePermissions`, `installInfo.originatingURI`, `lazy.SITEPERMS_ADDON_TYPE`, `notification._startTime`, `options.contentWindow`, `options.displayURI`, `options.displayURI.displayHost`, `options.displayURI.host`, `options.eventCallback`, `options.installs`, `options.learnMoreURL`, `options.name`, `options.persistent`, `options.removeOnDismissal`, `options.sourceURI`, `progressNotification._startTime`, `stringIds.header`, `stringIds.message`, `stringIds?.header`, `stringIds?.message`
- XPCOM: `nsISecurityUITelemetry` / [`nsIStandardURL`](../../../netwerk/base/nsIStandardURL.idl.md) / `Services.appinfo` / `Services.policies` / `Services.prefs` / `Services.urlFormatter`

## cancelInstallation()
- 位置: L1273-1282
- 役割: インストールを全て取り消し、installInfo 側のキャンセルも呼ぶ。
- 触るとき: インストール全体の取り消し経路を調べるとき。
- 条件付き依存: `if (install.state != AddonManager.STATE_CANCELLED)` → `install.cancel()`
- 条件付き依存: `if (installInfo.cancel)` → `installInfo.cancel()`
- 参照: `AddonManager.STATE_CANCELLED`, `install.state`, `installInfo.cancel`, `installInfo.installs`

## options.eventCallback()
- 位置: L1427-1456
- 役割: ブロックされたインストールの通知が表示された時に、説明文と詳細リンクの記事を設定する。
- 触るとき: インストールをブロックした時の説明文やリンク先を変えるとき。
- 呼び出し先: `doc.getElementById()`, `learnMore.setAttribute()`, `message.firstChild.remove()`
- 条件付き依存: `if (!(!hasHost))` → `doc.createElementNS()`
- 条件付き依存: `if (!(!hasHost))` → `BrowserUIUtils.getLocalizedFragment()`
- 条件付き依存: `if (!(!hasHost))` → `message.appendChild()`
- 参照: `b.textContent`, `browser.ownerDocument`, `message.firstChild`, `message.textContent`, `options.name`

## neverAllowCallback()
- 位置: L1481-1488
- 役割: サイトの install 権限を拒否に設定し、インストールをキャンセルする。
- 触るとき: 常に拒否する選択の挙動を変えるとき。
- 呼び出し先: `SitePermissions.setForPrincipal()`, `cancelInstallation()`
- 参照: `SitePermissions.BLOCK`, `browser.contentPrincipal`

## options.eventCallback()
- 位置: L1549-1556
- 役割: 進捗通知が閉じられた時に contentWindow と sourceURI を解放する。
- 触るとき: 進捗通知が保持する参照の後始末を変えるとき。
- 参照: `options.contentWindow`, `options.sourceURI`

## options.eventCallback()
- 位置: L1679-1692
- 役割: ブロックリスト由来の失敗通知が表示された時に、ブロックリストの URL をリンクへ設定する。
- 触るとき: インストール失敗時のブロックリスト案内リンクを変えるとき。
- 呼び出し先: `doc.getElementById()`
- 条件付き依存: `if (blocklistURL)` → `blocklistURLEl.setAttribute()`
- 条件付き依存: `if (!(blocklistURL))` → `blocklistURLEl.removeAttribute()`
- 参照: `browser.ownerDocument`

## showNotification()
- 位置: L1712-1724
- 役割: 進捗通知を消し、必要ならセキュリティ遅延の後に確認通知を表示する。
- 触るとき: インストール確認の表示タイミング(遅延)を変えるとき。
- 呼び出し先: `this._removeProgressNotification()`, `this.showInstallConfirmation()`
- 条件付き依存: `if (PopupNotifications.isPanelOpen)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (PopupNotifications.isPanelOpen)` → `document.getElementById()`
- 参照: `PopupNotifications.isPanelOpen`, `rect.height`

## _removeProgressNotification()
- 位置: L1752-1760
- 役割: addon-progress の通知があれば削除する。
- 触るとき: 進捗通知の後片付けを変えるとき。
- 呼び出し先: `PopupNotifications.getNotification()`
- 条件付き依存: `if (notification)` → `notification.remove()`

## init()
- 位置: L1765-1770
- 役割: 通知ボタンを更新し、ExtensionsUI の change 監視を始める。
- 触るとき: 拡張の通知ボタンの初期化を変えるとき。
- 呼び出し先: `ExtensionsUI.on()`, `this.updateAlerts()`, `this.updateAlerts.bind()`
- 参照: `this.boundUpdate`, `this.initialized`

## uninit()
- 位置: L1772-1779
- 役割: ExtensionsUI の change 監視を外す。init 前に呼ばれた場合は何もしない。
- 触るとき: 拡張通知の後始末を変えるとき。
- 呼び出し先: `ExtensionsUI.off()`
- 参照: `this.boundUpdate`, `this.initialized`

## _createAddonButton()
- 位置: L1781-1797
- 役割: 拡張の通知項目となるツールバーボタンを作ってアドオン通知の枠に追加する。
- 触るとき: 通知ボタンの見た目や並びを変えるとき。
- 呼び出し先: `PanelUI.addonNotificationContainer.appendChild()`, `button.addEventListener()`, `button.setAttribute()`, `document.createXULElement()`, `lazy.l10n.formatValueSync()`
- 参照: `addon.name`, `addon?.iconURL`, `button.className`

## updateAlerts()
- 位置: L1799-1842
- 役割: インポート待ち、更新、サイドロードの各通知ボタンを作り直す。合計は最大4件に抑える。
- 触るとき: メインメニューの拡張通知の内容や件数を変えるとき。
- 呼び出し先: `ExtensionsUI.showSideloaded()`, `ExtensionsUI.showUpdate()`, `PanelUI.hide()`, `container.firstChild.remove()`, `this._createAddonButton()`
- 条件付き依存: `if (lazy.AMBrowserExtensionsImport.canCompleteOrCancelInstalls)` → `this._createAddonButton()`
- 条件付き依存: `if (lazy.AMBrowserExtensionsImport.canCompleteOrCancelInstalls)` → `lazy.AMBrowserExtensionsImport.completeInstalls()`
- 参照: `ExtensionsUI.sideloaded`, `ExtensionsUI.updates`, `PanelUI.addonNotificationContainer`, `container.firstChild`, `lazy.AMBrowserExtensionsImport.canCompleteOrCancelInstalls`, `update.addon`

## promptRemoveExtension()
- 位置: async L1846-1895
- 役割: 削除確認ダイアログを出し、削除するか、通報も行うかを返す。
- 触るとき: 拡張の削除確認の文言や通報チェックの条件を変えるとき。
- 呼び出し先: `["extension", "theme"].includes()`, `confirmEx()`, `lazy.l10n.formatValues()`
- 条件付き依存: `if ( gAddonAbuseReportEnabled && ["extension", "theme"].includes(addon.type) )` → `lazy.l10n.formatValue()`
- 条件付き依存: `if (addon.type === "mlmodel")` → `lazy.l10n.formatValue()`
- 参照: `Services.prompt`, `addon.type`, `checkboxState.value`
- XPCOM: `Services.prompt`

## reportAddon()
- 位置: async L1897-1909
- 役割: アドオンの通報フォームを前面のタブで開く。
- 触るとき: 拡張の通報の開き先を変えるとき。
- 呼び出し先: `AddonManager.getAddonByID()`, `lazy.AbuseReporter.getAMOFormURL()`, `window.openTrustedLinkIn()`

## removeAddon()
- 位置: async L1911-1928
- 役割: アンインストール可能なら確認の上で削除し、通報が選ばれていれば通報も行う。
- 触るとき: 拡張の削除の一連の流れを変えるとき。
- 呼び出し先: `AddonManager.getAddonByID()`, `this.promptRemoveExtension()`
- 条件付き依存: `if (remove)` → `addon.uninstall()`
- 条件付き依存: `if (report)` → `this.reportAddon()`
- 参照: `AddonManager.PERM_CAN_UNINSTALL`, `addon.id`, `addon.permissions`

## manageAddon()
- 位置: async L1930-1937
- 役割: about:addons の詳細画面をアドオン ID で開く。
- 触るとき: 拡張の管理画面への遷移を変えるとき。
- 呼び出し先: `AddonManager.getAddonByID()`, `encodeURIComponent()`, `this.openAddonsMgr()`
- 参照: `addon.id`

## openAddonsMgr()
- 位置: L1960-2016
- 役割: 既存の about:addons を ping で探して前面化し、無ければ開いて指定のビューを読み込む。
- 触るとき: about:addons を開く経路やビュー選択を変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (aView && !selectTabByViewId)` → `emWindow.loadView()`
- 条件付き依存: `if (emWindow)` → `browserWindow.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (emWindow)` → `emWindow.focus()`
- 条件付き依存: `if (emWindow)` → `resolve()`
- 条件付き依存: `if (selectTabByViewId)` → `isBlankPageURL()`
- 条件付き依存: `if (selectTabByViewId)` → `openTrustedLinkIn()`
- 条件付き依存: `if (!(selectTabByViewId))` → `switchToTabHavingURI()`
- 参照: `browserWindow.gBrowser.selectedTab`, `emWindow.docShell.chromeEventHandler`, `gBrowser.currentURI.spec`
- XPCOM: `Services.obs`

## receivePong()
- 位置: L1965-1978
- 役割: EM-pong に応答した about:addons の窓を、現在の窓を優先して記録する。
- 触るとき: 既存の about:addons の選び方を変えるとき。
- 参照: `aSubject.browsingContext.topChromeWindow`, `aSubject.gViewController.currentViewId`

## observer()
- 位置: L2007-2014
- 役割: EM-loaded を一度だけ受けて、指定ビューを読み込み前面化する。
- 触るとき: about:addons を新規に開いた時の読み込み後処理を変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `aSubject.focus()`, `resolve()`
- 条件付き依存: `if (aView)` → `aSubject.loadView()`
- XPCOM: `Services.obs`

## init()
- 位置: L2044-2075
- 役割: 拡張ボタンの表示状態、権限・ブロックリスト・AppMenu・CUI の監視を登録する。
- 触るとき: 拡張ボタンの初期化処理や監視対象を変えるとき。
- 呼び出し先: `AddonManager.addManagerListener()`, `CustomizableUI.addListener()`, `Glean.extensionsButton.prefersHiddenButton.set()`, `PanelUI.mainView.addEventListener()`, `document.getElementById()`, `gBrowser.addTabsProgressListener()`, `gNavToolbox.addEventListener()`, `lazy.ExtensionPermissions.addListener()`, `this._button.addEventListener()`, `this._buttonAttrObs.observe()`, `this._updateButtonBarListeners()`, `this.onAppMenuShowing.bind()`, `this.onButtonOpenChange()`, `this.updateAttention()`, `this.updateButtonVisibility()`, `window.addEventListener()`
- 参照: `this._button`, `this._buttonAttrObs`, `this._initialized`, `this._navbar`, `this.buttonAlwaysVisible`, `this.onAppMenuShowing`, `this.permListener`

## this.permListener()
- 位置: L2062-2062
- 役割: 拡張の権限が変わった時に注意表示を更新する。
- 触るとき: 権限変更による注意表示の更新条件を変えるとき。
- 呼び出し先: `this.updateAttention()`

## uninit()
- 位置: L2077-2095
- 役割: init で登録した監視をすべて外す。
- 触るとき: 拡張ボタンの後始末を変えるとき。
- 呼び出し先: `AddonManager.removeManagerListener()`, `CustomizableUI.removeListener()`, `PanelUI.mainView.removeEventListener()`, `gNavToolbox.removeEventListener()`, `lazy.ExtensionPermissions.removeListener()`, `this._button.removeEventListener()`, `this._buttonAttrObs.disconnect()`, `window.removeEventListener()`
- 参照: `this._initialized`, `this.onAppMenuShowing`, `this.permListener`

## _updateButtonBarListeners()
- 位置: L2097-2117
- 役割: 常時表示でない時だけ navbar の mouseover と mouseout を監視する。
- 触るとき: ツールバーにマウスがあるかによるボタンの表示保持を変えるとき。
- 条件付き依存: `if (this.buttonAlwaysVisible)` → `this._navbar.removeEventListener()`
- 条件付き依存: `if (!(this.buttonAlwaysVisible))` → `this._navbar.addEventListener()`
- 参照: `this._buttonBarHasMouse`, `this.buttonAlwaysVisible`

## onBlocklistAttentionUpdated()
- 位置: L2119-2121
- 役割: ブロックリストの注意が更新されたら注意表示を更新する。
- 触るとき: ブロックリスト由来の注意表示の契機を変えるとき。
- 呼び出し先: `this.updateAttention()`

## onAppMenuShowing()
- 位置: L2123-2128
- 役割: アプリメニューの拡張関連項目を、常時表示設定に応じて切り替える。
- 触るとき: アプリメニューの拡張ボタン項目の出し分けを変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `document.getElementById("appMenu-extensions-themes-button").hidden`, `document.getElementById("appMenu-unified-extensions-button").hidden`, `this.buttonAlwaysVisible`

## onLocationChange()
- 位置: L2130-2139
- 役割: 選択タブで文書が切り替わった時に注意表示を更新する。
- 触るとき: ページ遷移に伴う注意表示の更新条件を変えるとき。
- 条件付き依存: `if ( webProgress.isTopLevel && browser === gBrowser.selectedBrowser && !(flags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT) )` → `this.updateAttention()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `gBrowser.selectedBrowser`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## updateButtonVisibility()
- 位置: L2141-2167
- 役割: 常時表示、開いている、注意がある、ツールバーにマウスがある等の条件で拡張ボタンの表示を決める。
- 触るとき: 拡張ボタンを表示する条件を変えるとき。
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `this.button.hasAttribute()`
- 条件付き依存: `if (shouldShowButton)` → `this._navbar.setAttribute()`
- 条件付き依存: `if (!(shouldShowButton))` → `this._navbar.removeAttribute()`
- 参照: `this._button.hidden`, `this._button.open`, `this._buttonBarHasMouse`, `this._buttonShownBeforeButtonOpen`, `this.button.hidden`, `this.buttonAlwaysVisible`, `this.buttonIgnoresAttention`

## ensureButtonShownBeforeAttachingPanel()
- 位置: L2169-2178
- 役割: パネルをボタンに付ける前に、アンカーとしてボタンを一時的に表示する。
- 触るとき: 通知やパネルのアンカー位置の扱いを変えるとき。
- 条件付き依存: `if (!this.buttonAlwaysVisible && !this._button.open)` → `this.updateButtonVisibility()`
- 参照: `this._button.open`, `this._buttonShownBeforeButtonOpen`, `this.buttonAlwaysVisible`

## onButtonOpenChange()
- 位置: L2180-2187
- 役割: ボタンの open 状態が変わった時に一時表示の扱いを解除し、表示を再判定する。
- 触るとき: ボタンが開いた/閉じた時の表示遷移を変えるとき。
- 条件付き依存: `if (!this.buttonAlwaysVisible && !this._button.open)` → `this.updateButtonVisibility()`
- 参照: `this._button.open`, `this._buttonShownBeforeButtonOpen`, `this.buttonAlwaysVisible`

## updateAttention()
- 位置: L2190-2243
- 役割: 権限要求・隔離ドメイン・ブロックリストの注意を計算してボタンの attention とツールチップを更新する。
- 触るとき: 拡張ボタンの注意ドットや文言の優先順位を変えるとき。
- 呼び出し先: `AddonManager.shouldShowBlocklistAttention()`, `this.button.ownerDocument.l10n.setAttributes()`, `this.button.toggleAttribute()`
- 条件付き依存: `if (!blocklistAttention)` → `this.getActivePolicies()`
- 条件付き依存: `if (!blocklistAttention)` → `this.browserActionFor()`
- 条件付き依存: `if (!widget || widget.areaType !== CustomizableUI.TYPE_TOOLBAR)` → `lazy.OriginControls.getAttentionState()`
- 条件付き依存: `if (!blocklistAttention)` → `this._shouldShowQuarantinedNotification()`
- 条件付き依存: `if (blocklistAttention)` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (permissionsAttention || quarantinedAttention)` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (!this.buttonAlwaysVisible && !this.buttonIgnoresAttention)` → `this.updateButtonVisibility()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `lazy.OriginControls.getAttentionState(policy, window).attention`, `this.browserActionFor(policy)?.widget`, `this.button`, `this.buttonAlwaysVisible`, `this.buttonIgnoresAttention`, `widget.areaType`

## getPopupAnchorID()
- 位置: L2249-2265
- 役割: 通知のアンカーとして拡張ボタンを使えるよう、子要素を窓ごとに記録して ID を返す。
- 触るとき: 拡張ボタンを通知のアンカーに使う仕組みを変えるとき。
- 条件付き依存: `if (!aBrowser[attr])` → `aWindow.document.getElementById()`

## button()
- 位置: L2267-2269
- 役割: 拡張ボタン要素を返す。
- 触るとき: 拡張ボタン要素の参照元を調べるとき。
- 参照: `this._button`

## getActivePolicies()
- 位置: L2281-2307
- 役割: 有効な拡張のうち、隠し拡張と、この窓で使えない拡張を除いて返す。
- 触るとき: パネルに出す拡張の対象範囲を変えるとき。
- 呼び出し先: `WebExtensionPolicy.getActiveExtensions()`, `policies.filter()`, `policy.canAccessWindow()`
- 参照: `extension.isHidden`, `extension?.type`

## hasExtensionsInPanel()
- 位置: L2319-2328
- 役割: ツールバー外または溢れた拡張が1つでもあるかを返す。
- 触るとき: パネルに拡張一覧を出すべきかの判定を変えるとき。
- 呼び出し先: `policies.some()`, `this.browserActionFor()`, `this.getActivePolicies()`, `widget.forWindow()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `this.browserActionFor(policy)?.widget`, `widget.areaType`, `widget.forWindow(window).overflowed`

## isPrivateWindowMissingExtensionsWithoutPBMAccess()
- 位置: L2330-2336
- 役割: プライベート窓で、プライベートブラウズを許可されていない拡張があるかを返す。
- 触るとき: プライベート窓の空状態の表示条件を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `policies.some()`, `this.getActivePolicies()`
- 参照: `p.privateBrowsingAllowed`

## isAtLeastOneExtensionWithPBMOptIn()
- 位置: async L2348-2366
- 役割: プライベートブラウズ許可を切り替えられる拡張が、まだ許可されていない状態で1つでもあるかを返す。
- 触るとき: プライベート窓の空状態で出す文言を変えるとき。
- 呼び出し先: `AddonManager.getAddonsByTypes()`, `WebExtensionPolicy.getByID()`, `addons.some()`
- 参照: `addon.hidden`, `addon.id`, `addon.permissions`, `lazy.AddonManager.PERM_CAN_CHANGE_PRIVATEBROWSING_ACCESS`, `policy.privateBrowsingAllowed`

## getDisabledExtensionsInfo()
- 位置: async L2368-2376
- 役割: 無効な拡張の有無と、有効化できるものがあるかを返す。
- 触るとき: パネルの空状態で無効拡張の案内を出す条件を変えるとき。
- 呼び出し先: `AddonManager.getAddonsByTypes()`, `addons.filter()`, `addons.some()`
- 参照: `a.hidden`, `a.isActive`, `a.permissions`, `addons.length`, `lazy.AddonManager.PERM_CAN_ENABLE`

## handleEvent()
- 位置: L2378-2433
- 役割: パネルの表示・非表示、通知アンカー、マウス、カスタマイズ、ツールバー表示のイベントを対応する処理に振り分ける。
- 触るとき: 拡張ボタンが受け取るイベントと動作の対応を変えるとき。
- 呼び出し先: `popupnotification?.getAttribute()`, `this._navbar.contains()`, `this.ensureButtonShownBeforeAttachingPanel()`, `this.onPanelViewHiding()`, `this.onPanelViewShowing()`, `this.onToolbarVisibilityChange()`, `this.panel.hidePopup()`, `this.recordButtonTelemetry()`, `this.updateButtonVisibility()`
- 条件付き依存: `if (popupid === "addon-webext-permissions")` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (!(popupid === "addon-webext-permissions"))` → `gXPInstallObserver.NOTIFICATION_IDS.includes()`
- 条件付き依存: `if (gXPInstallObserver.NOTIFICATION_IDS.includes(popupid))` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (!(gXPInstallObserver.NOTIFICATION_IDS.includes(popupid)))` → `console.error()`
- 条件付き依存: `if ( this._buttonBarHasMouse && !this._navbar.contains(event.relatedTarget) )` → `this.updateButtonVisibility()`
- 参照: `PopupNotifications.panel`, `PopupNotifications.panel.firstElementChild`, `event.detail.visible`, `event.relatedTarget`, `event.target`, `event.target.id`, `event.type`, `this._buttonBarHasMouse`

## onPanelViewShowing()
- 位置: L2435-2579
- 役割: パネル表示時に一覧、空状態の文言と案内、セーフモード・ブロックリスト・隔離の警告バーを組み立てる。
- 触るとき: 拡張パネルの表示内容や空状態の出し分けを変えるとき。
- 呼び出し先: `a.name.localeCompare()`, `document.createElement()`, `item.setExtension()`, `list.appendChild()`, `panelview.querySelector()`, `policies.filter()`, `policiesForList.sort()`, `this._shouldShowQuarantinedNotification()`, `this.getActivePolicies()`, `this.hasExtensionsInPanel()`
- 条件付き依存: `if (this.hasExtensionsInPanel(policies))` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!(this.hasExtensionsInPanel(policies)))` → `this.isPrivateWindowMissingExtensionsWithoutPBMAccess()`
- 条件付き依存: `if (this.isPrivateWindowMissingExtensionsWithoutPBMAccess())` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (this.isPrivateWindowMissingExtensionsWithoutPBMAccess())` → `this.isAtLeastOneExtensionWithPBMOptIn().then()`
- 条件付き依存: `if (this.isPrivateWindowMissingExtensionsWithoutPBMAccess())` → `this.isAtLeastOneExtensionWithPBMOptIn()`
- 条件付き依存: `if (this.isPrivateWindowMissingExtensionsWithoutPBMAccess())` → `isStillShowing()`
- 条件付き依存: `if (!result && isStillShowing())` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!(this.isPrivateWindowMissingExtensionsWithoutPBMAccess()))` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!(this.isPrivateWindowMissingExtensionsWithoutPBMAccess()))` → `this.getDisabledExtensionsInfo().then()`
- 条件付き依存: `if (!(this.isPrivateWindowMissingExtensionsWithoutPBMAccess()))` → `this.getDisabledExtensionsInfo()`
- 条件付き依存: `if (!(this.isPrivateWindowMissingExtensionsWithoutPBMAccess()))` → `isStillShowing()`
- 条件付き依存: `if (disabledExtensionsInfo.isAnyDisabled)` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!policies.length)` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!policies.length)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!policies.length)` → `this._createDiscoverButton()`
- 条件付き依存: `if (!policies.length)` → `panelview.querySelector()`
- 条件付き依存: `if (!policies.length)` → `manageExtensionsButton.previousElementSibling.before()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `this._makeMessageBar()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `container.prepend()`
- 条件付き依存: `if (this.blocklistAttentionInfo?.shouldShow)` → `this._createBlocklistMessageBar()`
- 条件付き依存: `if (!(this.blocklistAttentionInfo?.shouldShow))` → `this._messageBarBlocklist?.remove()`
- 条件付き依存: `if (!this._messageBarQuarantinedDomain)` → `this._makeMessageBar()`
- 条件付き依存: `if (!this._messageBarQuarantinedDomain)` → `this._messageBarQuarantinedDomain .querySelector("a") .addEventListener()`
- 条件付き依存: `if (!this._messageBarQuarantinedDomain)` → `this._messageBarQuarantinedDomain .querySelector()`
- 条件付き依存: `if (!this._messageBarQuarantinedDomain)` → `this.togglePanel()`
- 条件付き依存: `if (shouldShowQuarantinedNotification)` → `container.appendChild()`
- 条件付き依存: `if (!(shouldShowQuarantinedNotification))` → `container.contains()`
- 条件付き依存: `if ( !shouldShowQuarantinedNotification && this._messageBarQuarantinedDomain && container.contains(this._messageBarQuarantinedDomain) )` → `container.removeChild()`
- 参照: `Services.appinfo.inSafeMode`, `b.name`, `disabledExtensionsInfo.isAnyDisabled`, `disabledExtensionsInfo.isAnyEnableable`, `p.extension.hasBrowserActionUI`, `policies.length`, `policy.extension`, `this._messageBarBlocklist`, `this._messageBarQuarantinedDomain`, `this._messageBarSafemode`, `this._panelShownCount`, `this.blocklistAttentionInfo?.shouldShow`
- XPCOM: `Services.appinfo` / `Services.prefs`

## isStillShowing()
- 位置: L2437-2437
- 役割: 非同期の結果が古くなっていないか、表示の世代番号で確認する。
- 触るとき: 非同期更新が古い表示を上書きしないよう調べるとき。
- 参照: `this._panelShownCount`

## onPanelViewHiding()
- 位置: L2581-2596
- 役割: パネルが閉じた時に一覧と Discover ボタンを消し、注意表示を次フレームで更新する。
- 触るとき: パネルを閉じた後の後始末を変えるとき。
- 呼び出し先: `list.lastChild.remove()`, `panelview .querySelector()`, `panelview .querySelector("#unified-extensions-discover-extensions") ?.remove()`, `panelview.querySelector()`, `requestAnimationFrame()`, `this.updateAttention()`
- 参照: `list.lastChild`, `this._panelShownCount`, `window.closed`

## onToolbarVisibilityChange()
- 位置: L2598-2645
- 役割: ツールバーが隠れた時、その中の拡張ウィジェットを見た目だけパネル側へ移し、表示された時に戻す。
- 触るとき: ツールバーを隠した時の拡張の見せ方を変えるとき。
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidgetIdsInArea()`, `CustomizableUI.getWidgetIdsInArea(toolbarId).filter()`, `this.panel.querySelector()`
- 条件付き依存: `if (isVisible)` → `this._maybeMoveWidgetNodeBack()`
- 条件付き依存: `if (!(isVisible))` → `widget.forWindow()`
- 条件付き依存: `if (!(isVisible))` → `node.setAttribute()`
- 条件付き依存: `if (!(isVisible))` → `overflowedExtensionsList.appendChild()`
- 条件付き依存: `if (!(isVisible))` → `this._updateWidgetClassName()`
- 参照: `CustomizableUI.isWebExtensionWidget`, `widget.id`

## _maybeMoveWidgetNodeBack()
- 位置: L2647-2701
- 役割: 見た目だけ移したウィジェットを、CUI の配置情報をもとに元のツールバー位置へ戻す。
- 触るとき: ウィジェットを元の位置へ戻す挿入位置の計算を変えるとき。
- 呼び出し先: `CustomizableUI.getCustomizationTarget()`, `CustomizableUI.getPlacementOfWidget()`, `CustomizableUI.getWidget()`, `child.getAttribute()`, `document.getElementById()`, `node.hasAttribute()`, `widget.forWindow()`
- 条件付き依存: `if (currentPosition === position)` → `child.before()`
- 条件付き依存: `if (child === container.lastChild)` → `child.after()`
- 条件付き依存: `if (moved)` → `node.removeAttribute()`
- 条件付き依存: `if (moved)` → `this._updateWidgetClassName()`
- 参照: `container.childNodes`, `container.lastChild`

## panel()
- 位置: L2704-2739
- 役割: 拡張パネルをテンプレートから初めて使う時に生成し、CUI の登録と一部の l10n を行って返す。
- 触るとき: 拡張パネルの生成と初期化を変えるとき。
- 条件付き依存: `if (!this._panel)` → `document.getElementById()`
- 条件付き依存: `if (!this._panel)` → `template.replaceWith()`
- 条件付き依存: `if (!this._panel)` → `this._panel.querySelector()`
- 条件付き依存: `if (!this._panel)` → `CustomizableUI.registerPanelNode()`
- 条件付き依存: `if (!this._panel)` → `CustomizableUI.addPanelCloseListeners()`
- 条件付き依存: `if (!this._panel)` → `this._panel .querySelector("#unified-extensions-manage-extensions") .addEventListener()`
- 条件付き依存: `if (!this._panel)` → `this._panel .querySelector()`
- 条件付き依存: `if (!this._panel)` → `BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (!this._panel)` → `document .getElementById("unified-extensions-context-menu") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`
- 条件付き依存: `if (!this._panel)` → `document .getElementById("unified-extensions-context-menu") .querySelectorAll()`
- 条件付き依存: `if (!this._panel)` → `document .getElementById()`
- 条件付き依存: `if (!this._panel)` → `el.setAttribute()`
- 条件付き依存: `if (!this._panel)` → `el.getAttribute()`
- 条件付き依存: `if (!this._panel)` → `el.removeAttribute()`
- 参照: `CustomizableUI.AREA_ADDONS`, `template.content`, `this._panel`

## togglePanel()
- 位置: async L2743-2813
- 役割: 拡張パネルを開閉する。拡張が一覧に無く他に出せるものも無い時は about:addons を開く。
- 触るとき: 拡張ボタンを押した時の挙動や開く条件を変えるとき。
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `window.dispatchEvent()`
- 条件付き依存: `if (aEvent)` → `this.getActivePolicies()`
- 条件付き依存: `if (aEvent)` → `this.hasExtensionsInPanel()`
- 条件付き依存: `if (aEvent)` → `this.isPrivateWindowMissingExtensionsWithoutPBMAccess()`
- 条件付き依存: `if (aEvent)` → `this.getDisabledExtensionsInfo()`
- 条件付き依存: `if ( policies.length && !this.hasExtensionsInPanel(policies) && !this.isPrivateWindowMissingExtensionsWithoutPBMAccess() && !(await this.getDisabledExtensionsInf...)` → `BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (!CustomizationHandler.isCustomizing())` → `AddonManager.getBlocklistAttentionInfo()`
- 条件付き依存: `if (!this._listView)` → `PanelMultiView.getViewNode()`
- 条件付き依存: `if (!this._listView)` → `this._listView.addEventListener()`
- 条件付き依存: `if (this._button.open)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (!(this._button.open))` → `CustomizableUI.getCollapsedToolbarIds()`
- 条件付き依存: `if (!(this._button.open))` → `this.onToolbarVisibilityChange()`
- 条件付き依存: `if (!(this._button.open))` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (!(this._button.open))` → `this.ensureButtonShownBeforeAttachingPanel()`
- 条件付き依存: `if (!(this._button.open))` → `PanelMultiView.openPopup()`
- 参照: `(await this.getDisabledExtensionsInfo()).isAnyDisabled`, `AppConstants.platform`, `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `aEvent.button`, `aEvent.charCode`, `aEvent.ctrlKey`, `aEvent.keyCode`, `aEvent.type`, `panel.hidden`, `policies.length`, `this._button`, `this._button.open`, `this._listView`, `this.blocklistAttentionInfo`, `this.panel`

## openPanel()
- 位置: async L2815-2831
- 役割: パネルを開く入口。既に開いている時や編集モード中は例外を投げ、アプリメニュー経由なら計測してから togglePanel に渡す。
- 触るとき: 拡張パネルを外部から開く経路を変えるとき。
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `this.togglePanel()`
- 条件付き依存: `if (event?.sourceEvent?.target.id === "appMenu-unified-extensions-button")` → `Glean.extensionsButton.openViaAppMenu.record()`
- 条件付き依存: `if (event?.sourceEvent?.target.id === "appMenu-unified-extensions-button")` → `this.hasExtensionsInPanel()`
- 参照: `event?.sourceEvent?.target.id`, `this._button.hidden`, `this._button.open`

## isPanelOpen()
- 位置: L2837-2839
- 役割: 拡張ボタンが開いているか(拡張パネルかボタンに付いた別パネルか)を返す。
- 触るとき: パネルが開いているかの判定を他から参照するとき。
- 参照: `this._button?.open`

## updateContextMenu()
- 位置: L2841-2920
- 役割: 拡張の右クリックメニューの項目の表示と有効状態を、ウィジェットの配置と拡張の権限に応じて更新する。
- 触るとき: 拡張の右クリックメニューの項目の出し分けを変えるとき。
- 呼び出し先: `AddonManager.getAddonByID()`, `AddonManager.getAddonByID(id).then()`, `ExtensionsUI.originControlsMenu()`, `WebExtensionPolicy.getByID()`, `menu.querySelector()`, `this._getExtensionId()`, `this._getWidgetId()`, `this.browserActionFor()`
- 条件付き依存: `if (forBrowserAction)` → `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (forBrowserAction)` → `pinButton.toggleAttribute()`
- 条件付き依存: `if (forBrowserAction)` → `document.querySelector()`
- 条件付き依存: `if (browserAction)` → `browserAction.updateContextMenu()`
- 参照: `AddonManager.PERM_CAN_UNINSTALL`, `CustomizableUI.AREA_ADDONS`, `CustomizableUI.getPlacementOfWidget(widgetId).area`, `addon.permissions`, `document.querySelector("#unified-extensions-area > :first-child") ?.id`, `document.querySelector("#unified-extensions-area > :last-child")?.id`, `element.hidden`, `event.target.id`, `moveDown.hidden`, `moveUp.hidden`, `placement?.area`, `removeButton.disabled`, `reportButton.hidden`

## onContextMenuCommand()
- 位置: L2923-2935
- 役割: メニューの項目を選んだ時にパネルを閉じる。ただし移動の項目では閉じない。
- 触るとき: 右クリックメニューからの操作後にパネルを閉じるかを変えるとき。
- 呼び出し先: `classList.contains()`, `this.togglePanel()`
- 参照: `event.target`

## browserActionFor()
- 位置: L2937-2943
- 役割: 拡張のブラウザアクションを、ext-browserAction 側の登録から取り出す。
- 触るとき: ブラウザアクションの取得経路を調べるとき。
- 呼び出し先: `method()`
- 参照: `lazy.ExtensionParent.apiManager.global.browserActionFor`, `policy?.extension`

## manageExtension()
- 位置: async L2945-2949
- 役割: 右クリックメニューから拡張の管理画面を開く。
- 触るとき: 拡張の管理メニュー項目の動作を変えるとき。
- 呼び出し先: `BrowserAddonUI.manageAddon()`, `this._getExtensionId()`

## removeExtension()
- 位置: async L2951-2955
- 役割: 右クリックメニューから拡張の削除を行う。
- 触るとき: 拡張の削除メニュー項目の動作を変えるとき。
- 呼び出し先: `BrowserAddonUI.removeAddon()`, `this._getExtensionId()`

## reportExtension()
- 位置: async L2957-2961
- 役割: 右クリックメニューから拡張の通報を行う。
- 触るとき: 拡張の通報メニュー項目の動作を変えるとき。
- 呼び出し先: `BrowserAddonUI.reportAddon()`, `this._getExtensionId()`

## _getExtensionId()
- 位置: L2963-2968
- 役割: メニューの対象項目から拡張 ID を取り出す。
- 触るとき: 右クリックメニューの対象拡張の特定方法を変えるとき。
- 呼び出し先: `triggerNode .closest()`, `triggerNode .closest(".unified-extensions-item") ?.querySelector()`
- 参照: `triggerNode .closest(".unified-extensions-item") ?.querySelector("toolbarbutton")?.dataset.extensionid`

## _getWidgetId()
- 位置: L2970-2973
- 役割: メニューの対象項目からウィジェット ID を取り出す。
- 触るとき: 右クリックメニューの対象ウィジェットの特定方法を変えるとき。
- 呼び出し先: `triggerNode.closest()`
- 参照: `triggerNode.closest(".unified-extensions-item")?.id`

## onPinToToolbarChange()
- 位置: async L2975-3001
- 役割: ピン留めの項目の変更を処理し、チェック表示は元に戻したうえでツールバーへの移動を行う。
- 触るとき: 右クリックからのツールバーへのピン留め操作を変えるとき。
- 呼び出し先: `event.target.hasAttribute()`, `event.target.toggleAttribute()`, `this._getWidgetId()`, `this.pinToToolbar()`
- 条件付き依存: `if (shouldPinToToolbar)` → `this._maybeMoveWidgetNodeBack()`

## pinToToolbar()
- 位置: L3003-3012
- 役割: ウィジェットをツールバーの navbar またはパネルの AREA_ADDONS に移す。
- 触るとき: ツールバーとパネルの間の拡張の移動先を変えるとき。
- 呼び出し先: `CustomizableUI.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_NAVBAR`

## moveWidget()
- 位置: async L3014-3045
- 役割: 右クリックの上/下操作で、隣の項目の位置を基に CUI 上でウィジェットを並べ替える。
- 触るとき: 拡張の並べ替え操作の位置計算を変えるとき。
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `menu.triggerNode.closest()`
- 条件付き依存: `if (placement)` → `CustomizableUI.moveWidgetWithinArea()`
- 参照: `element?.id`, `node.id`, `node.nextElementSibling`, `node.previousElementSibling`, `placement.position`

## onWidgetAdded()
- 位置: L3047-3064
- 役割: 拡張ウィジェットが追加された時に注意表示を更新し、溢れていなければパネル用か否かのクラス名を付け直す。
- 触るとき: ウィジェット追加時の表示クラスの決め方を変えるとき。
- 呼び出し先: `CustomizableUI.getAreaType()`, `CustomizableUI.getWidget()`, `CustomizableUI.getWidget(aWidgetId)?.forWindow()`, `CustomizableUI.isWebExtensionWidget()`, `this._updateWidgetClassName()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(aWidgetId))` → `this.updateAttention()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `CustomizableUI.getWidget(aWidgetId)?.forWindow(window)?.overflowed`

## onWidgetMoved()
- 位置: L3066-3070
- 役割: 拡張ウィジェットが移動した時に注意表示を更新する。
- 触るとき: ウィジェット移動時の注意表示の更新条件を変えるとき。
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(aWidgetId))` → `this.updateAttention()`

## onWidgetOverflow()
- 位置: L3072-3080
- 役割: この窓のウィジェットが溢れた時に、パネル用のクラス名へ切り替える。
- 触るとき: 溢れたウィジェットの見た目を変えるとき。
- 呼び出し先: `aNode.getAttribute()`, `this._updateWidgetClassName()`
- 参照: `aNode.documentGlobal`

## onWidgetUnderflow()
- 位置: L3082-3090
- 役割: この窓のウィジェットが溢れから戻った時に、ツールバー用のクラス名へ切り替える。
- 触るとき: 溢れから戻ったウィジェットの見た目を変えるとき。
- 呼び出し先: `aNode.getAttribute()`, `this._updateWidgetClassName()`
- 参照: `aNode.documentGlobal`

## onAreaNodeRegistered()
- 位置: L3092-3105
- 役割: この窓にエリアが登録された時に、そのエリアの拡張ウィジェットへクラス名を当てる。
- 触るとき: エリア登録時の初期表示を変えるとき。
- 呼び出し先: `CustomizableUI.getAreaType()`, `CustomizableUI.getWidgetIdsInArea()`, `this._updateWidgetClassName()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `aContainer.documentGlobal`

## _updateWidgetClassName()
- 位置: L3112-3134
- 役割: 拡張ウィジェットのアクションボタンと メニューボタンを、パネル用かツールバー用のクラスに切り替える。
- 触るとき: パネル内とツールバー内での拡張ボタンの見た目を変えるとき。
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidget(aWidgetId)?.forWindow()`, `CustomizableUI.isWebExtensionWidget()`, `node?.querySelector()`
- 条件付き依存: `if (actionButton)` → `actionButton.classList.toggle()`
- 条件付き依存: `if (menuButton)` → `menuButton.classList.toggle()`
- 参照: `CustomizableUI.getWidget(aWidgetId)?.forWindow(window)?.node`

## _createBlocklistMessageBar()
- 位置: L3136-3195
- 役割: ブロックリストの警告バーを作り、既存のものと差し替えるか、隔離警告の前に挿入する。閉じられたら記録を消す。
- 触るとき: ブロックリスト警告の文言・種類・閉じる動作を変えるとき。
- 呼び出し先: `container.contains()`, `messageBarBlocklist.addEventListener()`, `this._makeMessageBar()`, `this.blocklistAttentionInfo?.dismiss()`
- 条件付き依存: `if ( this._messageBarBlocklist && container.contains(this._messageBarBlocklist) )` → `container.replaceChild()`
- 条件付き依存: `if (!( this._messageBarBlocklist && container.contains(this._messageBarBlocklist) ))` → `container.contains()`
- 条件付き依存: `if (container.contains(this._messageBarQuarantinedDomain))` → `container.insertBefore()`
- 条件付き依存: `if (!(container.contains(this._messageBarQuarantinedDomain)))` → `container.appendChild()`
- 参照: `addons[0].name`, `this._messageBarBlocklist`, `this._messageBarQuarantinedDomain`, `this.blocklistAttentionInfo`

## _makeMessageBar()
- 位置: L3197-3253
- 役割: 種類、閉じるボタン、about:addons へのリンク、サポートページのリンクを持つ警告バーを組み立てる。
- 触るとき: 拡張パネルの警告バーの共通部品を変えるとき。
- 呼び出し先: `document.createElement()`, `document.l10n.setAttributes()`, `messageBar.classList.add()`, `messageBar.setAttribute()`
- 条件付き依存: `if (dismissible)` → `messageBar.setAttribute()`
- 条件付き依存: `if (linkToAboutAddons)` → `document.createElement()`
- 条件付き依存: `if (linkToAboutAddons)` → `linkToAboutAddonsEl.setAttribute()`
- 条件付き依存: `if (linkToAboutAddons)` → `linkToAboutAddonsEl.addEventListener()`
- 条件付き依存: `if (linkToAboutAddons)` → `BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (linkToAboutAddons)` → `this.togglePanel()`
- 条件付き依存: `if (linkToAboutAddons)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (linkToAboutAddons)` → `messageBar.append()`
- 条件付き依存: `if (supportPage)` → `document.createElement()`
- 条件付き依存: `if (supportPage)` → `supportUrl.setAttribute()`
- 条件付き依存: `if (supportPageFluentId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (supportPage)` → `messageBar.append()`

## _updateEmptyStateBox()
- 位置: L3255-3287
- 役割: パネルの空状態の見出し・説明・画像を設定し、表示・非表示を切り替える。
- 触るとき: 拡張パネルの空状態の表示を変えるとき。
- 呼び出し先: `panelview.querySelector()`
- 条件付き依存: `if (!hidden)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!hidden)` → `emptyStateBox.querySelector()`
- 条件付き依存: `if (!hidden)` → `img.classList.toggle()`
- 参照: `emptyStateBox.hidden`, `this.EMPTY_STATE_ILLUSTRATION_CLASS`, `this.EMPTY_STATE_ILLUSTRATION_ONBOARDING_CLASS`

## _createDiscoverButton()
- 位置: L3289-3306
- 役割: 拡張を探すボタンを作り、クリックで about:addons の discover ビューを開く。
- 触るとき: 拡張を探すボタンの動作や見た目を変えるとき。
- 呼び出し先: `BrowserAddonUI.openAddonsMgr()`, `discoverButton.addEventListener()`, `document.createElement()`, `document.l10n.setAttributes()`
- 参照: `discoverButton.className`, `discoverButton.id`, `discoverButton.type`

## _shouldShowQuarantinedNotification()
- 位置: L3308-3321
- 役割: 隔離ドメインを開いていて、パネルに拡張があり、そのうち隔離中のものがあるかを返す。
- 触るとき: 隔離ドメインの警告を出す条件を変えるとき。
- 呼び出し先: `WebExtensionPolicy.isQuarantinedURI()`, `lazy.OriginControls.getState()`, `this.getActivePolicies()`, `this.getActivePolicies().some()`, `this.hasExtensionsInPanel()`
- 参照: `lazy.OriginControls.getState(policy, selectedTab).quarantined`, `window.gBrowser`

## recordButtonTelemetry()
- 位置: L3331-3335
- 役割: 拡張ボタンが隠れている時の一時表示の理由を Glean に記録する。
- 触るとき: 拡張ボタンの一時表示の計測項目を変えるとき。
- 条件付き依存: `if (!this.buttonAlwaysVisible && this._button.hidden)` → `Glean.extensionsButton.temporarilyUnhidden[reason].add()`
- 参照: `Glean.extensionsButton.temporarilyUnhidden`, `this._button.hidden`, `this.buttonAlwaysVisible`

## hideExtensionsButtonFromToolbar()
- 位置: L3337-3356
- 役割: 常時表示の設定を外してボタンを隠し、確認ヒントと計測を出す。
- 触るとき: 拡張ボタンを隠すメニューの挙動を変えるとき。
- 呼び出し先: `ConfirmationHint.show()`, `CustomizationHandler.isCustomizing()`, `Glean.extensionsButton.toggleVisibility.record()`, `Services.prefs.setBoolPref()`, `document.getElementById()`, `this.hasExtensionsInPanel()`
- 参照: `this._button.hidden`
- XPCOM: `Services.prefs`

## showExtensionsButtonInToolbar()
- 位置: L3358-3371
- 役割: 常時表示の設定を入れてボタンを表示し、計測を記録する。
- 触るとき: 拡張ボタンを表示するメニューの挙動を変えるとき。
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `Glean.extensionsButton.toggleVisibility.record()`, `Services.prefs.setBoolPref()`, `this.hasExtensionsInPanel()`
- 参照: `this._button.hidden`, `this.buttonAlwaysVisible`
- XPCOM: `Services.prefs`
