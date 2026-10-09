# browser/components/sidebar/sidebar-pins-promo.mjs

source: browser/components/sidebar/sidebar-pins-promo.mjs
source-hash: 53e0248ac459468a0368ff303f4ed0c9e8f4d3c3
lines: 187

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `customElements.define()`

## SidebarPinsPromo.constructor()
- 位置: L40-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`, `this.requestUpdate()`
- 参照: `this.launcherObserver`

## SidebarPinsPromo.connectedCallback()
- 位置: L72-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SidebarManager.addEventListener()`, `lazy.SidebarManager.checkForPinnedTabs()`, `super.connectedCallback()`, `this.addEventListener()`, `this.launcherObserver.observe()`, `window.addEventListener()`
- 参照: `window.SidebarController.sidebarMain`

## SidebarPinsPromo.disconnectedCallback()
- 位置: L85-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SidebarManager.removeEventListener()`, `super.disconnectedCallback()`, `this.launcherObserver.disconnect()`, `this.removeEventListener()`, `window.removeEventListener()`

## SidebarPinsPromo.handleEvent()
- 位置: L100-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.dataTransfer.types.includes()`, `this.card.toggleAttribute()`, `this.dismissDragToPinPromo()`, `this.requestUpdate()`
- 条件付き依存: `if (event.dataTransfer.types.includes(TAB_DROP_TYPE))` → `event.preventDefault()`
- 条件付き依存: `if (event.dataTransfer.types.includes(TAB_DROP_TYPE))` → `this.card.toggleAttribute()`
- 参照: `event.type`

## SidebarPinsPromo.dismissDragToPinPromo()
- 位置: L121-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## SidebarPinsPromo.#iconCellTemplate()
- 位置: L134-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`
- 参照: `icon.name`, `icon.src`

## SidebarPinsPromo.shouldRender()
- 位置: L145-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.SidebarController.sidebarMain.hasAttribute()`
- 参照: `lazy.SidebarManager.checkForPinnedTabsComplete`, `this.dragToPinPromoDismissed`, `this.novaEnabled`, `this.verticalTabsEnabled`

## SidebarPinsPromo.willUpdate()
- 位置: L156-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`
- 参照: `this.shouldRender`

## SidebarPinsPromo.render()
- 位置: L160-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `map()`, `this.#iconCellTemplate()`
- 参照: `this.#icons`, `this.dismissDragToPinPromo`, `this.shouldRender`
