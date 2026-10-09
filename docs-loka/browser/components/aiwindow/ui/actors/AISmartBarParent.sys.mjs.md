# browser/components/aiwindow/ui/actors/AISmartBarParent.sys.mjs

source: browser/components/aiwindow/ui/actors/AISmartBarParent.sys.mjs
source-hash: f847011b6555f0799df3b5ba6addb806f8fbc5ee
lines: 34

## <module>
- 役割: urlbar から smartbar へ質問を渡す親アクター。送信内容を子アクターへ AskFromParent メッセージとして送る。

## AISmartBarParent.ask()
- 位置: async L30-32
- 役割: SmartbarCommitDetails をそのまま AskFromParent メッセージとして子アクターへ送る。
- 触るとき: urlbar から AI チャットへ渡す値(検索語、コンテキストのメンション、ページ URL)が smartbar に届かないとき、または送信経路を変えるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`
