# browser/components/aiwindow/ui/actors/AISmartBarChild.sys.mjs

source: browser/components/aiwindow/ui/actors/AISmartBarChild.sys.mjs
source-hash: e6949695361b3383b1d98215c14b794f2f35b5e3
lines: 43

## <module>
- 役割: (未記入)

## AISmartBarChild.receiveMessage()
- 位置: L16-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (msg.name === "AskFromParent")` → `this.contentWindow.document.dispatchEvent()`
- 参照: `msg.data`, `msg.name`, `this.contentWindow.CustomEvent`
