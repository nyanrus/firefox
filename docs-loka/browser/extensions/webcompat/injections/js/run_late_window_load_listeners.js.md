# browser/extensions/webcompat/injections/js/run_late_window_load_listeners.js

source: browser/extensions/webcompat/injections/js/run_late_window_load_listeners.js
source-hash: d8628a13a947e14ea40d5def8a6bc6c16eab85d6
lines: 30

## <module>
- 役割: (未記入)

## prototype.addEventListener()
- 位置: L10-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `b?.call()`, `console.error()`, `console.log()`, `type?.toLowerCase()`
- 条件付き依存: `if ( this !== window || document.readyState !== "complete" || type?.toLowerCase() !== "load" )` → `addEventListener.call()`
- 参照: `document.readyState`
