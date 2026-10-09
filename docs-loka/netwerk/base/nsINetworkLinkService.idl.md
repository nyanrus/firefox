# nsINetworkLinkService (netwerk/base/nsINetworkLinkService.idl)

source: netwerk/base/nsINetworkLinkService.idl
source-hash: 422c6a776e0e981ac6d05964e09f61820628f4ef

- 継承: nsISupports
- 役割: Network link status monitoring service.
- 実装: (未記入)
- 使っているJS: [`browser/components/firefoxview/firefox-view-synced-tabs-error-handler.sys.mjs`](../../browser/components/firefoxview/firefox-view-synced-tabs-error-handler.sys.mjs.md)

## メソッド / 属性
- `const unsigned long LINK_TYPE_UNKNOWN`: (未記入)
- `const unsigned long LINK_TYPE_ETHERNET`: (未記入)
- `const unsigned long LINK_TYPE_USB`: (未記入)
- `const unsigned long LINK_TYPE_WIFI`: (未記入)
- `const unsigned long LINK_TYPE_WIMAX`: (未記入)
- `const unsigned long LINK_TYPE_MOBILE`: (未記入)
- `readonly attribute boolean isLinkUp`: This is set to true when the system is believed to have a usable
- `readonly attribute boolean linkStatusKnown`: This is set to true when we believe that isLinkUp is accurate.
- `readonly attribute unsigned long linkType`: The type of network connection.
- `readonly attribute ACString networkID`: A string uniquely identifying the current active network interfaces.
- `readonly attribute Array<ACString> dnsSuffixList`: The list of DNS suffixes for the currently active network interfaces.
- `readonly attribute Array<NetAddr> nativeResolvers`: The IPs of the DNS resolvers currently used by the platform.
- `readonly attribute Array<nsINetAddr> resolvers`: Same as previous - returns the IPs of DNS resolvers but this time as
- `const unsigned long NONE_DETECTED`: (未記入)
- `const unsigned long VPN_DETECTED`: (未記入)
- `const unsigned long PROXY_DETECTED`: (未記入)
- `const unsigned long NRPT_DETECTED`: (未記入)
- `const unsigned long PRIVATE_DNS_DETECTED`: (未記入)
- `readonly attribute unsigned long platformDNSIndications`: A bitfield that encodes the platform attributes we detected which
