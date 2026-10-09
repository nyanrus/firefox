# browser/components/aiwindow/models/Conversation.sys.mjs

source: browser/components/aiwindow/models/Conversation.sys.mjs
source-hash: 2c4e48cf2993f2d0102e119a5b1df9e2e49ba2ad
lines: 523

## <module>
- 役割: AI ウィンドウの LLM 会話の基底クラス Conversation と、メッセージ役割の定数 MESSAGE_ROLE / ROLE_LABEL を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`

## Conversation.constructor()
- 位置: L113-144
- 役割: id・日時・メッセージ・既知 URL 集合・エンジンとパラメータを受け取り、securityProperties を生成または復元する。
- 触るとき: 会話の保存データから復元する項目を増やすとき、または securityProperties が復元されない問題を調べるとき。
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`
- 条件付き依存: `if (securityProperties != null)` → `SecurityProperties.fromJSON()`
- 参照: `this.#messages`, `this.createdDate`, `this.engine`, `this.feature`, `this.id`, `this.parameters`, `this.securityProperties`, `this.seenUrls`, `this.serpUrlsForAnonymousFetch`, `this.updatedDate`

## Conversation.messages()
- 位置: L146-148
- 役割: messages の setter で内部の #messages 配列を差し替える。
- 触るとき: 外から会話のメッセージ配列を丸ごと入れ替える経路を追うとき。
- 参照: `this.#messages`

## Conversation.messages()
- 位置: L150-152
- 役割: 内部の #messages 配列をそのまま返す getter。
- 触るとき: メッセージ一覧を読む側の挙動を調べるとき、または配列の直接変更が意図せず効く箇所を探すとき。
- 参照: `this.#messages`

## Conversation.messageCount()
- 位置: L154-156
- 役割: 内部メッセージ配列の件数を返す。
- 触るとき: ツール呼び出しのテレメトリや UI が件数を参照するとき。
- 参照: `this.#messages.length`

## Conversation.save()
- 位置: async L166-174
- 役割: 基底 Conversation だけ ConversationStore へ保存し、サブクラスから呼ばれたら例外で止める。
- 触るとき: 会話の保存先を変えるとき、または ChatConversation など派生クラスが保存できない理由を追うとき。
- 呼び出し先: `lazy.ConversationStore.updateConversation()`
- 参照: `this.constructor`, `this.constructor.name`

## Conversation.isReady()
- 位置: L177-179
- 役割: エンジンの engineStatus が ready かを返す。
- 触るとき: モデル未準備時に送信を止める判定を変えるとき。
- 参照: `this.engine?.engineInstance?.engineStatus`

## Conversation.currentTurnIndex()
- 位置: L185-190
- 役割: 全メッセージの turnIndex の最大値を返し、無ければ 0 を返す。
- 触るとき: 新しいメッセージに振るターン番号の決まり方を変えるとき、またはターンの連番がずれるとき。
- 呼び出し先: `Math.max()`, `this.#messages.reduce()`
- 参照: `message.turnIndex`

## Conversation.systemPromptVersion()
- 位置: L197-200
- 役割: 先頭のシステムメッセージの content.version を返し、無ければ空文字を返す。
- 触るとき: ツール呼び出しのログにプロンプト版を載せる仕組みを確認するとき、またはプロンプト版が空になる原因を探すとき。
- 呼び出し先: `this.#messages.find()`
- 参照: `MESSAGE_ROLE.SYSTEM`, `m.role`, `sysMsg?.content?.version`

## Conversation.addMessage()
- 位置: L211-233
- 役割: 直前のメッセージを親とし、既存の最大 ordinal より 1 大きい値を振ってメッセージを末尾に追加する。
- 触るとき: メッセージ追加時の親子関係や ordinal の採番を変えるとき。
- 呼び出し先: `Math.max()`, `this.#messages.map()`, `this.#messages.push()`, `this._createMessage()`
- 参照: `m.ordinal`, `this.#messages`, `this.#messages.length`, `this.#messages[this.#messages.length - 1].id`, `this._minNextOrdinal`

## Conversation._createMessage()
- 位置: L235-237
- 役割: 引数から Message インスタンスを生成する。サブクラスが差し替えられる生成点。
- 触るとき: 派生クラスで独自の Message を使わせたいとき。

## Conversation.addUserMessage()
- 位置: L239-245
- 役割: 現在のターン番号に 1 を足した turnIndex でユーザーのメッセージを追加する。
- 触るとき: ユーザー発言が新しいターンとして数えられない問題を調べるとき。
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.USER`

## Conversation.addAssistantMessage()
- 位置: L247-261
- 役割: tool_calls があれば本文と合わせた content を作り、現在のターン番号でアシスタントのメッセージを追加する。
- 触るとき: アシスタントのツール呼び出しを履歴に保存する形を変えるとき。
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `opts.tool_calls`

## Conversation.setSystemMessage()
- 位置: L271-286
- 役割: 先頭がシステムメッセージなら内容を置き換え、無ければ ordinal 0 で先頭に挿入する(冪等)。
- 触るとき: システムプロンプトの差し替えや版の記録方法を変えるとき。
- 呼び出し先: `this.#messages.unshift()`, `this._createMessage()`
- 参照: `MESSAGE_ROLE.SYSTEM`, `this.#messages`, `this.#messages[0].content`, `this.#messages[0]?.role`

## Conversation.addToolMessage()
- 位置: L288-295
- 役割: tool_call_id と name を持つ tool 役割のメッセージを現在のターンに追加する。
- 触るとき: ツール結果を会話に追加する際の項目を増やすとき、または tool メッセージが対応する呼び出しと結びつかないとき。
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.TOOL`

## Conversation.removeLastMessage()
- 位置: L297-299
- 役割: 末尾のメッセージを取り除いて返す。
- 触るとき: 送信失敗時などに直前の発言を取り消す処理を追うとき。
- 呼び出し先: `this.#messages.pop()`

## Conversation.clearMessages()
- 位置: L301-303
- 役割: メッセージ配列を空にする。
- 触るとき: 会話をリセットする経路を変えるとき。
- 参照: `this.#messages`

## Conversation.replaceMessages()
- 位置: L305-307
- 役割: メッセージ配列を渡された配列に丸ごと置き換える。
- 触るとき: 要約や圧縮の結果で履歴を入れ替えるとき。
- 参照: `this.#messages`

## Conversation.retryMessage()
- 位置: L316-329
- 役割: 指定メッセージ以降を切り取って返し、切り取り前の最大 ordinal を下限として保持して ordinal の再利用を防ぐ。
- 触るとき: 再生成で途中から履歴を巻き戻すとき、または再生成後の ordinal 衝突を調べるとき。
- 呼び出し先: `Math.max()`, `this.#messages.findIndex()`, `this.#messages.map()`, `this.#messages.splice()`
- 参照: `m.id`, `m.ordinal`, `message.id`, `this._minNextOrdinal`

## Conversation.compactChatCompletions()
- 位置: L332-334
- 役割: chat-completions 形式の履歴を compactMessages で圧縮して返す。
- 触るとき: モデルに送るトークン量を減らす圧縮の対象や方法を変えるとき。
- 呼び出し先: `compactMessages()`, `this.getMessagesInChatCompletionsFormat()`

## Conversation.getMessagesInChatCompletionsFormat()
- 位置: L341-366
- 役割: 内部メッセージを role・content・tool_calls・tool_call_id・name を持つ chat-completions の配列に変換する。tool の content は JSON 文字列にする。
- 触るとき: モデルへ送る履歴の形式を変えるとき、またはツール結果が正しい形でモデルに届かないとき。
- 呼び出し先: `this.#messages.map()`
- 条件付き依存: `if (msg.role === "tool")` → `JSON.stringify()`
- 参照: `bodyOrContent.tool_calls`, `message.content`, `message.content?.body`, `message.content?.name`, `message.content?.tool_call_id`, `message.role`, `message.toolCallId`, `message.toolName`, `msg.content`, `msg.name`, `msg.role`, `msg.tool_call_id`, `msg.tool_calls`

## Conversation.handleChunk()
- 位置: L378-391
- 役割: ストリームの 1 チャンクを parser で分け、平文を現在のメッセージ本文に追記し、トークンを addTokens に渡す。
- 触るとき: ストリーム中の本文更新やトークン(検索・記憶の印)の扱いを変えるとき。
- 呼び出し先: `Boolean()`, `consumeStreamChunk()`
- 条件付き依存: `if (tokens)` → `currentMessage?.addTokens()`
- 参照: `currentMessage.content.body`, `currentMessage?.content`

## Conversation.receiveResponse()
- 位置: async L400-424
- 役割: ストリームを順に読み、本文を追記しながらツール呼び出しと usage を集め、末尾の残りを flush して返す。
- 触るとき: モデル応答の受信・集計の処理を変えるとき、またはストリームの本文が途中で欠けるとき。
- 呼び出し先: `createParserState()`, `flushTokenRemainder()`
- 条件付き依存: `if (chunk.text)` → `this.handleChunk()`
- 参照: `chunk.text`, `chunk.toolCalls`, `chunk?.toolCalls?.length`, `chunk?.usage`, `currentMessage.content.body`, `currentMessage?.content`

## Conversation.run()
- 位置: async L439-446
- 役割: セキュリティ属性を commit してから、履歴の chat-completions 形式と推論パラメータを engine.run に渡す。
- 触るとき: 非ストリーミングでのモデル呼び出し条件を変えるとき。
- 呼び出し先: `this.engine.run()`, `this.getMessagesInChatCompletionsFormat()`, `this.securityProperties.commit()`
- 参照: `opts.inferenceParams`, `this.parameters`

## Conversation.runWithGenerator()
- 位置: L456-465
- 役割: セキュリティ属性を commit してから、args が無ければ履歴を作り、推論パラメータを合わせて engine.runWithGenerator にストリーム生成を委譲する。
- 触るとき: ストリーミング呼び出しへ渡す引数やパラメータを変えるとき、またはセキュリティ属性の commit のタイミングを調べるとき。
- 呼び出し先: `this.engine.runWithGenerator()`, `this.getMessagesInChatCompletionsFormat()`, `this.securityProperties.commit()`
- 参照: `opts.args`, `opts.inferenceParams`, `this.parameters`

## Conversation.toJSON()
- 位置: L467-475
- 役割: id・日時・feature・メッセージを持つ保存用オブジェクトを返す(engine や securityProperties は含めない)。
- 触るとき: 保存データに項目を加えるとき、または保存時に欠ける項目を調べるとき。
- 参照: `this.#messages`, `this.createdDate`, `this.feature`, `this.id`, `this.updatedDate`

## Conversation.addSeenUrls()
- 位置: L482-486
- 役割: 渡された URL をすべて seenUrls 集合に追加する。
- 触るとき: 会話で既に見た URL の記録条件を変えるとき。
- 呼び出し先: `this.seenUrls.add()`

## Conversation.addSerpUrlsForAnonymousFetch()
- 位置: L493-497
- 役割: 渡された URL を serpUrlsForAnonymousFetch 集合に追加する。
- 触るとき: 匿名取得を許可する SERP 由来の URL の登録条件を変えるとき。
- 呼び出し先: `this.serpUrlsForAnonymousFetch.add()`

## Conversation.getAllMentionURLs()
- 位置: L507-521
- 役割: 全メッセージの contextMentions から、グループに属さない URL を集めて Set で返す。
- 触るとき: ユーザーがメンションした URL に高い権限を与える範囲を変えるとき、またはタブグループ由来の URL が除外される理由を確認するとき。
- 条件付き依存: `if (url && !groupId)` → `mentionUrls.add()`
- 参照: `message.content`, `this.messages`
