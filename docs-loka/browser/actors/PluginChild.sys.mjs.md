# browser/actors/PluginChild.sys.mjs

source: browser/actors/PluginChild.sys.mjs
source-hash: 8dda1191040ad8f16878d38f92f826fc2fc7a370
lines: 95

## <module>
- 役割: (未記入)

## PluginChild.handleEvent()
- 位置: L7-18
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (eventType == "PluginCrashed")` → `this.onPluginCrashed()`
- 参照: `event.target.document`, `event.target.ownerDocument`, `event.type`, `this.document`

## PluginChild.isWithinFullScreenElement()
- 位置: L32-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fullScreenElement.contains()`
- 条件付き依存: `if (fullScreenElement.tagName === "IFRAME")` → `getTrueFullScreenElement()`
- 条件付き依存: `if (parentIframe)` → `this.isWithinFullScreenElement()`
- 参照: `domElement.documentGlobal.frameElement`, `fullScreenElement.tagName`

## getTrueFullScreenElement()
- 位置: L41-51
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( typeof fullScreenIframe.contentDocument !== "undefined" && fullScreenIframe.contentDocument.mozFullScreenElement )` → `getTrueFullScreenElement()`
- 参照: `fullScreenIframe.contentDocument`, `fullScreenIframe.contentDocument.mozFullScreenElement`

## PluginChild.onPluginCrashed()
- 位置: async L71-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contentWindow.PluginCrashedEvent.isInstance()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (fullScreenElement)` → `this.isWithinFullScreenElement()`
- 条件付き依存: `if (this.isWithinFullScreenElement(fullScreenElement, target))` → `this.contentWindow.top.document.mozCancelFullScreen()`
- 参照: `target.document`, `this.contentWindow.top.document.mozFullScreenElement`
