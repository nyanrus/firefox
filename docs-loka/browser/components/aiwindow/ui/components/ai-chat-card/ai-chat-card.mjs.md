# browser/components/aiwindow/ui/components/ai-chat-card/ai-chat-card.mjs

source: browser/components/aiwindow/ui/components/ai-chat-card/ai-chat-card.mjs
source-hash: cd4db10c925f701c6c89359c9549de5a2ab1401a
lines: 226

## <module>
- 役割: 履歴 URL を表示するカード型の ai-chat-card 要素を定義する。サムネイル、ファビコン、フォールバック図を切り替える。
- 呼び出し先: `customElements.define()`

## AIChatCard.domain()
- 位置: L25-28
- 役割: url を解析してホスト名を返す。解析できない場合は空文字を返す。
- 触るとき: カードに出すドメイン名の形式を変えるとき、または不正な URL でドメインが空になる問題を見るときに使う。
- 呼び出し先: `URL.parse()`
- 参照: `this.url`, `url?.hostname`

## AIChatCard.willUpdate()
- 位置: L30-34
- 役割: thumbnail が変わったら、前回のサムネイル読み込みエラー状態を解除する。
- 触るとき: サムネイルを差し替えても古いフォールバックが残るときに見る。
- 呼び出し先: `changed.has()`
- 参照: `this.thumbnailError`

## AIChatCard.renderImage()
- 位置: L36-73
- 役割: エラー時はフォールバック、サムネイルがあれば画像、無ければファビコン、最後に図を出し分ける。
- 触るとき: サムネイルの優先順位や読み込み失敗時の表示を変えるとき、またはカードに画像が出ないときに見る。
- 呼び出し先: `this.renderFallback()`
- 条件付き依存: `if (this.thumbnailError)` → `this.renderFallback()`
- 条件付き依存: `if (this.thumbnail)` → `html()`
- 条件付き依存: `if (this.favicon)` → `html()`
- 参照: `e.target.src`, `this.favicon`, `this.thumbnail`, `this.thumbnailError`

## AIChatCard.renderFavicon()
- 位置: L75-84
- 役割: ファビコンの小さな画像を描画し、読み込み失敗時は既定のファビコンに差し替える。
- 触るとき: メタ行のファビコン表示を変えるとき、またはファビコンが空白になるときに見る。
- 呼び出し先: `html()`
- 参照: `e.target.src`, `this.favicon`

## AIChatCard.render()
- 位置: L86-108
- 役割: カード全体を a 要素（新しいタブで開く）と moz-card で組み、タイトル、ドメイン、日時を並べる。
- 触るとき: カードのレイアウトや全体のリンク先を変えるとき、またはカードのクリック動作を確認するときに見る。
- 呼び出し先: `html()`, `this.renderFavicon()`, `this.renderImage()`
- 参照: `this.domain`, `this.timestamp`, `this.title`, `this.url`

## AIChatCard.renderFallback()
- 位置: L110-222
- 役割: サムネイルが無いときに使う、固定座標の SVG のプレースホルダー図を返す。
- 触るとき: プレースホルダー図の形や色（context-fill）を変えるとき、または図の位置を調整するときに見る。
- 呼び出し先: `html()`
