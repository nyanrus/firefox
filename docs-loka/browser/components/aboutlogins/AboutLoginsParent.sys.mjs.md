# browser/components/aboutlogins/AboutLoginsParent.sys.mjs

source: browser/components/aboutlogins/AboutLoginsParent.sys.mjs
source-hash: 4021fadcc30686d93f331fe43d350162a6755eda
lines: 901

## <module>
- 役割: about:logins の親アクター AboutLoginsParent と、ログイン変更を購読してページへ配る AboutLoginsInternal(シングルトン)を定義する。
- 呼び出し先: `AboutLogins.onPasswordSyncEnabledPreferenceChange.bind()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.LoginHelper.createLogger()`

## convertSubjectToLogin()
- 位置: L61-68
- 役割: nsILoginInfo の subject をバニラオブジェクトに変換する。ユーザー向けのログインでなければ null を返し、そうでなければ title を付けて返す。
- 触るとき: 保存・変更の通知のうち、ページへ送るログインを絞る条件を変えるとき。
- 呼び出し先: `augmentVanillaLoginObject()`, `lazy.LoginHelper.isUserFacingLogin()`, `lazy.LoginHelper.loginToVanillaObject()`, `subject.QueryInterface()`, `subject.QueryInterface(Ci.nsILoginMetaInfo).QueryInterface()`
- 参照: `Ci.nsILoginInfo`, `Ci.nsILoginMetaInfo`
- XPCOM: [`nsILoginInfo`](../../../toolkit/components/passwordmgr/nsILoginInfo.idl.md) / [`nsILoginMetaInfo`](../../../toolkit/components/passwordmgr/nsILoginMetaInfo.idl.md)

## augmentVanillaLoginObject()
- 位置: L71-77
- 役割: displayOrigin の先頭の www 系サブドメインを外したものを title として付けた、ログインのコピーを返す。
- 触るとき: 一覧に出すサイト名の形式を変えるとき。
- 呼び出し先: `Object.assign()`, `login.displayOrigin.replace()`

## AboutLoginsParent.receiveMessage()
- 位置: async L85-162
- 役割: 送信元の remote type が privileged about であることを確かめ、購読者に加えてから、メッセージ名で各処理に振り分ける。想定外の remote type では例外を投げる。
- 触るとき: about:logins から届く新しいメッセージを扱うとき、または送信元の検査を変えるとき。
- 呼び出し先: `AboutLogins.subscribers.add()`, `this.#createLogin()`, `this.#deleteLogin()`, `this.#exportPasswords()`, `this.#getHelp()`, `this.#importFromBrowser()`, `this.#importFromFile()`, `this.#importReportInit()`, `this.#openPreferences()`, `this.#primaryPasswordRequest()`, `this.#removeAllLogins()`, `this.#sortChanged()`, `this.#subscribe()`, `this.#syncEnable()`, `this.#updateLogin()`
- 参照: `message.data`, `message.data.login`, `message.data.messageId`, `message.data.reason`, `message.name`, `this.browsingContext`, `this.browsingContext.embedderElement`, `this.manager.remoteType`

## AboutLoginsParent.#documentGlobal()
- 位置: L164-166
- 役割: embedderElement の documentGlobal を返す。無ければ undefined を返す。
- 触るとき: 親側からブラウザウィンドウの API(ダイアログや通知など)を呼ぶ経路を変えるとき。
- 参照: `this.browsingContext.embedderElement?.documentGlobal`

## AboutLoginsParent.#createLogin()
- 位置: async L168-201
- 役割: 主パスワードの方針で必要なら変更ダイアログを開く。origin をパス無しに正規化し、空のフォーム項目を入れて addLoginAsync で保存する。保存エラーは #handleLoginStorageErrors に渡す。
- 触るとき: 新規ログインの保存時の検証や、主パスワード要求の方針を変えるとき。
- 呼び出し先: `Object.assign()`, `Services.logins.addLoginAsync()`, `Services.policies.isAllowed()`, `lazy.LoginHelper.getLoginOrigin()`, `lazy.LoginHelper.vanillaObjectToLogin()`, `this.#handleLoginStorageErrors()`
- 条件付き依存: `if (!Services.policies.isAllowed("removeMasterPassword"))` → `lazy.LoginHelper.isPrimaryPasswordSet()`
- 条件付き依存: `if (!lazy.LoginHelper.isPrimaryPasswordSet())` → `this.#documentGlobal.openDialog()`
- 条件付き依存: `if (!lazy.LoginHelper.isPrimaryPasswordSet())` → `lazy.LoginHelper.isPrimaryPasswordSet()`
- 条件付き依存: `if (!origin)` → `console.error()`
- 参照: `newLogin.origin`
- XPCOM: `Services.logins` / `Services.policies`

## AboutLoginsParent.preselectedLogin()
- 位置: L203-212
- 役割: 選択中タブの preselect-login 属性、無ければ現在の URL の fragment を読んで選択対象の値にする。読んだ後に属性を削除するので、読み出し自体が副作用を持つ。
- 触るとき: 管理画面を開いたときに初めから選ばれているログインの決め方を変えるとき。
- 呼び出し先: `this.#documentGlobal?.gBrowser.selectedTab.getAttribute()`, `this.#documentGlobal?.gBrowser.selectedTab.removeAttribute()`
- 参照: `this.browsingContext.currentURI?.ref`

## AboutLoginsParent.#deleteLogin()
- 位置: async L214-217
- 役割: 受け取ったログインを removeLoginAsync で削除する。
- 触るとき: ログインの削除処理を変えるとき。
- 呼び出し先: `Services.logins.removeLoginAsync()`, `lazy.LoginHelper.vanillaObjectToLogin()`
- XPCOM: `Services.logins`

## AboutLoginsParent.#sortChanged()
- 位置: L219-221
- 役割: 並び順を signon.management.page.sort の pref に保存する。
- 触るとき: 並び順の保存先や値の形式を変えるとき。
- 呼び出し先: `Services.prefs.setCharPref()`
- XPCOM: `Services.prefs`

## AboutLoginsParent.#syncEnable()
- 位置: L223-225
- 役割: Sync のメールアドレス入力の最初のページを password-manager の文脈で開く。
- 触るとき: パスワード同期の有効化の入口を変えるとき。
- 呼び出し先: `this.#documentGlobal.gSync.openFxAEmailFirstPage()`

## AboutLoginsParent.#importFromBrowser()
- 位置: L227-235
- 役割: 他ブラウザからのインポートウィザードを passwords のエントリポイントで開く。例外はコンソールに出す。
- 触るとき: ブラウザからのインポートの入口を変えるとき。
- 呼び出し先: `console.error()`, `lazy.MigrationUtils.showMigrationWizard()`
- 参照: `lazy.MigrationUtils.MIGRATION_ENTRYPOINTS.PASSWORDS`, `this.#documentGlobal`

## AboutLoginsParent.#importReportInit()
- 位置: L237-240
- 役割: 直近のインポート報告を取得し、ImportReportData としてページへ送る。
- 触るとき: インポート報告ページに渡すデータを変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `lazy.LoginCSVImport.lastImportReport`

## AboutLoginsParent.#getHelp()
- 位置: L242-249
- 役割: サポート URL(password-manager-remember-delete-edit-logins)を関連タブとして新しいタブで開く。
- 触るとき: ヘルプのリンク先を変えるとき。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `this.#documentGlobal.openWebLinkIn()`
- XPCOM: `Services.urlFormatter`

## AboutLoginsParent.#openPreferences()
- 位置: L251-253
- 役割: 設定の privacy-logins のパネルを開く。
- 触るとき: パスワード関連の設定への導線を変えるとき。
- 呼び出し先: `this.#documentGlobal.openPreferences()`

## AboutLoginsParent.#primaryPasswordRequest()
- 位置: async L255-299
- 役割: messageId が無ければ例外を投げる。Windows と macOS で OS 認証が有効なら、そのプラットフォーム用の文言で再認証を要求し、結果を PrimaryPasswordResponse としてページへ返す。成功時は認証期限を更新し、AUTH_TIMEOUT_MS(5 分)後に再マスクのタイマーを張り直す。
- 触るとき: パスワードの再表示のための認証や、再マスクまでの時間を変えるとき。
- 呼び出し先: `lazy.LoginHelper.getOSAuthEnabled()`, `lazy.LoginHelper.requestReauth()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (isOSAuthEnabled)` → `lazy.AboutLoginsL10n.formatMessages()`
- 条件付き依存: `if (isAuthorized)` → `Date.now()`
- 条件付き依存: `if (isAuthorized)` → `clearTimeout()`
- 条件付き依存: `if (isAuthorized)` → `setTimeout()`
- 参照: `AboutLogins._authExpirationTime`, `AppConstants.platform`, `captionText.value`, `messageText.value`, `this.browsingContext.embedderElement`

## remaskPasswords()
- 位置: L293-295
- 役割: タイマーから呼ばれ、AboutLogins:RemaskPassword をページへ送る。
- 触るとき: 再マスクの通知の仕組みを変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsParent.#subscribe()
- 位置: async L301-345
- 役割: 認証期限を初期化し監視を開始する。全ログインと同期状態を取り、並び順(旧 breached は alerts に読み替え)や主パスワード・表示可否・インポート可否(Linux では不可)・初期選択を Setup としてページへ送り、続けて関連情報を送る。NOT_INITIALIZED の例外だけは握りつぶす。
- 触るとき: about:logins を開いたときの初期データの組み立てを変えるとき。
- 呼び出し先: `AboutLogins.addObservers()`, `AboutLogins.getAllLogins()`, `AboutLogins.getSyncState()`, `AboutLogins.sendAllLoginRelatedObjects()`, `Services.policies.isAllowed()`, `Services.prefs.getCharPref()`, `lazy.LoginHelper.isPrimaryPasswordSet()`, `lazy.log.debug()`, `this.sendAsyncMessage()`
- 参照: `AboutLogins._authExpirationTime`, `AppConstants.platform`, `Cr.NS_ERROR_NOT_INITIALIZED`, `Number.NEGATIVE_INFINITY`, `ex.result`, `this.browsingContext`, `this.preselectedLogin`
- XPCOM: `Services.policies` / `Services.prefs`

## AboutLoginsParent.#updateLogin()
- 位置: async L347-370
- 役割: guid で保存済みログインを検索し、1 件のときだけ clone に username と password の変更を反映して modifyLoginAsync で保存する。件数が 1 でなければ警告して終える。保存エラーは #handleLoginStorageErrors に渡す。
- 触るとき: ログインの編集で保存できる項目や、保存時のエラー処理を変えるとき。
- 呼び出し先: `Services.logins.modifyLoginAsync()`, `Services.logins.searchLoginsAsync()`, `loginUpdates.hasOwnProperty()`, `logins[0].clone()`, `this.#handleLoginStorageErrors()`
- 条件付き依存: `if (logins.length != 1)` → `lazy.log.warn()`
- 参照: `loginUpdates.guid`, `loginUpdates.password`, `loginUpdates.username`, `logins.length`, `modifiedLogin.password`, `modifiedLogin.username`
- XPCOM: `Services.logins`

## AboutLoginsParent.#exportPasswords()
- 位置: async L372-452
- 役割: Windows と macOS で OS 認証が有効なら、そのプラットフォーム用の文言で再認証を要求する。承認後は、フォーカスが戻るのを待ってから CSV 保存のファイルピッカーを開く。
- 触るとき: エクスポートの認証の順序やファイル保存の流れを変えるとき。
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `fp.appendFilter()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`, `lazy.AboutLoginsL10n.formatValues()`, `lazy.LoginHelper.getOSAuthEnabled()`, `lazy.LoginHelper.recordReauthTelemetryEvent()`, `lazy.LoginHelper.requestReauth()`
- 条件付き依存: `if (isOSAuthEnabled)` → `lazy.AboutLoginsL10n.formatMessages()`
- 条件付き依存: `if (!this.browsingContext.canOpenModalPicker)` → `this.sendQuery()`
- 参照: `AppConstants.platform`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterAll`, `Ci.nsIFilePicker.modeSave`, `captionText.value`, `fp.defaultExtension`, `fp.defaultString`, `fp.okButtonLabel`, `messageText.value`, `this.browsingContext`, `this.browsingContext.canOpenModalPicker`, `this.browsingContext.embedderElement`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## fpCallback()
- 位置: L423-428
- 役割: ファイルピッカーがキャンセル以外で閉じたら、選ばれたパスへ LoginExport.exportAsCSV で書き出し、完了を Glean に記録する。
- 触るとき: エクスポートの完了後の処理や計測を変えるとき。
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `lazy.LoginExport.exportAsCSV()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `Glean.pwmgr.mgmtMenuItemUsedExportComplete.record()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `fp.file.path`
- XPCOM: `nsIFilePicker`

## AboutLoginsParent.#importFromFile()
- 位置: async L454-501
- 役割: CSV と TSV のフィルタ付きでファイルを選ばせ、importFromCSV で取り込む。成功すると ImportPasswordsDialog、失敗すると ImportPasswordsErrorDialog をページへ送り、成功時は完了を記録する。
- 触るとき: インポートの結果通知やエラー種別の扱いを変えるとき。
- 呼び出し先: `lazy.AboutLoginsL10n.formatValues()`, `this.openFilePickerDialog()`
- 条件付き依存: `if (result != Ci.nsIFilePicker.returnCancel)` → `lazy.LoginCSVImport.importFromCSV()`
- 条件付き依存: `if (result != Ci.nsIFilePicker.returnCancel)` → `console.error()`
- 条件付き依存: `if (result != Ci.nsIFilePicker.returnCancel)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (summary)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (summary)` → `Glean.pwmgr.mgmtMenuItemUsedImportCsvComplete.record()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `e.errorType`
- XPCOM: `nsIFilePicker`

## AboutLoginsParent.#removeAllLogins()
- 位置: async L503-505
- 役割: ユーザー向けの全ログインを removeAllUserFacingLoginsAsync で削除する。
- 触るとき: すべて削除の処理を変えるとき。
- 呼び出し先: `Services.logins.removeAllUserFacingLoginsAsync()`
- XPCOM: `Services.logins`

## AboutLoginsParent.#handleLoginStorageErrors()
- 位置: L507-522
- 役割: ログインのエラーメッセージを ShowLoginItemError としてページへ送る。「This login already exists」の場合は、既存ログインの GUID も付ける。
- 触るとき: 保存時の重複エラーの表示内容を変えるとき。
- 呼び出し先: `augmentVanillaLoginObject()`, `error.message.includes()`, `lazy.LoginHelper.loginToVanillaObject()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (error.message.includes("This login already exists"))` → `error.data.toString()`
- 参照: `error.message`, `messageObject.existingLoginGuid`

## AboutLoginsParent.openFilePickerDialog()
- 位置: async L524-537
- 役割: open モードのファイルピッカーを作り、渡されたフィルタとすべてのファイルを付けて開く。結果と選ばれたパスを Promise で返す。
- 触るとき: ファイル選択ダイアログの種類やフィルタを変えるとき。
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `fp.appendFilter()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`, `resolve()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterAll`, `Ci.nsIFilePicker.modeOpen`, `appendFilter.extensionPattern`, `appendFilter.title`, `fp.file.path`, `fp.okButtonLabel`, `this.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## AboutLoginsInternal.observe()
- 位置: async L546-594
- 役割: 購読者が 1 人もいなければ監視を外して終える。トピックに応じて、ログインの再読み込み・主パスワードの通知・同期状態の更新・ログインの追加・変更・削除をページへ反映する。
- 触るとき: ログインの保存の変更をページへ反映する経路を変えるとき。
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `this.#addLogin()`, `this.#messageSubscribers()`, `this.#modifyLogin()`, `this.#reloadAllLogins()`, `this.#removeAllLogins()`, `this.#removeLogin()`, `this.#removeNotifications()`, `this.#showPrimaryPasswordLoginNotifications()`, `this.getSyncState()`
- 条件付き依存: `if (!ChromeUtils.nondeterministicGetWeakSetKeys(this.subscribers).length)` → `this.#removeObservers()`
- 参照: `ChromeUtils.nondeterministicGetWeakSetKeys(this.subscribers).length`, `lazy.UIState.ON_UPDATE`, `this.subscribers`

## AboutLoginsInternal.#addLogin()
- 位置: async L596-621
- 役割: 変換したログインについて、侵害警告と脆弱パスワードの判定が有効なら結果を送り、変更ページ URL を送ってから LoginAdded を送る。
- 触るとき: 追加時に一覧へ反映する情報の順序や内容を変えるとき。
- 呼び出し先: `convertSubjectToLogin()`, `lazy.ChangePasswordURLs.getChangePasswordURLsByLoginGUID()`, `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `lazy.LoginBreaches.getPotentialBreachesByLoginGUID()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `lazy.LoginBreaches.getPotentiallyVulnerablePasswordsByLoginGUID()`
- 参照: `lazy.BREACH_ALERTS_ENABLED`, `lazy.VULNERABLE_PASSWORDS_ENABLED`

## AboutLoginsInternal.#modifyLogin()
- 位置: async L623-657
- 役割: このログイン 1 件について侵害と脆弱の判定を行い、結果を 1 件分の Map として送る。続けて変更ページ URL を送り、LoginModified を送る。
- 触るとき: 編集後に警告の表示が古いままになる問題を調べるとき。
- 呼び出し先: `convertSubjectToLogin()`, `lazy.ChangePasswordURLs.getChangePasswordURLsByLoginGUID()`, `subject.GetElementAt()`, `subject.QueryInterface()`, `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `lazy.LoginBreaches.getPotentialBreachesByLoginGUID()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `breachesForThisLogin.get()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `lazy.LoginBreaches.getPotentiallyVulnerablePasswordsByLoginGUID()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `this.#messageSubscribers()`
- 参照: `Ci.nsIArrayExtensions`, `breachesForThisLogin.size`, `lazy.BREACH_ALERTS_ENABLED`, `lazy.VULNERABLE_PASSWORDS_ENABLED`, `login.guid`, `vulnerablePasswordsForThisLogin.size`
- XPCOM: [`nsIArrayExtensions`](../../../xpcom/ds/nsIArrayExtensions.idl.md)

## AboutLoginsInternal.#removeLogin()
- 位置: L659-665
- 役割: 変換したログインを LoginRemoved として購読者に送る。
- 触るとき: 削除時に一覧から外す通知を変えるとき。
- 呼び出し先: `convertSubjectToLogin()`, `this.#messageSubscribers()`

## AboutLoginsInternal.#removeAllLogins()
- 位置: async L667-669
- 役割: 空の配列を添えて RemoveAllLogins を購読者に送る。
- 触るとき: すべて削除後の通知内容を変えるとき。
- 呼び出し先: `this.#messageSubscribers()`

## AboutLoginsInternal.#reloadAllLogins()
- 位置: async L671-675
- 役割: 全ログインを取得して AllLogins を送り、続けて関連情報を送る。
- 触るとき: 全件の再読み込みの流れを変えるとき。
- 呼び出し先: `this.#messageSubscribers()`, `this.getAllLogins()`, `this.sendAllLoginRelatedObjects()`

## AboutLoginsInternal.#showPrimaryPasswordLoginNotifications()
- 位置: L677-691
- 役割: 各購読者の画面に主パスワードの要求通知(再読み込みボタン付き)を出し、PrimaryPasswordAuthRequired をページへ送る。
- 触るとき: 主パスワード要求の通知の文言やボタンを変えるとき。
- 呼び出し先: `this.#messageSubscribers()`, `this.#showNotifications()`

## onReloadClick()
- 位置: L685-687
- 役割: 通知のボタンが押されたら、対象のブラウザを再読み込みする。
- 触るとき: 主パスワード通知の再読み込みの動作を変えるとき。
- 呼び出し先: `browser.reload()`

## AboutLoginsInternal.#showNotifications()
- 位置: L693-739
- 役割: 各購読者の通知ボックスに、同じ ID の通知が無ければ、ボタンと onClicks を付けた通知を追加する。
- 触るとき: 通知の表示条件・優先度・文言を変えるとき。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `gBrowser.getNotificationBox()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.#subscriberIterator()`
- 参照: `browser.documentGlobal`, `browser.documentGlobal.MozXULElement`, `buttonIds.length`, `subscriber.embedderElement`

## callback()
- 位置: L723-725
- 役割: 通知のボタンが押されたら、対応する onClicks をブラウザを渡して実行する。
- 触るとき: 通知ボタンの動作を変えるとき。
- 呼び出し先: `onClicks[i]()`

## AboutLoginsInternal.#removeNotifications()
- 位置: L741-753
- 役割: 各購読者の通知ボックスから、指定 ID の通知を外す。
- 触るとき: 通知を消す条件を変えるとき。
- 呼び出し先: `gBrowser.getNotificationBox()`, `notificationBox.getNotificationWithValue()`, `notificationBox.removeNotification()`, `this.#subscriberIterator()`
- 参照: `browser.documentGlobal`, `subscriber.embedderElement`

## AboutLoginsInternal.#subscriberIterator()
- 位置: L755-770
- 役割: 購読者のうち、about:logins の privileged content で動いているものだけを列挙する。条件を満たさない購読者は購読から外す。
- 触るとき: 購読者の絞り込みや掃除の条件を変えるとき。
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`
- 条件付き依存: `if ( browser?.remoteType != EXPECTED_ABOUTLOGINS_REMOTE_TYPE || browser?.contentPrincipal?.originNoSuffix != ABOUT_LOGINS_ORIGIN )` → `this.subscribers.delete()`
- 参照: `browser?.contentPrincipal?.originNoSuffix`, `browser?.remoteType`, `subscriber.embedderElement`, `this.subscribers`

## AboutLoginsInternal.#messageSubscribers()
- 位置: L772-791
- 役割: 各購読者のウィンドウのアクターへ name と details を送る。ウィンドウが破棄済みで NOT_INITIALIZED の場合は無視する。
- 触るとき: 全購読者への通知の送り方や例外処理を変えるとき。
- 呼び出し先: `this.#subscriberIterator()`
- 条件付き依存: `if (subscriber.currentWindowGlobal)` → `subscriber.currentWindowGlobal.getActor()`
- 条件付き依存: `if (subscriber.currentWindowGlobal)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (ex.result == Cr.NS_ERROR_NOT_INITIALIZED)` → `lazy.log.debug()`
- 参照: `Cr.NS_ERROR_NOT_INITIALIZED`, `ex.result`, `subscriber.currentWindowGlobal`

## AboutLoginsInternal.getAllLogins()
- 位置: async L793-806
- 役割: ユーザー向けログインを取得し、バニラ化してから title を付ける。主パスワードの入力がキャンセルされた(NS_ERROR_ABORT)場合は空の配列を返す。
- 触るとき: ページに渡す全件の内容や、主パスワードのキャンセル時の扱いを変えるとき。
- 呼び出し先: `lazy.LoginHelper.getAllUserFacingLogins()`, `logins .map()`, `logins .map(lazy.LoginHelper.loginToVanillaObject) .map()`
- 参照: `Cr.NS_ERROR_ABORT`, `e.result`, `lazy.LoginHelper.loginToVanillaObject`

## AboutLoginsInternal.sendAllLoginRelatedObjects()
- 位置: async L808-837
- 役割: 侵害・脆弱・変更ページ URL の情報を計算し、browsingContext があればそこへ、無ければ全購読者へ送る。
- 触るとき: 一覧の初期表示や更新時に付随して送る情報を増やすとき。
- 呼び出し先: `lazy.ChangePasswordURLs.getChangePasswordURLsByLoginGUID()`, `sendMessageFn()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `sendMessageFn()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `lazy.LoginBreaches.getPotentialBreachesByLoginGUID()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `sendMessageFn()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `lazy.LoginBreaches.getPotentiallyVulnerablePasswordsByLoginGUID()`
- 参照: `lazy.BREACH_ALERTS_ENABLED`, `lazy.VULNERABLE_PASSWORDS_ENABLED`

## sendMessageFn()
- 位置: L809-816
- 役割: browsingContext の現在のウィンドウのアクターへ送る。無ければ #messageSubscribers に任せる。
- 触るとき: 付随情報の送り先を変えるとき。
- 条件付き依存: `if (browsingContext?.currentWindowGlobal)` → `browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if (browsingContext?.currentWindowGlobal)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (!(browsingContext?.currentWindowGlobal))` → `this.#messageSubscribers()`
- 参照: `browsingContext?.currentWindowGlobal`

## AboutLoginsInternal.getSyncState()
- 位置: async L839-857
- 役割: UIState から、同期が設定されているか(loggedIn)、メール、アバター、FxA の有効状態、パスワード同期の有効状態、アカウント管理 URL をまとめて返す。
- 触るとき: 同期状態としてページに渡す項目を増やすとき。
- 呼び出し先: `lazy.FxAccounts.config.promiseManageURI()`, `lazy.UIState.get()`
- 参照: `lazy.FXA_ENABLED`, `lazy.PASSWORD_SYNC_ENABLED`, `lazy.UIState.STATUS_NOT_CONFIGURED`, `state.avatarURL`, `state.email`, `state.status`, `state.syncEnabled`

## AboutLoginsInternal.onPasswordSyncEnabledPreferenceChange()
- 位置: async L859-864
- 役割: パスワード同期の pref が変わったら、最新の同期状態を全購読者に送る。
- 触るとき: 同期の設定変更がページに反映されない問題を調べるとき。
- 呼び出し先: `this.#messageSubscribers()`, `this.getSyncState()`

## AboutLoginsInternal.addObservers()
- 位置: L874-881
- 役割: 監視対象のトピックを、まだ登録していなければ一度だけ登録する。
- 触るとき: about:logins の監視対象トピックを増やすとき。
- 条件付き依存: `if (!this.#observersAdded)` → `Services.obs.addObserver()`
- 参照: `this.#observedTopics`, `this.#observersAdded`
- XPCOM: `Services.obs`

## AboutLoginsInternal.#removeObservers()
- 位置: L883-888
- 役割: 監視対象のトピックをすべて登録解除し、登録フラグを戻す。
- 触るとき: 購読者が 0 になったときの監視解除の条件を変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this.#observedTopics`, `this.#observersAdded`
- XPCOM: `Services.obs`
