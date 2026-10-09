# browser/modules/PrivateBrowsingUI.sys.mjs

source: browser/modules/PrivateBrowsingUI.sys.mjs
source-hash: bdbaf089c59bcbdabb02e776d6a1658110a4efeb
lines: 68

## <module>
- 役割: (未記入)

## PBUI_init()
- 位置: L12-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `docElement.setAttribute()`, `document.getElementById()`, `document.getElementById("Tools:Sanitize").setAttribute()`, `gBrowser.updateTitlebar()`
- 条件付き依存: `if (PrivateBrowsingUtils.permanentPrivateBrowsing)` → `hideNewWindowItem()`
- 条件付き依存: `if (PrivateBrowsingUtils.permanentPrivateBrowsing)` → `document.getElementById()`
- 条件付き依存: `if (PrivateBrowsingUtils.permanentPrivateBrowsing)` → `PanelMultiView.getViewNode()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `PrivateBrowsingUtils.permanentPrivateBrowsing`, `document.documentElement`, `window.document`, `window.gBrowser`, `window.location.href`

## hideNewWindowItem()
- 位置: L37-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `privateWindowItem.getAttribute()`, `windowItem.setAttribute()`
- 参照: `privateWindowItem.hidden`
