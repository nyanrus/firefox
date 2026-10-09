# browser/components/urlbar/UrlbarProviderOmnibox.sys.mjs

source: browser/components/urlbar/UrlbarProviderOmnibox.sys.mjs
source-hash: 03bef140a3a6f171d0a03381ccb7b396c66c96a7
lines: 183

## <module>
- 役割: WebExtensions の omnibox API で登録されたキーワードの入力を拾い、拡張機能に検索を依頼して候補を返すプロバイダー。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderOmnibox.constructor()
- 位置: L33-35
- 役割: プロバイダーを生成する(super のみ)。
- 触るとき: コンストラクタに初期状態を足すときのみ。
- 呼び出し先: `super()`

## UrlbarProviderOmnibox.type()
- 位置: L40-42
- 役割: プロバイダー種別として HEURISTIC を返す。
- 触るとき: omnibox 結果を他のヒューリスティック結果と並べる順序を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderOmnibox.isActive()
- 位置: async L52-77
- 役割: 先頭トークンが登録済みキーワードで、後続の文字列があり、検索モードでなければ true。そうでなければ入力セッションが残っていれば拡張機能へキャンセルを通知し、false を返す。
- 触るとき: 拡張機能のキーワードへ入る条件を変えたり、入力キャンセル時の後始末を調べたりするとき。
- 呼び出し先: `UrlbarUtils.substringAfter()`, `lazy.ExtensionSearchHandler.hasActiveInputSession()`, `lazy.ExtensionSearchHandler.isKeywordRegistered()`, `queryContext.restrictInSearchMode()`
- 条件付き依存: `if (lazy.ExtensionSearchHandler.hasActiveInputSession())` → `lazy.ExtensionSearchHandler.handleInputCancelled()`
- 参照: `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0].value`, `queryContext.tokens[0].value.length`

## UrlbarProviderOmnibox.getPriority()
- 位置: L85-87
- 役割: 優先度として 0 を返す。
- 触るとき: omnibox 結果の優先度を調整したいとき。

## UrlbarProviderOmnibox.startQuery()
- 位置: async L96-168
- 役割: キーワードの説明を見出しにした先頭結果を即座に追加し、拡張機能の候補を非同期に追加する。拡張機能の応答か omnibox.timeout のどちらか早い方で待機を終える。
- 触るとき: 拡張機能の候補の待ち時間、先頭結果の内容、重複除去を変えるとき。
- 呼び出し先: `Promise.race()`, `Promise.race([timeoutPromise, resultsPromise]).catch()`, `addCallback()`, `lazy.ExtensionSearchHandler.getDescription()`, `lazy.ExtensionSearchHandler.handleSearch()`, `lazy.UrlbarPrefs.get()`, `this.logger.error()`
- 参照: `heuristicResult.payload.content`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.ICON.EXTENSION`, `lazy.UrlbarShared.RESULT_SOURCE.ADDON`, `lazy.UrlbarShared.RESULT_TYPE.OMNIBOX`, `queryContext.isPrivate`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0].value`, `suggestion.content`, `suggestion.deletable`, `suggestion.description`, `this.logger`, `this.queryInstance`

## UrlbarProviderOmnibox.onEngagement()
- 位置: L175-181
- 役割: 削除可能な omnibox 結果で「削除」が選ばれたら、拡張機能へ入力の削除を通知し、結果を取り除く。
- 触るとき: 拡張機能の候補の削除を拡張機能側へ伝える処理を変えるとき。
- 条件付き依存: `if (details.selType == "dismiss" && result.payload.isBlockable)` → `lazy.ExtensionSearchHandler.handleInputDeleted()`
- 条件付き依存: `if (details.selType == "dismiss" && result.payload.isBlockable)` → `controller.removeResult()`
- 参照: `details.selType`, `result.payload.isBlockable`, `result.payload.title`
