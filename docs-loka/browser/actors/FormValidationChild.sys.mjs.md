# browser/actors/FormValidationChild.sys.mjs

source: browser/actors/FormValidationChild.sys.mjs
source-hash: 428962d87b73a10440da8f86158bc975f9a50575
lines: 198

## <module>
- 役割: フォームの入力検証エラーを、親プロセスのポップアップで要素の近くに示す子側アクター。

## FormValidationChild.constructor()
- 位置: L11-15
- 役割: 検証メッセージと対象要素の保持領域を空で初期化する。
- 触るとき: ポップアップの状態の初期値を変えるとき。
- 呼び出し先: `super()`
- 参照: `this._element`, `this._validationMessage`

## FormValidationChild.handleEvent()
- 位置: L21-44
- 役割: 無効フォームの送信、ページ表示・非表示、input、blur をそれぞれの処理へ振り分ける。
- 触るとき: ポップアップを開閉するきっかけを追加・変更するとき。
- 呼び出し先: `aEvent.preventDefault()`, `this._isRootDocumentEvent()`, `this._onBlur()`, `this._onInput()`, `this.notifyInvalidSubmit()`
- 条件付き依存: `if (this._isRootDocumentEvent(aEvent))` → `this._hidePopup()`
- 参照: `aEvent.detail`, `aEvent.type`

## FormValidationChild.notifyInvalidSubmit()
- 位置: L46-107
- 役割: 無効な要素のうち最初にフォーカス可能なものへフォーカスし、メッセージを出して input と blur を監視する。カスタム要素は validationAnchor を使う。
- 触るとき: 送信時にどの要素へ案内するかを変えるとき。
- 呼び出し先: `ChromeUtils.getClassName()`, `Services.focus.elementIsFocusable()`, `element.addEventListener()`, `element.focus()`, `this._showPopup()`
- 条件付き依存: `if (this._element == element)` → `this._showPopup()`
- 参照: `element.documentGlobal`, `element.internals.validationAnchor`, `element.internals.validationMessage`, `element.isFormAssociatedCustomElement`, `element.validationMessage`, `this._element`, `this._validationMessage`, `this.contentWindow`
- XPCOM: `Services.focus`

## FormValidationChild._onInput()
- 位置: L118-133
- 役割: 値が有効になればポップアップを隠し、まだ無効でメッセージが変わっていれば表示を更新する。
- 触るとき: 入力中の検証メッセージの更新を変えるとき。
- 条件付き依存: `if (element.validity.valid)` → `this._hidePopup()`
- 条件付き依存: `if (this._validationMessage != element.validationMessage)` → `this._showPopup()`
- 参照: `aEvent.originalTarget`, `element.validationMessage`, `element.validity.valid`, `this._validationMessage`

## FormValidationChild._onBlur()
- 位置: L139-146
- 役割: input と blur の監視を外し、ポップアップを隠して対象要素を忘れる。
- 触るとき: フォーカスが外れた時の後始末を変えるとき。
- 呼び出し先: `this._hidePopup()`
- 条件付き依存: `if (this._element)` → `this._element.removeEventListener()`
- 参照: `this._element`

## FormValidationChild._showPopup()
- 位置: L153-178
- 役割: 要素の画面上の位置とメッセージを親へ送り、ページ非表示の監視を付ける。ラジオやチェックボックスは中央寄せにする。
- 触るとき: ポップアップの位置や送る内容を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`, `win.addEventListener()`, `win.windowUtils.getElementBoundingScreenRect()`
- 参照: `aElement.documentGlobal`, `aElement.tagName`, `aElement.type`, `panelData.message`, `panelData.position`, `panelData.screenRect`, `this._validationMessage`

## FormValidationChild._hidePopup()
- 位置: L180-185
- 役割: 親へ隠す指示を送り、pagehide の監視を外す。
- 触るとき: ポップアップを閉じる処理を変えるとき。 注意: 対象要素が null のとき例外になりうる (要確認)。
- 呼び出し先: `this._element.documentGlobal.removeEventListener()`, `this.sendAsyncMessage()`

## FormValidationChild._isRootDocumentEvent()
- 位置: L187-196
- 役割: イベントの発生元が、このアクターの文書かその直下の文書かを判定する。
- 触るとき: pageshow でポップアップを隠す条件を変えるとき。
- 参照: `aEvent.originalTarget`, `target.ownerDocument`, `this.contentWindow`, `this.document`
