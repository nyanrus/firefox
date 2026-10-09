# browser/extensions/webcompat/shims/google-ima.js

source: browser/extensions/webcompat/shims/google-ima.js
source-hash: 74013cc8499171ca863f7891cac956ad90ba13b6
lines: 621

## <module>
- 役割: (未記入)

## AdDisplayContainer.destroy()
- 位置: L63-63
- 役割: (未記入)
- 触るとき: (未記入)

## AdDisplayContainer.initialize()
- 位置: L64-64
- 役割: (未記入)
- 触るとき: (未記入)

## ImaSdkSettings.getCompanionBackfill()
- 位置: L76-76
- 役割: (未記入)
- 触るとき: (未記入)

## ImaSdkSettings.getDisableCustomPlaybackForIOS10Plus()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#i`

## ImaSdkSettings.getFeatureFlags()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#f`

## ImaSdkSettings.getLocale()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#l`

## ImaSdkSettings.getNumRedirects()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#r`

## ImaSdkSettings.getPlayerType()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#t`

## ImaSdkSettings.getPlayerVersion()
- 位置: L92-94
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#v`

## ImaSdkSettings.getPpid()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#p`

## ImaSdkSettings.isCookiesEnabled()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#c`

## ImaSdkSettings.setAutoPlayAdBreaks()
- 位置: L101-101
- 役割: (未記入)
- 触るとき: (未記入)

## ImaSdkSettings.setCompanionBackfill()
- 位置: L102-102
- 役割: (未記入)
- 触るとき: (未記入)

## ImaSdkSettings.setCookiesEnabled()
- 位置: L103-105
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#c`

## ImaSdkSettings.setDisableCustomPlaybackForIOS10Plus()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#i`

## ImaSdkSettings.setFeatureFlags()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#f`

## ImaSdkSettings.setLocale()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#l`

## ImaSdkSettings.setNumRedirects()
- 位置: L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#r`

## ImaSdkSettings.setPlayerType()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#t`

## ImaSdkSettings.setPlayerVersion()
- 位置: L121-123
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#v`

## ImaSdkSettings.setPpid()
- 位置: L124-126
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#p`

## ImaSdkSettings.setSessionId()
- 位置: L127-127
- 役割: (未記入)
- 触るとき: (未記入)

## ImaSdkSettings.setVpaidAllowed()
- 位置: L128-128
- 役割: (未記入)
- 触るとき: (未記入)

## ImaSdkSettings.setVpaidMode()
- 位置: L129-129
- 役割: (未記入)
- 触るとき: (未記入)

## EventHandler._dispatch()
- 位置: L144-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `console.error()`, `listener()`, `this.#listeners.get()`
- 参照: `e.type`

## EventHandler.addEventListener()
- 位置: L155-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.get()`, `this.#listeners.get(t).add()`, `this.#listeners.has()`
- 条件付き依存: `if (!this.#listeners.has(t))` → `this.#listeners.set()`

## EventHandler.removeEventListener()
- 位置: L162-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.get()`, `this.#listeners.get(t)?.delete()`

## AdsLoader.contentComplete()
- 位置: L169-169
- 役割: (未記入)
- 触るとき: (未記入)

## AdsLoader.destroy()
- 位置: L170-170
- 役割: (未記入)
- 触るとき: (未記入)

## AdsLoader.getSettings()
- 位置: L171-173
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#settings`

## AdsLoader.getVersion()
- 位置: L174-176
- 役割: (未記入)
- 触るとき: (未記入)

## AdsLoader.requestAds()
- 位置: L177-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CheckCanAutoplay()`, `CheckCanAutoplay().then()`, `this._dispatch()`
- 参照: `AdsManagerLoadedEvent.Type`, `ima.AdError`, `ima.AdErrorEvent`, `ima.AdsManagerLoadedEvent`

## AdsManager.collapse()
- 位置: L201-201
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.configureAdsManager()
- 位置: L202-202
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.destroy()
- 位置: L203-203
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.discardAdBreak()
- 位置: L204-204
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.expand()
- 位置: L205-205
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.focus()
- 位置: L206-206
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.getAdSkippableState()
- 位置: L207-209
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.getCuePoints()
- 位置: L210-212
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.getCurrentAd()
- 位置: L213-215
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.getCurrentAdCuePoints()
- 位置: L216-218
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.getRemainingTime()
- 位置: L219-221
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.getVolume()
- 位置: L222-224
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#volume`

## AdsManager.init()
- 位置: L225-225
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.isCustomClickTrackingUsed()
- 位置: L226-228
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.isCustomPlaybackUsed()
- 位置: L229-231
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.pause()
- 位置: L232-232
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.requestNextAdBreak()
- 位置: L233-233
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.resize()
- 位置: L234-234
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.resume()
- 位置: L235-235
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.setVolume()
- 位置: L236-238
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#volume`

## AdsManager.skip()
- 位置: L239-239
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.start()
- 位置: L240-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `requestAnimationFrame()`, `this._dispatch()`
- 参照: `AdEvent.Type.AD_BUFFERING`, `AdEvent.Type.ALL_ADS_COMPLETED`, `AdEvent.Type.COMPLETE`, `AdEvent.Type.CONTENT_RESUME_REQUESTED`, `AdEvent.Type.FIRST_QUARTILE`, `AdEvent.Type.LOADED`, `AdEvent.Type.MIDPOINT`, `AdEvent.Type.STARTED`, `AdEvent.Type.THIRD_QUARTILE`, `ima.AdEvent`

## AdsManager.stop()
- 位置: L261-261
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManager.updateAdsRenderingSettings()
- 位置: L262-262
- 役割: (未記入)
- 触るとき: (未記入)

## AdsRequest.setAdWillAutoPlay()
- 位置: L268-268
- 役割: (未記入)
- 触るとき: (未記入)

## AdsRequest.setAdWillPlayMuted()
- 位置: L269-269
- 役割: (未記入)
- 触るとき: (未記入)

## AdsRequest.setContinuousPlayback()
- 位置: L270-270
- 役割: (未記入)
- 触るとき: (未記入)

## AdPodInfo.getAdPosition()
- 位置: L274-276
- 役割: (未記入)
- 触るとき: (未記入)

## AdPodInfo.getIsBumper()
- 位置: L277-279
- 役割: (未記入)
- 触るとき: (未記入)

## AdPodInfo.getMaxDuration()
- 位置: L280-282
- 役割: (未記入)
- 触るとき: (未記入)

## AdPodInfo.getPodIndex()
- 位置: L283-285
- 役割: (未記入)
- 触るとき: (未記入)

## AdPodInfo.getTimeOffset()
- 位置: L286-288
- 役割: (未記入)
- 触るとき: (未記入)

## AdPodInfo.getTotalAds()
- 位置: L289-291
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getAdId()
- 位置: L296-298
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getAdPodInfo()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._pi`

## Ad.getAdSystem()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getAdvertiserName()
- 位置: L305-307
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getApiFramework()
- 位置: L308-310
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getCompanionAds()
- 位置: L311-313
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getContentType()
- 位置: L314-316
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getCreativeAdId()
- 位置: L317-319
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getCreativeId()
- 位置: L320-322
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getDealId()
- 位置: L323-325
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getDescription()
- 位置: L326-328
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getDuration()
- 位置: L329-331
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getHeight()
- 位置: L332-334
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getMediaUrl()
- 位置: L335-337
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getMinSuggestedDuration()
- 位置: L338-340
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getSkipTimeOffset()
- 位置: L341-343
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getSurveyUrl()
- 位置: L344-346
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getTitle()
- 位置: L347-349
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getTraffickingParameters()
- 位置: L350-352
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getTraffickingParametersString()
- 位置: L353-355
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getUiElements()
- 位置: L356-358
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getUniversalAdIdRegistry()
- 位置: L359-361
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getUniversalAdIds()
- 位置: L362-364
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getUniversalAdIdValue()
- 位置: L365-367
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getVastMediaBitrate()
- 位置: L368-370
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getVastMediaHeight()
- 位置: L371-373
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getVastMediaWidth()
- 位置: L374-376
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getWidth()
- 位置: L377-379
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getWrapperAdIds()
- 位置: L380-382
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getWrapperAdSystems()
- 位置: L383-385
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.getWrapperCreativeIds()
- 位置: L386-388
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.isLinear()
- 位置: L389-391
- 役割: (未記入)
- 触るとき: (未記入)

## Ad.isSkippable()
- 位置: L392-394
- 役割: (未記入)
- 触るとき: (未記入)

## CompanionAd.getAdSlotId()
- 位置: L398-400
- 役割: (未記入)
- 触るとき: (未記入)

## CompanionAd.getContent()
- 位置: L401-403
- 役割: (未記入)
- 触るとき: (未記入)

## CompanionAd.getContentType()
- 位置: L404-406
- 役割: (未記入)
- 触るとき: (未記入)

## CompanionAd.getHeight()
- 位置: L407-409
- 役割: (未記入)
- 触るとき: (未記入)

## CompanionAd.getWidth()
- 位置: L410-412
- 役割: (未記入)
- 触るとき: (未記入)

## AdError.constructor()
- 位置: L420-425
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#errorCode`, `this.#message`, `this.#type`, `this.#vastErrorCode`

## AdError.getErrorCode()
- 位置: L426-428
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#errorCode`

## AdError.getInnerError()
- 位置: L429-429
- 役割: (未記入)
- 触るとき: (未記入)

## AdError.getMessage()
- 位置: L430-432
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#message`

## AdError.getType()
- 位置: L433-435
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#type`

## AdError.getVastErrorCode()
- 位置: L436-438
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#vastErrorCode`

## AdError.toString()
- 位置: L439-441
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#errorCode`, `this.#message`

## isEngadget()
- 位置: L446-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `ctx.getPlayer()`, `ctx.getPlayer()?.div?.innerHTML.includes()`, `window.vidible._getContexts()`

## AdEvent.constructor()
- 位置: L460-462
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.type`

## AdEvent.getAd()
- 位置: L463-465
- 役割: (未記入)
- 触るとき: (未記入)

## AdEvent.getAdData()
- 位置: L466-468
- 役割: (未記入)
- 触るとき: (未記入)

## AdErrorEvent.constructor()
- 位置: L508-510
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#error`

## AdErrorEvent.getError()
- 位置: L511-513
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#error`

## AdErrorEvent.getUserRequestContext()
- 位置: L514-516
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManagerLoadedEvent.constructor()
- 位置: L525-527
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.type`

## AdsManagerLoadedEvent.getAdsManager()
- 位置: L528-530
- 役割: (未記入)
- 触るとき: (未記入)

## AdsManagerLoadedEvent.getUserRequestContext()
- 位置: L531-533
- 役割: (未記入)
- 触るとき: (未記入)

## AdCuePoints.getCuePoints()
- 位置: L563-565
- 役割: (未記入)
- 触るとき: (未記入)

## UniversalAdIdInfo.getAdIdRegistry()
- 位置: L571-573
- 役割: (未記入)
- 触るとき: (未記入)

## UniversalAdIdInfo.getAdIsValue()
- 位置: L574-576
- 役割: (未記入)
- 触るとき: (未記入)
