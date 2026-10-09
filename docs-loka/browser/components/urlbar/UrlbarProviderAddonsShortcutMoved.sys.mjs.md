# browser/components/urlbar/UrlbarProviderAddonsShortcutMoved.sys.mjs

source: browser/components/urlbar/UrlbarProviderAddonsShortcutMoved.sys.mjs
source-hash: efceb85085ccf32552432bd8d3f4da6ca513e194
lines: 177

## <module>
- 役割: 旧アドオン管理画面のショートカットが検索タブに移ったことを、以前そのショートカットを使った人に知らせる案内プロバイダーを定義するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderAddonsShortcutMoved.type()
- 位置: L60-62
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: この案内が他の候補とどの種別として並ぶかを確かめるとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderAddonsShortcutMoved.isActive()
- 位置: async L64-71
- 役割: 検索文字列が空で、タブ検索モードの shortcut から入ったことがあり、LAST_USED_PREF が設定済みのときだけ有効にする。
- 触るとき: 案内が出る条件(旧ショートカットを使った履歴があるか)を確かめるとき。
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `queryContext.searchMode.entry`, `queryContext.searchMode?.source`, `queryContext.searchString`
- XPCOM: `Services.prefs`

## UrlbarProviderAddonsShortcutMoved.getViewTemplate()
- 位置: L73-75
- 役割: タイトルと説明を持つ固定の表示テンプレートを返す。
- 触るとき: 案内の見た目の構造(タイトルと説明の要素)を変えるとき。

## UrlbarProviderAddonsShortcutMoved.getViewUpdate()
- 位置: L82-106
- 役割: 検索タブとアドオンのショートカット表記を取得し、タイトルと説明の l10n 引数に渡す。
- 触るとき: ショートカットの表記が案内文に正しく出ない、または文言の引数を変えたいとき。
- 呼び出し先: `document.getElementById()`, `lazy.ShortcutUtils.prettifyShortcut()`
- 参照: `controller.browserWindow.document`

## UrlbarProviderAddonsShortcutMoved.onEngagement()
- 位置: L113-125
- 役割: ショートカット変更なら about:keyboard を開き、dismiss なら何もせず、どちらでも停止して結果を閉じる。
- 触るとき: 案内のボタンを押した後に何が起きるか、閉じ方を変えたいとき。
- 呼び出し先: `controller.browserWindow.switchToTabHavingURI()`, `controller.view.close()`, `this.#stop()`
- 参照: `details.selType`

## UrlbarProviderAddonsShortcutMoved.onImpression()
- 位置: L127-139
- 役割: 表示回数を数え、上限に達したら案内を停止する。上限未満の間は表示回数の pref を更新する。
- 触るとき: 案内が出続ける、または早く消えすぎるとき、表示回数の上限の数え方を確かめるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (shownCount < SHOWN_LIMIT)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!(shownCount < SHOWN_LIMIT))` → `this.#stop()`
- XPCOM: `Services.prefs`

## UrlbarProviderAddonsShortcutMoved.#stop()
- 位置: L141-144
- 役割: LAST_USED_PREF と表示回数の pref のユーザー設定を消して案内を終わらせる。
- 触るとき: 案内を止めた後も pref が残っていないかを調べるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## UrlbarProviderAddonsShortcutMoved.startQuery()
- 位置: async L153-175
- 役割: 先頭に出す DYNAMIC の結果を1件作り、「変更」と「閉じる」の2つのボタンを付けて追加する。
- 触るとき: 案内の位置やボタンの構成を変えたいとき。
- 呼び出し先: `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`
