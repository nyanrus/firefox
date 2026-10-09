# browser/components/extensions/parent/ext-omnibox.js

source: browser/components/extensions/parent/ext-omnibox.js
source-hash: 95bed5cb0078d8aa1d7023666e7c342b24bdcc8c
lines: 178

## <module>
- 役割: omnibox WebExtension API の実装。アドレスバーのキーワード登録と、入力イベントの拡張への転送を ExtensionSearchHandler に委ねる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## onInputStarted()
- 位置: L14-28
- 役割: キーワード入力の開始を通知するイベントを、ExtensionSearchHandler の MSG_INPUT_STARTED に繋ぐ。
- 触るとき: omnibox.onInputStarted が発火しない、または発火が重複するときに、登録と解除の対応を確認する。
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_STARTED`

## listener()
- 位置: L16-18
- 役割: MSG_INPUT_STARTED を受けて fire.sync() を呼び、拡張へ入力開始を通知する。
- 触るとき: onInputStarted が発火しない、または引数なしで届くべきところで別の値が出るときに見る。
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L21-23
- 役割: MSG_INPUT_STARTED のリスナーを extension から外す。
- 触るとき: 拡張を無効化した後も onInputStarted が届き続けるときに、解除が呼ばれているか確認する。
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_STARTED`

## convert()
- 位置: L24-26
- 役割: 永続イベントの再接続時に fire を新しいものへ差し替える。
- 触るとき: 拡張の background が再起動した後、古い fire に送られて通知が届かないときに見る。

## onInputCancelled()
- 位置: L29-43
- 役割: 入力のキャンセルを通知するイベントを MSG_INPUT_CANCELLED に繋ぐ。
- 触るとき: omnibox.onInputCancelled の発火条件や、解除漏れを調べるとき。
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_CANCELLED`

## listener()
- 位置: L31-33
- 役割: MSG_INPUT_CANCELLED を受けて fire.sync() を呼び、入力キャンセルを通知する。
- 触るとき: onInputCancelled が発火しないときに見る。
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L36-38
- 役割: MSG_INPUT_CANCELLED のリスナーを extension から外す。
- 触るとき: 無効化後もキャンセル通知が届くときに解除を確認する。
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_CANCELLED`

## convert()
- 位置: L39-41
- 役割: 永続イベントの再接続時に onInputCancelled の fire を差し替える。
- 触るとき: 再起動後に onInputCancelled が古い fire へ送られるときに見る。

## onInputEntered()
- 位置: L44-59
- 役割: 確定された入力を MSG_INPUT_ENTERED から受け、拡張のアクティブタブ権限を付与してから text と disposition を発火する。
- 触るとき: omnibox.onInputEntered で拡張に渡る引数を変えるときや、確定時にタブ権限が付与される流れを確認するとき。
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_ENTERED`

## listener()
- 位置: L46-49
- 役割: MSG_INPUT_ENTERED を受けて、拡張のアクティブタブ権限を付与し、text と disposition を fire.sync() する。
- 触るとき: 確定入力で拡張がタブ操作できない、または権限が付与されないタイミングを調べるとき。
- 呼び出し先: `extension.tabManager.addActiveTabPermission()`, `fire.sync()`

## unregister()
- 位置: L52-54
- 役割: MSG_INPUT_ENTERED のリスナーを extension から外す。
- 触るとき: 無効化後も確定入力が拡張へ届くときに解除を確認する。
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_ENTERED`

## convert()
- 位置: L55-57
- 役割: 永続イベントの再接続時に onInputEntered の fire を差し替える。
- 触るとき: 再起動後に確定入力が古い fire へ送られるときに見る。

## onInputChanged()
- 位置: L60-74
- 役割: 入力文字列の変化を MSG_INPUT_CHANGED から受け、text と suggestion の id を発火する。
- 触るとき: 候補の更新イベントに渡す値を変えるとき。
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_CHANGED`

## listener()
- 位置: L62-64
- 役割: MSG_INPUT_CHANGED を受けて text と id を fire.sync() する。
- 触るとき: 入力変更イベントの引数が想定と違うときに見る。
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L67-69
- 役割: MSG_INPUT_CHANGED のリスナーを extension から外す。
- 触るとき: 無効化後も入力変更が届くときに解除を確認する。
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_CHANGED`

## convert()
- 位置: L70-72
- 役割: 永続イベントの再接続時に onInputChanged の fire を差し替える。
- 触るとき: 再起動後に入力変更が古い fire へ送られるときに見る。

## onDeleteSuggestion()
- 位置: L75-89
- 役割: 候補の削除要求を MSG_INPUT_DELETED から受け、削除された text を発火する。
- 触るとき: ユーザーが候補を削除したときに拡張へ通知されない、または値が違うとき。
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_DELETED`

## listener()
- 位置: L77-79
- 役割: MSG_INPUT_DELETED を受けて削除された text を fire.sync() する。
- 触るとき: 候補削除が拡張に通知されないときに見る。
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L82-84
- 役割: MSG_INPUT_DELETED のリスナーを extension から外す。
- 触るとき: 無効化後も削除通知が届くときに解除を確認する。
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_DELETED`

## convert()
- 位置: L85-87
- 役割: 永続イベントの再接続時に onDeleteSuggestion の fire を差し替える。
- 触るとき: 再起動後に削除通知が古い fire へ送られるときに見る。

## onManifestEntry()
- 位置: L92-104
- 役割: manifest の omnibox.keyword を ExtensionSearchHandler に登録し、成功時のみ this.keyword に保持する。
- 触るとき: キーワードが登録できない、または別の拡張と衝突するときに見る。登録失敗は manifestError としてエラーになる。
- 呼び出し先: `ExtensionSearchHandler.registerKeyword()`, `extension.manifestError()`
- 参照: `e.message`, `manifest.omnibox.keyword`, `this.keyword`

## onShutdown()
- 位置: L106-108
- 役割: 拡張の終了時に this.keyword の登録を解除する。
- 触るとき: 拡張を無効化した後もキーワードがアドレスバーに残るとき。キーワード登録に失敗していた場合は undefined を渡すことになる。
- 呼び出し先: `ExtensionSearchHandler.unregisterKeyword()`
- 参照: `this.keyword`

## getAPI()
- 位置: L110-176
- 役割: omnibox API オブジェクトを組み立て、5 つのイベントと内部用の addSuggestions を返す。
- 触るとき: 拡張から見える omnibox API を増減するとき。
- 呼び出し先: `new EventManager({ context, module: "omnibox", event: "onDeleteSuggestion", extensionApi: this, }).api()`, `new EventManager({ context, module: "omnibox", event: "onInputCancelled", extensionApi: this, }).api()`, `new EventManager({ context, module: "omnibox", event: "onInputChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "omnibox", event: "onInputEntered", extensionApi: this, inputHandling: true, }).api()`, `new EventManager({ context, module: "omnibox", event: "onInputStarted", extensionApi: this, }).api()`

## setDefaultSuggestion()
- 位置: L113-123
- 役割: 登録済みキーワードの既定候補を設定する。キーワードが未登録なら例外を Promise の reject として返す。
- 触るとき: 拡張の既定候補が表示されないときや、登録失敗時のエラーメッセージを確認するとき。
- 呼び出し先: `ExtensionSearchHandler.setDefaultSuggestion()`, `Promise.reject()`
- 参照: `e.message`, `this.keyword`

## addSuggestions()
- 位置: L162-173
- 役割: 非同期に生成された候補を、キーワードと id を指定して ExtensionSearchHandler に渡す。
- 触るとき: 候補が遅れて届く、または古い id の候補が捨てられるときに見る。例外は握りつぶされる。
- 呼び出し先: `ExtensionSearchHandler.addSuggestions()`
- 参照: `this.keyword`
