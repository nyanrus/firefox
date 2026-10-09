# browser/components/aiwindow/ui/components/ai-chat-message/ai-chat-message.stories.mjs

source: browser/components/aiwindow/ui/components/ai-chat-message/ai-chat-message.stories.mjs
source-hash: 72e65af86c33a743ab852df79ab97b844f9e16ab
lines: 45

## <module>
- 役割: ai-chat-message の Storybook 定義。ユーザー・アシスタント・Markdown 付きのストーリーを持つ。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L22-24
- 役割: role と本文を ai-chat-message に渡す共通テンプレート。
- 触るとき: メッセージの表示バリエーションを増やすとき、ここで role と本文を渡す。
- 呼び出し先: `html()`
