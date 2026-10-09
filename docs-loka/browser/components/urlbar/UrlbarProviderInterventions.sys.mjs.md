# browser/components/urlbar/UrlbarProviderInterventions.sys.mjs

source: browser/components/urlbar/UrlbarProviderInterventions.sys.mjs
source-hash: 5ddd82ec5962df1d7b39637a0d752e52b4551048
lines: 777

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.declareLazy()`

## Node.constructor()
- 位置: L110-114
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.childrenByWord`, `this.documents`, `this.word`

## QueryScorer.constructor()
- 位置: L158-163
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._distanceThreshold`, `this._documents`, `this._rootNode`, `this._variations`

## QueryScorer.addDocument()
- 位置: L175-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `phrase.indexOf()`, `phraseStr .trim()`, `phraseStr .trim() .split()`, `phraseStr .trim() .split(/\s+/) .map()`, `this._buildPhraseTree()`, `this._documents.add()`, `word.toLocaleLowerCase()`
- 条件付き依存: `if (index >= 0)` → `Array.from()`
- 条件付き依存: `if (index >= 0)` → `variationPhrase.splice()`
- 条件付き依存: `if (index >= 0)` → `variation.split()`
- 条件付き依存: `if (index >= 0)` → `phrases.push()`
- 参照: `doc.phrases`, `this._rootNode`, `this._variations`

## QueryScorer.score()
- 位置: L217-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `minDistanceByDoc.get()`, `queryString .trim()`, `queryString .trim() .split()`, `queryString .trim() .split(/\s+/) .map()`, `results.push()`, `results.sort()`, `this._traverse()`, `word.toLocaleLowerCase()`
- 参照: `a.score`, `b.score`, `this._documents`

## QueryScorer._buildPhraseTree()
- 位置: L258-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.documents.add()`, `node.childrenByWord.get()`, `phrase[wordIndex].toLocaleLowerCase()`, `this._buildPhraseTree()`
- 条件付き依存: `if (!child)` → `node.childrenByWord.set()`
- 参照: `phrase.length`

## QueryScorer._traverse()
- 位置: L296-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NLP.levenshtein()`
- 条件付き依存: `if (!node.childrenByWord.size)` → `minDistanceByDoc.set()`
- 条件付き依存: `if (!node.childrenByWord.size)` → `Math.min()`
- 条件付き依存: `if (!node.childrenByWord.size)` → `minDistanceByDoc.has()`
- 条件付き依存: `if (!node.childrenByWord.size)` → `minDistanceByDoc.get()`
- 条件付き依存: `if (distance <= this._distanceThreshold)` → `this._traverse()`
- 参照: `node.childrenByWord`, `node.childrenByWord.size`, `node.documents`, `queryWords.length`, `this._distanceThreshold`, `this._rootNode`

## getPayloadForTip()
- 位置: L356-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- 参照: `UrlbarShared.INTERVENTION_TIP_TYPE.CLEAR`, `UrlbarShared.INTERVENTION_TIP_TYPE.REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_ASK`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_RESTART`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_WEB`
- XPCOM: `Services.urlFormatter`

## queryScorer()
- 位置: L407-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `queryScorer.addDocument()`

## UrlbarProviderInterventions.type()
- 位置: L435-437
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderInterventions.isActive()
- 位置: async L446-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EN_LOCALE_MATCH.test()`, `Services.policies.isAllowed()`, `UrlbarProviderInterventions.lazy.queryScorer.score()`, `lazy.UrlUtils.REGEXP_LIKE_PROTOCOL.test()`, `this.queryInstance .getProvider()`, `this.queryInstance .getProvider(lazy.UrlbarProviderGlobalActions.name) ?.isActive()`, `topDocIDs.has()`
- 条件付き依存: `if (topDocScore.score != Infinity)` → `topDocIDs.add()`
- 条件付き依存: `if (topDocIDs.has("update"))` → `this._setCurrentTipFromAppUpdaterStatus()`
- 条件付き依存: `if (!(topDocIDs.has("update")))` → `topDocIDs.has()`
- 条件付き依存: `if (topDocIDs.has("clear"))` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (topDocIDs.has("clear"))` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!(topDocIDs.has("clear")))` → `topDocIDs.has()`
- 参照: `Services.locale.appLocaleAsBCP47`, `UrlbarShared.INTERVENTION_TIP_TYPE.CLEAR`, `UrlbarShared.INTERVENTION_TIP_TYPE.NONE`, `UrlbarShared.INTERVENTION_TIP_TYPE.REFRESH`, `UrlbarShared.MAX_TEXT_LENGTH`, `document.id`, `lazy.UrlbarProviderGlobalActions.name`, `queryContext.searchString`, `queryContext.searchString.length`, `this.currentTip`, `topDocScore.score`
- XPCOM: `Services.locale` / `Services.policies`

## UrlbarProviderInterventions._setCurrentTipFromAppUpdaterStatus()
- 位置: async L500-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarProviderInterventions.checkForBrowserUpdate()`
- 参照: `UrlbarShared.INTERVENTION_TIP_TYPE.NONE`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_ASK`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_RESTART`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_WEB`, `lazy.AppUpdater.STATUS.CHECKING`, `lazy.AppUpdater.STATUS.DOWNLOAD_AND_INSTALL`, `lazy.AppUpdater.STATUS.NO_UPDATER`, `lazy.AppUpdater.STATUS.NO_UPDATES_FOUND`, `lazy.AppUpdater.STATUS.READY_FOR_RESTART`, `lazy.AppUpdater.STATUS.UPDATE_DISABLED_BY_POLICY`, `lazy.appUpdater.status`, `this.currentTip`

## UrlbarProviderInterventions.startQuery()
- 位置: async L558-622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`, `getPayloadForTip()`
- 条件付き依存: `if (this.currentTip == UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING)` → `this._setCurrentTipFromAppUpdaterStatus()`
- 条件付き依存: `if ( this.currentTip == UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING )` → `lazy.appUpdater.addListener()`
- 条件付き依存: `if ( this.currentTip == UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING )` → `this._setCurrentTipFromAppUpdaterStatus()`
- 参照: `UrlbarShared.ICON.TIP`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING`, `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.TIP`, `lazy.UrlbarResult`, `this._appUpdaterListener`, `this.currentTip`, `this.queryInstance`

## this._appUpdaterListener()
- 位置: L583-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.appUpdater.removeListener()`, `resolve()`
- 参照: `this._appUpdaterListener`

## UrlbarProviderInterventions.cancelQuery()
- 位置: L627-634
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._appUpdaterListener)` → `lazy.appUpdater.removeListener()`
- 参照: `this._appUpdaterListener`

## UrlbarProviderInterventions.#pickResult()
- 位置: L636-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `installBrowserUpdateAndRestart()`, `openClearHistoryDialog()`, `resetBrowser()`, `restartBrowser()`, `window.gBrowser.addWebTab()`
- 参照: `UrlbarShared.INTERVENTION_TIP_TYPE.CLEAR`, `UrlbarShared.INTERVENTION_TIP_TYPE.REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_ASK`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_RESTART`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_WEB`, `result.payload.type`, `window.gBrowser.selectedTab`

## UrlbarProviderInterventions.onEngagement()
- 位置: L667-675
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (details.selType == "tip")` → `this.#pickResult()`
- 参照: `controller.browserWindow`, `details.result`, `details.selType`

## UrlbarProviderInterventions.checkForBrowserUpdate()
- 位置: L685-695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if ( force || !UrlbarProviderInterventions._lastUpdateCheckTime || Date.now() - UrlbarProviderInterventions._lastUpdateCheckTime >= UPDATE_CHECK_PERIOD_MS )` → `Date.now()`
- 条件付き依存: `if ( force || !UrlbarProviderInterventions._lastUpdateCheckTime || Date.now() - UrlbarProviderInterventions._lastUpdateCheckTime >= UPDATE_CHECK_PERIOD_MS )` → `lazy.appUpdater.check()`
- 参照: `UrlbarProviderInterventions._lastUpdateCheckTime`

## UrlbarProviderInterventions.resetAppUpdater()
- 位置: L701-706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.getOwnPropertyDescriptor()`
- 参照: `Object.getOwnPropertyDescriptor(lazy, "appUpdater").get`, `lazy.AppUpdater`, `lazy.appUpdater`

## installBrowserUpdateAndRestart()
- 位置: L713-736
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.appUpdater.addListener()`, `lazy.appUpdater.allowUpdateDownload()`
- 条件付き依存: `if (lazy.appUpdater.status != lazy.AppUpdater.STATUS.DOWNLOAD_AND_INSTALL)` → `Promise.resolve()`
- 参照: `lazy.AppUpdater.STATUS.DOWNLOAD_AND_INSTALL`, `lazy.appUpdater.status`

## listener()
- 位置: L718-732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.appUpdater.removeListener()`, `resolve()`
- 条件付き依存: `if (lazy.appUpdater.status == lazy.AppUpdater.STATUS.READY_FOR_RESTART)` → `restartBrowser()`
- 参照: `lazy.AppUpdater.STATUS.DOWNLOAD_FAILED`, `lazy.AppUpdater.STATUS.READY_FOR_RESTART`, `lazy.appUpdater.status`

## openClearHistoryDialog()
- 位置: L738-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.Sanitizer.showUI()`

## restartBrowser()
- 位置: L747-769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.startup.restartInSafeMode()`
- 条件付き依存: `if (!(Services.appinfo.inSafeMode))` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `Ci.nsISupportsPRBool`, `Services.appinfo.inSafeMode`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.appinfo` / `Services.obs` / `Services.startup`

## resetBrowser()
- 位置: L771-776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ResetProfile.openConfirmationDialog()`, `lazy.ResetProfile.resetSupported()`
