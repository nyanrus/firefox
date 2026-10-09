# nsIOpenURIInFrameParams (dom/interfaces/base/nsIBrowserDOMWindow.idl)

source: dom/interfaces/base/nsIBrowserDOMWindow.idl
source-hash: 77d61061111f0a2055e67623df5deaaa1a676669

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute nsIOpenWindowInfo openWindowInfo`: (未記入)
- `attribute nsIReferrerInfo referrerInfo`: (未記入)
- `readonly attribute boolean isPrivate`: (未記入)
- `attribute nsIPrincipal triggeringPrincipal`: (未記入)
- `attribute nsIPolicyContainer policyContainer`: (未記入)
- `readonly attribute Element openerBrowser`: (未記入)
- `readonly attribute jsval openerOriginAttributes`: (未記入)

# nsIBrowserDOMWindow (dom/interfaces/base/nsIBrowserDOMWindow.idl)

source: dom/interfaces/base/nsIBrowserDOMWindow.idl
source-hash: 77d61061111f0a2055e67623df5deaaa1a676669

- 継承: nsISupports
- 役割: The C++ source has access to the browser script source through
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserContentHandler.sys.mjs`](../../../browser/components/BrowserContentHandler.sys.mjs.md), [`browser/components/preferences/config/tabs-browsing.mjs`](../../../browser/components/preferences/config/tabs-browsing.mjs.md), [`browser/components/preferences/main.js`](../../../browser/components/preferences/main.js.md), [`browser/modules/BrowserDOMWindow.sys.mjs`](../../../browser/modules/BrowserDOMWindow.sys.mjs.md), [`browser/modules/BrowserUsageTelemetry.sys.mjs`](../../../browser/modules/BrowserUsageTelemetry.sys.mjs.md)

## メソッド / 属性
- `const short OPEN_DEFAULTWINDOW`: Values for createContentWindow's and openURI's aWhere parameter.
- `const short OPEN_CURRENTWINDOW`: Open in the "current window".  If aOpener is provided, this should be the
- `const short OPEN_NEWWINDOW`: Open in a new window.
- `const short OPEN_NEWTAB`: Open in a new content tab in the toplevel browser window corresponding to
- `const short OPEN_PRINT_BROWSER`: Open in a hidden browser. Used for printing.
- `const short OPEN_NEWTAB_BACKGROUND`: Open in a new background content tab in the toplevel browser window
- `const short OPEN_NEWTAB_FOREGROUND`: Open in a new foreground content tab in the toplevel browser window
- `const short OPEN_NEWTAB_AFTER_CURRENT`: Open in a new content tab in the toplevel browser window
- `const long OPEN_NEW`: Values for createContentWindow's and openURI's aFlags parameter.
- `const long OPEN_EXTERNAL`: External link (load request from another application, xremote, etc).
- `const long OPEN_NO_OPENER`: Don't set the window.opener property on the window which is being opened.
- `const long OPEN_NO_REFERRER`: Don't set the referrer on the navigation inside the window which is
- `const long OPEN_FORCE_ALLOW_DATA_URI`: Force allow a data URI to load as a top-level document.
- `BrowsingContext createContentWindow(nsIURI aURI, nsIOpenWindowInfo aOpenWindowInfo, short aWhere, long aFlags, nsIPrincipal aTriggeringPrincipal, nsIPolicyContainer aPolicyContainer)`: Create the content window for the given URI.
- `Element createContentWindowInFrame(nsIURI aURI, nsIOpenURIInFrameParams params, short aWhere, long aFlags, AString aName)`: As above, but return the nsFrameLoaderOwner for the new window. Value is
- `BrowsingContext openURI(nsIURI aURI, nsIOpenWindowInfo aOpenWindowInfo, short aWhere, long aFlags, nsIPrincipal aTriggeringPrincipal, nsIPolicyContainer aPolicyContainer)`: Load a URI.
- `Element openURIInFrame(nsIURI aURI, nsIOpenURIInFrameParams params, short aWhere, long aFlags, AString aName)`: As above, but return the nsFrameLoaderOwner for the new window. Value is
- `boolean canClose()`: This function is responsible for calling
- `readonly attribute unsigned long tabCount`: The number browser tabs in the window. This number currently includes
