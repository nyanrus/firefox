# browser/components/aboutlogins/AboutLoginsChild.sys.mjs

source: browser/components/aboutlogins/AboutLoginsChild.sys.mjs
source-hash: 967023b4e8bac2133b50705b6664fa570b8642c4
lines: 319

## <module>
- 役割: about:logins の子アクター AboutLoginsChild。ページ側の要求を親アクターへのメッセージに変換し、親からの応答をページのイベントとして返す。
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`

## recordTelemetryEvent()
- 位置: L24-34
- 役割: イベント名に対応する Glean.pwmgr の指標に extra(value があれば extra.value)を record する。失敗はコンソールに出して握りつぶす。
- 触るとき: about:logins のテレメトリ項目を追加・変更するとき。指標名は Glean の pwmgr に定義されている必要がある。
- 呼び出し先: `Glean.pwmgr[name].record()`, `console.error()`
- 参照: `Glean.pwmgr`, `extra.value`

## AboutLoginsChild.handleEvent()
- 位置: L37-100
- 役割: ページが発行したカスタムイベントの type で振り分け、対応する private メソッドを呼ぶ。
- 触るとき: ページから新しい操作イベントを追加するとき、ここに振り分けを足す必要がある。
- 呼び出し先: `this.#aboutLoginsCopyLoginDetail()`, `this.#aboutLoginsCreateLogin()`, `this.#aboutLoginsDeleteLogin()`, `this.#aboutLoginsExportPasswords()`, `this.#aboutLoginsGetHelp()`, `this.#aboutLoginsImportFromBrowser()`, `this.#aboutLoginsImportFromFile()`, `this.#aboutLoginsImportReportInit()`, `this.#aboutLoginsInit()`, `this.#aboutLoginsOpenPreferences()`, `this.#aboutLoginsRecordTelemetryEvent()`, `this.#aboutLoginsRemoveAllLogins()`, `this.#aboutLoginsSortChanged()`, `this.#aboutLoginsSyncEnable()`, `this.#aboutLoginsUpdateLogin()`
- 参照: `event.detail`, `event.type`

## AboutLoginsChild.#aboutLoginsInit()
- 位置: L102-150
- 役割: 親に Subscribe を送り、ページの window に AboutLoginsUtils(一致判定・origin 取得・フォーカス・主パスワード要求など)を cloneInto で渡す。
- 触るとき: ページから呼べる補助 API を追加・変更するとき。
- 呼び出し先: `Cu.cloneInto()`, `Cu.waiveXrays()`, `this.sendAsyncMessage()`
- 参照: `this.browsingContext.window`, `waivedContent.AboutLoginsUtils`

## AboutLoginsChild.doLoginsMatch()
- 位置: L109-111
- 役割: LoginHelper.doLoginsMatch に、空のオプションを付けて委譲する。
- 触るとき: ページ側でログインの同一判定を使う箇所の挙動を変えるとき。
- 呼び出し先: `LoginHelper.doLoginsMatch()`

## AboutLoginsChild.getLoginOrigin()
- 位置: L112-114
- 役割: LoginHelper.getLoginOrigin に委譲して、URI 文字列からログインの origin を得る。
- 触るとき: ページ側で表示する origin の形式を変えるとき。
- 呼び出し先: `LoginHelper.getLoginOrigin()`

## AboutLoginsChild.setFocus()
- 位置: L115-117
- 役割: Services.focus.setFocus をキーボード由来のフラグ付きで呼び、指定要素にフォーカスを移す。
- 触るとき: ダイアログを閉じた後などのフォーカス先が意図と違うときに調べる。
- 呼び出し先: `Services.focus.setFocus()`
- 参照: `Services.focus.FLAG_BYKEY`
- XPCOM: `Services.focus`

## AboutLoginsChild.promptForPrimaryPassword()
- 位置: async L127-138
- 役割: resolve を gPrimaryPasswordPromise に保存し、親へ PrimaryPasswordRequest(messageId と reason)を送る。親の PrimaryPasswordResponse を受けて resolve される。
- 触るとき: 主パスワードや OS 認証の再入力要求の流れを変えるとき。
- 呼び出し先: `that.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsImportReportInit()
- 位置: L152-154
- 役割: 親に ImportReportInit を送る。
- 触るとき: インポート報告ページの初期化の流れを変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsCopyLoginDetail()
- 位置: L156-162
- 役割: 文字列をクリップボードに機密扱い(Sensitive)でコピーする。
- 触るとき: コピーの対象や機密属性の扱いを変えるとき。
- 呼び出し先: `lazy.ClipboardHelper.copyString()`
- 参照: `lazy.ClipboardHelper.Sensitive`, `this.windowContext`

## AboutLoginsChild.#aboutLoginsCreateLogin()
- 位置: L164-168
- 役割: login を載せて親に CreateLogin を送る。
- 触るとき: 新規作成時に親へ渡すデータを変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsDeleteLogin()
- 位置: L170-174
- 役割: login を載せて親に DeleteLogin を送る。
- 触るとき: 削除時に親へ渡すデータを変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsExportPasswords()
- 位置: L176-178
- 役割: 親に ExportPasswords を送る。
- 触るとき: エクスポートの経路を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsGetHelp()
- 位置: L180-182
- 役割: 親に GetHelp を送る。
- 触るとき: ヘルプ導線の経路を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsImportFromBrowser()
- 位置: L184-189
- 役割: 親に ImportFromBrowser を送り、mgmtMenuItemUsedImportFromBrowser を記録する。
- 触るとき: ブラウザからのインポート導線を変えるとき、またはその計測を調べるとき。
- 呼び出し先: `recordTelemetryEvent()`, `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsImportFromFile()
- 位置: L191-196
- 役割: 親に ImportFromFile を送り、mgmtMenuItemUsedImportFromCsv を記録する。
- 触るとき: ファイルからのインポート導線を変えるとき、またはその計測を調べるとき。
- 呼び出し先: `recordTelemetryEvent()`, `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsOpenPreferences()
- 位置: L198-203
- 役割: 親に OpenPreferences を送り、mgmtMenuItemUsedPreferences を記録する。
- 触るとき: 設定を開く導線を変えるとき。
- 呼び出し先: `recordTelemetryEvent()`, `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsRecordTelemetryEvent()
- 位置: L205-225
- 役割: openManagement で始まるイベントは、同じブラウザで 5 秒(TELEMETRY_MIN_MS_BETWEEN_OPEN_MANAGEMENT)以内の重複を捨ててから記録する。それ以外はそのまま記録する。
- 触るとき: 管理画面を開いた回数の計測を変えるとき。リダイレクトによる二重計上を調べるとき。
- 呼び出し先: `event.detail.name.startsWith()`, `recordTelemetryEvent()`
- 条件付き依存: `if (event.detail.name.startsWith("openManagement"))` → `docShell.now()`
- 参照: `event.detail`, `this.browsingContext`, `this.browsingContext.browserId`

## AboutLoginsChild.#aboutLoginsRemoveAllLogins()
- 位置: L227-229
- 役割: 親に RemoveAllLogins を送る。
- 触るとき: すべて削除の経路を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsSortChanged()
- 位置: L231-233
- 役割: 並び順の detail を親に SortChanged として送る。
- 触るとき: 並び順の保存や通知の仕組みを変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsSyncEnable()
- 位置: L235-237
- 役割: 親に SyncEnable を送る。
- 触るとき: Sync 有効化の経路を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.#aboutLoginsUpdateLogin()
- 位置: L239-243
- 役割: login を載せて親に UpdateLogin を送る。
- 触るとき: 編集・保存時に親へ渡すデータを変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsChild.receiveMessage()
- 位置: L246-278
- 役割: 親からのメッセージ名で振り分ける。ImportReportData・PrimaryPasswordResponse・RemaskPassword・Setup は専用処理へ回し、WaitForFocus は document がフォーカスを得るまで待つ Promise を返す。それ以外は名前から AboutLogins: を外してページへ流す。
- 触るとき: 親から届く新しいメッセージを扱うとき、または専用処理に回すメッセージを増やすとき。
- 呼び出し先: `this.#importReportData()`, `this.#passMessageDataToContent()`, `this.#primaryPasswordResponse()`, `this.#remaskPassword()`, `this.#setup()`, `this.document.hasFocus()`
- 条件付き依存: `if (!this.document.hasFocus())` → `this.document.documentGlobal.addEventListener()`
- 条件付き依存: `if (!this.document.hasFocus())` → `resolve()`
- 条件付き依存: `if (!(!this.document.hasFocus()))` → `resolve()`
- 参照: `message.data`, `message.name`

## AboutLoginsChild.#importReportData()
- 位置: L280-282
- 役割: 受け取ったデータを ImportReportData としてページへ送る。
- 触るとき: インポート報告に渡るデータの形式を変えるとき。
- 呼び出し先: `this.sendToContent()`

## AboutLoginsChild.#primaryPasswordResponse()
- 位置: L284-289
- 役割: 保留中の主パスワード要求があれば、結果で resolve し、添付の telemetryEvent を記録する。
- 触るとき: 主パスワードの入力結果の扱いや、その計測を変えるとき。
- 条件付き依存: `if (gPrimaryPasswordPromise)` → `gPrimaryPasswordPromise.resolve()`
- 条件付き依存: `if (gPrimaryPasswordPromise)` → `recordTelemetryEvent()`
- 参照: `data.result`, `data.telemetryEvent`

## AboutLoginsChild.#remaskPassword()
- 位置: L291-293
- 役割: RemaskPassword をページへ送る。
- 触るとき: パスワードの再マスクの通知経路を変えるとき。
- 呼び出し先: `this.sendToContent()`

## AboutLoginsChild.#setup()
- 位置: L295-304
- 役割: 主パスワード有無・パスワード表示可否・インポート可否・サポート URL の基準を AboutLoginsUtils に書き込んでから、Setup をページへ送る。
- 触るとき: ページ初期化時に親から渡す設定項目を増やすとき。
- 呼び出し先: `Cu.waiveXrays()`, `Services.urlFormatter.formatURLPref()`, `this.sendToContent()`
- 参照: `Cu.waiveXrays(this.browsingContext.window).AboutLoginsUtils`, `data.importVisible`, `data.passwordRevealVisible`, `data.primaryPasswordEnabled`, `this.browsingContext.window`, `utils.importVisible`, `utils.passwordRevealVisible`, `utils.primaryPasswordEnabled`, `utils.supportBaseURL`
- XPCOM: `Services.urlFormatter`

## AboutLoginsChild.#passMessageDataToContent()
- 位置: L306-308
- 役割: メッセージ名から AboutLogins: を外した名前で、データをそのままページへ送る。
- 触るとき: 親が新しい種類のメッセージを送り、ページまで届くかを確認するとき。
- 呼び出し先: `message.name.replace()`, `this.sendToContent()`
- 参照: `message.data`

## AboutLoginsChild.sendToContent()
- 位置: L310-317
- 役割: messageType と value を持つ AboutLoginsChromeToContent を作り、ページの window に cloneInto して発行する。
- 触るとき: 親からページへ送る共通の経路や形式を変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `Object.assign()`, `win.dispatchEvent()`
- 参照: `this.document.defaultView`, `win.CustomEvent`
