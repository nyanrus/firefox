# browser/components/aiwindow/ui/components/smartwindow-topsites/smartwindow-topsites.stories.mjs

source: browser/components/aiwindow/ui/components/smartwindow-topsites/smartwindow-topsites.stories.mjs
source-hash: c8620d9ef53228ef06496d708ff3261fcb9f123d
lines: 65

## <module>
- 役割: トップサイトの Storybook 用ストーリー(サンプル 4 件の表示と空表示)を定義する
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L45-54
- 役割: sites を受けて smartwindow-topsites を描き、選択時に alert で URL を出す
- 触るとき: ストーリーでの選択挙動や表示幅の確認方法を変えるとき
- 呼び出し先: `alert()`, `html()`
- 参照: `e.detail.url`
