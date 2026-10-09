# browser/components/aiwindow/ui/components/aitab-highlights/aitab-highlights.mjs

source: browser/components/aiwindow/ui/components/aitab-highlights/aitab-highlights.mjs
source-hash: b7a1304d60b77b7d62104b30d5a8a440e0536615
lines: 122

## <module>
- 役割: AI Tab のハイライト一覧を表示する aitab-highlights 要素を定義する
- 呼び出し先: `customElements.define()`

## AITabHighlights.constructor()
- 位置: L36-40
- 役割: title を空文字、items を空配列で初期化する
- 触るとき: ハイライトが未指定のまま描画されても落ちないようにしたいとき、初期値を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.items`, `this.title`

## AITabHighlights.#renderSource()
- 位置: L42-51
- 役割: 1つの出典を ai-website-chip として描画する
- 触るとき: 出典チップの表示名やアイコン、クリック時のリンク先を変えるとき。favicon が無い場合は page-icon: 指定に落とす。
- 呼び出し先: `html()`
- 参照: `source.favicon`, `source.title`, `url.hostname`, `url.href`

## AITabHighlights.#renderSources()
- 位置: L53-63
- 役割: 出典のうち有効な http URL だけをチップ列にする
- 触るとき: 不正な URL の出典を表示から外す条件を見直すとき。全て無効なら何も出さない。
- 呼び出し先: `(sources?.items ?? []) .map()`, `(sources?.items ?? []) .map(source => ({ source, url: httpUrl(source?.href) })) .filter()`, `html()`, `httpUrl()`, `links.map()`, `this.#renderSource()`
- 参照: `link.url`, `links.length`, `source?.href`, `sources?.items`

## AITabHighlights.#renderItem()
- 位置: L65-84
- 役割: 1件のハイライトを li として組み立てる
- 触るとき: eyebrow・title・body・出典のどれかが空のときの表示を変えるとき。
- 呼び出し先: `html()`, `this.#renderSources()`
- 参照: `item.body`, `item.eyebrow`, `item.sources`, `item.title`

## AITabHighlights.#renderList()
- 位置: L86-97
- 役割: 有効な項目を ul にまとめ、空なら何も出さない
- 触るとき: 項目が無いときに見出しや枠を残すかどうかを変えるとき。title があれば aria-labelledby で結び付ける。
- 呼び出し先: `(this.items ?? []).filter()`, `html()`, `items.map()`, `this.#renderItem()`
- 参照: `items.length`, `this.items`, `this.title`

## AITabHighlights.render()
- 位置: L99-118
- 役割: スタイルシートを読み込み、見出しと項目一覧のセクションを描画する
- 触るとき: ハイライト欄全体の外枠や、タイトル見出しの有無による構造を変えるとき。
- 呼び出し先: `html()`, `this.#renderList()`
- 参照: `this.title`
