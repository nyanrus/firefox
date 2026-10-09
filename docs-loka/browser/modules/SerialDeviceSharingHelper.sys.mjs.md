# browser/modules/SerialDeviceSharingHelper.sys.mjs

source: browser/modules/SerialDeviceSharingHelper.sys.mjs
source-hash: 2919702e36dcbeffa6bf9e37f193706e5fd7bfa6
lines: 40

## <module>
- 役割: シリアルポートの接続状態を、タブごとに数えてブラウザーの共有インジケーターに反映する。

## observe()
- 位置: L8-34
- 役割: serial-device-state-changed を受け、browserId のブラウザーの接続数を増減し、0 より多ければ serial 共有表示を有効にする。
- 触るとき: シリアルデバイスの共有表示が付いたまま消えない、または付かない問題を調べるとき。接続数の数え方を変えるとき。
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`, `Math.max()`, `browser.documentGlobal?.gBrowser?.updateBrowserSharing()`, `props.getPropertyAsBool()`, `props.getPropertyAsUint64()`, `subject.QueryInterface()`, `this._activePortCounts.get()`, `this._activePortCounts.set()`
- 条件付き依存: `if (!bc)` → `console.warn()`
- 条件付き依存: `if (!browser)` → `console.warn()`
- 参照: `Ci.nsIPropertyBag2`, `bc.embedderElement`
- XPCOM: [`nsIPropertyBag2`](../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## resetBrowserCount()
- 位置: L36-38
- 役割: 指定ブラウザーの接続数の記録を削除する。
- 触るとき: サイト権限パネルから serial の権限を削除して共有表示をリセットする処理の挙動を調べるとき。
- 呼び出し先: `this._activePortCounts.delete()`
