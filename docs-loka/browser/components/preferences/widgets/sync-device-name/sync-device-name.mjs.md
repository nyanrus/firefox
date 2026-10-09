# browser/components/preferences/widgets/sync-device-name/sync-device-name.mjs

source: browser/components/preferences/widgets/sync-device-name/sync-device-name.mjs
source-hash: c8dc90e4413fdcc851e296b1126e68ba392fca34
lines: 142

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SyncDeviceName.constructor()
- 位置: L31-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._isInEditMode`, `this.defaultValue`, `this.disabled`, `this.value`

## SyncDeviceName.setFocus()
- 位置: L47-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `targetEl?.focus()`, `this.updateComplete.then()`
- 参照: `this._isInEditMode`, `this.changeBtnEl`, `this.inputTextEl`

## SyncDeviceName.onDeviceNameChange()
- 位置: L54-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setFocus()`
- 参照: `this._isInEditMode`

## SyncDeviceName.onDeviceNameCancel()
- 位置: L59-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setFocus()`
- 参照: `this._isInEditMode`

## SyncDeviceName.onDeviceNameSave()
- 位置: L64-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`, `this.inputTextEl.value?.trim()`, `this.setFocus()`
- 参照: `this._isInEditMode`, `this.defaultValue`, `this.value`

## SyncDeviceName.onDeviceNameKeyDown()
- 位置: L79-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.onDeviceNameCancel()`, `this.onDeviceNameSave()`
- 参照: `event.key`

## SyncDeviceName.displayDeviceNameTemplate()
- 位置: L92-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.disabled`, `this.onDeviceNameChange`

## SyncDeviceName.editDeviceNameTemplate()
- 位置: L103-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.defaultValue`, `this.onDeviceNameCancel`, `this.onDeviceNameKeyDown`, `this.onDeviceNameSave`, `this.value`

## SyncDeviceName.render()
- 位置: L127-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.displayDeviceNameTemplate()`, `this.editDeviceNameTemplate()`
- 参照: `this._isInEditMode`, `this.defaultValue`, `this.value`
