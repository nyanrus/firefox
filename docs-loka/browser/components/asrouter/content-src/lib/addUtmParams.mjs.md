# browser/components/asrouter/content-src/lib/addUtmParams.mjs

source: browser/components/asrouter/content-src/lib/addUtmParams.mjs
source-hash: a816a1a7cc7db733c616eea8fe6542aba0317557
lines: 35

## <module>
- 役割: (未記入)

## addUtmParams()
- 位置: L20-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `returnUrl.searchParams.has()`
- 条件付き依存: `if (!returnUrl.searchParams.has(key))` → `returnUrl.searchParams.append()`
- 条件付き依存: `if (!returnUrl.searchParams.has("utm_term"))` → `returnUrl.searchParams.append()`
