# browser/components/preferences/config/containers.mjs

source: browser/components/preferences/config/containers.mjs
source-hash: ecd46c8cd4763c859476012c6a02c0e60a0c0e07
lines: 425

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/network/idn-service;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Glean.containers.manageContainersOpened.record()`, `Preferences.addAll()`, `Preferences.addSetting()`, `SettingGroupManager.registerGroups()`, `URL.fromURI()`, `URL.fromURI(document.documentURIObject).searchParams.get()`, `document.addEventListener()`

## siteContainersEnabled()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## openContainerDialog()
- 位置: L69-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSubDialog.open()`
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.getPublicIdentityFromId()`
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.getUserContextLabel()`
- 参照: `identity.name`, `identity.userContextId`, `lazy.ContextualIdentityService.containerColors`, `lazy.ContextualIdentityService.containerIcons`

## openSiteContainerDialog()
- 位置: L89-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSubDialog.open()`

## removeContainer()
- 位置: async L95-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.countContainerTabs()`, `lazy.ContextualIdentityService.remove()`
- 条件付き依存: `if (count > 0)` → `document.l10n.formatValues()`
- 条件付き依存: `if (count > 0)` → `Services.prompt.confirmEx()`
- 条件付き依存: `if (count > 0)` → `lazy.ContextualIdentityService.closeContainerTabs()`
- 参照: `Ci.nsIPrompt.BUTTON_POS_0`, `Ci.nsIPrompt.BUTTON_POS_1`, `Ci.nsIPrompt.BUTTON_TITLE_IS_STRING`
- XPCOM: [`nsIPrompt`](../../../../netwerk/base/nsIAuthPrompt.idl.md) / `Services.prompt`

## beforeRefresh()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.getPublicIdentities()`
- 参照: `this.containers`

## getControlConfig()
- 位置: async L139-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.getContainerIconURL()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `this.containers.map()`
- 参照: `container.color`, `container.icon`, `container.userContextId`

## onUserReorder()
- 位置: L183-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `draggedElement.getAttribute()`, `lazy.ContextualIdentityService.move()`, `parseInt()`
- 参照: `event.detail`

## onUserClick()
- 位置: async L189-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.getAttribute()`, `parseInt()`
- 条件付き依存: `if (action === "edit")` → `openContainerDialog()`
- 条件付き依存: `if (action === "remove")` → `removeContainer()`

## setup()
- 位置: L199-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs`

## onUserClick()
- 位置: L214-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.containers.addContainerClicked.record()`, `openContainerDialog()`

## beforeRefresh()
- 位置: L236-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.getPublicIdentities()`
- 参照: `this.containers`

## visible()
- 位置: async L240-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `siteContainersEnabled()`

## disabled()
- 位置: async L244-246
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.containers.length`

## onUserClick()
- 位置: L248-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openSiteContainerDialog()`

## setup()
- 位置: L252-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs` / `Services.prefs`

## beforeRefresh()
- 位置: L280-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.displaySite.localeCompare()`, `containerOptions()`, `lazy.ContextualIdentityService.getSiteAssociations()`, `lazy.ContextualIdentityService.getSiteAssociations() .map()`, `lazy.idnService.domainToDisplay()`
- 参照: `b.displaySite`, `this.associations`, `this.containers`

## visible()
- 位置: async L291-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `siteContainersEnabled()`
- 参照: `this.associations.length`

## getControlConfig()
- 位置: async L295-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `this.#itemConfig()`, `this.associations.map()`

## #itemConfig()
- 位置: async L302-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `document.l10n.formatValues()`, `this.containers.map()`
- 参照: `attrs.value`

## onUserClick()
- 位置: L347-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.getAttribute()`, `lazy.ContextualIdentityService.removeSiteAssociation()`

## setup()
- 位置: L356-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs` / `Services.prefs`
