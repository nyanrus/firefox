# browser/components/preferences/widgets/setting-group/setting-group.mjs

source: browser/components/preferences/widgets/setting-group/setting-group.mjs
source-hash: ec068a4e2a565063a7cc0e1a039d4d8c9afeea42
lines: 317

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `customElements.define()`

## SettingGroup.childControlEls()
- 位置: L77-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...this.fieldsetEl.children].filter()`
- 参照: `this.config`, `this.fieldsetEl.children`

## SettingGroup.constructor()
- 位置: L87-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.config`, `this.getSetting`, `this.inSubPane`, `this.srdEnabled`

## SettingGroup.createRenderRoot()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)

## SettingGroup.connectedCallback()
- 位置: L122-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SettingGroupManager.onRegister()`, `super.connectedCallback()`
- 条件付き依存: `if (id === this.groupId && !this.config)` → `window.initSettingGroup()`
- 参照: `this.#unsubscribeGroupRegister`, `this.config`, `this.groupId`

## SettingGroup.disconnectedCallback()
- 位置: L133-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#unsubscribeGroupRegister()`
- 参照: `this.#unsubscribeGroupRegister`

## SettingGroup.willUpdate()
- 位置: L139-158
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.srdEnabled)` → `this.classList.toggle()`
- 条件付き依存: `if (this.config.hiddenFromSearch)` → `this.setAttribute()`
- 条件付き依存: `if (!(this.config.hiddenFromSearch))` → `this.removeAttribute()`
- 条件付き依存: `if (this.config?.hidden !== undefined)` → `this.toggleAttribute()`
- 条件付き依存: `if (this.config?.subcategory)` → `this.setAttribute()`
- 参照: `HiddenAttr.Search`, `HiddenAttr.Self`, `this.config.hidden`, `this.config.hiddenFromSearch`, `this.config.subcategory`, `this.config?.headingLevel`, `this.config?.hidden`, `this.config?.hiddenFromSearch`, `this.config?.subcategory`, `this.srdEnabled`

## SettingGroup.handleVisibilityChange()
- 位置: async L160-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.childControlEls?.some()`, `this.closest()`
- 条件付き依存: `if (hasVisibleControls)` → `this.hasAttribute()`
- 条件付き依存: `if (this.hasAttribute(HiddenAttr.Self))` → `this.removeAttribute()`
- 条件付き依存: `if (hasVisibleControls)` → `groupbox.hasAttribute()`
- 条件付き依存: `if (groupbox && groupbox.hasAttribute(HiddenAttr.Self))` → `groupbox.removeAttribute()`
- 条件付き依存: `if (!(hasVisibleControls))` → `this.setAttribute()`
- 条件付き依存: `if (!(hasVisibleControls))` → `groupbox.hasAttribute()`
- 条件付き依存: `if (groupbox && !groupbox.hasAttribute(HiddenAttr.Search))` → `groupbox.setAttribute()`
- 参照: `HiddenAttr.Search`, `HiddenAttr.Self`, `el.hidden`, `this.childControlEls?.length`, `this.config?.hidden`, `this.updateComplete`

## SettingGroup.getUpdateComplete()
- 位置: async L192-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `[...this.allControlEls].map()`, `super.getUpdateComplete()`
- 参照: `el.updateComplete`, `this.allControlEls`

## SettingGroup.onChange()
- 位置: L206-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `inputEl.control?.onChange()`
- 参照: `e.target`

## SettingGroup.onClick()
- 位置: L218-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CLICK_HANDLERS.has()`, `inputEl.control?.onClick()`
- 参照: `e.target`, `inputEl.localName`

## SettingGroup.onMessageBarDismiss()
- 位置: L233-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DISMISS_HANDLERS.has()`, `inputEl.control?.onMessageBarDismiss()`
- 参照: `e.target`, `inputEl.localName`

## SettingGroup.onReorder()
- 位置: L257-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `REORDER_HANDLERS.has()`, `inputEl.control?.onReorder()`
- 参照: `e.target`, `inputEl.localName`

## SettingGroup.itemTemplate()
- 位置: L268-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.getSetting()`
- 参照: `item.id`, `this.getSetting`

## SettingGroup.containerTemplate()
- 位置: L280-288
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( (this.srdEnabled || this.inSubPane || this.config.card == "always") && this.config.card != "never" )` → `html()`
- 参照: `this.config.card`, `this.inSubPane`, `this.srdEnabled`

## SettingGroup.render()
- 位置: L290-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `spread()`, `this.config.items.map()`, `this.containerTemplate()`, `this.getCommonPropertyMapping()`, `this.itemTemplate()`
- 参照: `config.headingLevel`, `this.config`, `this.handleVisibilityChange`, `this.onChange`, `this.onClick`, `this.onMessageBarDismiss`, `this.onReorder`, `this.srdEnabled`
