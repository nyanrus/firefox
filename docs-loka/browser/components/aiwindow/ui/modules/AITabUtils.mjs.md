# browser/components/aiwindow/ui/modules/AITabUtils.mjs

source: browser/components/aiwindow/ui/modules/AITabUtils.mjs
source-hash: 3f8c8551d7ff8f89d375099903d85c1485ba882b
lines: 19

## <module>
- 役割: AI タブページ用のユーティリティ(生成ページ内のリンク判定)を提供する

## httpUrl()
- 位置: L13-18
- 役割: trim した href を解析し、http か https の URL なら返し、それ以外は null を返す
- 触るとき: 生成ページのリンクを外部リンクとして開いてよいかの判定を変えるとき
- 呼び出し先: `String()`, `String(href ?? "").trim()`, `URL.parse()`
- 参照: `parsed?.protocol`
