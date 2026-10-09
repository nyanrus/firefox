# browser/components/urlbar/UrlbarProviderAboutPages.sys.mjs

source: browser/components/urlbar/UrlbarProviderAboutPages.sys.mjs
source-hash: 9e3639412e217b272dab57687a98c4b1598d77b6
lines: 70

## <module>
- 役割: about: で始まる入力に対して、表示可能な about: ページを候補として出すプロバイダーを定義するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderAboutPages.type()
- 位置: L26-28
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: about: ページ候補が、プロファイル系の結果として他の候補とどう並ぶかを確かめるとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderAboutPages.isActive()
- 位置: async L37-39
- 役割: トリム・小文字化した入力が about: で始まるときだけ有効にする。
- 触るとき: about: と打っても候補が出ないとき、入力の前処理条件を疑って見るとき。
- 呼び出し先: `queryContext.trimmedLowerCaseSearchString.startsWith()`

## UrlbarProviderAboutPages.startQuery()
- 位置: L48-68
- 役割: visibleAboutUrls のうち入力で始まるものを、一致部分を強調した URL 結果として1件ずつ追加する。
- 触るとき: 表示される about: 候補の一覧や強調(ハイライト)の付き方を変えるとき、候補の絞り込み条件を確認するとき。
- 呼び出し先: `aboutUrl.startsWith()`
- 条件付き依存: `if (aboutUrl.startsWith(searchString))` → `lazy.UrlbarShared.getIconForUrl()`
- 条件付き依存: `if (aboutUrl.startsWith(searchString))` → `addCallback()`
- 参照: `lazy.AboutPagesUtils.visibleAboutUrls`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.trimmedLowerCaseSearchString`
