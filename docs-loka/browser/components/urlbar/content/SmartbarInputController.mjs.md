# browser/components/urlbar/content/SmartbarInputController.mjs

source: browser/components/urlbar/content/SmartbarInputController.mjs
source-hash: 64b52574dca6b2671508c745ccf64992148d2eb1
lines: 209

## <module>
- 役割: (未記入)

## SmartbarInputController.constructor()
- 位置: L24-29
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `adapter.editor`, `adapter.input`, `this.editor`, `this.input`

## SmartbarInputController.focus()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.focus()`

## SmartbarInputController.blur()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.blur()`

## SmartbarInputController.readOnly()
- 位置: L50-52
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.readOnly`

## SmartbarInputController.readOnly()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.readOnly`

## SmartbarInputController.placeholder()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.placeholder`

## SmartbarInputController.placeholder()
- 位置: L67-69
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.placeholder`

## SmartbarInputController.value()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.value`

## SmartbarInputController.setValue()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.value`

## SmartbarInputController.selectionStart()
- 位置: L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.selectionStart`

## SmartbarInputController.selectionStart()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setSelectionRange()`
- 参照: `this.selectionEnd`

## SmartbarInputController.selectionEnd()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.input.selectionEnd`

## SmartbarInputController.selectionEnd()
- 位置: L111-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setSelectionRange()`
- 参照: `this.selectionStart`

## SmartbarInputController.setSelectionRange()
- 位置: L123-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.input.setSelectionRange()`
- 参照: `this.input.setSelectionRange`

## SmartbarInputController.setRangeText()
- 位置: L140-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.setRangeText()`

## SmartbarInputController.select()
- 位置: L147-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.select()`

## SmartbarInputController.dispatchInput()
- 位置: L161-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.dispatchEvent()`

## SmartbarInputController.dispatchSelectionChange()
- 位置: L175-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.dispatchEvent()`

## SmartbarInputController.composing()
- 位置: L186-188
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.editor.composing`

## SmartbarInputController.selectionRangeCount()
- 位置: L195-197
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.editor.selection?.rangeCount`

## SmartbarInputController.selectionToStringWithFormat()
- 位置: L205-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.editor.selection?.toStringWithFormat()`
