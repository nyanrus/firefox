# browser/components/urlbar/UrlbarProviderUnitConversion.sys.mjs

source: browser/components/urlbar/UrlbarProviderUnitConversion.sys.mjs
source-hash: ab23c8b3eabdba0d16a540d0a0f49b78c5aeebee
lines: 161

## <module>
- 役割: 入力文字列を単位変換として解釈し、換算結果をクリップボードへコピーできる動的結果を出す UrlbarProviderUnitConversion を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## UrlbarProviderUnitConversion.constructor()
- 位置: L76-78
- 役割: 基底の UrlbarProvider をそのまま初期化するだけのコンストラクターである。
- 触るとき: プロバイダーに初期状態を持たせるとき、ここに処理を足す。
- 呼び出し先: `super()`

## UrlbarProviderUnitConversion.type()
- 位置: L83-85
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: 単位変換結果を他の結果種別とどう並べるかを変えるとき見る。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderUnitConversion.isActive()
- 位置: async L95-110
- 役割: unitConversion.enabled が有効なときだけ、三つの変換器を順に試し、変換できた結果を _activeResult に保存して有効にする。
- 触るとき: 単位変換が出ない、または通常の検索語で誤って出る問題を調べるとき見る。変換器の追加や順序もここで効く。
- 呼び出し先: `converter.convert()`, `lazy.UrlbarPrefs.get()`
- 参照: `this._activeResult`

## UrlbarProviderUnitConversion.getViewTemplate()
- 位置: L112-114
- 役割: 単位変換結果の表示部品(アイコン、出力、アクションの span)の構造を返す。
- 触るとき: 変換結果の表示レイアウトやアイコンを変えるとき、VIEW_TEMPLATE を見る。

## UrlbarProviderUnitConversion.getViewUpdate()
- 位置: L120-129
- 役割: 出力欄に換算結果の文字列を入れ、アクション欄にクリップボードへのコピーの l10n ID を設定する。
- 触るとき: 表示文言や、コピー操作の案内を変えたいとき見る。
- 参照: `result.payload.output`

## UrlbarProviderUnitConversion.startQuery()
- 位置: L138-150
- 役割: 保持した換算結果を DYNAMIC 型の結果として一件追加する。suggestedIndex は設定 unitConversion.suggestedIndex に従う。
- 触るとき: 換算結果の表示位置を変えたい、または結果の payload を増やしたいときに見る。
- 呼び出し先: `addCallback()`, `lazy.UrlbarPrefs.get()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `queryContext.searchString`, `this._activeResult`

## UrlbarProviderUnitConversion.onEngagement()
- 位置: L157-159
- 役割: 選択された結果の換算値をクリップボードへコピーする。
- 触るとき: 選択時の動作(コピー以外の操作を足す等)を変えるとき見る。
- 呼び出し先: `lazy.ClipboardHelper.copyString()`
- 参照: `details.result.payload.output`
