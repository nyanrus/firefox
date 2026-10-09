# browser/components/screenshots/fileHelpers.mjs

source: browser/components/screenshots/fileHelpers.mjs
source-hash: 1cc33c178adf98b4326e18d1a6543aa68d3acdc4
lines: 340

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## getMaxFilenameLength()
- 位置: L48-54
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`, `downloadDir.length`

## checkFilenameLength()
- 位置: L64-70
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`, `filename.length`, `new Blob([filename]).size`

## getFilename()
- 位置: async L79-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkFilenameLength()`, `currentDateTime.substring()`, `currentDateTime.substring(11, 19).replace()`, `date.getTime()`, `date.getTimezoneOffset()`, `filenameTitle .replace()`, `filenameTitle .replace(/[\\/]/g, "_") .replace()`, `filenameTitle .replace(/[\\/]/g, "_") .replace(/[\u200e\u200f\u202a-\u202e]/g, "") .replace()`, `filenameTitle.replace()`, `getDownloadDirectory()`, `getMaxFilenameLength()`, `new Date( date.getTime() - date.getTimezoneOffset() * 60 * 1000 ).toISOString()`
- 条件付き依存: `if (filenameTitle === null)` → `lazy.ScreenshotsUtils.getActor(browser).sendQuery()`
- 条件付き依存: `if (filenameTitle === null)` → `lazy.ScreenshotsUtils.getActor()`
- 条件付き依存: `if (checkFilenameLength(clipFilename, maxNameStemLength))` → `clipFilename.substring()`
- 条件付き依存: `if (knownDownloadsDir)` → `PathUtils.join()`
- 条件付き依存: `if (!(knownDownloadsDir))` → `promiseTargetFile()`
- 参照: `"[...].png".length`, `browser.documentGlobal`, `filenameTitle.length`, `fpParams.file.path`

## getDownloadDirectory()
- 位置: async L160-169
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.useDownloadDir)` → `lazy.Downloads.getPreferredScreenshotsDirectory()`
- 条件付き依存: `if (lazy.useDownloadDir)` → `IOUtils.exists()`
- 参照: `lazy.useDownloadDir`

## FileInfo.constructor()
- 位置: L179-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aFileName.replace()`
- 参照: `this.fileBaseName`, `this.fileExt`, `this.fileName`

## stringBundle()
- 位置: L187-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.strings.createBundle()`
- 参照: `this.stringBundle`
- XPCOM: `Services.strings`

## makeFilePicker()
- 位置: L195-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[fpContractID].createInstance()`
- 参照: `Ci.nsIFilePicker`
- XPCOM: `nsIFilePicker`

## getMIMEService()
- 位置: L201-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[mimeSvcContractID].getService()`
- 参照: `Ci.nsIMIMEService`
- XPCOM: [`nsIMIMEService`](../../../netwerk/mime/nsIMIMEService.idl.md)

## getMIMEInfoForType()
- 位置: L208-215
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aMIMEType || aExtension)` → `getMIMEService().getFromTypeAndExtension()`
- 条件付き依存: `if (aMIMEType || aExtension)` → `getMIMEService()`

## validateFileName()
- 位置: L218-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DownloadPaths.sanitize()`
- 条件付き依存: `if (AppConstants.platform == "android")` → `processed.replace()`
- 条件付き依存: `if (processed.replace(/_/g, "").length <= processed.length / 2)` → `original.includes()`
- 条件付き依存: `if (original.includes("."))` → `original.split(".").pop()`
- 条件付き依存: `if (original.includes("."))` → `original.split()`
- 条件付き依存: `if (original.includes("."))` → `suffix.includes()`
- 参照: `AppConstants.platform`, `processed.length`, `processed.replace(/_/g, "").length`

## appendFiltersForContentType()
- 位置: L247-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aFilePicker.appendFilters()`, `getMIMEInfoForType()`
- 条件付き依存: `if (mimeInfo)` → `mimeInfo.getFileExtensions()`
- 条件付き依存: `if (extString)` → `aFilePicker.appendFilter()`
- 参照: `Ci.nsIFilePicker.filterAll`, `mimeInfo.description`
- XPCOM: `nsIFilePicker`

## promiseTargetFile()
- 位置: L285-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentAreaUtils.stringBundle.GetStringFromName()`, `IOUtils.exists()`, `appendFiltersForContentType()`, `downloadLastDir.getFileAsync()`, `downloadLastDir.setFile()`, `fp.init()`, `fp.open()`, `lazy.Downloads.getPreferredDownloadsDirectory()`, `makeFilePicker()`, `resolve()`, `validateFileName()`
- 条件付き依存: `if (!dirExists)` → `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Ci.nsIFilePicker.modeSave`, `Ci.nsIFilePicker.returnCancel`, `aFpP.contentType`, `aFpP.file`, `aFpP.file.leafName`, `aFpP.fileInfo.fileExt`, `aFpP.fileInfo.fileName`, `aFpP.fpTitleKey`, `aFpP.saveAsType`, `file.path`, `fp.defaultExtension`, `fp.defaultString`, `fp.displayDirectory`, `fp.file`, `fp.file.parent`, `fp.filterIndex`, `lazy.DownloadLastDir`, `lazy.FileUtils.File`, `win.browsingContext`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `nsIFilePicker` / `Services.dirsvc`
