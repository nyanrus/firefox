# browser/components/taskbartabs/TaskbarTabsPin.sys.mjs

source: browser/components/taskbartabs/TaskbarTabsPin.sys.mjs
source-hash: 7f429d2db809455b3102f73acc7e850ec7374291
lines: 299

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## pinTaskbarTab()
- 位置: async L35-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webApp.pin.record()`, `createShortcut()`, `createTaskbarIcon()`, `lazy.TaskbarTabsUtils.isMSIX()`, `lazy.logConsole.error()`, `lazy.logConsole.info()`
- 条件付き依存: `if (AppConstants.platform === "win" && !lazy.TaskbarTabsUtils.isMSIX())` → `lazy.ShellService.pinShortcutToTaskbar()`
- 参照: `AppConstants.platform`, `aTaskbarTab.id`, `e.message`, `e.name`

## unpinTaskbarTab()
- 位置: async L66-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webApp.unpin.record()`, `IOUtils.remove()`, `Promise.all()`, `Promise.resolve()`, `getIconFile()`, `lazy.TaskbarTabsUtils.isMSIX()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `lazy.logConsole.info()`, `message()`
- 条件付き依存: `if (AppConstants.platform === "win" && !isMSIX)` → `lazy.ShellService.unpinShortcutFromTaskbar()`
- 条件付き依存: `if (relativePath && AppConstants.platform === "win" && !isMSIX)` → `lazy.ShellService.deleteShortcut()`
- 条件付き依存: `if (relativePath && AppConstants.platform === "win" && isMSIX)` → `lazy.ShellService.requestDeleteSecondaryTile()`
- 条件付き依存: `if (relativePath && AppConstants.platform === "linux")` → `lazy.ShellService.deleteLinuxDesktopEntry()`
- 条件付き依存: `if (relativePath && AppConstants.platform === "linux")` → `relativePath.replace()`
- 参照: `AppConstants.platform`, `aTaskbarTab.shortcutRelativePath`, `e.message`, `iconFile.path`

## message()
- 位置: L113-113
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `e.name`

## _getLocalization()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)

## createTaskbarIcon()
- 位置: async L138-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.makeDirectory()`, `getIconFile()`, `lazy.ShellService.writeShortcutIcon()`, `lazy.logConsole.debug()`, `lazy.logConsole.info()`
- 参照: `iconFile.parent.path`, `iconFile.path`

## createShortcut()
- 位置: async L162-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `aTaskbarTab.userContextId.toString()`, `lazy.TaskbarTabsUtils.isMSIX()`, `lazy.logConsole.info()`
- 条件付き依存: `if (AppConstants.platform === "win" && lazy.TaskbarTabsUtils.isMSIX())` → `lazy.ShellService.requestCreateAndPinSecondaryTile()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `generateShortcutInfo()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `lazy.logConsole.debug()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `lazy.ShellService.createShortcut()`
- 条件付き依存: `if (AppConstants.platform === "linux")` → `lazy.TaskbarTabsUtils._determineNewDesktopEntryName()`
- 条件付き依存: `if (AppConstants.platform === "linux")` → `lazy.ShellService.createLinuxDesktopEntry()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `aFileIcon.path`, `aTaskbarTab.id`, `aTaskbarTab.name`, `aTaskbarTab.startUrl`, `profileFolder.path`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## generateShortcutInfo()
- 位置: async L239-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TaskbarTabsPin._getLocalization()`, `l10n.formatValue()`, `sanitizeFilename()`
- 参照: `aTaskbarTab.name`

## sanitizeFilename()
- 位置: L269-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/mime;1"].getService()`, `mimeService.validateFileNameForSaving()`
- 参照: `Ci.nsIMIMEService`, `Ci.nsIMIMEService.VALIDATE_ALLOW_DIRECTORY_NAMES`, `Ci.nsIMIMEService.VALIDATE_ALLOW_INVALID_FILENAMES`, `Ci.nsIMIMEService.VALIDATE_DONT_COLLAPSE_WHITESPACE`, `Ci.nsIMIMEService.VALIDATE_SANITIZE_ONLY`
- XPCOM: [`nsIMIMEService`](../../../netwerk/mime/nsIMIMEService.idl.md) / `@mozilla.org/mime;1`

## getIconFile()
- 位置: L291-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `iconPath.append()`, `lazy.TaskbarTabsUtils.getTaskbarTabsFolder()`
- 参照: `aTaskbarTab.id`, `lazy.ShellService.shortcutIconType.extension`
