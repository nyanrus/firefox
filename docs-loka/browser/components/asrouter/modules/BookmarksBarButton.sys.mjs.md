# browser/components/asrouter/modules/BookmarksBarButton.sys.mjs

source: browser/components/asrouter/modules/BookmarksBarButton.sys.mjs
source-hash: f7d10657993dc47382262ec08c9cb7d49a843d38
lines: 129

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## showBookmarksBarButton()
- 位置: async L18-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.CustomizableUI.addListener()`, `lazy.CustomizableUI.createWidget()`
- 条件付き依存: `if (expiry_ms)` → `parseInt()`
- 条件付き依存: `if (expiry_ms)` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (expiry_ms)` → `Date.now()`
- 条件付き依存: `if (shownAt && Date.now() - shownAt > expiry_ms)` → `lazy.CustomizableUI.destroyWidget()`
- 参照: `browser.documentGlobal`, `label?.raw`, `label?.string_id`, `label?.tooltiptext`, `lazy.CustomizableUI.AREA_BOOKMARKS`, `message.content`
- XPCOM: `Services.prefs`

## handleExperimentUpdate()
- 位置: L46-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `lazy.NimbusFeatures[featureId].getAllVariables()`
- 条件付き依存: `if (!Object.keys(value).length)` → `lazy.CustomizableUI.removeWidgetFromArea()`
- 参照: `Object.keys(value).length`, `lazy.NimbusFeatures`

## onCreated()
- 位置: L54-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `lazy.ASRouter.addImpression()`, `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `lazy.NimbusFeatures[featureId].onUpdate()`, `parseInt()`
- 条件付き依存: `if (!shownAt)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!shownAt)` → `String()`
- 条件付き依存: `if (!shownAt)` → `Date.now()`
- 参照: `aNode.className`, `aNode.style.listStyleImage`, `lazy.CustomizableUI.AREA_BOOKMARKS`, `lazy.NimbusFeatures`, `logo.imageURL`, `logo?.imageURL`, `this.handleExperimentUpdate`
- XPCOM: `Services.prefs`

## onCommand()
- 位置: L79-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `supportedActions.includes()`
- 条件付き依存: `if (supportedActions.includes(action.type))` → `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if (supportedActions.includes(action.type))` → `action.data.actions.every()`
- 条件付き依存: `if (supportedActions.includes(action.type))` → `supportedActions.includes()`
- 条件付き依存: `if ( action.data.actions.every(iAction => supportedActions.includes(iAction.type) ) )` → `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if (action.navigate || action.dismiss)` → `lazy.CustomizableUI.destroyWidget()`
- 参照: `action.dismiss`, `action.navigate`, `action.type`, `iAction.type`

## onWidgetRemoved()
- 位置: L105-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.destroyWidget()`

## onDestroyed()
- 位置: L109-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `lazy.CustomizableUI.removeListener()`
