# browser/extensions/newtab/content-src/lib/theme-picker-shown.mjs

source: browser/extensions/newtab/content-src/lib/theme-picker-shown.mjs
source-hash: f70ea565f30bbd2f396c2087ca25361fb175a3b0
lines: 90

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## isRootPanelVisible()
- 位置: L16-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `props.activeSubpanel`, `props.showing`

## isThemesPanelVisible()
- 位置: L20-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `CUSTOMIZE_SUBPANELS.THEMES`, `props.activeSubpanel`, `props.showing`

## findPicker()
- 位置: L34-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialog.querySelectorAll()`, `el.getAttribute()`
- 参照: `el.layout`

## notifyThemePickerShown()
- 位置: async L49-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `customElements.whenDefined()`, `el.shown()`, `isStillVisible()`, `latestRequest.get()`, `latestRequest.set()`
- 参照: `el.isConnected`, `el.shown`

## notifyThemePickersOnTransition()
- 位置: L73-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCurrentProps()`, `isVisible()`
- 条件付き依存: `if (!isVisible(prevProps) && isVisible(props))` → `notifyThemePickerShown()`
- 条件付き依存: `if (!isVisible(prevProps) && isVisible(props))` → `findPicker()`
- 条件付き依存: `if (!isVisible(prevProps) && isVisible(props))` → `isVisible()`
- 条件付き依存: `if (!isVisible(prevProps) && isVisible(props))` → `getCurrentProps()`
