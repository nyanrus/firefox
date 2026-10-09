# browser/components/profiles/content/edit-profile-card.mjs

source: browser/components/profiles/content/edit-profile-card.mjs
source-hash: 0074b6d58b572e197633ad3cee35474ce9515ddb
lines: 706

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## Debounce.constructor()
- 位置: L16-20
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#callback`, `this.#timeoutId`, `this.timeout`

## Debounce.#trigger()
- 位置: L22-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#callback()`
- 参照: `this.#timeoutId`

## Debounce.arm()
- 位置: L27-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this.#trigger()`, `this.disarm()`
- 参照: `this.#timeoutId`, `this.timeout`

## Debounce.disarm()
- 位置: L32-37
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isArmed)` → `clearTimeout()`
- 参照: `this.#timeoutId`, `this.isArmed`

## Debounce.finalize()
- 位置: L39-44
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isArmed)` → `this.disarm()`
- 条件付き依存: `if (this.isArmed)` → `this.#callback()`
- 参照: `this.isArmed`

## Debounce.isArmed()
- 位置: L46-48
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#timeoutId`

## EditProfileCard.themeCards()
- 位置: L113-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.novaEnabled`, `this.themesPicker.childElements`, `this.themesPicker.pickerEl.childElements`

## EditProfileCard.constructor()
- 位置: L120-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.hideSavedMessage()`, `this.updateName()`
- 参照: `this.clearSavedMessageTimer`, `this.updateNameDebouncer`

## EditProfileCard.connectedCallback()
- 位置: L134-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `super.connectedCallback()`, `this.addEventListener()`, `this.init()`, `this.init().then()`, `window.addEventListener()`
- 参照: `this.initialized`

## EditProfileCard.disconnectedCallback()
- 位置: L149-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.removeEventListener()`, `super.disconnectedCallback()`, `this.removeEventListener()`, `window.removeEventListener()`

## EditProfileCard.init()
- 位置: async L162-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `document.location.hash.includes()`, `document.location.hash.replace()`, `fakeParams.get()`, `this.setInitialInput()`, `this.setProfile()`
- 参照: `this.copiedProfileName`, `this.hasDesktopShortcut`, `this.initialized`, `this.isCopy`, `this.isRestored`, `this.novaEnabled`, `this.platform`, `this.profiles`, `this.themes`, `this.updateNameDebouncer.timeout`

## EditProfileCard.#shouldRecordThemePickerShown()
- 位置: L199-203
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `document.hidden`, `this.hasRecordedThemePickerShown`, `this.isConnected`

## EditProfileCard.maybeRecordThemePickerShown()
- 位置: async L205-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.removeEventListener()`, `themePicker.shown()`, `this.#shouldRecordThemePickerShown()`, `this.getUpdateComplete()`, `this.removeEventListener()`
- 参照: `themePicker.updateComplete`, `themePicker?.themes.length`, `this.hasRecordedThemePickerShown`, `this.novaEnabled`, `this.themesPicker`

## EditProfileCard.setInitialInput()
- 位置: async L229-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getUpdateComplete()`
- 参照: `this.isCopy`, `this.isRestored`, `this.nameInput.value`

## EditProfileCard.createAvatarURL()
- 位置: L239-245
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.profile.avatarFiles?.file16)` → `URL.createObjectURL()`
- 参照: `this.profile.avatarFiles.file16`, `this.profile.avatarFiles?.file16`, `this.profile.avatarURLs.url16`, `this.profile.avatarURLs.url80`

## EditProfileCard.getUpdateComplete()
- 位置: async L247-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.themeCards).map()`, `Promise.all()`, `super.getUpdateComplete()`
- 参照: `card.updateComplete`, `this.mozCard.updateComplete`, `this.themeCards`

## EditProfileCard.setProfile()
- 位置: L259-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setFavicon()`
- 条件付き依存: `if (this.profile?.hasCustomAvatar && this.profile?.avatarURLs.url16)` → `URL.revokeObjectURL()`
- 条件付き依存: `if (this.profile?.favicon)` → `URL.revokeObjectURL()`
- 条件付き依存: `if (this.profile.hasCustomAvatar)` → `this.createAvatarURL()`
- 参照: `this.profile`, `this.profile.avatarURLs.url16`, `this.profile.avatarURLs.url80`, `this.profile.favicon`, `this.profile.hasCustomAvatar`, `this.profile?.avatarURLs.url16`, `this.profile?.favicon`, `this.profile?.hasCustomAvatar`

## EditProfileCard.setFavicon()
- 位置: L279-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.createObjectURL()`, `document.getElementById()`
- 参照: `favicon.href`, `this.profile.avatarURLs.url16`, `this.profile.favicon`, `this.profile.faviconSVGText`, `this.profile.hasCustomAvatar`

## EditProfileCard.handleEvent()
- 位置: L295-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `this.maybeRecordThemePickerShown()`, `this.nameInput.value.trim()`, `this.refreshProfile()`, `this.updateAvatar()`
- 条件付き依存: `if (newName === "")` → `this.showErrorMessage()`
- 条件付き依存: `if (newName === "")` → `event.preventDefault()`
- 条件付き依存: `if (!(newName === ""))` → `this.updateNameDebouncer.finalize()`
- 参照: `event.detail`, `event.type`, `this.profile?.themeId`

## EditProfileCard.refreshProfile()
- 位置: async L341-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `this.requestUpdate()`, `this.setProfile()`

## EditProfileCard.updated()
- 位置: L349-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.updated()`
- 参照: `this.headerAvatar.style.fill`, `this.headerAvatar.style.stroke`, `this.profile`

## EditProfileCard.updateName()
- 位置: L361-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `this.nameInput.value.trim()`, `this.showSavedMessage()`, `this.updateNameDebouncer.disarm()`
- 参照: `this.profile`, `this.profile.name`

## EditProfileCard.updateTheme()
- 位置: async L374-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `this.requestUpdate()`, `this.setProfile()`
- 参照: `this.profile.themeId`

## EditProfileCard.updateAvatar()
- 位置: async L388-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `this.requestUpdate()`, `this.setProfile()`
- 参照: `this.profile.avatar`

## EditProfileCard.isDuplicateName()
- 位置: L401-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.profiles.find()`
- 参照: `p.id`, `p.name`, `this.profile.id`

## EditProfileCard.handleInputEvent()
- 位置: async L407-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideSavedMessage()`, `this.nameInput.value.trim()`
- 条件付き依存: `if (newName === "")` → `this.showErrorMessage()`
- 条件付き依存: `if (!(newName === ""))` → `this.isDuplicateName()`
- 条件付き依存: `if (this.isDuplicateName(newName))` → `this.showErrorMessage()`
- 条件付き依存: `if (!(this.isDuplicateName(newName)))` → `this.hideErrorMessage()`
- 条件付き依存: `if (!(this.isDuplicateName(newName)))` → `this.updateNameDebouncer.arm()`

## EditProfileCard.showErrorMessage()
- 位置: L420-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `this.nameInput.setCustomValidity()`, `this.updateNameDebouncer.disarm()`
- 参照: `this.errorMessage`, `this.errorMessage.parentElement.hidden`

## EditProfileCard.hideErrorMessage()
- 位置: L427-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.nameInput.setCustomValidity()`
- 参照: `this.errorMessage.parentElement.hidden`

## EditProfileCard.showSavedMessage()
- 位置: L432-435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearSavedMessageTimer.arm()`
- 参照: `this.savedMessage.parentElement.hidden`

## EditProfileCard.hideSavedMessage()
- 位置: L437-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearSavedMessageTimer.disarm()`
- 参照: `this.savedMessage.parentElement.hidden`

## EditProfileCard.headerTemplate()
- 位置: L442-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (this.isCopy)` → `html()`
- 条件付き依存: `if (this.isCopy)` → `JSON.stringify()`
- 条件付き依存: `if (this.isRestored)` → `html()`
- 参照: `this.copiedProfileName`, `this.isCopy`, `this.isRestored`

## EditProfileCard.nameInputTemplate()
- 位置: L478-487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.handleInputEvent`, `this.profile.name`

## EditProfileCard.profilesNameTemplate()
- 位置: L489-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.nameInputTemplate()`

## EditProfileCard.themesTemplate()
- 位置: L520-531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.legacyThemesTemplate()`
- 条件付き依存: `if (this.novaEnabled)` → `html()`
- 参照: `this.novaEnabled`

## EditProfileCard.legacyThemesTemplate()
- 位置: L533-563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.themes.map()`
- 参照: `t.dataL10nId`, `t.id`, `t.name`, `this.handleThemeChange`, `this.profile.themeId`, `this.themes`

## EditProfileCard.desktopShortcutTemplate()
- 位置: L565-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.handleDesktopShortcutToggle`, `this.hasDesktopShortcut`, `this.platform`

## EditProfileCard.handleDesktopShortcutToggle()
- 位置: async L580-590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `event.preventDefault()`, `this.requestUpdate()`
- 参照: `event.target.pressed`, `this.shortcutToggle.pressed`

## EditProfileCard.handleThemeChange()
- 位置: L592-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateTheme()`
- 参照: `this.themesPicker.value`

## EditProfileCard.headerAvatarTemplate()
- 位置: L596-619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.profile.avatar`, `this.profile.avatarL10nId`, `this.profile.avatarURLs.url80`, `this.toggleAvatarSelectorCard`

## EditProfileCard.toggleAvatarSelectorCard()
- 位置: L621-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.avatarSelector.toggleHidden()`

## EditProfileCard.onDeleteClick()
- 位置: L626-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `window.removeEventListener()`

## EditProfileCard.onDoneClick()
- 位置: L631-644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.nameInput.value.trim()`
- 条件付き依存: `if (newName === "")` → `this.showErrorMessage()`
- 条件付き依存: `if (!(newName === ""))` → `this.isDuplicateName()`
- 条件付き依存: `if (this.isDuplicateName(newName))` → `this.showErrorMessage()`
- 条件付き依存: `if (!(this.isDuplicateName(newName)))` → `this.updateNameDebouncer.finalize()`
- 条件付き依存: `if (!(this.isDuplicateName(newName)))` → `window.removeEventListener()`
- 条件付き依存: `if (!(this.isDuplicateName(newName)))` → `RPMSendAsyncMessage()`

## EditProfileCard.onMoreThemesClick()
- 位置: L646-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`
- 参照: `window.location.href`

## EditProfileCard.buttonsTemplate()
- 位置: L654-668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.onDeleteClick`, `this.onDoneClick`

## EditProfileCard.render()
- 位置: L670-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.buttonsTemplate()`, `this.desktopShortcutTemplate()`, `this.headerAvatarTemplate()`, `this.headerTemplate()`, `this.profilesNameTemplate()`, `this.themesTemplate()`
- 参照: `this.onMoreThemesClick`, `this.profile`
