# browser/components/asrouter/content-src/lib/addUtmParams.mjs

source: browser/components/asrouter/content-src/lib/addUtmParams.mjs
source-hash: a816a1a7cc7db733c616eea8fe6542aba0317557
lines: 35

## <module>
- 役割: ASRouter のメッセージ内リンクに付ける UTM 計測パラメータの既定値と、それを URL に加える関数。

## addUtmParams()
- 位置: L20-34
- 役割: URL に utm_source・utm_campaign・utm_medium(未設定のもの)と utm_term を追加して URL オブジェクトを返す。
- 触るとき: リンクの計測パラメータを変えるとき、または既に付いた utm 値が上書きされない理由を調べるとき。
- 呼び出し先: `Object.entries()`, `returnUrl.searchParams.has()`
- 条件付き依存: `if (!returnUrl.searchParams.has(key))` → `returnUrl.searchParams.append()`
- 条件付き依存: `if (!returnUrl.searchParams.has("utm_term"))` → `returnUrl.searchParams.append()`
