# browser/components/asrouter/modules/PageEventManager.sys.mjs

source: browser/components/asrouter/modules/PageEventManager.sys.mjs
source-hash: a31dbe19412a61823c8eaf2365c24eea4c1daa0d
lines: 166

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## PageEventManager.constructor()
- 位置: L49-52
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.doc`, `this.win`, `win.document`

## PageEventManager.on()
- 位置: L60-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._listeners.has()`, `this._listeners.set()`
- 条件付き依存: `if (options?.every_window)` → `Services.uuid.generateUUID()`
- 条件付き依存: `if (options?.every_window)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (options?.every_window)` → `win.document.querySelectorAll()`
- 条件付き依存: `if (options?.every_window)` → `target.addEventListener()`
- 条件付き依存: `if (options?.every_window)` → `target.removeEventListener()`
- 条件付き依存: `if (!(options?.every_window))` → `this.doc.querySelectorAll()`
- 条件付き依存: `if (!(options?.every_window))` → `target.addEventListener()`
- 条件付き依存: `if (!(selectors))` → `["timeout", "interval"].includes()`
- 条件付き依存: `if (["timeout", "interval"].includes(type) && options.interval)` → `this.win.setInterval()`
- 参照: `Services.uuid.generateUUID().number`, `controller.signal`, `listener.callback`, `listener.controller`, `listener.uninit`, `options.capture`, `options.interval`, `options.preventDefault`, `options?.every_window`
- XPCOM: `Services.uuid`

## listener.uninit()
- 位置: L90-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.unregisterCallback()`

## abort()
- 位置: L99-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.win.clearInterval()`

## onInterval()
- 位置: L100-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`
- 条件付き依存: `if (type === "timeout")` → `abort()`

## PageEventManager.off()
- 位置: L118-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listener.controller?.abort()`, `listener.uninit()`, `this._listeners.delete()`, `this._listeners.get()`

## PageEventManager.once()
- 位置: L134-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.on()`

## wrappedCallback()
- 位置: L135-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `this.off()`

## PageEventManager.clear()
- 位置: L145-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listener.controller?.abort()`, `listener.uninit()`, `this._listeners.clear()`, `this._listeners.values()`

## PageEventManager.emit()
- 位置: L158-164
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (params.type === event.type)` → `listener.callback()`
- 参照: `event.type`, `params.type`, `this._listeners`
