# nsIPushSubscription (dom/push/nsIPushService.idl)

source: dom/push/nsIPushService.idl
source-hash: eea1fc1a0ae6b9701088f663c9e51e38483216b6

- 継承: nsISupports
- 役割: A push subscription, passed as an argument to a subscription callback.
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString endpoint`: (未記入)
- `readonly attribute long long pushCount`: (未記入)
- `readonly attribute long long lastPush`: (未記入)
- `readonly attribute long quota`: (未記入)
- `readonly attribute boolean isSystemSubscription`: (未記入)
- `readonly attribute jsval p256dhPrivateKey`: (未記入)
- `boolean quotaApplies()`: (未記入)
- `boolean isExpired()`: (未記入)
- `Array<uint8_t> getKey(AString name)`: (未記入)

# nsIPushSubscriptionCallback (dom/push/nsIPushService.idl)

source: dom/push/nsIPushService.idl
source-hash: eea1fc1a0ae6b9701088f663c9e51e38483216b6

- 継承: nsISupports
- 役割: Called by methods that return a push subscription. A non-success
- 実装: (未記入)

## メソッド / 属性
- `void onPushSubscription(nsresult status, nsIPushSubscription subscription)`: (未記入)

# nsIUnsubscribeResultCallback (dom/push/nsIPushService.idl)

source: dom/push/nsIPushService.idl
source-hash: eea1fc1a0ae6b9701088f663c9e51e38483216b6

- 継承: nsISupports
- 役割: Called by |unsubscribe|. A non-success |status| indicates that there was
- 実装: (未記入)

## メソッド / 属性
- `void onUnsubscribe(nsresult status, boolean success)`: (未記入)

# nsIPushClearResultCallback (dom/push/nsIPushService.idl)

source: dom/push/nsIPushService.idl
source-hash: eea1fc1a0ae6b9701088f663c9e51e38483216b6

- 継承: nsISupports
- 役割: Called by |clearForDomain|. A non-success |status| indicates that there was
- 実装: (未記入)

## メソッド / 属性
- `void onClear(nsresult status)`: (未記入)

# nsIPushService (dom/push/nsIPushService.idl)

source: dom/push/nsIPushService.idl
source-hash: eea1fc1a0ae6b9701088f663c9e51e38483216b6

- 継承: nsISupports
- 役割: A service for components to subscribe and receive push messages from web
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserGlue.sys.mjs`](../../browser/components/BrowserGlue.sys.mjs.md)

## メソッド / 属性
- `readonly attribute AString pushTopic`: Observer topic names, exported for convenience.
- `readonly attribute AString pushMessageHandledTopic`: (未記入)
- `readonly attribute AString subscriptionChangeTopic`: (未記入)
- `readonly attribute AString subscriptionModifiedTopic`: (未記入)
- `void subscribe(AString scope, nsIPrincipal principal, nsIPushSubscriptionCallback callback)`: Creates a push subscription for the given |scope| URL and |principal|.
- `void subscribeWithKey(AString scope, nsIPrincipal principal, Array<uint8_t> key, nsIPushSubscriptionCallback callback)`: Creates a restricted push subscription with the given public |key|. The
- `void unsubscribe(AString scope, nsIPrincipal principal, nsIUnsubscribeResultCallback callback)`: Removes a push subscription for the given |scope|.
- `void getSubscription(AString scope, nsIPrincipal principal, nsIPushSubscriptionCallback callback)`: Retrieves the subscription record associated with the given
- `void clearForDomain(AString domain, jsval originAttributesPattern, nsIPushClearResultCallback callback)`: Drops every subscription for the given |domain|, or all domains if
- `void clearForPrincipal(nsIPrincipal principal, nsIPushClearResultCallback callback)`: Drops every subscription for the given |principal|.

# nsIPushQuotaManager (dom/push/nsIPushService.idl)

source: dom/push/nsIPushService.idl
source-hash: eea1fc1a0ae6b9701088f663c9e51e38483216b6

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void notificationForOriginShown(string origin)`: Informs the quota manager that a notification
- `void notificationForOriginClosed(string origin)`: Informs the quota manager that a notification
