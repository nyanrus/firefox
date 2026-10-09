# browser/base/content/browser-unified-extensions.js

source: browser/base/content/browser-unified-extensions.js
source-hash: 49d61666662d989c1f3fcdeb1a6c4dfeacd0a737
lines: 209

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## setExtension()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.extension`

## connectedCallback()
- 位置: L35-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `template.content.cloneNode()`, `this._actionButton.addEventListener()`, `this._menuButton.addEventListener()`, `this.addEventListener()`, `this.appendChild()`, `this.querySelector()`, `this.render()`
- 参照: `this._actionButton`, `this._menuButton`, `this._messageBarWrapper`, `this._messageBarWrapper.extensionId`, `this._messageDeck`, `this.extension?.id`

## handleEvent()
- 位置: L72-118
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (target === this._menuButton)` → `target.ownerDocument.getElementById()`
- 条件付き依存: `if (target === this._menuButton)` → `popup.openPopup()`
- 条件付き依存: `if (target === this._actionButton)` → `this.extension.tabManager.addActiveTabPermission()`
- 条件付き依存: `if (target === this._actionButton)` → `this.extension.tabManager.activateScripts()`
- 参照: `event.target.documentGlobal`, `event.type`, `gUnifiedExtensions.MESSAGE_DECK_INDEX_DEFAULT`, `gUnifiedExtensions.MESSAGE_DECK_INDEX_HOVER`, `gUnifiedExtensions.MESSAGE_DECK_INDEX_MENU_HOVER`, `target.firstElementChild`, `this._actionButton`, `this._menuButton`, `this._messageDeck.selectedIndex`, `win.gBrowser.selectedTab`

## #setStateMessage()
- 位置: L120-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OriginControls.getStateMessageIDs()`, `this.ownerDocument.l10n.setAttributes()`, `this.querySelector()`
- 参照: `messages.default`, `messages.onHover`, `this.documentGlobal.gBrowser.selectedTab`, `this.extension.policy`

## #hasAction()
- 位置: L147-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OriginControls.getState()`
- 参照: `state.hasAccess`, `state.whenClicked`, `this.documentGlobal.gBrowser.selectedTab`, `this.extension.policy`

## render()
- 位置: L156-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`, `AddonManager.getAddonByID(this.extension.id).then()`, `AddonManager.getPreferredIconURL()`, `OriginControls.getAttentionState()`, `this.#hasAction()`, `this.#setStateMessage()`, `this._messageBarWrapper?.refresh()`, `this.classList.add()`, `this.ownerDocument.l10n.setAttributes()`, `this.querySelector()`, `this.setAttribute()`, `this.toggleAttribute()`
- 条件付き依存: `if (iconURL)` → `this.querySelector(".unified-extensions-item-icon").setAttribute()`
- 条件付き依存: `if (iconURL)` → `this.querySelector()`
- 参照: `this._actionButton.dataset.extensionid`, `this._actionButton.disabled`, `this._menuButton`, `this._menuButton.dataset.extensionid`, `this.documentGlobal`, `this.extension`, `this.extension.id`, `this.extension.name`, `this.extension.policy`, `this.querySelector(".unified-extensions-item-name").textContent`
