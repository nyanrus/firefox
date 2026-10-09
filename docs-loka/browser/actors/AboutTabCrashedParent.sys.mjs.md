# browser/actors/AboutTabCrashedParent.sys.mjs

source: browser/actors/AboutTabCrashedParent.sys.mjs
source-hash: 79d589c04b216a90526e5f913fa80559c115f09d
lines: 89

## <module>
- 役割: about:tabcrashed の親側アクター。クラッシュしたタブの一覧を管理し、復元・閉じる操作とクラッシュレポート送信を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutTabCrashedParent.didDestroy()
- 位置: L17-19
- 役割: アクターが破棄されたとき、クラッシュページの登録を外す。
- 触るとき: クラッシュ後のタブを閉じた際に一覧の件数がずれる問題を調べるときに見る。
- 呼び出し先: `this.removeCrashedPage()`

## AboutTabCrashedParent.receiveMessage()
- 位置: async L21-61
- 役割: Load・closeTab・restoreTab・restoreAll を処理し、登録・レポート送信・タブ閉じや SessionStore での復元を行う。
- 触るとき: クラッシュ画面のボタン操作やクラッシュレポートの送信条件を変えるときに見る。
- 呼び出し先: `browser.getTabBrowser()`, `gAboutTabCrashedPages.set()`, `gBrowser.getTabForBrowser()`, `gBrowser.removeTab()`, `lazy.SessionStore.reviveAllCrashedTabs()`, `lazy.SessionStore.reviveCrashedTab()`, `lazy.TabCrashHandler.maybeSendCrashReport()`, `lazy.TabCrashHandler.onAboutTabCrashedLoad()`, `this.sendAsyncMessage()`, `this.updateTabCrashedCount()`
- 条件付き依存: `if (!browser)` → `this.removeCrashedPage()`
- 参照: `message.name`, `this.browsingContext.top.embedderElement`

## AboutTabCrashedParent.removeCrashedPage()
- 位置: L63-72
- 役割: 一覧から自分を外し、件数を更新して、ブラウザのクラッシュ処理の終了を通知する。
- 触るとき: クラッシュページを閉じた後の後始末に問題があるときに見る。
- 呼び出し先: `gAboutTabCrashedPages.delete()`, `gAboutTabCrashedPages.get()`, `lazy.TabCrashHandler.onAboutTabCrashedUnload()`, `this.updateTabCrashedCount()`
- 参照: `this.browsingContext.top.embedderElement`

## AboutTabCrashedParent.updateTabCrashedCount()
- 位置: L74-87
- 役割: 開いている about:tabcrashed ページ全部に、現在の件数を UpdateCount メッセージで送る。
- 触るとき: 「すべて復元」ボタンの表示条件に関わる件数の同期を調べるときに見る。
- 呼び出し先: `gAboutTabCrashedPages.keys()`
- 条件付き依存: `if (browser)` → `browser.sendMessageToActor()`
- 参照: `actor.browsingContext.top.embedderElement`, `gAboutTabCrashedPages.size`
