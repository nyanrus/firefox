# nsIBrowserHandler (browser/components/nsIBrowserHandler.idl)

source: browser/components/nsIBrowserHandler.idl
source-hash: 8666f79e57e8a58c972c0bd4a0c0c97ad5751354

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/actors/ContextMenuParent.sys.mjs`](../actors/ContextMenuParent.sys.mjs.md), [`browser/base/content/browser.js`](../base/content/browser.js.md), [`browser/components/BrowserGlue.sys.mjs`](BrowserGlue.sys.mjs.md), [`browser/components/asrouter/modules/ASRouter.sys.mjs`](asrouter/modules/ASRouter.sys.mjs.md), [`browser/components/asrouter/modules/ASRouterTargeting.sys.mjs`](asrouter/modules/ASRouterTargeting.sys.mjs.md), [`browser/components/asrouter/modules/PreonboardingSplash.sys.mjs`](asrouter/modules/PreonboardingSplash.sys.mjs.md), [`browser/components/places/PlacesBrowserStartup.sys.mjs`](places/PlacesBrowserStartup.sys.mjs.md), [`browser/components/sessionstore/SessionStore.sys.mjs`](sessionstore/SessionStore.sys.mjs.md), [`browser/components/shell/StartupOSIntegration.sys.mjs`](shell/StartupOSIntegration.sys.mjs.md), [`browser/modules/BrowserWindowTracker.sys.mjs`](../modules/BrowserWindowTracker.sys.mjs.md), [`browser/modules/Sanitizer.sys.mjs`](../modules/Sanitizer.sys.mjs.md)

## メソッド / 属性
- `attribute AUTF8String startPage`: (未記入)
- `attribute AUTF8String defaultArgs`: (未記入)
- `AUTF8String getFirstWindowArgs()`: (未記入)
- `attribute boolean kiosk`: (未記入)
- `attribute boolean majorUpgrade`: (未記入)
- `attribute boolean firstRunProfile`: (未記入)
- `AUTF8String getFeatures(nsICommandLine aCmdLine)`: Extract the width and height specified on the command line, if present.
