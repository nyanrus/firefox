# browser/components/profiles/SelectableProfile.sys.mjs

source: browser/components/profiles/SelectableProfile.sys.mjs
source-hash: 9ecda4990e2f2d8769108d2ce8ba235296c196f7
lines: 779

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`

## standardAvatarURL()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)

## resolveDir()
- 位置: L64-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.splitRelative()`
- 条件付き依存: `if (pathPart === "..")` → `PathUtils.parent()`
- 条件付き依存: `if (!(pathPart === ".."))` → `PathUtils.join()`
- 参照: `AppConstants.platform`

## SelectableProfile.constructor()
- 位置: L121-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.getResultByName()`
- 参照: `this.#avatar`, `this.#id`, `this.#name`, `this.#path`, `this.#themeBg`, `this.#themeFg`, `this.#themeId`

## SelectableProfile.id()
- 位置: L136-138
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#id`

## SelectableProfile.name()
- 位置: L147-149
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#name`

## SelectableProfile.name()
- 位置: L157-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setNameAsync()`

## SelectableProfile.setNameAsync()
- 位置: async L167-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectableProfileService.updateProfile()`, `Services.prefs.setBoolPref()`
- 参照: `this.#name`
- XPCOM: `Services.prefs`

## SelectableProfile.path()
- 位置: L178-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.constructor.getDirectory()`, `resolveDir()`
- 参照: `ProfilesDatastoreService.constructor.getDirectory("UAppData").path`, `this.#path`

## SelectableProfile.rootDir()
- 位置: L191-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getDirectory()`
- 参照: `this.path`

## SelectableProfile.localDir()
- 位置: L201-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.toolkitProfileService.getLocalDirFromRootDir()`, `this.rootDir.then()`

## SelectableProfile.avatar()
- 位置: L214-216
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#avatar`

## SelectableProfile.getAvatarPath()
- 位置: L228-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`
- 条件付き依存: `if (!this.hasCustomAvatar)` → `standardAvatarURL()`
- 参照: `ProfilesDatastoreService.constructor.PROFILE_GROUPS_DIR`, `this.avatar`, `this.hasCustomAvatar`

## SelectableProfile.getAvatarURL()
- 位置: async L251-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `File.createFromFileName()`, `IOUtils.exists()`, `URL.createObjectURL()`, `this.getAvatarPath()`
- 条件付き依存: `if (!this.hasCustomAvatar)` → `standardAvatarURL()`
- 条件付き依存: `if (this.#lastAvatarURL)` → `URL.revokeObjectURL()`
- 条件付き依存: `if (!fileExists)` → `Glean.profilesError.avatar.record()`
- 条件付き依存: `if (!fileExists)` → `this.setAvatar()`
- 条件付き依存: `if (!fileExists)` → `standardAvatarURL()`
- 参照: `this.#lastAvatarURL`, `this.avatar`, `this.hasCustomAvatar`

## SelectableProfile.getAvatarFile()
- 位置: async L279-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `File.createFromFileName()`, `this.getAvatarPath()`
- 参照: `this.hasCustomAvatar`

## SelectableProfile.hasCustomAvatar()
- 位置: L289-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `STANDARD_AVATARS.has()`
- 参照: `this.avatar`

## SelectableProfile.setAvatar()
- 位置: async L299-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.saveUpdatesToDB()`
- 条件付き依存: `if (!(aAvatarOrFile === this.avatar))` → `STANDARD_AVATARS.has()`
- 条件付き依存: `if (!(STANDARD_AVATARS.has(aAvatarOrFile)))` → `this.#uploadCustomAvatar()`
- 参照: `this.#avatar`, `this.avatar`

## SelectableProfile.#uploadCustomAvatar()
- 位置: async L313-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.makeDirectory()`, `IOUtils.write()`, `PathUtils.join()`, `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `Services.uuid.generateUUID().toString().slice()`, `file.arrayBuffer()`
- 参照: `ProfilesDatastoreService.constructor.PROFILE_GROUPS_DIR`, `this.#avatar`
- XPCOM: `Services.uuid`

## SelectableProfile.avatarL10nId()
- 位置: L339-400
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.avatar`

## SelectableProfile.theme()
- 位置: L411-417
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#themeBg`, `this.#themeFg`, `this.#themeId`

## SelectableProfile.iconPaintContext()
- 位置: L419-426
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#themeBg`, `this.#themeFg`

## SelectableProfile.theme()
- 位置: L437-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setThemeAsync()`

## SelectableProfile.setThemeAsync()
- 位置: async L450-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectableProfileService.updateProfile()`
- 参照: `this.#themeBg`, `this.#themeFg`, `this.#themeId`

## SelectableProfile.saveUpdatesToDB()
- 位置: L458-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectableProfileService.updateProfile()`

## SelectableProfile.toDbObject()
- 位置: L467-477
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#path`, `this.avatar`, `this.id`, `this.name`, `this.theme`

## SelectableProfile.toContentSafeObject()
- 位置: async L486-531
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.hasCustomAvatar)` → `this.getAvatarPath()`
- 条件付き依存: `if (this.hasCustomAvatar)` → `this.getAvatarFile()`
- 条件付き依存: `if (this.hasCustomAvatar)` → `Object.fromEntries()`
- 条件付き依存: `if (this.hasCustomAvatar)` → `STANDARD_AVATAR_SIZES.map()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `Object.fromEntries()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `STANDARD_AVATAR_SIZES.map()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `this.getAvatarPath()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `Promise.all()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `this.getAvatarURL()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `fetch()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `response.text()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `faviconSVGText .replaceAll("context-fill", profileObj.themeBg) .replaceAll()`
- 条件付き依存: `if (!(this.hasCustomAvatar))` → `faviconSVGText .replaceAll()`
- 参照: `profileObj.avatarFiles`, `profileObj.avatarPaths`, `profileObj.avatarURLs`, `profileObj.avatarURLs.url16`, `profileObj.faviconSVGText`, `profileObj.themeBg`, `profileObj.themeFg`, `this.#path`, `this.avatar`, `this.avatarL10nId`, `this.hasCustomAvatar`, `this.id`, `this.name`, `this.theme`

## SelectableProfile.copyProfile()
- 位置: async L533-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ArchiveEncryptionState.initialize()`, `Services.prefs.clearUserPref()`, `Services.prefs.setBoolPref()`, `backupServiceInstance.createAndPopulateStagingFolder()`, `backupServiceInstance.recoverFromSnapshotFolderIntoSelectableProfile()`, `copiedProfile.setAvatar()`
- 参照: `copiedProfile.theme`, `result.error`, `result.stagingPath`, `this.avatar`, `this.path`, `this.theme`
- XPCOM: `Services.prefs`

## SelectableProfile.getWindowsShellService()
- 位置: L582-589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/browser/shell-service;1"].getService()`
- 参照: `AppConstants.platform`, `Ci.nsIWindowsShellService`
- XPCOM: [`nsIWindowsShellService`](../shell/nsIWindowsShellService.idl.md) / `@mozilla.org/browser/shell-service;1`

## SelectableProfile.ensureDesktopShortcut()
- 位置: async L598-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getDesktopShortcut()`, `this.hasDesktopShortcut()`
- 条件付き依存: `if (!this.hasDesktopShortcut())` → `this.getSafeDesktopShortcutFileName()`
- 条件付き依存: `if (!this.hasDesktopShortcut())` → `Services.dirsvc.get()`
- 条件付き依存: `if (!this.hasDesktopShortcut())` → `this.getWindowsShellService()`
- 条件付き依存: `if (!this.hasDesktopShortcut())` → `shellService.createShortcut()`
- 条件付き依存: `if (!this.hasDesktopShortcut())` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (!this.hasDesktopShortcut())` → `console.error()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `this.name`, `this.path`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc` / `Services.prefs`

## SelectableProfile.removeDesktopShortcut()
- 位置: async L646-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.getCharPref()`, `console.error()`, `shellService.deleteShortcut()`, `this.getWindowsShellService()`, `this.hasDesktopShortcut()`
- XPCOM: `Services.prefs`

## SelectableProfile.getDesktopShortcut()
- 位置: L675-700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `Services.dirsvc.get()`, `Services.prefs.getCharPref()`, `console.error()`, `file?.exists()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `FileUtils.File`, `Services.dirsvc.get("Desk", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc` / `Services.prefs`

## SelectableProfile.hasDesktopShortcut()
- 位置: L708-711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getDesktopShortcut()`

## SelectableProfile.getSafeDesktopShortcutFileName()
- 位置: async L723-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadPaths.createNiceUniqueFile()`, `DownloadPaths.sanitize()`, `IOUtils.remove()`, `PathUtils.join()`, `Services.dirsvc.get()`, `Services.prefs.getCharPref()`, `console.error()`, `fileName.substring()`
- 条件付き依存: `if (!fileName)` → `lazy.localization.formatMessages()`
- 参照: `Ci.nsIFile`, `FileUtils.File`, `desktopFile.path`, `desktopFile.path.length`, `strings[0].value`, `this.name`, `uniqueShortcutFile.leafName`, `uniqueShortcutFile.path`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc` / `Services.prefs`
