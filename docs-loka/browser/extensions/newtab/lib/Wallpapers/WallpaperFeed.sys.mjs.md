# browser/extensions/newtab/lib/Wallpapers/WallpaperFeed.sys.mjs

source: browser/extensions/newtab/lib/Wallpapers/WallpaperFeed.sys.mjs
source-hash: 5299d6a5027649e4db9047bc2bb7a7603278d21c
lines: 1620

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## WallpaperFeed.constructor()
- 位置: L77-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onSync.bind()`
- 参照: `this._onSync`, `this.applyingWallpaper`, `this.loaded`, `this.wallpaperClient`

## WallpaperFeed.wallpaperDirectory()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`
- 参照: `PathUtils.profileDir`

## WallpaperFeed.libraryEnabled()
- 位置: L92-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isWallpaperLibraryEnabled()`, `this.store?.getState()`
- 参照: `this.store?.getState()?.Prefs?.values`

## WallpaperFeed.libraryDirectory()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`
- 参照: `this.wallpaperDirectory`

## WallpaperFeed.fetch()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`

## WallpaperFeed.formatString()
- 位置: L113-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gNewTabStrings.formatValue()`

## WallpaperFeed.RemoteSettings()
- 位置: L121-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteSettings()`

## WallpaperFeed.writeFile()
- 位置: L128-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.write()`

## WallpaperFeed.writeJSON()
- 位置: L136-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.writeJSON()`

## WallpaperFeed.removeFile()
- 位置: L144-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`

## WallpaperFeed.copyFile()
- 位置: L151-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.copy()`

## WallpaperFeed.wallpaperSetup()
- 位置: async L155-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (wallpapersEnabled)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref( PREF_WALLPAPERS_USER_ENABLED_MIGRATED, false ) )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref( PREF_WALLPAPERS_USER_ENABLED_MIGRATED, false ) )` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (selectedWallpaper)` → `this.store.dispatch()`
- 条件付き依存: `if (selectedWallpaper)` → `ac.SetPref()`
- 条件付き依存: `if (!this.wallpaperClient)` → `this.RemoteSettings()`
- 条件付き依存: `if (wallpapersEnabled)` → `this.wallpaperClient.on()`
- 条件付き依存: `if (wallpapersEnabled)` → `this.updateWallpapers()`
- 参照: `this._onSync`, `this.wallpaperClient`
- XPCOM: `Services.prefs`

## WallpaperFeed.wallpaperTeardown()
- 位置: async L208-214
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._onSync)` → `this.wallpaperClient?.off()`
- 参照: `this._onSync`, `this.loaded`, `this.wallpaperClient`

## WallpaperFeed.onSync()
- 位置: async L216-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.rescueRetiredWallpaper()`, `this.wallpaperSetup()`, `this.wallpaperTeardown()`
- 参照: `event?.data?.current`, `event?.data?.deleted`

## WallpaperFeed.rescueRetiredWallpaper()
- 位置: async L229-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `currentRecords?.some()`, `deletedRecords.find()`, `locks.request()`, `this.#downloadRetiredWallpaper()`, `this.#retiredWallpaperName()`, `this.#saveRetiredWallpaper()`, `this.#shownWallpaperTitle()`
- 参照: `deleted.attachment`, `deleted.title`, `deletedRecords?.length`, `record.title`

## WallpaperFeed.#downloadRetiredWallpaper()
- 位置: async L271-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `contentType.split()`, `contentType.split(";")[0].trim()`, `contentType.startsWith()`, `lazy.Utils.baseAttachmentsURL()`, `response.arrayBuffer()`, `response.headers?.get()`, `this.fetch()`
- 条件付き依存: `if (!response.ok || !contentType.startsWith("image/"))` → `console.error()`
- 参照: `record.attachment.location`, `response.ok`, `response.status`

## WallpaperFeed.#retiredWallpaperName()
- 位置: async L303-315
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (record.fluent_id)` → `this.formatString()`
- 条件付き依存: `if (record.fluent_id)` → `console.error()`
- 参照: `record.fluent_id`, `record.title`

## WallpaperFeed.#saveRetiredWallpaper()
- 位置: async L326-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.makeDirectory()`, `Object.keys()`, `PathUtils.join()`, `Services.prefs.setStringPref()`, `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `Services.uuid.generateUUID().toString().slice()`, `ac.SetPref()`, `buildSavedWallpaperFilename()`, `console.error()`, `this.#copyAppliedWallpaper()`, `this.#shownWallpaperTitle()`, `this.#takeNextWallpaperNumber()`, `this.broadcastWallpaperLibrary()`, `this.store.dispatch()`, `this.writeFile()`
- 条件付き依存: `if (Object.keys(details).length)` → `PathUtils.join()`
- 条件付き依存: `if (Object.keys(details).length)` → `getDetailsFilename()`
- 条件付き依存: `if (Object.keys(details).length)` → `this.writeJSON()`
- 参照: `Object.keys(details).length`, `WALLPAPER_TYPES.Builtin`, `details.fallbackName`, `image.bytes`, `record.attribution`, `record.background_position`, `record.theme`, `record.title`, `this.libraryDirectory`
- XPCOM: `Services.prefs` / `Services.uuid`

## WallpaperFeed.#shownWallpaperTitle()
- 位置: L393-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## WallpaperFeed.updateWallpapers()
- 位置: async L400-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CATEGORY_ORDER.indexOf()`, `Services.prefs.getBoolPref()`, `ac.BroadcastToContent()`, `console.error()`, `records.map()`, `this.broadcastWallpaperLibrary()`, `this.migrateWallpaperLibrary()`, `this.store.dispatch()`, `this.wallpaperClient.get()`, `wallpapers.map()`, `wallpapers.map(wallpaper => wallpaper.category).filter()`
- 条件付き依存: `if (!this.applyingWallpaper)` → `this.broadcastAppliedWallpaper()`
- 条件付き依存: `if ((await this.migrateWallpaperLibrary()) && !this.applyingWallpaper)` → `this.broadcastAppliedWallpaper()`
- 条件付き依存: `if (records.length)` → `lazy.Utils.baseAttachmentsURL()`
- 条件付き依存: `if (records.length)` → `console.error()`
- 条件付き依存: `if (isStartup)` → `this.cleanWallpaperDirectory()`
- 参照: `CATEGORY_ORDER.length`, `at.WALLPAPERS_CATEGORY_SET`, `at.WALLPAPERS_SET`, `record.attachment`, `record.attachment.location`, `record.background_position`, `record.category`, `record.order`, `record.thumbnail`, `records.length`, `this.applyingWallpaper`, `wallpaper.category`
- XPCOM: `Services.prefs`

## WallpaperFeed.initHighlightCounter()
- 位置: L508-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `ac.AlsoToPreloaded()`, `this.store.dispatch()`
- 参照: `at.WALLPAPERS_FEATURE_HIGHLIGHT_COUNTER_INCREMENT`
- XPCOM: `Services.prefs`

## WallpaperFeed.wallpaperSeenEvent()
- 位置: L523-548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `ac.AlsoToPreloaded()`, `ac.OnlyToMain()`, `this.store.dispatch()`
- 参照: `at.SET_PREF`, `at.WALLPAPERS_FEATURE_HIGHLIGHT_COUNTER_INCREMENT`
- XPCOM: `Services.prefs`

## WallpaperFeed.wallpaperUpload()
- 位置: async L567-617
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Blob.isInstance()`, `ac.BroadcastToContent()`, `console.error()`, `locks.request()`, `this.#writeWallpaper()`, `this.store.dispatch()`
- 条件付き依存: `if (!Blob.isInstance(file))` → `console.error()`
- 条件付き依存: `if (wallpaperTheme !== "dark" && wallpaperTheme !== "light")` → `console.error()`
- 条件付き依存: `if ( type !== WALLPAPER_TYPES.Custom && type !== WALLPAPER_TYPES.PictureOfTheDay )` → `console.error()`
- 条件付き依存: `if (!savedPath && !this.applyingWallpaper)` → `this.broadcastAppliedWallpaper()`
- 参照: `WALLPAPER_TYPES.Custom`, `WALLPAPER_TYPES.PictureOfTheDay`, `at.WALLPAPERS_CUSTOM_SET`, `this.applyingWallpaper`

## WallpaperFeed.#writeWallpaper()
- 位置: async L632-763
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.makeDirectory()`, `Object.values()`, `Object.values(details).some()`, `PathUtils.join()`, `Services.prefs.getStringPref()`, `Services.prefs.setStringPref()`, `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `Services.uuid.generateUUID().toString().slice()`, `ac.BroadcastToContent()`, `ac.SetPref()`, `buildSavedWallpaperFilename()`, `console.error()`, `file.arrayBuffer()`, `getWallpaperURL()`, `parseWallpaperFilename()`, `sanitizeSavedName()`, `this.#copyAppliedWallpaper()`, `this.#recordSavedWallpaperEvent()`, `this.#sweepWallpaperDirectory()`, `this.#takeNextWallpaperNumber()`, `this.broadcastWallpaperLibrary()`, `this.getSavedWallpapers()`, `this.store.dispatch()`, `this.writeFile()`
- 条件付き依存: `if (type === WALLPAPER_TYPES.PictureOfTheDay && info.publishedDate)` → `(await this.getSavedWallpapers()).find()`
- 条件付き依存: `if (type === WALLPAPER_TYPES.PictureOfTheDay && info.publishedDate)` → `this.getSavedWallpapers()`
- 条件付き依存: `if (type === WALLPAPER_TYPES.PictureOfTheDay && info.publishedDate)` → `this.#applySavedWallpaper()`
- 条件付き依存: `if ( existing && (await this.#applySavedWallpaper(existing.filename, target)) )` → `PathUtils.join()`
- 条件付き依存: `if (Object.values(details).some(Boolean))` → `PathUtils.join()`
- 条件付き依存: `if (Object.values(details).some(Boolean))` → `getDetailsFilename()`
- 条件付き依存: `if (Object.values(details).some(Boolean))` → `this.writeJSON()`
- 条件付き依存: `if ( replaced && replaced !== filename && parseWallpaperFilename(replaced).kind === "saved" && !this.libraryEnabled )` → `this.#removeLibraryEntry()`
- 参照: `(await this.getSavedWallpapers()).length`, `WALLPAPER_TYPES.PictureOfTheDay`, `at.WALLPAPERS_CUSTOM_SET`, `at.WALLPAPER_SAVED_ADDED`, `existing.filename`, `info.name`, `info.publishedDate`, `parseWallpaperFilename(replaced).kind`, `this.libraryDirectory`, `this.libraryEnabled`, `this.wallpaperDirectory`, `wallpaper.publishedDate`, `wallpaper.type`
- XPCOM: `Services.prefs` / `Services.uuid`

## WallpaperFeed.#takeNextWallpaperNumber()
- 位置: L772-782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## WallpaperFeed.#copyAppliedWallpaper()
- 位置: async L794-808
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `console.error()`, `this.copyFile()`
- 参照: `this.libraryDirectory`, `this.libraryEnabled`, `this.wallpaperDirectory`

## WallpaperFeed.#removeLibraryEntry()
- 位置: async L818-853
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `console.error()`, `getDetailsFilename()`, `getThumbnailFilename()`, `this.removeFile()`
- 参照: `this.libraryDirectory`

## WallpaperFeed.applySavedWallpaper()
- 位置: async L864-873
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `locks.request()`, `this.#applySavedWallpaper()`

## WallpaperFeed.#applySavedWallpaper()
- 位置: async L886-965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `Services.prefs.setStringPref()`, `ac.BroadcastToContent()`, `ac.SetPref()`, `getDetailsFilename()`, `getWallpaperURL()`, `parseWallpaperFilename()`, `this.#copyAppliedWallpaper()`, `this.#recordSavedWallpaperEvent()`, `this.#sweepWallpaperDirectory()`, `this.getSavedWallpapers()`, `this.store.dispatch()`
- 条件付き依存: `if (parsed.kind !== "saved")` → `console.error()`
- 条件付き依存: `if ( !(await IOUtils.exists(PathUtils.join(this.libraryDirectory, filename))) )` → `console.error()`
- 条件付き依存: `if (parsed.type === WALLPAPER_TYPES.PictureOfTheDay)` → `IOUtils.exists()`
- 条件付き依存: `if (parsed.type === WALLPAPER_TYPES.PictureOfTheDay)` → `PathUtils.join()`
- 条件付き依存: `if (parsed.type === WALLPAPER_TYPES.PictureOfTheDay)` → `this.#readDetails()`
- 参照: `WALLPAPER_TYPES.PictureOfTheDay`, `at.WALLPAPERS_CUSTOM_SET`, `at.WALLPAPER_SAVED_APPLIED`, `details?.publishedDate`, `parsed.kind`, `parsed.position`, `parsed.theme`, `parsed.type`, `saved.length`, `this.applyingWallpaper`, `this.libraryDirectory`, `this.libraryEnabled`
- XPCOM: `Services.prefs`

## WallpaperFeed.broadcastAppliedWallpaper()
- 位置: L971-1037
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `ac.BroadcastToContent()`, `getWallpaperURL()`, `parseWallpaperFilename()`, `this.store.dispatch()`
- 条件付き依存: `if (selectedWallpaper !== "custom" || !isApplied)` → `this.store.dispatch()`
- 条件付き依存: `if (selectedWallpaper !== "custom" || !isApplied)` → `ac.BroadcastToContent()`
- 条件付き依存: `if ( applied.theme && applied.theme !== Services.prefs.getStringPref(PREF_WALLPAPERS_CUSTOM_WALLPAPER_THEME, "") )` → `this.store.dispatch()`
- 条件付き依存: `if ( applied.theme && applied.theme !== Services.prefs.getStringPref(PREF_WALLPAPERS_CUSTOM_WALLPAPER_THEME, "") )` → `ac.SetPref()`
- 条件付き依存: `if ( applied.position && applied.position !== Services.prefs.getStringPref( PREF_WALLPAPERS_CUSTOM_WALLPAPER_POSITION, "" ) )` → `this.store.dispatch()`
- 条件付き依存: `if ( applied.position && applied.position !== Services.prefs.getStringPref( PREF_WALLPAPERS_CUSTOM_WALLPAPER_POSITION, "" ) )` → `ac.SetPref()`
- 参照: `applied.kind`, `applied.position`, `applied.theme`, `at.WALLPAPERS_CUSTOM_SET`, `this.libraryEnabled`
- XPCOM: `Services.prefs`

## WallpaperFeed.broadcastWallpaperLibrary()
- 位置: async L1047-1071
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.getSavedWallpapers()`, `this.store.dispatch()`
- 条件付き依存: `if (target)` → `this.store.dispatch()`
- 条件付き依存: `if (target)` → `ac.OnlyToOneContent()`
- 参照: `at.WALLPAPERS_CUSTOM_LIBRARY_SET`

## WallpaperFeed.getSavedWallpapers()
- 位置: async L1080-1137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getChildren()`, `IOUtils.stat()`, `Object.keys()`, `PathUtils.filename()`, `a.filename.localeCompare()`, `children.map()`, `console.error()`, `filenames.has()`, `getDetailsFilename()`, `parseWallpaperFilename()`, `this.#readDetails()`, `wallpapers.push()`, `wallpapers.sort()`
- 参照: `Object.keys(credit).length`, `a.lastModified`, `b.filename`, `b.lastModified`, `parsed.kind`, `parsed.number`, `parsed.position`, `parsed.theme`, `parsed.type`, `this.libraryDirectory`

## WallpaperFeed.#readDetails()
- 位置: async L1147-1156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readJSON()`, `PathUtils.join()`, `console.error()`
- 参照: `this.libraryDirectory`

## WallpaperFeed.migrateWallpaperLibrary()
- 位置: async L1165-1174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `locks.request()`, `this.#migrateWallpaperLibrary()`

## WallpaperFeed.#migrateWallpaperLibrary()
- 位置: async L1182-1260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.getChildren()`, `PathUtils.filename()`, `PathUtils.join()`, `Services.prefs.getStringPref()`, `console.error()`, `parseWallpaperFilename()`
- 条件付き依存: `if (parsed.kind === "saved" || parsed.kind === "details")` → `IOUtils.exists()`
- 条件付き依存: `if (parsed.kind === "saved" || parsed.kind === "details")` → `PathUtils.join()`
- 条件付き依存: `if (parsed.kind === "saved" || parsed.kind === "details")` → `IOUtils.makeDirectory()`
- 条件付き依存: `if (parsed.kind === "saved" || parsed.kind === "details")` → `IOUtils.move()`
- 条件付き依存: `if (parsed.kind === "saved")` → `moved.push()`
- 条件付き依存: `if (parsed.kind === "saved" || parsed.kind === "details")` → `console.error()`
- 条件付き依存: `if (parsed.kind === "legacy" && filename === applied)` → `this.#adoptLooseWallpaper()`
- 条件付き依存: `if (renamed)` → `moved.push()`
- 条件付き依存: `if ( parseWallpaperFilename(appliedNow).kind === "saved" && !(await IOUtils.exists(PathUtils.join(wallpaperDir, appliedNow))) && (await IOUtils.exists(PathUtils....)` → `this.#copyAppliedWallpaper()`
- 条件付き依存: `if (moved.length)` → `this.#sweepWallpaperDirectory()`
- 参照: `moved.length`, `parseWallpaperFilename(appliedNow).kind`, `parsed.kind`, `this.libraryDirectory`, `this.wallpaperDirectory`
- XPCOM: `Services.prefs`

## WallpaperFeed.#adoptLooseWallpaper()
- 位置: async L1271-1316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.copy()`, `IOUtils.makeDirectory()`, `IOUtils.remove()`, `PathUtils.join()`, `Services.prefs.getStringPref()`, `Services.prefs.setStringPref()`, `buildSavedWallpaperFilename()`, `console.error()`, `this.#copyAppliedWallpaper()`, `this.#takeNextWallpaperNumber()`
- 条件付き依存: `if (!(await this.#copyAppliedWallpaper(filename)))` → `IOUtils.remove()`
- 参照: `WALLPAPER_TYPES.Custom`, `parsed.uuid`, `this.libraryDirectory`, `this.wallpaperDirectory`
- XPCOM: `Services.prefs`

## WallpaperFeed.#sweepWallpaperDirectory()
- 位置: async L1322-1368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.getChildren()`, `IOUtils.stat()`, `PathUtils.filename()`, `PathUtils.join()`, `Services.prefs.getStringPref()`, `console.error()`, `parseWallpaperFilename()`, `this.#sweepLibraryDirectory()`
- 条件付き依存: `if (type === "regular")` → `IOUtils.remove()`
- 参照: `parsed.kind`, `this.libraryDirectory`, `this.libraryEnabled`, `this.wallpaperDirectory`
- XPCOM: `Services.prefs`

## WallpaperFeed.#sweepLibraryDirectory()
- 位置: async L1376-1408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getChildren()`, `IOUtils.stat()`, `PathUtils.filename()`, `children.map()`, `console.error()`, `filenames.has()`, `parseWallpaperFilename()`
- 条件付き依存: `if (type === "regular")` → `IOUtils.remove()`
- 参照: `parsed.imageFilename`, `parsed.kind`, `this.libraryDirectory`

## WallpaperFeed.cleanWallpaperDirectory()
- 位置: async L1414-1422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `locks.request()`, `this.#sweepWallpaperDirectory()`

## WallpaperFeed.removeCustomWallpaper()
- 位置: async L1426-1434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `locks.request()`, `this.#deleteCustomWallpaper()`

## WallpaperFeed.#deleteCustomWallpaper()
- 位置: async L1436-1511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `console.error()`, `parseWallpaperFilename()`, `this.#recordSavedWallpaperEvent()`, `this.#removeLibraryEntry()`, `this.broadcastWallpaperLibrary()`, `this.getSavedWallpapers()`
- 条件付き依存: `if (parsed.kind !== "saved")` → `console.error()`
- 条件付き依存: `if (filename === appliedNow)` → `this.removeFile()`
- 条件付き依存: `if (filename === appliedNow)` → `PathUtils.join()`
- 条件付き依存: `if (filename === appliedNow)` → `console.error()`
- 条件付き依存: `if (filename === appliedNow)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (filename === appliedNow)` → `this.store.dispatch()`
- 条件付き依存: `if (filename === appliedNow)` → `ac.SetPref()`
- 条件付き依存: `if (filename === appliedNow)` → `ac.BroadcastToContent()`
- 参照: `(await this.getSavedWallpapers()).length`, `at.WALLPAPERS_CUSTOM_SET`, `at.WALLPAPER_SAVED_REMOVED`, `parsed.kind`, `parsed.type`, `this.wallpaperDirectory`
- XPCOM: `Services.prefs`

## WallpaperFeed.#recordSavedWallpaperEvent()
- 位置: L1516-1521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.dispatch()`

## WallpaperFeed.onAction()
- 位置: async L1523-1618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `locks.request()`, `this.applySavedWallpaper()`, `this.broadcastWallpaperLibrary()`, `this.initHighlightCounter()`, `this.removeCustomWallpaper()`, `this.wallpaperSeenEvent()`, `this.wallpaperSetup()`, `this.wallpaperUpload()`
- 条件付き依存: `if ( action.data.name === "newtabWallpapers.customColor.enabled" || action.data.name === "newtabWallpapers.customWallpaper.enabled" || action.data.name === "newt...)` → `this.wallpaperTeardown()`
- 条件付き依存: `if ( action.data.name === "newtabWallpapers.customColor.enabled" || action.data.name === "newtabWallpapers.customWallpaper.enabled" || action.data.name === "newt...)` → `this.wallpaperSetup()`
- 条件付き依存: `if ( !this.applyingWallpaper && (action.data.name === "newtabWallpapers.customWallpaper.uuid" || action.data.name === "newtabWallpapers.wallpaper") )` → `this.broadcastAppliedWallpaper()`
- 条件付き依存: `if ( !this.applyingWallpaper && (action.data.name === "newtabWallpapers.customWallpaper.uuid" || action.data.name === "newtabWallpapers.wallpaper") )` → `this.cleanWallpaperDirectory()`
- 条件付き依存: `if (action.data.name === "newtabWallpapers.highlightSeenCounter")` → `this.initHighlightCounter()`
- 条件付き依存: `if (target && action.data.requestId)` → `this.store.dispatch()`
- 条件付き依存: `if (target && action.data.requestId)` → `ac.OnlyToOneContent()`
- 条件付き依存: `if (target && action.data.requestId)` → `PathUtils.filename()`
- 参照: `action.data.file`, `action.data.name`, `action.data.publishedDate`, `action.data.requestId`, `action.data.theme`, `action.data.type`, `action.data?.filename`, `action.meta?.fromTarget`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.SYSTEM_TICK`, `at.UNINIT`, `at.WALLPAPERS_CUSTOM_APPLY`, `at.WALLPAPERS_CUSTOM_LIBRARY_REQUEST`, `at.WALLPAPERS_FEATURE_HIGHLIGHT_SEEN`, `at.WALLPAPERS_SET`, `at.WALLPAPER_REMOVE_UPLOAD`, `at.WALLPAPER_UPLOAD`, `at.WALLPAPER_UPLOAD_RESULT`, `this.applyingWallpaper`
