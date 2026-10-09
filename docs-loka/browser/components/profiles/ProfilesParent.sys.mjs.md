# browser/components/profiles/ProfilesParent.sys.mjs

source: browser/components/profiles/ProfilesParent.sys.mjs
source-hash: 67bbde85b130c6c1ecfbed24c93378c7899d412a
lines: 343

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ProfilesParent.tab()
- 位置: L30-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.getTabForBrowser()`
- 参照: `this.browsingContext.embedderElement`, `this.browsingContext.topChromeWindow.gBrowser`

## ProfilesParent.#getProfileContent()
- 位置: async L36-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfileAge()`, `Promise.all()`, `SelectableProfileService.getAllProfiles()`, `SelectableProfileService.init()`, `Services.prefs.getBoolPref()`, `currentProfile.hasDesktopShortcut()`, `currentProfile.toContentSafeObject()`, `p.toContentSafeObject()`, `profiles.map()`, `this.getSafeForContentThemes()`
- 参照: `AppConstants.platform`, `Cu.isInAutomation`, `SelectableProfileService.currentProfile`, `profileAge.created`
- XPCOM: `Services.prefs`

## ProfilesParent.receiveMessage()
- 位置: async L54-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( await db.executeCached(bookmarksQuery, bookmarksQueryParams) )[0].getResultByIndex()`, `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Glean.profilesDelete.cancel.record()`, `Glean.profilesDelete.displayed.record()`, `Glean.profilesExisting.deleted.record()`, `Glean.profilesExisting.displayed.record()`, `Glean.profilesNew.displayed.record()`, `Promise.all()`, `SelectableProfileService.currentProfile.setAvatar()`, `SelectableProfileService.currentProfile.toContentSafeObject()`, `SelectableProfileService.deleteCurrentProfile()`, `SelectableProfileService.init()`, `Services.io.newURI()`, `Services.obs.notifyObservers()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `Services.startup.quit()`, `console.error()`, `db.executeCached()`, `gBrowser.removeTab()`, `gBrowser.selectedBrowser.documentGlobal.matchMedia()`, `lazy.BackupService.init()`, `lazy.BackupService.maybeRemoveFromEnabledListPref()`, `lazy.EveryWindow.readyWindows .flatMap()`, `lazy.EveryWindow.readyWindows .flatMap(win => win.gBrowser.openTabs.length) .reduce()`, `lazy.LoginHelper.getAllUserFacingLogins()`, `lazy.PlacesDBUtils.getEntitiesStatsAndCounts()`, `lazy.PlacesUtils.promiseDBConnection()`, `lazy.formAutofillStorage.addresses.getAll()`, `lazy.formAutofillStorage.creditCards.getAll()`, `lazy.formAutofillStorage.initialize()`, `profile.hasDesktopShortcut()`, `stats.find()`, `this.#getProfileContent()`, `this.browsingContext.embedderElement.loadURI()`, `this.enableTheme()`
- 条件付き依存: `if (source === "about:newprofile")` → `Glean.profilesNew.closed.record()`
- 条件付き依存: `if (source === "about:newprofile")` → `GleanPings.profiles.submit()`
- 条件付き依存: `if (source === "about:deleteprofile")` → `Glean.profilesDelete.confirm.record()`
- 条件付き依存: `if (gBrowser.tabs.length === 1)` → `gBrowser.addTrustedTab()`
- 条件付き依存: `if (message.data.source === "about:editprofile")` → `Glean.profilesExisting.learnMore.record()`
- 条件付き依存: `if (message.data.source === "about:newprofile")` → `Glean.profilesNew.learnMore.record()`
- 条件付き依存: `if (source === "about:editprofile")` → `Glean.profilesExisting.closed.record()`
- 条件付き依存: `if (source === "about:editprofile")` → `Glean.profilesExisting.name.record()`
- 条件付き依存: `if (source === "about:newprofile")` → `Glean.profilesNew.name.record()`
- 条件付き依存: `if (shouldEnable)` → `profile.ensureDesktopShortcut()`
- 条件付き依存: `if (shouldEnable)` → `Glean.profilesExisting.shortcut.record()`
- 条件付き依存: `if (!(shouldEnable))` → `profile.removeDesktopShortcut()`
- 条件付き依存: `if (!(shouldEnable))` → `Glean.profilesExisting.shortcut.record()`
- 条件付き依存: `if (source === "about:editprofile")` → `Glean.profilesExisting.avatar.record()`
- 条件付き依存: `if (source === "about:newprofile")` → `Glean.profilesNew.avatar.record()`
- 条件付き依存: `if (source === "about:editprofile")` → `Glean.profilesExisting.theme.record()`
- 条件付き依存: `if (source === "about:newprofile")` → `Glean.profilesNew.theme.record()`
- 条件付き依存: `if (source === "about:newprofile")` → `lazy.ASRouter.sendTriggerMessage()`
- 参照: `(await lazy.LoginHelper.getAllUserFacingLogins()) .length`, `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsISupportsPRBool`, `SelectableProfileService.currentProfile`, `SelectableProfileService.currentProfile.hasCustomAvatar`, `SelectableProfileService.currentProfile.name`, `Services.cookies.cookies.length`, `addresses.length`, `cancelQuit.data`, `creditCards.length`, `gBrowser.selectedBrowser`, `gBrowser.selectedBrowser.documentGlobal.matchMedia( "(-moz-system-dark-theme)" ).matches`, `gBrowser.tabs.length`, `item.entity`, `lazy.ASRouter.waitForInitialized`, `lazy.BackupService.init().postRecoveryComplete`, `lazy.EveryWindow.readyWindows.length`, `lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK`, `lazy.PlacesUtils.tagsFolderId`, `message.data`, `message.data.source`, `message.name`, `profileObj.name`, `stats.find( item => item.entity == "moz_historyvisits" ).count`, `this.browsingContext.embedderElement?.currentURI.displaySpec`, `this.browsingContext.topChromeWindow?.gBrowser`, `this.tab`, `win.gBrowser.openTabs.length`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.cookies` / `Services.io` / `Services.obs` / `Services.scriptSecurityManager` / `Services.startup`

## ProfilesParent.enableTheme()
- 位置: async L291-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectableProfileService.enableTheme()`

## ProfilesParent.getSafeForContentThemes()
- 位置: async L295-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`, `Services.prefs.getBoolPref()`, `lazy.AddonManager.getActiveAddons()`, `lazy.AddonManager.getAddonByID()`, `themes.find()`, `themes.push()`
- 条件付き依存: `if (novaEnabled)` → `lazy.getThemesList()`
- 条件付き依存: `if (novaEnabled)` → `themesList.getThemesInfo()`
- 条件付き依存: `if (!themes.find(t => t.id === currentTheme.id))` → `themes.push()`
- 参照: `SelectableProfileService.currentProfile.theme.themeBg`, `SelectableProfileService.currentProfile.theme.themeFg`, `activeAddons.addons`, `currentTheme.id`, `currentTheme.isActive`, `currentTheme.name`, `t.id`, `theme?.isActive`, `themeObj.colors`, `themeObj.dataL10nId`, `themeObj.dataL10nTitle`, `themeObj.isDark`, `themeObj?.useInAutomation`
- XPCOM: `Services.prefs`
