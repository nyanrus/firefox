# browser/components/aiwindow/ui/components/agent-monitor-item/agent-monitor-item.stories.mjs

source: browser/components/aiwindow/ui/components/agent-monitor-item/agent-monitor-item.stories.mjs
source-hash: a34534f503e194671a76fad3852f62ff6f6ca764
lines: 150

## <module>
- 役割: agent-monitor-item の Storybook 定義。表示、展開、編集、作成、失敗履歴の各状態を見せるためのサンプルを並べる。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L51-61
- 役割: agent と各種フラグを agent-monitor-item に渡して、幅 416px の枠の中に描画する。
- 触るとき: Storybook の見た目を確かめるときや、カードに渡す属性を増やすときに見る。
- 呼び出し先: `html()`
