# browser/components/aiwindow/ui/components/input-cta/input-cta.stories.mjs

source: browser/components/aiwindow/ui/components/input-cta/input-cta.stories.mjs
source-hash: f377a2f43776b39ff9d0d13b641317920a871ea6
lines: 74

## <module>
- 役割: input-cta の Storybook 用ストーリーを定義し、action ごとの送信ボタンと検索エンジン一覧の例を並べるモジュール。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L40-46
- 役割: action・検索エンジン情報・検索エンジン一覧を input-cta の プロパティに渡して描く。
- 触るとき: ストーリーに渡す値を増やすとき、または action ごとの表示を比べたいとき。
- 呼び出し先: `html()`
