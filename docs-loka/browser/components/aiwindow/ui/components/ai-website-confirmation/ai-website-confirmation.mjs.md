# browser/components/aiwindow/ui/components/ai-website-confirmation/ai-website-confirmation.mjs

source: browser/components/aiwindow/ui/components/ai-website-confirmation/ai-website-confirmation.mjs
source-hash: 08ed446894a0b17677748116e589885e7ee3daa3
lines: 229

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AIWebsiteConfirmation.constructor()
- 位置: L40-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.actionType`, `this.confirmActionL10n`, `this.tabGroupLabel`, `this.tabs`

## AIWebsiteConfirmation.handleSelectChange()
- 位置: L57-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.dispatchSelectionEvent()`, `this.tabs.map()`
- 参照: `event.detail`, `tab.token`, `this.tabs`

## AIWebsiteConfirmation.handleToggleAll()
- 位置: L72-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabs.every()`
- 条件付き依存: `if (this.tabs.every(tab => tab.checked))` → `this.deselectAll()`
- 条件付き依存: `if (!(this.tabs.every(tab => tab.checked)))` → `this.selectAll()`
- 参照: `tab.checked`

## AIWebsiteConfirmation.selectAll()
- 位置: L83-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchSelectionEvent()`, `this.tabs.map()`
- 参照: `this.tabs`

## AIWebsiteConfirmation.deselectAll()
- 位置: L91-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchSelectionEvent()`, `this.tabs.map()`
- 参照: `this.tabs`

## AIWebsiteConfirmation.getSelectedTabs()
- 位置: L101-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabs.filter()`
- 参照: `tab.checked`

## AIWebsiteConfirmation.handleClose()
- 位置: L108-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.actionType`

## AIWebsiteConfirmation.handleConfirm()
- 位置: L122-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`, `this.getSelectedTabs()`
- 参照: `selectedTabs.length`, `this.tabGroupLabel`

## AIWebsiteConfirmation.dispatchSelectionEvent()
- 位置: L141-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`, `this.getSelectedTabs()`
- 参照: `this.tabs`

## AIWebsiteConfirmation.render()
- 位置: L153-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `ifDefined()`, `this.tabs.every()`, `this.tabs.filter()`, `this.tabs.map()`
- 参照: `tab.checked`, `tab.iconSrc`, `tab.linkedPanel`, `tab.title`, `tab.token`, `tab.url`, `this.confirmActionL10n.disabled`, `this.confirmActionL10n.enabled`, `this.handleClose`, `this.handleConfirm`, `this.handleSelectChange`, `this.handleToggleAll`, `this.tabs.filter(tab => tab.checked).length`, `this.tabs.length`
