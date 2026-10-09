# browser/components/taskbartabs/TaskbarTabsUtils.sys.mjs

source: browser/components/taskbartabs/TaskbarTabsUtils.sys.mjs
source-hash: dc70912a1d2ce13bb88f62997bb7848827c6bdad
lines: 217

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetters()`

## isEnabled()
- 位置: L25-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## isMSIX()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.sysinfo`

## getTaskbarTabsFolder()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `folder.append()`
- 参照: `Ci.nsIFile`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## isTaskbarTabWindow()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWin.document.documentElement.hasAttribute()`

## getTaskbarTabIdFromWindow()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWin.document.documentElement.getAttribute()`

## _remoteDecodeImageFromFile()
- 位置: async L84-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.read()`, `Services.io.newURI()`, `content.toBase64()`, `this._remoteDecodeImageFromURI()`
- 参照: `aFile.path`
- XPCOM: `Services.io`

## _remoteDecodeImageFromURI()
- 位置: async L109-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.FaviconUtils.getMozRemoteImageURL()`, `unsafeDecodeImageFromAnyURI()`
- 参照: `Ci.nsIURI`, `aBrowser.browsingContext.currentWindowContext.contentParentId`, `aUri.spec`, `params.contentParentId`
- XPCOM: [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## _imageFromLocalURI()
- 位置: async L144-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.getProtocolFlags()`, `unsafeDecodeImageFromAnyURI()`
- 参照: `Ci.nsIProtocolHandler.URI_IS_LOCAL_RESOURCE`, `Ci.nsIURI`, `aUri.scheme`
- XPCOM: [`nsIProtocolHandler`](../../../netwerk/base/nsIIOService.idl.md) / [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## getFaviconUri()
- 位置: async L165-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Favicons.getFaviconForPage()`
- 参照: `favicon?.dataURI`

## getDefaultIcon()
- 位置: async L176-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TaskbarTabsUtils._imageFromLocalURI()`
- 参照: `lazy.Favicons.defaultFavicon`

## _determineNewDesktopEntryName()
- 位置: L191-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ShellService.getGlibPrgname()`

## unsafeDecodeImageFromAnyURI()
- 位置: async L205-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.fetchDecodedImage()`, `Services.io.newChannelFromURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `Ci.nsIContentPolicy.TYPE_IMAGE`, `Ci.nsILoadInfo.SEC_ALLOW_CROSS_ORIGIN_SEC_CONTEXT_IS_NULL`
- XPCOM: [`nsIContentPolicy`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / `Services.io` / `Services.scriptSecurityManager`
