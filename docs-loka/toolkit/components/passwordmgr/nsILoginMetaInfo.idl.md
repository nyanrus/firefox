# nsILoginMetaInfo (toolkit/components/passwordmgr/nsILoginMetaInfo.idl)

source: toolkit/components/passwordmgr/nsILoginMetaInfo.idl
source-hash: c488f95932718c940f673aec92b138d32b1b2281

- 継承: nsISupports
- 役割: An object containing metainfo for a login stored by the login manager.
- 実装: (未記入)
- 使っているJS: [`browser/components/aboutlogins/AboutLoginsParent.sys.mjs`](../../../browser/components/aboutlogins/AboutLoginsParent.sys.mjs.md)

## メソッド / 属性
- `attribute AString guid`: The GUID to uniquely identify the login. This can be any arbitrary
- `attribute unsigned long long timeCreated`: The time, in Unix Epoch milliseconds, when the login was first created.
- `attribute unsigned long long timeLastUsed`: The time, in Unix Epoch milliseconds, when the login was last submitted
- `attribute unsigned long long timePasswordChanged`: The time, in Unix Epoch milliseconds, when the login was last modified.
- `attribute unsigned long timesUsed`: The number of times the login was submitted in a form or used to begin
- `attribute unsigned long long timeLastBreachAlertDismissed`: The time, in Unix Epoch milliseconds, when the user last dismissed the
