# nsIContentPrefObserver (dom/interfaces/base/nsIContentPrefService2.idl)

source: dom/interfaces/base/nsIContentPrefService2.idl
source-hash: a42a77396fdaa288f08642e9dcc1fd412d6a64c3

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void onContentPrefSet(AString aGroup, AString aName, nsIVariant aValue, boolean aIsPrivate)`: Called when a content pref is set to a different value.
- `void onContentPrefRemoved(AString aGroup, AString aName, boolean aIsPrivate)`: Called when a content pref is removed.

# nsIContentPrefService2 (dom/interfaces/base/nsIContentPrefService2.idl)

source: dom/interfaces/base/nsIContentPrefService2.idl
source-hash: a42a77396fdaa288f08642e9dcc1fd412d6a64c3

- 継承: nsISupports
- 役割: Content Preferences
- 実装: (未記入)
- 使っているJS: [`browser/components/tabbrowser/content/browser-fullZoom.js`](../../../browser/components/tabbrowser/content/browser-fullZoom.js.md)

## メソッド / 属性
- `const unsigned short GROUP_NAME_MAX_LENGTH`: Group (called "domain" in this interface) names longer than this will be
- `void getByName(AString name, nsILoadContext context, nsIContentPrefCallback2 callback)`: Gets all the preferences with the given name.
- `void getByDomainAndName(AString domain, AString name, nsILoadContext context, nsIContentPrefCallback2 callback)`: Gets the preference with the given domain and name.
- `void getBySubdomainAndName(AString domain, AString name, nsILoadContext context, nsIContentPrefCallback2 callback)`: Gets all preferences with the given name whose domains are either the same
- `void getGlobal(AString name, nsILoadContext context, nsIContentPrefCallback2 callback)`: Gets the preference with no domain and the given name.
- `nsIContentPref getCachedByDomainAndName(AString domain, AString name, nsILoadContext context)`: Synchronously retrieves from the in-memory cache the preference with the
- `Array<nsIContentPref> getCachedBySubdomainAndName(AString domain, AString name, nsILoadContext context)`: Synchronously retrieves from the in-memory cache all preferences with the
- `nsIContentPref getCachedGlobal(AString name, nsILoadContext context)`: Synchronously retrieves from the in-memory cache the preference with no
- `void set(AString domain, AString name, nsIVariant value, nsILoadContext context, nsIContentPrefCallback2 callback)`: Sets a preference.
- `void setGlobal(AString name, nsIVariant value, nsILoadContext context, nsIContentPrefCallback2 callback)`: Sets a preference with no domain.
- `void removeByDomainAndName(AString domain, AString name, nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes the preference with the given domain and name.
- `void removeBySubdomainAndName(AString domain, AString name, nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes all the preferences with the given name whose domains are either
- `void removeGlobal(AString name, nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes the preference with no domain and the given name.
- `void removeByDomain(AString domain, nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes all preferences with the given domain.
- `void removeBySubdomain(AString domain, nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes all preferences whose domains are either the same as or subdomains
- `void removeByName(AString name, nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes all preferences with the given name regardless of domain, including
- `void removeAllDomains(nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes all non-global preferences -- in other words, all preferences that
- `void removeAllDomainsSince(unsigned long long since, nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes all non-global preferences created after and including |since|.
- `void removeAllGlobals(nsILoadContext context, nsIContentPrefCallback2 callback)`: Removes all global preferences -- in other words, all preferences that have
- `void addObserverForName(AString name, nsIContentPrefObserver observer)`: Registers an observer that will be notified whenever a preference with the
- `void removeObserverForName(AString name, nsIContentPrefObserver observer)`: Unregisters an observer for the given name.
- `AString extractDomain(AString str)`: Extracts and returns the domain from the given string representation of a

# nsIContentPrefCallback2 (dom/interfaces/base/nsIContentPrefService2.idl)

source: dom/interfaces/base/nsIContentPrefService2.idl
source-hash: a42a77396fdaa288f08642e9dcc1fd412d6a64c3

- 継承: nsISupports
- 役割: The callback used by the above methods.
- 実装: (未記入)

## メソッド / 属性
- `void handleResult(nsIContentPref pref)`: For the retrieval methods, this is called once for each retrieved
- `void handleError(nsresult error)`: Called when an error occurs.  This may be called multiple times before
- `void handleCompletion(unsigned short reason)`: Called when the method finishes.  This will be called exactly once for
- `const unsigned short COMPLETE_OK`: (未記入)
- `const unsigned short COMPLETE_ERROR`: (未記入)

# nsIContentPref (dom/interfaces/base/nsIContentPrefService2.idl)

source: dom/interfaces/base/nsIContentPrefService2.idl
source-hash: a42a77396fdaa288f08642e9dcc1fd412d6a64c3

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString domain`: (未記入)
- `readonly attribute AString name`: (未記入)
- `readonly attribute nsIVariant value`: (未記入)
