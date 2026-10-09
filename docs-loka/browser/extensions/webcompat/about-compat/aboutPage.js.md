# browser/extensions/webcompat/about-compat/aboutPage.js

source: browser/extensions/webcompat/about-compat/aboutPage.js
source-hash: 9eb25b37f5af20c7905caa53322ad2b318818848
lines: 43

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`

## onStartup()
- 位置: L21-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `resProto.setSubstitution()`
- 条件付き依存: `if (!(ContractID in Cc))` → `Services.ppmm.loadProcessScript()`
- 参照: `this.extension`, `this.processScriptRegistered`
- XPCOM: `Services.io` / `Services.ppmm`

## onShutdown()
- 位置: L35-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resProto.setSubstitution()`
- 条件付き依存: `if (this.processScriptRegistered)` → `Services.ppmm.removeDelayedProcessScript()`
- 参照: `this.processScriptRegistered`
- XPCOM: `Services.ppmm`
