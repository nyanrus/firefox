# browser/components/protections/content/lockwise-card.mjs

source: browser/components/protections/content/lockwise-card.mjs
source-hash: 0f3f334b8b539840c8ad27e216f0328a728da5a6
lines: 136

## <module>
- 役割: (未記入)
- 呼び出し先: `RPMGetFormatURLPref()`

## LockwiseCard.constructor()
- 位置: L10-12
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.doc`

## LockwiseCard.init()
- 位置: L17-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lockwiseReportLink.addEventListener()`, `managePasswordsButton.addEventListener()`, `savePasswordsButton.addEventListener()`, `this.doc.getElementById()`, `this.doc.sendTelemetryEvent()`, `this.openAboutLogins.bind()`

## LockwiseCard.openAboutLogins()
- 位置: L41-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `lockwiseCard.classList.contains()`, `this.doc.querySelector()`
- 条件付き依存: `if (lockwiseCard.classList.contains("has-logins"))` → `lockwiseCard.classList.contains()`
- 条件付き依存: `if (lockwiseCard.classList.contains("breached-logins"))` → `this.doc.sendTelemetryEvent()`
- 条件付き依存: `if (!(lockwiseCard.classList.contains("breached-logins")))` → `lockwiseCard.classList.contains()`
- 条件付き依存: `if (lockwiseCard.classList.contains("no-breached-logins"))` → `this.doc.sendTelemetryEvent()`
- 条件付き依存: `if (!(lockwiseCard.classList.contains("has-logins")))` → `lockwiseCard.classList.contains()`
- 条件付き依存: `if (lockwiseCard.classList.contains("no-logins"))` → `this.doc.sendTelemetryEvent()`

## LockwiseCard.buildContent()
- 位置: L58-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `lockwiseUI.classList.remove()`, `this.doc.getElementById()`, `this.doc.querySelector()`
- 条件付き依存: `if (hasLogins)` → `lockwiseCard.classList.remove()`
- 条件付き依存: `if (hasLogins)` → `lockwiseCard.classList.add()`
- 条件付き依存: `if (hasLogins)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (hasLogins)` → `this.renderContentForLoggedInUser()`
- 条件付き依存: `if (!(hasLogins))` → `lockwiseCard.classList.remove()`
- 条件付き依存: `if (!(hasLogins))` → `lockwiseCard.classList.add()`
- 条件付き依存: `if (!(hasLogins))` → `document.l10n.setAttributes()`

## LockwiseCard.renderContentForLoggedInUser()
- 位置: L95-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.doc.getElementById()`, `this.doc.querySelector()`
- 条件付き依存: `if (potentiallyBreachedLogins)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (potentiallyBreachedLogins)` → `lockwiseScannedIcon.setAttribute()`
- 条件付き依存: `if (potentiallyBreachedLogins)` → `lockwiseCard.classList.add()`
- 条件付き依存: `if (!(potentiallyBreachedLogins))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(potentiallyBreachedLogins))` → `lockwiseScannedIcon.setAttribute()`
- 条件付き依存: `if (!(potentiallyBreachedLogins))` → `lockwiseCard.classList.add()`
- 参照: `howItWorksLink.href`
