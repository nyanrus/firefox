# browser/components/urlbar/private/SportsSuggestions.sys.mjs

source: browser/components/urlbar/private/SportsSuggestions.sys.mjs
source-hash: b52fc22c0a52187bac199d8d262922eef238748b
lines: 344

## <module>
- 役割: スポーツの試合結果(チーム、スコア、日時、状態)を urlbar に表示するリアルタイム提案。試合情報の表示テンプレートと更新内容を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SportsSuggestions.realtimeType()
- 位置: L20-22
- 役割: 種別名 'sports' を返す。
- 触るとき: スポーツ提案の種別名や、それに付く設定 pref を追うとき。

## SportsSuggestions.isSponsored()
- 位置: L24-26
- 役割: スポンサーではない false を返す。
- 触るとき: スポーツ提案に広告表記が付く条件を調べるとき。

## SportsSuggestions.merinoProvider()
- 位置: L28-30
- 役割: Merino の provider 名 'sports' を返す。
- 触るとき: スポーツの結果が Merino から来ないときに provider 名を確かめるとき。

## SportsSuggestions.getViewTemplateForImageContainer()
- 位置: L32-69
- 役割: ホームとアウェイの2つの画像コンテナを作る。各コンテナは画像と日付のチクレット(日と月)を持つ。
- 触るとき: チームのアイコン表示や日付チクレットの構成を変えるとき。
- 呼び出し先: `["home", "away"].map()`

## SportsSuggestions.getViewTemplateForDescriptionTop()
- 位置: L71-76
- 役割: 両チームのスコアがあれば #viewTemplateTopWithScores、無ければ #viewTemplateTopWithoutScores のテンプレートを返す。
- 触るとき: 上段の表示をスコアの有無で切り替える条件を変えるとき。
- 呼び出し先: `stringifiedScore()`, `this.#viewTemplateTopWithScores()`, `this.#viewTemplateTopWithoutScores()`
- 参照: `item.away_team.score`, `item.home_team.score`

## SportsSuggestions.#viewTemplateTopWithScores()
- 位置: L78-103
- 役割: ホームのチーム名とスコア、区切り、アウェイのスコアとチーム名を並べたテンプレートを返す。
- 触るとき: スコア付きの上段の並びや CSS クラスを変えるとき。

## SportsSuggestions.#viewTemplateTopWithoutScores()
- 位置: L105-113
- 役割: チーム名をまとめて1つの要素にするテンプレートを返す。
- 触るとき: スコアが無い試合の上段表示を変えるとき。

## SportsSuggestions.getViewTemplateForDescriptionBottom()
- 位置: L115-139
- 役割: 競技名、区切り、日付、区切り、状態の要素のテンプレートを返す。
- 触るとき: 下段に出す項目や並びを変えるとき。

## SportsSuggestions.getViewUpdateForPayloadItem()
- 位置: L141-158
- 役割: スコアの有無に応じた上段の更新と、画像と下段の更新を合わせ、競技カテゴリと状態を item の属性に入れて返す。
- 触るとき: 試合1件の表示更新の組み立て方を変えるとき。
- 呼び出し先: `stringifiedScore()`, `this.#viewUpdateImageAndBottom()`, `this.#viewUpdateTopWithScores()`, `this.#viewUpdateTopWithoutScores()`
- 参照: `item.away_team.score`, `item.home_team.score`, `item.sport_category`, `item.status_type`

## SportsSuggestions.#viewUpdateTopWithScores()
- 位置: L160-175
- 役割: 両チームの名前とスコアを textContent に設定する更新を返す。
- 触るとき: スコア付きの上段の文字列を変えるとき。
- 呼び出し先: `stringifiedScore()`
- 参照: `item.away_team.name`, `item.away_team.score`, `item.home_team.name`, `item.home_team.score`

## SportsSuggestions.#viewUpdateTopWithoutScores()
- 位置: L177-189
- 役割: チーム名を 'urlbar-result-sports-team-names' のローカライズ文字列に渡して返す。
- 触るとき: スコアが無い試合のチーム名の文言を変えるとき。
- 参照: `item.away_team.name`, `item.home_team.name`

## SportsSuggestions.#viewUpdateImageAndBottom()
- 位置: L191-334
- 役割: 日時を整形し、チクレットの日と月を作る。チームごとにアイコン URL があれば表示し、無ければ has-team-icon を付けずにチクレットを見せる。両チームの内容が同じならアウェイ側の画像コンテナを隠す。状態は live なら「ライブ」、当日の past なら「終了」、それ以外は空にする。
- 触るとき: 日付の表示形式、アイコンの有無による出し分け、状態の文言を変えるとき。
- 呼び出し先: `Object.entries()`, `Object.entries(imageUpdatesByTeam).reduce()`, `Object.fromEntries()`, `["home", "away"].reduce()`, `lazy.ObjectUtils.deepEqual()`, `lazy.UrlbarShared.formatDate()`, `new Intl.DateTimeFormat(undefined, { month: "short", day: "numeric", timeZone: zonedNow.timeZoneId, }).formatToParts()`, `partsArray.map()`
- 条件付き依存: `if (item[itemKey]?.icon)` → `UrlbarUtils.getRemoteImageUrl()`
- 参照: `Intl.DateTimeFormat`, `imageUpdatesByTeam.away`, `imageUpdatesByTeam.away[`image-container-${i}`].attributes.hidden`, `imageUpdatesByTeam.home`, `item.away_team?.icon`, `item.date`, `item.home_team?.icon`, `item.sport`, `item.status_type`, `item[itemKey].icon`, `item[itemKey]?.icon`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`, `partsMap.day`, `partsMap.month`, `zonedNow.timeZoneId`

## stringifiedScore()
- 位置: L337-343
- 役割: スコアを文字列にする。数値は String に変換し、文字列以外(欠損など)は空文字を返す。
- 触るとき: スコアが 0 や欠損のときに画面にどう出るかを確かめるとき。
- 条件付き依存: `if (typeof s == "number")` → `String()`
