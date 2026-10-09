# browser/components/shell/WindowsSetDefaultRedirect.sys.mjs

source: browser/components/shell/WindowsSetDefaultRedirect.sys.mjs
source-hash: d2c8d5812ae7463b39a870c2656a0a69607bbd10
lines: 136

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## WindowsSetDefaultRedirect.arm()
- 位置: L51-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.clearUserPref()`, `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## WindowsSetDefaultRedirect.clear()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## WindowsSetDefaultRedirect.consume()
- 位置: L78-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `this.#matches()`, `this.#read()`
- 参照: `state.overrideUri`
- XPCOM: `Services.prefs`

## WindowsSetDefaultRedirect.#read()
- 位置: L94-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`
- 参照: `state.openWithArg`
- XPCOM: `Services.prefs`

## WindowsSetDefaultRedirect.#matches()
- 位置: L119-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new lazy.FileUtils.File(state.openWithArg).equals()`
- 参照: `lazy.FileUtils.File`, `state.openWithArg`, `state.type`, `this.TYPE.FILE`, `this.TYPE.PROTOCOL`
