# nsILoginInfo (toolkit/components/passwordmgr/nsILoginInfo.idl)

source: toolkit/components/passwordmgr/nsILoginInfo.idl
source-hash: d1e8526b27f32dbe5e25df3c1ba6189732f91a00

- 継承: nsISupports
- 役割: An object containing information for a login stored by the
- 実装: (未記入)
- 使っているJS: [`browser/components/aboutlogins/AboutLoginsParent.sys.mjs`](../../../browser/components/aboutlogins/AboutLoginsParent.sys.mjs.md)

## メソッド / 属性
- `readonly attribute AString displayOrigin`: A string to display to the user for the origin which includes the httpRealm,
- `attribute AString origin`: The origin the login applies to.
- `attribute AString hostname`: The origin the login applies to, incorrectly called a hostname.
- `attribute AString formActionOrigin`: The origin a form-based login was submitted to.
- `attribute AString formSubmitURL`: The origin a form-based login was submitted to, incorrectly referred to as a URL.
- `attribute AString httpRealm`: The HTTP Realm a login was requested for.
- `attribute AString username`: The username for the login.
- `attribute AString usernameField`: The |name| attribute for the username input field.
- `attribute AString password`: The password for the login.
- `attribute AString passwordField`: The |name| attribute for the password input field.
- `attribute AString unknownFields`: Unknown fields this client doesn't know about but will be roundtripped
- `attribute boolean everSynced`: True if the login has ever been synced at some point.
- `attribute long syncCounter`: A counter used to indicate that syncing is occuring. It will get restored to 0
- `void init(AString aOrigin, AString aFormActionOrigin, AString aHttpRealm, AString aUsername, AString aPassword, AString aUsernameField, AString aPasswordField)`: Initialize a newly created nsLoginInfo object.
- `boolean equals(nsILoginInfo aLoginInfo)`: Test for strict equality with another nsILoginInfo object.
- `boolean matches(nsILoginInfo aLoginInfo, boolean ignorePassword)`: Test for loose equivalency with another nsILoginInfo object. The
- `nsILoginInfo clone()`: Create an identical copy of the login, duplicating all of the login's
