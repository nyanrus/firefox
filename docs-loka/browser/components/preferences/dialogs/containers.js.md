# browser/components/preferences/dialogs/containers.js

source: browser/components/preferences/dialogs/containers.js
source-hash: 52d38c8bddb53ff113013357f714d43381184502
lines: 44

## <module>
- 役割: (未記入)
- 呼び出し先: `AdjustableTitle.hide()`, `ChromeUtils.importESModule()`, `dialog.getButton()`, `document.addEventListener()`, `document.getElementById()`, `document.querySelector()`, `editor.commit()`, `editor.form.addEventListener()`, `editor.render()`, `setTitle()`, `updateValidity()`, `window.addEventListener()`

## setTitle()
- 位置: L12-22
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (params.userContextId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(params.userContextId))` → `document.l10n.setAttributes()`
- 参照: `document.documentElement`, `params.identity.name`, `params.userContextId`, `window.arguments`

## updateValidity()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `acceptButton.disabled`, `editor.isValid`
