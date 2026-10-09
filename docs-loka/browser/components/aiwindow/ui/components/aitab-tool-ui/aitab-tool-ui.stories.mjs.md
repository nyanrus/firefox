# browser/components/aiwindow/ui/components/aitab-tool-ui/aitab-tool-ui.stories.mjs

source: browser/components/aiwindow/ui/components/aitab-tool-ui/aitab-tool-ui.stories.mjs
source-hash: 11451a70e8acbb2f98324b6882142440a7e086e7
lines: 73

## <module>
- 役割: aitab-tool-ui の Storybook 用ストーリーを定義し、作成中・選択・完了の各状態を並べるモジュール。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L35-44
- 役割: state・title・viewerURL・completeStateOpen を aitab-tool-ui に渡し、幅360pxの枠の中に描く。
- 触るとき: ストーリーの表示幅や渡すプロパティを変えるとき。viewerURL は要素側に宣言が無いので、渡しても効かない点に注意する。
- 呼び出し先: `html()`
