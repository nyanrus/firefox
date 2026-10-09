# browser/components/asrouter/modules/Spotlight.sys.mjs

source: browser/components/asrouter/modules/Spotlight.sys.mjs
source-hash: f75e48dadbf8cf15c96c80e065d5e370606cbc1f
lines: 156

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## isOpen()
- 位置: L26-28
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._dialog`

## close()
- 位置: L30-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!window || this._dialogWindow === window)` → `dialog.close()`
- 参照: `this._dialog`, `this._dialogWindow`

## sendUserEventTelemetry()
- 位置: L43-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatch()`
- 参照: `data.event_context.write_in_microsurvey`, `message.content.id`, `message.content.write_in_microsurvey`, `message.content?.metrics`

## defaultDispatch()
- 位置: L59-64
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.type === "SPOTLIGHT_TELEMETRY")` → `lazy.AWTelemetry.sendTelemetry()`
- 参照: `message.data`, `message.type`

## showSpotlightDialog()
- 位置: async L74-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchCFRAction()`, `lazy.ASRouterScreenUtils.prepareContentForFirstPaint()`, `lazy.MessagingSystemAllowlists.ensureInit()`, `this.sendUserEventTelemetry()`, `win.addEventListener()`, `win.removeEventListener()`
- 条件付き依存: `if (message.trigger?.id === "lastWindowClose")` → `win.gDialogBox.replaceDialogIfOpen()`
- 条件付き依存: `if (message.trigger?.id === "lastWindowClose")` → `win.gBrowser .getTabDialogBox(win.gBrowser.selectedBrowser) .abortAllDialogs()`
- 条件付き依存: `if (message.trigger?.id === "lastWindowClose")` → `win.gBrowser .getTabDialogBox()`
- 条件付き依存: `if (renderedContent?.modal === "tab")` → `win.gBrowser .getTabDialogBox(browser) .open()`
- 条件付き依存: `if (renderedContent?.modal === "tab")` → `win.gBrowser .getTabDialogBox()`
- 条件付き依存: `if (!(renderedContent?.modal === "tab"))` → `win.gDialogBox.open()`
- 参照: `browser.isConnected`, `browser?.documentGlobal`, `message.content`, `message.content?.metrics`, `message.trigger?.id`, `renderedContent?.modal`, `this._dialog`, `this._dialogWindow`, `this.defaultDispatch`, `win.closed`, `win.gBrowser.selectedBrowser`, `win.gDialogBox.dialog`, `win.gDialogBox.isOpen`

## unloadHandler()
- 位置: L118-121
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._dialog`, `this._dialogWindow`
