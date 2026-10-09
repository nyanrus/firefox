# browser/actors/AboutTabCrashedParent.sys.mjs

source: browser/actors/AboutTabCrashedParent.sys.mjs
source-hash: 79d589c04b216a90526e5f913fa80559c115f09d
lines: 89

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutTabCrashedParent.didDestroy()
- 位置: L17-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeCrashedPage()`

## AboutTabCrashedParent.receiveMessage()
- 位置: async L21-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `gAboutTabCrashedPages.set()`, `gBrowser.getTabForBrowser()`, `gBrowser.removeTab()`, `lazy.SessionStore.reviveAllCrashedTabs()`, `lazy.SessionStore.reviveCrashedTab()`, `lazy.TabCrashHandler.maybeSendCrashReport()`, `lazy.TabCrashHandler.onAboutTabCrashedLoad()`, `this.sendAsyncMessage()`, `this.updateTabCrashedCount()`
- 条件付き依存: `if (!browser)` → `this.removeCrashedPage()`
- 参照: `message.name`, `this.browsingContext.top.embedderElement`

## AboutTabCrashedParent.removeCrashedPage()
- 位置: L63-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAboutTabCrashedPages.delete()`, `gAboutTabCrashedPages.get()`, `lazy.TabCrashHandler.onAboutTabCrashedUnload()`, `this.updateTabCrashedCount()`
- 参照: `this.browsingContext.top.embedderElement`

## AboutTabCrashedParent.updateTabCrashedCount()
- 位置: L74-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAboutTabCrashedPages.keys()`
- 条件付き依存: `if (browser)` → `browser.sendMessageToActor()`
- 参照: `actor.browsingContext.top.embedderElement`, `gAboutTabCrashedPages.size`
