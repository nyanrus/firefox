# browser/components/miniwindow/MiniWindowUtils.sys.mjs

source: browser/components/miniwindow/MiniWindowUtils.sys.mjs
source-hash: 102d12b2163b68469755f3b263ff15f6615f9903
lines: 350

## <module>
- 役割: (未記入)

## MiniWindowUtils.fullTabSize()
- 位置: L21-26
- 役割: (未記入)
- 触るとき: (未記入)

## MiniWindowUtils.windowRectDesktopPx()
- 位置: L34-42
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `win.desktopToDeviceScale`, `win.devicePixelRatio`, `win.outerHeight`, `win.outerWidth`, `win.screenX`, `win.screenY`

## MiniWindowUtils.resolveOverlapConflicts()
- 位置: L67-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`, `candidate.center()`, `conflict.center()`, `distanceFromOriginal()`, `fits()`, `obstacles.map()`, `r.intersects()`, `taken.find()`
- 参照: `best.distance`, `best.left`, `best.top`, `bestCorner.distance`, `bestCorner.left`, `bestCorner.top`, `center.x`, `center.y`, `conflictCenter.x`, `conflictCenter.y`, `corner.x`, `corner.y`, `o.height`, `o.left`, `o.top`, `o.width`, `r.bottom`, `r.left`, `r.right`, `r.top`, `rect.height`, `rect.left`, `rect.top`, `rect.width`, `screen.bottom`, `screen.left`, `screen.right`, `screen.top`, `screenRect.height`, `screenRect.left`, `screenRect.top`, `screenRect.width`

## fits()
- 位置: L84-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `o.intersects()`, `screen.contains()`, `taken.some()`
- 参照: `corner.x`, `corner.y`, `rect.height`, `rect.width`

## distanceFromOriginal()
- 位置: L90-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 参照: `corner.x`, `corner.y`, `original.left`, `original.top`

## MiniWindowUtils.computeWindowRect()
- 位置: L150-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/gfx/screenmanager;1"].getService()`, `MiniWindowUtils.computeWindowRectForScreen()`, `screen.GetAvailRectDisplayPix()`, `sm.screenForRect()`
- 参照: `Ci.nsIScreenManager`, `Services.locale.isAppLocaleRTL`, `h.value`, `l.value`, `originWin.desktopToDeviceScale`, `originWin.devicePixelRatio`, `originWin.outerHeight`, `originWin.outerWidth`, `originWin.screenX`, `originWin.screenY`, `screen.contentsScaleFactor`, `screen.defaultCSSScaleFactor`, `t.value`, `w.value`
- XPCOM: `nsIScreenManager` / `@mozilla.org/gfx/screenmanager;1` / `Services.locale`

## MiniWindowUtils.repositionToAvoid()
- 位置: L190-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/gfx/screenmanager;1"].getService()`, `Math.round()`, `MiniWindowUtils.resolveOverlapConflicts()`, `MiniWindowUtils.windowRectDesktopPx()`, `avoidWins.map()`, `screen.GetAvailRectDisplayPix()`, `sm.screenForRect()`
- 参照: `Ci.nsIScreenManager`, `avoidWins.length`, `h.value`, `l.value`, `t.value`, `w.value`, `win.desktopToDeviceScale`, `win.devicePixelRatio`, `winRect.height`, `winRect.left`, `winRect.top`, `winRect.width`
- XPCOM: `nsIScreenManager` / `@mozilla.org/gfx/screenmanager;1`

## MiniWindowUtils.computeWindowRectForScreen()
- 位置: L249-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.round()`
- 条件付き依存: `if (aspect > availAspect)` → `Math.round()`
- 条件付き依存: `if (!(aspect > availAspect))` → `Math.round()`
- 参照: `availRect.height`, `availRect.left`, `availRect.top`, `availRect.width`, `cropInfo.height`, `cropInfo.width`

## MiniWindowUtils.computeFrameBox()
- 位置: L310-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`
- 参照: `cropInfo.viewportHeight`, `cropInfo.viewportWidth`, `measuredSize?.height`, `measuredSize?.width`

## MiniWindowUtils.computeTransform()
- 位置: L338-348
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `crop.left`, `crop.top`, `crop.width`
