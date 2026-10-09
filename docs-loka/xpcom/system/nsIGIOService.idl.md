# nsIGIOHandlerApp (xpcom/system/nsIGIOService.idl)

source: xpcom/system/nsIGIOService.idl
source-hash: 1cbf2a3a9fc78e3dc88f6732db896f82f633261c

- 継承: nsIHandlerApp
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md)

## メソッド / 属性
- `readonly attribute AUTF8String id`: (未記入)
- `void launchFile(AUTF8String fileName)`: (未記入)
- `AUTF8String getMozIconURL()`: (未記入)

# nsIGIOMimeApp (xpcom/system/nsIGIOService.idl)

source: xpcom/system/nsIGIOService.idl
source-hash: 1cbf2a3a9fc78e3dc88f6732db896f82f633261c

- 継承: nsIHandlerApp
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md)

## メソッド / 属性
- `const long EXPECTS_URIS`: (未記入)
- `const long EXPECTS_PATHS`: (未記入)
- `const long EXPECTS_URIS_FOR_NON_FILES`: (未記入)
- `readonly attribute AUTF8String id`: (未記入)
- `readonly attribute AUTF8String command`: (未記入)
- `readonly attribute long expectsURIs`: (未記入)
- `readonly attribute nsIUTF8StringEnumerator supportedURISchemes`: (未記入)
- `void setAsDefaultForMimeType(AUTF8String mimeType)`: (未記入)
- `void setAsDefaultForFileExtensions(AUTF8String extensions)`: (未記入)
- `void setAsDefaultForURIScheme(AUTF8String uriScheme)`: (未記入)

# nsIGIOService (xpcom/system/nsIGIOService.idl)

source: xpcom/system/nsIGIOService.idl
source-hash: 1cbf2a3a9fc78e3dc88f6732db896f82f633261c

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/DefaultBrowserCheck.sys.mjs`](../../browser/components/DefaultBrowserCheck.sys.mjs.md), [`browser/components/migration/MigrationUtils.sys.mjs`](../../browser/components/migration/MigrationUtils.sys.mjs.md), [`browser/components/preferences/DefaultBrowserHelper.mjs`](../../browser/components/preferences/DefaultBrowserHelper.mjs.md), [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/preferences.js`](../../browser/components/preferences/preferences.js.md), [`browser/components/shell/ShellService.sys.mjs`](../../browser/components/shell/ShellService.sys.mjs.md)

## メソッド / 属性
- `AUTF8String getMimeTypeFromExtension(AUTF8String extension)`: MIME registry methods
- `nsIHandlerApp getAppForURIScheme(AUTF8String aURIScheme)`: (未記入)
- `nsIMutableArray getAppsForURIScheme(AUTF8String aURIScheme)`: (未記入)
- `nsIHandlerApp getAppForMimeType(AUTF8String mimeType)`: (未記入)
- `nsIGIOHandlerApp createHandlerAppFromAppId(string appId)`: (未記入)
- `nsIGIOMimeApp createAppFromCommand(AUTF8String cmd, AUTF8String appName)`: (未記入)
- `nsIGIOMimeApp findAppFromCommand(AUTF8String cmd)`: (未記入)
- `AUTF8String getDescriptionForMimeType(AUTF8String mimeType)`: (未記入)
- `readonly attribute boolean isRunningUnderFlatpak`: Misc. methods
- `readonly attribute boolean isRunningUnderSnap`: (未記入)
- `void showURI(nsIURI uri)`: (未記入)
- `void revealFile(nsIFile file)`: (未記入)
- `void launchFile(ACString path)`: (未記入)
