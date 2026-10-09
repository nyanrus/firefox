# browser/components/asrouter/modules/FeatureCalloutBroker.sys.mjs

source: browser/components/asrouter/modules/FeatureCalloutBroker.sys.mjs
source-hash: 080d1c7d552964d4956275f201218f00f772e416
lines: 221

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _FeatureCalloutBroker.makeFeatureCallout()
- 位置: L48-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#calloutMap.set()`, `this.handleFeatureCalloutCallback.bind()`, `win.addEventListener()`
- 参照: `controller.signal`, `lazy.FeatureCallout`

## cleanup()
- 位置: L53-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.cleanup()`, `controller.abort()`, `this.#calloutMap.delete()`

## _FeatureCalloutBroker.showFeatureCallout()
- 位置: async L83-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...win.document.querySelectorAll("panel")].some()`, `callout.showFeatureCallout()`, `callout.showFeatureCallout(message).catch()`, `item.cleanup()`, `this.#calloutMap.get()`, `win.document.querySelectorAll()`
- 条件付き依存: `if (currentCallout && currentCallout.callout.location !== "chrome")` → `currentCallout.cleanup()`
- 条件付き依存: `if (item)` → `callout.teardownFeatureTourProgress()`
- 条件付き依存: `if (message.content.tour_pref_name)` → `callout.setupFeatureTourProgress()`
- 条件付き依存: `if (!(item))` → `this.makeFeatureCallout()`
- 条件付き依存: `if (!(item))` → `this.#calloutMap.get()`
- 参照: `browser.documentGlobal`, `callout.browser`, `callout.pref`, `currentCallout.callout.location`, `item.callout`, `item.showing`, `item?.callout`, `message.content.tour_pref_default_value`, `message.content.tour_pref_name`, `options.pref`, `p.state`, `this.isCalloutShowing`, `win.gDialogBox?.dialog`

## _FeatureCalloutBroker.showCustomFeatureCallout()
- 位置: L162-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callout .showFeatureCallout()`, `callout .showFeatureCallout(message) .then()`, `callout .showFeatureCallout(message) .then(showing => { item.showing = showing; }) .catch()`, `item.cleanup()`, `this.#calloutMap.get()`
- 条件付き依存: `if (currentCallout && currentCallout.location !== location)` → `currentCallout.cleanup()`
- 条件付き依存: `if (item)` → `callout.teardownFeatureTourProgress()`
- 条件付き依存: `if (pref)` → `callout.setupFeatureTourProgress()`
- 条件付き依存: `if (!(item))` → `this.makeFeatureCallout()`
- 条件付き依存: `if (!(item))` → `this.#calloutMap.get()`
- 参照: `callout.pref`, `currentCallout.location`, `item.callout`, `item.showing`, `item?.callout`, `this.isCalloutShowing`

## _FeatureCalloutBroker.handleFeatureCalloutCallback()
- 位置: L199-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#calloutMap.get()`
- 参照: `item.showing`

## _FeatureCalloutBroker.isCalloutShowing()
- 位置: L212-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...this.#calloutMap.values()].some()`, `this.#calloutMap.values()`
