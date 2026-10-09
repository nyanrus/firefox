# browser/components/contextualidentity/content/container-select.mjs

source: browser/components/contextualidentity/content/container-select.mjs
source-hash: 313bfdcd8edc1dcf04b45da919a797173507e05c
lines: 144

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`, `this.populateOptions()`

## containerOptions()
- 位置: L21-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `lazy.ContextualIdentityService.getContainerIconURL()`, `lazy.ContextualIdentityService.getPublicIdentities()`, `lazy.ContextualIdentityService.getPublicIdentities().map()`, `lazy.ContextualIdentityService.getUserContextLabel()`
- 参照: `identity.color`, `identity.icon`, `identity.userContextId`

## ContainerSelect.constructor()
- 位置: L49-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.#bindSite()`, `this.addEventListener()`
- 参照: `this.site`

## ContainerSelect.firstUpdated()
- 位置: L58-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.firstUpdated()`, `this.#colorObserver.observe()`

## ContainerSelect.inputStylesTemplate()
- 位置: L69-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `super.inputStylesTemplate()`

## ContainerSelect.populateOptions()
- 位置: L84-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["moz-option", "hr"].includes()`, `nodes?.[index]?.getAttribute()`, `super.populateOptions()`, `this.options.map()`, `this.slotRef.value ?.assignedNodes()`, `this.slotRef.value ?.assignedNodes() .filter()`
- 参照: `node.localName`, `this.options`

## ContainerSelect.willUpdate()
- 位置: L98-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cls.startsWith()`, `super.willUpdate()`
- 条件付き依存: `if (cls.startsWith("identity-color-"))` → `this.classList.remove()`
- 条件付き依存: `if (this.selectedOption?.itemClass)` → `this.classList.add()`
- 参照: `this.classList`, `this.selectedOption.itemClass`, `this.selectedOption?.itemClass`

## ContainerSelect.updated()
- 位置: L118-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[ ...(this.panelList?.querySelectorAll("panel-item") ?? []), ].entries()`, `[...item.classList].filter()`, `cls.startsWith()`, `item.classList.remove()`, `super.updated()`, `this.panelList?.querySelectorAll()`
- 条件付き依存: `if (this.options[index]?.itemClass)` → `item.classList.add()`
- 参照: `item.classList`, `this.options`, `this.options[index].itemClass`, `this.options[index]?.itemClass`

## ContainerSelect.#bindSite()
- 位置: L132-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`
- 条件付き依存: `if (this.site && userContextId)` → `lazy.ContextualIdentityService.setSiteAssociation()`
- 参照: `this.site`, `this.value`
