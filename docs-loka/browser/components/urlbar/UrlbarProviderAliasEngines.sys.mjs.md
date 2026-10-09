# browser/components/urlbar/UrlbarProviderAliasEngines.sys.mjs

source: browser/components/urlbar/UrlbarProviderAliasEngines.sys.mjs
source-hash: e7ebfcac125066fb15997c7993c292dfffe5c139
lines: 93

## <module>
- 役割: 検索エンジンのエイリアス(キーワード)入力を、ヒューリスティックの検索結果として返すプロバイダーを定義するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderAliasEngines.type()
- 位置: L31-33
- 役割: プロバイダー種別として HEURISTIC を返す。
- 触るとき: エイリアス結果が先頭の候補として扱われる(ヒューリスティック扱い)かどうかを確かめるとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderAliasEngines.isActive()
- 位置: async L42-50
- 役割: restrictSource が未指定か SEARCH で、検索モード外かつトークンが1つ以上あるときだけ有効にする。
- 触るとき: エイリアスを入力しても結果が出ないとき、source 制限や検索モードのせいで止まっていないかを調べるとき。
- 呼び出し先: `queryContext.restrictInSearchMode()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `queryContext.restrictSource`, `queryContext.tokens.length`

## UrlbarProviderAliasEngines.startQuery()
- 位置: async L60-91
- 役割: 先頭トークンを engineForAlias でエンジンに解決し、アイコンと残りの検索語を付けたヒューリスティックの検索結果を1件追加する。非同期の途中でクエリが入れ替わったら何もしない。
- 触るとき: エイリアスの後ろに続けた語がタイトルや検索語にどう渡るかを変えたいとき、またはエンジンのアイコンが出ない原因を探すとき。
- 呼び出し先: `UrlbarUtils.getEngineIconUrl()`, `UrlbarUtils.substringAfter()`, `UrlbarUtils.substringAfter( queryContext.searchString, alias ).trimStart()`, `addCallback()`, `lazy.UrlbarSearchUtils.engineForAlias()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0]?.value`, `this.queryInstance`
