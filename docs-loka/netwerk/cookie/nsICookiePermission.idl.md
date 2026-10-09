# nsICookiePermission (netwerk/cookie/nsICookiePermission.idl)

source: netwerk/cookie/nsICookiePermission.idl
source-hash: dc9b2b0a1bdd72f7acf626855148e9fc1649761f

- 継承: nsISupports
- 役割: An interface to test for cookie permissions
- 実装: (未記入)
- 使っているJS: [`browser/base/content/pageinfo/pageInfo.js`](../../browser/base/content/pageinfo/pageInfo.js.md), [`browser/components/ProfileDataUpgrader.sys.mjs`](../../browser/components/ProfileDataUpgrader.sys.mjs.md), [`browser/components/StartupTelemetry.sys.mjs`](../../browser/components/StartupTelemetry.sys.mjs.md), [`browser/components/enterprisepolicies/Policies.sys.mjs`](../../browser/components/enterprisepolicies/Policies.sys.mjs.md), [`browser/components/preferences/dialogs/permissions.js`](../../browser/components/preferences/dialogs/permissions.js.md), [`browser/modules/Sanitizer.sys.mjs`](../../browser/modules/Sanitizer.sys.mjs.md), [`browser/modules/SitePermissions.sys.mjs`](../../browser/modules/SitePermissions.sys.mjs.md)

## メソッド / 属性
- `const nsCookieAccess ACCESS_DEFAULT`: nsCookieAccess values
- `const nsCookieAccess ACCESS_ALLOW`: (未記入)
- `const nsCookieAccess ACCESS_DENY`: (未記入)
- `const nsCookieAccess ACCESS_SESSION`: additional values for nsCookieAccess which may not match
