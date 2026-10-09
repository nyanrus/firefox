# browser/components/aiwindow/ui/components/ai-chat-card/ai-chat-card.stories.mjs

source: browser/components/aiwindow/ui/components/ai-chat-card/ai-chat-card.stories.mjs
source-hash: 74685cd99f12735c63978492a335640a429af338
lines: 54

## <module>
- 役割: ai-chat-card の Storybook 定義。タイトル、操作欄の設定、サムネイルの有無ごとのストーリーを持つ。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L20-28
- 役割: url・title・favicon・thumbnail・timestamp を ai-chat-card に渡す共通テンプレート。
- 触るとき: カードに新しい属性を足すとき、このテンプレートにも渡す項目を追加する。
- 呼び出し先: `html()`
