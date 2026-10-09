# browser/extensions/webcompat/injections/js/bug1287715-littlealchemy2.com-fix-audio-race-condition.js

source: browser/extensions/webcompat/injections/js/bug1287715-littlealchemy2.com-fix-audio-race-condition.js
source-hash: 7e7f08ab51e5a751f8ad66e9229bae604e569c14
lines: 69

## <module>
- 役割: (未記入)

## value()
- 位置: L32-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addEventListener.call()`, `type?.toLowerCase()`
- 条件付き依存: `if (type?.toLowerCase() === "loadedmetadata")` → `addEventListener.call()`

## value()
- 位置: L49-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchEvent.call()`
- 条件付き依存: `if ( e?.type === "GAME_READY" && loadedmetadataEvent && loadedmetadataListener )` → `(loadedmetadataListener?.handleEvent ?? loadedmetadataListener)()`
- 条件付き依存: `if ( e?.type === "GAME_READY" && loadedmetadataEvent && loadedmetadataListener )` → `console.trace()`
- 参照: `e?.type`, `loadedmetadataListener?.handleEvent`
