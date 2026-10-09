# browser/components/syncedtabs/sidebar.js

source: browser/components/syncedtabs/sidebar.js
source-hash: ce2642995f838cf27425cbe31d0d4116ddc0c47b
lines: 42

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `addEventListener()`

## onLoaded()
- 位置: L19-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("template-container") .appendChild()`, `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `syncedTabsDeckComponent.init()`, `window.top.MozXULElement.insertFTLIfNeeded()`, `window.top.document .getElementById()`, `window.top.document .getElementById("SyncedTabsSidebarContext") .querySelectorAll()`, `window.top.document .getElementById("SyncedTabsSidebarContext") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`
- 参照: `syncedTabsDeckComponent.container`

## onUnloaded()
- 位置: L34-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `removeEventListener()`, `syncedTabsDeckComponent.uninit()`
