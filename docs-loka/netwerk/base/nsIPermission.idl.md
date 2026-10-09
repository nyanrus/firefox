# nsIPermission (netwerk/base/nsIPermission.idl)

source: netwerk/base/nsIPermission.idl
source-hash: 8f6e46d88c93e523d598e1b2d4eb8f326638e651

- 継承: nsISupports
- 役割: This interface defines a "permission" object,
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-siteIdentity.js`](../../browser/base/content/browser-siteIdentity.js.md), [`browser/base/content/pageinfo/permissions.js`](../../browser/base/content/pageinfo/permissions.js.md), [`browser/components/ipprotection/IPPOnboardingMessageHelper.sys.mjs`](../../browser/components/ipprotection/IPPOnboardingMessageHelper.sys.mjs.md), [`browser/components/preferences/config/privacy.mjs`](../../browser/components/preferences/config/privacy.mjs.md), [`browser/components/preferences/dialogs/permissions.js`](../../browser/components/preferences/dialogs/permissions.js.md), [`browser/components/preferences/dialogs/sitePermissions.js`](../../browser/components/preferences/dialogs/sitePermissions.js.md), [`browser/components/preferences/dialogs/translations.js`](../../browser/components/preferences/dialogs/translations.js.md), [`browser/components/preferences/translations.js`](../../browser/components/preferences/translations.js.md), [`browser/components/sidebar/sidebar-permissions.mjs`](../../browser/components/sidebar/sidebar-permissions.mjs.md), [`browser/extensions/ipp-activator/extension/api/parent/ext-ipp.js`](../../browser/extensions/ipp-activator/extension/api/parent/ext-ipp.js.md), [`browser/modules/SitePermissions.sys.mjs`](../../browser/modules/SitePermissions.sys.mjs.md)

## メソッド / 属性
- `readonly attribute nsIPrincipal principal`: The principal for which this permission applies.
- `readonly attribute ACString type`: a case-sensitive ASCII string, indicating the type of permission
- `readonly attribute uint32_t capability`: The permission (see nsIPermissionManager.idl for allowed values)
- `readonly attribute uint32_t expireType`: The expiration type of the permission (session, time-based or none).
- `readonly attribute int64_t expireTime`: The expiration time of the permission (milliseconds since Jan 1 1970
- `readonly attribute int64_t modificationTime`: The last modification time of the permission (milliseconds since Jan 1 1970
- `readonly attribute uint64_t browserId`: The BrowserId this permission is scoped to, or 0 for global
- `boolean matches(nsIPrincipal principal, boolean exactHost)`: Test whether a principal would be affected by this permission.
- `boolean matchesURI(nsIURI uri, boolean exactHost)`: Test whether a URI would be affected by this permission.
