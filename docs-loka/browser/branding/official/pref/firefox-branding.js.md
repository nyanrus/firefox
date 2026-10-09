# browser/branding/official/pref/firefox-branding.js

source: browser/branding/official/pref/firefox-branding.js
source-hash: 6fb89554be5bfd49564186dfbe24f2aff076b8e9
lines: 49

## <module>
- 役割: 正式版向けのブランディング固有の pref を定義する。更新 URL とリリースノート URL を MOZ_UPDATE_CHANNEL(beta)と MOZ_ESR の条件分岐で切り替え、更新チェック間隔などを設定する。
- 呼び出し先: `pref()`
