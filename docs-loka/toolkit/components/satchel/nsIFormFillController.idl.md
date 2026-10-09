# nsIFormFillFocusListener (toolkit/components/satchel/nsIFormFillController.idl)

source: toolkit/components/satchel/nsIFormFillController.idl
source-hash: 62164baeb75c045b18575fb352f087b78de4251e

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `Promise handleFocus(Element element)`: (未記入)

# nsIFormFillController (toolkit/components/satchel/nsIFormFillController.idl)

source: toolkit/components/satchel/nsIFormFillController.idl
source-hash: 62164baeb75c045b18575fb352f087b78de4251e

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/aiwindow/ui/actors/SmartFormFillChild.sys.mjs`](../../../browser/components/aiwindow/ui/actors/SmartFormFillChild.sys.mjs.md)

## メソッド / 属性
- `attribute Element controlledElement`: (未記入)
- `readonly attribute boolean passwordPopupAutomaticallyOpened`: (未記入)
- `void markAsAutoCompletableField(Element aElement)`: (未記入)
- `void showPopup()`: (未記入)
- `void addFocusListener(nsIFormFillFocusListener listener)`: (未記入)

# nsIFormFillCompleteObserver (toolkit/components/satchel/nsIFormFillController.idl)

source: toolkit/components/satchel/nsIFormFillController.idl
source-hash: 62164baeb75c045b18575fb352f087b78de4251e

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void onSearchCompletion(nsIAutoCompleteResult result)`: (未記入)
