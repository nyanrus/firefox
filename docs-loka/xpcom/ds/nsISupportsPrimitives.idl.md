# nsISupportsPrimitive (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupports
- 役割: Primitive base interface.
- 実装: (未記入)

## メソッド / 属性
- `const unsigned short TYPE_ID`: (未記入)
- `const unsigned short TYPE_CSTRING`: (未記入)
- `const unsigned short TYPE_STRING`: (未記入)
- `const unsigned short TYPE_PRBOOL`: (未記入)
- `const unsigned short TYPE_PRUINT8`: (未記入)
- `const unsigned short TYPE_PRUINT16`: (未記入)
- `const unsigned short TYPE_PRUINT32`: (未記入)
- `const unsigned short TYPE_PRUINT64`: (未記入)
- `const unsigned short TYPE_PRTIME`: (未記入)
- `const unsigned short TYPE_CHAR`: (未記入)
- `const unsigned short TYPE_PRINT16`: (未記入)
- `const unsigned short TYPE_PRINT32`: (未記入)
- `const unsigned short TYPE_PRINT64`: (未記入)
- `const unsigned short TYPE_FLOAT`: (未記入)
- `const unsigned short TYPE_DOUBLE`: (未記入)
- `const unsigned short TYPE_INTERFACE_POINTER`: (未記入)
- `readonly attribute unsigned short type`: (未記入)

# nsISupportsID (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for nsID structures
- 実装: (未記入)

## メソッド / 属性
- `attribute nsIDPtr data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsCString (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for ASCII strings
- 実装: (未記入)
- 使っているJS: [`browser/actors/ContextMenuChild.sys.mjs`](../../browser/actors/ContextMenuChild.sys.mjs.md), [`browser/components/urlbar/UrlbarUtils.sys.mjs`](../../browser/components/urlbar/UrlbarUtils.sys.mjs.md)

## メソッド / 属性
- `attribute ACString data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsString (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for Unicode strings
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-init.js`](../../browser/base/content/browser-init.js.md), [`browser/base/content/browser.js`](../../browser/base/content/browser.js.md), [`browser/base/content/utilityOverlay.js`](../../browser/base/content/utilityOverlay.js.md), [`browser/components/AccountsGlue.sys.mjs`](../../browser/components/AccountsGlue.sys.mjs.md), [`browser/components/BrowserContentHandler.sys.mjs`](../../browser/components/BrowserContentHandler.sys.mjs.md), [`browser/components/BrowserGlue.sys.mjs`](../../browser/components/BrowserGlue.sys.mjs.md), [`browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs`](../../browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs.md), [`browser/components/aiwindow/ui/modules/AIWindow.sys.mjs`](../../browser/components/aiwindow/ui/modules/AIWindow.sys.mjs.md), [`browser/components/downloads/content/allDownloadsView.js`](../../browser/components/downloads/content/allDownloadsView.js.md), [`browser/components/downloads/content/downloads.js`](../../browser/components/downloads/content/downloads.js.md), [`browser/components/extensions/parent/ext-windows.js`](../../browser/components/extensions/parent/ext-windows.js.md), [`browser/components/places/content/controller.js`](../../browser/components/places/content/controller.js.md), [`browser/components/sessionstore/SessionStartup.sys.mjs`](../../browser/components/sessionstore/SessionStartup.sys.mjs.md), [`browser/components/shell/WindowsSetDefaultAppCmdHandler.sys.mjs`](../../browser/components/shell/WindowsSetDefaultAppCmdHandler.sys.mjs.md), [`browser/components/sidebar/sidebar-bookmarks.mjs`](../../browser/components/sidebar/sidebar-bookmarks.mjs.md), [`browser/components/taskbartabs/TaskbarTabsWindowManager.sys.mjs`](../../browser/components/taskbartabs/TaskbarTabsWindowManager.sys.mjs.md), [`browser/components/urlbar/content/SmartbarInput.mjs`](../../browser/components/urlbar/content/SmartbarInput.mjs.md), [`browser/modules/BrowserWindowTracker.sys.mjs`](../../browser/modules/BrowserWindowTracker.sys.mjs.md), [`browser/modules/PermissionUI.sys.mjs`](../../browser/modules/PermissionUI.sys.mjs.md), [`browser/modules/URILoadingHelper.sys.mjs`](../../browser/modules/URILoadingHelper.sys.mjs.md)

## メソッド / 属性
- `attribute AString data`: (未記入)
- `wstring toString()`: (未記入)

# nsISupportsPRBool (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: The rest are truly primitive and are passed by value
- 実装: (未記入)
- 使っているJS: [`browser/base/content/aboutDialog-appUpdater.js`](../../browser/base/content/aboutDialog-appUpdater.js.md), [`browser/base/content/browser.js`](../../browser/base/content/browser.js.md), [`browser/components/BrowserGlue.sys.mjs`](../../browser/components/BrowserGlue.sys.mjs.md), [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md), [`browser/components/backup/actors/BackupUIParent.sys.mjs`](../../browser/components/backup/actors/BackupUIParent.sys.mjs.md), [`browser/components/extensions/parent/ext-windows.js`](../../browser/components/extensions/parent/ext-windows.js.md), [`browser/components/preferences/config/languages.mjs`](../../browser/components/preferences/config/languages.mjs.md), [`browser/components/preferences/preferences.js`](../../browser/components/preferences/preferences.js.md), [`browser/components/profiles/ProfilesParent.sys.mjs`](../../browser/components/profiles/ProfilesParent.sys.mjs.md), [`browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs`](../../browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs.md), [`browser/components/urlbar/UrlbarProviderInterventions.sys.mjs`](../../browser/components/urlbar/UrlbarProviderInterventions.sys.mjs.md), [`browser/modules/URILoadingHelper.sys.mjs`](../../browser/modules/URILoadingHelper.sys.mjs.md)

## メソッド / 属性
- `attribute boolean data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsPRUint8 (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for 8-bit integers
- 実装: (未記入)

## メソッド / 属性
- `attribute uint8_t data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsPRUint16 (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for unsigned 16-bit integers
- 実装: (未記入)

## メソッド / 属性
- `attribute uint16_t data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsPRUint32 (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for unsigned 32-bit integers
- 実装: (未記入)
- 使っているJS: [`browser/components/extensions/parent/ext-windows.js`](../../browser/components/extensions/parent/ext-windows.js.md), [`browser/components/taskbartabs/TaskbarTabsWindowManager.sys.mjs`](../../browser/components/taskbartabs/TaskbarTabsWindowManager.sys.mjs.md), [`browser/modules/URILoadingHelper.sys.mjs`](../../browser/modules/URILoadingHelper.sys.mjs.md)

## メソッド / 属性
- `attribute uint32_t data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsPRUint64 (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for 64-bit integers
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser.js`](../../browser/base/content/browser.js.md), [`browser/modules/BrowserWindowTracker.sys.mjs`](../../browser/modules/BrowserWindowTracker.sys.mjs.md), [`browser/modules/SitePermissions.sys.mjs`](../../browser/modules/SitePermissions.sys.mjs.md)

## メソッド / 属性
- `attribute uint64_t data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsPRTime (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for NSPR date/time values
- 実装: (未記入)

## メソッド / 属性
- `attribute PRTime data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsChar (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for single character values
- 実装: (未記入)

## メソッド / 属性
- `attribute char data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsPRInt16 (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for 16-bit integers
- 実装: (未記入)

## メソッド / 属性
- `attribute int16_t data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsPRInt32 (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for 32-bit integers
- 実装: (未記入)

## メソッド / 属性
- `attribute int32_t data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsPRInt64 (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for 64-bit integers
- 実装: (未記入)

## メソッド / 属性
- `attribute int64_t data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsFloat (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for floating point numbers
- 実装: (未記入)

## メソッド / 属性
- `attribute float data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsDouble (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for doubles
- 実装: (未記入)

## メソッド / 属性
- `attribute double data`: (未記入)
- `string toString()`: (未記入)

# nsISupportsInterfacePointer (xpcom/ds/nsISupportsPrimitives.idl)

source: xpcom/ds/nsISupportsPrimitives.idl
source-hash: c03ea225462a9e59421b04601fc836cd62606612

- 継承: nsISupportsPrimitive
- 役割: Scriptable storage for other XPCOM objects
- 実装: (未記入)

## メソッド / 属性
- `attribute nsISupports data`: (未記入)
- `attribute nsIDPtr dataIID`: (未記入)
- `string toString()`: (未記入)
