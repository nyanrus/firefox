# browser/components/urlbar/private/FlightStatusSuggestions.sys.mjs

source: browser/components/urlbar/private/FlightStatusSuggestions.sys.mjs
source-hash: 5369522add36f8d9687096024bf49d5ad4db6f86
lines: 299

## <module>
- 役割: フライト状況の候補を表示するための提供元クラスと、表示用の DOM テンプレートと更新内容を組み立てる処理。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## FlightStatusSuggestions.realtimeType()
- 位置: L19-21
- 役割: リアルタイム候補の種類として "flightStatus" を返す。
- 触るとき: フライト状況の候補を他のリアルタイム候補と区別する識別子を変えるとき、または候補の種類で分岐する箇所を調べるときに見る。

## FlightStatusSuggestions.isSponsored()
- 位置: L23-25
- 役割: 候補が広告(スポンサー)ではないことを表す false を返す。
- 触るとき: フライト状況の候補にスポンサー表示や広告向けの扱いを加えるときに見る。

## FlightStatusSuggestions.merinoProvider()
- 位置: L27-29
- 役割: Merino に問い合わせるときのプロバイダ名 "flightaware" を返す。
- 触るとき: フライト状況の取得元を別のプロバイダに変えるとき、または Merino 側の提供元名と合っているか確かめるときに見る。

## FlightStatusSuggestions.baseTelemetryType()
- 位置: L31-33
- 役割: テレメトリで使う基本の種類名 "flights" を返す。
- 触るとき: フライト状況の候補の計測名を変えるとき、またはテレメトリの集計で候補を識別する名前を確かめるときに見る。

## FlightStatusSuggestions.getViewTemplateForDescriptionTop()
- 位置: L35-62
- 役割: 説明の上段(出発時刻、出発空港、区切り、到着時刻、到着空港)の span 要素テンプレートを item ごとの index 付きで返す。
- 触るとき: 上段に表示する要素の並びや CSS クラスを変えるとき、または index 付きの要素名が更新処理の名前と合っているか確かめるときに見る。

## FlightStatusSuggestions.getViewTemplateForDescriptionBottom()
- 位置: L64-99
- 役割: 説明の下段(出発日、便名、状態、残り時間)の span 要素テンプレートを index 付きで返す。
- 触るとき: 下段の表示項目を増減したり並び替えたりするとき、または下段の要素名と getViewUpdateForPayloadItem の対応を確かめるときに見る。

## FlightStatusSuggestions.getViewUpdateForPayloadItem()
- 位置: L101-287
- 役割: Merino の応答 item を表示用の状態(Scheduled などを ontime などへ変換)、時刻、空港、便名、残り時間などの更新内容にまとめる。
- 触るとき: 状態の文言や色、遅延時の時刻の選び方(予定時刻か推定時刻か)を変えるとき、または表示が古い値のまま更新されない原因を調べるときに見る。
- 呼び出し先: `new Intl.DateTimeFormat(undefined, { hour: "numeric", minute: "numeric", timeZone: arrivalTimeZone, }).format()`, `new Intl.DateTimeFormat(undefined, { hour: "numeric", minute: "numeric", timeZone: departureTimeZone, }).format()`
- 条件付き依存: `if (status == "delayed" || !item.delayed)` → `getTimeZone()`
- 条件付き依存: `if (!(status == "delayed" || !item.delayed))` → `getTimeZone()`
- 条件付き依存: `if (status == "delayed")` → `getTimeZone()`
- 条件付き依存: `if (item.airline.icon)` → `UrlbarUtils.getRemoteImageUrl()`
- 条件付き依存: `if (status == "inflight")` → `Math.floor()`
- 条件付き依存: `if (typeof item.time_left_minutes == "number")` → `Math.floor()`
- 条件付き依存: `if (typeof item.time_left_minutes == "number")` → `new Intl.DurationFormat(undefined, { style: "short", }).format()`
- 参照: `Intl.DateTimeFormat`, `Intl.DurationFormat`, `item.airline.color`, `item.airline.icon`, `item.airline.name`, `item.arrival.estimated_time`, `item.arrival.scheduled_time`, `item.delayed`, `item.departure.estimated_time`, `item.departure.scheduled_time`, `item.destination.city`, `item.destination.code`, `item.flight_number`, `item.origin.city`, `item.origin.code`, `item.progress_percent`, `item.status`, `item.time_left_minutes`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`

## getTimeZone()
- 位置: L290-298
- 役割: ISO 時刻文字列末尾の UTC オフセットを取り出す。Z なら "UTC" を、オフセットが無ければ undefined を返す。
- 触るとき: 時刻の表示タイムゾーンが誤るとき、または Merino が返す時刻の書式が変わったときに見る。
- 呼び出し先: `isoTimeString.match()`
