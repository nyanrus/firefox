# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-error/chat-assistant-error.stories.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-error/chat-assistant-error.stories.mjs
source-hash: f8c991ace87fe00cba2b1dd888598f55e88df6f6
lines: 89

## <module>
- 役割: chat-assistant-error の Storybook 定義。エラーコード別のストーリーと翻訳文字列を持つ。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L35-41
- 役割: error、errorText、actionButton を chat-assistant-error に渡す共通テンプレート。
- 触るとき: エラーコードの表示を確認する新しいストーリーを足すとき、このテンプレートで値を渡す。
- 呼び出し先: `html()`
