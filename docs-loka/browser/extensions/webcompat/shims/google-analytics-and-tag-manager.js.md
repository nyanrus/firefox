# browser/extensions/webcompat/shims/google-analytics-and-tag-manager.js

source: browser/extensions/webcompat/shims/google-analytics-and-tag-manager.js
source-hash: 8809fca8ece18422ea8eede2d45248d299a0bf8f
lines: 188

## <module>
- 役割: (未記入)

## run()
- 位置: L28-36
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof fn === "function")` → `fn()`
- 条件付き依存: `if (typeof fn === "function")` → `console.error()`

## create()
- 位置: L38-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `trackers.get()`, `trackers.has()`
- 条件付き依存: `if (!trackers.has(name))` → `Object.entries()`
- 条件付き依存: `if (!trackers.has(name))` → `trackers.set()`
- 参照: `opts?.cookieDomain`, `opts?.name`, `opts?.trackerId`

## get()
- 位置: L53-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `props.get()`

## ma()
- 位置: L63-63
- 役割: (未記入)
- 触るとき: (未記入)

## requireSync()
- 位置: L64-64
- 役割: (未記入)
- 触るとき: (未記入)

## send()
- 位置: L65-65
- 役割: (未記入)
- 触るとき: (未記入)

## set()
- 位置: L66-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `props.set()`
- 条件付き依存: `if (typeof p !== "object")` → `Object.fromEntries()`
- 条件付き依存: `if (k === "hitCallback")` → `run()`

## ga()
- 位置: L84-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cmdRE.exec()`
- 条件付き依存: `if (arguments.length === 1 && typeof cmd === "function")` → `run()`
- 条件付き依存: `if (arguments.length === 1 && typeof cmd === "function")` → `trackers.get()`
- 条件付き依存: `if (!groups)` → `console.error()`
- 条件付き依存: `if (cmd === "set")` → `trackers.get(name)?.set()`
- 条件付き依存: `if (cmd === "set")` → `trackers.get()`
- 条件付き依存: `if (method === "remove")` → `trackers.delete()`
- 条件付き依存: `if (cmd === "send")` → `run()`
- 条件付き依存: `if (cmd === "send")` → `args.at()`
- 条件付き依存: `if (method === "create")` → `args.slice()`
- 条件付き依存: `if (method === "create")` → `create()`
- 参照: `args.at(-1)?.hitCallback`, `arguments.length`, `cmdRE.exec(cmd)?.groups`

## create()
- 位置: L142-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ga()`

## getAll()
- 位置: L143-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `trackers.values()`

## getByName()
- 位置: L144-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `trackers.get()`

## remove()
- 位置: L146-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ga()`

## push()
- 位置: L154-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ga()`

## push()
- 位置: L166-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `run()`, `setTimeout()`
- 参照: `o?.eventCallback`

## autoLink()
- 位置: L181-181
- 役割: (未記入)
- 触るとき: (未記入)

## decorate()
- 位置: L182-184
- 役割: (未記入)
- 触るとき: (未記入)

## passthrough()
- 位置: L185-185
- 役割: (未記入)
- 触るとき: (未記入)
