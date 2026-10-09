# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-loader/chat-assistant-loader.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-loader/chat-assistant-loader.mjs
source-hash: 455dc16cb293e74c1754b2cfe34d6e8e7af3b65d
lines: 76

## <module>
- 役割: アシスタントの応答準備中に出す読み込み表示 chat-assistant-loader を定義する。
- 呼び出し先: `customElements.define()`

## ChatAssistantLoader.constructor()
- 位置: L18-21
- 役割: mode を既定の default に設定する。
- 触るとき: 読み込み表示の既定モードを変えるときに見る。
- 呼び出し先: `super()`
- 参照: `this.mode`

## ChatAssistantLoader.render()
- 位置: L23-72
- 役割: mode ごとにスピナーか専用アイコン、文言を切り替えて描画する。default では aria-label を付ける。
- 触るとき: 検索中や自然言語処理中の表示を変えるとき、または mode の追加時に分岐を足すときに見る。
- 呼び出し先: `html()`
- 参照: `this.mode`
