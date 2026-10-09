# browser/components/contextualidentity/content/ContainerEditor.mjs

source: browser/components/contextualidentity/content/ContainerEditor.mjs
source-hash: 7d789c2a1d9b12e875ed0fa638036dd85d8827b4
lines: 143

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ContainerEditor.constructor()
- 位置: L30-39
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `host.ownerDocument`, `lazy.ContextualIdentityService.containerColors`, `lazy.ContextualIdentityService.containerIcons`, `this.document`, `this.host`, `this.identity`, `this.userContextId`

## ContainerEditor.render()
- 位置: L41-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createElementNS()`, `doc.defaultView.MozXULElement.insertFTLIfNeeded()`, `doc.l10n.setAttributes()`, `lazy.ContextualIdentityService.getContainerColorLabel()`, `lazy.ContextualIdentityService.getContainerIconLabel()`, `this._buildSwatches()`, `this._colorPicker.classList.add()`, `this._createPicker()`, `this._iconPicker.classList.add()`, `this._name.setAttribute()`, `this.form.append()`, `this.host.append()`
- 参照: `lazy.ContextualIdentityService.containerColors`, `lazy.ContextualIdentityService.containerIcons`, `this._colorPicker`, `this._iconPicker`, `this._name`, `this._name.value`, `this.document`, `this.form`, `this.form.className`, `this.identity.color`, `this.identity.icon`, `this.identity.name`

## ContainerEditor._createPicker()
- 位置: L80-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `picker.classList.add()`, `picker.setAttribute()`, `this.document.createElementNS()`, `this.document.l10n.setAttributes()`

## ContainerEditor._buildSwatches()
- 位置: L89-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createElementNS()`, `getLabel()`, `iconClass()`, `item.append()`, `picker.append()`
- 参照: `icon.className`, `item.ariaLabel`, `item.className`, `item.title`, `item.value`, `picker.value`, `this.document`

## ContainerEditor.focus()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._name.focus()`

## ContainerEditor.isValid()
- 位置: L114-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._name.value.trim()`

## ContainerEditor.commit()
- 位置: L118-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formData.get()`, `formData.get("name").trim()`, `lazy.ContextualIdentityService.getContainerColorCode()`, `lazy.ContextualIdentityService.getContainerIconURL()`
- 条件付き依存: `if (this.userContextId)` → `lazy.ContextualIdentityService.update()`
- 条件付き依存: `if (!(this.userContextId))` → `lazy.ContextualIdentityService.create()`
- 参照: `this.form`, `this.userContextId`
