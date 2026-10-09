# browser/components/taskbartabs/TaskbarTabs.sys.mjs

source: browser/components/taskbartabs/TaskbarTabs.sys.mjs
source-hash: aa395b25ed92c802f1b16cdca1d5e62a82481965
lines: 409

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## constructor()
- 位置: L42-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `initRegistry()`, `initRegistry().then()`, `initWindowManager()`, `this.#updateMetrics()`
- 参照: `this.#ready`, `this.#registry`, `this.#windowManager`

## #updateMetrics()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webApp.installedWebAppCount.set()`, `this.#registry.countTaskbarTabs()`

## waitUntilReady()
- 位置: async L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#ready`

## getTaskbarTab()
- 位置: async L59-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registry.getTaskbarTab()`
- 参照: `this.#ready`

## findOrCreateTaskbarTab()
- 位置: async L84-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#findOrCreateTaskbarTab()`
- 条件付き依存: `if (aDetails.manifest)` → `lazy.ManifestProcessor.process()`
- 条件付き依存: `if (aDetails.manifest)` → `JSON.stringify()`
- 条件付き依存: `if (result.created || aDetails.ensurePinned)` → `this.#pinTaskbarTab()`
- 参照: `aDetails.ensurePinned`, `aDetails.manifest`, `aDetails.window`, `aUrl.prePath`, `result.created`, `result.icon`, `result.taskbarTab`

## #findOrCreateTaskbarTab()
- 位置: async L120-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registry.findOrCreateTaskbarTab()`
- 条件付き依存: `if (!aDetails.manifest?.name && aUrl.scheme === "moz-extension")` → `WebExtensionPolicy.getByURI()`
- 条件付き依存: `if (result.created)` → `this.#updateMetrics()`
- 条件付き依存: `if (result.created)` → `fetchIconForTaskbarTab()`
- 条件付き依存: `if (!(result.created))` → `loadSavedTaskbarTabIcon()`
- 参照: `WebExtensionPolicy.getByURI(aUrl)?.name`, `aDetails.manifest`, `aDetails.manifest?.name`, `aUrl.scheme`, `result.created`, `result.icon`, `result.taskbarTab`, `result.taskbarTab.id`, `this.#ready`

## #pinTaskbarTab()
- 位置: async L148-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TaskbarTabsPin.pinTaskbarTab()`, `this.#registry.patchTaskbarTab()`

## findTaskbarTab()
- 位置: async L160-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registry.findTaskbarTab()`
- 参照: `this.#ready`

## countTaskbarTabs()
- 位置: async L165-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registry.countTaskbarTabs()`
- 参照: `this.#ready`

## moveTabIntoTaskbarTab()
- 位置: async L180-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.ManifestObtainer.browserObtainManifest()`, `lazy.ManifestObtainer.browserObtainManifest(browser).catch()`, `lazy.logConsole.error()`, `this.#findOrCreateTaskbarTab()`, `this.#windowManager.replaceTabWithWindow()`
- 条件付き依存: `if (created)` → `this.#pinTaskbarTab()`
- 参照: `aTab.linkedBrowser`, `aTab.userContextId`, `browser.currentURI`, `this.#ready`

## resetForTests()
- 位置: async L223-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registry.resetForTests()`
- 参照: `this.#ready`

## removeTaskbarTab()
- 位置: async L228-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TaskbarTabsPin.unpinTaskbarTab()`, `this.#registry.removeTaskbarTab()`, `this.#updateMetrics()`
- 参照: `this.#ready`

## openWindow()
- 位置: async L238-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadSavedTaskbarTabIcon()`, `this.#windowManager.openWindow()`
- 参照: `aTaskbarTab.id`, `this.#ready`

## replaceTabWithWindow()
- 位置: async L245-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadSavedTaskbarTabIcon()`, `this.#windowManager.replaceTabWithWindow()`
- 参照: `aTaskbarTab.id`, `this.#ready`

## ejectWindow()
- 位置: async L252-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowManager.ejectWindow()`
- 参照: `this.#ready`

## getCountForId()
- 位置: async L257-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowManager.getCountForId()`
- 参照: `this.#ready`

## initRegistry()
- 位置: async L268-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TaskbarTabsUtils.getTaskbarTabsFolder()`, `new TaskbarTabsRegistryStorage(registryFile).load()`, `registryFile.append()`

## initWindowManager()
- 位置: L282-286
- 役割: (未記入)
- 触るとき: (未記入)

## fetchIconForTaskbarTab()
- 位置: async L288-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `TaskbarTabsUtils._remoteDecodeImageFromURI()`, `TaskbarTabsUtils.getDefaultIcon()`, `TaskbarTabsUtils.getFaviconUri()`, `choice()`, `findBestManifestIcon()`, `lazy.logConsole.warn()`
- 条件付き依存: `if (aDetails.browser)` → `lazy.ManifestIcons.browserFetchIcon()`
- 条件付き依存: `if (aDetails.browser)` → `Services.io.newURI()`
- 参照: `aDetails.browser`, `aDetails.createdForUrl`, `aDetails.manifest`, `aTaskbarTab.startUrl`
- XPCOM: `Services.io`

## loadSavedTaskbarTabIcon()
- 位置: async L341-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TaskbarTabsUtils._remoteDecodeImageFromFile()`, `TaskbarTabsUtils.getDefaultIcon()`, `TaskbarTabsUtils.getTaskbarTabsFolder()`, `iconPath.append()`, `lazy.logConsole.warn()`
- 参照: `lazy.ShellService.shortcutIconType.extension`, `lazy.ShellService.shortcutIconType.mimeType`

## findBestManifestIcon()
- 位置: L373-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["", "any"].includes()`, `aManifest.icons?.flatMap()`, `collectedIcons.findIndex()`, `collectedIcons.sort()`, `icon.purpose.includes()`, `parseInt()`, `sizes.map()`
- 参照: `a.size`, `b.size`, `collectedIcons.length`, `collectedIcons[collectedIcons.length - 1].src`, `collectedIcons[index].src`, `icon.size`, `icon.sizes`, `icon.src`
