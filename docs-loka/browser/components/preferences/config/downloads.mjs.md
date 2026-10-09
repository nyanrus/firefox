# browser/components/preferences/config/downloads.mjs

source: browser/components/preferences/config/downloads.mjs
source-hash: e1aaacd21b6ee033bc9c2f0bd8f8ad6a41214cce
lines: 1882

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/handler-service;1" ].getService()`, `Cc["@mozilla.org/mime;1"].getService()`, `ChromeUtils.importESModule()`, `Integration.downloads.defineESModuleGetter()`, `Preferences.addAll()`, `Preferences.addSetting()`, `SettingGroupManager.registerGroups()`

## DownloadsHelpers.setupDownloadsHelpersFields()
- 位置: async L124-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatValues()`, `this._getDownloadsFolder()`
- 参照: `this.desktopDir`, `this.desktopFolderLocalizedName`, `this.downloadsDir`, `this.downloadsFolderLocalizedName`

## DownloadsHelpers._getDownloadsFolder()
- 位置: async L143-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Downloads.getSystemDownloadsDirectory()`, `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `FileUtils.File`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `Services.dirsvc`

## DownloadsHelpers._getSystemDownloadFolderDetails()
- 位置: L157-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`
- 条件付き依存: `if (folderIndex == 2 && currentDirPref.value)` → `file.equals()`
- 条件付き依存: `if (!(file.equals(this.downloadsDir)))` → `file.equals()`
- 条件付き依存: `if (displayName != this.folderPath)` → `file.hostPath().then()`
- 条件付き依存: `if (displayName != this.folderPath)` → `file.hostPath()`
- 条件付き依存: `if (displayName != this.folderPath)` → `Preferences.getSetting("downloadFolder")?.onChange()`
- 条件付き依存: `if (displayName != this.folderPath)` → `Preferences.getSetting()`
- 参照: `AppConstants.platform`, `currentDirPref.value`, `file.displayName`, `file.leafName`, `file.path`, `this.desktopDir`, `this.desktopDir.path`, `this.desktopFolderLocalizedName`, `this.downloadsDir`, `this.downloadsDir.path`, `this.downloadsFolderLocalizedName`, `this.folderHostPath`, `this.folderPath`

## DownloadsHelpers._folderToIndex()
- 位置: L270-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aFolder.equals()`
- 条件付き依存: `if (!(!aFolder || aFolder.equals(this.desktopDir)))` → `aFolder.equals()`
- 参照: `this.desktopDir`, `this.downloadsDir`

## DownloadsHelpers.getFolderDetails()
- 位置: L279-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `this._getSystemDownloadFolderDetails()`
- 参照: `Preferences.get("browser.download.folderList").value`, `file?.path`, `this.displayName`, `this.folderPath`

## DownloadsHelpers.setFolder()
- 位置: L288-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `this._folderToIndex()`
- 参照: `folderListPref.value`, `this.folder`

## get()
- 位置: L304-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsHelpers.getFolderDetails()`
- 参照: `DownloadsHelpers.folderPath`

## set()
- 位置: L308-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsHelpers.setFolder()`
- 参照: `DownloadsHelpers.folder`

## getControlConfig()
- 位置: L312-325
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `DownloadsHelpers.displayName`, `config.controlAttrs`

## setup()
- 位置: L326-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsHelpers.setupDownloadsHelpersFields()`, `DownloadsHelpers.setupDownloadsHelpersFields().then()`

## disabled()
- 位置: L329-331
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `browserDownloadFolderList.locked`

## setup()
- 位置: L340-368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`, `window.addEventListener()`, `window.removeEventListener()`

## appInitializer()
- 位置: async L346-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ApplicationsHandler.preInitApplications()`, `Services.obs.notifyObservers()`, `window.removeEventListener()`
- 参照: `event.detail.category`
- XPCOM: `Services.obs`

## get()
- 位置: L377-379
- 役割: (未記入)
- 触るとき: (未記入)

## visible()
- 位置: L395-395
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `enableDeletePrivate.value`

## onUserChange()
- 位置: L396-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## HandlerInfoWrapper.constructor()
- 位置: L428-432
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.disambiguateDescription`, `this.type`, `this.wrappedHandlerInfo`

## HandlerInfoWrapper.description()
- 位置: L434-445
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.primaryExtension)` → `this.primaryExtension.toUpperCase()`
- 参照: `this.primaryExtension`, `this.type`, `this.wrappedHandlerInfo.description`

## HandlerInfoWrapper.typeDescription()
- 位置: L454-477
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `args.type`, `description.id`, `description.raw`, `this.description`, `this.disambiguateDescription`, `this.type`

## HandlerInfoWrapper.actionIconClass()
- 位置: L479-496
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIHandlerInfo.handleInternally`, `Ci.nsIHandlerInfo.saveToDisk`, `this.alwaysAskBeforeHandling`, `this.preferredAction`
- XPCOM: [`nsIHandlerInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## HandlerInfoWrapper.actionIconSrcset()
- 位置: L498-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `icon.startsWith()`, `srcset.join()`, `srcset.push()`
- 参照: `this.actionIcon`

## HandlerInfoWrapper.actionIcon()
- 位置: L512-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ApplicationsHandler.isValidHandlerApp()`
- 条件付き依存: `if (ApplicationsHandler.isValidHandlerApp(preferredApp))` → `getIconURLForHandlerApp()`
- 参照: `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIHandlerInfo.useSystemDefault`, `this.iconURLForSystemDefault`, `this.preferredAction`, `this.preferredApplicationHandler`
- XPCOM: [`nsIHandlerInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## HandlerInfoWrapper.iconURLForSystemDefault()
- 位置: L531-553
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( this.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo && this.wrappedHandlerInfo instanceof Ci.nsIPropertyBag )` → `this.wrappedHandlerInfo.getProperty()`
- 参照: `Ci.nsIMIMEInfo`, `Ci.nsIPropertyBag`, `this.wrappedHandlerInfo`
- XPCOM: [`nsIMIMEInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIPropertyBag`](../../../../toolkit/components/passwordmgr/nsILoginManager.idl.md)

## HandlerInfoWrapper.preferredApplicationHandler()
- 位置: L558-560
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.wrappedHandlerInfo.preferredApplicationHandler`

## HandlerInfoWrapper.preferredApplicationHandler()
- 位置: L562-569
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNewValue)` → `this.addPossibleApplicationHandler()`
- 参照: `this.wrappedHandlerInfo.preferredApplicationHandler`

## HandlerInfoWrapper.possibleApplicationHandlers()
- 位置: L571-573
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.wrappedHandlerInfo.possibleApplicationHandlers`

## HandlerInfoWrapper.addPossibleApplicationHandler()
- 位置: L579-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `app.equals()`, `this.possibleApplicationHandlers.appendElement()`, `this.possibleApplicationHandlers.enumerate()`

## HandlerInfoWrapper.removePossibleApplicationHandler()
- 位置: L592-609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aHandler.equals()`, `handler.equals()`, `handlers.queryElementAt()`
- 条件付き依存: `if (handler.equals(aHandler))` → `handlers.removeElementAt()`
- 参照: `Ci.nsIHandlerApp`, `handlers.length`, `this.alwaysAskBeforeHandling`, `this.possibleApplicationHandlers`, `this.preferredApplicationHandler`
- XPCOM: [`nsIHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## HandlerInfoWrapper.hasDefaultHandler()
- 位置: L611-613
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.wrappedHandlerInfo.hasDefaultHandler`

## HandlerInfoWrapper.defaultDescription()
- 位置: L615-617
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.wrappedHandlerInfo.defaultDescription`

## HandlerInfoWrapper.preferredAction()
- 位置: L620-639
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ApplicationsHandler.isValidHandlerApp()`
- 参照: `Ci.nsIHandlerInfo.saveToDisk`, `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIHandlerInfo.useSystemDefault`, `this.preferredApplicationHandler`, `this.wrappedHandlerInfo.hasDefaultHandler`, `this.wrappedHandlerInfo.preferredAction`
- XPCOM: [`nsIHandlerInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## HandlerInfoWrapper.preferredAction()
- 位置: L641-643
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.wrappedHandlerInfo.preferredAction`

## HandlerInfoWrapper.alwaysAskBeforeHandling()
- 位置: L645-660
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIHandlerInfo.saveToDisk`, `Ci.nsIMIMEInfo`, `this.preferredAction`, `this.wrappedHandlerInfo`, `this.wrappedHandlerInfo.alwaysAskBeforeHandling`
- XPCOM: [`nsIHandlerInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIMIMEInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## HandlerInfoWrapper.alwaysAskBeforeHandling()
- 位置: L662-664
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.wrappedHandlerInfo.alwaysAskBeforeHandling`

## HandlerInfoWrapper.primaryExtension()
- 位置: L667-678
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIMIMEInfo`, `this.wrappedHandlerInfo`, `this.wrappedHandlerInfo.primaryExtension`
- XPCOM: [`nsIMIMEInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## HandlerInfoWrapper.store()
- 位置: L680-682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gHandlerService.store()`
- 参照: `this.wrappedHandlerInfo`

## HandlerInfoWrapper.iconSrcSet()
- 位置: L684-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `srcset.join()`, `srcset.push()`, `this._getIcon()`

## HandlerInfoWrapper._getIcon()
- 位置: L701-713
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIMIMEInfo`, `this.primaryExtension`, `this.type`, `this.wrappedHandlerInfo`
- XPCOM: [`nsIMIMEInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## InternalHandlerInfoWrapper.constructor()
- 位置: L722-725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMIMEService.getFromTypeAndExtension()`, `super()`
- 参照: `type.type`

## InternalHandlerInfoWrapper.store()
- 位置: L729-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.store()`

## InternalHandlerInfoWrapper.preventInternalViewing()
- 位置: L733-735
- 役割: (未記入)
- 触るとき: (未記入)

## InternalHandlerInfoWrapper.enabled()
- 位置: L737-739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## PDFHandlerInfoWrapper.constructor()
- 位置: L743-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## PDFHandlerInfoWrapper.preventInternalViewing()
- 位置: L747-749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## PDFHandlerInfoWrapper.enabled()
- 位置: L753-755
- 役割: (未記入)
- 触るとき: (未記入)

## ViewableInternallyHandlerInfoWrapper.enabled()
- 位置: L759-761
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadIntegration.shouldViewDownloadInternally()`
- 参照: `this.type`

## loadInternalHandlers()
- 位置: L774-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs .getCharPref()`, `Services.prefs .getCharPref("browser.download.viewableInternally.enabledTypes", "") .trim()`
- 条件付き依存: `if (enabledHandlers)` → `enabledHandlers.split()`
- 条件付き依存: `if (enabledHandlers)` → `internalHandlers.push()`
- 条件付き依存: `if (enabledHandlers)` → `ext.trim()`
- 参照: `internalHandler.enabled`, `internalHandler.type`
- XPCOM: `Services.prefs`

## loadApplicationHandlers()
- 位置: L797-812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gHandlerService.enumerate()`
- 条件付き依存: `if (!(type in handledTypes))` → `lazy.DownloadIntegration.shouldViewDownloadInternally()`
- 参照: `wrappedHandlerInfo.type`

## getFileDisplayName()
- 位置: L817-833
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (file instanceof Ci.nsILocalFileWin)` → `file.getVersionInfoField()`
- 参照: `AppConstants.platform`, `Ci.nsILocalFileMac`, `Ci.nsILocalFileWin`, `file.bundleDisplayName`, `file.leafName`
- XPCOM: [`nsILocalFileMac`](../../../../xpcom/io/nsILocalFileMac.idl.md) / [`nsILocalFileWin`](../../../../xpcom/io/nsILocalFileWin.idl.md)

## getLocalHandlerApp()
- 位置: L835-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/local-handler-app;1" ].createInstance()`, `getFileDisplayName()`
- 参照: `Ci.nsILocalHandlerApp`, `localHandlerApp.executable`, `localHandlerApp.name`
- XPCOM: [`nsILocalHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / `@mozilla.org/uriloader/local-handler-app;1`

## getIconURLForAppId()
- 位置: L845-847
- 役割: (未記入)
- 触るとき: (未記入)

## getIconURLForFile()
- 位置: L849-856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io .getProtocolHandler()`, `Services.io .getProtocolHandler("file") .QueryInterface()`, `fph.getURLSpecFromActualFile()`
- 参照: `Ci.nsIFileProtocolHandler`
- XPCOM: [`nsIFileProtocolHandler`](../../../../netwerk/protocol/file/nsIFileProtocolHandler.idl.md) / `Services.io`

## getIconURLForHandlerApp()
- 位置: L858-873
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aHandlerApp instanceof Ci.nsILocalHandlerApp)` → `getIconURLForFile()`
- 条件付き依存: `if (aHandlerApp instanceof Ci.nsIWebHandlerApp)` → `getIconURLForWebApp()`
- 条件付き依存: `if (aHandlerApp instanceof Ci.nsIGIOHandlerApp)` → `getIconURLForAppId()`
- 参照: `Ci.nsIGIOHandlerApp`, `Ci.nsILocalHandlerApp`, `Ci.nsIWebHandlerApp`, `aHandlerApp.executable`, `aHandlerApp.id`, `aHandlerApp.uriTemplate`
- XPCOM: [`nsIGIOHandlerApp`](../../../../xpcom/system/nsIGIOService.idl.md) / [`nsILocalHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIWebHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## getIconURLForWebApp()
- 位置: L875-895
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^https?$/.test()`, `Services.io.newURI()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( /^https?$/.test(uri.scheme) && Services.prefs.getBoolPref("browser.chrome.site_icons") )` → `getMozRemoteImageURL()`
- 参照: `uri.prePath`, `uri.scheme`
- XPCOM: `Services.io` / `Services.prefs`

## setLocalizedLabel()
- 位置: async L905-914
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.removeAttribute()`, `item.setAttribute()`, `l10n.hasOwnProperty()`
- 条件付き依存: `if (!(l10n.hasOwnProperty("raw")))` → `document.l10n.formatValues()`
- 参照: `l10n.raw`

## ApplicationListItem.forNode()
- 位置: L926-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNodeToObjectMap.get()`

## ApplicationListItem.constructor()
- 位置: L933-935
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.handlerInfoWrapper`

## ApplicationListItem.setOrRemoveAttributes()
- 位置: L949-958
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `node.setAttribute()`
- 条件付き依存: `if (!(value))` → `node.removeAttribute()`
- 参照: `this.node`

## ApplicationListItem.createNode()
- 位置: async L960-986
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`, `document.createElement()`, `gNodeToObjectMap.set()`, `setLocalizedLabel()`, `this.actionsMenu.classList.add()`, `this.buildActionsMenu()`, `this.handlerInfoWrapper._getIcon()`, `this.node.appendChild()`, `this.setOrRemoveAttributes()`
- 条件付き依存: `if (iconSrc)` → `this.node.setAttribute()`
- 参照: `this.actionsMenu`, `this.actionsMenu.disabled`, `this.actionsMenu.slot`, `this.handlerInfoWrapper.type`, `this.handlerInfoWrapper.typeDescription`, `this.node`
- XPCOM: `Services.prefs`

## ApplicationListItem._buildActionsMenuOption()
- 位置: L1000-1024
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.l10n.setAttributes()`, `option.setAttribute()`
- 条件付き依存: `if (iconSrc)` → `option.setAttribute()`
- 条件付き依存: `if (action)` → `option.setAttribute()`
- 参照: `this.actionsMenuOptionCount`

## ApplicationListItem._getSaveFileIcon()
- 位置: L1031-1036
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## ApplicationListItem._isInternalMenuItem()
- 位置: L1042-1047
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `handlerInfo.preventInternalViewing`

## ApplicationListItem._buildActionsMenuDefaultItem()
- 位置: L1056-1086
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._buildActionsMenuOption()`, `this._isInternalMenuItem()`
- 条件付き依存: `if (this._isInternalMenuItem(handlerInfo))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._isInternalMenuItem(handlerInfo)))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (image)` → `defaultMenuItem.setAttribute()`
- 参照: `Ci.nsIHandlerInfo.useSystemDefault`, `handlerInfo.defaultDescription`, `handlerInfo.hasDefaultHandler`, `handlerInfo.iconURLForSystemDefault`
- XPCOM: [`nsIHandlerInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## ApplicationListItem.buildActionsMenu()
- 位置: L1091-1309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ApplicationsHandler.isValidHandlerApp()`, `document.createElement()`, `getIconURLForHandlerApp()`, `handlerInfo.possibleApplicationHandlers.enumerate()`, `possibleAppMenuItems.push()`, `this._buildActionsMenuDefaultItem()`, `this._buildActionsMenuOption()`, `this._isInternalMenuItem()`, `this.actionsMenu.appendChild()`, `this.actionsMenu.hasChildNodes()`, `this.actionsMenu.removeChild()`
- 条件付き依存: `if (this._isInternalMenuItem(handlerInfo))` → `this._buildActionsMenuOption()`
- 条件付き依存: `if (this._isInternalMenuItem(handlerInfo))` → `this.actionsMenu.appendChild()`
- 条件付き依存: `if (handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo)` → `this._buildActionsMenuOption()`
- 条件付き依存: `if (handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo)` → `this._getSaveFileIcon()`
- 条件付き依存: `if (handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo)` → `this.actionsMenu.appendChild()`
- 条件付き依存: `if (defaultMenuItem)` → `this.actionsMenu.appendChild()`
- 条件付き依存: `if (possibleApp instanceof Ci.nsILocalHandlerApp)` → `getFileDisplayName()`
- 条件付き依存: `if (gGIOService)` → `gGIOService.getAppsForURIScheme()`
- 条件付き依存: `if (gGIOService)` → `gioApps.enumerate()`
- 条件付き依存: `if (gGIOService)` → `possibleHandlers.queryElementAt()`
- 条件付き依存: `if (gGIOService)` → `handler.equals()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `this._buildActionsMenuOption()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `getIconURLForHandlerApp()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `this.actionsMenu.appendChild()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `possibleAppMenuItems.push()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Cc["@mozilla.org/mime;1"] .getService(Ci.nsIMIMEService) .getTypeFromExtension()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Cc["@mozilla.org/mime;1"] .getService()`
- 条件付き依存: `if (canOpenWithOtherApp)` → `this._buildActionsMenuOption()`
- 条件付き依存: `if (canOpenWithOtherApp)` → `this.actionsMenu.appendChild()`
- 条件付き依存: `if (possibleAppMenuItems.length)` → `this.actionsMenu.appendChild()`
- 条件付き依存: `if (possibleAppMenuItems.length)` → `document.createElement()`
- 条件付き依存: `if (possibleAppMenuItems.length)` → `this._buildActionsMenuOption()`
- 条件付き依存: `if (!(internalMenuItem))` → `console.error()`
- 条件付き依存: `if (preferredApp)` → `possibleAppMenuItems.find()`
- 条件付き依存: `if (preferredApp)` → `v.handlerApp.equals()`
- 条件付き依存: `if (!(preferredItem))` → `possibleAppMenuItems .map(v => v.handlerApp && v.handlerApp.name) .join()`
- 条件付き依存: `if (!(preferredItem))` → `possibleAppMenuItems .map()`
- 条件付き依存: `if (!(preferredItem))` → `console.error()`
- 参照: `AppConstants.platform`, `Ci.nsIHandlerApp`, `Ci.nsIHandlerInfo.alwaysAsk`, `Ci.nsIHandlerInfo.handleInternally`, `Ci.nsIHandlerInfo.saveToDisk`, `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIHandlerInfo.useSystemDefault`, `Ci.nsILocalHandlerApp`, `Ci.nsIMIMEInfo`, `Ci.nsIMIMEService`, `askMenuItem.value`, `defaultMenuItem.value`, `handler.name`, `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.defaultDescription`, `handlerInfo.possibleApplicationHandlers`, `handlerInfo.preferredAction`, `handlerInfo.preferredApplicationHandler`, `handlerInfo.type`, `handlerInfo.wrappedHandlerInfo`, `internalMenuItem.value`, `menuItem.className`, `menuItem.handlerApp`, `possibleApp.executable`, `possibleApp.name`, `possibleAppMenuItems.length`, `possibleHandlers.length`, `preferredItem.value`, `saveMenuItem.className`, `saveMenuItem.value`, `this.actionsMenu.lastChild`, `this.actionsMenu.value`, `this.actionsMenuOptionCount`, `v.handlerApp`, `v.handlerApp.name`
- XPCOM: [`nsIHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIHandlerInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsILocalHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIMIMEInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIMIMEService`](../../../../netwerk/mime/nsIMIMEService.idl.md) / `@mozilla.org/mime;1`

## Handler._list()
- 位置: L1357-1361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## Handler._filter()
- 位置: L1363-1367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## Handler.preInitApplications()
- 位置: async L1369-1391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HandlerServiceHelpers.loadApplicationHandlers()`, `HandlerServiceHelpers.loadInternalHandlers()`, `this._buildHeader()`, `this._buildView()`, `this._list.appendChild()`, `this._rebuildVisibleTypes()`
- 参照: `this._handledTypes`, `this._list`, `this._list.updateComplete`, `this.headerElement`, `this.initialized`

## Handler._rebuildVisibleTypes()
- 位置: async L1393-1427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.tm.dispatchToMainThread()`, `this._visibleTypes.push()`, `visibleDescriptions.get()`
- 条件付き依存: `if (!otherHandlerInfo)` → `visibleDescriptions.set()`
- 参照: `handlerInfo.description`, `handlerInfo.disambiguateDescription`, `otherHandlerInfo.disambiguateDescription`, `this._handledTypes`, `this._visibleTypes`
- XPCOM: `Services.tm`

## Handler._buildHeader()
- 位置: L1434-1450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `headerElement.appendChild()`, `this.actionColumn.setAttribute()`, `this.typeColumn.setAttribute()`
- 参照: `headerElement.slot`, `this.actionColumn`, `this.actionColumn.slot`, `this.typeColumn`

## Handler._sortItems()
- 位置: L1458-1467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `comp.compare()`, `textForNode()`, `unorderedItems.sort()`
- 参照: `Services.intl.Collator`
- XPCOM: `Services.intl`

## textForNode()
- 位置: L1462-1462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.getAttribute()`

## Handler._rebuildView()
- 位置: async L1469-1475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._buildView()`, `this._rebuildVisibleTypes()`
- 参照: `this._list.textContent`, `this.items`

## Handler._buildView()
- 位置: async L1477-1565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `document.createDocumentFragment()`, `handlerItem .createNode()`, `handlerItem .createNode() .then()`, `handlerItem.actionsMenu.addEventListener()`, `itemsFragment.appendChild()`, `promises.push()`, `this._filter.addEventListener()`, `this._list.appendChild()`, `this._sortItems()`, `this.filter()`, `this.items.push()`, `unorderedItems.push()`
- 条件付き依存: `if (newValue !== "choose-app" && newValue !== "manage-app")` → `this._onSelectActionsMenuOption()`
- 条件付き依存: `if (newValue === "choose-app")` → `this.chooseApp()`
- 条件付き依存: `if (!(newValue === "choose-app"))` → `this.manageApp()`
- 条件付き依存: `if (this._filter.value)` → `document.l10n.translateFragment()`
- 条件付き依存: `if (this._filter.value)` → `this.filter()`
- 条件付き依存: `if (this._filter.value)` → `document.l10n.pauseObserving()`
- 条件付き依存: `if (this._filter.value)` → `document.l10n.resumeObserving()`
- 参照: `console.error`, `handlerItem.actionsMenu.updateComplete`, `handlerItem.actionsMenu.value`, `item.node.hidden`, `this._filter.value`, `this._visibleTypes`, `this.items`

## Handler.filter()
- 位置: L1570-1579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.actionsMenu.selectedOption.label .toLowerCase()`, `item.actionsMenu.selectedOption.label .toLowerCase() .includes()`, `item.node.label.toLowerCase()`, `item.node.label.toLowerCase().includes()`, `this._filter.value.toLowerCase()`
- 参照: `item.node.hidden`, `this.items`

## Handler._onSelectActionsMenuOption()
- 位置: L1596-1598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._storeAction()`

## Handler._storeAction()
- 位置: L1603-1637
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handlerInfo.store()`, `handlerItem.actionsMenu.querySelector()`, `parseInt()`, `selectedOption.getAttribute()`
- 参照: `Ci.nsIHandlerInfo.alwaysAsk`, `Ci.nsIHandlerInfo.useHelperApp`, `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerInfo.preferredApplicationHandler`, `handlerItem.actionsMenu.value`, `handlerItem.handlerInfoWrapper`, `selectedOption.handlerApp`, `this._storingAction`
- XPCOM: [`nsIHandlerInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## Handler.manageApp()
- 位置: L1642-1654
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`
- 参照: `handlerItem.handlerInfoWrapper`

## closedCallback()
- 位置: L1647-1650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handlerItem.buildActionsMenu()`

## Handler.chooseApp()
- 位置: async L1659-1765
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "win")` → `document.l10n.formatValue()`
- 条件付き依存: `if ("id" in handlerInfo.description)` → `document.l10n.formatValue()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `gSubDialog.open()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `document.l10n.formatValue()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `Cc["@mozilla.org/filepicker;1"].createInstance()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `fp.init()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `fp.appendFilters()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `fp.open()`
- 参照: `AppConstants.platform`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterApps`, `Ci.nsIFilePicker.modeOpen`, `handlerInfo.description`, `handlerInfo.description.args`, `handlerInfo.description.id`, `handlerInfo.typeDescription.raw`, `handlerInfo.wrappedHandlerInfo`, `handlerItem.handlerInfoWrapper`, `params.description`, `params.filename`, `params.handlerApp`, `params.mimeInfo`, `params.title`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## chooseAppCallback()
- 位置: L1669-1689
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aHandlerApp)` → `handlerItem.buildActionsMenu()`
- 条件付き依存: `if (aHandlerApp)` → `[ ...actionsMenu.querySelectorAll("moz-option"), ].entries()`
- 条件付き依存: `if (aHandlerApp)` → `actionsMenu.querySelectorAll()`
- 条件付き依存: `if (aHandlerApp)` → `menuItem.handlerApp.equals()`
- 条件付き依存: `if ( menuItem.handlerApp && menuItem.handlerApp.equals(aHandlerApp) )` → `this._storeAction()`
- 参照: `actionsMenu.value`, `handlerItem.actionsMenu`, `menuItem.handlerApp`

## onAppPickerClose()
- 位置: L1709-1722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chooseAppCallback()`, `handlerItem.buildActionsMenu()`, `this.isValidHandlerApp()`
- 条件付き依存: `if (this.isValidHandlerApp(params.handlerApp))` → `handlerInfo.addPossibleApplicationHandler()`
- 参照: `params.handlerApp`

## fpCallback()
- 位置: L1736-1757
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isValidHandlerExecutable()`
- 条件付き依存: `if ( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) )` → `Cc[ "@mozilla.org/uriloader/local-handler-app;1" ].createInstance()`
- 条件付き依存: `if ( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) )` → `getFileDisplayName()`
- 条件付き依存: `if ( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) )` → `handler.addPossibleApplicationHandler()`
- 条件付き依存: `if ( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) )` → `chooseAppCallback()`
- 条件付き依存: `if (!( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) ))` → `handlerItem.buildActionsMenu()`
- 参照: `Ci.nsIFilePicker.returnOK`, `Ci.nsILocalHandlerApp`, `fp.file`, `handlerApp.executable`, `handlerApp.name`, `handlerItem.handlerInfoWrapper`
- XPCOM: `nsIFilePicker` / [`nsILocalHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / `@mozilla.org/uriloader/local-handler-app;1`

## Handler.isValidHandlerApp()
- 位置: L1773-1794
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aHandlerApp instanceof Ci.nsILocalHandlerApp)` → `this._isValidHandlerExecutable()`
- 参照: `Ci.nsIGIOHandlerApp`, `Ci.nsIGIOMimeApp`, `Ci.nsILocalHandlerApp`, `Ci.nsIWebHandlerApp`, `aHandlerApp.command`, `aHandlerApp.executable`, `aHandlerApp.id`, `aHandlerApp.uriTemplate`
- XPCOM: [`nsIGIOHandlerApp`](../../../../xpcom/system/nsIGIOService.idl.md) / [`nsIGIOMimeApp`](../../../../xpcom/system/nsIGIOService.idl.md) / [`nsILocalHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIWebHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## Handler._isValidHandlerExecutable()
- 位置: L1796-1814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aExecutable.exists()`, `aExecutable.isExecutable()`
- 参照: `AppConstants.MOZ_APP_NAME`, `AppConstants.MOZ_MACBUNDLE_NAME`, `AppConstants.platform`, `aExecutable.leafName`
