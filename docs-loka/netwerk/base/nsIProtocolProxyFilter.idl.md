# nsIProxyProtocolFilterResult (netwerk/base/nsIProtocolProxyFilter.idl)

source: netwerk/base/nsIProtocolProxyFilter.idl
source-hash: 9dee2da9df5b888af1d1ea619dede97582a3341a

- 継承: nsISupports
- 役割: Recipient of the result of implementers of nsIProtocolProxy(Channel)Filter
- 実装: (未記入)

## メソッド / 属性
- `void onProxyFilterResult(nsIProxyInfo aProxy)`: It's mandatory to call this method exactly once when the applyFilter()

# nsIProtocolProxyFilter (netwerk/base/nsIProtocolProxyFilter.idl)

source: netwerk/base/nsIProtocolProxyFilter.idl
source-hash: 9dee2da9df5b888af1d1ea619dede97582a3341a

- 継承: nsISupports
- 役割: This interface is used to apply filters to the proxies selected for a given
- 実装: (未記入)

## メソッド / 属性
- `void applyFilter(nsIURI aURI, nsIProxyInfo aProxy, nsIProxyProtocolFilterResult aCallback)`: This method is called to apply proxy filter rules for the given URI

# nsIProtocolProxyChannelFilter (netwerk/base/nsIProtocolProxyFilter.idl)

source: netwerk/base/nsIProtocolProxyFilter.idl
source-hash: 9dee2da9df5b888af1d1ea619dede97582a3341a

- 継承: nsISupports
- 役割: This interface is used to apply filters to the proxies selected for a given
- 実装: (未記入)
- 使っているJS: [`browser/components/newtab/SponsorProtection.sys.mjs`](../../browser/components/newtab/SponsorProtection.sys.mjs.md), [`browser/extensions/newtab/lib/ActivityStream.sys.mjs`](../../browser/extensions/newtab/lib/ActivityStream.sys.mjs.md)

## メソッド / 属性
- `void applyFilter(nsIChannel aChannel, nsIProxyInfo aProxy, nsIProxyProtocolFilterResult aCallback)`: This method is called to apply proxy filter rules for the given channel
