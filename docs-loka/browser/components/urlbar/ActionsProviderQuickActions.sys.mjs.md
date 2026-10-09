# browser/components/urlbar/ActionsProviderQuickActions.sys.mjs

source: browser/components/urlbar/ActionsProviderQuickActions.sys.mjs
source-hash: ea83d2727b89037ac3ca4b9f055aa7655d761895
lines: 224

## <module>
- 役割: urlbar で「クイックアクション」（タブの音消し、再起動など）を入力の接頭辞と語句から選んで候補にするアクションプロバイダ。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ProviderQuickActions.name()
- 位置: L51-53
- 役割: プロバイダ名 "ActionsProviderQuickActions" を返す。
- 触るとき: クイックアクション由来の結果を識別する箇所を追うとき。

## ProviderQuickActions.isActive()
- 位置: L55-64
- 役割: urlbar で、suggest.quickactions が有効、検索モード外、入力が 50 字未満かつ最小文字数以上のときに有効にする。
- 触るとき: クイックアクションが出ない条件を調べるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.sapName`, `queryContext.trimmedSearchString.length`

## ProviderQuickActions.queryActions()
- 位置: async L66-103
- 役割: 接頭辞一致の結果に、設定が有効なら語句に含まれるキーワードの結果を足し、対応不可・無効のものを除いて ActionsResult にする。
- 触るとき: 入力に対して出るクイックアクションの絞り込みを変えるとき。
- 呼び出し先: `[...results].map()`, `action.isInactive()`, `action.isUnsupported()`, `lazy.UrlbarPrefs.get()`, `results.forEach()`, `this.#actions.get()`, `this.getActions()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get(MATCH_IN_PHRASE_PREF))` → `input.includes()`
- 条件付き依存: `if (input.includes(keyword) && keys.length)` → `keys.forEach()`
- 条件付き依存: `if (input.includes(keyword) && keys.length)` → `results.add()`
- 条件付き依存: `if (action.isUnsupported?.() || action.isInactive?.())` → `results.delete()`
- 参照: `action.icon`, `action.label`, `keys.length`, `queryContext.trimmedLowerCaseSearchString`, `queryContext.trimmedSearchString.length`, `results.size`, `this.#keywords`, `this.name`

## ProviderQuickActions.getActions()
- 位置: async L105-116
- 役割: ロード済みにしてから、入力の接頭辞一致の集合を返す。exact 一致指定ならキーワード一致も加える。
- 触るとき: 接頭辞一致の候補の数や取得方法を変えるとき。
- 呼び出し先: `lazy.QuickActionsLoaderDefault.ensureLoaded()`, `this.#prefixes.get()`
- 条件付き依存: `if (includesExactMatch)` → `this.#keywords.get()`
- 条件付き依存: `if (includesExactMatch)` → `actions?.forEach()`
- 条件付き依存: `if (includesExactMatch)` → `results.add()`

## ProviderQuickActions.getAction()
- 位置: L118-120
- 役割: キーで登録済みのクイックアクション定義を返す。
- 触るとき: 登録済みアクションの定義を参照する箇所を追うとき。
- 呼び出し先: `this.#actions.get()`

## ProviderQuickActions.onPick()
- 位置: L122-129
- 役割: 結果の key と入力長を取り出して pickAction を呼ぶ。
- 触るとき: 候補を選んだときの入口を確かめるとき。
- 呼び出し先: `this.pickAction()`
- 参照: `actionResult.dataset.inputLength`, `actionResult.key`

## ProviderQuickActions.pickAction()
- 位置: L131-138
- 役割: 入力長を 10 以下に丸め、キー-入力長で Glean の picked を記録し、アクションの onPick を実行する。focusContent が返ればコンテンツにフォーカスを移す。
- 触るとき: 選択時のテレメトリの集計単位や、選択後のフォーカス移動を変えるとき。
- 呼び出し先: `Glean.urlbarQuickaction.picked[`${key}-${inputLength}`].add()`, `Math.min()`, `this.#actions.get()`, `this.#actions.get(key).onPick()`
- 条件付き依存: `if (options?.focusContent)` → `controller.browserWindow.gBrowser.selectedBrowser.focus()`
- 参照: `Glean.urlbarQuickaction.picked`, `options?.focusContent`

## ProviderQuickActions.addAction()
- 位置: L146-162
- 役割: アクションを登録し、各コマンド語をキーワードに加え、語の接頭辞（完全一致を除く）も引けるように登録する。
- 触るとき: 新しいクイックアクションを足すときの登録の仕組みを確かめるとき。
- 呼び出し先: `definition.commands.forEach()`, `keys.push()`, `this.#actions.set()`, `this.#keywords.get()`, `this.#keywords.set()`, `this.#loopOverPrefixes()`, `this.#prefixes.get()`, `this.#prefixes.set()`
- 条件付き依存: `if (result)` → `result.add()`
- 参照: `definition.commands`

## ProviderQuickActions.removeAction()
- 位置: L169-186
- 役割: アクションを削除し、キーワードと接頭辞の対応からも取り除く。
- 触るとき: アクションを無効化・削除したのに候補に残る問題を調べるとき。
- 呼び出し先: `definition.commands.forEach()`, `keys.filter()`, `this.#actions.delete()`, `this.#actions.get()`, `this.#keywords.get()`, `this.#keywords.set()`, `this.#loopOverPrefixes()`, `this.#prefixes.get()`, `this.#prefixes.set()`
- 条件付き依存: `if (result)` → `result.delete()`
- 参照: `definition.commands`

## ProviderQuickActions.#loopOverPrefixes()
- 位置: L209-220
- 役割: 各コマンド語について、空文字から完全一致の 1 字手前までの接頭辞を順に渡す。
- 触るとき: 接頭辞の登録範囲（何字から候補に出すか）を変えるとき。
- 呼び出し先: `command.substring()`, `fun()`
- 参照: `command.length`
