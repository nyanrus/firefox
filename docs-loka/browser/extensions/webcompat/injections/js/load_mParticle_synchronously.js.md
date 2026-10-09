# browser/extensions/webcompat/injections/js/load_mParticle_synchronously.js

source: browser/extensions/webcompat/injections/js/load_mParticle_synchronously.js
source-hash: ab24e0d6d29547f690a3e8c362b3205e707aeadb
lines: 37

## <module>
- 役割: (未記入)
- 呼び出し先: `(function () { const s = document.createElement("script"); s.async = true; s.src = "mparticle.js"; return s.async; })()`, `document.createElement()`

## desc.set()
- 位置: L26-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `origSet.call()`, `url?.includes()`
- 参照: `this.async`
