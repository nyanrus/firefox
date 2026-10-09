# browser/components/asrouter/modules/ASRouterParentProcessMessageHandler.sys.mjs

source: browser/components/asrouter/modules/ASRouterParentProcessMessageHandler.sys.mjs
source-hash: 390bfcd647c428473d6edc69e7c3f980d61300be
lines: 179

## <module>
- 役割: (未記入)

## ASRouterParentProcessMessageHandler.constructor()
- 位置: L10-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleCFRAction.bind()`, `this.handleMessage.bind()`
- 参照: `this._preferences`, `this._queryCache`, `this._router`, `this._specialMessageActions`, `this.handleCFRAction`, `this.handleMessage`, `this.handleTelemetry`

## ASRouterParentProcessMessageHandler.handleCFRAction()
- 位置: L26-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleMessage()`, `this.handleTelemetry()`
- 参照: `msg.ACTION_ONLY_TELEMETRY`, `msg.DOORHANGER_TELEMETRY`, `msg.INFOBAR_TELEMETRY`, `msg.MENU_MESSAGE_TELEMETRY`, `msg.MOMENTS_PAGE_TELEMETRY`, `msg.NEWTAB_MESSAGE_TELEMETRY`, `msg.SIDEBAR_CHATBOT_PROMO_TELEMETRY`, `msg.SMART_WINDOW_PROMO_TELEMETRY`, `msg.SPOTLIGHT_TELEMETRY`, `msg.TOAST_NOTIFICATION_TELEMETRY`, `msg.TOOLBAR_BADGE_TELEMETRY`

## ASRouterParentProcessMessageHandler.handleMessage()
- 位置: L47-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterPreferences.console.debug()`, `ASRouterPreferences.console.trace()`, `ASRouterScreenUtils.addScreenImpression()`, `ASRouterScreenUtils.evaluateTargetingAndRemoveScreens()`, `Object.entries()`, `Promise.reject()`, `Promise.resolve()`, `Services.prefs.getStringPref()`, `data.bundle.map()`, `messageBlockList.indexOf()`, `messageBlockList.splice()`, `this._preferences.enableOrDisableProvider()`, `this._preferences.resetProviderPref()`, `this._preferences.setUserPreference()`, `this._queryCache.expireAll()`, `this._router .blockMessageById()`, `this._router .blockMessageById(data.id) .then()`, `this._router .resetGroupsState()`, `this._router .resetGroupsState(data) .then()`, `this._router._storage.set()`, `this._router.addImpression()`, `this._router.blockMessageById()`, `this._router.editState()`, `this._router.evaluateExpression()`, `this._router.forceAttribution()`, `this._router.forcePBWindow()`, `this._router.loadMessagesFromAllProviders()`, `this._router.resetMessageState()`, `this._router.resetScreenImpressions()`, `this._router.routeCFRMessage()`, `this._router.sendPBNewTabMessage()`, `this._router.sendTriggerMessage()`, `this._router.setMessageById()`, `this._router.setState()`, `this._router.unblockAll()`, `this._router.unblockMessageById()`, `this._router.updateTargetingParameters()`, `this._specialMessageActions.handleAction()`, `this.handleTelemetry()`
- 条件付き依存: `if (data && data.endpoint)` → `this._router.loadMessagesFromAllProviders()`
- 参照: `b.id`, `data.bundle`, `data.content`, `data.endpoint`, `data.id`, `data.message`, `data.preventDismiss`, `data.trigger`, `data.value`, `message.id`, `msg.ADMIN_CONNECT_STATE`, `msg.AS_ROUTER_TELEMETRY_USER_EVENT`, `msg.AW_ADD_SCREEN_IMPRESSION`, `msg.AW_EVALUATE_SCREEN_TARGETING`, `msg.AW_GET_ACTIVE_THEME_ID`, `msg.BLOCK_BUNDLE`, `msg.BLOCK_MESSAGE_BY_ID`, `msg.DISABLE_PROVIDER`, `msg.EDIT_STATE`, `msg.ENABLE_PROVIDER`, `msg.EVALUATE_JEXL_EXPRESSION`, `msg.EXPIRE_QUERY_CACHE`, `msg.FORCE_ATTRIBUTION`, `msg.FORCE_PRIVATE_BROWSING_WINDOW`, `msg.IMPRESSION`, `msg.MODIFY_MESSAGE_JSON`, `msg.OVERRIDE_MESSAGE`, `msg.PBNEWTAB_MESSAGE_REQUEST`, `msg.RESET_GROUPS_STATE`, `msg.RESET_MESSAGE_STATE`, `msg.RESET_PROVIDER_PREF`, `msg.RESET_SCREEN_IMPRESSIONS`, `msg.SET_PROVIDER_USER_PREF`, `msg.TRIGGER`, `msg.UNBLOCK_ALL`, `msg.UNBLOCK_BUNDLE`, `msg.UNBLOCK_MESSAGE_BY_ID`, `msg.USER_ACTION`, `state.messageBlockList`
- XPCOM: `Services.prefs`
