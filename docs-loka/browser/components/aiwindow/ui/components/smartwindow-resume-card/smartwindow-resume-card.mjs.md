# browser/components/aiwindow/ui/components/smartwindow-resume-card/smartwindow-resume-card.mjs

source: browser/components/aiwindow/ui/components/smartwindow-resume-card/smartwindow-resume-card.mjs
source-hash: db4988b606910e6ed850d7a3dc9c0d9230831023
lines: 181

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SmartwindowResumeCard.constructor()
- 位置: L28-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.content`, `this.journeyId`

## SmartwindowResumeCard.#dispatch()
- 位置: L34-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowResumeCard.#onCardPointerDown()
- 位置: L47-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.getElementById()`
- 参照: `this.#wasMoreMenuOpenOnPointerDown`, `this.shadowRoot.getElementById(MORE_MENU_ID)?.open`

## SmartwindowResumeCard.#onCardClick()
- 位置: L52-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`, `this.ownerDocument.getSelection()`
- 参照: `event.detail`, `selection.isCollapsed`, `this.#wasMoreMenuOpenOnPointerDown`, `this.journeyId`

## SmartwindowResumeCard.#onDismissClick()
- 位置: L69-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.stopPropagation()`, `this.#dispatch()`
- 参照: `this.journeyId`

## SmartwindowResumeCard.#stopPropagation()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.stopPropagation()`

## SmartwindowResumeCard.#onMenuItemClick()
- 位置: L78-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`
- 参照: `this.journeyId`

## SmartwindowResumeCard.#renderFavicons()
- 位置: L85-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `tabs.slice()`, `tabs.slice(0, MAX_VISIBLE_FAVICONS).map()`
- 参照: `e.target.src`, `tab.url`, `tabs.length`, `this.content?.previewTabs`

## SmartwindowResumeCard.render()
- 位置: L109-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#onMenuItemClick()`, `this.#renderFavicons()`
- 条件付き依存: `if (!this.content)` → `html()`
- 参照: `this.#onCardClick`, `this.#onCardPointerDown`, `this.#onDismissClick`, `this.#stopPropagation`, `this.content`, `this.content.headline`, `this.content.previewTabs?.length`, `this.content.status`
