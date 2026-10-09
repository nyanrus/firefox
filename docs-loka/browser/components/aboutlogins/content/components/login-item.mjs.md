# browser/components/aboutlogins/content/components/login-item.mjs

source: browser/components/aboutlogins/content/components/login-item.mjs
source-hash: 2309c29fb6f427825b6d91b3d5a1ef537af42376
lines: 1062

## <module>
- 役割: about:logins の単一ログイン詳細パネル(login-item カスタム要素)の表示・編集・コピー・削除・確認ダイアログ処理をまとめたモジュール
- 呼び出し先: `customElements.define()`

## LoginItem.COPY_BUTTON_RESET_TIMEOUT()
- 位置: L16-18
- 役割: コピー成功表示を元に戻すまでの待ち時間(5000ms)を返す静的getter
- 触るとき: 「コピー済み」表示の持続時間を変えたいとき。handleCopyPasswordClick と handleCopyUsernameClick のタイマーがこの値を使う

## LoginItem.constructor()
- 位置: L20-26
- 役割: 内部状態(_login、_error、コピー用タイマーID)を初期化する
- 触るとき: 新しい状態フィールドを足すとき、またはログイン未選択時の初期値を確認したいとき
- 呼び出し先: `super()`
- 参照: `this._copyPasswordTimeoutId`, `this._copyUsernameTimeoutId`, `this._error`, `this._login`

## LoginItem.connectedCallback()
- 位置: L28-172
- 役割: テンプレートから shadow DOM を一度だけ組み立て、子要素の参照取得と各種イベントリスナーの登録を行う
- 触るとき: ボタンやフォームを追加・改名したとき、またはイベント配線(click/blur/keydown など)が効かない原因を探すとき。既に shadowRoot があれば render() だけ呼ぶ
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `loginItemTemplate.content.cloneNode()`, `shadowRoot.appendChild()`, `this._cancelButton.addEventListener()`, `this._copyPasswordButton.addEventListener()`, `this._copyUsernameButton.addEventListener()`, `this._deleteButton.addEventListener()`, `this._editButton.addEventListener()`, `this._errorMessage.querySelector()`, `this._errorMessageLink.addEventListener()`, `this._form.addEventListener()`, `this._originDisplayInput.addEventListener()`, `this._originInput.addEventListener()`, `this._passwordDisplayInput.addEventListener()`, `this._passwordInput.addEventListener()`, `this._revealCheckbox.addEventListener()`, `this.addHTTPSPrefix()`, `this.attachShadow()`, `this.handleAboutLoginsInitial()`, `this.handleAboutLoginsLoginSelected()`, `this.handleAboutLoginsRemaskPassword()`, `this.handleAboutLoginsShowBlankLogin()`, `this.handleCancelEvent()`, `this.handleCopyPasswordClick()`, `this.handleCopyUsernameClick()`, `this.handleDeleteEvent()`, `this.handleDuplicateErrorGuid()`, `this.handleEditEvent()`, `this.handleEditPasswordInputBlur()`, `this.handleInputAuxclick()`, `this.handleInputMousedown()`, `this.handleInputSubmit()`, `this.handleKeydown()`, `this.handleOriginInputClick()`, `this.handlePasswordDisplayBlur()`, `this.handlePasswordDisplayFocus()`, `this.handleRevealPasswordClick()`, `this.render()`, `this.shadowRoot.querySelector()`, `window.addEventListener()`
- 条件付き依存: `if (this.shadowRoot)` → `this.render()`
- 参照: `this._breachAlert`, `this._cancelButton`, `this._confirmDeleteDialog`, `this._copyPasswordButton`, `this._copyUsernameButton`, `this._deleteButton`, `this._editButton`, `this._errorMessage`, `this._errorMessageLink`, `this._errorMessageText`, `this._favicon`, `this._form`, `this._originDisplayInput`, `this._originInput`, `this._originWarning`, `this._passwordDisplayInput`, `this._passwordInput`, `this._passwordWarning`, `this._revealCheckbox`, `this._saveChangesButton`, `this._title`, `this._usernameInput`, `this._vulnerableAlert`, `this.dataset.editing`, `this.shadowRoot`

## LoginItem.focus()
- 位置: L174-182
- 役割: 編集ボタン、削除ボタン、オリジン入力の順で、最初に無効化されていないものへフォーカスを移す
- 触るとき: ログイン選択後のフォーカス位置を変えたいとき、または編集ボタンが無効のときのフォーカス先を確認したいとき
- 条件付き依存: `if (!this._editButton.disabled)` → `this._editButton.focus()`
- 条件付き依存: `if (!this._deleteButton.disabled)` → `this._deleteButton.focus()`
- 条件付き依存: `if (!(!this._deleteButton.disabled))` → `this._originInput.focus()`
- 参照: `this._deleteButton.disabled`, `this._editButton.disabled`

## LoginItem.render()
- 位置: async L184-275
- 役割: 現在の _login の内容を各入力欄、favicon、侵害/脆弱アラート、タイムラインへ反映する
- 触るとき: 表示項目を増やすとき、またはログイン切り替え後に古い値が残る不具合を調べるとき。onlyUpdateErrorsAndAlerts 指定時はエラーとアラートだけ更新して返る
- 呼び出し先: `document.l10n.setAttributes()`, `this.#updatePasswordMessage()`, `this.#updateTimeline()`, `this._breachesMap.has()`, `this._updateOriginDisplayState()`, `this._updatePasswordRevealState()`, `this._vulnerableLoginsMap.has()`
- 条件付き依存: `if (this._error)` → `this._error.errorMessage.includes()`
- 条件付き依存: `if (this._error.errorMessage.includes("This login already exists"))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!this._breachAlert.hidden)` → `this._breachesMap.get()`
- 条件付き依存: `if (!this._breachAlert.hidden)` → `new Date(breachDetails.BreachDate ?? 0).getTime()`
- 条件付き依存: `if (!this._breachAlert.hidden)` → `this.#updateBreachAlert()`
- 条件付き依存: `if (!this._vulnerableAlert.hidden)` → `this.#updateVulnerablePasswordAlert()`
- 条件付き依存: `if (this.dataset.editing)` → `this._usernameInput.removeAttribute()`
- 条件付き依存: `if (!(this.dataset.editing))` → `document.l10n.setAttributes()`
- 参照: `breachDetails.BreachDate`, `breachDetails.Name`, `this._breachAlert.hidden`, `this._breachesMap`, `this._copyUsernameButton.disabled`, `this._error`, `this._error.existingLoginGuid`, `this._error.login.title`, `this._errorMessage.hidden`, `this._errorMessageLink`, `this._errorMessageLink.dataset.errorGuid`, `this._errorMessageLink.hidden`, `this._errorMessageText.hidden`, `this._favicon.src`, `this._login.guid`, `this._login.origin`, `this._login.password`, `this._login.title`, `this._login.username`, `this._originDisplayInput.href`, `this._originDisplayInput.innerText`, `this._originInput.defaultValue`, `this._passwordDisplayInput.value`, `this._passwordInput.value`, `this._saveChangesButton`, `this._title.textContent`, `this._title.title`, `this._usernameInput`, `this._usernameInput.defaultValue`, `this._usernameInput.placeholder`, `this._vulnerableAlert.hidden`, `this._vulnerableLoginsMap`, `this.dataset.editing`, `this.dataset.isNewLogin`

## LoginItem.#updateTimeline()
- 位置: L277-296
- 役割: 作成日時、パスワード変更日時、最終使用日時からタイムラインの履歴項目を組み立てる
- 触るとき: タイムラインに出す出来事を追加・削除するとき。パスワード変更日時が作成日時と同じなら変更項目を省く
- 呼び出し先: `this.shadowRoot.querySelector()`
- 参照: `this._login.guid`, `this._login.timeCreated`, `this._login.timeLastUsed`, `this._login.timePasswordChanged`, `timeline.hidden`, `timeline.history`

## LoginItem.setBreaches()
- 位置: L298-300
- 役割: 漏えい情報のマップ(GUID単位)を置き換えて再描画する
- 触るとき: Monitor から全件の侵害データが届く経路を変えるとき
- 呼び出し先: `this._internalSetMonitorData()`

## LoginItem.updateBreaches()
- 位置: L302-304
- 役割: 漏えい情報を差分で更新する(_internalUpdateMonitorData に委譲)
- 触るとき: 侵害データが個別に追加・解除されたときの反映処理を調べるとき
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginItem.setVulnerableLogins()
- 位置: L306-311
- 役割: 脆弱なパスワードのマップを置き換えて再描画する
- 触るとき: 脆弱性情報の受け渡しを変えるとき
- 呼び出し先: `this._internalSetMonitorData()`

## LoginItem.updateVulnerableLogins()
- 位置: L313-318
- 役割: 脆弱性情報を差分で更新する
- 触るとき: 脆弱性データの個別更新処理を調べるとき
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginItem.setChangePasswordURLs()
- 位置: L320-325
- 役割: パスワード変更 URL のマップを置き換えて再描画する
- 触るとき: 侵害・脆弱アラートに出すパスワード変更リンクの供給元を変えるとき
- 呼び出し先: `this._internalSetMonitorData()`

## LoginItem.updateChangePasswordURLs()
- 位置: L327-332
- 役割: パスワード変更 URL のマップを差分で更新する
- 触るとき: 変更 URL の個別更新で表示がずれるとき
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginItem._internalSetMonitorData()
- 位置: L334-337
- 役割: 指定の内部メンバーへマップを代入し、エラーとアラートだけを再描画する
- 触るとき: Monitor 系の setXxx 全般の共通経路を変えるとき
- 呼び出し先: `this.render()`

## LoginItem._internalUpdateMonitorData()
- 位置: L339-351
- 役割: マップの各エントリを追加(データあり)または削除(null)し、結果を _internalSetMonitorData に渡す
- 触るとき: 差分更新で null を削除扱いにする仕様を変えたいとき、または更新が反映されない原因を調べるとき
- 呼び出し先: `this._internalSetMonitorData()`
- 条件付き依存: `if (data)` → `this[internalMemberName].set()`
- 条件付き依存: `if (!(data))` → `this[internalMemberName].delete()`

## LoginItem.showLoginItemError()
- 位置: L353-356
- 役割: エラー情報を _error に保存して再描画し、重複エラーのリンクなどを表示する
- 触るとき: 保存失敗時のエラー表示を変えるとき
- 呼び出し先: `this.render()`
- 参照: `this._error`

## LoginItem.handleKeydown()
- 位置: async L358-367
- 役割: Escape で編集を取り消し、Alt+Enter で編集開始、Alt+Backspace か Alt+Delete で削除確認を開く
- 触るとき: キーボードショートカットを追加・変更するとき。編集中かどうかで有効なキーが変わる
- 条件付き依存: `if (e.key === "Escape" && this.dataset.editing)` → `this.handleCancelEvent()`
- 条件付き依存: `if (e.altKey && e.key === "Enter" && !this.dataset.editing)` → `this.handleEditEvent()`
- 条件付き依存: `if (e.altKey && (e.key === "Backspace" || e.key === "Delete"))` → `this.handleDeleteEvent()`
- 参照: `e.altKey`, `e.key`, `this.dataset.editing`

## LoginItem.handlePasswordDisplayFocus()
- 位置: async L369-383
- 役割: パスワード表示欄のフォーカス時に、表示切替チェックボックスの状態を合わせて reveal 状態を更新する
- 触るとき: パスワード欄へのフォーカス動作やマスク解除の流れを変えるとき。チェックボックスから来た場合は早期に戻る(Bug 1838494 の暫定処理)
- 呼び出し先: `this._updatePasswordRevealState()`
- 参照: `e.relatedTarget`, `this._passwordInput.type`, `this._revealCheckbox`, `this._revealCheckbox.checked`, `this.dataset.editing`, `this.dataset.isNewLogin`

## LoginItem.addHTTPSPrefix()
- 位置: async L385-402
- 役割: オリジン欄の値に スキーマがなければ https:// を付ける
- 触るとき: URL 入力の補完規則を変えるとき。チェックボックスへフォーカスが移った場合は何もしない
- 呼び出し先: `originValue.match()`, `this._originInput.value.trim()`
- 参照: `e.relatedTarget`, `this._originInput.value`, `this._revealCheckbox`

## LoginItem.handlePasswordDisplayBlur()
- 位置: async L404-416
- 役割: マスク表示欄からフォーカスが外れたとき、チェックボックスを編集状態に合わせ、reveal 状態更新と https 補完を行う
- 触るとき: フォーカス移動時のパスワード表示の戻り方を調べるとき
- 呼び出し先: `this._updatePasswordRevealState()`, `this.addHTTPSPrefix()`
- 参照: `e.relatedTarget`, `this._revealCheckbox`, `this._revealCheckbox.checked`, `this.dataset.editing`

## LoginItem.handleEditPasswordInputBlur()
- 位置: async L418-430
- 役割: 編集中のパスワード欄からフォーカスが外れたとき、表示切替を解除し https 補完を行う
- 触るとき: 編集欄を離れたときのパスワード表示の扱いを変えるとき
- 呼び出し先: `this._updatePasswordRevealState()`, `this.addHTTPSPrefix()`
- 参照: `e.relatedTarget`, `this._revealCheckbox`, `this._revealCheckbox.checked`

## LoginItem.handleRevealPasswordClick()
- 位置: async L432-458
- 役割: 編集中・新規作成中は入力欄をそのまま表示し、閲覧中は表示切替時にプライマリパスワードを確認してから表示状態を更新する
- 触るとき: パスワードの表示切替やプライマリパスワード確認の挙動を変えるとき。表示時には reveal 系のテレメトリを送る
- 呼び出し先: `this._recordTelemetryEvent()`, `this._updatePasswordRevealState()`
- 条件付き依存: `if (this.dataset.editing || this.dataset.isNewLogin)` → `this._passwordDisplayInput.replaceWith()`
- 条件付き依存: `if (this.dataset.editing || this.dataset.isNewLogin)` → `this._passwordInput.focus()`
- 条件付き依存: `if (this._revealCheckbox.checked && !this.dataset.editing)` → `promptForPrimaryPassword()`
- 参照: `this._passwordInput`, `this._passwordInput.type`, `this._revealCheckbox.checked`, `this.dataset.editing`, `this.dataset.isNewLogin`

## LoginItem.handleCancelEvent()
- 位置: async L460-488
- 役割: 編集の取り消しを行う。既存ログインは未保存の変更があれば破棄確認を出して元に戻し、新規ログインは選択解除する
- 触るとき: キャンセル時の確認ダイアログや、新規作成の取り消し後の画面状態を変えるとき
- 条件付き依存: `if (wasExistingLogin)` → `this.hasPendingChanges()`
- 条件付き依存: `if (this.hasPendingChanges())` → `this.showConfirmationDialog()`
- 条件付き依存: `if (this.hasPendingChanges())` → `this.setLogin()`
- 条件付き依存: `if (!(this.hasPendingChanges()))` → `this.setLogin()`
- 条件付き依存: `if (!(wasExistingLogin))` → `this.hasPendingChanges()`
- 条件付き依存: `if (!this.hasPendingChanges())` → `window.dispatchEvent()`
- 条件付き依存: `if (!this.hasPendingChanges())` → `this._recordTelemetryEvent()`
- 条件付き依存: `if (!this.hasPendingChanges())` → `this.setLogin()`
- 条件付き依存: `if (!this.hasPendingChanges())` → `this._toggleEditing()`
- 条件付き依存: `if (!this.hasPendingChanges())` → `this.render()`
- 条件付き依存: `if (!(!this.hasPendingChanges()))` → `this.showConfirmationDialog()`
- 条件付き依存: `if (!(!this.hasPendingChanges()))` → `window.dispatchEvent()`
- 条件付き依存: `if (!(!this.hasPendingChanges()))` → `this.setLogin()`
- 条件付き依存: `if (!(!this.hasPendingChanges()))` → `this._toggleEditing()`
- 条件付き依存: `if (!(!this.hasPendingChanges()))` → `this.render()`
- 参照: `this._login`, `this._login.guid`

## LoginItem.handleCopyPasswordClick()
- 位置: async L490-527
- 役割: プライマリパスワードを確認してからパスワードを AboutLoginsCopyLoginDetail で送り、ボタンを一時的に「コピー済み」にする
- 触るとき: パスワードのコピー動作、認証タイミング、テレメトリを変えるとき
- 呼び出し先: `clearTimeout()`, `document.dispatchEvent()`, `promptForPrimaryPassword()`, `setTimeout()`, `this._recordTelemetryEvent()`
- 参照: `LoginItem.COPY_BUTTON_RESET_TIMEOUT`, `currentTarget.copiedText`, `currentTarget.dataset.copied`, `currentTarget.disabled`, `this._copyPasswordTimeoutId`, `this._copyUsernameButton.copiedText`, `this._copyUsernameButton.dataset.copied`, `this._copyUsernameButton.disabled`, `this._copyUsernameTimeoutId`, `this._login.password`, `this._login.username`

## LoginItem.handleCopyUsernameClick()
- 位置: async L529-558
- 役割: ユーザー名を AboutLoginsCopyLoginDetail で送り、ボタンを一時的に「コピー済み」にする
- 触るとき: ユーザー名のコピー動作や表示のリセットを変えるとき。パスワード側の状態も同時に解除する
- 呼び出し先: `clearTimeout()`, `document.dispatchEvent()`, `setTimeout()`, `this._recordTelemetryEvent()`
- 参照: `LoginItem.COPY_BUTTON_RESET_TIMEOUT`, `currentTarget.copiedText`, `currentTarget.dataset.copied`, `currentTarget.disabled`, `this._copyPasswordButton.copiedText`, `this._copyPasswordButton.dataset.copied`, `this._copyPasswordButton.disabled`, `this._copyPasswordTimeoutId`, `this._copyUsernameTimeoutId`, `this._login.username`

## LoginItem.handleDeleteEvent()
- 位置: async L560-569
- 役割: 削除の確認ダイアログを出し、承諾されたら AboutLoginsDeleteLogin イベントを発火する
- 触るとき: 削除の流れや確認文言を変えるとき
- 呼び出し先: `document.dispatchEvent()`, `this.showConfirmationDialog()`
- 参照: `this._login`

## LoginItem.handleEditEvent()
- 位置: async L571-587
- 役割: プライマリパスワードを確認してから編集モードに入り、テレメトリを記録する
- 触るとき: 編集開始の認証条件を変えるとき
- 呼び出し先: `promptForPrimaryPassword()`, `this._recordTelemetryEvent()`, `this._toggleEditing()`, `this.render()`

## LoginItem.handleAlertLearnMoreClick()
- 位置: async L589-595
- 役割: 脆弱性アラートの「詳細」リンク押下を、脆弱アラート内であればテレメトリに記録する
- 触るとき: アラートのリンク計測を変えるとき
- 呼び出し先: `currentTarget.closest()`
- 条件付き依存: `if (currentTarget.closest(".vulnerable-alert"))` → `this._recordTelemetryEvent()`

## LoginItem.handleOriginInputClick()
- 位置: async L597-599
- 役割: オリジンのクリックを _handleOriginClick に渡す
- 触るとき: オリジン欄クリック時の処理を追加するとき
- 呼び出し先: `this._handleOriginClick()`

## LoginItem.handleDuplicateErrorGuid()
- 位置: async L601-611
- 役割: 重複エラーのリンクから、既存ログインの GUID を指定して AboutLoginsLoginSelected を発火する
- 触るとき: 重複ログインへの移動動作を変えるとき
- 呼び出し先: `window.dispatchEvent()`
- 参照: `currentTarget.dataset.errorGuid`

## LoginItem.handleInputSubmit()
- 位置: async L613-649
- 役割: フォーム送信時に入力を検証し、変更がなければ閲覧に戻し、変更があれば既存ならUpdate、新規ならCreate イベントを発火する
- 触るとき: 保存処理の分岐(既存更新か新規作成か)や保存後の表示遷移を変えるとき
- 呼び出し先: `event.preventDefault()`, `this._isFormValid()`, `this._loginFromForm()`, `this.hasPendingChanges()`
- 条件付き依存: `if (!this.hasPendingChanges())` → `this._toggleEditing()`
- 条件付き依存: `if (!this.hasPendingChanges())` → `this.render()`
- 条件付き依存: `if (this._login.guid)` → `document.dispatchEvent()`
- 条件付き依存: `if (this._login.guid)` → `this._recordTelemetryEvent()`
- 条件付き依存: `if (this._login.guid)` → `this._toggleEditing()`
- 条件付き依存: `if (this._login.guid)` → `this.render()`
- 条件付き依存: `if (!(this._login.guid))` → `document.dispatchEvent()`
- 条件付き依存: `if (!(this._login.guid))` → `this._recordTelemetryEvent()`
- 参照: `loginUpdates.guid`, `this._login.guid`

## LoginItem.handleInputAuxclick()
- 位置: async L651-655
- 役割: オリジン欄での中ボタンクリックを、オリジンを開く処理として扱う
- 触るとき: 中ボタンでのオリジン操作を変えるとき
- 条件付き依存: `if (button == 1)` → `this._handleOriginClick()`

## LoginItem.handleInputMousedown()
- 位置: async L657-662
- 役割: オリジン欄での中ボタン押下時に既定動作を止め、オートスクロールを防ぐ
- 触るとき: 中ボタン操作で意図せずスクロールが起きる問題を調べるとき
- 条件付き依存: `if (event.currentTarget == this._originInput && event.button == 1)` → `event.preventDefault()`
- 参照: `event.button`, `event.currentTarget`, `this._originInput`

## LoginItem.handleAboutLoginsInitial()
- 位置: async L664-666
- 役割: ページ読み込み時の最初の選択イベントを受け、フォーカスを移さずにログインを表示する
- 触るとき: 初期表示時にフォーカスを奪わないための仕組みを変えるとき
- 呼び出し先: `this.setLogin()`

## LoginItem.handleAboutLoginsLoginSelected()
- 位置: async L668-670
- 役割: 別のログインが選ばれたとき、未保存変更の確認を経由するよう #confirmPendingChangesOnEvent に渡す
- 触るとき: ログイン切り替え時の未保存確認の条件を変えるとき
- 呼び出し先: `this.#confirmPendingChangesOnEvent()`
- 参照: `event.detail`

## LoginItem.handleAboutLoginsShowBlankLogin()
- 位置: async L672-674
- 役割: 新規作成画面を開くイベントを、未保存変更の確認付きで空のログインとして扱う
- 触るとき: 新規作成ボタン押下時の確認挙動を変えるとき
- 呼び出し先: `this.#confirmPendingChangesOnEvent()`

## LoginItem.handleAboutLoginsRemaskPassword()
- 位置: async L676-683
- 役割: パスワードの再マスク要求で、閲覧中なら表示チェックを外して表示状態を戻す
- 触るとき: 一定時間後やページ操作時に表示を隠す仕組みを調べるとき
- 呼び出し先: `this._recordTelemetryEvent()`, `this._updatePasswordRevealState()`
- 参照: `this._revealCheckbox.checked`, `this.dataset.editing`

## LoginItem.#confirmPendingChangesOnEvent()
- 位置: L692-709
- 役割: 未保存変更があれば元イベントを止めて破棄確認を出し、承諾後に同じイベントを再発火する。変更がなければそのままログインを設定する
- 触るとき: 未保存変更の扱いをログイン切り替え全体で変えるとき
- 呼び出し先: `this.hasPendingChanges()`
- 条件付き依存: `if (this.hasPendingChanges())` → `event.preventDefault()`
- 条件付き依存: `if (this.hasPendingChanges())` → `this.showConfirmationDialog()`
- 条件付き依存: `if (this.hasPendingChanges())` → `this.setLogin()`
- 条件付き依存: `if (this.hasPendingChanges())` → `window.dispatchEvent()`
- 条件付き依存: `if (!(this.hasPendingChanges()))` → `this.setLogin()`
- 参照: `event.type`

## LoginItem.showConfirmationDialog()
- 位置: L717-754
- 役割: 削除または破棄の確認ダイアログを表示し、承諾時に onConfirm を実行して該当テレメトリを送る
- 触るとき: 確認ダイアログの文言や、承諾・キャンセル時の挙動を変えるとき
- 呼び出し先: `dialog.show()`, `dialogPromise.then()`, `document.querySelector()`, `onConfirm()`, `this._recordTelemetryEvent()`
- 参照: `this._login.guid`

## LoginItem.hasPendingChanges()
- 位置: L756-763
- 役割: 編集中かつ、フォームの値が保存済みのログインと異なるかを返す
- 触るとき: 未保存変更の判定基準(比較する項目)を変えるとき
- 呼び出し先: `Object.assign()`, `this._loginFromForm()`, `window.AboutLoginsUtils.doLoginsMatch()`
- 参照: `this._login`, `this.dataset.editing`

## LoginItem.resetForm()
- 位置: L765-781
- 役割: フォームをリセットする。パスワード欄が DOM に無いときは一時的に差し込んでからリセットし、元に戻す
- 触るとき: リセット時に値やダーティ状態が残る不具合を調べるとき
- 呼び出し先: `this._form.reset()`
- 条件付き依存: `if (!wasConnected)` → `this._revealCheckbox.insertAdjacentElement()`
- 条件付き依存: `if (!wasConnected)` → `this._passwordInput.remove()`
- 参照: `this._passwordInput`, `this._passwordInput.isConnected`

## LoginItem.setLogin()
- 位置: L790-822
- 役割: 表示するログインを差し替え、新規かどうかの印、編集状態、コピーボタンの状態を初期化して再描画する
- 触るとき: ログイン選択時の初期状態(編集中か閲覧か、フォーカス移動の有無)を変えるとき
- 呼び出し先: `clearTimeout()`, `document.documentElement.classList.toggle()`, `this._toggleEditing()`, `this.render()`, `this.resetForm()`
- 条件付き依存: `if (!skipFocusChange)` → `this._editButton.focus()`
- 参照: `currentTarget.dataset.copied`, `currentTarget.disabled`, `login.guid`, `this._copyPasswordButton`, `this._copyPasswordButton.copiedText`, `this._copyPasswordTimeoutId`, `this._copyUsernameButton`, `this._copyUsernameButton.copiedText`, `this._copyUsernameTimeoutId`, `this._error`, `this._login`, `this._revealCheckbox.checked`, `this.dataset.isNewLogin`

## LoginItem.loginAdded()
- 位置: L831-847
- 役割: 保存されたログインが新規入力中の内容と一致した場合に、その内容を閲覧表示へ切り替えて選択を通知する
- 触るとき: 新規作成の保存完了後の画面遷移を調べるとき
- 呼び出し先: `this._loginFromForm()`, `this.dispatchEvent()`, `this.setLogin()`, `window.AboutLoginsUtils.doLoginsMatch()`
- 参照: `this._login.guid`

## LoginItem.loginModified()
- 位置: L856-871
- 役割: 表示中のログインが更新されたとき、編集中の未保存変更があれば破棄確認を出してから表示を更新する
- 触るとき: 外部からの更新通知で入力中の内容を失わないようにする処理を変えるとき
- 呼び出し先: `this._loginFromForm()`, `window.AboutLoginsUtils.doLoginsMatch()`
- 条件付き依存: `if (valuesChanged)` → `this.showConfirmationDialog()`
- 条件付き依存: `if (valuesChanged)` → `this.setLogin()`
- 条件付き依存: `if (!(valuesChanged))` → `this.setLogin()`
- 参照: `login.guid`, `this._login.guid`, `this.dataset.editing`

## LoginItem.loginRemoved()
- 位置: L880-887
- 役割: 表示中のログインが削除されたとき、表示を空にして編集状態を解除する
- 触るとき: 削除後の表示を変えるとき
- 呼び出し先: `this._toggleEditing()`, `this.setLogin()`
- 参照: `login.guid`, `this._login.guid`

## LoginItem._handleOriginClick()
- 位置: L889-893
- 役割: オリジンを開いたことを、既存ログインのテレメトリとして記録する
- 触るとき: オリジンを開く操作の計測項目を変えるとき
- 呼び出し先: `this._recordTelemetryEvent()`

## LoginItem._isFormValid()
- 位置: L902-918
- 役割: パスワード欄と(新規のときは)オリジン欄の妥当性を検査する。reportErrors 指定時はエラーを表示する
- 触るとき: 保存時に必須とする項目を変えるとき
- 条件付き依存: `if (this.dataset.isNewLogin)` → `fields.push()`
- 条件付き依存: `if (reportErrors)` → `field.reportValidity()`
- 条件付き依存: `if (!(reportErrors))` → `field.checkValidity()`
- 参照: `this._originInput`, `this._passwordInput`, `this.dataset.isNewLogin`

## LoginItem._loginFromForm()
- 位置: L920-927
- 役割: フォームの値(ユーザー名は trim、オリジンは正規化)を既存ログインに重ねたオブジェクトを作る
- 触るとき: フォームから保存データを作る際の項目や正規化規則を変えるとき
- 呼び出し先: `Object.assign()`, `this._usernameInput.value.trim()`, `window.AboutLoginsUtils.getLoginOrigin()`
- 参照: `this._login`, `this._originInput.value`, `this._passwordInput.value`

## LoginItem._recordTelemetryEvent()
- 位置: L929-944
- 役割: 侵害済みなら extra.breached、脆弱なら extra.vulnerable を付けて、テレメトリを送る(侵害が優先)
- 触るとき: テレメトリに付ける属性やその優先順位を変えるとき
- 呼び出し先: `eventObject.hasOwnProperty()`, `recordTelemetryEvent()`, `this._breachesMap.has()`
- 条件付き依存: `if (this._breachesMap && this._breachesMap.has(this._login.guid))` → `Object.assign()`
- 条件付き依存: `if (!(this._breachesMap && this._breachesMap.has(this._login.guid)))` → `this._vulnerableLoginsMap.has()`
- 条件付き依存: `if ( this._vulnerableLoginsMap && this._vulnerableLoginsMap.has(this._login.guid) )` → `Object.assign()`
- 参照: `eventObject.extra`, `this._breachesMap`, `this._login.guid`, `this._vulnerableLoginsMap`

## LoginItem._toggleEditing()
- 位置: L952-989
- 役割: 編集モードの切り替え。入力欄の readOnly と tabIndex、ボタンの disabled、フォーカス、パスワード欄の幅を更新する
- 触るとき: 編集中と閲覧中で見た目や操作可能範囲が食い違うとき。閲覧中はパスワード欄の幅を文字数に合わせる
- 条件付き依存: `if (shouldEdit)` → `this._passwordInput.style.removeProperty()`
- 条件付き依存: `if (shouldEdit)` → `this._usernameInput.focus()`
- 条件付き依存: `if (shouldEdit)` → `this._usernameInput.select()`
- 参照: `(this._login.password || "").length`, `this._deleteButton.disabled`, `this._editButton.disabled`, `this._login.password`, `this._originInput.readOnly`, `this._originInput.tabIndex`, `this._passwordInput.readOnly`, `this._passwordInput.style.width`, `this._passwordInput.tabIndex`, `this._revealCheckbox.checked`, `this._usernameInput.readOnly`, `this._usernameInput.scrollLeft`, `this._usernameInput.tabIndex`, `this.dataset.editing`, `this.dataset.isNewLogin`

## LoginItem._updatePasswordRevealState()
- 位置: L991-1024
- 役割: チェックボックスに応じて入力欄の type を text か password にし、マスク表示欄と本物の入力欄を入れ替える
- 触るとき: パスワード表示の仕組み(マスク用の別要素を使う理由)を調べるとき。主要な入れ替え処理なので表示バグの起点になりやすい
- 条件付き依存: `if (this.dataset.editing)` → `this._passwordDisplayInput.removeAttribute()`
- 条件付き依存: `if (!(this.dataset.editing))` → `this._passwordDisplayInput.setAttribute()`
- 条件付き依存: `if (checked || this.dataset.isNewLogin)` → `this._passwordDisplayInput.replaceWith()`
- 条件付き依存: `if (this.dataset.editing && inputType === "text")` → `this._passwordInput.focus()`
- 条件付き依存: `if (!(checked || this.dataset.isNewLogin))` → `this._passwordInput.replaceWith()`
- 参照: `this._passwordDisplayInput`, `this._passwordInput`, `this._passwordInput.type`, `this._revealCheckbox`, `this._revealCheckbox.hidden`, `this.dataset.editing`, `this.dataset.isNewLogin`, `window.AboutLoginsUtils`, `window.AboutLoginsUtils.passwordRevealVisible`

## LoginItem._updateOriginDisplayState()
- 位置: L1026-1035
- 役割: 新規作成時はオリジン入力欄を、既存時はリンク表示を DOM に出す
- 触るとき: オリジンの表示と入力欄の切り替え条件を変えるとき
- 条件付き依存: `if (this.dataset.isNewLogin)` → `this._originDisplayInput.replaceWith()`
- 条件付き依存: `if (this.dataset.isNewLogin)` → `this._originInput.focus()`
- 条件付き依存: `if (!(this.dataset.isNewLogin))` → `this._originInput.replaceWith()`
- 参照: `this._originDisplayInput`, `this._originInput`, `this.dataset.isNewLogin`

## LoginItem.#updateBreachAlert()
- 位置: L1042-1048
- 役割: 侵害アラート要素へホスト名、日時、侵害名、パスワード変更 URL を渡す
- 触るとき: 侵害アラートに渡すプロパティを増やすとき。lit 化までの橋渡しコード
- 呼び出し先: `this._changePasswordURLsMap?.get()`
- 参照: `this._breachAlert.breachName`, `this._breachAlert.changePasswordURL`, `this._breachAlert.date`, `this._breachAlert.hostname`, `this._login.guid`

## LoginItem.#updateVulnerablePasswordAlert()
- 位置: L1050-1054
- 役割: 脆弱パスワードのアラート要素へホスト名とパスワード変更 URL を渡す
- 触るとき: 脆弱アラートの表示データを変えるとき。lit 化までの橋渡しコード
- 呼び出し先: `this._changePasswordURLsMap?.get()`
- 参照: `this._login.guid`, `this._vulnerableAlert.changePasswordURL`, `this._vulnerableAlert.hostname`

## LoginItem.#updatePasswordMessage()
- 位置: L1056-1059
- 役割: パスワード警告要素へ新規か否かとログインのタイトルを渡す
- 触るとき: パスワード警告の文言に出す情報を変えるとき
- 参照: `this._login.title`, `this._passwordWarning.isNewLogin`, `this._passwordWarning.webTitle`, `this.dataset.isNewLogin`
