# browser/components/customkeys/CustomKeys.sys.mjs

source: browser/components/customkeys/CustomKeys.sys.mjs
source-hash: 76f99381ab7011992b8f28f8d031ed41f73d6293
lines: 301

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `PathUtils.join()`

## applyToKeyEl()
- 位置: L34-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keyEl.removeAttribute()`, `keysets.add()`, `window.document.getElementById()`
- 条件付き依存: `if (!original[keyId])` → `keyEl.getAttribute()`
- 条件付き依存: `if (val)` → `keyEl.setAttribute()`
- 参照: `config.data`, `keyEl.parentElement`, `keyEl.tagName`

## resetKeyEl()
- 位置: L62-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keyEl.removeAttribute()`, `keysets.add()`, `window.document.getElementById()`
- 条件付き依存: `if (val !== undefined)` → `keyEl.setAttribute()`
- 参照: `keyEl.parentElement`

## applyToNewWindow()
- 位置: async L78-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `applyToKeyEl()`, `config.load()`, `observe()`, `refreshKeysets()`
- 参照: `config.data`

## refreshKeysets()
- 位置: L88-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keyset.remove()`, `parent.append()`, `windows.get()`
- 条件付き依存: `if (observer)` → `observer.disconnect()`
- 条件付き依存: `if (observer)` → `observe()`
- 参照: `keyset.parentElement`, `keysets.size`

## observe()
- 位置: L111-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `observer.observe()`, `windows.get()`
- 条件付き依存: `if (!observer)` → `applyToKeyEl()`
- 条件付き依存: `if (!observer)` → `refreshKeysets()`
- 条件付き依存: `if (!observer)` → `windows.set()`
- 参照: `config.data`, `key.id`, `key.tagName`, `mutation.addedNodes`, `node.children`, `node.tagName`, `window.MutationObserver`, `window.document`, `window.document.body`

## changeKey()
- 位置: L154-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `applyToKeyEl()`, `config.saveSoon()`, `refreshKeysets()`, `this.getDefaultKey()`, `windows.keys()`
- 条件付き依存: `if ( defaultKey && modifiers == defaultKey.modifiers && key == defaultKey.key && keycode == defaultKey.keycode )` → `this.resetKey()`
- 参照: `config.data`, `data.key`, `data.keycode`, `data.modifiers`, `defaultKey.key`, `defaultKey.keycode`, `defaultKey.modifiers`, `existing.key`, `existing.keycode`, `existing.modifiers`

## resetKey()
- 位置: L197-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.saveSoon()`, `refreshKeysets()`, `resetKeyEl()`, `windows.keys()`
- 参照: `config.data`

## clearKey()
- 位置: L216-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.changeKey()`

## clearAll()
- 位置: L225-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keyEl.hasAttribute()`, `this.clearKey()`, `window.document.querySelectorAll()`, `windows.keys()`
- 条件付き依存: `if ( config.data[keyEl.id] || keyEl.hasAttribute("key") || keyEl.hasAttribute("keycode") )` → `ids.add()`
- 参照: `config.data`, `keyEl.id`

## resetAll()
- 位置: L250-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `config.saveSoon()`, `refreshKeysets()`, `resetKeyEl()`, `windows.keys()`
- 参照: `config.data`

## initWindow()
- 位置: L265-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `applyToNewWindow()`

## uninitWindow()
- 位置: L269-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windows.delete()`, `windows.get()`, `windows.get(window).disconnect()`

## getDefaultKey()
- 位置: L281-297
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `data.key`, `data.keycode`, `data.modifiers`, `origKey.key`, `origKey.keycode`, `origKey.modifiers`
