# browser/actors/SpeechDispatcherChild.sys.mjs

source: browser/actors/SpeechDispatcherChild.sys.mjs
source-hash: 732398b85b5b576007a04d447a8d001ea0cc2709
lines: 10

## <module>
- 役割: speech-dispatcher(音声合成)のエラー通知を親プロセスへ中継する子側アクター。

## SpeechDispatcherChild.observe()
- 位置: L6-8
- 役割: オブザーバーで受けたエラー種別を SpeechDispatcher:Error として親へ送る。
- 触るとき: 送るエラーの内容や経路を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`
