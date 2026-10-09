# nsIHandlerInfo (netwerk/mime/nsIMIMEInfo.idl)

source: netwerk/mime/nsIMIMEInfo.idl
source-hash: 7bccc1afafab61775cb6ceb73df8711ce63b578b

- 継承: nsISupports
- 役割: nsIHandlerInfo gives access to the information about how a given protocol
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/components/asrouter/modules/ASRouterTargeting.sys.mjs`](../../browser/components/asrouter/modules/ASRouterTargeting.sys.mjs.md), [`browser/components/downloads/DownloadsViewableInternally.sys.mjs`](../../browser/components/downloads/DownloadsViewableInternally.sys.mjs.md), [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md), [`browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs`](../../browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs.md)

## メソッド / 属性
- `readonly attribute ACString type`: The type of this handler info.  For MIME handlers, this is the MIME type.
- `attribute AString description`: A human readable description of the handler type
- `attribute nsIHandlerApp preferredApplicationHandler`: The application the user has said they want associated with this content
- `readonly attribute nsIMutableArray possibleApplicationHandlers`: Applications that can handle this content type.
- `readonly attribute boolean hasDefaultHandler`: Indicates whether a default OS application handler exists,
- `readonly attribute AString defaultDescription`: A pretty name description of the associated default OS application. Only
- `readonly attribute nsIFile defaultExecutable`: The default OS application. Only usable if hasDefaultHandler is true.
- `void launchWithURI(nsIURI aURI, BrowsingContext aBrowsingContext)`: Launches the application with the specified URI, in a way that
- `attribute nsHandlerInfoAction preferredAction`: preferredAction is how the user specified they would like to handle
- `const long saveToDisk`: (未記入)
- `const long alwaysAsk`: Used to indicate that we know nothing about what to do with this.  You
- `const long useHelperApp`: (未記入)
- `const long handleInternally`: (未記入)
- `const long useSystemDefault`: (未記入)
- `attribute boolean alwaysAskBeforeHandling`: alwaysAskBeforeHandling: if true, we should always give the user a

# nsIMIMEInfo (netwerk/mime/nsIMIMEInfo.idl)

source: netwerk/mime/nsIMIMEInfo.idl
source-hash: 7bccc1afafab61775cb6ceb73df8711ce63b578b

- 継承: nsIHandlerInfo
- 役割: nsIMIMEInfo extends nsIHandlerInfo with a bunch of information specific to
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/dialogs/applicationManager.js`](../../browser/components/preferences/dialogs/applicationManager.js.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md)

## メソッド / 属性
- `nsIUTF8StringEnumerator getFileExtensions()`: Gives you an array of file types associated with this type.
- `void setFileExtensions(AUTF8String aExtensions)`: Set File Extensions. Input is a comma delimited list of extensions.
- `boolean extensionExists(AUTF8String aExtension)`: Returns whether or not the given extension is
- `void appendExtension(AUTF8String aExtension)`: Append a given extension to the set of extensions
- `attribute AUTF8String primaryExtension`: Returns the first extension association in
- `readonly attribute ACString MIMEType`: The MIME type of this MIMEInfo.
- `boolean equals(nsIMIMEInfo aMIMEInfo)`: Returns whether or not these two nsIMIMEInfos are logically
- `readonly attribute nsIArray possibleLocalHandlers`: Returns a list of nsILocalHandlerApp objects containing
- `void launchWithFile(nsIFile aFile)`: Launches the application with the specified file, in a way that
- `boolean isCurrentAppOSDefault()`: Check if we ourselves are registered as the OS default for this type.

# nsIHandlerApp (netwerk/mime/nsIMIMEInfo.idl)

source: netwerk/mime/nsIMIMEInfo.idl
source-hash: 7bccc1afafab61775cb6ceb73df8711ce63b578b

- 継承: nsISupports
- 役割: nsIHandlerApp represents an external application that can handle content
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md)

## メソッド / 属性
- `attribute AString name`: Human readable name for the handler
- `attribute AString detailedDescription`: Detailed description for this handler. Suitable for
- `boolean equals(nsIHandlerApp aHandlerApp)`: Whether or not the given handler app is logically equivalent to the
- `void launchWithURI(nsIURI aURI, BrowsingContext aBrowsingContext)`: Launches the application with the specified URI.

# nsILocalHandlerApp (netwerk/mime/nsIMIMEInfo.idl)

source: netwerk/mime/nsIMIMEInfo.idl
source-hash: 7bccc1afafab61775cb6ceb73df8711ce63b578b

- 継承: nsIHandlerApp
- 役割: nsILocalHandlerApp is a local OS-level executable
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/dialogs/applicationManager.js`](../../browser/components/preferences/dialogs/applicationManager.js.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md)

## メソッド / 属性
- `attribute nsIFile executable`: Pointer to the executable file used to handle content
- `readonly attribute unsigned long parameterCount`: Returns the current number of command line parameters.
- `Promise prettyNameAsync()`: Asynchronously returns the pretty (user friendly) name of the
- `void clearParameters()`: Clears the current list of command line parameters.
- `void appendParameter(AString param)`: Appends a command line parameter to the command line
- `AString getParameter(unsigned long parameterIndex)`: Retrieves a specific command line parameter.
- `boolean parameterExists(AString param)`: Checks to see if a parameter exists in the command line

# nsIWebHandlerApp (netwerk/mime/nsIMIMEInfo.idl)

source: netwerk/mime/nsIMIMEInfo.idl
source-hash: 7bccc1afafab61775cb6ceb73df8711ce63b578b

- 継承: nsIHandlerApp
- 役割: nsIWebHandlerApp is a web-based handler, as speced by the WhatWG HTML5
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/components/asrouter/modules/ASRouterTargeting.sys.mjs`](../../browser/components/asrouter/modules/ASRouterTargeting.sys.mjs.md), [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/dialogs/applicationManager.js`](../../browser/components/preferences/dialogs/applicationManager.js.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md), [`browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs`](../../browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs.md)

## メソッド / 属性
- `attribute AUTF8String uriTemplate`: Template used to construct the URI to GET.  Template is expected to have

# nsIDBusHandlerApp (netwerk/mime/nsIMIMEInfo.idl)

source: netwerk/mime/nsIMIMEInfo.idl
source-hash: 7bccc1afafab61775cb6ceb73df8711ce63b578b

- 継承: nsIHandlerApp
- 役割: nsIDBusHandlerApp represents local applications launched by DBus a message
- 実装: (未記入)

## メソッド / 属性
- `attribute AUTF8String service`: Service defines the dbus service that should handle this protocol.
- `attribute AUTF8String objectPath`: Objpath defines the object path of the dbus service that should handle
- `attribute AUTF8String dBusInterface`: DBusInterface defines the interface of the dbus service that should
- `attribute AUTF8String method`: Method defines the dbus method that should be invoked to handle this
