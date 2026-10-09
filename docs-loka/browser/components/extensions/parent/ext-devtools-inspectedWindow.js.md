# browser/components/extensions/parent/ext-devtools-inspectedWindow.js

source: browser/components/extensions/parent/ext-devtools-inspectedWindow.js
source-hash: e3c5b0e7dca76a22b7fde27b6894023f8418a287
lines: 52

## <module>
- 役割: (未記入)

## getAPI()
- 位置: L10-50
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `context.extension.baseURI.spec`, `context.extension.id`

## eval()
- 位置: async L22-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `commands.inspectedWindowCommand.eval()`, `context.getDevToolsCommands()`, `getToolboxEvalOptions()`
- 参照: `evalResult.exceptionInfo`, `evalResult.value`

## reload()
- 位置: async L37-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.inspectedWindowCommand.reload()`, `context.getDevToolsCommands()`
