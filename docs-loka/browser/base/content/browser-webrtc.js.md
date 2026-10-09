# browser/base/content/browser-webrtc.js

source: browser/base/content/browser-webrtc.js
source-hash: 6e5ae91b9c0056c057618818f90b7dc792e4e7f5
lines: 139

## <module>
- 役割: (未記入)

## willShowSharedTabWarning()
- 位置: L20-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `panel.openPopup()`, `this._createSharedTabWarningIfNeeded()`, `webrtcUI.getWindowShareState()`, `webrtcUI.shouldShowSharedTabWarning()`
- 条件付き依存: `if (shareState == webrtcUI.SHARING_SCREEN)` → `hbox.setAttribute()`
- 条件付き依存: `if (shareState == webrtcUI.SHARING_SCREEN)` → `panel.setAttribute()`
- 条件付き依存: `if (!(shareState == webrtcUI.SHARING_SCREEN))` → `hbox.setAttribute()`
- 条件付き依存: `if (!(shareState == webrtcUI.SHARING_SCREEN))` → `panel.setAttribute()`
- 参照: `allowForSessionCheckbox.checked`, `panel.firstChild`, `this._sharedTabWarningEnabled`, `webrtcUI.SHARING_NONE`, `webrtcUI.SHARING_SCREEN`

## sharedTabWarningShown()
- 位置: L66-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowButton.focus()`, `document.getElementById()`

## allowSharedTabSwitch()
- 位置: L75-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._hideSharedTabWarning()`, `webrtcUI.allowSharedTabSwitch()`
- 参照: `document.getElementById( "sharing-warning-disable-for-session" ).checked`, `panel.anchorNode`

## tabAdded()
- 位置: L96-103
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._sharedTabWarningEnabled)` → `webrtcUI.getWindowShareState()`
- 条件付き依存: `if (shareState != webrtcUI.SHARING_NONE)` → `webrtcUI.tabAddedWhileSharing()`
- 参照: `this._sharedTabWarningEnabled`, `webrtcUI.SHARING_NONE`

## _sharedTabWarningEnabled()
- 位置: L105-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._sharedTabWarningEnabled`

## _hideSharedTabWarning()
- 位置: L118-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (panel)` → `panel.hidePopup()`

## _createSharedTabWarningIfNeeded()
- 位置: L129-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("sharing-tabs-warning-panel"))` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("sharing-tabs-warning-panel"))` → `template.replaceWith()`
- 参照: `template.content`
