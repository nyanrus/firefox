# browser/modules/PrivateBrowsingUI.sys.mjs

source: browser/modules/PrivateBrowsingUI.sys.mjs
source-hash: bdbaf089c59bcbdabb02e776d6a1658110a4efeb
lines: 68

## <module>
- 役割: プライベートブラウズ時のウィンドウ UI(タイトルバーとメニュー項目)を初期化する

## PBUI_init()
- 位置: L12-66
- 役割: プライベートウィンドウなら履歴消去メニューを無効化し、ブラウザ本体ではタイトルバー属性と新規ウィンドウ項目を調整する
- 触るとき: プライベートウィンドウのタイトルやメニューが崩れる、または永続プライベートブラウズ時の表示を変えたいとき。通常ウィンドウでは早期 return する
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `docElement.setAttribute()`, `document.getElementById()`, `document.getElementById("Tools:Sanitize").setAttribute()`, `gBrowser.updateTitlebar()`
- 条件付き依存: `if (PrivateBrowsingUtils.permanentPrivateBrowsing)` → `hideNewWindowItem()`
- 条件付き依存: `if (PrivateBrowsingUtils.permanentPrivateBrowsing)` → `document.getElementById()`
- 条件付き依存: `if (PrivateBrowsingUtils.permanentPrivateBrowsing)` → `PanelMultiView.getViewNode()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `PrivateBrowsingUtils.permanentPrivateBrowsing`, `document.documentElement`, `window.document`, `window.gBrowser`, `window.location.href`

## hideNewWindowItem()
- 位置: L37-50
- 役割: 永続プライベートブラウズ時に「新しいプライベートウィンドウ」項目を隠し、「新しいウィンドウ」項目の l10n ID を差し替える
- 触るとき: ファイルメニューとアプリメニューの新規ウィンドウ項目を変えるとき。Ctrl+N のキー表示を残すため、隠すのは「プライベートウィンドウ」項目の側である点を確認する
- 呼び出し先: `privateWindowItem.getAttribute()`, `windowItem.setAttribute()`
- 参照: `privateWindowItem.hidden`
