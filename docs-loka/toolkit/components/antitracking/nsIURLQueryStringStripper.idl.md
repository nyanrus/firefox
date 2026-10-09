# nsIURLQueryStringStripper (toolkit/components/antitracking/nsIURLQueryStringStripper.idl)

source: toolkit/components/antitracking/nsIURLQueryStringStripper.idl
source-hash: d05b217790a7678375ca53ffb6e38f8d0b043d79

- 継承: nsISupports
- 役割: nsIURLQueryStringStripper is responsible for stripping certain part of the
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/components/urlbar/content/SmartbarInput.mjs`](../../../browser/components/urlbar/content/SmartbarInput.mjs.md), [`browser/components/urlbar/content/UrlbarInputBase.mjs`](../../../browser/components/urlbar/content/UrlbarInputBase.mjs.md)

## メソッド / 属性
- `uint32_t strip(nsIURI aURI, boolean aIsPBM, nsIURI aOutput)`: (未記入)
- `nsIURI stripForCopyOrShare(nsIURI aURI)`: (未記入)
- `boolean canStripForShare(nsIURI aURI)`: (未記入)
- `ACString testGetStripList()`: (未記入)
