# browser/modules/PageActions.sys.mjs

source: browser/modules/PageActions.sys.mjs
source-hash: 6014ddbb406821a10937c2666ae7cc614e55bd16
lines: 1290

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## escapeCSSURL()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.replace()`

## init()
- 位置: L36-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allBrowserPageActions()`, `bpa.placeAllActionsInUrlbar()`, `callbacks.shift()`, `callbacks.shift()()`, `this._initBuiltInActions()`, `this._loadPersistedActions()`, `this.actionForID()`
- 条件付き依存: `if (!this.actionForID(options.id))` → `this._registerAction()`
- 条件付き依存: `if (addShutdownBlocker)` → `lazy.AsyncShutdown.profileBeforeChange.addBlocker()`
- 条件付き依存: `if (addShutdownBlocker)` → `this._purgeUnregisteredPersistedActions()`
- 参照: `callbacks.length`, `options.id`, `this._deferredAddActionCalls`

## actions()
- 位置: L85-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lists.reduce()`, `memo.concat()`
- 参照: `this._builtInActions`, `this._nonBuiltInActions`, `this._transientActions`

## actionsInPanel()
- 位置: L105-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._builtInActions.filter()`, `this._nonBuiltInActions.filter()`, `this._transientActions.filter()`
- 条件付き依存: `if (actions.length)` → `actions.push()`
- 条件付き依存: `if (nonBuiltInActions.length)` → `actions.push()`
- 条件付き依存: `if (transientActions.length)` → `actions.push()`
- 参照: `actions.length`, `nonBuiltInActions.length`, `transientActions.length`

## filter()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.shouldShowInPanel()`

## actionsInUrlbar()
- 位置: L146-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.shouldShowInUrlbar()`, `this._persistedActions.idsInUrlbar.reduce()`, `this.actionForID()`
- 条件付き依存: `if (action && action.shouldShowInUrlbar(browserWindow))` → `actions.push()`

## actionForID()
- 位置: L165-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._actionsByID.get()`

## addAction()
- 位置: L184-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allBrowserPageActions()`, `bpa.placeAction()`, `this._registerAction()`
- 条件付き依存: `if (this._deferredAddActionCalls)` → `this._deferredAddActionCalls.push()`
- 条件付き依存: `if (this._deferredAddActionCalls)` → `this.addAction()`
- 参照: `this._deferredAddActionCalls`

## _registerAction()
- 位置: L198-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._actionsByID.set()`, `this._persistedActions.ids.includes()`, `this._updateIDsPinnedToUrlbarForAction()`, `this.actionForID()`
- 条件付き依存: `if ("__insertBeforeActionID" in action)` → `this._builtInActions.findIndex()`
- 条件付き依存: `if (index < 0)` → `this._builtInActions.filter()`
- 条件付き依存: `if ("__insertBeforeActionID" in action)` → `this._builtInActions.splice()`
- 条件付き依存: `if (action.__transient)` → `this._transientActions.push()`
- 条件付き依存: `if (action._isBuiltIn)` → `this._builtInActions.push()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `lazy.BinarySearch.insertionIndexOf()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `a1.getTitle().localeCompare()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `a1.getTitle()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `a2.getTitle()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `this._nonBuiltInActions.splice()`
- 条件付き依存: `if (isNew)` → `this._persistedActions.ids.push()`
- 参照: `a.__transient`, `a.id`, `action.__insertBeforeActionID`, `action.__isSeparator`, `action.__transient`, `action._isBuiltIn`, `action._pinnedToUrlbar`, `action.id`, `this._builtInActions.filter(a => !a.__transient).length`, `this._nonBuiltInActions`

## _updateIDsPinnedToUrlbarForAction()
- 位置: L255-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._persistedActions.idsInUrlbar.indexOf()`, `this._storePersistedActions()`
- 条件付き依存: `if (index < 0)` → `this._persistedActions.idsInUrlbar.indexOf()`
- 条件付き依存: `if (index < 0)` → `this._persistedActions.idsInUrlbar.splice()`
- 条件付き依存: `if (index >= 0)` → `this._persistedActions.idsInUrlbar.splice()`
- 参照: `action.id`, `action.pinnedToUrlbar`, `this._persistedActions.idsInUrlbar.length`

## onActionRemoved()
- 位置: L286-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allBrowserPageActions()`, `bpa.removeAction()`, `list.findIndex()`, `this._actionsByID.delete()`, `this.actionForID()`
- 条件付き依存: `if (index >= 0)` → `list.splice()`
- 参照: `a.id`, `action.id`, `this._builtInActions`, `this._nonBuiltInActions`, `this._transientActions`

## onActionToggledPinnedToUrlbar()
- 位置: L317-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allBrowserPageActions()`, `bpa.placeActionInUrlbar()`, `this._updateIDsPinnedToUrlbarForAction()`, `this.actionForID()`
- 参照: `action.id`

## _reset()
- 位置: L329-335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PageActions._purgeUnregisteredPersistedActions()`
- 参照: `PageActions._actionsByID`, `PageActions._builtInActions`, `PageActions._nonBuiltInActions`, `PageActions._transientActions`

## _storePersistedActions()
- 位置: L337-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`
- 参照: `this._persistedActions`
- XPCOM: `Services.prefs`

## _loadPersistedActions()
- 位置: L342-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`, `this._migratePersistedActions()`, `this._migratePersistedActionsProton()`
- 参照: `this._persistedActions`
- XPCOM: `Services.prefs`

## _purgeUnregisteredPersistedActions()
- 位置: L368-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._persistedActions[name].filter()`, `this._storePersistedActions()`, `this.actionForID()`
- 参照: `this._persistedActions`

## _migratePersistedActions()
- 位置: L379-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this[methodName]()`
- 参照: `actions.version`

## _migratePersistedActionsTo1()
- 位置: L394-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actions.idsInUrlbar.indexOf()`, `ids.push()`
- 条件付き依存: `if (bookmarkIndex >= 0)` → `actions.idsInUrlbar.splice()`
- 条件付き依存: `if (bookmarkIndex >= 0)` → `actions.idsInUrlbar.push()`
- 参照: `actions.ids`, `actions.idsInUrlbar`

## _migratePersistedActionsProton()
- 位置: L414-430
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `actions.idsInUrlbar`, `actions.idsInUrlbarPreProton`, `actions?.idsInUrlbarPreProton`

## sendPlacedInUrlbarTrigger()
- 位置: L438-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.sendTriggerMessage()`, `lazy.setTimeout()`
- 参照: `buttonNode.hidden`, `buttonNode.id`, `buttonNode?.documentGlobal`, `lazy.ASRouter.waitForInitialized`, `param.host`, `trigger.param`, `win.gBrowser.selectedBrowser`, `win.gBrowser.selectedBrowser?.currentURI`

## Action()
- 位置: L588-668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setProperties()`, `this._createIconProperties()`
- 参照: `this._disabled`, `this._globalProps`, `this._iconProperties`, `this._iconURL`, `this._title`, `this._tooltip`, `this._wantsSubview`, `this._windowProps`

## extensionID()
- 位置: L674-676
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._extensionID`

## id()
- 位置: L681-683
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._id`

## disablePrivateBrowsing()
- 位置: L685-687
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._disablePrivateBrowsing`

## canShowInWindow()
- 位置: L693-704
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (this._extensionID)` → `WebExtensionPolicy.getByID()`
- 条件付き依存: `if (this._extensionID)` → `policy.canAccessWindow()`
- 参照: `this._extensionID`, `this.disablePrivateBrowsing`

## pinnedToUrlbar()
- 位置: L710-712
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._pinnedToUrlbar`

## pinnedToUrlbar()
- 位置: L713-719
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.pinnedToUrlbar != shown)` → `PageActions.onActionToggledPinnedToUrlbar()`
- 条件付き依存: `if (this.pinnedToUrlbar != shown)` → `this.onPinToUrlbarToggled()`
- 参照: `this._pinnedToUrlbar`, `this.pinnedToUrlbar`

## getDisabled()
- 位置: L724-726
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).disabled`

## setDisabled()
- 位置: L727-729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setProperty()`

## getIconURL()
- 位置: L735-737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).iconURL`

## setIconURL()
- 位置: L738-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._createIconProperties()`, `this._getProperties()`, `this._updateProperty()`
- 参照: `props.iconProps`, `props.iconURL`

## getIconProperties()
- 位置: L751-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).iconProps`

## _createIconProperties()
- 位置: L755-774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.freeze()`, `escapeCSSURL()`
- 条件付き依存: `if (urls && typeof urls == "object")` → `this._iconProperties.get()`
- 条件付き依存: `if (!props)` → `Object.freeze()`
- 条件付き依存: `if (!props)` → `escapeCSSURL()`
- 条件付き依存: `if (!props)` → `this._iconURLForSize()`
- 条件付き依存: `if (!props)` → `this._iconProperties.set()`

## getTitle()
- 位置: L780-782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).title`

## setTitle()
- 位置: L783-785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setProperty()`

## getTooltip()
- 位置: L790-792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).tooltip`

## setTooltip()
- 位置: L793-795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setProperty()`

## getWantsSubview()
- 位置: L800-802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).wantsSubview`

## setWantsSubview()
- 位置: L803-805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setProperty()`

## _setProperty()
- 位置: L818-824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getProperties()`, `this._updateProperty()`

## _updateProperty()
- 位置: L826-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PageActions.actionForID()`
- 条件付き依存: `if (PageActions.actionForID(this.id))` → `allBrowserPageActions()`
- 条件付き依存: `if (PageActions.actionForID(this.id))` → `bpa.updateAction()`
- 参照: `this.id`

## _getProperties()
- 位置: L849-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._windowProps.get()`
- 条件付き依存: `if (!props && forceWindowSpecific)` → `Object.create()`
- 条件付き依存: `if (!props && forceWindowSpecific)` → `this._windowProps.set()`
- 参照: `this._globalProps`

## anchorIDOverride()
- 位置: L863-865
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._anchorIDOverride`

## urlbarIDOverride()
- 位置: L870-872
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._urlbarIDOverride`

## wantsIframe()
- 位置: L877-879
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._wantsIframe`

## isBadged()
- 位置: L881-883
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isBadged`

## labelForHistogram()
- 位置: L885-893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `match[1].toUpperCase()`, `this._id.replace()`, `this._id.replace(/_\w{1}/g, match => match[1].toUpperCase()).substr()`
- 参照: `this._labelForHistogram`

## _iconURLForSize()
- 位置: L911-928
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `Object.keys(urls) .map(key => parseInt(key, 10)) .sort()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `Object.keys(urls) .map()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `Object.keys()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `parseInt()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `sizes.find()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `sizes.pop()`

## doCommand()
- 位置: L938-940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserPageActions()`, `browserPageActions(browserWindow).doCommandForAction()`

## onBeforePlacedInWindow()
- 位置: L948-952
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onBeforePlacedInWindow)` → `this._onBeforePlacedInWindow()`
- 参照: `this._onBeforePlacedInWindow`

## onCommand()
- 位置: L962-966
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onCommand)` → `this._onCommand()`
- 参照: `this._onCommand`

## onIframeHiding()
- 位置: L976-980
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onIframeHiding)` → `this._onIframeHiding()`
- 参照: `this._onIframeHiding`

## onIframeHidden()
- 位置: L990-994
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onIframeHidden)` → `this._onIframeHidden()`
- 参照: `this._onIframeHidden`

## onIframeShowing()
- 位置: L1004-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onIframeShowing)` → `this._onIframeShowing()`
- 参照: `this._onIframeShowing`

## onLocationChange()
- 位置: L1016-1020
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onLocationChange)` → `this._onLocationChange()`
- 参照: `this._onLocationChange`

## onPlacedInPanel()
- 位置: L1028-1032
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onPlacedInPanel)` → `this._onPlacedInPanel()`
- 参照: `this._onPlacedInPanel`

## onPlacedInUrlbar()
- 位置: L1040-1044
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onPlacedInUrlbar)` → `this._onPlacedInUrlbar()`
- 参照: `this._onPlacedInUrlbar`

## onRemovedFromWindow()
- 位置: L1053-1057
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onRemovedFromWindow)` → `this._onRemovedFromWindow()`
- 参照: `this._onRemovedFromWindow`

## onShowingInPanel()
- 位置: L1065-1069
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onShowingInPanel)` → `this._onShowingInPanel()`
- 参照: `this._onShowingInPanel`

## onSubviewPlaced()
- 位置: L1078-1082
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onSubviewPlaced)` → `this._onSubviewPlaced()`
- 参照: `this._onSubviewPlaced`

## onSubviewShowing()
- 位置: L1090-1094
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onSubviewShowing)` → `this._onSubviewShowing()`
- 参照: `this._onSubviewShowing`

## onPinToUrlbarToggled()
- 位置: L1098-1102
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onPinToUrlbarToggled)` → `this._onPinToUrlbarToggled()`
- 参照: `this._onPinToUrlbarToggled`

## remove()
- 位置: L1112-1114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PageActions.onActionRemoved()`

## shouldShowInPanel()
- 位置: L1125-1141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.canShowInWindow()`, `this.getDisabled()`
- 参照: `this.__transient`, `this.extensionID`

## shouldShowInUrlbar()
- 位置: L1151-1157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.canShowInWindow()`, `this.getDisabled()`
- 参照: `this.pinnedToUrlbar`

## _isBuiltIn()
- 位置: L1159-1164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["screenshots_mozilla_org"].concat()`, `builtInIDs.includes()`, `gBuiltInActions.filter()`, `gBuiltInActions.filter(a => !a.__isSeparator).map()`
- 参照: `a.__isSeparator`, `a.id`, `this.id`

## _isMozillaAction()
- 位置: L1166-1168
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isBuiltIn`, `this.id`

## PageActions._initBuiltInActions()
- 位置: L1188-1204
- 役割: (未記入)
- 触るとき: (未記入)

## onShowingInPanel()
- 位置: L1196-1198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserPageActions()`, `browserPageActions(buttonNode).bookmark.onShowingInPanel()`

## onCommand()
- 位置: L1199-1201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserPageActions()`, `browserPageActions(buttonNode).bookmark.onCommand()`

## browserPageActions()
- 位置: L1214-1219
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `obj.BrowserPageActions`, `obj.documentGlobal.BrowserPageActions`

## allBrowserWindows()
- 位置: L1230-1236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`
- XPCOM: `Services.wm`

## allBrowserPageActions()
- 位置: L1245-1249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allBrowserWindows()`, `browserPageActions()`

## setProperties()
- 位置: L1266-1289
- 役割: (未記入)
- 触るとき: (未記入)
