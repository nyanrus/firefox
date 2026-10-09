# nsIUrlListManager (toolkit/components/url-classifier/nsIUrlListManager.idl)

source: toolkit/components/url-classifier/nsIUrlListManager.idl
source-hash: 614d4f09ec29d602a7ce5cc81dc105c6523c0af2

- 継承: nsISupports
- 役割: Interface for a class that manages updates of the url classifier database.
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/privacy.mjs`](../../../browser/components/preferences/config/privacy.mjs.md), [`browser/components/preferences/preferences.js`](../../../browser/components/preferences/preferences.js.md)

## メソッド / 属性
- `ACString getGethashUrl(ACString tableName)`: Get the gethash url for this table
- `ACString getUpdateUrl(ACString tableName)`: Get the update url for this table
- `boolean registerTable(ACString tableName, ACString providerName, ACString updateUrl, ACString gethashUrl)`: Add a table to the list of tables we are managing. The name is a
- `void unregisterTable(ACString tableName)`: Unregister table from the list
- `void enableUpdate(ACString tableName)`: Turn on update checking for a table. I.e., during the next server
- `void disableAllUpdates()`: Turn off update checking for all tables.
- `void disableUpdate(ACString tableName)`: Turn off update checking for a single table. Only used in tests.
- `void maybeToggleUpdateChecking()`: Toggle update checking, if necessary.
- `boolean checkForUpdates(ACString updateUrl)`: This is currently used by about:url-classifier to force an update
- `boolean forceUpdates(ACString tableNames)`: Force updates for the given tables, updates are still restricted to
- `uint64_t getBackOffTime(ACString provider)`: This is currently used by about:url-classifier to get back-off time
- `boolean isRegistered()`: Return true if someone registers a table, this is used by testcase
