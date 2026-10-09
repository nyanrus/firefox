# browser/components/tabbrowser/TabMetrics.sys.mjs

source: browser/components/tabbrowser/TabMetrics.sys.mjs
source-hash: aa68c600db2147881f906be5564bfedd414c2b63
lines: 165

## <module>
- 役割: タブ操作のテレメトリで使う操作元・操作種別などの定数と、コンテキスト生成関数を凍結オブジェクトにまとめて TabMetrics として公開する。
- 呼び出し先: `Object.freeze()`

## userTriggeredContext()
- 位置: L113-119
- 役割: ユーザーの明示操作を表す isUserTriggered: true のコンテキストを、指定した操作元付きで作る(操作元が空なら unknown)。
- 触るとき: ユーザー操作起点のタブ操作にテレメトリ用コンテキストを渡す呼び出し側を書く・直すとき。
- 参照: `METRIC_SOURCE.UNKNOWN`

## decomposedContext()
- 位置: L127-132
- 役割: 既存コンテキストを複製し、個別イベントに分解された操作であることを示す isDecomposed: true を加える。
- 触るとき: 複数タブの一括操作を1件ずつの処理に分けて数える挙動を調べるとき。

## sourceForEvent()
- 位置: L134-152
- 役割: DOM イベントの種類から操作元を決める(DOMMouseScroll はホイール、ジェスチャーとキーボードはそれぞれ対応値、それ以外や無しは unknown)。
- 触るとき: ホイール・ジェスチャー・キー操作の操作元が誤って記録されるなど、イベントから操作元への判定を調べるとき。
- 呼び出し先: `KeyboardEvent.isInstance()`, `SimpleGestureEvent.isInstance()`
- 参照: `METRIC_SOURCE.GESTURE`, `METRIC_SOURCE.KEYBOARD`, `METRIC_SOURCE.MOUSE_WHEEL`, `METRIC_SOURCE.UNKNOWN`, `event.type`
