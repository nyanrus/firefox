# browser/components/messagepreview/actors/AboutMessagePreviewParent.sys.mjs

source: browser/components/messagepreview/actors/AboutMessagePreviewParent.sys.mjs
source-hash: 00aa03290b22f559fc4d8a9aaad01dee887435af
lines: 222

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.declareLazy()`

## log()
- 位置: L24-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## dispatchCFRAction()
- 位置: L37-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (type === "USER_ACTION")` → `lazy.SpecialMessageActions.handleAction()`

## infobar()
- 位置: L63-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.InfoBar.showInfoBarMessage()`

## spotlight()
- 位置: L66-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Spotlight.showSpotlightDialog()`

## feature_callout()
- 位置: async L69-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FeatureCalloutBroker.showFeatureCallout()`
- 条件付き依存: `if (tourPref)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!showing)` → `existingAnchors[0].hasOwnProperty()`
- 条件付き依存: `if (!showing)` → `lazy.log.debug()`
- 条件付き依存: `if (!showing)` → `lazy.FeatureCalloutBroker.showFeatureCallout()`
- 参照: `fallbackAnchor.arrow_position`, `fallbackAnchor.panel_position`, `message.content.screens`, `message.content.tour_pref_name`, `message.targeting`, `message.trigger`, `screen.anchors`
- XPCOM: `Services.prefs`

## bookmarks_bar_button()
- 位置: L108-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BookmarksBarButton.showBookmarksBarButton()`, `lazy.CustomizableUI.setToolbarVisibility()`
- 参照: `lazy.CustomizableUI.AREA_BOOKMARKS`

## pb_newtab()
- 位置: L117-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.forcePBWindow()`

## sidebar_chatbot_promo()
- 位置: L120-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SidebarChatBotPromo.showPromo()`

## AboutMessagePreviewParent.getSupportedTemplates()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`

## AboutMessagePreviewParent.constructor()
- 位置: L136-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `super()`
- 参照: `this._onUnload`
- XPCOM: `Services.prefs`

## this._onUnload()
- 位置: L143-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addon.enable()`, `lazy.AddonManager.getAddonByID()`, `lazy.AddonManager.getAddonByID(EXISTING_THEME).then()`

## AboutMessagePreviewParent.didDestroy()
- 位置: L150-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onUnload()`

## AboutMessagePreviewParent.showMessage()
- 位置: async L164-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `lazy.MessageLoaderUtils._delocalizeValues()`, `lazy.log.error()`
- 条件付き依存: `if (validationEnabled)` → `fetch( "chrome://browser/content/asrouter/schemas/MessagingExperiment.schema.json", { credentials: "omit" } ).then()`
- 条件付き依存: `if (validationEnabled)` → `fetch()`
- 条件付き依存: `if (validationEnabled)` → `rsp.json()`
- 条件付き依存: `if (validationEnabled)` → `lazy.JsonSchema.validate()`
- 条件付き依存: `if (!result.valid)` → `lazy.log.error()`
- 条件付き依存: `if (!result.valid)` → `JSON.stringify()`
- 条件付き依存: `if (handler)` → `handler()`
- 条件付き依存: `if (!(handler))` → `lazy.log.error()`
- 参照: `message.template`, `result.errors`, `result.valid`, `this.browsingContext.topChromeWindow.gBrowser.selectedBrowser`

## AboutMessagePreviewParent.receiveMessage()
- 位置: async L202-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addon.enable()`, `lazy.AddonManager.getAddonByID()`, `lazy.AddonManager.getAddonByID(theme).then()`, `lazy.log.debug()`, `this.showMessage()`
- 参照: `SWITCH_THEMES.DARK`, `SWITCH_THEMES.LIGHT`, `data.isDark`
