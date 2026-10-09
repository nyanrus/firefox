# browser/components/urlbar/content/SmartbarMentionUtils.mjs

source: browser/components/urlbar/content/SmartbarMentionUtils.mjs
source-hash: c7dfffea452787065aee56ecebca7d9b42532c3f
lines: 55

## <module>
- 役割: コンテキストメンション(タブまたはタブグループ)の識別子を作成・解析する純粋関数群。
- 呼び出し先: `Object.freeze()`

## getTabGroupMentionId()
- 位置: L22-24
- 役割: groupId に prefix を付けてタブグループのメンション ID を作る。
- 触るとき: タブグループ用メンションの ID 形式を変えたり、保存済み ID との互換性を確認するとき。

## parseTabGroupMentionId()
- 位置: L30-35
- 役割: メンション ID から group: 接頭辞を外して groupId を取り出す。接頭辞がない、または空なら null を返す。
- 触るとき: メンション ID からタブグループを特定する処理を書くとき。
- 呼び出し先: `mentionId.slice()`, `mentionId.startsWith()`
- 参照: `TAB_GROUP_MENTION_ID_PREFIX.length`

## getContextMentionKey()
- 位置: L41-46
- 役割: メンションの種類に応じてキーを返す。タブグループは group ID 由来の ID、それ以外は URL を使い、無ければ null を返す。
- 触るとき: メンションの一意性チェックや一覧からの削除で使われるキーの決め方を確認するとき。
- 条件付き依存: `if (mention.type == CONTEXT_MENTION_TYPE.TAB_GROUP)` → `getTabGroupMentionId()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `mention.groupId`, `mention.type`, `mention.url`

## isTabGroupMember()
- 位置: L52-54
- 役割: タブグループ由来の展開タブかどうか判定する。タブグループ自体ではなく groupId を持つ場合に true。
- 触るとき: グループに属するタブを一覧や候補でまとめて扱う判定を変えるとき。
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `mention.groupId`, `mention.type`
