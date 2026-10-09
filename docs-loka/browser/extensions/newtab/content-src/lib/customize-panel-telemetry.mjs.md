# browser/extensions/newtab/content-src/lib/customize-panel-telemetry.mjs

source: browser/extensions/newtab/content-src/lib/customize-panel-telemetry.mjs
source-hash: ae15c7202025275521d8768bffb74b45a45f5fbc
lines: 35

## <module>
- 役割: (未記入)

## getCustomizePanelTransitions()
- 位置: L7-16
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `prevProps.activeSubpanel`, `prevProps.showing`, `props.activeSubpanel`, `props.showing`

## recordCustomizePanelTransitions()
- 位置: L18-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCustomizePanelTransitions()`
- 条件付き依存: `if (panelOpened)` → `dispatch()`
- 条件付き依存: `if (panelOpened)` → `ac.UserEvent()`
- 条件付き依存: `if (subpanelOpened)` → `dispatch()`
- 条件付き依存: `if (subpanelOpened)` → `ac.UserEvent()`
