# browser/modules/ObserverForwarder.sys.mjs

source: browser/modules/ObserverForwarder.sys.mjs
source-hash: b62b572cdb111d87c21bd43a65d03728aece3867
lines: 79

## <module>
- 役割: オブザーバー通知を、対応するモジュールへ遅延読み込みしてから転送する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## init()
- 位置: L63-67
- 役割: gObservers に並ぶ全トピックを、この関数を観測者として登録する。
- 触るとき: 起動時にどのトピックを監視するかを変えるとき。
- 呼び出し先: `Object.keys()`, `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## observe()
- 位置: L69-77
- 役割: トピックに対応するモジュールの observe を呼び、例外はコンソールに出して続行する。
- 触るとき: 通知を受けたモジュールが動かない報告を調べるとき。1つのモジュールが失敗しても他には影響しない。
- 呼び出し先: `console.error()`, `lazy[objectName].observe()`
