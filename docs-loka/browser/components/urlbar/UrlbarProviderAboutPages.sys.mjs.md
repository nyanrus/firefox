# browser/components/urlbar/UrlbarProviderAboutPages.sys.mjs

source: browser/components/urlbar/UrlbarProviderAboutPages.sys.mjs
source-hash: 9e3639412e217b272dab57687a98c4b1598d77b6
lines: 70

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderAboutPages.type()
- 位置: L26-28
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderAboutPages.isActive()
- 位置: async L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.trimmedLowerCaseSearchString.startsWith()`

## UrlbarProviderAboutPages.startQuery()
- 位置: L48-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aboutUrl.startsWith()`
- 条件付き依存: `if (aboutUrl.startsWith(searchString))` → `lazy.UrlbarShared.getIconForUrl()`
- 条件付き依存: `if (aboutUrl.startsWith(searchString))` → `addCallback()`
- 参照: `lazy.AboutPagesUtils.visibleAboutUrls`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.trimmedLowerCaseSearchString`
