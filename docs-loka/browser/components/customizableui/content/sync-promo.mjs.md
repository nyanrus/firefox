# browser/components/customizableui/content/sync-promo.mjs

source: browser/components/customizableui/content/sync-promo.mjs
source-hash: ab21f695c6812105fad6418242c7706d99f6d044
lines: 184

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`, `window.MozXULElement?.insertFTLIfNeeded()`

## SyncPromo.constructor()
- 位置: L74-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.disconnectedCallback.bind()`
- 参照: `this._promoState`, `this.disconnectedCallback`, `this.promoType`

## SyncPromo.#onViewShowing()
- 位置: L82-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#refresh()`

## observe()
- 位置: L85-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#refresh()`

## SyncPromo.#dismissedPrefBranch()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.promoType`

## SyncPromo.connectedCallback()
- 位置: L91-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `super.connectedCallback()`, `this.#panelview?.addEventListener()`, `this.#refresh()`, `this.closest()`, `window.addEventListener()`
- 参照: `this.#dismissedPrefBranch`, `this.#observer`, `this.#onViewShowing`, `this.#panelview`, `this.disconnectedCallback`
- XPCOM: `Services.obs` / `Services.prefs`

## SyncPromo.disconnectedCallback()
- 位置: L106-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `super.disconnectedCallback()`, `this.#panelview?.removeEventListener()`, `window.removeEventListener()`
- 参照: `this.#dismissedPrefBranch`, `this.#observer`, `this.#onViewShowing`, `this.#panelview`, `this.disconnectedCallback`
- XPCOM: `Services.obs` / `Services.prefs`

## SyncPromo.#config()
- 位置: L116-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.promoType`

## SyncPromo.#dismissedPref()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#dismissedPrefBranch`

## SyncPromo.#refresh()
- 位置: L124-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.#dismissedPref()`, `window.gSync?.getSyncPromoState()`
- 参照: `this._promoState`, `this.hidden`
- XPCOM: `Services.prefs`

## SyncPromo.#onDismiss()
- 位置: L136-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `event.preventDefault()`, `this.#dismissedPref()`, `this.#refresh()`
- 参照: `this._promoState`
- XPCOM: `Services.prefs`

## SyncPromo.#onCta()
- 位置: L142-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `window.CustomizableUI.hidePanelForNode()`, `window.gSync.handleSyncPromoAction()`
- 参照: `this.#config.entryPoint`, `this._promoState`

## SyncPromo.render()
- 位置: L153-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#config.variants`, `this.#onCta`, `this.#onDismiss`, `this._promoState`, `variant.cta`, `variant.heading`, `variant.image`
