# browser/components/aboutlogins/AboutLoginsChild.sys.mjs

source: browser/components/aboutlogins/AboutLoginsChild.sys.mjs
source-hash: 967023b4e8bac2133b50705b6664fa570b8642c4
lines: 319

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`

## recordTelemetryEvent()
- 位置: L24-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.pwmgr[name].record()`, `console.error()`
- 参照: `Glean.pwmgr`, `extra.value`

## AboutLoginsChild.handleEvent()
- 位置: L37-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#aboutLoginsCopyLoginDetail()`, `this.#aboutLoginsCreateLogin()`, `this.#aboutLoginsDeleteLogin()`, `this.#aboutLoginsExportPasswords()`, `this.#aboutLoginsGetHelp()`, `this.#aboutLoginsImportFromBrowser()`, `this.#aboutLoginsImportFromFile()`, `this.#aboutLoginsImportReportInit()`, `this.#aboutLoginsInit()`, `this.#aboutLoginsOpenPreferences()`, `this.#aboutLoginsRecordTelemetryEvent()`, `this.#aboutLoginsRemoveAllLogins()`, `this.#aboutLoginsSortChanged()`, `this.#aboutLoginsSyncEnable()`, `this.#aboutLoginsUpdateLogin()`
- 参照: `event.detail`, `event.type`

## AboutLoginsChild.#aboutLoginsInit()
- 位置: L102-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `Cu.waiveXrays()`, `this.sendAsyncMessage()`
- 参照: `this.browsingContext.window`, `waivedContent.AboutLoginsUtils`

## AboutLoginsChild.doLoginsMatch()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LoginHelper.doLoginsMatch()`

## AboutLoginsChild.getLoginOrigin()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LoginHelper.getLoginOrigin()`

## AboutLoginsChild.setFocus()
- 位置: L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.setFocus()`
- 参照: `Services.focus.FLAG_BYKEY`
- XPCOM: `Services.focus`

## AboutLoginsChild.promptForPrimaryPassword()
- 位置: async L127-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `that.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsImportReportInit()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsCopyLoginDetail()
- 位置: L156-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ClipboardHelper.copyString()`
- 参照: `lazy.ClipboardHelper.Sensitive`, `this.windowContext`

## AboutLoginsChild.#aboutLoginsCreateLogin()
- 位置: L164-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsDeleteLogin()
- 位置: L170-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsExportPasswords()
- 位置: L176-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsGetHelp()
- 位置: L180-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsImportFromBrowser()
- 位置: L184-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordTelemetryEvent()`, `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsImportFromFile()
- 位置: L191-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordTelemetryEvent()`, `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsOpenPreferences()
- 位置: L198-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordTelemetryEvent()`, `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsRecordTelemetryEvent()
- 位置: L205-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.detail.name.startsWith()`, `recordTelemetryEvent()`
- 条件付き依存: `if (event.detail.name.startsWith("openManagement"))` → `docShell.now()`
- 参照: `event.detail`, `this.browsingContext`, `this.browsingContext.browserId`

## AboutLoginsChild.#aboutLoginsRemoveAllLogins()
- 位置: L227-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsSortChanged()
- 位置: L231-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsSyncEnable()
- 位置: L235-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsUpdateLogin()
- 位置: L239-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.receiveMessage()
- 位置: L246-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#importReportData()`, `this.#passMessageDataToContent()`, `this.#primaryPasswordResponse()`, `this.#remaskPassword()`, `this.#setup()`, `this.document.hasFocus()`
- 条件付き依存: `if (!this.document.hasFocus())` → `this.document.documentGlobal.addEventListener()`
- 条件付き依存: `if (!this.document.hasFocus())` → `resolve()`
- 条件付き依存: `if (!(!this.document.hasFocus()))` → `resolve()`
- 参照: `message.data`, `message.name`

## AboutLoginsChild.#importReportData()
- 位置: L280-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendToContent()`

## AboutLoginsChild.#primaryPasswordResponse()
- 位置: L284-289
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (gPrimaryPasswordPromise)` → `gPrimaryPasswordPromise.resolve()`
- 条件付き依存: `if (gPrimaryPasswordPromise)` → `recordTelemetryEvent()`
- 参照: `data.result`, `data.telemetryEvent`

## AboutLoginsChild.#remaskPassword()
- 位置: L291-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendToContent()`

## AboutLoginsChild.#setup()
- 位置: L295-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.waiveXrays()`, `Services.urlFormatter.formatURLPref()`, `this.sendToContent()`
- 参照: `Cu.waiveXrays(this.browsingContext.window).AboutLoginsUtils`, `data.importVisible`, `data.passwordRevealVisible`, `data.primaryPasswordEnabled`, `this.browsingContext.window`, `utils.importVisible`, `utils.passwordRevealVisible`, `utils.primaryPasswordEnabled`, `utils.supportBaseURL`
- XPCOM: `Services.urlFormatter`

## AboutLoginsChild.#passMessageDataToContent()
- 位置: L306-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `message.name.replace()`, `this.sendToContent()`
- 参照: `message.data`

## AboutLoginsChild.sendToContent()
- 位置: L310-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `Object.assign()`, `win.dispatchEvent()`
- 参照: `this.document.defaultView`, `win.CustomEvent`
