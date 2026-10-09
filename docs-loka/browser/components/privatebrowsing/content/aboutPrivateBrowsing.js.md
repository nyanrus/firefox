# browser/components/privatebrowsing/content/aboutPrivateBrowsing.js

source: browser/components/privatebrowsing/content/aboutPrivateBrowsing.js
source-hash: 911604565f10a34624ed01c5c8f6d9375bccc54e
lines: 531

## <module>
- 役割: (未記入)
- 呼び出し先: `RPMGetBoolPref()`, `RPMGetFormatURLPref()`, `RPMIsWindowPrivate()`, `RPMSendQuery()`, `RPMSendQuery("ShouldShowSearchBanner", {}).then()`, `document .getElementById()`, `document .getElementById("search-banner-close-button") .addEventListener()`, `document.addEventListener()`, `document.documentElement.setAttribute()`, `document.getElementById()`, `document.location.toString()`, `document.location.toString().includes()`, `hideSearchBanner()`, `linkEl.setAttribute()`, `openSearchOptions.addEventListener()`, `setupMessageConfig()`, `window.PrivateBrowsingRedesignEnabled()`

## translateElements()
- 位置: L11-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.forEach()`, `value.replace()`
- 条件付き依存: `if (fluentId !== value)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(fluentId !== value))` → `element.removeAttribute()`
- 参照: `element.textContent`

## renderPromo()
- 位置: async L27-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(novaEnabled ? legacyContainer : novaContainer)?.remove()`, `RPMGetBoolPref()`, `RPMSendQuery()`, `document.querySelector()`
- 条件付き依存: `if (!promoEnabled || !shouldShowPromo)` → `container.remove()`
- 条件付き依存: `if (!novaEnabled && messageId)` → `container .querySelector(".promo-dismiss") ?.addEventListener()`
- 条件付き依存: `if (!novaEnabled && messageId)` → `container .querySelector()`
- 条件付き依存: `if (!promoButton?.action)` → `container.remove()`
- 条件付き依存: `if (novaEnabled)` → `renderNovaPromo()`
- 条件付き依存: `if (!(novaEnabled))` → `renderLegacyPromo()`
- 参照: `promoButton?.action`

## onLinkClick()
- 位置: async L58-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `event.preventDefault()`, `window.PrivateBrowsingIsEnrolledInExperiment()`
- 参照: `promoButton.action`, `promoButton?.action?.data`, `promoButton?.action?.type`, `promoButtonData.content.metrics`, `promoButtonData?.content`

## onDismiss()
- 位置: L75-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.remove()`, `window.ASRouterMessage()`

## resolvePromoText()
- 位置: async L138-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value.replace()`
- 条件付き依存: `if (fluentId !== value)` → `document.l10n.formatValue()`
- 条件付き依存: `if (fluentId !== value)` → `console.error()`

## renderNovaPromo()
- 位置: async L165-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(useButton ? linkEl : buttonEl).remove()`, `container.querySelector()`, `ctaEl.addEventListener()`, `customElements.whenDefined()`, `document.querySelector()`, `infoBorderEl?.insertAdjacentElement()`, `resolvePromoText()`
- 条件付き依存: `if (dismissable)` → `promoEl.addEventListener()`
- 条件付き依存: `if (dismissable)` → `event.preventDefault()`
- 条件付き依存: `if (dismissable)` → `onDismiss()`
- 条件付き依存: `if (promoHeader)` → `resolvePromoText()`
- 条件付き依存: `if (promoTitleEnabled)` → `resolvePromoText()`
- 参照: `container.hidden`, `ctaEl.label`, `ctaEl.textContent`, `promoEl.dismissable`, `promoEl.heading`, `promoEl.imageSrc`, `promoEl.message`

## renderLegacyPromo()
- 位置: L229-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.classList.add()`, `document.getElementById()`, `document.querySelector()`, `linkEl.addEventListener()`, `translateElements()`
- 条件付き依存: `if (promoLinkType === "link")` → `linkEl.classList.remove()`
- 条件付き依存: `if (promoLinkType === "link")` → `linkEl.classList.add()`
- 条件付き依存: `if (promoSectionStyle)` → `container.classList.add()`
- 条件付き依存: `if (promoSectionStyle)` → `container.remove()`
- 条件付き依存: `if (promoSectionStyle)` → `infoContainerEl?.insertAdjacentElement()`
- 条件付き依存: `if (promoSectionStyle)` → `document.body.insertAdjacentElement()`
- 条件付き依存: `if (!(promoImageLarge))` → `promoImageLargeEl.parentNode.remove()`
- 条件付き依存: `if (!(promoImageSmall))` → `promoImageSmallEl.parentNode.remove()`
- 条件付き依存: `if (!promoTitleEnabled)` → `titleEl.remove()`
- 条件付き依存: `if (!promoHeader)` → `promoHeaderEl.remove()`
- 参照: `container.hidden`, `promoImageLargeEl.src`, `promoImageSmallEl.src`

## recordOnceVisible()
- 位置: L307-330
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (document.visibilityState === "visible")` → `window.ASRouterMessage()`
- 条件付き依存: `if (document.visibilityState === "visible")` → `window.PrivateBrowsingPromoExposureTelemetry()`
- 条件付き依存: `if (!(document.visibilityState === "visible"))` → `document.addEventListener()`
- 参照: `document.visibilityState`

## recordImpression()
- 位置: L308-318
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (document.visibilityState === "visible")` → `window.ASRouterMessage()`
- 条件付き依存: `if (document.visibilityState === "visible")` → `window.PrivateBrowsingPromoExposureTelemetry()`
- 条件付き依存: `if (document.visibilityState === "visible")` → `document.removeEventListener()`
- 参照: `document.visibilityState`

## handlePromoOnPreload()
- 位置: L333-348
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (document.visibilityState !== "visible")` → `document.addEventListener()`
- 参照: `document.visibilityState`

## removePromoIfBlocked()
- 位置: async L334-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.removeEventListener()`
- 条件付き依存: `if (document.visibilityState === "visible")` → `RPMSendQuery()`
- 条件付き依存: `if (blocked)` → `document.querySelector()`
- 条件付き依存: `if (blocked)` → `container?.remove()`
- 参照: `document.visibilityState`

## setupMessageConfig()
- 位置: async L350-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.setAttribute()`, `renderPromo()`
- 条件付き依存: `if (!config)` → `window.PrivateBrowsingShouldHideDefault()`
- 条件付き依存: `if (!config)` → `document.documentElement.classList.contains()`
- 条件付き依存: `if (!config)` → `window.ASRouterMessage()`
- 条件付き依存: `if (hasRendered && message)` → `recordOnceVisible()`
- 条件付き依存: `if (hasRendered && message)` → `handlePromoOnPreload()`
- 参照: `config.messageId`, `message?.content`, `message?.id`, `response?.message`

## showDevToolsMessage()
- 位置: L381-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMRemoveMessageListener()`, `setupMessageConfig()`
- 参照: `msg.data.content.messageId`, `msg?.data?.content`

## hideSearchBanner()
- 位置: L504-508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `document.body.classList.remove()`
- 参照: `privateSearchBanner.hidden`

## openSearchOptionsEvtHandler()
- 位置: L519-527
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( evt.target.id == "open-search-options-link" && (evt.keyCode == evt.DOM_VK_RETURN || evt.type == "click") )` → `RPMSendAsyncMessage()`
- 条件付き依存: `if ( evt.target.id == "open-search-options-link" && (evt.keyCode == evt.DOM_VK_RETURN || evt.type == "click") )` → `hideSearchBanner()`
- 参照: `evt.DOM_VK_RETURN`, `evt.keyCode`, `evt.target.id`, `evt.type`
