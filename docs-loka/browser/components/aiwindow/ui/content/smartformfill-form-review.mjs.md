# browser/components/aiwindow/ui/content/smartformfill-form-review.mjs

source: browser/components/aiwindow/ui/content/smartformfill-form-review.mjs
source-hash: dc218c9b7980343b03c98cb296a3e98d7fe9b9aa
lines: 230

## <module>
- 役割: (未記入)
- 呼び出し先: `addEventListener()`, `closeDialog()`, `console.error()`, `dialogBox.classList.add()`, `dialogBox.classList.remove()`, `dialogBox.removeAttribute()`, `dialogBox.setAttribute()`, `dialogBrowser.closest()`, `document.querySelector()`, `initialize()`, `initialize().catch()`, `removeEventListener()`

## closeDialog()
- 位置: L63-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.close()`

## handleAction()
- 位置: async L79-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closeDialog()`, `dialogArguments.onAction()`
- 参照: `FORM_REVIEW_ACTIONS.CANCEL`, `FORM_REVIEW_ACTIONS.CLOSE`, `FORM_REVIEW_ACTIONS.FILL_FORM`, `FORM_REVIEW_ACTIONS.STOP`, `action.type`

## showGenerationResult()
- 位置: async L106-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `reviewActor.showGenerationError()`, `reviewActor.showSuggestions()`
- 条件付き依存: `if (!displayed)` → `closeDialog()`
- 参照: `dialogArguments.generationResult`, `result.fields`, `result?.errorType`, `result?.fields`

## handleKeydown()
- 位置: L128-134
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key === "Escape")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Escape")` → `event.stopPropagation()`
- 条件付き依存: `if (event.key === "Escape")` → `closeDialog()`
- 参照: `event.key`

## createReviewBrowser()
- 位置: L141-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.setAttribute()`, `document.createXULElement()`
- 参照: `browser.id`

## initialize()
- 位置: async L161-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.append()`, `createReviewBrowser()`, `dialogArguments.onReady()`, `reviewActor.connect()`, `reviewActor.initialize()`, `reviewBrowser.addEventListener()`, `reviewBrowser.browsingContext.currentWindowGlobal.getActor()`, `showGenerationResult()`, `showGenerationResult().catch()`
- 条件付き依存: `if (reviewBrowser.currentURI.spec !== REVIEW_URL)` → `closeDialog()`
- 条件付き依存: `if (!initialized)` → `closeDialog()`
- 条件付き依存: `if (!closing)` → `console.error()`
- 条件付き依存: `if (!closing)` → `closeDialog()`
- 参照: `document.subDialogSetDefaultFocus`, `reviewBrowser.currentURI.spec`

## document.subDialogSetDefaultFocus()
- 位置: L177-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reviewBrowser.focus()`
