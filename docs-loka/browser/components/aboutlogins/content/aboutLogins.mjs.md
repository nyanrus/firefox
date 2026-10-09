# browser/components/aboutlogins/content/aboutLogins.mjs

source: browser/components/aboutlogins/content/aboutLogins.mjs
source-hash: afab4e6ff2137a05e1321712fc03b3e4bb034ae0
lines: 298

## <module>
- 役割: (未記入)
- 呼び出し先: `dialog.show()`, `dialogPromise.then()`, `document .querySelector()`, `document .querySelector("login-list") .shadowRoot.querySelector()`, `document.dispatchEvent()`, `document.documentElement.classList.add()`, `document.documentElement.classList.remove()`, `document.querySelector()`, `gElements.loginItem.loginAdded()`, `gElements.loginItem.loginModified()`, `gElements.loginItem.loginRemoved()`, `gElements.loginItem.setBreaches()`, `gElements.loginItem.setChangePasswordURLs()`, `gElements.loginItem.setVulnerableLogins()`, `gElements.loginItem.showLoginItemError()`, `gElements.loginItem.updateBreaches()`, `gElements.loginItem.updateVulnerableLogins()`, `gElements.loginList.classList.add()`, `gElements.loginList.loginAdded()`, `gElements.loginList.loginModified()`, `gElements.loginList.loginRemoved()`, `gElements.loginList.selectLoginByDomainOrGuid()`, `gElements.loginList.setBreaches()`, `gElements.loginList.setChangePasswordURLs()`, `gElements.loginList.setSortDirection()`, `gElements.loginList.setVulnerableLogins()`, `gElements.loginList.updateBreaches()`, `gElements.loginList.updateVulnerableLogins()`, `handleAllLogins()`, `handleSyncState()`, `interceptFocusKey()`, `recordTelemetryEvent()`, `searchParams.get()`, `searchParams.has()`, `setKeyboardAccessForNonDialogElements()`, `updateNoLogins()`, `window.addEventListener()`, `window.dispatchEvent()`, `window.document.documentElement.classList.remove()`

## exportButton()
- 位置: L21-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.menuButton.shadowRoot.querySelector()`

## removeAllButton()
- 位置: L25-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.menuButton.shadowRoot.querySelector()`

## updateNoLogins()
- 位置: L34-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.classList.toggle()`, `gElements.loginItem.classList.toggle()`, `gElements.loginList.classList.toggle()`
- 参照: `gElements.exportButton.disabled`, `gElements.removeAllButton.disabled`

## handleAllLogins()
- 位置: L42-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gElements.loginList.setLogins()`, `updateNoLogins()`
- 参照: `logins.length`

## handleSyncState()
- 位置: L51-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gElements.fxAccountsButton.updateState()`, `gElements.loginIntro.updateState()`
- 参照: `syncState.loggedIn`, `syncState.passwordSyncEnabled`

## interceptFocusKey()
- 位置: async L233-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `document.l10n.formatMessages()`, `event.getModifierState()`, `findKey.attributes .find()`, `findKey.attributes .find(a => a.name == "key") .value.toLowerCase()`
- 条件付き依存: `if (event.key == focusKey && event.getModifierState("Accel"))` → `event.preventDefault()`
- 条件付き依存: `if (event.key == focusKey && event.getModifierState("Accel"))` → `document .querySelector("login-list") .shadowRoot.querySelector("login-filter") .shadowRoot.querySelector()`
- 条件付き依存: `if (event.key == focusKey && event.getModifierState("Accel"))` → `document .querySelector("login-list") .shadowRoot.querySelector()`
- 条件付き依存: `if (event.key == focusKey && event.getModifierState("Accel"))` → `document .querySelector()`
- 参照: `a.name`, `event.key`
