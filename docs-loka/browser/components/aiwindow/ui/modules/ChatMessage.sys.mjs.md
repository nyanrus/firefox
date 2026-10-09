# browser/components/aiwindow/ui/modules/ChatMessage.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatMessage.sys.mjs
source-hash: 41347a167619655f7362b9e97c08daf6735b5adc
lines: 408

## <module>
- 役割: チャットメッセージと、履歴・メニュー表示用の軽量な会話情報クラスを定義する。

## normalizeFollowUp()
- 位置: L22-31
- 役割: フォローアップ提案の末尾の句読点を外し、空白と句読点の前後の空白を整える。
- 触るとき: 提案チップの表示文字列を変えるとき、または提案の見た目に余分な空白や記号が出る問題を調べるとき。
- 呼び出し先: `value .replace()`, `value .replace(/[.!?…]+\s*$/u, "") .trim()`, `value .replace(/[.!?…]+\s*$/u, "") .trim() .replace()`, `value .replace(/[.!?…]+\s*$/u, "") .trim() .replace(/\s+/g, " ") .replace()`

## ChatMessage.constructor()
- 位置: L129-189
- 役割: メッセージの共通項目と、アシスタント・ツール・ユーザー向けの付帯情報を設定し、トークン配列を空で用意する。
- 触るとき: メッセージに新しい属性を足すとき、またはDBから復元した行が既定値で埋まる経路を確認するとき。
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`, `super()`
- 参照: `this.citations`, `this.convId`, `this.followUpSuggestions`, `this.historyResults`, `this.isActiveBranch`, `this.memoriesApplied`, `this.memoriesEnabled`, `this.memoriesFlagSource`, `this.pageHistoryDeleted`, `this.pageUrl`, `this.revisionRootMessageId`, `this.tokens`, `this.toolUIData`, `this.toolUIDraft`, `this.webSearchQueries`

## ChatMessage.addTokens()
- 位置: L198-226
- 役割: モデルのストリームから来たトークンを種類ごとに振り分け、記憶・検索語・提案・種別の各欄へ追加する。
- 触るとき: トークンの種類を増やすとき、または記憶の適用や検索語の表示が欠ける問題を調べるとき。提案は正規化後に空なら捨てる。
- 呼び出し先: `Array.isArray()`, `this.followUpSuggestions.push()`, `this.memoriesApplied.push()`, `this.webSearchQueries.push()`, `tokens.forEach()`
- 条件付き依存: `if (key == TOKEN_LABELS.FOLLOWUP)` → `normalizeFollowUp()`
- 条件付き依存: `if (Array.isArray(this.tokens[key]))` → `this.tokens[key].push()`
- 参照: `TOKEN_LABELS.EXISTING_MEMORY`, `TOKEN_LABELS.FOLLOWUP`, `TOKEN_LABELS.KIT`, `TOKEN_LABELS.SEARCH`, `this.kit`, `this.tokens`

## AssistantRoleOpts.constructor()
- 位置: L257-275
- 役割: アシスタント応答の保存時に使うモデル ID、パラメータ、使用量、記憶と検索の情報を保持する。
- 触るとき: アシスタントメッセージに保存する項目を増やす・既定値を変えるとき。
- 参照: `this.followUpSuggestions`, `this.memoriesApplied`, `this.memoriesEnabled`, `this.memoriesFlagSource`, `this.modelId`, `this.params`, `this.usage`, `this.webSearchQueries`

## ToolRoleOpts.constructor()
- 位置: L288-290
- 役割: ツールメッセージ用にモデル ID だけを保持する。
- 触るとき: ツールメッセージに付ける項目を増やすとき。
- 参照: `this.modelId`

## UserRoleOpts.constructor()
- 位置: L306-318
- 役割: ユーザー発言用に、元となる発言 ID、記憶の設定、コンテキストメンションを保持する。
- 触るとき: ユーザー発言の付帯情報を増やすとき、または編集・再生成で元の発言 ID がどう引き継がれるかを調べるとき。
- 参照: `this.contextMentions`, `this.memoriesEnabled`, `this.memoriesFlagSource`, `this.revisionRootMessageId`

## ChatMinimal.constructor()
- 位置: L336-340
- 役割: 履歴メニュー向けに会話 ID、タイトル、ページ URL を保持する。
- 触るとき: 履歴メニューに渡す会話情報の項目を変えるとき。
- 参照: `this.#id`, `this.#pageUrl`, `this.#title`

## ChatMinimal.id()
- 位置: L342-344
- 役割: 会話 ID を返す。
- 触るとき: 履歴メニューの項目から会話を特定する処理を変えるとき。
- 参照: `this.#id`

## ChatMinimal.title()
- 位置: L346-348
- 役割: 会話のタイトルを返す。
- 触るとき: 履歴メニューに表示される名前の出どころを調べるとき。
- 参照: `this.#title`

## ChatMinimal.pageUrl()
- 位置: L350-352
- 役割: 会話に紐づくページ URL を返す。ページに紐づかない会話では null。
- 触るとき: 履歴メニューのファビコン表示を調べるとき、またはページ未指定の会話の扱いを変えるとき。
- 参照: `this.#pageUrl`

## ChatHistoryResult.constructor()
- 位置: L365-371
- 役割: チャット履歴画面向けに会話 ID、タイトル、作成日時、更新日時、URL 一覧を保持する。
- 触るとき: チャット履歴画面に渡す項目を増やす・変えるとき。
- 参照: `this.#convId`, `this.#createdDate`, `this.#title`, `this.#updatedDate`, `this.#urls`

## ChatHistoryResult.convId()
- 位置: L376-378
- 役割: 会話 ID を返す。
- 触るとき: 履歴画面の行から会話を開く・削除する処理を変えるとき。
- 参照: `this.#convId`

## ChatHistoryResult.title()
- 位置: L383-385
- 役割: 会話のタイトルを返す。
- 触るとき: 履歴画面に表示される名前を調べるとき。
- 参照: `this.#title`

## ChatHistoryResult.createdDate()
- 位置: L390-392
- 役割: 会話の作成日時を返す。
- 触るとき: 履歴画面の日付表示や並び順を調べるとき。
- 参照: `this.#createdDate`

## ChatHistoryResult.updatedDate()
- 位置: L397-399
- 役割: 会話の更新日時を返す。
- 触るとき: 履歴画面で最終更新の表示や並び替えを変えるとき。
- 参照: `this.#updatedDate`

## ChatHistoryResult.urls()
- 位置: L404-406
- 役割: 会話で扱った URL の一覧を返す。
- 触るとき: 履歴画面で会話に紐づく URL を表示・検索する処理を変えるとき。
- 参照: `this.#urls`
