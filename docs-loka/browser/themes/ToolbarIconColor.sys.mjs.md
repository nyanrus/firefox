# browser/themes/ToolbarIconColor.sys.mjs

source: browser/themes/ToolbarIconColor.sys.mjs
source-hash: 049e9852e1228d2978dc48293335ec892152f4d3
lines: 133

## <module>
- 役割: (未記入)

## init()
- 位置: L15-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_windowStateMap.has()`, `_windowStateMap.set()`, `window.addEventListener()`
- 条件付き依存: `if (Services.focus.activeWindow == window)` → `this.inferFromText()`
- 参照: `Services.focus.activeWindow`
- XPCOM: `Services.focus`

## uninit()
- 位置: L43-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_windowStateMap.delete()`, `_windowStateMap.get()`, `window.removeEventListener()`

## handleEvent()
- 位置: L58-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.inferFromText()`
- 参照: `event.target`, `event.type`, `event.visible`

## inferFromText()
- 位置: L73-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `_windowStateMap.get()`, `cachedLuminances.get()`, `isNaN()`, `luminances.set()`, `state.toolbarLuminanceCache.clear()`, `toolbar.toggleAttribute()`, `window.document.querySelectorAll()`
- 条件付き依存: `if (isNaN(luminance))` → `InspectorUtils.colorToRGBA()`
- 条件付き依存: `if (isNaN(luminance))` → `window.getComputedStyle()`
- 条件付き依存: `if (cacheKey)` → `cachedLuminances.set()`
- 参照: `Services.appinfo.nativeMenubar`, `state.active`, `state.customtitlebar`, `state.fullscreen`, `state.toolbarLuminanceCache`, `toolbar.id`, `window.getComputedStyle(toolbar).color`
- XPCOM: `Services.appinfo`
