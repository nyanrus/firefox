# browser/modules/SelectionChangedMenulist.sys.mjs

source: browser/modules/SelectionChangedMenulist.sys.mjs
source-hash: fd794004ede29198d855c1cc7090eb2758f85226
lines: 29

## <module>
- 役割: メニューリストのキーボード操作時にポップアップを開き、閉じたときに選択を通知する共通の補助。

## SelectionChangedMenulist.constructor()
- 位置: L10-27
- 役割: command でポップアップを開き、popuphiding のとき最後の command イベントを onCommand に渡す。
- 触るとき: Windows でキーボードでメニューリストを選ぶ挙動や、ポップアップを閉じたときに選択が反映されないタイミングの問題を調べるとき。
- 呼び出し先: `menulist.addEventListener()`, `popup.addEventListener()`
- 条件付き依存: `if (popup.state != "open" && popup.state != "showing")` → `popup.openPopup()`
- 条件付き依存: `if (lastEvent)` → `onCommand()`
- 参照: `menulist.menupopup`, `popup.state`
