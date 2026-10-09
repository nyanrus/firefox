# browser/components/sessionstore/PageWireframes.sys.mjs

source: browser/components/sessionstore/PageWireframes.sys.mjs
source-hash: ed59f8637d970ee4232030ca844b7f3b476b2ded
lines: 126

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## getWireframeState()
- 位置: L21-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.getSessionHistory()`
- 参照: `sessionHistory.index`, `sessionHistory?.entries`, `sessionHistory?.entries[sessionHistory.index]?.wireframe`

## getWireframeElementForTab()
- 位置: L36-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWireframeElement()`, `this.getWireframeState()`
- 参照: `tab.ownerDocument`

## nscolorToRGB()
- 位置: L50-55
- 役割: (未記入)
- 触るとき: (未記入)

## getWireframeElement()
- 位置: L68-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `document.createElementNS()`, `rectEl.setAttribute()`, `svg.appendChild()`, `svg.setAttributeNS()`, `this.nscolorToRGB()`, `wireframe.rects.reduce()`
- 参照: `rect.height`, `rect.width`, `rect.x`, `rect.y`, `rectObj.color`, `rectObj.height`, `rectObj.type`, `rectObj.width`, `rectObj.x`, `rectObj.y`, `svg.style.backgroundColor`, `wireframe.canvasBackground`, `wireframe.rects`
