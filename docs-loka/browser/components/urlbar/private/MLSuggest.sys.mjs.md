# browser/components/urlbar/private/MLSuggest.sys.mjs

source: browser/components/urlbar/private/MLSuggest.sys.mjs
source-hash: 069afd07d79ddc8017e37bb295249fb0d04202d7
lines: 456

## <module>
- 役割: インテント分類と固有表現抽出(NER)の ML モデルで、クエリの意図・地名(都市・州)・件名を推定する。
- 呼び出し先: `NAME_PUNCTUATION.filter()`, `XPCOMUtils.declareLazy()`

## _MLSuggest.createEngine()
- 位置: L70-72
- 役割: ML エンジンの作成を lazy に読み込んだ createEngine へ渡す。テストで差し替えられるように包んである。
- 触るとき: テストでエンジン作成をモックするとき、またはエンジンのオプションを変えるとき。
- 呼び出し先: `lazy.createEngine()`

## _MLSuggest.initialize()
- 位置: async L77-82
- 役割: インテントと NER の両エンジンを並列に作成する。
- 触るとき: 起動時にモデルの読み込みを始めるタイミングを変えるとき。
- 呼び出し先: `Promise.all()`, `this.#initializeModelEngine()`
- 参照: `this.INTENT_OPTIONS`, `this.NER_OPTIONS`

## _MLSuggest.makeSuggestions()
- 位置: async L117-153
- 役割: 200 文字を超えるクエリは null を返す。インテントと NER を並列に実行し、場所の統合と閾値の適用を経て、インテント・場所・件名・メトリクスを返す。どちらかが失敗すれば null を返す。
- 触るとき: ML による提案が出ない、または件名が想定と違うときに処理の流れを追うとき。
- 呼び出し先: `Promise.all()`, `lazy.UrlbarPrefs.get()`, `this.#applyIntentThreshold()`, `this.#combineLocations()`, `this.#findSubjectFromQuery()`, `this._findIntent()`, `this._findNER()`
- 参照: `intentRes.metrics`, `nerResult.metrics`, `query.length`

## _MLSuggest.shutdown()
- 位置: async L158-167
- 役割: 作成済みの全エンジンを terminate し、各エンジンをキャッシュから削除する。
- 触るとき: 終了時にエンジンプロセスが残る問題を確認するとき。
- 呼び出し先: `Object.entries()`, `engine.terminate()`
- 参照: `this.#modelEngines`

## _MLSuggest.#initializeModelEngine()
- 位置: async L179-204
- 役割: featureId をキーにキャッシュを確認し、無ければ作成してキャッシュする。作成に失敗したらエラーを出して null を返す。
- 触るとき: モデル読み込み失敗時の扱いや、エンジンの再利用の仕方を変えるとき。
- 呼び出し先: `console.error()`, `this.createEngine()`
- 参照: `options.featureId`, `this.#modelEngines`

## _MLSuggest._findIntent()
- 位置: async L215-237
- 役割: インテント用エンジンでクエリを分類する。実行が失敗したらキャッシュから外して作り直しを始め、null を返す。
- 触るとき: インテント判定が null になり続けるとき、またはエンジンの再作成が効いているかを確かめるとき。
- 呼び出し先: `engineIntentClassifier.run()`, `this.#initializeModelEngine()`
- 参照: `this.#modelEngines`, `this.INTENT_OPTIONS`, `this.INTENT_OPTIONS.featureId`

## _MLSuggest._findNER()
- 位置: async L248-259
- 役割: NER エンジンでクエリの固有表現を抽出する。実行が失敗したらキャッシュから外して作り直しを始め、null を返す。エンジンが未作成なら undefined を返す。
- 触るとき: NER の結果が取れない原因を追うとき、または未作成時の戻り値を扱う箇所を変えるとき。
- 呼び出し先: `engineNER?.run()`, `this.#initializeModelEngine()`
- 参照: `this.#modelEngines`, `this.NER_OPTIONS`, `this.NER_OPTIONS.featureId`

## _MLSuggest.#applyIntentThreshold()
- 位置: L275-279
- 役割: 最上位インテントの score が閾値を超えればその label を返し、超えなければ空文字を返す。(要確認: 型の説明文は 'unknown' と書かれている)
- 触るとき: インテントを採用する閾値の効き方を変えるとき、または 'unknown' と空文字のどちらを使うか決めるとき。
- 参照: `intentResult[0].label`, `intentResult[0]?.score`

## _MLSuggest.#combineLocations()
- 位置: L298-338
- 役割: NER の city・state・citystate トークンを閾値で絞って結合する。citystate だけのときはカンマで city と state に分ける。末尾の句読点を除いて返す。
- 触るとき: 都市名や州名の抽出結果がずれるとき、または複数トークンの地名を扱いを変えるとき。
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
- 役割: 閾値以下のトークンを捨てる。'##' で始まる語は直前の語に連結し、句読点は直前の語に付ける。それ以外は配列に追加する。
- 触るとき: 分割された地名が一語にまとまらない、または余分な記号が付く問題を調べるとき。
- 呼び出し先: `res.word.startsWith()`
- 条件付き依存: `if (res.word.startsWith("##") && resultArray.length)` → `res.word.slice()`
- 条件付き依存: `if (!(res.word.startsWith("##") && resultArray.length))` → `NAME_PUNCTUATION.includes()`
- 条件付き依存: `if (!(res.word.startsWith("##") && resultArray.length))` → `NAME_PUNCTUATION_EXCEPT_DOT.includes()`
- 条件付き依存: `if (!(res.word.startsWith("##") && resultArray.length))` → `resultArray[lastTokenIndex].slice()`
- 条件付き依存: `if (!( resultArray.length && (NAME_PUNCTUATION.includes(res.word) || NAME_PUNCTUATION_EXCEPT_DOT.includes( resultArray[lastTokenIndex].slice(-1) )) ))` → `resultArray.push()`
- 参照: `res.score`, `res.word`, `resultArray.length`

## _MLSuggest.#removePunctFromEndIfPresent()
- 位置: L398-406
- 役割: 配列の末尾要素の最後の文字が '.'、'-'、'\'' のいずれかなら、その1文字を削る。
- 触るとき: 地名の末尾に記号が残る問題を調べるとき。
- 呼び出し先: `NAME_PUNCTUATION.includes()`, `resultArray[lastTokenIndex].slice()`
- 条件付き依存: `if ( resultArray.length && NAME_PUNCTUATION.includes(resultArray[lastTokenIndex].slice(-1)) )` → `resultArray[lastTokenIndex].slice()`
- 参照: `resultArray.length`

## _MLSuggest.#findSubjectFromQuery()
- 位置: L414-439
- 役割: 場所が無ければクエリ全体を返す。場所の語を正規表現でクエリから取り除き、単語に分け直し、末尾の前置詞を外して空白でつないだ件名を返す。
- 触るとき: 件名に地名が残る、または件名が削りすぎられるときに確認するとき。
- 呼び出し先: `Object.values()`, `Object.values(location) .map()`, `Object.values(location) .map(loc => loc?.replace(/\W+/g, " ")) .filter()`, `loc?.replace()`, `loc?.trim()`, `locValues.map()`, `locValues.map(loc => `\\b${loc}\\b`).join()`, `query .replace()`, `query .replace(/\W+/g, " ") .replace()`, `query .replace(/\W+/g, " ") .replace(locRegex, "") .split()`, `query .replace(/\W+/g, " ") .replace(locRegex, "") .split(/\W+/) .filter()`, `subjectWords.join()`, `this.#cleanSubject()`
- 参照: `location.city`, `location.state`, `word.length`

## _MLSuggest.#cleanSubject()
- 位置: L446-451
- 役割: 末尾が前置詞(in、at、on、for、to、near)の語を取り除く。
- 触るとき: 件名の末尾に前置詞が残る問題を調べるとき、または前置詞の一覧を変えるとき。
- 呼び出し先: `PREPOSITIONS.includes()`, `words.pop()`
- 参照: `words.length`
