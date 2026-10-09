# browser/components/aiwindow/ui/modules/SmartFormFillAutocomplete.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillAutocomplete.sys.mjs
source-hash: 151454d4331af5e61882ee9a9d1ade4922816ca9
lines: 274

## <module>
- 役割: Smart Form Fill の候補を Firefox の autocomplete ポップアップ向けに作り、表示元タブの情報を後から行へ反映する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## SmartFormFillAutocompleteItem.constructor()
- 位置: L82-126
- 役割: 候補行の表示データを JSON にして comment に入れ、タブ数が 2 以上なら編集用の secondary action を付ける。
- 触るとき: 候補行のラベルや aria ラベル、タブ編集ボタンの出る条件を変えるとき。
- 呼び出し先: `JSON.stringify()`
- 参照: `comment.secondaryAction`, `this.comment`, `this.image`, `this.label`

## autocompleteItemsAsync()
- 位置: async L149-182
- 役割: 検索文字列が空で、対応入力型かつ機能が有効かつ AI Window が有効なときだけ、SFF actor から候補を取得する。失敗時は空配列を返す。
- 触るとき: 入力欄にフォーカスしたときに候補が出ない、または出すべきでないところで出るとき、この条件を確認する。
- 呼び出し先: `SUPPORTED_INPUT_TYPES.includes()`, `browsingContext.currentWindowGlobal.getActor()`, `lazy.AIWindow.isAIWindowActive()`, `sffActor.searchAutoCompleteEntries()`
- 参照: `browsingContext?.topChromeWindow`, `lazy.SFF_ENABLED`, `result?.entries`

## createItemsAsync()
- 位置: async L198-252
- 役割: l10n 文字列と選択タブ数、読込状態から候補行を 1 件作り、読込中やソース無しの文言と aria ラベルを決める。
- 触るとき: 候補行の文言を変えるとき、または関連タブの読込完了前後で表示がおかしいとき。
- 呼び出し先: `[ label, loading ? loadingLabel : (emptySourcesLabel ?? sourcesPillsLabel), ].join()`, `lazy.l10n.formatValue()`, `lazy.l10n.formatValues()`, `sffActor.areRelevantTabsReady()`, `sffActor.getSelectedTabSources()`
- 参照: `sffActor.getSelectedTabSources(formId).length`, `sffActor.hasSourceTabs`

## updatePopupSources()
- 位置: L263-272
- 役割: ポップアップ内の SFF 行を探し、そのタブ情報を行要素の sources に設定する。
- 触るとき: 候補行のタブ一覧 (pill 表示) が更新されず古いままのとき、この反映経路を確認する。
- 呼び出し先: `browser.autoCompletePopup.querySelector()`, `item?.querySelector()`
- 参照: `row.sources`
