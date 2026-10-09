# browser/components/uitour/UITour-lib.js

source: browser/components/uitour/UITour-lib.js
source-hash: d7d31841d265451501e8c417521261aef94d5314
lines: 896

## <module>
- 役割: (未記入)

## _sendEvent()
- 位置: L30-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`

## _generateCallbackID()
- 位置: L42-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.random()`, `Math.random() .toString()`, `Math.random() .toString(36) .replace()`

## _waitForCallback()
- 位置: L48-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_generateCallbackID()`, `document.addEventListener()`

## listener()
- 位置: L51-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `document.removeEventListener()`
- 参照: `event.detail`, `event.detail.callbackID`, `event.detail.data`

## _notificationListener()
- 位置: L68-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notificationListener()`
- 参照: `event.detail`, `event.detail.event`, `event.detail.params`

## Mozilla.UITour.ping()
- 位置: L134-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`
- 条件付き依存: `if (callback)` → `_waitForCallback()`
- 参照: `data.callbackID`

## Mozilla.UITour.observe()
- 位置: L152-164
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (listener)` → `document.addEventListener()`
- 条件付き依存: `if (listener)` → `Mozilla.UITour.ping()`
- 条件付き依存: `if (!(listener))` → `document.removeEventListener()`

## Mozilla.UITour.registerPageID()
- 位置: L177-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.showHighlight()
- 位置: L213-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.hideHighlight()
- 位置: L225-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.showInfo()
- 位置: L269-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `_sendEvent()`
- 条件付き依存: `if (Array.isArray(buttons))` → `buttonData.push()`
- 条件付き依存: `if (Array.isArray(buttons))` → `_waitForCallback()`
- 条件付き依存: `if (options && options.closeButtonCallback)` → `_waitForCallback()`
- 条件付き依存: `if (options && options.targetCallback)` → `_waitForCallback()`
- 参照: `buttons.length`, `buttons[i].callback`, `buttons[i].icon`, `buttons[i].label`, `buttons[i].style`, `options.closeButtonCallback`, `options.targetCallback`

## Mozilla.UITour.hideInfo()
- 位置: L313-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.showMenu()
- 位置: L344-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`
- 条件付き依存: `if (callback)` → `_waitForCallback()`

## Mozilla.UITour.hideMenu()
- 位置: L363-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.showNewTab()
- 位置: L378-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.showHome()
- 位置: L394-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.showProtectionReport()
- 位置: L405-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.getConfiguration()
- 位置: L587-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`, `_waitForCallback()`

## Mozilla.UITour.setConfiguration()
- 位置: L609-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.showFirefoxAccounts()
- 位置: L659-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `_sendEvent()`

## Mozilla.UITour.showFirefoxAccountsForAIWindow()
- 位置: L680-682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.showConnectAnotherDevice()
- 位置: L706-710
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `_sendEvent()`

## Mozilla.UITour.resetFirefox()
- 位置: L721-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.addNavBarWidget()
- 位置: L737-742
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`, `_waitForCallback()`

## Mozilla.UITour.setDefaultSearchEngine()
- 位置: L753-757
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.pinToTaskbar()
- 位置: L765-767
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.setNewtabWallpaper()
- 位置: L781-785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.setTreatmentTag()
- 位置: L797-802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.getTreatmentTag()
- 位置: L816-821
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`, `_waitForCallback()`

## Mozilla.UITour.setSearchTerm()
- 位置: L831-835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.forceShowReaderIcon()
- 位置: L844-846
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.toggleReaderMode()
- 位置: L853-855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.openPreferences()
- 位置: L871-875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`

## Mozilla.UITour.closeTab()
- 位置: L887-889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_sendEvent()`
