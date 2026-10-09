# browser/components/urlbar/UrlbarProviderClipboard.sys.mjs

source: browser/components/urlbar/UrlbarProviderClipboard.sys.mjs
source-hash: c9bad3fd842ef2c7e398c998e25c1f36b5af689f
lines: 169

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderClipboard.constructor()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderClipboard.type()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderClipboard.setPreviousClipboardValue()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#previousClipboard.value`

## UrlbarProviderClipboard.isActive()
- 位置: async L49-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.getFixupPrimitives()`, `controller.browserWindow.readFromClipboard()`, `lazy.UrlUtils.REGEXP_SPACES.test()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.sanitizeTextFromClipboard()`, `queryContext.restrictInSearchMode()`, `this.#validUrl()`
- 参照: `queryContext.isPrivate`, `queryContext.searchString`, `textFromClipboard.length`, `this.#previousClipboard`, `this.#previousClipboard.impressionsLeft`, `this.#previousClipboard.value`

## UrlbarProviderClipboard.#validUrl()
- 位置: L93-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 参照: `givenUrl.href`, `givenUrl.protocol`

## UrlbarProviderClipboard.getPriority()
- 位置: L107-110
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderClipboard.startQuery()
- 位置: async L119-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`, `lazy.UrlbarShared.prepareUrlForDisplay()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `this.#previousClipboard.value`

## UrlbarProviderClipboard.onEngagement()
- 位置: L145-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handlePossibleCommand()`
- 参照: `details.result`, `details.selType`, `this.#previousClipboard.impressionsLeft`

## UrlbarProviderClipboard.onImpression()
- 位置: L151-153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#previousClipboard.impressionsLeft`

## UrlbarProviderClipboard.#handlePossibleCommand()
- 位置: L160-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`
- 参照: `RESULT_MENU_COMMANDS.DISMISS`, `this.#previousClipboard.impressionsLeft`
