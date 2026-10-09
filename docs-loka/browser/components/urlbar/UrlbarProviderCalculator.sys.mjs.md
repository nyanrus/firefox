# browser/components/urlbar/UrlbarProviderCalculator.sys.mjs

source: browser/components/urlbar/UrlbarProviderCalculator.sys.mjs
source-hash: 1b32a48035e643b5e70ccee73c0eda3b724bb37f
lines: 563

## <module>
- 役割: (未記入)
- 呼び出し先: `Calculator.addNumberSystem()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## UrlbarProviderCalculator.type()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderCalculator.isActive()
- 位置: async L106-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.trimmedSearchString`

## UrlbarProviderCalculator.startQuery()
- 位置: async L121-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Calculator.evaluatePostfix()`, `Calculator.infix2postfix()`, `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `postfix.length`, `queryContext.sapName`, `queryContext.searchString`, `this.#sapName`

## UrlbarProviderCalculator.getViewTemplate()
- 位置: L145-147
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderCalculator.getViewUpdate()
- 位置: L149-176
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload`, `this.#sapName`

## UrlbarProviderCalculator.onEngagement()
- 位置: L183-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ClipboardHelper.copyString()`, `this.getViewUpdate()`
- 条件付き依存: `if (details.selType === "tail150")` → `controller.view.startTail150()`
- 条件付き依存: `if ("l10n" in input)` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if (!("l10n" in input))` → `input.textContent.replace()`
- 参照: `details.selType`, `input.l10n.args`, `input.l10n.id`, `this.getViewUpdate(result).input`

## BaseCalculator.addNumberSystem()
- 位置: L211-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.numberSystems.push()`

## BaseCalculator.isNumeric()
- 位置: L215-217
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `value.length`

## BaseCalculator.isOperator()
- 位置: L219-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sys.isOperator()`, `this.numberSystems.some()`

## BaseCalculator.isNumericToken()
- 位置: L223-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sys.isNumericToken()`, `this.numberSystems.some()`

## BaseCalculator.parsel10nFloat()
- 位置: L232-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseFloat()`, `system.transformNumber()`
- 参照: `this.numberSystems`

## BaseCalculator.precedence()
- 位置: L239-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["*", "/", "÷", "×"].includes()`, `["-", "+"].includes()`

## BaseCalculator.isLeftAssociative()
- 位置: L253-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["-", "+", "*", "/", "÷", "×"].includes()`

## BaseCalculator.infix2postfix()
- 位置: L267-309
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)

## "×"()
- 位置: L313-313
- 役割: (未記入)
- 触るとき: (未記入)

## "+"()
- 位置: L314-314
- 役割: (未記入)
- 触るとき: (未記入)

## "-"()
- 位置: L315-315
- 役割: (未記入)
- 触るとき: (未記入)

## "/"()
- 位置: L316-316
- 役割: (未記入)
- 触るとき: (未記入)

## "÷"()
- 位置: L317-317
- 役割: (未記入)
- 触るとき: (未記入)

## "^"()
- 位置: L318-318
- 役割: (未記入)
- 触るとき: (未記入)

## BaseCalculator.evaluatePostfix()
- 位置: L321-373
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`
- 参照: `this.calculator`

## init()
- 位置: L382-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `input.replace()`, `this._chars.push()`
- 参照: `input.length`, `this._chars`, `this._tokens`

## parse()
- 位置: L398-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tokenizeBlock()`
- 参照: `this._chars.length`, `this._tokens`

## _tokenizeBlock()
- 位置: L407-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tokenizeBlock()`, `this._tokenizeOther()`
- 条件付き依存: `if (this._chars[0] == "(")` → `this._tokens.push()`
- 条件付き依存: `if (this._chars[0] == "(")` → `this._chars.shift()`
- 条件付き依存: `if (this._chars[0] == "(")` → `this._tokenizeBlock()`
- 条件付き依存: `if (!(this._chars[0] == "("))` → `this._tokenizeNumber()`
- 参照: `this._chars`, `this._chars.length`

## _tokenizeNumber()
- 位置: L451-508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/[+-]/.test()`, `number.join()`, `number.push()`, `this._chars.shift()`, `this._tokens.push()`, `tokenizeNumberInternal()`
- 条件付き依存: `if (/[+-]/.test(this._chars[0]))` → `number.push()`
- 条件付き依存: `if (/[+-]/.test(this._chars[0]))` → `this._chars.shift()`
- 条件付き依存: `if (!this._chars.length || this._chars[0] != "e")` → `this._tokens.push()`
- 条件付き依存: `if (!this._chars.length || this._chars[0] != "e")` → `number.join()`
- 参照: `this._chars`, `this._chars.length`

## tokenizeNumberInternal()
- 位置: L462-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `number.push()`, `this._chars.shift()`, `this.calculator.isNumericToken()`
- 参照: `this._chars`, `this._chars.length`

## _tokenizeOther()
- 位置: L510-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.calculator.isOperator()`
- 条件付き依存: `if (this.calculator.isOperator(this._chars[0]))` → `this._tokens.push()`
- 条件付き依存: `if (this.calculator.isOperator(this._chars[0]))` → `this._chars.shift()`
- 参照: `this._chars`, `this._chars.length`

## isOperator()
- 位置: L527-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["÷", "×", "-", "+", "*", "/", "^"].includes()`

## isNumericToken()
- 位置: L528-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^[0-9\.,]/.test()`

## transformNumber()
- 位置: L536-561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `num.indexOf()`
- 条件付き依存: `if (firstPeriod != -1 && firstComma != -1 && firstPeriod < firstComma)` → `num.replace()`
- 条件付き依存: `if (firstPeriod != -1 && firstComma != -1)` → `num.replace()`
- 条件付き依存: `if (!(firstPeriod != -1 && firstComma != -1))` → `num.includes()`
- 条件付き依存: `if (firstComma != -1 && num.includes(",", firstComma + 1))` → `num.replace()`
- 条件付き依存: `if (!(firstComma != -1 && num.includes(",", firstComma + 1)))` → `num.includes()`
- 条件付き依存: `if (firstPeriod != -1 && num.includes(".", firstPeriod + 1))` → `num.replace()`
- 条件付き依存: `if (firstComma != -1)` → `num.replace()`
