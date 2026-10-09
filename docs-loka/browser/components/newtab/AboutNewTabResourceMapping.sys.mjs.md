# browser/components/newtab/AboutNewTabResourceMapping.sys.mjs

source: browser/components/newtab/AboutNewTabResourceMapping.sys.mjs
source-hash: d010585837493676a168ce0b88cdf12afe283148
lines: 1158

## <module>
- 役割: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `XPCOMUtils.declareLazy()`, `console.createInstance()`

## addonVersion()
- 位置: L122-124
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._addonVersion`

## addonIsXPI()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._addonIsXPI`

## init()
- 位置: L142-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.addAddonListener()`, `this.getBuiltinAddonVersion()`, `this.logger.debug()`, `this.registerNewTabResources()`
- 参照: `Services.appinfo.inSafeMode`, `this.inSafeMode`, `this.initialized`, `this.newTabAsAddonDisabled`
- XPCOM: `Services.appinfo` / `Services.prefs`

## addAddonListener()
- 位置: L172-190
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._addonListener && !this.newTabAsAddonDisabled)` → `lazy.AddonManager.addInstallListener()`
- 参照: `addonInstallListener.onInstallPostponed`, `this._addonListener`, `this.newTabAsAddonDisabled`

## addonInstallListener.onInstallPostponed()
- 位置: L179-186
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (install.addon.id === BUILTIN_ADDON_ID)` → `this.logger.debug()`
- 条件付き依存: `if (install.addon.id === BUILTIN_ADDON_ID)` → `lazy.AboutHomeStartupCache.clearCacheAndUninit()`
- 参照: `install.addon.id`

## getBuiltinAddonVersion()
- 位置: L199-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonManager.getBuiltinAddonVersion()`, `this.logger.warn()`
- 参照: `this._builtinVersion`

## isXPIInCurrentProfile()
- 位置: L212-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rootURI .QueryInterface()`, `rootURI .QueryInterface(Ci.nsIJARURI) .JARFile.QueryInterface()`, `this.logger.error()`
- 条件付き依存: `if (!xpiIsInsideProfile)` → `this.logger.warn()`
- 参照: `Ci.nsIFileURL`, `Ci.nsIJARURI`, `PathUtils.profileDir`, `xpiFile.parent.parent.path`
- XPCOM: [`nsIFileURL`](../../../netwerk/base/nsIFileURL.idl.md) / `nsIJARURI`

## getActiveAddonInfo()
- 位置: L251-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByID()`
- 参照: `policy?.extension`

## getPreferredMapping()
- 位置: L272-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.vc.compare()`, `rootURI?.spec.endsWith()`, `this.getActiveAddonInfo()`, `this.isXPIInCurrentProfile()`
- 条件付き依存: `if (!rootURI || inSafeMode || newTabAsAddonDisabled || shouldUninstallXPI)` → `lazy.resProto.getSubstitution()`
- 条件付き依存: `if (!rootURI || inSafeMode || newTabAsAddonDisabled || shouldUninstallXPI)` → `Services.io.newURI()`
- 参照: `lazy.AddonSettings.REQUIRE_SIGNING`, `lazy.trainhopAddonDeploymentXPIVersion`, `this._builtinVersion`
- XPCOM: `Services.io` / `Services.vc`

## registerNewTabResources()
- 位置: L339-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.addonReadySuccess.set()`, `Glean.newtab.addonXpiUsed.set()`, `Services.io.newURI()`, `lazy.aboutRedirector.wrappedJSObject.notifyBuiltInAddonInitialized()`, `lazy.aomStartup.registerChrome()`, `lazy.resProto.setSubstitutionWithFlags()`, `this.getPreferredMapping()`, `this.logger.debug()`, `this.logger.error()`, `this.logger.log()`
- 条件付き依存: `if (isXPI)` → `this.registerFluentSources()`
- 条件付き依存: `if (isXPI)` → `this.registerMetricsFromJson()`
- 条件付き依存: `if (isXPI)` → `this.reevaluateNimbusRecipes()`
- 参照: `AppConstants.MOZ_APP_VERSION_DISPLAY`, `Ci.nsISubstitutingProtocolHandler.ALLOW_CONTENT_ACCESS`, `rootURI.spec`, `this._addonIsXPI`, `this._addonVersion`, `this._chromeHandle`, `this._rootURISpec`, `this.newTabAsAddonDisabled`
- XPCOM: [`nsISubstitutingProtocolHandler`](../../../netwerk/protocol/res/nsISubstitutingProtocolHandler.idl.md) / `Services.io`

## registerFluentSources()
- 位置: async L389-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `fetch()`, `fetch(rootURI.resolve("/locales/supported-locales.json")).then()`, `r.json()`, `rootURI.resolve()`, `shadowSources.push()`, `this._buildNewtabFileSource()`, `this._langpackShadowSources.add()`, `this._langpackShadowSources.has()`, `this._updateFluentSourcesRegistration()`, `this.logger.error()`
- 条件付き依存: `if (shadowSources.length)` → `L10nRegistry.getInstance().registerSources()`
- 条件付き依存: `if (shadowSources.length)` → `L10nRegistry.getInstance()`
- 参照: `lazy.Langpack.activeLangpackIds`, `rootURI.spec`, `shadowSources.length`, `this._langpackShadowSources`, `this._supportedLocales`
- XPCOM: `Services.obs`

## reevaluateNimbusRecipes()
- 位置: async L457-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExperimentAPI._rsLoader.finishedUpdating()`, `lazy.ExperimentAPI._rsLoader.updateRecipes()`, `this.logger.error()`

## _updateFluentSourcesRegistration()
- 位置: L476-500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `L10nRegistry.getInstance()`, `registry.hasSource()`, `this._buildNewtabFileSource()`, `this._supportedLocales.intersection()`
- 条件付き依存: `if (registry.hasSource(FLUENT_SOURCE_NAME))` → `registry.updateSources()`
- 条件付き依存: `if (registry.hasSource(FLUENT_SOURCE_NAME))` → `this.logger.debug()`
- 条件付き依存: `if (registry.hasSource(FLUENT_SOURCE_NAME))` → `Array.from()`
- 条件付き依存: `if (!(registry.hasSource(FLUENT_SOURCE_NAME)))` → `registry.registerSources()`
- 条件付き依存: `if (!(registry.hasSource(FLUENT_SOURCE_NAME)))` → `this.logger.debug()`
- 条件付き依存: `if (!(registry.hasSource(FLUENT_SOURCE_NAME)))` → `Array.from()`
- 参照: `Services.locale.availableLocales`
- XPCOM: `Services.locale`

## _buildNewtabFileSource()
- 位置: L514-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._supportedLocales.intersection()`
- 参照: `Services.locale.availableLocales`
- XPCOM: `Services.locale`

## _registerLangpackShadow()
- 位置: L542-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `L10nRegistry.getInstance()`, `L10nRegistry.getInstance().registerSources()`, `this._buildNewtabFileSource()`, `this._langpackShadowSources.add()`, `this._langpackShadowSources.has()`, `this.logger.debug()`

## _unregisterLangpackShadow()
- 位置: L565-575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `L10nRegistry.getInstance()`, `L10nRegistry.getInstance().removeSources()`, `this._langpackShadowSources.delete()`, `this._langpackShadowSources.has()`, `this.logger.debug()`

## _updateLangpackShadows()
- 位置: L583-591
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `L10nRegistry.getInstance()`, `registry.updateSources()`, `this._buildNewtabFileSource()`
- 参照: `this._langpackShadowSources`

## observe()
- 位置: L593-643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this._updateFluentSourcesRegistration()`, `this._updateLangpackShadows()`
- 条件付き依存: `if (langpackId)` → `this._registerLangpackShadow()`
- 条件付き依存: `if (langpackId)` → `this._unregisterLangpackShadow()`
- 参照: `subject?.wrappedJSObject?.langpack?.langpackId`, `this._inObserveHandler`
- XPCOM: `Services.obs`

## registerMetricsFromJson()
- 位置: L649-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppConstants.MOZ_APP_VERSION.match()`, `lazy.NewTabGleanUtils.registerMetricsAndPings()`, `this.logger.debug()`

## _isAppShuttingDown()
- 位置: L665-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.startup.isInOrBeyondShutdownPhase()`
- 参照: `Ci.nsIAppStartup.SHUTDOWN_PHASE_APPSHUTDOWNCONFIRMED`, `Services.startup.attemptingQuit`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.startup`

## scheduleUpdateTrainhopAddonState()
- 位置: L674-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateAddonStateDeferredTask.arm()`, `this.logger.debug()`
- 条件付き依存: `if (!this._updateAddonStateDeferredTask)` → `this.logger.debug()`
- 条件付き依存: `if (!this._updateAddonStateDeferredTask)` → `this._isAppShuttingDown()`
- 条件付き依存: `if (this._isAppShuttingDown())` → `this.logger.warn()`
- 条件付き依存: `if (!this._updateAddonStateDeferredTask)` → `this.updateTrainhopAddonState().catch()`
- 条件付き依存: `if (!this._updateAddonStateDeferredTask)` → `this.updateTrainhopAddonState()`
- 条件付き依存: `if (!this._updateAddonStateDeferredTask)` → `this.logger.warn()`
- 条件付き依存: `if (!this._updateAddonStateDeferredTask)` → `lazy.NimbusFeatures[TRAINHOP_NIMBUS_DEPLOYMENT_FEATURE_ID].onUpdate()`
- 条件付き依存: `if (!this._updateAddonStateDeferredTask)` → `this._updateAddonStateDeferredTask.arm()`
- 参照: `lazy.DeferredTask`, `lazy.NimbusFeatures`, `lazy.trainhopAddonScheduledUpdateDelay`, `lazy.trainhopAddonScheduledUpdateTimeout`, `this._updateAddonStateDeferredTask`

## updateTrainhopAddonState()
- 位置: async L728-895
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.vc.compare()`, `feature.getAllEnrollments()`, `feature.ready()`, `lazy.AddonManager.getAddonByID()`, `this._installTrainhopAddon()`, `this.logger.debug()`
- 条件付き依存: `if (this.inSafeMode)` → `this.logger.debug()`
- 条件付き依存: `if (addon_version)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if ( lazy.trainhopAddonDeploymentXPIVersion !== TRAINHOP_ANY_VERSION_SENTINEL )` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (addon_version === null && xpi_download_path === null)` → `this.uninstallAddon()`
- 条件付き依存: `if (!this._addonIsXPI && addon)` → `Services.vc.compare()`
- 条件付き依存: `if ( this._builtinVersion && Services.vc.compare(this._builtinVersion, addon.version) >= 0 )` → `this.uninstallAddon()`
- 条件付き依存: `if ( addon_version !== null && Services.vc.compare(addon.version, addon_version) > 0 )` → `this.uninstallAddon()`
- 条件付き依存: `if ( lazy.AddonSettings.REQUIRE_SIGNING && addon.signedState !== lazy.AddonManager.SIGNEDSTATE_SYSTEM )` → `this.uninstallAddon()`
- 条件付き依存: `if (changed)` → `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (changed)` → `this.logger.debug()`
- 条件付き依存: `if (changed)` → `lazy.AboutHomeStartupCache.clearCacheAndUninit()`
- 条件付き依存: `if ( this._addonIsXPI && this._addonVersion === addon_version && winningEnrollment )` → `this.logger.debug()`
- 条件付き依存: `if ( this._addonIsXPI && this._addonVersion === addon_version && winningEnrollment )` → `feature.recordExposureEvent()`
- 条件付き依存: `if (addon?.version === addon_version)` → `this.logger.warn()`
- 条件付き依存: `if (!lazy.trainhopAddonXPIBaseURL)` → `this.logger.debug()`
- 条件付き依存: `if (addon_version == null && xpi_download_path == null)` → `this.logger.debug()`
- 条件付き依存: `if (addon_version == null)` → `this.logger.warn()`
- 条件付き依存: `if (xpi_download_path == null)` → `this.logger.warn()`
- 参照: `addon.signedState`, `addon.version`, `addon?.version`, `enrollment.value`, `lazy.AddonManager.SIGNEDSTATE_SYSTEM`, `lazy.AddonSettings.REQUIRE_SIGNING`, `lazy.NimbusFeatures`, `lazy.trainhopAddonDeploymentXPIVersion`, `lazy.trainhopAddonXPIBaseURL`, `this._addonIsXPI`, `this._addonVersion`, `this._builtinVersion`, `this.inSafeMode`, `winningEnrollment.meta.slug`, `winningEnrollment.value.addon_version`, `winningEnrollment?.value.addon_version`, `winningEnrollment?.value.xpi_download_path`
- XPCOM: `Services.prefs` / `Services.vc`

## _installTrainhopAddon()
- 位置: async L914-1079
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await lazy.AddonManager.getAllInstalls()) .filter()`, `Promise.withResolvers()`, `Services.vc.compare()`, `lazy.AddonManager.getAddonByID()`, `lazy.AddonManager.getAllInstalls()`, `lazy.AddonManager.getInstallForURL()`, `newInstall.addListener()`, `newInstall.install()`, `this._isAppShuttingDown()`, `this.logger.error()`, `this.logger.log()`
- 条件付き依存: `if ( this._builtinVersion && Services.vc.compare(this._builtinVersion, trainhopAddonVersion) >= 0 )` → `this.logger.warn()`
- 条件付き依存: `if ( addon?.version && Services.vc.compare(addon.version, trainhopAddonVersion) >= 0 )` → `this.logger.warn()`
- 条件付き依存: `if ( pendingInstall && Services.vc.compare(pendingInstall.addon.version, trainhopAddonVersion) >= 0 )` → `this.logger.debug()`
- 条件付き依存: `if (this._isAppShuttingDown())` → `this.logger.warn()`
- 条件付き依存: `if (forceRestartlessInstall)` → `this.logger.debug()`
- 条件付き依存: `if (!(forceRestartlessInstall))` → `this.logger.debug()`
- 参照: `addon.version`, `addon?.version`, `deferred.promise`, `install.addon?.id`, `install.state`, `lazy.AddonManager.STATE_POSTPONED`, `pendingInstall.addon.version`, `this._builtinVersion`
- XPCOM: `Services.vc`

## onDownloadEnded()
- 位置: L980-1009
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.logger.debug()`
- 条件付き依存: `if ( newInstall.addon.id !== BUILTIN_ADDON_ID || newInstall.addon.version !== trainhopAddonVersion )` → `deferred.reject()`
- 条件付き依存: `if ( newInstall.addon.id !== BUILTIN_ADDON_ID || newInstall.addon.version !== trainhopAddonVersion )` → `newInstall.cancel()`
- 条件付き依存: `if ( lazy.AddonSettings.REQUIRE_SIGNING && newInstall.addon.signedState !== lazy.AddonManager.SIGNEDSTATE_SYSTEM )` → `deferred.reject()`
- 条件付き依存: `if ( lazy.AddonSettings.REQUIRE_SIGNING && newInstall.addon.signedState !== lazy.AddonManager.SIGNEDSTATE_SYSTEM )` → `newInstall.cancel()`
- 参照: `lazy.AddonManager.SIGNEDSTATE_SYSTEM`, `lazy.AddonSettings.REQUIRE_SIGNING`, `newInstall.addon.id`, `newInstall.addon.signedState`, `newInstall.addon.version`

## onInstallPostponed()
- 位置: L1010-1031
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isAppShuttingDown()`, `this.logger.debug()`
- 条件付き依存: `if ( forceRestartlessInstall && !this.initialized && !isAppShuttingDown )` → `this.logger.debug()`
- 条件付き依存: `if ( forceRestartlessInstall && !this.initialized && !isAppShuttingDown )` → `newInstall.continuePostponedInstall()`
- 条件付き依存: `if (!( forceRestartlessInstall && !this.initialized && !isAppShuttingDown ))` → `this.logger.debug()`
- 条件付き依存: `if (forceRestartlessInstall)` → `this.logger.warn()`
- 条件付き依存: `if (!( forceRestartlessInstall && !this.initialized && !isAppShuttingDown ))` → `deferred.resolve()`
- 参照: `this.initialized`

## onInstallEnded()
- 位置: L1032-1038
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.logger.debug()`
- 条件付き依存: `if (forceRestartlessInstall)` → `this.logger.debug()`
- 条件付き依存: `if (forceRestartlessInstall)` → `deferred.resolve()`

## onDownloadCancelled()
- 位置: L1039-1045
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.reject()`

## onDownloadFailed()
- 位置: L1046-1050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.reject()`

## onInstallCancelled()
- 位置: L1051-1057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.reject()`

## onInstallFailed()
- 位置: L1058-1062
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.reject()`

## uninstallAddon()
- 位置: async L1095-1105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (uninstallReason)` → `this.logger.info()`
- 条件付き依存: `if (addon && addon.permissions & lazy.AddonManager.PERM_CAN_UNINSTALL)` → `addon.uninstall()`
- 参照: `addon.permissions`, `lazy.AddonManager.PERM_CAN_UNINSTALL`

## firstStartupNewProfile()
- 位置: async L1115-1146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExperimentAPI.ready()`, `nimbusFeature.getAllVariables()`, `nimbusFeature.ready()`, `this.logger.debug()`, `this.updateTrainhopAddonState()`
- 条件付き依存: `if (this.initialized)` → `this.logger.error()`
- 条件付き依存: `if (!enabled)` → `this.logger.debug()`
- 参照: `lazy.AddonManager.readyPromise`, `lazy.NimbusFeatures`, `this.initialized`
