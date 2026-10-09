# browser/components/asrouter/modules/SmartWindowNewTabPromo.sys.mjs

source: browser/components/asrouter/modules/SmartWindowNewTabPromo.sys.mjs
source-hash: b32b65982bd8f64ba56b9baa93a812ce61607f5f
lines: 149

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`

## showPromo()
- 位置: async L26-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PROMO_LISTENERS.set()`, `aiWindow.addEventListener()`, `browser.contentDocument?.querySelector()`, `lazy.ASRouter.addImpression()`, `lazy.ASRouter.getMessageById()`, `this.detachListeners()`, `this.hide()`, `this.recordTelemetry()`, `this.resolveText()`
- 条件付き依存: `if (primaryButton.action)` → `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if (additionalButton.action)` → `lazy.SpecialMessageActions.handleAction()`
- 参照: `SMARTWINDOW_PROMO_EVENTS.CLOSE`, `SMARTWINDOW_PROMO_EVENTS.DISMISS`, `SMARTWINDOW_PROMO_EVENTS.IMPRESSION`, `SMARTWINDOW_PROMO_EVENTS.PRIMARY`, `additionalButton.action`, `additionalButton.label`, `aiWindow.promoMessage`, `aiWindow?.documentGlobal`, `content.additional_button`, `content.dismissable`, `content.heading`, `content.imageAlignment`, `content.imageDisplay`, `content.imageSrc`, `content.imageWidth`, `content.message`, `content.primary_button`, `content.type`, `message.id`, `message?.content`, `message?.id`, `primaryButton.action`, `primaryButton.label`

## hide()
- 位置: L112-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.detachListeners()`
- 参照: `aiWindow.promoMessage`

## recordTelemetry()
- 位置: L120-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.dispatchCFRAction()`

## detachListeners()
- 位置: L131-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PROMO_LISTENERS.get()`
- 条件付き依存: `if (ac)` → `ac.abort()`
- 条件付き依存: `if (ac)` → `PROMO_LISTENERS.delete()`

## resolveText()
- 位置: async L139-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteL10n.formatLocalizableText()`
