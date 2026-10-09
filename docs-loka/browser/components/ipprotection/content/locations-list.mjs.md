# browser/components/ipprotection/content/locations-list.mjs

source: browser/components/ipprotection/content/locations-list.mjs
source-hash: 2cbb3a9679658e0bb00d56c375346c32a67fa724
lines: 205

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## LocationsList.#sortedLocations()
- 位置: L24-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `LocationsList.collator.compare()`, `countryName()`, `locations.sort()`
- 条件付き依存: `if (!this.premium)` → `locations.filter()`
- 参照: `a.code`, `aLocation.locked`, `b.code`, `this.locations`, `this.premium`

## LocationsList.#renderedLocations()
- 位置: L40-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `LocationsList.defaultLocation`, `this.#sortedLocations`

## LocationsList.#focusableLocation()
- 位置: L57-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderedLocations.some()`, `this.getSelectedLocation()`
- 参照: `aLocation.code`, `this.focusedLocation`

## LocationsList.constructor()
- 位置: L66-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.focusedLocation`, `this.locations`, `this.premium`, `this.selectedLocation`

## LocationsList.createRenderRoot()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)

## LocationsList.connectedCallback()
- 位置: L78-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`
- 参照: `this.focusedLocation`

## LocationsList.getSelectedLocation()
- 位置: L88-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.locations?.find()`
- 参照: `LocationsList.defaultLocation`, `l.code`, `selected?.locked`, `this.premium`, `this.selectedLocation`

## LocationsList.handleSelectLocation()
- 位置: L102-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `selectedLocation.available`, `selectedLocation.code`, `this.selectedLocation`

## LocationsList.#handleOptionKeydown()
- 位置: L119-124
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key === "Enter" || event.key === " ")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Enter" || event.key === " ")` → `this.handleSelectLocation()`
- 参照: `event.key`

## LocationsList.#handleOptionFocus()
- 位置: L126-128
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aLocation.code`, `this.focusedLocation`

## LocationsList.#locationRow()
- 位置: L130-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `countryName()`, `html()`, `this.#handleOptionFocus()`, `this.#handleOptionKeydown()`, `this.getSelectedLocation()`, `this.handleSelectLocation()`
- 参照: `LocationsList.defaultLocation`, `aLocation.available`, `aLocation.code`

## LocationsList.render()
- 位置: L181-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#focusableLocation()`, `this.#locationRow()`, `this.#renderedLocations.map()`
