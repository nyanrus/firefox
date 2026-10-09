# browser/components/protections/content/protections.mjs

source: browser/components/protections/content/protections.mjs
source-hash: f6e6ac5fda294f82627f0567dc69a245ee44739d
lines: 484

## <module>
- 役割: (未記入)
- 呼び出し先: `Date.now()`, `RPMGetBoolPref()`, `RPMGetStringPref()`, `RPMSendQuery()`, `RPMSendQuery("FetchContentBlockingEvents", { from: weekAgoInMs, to: todayInMs, }).then()`, `RPMSendQuery("FetchEntryPoint", {}).then()`, `RPMSendQuery("FetchUserLoginsData", {}).then()`, `RPMSetPref()`, `androidMobileAppLink.addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `document.getElementById("mobile-hanger").classList.add()`, `document.querySelector()`, `document.sendTelemetryEvent()`, `exitIcon.addEventListener()`, `iosMobileAppLink.addEventListener()`, `manageProtections.addEventListener()`, `manageProtectionsLink.addEventListener()`, `searchParams.has()`, `window.addEventListener()`

## document.sendTelemetryEvent()
- 位置: L10-15
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMRecordGleanEvent()`

## protectionSettingsEvtHandler()
- 位置: L65-77
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (evt.keyCode == evt.DOM_VK_RETURN || evt.type == "click")` → `RPMSendAsyncMessage()`
- 条件付き依存: `if (evt.target.id == "protection-settings")` → `document.sendTelemetryEvent()`
- 条件付き依存: `if (evt.target.id == "manage-protections")` → `document.sendTelemetryEvent()`
- 参照: `evt.DOM_VK_RETURN`, `evt.keyCode`, `evt.target.id`, `evt.type`

## createGraph()
- 位置: L90-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMGetBoolPref()`, `RPMGetFormatURLPref()`, `RPMGetIntPref()`, `bar.appendChild()`, `bar.setAttribute()`, `date.getDate()`, `date.setDate()`, `date.toISOString()`, `date.toISOString().split()`, `document.createElement()`, `document.getElementById()`, `document.querySelector()`, `document.sendTelemetryEvent()`, `graph.append()`, `graph.prepend()`, `graph.setAttribute()`, `label.setAttribute()`, `learnMoreLink.addEventListener()`
- 条件付き依存: `if (data.isPrivate)` → `graph.classList.add()`
- 条件付き依存: `if (!(data.isPrivate))` → `Date.now()`
- 条件付き依存: `if (!(data.isPrivate))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (data[dateString])` → `document.createElement()`
- 条件付き依存: `if (data[dateString])` → `count.setAttribute()`
- 条件付き依存: `if (data[dateString])` → `setTimeout()`
- 条件付き依存: `if (data[dateString])` → `count.classList.add()`
- 条件付き依存: `if (data[dateString])` → `bar.appendChild()`
- 条件付き依存: `if (content[type])` → `document.createElement()`
- 条件付き依存: `if (content[type])` → `cellSpan.setAttribute()`
- 条件付き依存: `if (content[type])` → `div.setAttribute()`
- 条件付き依存: `if (content[type])` → `document.l10n.setAttributes()`
- 条件付き依存: `if (content[type])` → `cellSpan.appendChild()`
- 条件付き依存: `if (content[type])` → `innerBar.appendChild()`
- 条件付き依存: `if (!(data[dateString]))` → `bar.classList.add()`
- 条件付き依存: `if (data.isPrivate)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (i == 6)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(i == 6))` → `new Date().getDay()`
- 条件付き依存: `if (notBlocking)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (notBlocking)` → `document.getElementById()`
- 条件付き依存: `if (notBlocking)` → `document.querySelector()`
- 条件付き依存: `if (notBlocking)` → `document.querySelector(".etp-card").classList.add()`
- 条件付き依存: `if (!tpEnabled)` → `legend.style.gridTemplateAreas.replace()`
- 条件付き依存: `if (!tpEnabled)` → `document.getElementById()`
- 条件付き依存: `if (!tpEnabled)` → `radio.setAttribute()`
- 条件付き依存: `if (!tpEnabled)` → `document.querySelector()`
- 条件付き依存: `if (!socialEnabled)` → `legend.style.gridTemplateAreas.replace()`
- 条件付き依存: `if (!socialEnabled)` → `document.getElementById()`
- 条件付き依存: `if (!socialEnabled)` → `radio.setAttribute()`
- 条件付き依存: `if (!socialEnabled)` → `document.querySelector()`
- 条件付き依存: `if (!blockingCookies)` → `legend.style.gridTemplateAreas.replace()`
- 条件付き依存: `if (!blockingCookies)` → `document.getElementById()`
- 条件付き依存: `if (!blockingCookies)` → `radio.setAttribute()`
- 条件付き依存: `if (!blockingCookies)` → `document.querySelector()`
- 条件付き依存: `if (!cryptominingEnabled)` → `legend.style.gridTemplateAreas.replace()`
- 条件付き依存: `if (!cryptominingEnabled)` → `document.getElementById()`
- 条件付き依存: `if (!cryptominingEnabled)` → `radio.setAttribute()`
- 条件付き依存: `if (!cryptominingEnabled)` → `document.querySelector()`
- 条件付き依存: `if (!fingerprintingEnabled)` → `legend.style.gridTemplateAreas.replace()`
- 条件付き依存: `if (!fingerprintingEnabled)` → `document.getElementById()`
- 条件付き依存: `if (!fingerprintingEnabled)` → `radio.setAttribute()`
- 条件付き依存: `if (!fingerprintingEnabled)` → `document.querySelector()`
- 条件付き依存: `if (!(notBlocking))` → `document.querySelector()`
- 条件付き依存: `if (!(notBlocking))` → `document.body.setAttribute()`
- 条件付き依存: `if (!(notBlocking))` → `addListeners()`
- 参照: `bar.className`, `bar.style.height`, `cellSpan.id`, `content.total`, `count.className`, `count.id`, `count.textContent`, `data.earliestDate`, `data.isPrivate`, `data.largest`, `data.sumEvents`, `data.weekdays`, `div.className`, `div.style.height`, `document.querySelector("#tab-cookie ~ label").style.display`, `document.querySelector("#tab-cryptominer ~ label").style.display`, `document.querySelector("#tab-fingerprinter ~ label").style.display`, `document.querySelector("#tab-social ~ label").style.display`, `document.querySelector("#tab-tracker ~ label").style.display`, `document.querySelector(`label[data-type=${type}] span`).textContent`, `firstRadio.checked`, `firstRadio.dataset.type`, `innerBar.className`, `label.className`, `label.id`, `label.textContent`, `learnMoreLink.href`, `legend.style.gridTemplateAreas`, `manageProtectionsLink.style.display`

## addListeners()
- 位置: L346-383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.body.setAttribute()`, `document.querySelector()`, `document.querySelectorAll()`, `radio.addEventListener()`, `wrapper.addEventListener()`, `wrapper.classList.add()`, `wrapper.classList.remove()`
- 参照: `ev.originalTarget.dataset.type`, `ev.target.dataset.type`

## triggerTabClick()
- 位置: L348-352
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (ev.originalTarget.dataset.type)` → `document.getElementById(`tab-${ev.target.dataset.type}`).click()`
- 条件付き依存: `if (ev.originalTarget.dataset.type)` → `document.getElementById()`
- 参照: `ev.originalTarget.dataset.type`, `ev.target.dataset.type`

## triggerTabFocus()
- 位置: L354-358
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (ev.originalTarget.dataset)` → `wrapper.classList.add()`
- 参照: `ev.originalTarget.dataset`, `ev.originalTarget.dataset.type`

## triggerTabBlur()
- 位置: L360-364
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (ev.originalTarget.dataset)` → `wrapper.classList.remove()`
- 参照: `ev.originalTarget.dataset`, `ev.originalTarget.dataset.type`
