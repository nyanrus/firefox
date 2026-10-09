# browser/base/content/browser-main.js

source: browser/base/content/browser-main.js
source-hash: 89ebf874267639dd85d9ddf9a828760afacb4869
lines: 61

## <module>
- 役割: ブラウザ起動時に各種サブスクリプトと ESModule を読み込み、window のイベントを gBrowserInit に接続する入口
- 呼び出し先: `AIWindow.isOpeningAIWindow()`, `ChromeUtils.importESModule()`, `Services.scriptloader.loadSubScript()`, `gBrowserInit.onBeforeInitialXULLayout.bind()`, `gBrowserInit.onDOMContentLoaded.bind()`, `gBrowserInit.onLoad.bind()`, `gBrowserInit.onUnload.bind()`, `window.addEventListener()`
