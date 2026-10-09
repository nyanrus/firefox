# browser/extensions/newtab/lib/Screenshots.sys.mjs

source: browser/extensions/newtab/lib/Screenshots.sys.mjs
source-hash: 51b4812350ccf86bf1fd9ea65451dfb4a8fb46a3
lines: 141

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## getScreenshotForURL()
- 位置: async L41-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `fetch()`, `filePathResponse.blob()`, `lazy.BackgroundPageThumbs.captureIfMissing()`, `lazy.PageThumbs._store()`, `lazy.PageThumbs.getThumbnailPath()`
- 条件付き依存: `if (lazy.gPrivilegedAboutProcessEnabled)` → `lazy.PageThumbs.getThumbnailURL()`
- 参照: `fileContents.size`, `lazy.gPrivilegedAboutProcessEnabled`

## _shouldGetScreenshots()
- 位置: L89-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- XPCOM: `Services.wm`

## maybeCacheScreenshot()
- 位置: async L108-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cache.updateLink()`, `onScreenshot()`, `this._shouldGetScreenshots()`, `this.getScreenshotForURL()`
- 参照: `cache.fetchingScreenshot`, `link.__sharedCache`

## updateLink()
- 位置: L117-119
- 役割: (未記入)
- 触るとき: (未記入)
