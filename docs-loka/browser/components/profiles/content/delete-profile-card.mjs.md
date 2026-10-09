# browser/components/profiles/content/delete-profile-card.mjs

source: browser/components/profiles/content/delete-profile-card.mjs
source-hash: 15d37d229f729236109e5b474499b0bcef2ac342
lines: 171

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## DeleteProfileCard.connectedCallback()
- 位置: L28-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.init()`

## DeleteProfileCard.init()
- 位置: async L33-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `RPMSendQuery()`, `document.querySelector()`, `this.setFavicon()`, `titleEl.setAttribute()`
- 条件付き依存: `if (this.data.profile.hasCustomAvatar)` → `URL.createObjectURL()`
- 参照: `this.data`, `this.data.profile.avatarFiles.file16`, `this.data.profile.avatarURLs.url16`, `this.data.profile.avatarURLs.url80`, `this.data.profile.hasCustomAvatar`, `this.data.profile.name`, `this.initialized`

## DeleteProfileCard.setFavicon()
- 位置: L56-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.createObjectURL()`, `document.getElementById()`
- 参照: `favicon.href`, `this.data.profile.avatarURLs.url16`, `this.data.profile.faviconSVGText`, `this.data.profile.hasCustomAvatar`

## DeleteProfileCard.updated()
- 位置: L71-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.updated()`
- 参照: `this.data.profile`, `this.data?.profile`, `this.headerAvatar.style.fill`, `this.headerAvatar.style.stroke`

## DeleteProfileCard.cancelDelete()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`

## DeleteProfileCard.confirmDelete()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`

## DeleteProfileCard.render()
- 位置: L91-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.cancelDelete`, `this.confirmDelete`, `this.data`, `this.data.autofillCount`, `this.data.bookmarkCount`, `this.data.historyCount`, `this.data.loginCount`, `this.data.profile.avatarL10nId`, `this.data.profile.avatarURLs.url80`, `this.data.profile.name`, `this.data.tabCount`, `this.data.windowCount`
