# browser/components/aboutlogins/content/components/login-item.mjs

source: browser/components/aboutlogins/content/components/login-item.mjs
source-hash: 2309c29fb6f427825b6d91b3d5a1ef537af42376
lines: 1062

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## LoginItem.COPY_BUTTON_RESET_TIMEOUT()
- 位置: L16-18
- 役割: (未記入)
- 触るとき: (未記入)

## LoginItem.constructor()
- 位置: L20-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._copyPasswordTimeoutId`, `this._copyUsernameTimeoutId`, `this._error`, `this._login`

## LoginItem.connectedCallback()
- 位置: L28-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `loginItemTemplate.content.cloneNode()`, `shadowRoot.appendChild()`, `this._cancelButton.addEventListener()`, `this._copyPasswordButton.addEventListener()`, `this._copyUsernameButton.addEventListener()`, `this._deleteButton.addEventListener()`, `this._editButton.addEventListener()`, `this._errorMessage.querySelector()`, `this._errorMessageLink.addEventListener()`, `this._form.addEventListener()`, `this._originDisplayInput.addEventListener()`, `this._originInput.addEventListener()`, `this._passwordDisplayInput.addEventListener()`, `this._passwordInput.addEventListener()`, `this._revealCheckbox.addEventListener()`, `this.addHTTPSPrefix()`, `this.attachShadow()`, `this.handleAboutLoginsInitial()`, `this.handleAboutLoginsLoginSelected()`, `this.handleAboutLoginsRemaskPassword()`, `this.handleAboutLoginsShowBlankLogin()`, `this.handleCancelEvent()`, `this.handleCopyPasswordClick()`, `this.handleCopyUsernameClick()`, `this.handleDeleteEvent()`, `this.handleDuplicateErrorGuid()`, `this.handleEditEvent()`, `this.handleEditPasswordInputBlur()`, `this.handleInputAuxclick()`, `this.handleInputMousedown()`, `this.handleInputSubmit()`, `this.handleKeydown()`, `this.handleOriginInputClick()`, `this.handlePasswordDisplayBlur()`, `this.handlePasswordDisplayFocus()`, `this.handleRevealPasswordClick()`, `this.render()`, `this.shadowRoot.querySelector()`, `window.addEventListener()`
- 条件付き依存: `if (this.shadowRoot)` → `this.render()`
- 参照: `this._breachAlert`, `this._cancelButton`, `this._confirmDeleteDialog`, `this._copyPasswordButton`, `this._copyUsernameButton`, `this._deleteButton`, `this._editButton`, `this._errorMessage`, `this._errorMessageLink`, `this._errorMessageText`, `this._favicon`, `this._form`, `this._originDisplayInput`, `this._originInput`, `this._originWarning`, `this._passwordDisplayInput`, `this._passwordInput`, `this._passwordWarning`, `this._revealCheckbox`, `this._saveChangesButton`, `this._title`, `this._usernameInput`, `this._vulnerableAlert`, `this.dataset.editing`, `this.shadowRoot`

## LoginItem.focus()
- 位置: L174-182
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._editButton.disabled)` → `this._editButton.focus()`
- 条件付き依存: `if (!this._deleteButton.disabled)` → `this._deleteButton.focus()`
- 条件付き依存: `if (!(!this._deleteButton.disabled))` → `this._originInput.focus()`
- 参照: `this._deleteButton.disabled`, `this._editButton.disabled`

## LoginItem.render()
- 位置: async L184-275
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.querySelector()`
- 参照: `this._login.guid`, `this._login.timeCreated`, `this._login.timeLastUsed`, `this._login.timePasswordChanged`, `timeline.hidden`, `timeline.history`

## LoginItem.setBreaches()
- 位置: L298-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalSetMonitorData()`

## LoginItem.updateBreaches()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginItem.setVulnerableLogins()
- 位置: L306-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalSetMonitorData()`

## LoginItem.updateVulnerableLogins()
- 位置: L313-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginItem.setChangePasswordURLs()
- 位置: L320-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalSetMonitorData()`

## LoginItem.updateChangePasswordURLs()
- 位置: L327-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginItem._internalSetMonitorData()
- 位置: L334-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.render()`

## LoginItem._internalUpdateMonitorData()
- 位置: L339-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalSetMonitorData()`
- 条件付き依存: `if (data)` → `this[internalMemberName].set()`
- 条件付き依存: `if (!(data))` → `this[internalMemberName].delete()`

## LoginItem.showLoginItemError()
- 位置: L353-356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.render()`
- 参照: `this._error`

## LoginItem.handleKeydown()
- 位置: async L358-367
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.key === "Escape" && this.dataset.editing)` → `this.handleCancelEvent()`
- 条件付き依存: `if (e.altKey && e.key === "Enter" && !this.dataset.editing)` → `this.handleEditEvent()`
- 条件付き依存: `if (e.altKey && (e.key === "Backspace" || e.key === "Delete"))` → `this.handleDeleteEvent()`
- 参照: `e.altKey`, `e.key`, `this.dataset.editing`

## LoginItem.handlePasswordDisplayFocus()
- 位置: async L369-383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updatePasswordRevealState()`
- 参照: `e.relatedTarget`, `this._passwordInput.type`, `this._revealCheckbox`, `this._revealCheckbox.checked`, `this.dataset.editing`, `this.dataset.isNewLogin`

## LoginItem.addHTTPSPrefix()
- 位置: async L385-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originValue.match()`, `this._originInput.value.trim()`
- 参照: `e.relatedTarget`, `this._originInput.value`, `this._revealCheckbox`

## LoginItem.handlePasswordDisplayBlur()
- 位置: async L404-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updatePasswordRevealState()`, `this.addHTTPSPrefix()`
- 参照: `e.relatedTarget`, `this._revealCheckbox`, `this._revealCheckbox.checked`, `this.dataset.editing`

## LoginItem.handleEditPasswordInputBlur()
- 位置: async L418-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updatePasswordRevealState()`, `this.addHTTPSPrefix()`
- 参照: `e.relatedTarget`, `this._revealCheckbox`, `this._revealCheckbox.checked`

## LoginItem.handleRevealPasswordClick()
- 位置: async L432-458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recordTelemetryEvent()`, `this._updatePasswordRevealState()`
- 条件付き依存: `if (this.dataset.editing || this.dataset.isNewLogin)` → `this._passwordDisplayInput.replaceWith()`
- 条件付き依存: `if (this.dataset.editing || this.dataset.isNewLogin)` → `this._passwordInput.focus()`
- 条件付き依存: `if (this._revealCheckbox.checked && !this.dataset.editing)` → `promptForPrimaryPassword()`
- 参照: `this._passwordInput`, `this._passwordInput.type`, `this._revealCheckbox.checked`, `this.dataset.editing`, `this.dataset.isNewLogin`

## LoginItem.handleCancelEvent()
- 位置: async L460-488
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `document.dispatchEvent()`, `promptForPrimaryPassword()`, `setTimeout()`, `this._recordTelemetryEvent()`
- 参照: `LoginItem.COPY_BUTTON_RESET_TIMEOUT`, `currentTarget.copiedText`, `currentTarget.dataset.copied`, `currentTarget.disabled`, `this._copyPasswordTimeoutId`, `this._copyUsernameButton.copiedText`, `this._copyUsernameButton.dataset.copied`, `this._copyUsernameButton.disabled`, `this._copyUsernameTimeoutId`, `this._login.password`, `this._login.username`

## LoginItem.handleCopyUsernameClick()
- 位置: async L529-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `document.dispatchEvent()`, `setTimeout()`, `this._recordTelemetryEvent()`
- 参照: `LoginItem.COPY_BUTTON_RESET_TIMEOUT`, `currentTarget.copiedText`, `currentTarget.dataset.copied`, `currentTarget.disabled`, `this._copyPasswordButton.copiedText`, `this._copyPasswordButton.dataset.copied`, `this._copyPasswordButton.disabled`, `this._copyPasswordTimeoutId`, `this._copyUsernameTimeoutId`, `this._login.username`

## LoginItem.handleDeleteEvent()
- 位置: async L560-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`, `this.showConfirmationDialog()`
- 参照: `this._login`

## LoginItem.handleEditEvent()
- 位置: async L571-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promptForPrimaryPassword()`, `this._recordTelemetryEvent()`, `this._toggleEditing()`, `this.render()`

## LoginItem.handleAlertLearnMoreClick()
- 位置: async L589-595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentTarget.closest()`
- 条件付き依存: `if (currentTarget.closest(".vulnerable-alert"))` → `this._recordTelemetryEvent()`

## LoginItem.handleOriginInputClick()
- 位置: async L597-599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleOriginClick()`

## LoginItem.handleDuplicateErrorGuid()
- 位置: async L601-611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.dispatchEvent()`
- 参照: `currentTarget.dataset.errorGuid`

## LoginItem.handleInputSubmit()
- 位置: async L613-649
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (button == 1)` → `this._handleOriginClick()`

## LoginItem.handleInputMousedown()
- 位置: async L657-662
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.currentTarget == this._originInput && event.button == 1)` → `event.preventDefault()`
- 参照: `event.button`, `event.currentTarget`, `this._originInput`

## LoginItem.handleAboutLoginsInitial()
- 位置: async L664-666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setLogin()`

## LoginItem.handleAboutLoginsLoginSelected()
- 位置: async L668-670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#confirmPendingChangesOnEvent()`
- 参照: `event.detail`

## LoginItem.handleAboutLoginsShowBlankLogin()
- 位置: async L672-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#confirmPendingChangesOnEvent()`

## LoginItem.handleAboutLoginsRemaskPassword()
- 位置: async L676-683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recordTelemetryEvent()`, `this._updatePasswordRevealState()`
- 参照: `this._revealCheckbox.checked`, `this.dataset.editing`

## LoginItem.#confirmPendingChangesOnEvent()
- 位置: L692-709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasPendingChanges()`
- 条件付き依存: `if (this.hasPendingChanges())` → `event.preventDefault()`
- 条件付き依存: `if (this.hasPendingChanges())` → `this.showConfirmationDialog()`
- 条件付き依存: `if (this.hasPendingChanges())` → `this.setLogin()`
- 条件付き依存: `if (this.hasPendingChanges())` → `window.dispatchEvent()`
- 条件付き依存: `if (!(this.hasPendingChanges()))` → `this.setLogin()`
- 参照: `event.type`

## LoginItem.showConfirmationDialog()
- 位置: L717-754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialog.show()`, `dialogPromise.then()`, `document.querySelector()`, `onConfirm()`, `this._recordTelemetryEvent()`
- 参照: `this._login.guid`

## LoginItem.hasPendingChanges()
- 位置: L756-763
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this._loginFromForm()`, `window.AboutLoginsUtils.doLoginsMatch()`
- 参照: `this._login`, `this.dataset.editing`

## LoginItem.resetForm()
- 位置: L765-781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._form.reset()`
- 条件付き依存: `if (!wasConnected)` → `this._revealCheckbox.insertAdjacentElement()`
- 条件付き依存: `if (!wasConnected)` → `this._passwordInput.remove()`
- 参照: `this._passwordInput`, `this._passwordInput.isConnected`

## LoginItem.setLogin()
- 位置: L790-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `document.documentElement.classList.toggle()`, `this._toggleEditing()`, `this.render()`, `this.resetForm()`
- 条件付き依存: `if (!skipFocusChange)` → `this._editButton.focus()`
- 参照: `currentTarget.dataset.copied`, `currentTarget.disabled`, `login.guid`, `this._copyPasswordButton`, `this._copyPasswordButton.copiedText`, `this._copyPasswordTimeoutId`, `this._copyUsernameButton`, `this._copyUsernameButton.copiedText`, `this._copyUsernameTimeoutId`, `this._error`, `this._login`, `this._revealCheckbox.checked`, `this.dataset.isNewLogin`

## LoginItem.loginAdded()
- 位置: L831-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._loginFromForm()`, `this.dispatchEvent()`, `this.setLogin()`, `window.AboutLoginsUtils.doLoginsMatch()`
- 参照: `this._login.guid`

## LoginItem.loginModified()
- 位置: L856-871
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._loginFromForm()`, `window.AboutLoginsUtils.doLoginsMatch()`
- 条件付き依存: `if (valuesChanged)` → `this.showConfirmationDialog()`
- 条件付き依存: `if (valuesChanged)` → `this.setLogin()`
- 条件付き依存: `if (!(valuesChanged))` → `this.setLogin()`
- 参照: `login.guid`, `this._login.guid`, `this.dataset.editing`

## LoginItem.loginRemoved()
- 位置: L880-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toggleEditing()`, `this.setLogin()`
- 参照: `login.guid`, `this._login.guid`

## LoginItem._handleOriginClick()
- 位置: L889-893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recordTelemetryEvent()`

## LoginItem._isFormValid()
- 位置: L902-918
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.dataset.isNewLogin)` → `fields.push()`
- 条件付き依存: `if (reportErrors)` → `field.reportValidity()`
- 条件付き依存: `if (!(reportErrors))` → `field.checkValidity()`
- 参照: `this._originInput`, `this._passwordInput`, `this.dataset.isNewLogin`

## LoginItem._loginFromForm()
- 位置: L920-927
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this._usernameInput.value.trim()`, `window.AboutLoginsUtils.getLoginOrigin()`
- 参照: `this._login`, `this._originInput.value`, `this._passwordInput.value`

## LoginItem._recordTelemetryEvent()
- 位置: L929-944
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eventObject.hasOwnProperty()`, `recordTelemetryEvent()`, `this._breachesMap.has()`
- 条件付き依存: `if (this._breachesMap && this._breachesMap.has(this._login.guid))` → `Object.assign()`
- 条件付き依存: `if (!(this._breachesMap && this._breachesMap.has(this._login.guid)))` → `this._vulnerableLoginsMap.has()`
- 条件付き依存: `if ( this._vulnerableLoginsMap && this._vulnerableLoginsMap.has(this._login.guid) )` → `Object.assign()`
- 参照: `eventObject.extra`, `this._breachesMap`, `this._login.guid`, `this._vulnerableLoginsMap`

## LoginItem._toggleEditing()
- 位置: L952-989
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (shouldEdit)` → `this._passwordInput.style.removeProperty()`
- 条件付き依存: `if (shouldEdit)` → `this._usernameInput.focus()`
- 条件付き依存: `if (shouldEdit)` → `this._usernameInput.select()`
- 参照: `(this._login.password || "").length`, `this._deleteButton.disabled`, `this._editButton.disabled`, `this._login.password`, `this._originInput.readOnly`, `this._originInput.tabIndex`, `this._passwordInput.readOnly`, `this._passwordInput.style.width`, `this._passwordInput.tabIndex`, `this._revealCheckbox.checked`, `this._usernameInput.readOnly`, `this._usernameInput.scrollLeft`, `this._usernameInput.tabIndex`, `this.dataset.editing`, `this.dataset.isNewLogin`

## LoginItem._updatePasswordRevealState()
- 位置: L991-1024
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.dataset.editing)` → `this._passwordDisplayInput.removeAttribute()`
- 条件付き依存: `if (!(this.dataset.editing))` → `this._passwordDisplayInput.setAttribute()`
- 条件付き依存: `if (checked || this.dataset.isNewLogin)` → `this._passwordDisplayInput.replaceWith()`
- 条件付き依存: `if (this.dataset.editing && inputType === "text")` → `this._passwordInput.focus()`
- 条件付き依存: `if (!(checked || this.dataset.isNewLogin))` → `this._passwordInput.replaceWith()`
- 参照: `this._passwordDisplayInput`, `this._passwordInput`, `this._passwordInput.type`, `this._revealCheckbox`, `this._revealCheckbox.hidden`, `this.dataset.editing`, `this.dataset.isNewLogin`, `window.AboutLoginsUtils`, `window.AboutLoginsUtils.passwordRevealVisible`

## LoginItem._updateOriginDisplayState()
- 位置: L1026-1035
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.dataset.isNewLogin)` → `this._originDisplayInput.replaceWith()`
- 条件付き依存: `if (this.dataset.isNewLogin)` → `this._originInput.focus()`
- 条件付き依存: `if (!(this.dataset.isNewLogin))` → `this._originInput.replaceWith()`
- 参照: `this._originDisplayInput`, `this._originInput`, `this.dataset.isNewLogin`

## LoginItem.#updateBreachAlert()
- 位置: L1042-1048
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._changePasswordURLsMap?.get()`
- 参照: `this._breachAlert.breachName`, `this._breachAlert.changePasswordURL`, `this._breachAlert.date`, `this._breachAlert.hostname`, `this._login.guid`

## LoginItem.#updateVulnerablePasswordAlert()
- 位置: L1050-1054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._changePasswordURLsMap?.get()`
- 参照: `this._login.guid`, `this._vulnerableAlert.changePasswordURL`, `this._vulnerableAlert.hostname`

## LoginItem.#updatePasswordMessage()
- 位置: L1056-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._login.title`, `this._passwordWarning.isNewLogin`, `this._passwordWarning.webTitle`, `this.dataset.isNewLogin`
