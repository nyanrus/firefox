# nsIUrlClassifierExceptionListObserver (netwerk/url-classifier/nsIUrlClassifierExceptionListService.idl)

source: netwerk/url-classifier/nsIUrlClassifierExceptionListService.idl
source-hash: 88387f13115d4bf3ba6257e98183223bd38b6b12

- 継承: nsISupports
- 役割: Observer for exception list updates.
- 実装: (未記入)

## メソッド / 属性
- `void onExceptionListUpdate(nsIUrlClassifierExceptionList aList)`: Called by nsIUrlClassifierExceptionListService when the exception list

# nsIUrlClassifierExceptionListService (netwerk/url-classifier/nsIUrlClassifierExceptionListService.idl)

source: netwerk/url-classifier/nsIUrlClassifierExceptionListService.idl
source-hash: 88387f13115d4bf3ba6257e98183223bd38b6b12

- 継承: nsISupports
- 役割: A service that monitors updates to the exception list of url-classifier
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/privacy.js`](../../browser/components/preferences/privacy.js.md)

## メソッド / 属性
- `void registerAndRunExceptionListObserver(ACString aFeature, ACString aPrefName, nsIUrlClassifierExceptionListObserver aObserver)`: Register a new observer to exception list updates. When the observer is
- `void unregisterExceptionListObserver(ACString aFeature, nsIUrlClassifierExceptionListObserver aObserver)`: Unregister an observer.
- `void clear()`: Clear all data in the service.
- `void maybeMigrateCategoryPrefs()`: Manually trigger the category prefs migration if it hasn't been run yet.
