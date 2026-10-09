# nsIParentalControlsService (toolkit/components/parentalcontrols/nsIParentalControlsService.idl)

source: toolkit/components/parentalcontrols/nsIParentalControlsService.idl
source-hash: f19ec1468af2d1a44879948061053c58a7c559fa

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/privacy.mjs`](../../../browser/components/preferences/config/privacy.mjs.md), [`browser/components/preferences/privacy.js`](../../../browser/components/preferences/privacy.js.md)

## メソッド / 属性
- `const short DOWNLOAD`: Action types that can be blocked for users.
- `const short INSTALL_EXTENSION`: (未記入)
- `const short INSTALL_APP`: (未記入)
- `const short BROWSE`: (未記入)
- `const short SHARE`: (未記入)
- `const short BOOKMARK`: (未記入)
- `const short ADD_CONTACT`: (未記入)
- `const short SET_IMAGE`: (未記入)
- `const short MODIFY_ACCOUNTS`: (未記入)
- `const short REMOTE_DEBUGGING`: (未記入)
- `const short IMPORT_SETTINGS`: (未記入)
- `const short PRIVATE_BROWSING`: (未記入)
- `const short DATA_CHOICES`: (未記入)
- `const short CLEAR_HISTORY`: (未記入)
- `const short MASTER_PASSWORD`: (未記入)
- `const short GUEST_BROWSING`: (未記入)
- `const short ADVANCED_SETTINGS`: (未記入)
- `const short CAMERA_MICROPHONE`: (未記入)
- `const short BLOCK_LIST`: (未記入)
- `const short TELEMETRY`: (未記入)
- `const short HEALTH_REPORT`: (未記入)
- `const short DEFAULT_THEME`: (未記入)
- `readonly attribute boolean parentalControlsEnabled`: @returns true if the current user account has parental controls
- `readonly attribute boolean blockFileDownloadsEnabled`: @returns true if the current user account parental controls
- `boolean isAllowed(short aAction, nsIURI aUri)`: Check if the user can do the prescibed action for this uri.
- `readonly attribute boolean loggingEnabled`: @returns true if the current user account has parental controls
- `const short ePCLog_URIVisit`: Log entry types. Additional types can be defined and implemented
- `const short ePCLog_FileDownload`: (未記入)
- `void log(short aEntryType, boolean aFlag, nsIURI aSource, nsIFile aTarget)`: Log an application specific parental controls
