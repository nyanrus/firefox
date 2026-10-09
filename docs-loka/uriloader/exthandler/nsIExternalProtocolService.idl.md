# nsIExternalProtocolService (uriloader/exthandler/nsIExternalProtocolService.idl)

source: uriloader/exthandler/nsIExternalProtocolService.idl
source-hash: 1b43e0d5eeb490e0cdfdae7b7eccaa71f2fd8da2

- 継承: nsISupports
- 役割: The external protocol service is used for finding and launching
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser.js`](../../browser/base/content/browser.js.md), [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/components/asrouter/modules/ASRouterTargeting.sys.mjs`](../../browser/components/asrouter/modules/ASRouterTargeting.sys.mjs.md), [`browser/components/downloads/DownloadsCommon.sys.mjs`](../../browser/components/downloads/DownloadsCommon.sys.mjs.md), [`browser/components/enterprisepolicies/Policies.sys.mjs`](../../browser/components/enterprisepolicies/Policies.sys.mjs.md), [`browser/components/migration/MigrationUtils.sys.mjs`](../../browser/components/migration/MigrationUtils.sys.mjs.md), [`browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs`](../../browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs.md), [`browser/components/sharing/SharingUtils.sys.mjs`](../../browser/components/sharing/SharingUtils.sys.mjs.md)

## メソッド / 属性
- `boolean externalProtocolHandlerExists(string aProtocolScheme)`: Check whether a handler for a specific protocol exists.  Specifically,
- `boolean isExposedProtocol(string aProtocolScheme)`: Check whether a handler for a specific protocol is "exposed" as a visible
- `nsIHandlerInfo getProtocolHandlerInfo(ACString aProtocolScheme)`: Retrieve the handler for the given protocol.  If neither the application
- `nsIHandlerInfo getProtocolHandlerInfoFromOS(ACString aProtocolScheme, boolean aFound)`: Given a scheme, looks up the protocol info from the OS.  This should be
- `void setProtocolHandlerDefaults(nsIHandlerInfo aHandlerInfo, boolean aOSHandlerExists)`: Set some sane defaults for a protocol handler object.
- `void loadURI(nsIURI aURI, nsIPrincipal aTriggeringPrincipal, nsIPrincipal aRedirectPrincipal, BrowsingContext aBrowsingContext, boolean aWasTriggeredExternally, boolean aHasValidUserGestureActivation, boolean aNewWindowTarget)`: Used to load a URI via an external application. Might prompt the user for
- `AString getApplicationDescription(AUTF8String aScheme)`: Gets a human-readable description for the application responsible for
- `boolean isCurrentAppOSDefaultForProtocol(AUTF8String aScheme)`: Check if this app is registered as the OS default for a given scheme.
