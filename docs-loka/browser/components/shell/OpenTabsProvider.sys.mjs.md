# browser/components/shell/OpenTabsProvider.sys.mjs

source: browser/components/shell/OpenTabsProvider.sys.mjs
source-hash: a9a13524c947f72346b938f687ada9b53e1f884b
lines: 27

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getOpenTabs()
- 位置: L13-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `lazy.UrlbarProviderOpenTabs.getOpenTabUrls()`, `urls.keys()`

## switchToOpenTab()
- 位置: L19-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win?.switchToTabHavingURI()`
