# nsIURIClassifierCallback (netwerk/url-classifier/nsIURIClassifier.idl)

source: netwerk/url-classifier/nsIURIClassifier.idl
source-hash: 497b32f7ff5a9dc74a0d34f292e1cbbb5daf5028

- 継承: nsISupports
- 役割: Callback function for nsIURIClassifier lookups.
- 実装: (未記入)

## メソッド / 属性
- `void onClassifyComplete(nsresult aErrorCode, ACString aList, ACString aProvider, ACString aFullHash)`: Called by the URI classifier service when it is done checking a URI.

# nsIURIClassifier (netwerk/url-classifier/nsIURIClassifier.idl)

source: netwerk/url-classifier/nsIURIClassifier.idl
source-hash: 497b32f7ff5a9dc74a0d34f292e1cbbb5daf5028

- 継承: nsISupports
- 役割: The URI classifier service checks a URI against lists of phishing
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser.js`](../../browser/base/content/browser.js.md)

## メソッド / 属性
- `boolean classify(nsIPrincipal aPrincipal, nsIURIClassifierCallback aCallback)`: Classify a Principal using its URI.
- `void asyncClassifyLocalWithFeatures(nsIURI aURI, Array<nsIUrlClassifierFeature> aFeatures, nsIUrlClassifierFeature_listType aListType, nsIUrlClassifierFeatureCallback aCallback, boolean aIdlePriority)`: Asynchronously classify a URI with list of features. This does not make
- `void asyncClassifyLocalWithFeatureNames(nsIURI aURI, Array<ACString> aFeatures, nsIUrlClassifierFeature_listType aListType, nsIUrlClassifierFeatureCallback aCallback)`: Asynchronously classify a URI with list of features. This does not make
- `nsIUrlClassifierFeature getFeatureByName(ACString aFeatureName)`: Returns a feature named aFeatureName.
- `Array<ACString> getFeatureNames()`: Returns all the feature names.
- `nsIUrlClassifierFeature createFeatureWithTables(ACString aName, Array<ACString> aBlocklistTables, Array<ACString> aEntitylistTables)`: Create a new feature with a list of tables. This method is just for
- `void sendThreatHitReport(nsIChannel aChannel, ACString aProvider, ACString aList, ACString aFullHash)`: Report to the provider that a Safe Browsing warning was shown.
