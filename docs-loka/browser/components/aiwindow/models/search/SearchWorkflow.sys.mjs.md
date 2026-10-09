# browser/components/aiwindow/models/search/SearchWorkflow.sys.mjs

source: browser/components/aiwindow/models/search/SearchWorkflow.sys.mjs
source-hash: 8c613a4f954a55ab47f7a7b4218e10a6efeedfc6
lines: 1116

## <module>
- 役割: search_the_web ツールの本体。回答サービス、根拠付き、高速の3経路を設定に応じて振り分け、それぞれの検索、ページ読取り、回答の検証を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## resultIdFor()
- 位置: L270-272
- 役割: 検索結果の位置(0始まり)から result_1 のような識別子を作る。
- 触るとき: モデルに見せる結果の番号と、番号からURLへの対応表がずれないよう変えるとき。

## normalizeAndTruncateText()
- 位置: L287-299
- 役割: スニペットの空白を詰め、2000字を超える分を切って省略記号を付け、切った字数も返す。高速経路で使う。
- 触るとき: 高速経路でスニペットが切れすぎる、または長すぎるとき、上限を変えるとき。
- 呼び出し先: `collapsed.slice()`, `text.replace()`, `text.replace(/\s+/g, " ").trim()`
- 参照: `collapsed.length`

## isValidHttpUrl()
- 位置: L309-315
- 役割: URLがhttpかhttpsとして解釈できるかを判定し、javascript:やdata:などを弾く。
- 触るとき: 検索結果のURLが除外される原因を調べるとき、許可するスキームを変えるとき。
- 呼び出し先: `URL.parse()`
- 参照: `parsed?.protocol`

## buildUserMessage()
- 位置: L329-346
- 役割: 現在の日付、質問、文脈(あれば)、番号付きの検索結果を並べ、タイトルとスニペットをサニタイズしてモデルに渡すユーザーメッセージを作る。
- 触るとき: 回答生成のモデルに渡る材料の形や、文脈の扱いを変えるとき。
- 呼び出し先: `context.trim()`, `lines.join()`, `lines.push()`, `resultIdFor()`, `results.forEach()`, `sanitizeUntrustedContent()`
- 条件付き依存: `if (context && context.trim())` → `lines.push()`
- 条件付き依存: `if (snippet)` → `lines.push()`
- 参照: `result.snippet`, `result.title`, `result.url`

## validateSearchAnswer()
- 位置: L359-382
- 役割: モデルの出力をSEARCH_ANSWER_SCHEMAで検証する。形が合わないか、回答ありなのに本文が空なら、回答なし・確信度0に戻す。
- 触るとき: 回答が Google への引き継ぎに回される理由を調べるとき、回答のスキーマや判定を変えるとき。
- 呼び出し先: `lazy.JsonSchema.validate()`, `parsed.answer.trim()`
- 参照: `SEARCH_ANSWER_SCHEMA.schema`, `parsed.answer`, `parsed.confidence`, `parsed.could_answer`

## generateAnswer()
- 位置: async L407-514
- 役割: 根拠付き回答用のモデルで、ページ読取りのツール呼び出しを最大3ラウンド行い、その後は読取りを禁じた最終ターンで構造化JSONを出させて、パースした結果を返す。
- 触るとき: 根拠付き検索の回答が空になる、または読取りが繰り返されるとき。読取りのラウンド数や最終ターンの指示を変えるとき。
- 呼び出し先: `(Array.isArray(ids) ? ids : []) .map()`, `(Array.isArray(ids) ? ids : []) .map(id => idToUrl.get(id)) .filter()`, `Array.isArray()`, `JSON.parse()`, `Promise.all()`, `String()`, `buildUserMessage()`, `conversation.addAssistantMessage()`, `conversation.addToolMessage()`, `conversation.addUserMessage()`, `conversation.receiveResponse()`, `conversation.run()`, `conversation.runWithGenerator()`, `conversation.setSystemMessage()`, `idToUrl.get()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `pageReadCalls.map()`, `parseAndExtractJSON()`, `pendingToolCalls.filter()`, `readPage()`, `renderPrompt()`, `resultIdFor()`, `results.map()`, `texts.join()`
- 参照: `JSON.parse(call.function.arguments || "{}").result_ids`, `MODEL_FEATURES.SEARCH_ANSWER_GENERATION`, `assistantMessage.content`, `call.function.arguments`, `call.function.name`, `call.function?.name`, `call.id`, `conversation.id`, `pageReadCalls.length`, `result.url`, `signal?.aborted`

## failure()
- 位置: L524-534
- 役割: 根拠付き経路の失敗結果を作る。回答は空、could_answerはfalse、確信度0にする。
- 触るとき: 根拠付き経路が失敗したときの戻り値の形を変えるとき。

## fastFailure()
- 位置: L542-548
- 役割: 高速経路の失敗結果を作る。結果は空で、エラーの文を持つ。
- 触るとき: 高速経路の失敗の戻り値を変えるとき。

## answersFailure()
- 位置: L557-563
- 役割: 回答経路の失敗結果を作る。読んだURLは空で、エラーの文を持つ。
- 触るとき: 回答経路が失敗したときの戻り値を変えるとき。

## shouldCallSearchHandoff()
- 位置: L565-567
- 役割: 同じターンで既に検索が走っていれば真を返す。その場合は検索をせず、引き継ぎを呼ぶ。
- 触るとき: 同じターンで検索が二重に走る、または引き継ぎが呼ばれないとき。
- 呼び出し先: `conversation.currentTurnIndex()`
- 参照: `conversation._searchTheWebTurn`

## runSearchTheWeb()
- 位置: async L583-605
- 役割: 引き継ぎが必要なターンならそれを返す。それ以外は、プライベートデータと信頼できない入力の印を会話に立ててから、選ばれた経路へ振り分ける。
- 触るとき: 経路の優先順位を変えるとき、どの経路が選ばれたかを確かめるとき。
- 呼び出し先: `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `runAnswersSearch()`, `runFastSearch()`, `runGroundedSearch()`, `selectSearchTheWebPath()`, `shouldCallSearchHandoff()`
- 参照: `SEARCH_THE_WEB_PATH.ANSWERS`, `SEARCH_THE_WEB_PATH.FAST`

## recordAnswerCitations()
- 位置: L620-648
- 役割: 回答サービスが返した引用のうち、http(s)で重複しないURLを、見たURL、匿名取得の許可、引用の3か所に登録し、そのURLの一覧を返す。
- 触るとき: 回答の出典チップが表示されない、または後続のページ読取りが拒否されるとき。
- 呼び出し先: `Array.isArray()`, `conversation.addCitations()`, `conversation.addSeenUrls()`, `conversation.addSerpUrlsForAnonymousFetch()`, `isValidHttpUrl()`, `records.map()`, `records.push()`, `seen.add()`, `seen.has()`
- 参照: `citation.title`, `citation.url`, `citation?.url`, `records.length`

## requestAnswer()
- 位置: async L665-702
- 役割: 回答サービス用のエンジンを作って1回だけ呼び、空でなければ長さを切った回答と引用URLを返す。空なら例外を投げる。
- 触るとき: 回答経路で回答が返らない原因を調べるとき、回答の長さの上限を変えるとき。
- 呼び出し先: `(response?.finalOutput ?? "").trim()`, `answer.slice()`, `engine.run()`, `openAIEngine.build()`, `openAIEngine.getFxAccountToken()`, `recordAnswerCitations()`
- 参照: `MODEL_FEATURES.SEARCH_ANSWERS`, `SERVICE_TYPES.SW_ANSWER`, `answer.length`, `conversation.id`, `response?.finalOutput`, `response?.providerSpecificFields?.citations`, `signal?.aborted`

## answerAsStream()
- 位置: async L718-736
- 役割: 完成している回答を64字ほどずつ区切り、全体で約500ミリ秒になるように間を空けて流す。中断されたら止まる。
- 触るとき: 回答が表示される速さや区切り方を変えるとき。
- 呼び出し先: `Math.min()`, `chunks.entries()`, `text.match()`
- 条件付き依存: `if (index)` → `lazy.setTimeout()`
- 参照: `chunks.length`, `signal?.aborted`

## runAnswersSearch()
- 位置: async L752-782
- 役割: 問い合わせを空でないか確かめてから回答サービスに渡し、成功なら回答の流れと読んだURLを、失敗なら回答なしの結果を返す。
- 触るとき: 回答経路の入口の検証や、失敗時に引き継ぎへ戻る流れを追うとき。
- 呼び出し先: `answerAsStream()`, `answersFailure()`, `conversation.currentTurnIndex()`, `lazy.console.error()`, `lazy.console.log()`, `query.trim()`, `requestAnswer()`
- 条件付き依存: `if (typeof query !== "string" || !query.trim())` → `answersFailure()`
- 参照: `conversation._searchTheWebTurn`, `e.message`, `readUrls.length`, `toolParams?.query`

## recordFastSearchTelemetry()
- 位置: L794-814
- 役割: 高速経路の計測値を、search_the_web のGleanイベントに1回記録する。
- 触るとき: 高速経路のテレメトリの項目を増やすとき、イベントが出ないと調べるとき。
- 呼び出し先: `Glean.smartWindow.searchTheWeb.record()`, `Math.round()`
- 参照: `conversation.id`, `conversation.messageCount`, `stats.error`, `stats.httpStatus`, `stats.processing`, `stats.retrieval`, `stats.retrieved`, `stats.returned`, `stats.snippetChars`, `stats.snippetCharsDropped`

## runFastSearch()
- 位置: async L832-862
- 役割: 計測値を用意して高速経路の本体を実行する。例外は内部エラーとして記録してから投げ直し、finallyで必ずイベントを送る。
- 触るとき: 高速経路の失敗がテレメトリでどう記録されるかを調べるとき。
- 呼び出し先: `ChromeUtils.now()`, `recordFastSearchTelemetry()`, `runFastSearchFlow()`
- 参照: `SEARCH_TELEMETRY_ERRORS.INTERNAL_ERROR`, `stats.error`

## runFastSearchFlow()
- 位置: async L872-966
- 役割: 問い合わせを確かめ、Exaから最大5件取得して、URLが正しく、スニペットが25字を超えるものを3件まで残す。見たURLと引用に登録し、スニペットを整えて返す。
- 触るとき: 高速経路の件数や条件を変えるとき、結果が0件になる原因を調べるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `conversation.addCitations()`, `conversation.addSeenUrls()`, `conversation.addSerpUrlsForAnonymousFetch()`, `conversation.currentTurnIndex()`, `fastFailure()`, `isValidHttpUrl()`, `kept.map()`, `lazy.console.error()`, `lazy.console.log()`, `normalizeAndTruncateText()`, `provider.search()`, `query.trim()`, `retrieved .filter()`, `retrieved .filter( item => isValidHttpUrl(item?.url) && item?.snippet?.length > MIN_SNIPPET_LENGTH ) .slice()`, `sanitizeUntrustedContent()`
- 条件付き依存: `if (typeof query !== "string" || !query.trim())` → `fastFailure()`
- 条件付き依存: `if (!kept.length)` → `fastFailure()`
- 参照: `SEARCH_TELEMETRY_ERRORS.INVALID_QUERY`, `SEARCH_TELEMETRY_ERRORS.NO_RESULTS`, `SEARCH_TELEMETRY_ERRORS.RETRIEVAL_FAILED`, `conversation._searchTheWebTurn`, `e.message`, `e?.httpStatus`, `e?.searchErrorCategory`, `item.snippet`, `item.title`, `item.url`, `item?.snippet?.length`, `item?.url`, `kept.length`, `response.results`, `response.status`, `retrieved.length`, `snippet.droppedChars`, `snippet.text`, `snippet.text.length`, `stats.error`, `stats.httpStatus`, `stats.processing`, `stats.retrieval`, `stats.retrieved`, `stats.returned`, `stats.snippetChars`, `stats.snippetCharsDropped`, `toolParams?.query`

## runGroundedSearch()
- 位置: async L983-1115
- 役割: Exaから最大件数の結果を取り、URLが正しいものを見たURLに登録してから、回答を生成して検証する。読んだページを引用に加え、検証結果と読んだURLを返す。
- 触るとき: 根拠付き経路の全体の流れを変えるとき、could_answerがfalseになる原因を調べるとき。
- 呼び出し先: `conversation.addCitations()`, `conversation.addSeenUrls()`, `conversation.addSerpUrlsForAnonymousFetch()`, `conversation.currentTurnIndex()`, `failure()`, `generateAnswer()`, `isValidHttpUrl()`, `lazy.console.error()`, `lazy.console.log()`, `new Date().toISOString()`, `new Date().toISOString().slice()`, `openAIEngine.getFxAccountToken()`, `provider.search()`, `query.trim()`, `readUrls.map()`, `results.filter()`, `results.map()`, `titlesByUrl.get()`, `validateSearchAnswer()`
- 条件付き依存: `if (typeof query !== "string" || !query.trim())` → `failure()`
- 条件付き依存: `if (!searchedUrls.length)` → `failure()`
- 参照: `ExaSearchProvider.MAX_RESULTS`, `conversation._searchTheWebTurn`, `e.message`, `item.title`, `item.url`, `item?.url`, `readUrls.length`, `response.results`, `searchedUrls.length`, `toolParams.context`, `toolParams?.context`, `toolParams?.query`, `validated.could_answer`

## readPage()
- 位置: async L1021-1076
- 役割: 1ターンのページ読取りの上限(3ページ)を守りながら、取得済みで未読のURLだけを読む。上限到達や未読なしのときは、回答に進むよう促す文を返す。
- 触るとき: ページ読取りの上限や、重複や未取得の扱いを変えるとき。
- 呼び出し先: `Promise.all()`, `Services.prefs.getIntPref()`, `fetchableSet.has()`, `fresh.forEach()`, `fresh.map()`, `perUrl.flat()`, `readSet.add()`, `readSet.has()`, `readUrls.push()`, `requestedUrls .filter()`, `requestedUrls .filter(url => fetchableSet.has(url) && !readSet.has(url)) .slice()`
- 参照: `fresh.length`, `readUrls.length`
- XPCOM: `Services.prefs`

## readOne()
- 位置: async L1046-1072
- 役割: 1つのURLを読み、設定された時間(既定15秒)を超えたら中断して、その旨の文を返す。遅れて届いた結果の例外は捨てる。
- 触るとき: 読取りが止まる、または遅いとき、タイムアウトの時間や挙動を変えるとき。
- 呼び出し先: `GetPageContent.getPageContentText()`, `Promise.race()`, `controller.abort()`, `fetchPromise.catch()`, `lazy.clearTimeout()`, `lazy.console.warn()`, `lazy.setTimeout()`, `resolve()`
- 参照: `controller.signal`
