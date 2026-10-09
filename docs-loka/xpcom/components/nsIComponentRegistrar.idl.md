# nsIComponentRegistrar (xpcom/components/nsIComponentRegistrar.idl)

source: xpcom/components/nsIComponentRegistrar.idl
source-hash: 6b85caffab4ff79194f36cfb8243382409aae9f9

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/enterprisepolicies/helpers/WebsiteFilter.sys.mjs`](../../browser/components/enterprisepolicies/helpers/WebsiteFilter.sys.mjs.md), [`browser/extensions/webcompat/about-compat/aboutPageProcessScript.js`](../../browser/extensions/webcompat/about-compat/aboutPageProcessScript.js.md)

## メソッド / 属性
- `void autoRegister(nsIFile aSpec)`: autoRegister
- `void registerFactory(nsCIDRef aClass, string aClassName, string aContractID, nsIFactory aFactory)`: registerFactory
- `void unregisterFactory(nsCIDRef aClass, nsIFactory aFactory)`: unregisterFactory
- `boolean isCIDRegistered(nsCIDRef aClass)`: isCIDRegistered
- `boolean isContractIDRegistered(string aContractID)`: isContractIDRegistered
- `Array<ACString> getContractIDs()`: getContractIDs
- `nsCIDPtr contractIDToCID(string aContractID)`: contractIDToCID
