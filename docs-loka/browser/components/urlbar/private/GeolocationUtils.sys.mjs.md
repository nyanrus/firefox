# browser/components/urlbar/private/GeolocationUtils.sys.mjs

source: browser/components/urlbar/private/GeolocationUtils.sys.mjs
source-hash: 5701b76f3e79a6914ae9e3a1af59c940e2d64fa2
lines: 296

## <module>
- 役割: Merino から利用者の位置情報を取得し、候補の中から位置に最も近い項目を選ぶユーティリティ。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `lazy.UrlbarShared.getLogger()`

## _GeolocationUtils.geolocation()
- 位置: async L59-76
- 役割: Merino の geolocation プロバイダに問い合わせ、位置情報を返す。取得できなければ null を返す。
- 触るとき: 位置情報の取得元やキャッシュ期間(2 時間)、タイムアウト(5000 ms)を変えるとき、または Merino の応答形式が変わって位置が取れなくなったときに見る。
- 呼び出し先: `lazy.logger.debug()`, `this.#merino.fetch()`
- 参照: `lazy.MerinoClient`, `results?.[0]?.custom_details?.geolocation`, `this.#merino`

## _GeolocationUtils.best()
- 位置: async L123-137
- 役割: 候補が 2 件以上あるとき、距離、地域、国の順に判定して最適な項目を返す。位置が無ければ先頭を返す。
- 触るとき: 候補の既定選択ルールを変えるとき、または位置情報が無い環境で先頭の候補が使われる理由を調べるときに見る。
- 呼び出し先: `this.#bestByDistance()`, `this.#bestByRegion()`, `this.geolocation()`
- 参照: `items.length`

## _GeolocationUtils.#bestByDistance()
- 位置: L165-225
- 役割: 球面三角法で距離を求め、利用者の座標に最も近い候補を返す。精度半径内で同距離なら人口の多い方を選ぶ。
- 触るとき: 座標による候補選択の精度や、半径・人口による同点判定を調整するとき、または座標が文字列で渡された場合の変換を確かめるときに見る。
- 呼び出し先: `Math.abs()`, `Math.acos()`, `Math.cos()`, `Math.sin()`, `[geoLat, geoLong].map()`, `[locationLat, locationLong].map()`, `hasLargerPopulation()`, `isNaN()`, `locationFromItem()`, `parseFloat()`
- 参照: `bestTuple.location`, `bestTuple?.item`, `geo.location?.latitude`, `geo.location?.longitude`, `geo.location?.radius`, `location.latitude`, `location.longitude`

## _GeolocationUtils.#bestByRegion()
- 位置: L248-278
- 役割: 同じ国の候補を探し、地域コードも一致する候補があればそれを、無ければ同国の候補を返す。同点は人口で決める。
- 触るとき: 座標が無い候補を国や地域で絞るときの挙動を変えるとき、または地域コードの大文字小文字の扱いを確かめるときに見る。
- 呼び出し先: `geo.country_code?.toLowerCase()`, `geo.region_code?.toLowerCase()`, `location?.country?.toLowerCase()`, `locationFromItem()`
- 条件付き依存: `if (location?.country?.toLowerCase() == geoCountry)` → `hasLargerPopulation()`
- 条件付き依存: `if (location?.country?.toLowerCase() == geoCountry)` → `location.region?.toLowerCase()`
- 参照: `bestCountryTuple.location`, `bestCountryTuple?.item`, `bestRegionTuple.location`, `bestRegionTuple?.item`

## toRadians()
- 位置: L284-286
- 役割: 度数法の角度をラジアンに変換する。
- 触るとき: 距離計算の結果が大きくずれたときに、座標の単位変換が正しいかを確かめるときに見る。
- 参照: `Math.PI`

## hasLargerPopulation()
- 位置: L288-293
- 役割: a に数値の人口があり、b より多いか b に人口が無いときに true を返す。
- 触るとき: 同点の候補をどちらに倒すかのルールを変えるとき、または人口データが無い候補が選ばれる理由を調べるときに見る。
- 参照: `a.population`, `b.population`
