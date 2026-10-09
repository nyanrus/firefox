# nsICookieNotification (netwerk/cookie/nsICookieNotification.idl)

source: netwerk/cookie/nsICookieNotification.idl
source-hash: fb11976fa3d573d0ce250e2cd062c2b82c5c6151

- 継承: nsISupports
- 役割: Meta object dispatched by cookie change notifications.
- 実装: (未記入)
- 使っているJS: [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md), [`browser/components/sessionstore/SessionCookies.sys.mjs`](../../browser/components/sessionstore/SessionCookies.sys.mjs.md)

## メソッド / 属性
- `readonly attribute nsICookieNotification_Action action`: Describes the cookie operation this notification is for. Cookies may be
- `readonly attribute nsICookie cookie`: The cookie the notification is for, may be null depending on the action.
- `readonly attribute ACString baseDomain`: Base domain of the cookie. May be empty if cookie is null.
- `readonly attribute boolean isThirdParty`: True if the cookie set (added or changed) is considered third-party.
- `readonly attribute nsIArray batchDeletedCookies`: List of cookies purged.
- `readonly attribute unsigned long long browsingContextId`: The id of the BrowsingContext the cookie change was triggered from. Set
- `readonly attribute BrowsingContext browsingContext`: BrowsingContext associated with browsingContextId. May be nullptr.
- `readonly attribute nsIDPtr operationID`: Operation ID to track which nsICookieManager operation has generated
