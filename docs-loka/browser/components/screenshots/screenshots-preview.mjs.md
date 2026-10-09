# browser/components/screenshots/screenshots-preview.mjs

source: browser/components/screenshots/screenshots-preview.mjs
source-hash: 4b40270d040ef351d966c02fe5c15b7cdd5349ff
lines: 269

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `customElements.define()`

## ScreenshotsPreview.constructor()
- 位置: L33-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.screenshotsLocalization.formatMessagesSync()`, `super()`
- 参照: `copyKey.value`, `downloadKey.value`, `this.copyKey`, `this.downloadKey`, `this.openerBrowser`, `window.arguments`

## ScreenshotsPreview.connectedCallback()
- 位置: L48-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.updateL10nAttributes()`, `window.addEventListener()`

## ScreenshotsPreview.updateL10nAttributes()
- 位置: async L56-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `lazy.ShortcutUtils.getModifierString()`
- 参照: `this.copyButtonEl`, `this.copyKey`, `this.downloadButtonEl`, `this.downloadKey`, `this.updateComplete`

## ScreenshotsPreview.close()
- 位置: L76-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.close()`, `window.removeEventListener()`

## ScreenshotsPreview.handleEvent()
- 位置: L81-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleClick()`, `this.handleKeydown()`
- 参照: `event.type`

## ScreenshotsPreview.handleClick()
- 位置: L92-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ScreenshotsUtils.recordTelemetryEvent()`, `lazy.ScreenshotsUtils.scheduleRetry()`, `this.close()`, `this.saveToClipboard()`, `this.saveToFile()`
- 参照: `event.target.id`, `this.openerBrowser`

## ScreenshotsPreview.handleKeydown()
- 位置: L111-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.copyKey.toLowerCase()`, `this.downloadKey.toLowerCase()`, `this.getAccelKey()`
- 条件付き依存: `if (this.getAccelKey(event))` → `event.preventDefault()`
- 条件付き依存: `if (this.getAccelKey(event))` → `event.stopPropagation()`
- 条件付き依存: `if (this.getAccelKey(event))` → `this.saveToClipboard()`
- 条件付き依存: `if (this.getAccelKey(event))` → `this.saveToFile()`
- 参照: `event.key`

## ScreenshotsPreview.imageLoadedPromise()
- 位置: async L137-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.previewImg.addEventListener()`
- 条件付き依存: `if (this.previewImg.complete && this.previewImg.height > 0)` → `Promise.resolve()`
- 参照: `this.previewImg.complete`, `this.previewImg.height`, `this.previewImg.src`, `this.updateComplete`

## onImageLoaded()
- 位置: L144-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`
- 参照: `event.target.src`

## ScreenshotsPreview.getAccelKey()
- 位置: L151-156
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `event.ctrlKey`, `event.metaKey`, `lazy.AppConstants.platform`

## ScreenshotsPreview.enableButtons()
- 位置: L162-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buttons.forEach()`
- 参照: `button.disabled`

## ScreenshotsPreview.disableButtons()
- 位置: L170-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buttons.forEach()`
- 参照: `button.disabled`

## ScreenshotsPreview.saveToFile()
- 位置: async L174-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ScreenshotsUtils.downloadScreenshot()`, `this.disableButtons()`, `this.imageLoadedPromise()`
- 条件付き依存: `if (downloadSucceeded)` → `this.close()`
- 条件付き依存: `if (!(downloadSucceeded))` → `this.enableButtons()`
- 参照: `this.openerBrowser`

## ScreenshotsPreview.saveToClipboard()
- 位置: async L195-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ScreenshotsUtils.copyScreenshotFromBlobURL()`, `this.close()`, `this.disableButtons()`, `this.imageLoadedPromise()`
- 参照: `this.openerBrowser`

## ScreenshotsPreview.focusButton()
- 位置: L216-222
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (buttonToFocus === "copy")` → `this.copyButtonEl.focus()`
- 条件付き依存: `if (!(buttonToFocus === "copy"))` → `this.downloadButtonEl.focus()`

## ScreenshotsPreview.render()
- 位置: L224-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.handleClick`
