# browser/actors/SpeechDispatcherParent.sys.mjs

source: browser/actors/SpeechDispatcherParent.sys.mjs
source-hash: d1f334a034058c027b2dcd9fb0a9d96b77ff8cc4
lines: 91

## <module>
- 役割: (未記入)

## SpeechDispatcherParent.prefName()
- 位置: L6-8
- 役割: (未記入)
- 触るとき: (未記入)

## SpeechDispatcherParent.disableNotification()
- 位置: L10-12
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.prefName()`
- XPCOM: `Services.prefs`

## SpeechDispatcherParent.receiveMessage()
- 位置: async L14-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `Services.prefs.getBoolPref()`, `browser.getTabBrowser()`, `browser.getTabBrowser().getNotificationBox()`, `console.error()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.prefName()`
- 条件付き依存: `if (Services.prefs.getBoolPref(this.prefName(), false))` → `console.info()`
- 参照: `aMessage.data`, `browser.documentGlobal.MozXULElement`, `notificationBox.PRIORITY_INFO_HIGH`, `this.browsingContext.top.embedderElement`
- XPCOM: `Services.prefs`

## callback()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.disableNotification()`
