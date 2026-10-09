# browser/components/aiwindow/models/HistoryThumbnails.sys.mjs

source: browser/components/aiwindow/models/HistoryThumbnails.sys.mjs
source-hash: f8f6101def102f0a8728727762fadc1a8f3636e9
lines: 54

## <module>
- 役割: AI ウィンドウの履歴ページのサムネイルを、og:image の URL から BackgroundPageThumbs で取得してキャッシュし、moz-page-thumb URI を返す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## captureThumbnail()
- 位置: async L30-53
- 役割: og:image の URL をキャプチャ(既存キャッシュがあれば再利用)し、サイズが 0 でなければ moz-page-thumb の URL を返す。失敗時や URL 無しは null を返す。
- 触るとき: 履歴のサムネイル取得の条件(タイムアウトや背景色)を変えるとき、または画像が出ない原因を調べるとき。
- 呼び出し先: `IOUtils.stat()`, `lazy.BackgroundPageThumbs.captureIfMissing()`, `lazy.PageThumbs.getThumbnailPath()`, `lazy.console.warn()`
- 条件付き依存: `if (size > 0)` → `lazy.PageThumbs.getThumbnailURL()`
