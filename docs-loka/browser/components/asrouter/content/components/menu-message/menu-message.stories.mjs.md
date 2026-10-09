# browser/components/asrouter/content/components/menu-message/menu-message.stories.mjs

source: browser/components/asrouter/content/components/menu-message/menu-message.stories.mjs
source-hash: 62eacedf0c2a9047e01f081eb1f99edb58668f34
lines: 104

## <module>
- 役割: menu-message 要素の Storybook 定義。column、split などのレイアウト例とオフセット調整用の引数を用意する。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L25-70
- 役割: menu-message を moz-card に入れ、オフセットや幅の引数を style の CSS 変数に変換して描画するテンプレート。
- 触るとき: ストーリーの見た目の調整項目を増やすとき。
- 呼び出し先: `html()`
