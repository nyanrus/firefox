# browser/components/urlbar/UrlbarProviderRestrictKeywords.sys.mjs

source: browser/components/urlbar/UrlbarProviderRestrictKeywords.sys.mjs
source-hash: 0a2e587c82301ecfc73c1a3a1f95329d67262502
lines: 91

## <module>
- 役割: 検索モードを指定する制限キーワード(@ で始まる語)を候補として出す UrlbarProviderRestrictKeywords を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderRestrictKeywords.constructor()
- 位置: L27-29
- 役割: 基底の UrlbarProvider をそのまま初期化するだけのコンストラクターである。
- 触るとき: プロバイダーに初期状態を持たせるとき、ここに処理を足す。
- 呼び出し先: `super()`

## UrlbarProviderRestrictKeywords.type()
- 位置: L34-36
- 役割: プロバイダー種別として HEURISTIC を返し、ヒューリスティック枠で扱われるようにする。
- 触るとき: 制限キーワード候補の表示位置や muxer での優先の扱いを変えたいとき見る。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderRestrictKeywords.getPriority()
- 位置: L38-40
- 役割: プロバイダーの優先度として 1 を返す。
- 触るとき: 制限キーワード候補を他の候補より前後させたいとき、この値を見直す。

## UrlbarProviderRestrictKeywords.isActive()
- 位置: async L42-51
- 役割: searchRestrictKeywords の feature gate が有効で、検索モード外かつ入力が「@」だけのときに限って有効にする。
- 触るとき: 「@」入力で候補が出ない、または別の入力でも出てしまう原因を調べるとき、有効化条件を確かめる。
- 呼び出し先: `lazy.UrlbarPrefs.getScotchBonnetPref()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.trimmedSearchString`

## UrlbarProviderRestrictKeywords.startQuery()
- 位置: async L60-89
- 役割: L10n の制限キーワードを列挙し、対応する検索モードのアイコン付きの RESTRICT 結果を一つずつ追加する。
- 触るとき: 候補の表示内容(キーワード、アイコン、ハイライト)を変えるとき、この関数の payload を変更する。
- 呼び出し先: `addCallback()`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.find()`, `lazy.UrlbarTokenizer.getL10nRestrictKeywords()`, `tokenToKeyword.entries()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.find( mode => mode.restrict == token )?.icon`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.RESTRICT`, `mode.restrict`, `this.queryInstance`
