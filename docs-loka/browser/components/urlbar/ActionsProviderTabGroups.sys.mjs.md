# browser/components/urlbar/ActionsProviderTabGroups.sys.mjs

source: browser/components/urlbar/ActionsProviderTabGroups.sys.mjs
source-hash: 38c872f4aa81093ef46af423965e3204f7b51dbc
lines: 160

## <module>
- 役割: urlbar に、開いているタブグループと保存済みタブグループへの切り替え候補を出すアクションプロバイダ。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ProviderTabGroups.name()
- 位置: L27-29
- 役割: プロバイダ名 "ActionsProviderTabGroups" を返す。
- 触るとき: 結果の providerName でこのプロバイダを識別する箇所を追うとき。

## ProviderTabGroups.isActive()
- 位置: L31-42
- 役割: urlbar か smartbar で、タブグループが有効、タブ検索のみでない、入力が 50 字未満かつ最小文字数以上のときに有効にする。
- 触るとき: タブグループ候補が出ない条件（最小文字数や有効化の pref）を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.UrlbarPrefs.get()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `queryContext.restrictSource`, `queryContext.sapName`, `queryContext.trimmedSearchString.length`
- XPCOM: `Services.prefs`

## ProviderTabGroups.queryActions()
- 位置: async L44-105
- 役割: 開いているグループ（現在のグループは除く）と、プライベートでなければ保存済みグループから、入力に合うものを結果にする。
- 触るとき: タブグループ候補の並びや対象範囲を変えるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.SessionStore.getSavedTabGroups()`, `results.push()`, `this.#makeResult()`, `this.#matches()`, `window.gBrowser.getAllTabGroups()`
- 条件付き依存: `if (!Cu.isInAutomation)` → `console.error()`
- 参照: `Cu.isInAutomation`, `group.color`, `group.documentGlobal`, `group.id`, `group.label`, `queryContext.isPrivate`, `savedGroup.color`, `savedGroup.id`, `savedGroup.name`, `window.gBrowser.selectedTab.group`

## ProviderTabGroups.onPick()
- 位置: L107-127
- 役割: 保存済みグループなら現在のウィンドウへ開き、そうでなければ既存グループを選んでそのコンテンツにフォーカスを移す。
- 触るとき: 候補を選んだときに保存済みグループが開かれない、またはフォーカスが移らないとき。
- 条件付き依存: `if (action.dataset.savedGroupId)` → `lazy.SessionStore.openSavedTabGroup()`
- 条件付き依存: `if (!(action.dataset.savedGroupId))` → `controller.browserWindow.gBrowser.getTabGroupById()`
- 条件付き依存: `if (group)` → `group.select()`
- 条件付き依存: `if (group)` → `group.documentGlobal.focus()`
- 参照: `action.dataset.groupId`, `action.dataset.savedGroupId`, `controller.browserWindow`, `lazy.TabMetrics.METRIC_SOURCE.SUGGEST`

## ProviderTabGroups.#matches()
- 位置: L129-137
- 役割: グループ名を小文字で比べる。1 文字なら前方一致、それ以外は入力の全トークンを含むかで判定する。
- 触るとき: グループ名の一致条件（前方一致か部分一致か）を変えるとき。
- 呼び出し先: `groupName.includes()`, `groupName.toLowerCase()`, `queryContext.tokens.every()`
- 条件付き依存: `if (queryContext.trimmedLowerCaseSearchString.length == 1)` → `groupName.startsWith()`
- 参照: `queryContext.trimmedLowerCaseSearchString`, `queryContext.trimmedLowerCaseSearchString.length`, `token.lowerCaseValue`

## ProviderTabGroups.#makeResult()
- 位置: L139-156
- 役割: タブグループのアイコンと、グループ色から作る CSS 変数を持つ ActionsResult を組み立てる。
- 触るとき: 候補の見た目や色の割り当てを変えるとき。
- 参照: `this.name`
