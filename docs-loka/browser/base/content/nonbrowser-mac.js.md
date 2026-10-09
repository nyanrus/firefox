# browser/base/content/nonbrowser-mac.js

source: browser/base/content/nonbrowser-mac.js
source-hash: 57cabf79c16656b32e2e974f9350139523395560
lines: 177

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`, `addEventListener()`

## openBrowserWindowFromDockMenu()
- 位置: L9-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `OpenBrowserWindow()`, `this.dockSupport.activateApplication()`, `win.addEventListener()`
- 参照: `options.openerWindow`

## startup()
- 位置: L22-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `setTimeout()`, `this.delayedStartup()`
- 条件付き依存: `if (element)` → `element.setAttribute()`
- 条件付き依存: `if (element)` → `element.removeAttribute()`
- 条件付き依存: `if (window.location.href == this.MAC_HIDDEN_WINDOW)` → `document.getElementById()`
- 条件付き依存: `if (dockMenuElement != null)` → `Cc[ "@mozilla.org/widget/standalonenativemenu;1" ].createInstance()`
- 条件付き依存: `if (dockMenuElement != null)` → `nativeMenu.init()`
- 条件付き依存: `if (window.location.href == this.MAC_HIDDEN_WINDOW)` → `dockMenuElement.addEventListener()`
- 条件付き依存: `if (PrivateBrowsingUtils.permanentPrivateBrowsing)` → `document.getElementById()`
- 条件付き依存: `if (!PrivateBrowsingUtils.enabled)` → `document.getElementById()`
- 条件付き依存: `if (!PrivateBrowsingUtils.enabled)` → `document.getElementById("key_privatebrowsing").remove()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById("key_quitApplication").remove()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById("menu_FileQuitItem").removeAttribute()`
- 参照: `BrowserUIUtils.quitShortcutDisabled`, `Ci.nsIStandaloneNativeMenu`, `PrivateBrowsingUtils.enabled`, `PrivateBrowsingUtils.permanentPrivateBrowsing`, `document.getElementById("Tools:PrivateBrowsing").hidden`, `document.getElementById("macDockMenuNewPrivateWindow").hidden`, `document.getElementById("macDockMenuNewWindow").hidden`, `document.getElementById("menu_newPrivateWindow").hidden`, `element.hidden`, `this.MAC_HIDDEN_WINDOW`, `this.delayedStartupTimeoutId`, `this.dockSupport.dockMenu`, `window.location.href`
- XPCOM: `nsIStandaloneNativeMenu` / `@mozilla.org/widget/standalonenativemenu;1`

## delayedStartup()
- 位置: L120-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserOffline.init()`, `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `PrivateBrowsingUI.init()`
- 参照: `this.delayedStartupTimeoutId`

## shutdown()
- 位置: L132-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserOffline.uninit()`
- 条件付き依存: `if (this.delayedStartupTimeoutId)` → `clearTimeout()`
- 参照: `this.MAC_HIDDEN_WINDOW`, `this.delayedStartupTimeoutId`, `this.dockSupport.dockMenu`, `window.location.href`

## handleEvent()
- 位置: L149-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.id.startsWith()`, `this.shutdown()`, `this.startup()`
- 条件付き依存: `if (event.target.id.startsWith("macDockMenuNew"))` → `this.openBrowserWindowFromDockMenu()`
- 参照: `event.target.id`, `event.type`
