# browser/components/protections/content/privacy-metrics-card.mjs

source: browser/components/protections/content/privacy-metrics-card.mjs
source-hash: e617c9e206db3375f0443a2250e08623dcfff82c
lines: 199

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## PrivacyMetricsCard.constructor()
- 位置: L51-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._error`, `this._isPrivate`, `this._loading`, `this.cookies`, `this.fingerprinters`, `this.socialTrackers`, `this.total`, `this.trackers`

## PrivacyMetricsCard.connectedCallback()
- 位置: async L63-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.#fetchStats()`

## PrivacyMetricsCard.#fetchStats()
- 位置: async L68-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `console.error()`
- 参照: `stats.cookies`, `stats.fingerprinters`, `stats.socialTrackers`, `stats.total`, `stats.trackers`, `stats?.isPrivate`, `this._error`, `this._isPrivate`, `this._loading`, `this.cookies`, `this.fingerprinters`, `this.isConnected`, `this.socialTrackers`, `this.total`, `this.trackers`

## PrivacyMetricsCard.#renderLoading()
- 位置: L98-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## PrivacyMetricsCard.#renderError()
- 位置: L106-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## PrivacyMetricsCard.#renderPrivateWindow()
- 位置: L114-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## PrivacyMetricsCard.#renderCategories()
- 位置: L122-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `[...CATEGORIES].sort()`, `html()`, `sorted.map()`
- 参照: `a.prop`, `b.prop`, `cat.icon`, `cat.key`, `cat.l10nId`, `cat.prop`

## PrivacyMetricsCard.#renderContent()
- 位置: L142-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#renderCategories()`
- 条件付き依存: `if (this._loading)` → `this.#renderLoading()`
- 条件付き依存: `if (this._isPrivate)` → `this.#renderPrivateWindow()`
- 条件付き依存: `if (this._error)` → `this.#renderError()`
- 条件付き依存: `if (this.total === 0)` → `html()`
- 条件付き依存: `if (this.total === 0)` → `this.#renderCategories()`
- 参照: `this._error`, `this._isPrivate`, `this._loading`, `this.total`

## PrivacyMetricsCard.render()
- 位置: L170-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderContent()`
