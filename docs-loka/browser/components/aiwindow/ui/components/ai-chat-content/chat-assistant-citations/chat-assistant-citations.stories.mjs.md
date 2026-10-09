# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-citations/chat-assistant-citations.stories.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-citations/chat-assistant-citations.stories.mjs
source-hash: 51ee722754b3d586c884d89fb3775dc876c41fb8
lines: 54

## <module>
- 役割: chat-assistant-citations の Storybook 定義。出典の件数別のストーリーと翻訳文字列を持つ。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L19-22
- 役割: citations 配列を chat-assistant-citations に渡す共通テンプレート。
- 触るとき: 出典の件数や title の有無を変えたストーリーを足すとき、このテンプレートで渡す。
- 呼び出し先: `html()`
