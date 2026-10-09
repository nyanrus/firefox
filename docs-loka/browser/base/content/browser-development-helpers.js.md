# browser/base/content/browser-development-helpers.js

source: browser/base/content/browser-development-helpers.js
source-hash: 5155b280b8ff1dec8c53b12861ed4401f5499659
lines: 46

## <module>
- 役割: (未記入)

## init()
- 位置: L11-14
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addRestartShortcut()`, `this.quickRestart.bind()`
- 参照: `this.quickRestart`

## quickRestart()
- 位置: L16-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.set()`, `Services.obs.notifyObservers()`, `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.env` / `Services.obs` / `Services.startup`

## addRestartShortcut()
- 位置: L25-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `command.addEventListener()`, `command.setAttribute()`, `document.createXULElement()`, `document.getElementById()`, `document.getElementById("mainCommandSet").prepend()`, `document.getElementById("mainKeyset").prepend()`, `document.getElementById("menu_FilePopup").appendChild()`, `key.setAttribute()`, `menuitem.addEventListener()`, `menuitem.setAttribute()`
- 参照: `this.quickRestart`
