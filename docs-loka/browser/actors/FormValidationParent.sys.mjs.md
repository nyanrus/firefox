# browser/actors/FormValidationParent.sys.mjs

source: browser/actors/FormValidationParent.sys.mjs
source-hash: 2eca818bc761b4a0a83e2458768a4dfca938617b
lines: 211

## <module>
- 役割: フォーム検証ポップアップの表示と位置を管理する親側アクター。他のポップアップと競合しないよう調整する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## PopupShownObserver.constructor()
- 位置: L18-20
- 役割: 対象の文脈を弱参照で保持する。
- 触るとき: オブザーバーが文脈を保持する方法を変えるとき。
- 呼び出し先: `Cu.getWeakReference()`
- 参照: `this._weakContext`

## PopupShownObserver.observe()
- 位置: L22-33
- 役割: 他のパネルが開いたら自分の検証ポップアップを隠す。アクターが無くなれば監視を外す。
- 触るとき: 他のポップアップとの共存ルールを変えるとき。
- 呼び出し先: `ctxt.currentWindowGlobal?.getExistingActor()`, `this._weakContext.get()`
- 条件付き依存: `if (!actor)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (topic == "popup-shown" && subject != actor._panel)` → `actor._hidePopup()`
- 参照: `actor._panel`
- XPCOM: `Services.obs`

## FormValidationParent.constructor()
- 位置: L42-47
- 役割: パネルとオブザーバーの参照を空で初期化する。
- 触るとき: パネル参照の初期状態を変えるとき。
- 呼び出し先: `super()`
- 参照: `this._obs`, `this._panel`

## FormValidationParent.hasOpenPopups()
- 位置: L49-63
- 役割: 全ウィンドウの panel や menupopup に開いているものがあるかを返す。自分のパネルは除く。
- 触るとき: 検証ポップアップを出してよいかの判定を変えるとき。
- 呼び出し先: `win.document.querySelectorAll()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`

## FormValidationParent.uninit()
- 位置: L69-72
- 役割: パネルとオブザーバーの参照を消す。
- 触るとき: アクター破棄時の後始末を変えるとき。
- 参照: `this._obs`, `this._panel`

## FormValidationParent.hidePopup()
- 位置: L74-76
- 役割: 外部から検証ポップアップを閉じるための入口で、_hidePopup に委譲する。
- 触るとき: 外から閉じる経路を追うとき。
- 呼び出し先: `this._hidePopup()`

## FormValidationParent.receiveMessage()
- 位置: L82-111
- 役割: 前面タブからの表示要求だけを受け、他のポップアップが無ければ表示する。隠す要求には閉じる。
- 触るとき: 表示の条件やメッセージの扱いを変えるとき。
- 呼び出し先: `FormValidationParent.hasOpenPopups()`, `this._hidePopup()`, `this._showPopup()`
- 参照: `aMessage.data`, `aMessage.name`, `browser.documentGlobal`, `tabBrowser.selectedBrowser`, `this._panel`, `this.browsingContext.top.embedderElement`, `window.gBrowser`

## FormValidationParent.handleEvent()
- 位置: L113-124
- 役割: ズーム変更やスクロールでポップアップを隠し、popuphidden で後始末を行う。
- 触るとき: ポップアップを閉じるきっかけを変えるとき。
- 呼び出し先: `this._hidePopup()`, `this._onPopupHidden()`
- 参照: `aEvent.type`

## FormValidationParent._onPopupHidden()
- 位置: L130-140
- 役割: popuphidden 後に、オブザーバーとタブのスクロール・ズームの監視を外し、参照を消す。
- 触るとき: 閉じた後の後始末を変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `aEvent.originalTarget.removeEventListener()`, `tabBrowser.selectedBrowser.removeEventListener()`
- 参照: `aEvent.originalTarget.documentGlobal.gBrowser`, `this._obs`, `this._panel`
- XPCOM: `Services.obs`

## FormValidationParent._showPopup()
- 位置: L153-186
- 役割: 表示中ならメッセージだけ更新する。初回は監視を付けてタブを制約し、位置を計算してパネルを開く。
- 触るとき: ポップアップの開き方や位置を変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `aBrowser.addEventListener()`, `aBrowser.constrainPopup()`, `this._getAndMaybeCreatePanel()`, `this._panel.addEventListener()`, `this._panel.openPopupAtScreenRect()`
- 参照: `aPanelData.message`, `aPanelData.position`, `aPanelData.screenRect`, `rect.height`, `rect.left`, `rect.top`, `rect.width`, `this._obs`, `this._panel`, `this._panel.firstChild.textContent`, `this.browsingContext`
- XPCOM: `Services.obs`

## FormValidationParent._hidePopup()
- 位置: L192-194
- 役割: パネルがあれば閉じる。
- 触るとき: 閉じる処理の条件を変えるとき。
- 呼び出し先: `this._panel?.hidePopup()`

## FormValidationParent._getAndMaybeCreatePanel()
- 位置: L196-209
- 役割: 初回だけテンプレートを展開し、invalid-form-popup パネルを取得して保持する。
- 触るとき: パネルの生成方法を変えるとき。
- 条件付き依存: `if (!this._panel)` → `window.document.getElementById()`
- 条件付き依存: `if (template)` → `template.replaceWith()`
- 参照: `browser.documentGlobal`, `template.content`, `this._panel`, `this.browsingContext.top.embedderElement`
