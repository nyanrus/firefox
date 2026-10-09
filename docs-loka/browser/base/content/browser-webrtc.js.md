# browser/base/content/browser-webrtc.js

source: browser/base/content/browser-webrtc.js
source-hash: 6e5ae91b9c0056c057618818f90b7dc792e4e7f5
lines: 139

## <module>
- 役割: 共有タブ警告(WebRTC で画面・ウィンドウ共有中にタブを切り替えるときの確認パネル)を管理する gSharedTabWarning オブジェクトを定義する。

## willShowSharedTabWarning()
- 位置: L20-60
- 役割: 共有中のウィンドウで別タブへ切り替える前に呼ばれ、警告パネルを出すべきなら表示して true を返し、切り替えを取り消させる。
- 触るとき: 共有タブ警告の表示条件を変えるとき、たとえばタブ切り替えを止める判定や共有種別(画面かウィンドウか)によるパネル文言を調べるとき。
- 呼び出し先: `document.getElementById()`, `panel.openPopup()`, `this._createSharedTabWarningIfNeeded()`, `webrtcUI.getWindowShareState()`, `webrtcUI.shouldShowSharedTabWarning()`
- 条件付き依存: `if (shareState == webrtcUI.SHARING_SCREEN)` → `hbox.setAttribute()`
- 条件付き依存: `if (shareState == webrtcUI.SHARING_SCREEN)` → `panel.setAttribute()`
- 条件付き依存: `if (!(shareState == webrtcUI.SHARING_SCREEN))` → `hbox.setAttribute()`
- 条件付き依存: `if (!(shareState == webrtcUI.SHARING_SCREEN))` → `panel.setAttribute()`
- 参照: `allowForSessionCheckbox.checked`, `panel.firstChild`, `this._sharedTabWarningEnabled`, `webrtcUI.SHARING_NONE`, `webrtcUI.SHARING_SCREEN`

## sharedTabWarningShown()
- 位置: L66-69
- 役割: 警告パネル表示後に「続行」ボタンへフォーカスを移す。
- 触るとき: 警告パネルのフォーカス順やキーボード操作を直すとき、パネルが開いた直後にどのボタンが選ばれるかを確認するとき。
- 呼び出し先: `allowButton.focus()`, `document.getElementById()`

## allowSharedTabSwitch()
- 位置: L75-84
- 役割: パネルの「続行」ボタンから呼ばれ、チェックボックスの値を添えて webrtcUI に切り替え許可を伝えてからパネルを隠す。
- 触るとき: 警告を今後出さない(セッション中は無効)チェックボックスの挙動を変えるとき、許可の記録先が webrtcUI のどこかを追うとき。
- 呼び出し先: `document.getElementById()`, `this._hideSharedTabWarning()`, `webrtcUI.allowSharedTabSwitch()`
- 参照: `document.getElementById( "sharing-warning-disable-for-session" ).checked`, `panel.anchorNode`

## tabAdded()
- 位置: L96-103
- 役割: 共有中にタブが開かれたとき、そのタブを警告の対象外として webrtcUI に登録する。
- 触るとき: 共有中に開いた新規タブで警告が出てしまう不具合を調べるとき、gBrowser からのタブ追加通知の流れを確認するとき。
- 条件付き依存: `if (this._sharedTabWarningEnabled)` → `webrtcUI.getWindowShareState()`
- 条件付き依存: `if (shareState != webrtcUI.SHARING_NONE)` → `webrtcUI.tabAddedWhileSharing()`
- 参照: `this._sharedTabWarningEnabled`, `webrtcUI.SHARING_NONE`

## _sharedTabWarningEnabled()
- 位置: L105-113
- 役割: privacy.webrtc.sharedTabWarning の値を遅延取得する getter で、初回参照時にゲッターを置き換えてキャッシュする。
- 触るとき: 警告機能の有効・無効を制御する pref を変えたとき、または pref 読み込みのタイミングを調べるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._sharedTabWarningEnabled`

## _hideSharedTabWarning()
- 位置: L118-123
- 役割: 警告パネルが存在すれば hidePopup() で閉じる。
- 触るとき: 警告パネルを閉じる経路を増やすとき、パネルが開きっぱなしになる不具合を調べるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (panel)` → `panel.hidePopup()`

## _createSharedTabWarningIfNeeded()
- 位置: L129-137
- 役割: 警告パネルの template を初回表示時に DOM へ挿入する(遅延生成)。
- 触るとき: 警告パネルの DOM 構造を変えたとき、またはパネルが見つからないエラーの原因を調べるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("sharing-tabs-warning-panel"))` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("sharing-tabs-warning-panel"))` → `template.replaceWith()`
- 参照: `template.content`
