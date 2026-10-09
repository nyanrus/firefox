# browser/components/aiwindow/ui/modules/ChatMessage.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatMessage.sys.mjs
source-hash: 41347a167619655f7362b9e97c08daf6735b5adc
lines: 408

## <module>
- 役割: (未記入)

## normalizeFollowUp()
- 位置: L22-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value .replace()`, `value .replace(/[.!?…]+\s*$/u, "") .trim()`, `value .replace(/[.!?…]+\s*$/u, "") .trim() .replace()`, `value .replace(/[.!?…]+\s*$/u, "") .trim() .replace(/\s+/g, " ") .replace()`

## ChatMessage.constructor()
- 位置: L129-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`, `super()`
- 参照: `this.citations`, `this.convId`, `this.followUpSuggestions`, `this.historyResults`, `this.isActiveBranch`, `this.memoriesApplied`, `this.memoriesEnabled`, `this.memoriesFlagSource`, `this.pageHistoryDeleted`, `this.pageUrl`, `this.revisionRootMessageId`, `this.tokens`, `this.toolUIData`, `this.toolUIDraft`, `this.webSearchQueries`

## ChatMessage.addTokens()
- 位置: L198-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `this.followUpSuggestions.push()`, `this.memoriesApplied.push()`, `this.webSearchQueries.push()`, `tokens.forEach()`
- 条件付き依存: `if (key == TOKEN_LABELS.FOLLOWUP)` → `normalizeFollowUp()`
- 条件付き依存: `if (Array.isArray(this.tokens[key]))` → `this.tokens[key].push()`
- 参照: `TOKEN_LABELS.EXISTING_MEMORY`, `TOKEN_LABELS.FOLLOWUP`, `TOKEN_LABELS.KIT`, `TOKEN_LABELS.SEARCH`, `this.kit`, `this.tokens`

## AssistantRoleOpts.constructor()
- 位置: L257-275
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.followUpSuggestions`, `this.memoriesApplied`, `this.memoriesEnabled`, `this.memoriesFlagSource`, `this.modelId`, `this.params`, `this.usage`, `this.webSearchQueries`

## ToolRoleOpts.constructor()
- 位置: L288-290
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.modelId`

## UserRoleOpts.constructor()
- 位置: L306-318
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.contextMentions`, `this.memoriesEnabled`, `this.memoriesFlagSource`, `this.revisionRootMessageId`

## ChatMinimal.constructor()
- 位置: L336-340
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#id`, `this.#pageUrl`, `this.#title`

## ChatMinimal.id()
- 位置: L342-344
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#id`

## ChatMinimal.title()
- 位置: L346-348
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#title`

## ChatMinimal.pageUrl()
- 位置: L350-352
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#pageUrl`

## ChatHistoryResult.constructor()
- 位置: L365-371
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#convId`, `this.#createdDate`, `this.#title`, `this.#updatedDate`, `this.#urls`

## ChatHistoryResult.convId()
- 位置: L376-378
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#convId`

## ChatHistoryResult.title()
- 位置: L383-385
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#title`

## ChatHistoryResult.createdDate()
- 位置: L390-392
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#createdDate`

## ChatHistoryResult.updatedDate()
- 位置: L397-399
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#updatedDate`

## ChatHistoryResult.urls()
- 位置: L404-406
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#urls`
