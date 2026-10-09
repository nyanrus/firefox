# browser/base/content/contentTheme.js

source: browser/base/content/contentTheme.js
source-hash: 73bd581c6cc9496e4798114332029f8d06834511
lines: 214

## <module>
- 役割: (未記入)
- 呼び出し先: `ContentThemeController.init()`, `window.matchMedia()`

## _isTextColorDark()
- 位置: L10-12
- 役割: (未記入)
- 触るとき: (未記入)

## processColor()
- 位置: L19-26
- 役割: (未記入)
- 触るとき: (未記入)

## processColor()
- 位置: L45-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_isTextColorDark()`, `element.toggleAttribute()`
- 条件付き依存: `if (!rgbaChannels)` → `element.toggleAttribute()`
- 参照: `prefersDarkQuery.matches`

## processColor()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)

## processColor()
- 位置: L75-82
- 役割: (未記入)
- 触るとき: (未記入)

## processColor()
- 位置: L89-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_isTextColorDark()`, `element.setAttribute()`
- 条件付き依存: `if (!rgbaChannels)` → `element.removeAttribute()`

## processColor()
- 位置: L109-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.toggleAttribute()`

## processColor()
- 位置: L130-132
- 役割: (未記入)
- 触るとき: (未記入)

## init()
- 位置: L147-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addEventListener()`, `prefersDarkQuery.addEventListener()`

## handleEvent()
- 位置: L162-173
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "LightweightTheme:Set")` → `this._setProperties()`
- 条件付き依存: `if (event.type == "change")` → `root.hasAttribute()`
- 条件付き依存: `if (!root.hasAttribute("lwt-newtab"))` → `root.toggleAttribute()`
- 参照: `document.documentElement`, `event.detail.data`, `event.matches`, `event.type`

## _setProperty()
- 位置: L182-188
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `elem.style.setProperty()`
- 条件付き依存: `if (!(value))` → `elem.style.removeProperty()`

## _setProperties()
- 位置: L195-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setProperty()`
- 条件付き依存: `if (processColor)` → `processColor()`
- 参照: `document.documentElement`
