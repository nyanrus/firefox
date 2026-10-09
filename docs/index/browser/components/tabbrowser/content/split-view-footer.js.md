# browser/components/tabbrowser/content/split-view-footer.js

source: browser/components/tabbrowser/content/split-view-footer.js
source-hash: bec7c2621ff9294a5ab560444057600b73f1c6ae
lines: 232

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `customElements.define()`

## onLocationChange()
- 位置: L40-44
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWebProgress?.isTopLevel && aLocation)` → `this.#updateUri()`

## onSecurityChange()
- 位置: L45-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#toggleInsecure()`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## MozSplitViewFooter.connectedCallback()
- 位置: L68-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateSecurityElement()`, `this.#updateTabImageIconElement()`, `this.#updateUriElement()`, `this.addEventListener()`, `this.appendChild()`, `this.menuButtonElement.addEventListener()`, `this.querySelector()`

## MozSplitViewFooter.disconnectedCallback()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resetTab()`

## MozSplitViewFooter.handleEvent()
- 位置: L95-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.stopPropagation()`, `gBrowser.openSplitViewMenu()`, `this.#handleTabAttrModified()`

## MozSplitViewFooter.#handleTabAttrModified()
- 位置: L111-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateTabImageIconSrc()`

## MozSplitViewFooter.#toggleInsecure()
- 位置: L124-132
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.securityElement)` → `this.#updateSecurityElement()`
- 条件付き依存: `if (this.tabImageIconElement)` → `this.#updateTabImageIconElement()`

## MozSplitViewFooter.#updateSecurityElement()
- 位置: L134-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#uri.schemeIs()`

## MozSplitViewFooter.#updateTabImageIconSrc()
- 位置: L145-150
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.tabImageIconElement)` → `this.#updateTabImageIconElement()`

## MozSplitViewFooter.#updateTabImageIconElement()
- 位置: L152-160
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (canShowIcon)` → `this.tabImageIconElement.setAttribute()`
- 条件付き依存: `if (!(canShowIcon))` → `this.tabImageIconElement.removeAttribute()`

## MozSplitViewFooter.#updateUri()
- 位置: L167-176
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.uriElement)` → `this.#updateUriElement()`
- 条件付き依存: `if (this.securityElement)` → `this.#updateSecurityElement()`

## MozSplitViewFooter.#updateUriElement()
- 位置: L178-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.formatURIForDisplay()`

## MozSplitViewFooter.setTab()
- 位置: L190-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.addEventListener()`, `tab.linkedBrowser.addProgressListener()`, `this.#resetTab()`, `this.#toggleInsecure()`, `this.#updateTabImageIconSrc()`, `this.#updateUri()`
- XPCOM: [`nsIWebProgress`](../../../../dom/interfaces/base/nsIBrowser.idl.md) / [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## MozSplitViewFooter.#resetTab()
- 位置: L217-227
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#tab)` → `this.#tab.removeEventListener()`
- 条件付き依存: `if (this.#tab.linkedBrowser?.webProgress)` → `this.#tab.linkedBrowser.removeProgressListener()`
