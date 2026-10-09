# browser/extensions/newtab/lib/FrecencyBoostProvider/FrecencyBoostProvider.mjs

source: browser/extensions/newtab/lib/FrecencyBoostProvider/FrecencyBoostProvider.mjs
source-hash: 6ce00ea5e0a1cb5123c565230a3be58c54db3552
lines: 259

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## FrecencyBoostProvider.constructor()
- 位置: L28-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onSync.bind()`
- 参照: `lazy.PersistentCache`, `this._frecencyBoostRS`, `this._frecencyBoostedSponsors`, `this._links`, `this._onSync`, `this.cache`, `this.frecentCache`

## FrecencyBoostProvider.init()
- 位置: L37-44
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._frecencyBoostRS)` → `lazy.RemoteSettings()`
- 条件付き依存: `if (!this._frecencyBoostRS)` → `this._frecencyBoostRS.on()`
- 参照: `this._frecencyBoostRS`, `this._onSync`

## FrecencyBoostProvider.uninit()
- 位置: L46-51
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._frecencyBoostRS)` → `this._frecencyBoostRS.off()`
- 参照: `this._frecencyBoostRS`, `this._onSync`

## FrecencyBoostProvider.onSync()
- 位置: async L53-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._importFrecencyBoostedSponsors()`
- 参照: `this._frecencyBoostedSponsors`

## FrecencyBoostProvider._importFrecencyBoostedSponsors()
- 位置: async L63-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.log.warn()`, `records.filter()`, `regionRecords.map()`, `this._frecencyBoostRS?.get()`, `this._importFrecencyBoostedSponsor()`, `this._importFrecencyBoostedSponsor(record).catch()`
- 参照: `lazy.Region.home`, `record.region`, `record.title`

## FrecencyBoostProvider._importFrecencyBoostedSponsor()
- 位置: async L91-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.shortURL()`, `this._fetchSponsorFaviconAsDataURI()`, `this._frecencyBoostedSponsors.set()`

## FrecencyBoostProvider._fetchSponsorFaviconAsDataURI()
- 位置: async L113-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buffer.toString()`, `lazy.log.warn()`, `this._frecencyBoostRS.attachments.download()`
- 参照: `record.attachment.mimetype`, `this._frecencyBoostRS`

## FrecencyBoostProvider.buildFrecencyBoostedSpocs()
- 位置: async L138-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidates.sort()`, `frecent.forEach()`, `lazy.NewTabUtils.blockedLinks.isBlocked()`, `lazy.NewTabUtils.shortURL()`, `lazy.PlacesUtils.history.pageFrecencyThreshold()`, `this._frecencyBoostedSponsors.get()`, `this.frecentCache.request()`
- 条件付き依存: `if ( candidate && !lazy.NewTabUtils.blockedLinks.isBlocked({ url: candidate.domain }) )` → `candidates.push()`
- 参照: `a.frecency`, `b.frecency`, `candidate.domain`, `candidate.faviconDataURI`, `candidate.hostname`, `candidate.redirectURL`, `candidate.title`, `site.frecency`, `this._frecencyBoostedSponsors.size`

## FrecencyBoostProvider.update()
- 位置: async L186-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buildFrecencyBoostedSpocs()`, `this.cache.set()`
- 条件付き依存: `if (!this._frecencyBoostedSponsors.size)` → `this._importFrecencyBoostedSponsors()`
- 参照: `this._frecencyBoostedSponsors.size`, `this._links`

## FrecencyBoostProvider.fetch()
- 位置: async L196-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.blockedLinks.isBlocked()`, `links.filter()`
- 条件付き依存: `if (!this._links)` → `this.cache.get()`
- 条件付き依存: `if (!this._links)` → `this.update()`
- 参照: `link.url`, `this._links`

## FrecencyBoostProvider.retrieveRandomFrecencyTile()
- 位置: async L215-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from( this._frecencyBoostedSponsors.values() ).filter()`, `JSON.stringify()`, `Math.floor()`, `Math.random()`, `lazy.NewTabUtils.blockedLinks.isBlocked()`, `this._frecencyBoostedSponsors.values()`, `this.cache.get()`, `this.cache.set()`
- 条件付き依存: `if (!this._frecencyBoostedSponsors.size)` → `this._importFrecencyBoostedSponsors()`
- 条件付き依存: `if (storedTile)` → `JSON.parse()`
- 条件付き依存: `if (storedTile)` → `this._frecencyBoostedSponsors.has()`
- 条件付き依存: `if (storedTile)` → `lazy.NewTabUtils.blockedLinks.isBlocked()`
- 条件付き依存: `if (storedTile)` → `this.cache.set()`
- 参照: `candidates.length`, `s.domain`, `selected.faviconDataURI`, `selected.hostname`, `selected.redirectURL`, `selected.title`, `this._frecencyBoostedSponsors.size`, `tile.hostname`, `tile.url`

## FrecencyBoostProvider.clearRandomFrecencyTile()
- 位置: async L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.set()`
