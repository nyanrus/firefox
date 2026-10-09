# browser/extensions/webcompat/injections/js/hide_messages.js

source: browser/extensions/webcompat/injections/js/hide_messages.js
source-hash: cc205c56553372610db8c7c89c1cf88bae78e9b6
lines: 61

## <module>
- 役割: (未記入)
- 呼び出し先: `browser.runtime.connect()`, `check()`, `observer.observe()`, `port.onMessage.addListener()`, `resolve()`, `window.metadata.then()`

## check()
- 位置: L17-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidate.innerText.includes()`, `document.querySelectorAll()`
- 条件付き依存: `if (click_adjacent)` → `candidate.parentElement.querySelector(click_adjacent)?.click()`
- 条件付き依存: `if (click_adjacent)` → `candidate.parentElement.querySelector()`
- 条件付き依存: `if (!(click_adjacent))` → `candidate.remove()`
- 参照: `window.top`

## disconnect()
- 位置: L39-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `observer.disconnect()`, `setTimeout()`
