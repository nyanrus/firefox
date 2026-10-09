# browser/components/aboutlogins/content/components/menu-button.mjs

source: browser/components/aboutlogins/content/components/menu-button.mjs
source-hash: 20db6b0366ac9945af3bf8fb066d9345427191ac
lines: 181

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## MenuButton.connectedCallback()
- 位置: L6-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MenuButtonTemplate.content.cloneNode()`, `document.addEventListener()`, `document.l10n.connectRoot()`, `document.querySelector()`, `menuitem.dataset.supportedPlatforms .split()`, `menuitem.dataset.supportedPlatforms .split(",") .map()`, `platform.trim()`, `shadowRoot.appendChild()`, `supportedPlatforms.includes()`, `this._menuButton.addEventListener()`, `this.attachShadow()`, `this.shadowRoot.querySelector()`, `this.shadowRoot.querySelectorAll()`
- 参照: `menuitem.hidden`, `navigator.platform`, `this._menu`, `this._menuButton`, `this.shadowRoot`

## MenuButton.handleEvent()
- 位置: L34-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classList.contains()`, `this._handleKeyDown()`, `this._hideMenu()`, `this._menu.contains()`, `this._menuButton.contains()`
- 条件付き依存: `if (event.explicitOriginalTarget)` → `node.closest()`
- 条件付き依存: `if (event.originalTarget == this._menuButton)` → `this._toggleMenu()`
- 条件付き依存: `if (!this._menu.hidden)` → `this._menuButton.focus()`
- 条件付き依存: `if (classList.contains("menuitem-button"))` → `document.dispatchEvent()`
- 条件付き依存: `if (classList.contains("menuitem-button"))` → `this._hideMenu()`
- 条件付き依存: `if ( !this._menu.contains(event.originalTarget) && !this._menuButton.contains(event.originalTarget) )` → `this._hideMenu()`
- 参照: `Node.TEXT_NODE`, `document.documentElement`, `event.currentTarget`, `event.explicitOriginalTarget`, `event.originalTarget`, `event.originalTarget.classList`, `event.originalTarget.dataset.eventName`, `event.target`, `event.type`, `node.nodeType`, `node.parentElement`, `this._menu`, `this._menu.hidden`, `this._menuButton`

## MenuButton._handleKeyDown()
- 位置: L101-116
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key == "Enter" && event.originalTarget == this._menuButton)` → `event.preventDefault()`
- 条件付き依存: `if (event.key == "Enter" && event.originalTarget == this._menuButton)` → `this._toggleMenu()`
- 条件付き依存: `if (event.key == "Enter" && event.originalTarget == this._menuButton)` → `this._focusSuccessor()`
- 条件付き依存: `if (event.key == "Escape" && !this._menu.hidden)` → `this._hideMenu()`
- 条件付き依存: `if (event.key == "Escape" && !this._menu.hidden)` → `this._menuButton.focus()`
- 条件付き依存: `if ( (event.key == "ArrowDown" || event.key == "ArrowUp") && !this._menu.hidden )` → `event.preventDefault()`
- 条件付き依存: `if ( (event.key == "ArrowDown" || event.key == "ArrowUp") && !this._menu.hidden )` → `this._focusSuccessor()`
- 参照: `event.key`, `event.originalTarget`, `this._menu.hidden`, `this._menuButton`

## MenuButton._focusSuccessor()
- 位置: L118-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...items].indexOf()`, `this._menu.querySelectorAll()`, `window.AboutLoginsUtils.setFocus()`
- 条件付き依存: `if (this._menu.hidden)` → `this._showMenu()`
- 参照: `items.length`, `successor.disabled`, `this._menu.hidden`, `this._menuButton`, `this.shadowRoot.activeElement`

## MenuButton._hideMenu()
- 位置: L153-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.removeEventListener()`, `this.removeEventListener()`
- 参照: `this._menu.hidden`

## MenuButton._showMenu()
- 位置: L160-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.addEventListener()`, `this.addEventListener()`
- 参照: `this._menu.hidden`

## MenuButton._toggleMenu()
- 位置: L171-178
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (wasHidden)` → `this._showMenu()`
- 条件付き依存: `if (!(wasHidden))` → `this._hideMenu()`
- 参照: `this._menu.hidden`
