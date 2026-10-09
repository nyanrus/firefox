# browser/components/shell/content/setDesktopBackground.js

source: browser/components/shell/content/setDesktopBackground.js
source-hash: 829a7cad0f91d60c275e18f49dacd5f6231ab762
lines: 271

## <module>
- 役割: (未記入)
- 呼び出し先: `gSetBackground.load()`, `window.addEventListener()`

## _shell()
- 位置: L16-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/browser/shell-service;1"].getService()`
- 参照: `Ci.nsIShellService`
- XPCOM: [`nsIShellService`](../nsIShellService.idl.md) / `@mozilla.org/browser/shell-service;1`

## load()
- 位置: L22-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `document.addEventListener()`, `document.getElementById()`, `gSetBackground.setDesktopBackground()`, `self.init()`, `setTimeout()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document .getElementById("SetDesktopBackgroundDialog") .getButton()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document .getElementById()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document .getElementById("setDesktopBackground") .addEventListener()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.setDesktopBackground()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document .getElementById("showDesktopPreferences") .addEventListener()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this._shell .QueryInterface(Ci.nsIMacShellService) .showDesktopPreferences()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this._shell .QueryInterface()`
- 条件付き依存: `if (!(AppConstants.platform == "linux"))` → `Cc["@mozilla.org/gfx/info;1"].getService()`
- 条件付き依存: `if (!(AppConstants.platform == "linux"))` → `gfxInfo.getMonitors()`
- 条件付き依存: `if (!multiMonitors)` → `document.getElementById()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `document .getElementById("menuPosition") .addEventListener()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `document .getElementById()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `this.updatePosition()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `document .getElementById("desktopColor") .addEventListener()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `this.updateColor()`
- 参照: `AppConstants.platform`, `Ci.nsIGfxInfo`, `Ci.nsIMacShellService`, `document .getElementById("SetDesktopBackgroundDialog") .getButton("accept").hidden`, `document.getElementById("preview-unavailable").style.width`, `document.getElementById("spanPosition").hidden`, `event.currentTarget.value`, `monitors.length`, `screen.height`, `screen.width`, `this._canvas`, `this._canvas.height`, `this._canvas.width`, `this._screenHeight`, `this._screenWidth`, `window.arguments`
- XPCOM: `nsIGfxInfo` / [`nsIMacShellService`](../nsIMacShellService.idl.md) / `@mozilla.org/gfx/info;1`

## init()
- 位置: L89-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctx.scale()`, `this._canvas.getContext()`, `this.updatePosition()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `this._initColor()`
- 条件付き依存: `if (!(AppConstants.platform != "macosx"))` → `document.getElementById()`
- 条件付き依存: `if (!(AppConstants.platform != "macosx"))` → `document.l10n.setAttributes()`
- 参照: `AppConstants.platform`, `document.getElementById("showDesktopPreferences").hidden`, `setDesktopBackground.disabled`, `setDesktopBackground.hidden`, `this._canvas.clientHeight`, `this._canvas.clientWidth`, `this._canvas.height`, `this._canvas.width`, `this._image`, `this._imageName`, `this._screenHeight`, `this._screenWidth`

## setDesktopBackground()
- 位置: L123-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._shell.setDesktopBackground()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `Services.xulStore.persist()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `document.getElementById()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `this._hexStringToLong()`
- 条件付き依存: `if (!(AppConstants.platform != "macosx"))` → `Services.obs.addObserver()`
- 条件付き依存: `if (!(AppConstants.platform != "macosx"))` → `document.getElementById()`
- 条件付き依存: `if (!(AppConstants.platform != "macosx"))` → `document.l10n.setAttributes()`
- 参照: `AppConstants.platform`, `Ci.nsIShellService`, `setDesktopBackground.disabled`, `this._backgroundColor`, `this._image`, `this._imageName`, `this._position`, `this._shell.desktopBackgroundColor`
- XPCOM: [`nsIShellService`](../nsIShellService.idl.md) / `Services.obs` / `Services.xulStore`

## updatePosition()
- 位置: L151-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctx.clearRect()`, `ctx.createPattern()`, `ctx.drawImage()`, `ctx.fillRect()`, `ctx.restore()`, `ctx.save()`, `ctx.stroke()`, `document.getElementById()`, `this._canvas.getContext()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `document.getElementById()`
- 参照: `AppConstants.platform`, `ctx.fillStyle`, `document.getElementById("menuPosition").value`, `document.getElementById("preview-unavailable").hidden`, `this._image`, `this._image.naturalHeight`, `this._image.naturalWidth`, `this._position`, `this._screenHeight`, `this._screenWidth`

## gSetBackground._initColor()
- 位置: L221-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._rgbToHex()`, `this.updateColor()`
- 参照: `colorpicker.value`, `this._backgroundColor`, `this._shell.desktopBackgroundColor`

## gSetBackground.updateColor()
- 位置: L236-239
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._backgroundColor`, `this._canvas.style.backgroundColor`

## gSetBackground._hexStringToLong()
- 位置: L242-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aString.substring()`, `parseInt()`

## gSetBackground._rgbToHex()
- 位置: L250-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[aR, aG, aB] .map()`, `[aR, aG, aB] .map(aInt => aInt.toString(16).replace(/^(.)$/, "0$1")) .join()`, `[aR, aG, aB] .map(aInt => aInt.toString(16).replace(/^(.)$/, "0$1")) .join("") .toUpperCase()`, `aInt.toString()`, `aInt.toString(16).replace()`

## gSetBackground.observe()
- 位置: L260-267
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTopic == "shell:desktop-background-changed")` → `document.getElementById()`
- 条件付き依存: `if (aTopic == "shell:desktop-background-changed")` → `Services.obs.removeObserver()`
- 参照: `document.getElementById("setDesktopBackground").hidden`, `document.getElementById("showDesktopPreferences").hidden`
- XPCOM: `Services.obs`
