# browser/components/screenshots/screenshots-buttons.js

source: browser/components/screenshots/screenshots-buttons.js
source-hash: 63342f7fa1bf6d136231470625b5bc6aedbc71e9
lines: 190

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `customElements.define()`

## ScreenshotsButtons.markup()
- 位置: L26-35
- 役割: (未記入)
- 触るとき: (未記入)

## ScreenshotsButtons.miniWindowMarkup()
- 位置: L37-55
- 役割: (未記入)
- 触るとき: (未記入)

## ScreenshotsButtons.fragmentFor()
- 位置: L57-66
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!ScreenshotsButtons.#templates[mode])` → `MozXULElement.parseXULToFragment()`
- 参照: `SELECTION_MODES.MINI_WINDOW`, `ScreenshotsButtons.#templates`, `ScreenshotsButtons.markup`, `ScreenshotsButtons.miniWindowMarkup`

## ScreenshotsButtons.isMiniWindow()
- 位置: L68-70
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SELECTION_MODES.MINI_WINDOW`, `this.#renderedMode`

## ScreenshotsButtons.clickTarget()
- 位置: L73-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.querySelector()`
- 参照: `this.isMiniWindow`

## ScreenshotsButtons.visibleButton()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.getElementById()`

## ScreenshotsButtons.fullpageButton()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.getElementById()`

## ScreenshotsButtons.moveSelectionButton()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.getElementById()`

## ScreenshotsButtons.moveFullTabButton()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.getElementById()`

## ScreenshotsButtons.#render()
- 位置: L91-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ScreenshotsButtons.fragmentFor()`, `ScreenshotsButtons.fragmentFor(mode).cloneNode()`, `shadowRoot.append()`, `shadowRoot.replaceChildren()`, `this.attachShadow()`, `this.clickTarget.addEventListener()`, `this.clickTarget?.removeEventListener()`, `this.getAttribute()`
- 参照: `this.#renderedMode`, `this.shadowRoot`

## ScreenshotsButtons.attributeChangedCallback()
- 位置: L104-108
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isConnected)` → `this.#render()`
- 参照: `this.isConnected`

## ScreenshotsButtons.connectedCallback()
- 位置: L110-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#render()`, `this.ownerDocument.l10n.connectRoot()`
- 条件付き依存: `if (alreadyRendered)` → `this.clickTarget.removeEventListener()`
- 条件付き依存: `if (alreadyRendered)` → `this.clickTarget.addEventListener()`
- 参照: `this.shadowRoot`

## ScreenshotsButtons.disconnectedCallback()
- 位置: L121-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clickTarget?.removeEventListener()`, `this.ownerDocument.l10n.disconnectRoot()`
- 参照: `this.shadowRoot`

## ScreenshotsButtons.handleEvent()
- 位置: L126-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ScreenshotsUtils.closePanel()`, `ScreenshotsUtils.miniWindowFullTab()`, `ScreenshotsUtils.miniWindowFullTab(browser).catch()`, `ScreenshotsUtils.moveFocusToContent()`, `ScreenshotsUtils.takeScreenshot()`, `event.target.closest()`
- 参照: `console.error`, `gBrowser.selectedBrowser`, `this.fullpageButton`, `this.moveFullTabButton`, `this.moveSelectionButton`, `this.visibleButton`

## ScreenshotsButtons.focusButton()
- 位置: async L162-185
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (buttonToFocus === "last")` → `this.moveFullTabButton.focus()`
- 条件付き依存: `if (!(buttonToFocus === "last"))` → `this.moveSelectionButton.focus()`
- 条件付き依存: `if (buttonToFocus === "fullpage")` → `this.fullpageButton.focus()`
- 条件付き依存: `if (buttonToFocus === "first")` → `this.clickTarget.firstElementChild.focus()`
- 条件付き依存: `if (buttonToFocus === "last")` → `this.clickTarget.lastElementChild.focus()`
- 条件付き依存: `if (!(buttonToFocus === "last"))` → `this.visibleButton.focus()`
- 参照: `this.clickTarget.updateComplete`, `this.isMiniWindow`
