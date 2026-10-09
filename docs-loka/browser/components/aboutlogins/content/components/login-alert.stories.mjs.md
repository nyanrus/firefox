# browser/components/aboutlogins/content/components/login-alert.stories.mjs

source: browser/components/aboutlogins/content/components/login-alert.stories.mjs
source-hash: 66e6a0ecd39dc66f328e68b13a75cebce5777975
lines: 74

## <module>
- 役割: login-alert と警告カードの Storybook 用の見本(ストーリー)を定義する。
- 呼び出し先: `window.MozXULElement.insertFTLIfNeeded()`

## BasicLoginAlert()
- 位置: L16-29
- 役割: variant と icon を引数に、login-alert の基本形(操作リンクと補足文)を描画する Storybook 用の見本。
- 触るとき: login-alert の見た目を Storybook で確かめるとき。
- 呼び出し先: `html()`

## VulnerablePasswordAlert()
- 位置: L50-54
- 役割: hostname を渡した脆弱パスワード警告の Storybook 用の見本。
- 触るとき: 脆弱パスワード警告の見た目を Storybook で確かめるとき。
- 呼び出し先: `html()`

## LoginBreachAlert()
- 位置: L60-62
- 役割: date と hostname を渡した侵害警告の Storybook 用の見本。
- 触るとき: 侵害警告の見た目を Storybook で確かめるとき。
- 呼び出し先: `html()`
