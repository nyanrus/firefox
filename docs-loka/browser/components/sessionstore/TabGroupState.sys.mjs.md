# browser/components/sessionstore/TabGroupState.sys.mjs

source: browser/components/sessionstore/TabGroupState.sys.mjs
source-hash: cc64fa43f5e142e7a4d91422d980872b808fde2d
lines: 192

## <module>
- 役割: (未記入)

## _TabGroupState.collect()
- 位置: L94-102
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabGroup.collapsed`, `tabGroup.color`, `tabGroup.id`, `tabGroup.label`, `tabGroup.saveOnWindowClose`

## _TabGroupState.closed()
- 位置: L116-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.collect()`

## _TabGroupState.savedInOpenWindow()
- 位置: L139-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closed()`

## _TabGroupState.savedInClosedWindow()
- 位置: L160-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`

## _TabGroupState.abbreviated()
- 位置: L180-188
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabGroupState.collapsed`, `tabGroupState.color`, `tabGroupState.id`, `tabGroupState.name`
