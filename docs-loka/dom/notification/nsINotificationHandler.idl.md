# nsINotificationHandler (dom/notification/nsINotificationHandler.idl)

source: dom/notification/nsINotificationHandler.idl
source-hash: fb332a5811f9ef5cd85670efe60ac18b09f70f73

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserContentHandler.sys.mjs`](../../browser/components/BrowserContentHandler.sys.mjs.md), [`browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs`](../../browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs.md)

## メソッド / 属性
- `Promise respondOnClick(nsIPrincipal aPrincipal, AString aNotificationId, AString aActionName, boolean aAutoClosed)`: Either ping the service worker corresponding to the notification, or open
