# browser/components/urlbar/UrlbarProviderClipboard.sys.mjs

source: browser/components/urlbar/UrlbarProviderClipboard.sys.mjs
source-hash: c9bad3fd842ef2c7e398c998e25c1f36b5af689f
lines: 169

## <module>
- 役割: 空の検索欄でクリップボードの http(s) URL を提案するプロファイル系プロバイダー。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderClipboard.constructor()
- 位置: L34-36
- 役割: プロバイダーを生成し、直前のクリップボード値と残り表示回数を初期化する。
- 触るとき: 表示回数の初期値や状態管理を変えるとき。
- 呼び出し先: `super()`

## UrlbarProviderClipboard.type()
- 位置: L41-43
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: クリップボード結果の種別と並び順の扱いを確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderClipboard.setPreviousClipboardValue()
- 位置: L45-47
- 役割: 直前のクリップボード値を外部から設定する。
- 触るとき: テストや外部からクリップボード状態を差し替える必要があるとき。
- 参照: `this.#previousClipboard.value`

## UrlbarProviderClipboard.isActive()
- 位置: async L49-91
- 役割: 空の検索で、機能フラグと設定が有効なとき、クリップボードを読んで 2048 文字以下・空白なし・http(s) の URL なら起動する。同じ URL の表示回数が尽きていれば起動しない。
- 触るとき: クリップボード提案が出る条件(空入力、長さ、空白の有無、表示回数)を変えるとき。
- 呼び出し先: `UrlbarUtils.getFixupPrimitives()`, `controller.browserWindow.readFromClipboard()`, `lazy.UrlUtils.REGEXP_SPACES.test()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.sanitizeTextFromClipboard()`, `queryContext.restrictInSearchMode()`, `this.#validUrl()`
- 参照: `queryContext.isPrivate`, `queryContext.searchString`, `textFromClipboard.length`, `this.#previousClipboard`, `this.#previousClipboard.impressionsLeft`, `this.#previousClipboard.value`

## UrlbarProviderClipboard.#validUrl()
- 位置: L93-105
- 役割: 文字列を URL として解析し、http または https なら href を返す。それ以外は null を返す。
- 触るとき: 提案対象とするスキームを増減させるとき。
- 呼び出し先: `URL.parse()`
- 参照: `givenUrl.href`, `givenUrl.protocol`

## UrlbarProviderClipboard.getPriority()
- 位置: L107-110
- 役割: 優先度として 1 を返す(ゼロ入力の提案と同等)。
- 触るとき: クリップボード提案を他のゼロ入力提案より上下させたいとき。

## UrlbarProviderClipboard.startQuery()
- 位置: async L119-138
- 役割: isActive で保存した URL から、表示用タイトルと clipboard アイコン付きの URL 結果を 1 件追加する。
- 触るとき: クリップボード結果の表示内容(タイトル、アイコン、ブロック可否)を変えるとき。
- 呼び出し先: `addCallback()`, `lazy.UrlbarShared.prepareUrlForDisplay()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `this.#previousClipboard.value`

## UrlbarProviderClipboard.onEngagement()
- 位置: L145-149
- 役割: 結果が選ばれたら表示回数を 0 にし、結果メニューのコマンド処理へ渡す。
- 触るとき: クリップボード結果を選んだ後に再表示されないようにする挙動を調べるとき。
- 呼び出し先: `this.#handlePossibleCommand()`
- 参照: `details.result`, `details.selType`, `this.#previousClipboard.impressionsLeft`

## UrlbarProviderClipboard.onImpression()
- 位置: L151-153
- 役割: 結果が表示されるたびに残り表示回数を 1 減らす。
- 触るとき: 同じクリップボード URL を何回まで表示するかを変えるとき。
- 参照: `this.#previousClipboard.impressionsLeft`

## UrlbarProviderClipboard.#handlePossibleCommand()
- 位置: L160-167
- 役割: 結果メニューの「削除」が選ばれたら結果を消し、表示回数を 0 にする。
- 触るとき: クリップボード結果の削除メニューの挙動を変えるとき。
- 呼び出し先: `controller.removeResult()`
- 参照: `RESULT_MENU_COMMANDS.DISMISS`, `this.#previousClipboard.impressionsLeft`
