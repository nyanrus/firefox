# browser/extensions/webcompat/injections/js/disable_resizeMode_in_GDM.js

source: browser/extensions/webcompat/injections/js/disable_resizeMode_in_GDM.js
source-hash: e0d21d791914d3d34ac59d4c49c2081ab849cdca
lines: 45

## <module>
- 役割: (未記入)

## maybeDeleteResizeMode()
- 位置: L8-13
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `video.resizeMode`

## getDisplayMedia()
- 位置: L18-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gDM.call()`
- 条件付き依存: `if (video)` → `maybeDeleteResizeMode()`

## applyConstraints()
- 位置: L30-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aC.call()`, `this.getConstraints()`
- 条件付き依存: `if (!this.getConstraints().resizeMode)` → `maybeDeleteResizeMode()`
- 参照: `this.getConstraints().resizeMode`
