# browser/components/tabbrowser/content/status-panel.js

source: browser/components/tabbrowser/content/status-panel.js
source-hash: 1200576f64defa343cbd9cf8b365797023d40908
lines: 155

## <module>
- 役割: (未記入)

## panel()
- 位置: L10-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._onTransitionEnd.bind()`, `this.panel.addEventListener()`

## isVisible()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel.hasAttribute()`

## update()
- 位置: L28-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `text.match()`, `types.push()`
- 条件付き依存: `if (XULBrowserWindow.busyUI)` → `types.push()`
- 条件付き依存: `if (text.length > 500 && text.match(/^data:[^,]+;base64,/))` → `text.substring()`
- 条件付き依存: `if (this._labelElement.value != text || (text && !this.isVisible))` → `this.panel.setAttribute()`
- 条件付き依存: `if (this._labelElement.value != text || (text && !this.isVisible))` → `this.panel.getAttribute()`
- 条件付き依存: `if (this._labelElement.value != text || (text && !this.isVisible))` → `this._labelElement.setAttribute()`

## _labelElement()
- 位置: L69-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## _label()
- 位置: L74-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel.getAttribute()`
- 条件付き依存: `if (!this.isVisible)` → `this.panel.removeAttribute()`
- 条件付き依存: `if ( this.panel.getAttribute("type") == "status" && this.panel.getAttribute("previoustype") == "status" )` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this.panel.hidden)` → `getComputedStyle()`
- 条件付き依存: `if (val)` → `this.panel.removeAttribute()`
- 条件付き依存: `if (val)` → `MousePosTracker.addListener()`
- 条件付き依存: `if (!(val))` → `this.panel.setAttribute()`
- 条件付き依存: `if (!(val))` → `MousePosTracker.removeListener()`

## _onTransitionEnd()
- 位置: L111-115
- 役割: (未記入)
- 触るとき: (未記入)

## getMouseTargetRect()
- 位置: L117-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`

## onMouseEnter()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._mirror()`

## onMouseLeave()
- 位置: L136-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._mirror()`

## _mirror()
- 位置: L140-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel.hasAttribute()`
- 条件付き依存: `if (this.panel.hasAttribute("mirror"))` → `this.panel.removeAttribute()`
- 条件付き依存: `if (!(this.panel.hasAttribute("mirror")))` → `this.panel.setAttribute()`
- 条件付き依存: `if (!this.panel.hasAttribute("sizelimit"))` → `this.panel.setAttribute()`
