# browser/components/asrouter/modules/MenuMessage.sys.mjs

source: browser/components/asrouter/modules/MenuMessage.sys.mjs
source-hash: cbf43ace23a23f3283c6d3e01d901fbf191f7dab
lines: 365

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`

## showMenuMessage()
- 位置: async L37-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.MESSAGE_TYPE_ALLOWED_BY_SOURCE[source]?.has()`, `this.showAppMenuMessage()`, `this.showPxiMenuMessage()`
- 参照: `browser.documentGlobal`, `message.content.messageType`, `message.testingTriggerContext`, `this.MESSAGE_TYPE_ALLOWED_BY_SOURCE`, `this.SOURCES.APP_MENU`, `this.SOURCES.PXI_MENU`, `trigger?.context?.source`

## shouldSuppressForSignedIn()
- 位置: L78-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UIState.get()`
- 参照: `lazy.UIState.STATUS_SIGNED_IN`, `lazy.UIState.get().status`, `message.content?.allowWhenSignedIn`, `message?.content?.messageType`, `this.MESSAGE_TYPES.FXA_CTA`

## preparePrimaryAction()
- 位置: L98-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `structuredClone()`
- 参照: `action.data`, `action.data.entrypoint`, `action.data.extraParams`, `action.data.extraParams.utm_content`, `message?.content?.messageType`, `message?.content?.primaryAction`, `this.MESSAGE_TYPES.FXA_CTA`, `this.SOURCES.APP_MENU`, `this.SOURCES.PXI_MENU`

## showAppMenuMessage()
- 位置: async L124-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `msgContainer.appendChild()`, `msgElement.addEventListener()`, `this.constructMenuMessage()`, `this.hideAppMenuMessage()`, `this.shouldSuppressForSignedIn()`, `win.PanelUI.hide()`, `win.PanelUI.mainView.removeAttribute()`, `win.PanelUI.mainView.setAttribute()`
- 条件付き依存: `if (force)` → `win.PanelUI.show()`
- 参照: `MenuMessage.SHOWING_FXA_MENU_MESSAGE_ATTR`, `MenuMessage.SHOWING_SET_TO_DEFAULT_MENU_MESSAGE_ATTR`, `MenuMessage.SOURCES.APP_MENU`, `browser.documentGlobal`, `lazy.AppMenuNotifications.activeNotification`, `message.content.layout`, `message.id`, `message?.content?.messageType`, `msgContainer.style.display`, `msgElement.style.flex`, `this.MESSAGE_TYPES.DEFAULT_CTA`

## hideAppMenuMessage()
- 位置: L173-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PanelMultiView.getViewNode()`, `win.PanelUI.mainView.removeAttribute()`
- 参照: `MenuMessage.SHOWING_FXA_MENU_MESSAGE_ATTR`, `MenuMessage.SHOWING_SET_TO_DEFAULT_MENU_MESSAGE_ATTR`, `browser.documentGlobal`, `browser.ownerDocument`, `msgContainer.innerHTML`

## showPxiMenuMessage()
- 位置: async L191-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fxaPanelView.closest()`, `fxaPanelView.removeAttribute()`, `fxaPanelView.setAttribute()`, `lazy.PanelMultiView.getViewNode()`, `msgContainer.appendChild()`, `msgElement.addEventListener()`, `this.constructMenuMessage()`, `this.hidePxiMenuMessage()`, `this.shouldSuppressForSignedIn()`
- 条件付き依存: `if (panelNode)` → `lazy.PanelMultiView.hidePopup()`
- 条件付き依存: `if (force)` → `win.gSync.toggleAccountPanel()`
- 条件付き依存: `if (force)` → `document.getElementById()`
- 参照: `MenuMessage.SHOWING_FXA_MENU_MESSAGE_ATTR`, `MenuMessage.SOURCES.PXI_MENU`, `browser.documentGlobal`, `message.content.layout`, `message.id`, `msgContainer.style.display`, `msgElement.style.flex`

## hidePxiMenuMessage()
- 位置: L239-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fxaPanelView.removeAttribute()`, `lazy.PanelMultiView.getViewNode()`
- 参照: `MenuMessage.SHOWING_FXA_MENU_MESSAGE_ATTR`, `browser.ownerDocument`, `msgContainer.innerHTML`

## constructMenuMessage()
- 位置: async L251-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `lazy.RemoteL10n.formatLocalizableText()`, `lazy.SpecialMessageActions.handleAction()`, `msgElement.addEventListener()`, `msgElement.remove()`, `this.preparePrimaryAction()`, `this.recordMenuMessageTelemetry()`, `win.MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (message.content.layout !== "simple" && message.content.secondaryText)` → `lazy.RemoteL10n.formatLocalizableText()`
- 条件付き依存: `if (message.content.imageWidth !== undefined)` → `msgElement.style.setProperty()`
- 条件付き依存: `if (message.content.imageHeight !== undefined)` → `msgElement.style.setProperty()`
- 条件付き依存: `if (message.content.logoWidth !== undefined)` → `msgElement.style.setProperty()`
- 条件付き依存: `if (message.content.imageVerticalTopOffset !== undefined)` → `msgElement.style.setProperty()`
- 条件付き依存: `if (message.content.imageVerticalBottomOffset !== undefined)` → `msgElement.style.setProperty()`
- 条件付き依存: `if (message.content.containerVerticalBottomOffset !== undefined)` → `msgElement.style.setProperty()`
- 条件付き依存: `if (message.content.containerPaddingBottom !== undefined)` → `msgElement.style.setProperty()`
- 条件付き依存: `if (primaryAction)` → `lazy.SpecialMessageActions.handleAction()`
- 参照: `gBrowser.selectedBrowser`, `message.content.closeAction`, `message.content.containerPaddingBottom`, `message.content.containerVerticalBottomOffset`, `message.content.directionalImage`, `message.content.imageHeight`, `message.content.imagePosition`, `message.content.imageURL`, `message.content.imageVerticalBottomOffset`, `message.content.imageVerticalTopOffset`, `message.content.imageWidth`, `message.content.layout`, `message.content.logoURL`, `message.content.logoWidth`, `message.content.primaryActionText`, `message.content.primaryButtonSize`, `message.content.primaryText`, `message.content.rtlImageURL`, `message.content.secondaryText`, `message.id`, `msgElement.buttonText`, `msgElement.dataset.navigableWithTabOnly`, `msgElement.directionalImage`, `msgElement.imagePosition`, `msgElement.imageURL`, `msgElement.layout`, `msgElement.logoURL`, `msgElement.primaryButtonSize`, `msgElement.primaryText`, `msgElement.rtlImageURL`, `msgElement.secondaryText`

## recordMenuMessageTelemetry()
- 位置: L353-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.dispatchCFRAction()`
