# browser/components/tabbrowser/OpenInTabsUtils.sys.mjs

source: browser/components/tabbrowser/OpenInTabsUtils.sys.mjs
source-hash: 489e7a063c45840b956fb2eea49862cf3a7c8c6a
lines: 76

## <module>
- 役割: タブブラウザのインスタンス無しで呼べる、複数タブを一度に開くときのユーティリティ OpenInTabsUtils を公開する。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## l10n()
- 位置: L8-9
- 役割: tabbrowser.ftl と brand.ftl を同期で読む Localization を遅延生成する。
- 触るとき: 確認ダイアログの文言取得元や読み込む ftl を変えるとき。

## confirmOpenInTabs()
- 位置: L20-63
- 役割: 開くタブ数が閾値以上なら確認ダイアログを出し、続行可否を返す。次回から警告しない選択で警告用の設定も無効化する。
- 触るとき: 大量タブを開く警告の条件、文言、設定(browser.tabs.warnOnOpen など)の挙動を変える・調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.prompt.confirmEx()`, `lazy.l10n.formatMessagesSync()`
- 条件付き依存: `if (reallyOpen && !warnOnOpen.value)` → `Services.prefs.setBoolPref()`
- 参照: `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `button.value`, `checkbox.value`, `message.value`, `title.value`, `warnOnOpen.value`
- XPCOM: `Services.prefs` / `Services.prompt`

## promiseConfirmOpenInTabs()
- 位置: L68-74
- 役割: confirmOpenInTabs をメインスレッドへ投げ直して実行し、結果を Promise で返す非同期版。
- 触るとき: 非同期の呼び出し元から確認ダイアログを使うときや、呼び出しタイミングの問題を調べるとき。
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `resolve()`, `this.confirmOpenInTabs()`
- XPCOM: `Services.tm`
