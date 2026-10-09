# browser/components/syncedtabs/SyncedTabsDeckView.sys.mjs

source: browser/components/syncedtabs/SyncedTabsDeckView.sys.mjs
source-hash: aacae71fa57faf757fc031677aa475ebe056f245
lines: 91

## <module>
- 役割: (未記入)

## SyncedTabsDeckView()
- 位置: L13-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._doc.createElement()`, `this._doc.getElementById()`
- 参照: `this._deckTemplate`, `this._doc`, `this._tabListComponent`, `this._window`, `this.container`, `this.props`, `window.document`

## render()
- 位置: L25-31
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (state.isUpdatable)` → `this.update()`
- 条件付き依存: `if (!(state.isUpdatable))` → `this.create()`
- 参照: `state.isUpdatable`

## create()
- 位置: L33-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deck.appendChild()`, `tabListWrapper.appendChild()`, `this._attachListeners()`, `this._clearChilden()`, `this._doc.createElement()`, `this._doc.importNode()`, `this._tabListComponent.init()`, `this.container.appendChild()`, `this.update()`
- 参照: `tabListWrapper.className`, `this._deckTemplate.content`, `this._doc.importNode( this._deckTemplate.content, true ).firstElementChild`, `this._tabListComponent.container`

## destroy()
- 位置: L51-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabListComponent.uninit()`, `this.container.remove()`

## update()
- 位置: L56-73
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (panel.selected)` → `Array.prototype.map.call()`
- 条件付き依存: `if (panel.selected)` → `this._doc.getElementsByClassName()`
- 条件付き依存: `if (panel.selected)` → `item.classList.add()`
- 条件付き依存: `if (!(panel.selected))` → `Array.prototype.map.call()`
- 条件付き依存: `if (!(panel.selected))` → `this._doc.getElementsByClassName()`
- 条件付き依存: `if (!(panel.selected))` → `item.classList.remove()`
- 参照: `panel.id`, `panel.selected`, `state.panels`

## _clearChilden()
- 位置: L75-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.container.firstChild.remove()`
- 参照: `this.container.firstChild`

## _attachListeners()
- 位置: L81-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `link.addEventListener()`, `this.container .querySelector()`, `this.container .querySelector(".connect-device") .addEventListener()`, `this.container.querySelectorAll()`
- 参照: `this.props.onConnectDeviceClick`, `this.props.onSyncPrefClick`
