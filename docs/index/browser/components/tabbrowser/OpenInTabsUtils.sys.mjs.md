# browser/components/tabbrowser/OpenInTabsUtils.sys.mjs

source: browser/components/tabbrowser/OpenInTabsUtils.sys.mjs
source-hash: 489e7a063c45840b956fb2eea49862cf3a7c8c6a
lines: 76

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## l10n()
- 位置: L8-9
- 役割: (未記入)
- 触るとき: (未記入)

## confirmOpenInTabs()
- 位置: L20-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.prompt.confirmEx()`, `lazy.l10n.formatMessagesSync()`
- 条件付き依存: `if (reallyOpen && !warnOnOpen.value)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs` / `Services.prompt`

## promiseConfirmOpenInTabs()
- 位置: L68-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `resolve()`, `this.confirmOpenInTabs()`
- XPCOM: `Services.tm`
