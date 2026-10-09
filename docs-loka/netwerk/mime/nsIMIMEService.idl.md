# nsIMIMEService (netwerk/mime/nsIMIMEService.idl)

source: netwerk/mime/nsIMIMEService.idl
source-hash: c4bf156ddc2c92227e334c6615951b51f0244ea3

- 継承: nsISupports
- 役割: The MIME service is responsible for mapping file extensions to MIME-types
- 実装: (未記入)
- 使っているJS: [`browser/components/downloads/DownloadsCommon.sys.mjs`](../../browser/components/downloads/DownloadsCommon.sys.mjs.md), [`browser/components/downloads/DownloadsViewableInternally.sys.mjs`](../../browser/components/downloads/DownloadsViewableInternally.sys.mjs.md), [`browser/components/enterprisepolicies/Policies.sys.mjs`](../../browser/components/enterprisepolicies/Policies.sys.mjs.md), [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md), [`browser/components/preferences/preferences.js`](../../browser/components/preferences/preferences.js.md), [`browser/components/screenshots/fileHelpers.mjs`](../../browser/components/screenshots/fileHelpers.mjs.md), [`browser/components/taskbartabs/TaskbarTabsPin.sys.mjs`](../../browser/components/taskbartabs/TaskbarTabsPin.sys.mjs.md)

## メソッド / 属性
- `nsIMIMEInfo getFromTypeAndExtension(ACString aMIMEType, AUTF8String aFileExt)`: Retrieves an nsIMIMEInfo using both the extension
- `ACString getTypeFromExtension(AUTF8String aFileExt)`: Retrieves a ACString representation of the MIME type
- `ACString getTypeFromURI(nsIURI aURI)`: Retrieves a ACString representation of the MIME type
- `ACString getDefaultTypeFromURI(nsIURI aURI)`: Retrieves a ACString representation of the MIME type
- `ACString getTypeFromFile(nsIFile aFile)`: (未記入)
- `AUTF8String getPrimaryExtension(ACString aMIMEType, AUTF8String aFileExt)`: Given a Type/Extension combination, returns the default extension
- `nsIMIMEInfo getMIMEInfoFromOS(ACString aType, ACString aFileExtension, boolean aFound)`: (未記入)
- `void updateDefaultAppInfo(nsIMIMEInfo aMIMEInfo)`: Update the mime info's default app information based on OS
- `const long VALIDATE_DEFAULT`: Default filename validation for getValidFileName and
- `const long VALIDATE_SANITIZE_ONLY`: If true, then the filename is only validated to ensure that it is
- `const long VALIDATE_DONT_COLLAPSE_WHITESPACE`: Don't collapse strings of duplicate whitespace into a single string.
- `const long VALIDATE_DONT_TRUNCATE`: Don't truncate long filenames.
- `const long VALIDATE_GUESS_FROM_EXTENSION`: True to ignore the content type and guess the type from any existing
- `const long VALIDATE_ALLOW_EMPTY`: If the filename is empty, return the empty filename
- `const long VALIDATE_NO_DEFAULT_FILENAME`: Don't apply a default filename if the non-extension portion of the
- `const long VALIDATE_FORCE_APPEND_EXTENSION`: When the filename has an invalid extension, force the the filename to
- `const long VALIDATE_ALLOW_INVALID_FILENAMES`: Don't modify filenames or extensions that might be invalid or dangerous
- `const long VALIDATE_ALLOW_DIRECTORY_NAMES`: Some names are unsafe as a file name, but safe for directory names.
- `AString getValidFileName(nsIChannel aChannel, ACString aType, nsIURI aOriginalURI, unsigned long aFlags)`: Generate a valid filename from the channel that can be used to save
- `AString validateFileNameForSaving(AString aFileName, ACString aType, unsigned long aFlags)`: Similar to getValidFileName, but used when a specific filename needs
