# browser/modules/SerialDeviceSharingHelper.sys.mjs

source: browser/modules/SerialDeviceSharingHelper.sys.mjs
source-hash: 2919702e36dcbeffa6bf9e37f193706e5fd7bfa6
lines: 40

## <module>
- 役割: (未記入)

## observe()
- 位置: L8-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`, `Math.max()`, `browser.documentGlobal?.gBrowser?.updateBrowserSharing()`, `props.getPropertyAsBool()`, `props.getPropertyAsUint64()`, `subject.QueryInterface()`, `this._activePortCounts.get()`, `this._activePortCounts.set()`
- 条件付き依存: `if (!bc)` → `console.warn()`
- 条件付き依存: `if (!browser)` → `console.warn()`
- 参照: `Ci.nsIPropertyBag2`, `bc.embedderElement`
- XPCOM: [`nsIPropertyBag2`](../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## resetBrowserCount()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._activePortCounts.delete()`
