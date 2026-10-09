# nsILoadContext (docshell/base/nsILoadContext.idl)

source: docshell/base/nsILoadContext.idl
source-hash: 3bb5d46718b6cd2e333cbc3611d3c985eb140467

- 継承: nsISupports
- 役割: An nsILoadContext represents the context of a load.  This interface
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser.js`](../../browser/base/content/browser.js.md), [`browser/components/BrowserContentHandler.sys.mjs`](../../browser/components/BrowserContentHandler.sys.mjs.md), [`browser/components/sessionstore/SessionStore.sys.mjs`](../../browser/components/sessionstore/SessionStore.sys.mjs.md), [`browser/modules/FilePickerCrashed.sys.mjs`](../../browser/modules/FilePickerCrashed.sys.mjs.md)

## メソッド / 属性
- `readonly attribute mozIDOMWindowProxy associatedWindow`: associatedWindow is the window with which the load is associated, if any.
- `readonly attribute mozIDOMWindowProxy topWindow`: topWindow is the top window which is of same type as associatedWindow.
- `readonly attribute Element topFrameElement`: topFrameElement is the <iframe>, <frame>, or <browser> element which
- `readonly attribute boolean isContent`: True if the load context is content (as opposed to chrome).  This is
- `attribute boolean usePrivateBrowsing`: (未記入)
- `readonly attribute boolean useRemoteTabs`: Attribute that determines if remote (out-of-process) tabs should be used.
- `readonly attribute boolean useRemoteSubframes`: Determines if out-of-process iframes should be used.
- `attribute boolean useTrackingProtection`: (未記入)
- `void SetPrivateBrowsing(boolean aInPrivateBrowsing)`: Set the private browsing state of the load context, meant to be used internally.
- `void SetRemoteTabs(boolean aUseRemoteTabs)`: Set the remote tabs state of the load context, meant to be used internally.
- `void SetRemoteSubframes(boolean aUseRemoteSubframes)`: Set the remote subframes bit of this load context. Exclusively meant to be used internally.
- `readonly attribute jsval originAttributes`: A dictionary of the non-default origin attributes associated with this
- `void GetOriginAttributes(OriginAttributes aAttrs)`: The C++ getter for origin attributes.
