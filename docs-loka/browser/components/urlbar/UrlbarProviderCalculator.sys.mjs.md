# browser/components/urlbar/UrlbarProviderCalculator.sys.mjs

source: browser/components/urlbar/UrlbarProviderCalculator.sys.mjs
source-hash: 1b32a48035e643b5e70ccee73c0eda3b724bb37f
lines: 563

## <module>
- 役割: URL バーに入力された算術式を計算して結果行を出すプロバイダーと、その計算器(中置式を後置式に変換して評価する)の実装。
- 呼び出し先: `Calculator.addNumberSystem()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## UrlbarProviderCalculator.type()
- 位置: L95-97
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: 電卓結果の種別と並び順を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderCalculator.isActive()
- 位置: async L106-112
- 役割: トリム済みの検索語が空でなく、検索モードでなく、設定 suggest.calculator が有効なときに起動する。
- 触るとき: 電卓結果を出す入力条件や設定の扱いを変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.trimmedSearchString`

## UrlbarProviderCalculator.startQuery()
- 位置: async L121-143
- 役割: 入力を後置式に変換し、要素が 3 つ未満なら何もしない。評価結果を suggestedIndex 1 の動的結果として追加する。式が不正なら例外を握りつぶして結果を出さない。
- 触るとき: 電卓結果の最小式長や、結果の位置(suggestedIndex)を変えるとき。
- 呼び出し先: `Calculator.evaluatePostfix()`, `Calculator.infix2postfix()`, `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `postfix.length`, `queryContext.sapName`, `queryContext.searchString`, `this.#sapName`

## UrlbarProviderCalculator.getViewTemplate()
- 位置: L145-147
- 役割: 結果行の定義(アイコン、式の表示、コピー用の文言、150 のときだけ出す小さな画像ボタン)を返す。
- 触るとき: 電卓結果行の DOM 構造を変えるとき。

## UrlbarProviderCalculator.getViewUpdate()
- 位置: L149-176
- 役割: 値を「= 値」の形で表示し、undefined の時は専用文言にする。150 のときだけ tail150 ボタンを表示する。
- 触るとき: 結果行の表示文言や、特別な値の扱いを変えるとき。
- 参照: `result.payload`, `this.#sapName`

## UrlbarProviderCalculator.onEngagement()
- 位置: L183-200
- 役割: tail150 が選ばれたときはビューに tail150 演出を開始させる。それ以外は表示されている値を(ローカライズして)クリップボードへコピーする。
- 触るとき: 電卓結果を選んだときのコピー内容や、特別な演出の扱いを変えるとき。
- 呼び出し先: `lazy.ClipboardHelper.copyString()`, `this.getViewUpdate()`
- 条件付き依存: `if (details.selType === "tail150")` → `controller.view.startTail150()`
- 条件付き依存: `if ("l10n" in input)` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if (!("l10n" in input))` → `input.textContent.replace()`
- 参照: `details.selType`, `input.l10n.args`, `input.l10n.id`, `this.getViewUpdate(result).input`

## BaseCalculator.addNumberSystem()
- 位置: L211-213
- 役割: 数字体系(演算子判定、数字判定、数値の正規化)を計算器に追加する。
- 触るとき: 別の数字体系や地域の数値表記に対応させるとき。
- 呼び出し先: `this.numberSystems.push()`

## BaseCalculator.isNumeric()
- 位置: L215-217
- 役割: 値が数値として解釈できる文字列かを判定する。
- 触るとき: 数値判定の緩さを確認したいとき。現在は呼び出し元が見当たらない。(要確認)
- 参照: `value.length`

## BaseCalculator.isOperator()
- 位置: L219-221
- 役割: いずれかの数字体系が演算子とみなす文字かを返す。
- 触るとき: 新しい演算子を足すとき。
- 呼び出し先: `sys.isOperator()`, `this.numberSystems.some()`

## BaseCalculator.isNumericToken()
- 位置: L223-225
- 役割: いずれかの数字体系が数字の構成文字とみなすかを返す。
- 触るとき: 数字に使える文字(小数点、カンマ等)を変えるとき。
- 呼び出し先: `sys.isNumericToken()`, `this.numberSystems.some()`

## BaseCalculator.parsel10nFloat()
- 位置: L232-237
- 役割: 各数字体系の transformNumber で地域の区切り記号を直してから、parseFloat で数値にする。
- 触るとき: カンマやピリオドの解釈で誤った値になる問題を調べるとき。
- 呼び出し先: `parseFloat()`, `system.transformNumber()`
- 参照: `this.numberSystems`

## BaseCalculator.precedence()
- 位置: L239-251
- 役割: 演算子の優先順位(加減は 2、乗除は 3、累乗は 4)を返す。
- 触るとき: 演算子の優先順位を変えるとき。
- 呼び出し先: `["*", "/", "÷", "×"].includes()`, `["-", "+"].includes()`

## BaseCalculator.isLeftAssociative()
- 位置: L253-262
- 役割: 加減乗除は左結合、累乗は右結合として返す。
- 触るとき: 結合規則(特に累乗)を変えるとき。
- 呼び出し先: `["-", "+", "*", "/", "÷", "×"].includes()`

## BaseCalculator.infix2postfix()
- 位置: L267-309
- 役割: Parser で字句に分け、操車場(shunting yard)の手法で中置式を後置式の配列に変換する。括弧の対応も処理する。
- 触るとき: 式の解析順序や括弧の扱い、構文エラーになる条件を調べるとき。
- 呼び出し先: `output.push()`, `parser.parse()`, `stack.pop()`, `this.isOperator()`, `tokens.forEach()`
- 条件付き依存: `if (token.number)` → `output.push()`
- 条件付き依存: `if (token.number)` → `this.parsel10nFloat()`
- 条件付き依存: `if (this.isOperator(token.value))` → `this.isOperator()`
- 条件付き依存: `if (this.isOperator(token.value))` → `i()`
- 条件付き依存: `if (this.isOperator(token.value))` → `this.isLeftAssociative()`
- 条件付き依存: `if (this.isOperator(token.value))` → `output.push()`
- 条件付き依存: `if (this.isOperator(token.value))` → `stack.pop()`
- 条件付き依存: `if (this.isOperator(token.value))` → `stack.push()`
- 条件付き依存: `if (token.value === "(")` → `stack.push()`
- 条件付き依存: `if (token.value === ")")` → `output.push()`
- 条件付き依存: `if (token.value === ")")` → `stack.pop()`
- 参照: `stack.length`, `this.precedence`, `token.number`, `token.value`

## "*"()
- 位置: L312-312
- 役割: 乗算を行う。
- 触るとき: 演算子の計算規則を変えるとき。

## "×"()
- 位置: L313-313
- 役割: 乗算を行う(全角記号の別名)。
- 触るとき: 演算子の別名を追加・変更するとき。

## "+"()
- 位置: L314-314
- 役割: 加算を行う。
- 触るとき: 加算の扱いを変えるとき。

## "-"()
- 位置: L315-315
- 役割: 減算を行う。
- 触るとき: 減算の扱いを変えるとき。

## "/"()
- 位置: L316-316
- 役割: 除算を行う。ゼロ除算の扱いは evaluatePostfix 側で判定する。
- 触るとき: 除算の扱いを変えるとき。

## "÷"()
- 位置: L317-317
- 役割: 除算を行う(全角記号の別名)。
- 触るとき: 演算子の別名を追加・変更するとき。

## "^"()
- 位置: L318-318
- 役割: 累乗を行う。
- 触るとき: 累乗の扱いを変えるとき。

## BaseCalculator.evaluatePostfix()
- 位置: L321-373
- 役割: 後置式をスタックで評価する。除数が 0 なら undefined を返し、NaN や無限大は例外にする。結果の大きさに応じて指数表記・小数・桁区切りなしの表記を選んで文字列にする。
- 触るとき: 計算結果の表示形式(指数表記に切り替える閾値、有効桁数)を変えるとき。
- 呼び出し先: `Math.abs()`, `isFinite()`, `isNaN()`, `stack.pop()`, `this.isOperator()`
- 条件付き依存: `if (!this.isOperator(token))` → `stack.push()`
- 条件付き依存: `if (!(!this.isOperator(token)))` → `stack.pop()`
- 条件付き依存: `if (!(!this.isOperator(token)))` → `this.evaluate[token]()`
- 条件付き依存: `if (!(!this.isOperator(token)))` → `isNaN()`
- 条件付き依存: `if (!(!this.isOperator(token)))` → `isFinite()`
- 条件付き依存: `if (!(!this.isOperator(token)))` → `stack.push()`
- 条件付き依存: `if (!( Math.abs(finalResult) >= FULL_NUMBER_MAX_THRESHOLD || (Math.abs(finalResult) <= FULL_NUMBER_MIN_THRESHOLD && finalResult != 0) ))` → `Math.abs()`
- 条件付き依存: `if (Math.abs(finalResult) < 1)` → `new Intl.NumberFormat(locale, { style: "decimal", maximumSignificantDigits: 9, numberingSystem: "latn", }).format()`
- 参照: `Intl.NumberFormat`, `Services.locale.appLocaleAsBCP47`, `this.evaluate`
- XPCOM: `Services.locale`

## Parser()
- 位置: L376-379
- 役割: 中置式の文字列を解析するための字句解析器の生成関数。
- 触るとき: 式の字句解析の構成を変えるとき。
- 呼び出し先: `this.init()`
- 参照: `this.calculator`

## init()
- 位置: L382-393
- 役割: 入力から空白を除き、1 文字ずつの配列とトークン配列を用意する。
- 触るとき: 入力の前処理(空白の扱い)を変えるとき。
- 呼び出し先: `input.replace()`, `this._chars.push()`
- 参照: `input.length`, `this._chars`, `this._tokens`

## parse()
- 位置: L398-405
- 役割: 入力全体を 1 つのブロックとして解析し、残りの文字があれば例外にする。トークン配列を返す。
- 触るとき: 式の全体の構文エラーになる条件を調べるとき。
- 呼び出し先: `this._tokenizeBlock()`
- 参照: `this._chars.length`, `this._tokens`

## _tokenizeBlock()
- 位置: L407-448
- 役割: 括弧で囲まれた部分や数字を読み、その後に続く演算子とブロックを再帰的に読む。
- 触るとき: 括弧のネストや演算子の連続など、構文の判定を変えるとき。
- 呼び出し先: `this._tokenizeBlock()`, `this._tokenizeOther()`
- 条件付き依存: `if (this._chars[0] == "(")` → `this._tokens.push()`
- 条件付き依存: `if (this._chars[0] == "(")` → `this._chars.shift()`
- 条件付き依存: `if (this._chars[0] == "(")` → `this._tokenizeBlock()`
- 条件付き依存: `if (!(this._chars[0] == "("))` → `this._tokenizeNumber()`
- 参照: `this._chars`, `this._chars.length`

## _tokenizeNumber()
- 位置: L451-508
- 役割: 符号、数字の並び、指数部(e 記法)を読んで数値トークンを 1 つ作る。
- 触るとき: 指数記法や符号付きの数の読み取りを変えるとき。
- 呼び出し先: `/[+-]/.test()`, `number.join()`, `number.push()`, `this._chars.shift()`, `this._tokens.push()`, `tokenizeNumberInternal()`
- 条件付き依存: `if (/[+-]/.test(this._chars[0]))` → `number.push()`
- 条件付き依存: `if (/[+-]/.test(this._chars[0]))` → `this._chars.shift()`
- 条件付き依存: `if (!this._chars.length || this._chars[0] != "e")` → `this._tokens.push()`
- 条件付き依存: `if (!this._chars.length || this._chars[0] != "e")` → `number.join()`
- 参照: `this._chars`, `this._chars.length`

## tokenizeNumberInternal()
- 位置: L462-478
- 役割: 数字体系で数字とみなされる文字を連続して読む。
- 触るとき: 数字として読む文字の範囲を変えるとき。
- 呼び出し先: `number.push()`, `this._chars.shift()`, `this.calculator.isNumericToken()`
- 参照: `this._chars`, `this._chars.length`

## _tokenizeOther()
- 位置: L510-521
- 役割: 次の文字が演算子ならそれを演算子トークンとして取り出す。
- 触るとき: 演算子として認める文字を増やすとき。
- 呼び出し先: `this.calculator.isOperator()`
- 条件付き依存: `if (this.calculator.isOperator(this._chars[0]))` → `this._tokens.push()`
- 条件付き依存: `if (this.calculator.isOperator(this._chars[0]))` → `this._chars.shift()`
- 参照: `this._chars`, `this._chars.length`

## isOperator()
- 位置: L527-527
- 役割: 既定の数字体系で演算子とみなす文字(÷ × - + * / ^)を判定する。
- 触るとき: 演算子の一覧を変えるとき。
- 呼び出し先: `["÷", "×", "-", "+", "*", "/", "^"].includes()`

## isNumericToken()
- 位置: L528-528
- 役割: 既定の数字体系で、数字の先頭になりうる文字(0-9、小数点、カンマ)を判定する。
- 触るとき: 数字の先頭として認める文字を変えるとき。
- 呼び出し先: `/^[0-9\.,]/.test()`

## transformNumber()
- 位置: L536-561
- 役割: 小数点とカンマの組み合わせから区切り記号を推定し、parseFloat で読める形へ直す。
- 触るとき: 地域によって異なる数の書き方(1.999,5 や 1,999.5)の解釈を変えるとき。
- 呼び出し先: `num.indexOf()`
- 条件付き依存: `if (firstPeriod != -1 && firstComma != -1 && firstPeriod < firstComma)` → `num.replace()`
- 条件付き依存: `if (firstPeriod != -1 && firstComma != -1)` → `num.replace()`
- 条件付き依存: `if (!(firstPeriod != -1 && firstComma != -1))` → `num.includes()`
- 条件付き依存: `if (firstComma != -1 && num.includes(",", firstComma + 1))` → `num.replace()`
- 条件付き依存: `if (!(firstComma != -1 && num.includes(",", firstComma + 1)))` → `num.includes()`
- 条件付き依存: `if (firstPeriod != -1 && num.includes(".", firstPeriod + 1))` → `num.replace()`
- 条件付き依存: `if (firstComma != -1)` → `num.replace()`
