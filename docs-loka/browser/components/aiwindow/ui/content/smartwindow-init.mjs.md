# browser/components/aiwindow/ui/content/smartwindow-init.mjs

source: browser/components/aiwindow/ui/content/smartwindow-init.mjs
source-hash: 405eabca2fea164fde65174992fdfd4ae2cf3798
lines: 44

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## init()
- 位置: async L17-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `triggerSwitcherButtonCallout()`
- 参照: `lazy.ASRouter.waitForInitialized`, `topChromeWindow.BROWSER_NEW_TAB_URL`, `window.location.href`

## triggerSwitcherButtonCallout()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.sendTriggerMessage()`
- 参照: `topChromeWindow.gBrowser.selectedBrowser`
