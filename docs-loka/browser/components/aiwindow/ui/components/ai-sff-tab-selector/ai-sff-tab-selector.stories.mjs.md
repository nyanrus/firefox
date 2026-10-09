# browser/components/aiwindow/ui/components/ai-sff-tab-selector/ai-sff-tab-selector.stories.mjs

source: browser/components/aiwindow/ui/components/ai-sff-tab-selector/ai-sff-tab-selector.stories.mjs
source-hash: 0f14b5a929abb56efb0b3622987ae41dfe464a02
lines: 124

## <module>
- 役割: ai-sff-tab-selector を Storybook で確認するためのストーリーと文言を定義する。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L40-45
- 役割: 候補タブとその他のタブを渡して ai-sff-tab-selector を描画する共通テンプレート。
- 触るとき: 確認用に別のタブ構成(候補なし、多数のタブなど)を試したいとき。
- 呼び出し先: `html()`
