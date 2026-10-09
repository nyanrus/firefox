# browser/components/extensions/ExtensionBrowsingData.sys.mjs

source: browser/components/extensions/ExtensionBrowsingData.sys.mjs
source-hash: 9ca3be643dd1158afb06de65c78375a940afbd7b
lines: 76

## <module>
- 役割: 拡張機能の browsingData API から、履歴、ダウンロード、フォーム入力の削除と既定の削除設定を Sanitizer へ橋渡しするデリゲートを定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## BrowsingDataDelegate.constructor()
- 位置: L21-21
- 役割: 何もしない空のコンストラクタ。
- 触るとき: デリゲートが状態を持つようになったとき、ここに初期化を足す。現状は引数も状態もない。

## BrowsingDataDelegate.handleRemoval()
- 位置: L25-39
- 役割: downloads、formData、history を Sanitizer の clear に範囲付きで渡して消す。それ以外の種類は undefined を返し、他の処理に任せる。
- 触るとき: 拡張から消せるデータの種類を増やすとき、または削除範囲(makeRange)の扱いを確かめるとき。内部の cleaner を直接使う TODO(Bug 1803799) の移行先でもある。
- 呼び出し先: `lazy.Sanitizer.items.downloads.clear()`, `lazy.Sanitizer.items.formdata.clear()`, `lazy.Sanitizer.items.history.clear()`, `lazy.makeRange()`

## BrowsingDataDelegate.settings()
- 位置: L41-74
- 役割: privacy.cpd の cache、cookies、history、formdata、downloads の pref を読み、開始時刻(since)、削除対象、常に許可の値を Promise で返す。
- 触るとき: browsingData.settings の応答内容を変えるとき、または拡張の設定画面に出る既定の削除範囲を調べるとき。削除範囲が無ければ since は0になる。
- 呼び出し先: `Promise.resolve()`, `Services.prefs.getBoolPref()`, `lazy.Sanitizer.getClearRange()`
- XPCOM: `Services.prefs`
