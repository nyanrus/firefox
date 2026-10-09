# browser/actors/AboutPrivateBrowsingParent.sys.mjs

source: browser/actors/AboutPrivateBrowsingParent.sys.mjs
source-hash: 0ad1a4eb3854b401eed69fb547dec53743f2cddb
lines: 187

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## AboutPrivateBrowsingParent.setShownThisSession()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)

## AboutPrivateBrowsingParent.receiveMessage()
- 位置: L41-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouter.handleMessageRequest()`, `ASRouter.isUnblockedMessage()`, `BrowserUtils.shouldShowPromo()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`, `browser.getAttribute()`, `lazy.SearchService.getDefaultPrivate()`, `lazy.SearchService.getDefaultPrivate().then()`, `lazy.SpecialMessageActions.handleAction()`, `resolve()`, `urlBar.inputField.addEventListener()`, `win.OpenBrowserWindow()`, `win.openPreferences()`
- 条件付き依存: `if (!aMessage.data || !aMessage.data.text)` → `urlBar.setHiddenFocus()`
- 条件付き依存: `if (!(!aMessage.data || !aMessage.data.text))` → `urlBar.handoff()`
- 条件付き依存: `if (message)` → `Glean.aboutprivatebrowsing.basicsModalShown.record()`
- 条件付き依存: `if (message)` → `lazy.Spotlight.showSpotlightDialog()`
- 参照: `ASRouter.waitForInitialized`, `BrowserUtils.PromoType`, `aMessage.data`, `aMessage.data.id`, `aMessage.data.text`, `aMessage.data.type`, `aMessage.name`, `browser.documentGlobal`, `engine.name`, `lazy.MAX_SEARCH_BANNER_SHOW_COUNT`, `lazy.SearchService.defaultPrivateEngine`, `lazy.isPrivateSearchUIEnabled`, `this.browsingContext.top.embedderElement`, `win.gURLBar`
- XPCOM: `Services.prefs`

## checkFirstChange()
- 位置: L71-83
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isFirstChange)` → `urlBar.removeHiddenFocus()`
- 条件付き依存: `if (isFirstChange)` → `urlBar.handoff()`
- 条件付き依存: `if (isFirstChange)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (isFirstChange)` → `urlBar.removeEventListener()`

## onKeydown()
- 位置: L85-94
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (ev.key.length === 1 && !ev.altKey && !ev.ctrlKey && !ev.metaKey)` → `checkFirstChange()`
- 条件付き依存: `if (ev.key === "Escape")` → `onDone()`
- 参照: `ev.altKey`, `ev.ctrlKey`, `ev.key`, `ev.key.length`, `ev.metaKey`

## onDone()
- 位置: L96-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`, `urlBar.inputField.removeEventListener()`, `urlBar.removeHiddenFocus()`
- 参照: `ev?.type`
