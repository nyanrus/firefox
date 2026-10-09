# browser/components/urlbar/content/UrlbarContentPrefs.mjs

source: browser/components/urlbar/content/UrlbarContentPrefs.mjs
source-hash: 80eab57d0b91d5dd1a1de20fbf659bf8b29c52ac
lines: 40

## <module>
- 役割: (未記入)
- 呼び出し先: `getPrefs()`

## getPrefs()
- 位置: L16-37
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof ChromeUtils != "undefined")` → `ChromeUtils.importESModule()`
- 参照: `ChromeUtils.importESModule( "moz-src:///browser/components/urlbar/UrlbarPrefs.sys.mjs" ).UrlbarPrefs`

## get()
- 位置: L26-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.UrlbarActorPort.getPref()`

## getScotchBonnetPref()
- 位置: L31-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `get()`

## addObserver()
- 位置: L32-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.UrlbarActorPort.addPrefObserver()`

## removeObserver()
- 位置: L33-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.UrlbarActorPort.removePrefObserver()`

## toggleResultMenuKeyboardAccessible()
- 位置: L34-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.UrlbarActorPort.toggleResultMenuKeyboardAccessible()`
