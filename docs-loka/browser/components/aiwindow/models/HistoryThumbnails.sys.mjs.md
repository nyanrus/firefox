# browser/components/aiwindow/models/HistoryThumbnails.sys.mjs

source: browser/components/aiwindow/models/HistoryThumbnails.sys.mjs
source-hash: f8f6101def102f0a8728727762fadc1a8f3636e9
lines: 54

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## captureThumbnail()
- 位置: async L30-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.stat()`, `lazy.BackgroundPageThumbs.captureIfMissing()`, `lazy.PageThumbs.getThumbnailPath()`, `lazy.console.warn()`
- 条件付き依存: `if (size > 0)` → `lazy.PageThumbs.getThumbnailURL()`
