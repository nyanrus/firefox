# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-loader/chat-assistant-loader.stories.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-loader/chat-assistant-loader.stories.mjs
source-hash: f99050b02c729ced0aab489110dd849f4664dac9
lines: 37

## <module>
- 役割: chat-assistant-loader の Storybook 定義。モード選択と翻訳文字列を持つ。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L22-24
- 役割: mode を chat-assistant-loader に渡す共通テンプレート。未指定時は default にする。
- 触るとき: 読み込み表示の新しいモードを試すストーリーを足すとき、ここで値を渡す。
- 呼び出し先: `html()`
