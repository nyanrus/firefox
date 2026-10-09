# browser/components/asrouter/modules/ToastNotification.sys.mjs

source: browser/components/asrouter/modules/ToastNotification.sys.mjs
source-hash: f15adf09abad19b0ad3af180c29bb85806f31631
lines: 247

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `console.createInstance()`

## AlertsService()
- 位置: L29-31
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AlertsService`

## sendUserEventTelemetry()
- 位置: L33-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatch()`
- 参照: `message.id`

## imageUrlForContent()
- 位置: L51-62
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo.chromeColorSchemeIsDark`, `Services.appinfo.prefersReducedMotion`, `content.dark_mode_image_url`, `content.dark_mode_reduced_motion_image_url`, `content.image_url`, `content.reduced_motion_image_url`
- XPCOM: `Services.appinfo`

## showToastNotification()
- 位置: async L71-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `alert.init()`, `dispatch()`, `imageData?.name.endsWith()`, `lazy.NimbusFeatures.backgroundTaskMessage.getEnrollmentMetadata()`, `lazy.RemoteL10n.formatLocalizableText()`, `this.AlertsService.isFullscreen()`, `this.AlertsService.showAlert()`, `this.imageUrlForContent()`, `this.sendUserEventTelemetry()`
- 条件付き依存: `if (this.AlertsService.isFullscreen?.())` → `lazy.logConsole.warn()`
- 条件付き依存: `if (imageUrl)` → `url.pathname.split("/").pop()`
- 条件付き依存: `if (imageUrl)` → `url.pathname.split()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `Cc["@mozilla.org/windows-alert-notification;1"].createInstance()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `fetch()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `resp.arrayBuffer()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `Services.uuid.generateUUID().toString()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `Services.uuid.generateUUID()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `PathUtils.join()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `lazy.logConsole.info()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `IOUtils.write()`
- 条件付き依存: `if (AppConstants.platform === "win" && imageData?.name.endsWith(".gif"))` → `lazy.logConsole.warn()`
- 条件付き依存: `if (!(AppConstants.platform === "win" && imageData?.name.endsWith(".gif")))` → `Cc["@mozilla.org/alert-notification;1"].createInstance()`
- 条件付き依存: `if (imageData?.url)` → `Services.io.newURI()`
- 条件付き依存: `if (imageData?.url)` → `Services.io.newChannelFromURI()`
- 条件付き依存: `if (imageData?.url)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (imageData?.url)` → `ChromeUtils.fetchDecodedImage()`
- 条件付き依存: `if (imageData?.url)` → `console.error()`
- 条件付き依存: `if (content.actions)` → `Cu.cloneInto()`
- 条件付き依存: `if (action.title)` → `lazy.RemoteL10n.formatLocalizableText()`
- 条件付き依存: `if (action.launch_action)` → `JSON.stringify()`
- 条件付き依存: `if (relaunchAction)` → `JSON.stringify()`
- 参照: `AppConstants.platform`, `Ci.nsIAlertNotification`, `Ci.nsIContentPolicy.TYPE_IMAGE`, `Ci.nsILoadInfo.SEC_ALLOW_CROSS_ORIGIN_SEC_CONTEXT_IS_NULL`, `Ci.nsIWindowsAlertNotification`, `PathUtils.tempDir`, `action.launch_action`, `action.opaqueRelaunchData`, `action.title`, `alert.actions`, `alert.image`, `alert.imagePathUnchecked`, `alert.opaqueRelaunchData`, `content.actions`, `content.body`, `content.data`, `content.launch_action`, `content.launch_url`, `content.requireInteraction`, `content.title`, `experimentMetadata.branch`, `experimentMetadata.slug`, `imageData.name`, `imageData.url`, `imageData?.url`, `lazy.EnrollmentType.EXPERIMENT`, `resp.ok`
- XPCOM: [`nsIAlertNotification`](../../../../toolkit/components/alerts/nsIAlertsService.idl.md) / [`nsIContentPolicy`](../../../../dom/base/nsIContentPolicy.idl.md) / [`nsILoadInfo`](../../../../dom/base/nsIContentPolicy.idl.md) / [`nsIWindowsAlertNotification`](../../../../toolkit/components/alerts/nsIWindowsAlertsService.idl.md) / `@mozilla.org/alert-notification;1` / `@mozilla.org/windows-alert-notification;1` / `Services.io` / `Services.scriptSecurityManager` / `Services.uuid`

## obs()
- 位置: L227-238
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "alertshow")` → `shownPromise.resolve()`
- 条件付き依存: `if (topic === "alertfinished" && alert?.imagePathUnchecked)` → `lazy.logConsole.info()`
- 条件付き依存: `if (topic === "alertfinished" && alert?.imagePathUnchecked)` → `IOUtils.remove()`
- 参照: `alert.imagePathUnchecked`, `alert?.imagePathUnchecked`
