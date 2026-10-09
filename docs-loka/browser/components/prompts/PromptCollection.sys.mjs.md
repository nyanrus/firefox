# browser/components/prompts/PromptCollection.sys.mjs

source: browser/components/prompts/PromptCollection.sys.mjs
source-hash: 78b3024e78d3d29a8b82f39fc26764436a758693
lines: 281

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Object.entries()`, `Services.strings.createBundle()`

## PromptCollection.confirmRepost()
- 位置: L17-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmExBC()`, `console.error()`, `this.stringBundles.app.GetStringFromName()`, `this.stringBundles.brand.GetStringFromName()`
- 条件付き依存: `if (brandName)` → `this.stringBundles.app.formatStringFromName()`
- 条件付き依存: `if (!(brandName))` → `this.stringBundles.app.GetStringFromName()`
- 参照: `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_1`, `Ci.nsIPromptService.BUTTON_TITLE_CANCEL`, `Ci.nsIPromptService.BUTTON_TITLE_IS_STRING`, `Ci.nsIPromptService.MODAL_TYPE_CONTENT`, `Ci.nsIPromptService.MODAL_TYPE_WINDOW`, `browsingContext?.docShell?.docViewer`, `docViewer?.isTabModalPromptAllowed`
- XPCOM: [`nsIPromptService`](../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / `Services.prompt`

## PromptCollection.asyncBeforeUnloadCheck()
- 位置: async L71-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.asyncConfirmEx()`, `console.error()`, `result .QueryInterface()`, `result .QueryInterface(Ci.nsIPropertyBag2) .get()`
- 条件付き依存: `if ( (docViewer && !docViewer.isTabModalPromptAllowed) || !browsingContext.ancestorsAreCurrent )` → `console.error()`
- 条件付き依存: `if (isPDFjs)` → `this.stringBundles.dom.GetStringFromName()`
- 条件付き依存: `if (isProfilePage)` → `this.stringBundles.dom.GetStringFromName()`
- 条件付き依存: `if (isProfilePage)` → `this.stringBundles.dom.formatStringFromName()`
- 条件付き依存: `if (!(isProfilePage))` → `this.stringBundles.dom.GetStringFromName()`
- 条件付き依存: `if (buttonNumClicked === 0)` → `Services.obs.addObserver()`
- 条件付き依存: `if (buttonNumClicked === 0)` → `browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if (buttonNumClicked === 0)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (buttonNumClicked === 0)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (isProfilePage)` → `Glean[gleanFn].alert.record()`
- 参照: `Ci.nsIPrompt.BUTTON_POS_0`, `Ci.nsIPrompt.BUTTON_POS_1`, `Ci.nsIPrompt.BUTTON_POS_2`, `Ci.nsIPrompt.BUTTON_TITLE_CANCEL`, `Ci.nsIPrompt.BUTTON_TITLE_DONT_SAVE`, `Ci.nsIPrompt.BUTTON_TITLE_SAVE`, `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_0_DEFAULT`, `Ci.nsIPromptService.BUTTON_POS_1`, `Ci.nsIPromptService.BUTTON_TITLE_IS_STRING`, `Ci.nsIPropertyBag2`, `Services.prompt.MODAL_TYPE_CONTENT`, `args.headerIconCSSValue`, `args.useTitle`, `browsingContext.ancestorsAreCurrent`, `browsingContext.embedderElement?.contentPrincipal.originNoSuffix`, `browsingContext?.docShell?.docViewer`, `docViewer.isTabModalPromptAllowed`, `lazy.SelectableProfileService.currentProfile.name`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsIPromptService`](../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.obs` / `Services.prefs` / `Services.prompt`

## PromptCollection.observe()
- 位置: L178-183
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTopic === "pdfjs:saveComplete")` → `Services.obs.removeObserver()`
- 条件付き依存: `if (aTopic === "pdfjs:saveComplete")` → `resolve()`
- XPCOM: `Services.obs`

## PromptCollection.confirmFolderUpload()
- 位置: L213-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmExBC()`, `console.error()`, `this.stringBundles.dom.GetStringFromName()`, `this.stringBundles.dom.formatStringFromName()`
- 参照: `Ci.nsIPrompt.BUTTON_DELAY_ENABLE`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_POS_1_DEFAULT`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `Services.prompt.MODAL_TYPE_TAB`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / `Services.prompt`
