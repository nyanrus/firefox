# browser/components/aiwindow/ui/components/ai-action-confirmation/ai-action-confirmation.stories.mjs

source: browser/components/aiwindow/ui/components/ai-action-confirmation/ai-action-confirmation.stories.mjs
source-hash: ac8e0622eee64bfa484e1ca35f953e086fc8e661
lines: 89

## <module>
- 役割: ai-action-confirmation の Storybook 定義。折りたたみ、展開、件数の多いタブ、元に戻した後の状態を見せる。
- 呼び出し先: `Array.from()`, `EXAMPLE_TABS.slice()`, `Template.bind()`

## Template()
- 位置: L37-53
- 役割: ラベル、件数、元に戻す可否、展開状態、タブを ai-action-confirmation に渡し、幅 320px の枠で描画する。
- 触るとき: Storybook で見た目を確かめるとき、またはカードに渡す属性を増やすときに見る。
- 呼び出し先: `html()`
