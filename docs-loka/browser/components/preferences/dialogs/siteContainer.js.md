# browser/components/preferences/dialogs/siteContainer.js

source: browser/components/preferences/dialogs/siteContainer.js
source-hash: 2c460b9bd4ae13deca773f3a41855035f1dc5f87
lines: 126

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `ContextualIdentityService.getSiteAssociation()`, `ContextualIdentityService.setSiteAssociation()`, `buildForm()`, `document.addEventListener()`, `document.querySelector()`, `document.querySelector("dialog").getButton()`, `gSiteInput.addEventListener()`, `gSiteInput.focus()`, `gSiteInput.value.trim()`, `parseInt()`, `setSiteError()`, `siteFromInput()`, `window.addEventListener()`

## siteFromInput()
- 位置: L25-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContextualIdentityService.normalizeSite()`, `site.includes()`, `value.trim()`
- 条件付き依存: `if (site.includes("://"))` → `Services.io.newURI()`
- 参照: `uri.host`, `uri.scheme`
- XPCOM: `Services.io`

## setSiteError()
- 位置: L42-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSiteError.hasAttribute()`, `gSiteInput.toggleAttribute()`, `window.resizeDialog()`
- 条件付き依存: `if (l10nId)` → `gSiteInput.inputEl.setAttribute()`
- 条件付き依存: `if (l10nId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(l10nId))` → `gSiteInput.inputEl.removeAttribute()`
- 条件付き依存: `if (!(l10nId))` → `gSiteError.removeAttribute()`
- 参照: `gSiteError.textContent`

## buildForm()
- 位置: L59-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `containerOptions()`, `containerOptions().map()`, `document .getElementById()`, `document .getElementById("siteContainerForm") .append()`, `document.createElement()`, `document.l10n.setAttributes()`, `gContainerSelect.append()`, `gSiteError.setAttribute()`, `option.setAttribute()`, `siteField.append()`
- 参照: `gSiteError.className`, `gSiteError.id`, `siteField.className`
