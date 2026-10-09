# browser/extensions/newtab/lib/Widgets/PictureOfTheDayFeed.sys.mjs

source: browser/extensions/newtab/lib/Widgets/PictureOfTheDayFeed.sys.mjs
source-hash: 7b83184bc74c818be515c543335910981fa82789
lines: 423

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `WIDGET_REGISTRY.find()`

## PictureOfTheDayFeed.constructor()
- 位置: L88-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this.cache`, `this.currentImageUrl`, `this.loaded`, `this.merino`, `this.settingWallpaper`

## PictureOfTheDayFeed.isEnabled()
- 位置: L101-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isWidgetEnabled()`, `this.store.getState()`
- 参照: `this.store.getState().Prefs`

## PictureOfTheDayFeed.getEndpoint()
- 位置: L112-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(values[PREF_ENDPOINTS_ALLOWLIST] ?? "") .split()`, `(values[PREF_ENDPOINTS_ALLOWLIST] ?? "") .split(",") .map()`, `(values[PREF_ENDPOINTS_ALLOWLIST] ?? "") .split(",") .map(item => item.trim()) .filter()`, `allowed.some()`, `endpoint.startsWith()`, `item.trim()`, `this.store.getState()`
- 条件付き依存: `if (!allowed.some(prefix => endpoint.startsWith(prefix)))` → `console.error()`
- 参照: `this.store.getState().Prefs`

## PictureOfTheDayFeed.isStale()
- 位置: L133-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `D.now()`, `new D(D.now()).toDateString()`, `new D(lastUpdated).toDateString()`, `this.Date()`

## PictureOfTheDayFeed.init()
- 位置: async L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.loadPicture()`

## PictureOfTheDayFeed.resetCache()
- 位置: async L145-149
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.cache)` → `this.cache.set()`
- 参照: `this.cache`

## PictureOfTheDayFeed.reset()
- 位置: async L151-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetCache()`, `this.update()`
- 参照: `this.loaded`

## PictureOfTheDayFeed.normalize()
- 位置: L159-178
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `raw.author`, `raw.description`, `raw.file_page`, `raw.high_res_image_url`, `raw.license_label`, `raw.license_link`, `raw.published_date`, `raw.thumbnail_image_url`, `raw.title`

## PictureOfTheDayFeed.fetch()
- 位置: async L180-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.Date()`, `this.Date().now()`, `this.cache.set()`, `this.getEndpoint()`, `this.merino.fetchPictureOfTheDay()`, `this.normalize()`, `this.update()`
- 条件付き依存: `if (!this.merino)` → `this.MerinoClient()`
- 条件付き依存: `if (!endpointUrl)` → `this.update()`
- 条件付き依存: `if (error || !picture)` → `this.update()`
- 参照: `Services.locale.appLocaleAsBCP47`, `this.merino`
- XPCOM: `Services.locale`

## PictureOfTheDayFeed.loadPicture()
- 位置: async L206-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`, `this.isStale()`
- 条件付き依存: `if (this.isStale(picture?.lastUpdated))` → `this.fetch()`
- 条件付き依存: `if (!(this.isStale(picture?.lastUpdated)))` → `this.update()`
- 参照: `picture?.lastUpdated`, `this.loaded`

## PictureOfTheDayFeed.update()
- 位置: L217-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.PICTURE_OF_THE_DAY_UPDATE`, `data.author`, `data.description`, `data.error`, `data.imageUrl`, `data.lastUpdated`, `data.licenseLabel`, `data.licenseUrl`, `data.publishedDate`, `data.sourceUrl`, `data.thumbnailUrl`, `data.title`, `this.currentImageUrl`

## PictureOfTheDayFeed.setWallpaper()
- 位置: async L245-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.SetMultiplePrefs()`, `console.error()`, `contentType.startsWith()`, `lazy.calculateTheme()`, `response.blob()`, `response.headers?.get()`, `this.fetchImage()`, `this.store.dispatch()`, `this.store.getState()`
- 条件付き依存: `if (!response.ok || !contentType.startsWith("image/"))` → `console.error()`
- 参照: `Services.appShell.hiddenDOMWindow`, `WALLPAPER_TYPES.PictureOfTheDay`, `at.WALLPAPER_UPLOAD`, `response.ok`, `response.status`, `this.currentImageUrl`, `this.settingWallpaper`, `this.store.getState().PictureOfTheDay`, `this.store.getState().Prefs`
- XPCOM: `Services.appShell`

## PictureOfTheDayFeed.onPrefChangedAction()
- 位置: async L329-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isEnabled()`, `this.store.getState()`
- 条件付き依存: `if (enabled && !this.loaded)` → `this.loadPicture()`
- 条件付き依存: `if (!enabled && this.loaded)` → `this.reset()`
- 条件付き依存: `if (this.isEnabled())` → `this.fetch()`
- 条件付き依存: `if ( values["widgets.pictureOfTheDay.wallpaperActive"] && values["newtabWallpapers.wallpaper"] !== "custom" )` → `this.store.dispatch()`
- 条件付き依存: `if ( values["widgets.pictureOfTheDay.wallpaperActive"] && values["newtabWallpapers.wallpaper"] !== "custom" )` → `ac.SetPref()`
- 参照: `action.data.name`, `this.loaded`, `this.store.getState().Prefs`

## PictureOfTheDayFeed.onAction()
- 位置: async L365-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isEnabled()`, `this.onPrefChangedAction()`, `this.onWallpaperUpload()`, `this.setWallpaper()`
- 条件付き依存: `if (this.isEnabled() && !this.loaded)` → `this.init()`
- 条件付き依存: `if (this.isEnabled())` → `this.loadPicture()`
- 参照: `action.meta?.fromTarget`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.SYSTEM_TICK`, `at.WALLPAPER_UPLOAD`, `at.WIDGETS_PICTURE_SET_WALLPAPER`, `this.loaded`

## PictureOfTheDayFeed.onWallpaperUpload()
- 位置: L394-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 条件付き依存: `if (values["widgets.pictureOfTheDay.wallpaperActive"])` → `this.store.dispatch()`
- 条件付き依存: `if (values["widgets.pictureOfTheDay.wallpaperActive"])` → `ac.SetPref()`
- 参照: `this.settingWallpaper`, `this.store.getState().Prefs`

## PictureOfTheDayFeed.prototype.MerinoClient()
- 位置: L411-413
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.TemporaryMerinoClientShim`

## PictureOfTheDayFeed.prototype.PersistentCache()
- 位置: L414-416
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`

## PictureOfTheDayFeed.prototype.Date()
- 位置: L417-419
- 役割: (未記入)
- 触るとき: (未記入)

## PictureOfTheDayFeed.prototype.fetchImage()
- 位置: L420-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`
