# browser/components/preferences/OnDeviceModelManager.mjs

source: browser/components/preferences/OnDeviceModelManager.mjs
source-hash: d9d3b7ba8a4b0f09aaf8771290dda3b3f467e158
lines: 285

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Object.freeze()`, `OnDeviceModelManager.init()`, `XPCOMUtils.declareLazy()`

## init()
- 位置: L86-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `this.prefsByFeature.set()`, `window.addEventListener()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L107-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.prefsByFeature .get()`, `this.prefsByFeature .get(/** @type {OnDeviceModelFeaturesEnum} */ (feature)) .has()`
- 条件付き依存: `if ( this.prefsByFeature .get(/** @type {OnDeviceModelFeaturesEnum} */ (feature)) .has(data) )` → `queueMicrotask()`
- 条件付き依存: `if ( this.prefsByFeature .get(/** @type {OnDeviceModelFeaturesEnum} */ (feature)) .has(data) )` → `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## getAIFeature()
- 位置: L132-153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `OnDeviceModelFeatures.KeyPoints`, `OnDeviceModelFeatures.PdfAltText`, `OnDeviceModelFeatures.SidebarChatbot`, `OnDeviceModelFeatures.SmartWindow`, `OnDeviceModelFeatures.SpeechRecognition`, `OnDeviceModelFeatures.TabGroups`, `OnDeviceModelFeatures.Translations`, `lazy.AIWindow`, `lazy.GenAI`, `lazy.LinkPreview`, `lazy.PdfJsGuessAltTextFeature`, `lazy.SmartTabGroupingManager`, `lazy.SpeechRecognitionFeature`, `lazy.TranslationsFeature`

## getFeaturePref()
- 位置: L160-179
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `OnDeviceModelFeatures.KeyPoints`, `OnDeviceModelFeatures.PdfAltText`, `OnDeviceModelFeatures.SidebarChatbot`, `OnDeviceModelFeatures.SmartWindow`, `OnDeviceModelFeatures.SpeechRecognition`, `OnDeviceModelFeatures.TabGroups`, `OnDeviceModelFeatures.Translations`

## isAllowed()
- 位置: L186-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAIFeature()`
- 参照: `this.getAIFeature(feature).isAllowed`

## hasDistinctEnabledState()
- 位置: L195-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAIFeature()`
- 参照: `this.getAIFeature(feature).hasDistinctEnabledState`

## isEnabled()
- 位置: L204-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAIFeature()`
- 参照: `this.getAIFeature(feature).isEnabled`

## isBlocked()
- 位置: L213-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAIFeature()`
- 参照: `this.getAIFeature(feature).isBlocked`

## canRunOnDevice()
- 位置: L222-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAIFeature()`
- 参照: `this.getAIFeature(feature).canRunOnDevice`

## getAiControlState()
- 位置: L231-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAIFeature()`
- 参照: `this.getAIFeature(feature).aiControlState`

## isManagedByPolicy()
- 位置: L240-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAIFeature()`
- 参照: `this.getAIFeature(feature).isManagedByPolicy`

## makeAvailable()
- 位置: async L249-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `this.getAIFeature()`, `this.getAIFeature(feature).makeAvailable()`, `this.getFeaturePref()`, `this.isManagedByPolicy()`
- XPCOM: `Services.prefs`

## enable()
- 位置: async L262-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `this.getAIFeature()`, `this.getAIFeature(feature).enable()`, `this.getFeaturePref()`, `this.isManagedByPolicy()`
- XPCOM: `Services.prefs`

## block()
- 位置: async L275-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `this.getAIFeature()`, `this.getAIFeature(feature).block()`, `this.getFeaturePref()`, `this.isManagedByPolicy()`
- XPCOM: `Services.prefs`
