# browser/components/firefoxview/OpenTabsController.sys.mjs

source: browser/components/firefoxview/OpenTabsController.sys.mjs
source-hash: 138c94f56ca01957e9203b58cf6f6cec474e5b2c
lines: 174

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## OpenTabsController.#getContainerObj()
- 位置: L22-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.getAttribute()`
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.getPublicIdentityFromId()`

## OpenTabsController.#getIndicatorsForTab()
- 位置: L40-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.hasAttribute()`, `this.#checkIfPinnedNewTab()`, `this.#getContainerObj()`
- 条件付き依存: `if (tab.pinned)` → `tabIndicators.push()`
- 条件付き依存: `if (this.#getContainerObj(tab))` → `tabIndicators.push()`
- 条件付き依存: `if (hasAttention)` → `tabIndicators.push()`
- 条件付き依存: `if (tab.hasAttribute("soundplaying") && !tab.hasAttribute("muted"))` → `tabIndicators.push()`
- 条件付き依存: `if (tab.hasAttribute("muted"))` → `tabIndicators.push()`
- 条件付き依存: `if (this.#checkIfPinnedNewTab(url))` → `tabIndicators.push()`
- 参照: `tab.linkedBrowser?.currentURI?.spec`, `tab.pinned`

## OpenTabsController.#checkIfPinnedNewTab()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.pinnedLinks.isPinned()`

## OpenTabsController.getPrimaryL10nId()
- 位置: L92-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabIndicators?.includes()`
- 条件付き依存: `if (!( tabIndicators?.includes("pinned") && tabIndicators?.includes("bookmark") ))` → `tabIndicators?.includes()`
- 条件付き依存: `if (!(tabIndicators?.includes("pinned")))` → `tabIndicators?.includes()`

## OpenTabsController.#getPrimaryL10nArgs()
- 位置: L122-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`
- 参照: `tab.label`

## OpenTabsController.getTabListItems()
- 位置: L137-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `filtered.map()`, `tab.getAttribute()`, `tabs?.filter()`, `this.#getContainerObj()`, `this.#getIndicatorsForTab()`, `this.#getPrimaryL10nArgs()`, `this.getPrimaryL10nId()`
- 参照: `tab.closing`, `tab.hidden`, `tab.label`, `tab.lastSeenActive`, `tab.pinned`, `tab?.linkedBrowser?.currentURI?.spec`
