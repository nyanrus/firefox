# nsIContentBlockingAllowList (toolkit/components/antitracking/nsIContentBlockingAllowList.idl)

source: toolkit/components/antitracking/nsIContentBlockingAllowList.idl
source-hash: 90c2c60492f6eec96aff81b83da67bb7400520ae

- 継承: nsISupports
- 役割: This file contains an interface to the ContentBlockingAllowList.
- 実装: `mozilla::ContentBlockingAllowList` (toolkit/components/components.conf)
- contract ID: `@mozilla.org/content-blocking-allow-list;1`
- 使っているJS: [`browser/components/preferences/dialogs/permissions.js`](../../../browser/components/preferences/dialogs/permissions.js.md)

## メソッド / 属性
- `nsIPrincipal computeContentBlockingAllowListPrincipal(nsIPrincipal aPrincipal)`: Computes a contentBlockingAllowList principal for a given content principal.
