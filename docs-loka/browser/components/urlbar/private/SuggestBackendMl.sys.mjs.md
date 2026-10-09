# browser/components/urlbar/private/SuggestBackendMl.sys.mjs

source: browser/components/urlbar/private/SuggestBackendMl.sys.mjs
source-hash: dec7f4157cfbe9d096ab4142aea30c7dd51ef7e8
lines: 112

## <module>
- 役割: ML 版の提案バックエンド。MLSuggest の結果を受け、対応する機能が有効なときだけ提案として返す。Rust バックエンドと同時に有効にできる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SuggestBackendMl.enablingPreferences()
- 位置: L22-24
- 役割: 有効判定に使う pref として quickSuggestMlEnabled と browser.ml.enable を返す。
- 触るとき: ML 提案が出ない問題で有効条件を確かめるとき。

## SuggestBackendMl.enable()
- 位置: L26-32
- 役割: 有効化なら #init()、無効化なら #uninit() を呼ぶ。
- 触るとき: ML 機能の有効・無効切り替えの流れを追うとき。
- 条件付き依存: `if (enabled)` → `this.#init()`
- 条件付き依存: `if (!(enabled))` → `this.#uninit()`

## SuggestBackendMl.query()
- 位置: async L47-82
- 役割: 検索文字列を小文字・トリム済みのものにする。ML インテントを持つ機能が1つも有効でなければ空配列を返す。MLSuggest のインテントに対応する機能が無効か不明なら捨て、有効なら source を 'ml' にして返す。
- 触るとき: ML 提案が出ない原因を調べるとき、またはインテントと機能の対応を変えるとき。
- 呼び出し先: `lazy.MLSuggest.makeSuggestions()`, `lazy.QuickSuggest.mlFeatures .values()`, `lazy.QuickSuggest.mlFeatures .values() .every()`, `this.logger.debug()`
- 条件付き依存: `if ( lazy.QuickSuggest.mlFeatures .values() .every(f => !f.isEnabled || !f.isMlIntentEnabled) )` → `this.logger.debug()`
- 条件付き依存: `if (suggestion?.intent)` → `lazy.QuickSuggest.getFeatureByMlIntent()`
- 条件付き依存: `if (!feature?.isEnabled || !feature?.isMlIntentEnabled)` → `this.logger.debug()`
- 参照: `f.isEnabled`, `f.isMlIntentEnabled`, `feature?.isEnabled`, `feature?.isMlIntentEnabled`, `queryContext.trimmedLowerCaseSearchString`, `suggestion.intent`, `suggestion.provider`, `suggestion.source`, `suggestion?.intent`

## SuggestBackendMl.#init()
- 位置: L84-102
- 役割: 初期化タイマーを作る。すでにあれば何もしない。遅延は quickSuggestMlInitDelaySeconds で決まり、発火時に MLSuggest の初期化を行う。モデル読み込みは端末に負荷がかかるため、起動直後を避けている。
- 触るとき: モデルの読み込みを始めるタイミングを変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.SkippableTimer`, `this.#initTimer`, `this.logger`, `this.name`

## callback()
- 位置: async L97-100
- 役割: タイマーの発火時にログを出し、MLSuggest.initialize() を待つ。
- 触るとき: モデルの初期化がいつ始まるか、またはどこで失敗するかを確かめるとき。
- 呼び出し先: `lazy.MLSuggest.initialize()`, `this.logger.info()`

## SuggestBackendMl.#uninit()
- 位置: async L104-108
- 役割: タイマーを止めて参照を消し、MLSuggest.shutdown() を待つ。
- 触るとき: 機能を無効にしたあとにモデルのエンジンが解放されるかを確かめるとき。
- 呼び出し先: `lazy.MLSuggest.shutdown()`, `this.#initTimer?.cancel()`
- 参照: `this.#initTimer`
