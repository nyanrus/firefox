# browser/extensions/webcompat/templates/hide_messages.js

source: browser/extensions/webcompat/templates/hide_messages.js
source-hash: c25b5ee50029eb3be5917bcc401c046362e83030
lines: 54

## <module>
- 役割: (未記入)
- 呼び出し先: `check()`, `observer.observe()`

## check()
- 位置: L10-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidate.innerText.includes()`, `document.querySelectorAll()`
- 条件付き依存: `if (click_adjacent)` → `candidate.parentElement.querySelector(click_adjacent)?.click()`
- 条件付き依存: `if (click_adjacent)` → `candidate.parentElement.querySelector()`
- 条件付き依存: `if (!(click_adjacent))` → `candidate.remove()`
- 参照: `window.top`

## disconnect()
- 位置: L32-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `observer.disconnect()`, `setTimeout()`
