# browser/components/aiwindow/ui/components/aitab-page/aitab-error/aitab-error.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-error/aitab-error.mjs
source-hash: 2f03f94424a98ada715ed8ad46ddd16252bbd36f
lines: 46

## <module>
- 役割: 利用できなくなった AI Tab ページの案内 aitab-error を定義する
- 呼び出し先: `customElements.define()`

## AITabError.render()
- 位置: L12-42
- 役割: 案内画像と見出し・説明文を翻訳 ID 付きで描画する
- 触るとき: エラー画面の構成や data-l10n-id を変えるとき。文言そのものは Fluent 側にある。
- 呼び出し先: `html()`
