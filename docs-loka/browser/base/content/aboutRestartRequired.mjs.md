# browser/base/content/aboutRestartRequired.mjs

source: browser/base/content/aboutRestartRequired.mjs
source-hash: 5a9c5487e2488d9e468c62f2d5f2168f5cc31861
lines: 53

## <module>
- 役割: (未記入)
- 呼び出し先: `AboutRestartRequired.init()`, `document.dispatchEvent()`

## addAutofocus()
- 位置: async L13-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.setAttribute()`
- 参照: `button.updateComplete`, `window.top`

## restart()
- 位置: L20-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.startup`

## toggleDetails()
- 位置: L25-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toggle.setAttribute()`
- 参照: `details.hidden`

## init()
- 位置: L36-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `restartButton.addEventListener()`, `this.addAutofocus()`, `this.restart()`, `this.toggleDetails()`, `toggle.addEventListener()`
