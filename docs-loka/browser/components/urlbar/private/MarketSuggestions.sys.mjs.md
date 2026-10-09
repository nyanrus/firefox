# browser/components/urlbar/private/MarketSuggestions.sys.mjs

source: browser/components/urlbar/private/MarketSuggestions.sys.mjs
source-hash: a8fff62fb25ad91d229784aeefba6ad2a4b6dba8
lines: 139

## <module>
- 役割: 株式・指数・投資信託の市況を urlbar に表示するリアルタイム提案。RealtimeSuggestProvider を継承し、表示テンプレートと更新内容を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## MarketSuggestions.realtimeType()
- 位置: L19-21
- 役割: リアルタイム提案の種別名 'market' を返す。
- 触るとき: 市況の提案を他のリアルタイム提案と区別する種別名を見直すとき。

## MarketSuggestions.isSponsored()
- 位置: L23-25
- 役割: スポンサー扱いではないことを示す false を返す。
- 触るとき: 市況の結果に広告表記が付く条件を調べるとき。

## MarketSuggestions.merinoProvider()
- 位置: L27-29
- 役割: Merino の provider 名 'polygon' を返す。
- 触るとき: 市況の結果が Merino から来ない問題で provider 名を確かめるとき。

## MarketSuggestions.getViewTemplateForDescriptionTop()
- 位置: L31-47
- 役割: 説明の上段(銘柄名、区切りの点、ティッカー)の要素テンプレートを返す。
- 触るとき: 上段に表示する項目を増減させるとき。

## MarketSuggestions.getViewTemplateForDescriptionBottom()
- 位置: L49-75
- 役割: 説明の下段(前日比、区切り、最終価格、区切り、取引所)の要素テンプレートを返す。
- 触るとき: 下段の項目やその CSS クラスを変えるとき。

## MarketSuggestions.getViewUpdateForPayloadItem()
- 位置: L77-137
- 役割: 前日比の正負で up・down・unchanged を決め、画像 URL があればそれを、なければ矢印画像を選ぶ。銘柄名や価格などの文字列と合わせて更新内容として返す。
- 触るとき: 価格や前日比の表示形式、矢印の出し分けを変えるとき。
- 呼び出し先: `parseFloat()`
- 条件付き依存: `if (item.image_url)` → `UrlbarUtils.getRemoteImageUrl()`
- 参照: `item.exchange`, `item.image_url`, `item.last_price`, `item.name`, `item.ticker`, `item.todays_change_perc`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`
