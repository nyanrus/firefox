# browser/components/asrouter/modules/ASRouterTelemetry.sys.mjs

source: browser/components/asrouter/modules/ASRouterTelemetry.sys.mjs
source-hash: 1ae15f8a75f1d9fdf6471ded6d8fd4835fcdb6df
lines: 287

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `lazy.TelemetrySession.getMetadata()`

## ASRouterTelemetry.constructor()
- 位置: L43-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getOrCreateImpressionId()`
- 参照: `this._impressionId`

## ASRouterTelemetry.telemetryClientId()
- 位置: L47-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `lazy.ClientID.getClientID()`
- 参照: `this.telemetryClientId`

## ASRouterTelemetry.getOrCreateImpressionId()
- 位置: L54-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`
- 条件付き依存: `if (!impressionId)` → `String()`
- 条件付き依存: `if (!impressionId)` → `Services.uuid.generateUUID()`
- 条件付き依存: `if (!impressionId)` → `Services.prefs.setCharPref()`
- XPCOM: `Services.prefs` / `Services.uuid`

## ASRouterTelemetry.isInCFRCohort()
- 位置: L68-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.cfr.getEnrollmentMetadata()`
- 参照: `lazy.EnrollmentType.EXPERIMENT`

## ASRouterTelemetry.createASRouterEvent()
- 位置: async L78-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.applyActionOnlyPolicy()`, `this.applyCFRPolicy()`, `this.applyInfoBarPolicy()`, `this.applyMenuMessagePolicy()`, `this.applyMomentsPolicy()`, `this.applyNewtabMessagePolicy()`, `this.applySidebarChatBotPromoPolicy()`, `this.applySmartWindowPromoPolicy()`, `this.applySpotlightPolicy()`, `this.applyToastNotificationPolicy()`, `this.applyToolbarBadgePolicy()`, `this.applyUndesiredEventPolicy()`
- 参照: `Services.appinfo.appBuildID`, `Services.locale.appLocaleAsBCP47`, `action.data`, `event.action`
- XPCOM: `Services.appinfo` / `Services.locale`

## ASRouterTelemetry.applyCFRPolicy()
- 位置: async L136-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UpdateUtils.getUpdateChannel()`
- 参照: `ping.action`, `ping.client_id`, `ping.impression_id`, `ping.is_private`, `ping.message_id`, `this._impressionId`, `this.isInCFRCohort`, `this.telemetryClientId`

## ASRouterTelemetry.applyToolbarBadgePolicy()
- 位置: async L156-162
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applyInfoBarPolicy()
- 位置: async L164-169
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applySpotlightPolicy()
- 位置: async L171-176
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applyToastNotificationPolicy()
- 位置: async L178-183
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applyMenuMessagePolicy()
- 位置: async L185-190
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applySmartWindowPromoPolicy()
- 位置: async L192-197
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applySidebarChatBotPromoPolicy()
- 位置: async L199-204
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applyMomentsPolicy()
- 位置: async L206-211
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applyActionOnlyPolicy()
- 位置: async L213-218
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applyNewtabMessagePolicy()
- 位置: async L220-225
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.browserSessionId`, `ping.action`, `ping.browser_session_id`, `ping.client_id`, `this.telemetryClientId`

## ASRouterTelemetry.applyUndesiredEventPolicy()
- 位置: L227-231
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ping.action`, `ping.impression_id`, `this._impressionId`

## ASRouterTelemetry.handleASRouterUserEvent()
- 位置: async L233-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Telemetry.parseAndSubmitPing()`, `this.createASRouterEvent()`
- 条件付き依存: `if (!pingType)` → `console.error()`

## ASRouterTelemetry.SendASRouterUndesiredEvent()
- 位置: L247-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleASRouterUserEvent()`

## ASRouterTelemetry.onAction()
- 位置: L253-285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleASRouterUserEvent()`
- 参照: `action.type`, `msg.ACTION_ONLY_TELEMETRY`, `msg.AS_ROUTER_TELEMETRY_USER_EVENT`, `msg.DOORHANGER_TELEMETRY`, `msg.INFOBAR_TELEMETRY`, `msg.MENU_MESSAGE_TELEMETRY`, `msg.MOMENTS_PAGE_TELEMETRY`, `msg.NEWTAB_MESSAGE_TELEMETRY`, `msg.SIDEBAR_CHATBOT_PROMO_TELEMETRY`, `msg.SMART_WINDOW_PROMO_TELEMETRY`, `msg.SPOTLIGHT_TELEMETRY`, `msg.TOAST_NOTIFICATION_TELEMETRY`, `msg.TOOLBAR_BADGE_TELEMETRY`, `msg.TOOLBAR_PANEL_TELEMETRY`
