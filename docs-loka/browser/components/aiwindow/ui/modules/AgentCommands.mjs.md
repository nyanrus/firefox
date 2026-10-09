# browser/components/aiwindow/ui/modules/AgentCommands.mjs

source: browser/components/aiwindow/ui/modules/AgentCommands.mjs
source-hash: ae75522e7769b492ca9914319da7fdb7c7bf7b82
lines: 74

## <module>
- 役割: スマートバーで / に続けて入力するエージェントコマンドの id と、パレット表示用の情報を定義する。
- 呼び出し先: `Object.freeze()`

## parseAgentCommand()
- 位置: L60-73
- 役割: スマートバーの入力の先頭から /コマンド を取り出し、小文字の id と残りの本文に分ける。先頭がコマンドでなければ null を返す。
- 触るとき: コマンドの書式や本文の切り出しを変えるとき、入力がコマンドとして解釈されない理由を調べるとき。
- 呼び出し先: `COMMAND_REGEX.exec()`, `match[1].toLowerCase()`, `match[2].trim()`, `value.trim()`
