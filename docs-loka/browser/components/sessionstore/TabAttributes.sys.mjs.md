# browser/components/sessionstore/TabAttributes.sys.mjs

source: browser/components/sessionstore/TabAttributes.sys.mjs
source-hash: ea53156d129cba5309702446a3994747af81c069
lines: 44

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## get()
- 位置: L12-14
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabAttributesInternal.get()`

## set()
- 位置: L16-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabAttributesInternal.set()`

## get()
- 位置: L22-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute(name))` → `tab.getAttribute()`

## set()
- 位置: L34-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.removeAttribute()`
- 条件付き依存: `if (name in data)` → `tab.setAttribute()`
