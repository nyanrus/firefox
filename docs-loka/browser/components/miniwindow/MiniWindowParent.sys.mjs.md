# browser/components/miniwindow/MiniWindowParent.sys.mjs

source: browser/components/miniwindow/MiniWindowParent.sys.mjs
source-hash: 5d5d28e63b76888e196b4276f9638b454844dd92
lines: 31

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## MiniWindowParent.receiveMessage()
- 位置: L16-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MiniWindowManager._miniWindowForBrowser()`
- 条件付き依存: `if (message.data.up)` → `miniwindow?.revealToolbar()`
- 条件付き依存: `if (!(message.data.up))` → `miniwindow?.hideToolbarOnScrollDown()`
- 参照: `message.data.up`, `message.name`, `this.browsingContext?.top?.embedderElement`
