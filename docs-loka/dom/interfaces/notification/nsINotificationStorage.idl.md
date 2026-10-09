# nsINotificationActionStorageEntry (dom/interfaces/notification/nsINotificationStorage.idl)

source: dom/interfaces/notification/nsINotificationStorage.idl
source-hash: c9dc06d94ae0ba4e223d086a144805a3f17cf207

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString name`: (未記入)
- `readonly attribute AString title`: (未記入)
- `readonly attribute ACString navigate`: (未記入)

# nsINotificationStorageEntry (dom/interfaces/notification/nsINotificationStorage.idl)

source: dom/interfaces/notification/nsINotificationStorage.idl
source-hash: c9dc06d94ae0ba4e223d086a144805a3f17cf207

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString id`: (未記入)
- `readonly attribute AString title`: (未記入)
- `readonly attribute ACString dir`: (未記入)
- `readonly attribute AString lang`: (未記入)
- `readonly attribute AString body`: (未記入)
- `readonly attribute AString tag`: (未記入)
- `readonly attribute ACString icon`: (未記入)
- `readonly attribute ACString navigate`: (未記入)
- `readonly attribute boolean requireInteraction`: (未記入)
- `readonly attribute boolean silent`: (未記入)
- `readonly attribute AString dataSerialized`: (未記入)
- `readonly attribute Array<nsINotificationActionStorageEntry> actions`: (未記入)
- `readonly attribute AString serviceWorkerRegistrationScope`: (未記入)

# nsINotificationStorageCallback (dom/interfaces/notification/nsINotificationStorage.idl)

source: dom/interfaces/notification/nsINotificationStorage.idl
source-hash: c9dc06d94ae0ba4e223d086a144805a3f17cf207

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void done(Array<nsINotificationStorageEntry> aEntries)`: Callback function used to pass single notification back

# nsINotificationStorage (dom/interfaces/notification/nsINotificationStorage.idl)

source: dom/interfaces/notification/nsINotificationStorage.idl
source-hash: c9dc06d94ae0ba4e223d086a144805a3f17cf207

- 継承: nsISupports
- 役割: Interface for notification persistence layer.
- 実装: (未記入)
- 使っているJS: [`browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs`](../../../browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs.md)

## メソッド / 属性
- `void put(AString aOrigin, nsINotificationStorageEntry aEntry, AString aScope)`: Add/replace a notification to the persistence layer.
- `void get(AString origin, AString scope, AString tag, nsINotificationStorageCallback aCallback)`: Retrieve a list of notifications.
- `Promise getById(AUTF8String origin, AString id)`: Retrieve a notification by ID.
- `void delete(AString origin, AString id)`: Remove a notification from storage.
- `void deleteAllExcept(Array<AString> ids)`: Remove all notifications from storage, except the ones in `ids`.
