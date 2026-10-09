# browser/components/urlbar/content/SmartbarMentionUtils.mjs

source: browser/components/urlbar/content/SmartbarMentionUtils.mjs
source-hash: c7dfffea452787065aee56ecebca7d9b42532c3f
lines: 55

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## getTabGroupMentionId()
- 位置: L22-24
- 役割: (未記入)
- 触るとき: (未記入)

## parseTabGroupMentionId()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mentionId.slice()`, `mentionId.startsWith()`
- 参照: `TAB_GROUP_MENTION_ID_PREFIX.length`

## getContextMentionKey()
- 位置: L41-46
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (mention.type == CONTEXT_MENTION_TYPE.TAB_GROUP)` → `getTabGroupMentionId()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `mention.groupId`, `mention.type`, `mention.url`

## isTabGroupMember()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `mention.groupId`, `mention.type`
