# browser/components/DesktopActorRegistry.sys.mjs

source: browser/components/DesktopActorRegistry.sys.mjs
source-hash: 4ceb32d5517d39074842e78c4f48b06c48e0881d
lines: 1124

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## onPreferenceChanged()
- 位置: L58-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.sendMessageToActor()`, `lazy.BrowserWindowTracker.orderedWindows.forEach()`
- 参照: `win.gBrowser.browsers`

## onPreferenceChanged()
- 位置: L409-418
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isEnabled)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(isEnabled))` → `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## onAddActor()
- 位置: L611-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `maybeRegister()`
- XPCOM: `Services.prefs`

## maybeRegister()
- 位置: L615-634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`
- 条件付き依存: `if (!isRegistered)` → `register()`
- 条件付き依存: `if (isRegistered)` → `unregister()`
- XPCOM: `Services.prefs`

## onAddActor()
- 位置: L965-992
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `maybeRegister()`
- XPCOM: `Services.prefs`

## maybeRegister()
- 位置: L968-984
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!isRegistered)` → `register()`
- 条件付き依存: `if (isRegistered)` → `unregister()`
- XPCOM: `Services.prefs`

## init()
- 位置: L1119-1122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ActorManagerParent.addJSProcessActors()`, `ActorManagerParent.addJSWindowActors()`
