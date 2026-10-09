# browser/modules/FilterAdult.sys.mjs

source: browser/modules/FilterAdult.sys.mjs
source-hash: e72ccd3f030f9c69e08c9702b51ad2e8a32a3e5e
lines: 69

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## _FilterAdult.constructor()
- 位置: L20-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FilterAdultComponent.init()`
- 参照: `this.#comp`

## _FilterAdult.filter()
- 位置: L32-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `links.filter()`, `this.#comp.contains()`
- 参照: `lazy.gFilterAdultEnabled`
- XPCOM: `Services.eTLD` / `Services.io`

## _FilterAdult.isAdultUrl()
- 位置: L55-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `this.#comp.contains()`
- 参照: `lazy.gFilterAdultEnabled`
- XPCOM: `Services.eTLD` / `Services.io`
