# browser/components/extensions/child/ext-omnibox.js

source: browser/components/extensions/child/ext-omnibox.js
source-hash: c144a1860ba10b035ebb0bbefc50b886516364f6
lines: 39

## <module>
- 役割: (未記入)

## getAPI()
- 位置: L8-37
- 役割: (未記入)
- 触るとき: (未記入)

## register()
- 位置: L16-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager .getParentEvent()`, `context.childManager .getParentEvent("omnibox.onInputChanged") .addListener()`, `context.childManager .getParentEvent("omnibox.onInputChanged") .removeListener()`

## listener()
- 位置: L17-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.callParentFunctionNoReturn()`, `fire.asyncWithoutClone()`
