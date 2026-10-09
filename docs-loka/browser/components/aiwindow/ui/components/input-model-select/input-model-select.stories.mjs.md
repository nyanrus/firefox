# browser/components/aiwindow/ui/components/input-model-select/input-model-select.stories.mjs

source: browser/components/aiwindow/ui/components/input-model-select/input-model-select.stories.mjs
source-hash: e1bb7c3590d31efded9a282e5a7efa1c94bb7e37
lines: 72

## <module>
- 役割: input-model-select の Storybook 用ストーリーを定義し、標準モデルとカスタムモデルを含む一覧の例を並べるモジュール。
- 呼び出し先: `Object.values()`, `Object.values(AVAILABLE_MODELS_WITH_CUSTOM).map()`, `Template.bind()`

## Template()
- 位置: L54-59
- 役割: availableModels と selectedModelId を input-model-select に渡して描く。
- 触るとき: モデル一覧の例を増やしたり、選択中のモデルの見え方を確かめたりするとき。
- 呼び出し先: `html()`
