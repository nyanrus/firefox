# nsIUrlClassifierBlockedChannel (netwerk/url-classifier/nsIChannelClassifierService.idl)

source: netwerk/url-classifier/nsIChannelClassifierService.idl
source-hash: 341f4ab7ccec0974060c466cd9aca1b2899a941c

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/extensions/webcompat/experiment-apis/trackingProtection.js`](../../browser/extensions/webcompat/experiment-apis/trackingProtection.js.md)

## メソッド / 属性
- `const unsigned long TRACKING_PROTECTION`: (未記入)
- `const unsigned long SOCIAL_TRACKING_PROTECTION`: (未記入)
- `const unsigned long FINGERPRINTING_PROTECTION`: (未記入)
- `const unsigned long CRYPTOMINING_PROTECTION`: (未記入)
- `readonly attribute uint8_t reason`: (未記入)
- `readonly attribute ACString tables`: (未記入)
- `readonly attribute AString url`: (未記入)
- `readonly attribute uint64_t tabId`: (未記入)
- `readonly attribute uint64_t channelId`: (未記入)
- `readonly attribute boolean isPrivateBrowsing`: (未記入)
- `readonly attribute AString topLevelUrl`: (未記入)
- `readonly attribute uint64_t browserId`: (未記入)
- `readonly attribute nsIChannel channel`: (未記入)
- `void replace()`: (未記入)
- `void allow()`: (未記入)

# nsIChannelClassifierService (netwerk/url-classifier/nsIChannelClassifierService.idl)

source: netwerk/url-classifier/nsIChannelClassifierService.idl
source-hash: 341f4ab7ccec0974060c466cd9aca1b2899a941c

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/extensions/webcompat/experiment-apis/trackingProtection.js`](../../browser/extensions/webcompat/experiment-apis/trackingProtection.js.md)

## メソッド / 属性
- `void addListener(nsIObserver aObserver)`: (未記入)
- `void removeListener(nsIObserver aObserver)`: (未記入)
