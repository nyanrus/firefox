# browser/components/storybook/stories/icon-directory.stories.mjs

source: browser/components/storybook/stories/icon-directory.stories.mjs
source-hash: 15525d2dbee63584adb5e9a111f0d807f0a8c6f6
lines: 513

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `buildIconData()`, `css()`, `customElements.define()`

## prioritizeGroups()
- 位置: L48-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bundleFileInfoMap.get()`, `bundleFileInfoMap.keys()`, `bundleGroupings.find()`, `bundleGroupings.map()`, `group.startsWith()`, `newGroups.get()`, `newGroups.get(bundleGroup).push()`, `newGroups.has()`
- 条件付き依存: `if (!newGroups.has(bundleGroup))` → `newGroups.set()`

## buildIconData()
- 位置: L80-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `a.fileName.localeCompare()`, `bundleFileInfoMap .get()`, `bundleFileInfoMap .get(bundleDir) .push()`, `bundleFileInfoMap.has()`, `bundleFileInfoMap.values()`, `bundlePath.endsWith()`, `chromeUri.startsWith()`, `icons.sort()`, `prioritizeGroups()`, `resolveToChrome()`, `reversePrefixMap.set()`, `srcPath.lastIndexOf()`, `srcPath.substring()`
- 条件付き依存: `if (!bundleFileInfoMap.has(bundleDir))` → `bundleFileInfoMap.set()`
- 参照: `b.fileName`

## resolveToChrome()
- 位置: L95-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bundlePath.substring()`, `dirPath.includes()`, `dirPath.lastIndexOf()`, `dirPath.substring()`, `reversePrefixMap.get()`
- 参照: `dir.length`

## rgbToHex()
- 位置: L152-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `match .slice()`, `match .slice(0, 3) .map()`, `match .slice(0, 3) .map(n => parseInt(n, 10).toString(16).padStart(2, "0")) .join()`, `parseInt()`, `parseInt(n, 10).toString()`, `parseInt(n, 10).toString(16).padStart()`, `rgb.match()`
- 参照: `match.length`

## IconDirectory.constructor()
- 位置: L300-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `IconSize.Normalize`, `this._successMessageTimeout`, `this.fillColor`, `this.filter`, `this.iconSize`, `this.strokeColor`

## IconDirectory.disconnectedCallback()
- 位置: L311-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `super.disconnectedCallback()`
- 参照: `this._successMessageTimeout`

## IconDirectory.firstUpdated()
- 位置: L319-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getComputedStyle()`, `rgbToHex()`, `this.renderRoot.querySelector()`
- 参照: `probeStyles.fill`, `probeStyles.stroke`, `this.fillColor`, `this.strokeColor`

## IconDirectory.successMessageBar()
- 位置: L327-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## IconDirectory.handleSearch()
- 位置: L332-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.detail.query.toLowerCase()`
- 参照: `this.filter`

## IconDirectory.handleFillChange()
- 位置: L337-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.style.setProperty()`
- 参照: `e.target.value`, `this.fillColor`

## IconDirectory.handleStrokeChange()
- 位置: L343-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.style.setProperty()`
- 参照: `e.target.value`, `this.strokeColor`

## IconDirectory.handleCopy()
- 位置: async L349-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `navigator.clipboard.writeText()`, `this.hideSuccessMessage()`, `this.showSuccessMessage()`
- 参照: `target.dataset.url`

## IconDirectory.showSuccessMessage()
- 位置: L364-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `setTimeout()`, `this.hideSuccessMessage()`, `this.successMessageBar.removeAttribute()`, `this.successMessageBar.showPopover()`
- 参照: `this._successMessageTimeout`

## IconDirectory.hideSuccessMessage()
- 位置: L378-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.successMessageBar.addEventListener()`, `this.successMessageBar.hidePopover()`, `this.successMessageBar.removeAttribute()`, `this.successMessageBar.setAttribute()`
- 条件付き依存: `if (instant)` → `this.successMessageBar.hidePopover()`

## IconDirectory.filteredIcons()
- 位置: L400-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeUri.toLowerCase()`, `chromeUri.toLowerCase().includes()`, `filePath.toLowerCase()`, `filePath.toLowerCase().includes()`, `icons.filter()`
- 参照: `this.filter`

## IconDirectory.iconGroupTemplate()
- 位置: L415-454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `fileName.endsWith()`, `filtered.map()`, `html()`, `this.filteredIcons()`
- 参照: `filtered.length`, `this.handleCopy`

## IconDirectory.render()
- 位置: L456-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...iconData.entries()].map()`, `html()`, `iconData.entries()`, `this.iconGroupTemplate()`
- 参照: `IconSize.Full`, `IconSize.Normalize`, `e.target.pressed`, `this.fillColor`, `this.handleFillChange`, `this.handleSearch`, `this.handleStrokeChange`, `this.iconSize`, `this.strokeColor`

## Default()
- 位置: L510-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
