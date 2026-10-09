# browser/components/aiwindow/ui/components/ai-action-result/ai-action-result.stories.mjs

source: browser/components/aiwindow/ui/components/ai-action-result/ai-action-result.stories.mjs
source-hash: 0d6f11e2e555363ddfe22584db29fa429d4019c5
lines: 154

## <module>
- 役割: ai-action-result の Storybook 定義。タイトル、引数の操作欄、翻訳文字列を設定する。
- 呼び出し先: `ResizableTemplate.bind()`, `Template.bind()`, `makeWebsites()`

## makeWebsites()
- 位置: L27-31
- 役割: 件数分の例 URL とラベルを持つ website 配列を作る。
- 触るとき: チップの件数を変えた見た目を試すストーリーを増やすときに使う。
- 呼び出し先: `Array.from()`

## Template()
- 位置: L33-41
- 役割: label・summary・undo・展開・rows を ai-action-result に渡す共通テンプレート。
- 触るとき: ストーリーに渡す属性を増やすとき、または属性名を変えたときに、このテンプレートも合わせる。
- 呼び出し先: `html()`

## ResizableTemplate()
- 位置: L103-121
- 役割: 幅を横方向にリサイズできる枠で ai-action-result を包むテンプレート。
- 触るとき: チップの折り返しや溢れを、狭い幅で確認するストーリーを変えるときに見る。
- 呼び出し先: `html()`
