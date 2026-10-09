# browser/components/aiwindow/models/SmartFormFillModel.sys.mjs

source: browser/components/aiwindow/models/SmartFormFillModel.sys.mjs
source-hash: d25ee50d4a54bdb64fa819b960c2f998c4142702
lines: 701

## <module>
- 役割: フォーム自動入力(Smart Form Fill)で LLM を呼ぶ処理を定義する。フィールドの分類、関連タブの選択、値の生成を行い、値の生成は並列数を絞ったバッチに分けて実行する。

## startPendingValuesBatchRequests()
- 位置: L212-236
- 役割: 同時実行数の上限(2)まで待ち行列からバッチを取り出して実行し、完了ごとに次を起動する。
- 触るとき: 値生成の同時実行数を変えるとき、または待ちが進まない問題を調べるとき。
- 呼び出し先: `generateFormValuesBatch()`, `generateFormValuesBatch(request, options).then()`, `options.signal?.removeEventListener()`, `pendingValuesBatchRequests.shift()`, `reject()`, `resolve()`, `startPendingValuesBatchRequests()`
- 参照: `pendingRequest.onAbort`, `pendingValuesBatchRequests.length`

## queueValuesBatchRequest()
- 位置: L247-275
- 役割: バッチを待ち行列に積んで Promise を返す。中断シグナルが来たら待ち行列から外して拒否する。
- 触るとき: 値生成の中断(キャンセル)の挙動を変えるとき。
- 呼び出し先: `Promise.withResolvers()`, `pendingValuesBatchRequests.push()`, `signal?.throwIfAborted()`, `startPendingValuesBatchRequests()`
- 条件付き依存: `if (signal)` → `signal.addEventListener()`
- 参照: `pendingRequest.onAbort`

## pendingRequest.onAbort()
- 位置: L261-268
- 役割: 待ち行列にあるバッチが中断されたとき、そのバッチを行列から取り除いて中断理由で拒否する。
- 触るとき: 待機中の中断で残骸が残る、または拒否されない問題を調べるとき。
- 呼び出し先: `pendingValuesBatchRequests.indexOf()`, `pendingValuesBatchRequests.splice()`, `reject()`
- 参照: `signal.reason`

## tokenizeUrl()
- 位置: L372-374
- 役割: URL を UrlTokenizer で短い §url_token§ 形式に変える。モデルが URL を繰り返せるようにするため。
- 触るとき: モデルへ渡す URL の形式(トークン化)を変えるとき。
- 呼び出し先: `urlTokenizer.encodeToken()`

## resolveUrlTokens()
- 位置: L386-391
- 役割: 文字列中の URL トークンを実 URL に戻し、解決できない残りのトークンは取り除く。文字列以外は空文字を返す。
- 触るとき: モデルが返した値に URL が混ざって入力欄に出る問題を調べるとき。
- 呼び出し先: `expandUrlTokens()`, `stripUnresolvedUrlTokens()`

## generateFormValuesBatch()
- 位置: async L405-472
- 役割: 分類用のシステム指示とユーザー入力を組み立て、JSON スキーマ付きで LLM を呼び、結果を fields・memories_used・tabs_used の形で返す。
- 触るとき: 値生成の入力データやスキーマ、プロンプトの版の扱いを変えるとき。
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `buildConversation()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `loadPrompt()`, `makeJSONSchemaBlob()`, `onDispatch()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `request.context.relevantTabs.map()`, `request.page.title.substring()`, `signal?.throwIfAborted()`, `tab.title.substring()`, `tokenizeUrl()`
- 参照: `MODEL_FEATURES.SMART_FORM_FILL`, `conversation.engine.model`, `request.candidates`, `request.context.memories`, `request.context.pageText`, `request.fields`, `request.page.url`, `tab.url`

## isRetryableRequestError()
- 位置: L485-487
- 役割: エラーが再試行可能かを openAIEngine の判定に委ねて返す。
- 触るとき: 再試行の条件を変えるとき。
- 呼び出し先: `openAIEngine.isRetryableError()`

## classifyFields()
- 位置: async L499-550
- 役割: ページの URL とタイトル、フィールド情報を入れて、各フィールドの種類と確信度を LLM に分類させる。
- 触るとき: フィールドの分類結果が合わない、または分類用プロンプトを変えるとき。
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `buildConversation()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `loadPrompt()`, `makeJSONSchemaBlob()`, `onDispatch()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `request.page.title.substring()`, `signal?.throwIfAborted()`, `urlTokenizer.encodeToken()`
- 参照: `MODEL_FEATURES.SMART_FORM_FILL`, `conversation.engine.model`, `request.fields`, `request.page.url`

## findRelevantTabs()
- 位置: async L562-625
- 役割: 開いているタブの中から、フォーム入力に使えそうなタブを最大数まで LLM に選ばせる。
- 触るとき: 入力に使うタブの選び方や件数上限を変えるとき。
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `buildConversation()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `loadPrompt()`, `makeJSONSchemaBlob()`, `onDispatch()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `request.page.title.substring()`, `request.tabs.map()`, `signal?.throwIfAborted()`, `tab.title.substring()`, `urlTokenizer.encodeToken()`
- 参照: `MODEL_FEATURES.SMART_FORM_FILL`, `conversation.engine.model`, `request.fields`, `request.maxSelectedTabs`, `request.page.url`, `tab.url`

## generateFormValues()
- 位置: async L640-699
- 役割: フィールドを 20 件ずつのバッチに分けて並列に値生成を依頼し、成功したバッチの結果を統合して URL トークンを戻す。全部失敗したら最初の失敗を投げる。
- 触るとき: フォーム値の生成単位や部分失敗の扱いを変えるとき。フィールドが空の場合は results[0] を参照して TypeError になる(要確認: 呼び出し側で空を弾いているか)。
- 呼び出し先: `Promise.allSettled()`, `fulfilled .flatMap()`, `fulfilled .flatMap(({ value }) => value.fields ?? []) .map()`, `fulfilled.flatMap()`, `queueValuesBatchRequest()`, `request.fields.slice()`, `requests.push()`, `resolveUrlTokens()`, `results.filter()`, `signal?.throwIfAborted()`
- 条件付き依存: `if (tabUrl)` → `tabsUsed.add()`
- 参照: `field.value`, `fulfilled.length`, `request.fields.length`, `results.length`, `results[0].reason`, `value.fields`, `value.memories_used`, `value.tabs_used`
