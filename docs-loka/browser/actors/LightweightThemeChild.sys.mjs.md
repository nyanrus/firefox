# browser/actors/LightweightThemeChild.sys.mjs

source: browser/actors/LightweightThemeChild.sys.mjs
source-hash: 97be44511cd336444edb92987385f83163474960
lines: 83

## <module>
- 役割: (未記入)

## LightweightThemeChild.constructor()
- 位置: L9-13
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cpmm.sharedData.addEventListener()`, `super()`
- 参照: `this._initted`
- XPCOM: `Services.cpmm`

## LightweightThemeChild.didDestroy()
- 位置: L15-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cpmm.sharedData.removeEventListener()`
- XPCOM: `Services.cpmm`

## LightweightThemeChild._getChromeOuterWindowID()
- 位置: L19-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`, `browserChild.chromeOuterWindowID`, `this.browsingContext.topChromeWindow.docShell.outerWindowID`, `this.docShell.browserChild`
- XPCOM: `Services.appinfo`

## LightweightThemeChild.handleEvent()
- 位置: L43-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.changedKeys.includes()`, `this._getChromeOuterWindowID()`
- 条件付き依存: `if (!this._initted && this._getChromeOuterWindowID())` → `this.update()`
- 条件付き依存: `if ( event.changedKeys.includes(`theme/${this._getChromeOuterWindowID()}`) )` → `this.update()`
- 参照: `event.type`, `this._initted`

## LightweightThemeChild.update()
- 位置: L67-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `Services.cpmm.sharedData.get()`, `this._getChromeOuterWindowID()`, `this.contentWindow.dispatchEvent()`
- 参照: `this.contentWindow`, `this.contentWindow.CustomEvent`
- XPCOM: `Services.cpmm`
