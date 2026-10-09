# browser/components/sidebar/sidebar-opentabs-preview.mjs

source: browser/components/sidebar/sidebar-opentabs-preview.mjs
source-hash: 942309628920115f928d96f9801f5853e66a37c0
lines: 312

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `customElements.define()`

## SidebarOpenTabsPreview.constructor()
- 位置: L42-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`
- 参照: `lazy.OpenTabsController`, `this.controller`, `this.tabItems`

## SidebarOpenTabsPreview.connectedCallback()
- 位置: L60-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addEventListener()`, `this.closest()`, `this.panel.addEventListener()`
- 参照: `this.panel`

## SidebarOpenTabsPreview.disconnectedCallback()
- 位置: L68-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#clearTimers()`, `this._openTabsTarget?.removeEventListener()`, `this.panel.removeEventListener()`, `this.removeEventListener()`

## SidebarOpenTabsPreview.openTabsTarget()
- 位置: L77-84
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._openTabsTarget)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!this._openTabsTarget)` → `lazy.getTabsTargetForWindow()`
- 参照: `lazy.NonPrivateTabs`, `this._openTabsTarget`

## SidebarOpenTabsPreview.handleEvent()
- 位置: L86-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateTabItems()`, `this._openTabsTarget?.removeEventListener()`, `this.contains()`
- 条件付き依存: `if (!this.contains(e.relatedTarget))` → `this.#clearHideTimer()`
- 条件付き依存: `if (!this.contains(e.relatedTarget))` → `this.deactivate()`
- 参照: `e.relatedTarget`, `e.type`

## SidebarOpenTabsPreview.activate()
- 位置: L113-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this.#clearHideTimer()`, `this.#show()`
- 参照: `this._showTimer`, `this.hoverPreviewEnabled`, `this.panel.state`, `this.showDelayMs`

## SidebarOpenTabsPreview.deactivate()
- 位置: L127-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this.#clearShowTimer()`, `this.panel.hidePopup()`
- 参照: `this._hideTimer`, `this.panel.state`

## SidebarOpenTabsPreview.hide()
- 位置: L138-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearTimers()`, `this.panel.hidePopup()`

## SidebarOpenTabsPreview.#show()
- 位置: async L143-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchor.shadowRoot.querySelector()`, `this.#updateTabItems()`, `this.openTabsTarget.addEventListener()`, `this.panel.openPopup()`
- 参照: `this.tabItems.length`, `this.updateComplete`

## SidebarOpenTabsPreview.#clearShowTimer()
- 位置: L156-161
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._showTimer)` → `clearTimeout()`
- 参照: `this._showTimer`

## SidebarOpenTabsPreview.#clearHideTimer()
- 位置: L163-168
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._hideTimer)` → `clearTimeout()`
- 参照: `this._hideTimer`

## SidebarOpenTabsPreview.#clearTimers()
- 位置: L170-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearHideTimer()`, `this.#clearShowTimer()`

## SidebarOpenTabsPreview.#hasAudio()
- 位置: L175-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.indicators?.includes()`

## SidebarOpenTabsPreview.#isMuted()
- 位置: L182-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.indicators?.includes()`

## SidebarOpenTabsPreview.#updateTabItems()
- 位置: L186-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.filter()`, `this.#hasAudio()`, `this.controller.getTabListItems()`, `this.openTabsTarget.getRecentTabs()`, `this.openTabsTarget.getRecentTabs().slice()`
- 参照: `this.tabItems`

## SidebarOpenTabsPreview.#getIconSrc()
- 位置: L195-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `icon.startsWith()`

## SidebarOpenTabsPreview.#activateTab()
- 位置: L210-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.focus()`, `this.hide()`
- 参照: `browserWindow.gBrowser.selectedTab`, `tabElement.documentGlobal`

## SidebarOpenTabsPreview.#closeTab()
- 位置: L221-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.stopPropagation()`, `tabElement?.documentGlobal.gBrowser.removeTabs()`

## SidebarOpenTabsPreview.#showAll()
- 位置: L227-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hide()`, `window.SidebarController.show()`

## SidebarOpenTabsPreview.#audioButtonTemplate()
- 位置: L232-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#hasAudio()`, `this.#isMuted()`, `this.#toggleAudio()`, `when()`

## SidebarOpenTabsPreview.#toggleAudio()
- 位置: L253-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `e.stopPropagation()`, `item.tabElement?.toggleMuteAudio()`

## SidebarOpenTabsPreview.#rowTemplate()
- 位置: L259-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#activateTab()`, `this.#audioButtonTemplate()`, `this.#closeTab()`, `this.#getIconSrc()`
- 参照: `item.title`

## SidebarOpenTabsPreview.render()
- 位置: L288-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#rowTemplate()`, `this.#showAll()`, `this.tabItems.map()`
