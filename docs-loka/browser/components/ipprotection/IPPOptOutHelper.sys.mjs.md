# browser/components/ipprotection/IPPOptOutHelper.sys.mjs

source: browser/components/ipprotection/IPPOptOutHelper.sys.mjs
source-hash: 5ec711e4c0b53e48968a2b943f9533e7207a94f8
lines: 47

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## IPPOptedOutHelperSingleton.init()
- 位置: L22-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`
- XPCOM: `Services.prefs`

## IPPOptedOutHelperSingleton.uninit()
- 位置: L26-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## IPPOptedOutHelperSingleton.initOnStartupCompleted()
- 位置: L30-30
- 役割: (未記入)
- 触るとき: (未記入)

## IPPOptedOutHelperSingleton.optedOut()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## IPPOptedOutHelperSingleton.observe()
- 位置: L36-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPProtectionService.updateState()`
- 条件付き依存: `if (this.optedOut)` → `lazy.CustomizableUI.removeWidgetFromArea()`
- 参照: `this.optedOut`
