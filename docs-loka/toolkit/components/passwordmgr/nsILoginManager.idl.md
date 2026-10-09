# nsILoginSearchCallback (toolkit/components/passwordmgr/nsILoginManager.idl)

source: toolkit/components/passwordmgr/nsILoginManager.idl
source-hash: 0bd35fbfccf22c3ae5de4cf0486001ac806aecd5

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void onSearchComplete(Array<nsILoginInfo> aLogins)`: Called when a search is complete and the results are ready.

# nsILoginManager (toolkit/components/passwordmgr/nsILoginManager.idl)

source: toolkit/components/passwordmgr/nsILoginManager.idl
source-hash: 0bd35fbfccf22c3ae5de4cf0486001ac806aecd5

- 継承: nsISupports
- 役割: (未記入)
- 実装: `logins` (toolkit/components/passwordmgr/components.conf)
- contract ID: `@mozilla.org/login-manager;1`

## メソッド / 属性
- `readonly attribute Promise initializationPromise`: This promise is resolved when initialization is complete, and is rejected
- `Promise addLoginAsync(nsILoginInfo aLogin)`: Like addLogin, but asynchronous.
- `Promise addLogins(jsval aLogins)`: Like addLogin, but asynchronous and for many logins.
- `Promise removeLoginAsync(nsILoginInfo aLogin)`: Remove a login from the login manager.
- `Promise modifyLoginAsync(nsILoginInfo oldLogin, nsISupports newLoginData)`: Like modifyLogin, but asynchronous.
- `Promise recordPasswordUseAsync(nsILoginInfo aLogin, boolean aPrivateContextWithoutExplicitConsent, AString aLoginType, boolean aFilled)`: Record that the password of a saved login was used (e.g. submitted or copied).
- `Promise removeAllUserFacingLoginsAsync()`: Remove all stored user facing logins.
- `Promise removeAllLoginsAsync()`: Completely remove all logins, including the user's FxA Sync key.
- `Promise getAllLogins()`: Fetch all logins in the login manager. An array is always returned;
- `void getAllLoginsWithCallback(nsILoginSearchCallback aCallback)`: Like getAllLogins, but with a callback returning the search results.
- `Promise reencryptAllLogins()`: For migration purposes, asynchronously reencrypt all logins in the
- `Promise listInvalidOrigins()`: Debug helper to identify logins with invalid origin/formActionOrigin URLs.
- `Array<AString> getAllDisabledHosts()`: Obtain a list of all origins for which password saving is disabled.
- `boolean getLoginSavingEnabled(AString aHost)`: Check to see if saving logins has been disabled for an origin.
- `void setLoginSavingEnabled(AString aHost, boolean isEnabled)`: Disable (or enable) storing logins for the specified origin. When
- `Array<nsILoginInfo> findLogins(AString aOrigin, AString aActionOrigin, AString aHttpRealm)`: Search for logins matching the specified criteria. Called when looking
- `Promise countLoginsAsync(AString aOrigin, AString aActionOrigin, AString aHttpRealm)`: Search for logins matching the specified criteria, as with
- `Promise searchLoginsAsync(jsval matchData)`: Asynchonously search for logins in the login manager. The Promise always
- `Promise getSyncID()`: Returns the "sync id" used by Sync to know whether the store is current with
- `Promise setSyncID(AString syncID)`: Sets the "sync id" used by Sync to know whether the store is current with
- `Promise getLastSync()`: Returns the timestamp of the last sync as a double (in seconds since Epoch
- `Promise setLastSync(double timestamp)`: Sets the timestamp of the last sync.
- `Promise ensureCurrentSyncID(AString newSyncID)`: Ensures that the local sync ID for the engine matches the sync ID for
- `Promise addPotentiallyVulnerablePassword(nsILoginInfo aLogin)`: Mark a login's password as potentially vulnerable (breached).
- `Promise isPotentiallyVulnerablePassword(nsILoginInfo aLogin)`: Check if a login's password is potentially vulnerable.
- `Promise recordBreachAlertDismissal(AString aLoginGUID)`: Record that a breach alert for a login was dismissed by the user.
- `Promise getBreachAlertDismissalsByLoginGUID()`: Get all breach alert dismissals keyed by login GUID.
- `Promise arePotentiallyVulnerablePasswords(jsval aLogins)`: Check which of the given logins have potentially vulnerable passwords.
- `Promise clearAllPotentiallyVulnerablePasswords()`: Clear all potentially vulnerable password records.
- `readonly attribute boolean uiBusy`: True when a primary password prompt is being displayed.
- `readonly attribute boolean isLoggedIn`: True when the primary password has already been entered, and so a caller
