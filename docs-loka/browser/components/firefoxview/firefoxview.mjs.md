# browser/components/firefoxview/firefoxview.mjs

source: browser/components/firefoxview/firefoxview.mjs
source-hash: 2681149a97c89503f07fda778b354fe8f376d42a
lines: 212

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `document.addEventListener()`, `document.querySelector()`, `e.getModifierState()`, `event.target.getAttribute()`, `isAIWindow()`, `item.getAttribute()`, `onHashChange()`, `onViewsDeckViewChange()`, `pageList.push()`, `recordEnteredTelemetry()`, `recordNavigationTelemetry()`, `topChromeWindow.addEventListener()`, `topChromeWindow.removeEventListener()`, `updateSearchKeyboardShortcut()`, `updateSearchTextboxSize()`, `updateSyncVisibility()`, `viewsDeck.addEventListener()`, `window.addEventListener()`, `window.scrollTo()`

## onHashChange()
- 位置: L32-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changeView()`, `document.location?.hash.substring()`, `pageList.includes()`

## changeView()
- 位置: L40-43
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `pageNav.currentView`, `viewsDeck.selectedViewName`

## onViewsDeckViewChange()
- 位置: L45-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.getAttribute()`
- 条件付き依存: `if (child.getAttribute("name") == viewsDeck.selectedViewName)` → `child.enter()`
- 条件付き依存: `if (!(child.getAttribute("name") == viewsDeck.selectedViewName))` → `child.exit()`
- 参照: `viewsDeck.children`, `viewsDeck.selectedViewName`

## recordNavigationTelemetry()
- 位置: L56-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.changePageNavigation.record()`
- 参照: `eventTarget.parentNode.currentView`, `eventTarget.shortPageName`

## updateSearchTextboxSize()
- 位置: async L70-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `document.l10n.formatMessages()`
- 参照: `child.searchTextboxSize`, `msg.attributes`, `msg.attributes[0].value`, `placeholder.length`, `viewsDeck.children`

## updateSearchKeyboardShortcut()
- 位置: async L89-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `key.toLocaleLowerCase()`, `topChromeWindow.document.l10n.formatMessages()`
- 参照: `message.attributes`, `message.attributes[0].value`

## updateSyncVisibility()
- 位置: L97-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.querySelectorAll()`
- 参照: `el.hidden`
- XPCOM: `Services.prefs`

## recordEnteredTelemetry()
- 位置: L158-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.enteredFirefoxview.record()`, `document.location?.hash?.substring()`

## onCommand()
- 位置: L190-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.browserContextMenuTabs.record()`, `e.target.closest()`, `location.hash?.substring()`
- 参照: `document.hidden`, `e.target`, `item.id`

## onLocalesChanged()
- 位置: L202-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestIdleCallback()`, `updateSearchKeyboardShortcut()`, `updateSearchTextboxSize()`

## isAIWindow()
- 位置: L209-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActiveAndEnabled()`
