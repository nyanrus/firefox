# browser/components/protections/content/monitor-card.mjs

source: browser/components/protections/content/monitor-card.mjs
source-hash: 68b7cc452a53b5cca401a613674355d5b4eb0611
lines: 430

## <module>
- 役割: (未記入)
- 呼び出し先: `RPMGetFormatURLPref()`, `RPMGetStringPref()`

## MonitorClass.constructor()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.doc`

## MonitorClass.init()
- 位置: L28-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `exposedPasswordsLink.addEventListener()`, `knownBreachesLink.addEventListener()`, `monitorAboutLink.addEventListener()`, `storedEmailLink.addEventListener()`, `this.doc.getElementById()`, `this.doc.sendTelemetryEvent()`, `this.getMonitorData()`, `this.onClickMonitorButton.bind()`
- 参照: `exposedPasswordsLink.href`, `knownBreachesLink.href`, `storedEmailLink.href`

## MonitorClass.onClickMonitorButton()
- 位置: L65-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `evt.currentTarget.classList.contains()`, `exposedPasswords.classList.contains()`, `knownBreaches.classList.contains()`, `this.doc.querySelector()`, `this.doc.sendTelemetryEvent()`
- 条件付き依存: `if (evt.currentTarget.classList.contains("no-breaches-resolved"))` → `this.doc.sendTelemetryEvent()`
- 条件付き依存: `if (!(evt.currentTarget.classList.contains("no-breaches-resolved")))` → `this.doc.sendTelemetryEvent()`
- 条件付き依存: `if (knownBreaches.classList.contains("known-resolved-breaches"))` → `this.doc.sendTelemetryEvent()`
- 条件付き依存: `if (!(knownBreaches.classList.contains("known-resolved-breaches")))` → `knownBreaches.classList.contains()`
- 条件付き依存: `if ( knownBreaches.classList.contains("known-unresolved-breaches") )` → `this.doc.sendTelemetryEvent()`
- 条件付き依存: `if ( exposedPasswords.classList.contains("passwords-exposed-all-breaches") )` → `this.doc.sendTelemetryEvent()`
- 条件付き依存: `if (!( exposedPasswords.classList.contains("passwords-exposed-all-breaches") ))` → `exposedPasswords.classList.contains()`
- 条件付き依存: `if ( exposedPasswords.classList.contains( "passwords-exposed-unresolved-breaches" ) )` → `this.doc.sendTelemetryEvent()`
- 参照: `evt.currentTarget.id`

## MonitorClass.getMonitorData()
- 位置: L129-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `RPMSendQuery("FetchMonitorData", {}).then()`, `monitorUI.classList.remove()`, `this.buildContent()`, `this.doc.querySelector()`

## MonitorClass.buildContent()
- 位置: L140-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.doc.querySelector()`
- 条件付き依存: `if (!monitorData.error)` → `monitorCard.classList.add()`
- 条件付き依存: `if (!monitorData.error)` → `this.doc.l10n.setAttributes()`
- 条件付き依存: `if (!monitorData.error)` → `this.renderContentForUserWithAccount()`
- 条件付き依存: `if (!(!monitorData.error))` → `monitorCard.classList.add()`
- 条件付き依存: `if (!(!monitorData.error))` → `this.doc.getElementById()`
- 条件付き依存: `if (!(!monitorData.error))` → `this.buildMonitorUrl()`
- 条件付き依存: `if (!(!monitorData.error))` → `this.doc.l10n.setAttributes()`
- 条件付き依存: `if (!(!monitorData.error))` → `signUpForMonitorLink.addEventListener()`
- 条件付き依存: `if (!(!monitorData.error))` → `this.doc.sendTelemetryEvent()`
- 参照: `monitorData.error`, `monitorData.userEmail`, `signUpForMonitorLink.href`

## MonitorClass.buildMonitorUrl()
- 位置: L179-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `encodeURIComponent()`

## MonitorClass.renderContentForUserWithAccount()
- 位置: L185-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `breachesLink.addEventListener()`, `breachesLink.setAttribute()`, `monitorCardBody.classList.remove()`, `this.doc.getElementById()`, `this.doc.l10n.setAttributes()`, `this.doc.querySelector()`, `this.onClickMonitorButton.bind()`
- 条件付き依存: `if (!numBreachesResolved)` → `partialBreachesWrapper.classList.add()`
- 条件付き依存: `if (!numBreachesResolved)` → `knownBreaches.classList.add()`
- 条件付き依存: `if (!numBreachesResolved)` → `knownBreaches.classList.remove()`
- 条件付き依存: `if (!numBreachesResolved)` → `this.doc.l10n.setAttributes()`
- 条件付き依存: `if (!numBreachesResolved)` → `exposedPasswords.classList.add()`
- 条件付き依存: `if (!numBreachesResolved)` → `exposedPasswords.classList.remove()`
- 条件付き依存: `if (!numBreachesResolved)` → `breachesIcon.setAttribute()`
- 条件付き依存: `if (!numBreachesResolved)` → `breachesLink.classList.add()`
- 条件付き依存: `if (numBreaches == numBreachesResolved)` → `partialBreachesWrapper.classList.add()`
- 条件付き依存: `if (numBreaches == numBreachesResolved)` → `knownBreaches.classList.remove()`
- 条件付き依存: `if (numBreaches == numBreachesResolved)` → `knownBreaches.classList.add()`
- 条件付き依存: `if (numBreaches == numBreachesResolved)` → `this.doc.l10n.setAttributes()`
- 条件付き依存: `if (numBreaches == numBreachesResolved)` → `exposedPasswords.classList.remove()`
- 条件付き依存: `if (numBreaches == numBreachesResolved)` → `exposedPasswords.classList.add()`
- 条件付き依存: `if (numBreaches == numBreachesResolved)` → `breachesIcon.setAttribute()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `breachesWrapper.classList.add()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `knownBreaches.classList.remove()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `knownBreaches.classList.add()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `this.doc.l10n.setAttributes()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `exposedPasswords.classList.remove()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `exposedPasswords.classList.add()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `document.getElementById()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `this.doc.querySelector()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `Math.floor()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `progressBar.setAttribute()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `partialBreachesLink.setAttribute()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `partialBreachesLink.addEventListener()`
- 条件付き依存: `if (!(numBreaches == numBreachesResolved))` → `this.onClickMonitorButton.bind()`
- 条件付き依存: `if (!(numBreaches))` → `partialBreachesWrapper.classList.add()`
- 条件付き依存: `if (!(numBreaches))` → `knownBreaches.classList.add()`
- 条件付き依存: `if (!(numBreaches))` → `knownBreaches.classList.remove()`
- 条件付き依存: `if (!(numBreaches))` → `this.doc.l10n.setAttributes()`
- 条件付き依存: `if (!(numBreaches))` → `exposedPasswords.classList.add()`
- 条件付き依存: `if (!(numBreaches))` → `exposedPasswords.classList.remove()`
- 条件付き依存: `if (!(numBreaches))` → `breachesIcon.setAttribute()`
- 参照: `exposedPasswords.textContent`, `howItWorksLink.href`, `knownBreaches.textContent`, `storedEmail.textContent`
