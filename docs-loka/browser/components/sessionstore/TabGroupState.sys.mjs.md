# browser/components/sessionstore/TabGroupState.sys.mjs

source: browser/components/sessionstore/TabGroupState.sys.mjs
source-hash: cc64fa43f5e142e7a4d91422d980872b808fde2d
lines: 192

## <module>
- 役割: タブグループの状態（開いている・閉じた・保存済み）を SessionStore が扱う形に変換する関数群。

## _TabGroupState.collect()
- 位置: L94-102
- 役割: 開いているタブグループの id・名前・色・折りたたみ状態・ウィンドウを閉じたとき保存するかを取り出す。
- 触るとき: セッションに保存されるタブグループの項目を増やす・減らすとき。
- 参照: `tabGroup.collapsed`, `tabGroup.color`, `tabGroup.id`, `tabGroup.label`, `tabGroup.saveOnWindowClose`

## _TabGroupState.closed()
- 位置: L116-124
- 役割: 閉じられるタブグループの状態を作る。closedAt・sourceWindowId を付け、tabs と splitViews は空にして呼び出し側が埋める。
- 触るとき: 閉じたタブグループが復元候補に入る流れを追うとき。
- 呼び出し先: `Date.now()`, `this.collect()`

## _TabGroupState.savedInOpenWindow()
- 位置: L139-141
- 役割: ユーザーが開いたままのウィンドウでグループを明示的に保存するときの状態を作る（closed の結果に saved: true を付ける）。
- 触るとき: 「グループを保存」操作で保存される内容を変えるとき。
- 呼び出し先: `this.closed()`

## _TabGroupState.savedInClosedWindow()
- 位置: L160-169
- 役割: ウィンドウを閉じた際に、そのウィンドウのグループを自動保存用の状態に変換する。windowClosedId を記録する。
- 触るとき: ウィンドウを閉じたときに残るグループの扱いや、移行時の保存を調べるとき。
- 呼び出し先: `Date.now()`

## _TabGroupState.abbreviated()
- 位置: L180-188
- 役割: 外部（拡張機能や公開 API）に返す際、id・名前・色・折りたたみ状態だけに絞る。saveOnWindowClose は含めない。
- 触るとき: 公開 API に出すタブグループの項目を増やす・減らすとき。
- 参照: `tabGroupState.collapsed`, `tabGroupState.color`, `tabGroupState.id`, `tabGroupState.name`
