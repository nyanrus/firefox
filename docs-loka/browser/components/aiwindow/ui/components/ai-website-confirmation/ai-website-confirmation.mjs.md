# browser/components/aiwindow/ui/components/ai-website-confirmation/ai-website-confirmation.mjs

source: browser/components/aiwindow/ui/components/ai-website-confirmation/ai-website-confirmation.mjs
source-hash: 08ed446894a0b17677748116e589885e7ee3daa3
lines: 229

## <module>
- 役割: 複数のサイトを一覧して選び、閉じる・まとめて実行する確認パネル ai-website-confirmation を定義する。
- 呼び出し先: `customElements.define()`

## AIWebsiteConfirmation.constructor()
- 位置: L40-50
- 役割: tabs を空配列、確認ボタンの文言を「タブを閉じる」系の既定値、actionType と tabGroupLabel を空にする。
- 触るとき: タブを閉じる以外の操作で文言を切り替える前提を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.actionType`, `this.confirmActionL10n`, `this.tabGroupLabel`, `this.tabs`

## AIWebsiteConfirmation.handleSelectChange()
- 位置: L57-67
- 役割: 子の選択変更イベントを止め、token が一致する行の checked を更新してから選択変更を通知する。
- 触るとき: 行の選択が反映されない、または行の同定に token を使う理由を調べるとき。
- 呼び出し先: `event.stopPropagation()`, `this.dispatchSelectionEvent()`, `this.tabs.map()`
- 参照: `event.detail`, `tab.token`, `this.tabs`

## AIWebsiteConfirmation.handleToggleAll()
- 位置: L72-78
- 役割: 全件選択済みなら全解除、そうでなければ全選択を呼ぶ。
- 触るとき: すべて選択ボタンの切り替え条件を変えるとき。
- 呼び出し先: `this.tabs.every()`
- 条件付き依存: `if (this.tabs.every(tab => tab.checked))` → `this.deselectAll()`
- 条件付き依存: `if (!(this.tabs.every(tab => tab.checked)))` → `this.selectAll()`
- 参照: `tab.checked`

## AIWebsiteConfirmation.selectAll()
- 位置: L83-86
- 役割: 全行の checked を true にして選択変更を通知する。
- 触るとき: 全選択の挙動や通知の内容を変えるとき。
- 呼び出し先: `this.dispatchSelectionEvent()`, `this.tabs.map()`
- 参照: `this.tabs`

## AIWebsiteConfirmation.deselectAll()
- 位置: L91-94
- 役割: 全行の checked を false にして選択変更を通知する。
- 触るとき: 全解除の挙動や通知の内容を変えるとき。
- 呼び出し先: `this.dispatchSelectionEvent()`, `this.tabs.map()`
- 参照: `this.tabs`

## AIWebsiteConfirmation.getSelectedTabs()
- 位置: L101-103
- 役割: checked が true の行だけを配列で返す。
- 触るとき: 確認時に実行対象として渡すタブを変えるとき。
- 呼び出し先: `this.tabs.filter()`
- 参照: `tab.checked`

## AIWebsiteConfirmation.handleClose()
- 位置: L108-117
- 役割: actionType を載せた close イベントを bubbles と composed 付きで発火する。
- 触るとき: 閉じるボタンの後に親が何をするかを追うとき。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.actionType`

## AIWebsiteConfirmation.handleConfirm()
- 位置: L122-136
- 役割: 選択が 0 件なら何もせず、あれば選択行と tabGroupLabel を載せた submit イベントを発火する。
- 触るとき: 確定時に親へ渡す値を変えるとき、または確定できない原因を調べるとき。
- 呼び出し先: `this.dispatchEvent()`, `this.getSelectedTabs()`
- 参照: `selectedTabs.length`, `this.tabGroupLabel`

## AIWebsiteConfirmation.dispatchSelectionEvent()
- 位置: L141-151
- 役割: 選択中の行と全行を載せた selection-change イベントを発火する。
- 触るとき: 選択変更を親が受けて表示を更新する経路を変えるとき。
- 呼び出し先: `this.dispatchEvent()`, `this.getSelectedTabs()`
- 参照: `this.tabs`

## AIWebsiteConfirmation.render()
- 位置: L153-225
- 役割: 全選択か全解除かの文言、選択件数による確認ボタンの有効化と文言を決め、行の一覧を描画する。
- 触るとき: 一覧の表示や、確認ボタンの無効条件・件数表示を変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `ifDefined()`, `this.tabs.every()`, `this.tabs.filter()`, `this.tabs.map()`
- 参照: `tab.checked`, `tab.iconSrc`, `tab.linkedPanel`, `tab.title`, `tab.token`, `tab.url`, `this.confirmActionL10n.disabled`, `this.confirmActionL10n.enabled`, `this.handleClose`, `this.handleConfirm`, `this.handleSelectChange`, `this.handleToggleAll`, `this.tabs.filter(tab => tab.checked).length`, `this.tabs.length`
