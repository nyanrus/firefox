# nsIHttpsOnlyModePermission (dom/security/nsIHttpsOnlyModePermission.idl)

source: dom/security/nsIHttpsOnlyModePermission.idl
source-hash: 4e48946634f1b24030cfd668a02dc1fdb4abae00

- 継承: nsISupports
- 役割: HTTPS-Only/First permission types
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-siteIdentity.js`](../../browser/base/content/browser-siteIdentity.js.md), [`browser/base/content/browser-trustPanel.js`](../../browser/base/content/browser-trustPanel.js.md), [`browser/components/preferences/dialogs/permissions.js`](../../browser/components/preferences/dialogs/permissions.js.md)

## メソッド / 属性
- `const uint32_t LOAD_INSECURE_DEFAULT`: nsIPermissionManager permission values
- `const uint32_t LOAD_INSECURE_ALLOW`: (未記入)
- `const uint32_t LOAD_INSECURE_BLOCK`: (未記入)
- `const uint32_t LOAD_INSECURE_ALLOW_SESSION`: additional values which do not match
- `const uint32_t HTTPSFIRST_LOAD_INSECURE_ALLOW`: While LOAD_INSECURE_ALLOW and LOAD_INSECURE_ALLOW_SESSION apply to both
