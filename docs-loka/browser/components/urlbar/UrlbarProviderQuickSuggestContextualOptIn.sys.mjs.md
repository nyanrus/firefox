# browser/components/urlbar/UrlbarProviderQuickSuggestContextualOptIn.sys.mjs

source: browser/components/urlbar/UrlbarProviderQuickSuggestContextualOptIn.sys.mjs
source-hash: dc45cb3564aa78d686738e1a8c5c67ce9dea1b84
lines: 362

## <module>
- 役割: Firefox Suggest のオプトイン案内を、検索欄が空のときに URL バーの動的結果として出すヒューリスティックのプロバイダー。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderQuickSuggestContextualOptIn.constructor()
- 位置: L69-71
- 役割: プロバイダーを生成する(super のみ)。
- 触るとき: コンストラクタに初期状態を足すときのみ。
- 呼び出し先: `super()`

## UrlbarProviderQuickSuggestContextualOptIn.type()
- 位置: L76-78
- 役割: プロバイダー種別として HEURISTIC を返す。
- 触るとき: オプトイン結果の種別と並び順を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderQuickSuggestContextualOptIn.#shouldDisplayContextualOptIn()
- 位置: L80-139
- 役割: 検索欄が空で非プライベートのとき、Suggest が有効かつオンライン未許可で、過去の非表示回数に応じた再表示間隔を過ぎていれば true を返す。
- 触るとき: オプトイン案内を出すかどうかの判定条件や、非表示後の再表示間隔を変えるとき。
- 呼び出し先: `Date.now()`, `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.isPrivate`, `queryContext.restrictSource`, `queryContext.searchString`

## UrlbarProviderQuickSuggestContextualOptIn.isActive()
- 位置: async L141-176
- 役割: 表示条件を満たしたうえで、表示回数の上限と期間を超えていれば #dismiss で非表示扱いにしてから false を返す。
- 触るとき: 案内が何回、何日表示されたら自動で非表示にするかを変えるとき。
- 呼び出し先: `Date.now()`, `lazy.UrlbarPrefs.get()`, `this.#dismiss()`, `this.#shouldDisplayContextualOptIn()`

## UrlbarProviderQuickSuggestContextualOptIn.getPriority()
- 位置: L178-180
- 役割: 優先度として TopSites の優先度を返す。
- 触るとき: オプトイン案内を他の空入力の候補と比べた位置を変えたいとき。
- 参照: `lazy.UrlbarProviderTopSites.PRIORITY`

## UrlbarProviderQuickSuggestContextualOptIn.getViewTemplate()
- 位置: L182-184
- 役割: アイコン、タイトル、説明、「詳細」リンクを持つ固定の表示テンプレートを返す。
- 触るとき: 案内の DOM 構造やリンクの data-command を変えるとき。

## UrlbarProviderQuickSuggestContextualOptIn.getViewUpdate()
- 位置: L190-208
- 役割: アイコン画像とタイトル・説明の l10n ID を返し、表示文言を決める。
- 触るとき: 案内の文言(l10n ID)を差し替えるとき。

## UrlbarProviderQuickSuggestContextualOptIn.onBeforeSelection()
- 位置: L214-218
- 役割: 「詳細」リンクが選ばれたとき、案内のタイトルと説明をスクリーンリーダー向けに通知する。
- 触るとき: 支援技術への通知文言や、選択前の挙動を変えるとき。
- 呼び出し先: `element.getAttribute()`
- 条件付き依存: `if (element.getAttribute("name") == "learn_more")` → `this.#a11yAlertRow()`
- 条件付き依存: `if (element.getAttribute("name") == "learn_more")` → `element.closest()`

## UrlbarProviderQuickSuggestContextualOptIn.#a11yAlertRow()
- 位置: L220-233
- 役割: 行内のタイトルと、「詳細」リンクを除いた説明文を連結し、行の ariaNotify で読み上げる。
- 触るとき: 案内を読み上げる文言の組み立てを変えるとき。
- 呼び出し先: `decription.firstElementChild?.remove()`, `row .querySelector()`, `row .querySelector( ".urlbarView-dynamic-quickSuggestContextualOptIn-description" ) .cloneNode()`, `row.ariaNotify()`, `row.querySelector()`
- 参照: `decription.textContent`, `row.querySelector( ".urlbarView-dynamic-quickSuggestContextualOptIn-title" ).textContent`

## UrlbarProviderQuickSuggestContextualOptIn.onImpression()
- 位置: L242-264
- 役割: 表示のたびに表示回数を 1 増やし、初回なら初回表示時刻を記録する。エンゲージメント時でこのプロバイダーの結果なら何もしない。
- 触るとき: 表示回数の数え方や、初回表示時刻の記録を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`
- 条件付き依存: `if (!firstImpressionTime)` → `lazy.UrlbarPrefs.set()`
- 条件付き依存: `if (!firstImpressionTime)` → `Date.now()`
- 参照: `details.provider`, `this.name`

## UrlbarProviderQuickSuggestContextualOptIn.onEngagement()
- 位置: L271-275
- 役割: 選ばれた操作の種類(selType)を _handleCommand に渡す。
- 触るとき: ボタンやリンクの操作が処理される入口を確認するとき。
- 呼び出し先: `this._handleCommand()`
- 参照: `details.result`, `details.selType`

## UrlbarProviderQuickSuggestContextualOptIn._handleCommand()
- 位置: L277-308
- 役割: learn_more は Suggest のヘルプを開き、allow はオンライン提案を有効化し、dismiss は #dismiss を呼ぶ。その後ビューを閉じ、もう表示条件を満たさなければ結果を削除する。
- 触るとき: オプトインの「許可」「閉じる」「詳細」の動作や、操作後に結果を消す条件を変えるとき。
- 呼び出し先: `controller.browserWindow.openHelpLink()`, `controller.view.close()`, `lazy.UrlbarPrefs.set()`, `this.#dismiss()`, `this.#shouldDisplayContextualOptIn()`
- 条件付き依存: `if (result)` → `controller.removeResult()`
- 参照: `container.hidden`

## UrlbarProviderQuickSuggestContextualOptIn.#dismiss()
- 位置: L310-325
- 役割: 初回表示時刻と表示回数をリセットし、非表示にした時刻と非表示回数を記録する。
- 触るとき: 閉じたときに何が記録され、次の再表示がいつになるかを変えるとき。
- 呼び出し先: `Date.now()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`

## UrlbarProviderQuickSuggestContextualOptIn.startQuery()
- 位置: async L334-360
- 役割: 「許可」と「閉じる」の 2 つのボタンを持つ動的結果を先頭(suggestedIndex 0)に追加する。
- 触るとき: 案内のボタンの構成や並び、先頭に出す位置を変えるとき。
- 呼び出し先: `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`
