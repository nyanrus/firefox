# browser/components/distribution.sys.mjs

source: browser/components/distribution.sys.mjs
source-hash: 5f3396dcf6be1541bb5e8a9bda5dcb09702d156f
lines: 678

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## DistributionCustomizer()
- 位置: L26-26
- 役割: (未記入)
- 触るとき: (未記入)

## _iniFile()
- 位置: L29-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `Services.prefs.getBoolPref()`, `iniFile.append()`, `this.__defineGetter__()`
- 条件付き依存: `if (loadFromProfile)` → `iniFile.append()`
- 参照: `Ci.nsIFile`
- XPCOM: [`nsIFile`](shell/nsIShellService.idl.md) / `Services.dirsvc` / `Services.prefs`

## _hasDistributionIni()
- 位置: L52-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `Services.prefs.setBoolPref()`, `Services.prefs.setStringPref()`, `this.__defineGetter__()`, `this._iniFile.exists()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(PREF_CACHED_FILE_EXISTENCE))` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(PREF_CACHED_FILE_EXISTENCE))` → `Cc["@mozilla.org/startupcacheinfo;1"].getService()`
- 条件付き依存: `if ( knownForVersion == AppConstants.MOZ_APP_VERSION && (Cu.isInAutomation || Cc["@mozilla.org/startupcacheinfo;1"].getService( Ci.nsIStartupCacheInfo ).FoundDis...)` → `Services.prefs.getBoolPref()`
- 参照: `AppConstants.MOZ_APP_VERSION`, `Cc["@mozilla.org/startupcacheinfo;1"].getService( Ci.nsIStartupCacheInfo ).FoundDiskCacheOnInit`, `Ci.nsIStartupCacheInfo`, `Cu.isInAutomation`
- XPCOM: `nsIStartupCacheInfo` / `@mozilla.org/startupcacheinfo;1` → `nsIStartupCacheInfo` (startupcache/components.conf) / `Services.prefs`

## _ini()
- 位置: L81-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.__defineGetter__()`
- 条件付き依存: `if (this._hasDistributionIni)` → `Cc["@mozilla.org/xpcom/ini-parser-factory;1"] .getService(Ci.nsIINIParserFactory) .createINIParser()`
- 条件付き依存: `if (this._hasDistributionIni)` → `Cc["@mozilla.org/xpcom/ini-parser-factory;1"] .getService()`
- 条件付き依存: `if (e.result == Cr.NS_ERROR_FILE_NOT_FOUND)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!(e.result == Cr.NS_ERROR_FILE_NOT_FOUND))` → `console.error()`
- 参照: `Ci.nsIINIParserFactory`, `Cr.NS_ERROR_FILE_NOT_FOUND`, `e.result`, `this._hasDistributionIni`, `this._ini`, `this._iniFile`
- XPCOM: [`nsIINIParserFactory`](../../xpcom/ds/nsIINIParser.idl.md) / `@mozilla.org/xpcom/ini-parser-factory;1` / `Services.prefs`

## _locale()
- 位置: L105-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.__defineGetter__()`
- 参照: `Services.locale.requestedLocale`, `this._locale`
- XPCOM: `Services.locale`

## _language()
- 位置: L111-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.__defineGetter__()`, `this._locale.split()`
- 参照: `this._language`

## _removeDistributionBookmarks()
- 位置: async L117-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.bookmarks.fetch()`, `lazy.PlacesUtils.bookmarks.remove()`, `lazy.PlacesUtils.bookmarks.remove(bookmark).catch()`, `lazy.PlacesUtils.bookmarks.remove(folder).catch()`
- 参照: `console.error`

## _parseBookmarksSection()
- 位置: async L131-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this._ini.getKeys(section)).sort()`, `lazy.PlacesUtils.bookmarks.insert()`, `lazy.PlacesUtils.generateGuidWithPrefix()`, `re.exec()`, `this._ini.getKeys()`, `this._parseBookmarksSection()`
- 条件付き依存: `if (m)` → `parseInt()`
- 条件付き依存: `if (m)` → `keys.includes()`
- 条件付き依存: `if (!(keys.includes(key + "." + this._locale)))` → `keys.includes()`
- 条件付き依存: `if (m)` → `this._ini.getString()`
- 条件付き依存: `if (!(m))` → `dump()`
- 条件付き依存: `if (item.icon && item.iconData)` → `lazy.PlacesUtils.favicons .setFaviconForPage()`
- 条件付き依存: `if (item.icon && item.iconData)` → `Services.io.newURI()`
- 条件付き依存: `if (item.icon && item.iconData)` → `console.error()`
- 参照: `console.error`, `folder.guid`, `item.folderId`, `item.icon`, `item.iconData`, `item.link`, `item.siteLink`, `item.title`, `item.type`, `items[itemIndex].type`, `lazy.PlacesUtils.bookmarks.DEFAULT_INDEX`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `lazy.PlacesUtils.bookmarks.TYPE_SEPARATOR`, `this._language`, `this._locale`
- XPCOM: `Services.io`

## DIST_applyCustomizations()
- 位置: L269-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (!this._ini)` → `this._checkCustomizationComplete()`
- 条件付き依存: `if (!this._prefDefaultsApplied)` → `this.applyPrefDefaults()`
- 参照: `this._customizationsApplied`, `this._ini`, `this._newProfile`, `this._prefDefaultsApplied`
- XPCOM: `Services.prefs`

## applyBookmarks()
- 位置: async L286-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs .getChildList()`, `Services.prefs .getChildList("distribution.yandex") .concat()`, `Services.prefs .getChildList("distribution.yandex") .concat(Services.prefs.getChildList("distribution.mailru")) .concat()`, `Services.prefs.getChildList()`, `this._checkCustomizationComplete()`
- 条件付き依存: `if (prefs.length)` → `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (addon)` → `addon.disable()`
- 条件付き依存: `if (prefs.length)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (prefs.length)` → `this._removeDistributionBookmarks()`
- 条件付き依存: `if (!(prefs.length))` → `this._doApplyBookmarks()`
- 参照: `prefs.length`, `this._bookmarksApplied`
- XPCOM: `Services.prefs`

## _doApplyBookmarks()
- 位置: async L315-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `ProfileAge()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`, `enumToObject()`, `this._ini.getKeys()`, `this._ini.getSections()`, `this._ini.getString()`
- 条件付き依存: `if (sections.BookmarksMenu)` → `this._parseBookmarksSection()`
- 条件付き依存: `if (sections.BookmarksToolbar)` → `this._parseBookmarksSection()`
- 参照: `globalPrefs.id`, `lazy.PlacesUtils.bookmarks.menuGuid`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `profileAge.reset`, `sections.BookmarksMenu`, `sections.BookmarksToolbar`, `sections.Global`, `this._ini`
- XPCOM: `Services.prefs`

## DIST_applyPrefDefaults()
- 位置: L375-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getDefaultBranch()`, `applyPrefsToDefaults()`, `defaults.setStringPref()`, `distroID.startsWith()`, `enumToObject()`, `this._checkCustomizationComplete()`, `this._ini.getKeys()`, `this._ini.getSections()`, `this._ini.getString()`
- 条件付き依存: `if (!this._ini)` → `this._checkCustomizationComplete()`
- 条件付き依存: `if (!sections.Global)` → `this._checkCustomizationComplete()`
- 条件付き依存: `if (!globalPrefs.id)` → `this._checkCustomizationComplete()`
- 条件付き依存: `if ( distroID == "MozillaOnline" && Services.prefs.getBoolPref("distribution.mozillaonline.ignore", false) )` → `Glean.distribution.mozillaonlineIgnored.set()`
- 条件付き依存: `if ( distroID == "MozillaOnline" && Services.prefs.getBoolPref("distribution.mozillaonline.ignore", false) )` → `Services.fog.clearDistribution()`
- 条件付き依存: `if ( distroID == "MozillaOnline" && Services.prefs.getBoolPref("distribution.mozillaonline.ignore", false) )` → `this.__defineGetter__()`
- 条件付き依存: `if ( distroID == "MozillaOnline" && Services.prefs.getBoolPref("distribution.mozillaonline.ignore", false) )` → `this._checkCustomizationComplete()`
- 条件付き依存: `if ( distroID.startsWith("yandex") || distroID.startsWith("mailru") || distroID.startsWith("okru") )` → `this.__defineGetter__()`
- 条件付き依存: `if ( distroID.startsWith("yandex") || distroID.startsWith("mailru") || distroID.startsWith("okru") )` → `this._checkCustomizationComplete()`
- 条件付き依存: `if (globalPrefs.version)` → `defaults.setStringPref()`
- 条件付き依存: `if (globalPrefs.version)` → `this._ini.getString()`
- 条件付き依存: `if (globalPrefs["about." + this._locale])` → `this._ini.getString()`
- 条件付き依存: `if (globalPrefs["about." + this._language])` → `this._ini.getString()`
- 条件付き依存: `if (!(globalPrefs["about." + this._language]))` → `this._ini.getString()`
- 条件付き依存: `if (sections.Preferences)` → `this._ini.getKeys()`
- 条件付き依存: `if (sections.Preferences)` → `this._ini.getString()`
- 条件付き依存: `if (value)` → `preferences.set()`
- 条件付き依存: `if (sections["Preferences-" + this._language])` → `this._ini.getKeys()`
- 条件付き依存: `if (sections["Preferences-" + this._language])` → `this._ini.getString()`
- 条件付き依存: `if (!(value))` → `preferences.delete()`
- 条件付き依存: `if (sections["Preferences-" + this._locale])` → `this._ini.getKeys()`
- 条件付き依存: `if (sections["Preferences-" + this._locale])` → `this._ini.getString()`
- 条件付き依存: `if (sections.LocalizablePreferences)` → `this._ini.getKeys()`
- 条件付き依存: `if (sections.LocalizablePreferences)` → `this._ini.getString()`
- 条件付き依存: `if (value)` → `localizablePreferences.set()`
- 参照: `globalPrefs.id`, `globalPrefs.version`, `sections.Global`, `sections.LocalizablePreferences`, `sections.Preferences`, `this._ini`, `this._language`, `this._locale`, `this._localizablePreferences`, `this._prefDefaultsApplied`
- XPCOM: `Services.fog` / `Services.prefs`

## DIST__checkCustomizationComplete()
- 位置: L500-557
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._newProfile)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (showPersonalToolbar)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (showMenubar)` → `Services.xulStore.setValue()`
- 条件付き依存: `if (this._newProfile)` → `Services.prefs.getDefaultBranch()`
- 条件付き依存: `if (this._newProfile)` → `defaults.getCharPref()`
- 条件付き依存: `if (activeThemeID)` → `lazy.AddonManager.getAddonByID(activeThemeID).then()`
- 条件付き依存: `if (activeThemeID)` → `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (activeThemeID)` → `addon?.enable()`
- 条件付き依存: `if (this._customizationsApplied && prefDefaultsApplied)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (this._bookmarksApplied)` → `Services.obs.notifyObservers()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `this._bookmarksApplied`, `this._customizationsApplied`, `this._ini`, `this._newProfile`, `this._prefDefaultsApplied`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.xulStore`

## applyPrefsToDefaults()
- 位置: L560-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getDefaultBranch()`, `locale.split()`, `parseValue()`
- 条件付き依存: `if (typeof prefValue == "string")` → `prefValue.replace()`
- 条件付き依存: `if (prefName == "general.useragent.locale")` → `defaults.setStringPref()`
- 条件付き依存: `if (!(prefName == "general.useragent.locale"))` → `defaults.setBoolPref()`
- 条件付き依存: `if (!(prefName == "general.useragent.locale"))` → `defaults.setIntPref()`
- 条件付き依存: `if (!(prefName == "general.useragent.locale"))` → `defaults.setStringPref()`
- 参照: `Services.locale.requestedLocale`
- XPCOM: `Services.locale` / `Services.prefs`

## parseValue()
- 位置: L594-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `value.replace()`

## enumToObject()
- 位置: L607-613
- 役割: (未記入)
- 触るとき: (未記入)

## BOOKMARK_GUID_PREFIX()
- 位置: L618-620
- 役割: (未記入)
- 触るとき: (未記入)

## FOLDER_GUID_PREFIX()
- 位置: L621-623
- 役割: (未記入)
- 触るとき: (未記入)

## _ensureCustomizer()
- 位置: L636-642
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._distributionCustomizer)` → `Services.obs.addObserver()`
- 参照: `this._distributionCustomizer`
- XPCOM: `Services.obs`

## observe()
- 位置: L644-654
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == DISTRIBUTION_CUSTOMIZATION_COMPLETE_TOPIC)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (topic == "intl:requested-locales-changed")` → `applyPrefsToDefaults()`
- 参照: `this._distributionCustomizer`, `this._localizablePreferences`
- XPCOM: `Services.obs`

## applyCustomizations()
- 位置: L656-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `customizer.applyCustomizations()`, `this._ensureCustomizer()`
- 条件付き依存: `if (localizablePreferences?.size)` → `Services.obs.addObserver()`
- 参照: `customizer._localizablePreferences`, `localizablePreferences?.size`, `this._localizablePreferences`
- XPCOM: `Services.obs`

## applyBookmarks()
- 位置: L672-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensureCustomizer()`, `this._ensureCustomizer().applyBookmarks()`
