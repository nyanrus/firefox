# browser/components/preferences/widgets/setting-pane/setting-pane.mjs

source: browser/components/preferences/widgets/setting-pane/setting-pane.mjs
source-hash: a76f9e0a180bdbe9807271107258f6d35b3146c6
lines: 246

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## shouldGoBackToParent()
- 位置: L26-34
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `win.history.state?.previousCategory`, `win.navigation?.canGoBack`

## SettingPane.pageHeaderEl()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## SettingPane.paneId()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.config.id`

## SettingPane.constructor()
- 位置: L70-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.config`, `this.initialized`, `this.isSubPane`, `this.name`, `this.onSearchPane`

## SettingPane.createRenderRoot()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)

## SettingPane.getUpdateComplete()
- 位置: async L92-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.getUpdateComplete()`
- 参照: `this.pageHeaderEl.updateComplete`

## SettingPane.goBack()
- 位置: L98-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `shouldGoBackToParent()`, `window.gotoPref()`
- 条件付き依存: `if (shouldGoBackToParent(window, this.config.parent))` → `window.history.back()`
- 参照: `this.config.parent`

## SettingPane.handleVisibility()
- 位置: L106-123
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.config.visible)` → `this.config.visible()`
- 条件付き依存: `if (this.config.visible)` → `document.querySelector()`
- 条件付き依存: `if (categoryButton)` → `categoryButton.remove()`
- 条件付き依存: `if (!visible && !this.isSubPane)` → `this.remove()`
- 参照: `categoryButton.hidden`, `this.config.visible`, `this.isSubPane`, `this.name`

## SettingPane.connectedCallback()
- 位置: L125-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `super.connectedCallback()`, `this.handleVisibility()`, `this.setAttribute()`
- 条件付き依存: `if (this.isSubPane)` → `this.setAttribute()`
- 条件付き依存: `if (this.isSubPane)` → `this._createCategoryButton()`
- 参照: `this.handlePaneShown`, `this.hidden`, `this.isSubPane`, `this.name`

## SettingPane.disconnectedCallback()
- 位置: L141-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.removeEventListener()`, `super.disconnectedCallback()`
- 参照: `this.handlePaneShown`

## SettingPane.handlePaneShown()
- 位置: L149-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contains()`
- 条件付き依存: `if ( this.isSubPane && e.detail.category === this.name && !this.contains(document.activeElement) )` → `this.pageHeaderEl.backButtonEl.focus()`
- 参照: `document.activeElement`, `e.detail.category`, `this.isSubPane`, `this.name`

## SettingPane.init()
- 位置: L166-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `SettingGroupManager.has()`, `SettingPaneManager.importPane()`
- 条件付き依存: `if (!this.initialized)` → `this.performUpdate()`
- 条件付き依存: `if (SettingGroupManager.has(groupId))` → `window.initSettingGroup()`
- 参照: `this.config.groupIds`, `this.config.id`, `this.initialized`, `this.paneId`
- XPCOM: `Services.obs`

## SettingPane._createCategoryButton()
- 位置: L192-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `categoryButton.setAttribute()`, `document.createElement()`, `document.getElementById()`, `document.getElementById("categories").append()`
- 条件付き依存: `if (this.isSubPane)` → `categoryButton.classList.add()`
- 参照: `this.isSubPane`, `this.name`

## SettingPane.groupTemplate()
- 位置: L202-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.isSubPane`

## SettingPane.breadcrumbsTemplate()
- 位置: L209-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SettingPaneManager.getWithParents()`, `SettingPaneManager.getWithParents(this.paneId).map()`, `html()`
- 参照: `config.id`, `config.l10nId`, `this.isSubPane`, `this.paneId`

## SettingPane.render()
- 位置: L224-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.breadcrumbsTemplate()`, `this.config.groupIds.map()`, `this.groupTemplate()`
- 参照: `this.config.badge`, `this.config.iconSrc`, `this.config.l10nId`, `this.config.supportPage`, `this.goBack`, `this.initialized`, `this.isSubPane`, `this.onSearchPane`
