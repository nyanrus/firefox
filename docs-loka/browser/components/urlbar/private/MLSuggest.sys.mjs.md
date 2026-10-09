# browser/components/urlbar/private/MLSuggest.sys.mjs

source: browser/components/urlbar/private/MLSuggest.sys.mjs
source-hash: 069afd07d79ddc8017e37bb295249fb0d04202d7
lines: 456

## <module>
- 役割: (未記入)
- 呼び出し先: `NAME_PUNCTUATION.filter()`, `XPCOMUtils.declareLazy()`

## _MLSuggest.createEngine()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.createEngine()`

## _MLSuggest.initialize()
- 位置: async L77-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `this.#initializeModelEngine()`
- 参照: `this.INTENT_OPTIONS`, `this.NER_OPTIONS`

## _MLSuggest.makeSuggestions()
- 位置: async L117-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.UrlbarPrefs.get()`, `this.#applyIntentThreshold()`, `this.#combineLocations()`, `this.#findSubjectFromQuery()`, `this._findIntent()`, `this._findNER()`
- 参照: `intentRes.metrics`, `nerResult.metrics`, `query.length`

## _MLSuggest.shutdown()
- 位置: async L158-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `engine.terminate()`
- 参照: `this.#modelEngines`

## _MLSuggest.#initializeModelEngine()
- 位置: async L179-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.createEngine()`
- 参照: `options.featureId`, `this.#modelEngines`

## _MLSuggest._findIntent()
- 位置: async L215-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engineIntentClassifier.run()`, `this.#initializeModelEngine()`
- 参照: `this.#modelEngines`, `this.INTENT_OPTIONS`, `this.INTENT_OPTIONS.featureId`

## _MLSuggest._findNER()
- 位置: async L248-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engineNER?.run()`, `this.#initializeModelEngine()`
- 参照: `this.#modelEngines`, `this.NER_OPTIONS`, `this.NER_OPTIONS.featureId`

## _MLSuggest.#applyIntentThreshold()
- 位置: L275-279
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `intentResult[0].label`, `intentResult[0]?.score`

## _MLSuggest.#combineLocations()
- 位置: L298-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cityResult.join()`, `cityResult.join(" ").trim()`, `stateResult.join()`, `stateResult.join(" ").trim()`, `this.#removePunctFromEndIfPresent()`
- 条件付き依存: `if (res.entity === "B-CITY" || res.entity === "I-CITY")` → `this.#processNERToken()`
- 条件付き依存: `if (res.entity === "B-STATE" || res.entity === "I-STATE")` → `this.#processNERToken()`
- 条件付き依存: `if (res.entity === "B-CITYSTATE" || res.entity === "I-CITYSTATE")` → `this.#processNERToken()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `cityStateResult.join(" ").split()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `cityStateResult.join()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `cityStateSplit[0] ?.trim?.() .split(",") .filter()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `cityStateSplit[0] ?.trim?.() .split()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `cityStateSplit[0] ?.trim()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `item.trim()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `cityStateSplit[1] ?.trim?.() .split(",") .filter()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `cityStateSplit[1] ?.trim?.() .split()`
- 条件付き依存: `if (cityStateResult.length && !cityResult.length && !stateResult.length)` → `cityStateSplit[1] ?.trim()`
- 参照: `cityResult.length`, `cityStateResult.length`, `nerResult.length`, `res.entity`, `stateResult.length`

## _MLSuggest.#processNERToken()
- 位置: L361-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `res.word.startsWith()`
- 条件付き依存: `if (res.word.startsWith("##") && resultArray.length)` → `res.word.slice()`
- 条件付き依存: `if (!(res.word.startsWith("##") && resultArray.length))` → `NAME_PUNCTUATION.includes()`
- 条件付き依存: `if (!(res.word.startsWith("##") && resultArray.length))` → `NAME_PUNCTUATION_EXCEPT_DOT.includes()`
- 条件付き依存: `if (!(res.word.startsWith("##") && resultArray.length))` → `resultArray[lastTokenIndex].slice()`
- 条件付き依存: `if (!( resultArray.length && (NAME_PUNCTUATION.includes(res.word) || NAME_PUNCTUATION_EXCEPT_DOT.includes( resultArray[lastTokenIndex].slice(-1) )) ))` → `resultArray.push()`
- 参照: `res.score`, `res.word`, `resultArray.length`

## _MLSuggest.#removePunctFromEndIfPresent()
- 位置: L398-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NAME_PUNCTUATION.includes()`, `resultArray[lastTokenIndex].slice()`
- 条件付き依存: `if ( resultArray.length && NAME_PUNCTUATION.includes(resultArray[lastTokenIndex].slice(-1)) )` → `resultArray[lastTokenIndex].slice()`
- 参照: `resultArray.length`

## _MLSuggest.#findSubjectFromQuery()
- 位置: L414-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(location) .map()`, `Object.values(location) .map(loc => loc?.replace(/\W+/g, " ")) .filter()`, `loc?.replace()`, `loc?.trim()`, `locValues.map()`, `locValues.map(loc => `\\b${loc}\\b`).join()`, `query .replace()`, `query .replace(/\W+/g, " ") .replace()`, `query .replace(/\W+/g, " ") .replace(locRegex, "") .split()`, `query .replace(/\W+/g, " ") .replace(locRegex, "") .split(/\W+/) .filter()`, `subjectWords.join()`, `this.#cleanSubject()`
- 参照: `location.city`, `location.state`, `word.length`

## _MLSuggest.#cleanSubject()
- 位置: L446-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PREPOSITIONS.includes()`, `words.pop()`
- 参照: `words.length`
