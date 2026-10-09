# browser/components/urlbar/private/YelpRealtimeSuggestions.sys.mjs

source: browser/components/urlbar/private/YelpRealtimeSuggestions.sys.mjs
source-hash: 0b5cf670712407b4560621345b9871bf31b17dca
lines: 136

## <module>
- 役割: Yelp の店舗情報(店名、住所、価格帯、営業状態、評価)を urlbar に表示するリアルタイム提案。スポンサー扱い。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## YelpRealtimeSuggestions.realtimeType()
- 位置: L19-23
- 役割: 種別名 'yelpRealtime' を返す。オフラインの Yelp 提案と混同しないよう 'yelp' を避けている。
- 触るとき: Yelp のリアルタイム提案の種別名や、それに付く設定 pref を追うとき。

## YelpRealtimeSuggestions.isSponsored()
- 位置: L25-27
- 役割: スポンサーとして true を返す。
- 触るとき: Yelp 提案にスポンサー表記や設定の効き方を調べるとき。

## YelpRealtimeSuggestions.merinoProvider()
- 位置: L29-31
- 役割: Merino の provider 名 'yelp' を返す。
- 触るとき: Yelp の結果が Merino から来ないときに provider 名を確かめるとき。

## YelpRealtimeSuggestions.getViewTemplateForDescriptionTop()
- 位置: L33-41
- 役割: 店名を表示する要素のテンプレートを返す。
- 触るとき: 店名の表示要素や CSS クラスを変えるとき。

## YelpRealtimeSuggestions.getViewTemplateForDescriptionBottom()
- 位置: L43-82
- 役割: 住所、価格帯、営業時間、評価の星、評価の数を区切りとともに並べたテンプレートを返す。
- 触るとき: 下段に出す項目を増減させるとき。

## YelpRealtimeSuggestions.getViewUpdateForPayloadItem()
- 位置: L84-134
- 役割: 最初の営業時間情報の is_open_now から open か closed を決めて属性に入れ、画像 URL と店の各項目を更新内容として返す。営業時間の文言には端末のローカル時刻の時を入れる(ソースの TODO のとおり、タイムゾーンの扱いは未解決)。
- 触るとき: 店舗の表示内容の更新方法を変えるとき、または営業時間の表示がずれるときに確かめるとき。
- 呼び出し先: `UrlbarUtils.getRemoteImageUrl()`, `new Intl.DateTimeFormat(undefined, { hour: "numeric", }).format()`
- 参照: `Intl.DateTimeFormat`, `item.address`, `item.business_hours`, `item.business_hours[0].is_open_now`, `item.image_url`, `item.name`, `item.pricing`, `item.rating`, `item.review_count`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`
