# browser/components/aiwindow/ui/components/input-model-select/input-model-select.mjs

source: browser/components/aiwindow/ui/components/input-model-select/input-model-select.mjs
source-hash: ea4ef034174b1f96298998928abab3c6f9568d57
lines: 293

## <module>
- 役割: スマートバーのモデル選択ボタン input-model-select を定義し、モデルの並び順・アイコン・ラベルを決めるモジュール。
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## getModelDisplayOrder()
- 位置: L26-26
- 役割: モデルの表示順を返す関数を解決する。Storybook では固定の並び、通常は Utils.sys.mjs のものを使う。
- 触るとき: 表示順の取得元を変えるとき、または Storybook でモデルの並びがおかしいときに確認するとき。

## InputModelSelect.constructor()
- 位置: L76-97
- 役割: 選択中モデルなどを初期化し、mistralRelease の pref を遅延取得器で監視して変わったら再描画する。
- 触るとき: 初期値や pref の監視方法を変えるとき、または Nimbus の切り替えで表示が更新されないと疑うとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `crypto.randomUUID()`, `super()`, `this.requestUpdate()`
- 参照: `this._menuId`, `this.availableModels`, `this.defaultModelChoiceId`, `this.mistralRelease`, `this.panelOpen`, `this.selectedModelId`, `this.sidebarMode`

## InputModelSelect.#caretIcon()
- 位置: L99-103
- 役割: パネルが開いているかに応じて上向きか下向きの矢印アイコンを返す。
- 触るとき: ボタン右側の開閉矢印の見た目を変えるとき。
- 参照: `this.panelOpen`

## InputModelSelect.#onPanelShown()
- 位置: L105-107
- 役割: パネルが開いたら panelOpen を true にする。
- 触るとき: パネルの開閉に連動する状態の扱いを変えるとき。
- 参照: `this.panelOpen`

## InputModelSelect.#onPanelHidden()
- 位置: L109-111
- 役割: パネルが閉じたら panelOpen を false にする。
- 触るとき: パネルの開閉に連動する状態の扱いを変えるとき。
- 参照: `this.panelOpen`

## InputModelSelect.#modelsList()
- 位置: L113-133
- 役割: availableModels を表示順に並べたモデル一覧を返し、カスタム(choice 0)を常に先頭にする。
- 触るとき: モデル一覧の並びを変えるとき、または一覧に出てこないモデルを調べるとき。
- 呼び出し先: `Object.entries()`, `Object.entries(this.availableModels) .map()`, `Object.entries(this.availableModels) .map(([index, availableModel]) => ({ ...availableModel, index, })) .sort()`, `getModelDisplayOrder()`, `rank()`
- 参照: `a.index`, `b.index`, `this.availableModels`

## rank()
- 位置: L118-126
- 役割: choice ID の表示順位を返す。カスタムは -1、順序表に無い ID は末尾にする。
- 触るとき: 並び順の規則を変えるとき。
- 呼び出し先: `order.indexOf()`
- 参照: `order.length`

## InputModelSelect.#selectedModel()
- 位置: L135-137
- 役割: selectedModelId に一致するモデルを一覧から探して返す。
- 触るとき: 選択中モデルの表示を変えるとき、または一致するモデルが無くボタンが描かれない理由を調べるとき。
- 呼び出し先: `this.#modelsList.find()`
- 参照: `m.model`, `this.selectedModelId`

## InputModelSelect.#setModelId()
- 位置: L139-156
- 役割: 一覧にあるモデルなら選択を更新し、変わったときだけ model-change を発火する。見つからなければエラーを出して戻る。
- 触るとき: モデル選択時に親へ渡す情報を変えるとき、または選択が反映されない条件を調べるとき。
- 呼び出し先: `this.#modelsList.find()`
- 条件付き依存: `if (!selectedModel)` → `console.error()`
- 条件付き依存: `if (modelId !== this.selectedModelId)` → `this.dispatchEvent()`
- 参照: `m.model`, `selectedModel.index`, `this.selectedModelId`

## InputModelSelect.#openSmartwindowSettings()
- 位置: L158-165
- 役割: AI Window の設定を開くための open-settings イベントを発火する。
- 触るとき: 設定リンクの遷移先や通知の内容を変えるとき。
- 呼び出し先: `this.dispatchEvent()`

## InputModelSelect.#getButtonLabelL10nId()
- 位置: L167-169
- 役割: choice ID に対応するボタンのラベル用 Fluent ID を返す。
- 触るとき: モデルごとのボタン文言を変えるとき。

## InputModelSelect.#getDescriptionL10nId()
- 位置: L171-179
- 役割: カスタムは専用の説明、mistralRelease 有効時はボタンラベル、それ以外は共通の説明の ID を返す。
- 触るとき: メニュー項目の説明文の出し分けを変えるとき。
- 参照: `this.mistralRelease`

## InputModelSelect.#iconSrc()
- 位置: L181-183
- 役割: mistralRelease の値に応じて新旧どちらかのアイコン表から引いて返す。
- 触るとき: モデルのアイコンを差し替えるとき、または pref による表示の違いを確認するとき。
- 参照: `this.mistralRelease`

## InputModelSelect.render()
- 位置: L185-289
- 役割: モデルか選択が無ければ空を返す。それ以外は選択中モデルのボタンと、モデル項目・区切り線・設定リンクを持つ panel-list を描く。
- 触るとき: モデル選択の見た目、メニューの項目構成、mistral 版の表示の違いを変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.#getButtonLabelL10nId()`, `this.#getDescriptionL10nId()`, `this.#iconSrc()`, `this.#setModelId()`
- 条件付き依存: `if (!this.#modelsList.length || !this.#selectedModel)` → `html()`
- 参照: `item.index`, `item.model`, `item.ownerName`, `item.shortName`, `this.#caretIcon`, `this.#modelsList`, `this.#modelsList.length`, `this.#onPanelHidden`, `this.#onPanelShown`, `this.#openSmartwindowSettings`, `this.#selectedModel`, `this.#selectedModel.brandName`, `this.#selectedModel.index`, `this._menuId`, `this.defaultModelChoiceId`, `this.mistralRelease`, `this.selectedModelId`
