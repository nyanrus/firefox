# browser/components/asrouter/modules/SidebarChatBotPromo.sys.mjs

source: browser/components/asrouter/modules/SidebarChatBotPromo.sys.mjs
source-hash: 6b9b65feb747132dc8493d79c8d9591ef9b284a5
lines: 198

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`

## getPromoElement()
- 位置: async L40-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findPromo()`, `resolve()`, `sidebarBrowser.addEventListener()`, `sidebarBrowser.removeEventListener()`, `win.setTimeout()`
- 条件付き依存: `if (force)` → `win?.SidebarController?.show()`
- 参照: `browser?.browsingContext?.topChromeWindow`, `browser?.documentGlobal`, `win?.SidebarController?.browser`

## findPromo()
- 位置: L51-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebarBrowser.contentDocument?.getElementById()`

## onLoad()
- 位置: L61-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `sidebarBrowser.removeEventListener()`, `win.clearTimeout()`

## showPromo()
- 位置: async L76-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PROMO_LISTENERS.set()`, `Services.prefs.getStringPref()`, `lazy.ASRouter.addImpression()`, `lazy.ASRouter.getMessageById()`, `promo.addEventListener()`, `promo.ownerDocument.getElementById()`, `promo.ownerDocument.getElementById("footer")?.classList.add()`, `this.detachListeners()`, `this.getPromoElement()`, `this.handleButtonAction()`, `this.recordTelemetry()`, `this.resolveText()`
- 参照: `SIDEBAR_CHATBOT_PROMO_EVENTS.CLOSE`, `SIDEBAR_CHATBOT_PROMO_EVENTS.IMPRESSION`, `SIDEBAR_CHATBOT_PROMO_EVENTS.PRIMARY`, `additionalButton.label`, `content.additional_button`, `content.heading`, `content.message`, `content.primary_button`, `content.type`, `message.content`, `message.id`, `message?.id`, `primaryButton.label`, `promo.message`, `promoContent.additionalActionText`, `promoContent.heading`, `promoContent.message`, `promoContent.primaryActionText`
- XPCOM: `Services.prefs`

## hide()
- 位置: L151-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promo.ownerDocument .getElementById()`, `promo.ownerDocument .getElementById("footer") ?.classList.remove()`, `this.detachListeners()`
- 参照: `promo.message`

## handleButtonAction()
- 位置: L162-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hide()`
- 条件付き依存: `if (button.action)` → `lazy.SpecialMessageActions.handleAction()`
- 参照: `button.action`

## recordTelemetry()
- 位置: L169-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.dispatchCFRAction()`

## detachListeners()
- 位置: L180-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PROMO_LISTENERS.get()`
- 条件付き依存: `if (ac)` → `ac.abort()`
- 条件付き依存: `if (ac)` → `PROMO_LISTENERS.delete()`

## resolveText()
- 位置: async L188-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteL10n.formatLocalizableText()`
