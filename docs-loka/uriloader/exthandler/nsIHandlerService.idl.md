# nsIHandlerService (uriloader/exthandler/nsIHandlerService.idl)

source: uriloader/exthandler/nsIHandlerService.idl
source-hash: 890c8ab59df819dfa1c8b7e995e89f0ffa36ae1e

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserGlue.sys.mjs`](../../browser/components/BrowserGlue.sys.mjs.md), [`browser/components/downloads/DownloadsViewUI.sys.mjs`](../../browser/components/downloads/DownloadsViewUI.sys.mjs.md), [`browser/components/downloads/DownloadsViewableInternally.sys.mjs`](../../browser/components/downloads/DownloadsViewableInternally.sys.mjs.md), [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md), [`browser/components/preferences/preferences.js`](../../browser/components/preferences/preferences.js.md), [`browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs`](../../browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs.md)

## メソッド / 属性
- `void asyncInit()`: Asynchronously performs any IO that the nsIHandlerService needs to do
- `nsISimpleEnumerator enumerate()`: Retrieve a list of all handlers in the datastore.  This list is not
- `void fillHandlerInfo(nsIHandlerInfo aHandlerInfo, ACString aOverrideType)`: Fill a handler info object with information from the datastore.
- `void store(nsIHandlerInfo aHandlerInfo)`: Save the preferred action, preferred handler, possible handlers, and
- `boolean exists(nsIHandlerInfo aHandlerInfo)`: Whether or not a record for the given handler info object exists
- `void remove(nsIHandlerInfo aHandlerInfo)`: Remove the given handler info object from the datastore.  Deletes all
- `ACString getTypeFromExtension(ACString aFileExtension)`: Get the MIME type mapped to the given file extension in the datastore.
- `boolean existsForProtocolOS(ACString aProtocolScheme)`: Whether or not there is a handler known to the OS for the
- `boolean existsForProtocol(ACString aProtocolScheme)`: Whether or not there is a handler in the datastore or OS for
- `nsIMIMEInfo getMIMEInfoFromOS(ACString aType, ACString aFileExtension, boolean aFound)`: (未記入)
- `AString getApplicationDescription(ACString aProtocolScheme)`: (未記入)
