# browser/components/preferences/config/moreFromMozilla.mjs

source: browser/components/preferences/config/moreFromMozilla.mjs
source-hash: d9438d6454b3639e95752e7059a20da60837a5f0
lines: 293

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Preferences.addSetting()`, `SettingGroupManager.registerGroups()`, `getProducts()`, `getProducts().map()`, `getURL()`

## getURL()
- 位置: L31-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `lazy.NimbusFeatures.moreFromMozilla.getVariable()`, `pageUrl.searchParams.append()`, `pageUrl.searchParams.set()`, `pageUrl.toString()`
- 条件付き依存: `if (option !== "default")` → `pageUrl.searchParams.set()`

## getProducts()
- 位置: L71-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.shouldShowPromo()`, `lazy.BrowserUtils.shouldShowVPNPromo()`, `lazy.Region.home?.toLowerCase()`, `products.push()`
- 条件付き依存: `if (lazy.BrowserUtils.shouldShowVPNPromo())` → `products.push()`
- 条件付き依存: `if (lazy.BrowserUtils.shouldShowPromo(lazy.BrowserUtils.PromoType.RELAY))` → `products.push()`
- 参照: `lazy.BrowserUtils.PromoType.RELAY`

## getControlConfig()
- 位置: L172-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getURL()`

## getControlConfig()
- 位置: L189-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.moreFromMozilla.getVariable()`

## visible()
- 位置: L205-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.sendToDeviceEmailsSupported()`

## getControlConfig()
- 位置: L206-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getURL()`
