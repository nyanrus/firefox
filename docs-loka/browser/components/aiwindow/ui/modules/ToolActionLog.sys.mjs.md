# browser/components/aiwindow/ui/modules/ToolActionLog.sys.mjs

source: browser/components/aiwindow/ui/modules/ToolActionLog.sys.mjs
source-hash: 99eed3da8cfccf92c8483edda2c9d04eedcd3b98
lines: 220

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `urlListChips()`

## urlListChips()
- 位置: L51-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(items ?? []).map()`, `getLabel()`
- 参照: `item.url`

## resolveSupportUrl()
- 位置: L134-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## getActionLogConfigForTool()
- 位置: L149-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TOOL_ACTION_LOG_CONFIG.get()`, `cfg.label()`, `resolveSupportUrl()`
- 参照: `body?.pending`, `cfg.label`, `cfg.link`, `cfg.link.l10nName`, `cfg.link.supportPage`, `cfg.pendingLabel`

## getActionLogChipsForTool()
- 位置: L187-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TOOL_RESULT_TO_CHIPS.get()`, `adapter()`

## buildActionLogRow()
- 位置: L204-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getActionLogChipsForTool()`
- 参照: `label.l10nArgs`, `label.l10nId`, `link?.href`, `row.label`, `row.labelL10nArgs`, `row.labelL10nId`, `row.link`
