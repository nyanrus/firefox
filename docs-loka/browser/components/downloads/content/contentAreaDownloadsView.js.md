# browser/components/downloads/content/contentAreaDownloadsView.js

source: browser/components/downloads/content/contentAreaDownloadsView.js
source-hash: 3f9c4ad956d7e5f40f00172e8486e0e7e9538c09
lines: 50

## <module>
- 役割: about:downloads 系の別ページ (コンテンツ領域のダウンロード一覧) を初期化し、ダウンロード一覧を表示する。
- 呼び出し先: `ChromeUtils.importESModule()`

## init()
- 位置: L12-44
- 役割: 一覧に初回読み込み完了時のフォーカスと表示抑制を設定し、表示状態に応じてインジケーターの注意表示を抑止する。プライベートウィンドウ以外では履歴のダウンロードも表示する。
- 触るとき: ダウンロード一覧を開いたときにフォーカスや注意表示 (インジケーター) がおかしい、またはプライベートでの履歴表示を変えるときに見る。
- 呼び出し先: `DownloadsCommon.getIndicatorData()`, `PrivateBrowsingUtils.isContentWindowPrivate()`, `box.addEventListener()`, `document .getElementById()`, `document .getElementById("downloadsListBox") .focus()`, `document.addEventListener()`, `document.getElementById()`
- 条件付き依存: `if (document.visibilityState === "visible")` → `DownloadsCommon.getIndicatorData()`
- 参照: `DownloadsCommon.SUPPRESS_CONTENT_AREA_DOWNLOADS_OPEN`, `DownloadsCommon.getIndicatorData(window).attentionSuppressed`, `document.visibilityState`, `indicator.attentionSuppressed`, `view.place`

## window.onload()
- 位置: L47-49
- 役割: ページ読み込み完了時に init を呼ぶ。
- 触るとき: ページ起動時の初期化順序を変えるとき。
- 呼び出し先: `ContentAreaDownloadsView.init()`
