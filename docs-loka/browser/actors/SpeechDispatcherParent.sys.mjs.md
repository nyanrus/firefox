# browser/actors/SpeechDispatcherParent.sys.mjs

source: browser/actors/SpeechDispatcherParent.sys.mjs
source-hash: d1f334a034058c027b2dcd9fb0a9d96b77ff8cc4
lines: 91

## <module>
- 役割: speech-dispatcher のエラーを受けて警告通知を出す親側アクター。通知の抑止設定も持つ。

## SpeechDispatcherParent.prefName()
- 位置: L6-8
- 役割: 通知の抑止に使う pref 名 media.webspeech.synth.dont_notify_on_error を返す。
- 触るとき: 抑止設定の pref 名を変えるとき。

## SpeechDispatcherParent.disableNotification()
- 位置: L10-12
- 役割: 上記 pref を true にして、以後この通知を出さないようにする。
- 触るとき: 「今後表示しない」の動作を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.prefName()`
- XPCOM: `Services.prefs`

## SpeechDispatcherParent.receiveMessage()
- 位置: async L14-89
- 役割: エラー種別を l10n ID に変換し、タブの通知ボックスに警告を出す。抑止済みなら何もしない。
- 触るとき: 音声合成エラーの表示内容やボタンを変えるとき。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `Services.prefs.getBoolPref()`, `browser.getTabBrowser()`, `browser.getTabBrowser().getNotificationBox()`, `console.error()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.prefName()`
- 条件付き依存: `if (Services.prefs.getBoolPref(this.prefName(), false))` → `console.info()`
- 参照: `aMessage.data`, `browser.documentGlobal.MozXULElement`, `notificationBox.PRIORITY_INFO_HIGH`, `this.browsingContext.top.embedderElement`
- XPCOM: `Services.prefs`

## callback()
- 位置: L72-74
- 役割: 通知の「閉じる」ボタンから呼ばれ、抑止設定を有効にする。
- 触るとき: 通知ボタンの動作を変えるとき。
- 呼び出し先: `this.disableNotification()`
