# browser/components/aiwindow/ui/components/agent-monitor-item/monitor-error-copy.mjs

source: browser/components/aiwindow/ui/components/agent-monitor-item/monitor-error-copy.mjs
source-hash: 8f2d11155d3a216402e0548f6e40e56ecd32b3bf
lines: 41

## <module>
- 役割: モニターの失敗理由を表示する文言の対応表。エラーコードごとの Fluent ID を持ち、カードや履歴から参照される。
- 呼び出し先: `Object.freeze()`

## monitorErrorL10nId()
- 位置: L38-40
- 役割: エラーコードに対応する Fluent ID を返す。対応が無いコードや旧形式の履歴は、汎用の未知のエラーの ID を返す。
- 触るとき: 履歴の失敗理由の文言が出ない、または新しいエラーコードを足すときに見る。
