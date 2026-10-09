# browser/components/preferences/widgets/setting-control/setting-control.mjs

source: browser/components/preferences/widgets/setting-control/setting-control.mjs
source-hash: e0abfc3c47bf9f1e2943287acb6bfe70db60506c
lines: 546

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`, `literal()`

## SettingNotDefinedError.constructor()
- 位置: L101-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.name`, `this.settingId`

## SettingControl.constructor()
- 位置: L127-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createRef()`, `super()`
- 参照: `this.config`, `this.controlRef`, `this.controlledMessageBarRef`, `this.enableMessageBarRef`, `this.getSetting`, `this.isDisablingExtension`, `this.parentDisabled`, `this.setting`, `this.showEnableExtensionMessage`

## SettingControl.createRenderRoot()
- 位置: L169-171
- 役割: (未記入)
- 触るとき: (未記入)

## SettingControl.focus()
- 位置: L173-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controlEl.focus()`

## SettingControl.controlEl()
- 位置: L177-179
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.controlRef.value`

## SettingControl.disabled()
- 位置: L181-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isDisabledByExtension()`
- 参照: `this.setting?.disabled`, `this.setting?.locked`

## SettingControl.getUpdateComplete()
- 位置: async L189-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.getUpdateComplete()`
- 参照: `this.controlEl?.updateComplete`

## SettingControl.onSettingChange()
- 位置: L195-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`, `this.setValue()`

## SettingControl.willUpdate()
- 位置: L203-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (this.#lastSetting)` → `this.#lastSetting.off()`
- 条件付き依存: `if (changedProperties.has("setting"))` → `this.setValue()`
- 条件付き依存: `if (changedProperties.has("setting"))` → `this.setting.on()`
- 条件付き依存: `if (prevHidden != this.hidden)` → `this.dispatchEvent()`
- 参照: `this.#lastSetting`, `this.config.id`, `this.hidden`, `this.id`, `this.onSettingChange`, `this.setting`, `this.setting.visible`

## SettingControl.updated()
- 位置: L223-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `control.requestUpdate()`
- 参照: `control.checked`, `control.pressed`, `control.value`, `this.controlRef?.value`, `this.value`

## SettingControl.getCommonPropertyMapping()
- 位置: L249-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.getCommonPropertyMapping()`
- 参照: `config.subcategory`, `this.setting`

## SettingControl.getOptionPropertyMapping()
- 位置: L263-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getCommonPropertyMapping()`
- 参照: `config.disabled`, `config.hidden`, `config.value`

## SettingControl.getControlPropertyMapping()
- 位置: L277-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getCommonPropertyMapping()`
- 参照: `config.control`, `this.disabled`, `this.hidden`, `this.parentDisabled`

## SettingControl.getValue()
- 位置: L288-290
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.value`

## SettingControl.setValue()
- 位置: L292-294
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.value`, `this.value`

## SettingControl.controlValue()
- 位置: L300-313
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Cls.activatedProperty`, `el.constructor`, `el.folder`, `el.localName`, `el.value`

## SettingControl.onChange()
- 位置: L320-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controlValue()`, `this.setting.userChange()`

## SettingControl.onClick()
- 位置: L329-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setting.userClick()`

## SettingControl.onMessageBarDismiss()
- 位置: L338-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setting.messageBarDismiss()`

## SettingControl.onReorder()
- 位置: L358-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setting.userReorder()`

## SettingControl.disableExtension()
- 位置: async L362-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setting.disableControllingExtension()`
- 参照: `this.isDisablingExtension`, `this.showEnableExtensionMessage`

## SettingControl.isControlledByExtension()
- 位置: L369-374
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.controllingExtensionInfo?.id`, `this.setting.controllingExtensionInfo?.name`

## SettingControl.isDisabledByExtension()
- 位置: L376-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isControlledByExtension()`
- 参照: `this.setting.controllingExtensionInfo.allowControl`

## SettingControl.handleEnableExtensionDismiss()
- 位置: L383-385
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.showEnableExtensionMessage`

## SettingControl.navigateToAddons()
- 位置: L390-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `link.matches()`
- 条件付き依存: `if (link.matches("a[data-l10n-name='addons-link']"))` → `event.preventDefault()`
- 条件付き依存: `if (link.matches("a[data-l10n-name='addons-link']"))` → `mainWindow.BrowserAddonUI.openAddonsMgr()`
- 参照: `event.target`, `window.browsingContext.topChromeWindow`

## SettingControl.extensionName()
- 位置: L400-402
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.controllingExtensionInfo.name`

## SettingControl.extensionMessageId()
- 位置: L404-406
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.controllingExtensionInfo.l10nId`

## SettingControl.itemsTemplate()
- 位置: L414-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ITEM_SLOT_BY_PARENT.get()`, `config.items.map()`, `html()`, `ifDefined()`, `repeat()`, `this.getSetting()`
- 参照: `config.control`, `config.items`, `i.id`, `item.config`, `item.config.id`, `item.config.key`, `item.config.slot`, `item.setting`, `this.getSetting`

## SettingControl.optionsTemplate()
- 位置: L445-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `KNOWN_OPTIONS.get()`, `repeat()`, `spread()`, `staticHtml()`, `this.getOptionPropertyMapping()`, `this.itemsTemplate()`, `this.optionsTemplate()`, `unsafeStatic()`
- 条件付き依存: `if (opt.control == "a" && opt.controlAttrs?.is == "moz-support-link")` → `html()`
- 参照: `config.control`, `config.options`, `opt.control`, `opt.controlAttrs?.is`, `opt.key`

## SettingControl.extensionSupportPage()
- 位置: L471-473
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.controllingExtensionInfo.supportPage`

## SettingControl.render()
- 位置: L475-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ifDefined()`, `ref()`, `spread()`, `staticHtml()`, `this.getControlPropertyMapping()`, `this.isControlledByExtension()`, `this.itemsTemplate()`, `this.optionsTemplate()`, `this.setting.getControlConfig()`, `unsafeStatic()`
- 条件付き依存: `if (this.isControlledByExtension())` → `html()`
- 条件付き依存: `if (this.isControlledByExtension())` → `ref()`
- 条件付き依存: `if (this.showEnableExtensionMessage)` → `html()`
- 条件付き依存: `if (this.showEnableExtensionMessage)` → `ref()`
- 参照: `config.control`, `this.config`, `this.controlRef`, `this.controlledMessageBarRef`, `this.disableExtension`, `this.enableMessageBarRef`, `this.extensionMessageId`, `this.extensionName`, `this.extensionSupportPage`, `this.handleEnableExtensionDismiss`, `this.isDisablingExtension`, `this.navigateToAddons`, `this.setting.controllingExtensionInfo.mayDisable`, `this.showEnableExtensionMessage`, `this.tabIndex`
