# browser/fxr/content/common.js

source: browser/fxr/content/common.js
source-hash: abdb0fef332047c133b7dc6e0ffff0002a5bde83
lines: 48

## <module>
- 役割: (未記入)

## showModalContainer()
- 位置: L7-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.appendChild()`, `content.classList.contains()`, `document.getElementById()`
- 条件付き依存: `if (container == null)` → `document.createElement()`
- 条件付き依存: `if (container == null)` → `container.classList.add()`
- 条件付き依存: `if (container == null)` → `mask.classList.add()`
- 条件付き依存: `if (container == null)` → `document.body.appendChild()`
- 条件付き依存: `if (!(container == null))` → `document.getElementById()`
- 条件付き依存: `if (content.classList.contains("modal_hide"))` → `content.classList.replace()`
- 条件付き依存: `if (!(content.classList.contains("modal_hide")))` → `content.classList.add()`
- 参照: `container.hidden`, `container.id`, `document.getElementById("eModalMask").hidden`, `mask.id`

## clearModalContainer()
- 位置: L37-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.removeChild()`, `content.classList.replace()`, `document.getElementById()`
- 参照: `container.firstElementChild`, `container.hidden`, `document.getElementById("eModalMask").hidden`
