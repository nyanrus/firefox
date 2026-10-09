# browser/components/downloads/content/contentAreaDownloadsView.js

source: browser/components/downloads/content/contentAreaDownloadsView.js
source-hash: 3f9c4ad956d7e5f40f00172e8486e0e7e9538c09
lines: 50

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## init()
- 位置: L12-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getIndicatorData()`, `PrivateBrowsingUtils.isContentWindowPrivate()`, `box.addEventListener()`, `document .getElementById()`, `document .getElementById("downloadsListBox") .focus()`, `document.addEventListener()`, `document.getElementById()`
- 条件付き依存: `if (document.visibilityState === "visible")` → `DownloadsCommon.getIndicatorData()`
- 参照: `DownloadsCommon.SUPPRESS_CONTENT_AREA_DOWNLOADS_OPEN`, `DownloadsCommon.getIndicatorData(window).attentionSuppressed`, `document.visibilityState`, `indicator.attentionSuppressed`, `view.place`

## window.onload()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentAreaDownloadsView.init()`
