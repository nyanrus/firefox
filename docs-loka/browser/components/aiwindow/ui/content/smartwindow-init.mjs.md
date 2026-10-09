# browser/components/aiwindow/ui/content/smartwindow-init.mjs

source: browser/components/aiwindow/ui/content/smartwindow-init.mjs
source-hash: 405eabca2fea164fde65174992fdfd4ae2cf3798
lines: 44

## <module>
- 役割: スマートウィンドウの新規タブページの読み込み時に、ASRouter の案内を出す初期化処理を行う
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## init()
- 位置: async L17-25
- 役割: AI ウィンドウでなければ新規タブ URL へ転送し、そうでなければ ASRouter の初期化を待って案内を出す
- 触るとき: AI ウィンドウ無効時の振る舞いや、案内を出すタイミングを変えるとき
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `triggerSwitcherButtonCallout()`
- 参照: `lazy.ASRouter.waitForInitialized`, `topChromeWindow.BROWSER_NEW_TAB_URL`, `window.location.href`

## triggerSwitcherButtonCallout()
- 位置: L30-35
- 役割: smartWindowNewTab のトリガーを選択中のブラウザに対して送る
- 触るとき: 切り替えボタンの案内を出す条件や対象ブラウザを変えるとき
- 呼び出し先: `lazy.ASRouter.sendTriggerMessage()`
- 参照: `topChromeWindow.gBrowser.selectedBrowser`
