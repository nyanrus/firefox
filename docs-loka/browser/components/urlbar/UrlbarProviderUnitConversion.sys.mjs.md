# browser/components/urlbar/UrlbarProviderUnitConversion.sys.mjs

source: browser/components/urlbar/UrlbarProviderUnitConversion.sys.mjs
source-hash: ab23c8b3eabdba0d16a540d0a0f49b78c5aeebee
lines: 161

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## UrlbarProviderUnitConversion.constructor()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderUnitConversion.type()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderUnitConversion.isActive()
- 位置: async L95-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `converter.convert()`, `lazy.UrlbarPrefs.get()`
- 参照: `this._activeResult`

## UrlbarProviderUnitConversion.getViewTemplate()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderUnitConversion.getViewUpdate()
- 位置: L120-129
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload.output`

## UrlbarProviderUnitConversion.startQuery()
- 位置: L138-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`, `lazy.UrlbarPrefs.get()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `queryContext.searchString`, `this._activeResult`

## UrlbarProviderUnitConversion.onEngagement()
- 位置: L157-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ClipboardHelper.copyString()`
- 参照: `details.result.payload.output`
