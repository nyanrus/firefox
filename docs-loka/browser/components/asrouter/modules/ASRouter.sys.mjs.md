# browser/components/asrouter/modules/ASRouter.sys.mjs

source: browser/components/asrouter/modules/ASRouter.sys.mjs
source-hash: 443451cae1a800039d8c4691ba8554158c433bf7
lines: 2777

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`

## isMozillaInternalPage()
- 位置: L136-152
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `uri.filePath`, `uri?.scheme`

## isMozillaWebpage()
- 位置: L154-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`, `["mozilla.org", "firefox.com"].some()`
- 参照: `uri.host`
- XPCOM: `Services.eTLD`

## isThirdPartyPage()
- 位置: L164-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isMozillaInternalPage()`, `isMozillaWebpage()`

## reportError()
- 位置: L179-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `e.toString()`, `this._errors.push()`
- 参照: `e.stack`

## errors()
- 位置: L187-191
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._errors`

## _localLoader()
- 位置: L200-202
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `provider.messages`

## _remoteLoaderCache()
- 位置: async L204-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MessageLoaderUtils.reportError()`, `storage.get()`
- 参照: `MessageLoaderUtils.REMOTE_LOADER_CACHE_KEY`

## _remoteLoader()
- 位置: async L226-314
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (provider.url)` → `MessageLoaderUtils._remoteLoaderCache()`
- 条件付き依存: `if ( cached && cached.url === provider.url && cached.version === STARTPAGE_VERSION )` → `MessageLoaderUtils.shouldProviderUpdate()`
- 条件付き依存: `if (etag)` → `headers.set()`
- 条件付き依存: `if (provider.url)` → `fetch()`
- 条件付き依存: `if (provider.url)` → `MessageLoaderUtils.reportError()`
- 条件付き依存: `if ( response && response.ok && response.status >= 200 && response.status < 400 )` → `response.json()`
- 条件付き依存: `if ( response && response.ok && response.status >= 200 && response.status < 400 )` → `MessageLoaderUtils.reportError()`
- 条件付き依存: `if (jsonResponse && jsonResponse.messages)` → `jsonResponse.messages.map()`
- 条件付き依存: `if (provider.updateCycleInMs > 0)` → `response.headers.get()`
- 条件付き依存: `if (provider.updateCycleInMs > 0)` → `Date.now()`
- 条件付き依存: `if (provider.updateCycleInMs > 0)` → `options.storage.set()`
- 条件付き依存: `if (!(jsonResponse && jsonResponse.messages))` → `MessageLoaderUtils.reportError()`
- 条件付き依存: `if (response)` → `MessageLoaderUtils.reportError()`
- 参照: `MessageLoaderUtils.REMOTE_LOADER_CACHE_KEY`, `cached.etag`, `cached.url`, `cached.version`, `jsonResponse.messages`, `options.storage`, `provider.id`, `provider.updateCycleInMs`, `provider.url`, `response.ok`, `response.status`

## _remoteSettingsLoader()
- 位置: async L338-402
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (provider.collection)` → `MessageLoaderUtils._getRemoteSettingsMessages()`
- 条件付き依存: `if (!messages.length)` → `MessageLoaderUtils._handleRemoteSettingsUndesiredEvent()`
- 条件付き依存: `if (!(!messages.length))` → `PROVIDERS_WITH_L10N.includes()`
- 条件付き依存: `if (!(!messages.length))` → `lazy.RemoteL10n.isLocaleSupported()`
- 条件付き依存: `if ( PROVIDERS_WITH_L10N.includes(provider.id) && lazy.RemoteL10n.isLocaleSupported(MessageLoaderUtils.locale) )` → `MessageLoaderUtils._getRemoteSettingsLanguagePackRecord()`
- 条件付き依存: `if (record && record.attachment)` → `IOUtils.exists()`
- 条件付き依存: `if (record && record.attachment)` → `IOUtils.stat()`
- 条件付き依存: `if ( !(await IOUtils.exists(localFile)) || (await IOUtils.stat(localFile)).size !== remoteSize )` → `downloader.download()`
- 条件付き依存: `if ( !(await IOUtils.exists(localFile)) || (await IOUtils.stat(localFile)).size !== remoteSize )` → `IOUtils.write()`
- 条件付き依存: `if (record && record.attachment)` → `lazy.RemoteL10n.reloadL10n()`
- 条件付き依存: `if (!(record && record.attachment))` → `MessageLoaderUtils._handleRemoteSettingsUndesiredEvent()`
- 条件付き依存: `if (provider.collection)` → `MessageLoaderUtils._handleRemoteSettingsUndesiredEvent()`
- 条件付き依存: `if (provider.collection)` → `MessageLoaderUtils.reportError()`
- 参照: `(await IOUtils.stat(localFile)).size`, `MessageLoaderUtils.locale`, `lazy.RemoteL10n.cfrFluentFilePath`, `lazy.UnstoredDownloader`, `messages.length`, `options.dispatchCFRAction`, `provider.collection`, `provider.id`, `record.attachment`

## _getRemoteSettingsMessages()
- 位置: L410-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteSettings()`, `lazy.RemoteSettings(collection).get()`

## _getRemoteSettingsLanguagePackRecord()
- 位置: async L421-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteSettings()`, `lazy.RemoteSettings(RS_COLLECTION_L10N).get()`

## _experimentsAPILoader()
- 位置: async L448-570
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `MESSAGING_EXPERIMENTS_DEFAULT_FEATURES.includes()`, `MessageLoaderUtils._recordedReachIds.has()`, `NO_REACH_EVENT_GROUPS.includes()`, `featureAPI.getAllEnrollments()`, `lazy.ASRouterTargeting.getMessageTriggers()`, `lazy.ExperimentAPI.getAllBranches()`, `nimbusMessages.push()`
- 条件付き依存: `if (enrollments.length > 1)` → `enrollments.filter()`
- 条件付き依存: `if (message?.id)` → `nimbusMessages.push()`
- 参照: `branch.slug`, `branchMessage.id`, `branchMessage?.recordReach`, `branchValue.messages`, `branchValue?.template`, `branch[featureId].value`, `enrollment.meta.isRollout`, `enrollments.length`, `featureAPI.allowCoenrollment`, `lazy.ASRouterTargeting.getMessageTriggers(branchMessage).length`, `lazy.NimbusFeatures`, `message._branchSlug`, `message._nimbusFeature`, `message._nimbusSlug`, `message?.id`, `meta.branch`, `meta.isRollout`, `meta.slug`, `provider.featureIds`, `value.messages`, `value?.template`

## _handleRemoteSettingsUndesiredEvent()
- 位置: L572-582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchCFRAction()`
- 参照: `lazy.MESSAGE_TYPE_HASH.AS_ROUTER_TELEMETRY_USER_EVENT`

## _getMessageLoader()
- 位置: L590-602
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `provider.type`, `this._experimentsAPILoader`, `this._localLoader`, `this._remoteLoader`, `this._remoteSettingsLoader`

## shouldProviderUpdate()
- 位置: L613-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 参照: `provider.lastUpdated`, `provider.updateCycleInMs`

## _loadDataForProvider()
- 位置: async L620-634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loader()`, `this._getMessageLoader()`
- 条件付き依存: `if (!messages)` → `MessageLoaderUtils.reportError()`
- 参照: `provider.id`

## loadMessagesForProvider()
- 位置: async L645-693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `messages .map()`, `this._loadDataForProvider()`
- 条件付き依存: `if (provider.exclude && provider.exclude.length)` → `messages.filter()`
- 条件付き依存: `if (provider.exclude && provider.exclude.length)` → `provider.exclude.includes()`
- 条件付き依存: `if ( provider.type === "local" && lazy.ASRouterPreferences.devtoolsEnabled )` → `this._delocalizeValues()`
- 条件付き依存: `if ( provider.type === "local" && lazy.ASRouterPreferences.devtoolsEnabled )` → `lazy.ASRouterPreferences.console.error()`
- 参照: `MessageLoaderUtils.errors`, `e.cause`, `e.message`, `lazy.ASRouterPreferences.devtoolsEnabled`, `message.id`, `message.weight`, `messageData.groups`, `provider.exclude`, `provider.exclude.length`, `provider.id`, `provider.type`

## _delocalizeValues()
- 位置: L712-739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.assign()`, `Object.entries()`, `this._delocalizeValues()`
- 条件付き依存: `if (Array.isArray(values))` → `values.map()`
- 条件付き依存: `if (Array.isArray(values))` → `this._delocalizeValues()`
- 参照: `value.text`, `value?.text`

## cleanupCache()
- 位置: async L746-759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MessageLoaderUtils._remoteLoaderCache()`, `ids.includes()`, `providers.filter()`, `providers.filter(p => p.type === "remote").map()`
- 条件付き依存: `if (dirty)` → `storage.set()`
- 参照: `MessageLoaderUtils.REMOTE_LOADER_CACHE_KEY`, `p.id`, `p.type`

## locale()
- 位置: L767-779
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## _ASRouter.constructor()
- 位置: L791-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleTargetingError.bind()`, `this._onExperimentEnrollmentsUpdated.bind()`, `this._onLocaleChanged.bind()`, `this._resetInitialization()`, `this._triggerHandler.bind()`, `this._updateMultiprofileData.bind()`, `this.addImpression.bind()`, `this.addScreenImpression.bind()`, `this.blockMessageById.bind()`, `this.forcePBWindow.bind()`, `this.handleMessageRequest.bind()`, `this.isUnblockedMessage.bind()`, `this.onPrefChange.bind()`, `this.unblockAll.bind()`, `this.unblockMessageById.bind()`
- 参照: `Services.locale.appLocaleAsBCP47`, `this._experimentChangedListeners`, `this._handleTargetingError`, `this._localProviders`, `this._onExperimentEnrollmentsUpdated`, `this._onLocaleChanged`, `this._state`, `this._storage`, `this._triggerHandler`, `this._updateMultiprofileData`, `this.addImpression`, `this.addScreenImpression`, `this.blockMessageById`, `this.clearChildMessages`, `this.clearChildProviders`, `this.dispatchCFRAction`, `this.forcePBWindow`, `this.handleMessageRequest`, `this.initialized`, `this.isUnblockedMessage`, `this.messagesEnabledInAutomation`, `this.onPrefChange`, `this.sendTelemetry`, `this.unblockAll`, `this.unblockMessageById`, `this.updateAdminState`
- XPCOM: `Services.locale`

## _ASRouter.onPrefChange()
- 位置: async L831-861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TARGETING_PREFERENCES.includes()`
- 条件付き依存: `if (lazy.TARGETING_PREFERENCES.includes(prefName))` → `this._getMessagesContext()`
- 条件付き依存: `if (lazy.TARGETING_PREFERENCES.includes(prefName))` → `this.state.messages.filter()`
- 条件付き依存: `if (lazy.TARGETING_PREFERENCES.includes(prefName))` → `targetingContext.evalWithDefault()`
- 条件付き依存: `if (!isMatch)` → `invalidMessages.push()`
- 条件付き依存: `if (lazy.TARGETING_PREFERENCES.includes(prefName))` → `this.clearChildMessages()`
- 条件付き依存: `if (!(lazy.TARGETING_PREFERENCES.includes(prefName)))` → `this._loadLocalProviders()`
- 条件付き依存: `if (!(lazy.TARGETING_PREFERENCES.includes(prefName)))` → `this._updateMessageProviders()`
- 条件付き依存: `if (invalidProviders.length)` → `this.clearChildProviders()`
- 条件付き依存: `if (!(lazy.TARGETING_PREFERENCES.includes(prefName)))` → `this.loadMessagesFromAllProviders()`
- 条件付き依存: `if (!(lazy.TARGETING_PREFERENCES.includes(prefName)))` → `this.setState()`
- 条件付き依存: `if (!(lazy.TARGETING_PREFERENCES.includes(prefName)))` → `state.groups.map()`
- 参照: `invalidProviders.length`, `lazy.TargetingContext`, `msg.id`, `msg.targeting`, `this._checkGroupEnabled`, `this.isUnblockedMessage`

## _ASRouter._updateMessageProviders()
- 位置: async L864-929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.ASRouterPreferences.console.debug()`, `lazy.ASRouterPreferences.getUserPreference()`, `lazy.ASRouterPreferences.providers.filter()`, `prevState.messages.filter()`, `previousProviders.filter()`, `providerIDs.includes()`, `providers.map()`, `this.setState()`
- 条件付き依存: `if (localProvider)` → `localProvider.getMessages()`
- 条件付き依存: `if (provider.type === "remote" && provider.url)` → `provider.url.replace()`
- 条件付き依存: `if (provider.type === "remote" && provider.url)` → `Services.urlFormatter.formatURL()`
- 条件付き依存: `if (!providerIDs.includes(prevProvider.id))` → `invalidProviders.push()`
- 参照: `message.provider`, `p.enabled`, `p.id`, `prevProvider.id`, `provider.featureIds`, `provider.id`, `provider.lastUpdated`, `provider.localProvider`, `provider.messages`, `provider.type`, `provider.url`, `this._localProviders`, `this.state.providers`
- XPCOM: `Services.urlFormatter`

## _ASRouter.state()
- 位置: L931-933
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state`

## _ASRouter.state()
- 位置: L935-939
- 役割: (未記入)
- 触るとき: (未記入)

## _ASRouter._resetInitialization()
- 位置: L950-960
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._finishInitializing`, `this.initialized`, `this.initializing`, `this.waitForInitialized`

## this._finishInitializing()
- 位置: L954-958
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`
- 参照: `this.initialized`, `this.initializing`

## _ASRouter.hasGroupsEnabled()
- 位置: L968-972
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `groups.includes()`, `this.state.groups .filter()`, `this.state.groups .filter(({ id }) => groups.includes(id)) .every()`

## _ASRouter.isExcludedByProvider()
- 位置: L983-992
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.state.providers.find()`
- 条件付き依存: `if (provider.exclude)` → `provider.exclude.includes()`
- 参照: `message.id`, `message.provider`, `p.id`, `provider.exclude`

## _ASRouter._checkGroupEnabled()
- 位置: L1001-1014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `group.userPreferences.some()`, `lazy.ASRouterPreferences.getUserPreference()`
- 参照: `group.enabled`, `group.userPreferences`

## _ASRouter.loadAllMessageGroups()
- 位置: async L1023-1043
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(remoteMessages || state.groups).map()`, `MessageLoaderUtils.shouldProviderUpdate()`, `this.setState()`, `this.state.providers.find()`
- 条件付き依存: `if (provider)` → `MessageLoaderUtils._loadDataForProvider()`
- 参照: `p.id`, `state.groups`, `this._checkGroupEnabled`, `this._storage`, `this.dispatchCFRAction`

## _ASRouter.loadMessagesFromAllProviders()
- 位置: async L1053-1125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `MessageLoaderUtils.shouldProviderUpdate()`, `lazy.ASRouterPreferences.console.debug()`, `this._fireMessagesLoadedTrigger()`, `this.loadAllMessageGroups()`, `this.state.providers.filter()`
- 条件付き依存: `if (needsUpdate.length)` → `needsUpdate.includes()`
- 条件付き依存: `if (needsUpdate.includes(provider.id))` → `MessageLoaderUtils.loadMessagesForProvider()`
- 条件付き依存: `if (needsUpdate.includes(provider.id))` → `newState.providers.push()`
- 条件付き依存: `if (!(needsUpdate.includes(provider.id)))` → `this.state.messages.filter()`
- 条件付き依存: `if (!(needsUpdate.includes(provider.id)))` → `newState.providers.push()`
- 条件付き依存: `if (needsUpdate.length)` → `lazy.ASRouterTriggerListeners.keys()`
- 条件付き依存: `if (needsUpdate.length)` → `this._shouldSkipForAutomation()`
- 条件付き依存: `if (needsUpdate.length)` → `lazy.ASRouterTargeting.getMessageTriggers()`
- 条件付き依存: `if (needsUpdate.length)` → `lazy.ASRouterTriggerListeners.has()`
- 条件付き依存: `if (trigger && lazy.ASRouterTriggerListeners.has(trigger.id))` → `lazy.ASRouterTriggerListeners.get(trigger.id).init()`
- 条件付き依存: `if (trigger && lazy.ASRouterTriggerListeners.has(trigger.id))` → `lazy.ASRouterTriggerListeners.get()`
- 条件付き依存: `if (trigger && lazy.ASRouterTriggerListeners.has(trigger.id))` → `unseenListeners.delete()`
- 条件付き依存: `if (needsUpdate.length)` → `lazy.ASRouterTriggerListeners.get(triggerID).uninit()`
- 条件付き依存: `if (needsUpdate.length)` → `lazy.ASRouterTriggerListeners.get()`
- 条件付き依存: `if (needsUpdate.length)` → `this.setState()`
- 条件付き依存: `if (needsUpdate.length)` → `this.cleanupImpressions()`
- 参照: `msg.provider`, `needsUpdate.length`, `newState.messages`, `p.id`, `provider.id`, `this._storage`, `this._triggerHandler`, `this.dispatchCFRAction`, `this.state`, `this.state.providers`, `trigger.id`, `trigger.params`, `trigger.patterns`, `trigger.regexPatterns`

## _ASRouter._fireMessagesLoadedTrigger()
- 位置: async L1127-1145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `lazy.ASRouterTriggerListeners.get()`, `this.sendTriggerMessage()`
- 参照: `lazy.ASRouterTriggerListeners.get("messagesLoaded")?.initialized`, `win?.gBrowser?.selectedBrowser`
- XPCOM: `Services.wm`

## _ASRouter._onLocaleChanged()
- 位置: async L1157-1179
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (newLocale !== localeInUse)` → `providers.forEach()`
- 条件付き依存: `if (newLocale !== localeInUse)` → `PROVIDERS_WITH_L10N.includes()`
- 条件付き依存: `if (needsUpdate)` → `this.setState()`
- 条件付き依存: `if (needsUpdate)` → `this.loadMessagesFromAllProviders()`
- 参照: `Services.locale.appLocaleAsBCP47`, `provider.id`, `provider.lastUpdated`, `this.state`, `this.state.localeInUse`, `this.state.providers`
- XPCOM: `Services.locale`

## _ASRouter.observe()
- 位置: L1181-1187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteL10n.reloadL10n()`

## _ASRouter.toWaitForInitFunc()
- 位置: L1189-1191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `func()`, `this.waitForInitialized.then()`

## _ASRouter.init()
- 位置: async L1199-1291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MessageLoaderUtils.cleanupCache()`, `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `lazy.ASRouterPreferences.addListener()`, `lazy.ASRouterPreferences.init()`, `lazy.MessagingSystemAllowlists.ensureInit()`, `lazy.MomentsPageHub.init()`, `lazy.ToolbarBadgeHub.init()`, `this._finishInitializing()`, `this._loadAllowHosts()`, `this._loadLocalProviders()`, `this._storage.get()`, `this._updateMessageProviders()`, `this.loadMessagesFromAllProviders()`, `this.setState()`, `this.toWaitForInitFunc()`
- 条件付き依存: `if ( lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles || lazy.ASRouterTargeting.Environment.hasSelectableProfiles )` → `this._storage.getSharedMessageImpressions()`
- 条件付き依存: `if ( lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles || lazy.ASRouterTargeting.Environment.hasSelectableProfiles )` → `this._storage.getSharedMessageBlocklist()`
- 参照: `lazy.ASRouterPreferences.specialConditions`, `lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles`, `lazy.ASRouterTargeting.Environment.hasSelectableProfiles`, `lazy.SpecialMessageActions.blockMessageById`, `this.ALLOWLIST_HOSTS`, `this._onExperimentEnrollmentsUpdated`, `this._onLocaleChanged`, `this._storage`, `this._updateMultiprofileData`, `this.addImpression`, `this.blockMessageById`, `this.clearChildMessages`, `this.clearChildProviders`, `this.dispatchCFRAction`, `this.handleMessageRequest`, `this.initialized`, `this.initializing`, `this.onPrefChange`, `this.sendTelemetry`, `this.state`, `this.state.providers`, `this.unblockMessageById`, `this.updateAdminState`, `this.waitForInitialized`
- XPCOM: `Services.obs` / `Services.prefs`

## _ASRouter.uninit()
- 位置: L1293-1325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `lazy.ASRouterPreferences.removeListener()`, `lazy.ASRouterPreferences.uninit()`, `lazy.ASRouterTriggerListeners.values()`, `lazy.MomentsPageHub.uninit()`, `lazy.ToolbarBadgeHub.uninit()`, `listener.uninit()`, `this._resetInitialization()`, `this._storage.set()`
- 参照: `this._onExperimentEnrollmentsUpdated`, `this._onLocaleChanged`, `this._updateMultiprofileData`, `this.clearChildMessages`, `this.clearChildProviders`, `this.dispatchCFRAction`, `this.onPrefChange`, `this.sendTelemetry`, `this.updateAdminState`
- XPCOM: `Services.obs` / `Services.prefs`

## _ASRouter.setState()
- 位置: L1327-1348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `callbackOrObj()`, `lazy.ASRouterPreferences.console.debug()`, `lazy.ASRouterPreferences.console.trace()`
- 条件付き依存: `if (lazy.ASRouterPreferences.devtoolsEnabled)` → `this.updateTargetingParameters().then()`
- 条件付き依存: `if (lazy.ASRouterPreferences.devtoolsEnabled)` → `this.updateTargetingParameters()`
- 条件付き依存: `if (lazy.ASRouterPreferences.devtoolsEnabled)` → `this.updateAdminState()`
- 参照: `lazy.ASRouterPreferences.devtoolsEnabled`, `this._state`, `this.state`

## _ASRouter.updateTargetingParameters()
- 位置: L1350-1362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterPreferences.getAllUserPreferences()`, `this._getMessagesContext()`, `this.getTargetingParameters()`, `this.getTargetingParameters( lazy.ASRouterTargeting.Environment, this._getMessagesContext() ).then()`
- 参照: `lazy.ASRouterPreferences.devtoolsEnabled`, `lazy.ASRouterPreferences.providers`, `lazy.ASRouterTargeting.Environment`, `this.errors`, `this.state`

## _ASRouter.getMessageById()
- 位置: L1364-1366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.state.messages.find()`
- 参照: `message.id`

## _ASRouter._loadLocalProviders()
- 位置: L1368-1376
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ASRouterPreferences.devtoolsEnabled`, `lazy.PanelTestProvider`, `this._localProviders`

## _ASRouter._updateMultiprofileData()
- 位置: async L1378-1396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._storage.getSharedMessageBlocklist()`, `this._storage.getSharedMessageImpressions()`, `this.setState()`
- 参照: `this.initialized`, `this.waitForInitialized`

## _ASRouter.getTargetingParameters()
- 位置: async L1402-1445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## resolve()
- 位置: async L1404-1437
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(object))` → `Promise.all()`
- 条件付き依存: `if (Array.isArray(object))` → `object.map()`
- 条件付き依存: `if (Array.isArray(object))` → `resolve()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Object.entries(object).map()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Object.entries()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `resolve()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Promise.allSettled()`

## _ASRouter._handleTargetingError()
- 位置: L1447-1458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.dispatchCFRAction()`
- 参照: `lazy.MESSAGE_TYPE_HASH.AS_ROUTER_TELEMETRY_USER_EVENT`, `message.id`

## _ASRouter._getMessagesContext()
- 位置: L1461-1476
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.state`

## _ASRouter.messageImpressions()
- 位置: L1466-1468
- 役割: (未記入)
- 触るとき: (未記入)

## _ASRouter.previousSessionEnd()
- 位置: L1469-1471
- 役割: (未記入)
- 触るとき: (未記入)

## _ASRouter.screenImpressions()
- 位置: L1472-1474
- 役割: (未記入)
- 触るとき: (未記入)

## _ASRouter.evaluateExpression()
- 位置: async L1478-1490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `targetingContext.evalWithDefault()`
- 参照: `e.message`, `lazy.TargetingContext`

## _ASRouter.unblockAll()
- 位置: L1492-1494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setState()`

## _ASRouter.hasValidProfileScope()
- 位置: L1496-1516
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PROFILE_MESSAGE_SCOPE.NONE`, `PROFILE_MESSAGE_SCOPE.SINGLE`, `message.id`, `message.profileScope`, `state.messageImpressions`, `state.multiProfileMessageImpressions`

## _ASRouter.isUnblockedMessage()
- 位置: L1518-1528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `state.messageBlockList.includes()`, `state.multiProfileMessageBlocklist.includes()`, `this.hasGroupsEnabled()`, `this.isExcludedByProvider()`
- 参照: `message.campaign`, `message.groups`, `message.id`

## _ASRouter.isBelowFrequencyCaps()
- 位置: L1531-1570
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `message.groups.every()`, `this._isBelowItemFrequencyCap()`, `this.state.groups.find()`
- 条件付き依存: `if (!_belowItemFrequencyCap)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!belowThisGroupCap)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!(!belowThisGroupCap))` → `lazy.ASRouterPreferences.console.debug()`
- 参照: `message.id`, `this.state`

## _ASRouter._isBelowItemFrequencyCap()
- 位置: L1574-1601
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (item && item.frequency && impressions && impressions.length)` → `Math.min()`
- 条件付き依存: `if ( item.frequency.lifetime && impressions.length >= Math.min(item.frequency.lifetime, maxLifetimeCap) )` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (item.frequency.custom)` → `Date.now()`
- 条件付き依存: `if (item.frequency.custom)` → `impressions.filter()`
- 条件付き依存: `if (impressionsInPeriod.length >= setting.cap)` → `lazy.ASRouterPreferences.console.debug()`
- 参照: `impressions.length`, `impressionsInPeriod.length`, `item.frequency`, `item.frequency.custom`, `item.frequency.lifetime`, `item.id`, `setting.cap`

## _ASRouter._shouldSkipForAutomation()
- 位置: L1603-1612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.exists()`, `Services.env.get()`, `this.messagesEnabledInAutomation?.includes()`
- 参照: `Cu.isInAutomation`, `message.id`, `message.skip_in_tests`
- XPCOM: `Services.env`

## _ASRouter._findProvider()
- 位置: L1614-1618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.state.providers.find()`
- 参照: `i.id`, `this._localProviders`, `this.state.providers.find(i => i.id === providerID).localProvider`

## _ASRouter._isAllowedActionOnlyMessageAction()
- 位置: L1629-1673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowed.has()`, `lazy.MessagingSystemAllowlists.getActionOnlyActions()`
- 条件付き依存: `if (action.type === "MULTI_ACTION")` → `Array.isArray()`
- 条件付き依存: `if (action.type === "MULTI_ACTION")` → `actions.every()`
- 条件付き依存: `if (action.type === "MULTI_ACTION")` → `allowed.has()`
- 参照: `action.data?.actions`, `action.type`, `actions.length`, `nested?.type`

## _ASRouter.routeCFRMessage()
- 位置: L1675-1785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MessageLoaderUtils._delocalizeValues()`, `Promise.resolve()`, `Services.obs.notifyObservers()`, `lazy.BookmarksBarButton.showBookmarksBarButton()`, `lazy.FeatureCalloutBroker.showFeatureCallout()`, `lazy.InfoBar.showInfoBarMessage()`, `lazy.MenuMessage.showMenuMessage()`, `lazy.MomentsPageHub.executeAction()`, `lazy.PanelTestProvider.tagMessageForTesting()`, `lazy.SidebarChatBotPromo.showPromo()`, `lazy.SmartWindowNewTabPromo.showPromo()`, `lazy.SpecialMessageActions.handleAction()`, `lazy.Spotlight.showSpotlightDialog()`, `lazy.ToastNotification.showToastNotification()`, `lazy.ToolbarBadgeHub.registerBadgeNotificationListener()`, `this._isAllowedActionOnlyMessageAction()`, `this.dispatchCFRAction()`
- 参照: `message.content`, `message.id`, `message.template`, `this.dispatchCFRAction`, `trigger.id`
- XPCOM: `Services.obs`

## _ASRouter.addScreenImpression()
- 位置: async L1787-1810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.ASRouterPreferences.console.debug()`, `this._storage.set()`, `this.setState()`
- 参照: `screen.id`, `this.initialized`, `this.state.screenImpressions`, `this.waitForInitialized`

## _ASRouter.addImpression()
- 位置: L1812-1867
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `lazy.ASRouterPreferences.console.debug()`, `message.groups?.includes()`, `this.state.groups?.filter()`
- 条件付き依存: `if (message.frequency || groupsWithFrequency.length)` → `Date.now()`
- 条件付き依存: `if (message.frequency || groupsWithFrequency.length)` → `this.setState()`
- 条件付き依存: `if (message.frequency || groupsWithFrequency.length)` → `this._addImpressionForItem()`
- 条件付き依存: `if ( message.profileScope === PROFILE_MESSAGE_SCOPE.SINGLE && lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles )` → `this._addImpressionForItem()`
- 参照: `PROFILE_MESSAGE_SCOPE.SINGLE`, `groupsWithFrequency.length`, `lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles`, `message.frequency`, `message.id`, `message.profileScope`, `state.messageImpressions`, `state.multiProfileMessageImpressions`

## _ASRouter._addImpressionForItem()
- 位置: L1871-1895
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (item.frequency)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (impressionsString === "multiProfileMessageImpressions")` → `this._storage.setSharedMessageImpressions()`
- 条件付き依存: `if (!(impressionsString === "multiProfileMessageImpressions"))` → `this._storage.set()`
- 参照: `item.frequency`, `item.id`

## _ASRouter.getLongestPeriod()
- 位置: L1905-1910
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.frequency.custom.sort()`
- 参照: `a.period`, `b.period`, `item.frequency`, `item.frequency.custom`, `item.frequency.custom.sort((a, b) => b.period - a.period)[0].period`

## _ASRouter.cleanupImpressions()
- 位置: L1925-1952
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cleanupImpressionsForItems()`, `this.setState()`
- 条件付き依存: `if (lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles)` → `this._cleanupMultiProfileImpressions()`
- 参照: `lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles`, `state.groups`, `state.messages`

## _ASRouter._cleanupImpressionsForItems()
- 位置: L1966-2047
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Date.now()`, `Object.keys()`, `items.filter()`
- 条件付き依存: `if (!Array.isArray(impressions[id]) || !impressions[id].length)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!item)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!item)` → `impressions[id].filter()`
- 条件付き依存: `if (!item.frequency)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (item.frequency.custom && !item.frequency.lifetime)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (item.frequency.custom && !item.frequency.lifetime)` → `impressions[id].filter()`
- 条件付き依存: `if (item.frequency.custom && !item.frequency.lifetime)` → `this.getLongestPeriod()`
- 条件付き依存: `if (needsUpdate)` → `this._storage.set()`
- 参照: `impressionsForItem.length`, `impressions[id].length`, `item.frequency`, `item.frequency.custom`, `item.frequency.lifetime`, `x.id`

## _ASRouter._cleanupMultiProfileImpressions()
- 位置: L2063-2094
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Date.now()`, `Object.keys()`, `items.filter()`
- 条件付き依存: `if (!Array.isArray(impressions[id]) || !impressions[id].length)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!Array.isArray(impressions[id]) || !impressions[id].length)` → `this._storage.setSharedMessageImpressions()`
- 条件付き依存: `if (!item)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!item)` → `impressions[id].filter()`
- 条件付き依存: `if (!item)` → `this._storage.setSharedMessageImpressions()`
- 参照: `impressionsForItem.length`, `impressions[id].length`, `x.id`

## _ASRouter.shouldShowMessagesToProfile()
- 位置: L2098-2117
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles`, `lazy.ASRouterTargeting.Environment.currentProfileId`, `lazy.ASRouterTargeting.Environment.hasSelectableProfiles`, `lazy.disableSingleProfileMessaging`, `lazy.messagingProfileId`

## _ASRouter.handleMessageRequest()
- 位置: L2119-2228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `lazy.ASRouterPreferences.console.debug()`, `lazy.ASRouterPreferences.console.trace()`, `lazy.ASRouterTargeting.findMatchingMessage()`, `this._getMessagesContext()`, `this._shouldSkipForAutomation()`, `this.hasValidProfileScope()`, `this.isBelowFrequencyCaps()`, `this.isUnblockedMessage()`, `this.shouldShowMessagesToProfile()`, `this.state.messages.filter()`
- 条件付き依存: `if (!this.shouldShowMessagesToProfile())` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (this._shouldSkipForAutomation(m))` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (provider && m.provider !== provider)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (template && m.template !== template)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (triggerId)` → `lazy.ASRouterTargeting.getMessageTriggers()`
- 条件付き依存: `if (!triggers.length)` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (triggerId)` → `triggers.some()`
- 条件付き依存: `if (!triggers.some(t => t.id === triggerId))` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!this.hasValidProfileScope(m))` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!this.isUnblockedMessage(m))` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!this.isBelowFrequencyCaps(m))` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (shouldCache !== false)` → `JEXL_PROVIDER_CACHE.has()`
- 参照: `m.id`, `m.provider`, `m.skip_in_tests`, `m.template`, `messages.length`, `t.id`, `this._handleTargetingError`, `triggers.length`

## _ASRouter.setMessageById()
- 位置: L2230-2232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getMessageById()`, `this.routeCFRMessage()`

## _ASRouter.blockMessageById()
- 位置: L2234-2288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `idsToBlock.forEach()`, `lazy.ASRouterPreferences.console.debug()`, `lazy.ASRouterPreferences.console.trace()`, `messageBlockList.includes()`, `state.messages.find()`, `this._storage.set()`, `this.setState()`
- 条件付き依存: `if (!messageBlockList.includes(idToBlock))` → `messageBlockList.push()`
- 条件付き依存: `if ( message && lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles && message.profileScope === PROFILE_MESSAGE_SCOPE.SINGLE )` → `this._storage.setSharedMessageBlocked()`
- 条件付き依存: `if ( message && lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles && message.profileScope === PROFILE_MESSAGE_SCOPE.SINGLE )` → `multiProfileMessageBlocklist.includes()`
- 条件付き依存: `if (!multiProfileMessageBlocklist.includes(idToBlock))` → `multiProfileMessageBlocklist.push()`
- 参照: `PROFILE_MESSAGE_SCOPE.SINGLE`, `lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles`, `m.id`, `message.campaign`, `message.profileScope`, `state.messageBlockList`, `state.messageImpressions`, `state.multiProfileMessageBlocklist`, `state.multiProfileMessageImpressions`

## _ASRouter.unblockMessageById()
- 位置: L2290-2320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `idsToUnblock .map()`, `idsToUnblock .map(id => state.messages.find(m => m.id === id)) // Remove all `id`s from the message block list .forEach()`, `messageBlockList.indexOf()`, `messageBlockList.splice()`, `state.messages.find()`, `this._storage.set()`, `this.setState()`
- 条件付き依存: `if ( lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles && message.profileScope === PROFILE_MESSAGE_SCOPE.SINGLE )` → `this._storage.setSharedMessageBlocked()`
- 条件付き依存: `if ( lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles && message.profileScope === PROFILE_MESSAGE_SCOPE.SINGLE )` → `multiProfileMessageBlocklist.splice()`
- 条件付き依存: `if ( lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles && message.profileScope === PROFILE_MESSAGE_SCOPE.SINGLE )` → `multiProfileMessageBlocklist.indexOf()`
- 参照: `PROFILE_MESSAGE_SCOPE.SINGLE`, `lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles`, `m.id`, `message.campaign`, `message.id`, `message.profileScope`, `state.messageBlockList`, `state.multiProfileMessageBlocklist`

## _ASRouter.resetGroupsState()
- 位置: L2322-2329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._storage.set()`, `this.setState()`

## _ASRouter.resetMessageState()
- 位置: L2331-2356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._storage.set()`, `this.setState()`
- 条件付き依存: `if (lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles)` → `this._storage.resetSharedMessageStorage()`
- 参照: `lazy.ASRouterTargeting.Environment.canCreateSelectableProfiles`

## _ASRouter.resetScreenImpressions()
- 位置: L2358-2362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._storage.set()`, `this.setState()`

## _ASRouter.editState()
- 位置: async L2377-2418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `this.setState()`
- 条件付き依存: `if (key === "multiProfileMessageImpressions")` → `Object.keys()`
- 条件付き依存: `if (key === "multiProfileMessageImpressions")` → `this._storage.setSharedMessageImpressions()`
- 条件付き依存: `if (!(key === "multiProfileMessageImpressions"))` → `this._storage.set()`
- 参照: `lazy.ASRouterPreferences.devtoolsEnabled`, `this.state.multiProfileMessageImpressions`

## _ASRouter._validPreviewEndpoint()
- 位置: L2420-2437
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.ALLOWLIST_HOSTS[endpoint.host])` → `console.error()`
- 条件付き依存: `if (endpoint.protocol !== "https:")` → `console.error()`
- 参照: `endpoint.host`, `endpoint.protocol`, `this.ALLOWLIST_HOSTS`

## _ASRouter._loadAllowHosts()
- 位置: L2439-2441
- 役割: (未記入)
- 触るとき: (未記入)

## _ASRouter._triggerHandler()
- 位置: L2444-2450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendTriggerMessage()`
- 条件付き依存: `if (lazy.BrowserHandler.kiosk)` → `Promise.resolve()`
- 参照: `lazy.BrowserHandler.kiosk`

## _ASRouter.setAttributionString()
- 位置: L2458-2460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MacAttribution.setAttributionString()`

## _ASRouter.forceAttribution()
- 位置: async L2470-2492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.set()`, `encodeURIComponent()`, `lazy.AttributionCode._clearCache()`, `lazy.AttributionCode.allowedCodeKeys .map()`, `lazy.AttributionCode.allowedCodeKeys .map(key => `${key}=${encodeURIComponent(data[key] || "")}`) .join()`, `lazy.AttributionCode.getAttrDataAsync()`, `this._updateMessageProviders()`, `this.loadMessagesFromAllProviders()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `lazy.AttributionCode.writeAttributionFile()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `encodeURIComponent()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `this.setAttributionString()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `encodeURIComponent()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.env`

## _ASRouter.sendPBNewTabMessage()
- 位置: async L2494-2539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.messagingSystem.messageRequestTime.start()`, `Glean.messagingSystem.messageRequestTime.stopAndAccumulate()`, `Services.prefs.getBoolPref()`, `state.messages.filter()`, `this.handleMessageRequest()`, `this.loadMessagesFromAllProviders()`, `this.setState()`
- 条件付き依存: `if (hideDefault)` → `this.setState()`
- 条件付き依存: `if (hideDefault)` → `state.messages.filter()`
- 参照: `PromoInfo[m.content?.promoType]?.enabledPref`, `m.content?.promoType`, `m.template`, `m.type`
- XPCOM: `Services.prefs`

## _ASRouter._recordReachEvent()
- 位置: L2541-2576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.messagingExperiments[`reach${featureName}`].record()`, `MessageLoaderUtils._recordedReachIds.add()`, `MessageLoaderUtils._recordedReachIds.has()`, `lazy.ASRouterPreferences.console.error()`, `lazy.ASRouterPreferences.console.log()`, `message._nimbusFeature .replace()`, `message._nimbusFeature .replace(/-/g, "_") .split()`, `message._nimbusFeature .replace(/-/g, "_") .split("_") .map()`, `message._nimbusFeature .replace(/-/g, "_") .split("_") .map(word => word[0].toUpperCase() + word.slice(1)) .join()`, `word.slice()`, `word[0].toUpperCase()`
- 参照: `Glean.messagingExperiments`, `message._branchSlug`, `message._nimbusSlug`, `message._reachId`, `message.id`

## _ASRouter.hasMessageForTrigger()
- 位置: L2594-2603
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterTargeting.getMessageTriggers()`, `lazy.ASRouterTargeting.getMessageTriggers(m).some()`, `this.isBelowFrequencyCaps()`, `this.isUnblockedMessage()`, `this.state.messages.some()`
- 参照: `t.id`

## _ASRouter.sendTriggerMessage()
- 位置: async L2623-2723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.messagingSystem.messageRequestTime.start()`, `Glean.messagingSystem.messageRequestTime.stopAndAccumulate()`, `browser?.documentGlobal?.document?.documentElement.hasAttribute()`, `lazy.ASRouterPreferences.console.debug()`, `this.handleMessageRequest()`, `this.routeCFRMessage()`
- 条件付き依存: `if (!skipLoadingMessages)` → `this.loadMessagesFromAllProviders()`
- 条件付き依存: `if (trigger && browser?.constructor.name === "MozBrowser")` → `Object.prototype.hasOwnProperty.call()`
- 条件付き依存: `if (typeof trigger.context === "object")` → `isThirdPartyPage()`
- 条件付き依存: `if (typeof trigger.context === "object")` → `lazy.AIWindow?.isAIWindowActive()`
- 条件付き依存: `if (message.recordReach && message._reachId)` → `this._recordReachEvent()`
- 条件付き依存: `if (!(message.recordReach && message._reachId))` → `lazy.ASRouterPreferences.console.debug()`
- 条件付き依存: `if (!(message.recordReach && message._reachId))` → `nonReachMessages.push()`
- 条件付き依存: `if (_nimbusFeature)` → `lazy.NimbusFeatures[_nimbusFeature].recordExposureEvent()`
- 参照: `browser.documentGlobal`, `browser.documentGlobal.gBrowser?.currentURI`, `browser.documentGlobal.gBrowser?.selectedBrowser`, `browser?.constructor.name`, `lazy.NimbusFeatures`, `message._reachId`, `message.recordReach`, `trigger.context`, `trigger.context.browserIsSelected`, `trigger.context.isAIWindow`, `trigger.context.onThirdPartyPage`, `trigger.id`, `trigger.param`

## _ASRouter._onExperimentEnrollmentsUpdated()
- 位置: async L2725-2740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterTriggerListeners.get()`, `this.loadMessagesFromAllProviders()`, `this.state.providers.find()`
- 条件付き依存: `if (lazy.ASRouterTriggerListeners.get("nimbusUpdate")?.initialized)` → `Services.wm.getMostRecentBrowserWindow()`
- 条件付き依存: `if (lazy.ASRouterTriggerListeners.get("nimbusUpdate")?.initialized)` → `this.sendTriggerMessage()`
- 参照: `Services.wm.getMostRecentBrowserWindow()?.gBrowser?.selectedBrowser`, `experimentProvider?.enabled`, `lazy.ASRouterTriggerListeners.get("nimbusUpdate")?.initialized`, `p.id`
- XPCOM: `Services.wm`

## _ASRouter.forcePBWindow()
- 位置: async L2742-2769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MessageLoaderUtils._delocalizeValues()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `browser.documentGlobal.openTrustedLinkIn()`, `lazy.setTimeout()`, `privateBrowserOpener.browsingContext.currentWindowGlobal .getActor()`, `privateBrowserOpener.browsingContext.currentWindowGlobal .getActor("AboutPrivateBrowsing") .sendAsyncMessage()`
- XPCOM: `Services.scriptSecurityManager`
