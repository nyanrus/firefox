# browser/base/content/browser-customtitlebar.js

source: browser/base/content/browser-customtitlebar.js
source-hash: 5e76f26fb6714d63118c145c18d80810fae06c53
lines: 80

## <module>
- 役割: OS 標準のタイトルバーを隠して独自のタイトルバーを使うか(customtitlebar)を、pref と条件から判定する。

## init()
- 位置: L6-12
- 役割: pref を読み、pref 変更の監視を始めて、判定結果を反映する。
- 触るとき: 起動時のカスタムタイトルバー判定の順序を変えるとき。
- 呼び出し先: `Services.prefs.addObserver()`, `this._readPref()`, `this._update()`
- 参照: `this._initialized`, `this._prefName`
- XPCOM: `Services.prefs`

## allowedBy()
- 位置: L14-24
- 役割: 指定の条件がカスタムタイトルバーを禁止しているかを増減し、変化があれば判定を更新する。
- 触るとき: カスタムタイトルバーを禁止する新しい条件を追加するとき。
- 条件付き依存: `if (condition in this._disallowed)` → `this._update()`
- 条件付き依存: `if (!(condition in this._disallowed))` → `this._update()`
- 参照: `this._disallowed`

## systemSupported()
- 位置: L26-39
- 役割: プラットフォームと GTK の CSD 対応から、OS がカスタムタイトルバーに対応しているかを返す。
- 触るとき: OS ごとの対応状況の判定を変えるとき。
- 呼び出し先: `window.matchMedia()`
- 参照: `AppConstants.MOZ_WIDGET_TOOLKIT`, `this.systemSupported`, `window.matchMedia("(-moz-gtk-csd-available)").matches`

## enabled()
- 位置: L41-43
- 役割: 文書要素に customtitlebar 属性があるかで、カスタムタイトルバーが有効かを返す。
- 触るとき: 有効判定を他から参照する箇所を調べるとき。
- 呼び出し先: `document.documentElement.hasAttribute()`

## observe()
- 位置: L45-49
- 役割: browser.tabs.inTitlebar の変更を受けて pref を読み直す。
- 触るとき: タイトルバー pref の変更への反応を変えるとき。
- 条件付き依存: `if (topic == "nsPref:changed")` → `this._readPref()`

## _readPref()
- 位置: L55-58
- 役割: 描画をタイトルバーに行う設定かを読み、pref の禁止条件として登録する。
- 触るとき: タイトルバー pref の解釈を変えるとき。
- 呼び出し先: `this.allowedBy()`
- 参照: `Services.appinfo.drawInTitlebar`
- XPCOM: `Services.appinfo`

## _update()
- 位置: L60-74
- 役割: 対応・全画面でない・禁止条件なし、の全てを満たすとき customtitlebar 属性を付け、アイコン色とタブバーを更新する。
- 触るとき: カスタムタイトルバーの有効条件や属性の反映を変えるとき。
- 呼び出し先: `Object.keys()`, `TabBarVisibility.update()`, `ToolbarIconColor.inferFromText()`, `document.documentElement.toggleAttribute()`
- 参照: `Object.keys(this._disallowed).length`, `this._disallowed`, `this._initialized`, `this.systemSupported`, `window.fullScreen`

## uninit()
- 位置: L76-78
- 役割: browser.tabs.inTitlebar の監視を外す。
- 触るとき: ウィンドウ終了時の後始末を変えるとき。
- 呼び出し先: `Services.prefs.removeObserver()`
- 参照: `this._prefName`
- XPCOM: `Services.prefs`
