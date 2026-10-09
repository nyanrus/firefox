# browser/modules/SelectionChangedMenulist.sys.mjs

source: browser/modules/SelectionChangedMenulist.sys.mjs
source-hash: fd794004ede29198d855c1cc7090eb2758f85226
lines: 29

## <module>
- 役割: (未記入)

## SelectionChangedMenulist.constructor()
- 位置: L10-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menulist.addEventListener()`, `popup.addEventListener()`
- 条件付き依存: `if (popup.state != "open" && popup.state != "showing")` → `popup.openPopup()`
- 条件付き依存: `if (lastEvent)` → `onCommand()`
- 参照: `menulist.menupopup`, `popup.state`
