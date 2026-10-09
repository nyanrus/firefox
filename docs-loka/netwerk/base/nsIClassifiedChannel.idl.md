# nsIClassifiedChannel (netwerk/base/nsIClassifiedChannel.idl)

source: netwerk/base/nsIClassifiedChannel.idl
source-hash: d43bad0257b3bdfdda4d3f40dd9af695a63549c5

- 継承: nsISupports
- 役割: nsIClassifiedChannel
- 実装: (未記入)
- 使っているJS: [`browser/actors/BlockedSiteChild.sys.mjs`](../../browser/actors/BlockedSiteChild.sys.mjs.md)

## メソッド / 属性
- `void setMatchedInfo(ACString aList, ACString aProvider, ACString aFullHash)`: Sets matched info of the classified channel.
- `readonly attribute ACString matchedList`: Name of the list that matched
- `readonly attribute ACString matchedProvider`: Name of provider that matched
- `readonly attribute ACString matchedFullHash`: Full hash of URL that matched
- `void setMatchedTrackingInfo(Array<ACString> aLists, Array<ACString> aFullHashes)`: Sets matched tracking info of the classified channel.
- `readonly attribute Array<ACString> matchedTrackingLists`: Name of the lists that matched
- `readonly attribute Array<ACString> matchedTrackingFullHashes`: Full hash of URLs that matched
- `readonly attribute unsigned long firstPartyClassificationFlags`: Returns the classification flags if the channel has been processed by
- `readonly attribute unsigned long thirdPartyClassificationFlags`: Returns the classification flags if the channel has been processed by
- `readonly attribute unsigned long classificationFlags`: (未記入)
- `boolean isThirdPartyTrackingResource()`: Returns true  if the channel has been processed by URL-Classifier features
- `boolean isThirdPartySocialTrackingResource()`: Returns true if the channel has loaded a 3rd party resource that is
