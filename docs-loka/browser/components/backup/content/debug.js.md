# browser/components/backup/content/debug.js

source: browser/components/backup/content/debug.js
source-hash: 5205efce7e023432c1602761891f6a5c8d6a4105
lines: 278

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `DebugUI.init()`, `Preferences.addAll()`, `addEventListener()`

## init()
- 位置: L17-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.init()`, `controls.addEventListener()`, `document.querySelector()`, `encryptionEnabled.addEventListener()`, `service.addEventListener()`, `service.loadEncryptionState()`, `this.onStateUpdate()`

## handleEvent()
- 位置: L34-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HTMLButtonElement.isInstance()`, `this.onStateUpdate()`
- 条件付き依存: `if (HTMLButtonElement.isInstance(event.target))` → `this.onButtonClick()`
- 条件付き依存: `if (!(HTMLButtonElement.isInstance(event.target)))` → `HTMLInputElement.isInstance()`
- 条件付き依存: `if ( HTMLInputElement.isInstance(event.target) && event.target.type == "checkbox" )` → `event.preventDefault()`
- 条件付き依存: `if ( HTMLInputElement.isInstance(event.target) && event.target.type == "checkbox" )` → `this.onCheckboxClick()`
- 参照: `event.target`, `event.target.type`, `event.type`

## secondsToHms()
- 位置: L56-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`

## onButtonClick()
- 位置: async L63-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.get()`, `Cc["@mozilla.org/filepicker;1"].createInstance()`, `ChromeUtils.now()`, `Components.Constructor()`, `IOUtils.exists()`, `IOUtils.getDirectory()`, `PathUtils.join()`, `PathUtils.parent()`, `document.querySelector()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`, `lastRecoveryStatus.textContent()`, `service.createBackup()`, `service.extractCompressedSnapshotFromArchive()`, `service.recoverFromBackupArchive()`, `service.recoverFromSnapshotFolder()`, `service.sampleArchive()`, `this.secondsToHms()`
- 条件付き依存: `if (await IOUtils.exists(backupsDir))` → `new nsLocalFile(backupsDir).reveal()`
- 条件付き依存: `if (!(await IOUtils.exists(backupsDir)))` → `alert()`
- 条件付き依存: `if (isEncrypted)` → `prompt()`
- 参照: `BackupService.PROFILE_FOLDER_NAME`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterHTML`, `Ci.nsIFilePicker.modeGetFolder`, `Ci.nsIFilePicker.modeOpen`, `Ci.nsIFilePicker.returnCancel`, `PathUtils.profileDir`, `button.disabled`, `button.id`, `e.message`, `extractionStatus.textContent`, `fp.displayDirectory`, `fp.file.path`, `lastBackupStatus.textContent`, `lastRecoveryStatus.textContent`, `newProfile.name`, `newProfile.rootDir.path`, `recoverFromArchiveStatus.textContent`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## onCheckboxClick()
- 位置: async L236-256
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (checkbox.id == "encryption-enabled")` → `BackupService.get()`
- 条件付き依存: `if (checkbox.checked)` → `prompt()`
- 条件付き依存: `if (password != null)` → `service.enableEncryption()`
- 条件付き依存: `if (password != null)` → `console.error()`
- 条件付き依存: `if (!(checkbox.checked))` → `confirm()`
- 条件付き依存: `if (confirm("Disable encryption?"))` → `service.disableEncryption()`
- 条件付き依存: `if (confirm("Disable encryption?"))` → `console.error()`
- 参照: `checkbox.checked`, `checkbox.id`

## onStateUpdate()
- 位置: L258-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.get()`, `document.querySelector()`
- 参照: `encryptionEnabled.checked`, `service.state`, `state.encryptionEnabled`
