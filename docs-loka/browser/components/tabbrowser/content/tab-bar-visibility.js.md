# browser/components/tabbrowser/content/tab-bar-visibility.js

source: browser/components/tabbrowser/content/tab-bar-visibility.js
source-hash: 45f3efabc9fe2d38e3a53324dd82aa54d683bda3
lines: 70

## <module>
- 役割: タブバー表示の判定をまとめた TabBarVisibility オブジェクトを定義する。

## update()
- 位置: L8-68
- 役割: ポップアップ等の単一タブ窓や縦タブかを見て、タブツールバーの表示/非表示とタイトルバー風スタイルを更新する。
- 触るとき: タブバーが出る/隠れる条件、単一タブ窓での見た目、カスタムタイトルバー連動を変えるとき。
- 呼び出し先: `CustomTitlebar.allowedBy()`, `Services.prefs.getBoolPref()`, `document .getElementById()`, `document .getElementById(id) .classList.toggle()`, `document.documentElement.hasAttribute()`, `document.getElementById()`, `gNavToolbox.toggleAttribute()`
- 参照: `CustomTitlebar.enabled`, `document.getElementById("menu_closeWindow").hidden`, `gBrowser.visibleTabs.length`, `tabsToolbar.collapsed`, `this._initialUpdateDone`, `window.toolbar.visible`
- XPCOM: `Services.prefs`
