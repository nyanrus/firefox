# browser/components/sidebar/sidebar-panel-header.mjs

source: browser/components/sidebar/sidebar-panel-header.mjs
source-hash: 42ac90c4ffae582188937a86274b38191c3f1bd2
lines: 64

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SidebarPanelHeader.getWindow()
- 位置: L29-31
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext.embedderWindowGlobal.browsingContext.window`

## SidebarPanelHeader.closeSidebarPanel()
- 位置: L33-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.hide()`, `e.preventDefault()`, `this.getWindow()`
- 参照: `controller._state.launcherHiddenWithPanel`, `this.getWindow().SidebarController`

## SidebarPanelHeader.render()
- 位置: L43-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.closeSidebarPanel`, `this.heading`, `this.view`
