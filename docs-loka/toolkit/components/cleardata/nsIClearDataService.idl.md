# nsIClearDataService (toolkit/components/cleardata/nsIClearDataService.idl)

source: toolkit/components/cleardata/nsIClearDataService.idl
source-hash: 03fe88bbe0c9b5aac81fbef2f962508026b28507

- 継承: nsISupports
- 役割: nsIClearDataService
- 実装: `clearData` (toolkit/components/cleardata/components.conf)
- contract ID: `@mozilla.org/clear-data-service;1`
- 使っているJS: [`browser/fxr/content/prefs.js`](../../../browser/fxr/content/prefs.js.md), [`browser/modules/Sanitizer.sys.mjs`](../../../browser/modules/Sanitizer.sys.mjs.md), [`browser/modules/SiteDataManager.sys.mjs`](../../../browser/modules/SiteDataManager.sys.mjs.md)

## メソッド / 属性
- `void deleteDataFromLocalFiles(boolean aIsUserRequest, uint32_t aFlags, nsIClearDataCallback aCallback)`: Delete data owned by local files or other hostless schemes.
- `void deleteDataFromHost(AUTF8String aHost, boolean aIsUserRequest, uint32_t aFlags, nsIClearDataCallback aCallback)`: Delete data owned by a host. For instance: mozilla.org. Data from any
- `void deleteDataFromSite(AUTF8String aSchemelessSite, jsval aOriginAttributesPattern, boolean aIsUserRequest, uint32_t aFlags, nsIClearDataCallback aCallback)`: Delete data from cookie jars associated with the given schemeless site
- `void deleteDataFromSiteAndOriginAttributesPatternString(AUTF8String aSchemelessSite, AString aOriginAttributesPatternString, boolean aIsUserRequest, uint32_t aFlags, nsIClearDataCallback aCallback)`: Variant of deleteDataFromSite that accepts a JSON string for the OriginAttributesPattern.
- `void deleteDataFromPrincipal(nsIPrincipal aPrincipal, boolean aIsUserRequest, uint32_t aFlags, nsIClearDataCallback aCallback)`: Delete data owned by a principal.
- `void deleteDataInTimeRange(PRTime aFrom, PRTime aTo, boolean aIsUserRequest, uint32_t aFlags, nsIClearDataCallback aCallback)`: Delete all data in a time range. Limit excluded.
- `void deleteData(uint32_t aFlags, nsIClearDataCallback aCallback)`: Delete all data from any host, in any time range.
- `void deleteDataFromOriginAttributesPattern(jsval aOriginAttributesPattern, nsIClearDataCallback aCallback)`: Delete all data from an OriginAttributesPatternDictionary.
- `void deleteUserInteractionForClearingHistory(Array<nsIPrincipal> aPrincipalsWithStorage, PRTime aFrom, nsIClearDataCallback aCallback)`: This is a helper function to clear storageAccessAPI permissions
- `void cleanupAfterDeletionAtShutdown(uint32_t aFlags, nsIClearDataCallback aCallback)`: Some cleaners, namely QuotaCleaner, can opt in and treat things as deleted
- `void clearPrivateBrowsingData(nsIClearDataCallback aCallback)`: Clear all private browsing data by firing "last-pb-context-exited"
- `boolean hostMatchesSite(AUTF8String aHost, jsval aOriginAttributes, AUTF8String aSchemelessSite, jsval aOriginAttributesPattern)`: Match a host and OriginAttributes against a schemeless site and
- `const uint32_t CLEAR_COOKIES`: Listed below are the various flags which may be or'd together.
- `const uint32_t CLEAR_NETWORK_CACHE`: Network Cache.
- `const uint32_t CLEAR_BFCACHE`: Clear bfcache.
- `const uint32_t CLEAR_IMAGE_CACHE`: Image cache.
- `const uint32_t CLEAR_JS_CACHE`: In-memory JS cache.
- `const uint32_t CLEAR_DOWNLOADS`: Completed downloads.
- `const uint32_t CLEAR_TLS_TOKEN_CACHE`: TLS session resumption tokens cached by SSLTokensCache.
- `const uint32_t CLEAR_MEDIA_DEVICES`: Media devices.
- `const uint32_t CLEAR_DOM_QUOTA`: LocalStorage, IndexedDB, ServiceWorkers, DOM Cache and so on.
- `const uint32_t CLEAR_DOM_PUSH_NOTIFICATIONS`: DOM Push notifications
- `const uint32_t CLEAR_HISTORY`: Places history
- `const uint32_t CLEAR_MESSAGING_LAYER_SECURITY_STATE`: Messaging Layer Security state
- `const uint32_t CLEAR_AUTH_TOKENS`: Auth tokens
- `const uint32_t CLEAR_AUTH_CACHE`: Login cache
- `const uint32_t CLEAR_SITE_PERMISSIONS`: Clear Site permissions. Excludes permissions which are used as shutdown data clearing exceptions.
- `const uint32_t CLEAR_CONTENT_PREFERENCES`: Site preferences
- `const uint32_t CLEAR_HSTS`: Clear HSTS data
- `const uint32_t CLEAR_EME`: Media plugin data
- `const uint32_t CLEAR_REPORTS`: Reporting API reports.
- `const uint32_t CLEAR_STORAGE_ACCESS`: StorageAccessAPI flag, which indicates user interaction.
- `const uint32_t CLEAR_CERT_EXCEPTIONS`: Clear Cert Exceptions.
- `const uint32_t CLEAR_CONTENT_BLOCKING_RECORDS`: Clear entries in the content blocking database.
- `const uint32_t CLEAR_CSS_CACHE`: Clear the in-memory CSS cache.
- `const uint32_t CLEAR_PREFLIGHT_CACHE`: Clear the CORS preflight cache.
- `const uint32_t CLEAR_CLIENT_AUTH_REMEMBER_SERVICE`: Forget descision about clients authentification certificate
- `const uint32_t CLEAR_CREDENTIAL_MANAGER_STATE`: Clear state associated with FedCM
- `const uint32_t CLEAR_FINGERPRINTING_PROTECTION_STATE`: Clear state associated with the fingerprinting protection.
- `const uint32_t CLEAR_BOUNCE_TRACKING_PROTECTION_STATE`: Clear the bounce tracking protection state.
- `const uint32_t CLEAR_STORAGE_PERMISSIONS`: Clear permissions of type "persistent-storage" and "storage-access"
- `const uint32_t CLEAR_SHUTDOWN_EXCEPTIONS`: Clear permissions of type "cookie" used for manual cookie rules and shutdown exceptions
- `const uint32_t CLEAR_ALL`: Use this value to delete all the data.
- `const uint32_t CLEAR_PERMISSIONS`: The following flags are helpers: they combine some of the previous flags
- `const uint32_t CLEAR_ALL_CACHES`: Delete all the possible caches.
- `const uint32_t CLEAR_DOM_STORAGES`: Delete all DOM storages
- `const uint32_t CLEAR_FORGET_ABOUT_SITE`: Helper flag for forget about site
- `const uint32_t CLEAR_COOKIES_AND_SITE_DATA`: Helper flag for clearing cookies and site data.
- `const uint32_t CLEAR_STATE_FOR_TRACKER_PURGING`: Helper flag for tracker purging

# nsIClearDataCallback (toolkit/components/cleardata/nsIClearDataService.idl)

source: toolkit/components/cleardata/nsIClearDataService.idl
source-hash: 03fe88bbe0c9b5aac81fbef2f962508026b28507

- 継承: nsISupports
- 役割: This is a companion interface for
- 実装: (未記入)

## メソッド / 属性
- `void onDataDeleted(uint32_t aFailedFlags)`: Called to indicate that the data cleaning is completed.

# nsIPBMCleanupCallback (toolkit/components/cleardata/nsIClearDataService.idl)

source: toolkit/components/cleardata/nsIClearDataService.idl
source-hash: 03fe88bbe0c9b5aac81fbef2f962508026b28507

- 継承: nsISupports
- 役割: Callback returned by nsIPBMCleanupCollector.addPendingCleanup().
- 実装: (未記入)

## メソッド / 属性
- `void complete(nsresult aStatus)`: (未記入)

# nsIPBMCleanupCollector (toolkit/components/cleardata/nsIClearDataService.idl)

source: toolkit/components/cleardata/nsIClearDataService.idl
source-hash: 03fe88bbe0c9b5aac81fbef2f962508026b28507

- 継承: nsISupports
- 役割: Passed as aSubject in the "last-pb-context-exited" notification when
- 実装: (未記入)

## メソッド / 属性
- `nsIPBMCleanupCallback addPendingCleanup()`: (未記入)
