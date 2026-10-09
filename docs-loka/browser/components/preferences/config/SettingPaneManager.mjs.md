# browser/components/preferences/config/SettingPaneManager.mjs

source: browser/components/preferences/config/SettingPaneManager.mjs
source-hash: 0cc43a0e2afe0ddc8aed68dbe7de8800c03e03b2
lines: 102

## <module>
- 役割: (未記入)

## friendlyPrefCategoryNameToInternalName()
- 位置: L13-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `categoryName.startsWith()`, `categoryName.substr()`, `categoryName.substring()`, `categoryName.substring(0, 1).toUpperCase()`

## get()
- 位置: L29-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.get()`, `this._data.has()`

## getWithParents()
- 位置: L39-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `configs.unshift()`, `this.get()`
- 参照: `configs[0].parent`

## importPane()
- 位置: L50-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWithParents()`
- 条件付き依存: `if (config.module)` → `ChromeUtils.importESModule()`
- 参照: `config.module`, `window.closed`

## registerPane()
- 位置: L67-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.getElementById()`, `document.getElementById("mainPrefPane").append()`, `friendlyPrefCategoryNameToInternalName()`, `this._data.has()`, `this._data.set()`, `window.register_module()`
- 参照: `config.parent`, `fullConfig.groupIds.length`, `settingPane.config`, `settingPane.isSubPane`, `settingPane.name`

## init()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `settingPane.init()`

## registerPanes()
- 位置: L96-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.registerPane()`
