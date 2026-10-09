# browser/components/aiwindow/ui/components/smartwindow-panel-list/smartwindow-panel-list.stories.mjs

source: browser/components/aiwindow/ui/components/smartwindow-panel-list/smartwindow-panel-list.stories.mjs
source-hash: aa219b3c2e3883dc11f65961473149b851a499d8
lines: 164

## <module>
- 役割: smartwindow-panel-list の Storybook 用ストーリーを定義し、空の状態や項目ありの状態を並べるモジュール。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L30-39
- 役割: groups と placeholderL10nId を渡し、固定の座標にアンカーを置いて常時表示の panel-list を描く。
- 触るとき: ストーリーでパネルの表示位置や常時表示の条件を変えるとき。
- 呼び出し先: `html()`
