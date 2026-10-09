# browser/components/urlbar/private/GeolocationUtils.sys.mjs

source: browser/components/urlbar/private/GeolocationUtils.sys.mjs
source-hash: 5701b76f3e79a6914ae9e3a1af59c940e2d64fa2
lines: 296

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `lazy.UrlbarShared.getLogger()`

## _GeolocationUtils.geolocation()
- 位置: async L59-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logger.debug()`, `this.#merino.fetch()`
- 参照: `lazy.MerinoClient`, `results?.[0]?.custom_details?.geolocation`, `this.#merino`

## _GeolocationUtils.best()
- 位置: async L123-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#bestByDistance()`, `this.#bestByRegion()`, `this.geolocation()`
- 参照: `items.length`

## _GeolocationUtils.#bestByDistance()
- 位置: L165-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`, `Math.acos()`, `Math.cos()`, `Math.sin()`, `[geoLat, geoLong].map()`, `[locationLat, locationLong].map()`, `hasLargerPopulation()`, `isNaN()`, `locationFromItem()`, `parseFloat()`
- 参照: `bestTuple.location`, `bestTuple?.item`, `geo.location?.latitude`, `geo.location?.longitude`, `geo.location?.radius`, `location.latitude`, `location.longitude`

## _GeolocationUtils.#bestByRegion()
- 位置: L248-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `geo.country_code?.toLowerCase()`, `geo.region_code?.toLowerCase()`, `location?.country?.toLowerCase()`, `locationFromItem()`
- 条件付き依存: `if (location?.country?.toLowerCase() == geoCountry)` → `hasLargerPopulation()`
- 条件付き依存: `if (location?.country?.toLowerCase() == geoCountry)` → `location.region?.toLowerCase()`
- 参照: `bestCountryTuple.location`, `bestCountryTuple?.item`, `bestRegionTuple.location`, `bestRegionTuple?.item`

## toRadians()
- 位置: L284-286
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Math.PI`

## hasLargerPopulation()
- 位置: L288-293
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.population`, `b.population`
