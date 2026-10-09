# nsIContentPolicy (dom/base/nsIContentPolicy.idl)

source: dom/base/nsIContentPolicy.idl
source-hash: 985602dab46208efb38b2792b9e5936d882fd822

- 継承: nsISupports
- 役割: Interface for content policy mechanism.  Implementations of this
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/components/asrouter/modules/ToastNotification.sys.mjs`](../../browser/components/asrouter/modules/ToastNotification.sys.mjs.md), [`browser/components/enterprisepolicies/helpers/WebsiteFilter.sys.mjs`](../../browser/components/enterprisepolicies/helpers/WebsiteFilter.sys.mjs.md), [`browser/components/genai/LinkPreviewChild.sys.mjs`](../../browser/components/genai/LinkPreviewChild.sys.mjs.md), [`browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs`](../../browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs.md), [`browser/components/profiles/SelectableProfileService.sys.mjs`](../../browser/components/profiles/SelectableProfileService.sys.mjs.md), [`browser/components/taskbartabs/TaskbarTabsUtils.sys.mjs`](../../browser/components/taskbartabs/TaskbarTabsUtils.sys.mjs.md), [`browser/components/topsites/TopSites.sys.mjs`](../../browser/components/topsites/TopSites.sys.mjs.md), [`browser/modules/ASWebAuthSessionService.sys.mjs`](../../browser/modules/ASWebAuthSessionService.sys.mjs.md), [`browser/modules/FaviconLoader.sys.mjs`](../../browser/modules/FaviconLoader.sys.mjs.md), [`browser/modules/WindowsPreviewPerTab.sys.mjs`](../../browser/modules/WindowsPreviewPerTab.sys.mjs.md)

## メソッド / 属性
- `const short REJECT_REQUEST`: Returned from shouldLoad or shouldProcess if the load or process request
- `const short REJECT_TYPE`: Returned from shouldLoad or shouldProcess if the load/process is rejected
- `const short REJECT_SERVER`: Returned from shouldLoad or shouldProcess if the load/process is rejected
- `const short REJECT_OTHER`: Returned from shouldLoad or shouldProcess if the load/process is rejected
- `const short REJECT_POLICY`: Returned from shouldLoad or shouldProcess if the load/process is forbiddden
- `const short ACCEPT`: Returned from shouldLoad or shouldProcess if the load or process request
- `short shouldLoad(nsIURI aContentLocation, nsILoadInfo aLoadInfo)`: Should the resource at this location be loaded?
- `short shouldProcess(nsIURI aContentLocation, nsILoadInfo aLoadInfo)`: Should the resource be processed?
