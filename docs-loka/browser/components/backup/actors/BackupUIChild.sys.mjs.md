# browser/components/backup/actors/BackupUIChild.sys.mjs

source: browser/components/backup/actors/BackupUIChild.sys.mjs
source-hash: 50f7d5aeabbaa946db53d740dabbb255c74530c3
lines: 231

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## BackupUIChild.#findWidget()
- 位置: L33-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`
- 参照: `this.#inittedWidgets`, `widget.isConnected`, `widget.nodeName`

## BackupUIChild.handleEvent()
- 位置: async L52-197
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "BackupUI:InitWidget")` → `this.#inittedWidgets.add()`
- 条件付き依存: `if (event.type == "BackupUI:InitWidget")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:TriggerCreateBackup")` → `this.sendQuery()`
- 条件付き依存: `if (event.type == "BackupUI:EnableScheduledBackups")` → `this.sendQuery()`
- 条件付き依存: `if (result.success)` → `target.close()`
- 条件付き依存: `if (event.type == "BackupUI:DisableScheduledBackups")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:DisableScheduledBackups")` → `target.close()`
- 条件付き依存: `if (event.type == "BackupUI:ShowFilepicker")` → `this.sendQuery()`
- 条件付き依存: `if (event.type == "BackupUI:ShowFilepicker")` → `this.#findWidget()`
- 条件付き依存: `if (widget)` → `Cu.cloneInto()`
- 条件付き依存: `if (widget)` → `widget.dispatchEvent()`
- 条件付き依存: `if (event.type == "BackupUI:GetBackupFileInfo")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:RestoreFromBackupFile")` → `this.sendQuery()`
- 条件付き依存: `if (result.success)` → `event.target.restoreFromBackupDialogEl?.close()`
- 条件付き依存: `if (result.success)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:RestoreFromBackupChooseFile")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:EnableEncryption")` → `this.sendQuery()`
- 条件付き依存: `if (event.type == "BackupUI:DisableEncryption")` → `this.sendQuery()`
- 条件付き依存: `if (event.type == "BackupUI:ShowBackupLocation")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:SetEmbeddedComponentPersistentData")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:FlushEmbeddedComponentPersistentData")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:ErrorBarDismissed")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:FindBackupsInWellKnownLocations")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "BackupUI:ProbeDefaultBackupDir")` → `this.sendQuery()`
- 条件付き依存: `if (event.type == "BackupUI:ProbeDefaultBackupDir")` → `lazy.logConsole.error()`
- 条件付き依存: `if (event.type == "BackupUI:ProbeDefaultBackupDir")` → `this.#findWidget()`
- 条件付き依存: `if (event.type == "BackupUI:PrepareRestoreDialog")` → `this.sendQuery()`
- 条件付き依存: `if (event.type == "BackupUI:PrepareRestoreDialog")` → `lazy.logConsole.error()`
- 条件付き依存: `if (event.type == "BackupUI:PrepareRestoreDialog")` → `this.#findWidget()`
- 参照: `event.composedTarget.nodeName`, `event.detail`, `event.detail?.alsoDeleteLastBackup`, `event.detail?.existingBackupPath`, `event.detail?.filter`, `event.detail?.win`, `event.target`, `event.target.backupErrorCode`, `event.type`, `result.errorCode`, `result.success`, `target.disableEncryptionErrorCode`, `target.enableBackupErrorCode`, `target.enableEncryptionErrorCode`, `widget.documentGlobal`, `widget.documentGlobal.CustomEvent`, `win.CustomEvent`

## BackupUIChild.receiveMessage()
- 位置: L205-229
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.name == "StateUpdate")` → `ChromeUtils.nondeterministicGetWeakSetKeys()`
- 条件付き依存: `if (message.name == "StateUpdate")` → `Cu.cloneInto()`
- 条件付き依存: `if (message.name == "StateUpdate")` → `Cu.waiveXrays()`
- 条件付き依存: `if (message.name == "StateUpdate")` → `widget.dispatchEvent()`
- 参照: `message.data.state`, `message.name`, `this.#inittedWidgets`, `this.contentWindow.CustomEvent`, `waivedWidget.backupServiceState`, `widget.documentGlobal`, `widget.isConnected`
