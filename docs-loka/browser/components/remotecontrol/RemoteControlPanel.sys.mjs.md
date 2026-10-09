# browser/components/remotecontrol/RemoteControlPanel.sys.mjs

source: browser/components/remotecontrol/RemoteControlPanel.sys.mjs
source-hash: 9b308570ba5a674d86bf8e767746b0289c4ff057
lines: 209

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `RemoteControlPanel.onPrefChange()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## RemoteControlPanelClass.constructor()
- 位置: L43-47
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#initialized`, `this.#serversAlreadyStarted`, `this.#toggling`

## RemoteControlPanelClass.init()
- 位置: L49-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onPrefChange()`
- 参照: `lazy.RemoteControlServers.enabled`, `this.#initialized`, `this.#serversAlreadyStarted`

## RemoteControlPanelClass.uninit()
- 位置: L63-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.destroyWidget()`, `lazy.RemoteControlServers.removeListener()`
- 参照: `this.#initialized`, `this.#onServersChanged`, `this.#serversAlreadyStarted`

## RemoteControlPanelClass.onPrefChange()
- 位置: L78-107
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.dynamicStartEnabled)` → `lazy.CustomizableUI.createWidget()`
- 条件付き依存: `if (lazy.dynamicStartEnabled)` → `lazy.RemoteControlServers.addListener()`
- 条件付き依存: `if (!(lazy.dynamicStartEnabled))` → `lazy.CustomizableUI.destroyWidget()`
- 条件付き依存: `if (!(lazy.dynamicStartEnabled))` → `lazy.RemoteControlServers.removeListener()`
- 参照: `AppConstants.ENABLE_WEBDRIVER`, `AppConstants.NIGHTLY_BUILD`, `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.dynamicStartEnabled`, `this.#initialized`, `this.#onServersChanged`, `this.#serversAlreadyStarted`

## onCreated()
- 位置: L95-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.setAttribute()`, `this.#updateButton()`

## onViewShowing()
- 位置: L99-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onViewShowing()`

## onViewHiding()
- 位置: L100-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onViewHiding()`

## RemoteControlPanelClass.handleEvent()
- 位置: L109-113
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target.id == `${VIEW_ID}-toggle-button`)` → `this.#onToggleCommand()`
- 参照: `event.target.id`

## RemoteControlPanelClass.#onServersChanged()
- 位置: L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateAllWindows()`

## RemoteControlPanelClass.#onToggleCommand()
- 位置: async L119-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#updateAllWindows()`
- 条件付き依存: `if (lazy.RemoteControlServers.runningDynamically)` → `lazy.RemoteControlServers.stop()`
- 条件付き依存: `if (!(lazy.RemoteControlServers.runningDynamically))` → `lazy.RemoteControlServers.start()`
- 参照: `lazy.RemoteControlServers.runningDynamically`, `this.#toggling`

## RemoteControlPanelClass.#onViewHiding()
- 位置: L146-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.removeEventListener()`

## RemoteControlPanelClass.#onViewShowing()
- 位置: L150-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelview.addEventListener()`, `this.#updatePanel()`
- 参照: `event.target`

## RemoteControlPanelClass.#updateAllWindows()
- 位置: L156-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getWidget()`
- 条件付き依存: `if (widget)` → `this.#updateButton()`
- 条件付き依存: `if (widget)` → `node.ownerDocument.getElementById()`
- 条件付き依存: `if (panelview)` → `this.#updatePanel()`
- 参照: `widget.instances`

## RemoteControlPanelClass.#updateButton()
- 位置: L170-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.ownerDocument.l10n.setAttributes()`, `node.toggleAttribute()`
- 参照: `lazy.RemoteControlServers.runningDynamically`

## RemoteControlPanelClass.#updatePanel()
- 位置: L186-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelview.ownerDocument.l10n.setAttributes()`, `panelview.querySelector()`, `panelview.toggleAttribute()`
- 参照: `lazy.RemoteControlServers.runningDynamically`, `this.#toggling`, `toggleButton.disabled`
