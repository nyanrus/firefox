# browser/components/genai/GenAIChild.sys.mjs

source: browser/components/genai/GenAIChild.sys.mjs
source-hash: ff3ebf13c8780de43eee685f78e8aa9a8a92bad5
lines: 303

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## GenAIChild.registerHideEvents()
- 位置: L38-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HIDE_EVENTS.forEach()`, `this.contentWindow.addEventListener()`, `this.document.addEventListener()`
- 参照: `this.pendingHide`

## GenAIChild.removeHideEvents()
- 位置: L48-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HIDE_EVENTS.forEach()`, `this.contentWindow?.removeEventListener()`, `this.document.removeEventListener()`
- 参照: `this.#compositionActive`, `this.pendingHide`

## GenAIChild.handleEvent()
- 位置: L59-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sendHide()`, `this.contentWindow.setTimeout()`, `this.getSelectionInfo()`
- 条件付き依存: `if (this.mouseUpTimeout)` → `this.contentWindow.clearTimeout()`
- 条件付き依存: `if ( (selectionInfo.selection && selectionInfo.selection !== this.downSelection) || delay > lazy.shortcutsDelay )` → `this.sendAsyncMessage()`
- 条件付き依存: `if ( (selectionInfo.selection && selectionInfo.selection !== this.downSelection) || delay > lazy.shortcutsDelay )` → `this.registerHideEvents()`
- 条件付き依存: `if (this.pendingHide)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (this.pendingHide)` → `this.removeHideEvents()`
- 条件付き依存: `if (!(this.#compositionActive))` → `sendHide()`
- 参照: `event.altKey`, `event.button`, `event.ctrlKey`, `event.metaKey`, `event.shiftKey`, `event.timeStamp`, `event.type`, `lazy.shortcutsDebounce`, `lazy.shortcutsDelay`, `selectionInfo.selection`, `this.#compositionActive`, `this.#isDestroyed`, `this.contentWindow.devicePixelRatio`, `this.downSelection`, `this.downTimeStamp`, `this.getSelectionInfo().selection`, `this.mouseUpTimeout`, `this.pendingHide`

## sendHide()
- 位置: L60-66
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.pendingHide)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (this.pendingHide)` → `this.removeHideEvents()`
- 参照: `event.type`, `this.pendingHide`

## GenAIChild.getSelectionInfo()
- 位置: L155-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contentSelection?.toString()`, `contentSelection?.toString().trim()`, `this.contentWindow.getSelection()`
- 条件付き依存: `if (selection)` → `anchorElement?.closest()`
- 条件付き依存: `if (anchorElement?.closest("[contenteditable]"))` → `anchorElement.getRootNode()`
- 条件付き依存: `if (selectionStart != null && value != null)` → `value.slice()`
- 参照: `Node.ELEMENT_NODE`, `activeElement.localName`, `activeElement.selectionEnd`, `anchor.nodeType`, `anchor.parentElement`, `anchorElement.getRootNode().host?.localName`, `contentSelection.anchorNode`, `this.document`

## GenAIChild.receiveMessage()
- 位置: async L191-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.autoSubmitClick()`

## GenAIChild.findTextareaEl()
- 位置: async L207-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.document.querySelector()`, `win.performance.now()`, `win.requestAnimationFrame()`

## GenAIChild.autoSubmitClick()
- 位置: async L226-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/chatgpt\.com/i.test()`, `this.findTextareaEl()`, `win.document.querySelector()`, `win.location.pathname.includes()`, `win.requestAnimationFrame()`
- 条件付き依存: `if (win.document.readyState === "loading")` → `win.addEventListener()`
- 条件付き依存: `if (!editable.textContent)` → `editable.dispatchEvent()`
- 条件付き依存: `if (submitBtn)` → `submitBtn.click()`
- 条件付き依存: `if ( win._autosent && (/chatgpt\.com/i.test(win.location.host) || win.location.pathname.includes("file_chat-autosubmit.html")) )` → `container.querySelector()`
- 条件付き依存: `if ( win._autosent && (/chatgpt\.com/i.test(win.location.host) || win.location.pathname.includes("file_chat-autosubmit.html")) )` → `currentEditable.textContent?.trim()`
- 条件付き依存: `if (hasText)` → `currentEditable.dispatchEvent()`
- 条件付き依存: `if ( win._autosent && (/chatgpt\.com/i.test(win.location.host) || win.location.pathname.includes("file_chat-autosubmit.html")) )` → `observer.observe()`
- 条件付き依存: `if ( win._autosent && (/chatgpt\.com/i.test(win.location.host) || win.location.pathname.includes("file_chat-autosubmit.html")) )` → `win.setTimeout()`
- 条件付き依存: `if ( win._autosent && (/chatgpt\.com/i.test(win.location.host) || win.location.pathname.includes("file_chat-autosubmit.html")) )` → `observer.disconnect()`
- 参照: `currentEditable.textContent`, `currentEditable.textContent?.trim().length`, `editable.parentElement`, `editable.textContent`, `this.contentWindow`, `win.InputEvent`, `win.MutationObserver`, `win._autosent`, `win.document.readyState`, `win.location.host`

## GenAIChild.didDestroy()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isDestroyed`
