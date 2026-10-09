# browser/components/aiwindow/ui/modules/ChatMarkdownParser.mjs

source: browser/components/aiwindow/ui/modules/ChatMarkdownParser.mjs
source-hash: c5f1cc2c48a56eab037921339fb9ba9da4bb433e
lines: 125

## <module>
- 役割: チャットメッセージの Markdown を HTML に変換するパーサー。テーブルのラッパー要素とリンクの描画方針を定める。
- 呼び出し先: `MarkdownIt()`, `Object.entries()`

## md.renderer.rules[`${element}_open`]()
- 位置: L26-44
- 役割: ラッパー対象の要素（table）の開始タグを独自要素で包み、table には行範囲の data 属性を付ける。
- 触るとき: テーブルの行範囲属性を読む側の表示を調べるとき。属性名や値の形式を変えると読み手にも影響する。
- 呼び出し先: `[...dataAttributes] .map()`, `[...dataAttributes] .map(([key, value]) => `${key}="${md.utils.escapeHtml(value)}"`) .join()`, `md.utils.escapeHtml()`, `renderer.renderToken()`
- 条件付き依存: `if (map)` → `dataAttributes.set()`
- 条件付き依存: `if (map)` → `JSON.stringify()`

## md.renderer.rules[`${element}_close`]()
- 位置: L45-51
- 役割: ラッパー対象の要素の閉じタグの後にラッパーの閉じタグを出す。
- 触るとき: テーブルの入れ子や閉じ忘れによる表示崩れを調べるとき。
- 呼び出し先: `renderer.renderToken()`

## hasDestination()
- 位置: L58-60
- 役割: リンクの href が空白でない値を持つかを判定する。
- 触るとき: モデルの作った URL トークンが除去されて空になったリンクの扱いを変えるとき。
- 呼び出し先: `Boolean()`, `token?.attrGet()`, `token?.attrGet("href")?.trim()`

## md.renderer.rules.link_open()
- 位置: L62-65
- 役割: href を持たないリンクは開始タグを出さず、ラベルの文字だけ残す。
- 触るとき: リンクが消えて文字だけになる表示を調べるとき、またはリンクの描画条件を変えるとき。
- 呼び出し先: `hasDestination()`, `renderer.renderToken()`

## md.renderer.rules.link_close()
- 位置: L67-80
- 役割: 対応する link_open に href が無ければ閉じタグを出さない。
- 触るとき: link_open 側の条件を変えるとき。両方を揃えないと閉じタグだけ残って表示が壊れる。
- 呼び出し先: `hasDestination()`, `renderer.renderToken()`
- 参照: `tokens[i].type`

## parseMarkdown()
- 位置: L88-90
- 役割: Markdown 文字列を HTML 文字列に変換する。
- 触るとき: チャット本文の変換結果や、HTML 出力を使う箇所の入力を調べるとき。
- 呼び出し先: `md.render()`

## parseMarkdownBlocks()
- 位置: L101-124
- 役割: トップレベルのブロックごとに分けた HTML の配列を返す。連結すると parseMarkdown と同じ結果になる。
- 触るとき: ストリーム中に変わったブロックだけ再描画したいとき、またはブロックの区切り方を変えるとき。
- 呼び出し先: `blocks.push()`, `md.parse()`, `md.renderer.render()`, `tokens.slice()`
- 参照: `md.options`, `tokens.length`, `tokens[end].nesting`, `tokens[start].nesting`
