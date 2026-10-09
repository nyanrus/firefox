# browser/base/content/global-scripts.js

source: browser/base/content/global-scripts.js
source-hash: bbeb801d5c7559b88dde56ad67d0950925a914e2
lines: 27

## <module>
- 役割: browser.xhtml 以外の最上位ウィンドウ用に、browser.js や周辺オーバーレイ群を loadSubScript で読み込む。macOS では macWindowMenu.js も追加で読む。
- 呼び出し先: `Services.scriptloader.loadSubScript()`
