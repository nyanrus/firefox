# browser/base/content/browser-customtitlebar.js

source: browser/base/content/browser-customtitlebar.js
source-hash: 5e76f26fb6714d63118c145c18d80810fae06c53
lines: 80

## <module>
- 役割: (未記入)

## init()
- 位置: L6-12
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `this._readPref()`, `this._update()`
- 参照: `this._initialized`, `this._prefName`
- XPCOM: `Services.prefs`

## allowedBy()
- 位置: L14-24
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (condition in this._disallowed)` → `this._update()`
- 条件付き依存: `if (!(condition in this._disallowed))` → `this._update()`
- 参照: `this._disallowed`

## systemSupported()
- 位置: L26-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.matchMedia()`
- 参照: `AppConstants.MOZ_WIDGET_TOOLKIT`, `this.systemSupported`, `window.matchMedia("(-moz-gtk-csd-available)").matches`

## enabled()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`

## observe()
- 位置: L45-49
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "nsPref:changed")` → `this._readPref()`

## _readPref()
- 位置: L55-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.allowedBy()`
- 参照: `Services.appinfo.drawInTitlebar`
- XPCOM: `Services.appinfo`

## _update()
- 位置: L60-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `TabBarVisibility.update()`, `ToolbarIconColor.inferFromText()`, `document.documentElement.toggleAttribute()`
- 参照: `Object.keys(this._disallowed).length`, `this._disallowed`, `this._initialized`, `this.systemSupported`, `window.fullScreen`

## uninit()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- 参照: `this._prefName`
- XPCOM: `Services.prefs`
