# nsIBounceTrackingProtection (toolkit/components/antitracking/bouncetrackingprotection/nsIBounceTrackingProtection.idl)

source: toolkit/components/antitracking/bouncetrackingprotection/nsIBounceTrackingProtection.idl
source-hash: 5cb25638bd41d27ef38354a941aacbbfc23a9cb2

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/protections/ContentBlockingPrefs.sys.mjs`](../../../../browser/components/protections/ContentBlockingPrefs.sys.mjs.md)

## メソッド / 属性
- `void clearAll()`: (未記入)
- `void clearBySiteHostAndOriginAttributes(ACString aSiteHost, jsval originAttributes)`: (未記入)
- `void clearBySiteHostAndOriginAttributesPattern(ACString aSiteHost, jsval aOriginAttributesPattern)`: (未記入)
- `void clearByTimeRange(PRTime aFrom, PRTime aTo)`: (未記入)
- `void clearByOriginAttributesPattern(AString aPattern)`: (未記入)
- `void addSiteHostExceptions(Array<ACString> aSiteHosts)`: (未記入)
- `void removeSiteHostExceptions(Array<ACString> aSiteHosts)`: (未記入)
- `boolean hasRecentlyPurgedSite(ACString aSiteHost)`: (未記入)
- `Array<nsIBounceTrackingPurgeEntry> getRecentPurgedChainEntriesForSite(ACString aSiteHost)`: (未記入)
- `Array<ACString> testGetSiteHostExceptions()`: (未記入)
- `Promise testRunPurgeBounceTrackers()`: (未記入)
- `void testClearExpiredUserActivations()`: (未記入)
- `Array<nsIBounceTrackingMapEntry> testGetBounceTrackerCandidateHosts(jsval originAttributes)`: (未記入)
- `Array<nsIBounceTrackingMapEntry> testGetUserActivationHosts(jsval originAttributes)`: (未記入)
- `void testAddBounceTrackerCandidate(jsval originAttributes, ACString aSiteHost, PRTime aBounceTime)`: (未記入)
- `void testAddUserActivation(jsval originAttributes, ACString aSiteHost, PRTime aActivationTime)`: (未記入)
- `Array<nsIBounceTrackingPurgeEntry> testGetRecentlyPurgedTrackers(jsval originAttributes)`: (未記入)
- `void testMaybeMigrateUserInteractionPermissions()`: (未記入)
