# browser/components/miniwindow/MiniWindowChild.sys.mjs

source: browser/components/miniwindow/MiniWindowChild.sys.mjs
source-hash: cb3387c06cd5870aac866de9f35cfdc321275014
lines: 136

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## MiniWindowChild.#enableScrollReveal()
- 位置: L33-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#scrollY()`, `this.contentWindow?.addEventListener()`
- 参照: `this.#lastScrollY`

## MiniWindowChild.handleEvent()
- 位置: L41-49
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type === "scroll")` → `this.#onScroll()`
- 条件付き依存: `if (event.type === "scroll")` → `this.#scrollTask.arm()`
- 参照: `event.type`, `lazy.DeferredTask`, `this.#scrollTask`

## MiniWindowChild.#scrollY()
- 位置: L55-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `utils.getScrollXY()`
- 参照: `scrollY.value`, `this.contentWindow?.windowUtils`

## MiniWindowChild.#onScroll()
- 位置: L70-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#scrollY()`, `this.sendAsyncMessage()`
- 参照: `this.#lastScrollY`

## MiniWindowChild.didDestroy()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#scrollTask?.disarm()`

## MiniWindowChild.receiveMessage()
- 位置: L84-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#enableScrollReveal()`, `this.#getSize()`, `this.#scrollTo()`
- 参照: `message.data`, `message.name`

## MiniWindowChild.#getSize()
- 位置: L104-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.logConsole.debug()`
- 参照: `el.scrollHeight`, `el.scrollWidth`, `this.contentWindow`, `win.innerHeight`, `win.innerWidth`, `win?.document?.documentElement`

## MiniWindowChild.#scrollTo()
- 位置: L127-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.contentWindow?.scrollTo()`
