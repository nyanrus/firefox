# browser/components/aiwindow/ui/components/ai-chat-content/ai-chat-content.stories.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/ai-chat-content.stories.mjs
source-hash: f5ff99601aac2c470b031992863a77b6457ed7d5
lines: 64

## <module>
- 役割: ai-chat-content の Storybook 定義。会話の状態を渡すための設定と翻訳文字列を持つ。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L28-30
- 役割: conversationState を ai-chat-content に渡す共通テンプレート。
- 触るとき: 会話ストーリーに渡す状態の形（role、body、appliedMemories）を変えるとき、ここで受け渡しを確認する。
- 呼び出し先: `html()`
