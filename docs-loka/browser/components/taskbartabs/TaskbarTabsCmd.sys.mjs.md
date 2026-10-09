# browser/components/taskbartabs/TaskbarTabsCmd.sys.mjs

source: browser/components/taskbartabs/TaskbarTabsCmd.sys.mjs
source-hash: b44b9d24f1ac670c80603fa7200d6a3f8d189a4b
lines: 104

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Components.ID()`, `console.createInstance()`

## CommandLineHandler.handle()
- 位置: L30-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.startup.enterLastWindowClosingSurvivalArea()`, `Services.startup.exitLastWindowClosingSurvivalArea()`, `aCmdLine.handleFlagWithParam()`, `launchTaskbarTab()`, `launchTaskbarTab(context).finally()`, `lazy.TaskbarTabsUtils.isEnabled()`, `lazy.logConsole.info()`
- 条件付き依存: `if (!lazy.TaskbarTabsUtils.isEnabled())` → `lazy.logConsole.info()`
- 条件付き依存: `if (containerParam !== null)` → `Number()`
- 参照: `aCmdLine.preventDefault`, `context.url`, `context.userContextId`
- XPCOM: `Services.io` / `Services.startup`

## launchTaskbarTab()
- 位置: async L74-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`, `lazy.TaskbarTabs.findOrCreateTaskbarTab()`, `lazy.TaskbarTabs.getTaskbarTab()`, `lazy.TaskbarTabs.openWindow()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (!Object.hasOwn(aContext, "userContextId"))` → `lazy.logConsole.error()`
- 参照: `Services.scriptSecurityManager.DEFAULT_USER_CONTEXT_ID`, `aContext.id`, `aContext.url`, `aContext.userContextId`
- XPCOM: `Services.scriptSecurityManager`
