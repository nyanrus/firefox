# browser/extensions/newtab/lib/AboutPreferences.sys.mjs

source: browser/extensions/newtab/lib/AboutPreferences.sys.mjs
source-hash: 4564a2107f110b54cf766e969627d0f1e2adad50
lines: 699

## <module>
- 役割: (未記入)

## widgetLabels()
- 位置: L27-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `messages[i]?.attributes?.find()`, `strings.formatMessagesSync()`, `widgets.map()`
- 参照: `attr.name`, `messages[i]?.attributes?.find(attr => attr.name === "label")?.value`, `w.id`, `w.prefsL10nId`

## AboutPreferences.init()
- 位置: L50-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## AboutPreferences.uninit()
- 位置: L55-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## AboutPreferences.onAction()
- 位置: L60-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action._target.window.BrowserAddonUI.openAddonsMgr()`, `action._target.window.openPreferences()`, `encodeURIComponent()`, `this.init()`, `this.uninit()`
- 参照: `action.data`, `action.type`, `at.INIT`, `at.OPEN_ABOUT_ADDONS_THEMES`, `at.OPEN_WEBEXT_SETTINGS`, `at.SETTINGS_OPEN`, `at.UNINIT`

## AboutPreferences.observe()
- 位置: L86-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SettingGroupManager.get()`, `SettingGroupManager.registerGroups()`, `this._registerPreferences()`, `this._setupHomeGroup()`, `window.MozXULElement.insertFTLIfNeeded()`

## AboutPreferences._registerPreferences()
- 位置: L122-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.addAll()`, `WIDGET_REGISTRY.filter()`, `WIDGET_REGISTRY.filter(w => !w.retired).flatMap()`
- 参照: `w.enabledPref`, `w.retired`, `w.systemEnabledPref`

## AboutPreferences._setupHomeGroup()
- 位置: L218-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(labels.get(a.id) ?? a.id).localeCompare()`, `Preferences.addSetting()`, `Services.prefs.getBoolPref()`, `WIDGET_REGISTRY.filter()`, `WIDGET_REGISTRY.find()`, `[...prefsWidgets].sort()`, `isWidgetsContainerVisible()`, `labels.get()`, `sortedWidgets .filter()`, `sortedWidgets .filter(w => weatherNested || w.id !== "weather") .map()`, `this.store.getState()`, `widgetLabels()`, `widgetToggleVisible()`
- 条件付き依存: `if (novaEnabled)` → `Preferences.addSetting()`
- 条件付き依存: `if (novaEnabled)` → `widgetToggleVisible()`
- 条件付き依存: `if (!(novaEnabled))` → `Preferences.addSetting()`
- 参照: `a.id`, `b.id`, `this.store.getState()?.Prefs?.values`, `w.id`, `w.retired`, `weatherWidget.enabledPref`, `weatherWidget.prefsL10nId`, `weatherWidget.trainhopEnabledKey`, `widget.enabledPref`, `widget.id`, `widget.systemEnabledPref`, `widget.trainhopEnabledKey`
- XPCOM: `Services.prefs`

## widgetToggleVisible()
- 位置: L227-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isWidgetToggleVisible()`
- 参照: `deps[widget.trainhopEnabledKey]?.value`, `widget.systemEnabledPref`, `widget.trainhopEnabledKey`

## firefoxHomeActive()
- 位置: L241-242
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `homepageNewTabs.value`, `homepageNewWindows.value`

## dispatchForHomeLink()
- 位置: L248-249
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `homepageNewTabs.value`

## visible()
- 位置: L254-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## disabled()
- 位置: L270-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## disabled()
- 位置: L279-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## visible()
- 位置: L292-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isWidgetsContainerVisible()`
- 参照: `widgetsEnabled.value`

## disabled()
- 位置: L297-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## disabled()
- 位置: L325-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## visible()
- 位置: L337-337
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `showWeather.value`

## disabled()
- 位置: L338-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## disabled()
- 位置: L347-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## visible()
- 位置: L365-365
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `systemTopstories.value`

## disabled()
- 位置: L366-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## visible()
- 位置: L396-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`
- 参照: `sectionsCustomizeMenuPanelEnabled.value`, `sectionsEnabled.value`, `sectionsPersonalizationEnabled.value`, `stories.value`

## onUserClick()
- 位置: L411-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchForHomeLink()`, `e.preventDefault()`, `window.openTrustedLinkIn()`

## disabled()
- 位置: L425-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## AboutPreferences.onUserChange()
- 位置: L426-430
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `sponsoredShortcuts.value`, `sponsoredStories.value`

## disabled()
- 位置: L440-440
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `topsitesEnabled.value`

## visible()
- 位置: L446-446
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `systemTopstories.value`

## disabled()
- 位置: L447-447
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `stories.value`

## disabled()
- 位置: L461-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## visible()
- 位置: L485-485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxHomeActive()`

## onUserClick()
- 位置: L486-489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchForHomeLink()`, `e.preventDefault()`, `window.openTrustedLinkIn()`
