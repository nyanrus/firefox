# browser/components/urlbar/content/UrlbarContentPrefs.mjs

source: browser/components/urlbar/content/UrlbarContentPrefs.mjs
source-hash: 80eab57d0b91d5dd1a1de20fbf659bf8b29c52ac
lines: 40

## <module>
- 役割: content 側から UrlbarPrefs を使えるようにする窓口で、通常の chrome 環境では sys.mjs の本体を、子プロセスでは actor のポート経由の代替を返す。
- 呼び出し先: `getPrefs()`

## getPrefs()
- 位置: L16-37
- 役割: 実行環境を判定し、chrome なら UrlbarPrefs 本体を、子プロセスなら window.UrlbarActorPort を使う薄い代替オブジェクトを返す。
- 触るとき: 子プロセスで urlbar の pref が読めない、または observer が効かないといった問題を調べるとき。
- 条件付き依存: `if (typeof ChromeUtils != "undefined")` → `ChromeUtils.importESModule()`
- 参照: `ChromeUtils.importESModule( "moz-src:///browser/components/urlbar/UrlbarPrefs.sys.mjs" ).UrlbarPrefs`

## get()
- 位置: L26-26
- 役割: 子プロセスで pref の値を actor ポート経由で取得する。
- 触るとき: content 側で新しい pref を読む箇所を追加するとき。
- 呼び出し先: `window.UrlbarActorPort.getPref()`

## getScotchBonnetPref()
- 位置: L31-31
- 役割: scotchBonnet.enableOverride が真ならそれを優先し、偽なら指定 pref の値を返す。子プロセスではこの合成を get で行う。
- 触るとき: Scotch Bonnet 系の実験機能フラグの判定を変えるとき。
- 呼び出し先: `get()`

## addObserver()
- 位置: L32-32
- 役割: pref 変更を監視するオブザーバーを actor ポート経由で登録する。
- 触るとき: 子プロセス側で pref 変更に反応する処理を追加するとき。
- 呼び出し先: `window.UrlbarActorPort.addPrefObserver()`

## removeObserver()
- 位置: L33-33
- 役割: actor ポート経由で登録済みの pref オブザーバーを解除する。
- 触るとき: オブザーバーの解除漏れによる残留を調べるとき。
- 呼び出し先: `window.UrlbarActorPort.removePrefObserver()`

## toggleResultMenuKeyboardAccessible()
- 位置: L34-35
- 役割: 結果メニューのキーボード操作可否の切り替えを actor ポートに依頼する。
- 触るとき: 結果メニューのキーボードアクセシビリティ設定を子プロセスから切り替える処理を変えるとき。
- 呼び出し先: `window.UrlbarActorPort.toggleResultMenuKeyboardAccessible()`
