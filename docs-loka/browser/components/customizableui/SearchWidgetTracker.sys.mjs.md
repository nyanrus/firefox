# browser/components/customizableui/SearchWidgetTracker.sys.mjs

source: browser/components/customizableui/SearchWidgetTracker.sys.mjs
source-hash: f44f96361d9a8fb5f5533251ba76764bbf4477cb
lines: 127

## <module>
- 役割: 検索バーウィジェットの使われ方を追跡し、長期間未使用なら自動でパレットへ戻す。

## init()
- 位置: L19-22
- 役割: CustomizableUI にリスナーを登録し、起動時に未使用判定を一度実行する。
- 触るとき: 起動時の検索バー整理の順序や、リスナー登録の条件を変えるとき。
- 呼び出し先: `CustomizableUI.addListener()`, `this._removeWidgetIfUnused()`

## onWidgetAfterDOMChange()
- 位置: L38-42
- 役割: 検索バーが DOM から取り除かれたとき、保存されている幅の指定を消す。
- 触るとき: ツールバーから検索バーを外したあとに幅が残る不具合を調べるとき。
- 条件付き依存: `if (node.id == WIDGET_ID && wasRemoval)` → `this._removePersistedWidths()`
- 参照: `node.id`

## onCustomizeStart()
- 位置: L44-46
- 役割: カスタマイズ開始時に、検索バーがナビバーにあったかを覚えておく。
- 触るとき: カスタマイズ終了時に『使った』扱いにする判定を変えるとき。
- 参照: `this._widgetIsInNavBar`, `this._widgetWasInNavBar`

## onCustomizeEnd()
- 位置: L48-58
- 役割: カスタマイズ中に検索バーをナビバーへ置いたときだけ、最終使用日時の pref を現在時刻にする。
- 触るとき: 手動配置を使用扱いにする条件や、browser.search.widget.lastUsed の更新を調べるとき。
- 条件付き依存: `if (!this._widgetWasInNavBar && this._widgetIsInNavBar)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!this._widgetWasInNavBar && this._widgetIsInNavBar)` → `new Date().toISOString()`
- 参照: `this._widgetIsInNavBar`, `this._widgetWasInNavBar`
- XPCOM: `Services.prefs`

## _removeWidgetIfUnused()
- 位置: L67-94
- 役割: ナビバーにある検索バーの最終使用から removeAfterDaysUnused 日を超えていれば、パレットへ移し Glean で記録する。
- 触るとき: 未使用の検索バーが勝手に消える条件やしきい値を変えるとき、または自動削除の計測を調べるとき。
- 呼び出し先: `Services.prefs.getStringPref()`
- 条件付き依存: `if (searchBarLastUsed)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (new Date() - new Date(searchBarLastUsed) > saerchBarUnusedThreshold)` → `CustomizableUI.removeWidgetFromArea()`
- 条件付き依存: `if (new Date() - new Date(searchBarLastUsed) > saerchBarUnusedThreshold)` → `Glean.browserUi.customizedWidgets[ "search-container_remove_na_na_auto-unused" ].add()`
- 参照: `Glean.browserUi.customizedWidgets`, `this._widgetIsInNavBar`
- XPCOM: `Services.prefs`

## _removePersistedWidths()
- 位置: L102-115
- 役割: xulstore の検索バー幅を消し、開いている各ウィンドウの検索バーから width 指定を外す。
- 触るとき: 検索バーの幅をリセットする処理や、幅の指定が残って表示が崩れる問題を調べるとき。
- 呼び出し先: `Services.xulStore.removeValue()`, `searchbar.removeAttribute()`, `searchbar.style.removeProperty()`, `win.document.getElementById()`, `win.gNavToolbox.palette.querySelector()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `CustomizableUI.windows`
- XPCOM: `Services.xulStore`

## _widgetIsInNavBar()
- 位置: L122-125
- 役割: 検索バーの現在の配置がナビゲーションバー領域かどうかを返す。
- 触るとき: 検索バーの配置判定を使う処理の前提を確かめるとき、またはナビバー外への移動を扱うとき。
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `placement?.area`
