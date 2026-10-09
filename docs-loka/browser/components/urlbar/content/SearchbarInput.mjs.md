# browser/components/urlbar/content/SearchbarInput.mjs

source: browser/components/urlbar/content/SearchbarInput.mjs
source-hash: e752d326b7ebae16dbd726fdbdbd6d6d4bcaf105
lines: 122

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## SearchbarInput.#shouldConnect()
- 位置: L26-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`

## SearchbarInput.connectedCallback()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.#shouldConnect()`

## SearchbarInput.disconnectedCallback()
- 位置: L37-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#shouldConnect()`

## SearchbarInput.sapInit()
- 位置: L44-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.inputField.setAttribute()`

## SearchbarInput.sapConnectedCallback()
- 位置: L49-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.xulStore.getValue()`, `document.documentElement.hasAttribute()`
- 条件付き依存: `if (storedWidth)` → `this.parentElement.setAttribute()`
- 参照: `(this.parentElement).style.width`, `document.documentURI`, `this.parentElement`, `this.parentElement.id`
- XPCOM: `Services.xulStore`

## SearchbarInput.sapDisconnectedCallback()
- 位置: L66-71
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.searchMode`

## SearchbarInput.initSapContextMenuItems()
- 位置: L73-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addContextMenuItems()`

## createItems()
- 位置: L77-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearHistory.addEventListener()`, `clearHistory.setAttribute()`, `fragment.append()`, `lazy.UrlbarUtils.clearFormHistory()`, `this.document.createDocumentFragment()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`, `this.handleRevert()`

## SearchbarInput.onPrefChanged()
- 位置: L95-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.onPrefChanged()`
- 条件付き依存: `if (pref == "browser.search.widget.new" && this.isConnected)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.search.widget.new"))` → `super.connectedCallback()`
- 条件付き依存: `if (!(UrlbarPrefs.get("browser.search.widget.new")))` → `super.disconnectedCallback()`
- 参照: `this.isConnected`

## SearchbarInput.handleEmptyValueNavigation()
- 位置: L108-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarSearchUtils.getDefaultEngine()`, `lazy.UrlbarSearchUtils.getEngineByName()`, `this.controller.whereToOpen()`, `this.openSearchEnginePage()`
- 参照: `this.isPrivate`, `this.searchMode`, `this.searchMode.engineName`
