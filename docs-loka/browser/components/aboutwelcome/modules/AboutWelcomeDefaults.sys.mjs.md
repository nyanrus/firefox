# browser/components/aboutwelcome/modules/AboutWelcomeDefaults.sys.mjs

source: browser/components/aboutwelcome/modules/AboutWelcomeDefaults.sys.mjs
source-hash: 722291c313bf2e14e09bcc97032c98f354acad49
lines: 1015

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`, `Services.sysinfo.getProperty()`

## getAddonFromRepository()
- 位置: async L813-827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonRepository.getAddonsByIDs()`
- 参照: `addonInfo.icons`, `addonInfo.id`, `addonInfo.name`, `addonInfo.screenshots`, `addonInfo.sourceURI.scheme`, `addonInfo.sourceURI.spec`, `addonInfo.type`

## getAddonInfo()
- 位置: async L829-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `content.includes()`, `content.startsWith()`, `decodeURIComponent()`
- 条件付き依存: `if (content.startsWith("rta:"))` → `getAddonFromRepository()`

## getAttributionContent()
- 位置: async L860-883
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AttributionCode.getAttrDataAsync()`
- 条件付き依存: `if (attribution?.source === "addons.mozilla.org")` → `getAddonInfo()`
- 条件付き依存: `if (addonInfo)` → `decodeURIComponent()`
- 条件付き依存: `if (attribution?.campaign === "smart_window")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (attribution)` → `decodeURIComponent()`
- 参照: `attribution.ua`, `attribution?.campaign`, `attribution?.source`
- XPCOM: `Services.prefs`

## getDefaults()
- 位置: L886-888
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`

## getLocalizedUA()
- 位置: L896-909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowedUAs.includes()`
- 条件付き依存: `if (allowedUAs.includes(ua))` → `gSourceL10n.formatValue()`

## prepareMobileDownload()
- 位置: L911-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content?.screens?.find()`, `lazy.BrowserUtils.sendToDeviceEmailsSupported()`
- 参照: `content?.screens?.find( screen => screen.id === "AW_MOBILE_DOWNLOAD" )?.content`, `mobileContent.cta_paragraph.action`, `mobileContent.cta_paragraph.text`, `screen.id`

## prepareContentForReact()
- 位置: async L930-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `prepareMobileDownload()`
- 条件付き依存: `if (content?.ua)` → `content?.screens?.find()`
- 条件付き依存: `if (content?.ua)` → `getLocalizedUA()`
- 条件付き依存: `if (!Services.prefs.getBoolPref("identity.fxaccounts.enabled", false))` → `content.screens?.find()`
- 条件付き依存: `if (content.languageMismatchEnabled)` → `content?.screens?.find()`
- 条件付き依存: `if (screen && content.appAndSystemLocaleInfo.canLiveReload)` → `addMessageArgs()`
- 条件付き依存: `if (shouldRemoveLanguageMismatchScreen)` → `lazy.ASRouterScreenUtils.removeScreens()`
- 参照: `action.data`, `content.appAndSystemLocaleInfo.canLiveReload`, `content.backdrop`, `content.languageMismatchEnabled`, `content.screens`, `content.skipFxA`, `content.ua`, `content?.campaign`, `content?.template`, `content?.ua`, `label.args`, `label.string_id`, `label?.string_id`, `s.id`, `screen.content`, `screen.content.languageSwitcher`, `screen.content?.secondary_button_top?.action?.type`, `screen.id`, `screen?.content?.primary_button?.action?.type`
- XPCOM: `Services.prefs`

## addMessageArgs()
- 位置: L986-992
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`
- 参照: `content.appAndSystemLocaleInfo.displayNames`, `value.args`, `value?.string_id`
