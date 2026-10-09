# nsICookieService (netwerk/cookie/nsICookieService.idl)

source: netwerk/cookie/nsICookieService.idl
source-hash: 3fe55e294c5e11a49963b71e046774c10ea1d0b3

- 継承: nsISupports
- 役割: nsICookieService
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-siteProtections.js`](../../browser/base/content/browser-siteProtections.js.md), [`browser/components/enterprisepolicies/Policies.sys.mjs`](../../browser/components/enterprisepolicies/Policies.sys.mjs.md), [`browser/components/preferences/config/privacy.mjs`](../../browser/components/preferences/config/privacy.mjs.md), [`browser/components/preferences/privacy.js`](../../browser/components/preferences/privacy.js.md), [`browser/components/protections/ContentBlockingPrefs.sys.mjs`](../../browser/components/protections/ContentBlockingPrefs.sys.mjs.md), [`browser/modules/SitePermissions.sys.mjs`](../../browser/modules/SitePermissions.sys.mjs.md)

## メソッド / 属性
- `const uint32_t BEHAVIOR_ACCEPT`: (未記入)
- `const uint32_t BEHAVIOR_REJECT_FOREIGN`: (未記入)
- `const uint32_t BEHAVIOR_REJECT`: (未記入)
- `const uint32_t BEHAVIOR_LIMIT_FOREIGN`: (未記入)
- `const uint32_t BEHAVIOR_REJECT_TRACKER`: (未記入)
- `const uint32_t BEHAVIOR_PARTITION_FOREIGN`: (未記入)
- `const uint32_t BEHAVIOR_LAST`: (未記入)
- `void getCookiesFromHost(ACString aBaseDomain, const_OriginAttributes aOriginAttributes, Array<CookieRefPtr> aCookies)`: (未記入)
- `void staleCookies(Array<CookieRefPtr> aCookies, int64_t aCurrentTimeInUsec)`: (未記入)
- `boolean hasExistingCookies(ACString aBaseDomain, const_OriginAttributes aOriginAttributes)`: (未記入)
- `void addCookieFromDocument(CookieParserPtr aCookieParser, ACString aBaseDomain, const_OriginAttributes aOriginAttributes, CookiePtr aCookie, int64_t aCurrentTimeInUsec, nsIURI aDocumentURI, boolean aThirdParty, Document document)`: (未記入)
- `ACString getCookieStringFromHttp(nsIURI aURI, nsIChannel aChannel)`: (未記入)
- `void setCookieStringFromHttp(nsIURI aURI, ACString aCookie, nsIChannel aChannel)`: (未記入)
