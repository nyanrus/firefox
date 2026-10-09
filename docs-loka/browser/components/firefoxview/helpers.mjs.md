# browser/components/firefoxview/helpers.mjs

source: browser/components/firefoxview/helpers.mjs
source-hash: 38d35c2181877c94f193d7bcdec2d67243a2aae3
lines: 123

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## formatURIForDisplay()
- 位置: L27-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.formatURIStringForDisplay()`

## convertTimestamp()
- 位置: L33-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (elapsed <= _nowThresholdMs)` → `fluentStrings.formatValueSync()`
- 条件付き依存: `if (!(elapsed <= _nowThresholdMs))` → `lazy.relativeTimeFormat.formatBestUnit()`

## createFaviconElement()
- 位置: L55-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `favicon.classList.add()`, `getImageUrl()`
- 参照: `favicon.style.backgroundImage`

## getImageUrl()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUIUtils.getImageURL()`

## getLogger()
- 位置: L73-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loggersByName.get()`, `loggersByName.has()`
- 条件付き依存: `if (!loggersByName.has(loggerName))` → `lazy.Log.repository.getLogger()`
- 条件付き依存: `if (!loggersByName.has(loggerName))` → `logger.manageLevelFromPref()`
- 条件付き依存: `if (!loggersByName.has(loggerName))` → `logger.addAppender()`
- 条件付き依存: `if (!loggersByName.has(loggerName))` → `loggersByName.set()`
- 参照: `lazy.Log.BasicFormatter`, `lazy.Log.ConsoleAppender`

## escapeHtmlEntities()
- 位置: L85-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(text || "") .replace()`, `(text || "") .replace(/&/g, "&amp;") .replace()`, `(text || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace()`, `(text || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace(/>/g, "&gt;") .replace()`, `(text || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace(/>/g, "&gt;") .replace(/"/g, "&quot;") .replace()`

## navigateToLink()
- 位置: L94-122
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(isModifierClick))` → `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (currentWindow.openTrustedLinkIn)` → `currentWindow.openTrustedLinkIn()`
- 参照: `currentWindow.openTrustedLinkIn`, `e.detail.originalEvent`, `e.originalTarget.url`, `e.target.documentGlobal.browsingContext.embedderWindowGlobal.browsingContext .window`, `lazy.AppConstants.platform`, `originalEvent?.ctrlKey`, `originalEvent?.metaKey`
