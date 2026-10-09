# nsIScopedPrefs (toolkit/components/antitracking/scopedprefs/nsIScopedPrefs.idl)

source: toolkit/components/antitracking/scopedprefs/nsIScopedPrefs.idl
source-hash: b6be8445fa6cb39e734247848ff56227d3c52aec

- 継承: nsISupports
- 役割: (未記入)
- 実装: `mozilla::ScopedPrefs` (toolkit/components/antitracking/scopedprefs/components.conf)
- contract ID: `@mozilla.org/scoped-prefs;1`
- 使っているJS: [`browser/modules/ReducedProtectionNotification.sys.mjs`](../../../../browser/modules/ReducedProtectionNotification.sys.mjs.md)

## メソッド / 属性
- `void setBoolPrefScoped(nsIScopedPrefs_Pref pref, BrowsingContext bc, boolean value)`: (未記入)
- `boolean getBoolPrefScoped(nsIScopedPrefs_Pref pref, BrowsingContext bc)`: (未記入)
- `void clearScoped()`: (未記入)
- `void clearScopedPref(nsIScopedPrefs_Pref pref)`: (未記入)
- `void clearScopedByHost(AUTF8String aHost)`: (未記入)
- `void clearScopedPrefByHost(nsIScopedPrefs_Pref pref, AUTF8String aHost)`: (未記入)
