# browser/components/aiwindow/ui/components/smartwindow-history-menu/smartwindow-history-menu.stories.mjs

source: browser/components/aiwindow/ui/components/smartwindow-history-menu/smartwindow-history-menu.stories.mjs
source-hash: 29ffe03b877ec243928111675281aecdd0af65e8
lines: 66

## <module>
- 役割: smartwindow-history-menu の Storybook 用ストーリーを定義し、サイドバーとフルページの表示例を並べるモジュール。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L42-49
- 役割: mode と recentChats を smartwindow-history-menu に渡し、周囲に余白を取った枠の中に描く。
- 触るとき: ストーリーの表示モードや例のチャット一覧を変えるとき。
- 呼び出し先: `html()`
