# nsIPermissionManager (netwerk/base/nsIPermissionManager.idl)

source: netwerk/base/nsIPermissionManager.idl
source-hash: 8526c563e235640866b671dda1fe84a3a8e99618

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/actors/BlockedSiteParent.sys.mjs`](../../browser/actors/BlockedSiteParent.sys.mjs.md), [`browser/base/content/browser-captivePortal.js`](../../browser/base/content/browser-captivePortal.js.md), [`browser/components/preferences/config/privacy.mjs`](../../browser/components/preferences/config/privacy.mjs.md), [`browser/components/preferences/dialogs/permissions.js`](../../browser/components/preferences/dialogs/permissions.js.md), [`browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs`](../../browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs.md), [`browser/modules/CanvasPermissionPromptHelper.sys.mjs`](../../browser/modules/CanvasPermissionPromptHelper.sys.mjs.md), [`browser/modules/PermissionUI.sys.mjs`](../../browser/modules/PermissionUI.sys.mjs.md), [`browser/modules/Sanitizer.sys.mjs`](../../browser/modules/Sanitizer.sys.mjs.md)

## メソッド / 属性
- `const uint32_t UNKNOWN_ACTION`: Predefined return values for the testPermission method and for
- `const uint32_t ALLOW_ACTION`: (未記入)
- `const uint32_t DENY_ACTION`: (未記入)
- `const uint32_t PROMPT_ACTION`: (未記入)
- `const uint32_t MAX_VALID_ACTION`: (未記入)
- `const uint32_t EXPIRE_NEVER`: Predefined expiration types for permissions.  Permissions can be permanent
- `const uint32_t EXPIRE_SESSION`: (未記入)
- `const uint32_t EXPIRE_TIME`: (未記入)
- `const uint32_t EXPIRE_POLICY`: (未記入)
- `const uint32_t EXPIRE_SESSION_TAB`: (未記入)
- `Array<nsIPermission> getAllForPrincipal(nsIPrincipal principal)`: Get all custom permissions for a given nsIPrincipal. This will return an
- `Array<nsIPermission> getAllWithTypePrefix(ACString prefix)`: Get all custom permissions of a specific type, specified with a prefix
- `Array<nsIPermission> getAllByTypes(Array<ACString> types)`: Get all custom permissions whose type exactly match one of the types defined
- `Array<nsIPermission> getAllByTypeSince(ACString type, int64_t since)`: Get all custom permissions of a specific type and that were modified after
- `void addFromPrincipal(nsIPrincipal principal, ACString type, uint32_t permission, uint32_t expireType, int64_t expireTime)`: Add permission information for a given principal.
- `void testAddFromPrincipalByTime(nsIPrincipal principal, ACString type, uint32_t permission, int64_t modificationTime)`: Test method to add a permission for a given principal with custom modification time.
- `void addFromPrincipalAndPersistInPrivateBrowsing(nsIPrincipal principal, ACString type, uint32_t permission)`: Add permanent permission information for a given principal in private
- `void addDefaultFromPrincipal(nsIPrincipal principal, ACString type, uint32_t permission)`: Add temporary default permission information for a given principal.
- `void removeFromPrincipal(nsIPrincipal principal, ACString type)`: Remove permission information for a given principal.
- `void removePermission(nsIPermission perm)`: Remove the given permission from the permission manager.
- `void removeAll()`: Clear permission information for all websites.
- `void removeAllSince(int64_t since)`: Clear all permission information added since the specified time.
- `void removeByType(ACString type)`: Clear all permissions of the passed type.
- `void removeAllExceptTypes(Array<ACString> typeExceptions)`: Clear all permissions not of the passed types.
- `void removeByTypeSince(ACString type, int64_t since)`: Clear all permissions of the passed type added since the specified time.
- `void removeAllSinceWithTypeExceptions(int64_t since, Array<ACString> typeExceptions)`: Clear all permissions of the passed types added since the specified time.
- `uint32_t testPermissionFromPrincipal(nsIPrincipal principal, ACString type)`: Test whether the principal has the permission to perform a given action.
- `uint32_t testExactPermissionFromPrincipal(nsIPrincipal principal, ACString type)`: Test whether the principal has the permission to perform a given action.
- `uint32_t testExactPermanentPermission(nsIPrincipal principal, ACString type)`: Test whether a website has permission to perform the given action
- `nsIPermission getPermissionObject(nsIPrincipal principal, ACString type, boolean exactHost)`: Get the permission object associated with the given principal and action.
- `readonly attribute Array<nsIPermission> all`: Returns all stored permissions.
- `void removePermissionsWithAttributes(AString patternAsJSON, Array<ACString> typeInclusions, Array<ACString> typeExceptions)`: Remove all permissions that will match the origin pattern.
- `void updateLastInteractionForPrincipal(nsIPrincipal principal)`: Update the last interaction time for a given principal's origin.
- `Promise removeOrphanedInteractionRecords()`: Remove interaction records from the moz_origin_interactions table
- `Promise testFlushPendingWrites()`: Test-only method. Flush all pending background-thread writes and resolve
- `void addFromPrincipalForBrowser(nsIPrincipal principal, ACString type, uint32_t permission, uint64_t browserId, int64_t expireTimeMS)`: Add a permission scoped to a specific browser (tab).
- `void removeFromPrincipalForBrowser(nsIPrincipal principal, ACString type, uint64_t browserId)`: Remove a browser-scoped permission for the given principal, type, and
- `void removeAllForBrowser(uint64_t browserId)`: Remove all browser-scoped permissions for a given browser (tab).
- `void removeByActionForBrowser(uint64_t browserId, uint32_t permission)`: Remove all browser-scoped permissions with the given action for a browser.
- `uint32_t testForBrowser(nsIPrincipal principal, ACString type, uint64_t browserId)`: Test for a browser-scoped permission. Returns the permission action
- `nsIPermission getForBrowser(nsIPrincipal principal, ACString type, uint64_t browserId)`: Get a browser-scoped permission as an nsIPermission object.
- `Array<nsIPermission> getAllForBrowser(nsIPrincipal principal, uint64_t browserId)`: Get all browser-scoped permissions for a given principal and browser,
- `void copyBrowserPermissions(uint64_t srcBrowserId, uint64_t destBrowserId)`: Copy all browser-scoped permissions from one browser to another.
