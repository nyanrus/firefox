# browser/components/places/InteractionsParent.sys.mjs

source: browser/components/places/InteractionsParent.sys.mjs
source-hash: cd781e0fab96a497663cdb6c38c96b6fde47b9b3
lines: 38

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## InteractionsParent.receiveMessage()
- 位置: L16-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Interactions.registerEndOfInteraction()`, `lazy.Interactions.registerNewInteraction()`
- 参照: `msg.data.referrer`, `msg.name`, `this.browsingContext.embedderElement`, `this.browsingContext.isActive`, `this.browsingContext?.embedderElement`, `this.manager.documentURI.specIgnoringRef`
