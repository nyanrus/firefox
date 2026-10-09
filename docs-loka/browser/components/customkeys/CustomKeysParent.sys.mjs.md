# browser/components/customkeys/CustomKeysParent.sys.mjs

source: browser/components/customkeys/CustomKeysParent.sys.mjs
source-hash: 3a3b05e5eecf89193be8931b77a2b8eb5b6271b7
lines: 376

## <module>
- 役割: (未記入)

## getAlphanumericKey()
- 位置: L24-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String.fromCharCode()`
- 参照: `KeyEvent.DOM_VK_0`, `KeyEvent.DOM_VK_9`, `KeyEvent.DOM_VK_A`, `KeyEvent.DOM_VK_Z`

## isSingleCharacter()
- 位置: L49-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `graphemeSegmenter.segment()`, `graphemeSegmenter.segment(key)[Symbol.iterator]()`, `segments.next()`
- 参照: `Symbol.iterator`, `segments.next().done`

## CustomKeysParent.getKeyData()
- 位置: L58-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomKeys.getDefaultKey()`, `ShortcutUtils.prettifyShortcut()`, `keyEl.getAttribute()`, `keyEl.hasAttribute()`, `this.browsingContext.topChromeWindow.document.getElementById()`

## CustomKeysParent.getKeys()
- 位置: L78-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `add()`, `item.closest()`, `item.getAttribute()`, `mainMenuBar.querySelectorAll()`, `topWin.document.getElementById()`
- 条件付き依存: `if (!isMac)` → `add()`
- 条件付き依存: `if (!isMac)` → `topWin.document.getElementById()`
- 条件付き依存: `if (AppConstants.platform !== "win")` → `add()`
- 条件付き依存: `if (isMac)` → `add()`
- 参照: `AppConstants.platform`, `item.label`, `menu.label`, `menu?.id`, `this.browsingContext.topChromeWindow`, `topWin.document.getElementById( "viewSidebarMenuMenu" ).label`, `topWin.document.getElementById("browserToolsMenu").label`, `topWin.document.getElementById("edit-menu").label`, `topWin.document.getElementById("file-menu").label`, `topWin.document.getElementById("history-menu").label`, `topWin.document.getElementById("menu_findAgain").label`, `topWin.document.getElementById("menu_openLocation").label`, `topWin.document.getElementById("tools-menu").label`, `topWin.document.getElementById("view-menu").label`
- XPCOM: `Services.obs`

## add()
- 位置: L84-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getKeyData()`
- 参照: `data.title`

## CustomKeysParent.prettifyShortcut()
- 位置: L210-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ShortcutUtils.getKeyString()`, `ShortcutUtils.getModifierString()`

## CustomKeysParent.receiveMessage()
- 位置: async L219-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomKeys.changeKey()`, `CustomKeys.clearKey()`, `CustomKeys.getDefaultKey()`, `CustomKeys.resetAll()`, `CustomKeys.resetKey()`, `Object.assign()`, `Services.prompt.asyncConfirmEx()`, `result.get()`, `this.getKeyData()`, `this.getKeys()`, `this.prettifyShortcut()`
- 条件付き依存: `if (message.data)` → `this.browsingContext.embedderElement.addEventListener()`
- 条件付き依存: `if (!(message.data))` → `this.browsingContext.embedderElement.removeEventListener()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_CONTENT`, `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_0_DEFAULT`, `Ci.nsIPromptService.BUTTON_POS_1`, `Ci.nsIPromptService.BUTTON_TITLE_IS_STRING`, `Ci.nsIPromptService.BUTTON_TITLE_OK`, `data.id`, `data.shortcut`, `message.data`, `message.data.body`, `message.data.buttonCancel`, `message.data.buttonConfirm`, `message.data.id`, `message.data.title`, `message.name`, `this.browsingContext`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsIPromptService`](../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / `Services.prompt`

## CustomKeysParent.handleEvent()
- 位置: L295-374
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "keydown")` → `event.preventDefault()`
- 条件付き依存: `if (event.type == "keydown")` → `event.stopPropagation()`
- 条件付き依存: `if (event.altKey)` → `modifiers.push()`
- 条件付き依存: `if (event.ctrlKey)` → `modifiers.push()`
- 条件付き依存: `if (event.metaKey && AppConstants.platform !== "win")` → `modifiers.push()`
- 条件付き依存: `if (event.shiftKey)` → `modifiers.push()`
- 条件付き依存: `if (event.type == "keydown")` → `modifiers.sort().join()`
- 条件付き依存: `if (event.type == "keydown")` → `modifiers.sort()`
- 条件付き依存: `if ( event.key == "Alt" || event.key == "Control" || event.key == "Meta" || event.key == "Shift" )` → `ShortcutUtils.getModifierString()`
- 条件付き依存: `if ( event.key == "Alt" || event.key == "Control" || event.key == "Meta" || event.key == "Shift" )` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "keydown")` → `event.getModifierState()`
- 条件付き依存: `if (event.type == "keydown")` → `getAlphanumericKey()`
- 条件付き依存: `if (event.type == "keydown")` → `isSingleCharacter()`
- 条件付き依存: `if (alphanumericKey || isSingleCharacter(event.key))` → `event.key.toUpperCase()`
- 条件付き依存: `if (!(alphanumericKey || isSingleCharacter(event.key)))` → `ShortcutUtils.getKeycodeAttribute()`
- 条件付き依存: `if (data.isValid)` → `this.prettifyShortcut()`
- 条件付き依存: `if (event.type == "keydown")` → `this.sendAsyncMessage()`
- 参照: `AppConstants.platform`, `data.isModifier`, `data.isValid`, `data.key`, `data.keycode`, `data.modifierString`, `data.modifiers`, `data.shortcut`, `event.altKey`, `event.ctrlKey`, `event.key`, `event.keyCode`, `event.metaKey`, `event.shiftKey`, `event.type`, `modifiers.length`
