# browser/fxr/content/fxr-fullScreen.js

source: browser/fxr/content/fxr-fullScreen.js
source-hash: b080eee4c86e5f8466ef31739e770aeb4625902b
lines: 61

## <module>
- 役割: (未記入)

## init()
- 位置: L12-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addEventListener()`
- 条件付き依存: `if (window.fullScreen)` → `this.toggle()`
- 参照: `window.fullScreen`

## toggle()
- 位置: L21-28
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (enterFS)` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (!(enterFS))` → `document.documentElement.removeAttribute()`
- 参照: `window.fullScreen`

## handleEvent()
- 位置: L30-34
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type === "fullscreen")` → `this.toggle()`
- 参照: `event.type`

## enterDomFullscreen()
- 位置: L36-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.setAttribute()`
- 条件付き依存: `if (aBrowser.isRemoteBrowser)` → `aActor.sendAsyncMessage()`
- 参照: `aBrowser.isRemoteBrowser`, `document.fullscreenElement`

## cleanupDomFullscreen()
- 位置: L56-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActor.sendAsyncMessage()`, `document.documentElement.removeAttribute()`
