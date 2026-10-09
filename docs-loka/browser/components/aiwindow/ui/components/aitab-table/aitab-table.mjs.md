# browser/components/aiwindow/ui/components/aitab-table/aitab-table.mjs

source: browser/components/aiwindow/ui/components/aitab-table/aitab-table.mjs
source-hash: a46dd4a56ec82d00235be67ea1a37cf6190b6966
lines: 271

## <module>
- 役割: AI タブの比較表を描く aitab-table カスタム要素を定義し、列の型に応じた値の整形を担うモジュール。
- 呼び出し先: `customElements.define()`

## formatter()
- 位置: L38-45
- 役割: キーごとに Intl フォーマッタを一度だけ作って Map に保存し、以後は使い回して返す。
- 触るとき: 数値・通貨・日付のフォーマッタを新しく追加するとき、またはキャッシュのキー形式を変えて表示が古いまま残ると疑うとき。
- 呼び出し先: `formatters.get()`
- 条件付き依存: `if (!instance)` → `create()`
- 条件付き依存: `if (!instance)` → `formatters.set()`

## numberFormatter()
- 位置: L47-49
- 役割: 既定の Intl.NumberFormat を formatter() 経由で取得する。
- 触るとき: 数値セルの桁区切りや既定の表示形式を変えるとき。
- 呼び出し先: `formatter()`
- 参照: `Intl.NumberFormat`

## ratingFormatter()
- 位置: L51-56
- 役割: 評価値用に小数点以下1桁までの Intl.NumberFormat を取得する。
- 触るとき: 評価セルの小数の桁数を変えたいとき、または評価が丸められて見えるとき。
- 呼び出し先: `formatter()`
- 参照: `Intl.NumberFormat`

## currencyFormatter()
- 位置: L58-68
- 役割: 通貨コードごとに通貨表示の Intl.NumberFormat を取得し、整数の末尾0は省略する。
- 触るとき: 通貨列の表示形式を変えるとき、または formatValue() が通貨セルで例外を受けて数値のみ表示する経路を確認するとき。
- 呼び出し先: `formatter()`
- 参照: `Intl.NumberFormat`

## dateFormatter()
- 位置: L70-75
- 役割: タイムゾーンごとに medium の日付用 Intl.DateTimeFormat を取得する。
- 触るとき: 日付列の表示形式を変えるとき、または日付の表示が1日ずれるときにタイムゾーン指定を確認するとき。
- 呼び出し先: `formatter()`
- 参照: `Intl.DateTimeFormat`

## formatValue()
- 位置: L86-140
- 役割: 列の type ごとに行の値を整形する。機械的に型付けされた数値や ISO 日付だけ整形し、他は文字列のまま返す。
- 触るとき: 表の数値・評価・通貨・日付セルの表示が想定と違うとき。モデルが文字で書いた値を変換してしまっていないか確認するとき。
- 呼び出し先: `DATE_ONLY.test()`, `ISO_DATE_TIME.test()`, `JSON.stringify()`, `Number.isFinite()`, `Number.isNaN()`, `currencyFormatter()`, `currencyFormatter(field.currency ?? "USD").format()`, `date.valueOf()`, `dateFormatter()`, `dateFormatter(timeZone).format()`, `html()`, `numberFormatter()`, `numberFormatter().format()`, `ratingFormatter()`, `ratingFormatter().format()`
- 参照: `field.currency`, `field.key`, `field.max`, `field.prefix`, `field.suffix`, `field.type`

## AITabTable.constructor()
- 位置: L162-168
- 役割: heading・description を空文字、columns・rows を空配列で初期化する。
- 触るとき: 表のプロパティに初期値を足すとき、または値が未設定の表が空で描かれる理由を調べるとき。
- 呼び出し先: `super()`
- 参照: `this.columns`, `this.description`, `this.heading`, `this.rows`

## AITabTable.#columnsByRole()
- 位置: L176-185
- 役割: 列を title・subtitle・detail に振り分ける。title 指定が無ければ最初の非 subtitle 列を名前列にする。
- 触るとき: 列の role の解釈を変えるとき、または名前列に出る列が想定と違うとき。
- 呼び出し先: `this.columns.filter()`, `this.columns.find()`
- 参照: `field.role`

## AITabTable.#label()
- 位置: L187-189
- 役割: 列見出しとして field.label を返し、無ければ field.key を返す。
- 触るとき: 列見出しの文言が意図と違うとき、または label を省略した列の見出しを確認するとき。
- 参照: `field.key`, `field.label`

## AITabTable.#renderSourceChip()
- 位置: L191-205
- 役割: 行の href を http(s) として検証し、ホスト名を出すサイトチップを返す。無効な URL なら何も描かない。
- 触るとき: 出典チップの表示条件を変えるとき、または href があるのに出典が出ないときに URL の検証を確認するとき。
- 呼び出し先: `html()`, `httpUrl()`
- 参照: `row?.href`, `url.hostname`, `url.href`

## AITabTable.#renderRow()
- 位置: L207-223
- 役割: 1行分の tr を組み立て、名前セルに title・subtitle・出典チップを載せ、detail 列を td として並べる。
- 触るとき: 行の構造(名前セルの中身や列の並び)を変えるとき、または subtitle が二重に出るなど行の描画を調べるとき。
- 呼び出し先: `details.map()`, `formatValue()`, `html()`, `subtitleValues.map()`, `subtitles .map()`, `subtitles .map(field => formatValue(field, row)) .filter()`, `this.#renderSourceChip()`

## AITabTable.render()
- 位置: L225-267
- 役割: title 列が無ければ何も描かず、見出し・説明・table(thead と全行)を組み立てて返す。
- 触るとき: 表全体のマークアップや見出しとの aria-labelledby の関連付け、スタイルシートの読み込みを変えるとき。
- 呼び出し先: `details.map()`, `html()`, `this.#label()`, `this.#renderRow()`, `this.rows.map()`
- 参照: `details.length`, `this.#columnsByRole`, `this.description`, `this.heading`
