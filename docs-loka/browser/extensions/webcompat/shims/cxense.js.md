# browser/extensions/webcompat/shims/cxense.js

source: browser/extensions/webcompat/shims/cxense.js
source-hash: 55862f4fb5c3a0b3223065fd729146e7854e7754
lines: 594

## <module>
- 役割: (未記入)

## getRandomString()
- 位置: L20-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(v, c => c.toString(16)).join()`, `c.toString()`, `crypto.getRandomValues()`, `s.slice()`

## call()
- 位置: L26-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb()`, `console.error()`

## invokeOn()
- 位置: L37-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lib[fn]()`

## displayWidget()
- 位置: L53-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## getUserSegmentIds()
- 位置: L54-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`
- 参照: `a?.callback`, `a?.defaultValue`

## init()
- 位置: L55-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## render()
- 位置: L56-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## run()
- 位置: L57-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## runCtrlVersion()
- 位置: L58-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## runCxVersion()
- 位置: L59-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## runTest()
- 位置: L60-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## sendConversionEvent()
- 位置: L61-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`
- 参照: `options?.callback`

## sendEvent()
- 位置: L62-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`
- 参照: `args?.callback`

## getDivId()
- 位置: L64-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`

## getDocumentSize()
- 位置: L72-76
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `document.body.clientHeight`, `document.body.clientWidth`

## getNowSeconds()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `new Date().getTime()`

## getPageContext()
- 位置: L82-88
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `location.href`

## getWindowSize()
- 位置: L90-94
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.innerHeight`, `window.innerWidth`

## isObject()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`

## runMulti()
- 位置: L100-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`, `widgets?.forEach()`

## addCustomerScript()
- 位置: L111-111
- 役割: (未記入)
- 触るとき: (未記入)

## addEventListener()
- 位置: L112-112
- 役割: (未記入)
- 触るとき: (未記入)

## addExternalId()
- 位置: L113-113
- 役割: (未記入)
- 触るとき: (未記入)

## afterInitializePage()
- 位置: L114-114
- 役割: (未記入)
- 触るとき: (未記入)

## allUserConsents()
- 位置: L115-115
- 役割: (未記入)
- 触るとき: (未記入)

## calculateAdSpaceSize()
- 位置: L129-131
- 役割: (未記入)
- 触るとき: (未記入)

## cint()
- 位置: L144-144
- 役割: (未記入)
- 触るとき: (未記入)

## clearCustomParameters()
- 位置: L147-147
- 役割: (未記入)
- 触るとき: (未記入)

## clearIds()
- 位置: L149-149
- 役割: (未記入)
- 触るとき: (未記入)

## clickTracker()
- 位置: L150-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## combineArgs()
- 位置: L152-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## combineKeywordsIntoArray()
- 位置: L153-153
- 役割: (未記入)
- 触るとき: (未記入)

## createDelegate()
- 位置: L157-157
- 役割: (未記入)
- 触るとき: (未記入)

## decodeUrlEncodedNameValuePairs()
- 位置: L164-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## defaultAdRenderer()
- 位置: L165-165
- 役割: (未記入)
- 触るとき: (未記入)

## deleteCookie()
- 位置: L166-166
- 役割: (未記入)
- 触るとき: (未記入)

## getAllText()
- 位置: L180-180
- 役割: (未記入)
- 触るとき: (未記入)

## getClientStorageVariable()
- 位置: L181-181
- 役割: (未記入)
- 触るとき: (未記入)

## getCookie()
- 位置: L182-182
- 役割: (未記入)
- 触るとき: (未記入)

## getCxenseUserId()
- 位置: L183-183
- 役割: (未記入)
- 触るとき: (未記入)

## getElementPosition()
- 位置: L185-185
- 役割: (未記入)
- 触るとき: (未記入)

## getHashFragment()
- 位置: L186-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `location.hash.substr()`

## getLocalStats()
- 位置: L187-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## getNodeValue()
- 位置: L188-188
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `n.nodeValue`

## getScrollPos()
- 位置: L192-192
- 役割: (未記入)
- 触るとき: (未記入)

## getSessionId()
- 位置: L193-193
- 役割: (未記入)
- 触るとき: (未記入)

## getSiteId()
- 位置: L194-194
- 役割: (未記入)
- 触るとき: (未記入)

## getTimezoneOffset()
- 位置: L195-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date().getTimezoneOffset()`

## getTopLevelDomain()
- 位置: L196-196
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `location.hostname`

## getUserId()
- 位置: L197-197
- 役割: (未記入)
- 触るとき: (未記入)

## hasConsent()
- 位置: L200-200
- 役割: (未記入)
- 触るとき: (未記入)

## hasHistory()
- 位置: L201-201
- 役割: (未記入)
- 触るとき: (未記入)

## hasLocalStorage()
- 位置: L202-202
- 役割: (未記入)
- 触るとき: (未記入)

## hasPassiveEventListeners()
- 位置: L203-203
- 役割: (未記入)
- 触るとき: (未記入)

## hasPostMessage()
- 位置: L204-204
- 役割: (未記入)
- 触るとき: (未記入)

## hasSessionStorage()
- 位置: L205-205
- 役割: (未記入)
- 触るとき: (未記入)

## initializePage()
- 位置: L206-206
- 役割: (未記入)
- 触るとき: (未記入)

## insertAdSpace()
- 位置: L207-207
- 役割: (未記入)
- 触るとき: (未記入)

## insertMultipleAdSpaces()
- 位置: L208-208
- 役割: (未記入)
- 触るとき: (未記入)

## insertWidget()
- 位置: L209-209
- 役割: (未記入)
- 触るとき: (未記入)

## isAmpIFrame()
- 位置: L211-211
- 役割: (未記入)
- 触るとき: (未記入)

## isArray()
- 位置: L212-212
- 役割: (未記入)
- 触るとき: (未記入)

## isCompatModeActive()
- 位置: L213-213
- 役割: (未記入)
- 触るとき: (未記入)

## isConsentRequired()
- 位置: L214-214
- 役割: (未記入)
- 触るとき: (未記入)

## isEdge()
- 位置: L215-215
- 役割: (未記入)
- 触るとき: (未記入)

## isFirefox()
- 位置: L216-216
- 役割: (未記入)
- 触るとき: (未記入)

## isIE6Or7()
- 位置: L217-217
- 役割: (未記入)
- 触るとき: (未記入)

## isRecsDestination()
- 位置: L219-219
- 役割: (未記入)
- 触るとき: (未記入)

## isSafari()
- 位置: L220-220
- 役割: (未記入)
- 触るとき: (未記入)

## isTextNode()
- 位置: L221-221
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `n?.nodeType`

## isTopWindow()
- 位置: L222-222
- 役割: (未記入)
- 触るとき: (未記入)

## jsonpRequest()
- 位置: L223-223
- 役割: (未記入)
- 触るとき: (未記入)

## loadScript()
- 位置: L224-224
- 役割: (未記入)
- 触るとき: (未記入)

## onClearIds()
- 位置: L285-285
- 役割: (未記入)
- 触るとき: (未記入)

## onFFP1()
- 位置: L286-286
- 役割: (未記入)
- 触るとき: (未記入)

## onP1()
- 位置: L287-287
- 役割: (未記入)
- 触るとき: (未記入)

## parseHashArgs()
- 位置: L290-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## parseMargins()
- 位置: L291-291
- 役割: (未記入)
- 触るとき: (未記入)

## parseUrlArgs()
- 位置: L292-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## postMessageToParent()
- 位置: L293-293
- 役割: (未記入)
- 触るとき: (未記入)

## removeClientStorageVariable()
- 位置: L295-295
- 役割: (未記入)
- 触るとき: (未記入)

## removeEventListener()
- 位置: L296-296
- 役割: (未記入)
- 触るとき: (未記入)

## renderContainedImage()
- 位置: L297-297
- 役割: (未記入)
- 触るとき: (未記入)

## renderTemplate()
- 位置: L298-298
- 役割: (未記入)
- 触るとき: (未記入)

## reportActivity()
- 位置: L299-299
- 役割: (未記入)
- 触るとき: (未記入)

## requireActivityEvents()
- 位置: L300-300
- 役割: (未記入)
- 触るとき: (未記入)

## requireConsent()
- 位置: L301-301
- 役割: (未記入)
- 触るとき: (未記入)

## requireOnlyFirstPartyIds()
- 位置: L302-302
- 役割: (未記入)
- 触るとき: (未記入)

## requireSecureCookies()
- 位置: L303-303
- 役割: (未記入)
- 触るとき: (未記入)

## requireTcf20()
- 位置: L304-304
- 役割: (未記入)
- 触るとき: (未記入)

## sendSpaRecsClick()
- 位置: L306-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## setAccountId()
- 位置: L307-307
- 役割: (未記入)
- 触るとき: (未記入)

## setAllConsentsTo()
- 位置: L308-308
- 役割: (未記入)
- 触るとき: (未記入)

## setClientStorageVariable()
- 位置: L309-309
- 役割: (未記入)
- 触るとき: (未記入)

## setCompatMode()
- 位置: L310-310
- 役割: (未記入)
- 触るとき: (未記入)

## setConsent()
- 位置: L311-311
- 役割: (未記入)
- 触るとき: (未記入)

## setCookie()
- 位置: L312-312
- 役割: (未記入)
- 触るとき: (未記入)

## setCustomParameters()
- 位置: L313-313
- 役割: (未記入)
- 触るとき: (未記入)

## setEventAttributes()
- 位置: L314-314
- 役割: (未記入)
- 触るとき: (未記入)

## setGeoPosition()
- 位置: L315-315
- 役割: (未記入)
- 触るとき: (未記入)

## setNodeValue()
- 位置: L316-316
- 役割: (未記入)
- 触るとき: (未記入)

## setRandomId()
- 位置: L317-317
- 役割: (未記入)
- 触るとき: (未記入)

## setRestrictionsToConsentClasses()
- 位置: L318-318
- 役割: (未記入)
- 触るとき: (未記入)

## setRetargetingParameters()
- 位置: L319-319
- 役割: (未記入)
- 触るとき: (未記入)

## setSiteId()
- 位置: L320-320
- 役割: (未記入)
- 触るとき: (未記入)

## setUserProfileParameters()
- 位置: L321-321
- 役割: (未記入)
- 触るとき: (未記入)

## setupIabCmp()
- 位置: L322-322
- 役割: (未記入)
- 触るとき: (未記入)

## setupTcfApi()
- 位置: L323-323
- 役割: (未記入)
- 触るとき: (未記入)

## shouldPollActivity()
- 位置: L324-324
- 役割: (未記入)
- 触るとき: (未記入)

## startLocalStats()
- 位置: L325-325
- 役割: (未記入)
- 触るとき: (未記入)

## startSessionAnnotation()
- 位置: L326-326
- 役割: (未記入)
- 触るとき: (未記入)

## stopAllSessionAnnotations()
- 位置: L327-327
- 役割: (未記入)
- 触るとき: (未記入)

## stopSessionAnnotation()
- 位置: L328-328
- 役割: (未記入)
- 触るとき: (未記入)

## sync()
- 位置: L329-329
- 役割: (未記入)
- 触るとき: (未記入)

## trackAmpIFrame()
- 位置: L330-330
- 役割: (未記入)
- 触るとき: (未記入)

## trackElement()
- 位置: L331-331
- 役割: (未記入)
- 触るとき: (未記入)

## trim()
- 位置: L332-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `s.trim()`

## clickTracker()
- 位置: L346-346
- 役割: (未記入)
- 触るとき: (未記入)

## displayResult()
- 位置: L347-347
- 役割: (未記入)
- 触るとき: (未記入)

## getTestGroup()
- 位置: L350-350
- 役割: (未記入)
- 触るとき: (未記入)

## insertMaster()
- 位置: L352-352
- 役割: (未記入)
- 触るとき: (未記入)

## instrumentClickLinks()
- 位置: L353-353
- 役割: (未記入)
- 触るとき: (未記入)

## processCxResult()
- 位置: L363-363
- 役割: (未記入)
- 触るとき: (未記入)

## reportTestImpression()
- 位置: L365-365
- 役割: (未記入)
- 触るとき: (未記入)

## sendPageViewEvent()
- 位置: L372-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## setSnapPoints()
- 位置: L373-375
- 役割: (未記入)
- 触るとき: (未記入)

## setTestGroup()
- 位置: L376-378
- 役割: (未記入)
- 触るとき: (未記入)

## setVisibilityField()
- 位置: L379-379
- 役割: (未記入)
- 触るとき: (未記入)

## snapPoints()
- 位置: L380-382
- 役割: (未記入)
- 触るとき: (未記入)

## testGroup()
- 位置: L384-386
- 役割: (未記入)
- 触るとき: (未記入)

## trackVisibility()
- 位置: L389-389
- 役割: (未記入)
- 触るとき: (未記入)

## updateRecsClickUrls()
- 位置: L390-390
- 役割: (未記入)
- 触るとき: (未記入)

## clickTracker()
- 位置: L401-401
- 役割: (未記入)
- 触るとき: (未記入)

## displayResult()
- 位置: L402-402
- 役割: (未記入)
- 触るとき: (未記入)

## getTestGroup()
- 位置: L405-405
- 役割: (未記入)
- 触るとき: (未記入)

## insertMaster()
- 位置: L407-407
- 役割: (未記入)
- 触るとき: (未記入)

## instrumentClickLinks()
- 位置: L408-408
- 役割: (未記入)
- 触るとき: (未記入)

## processCxResult()
- 位置: L419-419
- 役割: (未記入)
- 触るとき: (未記入)

## reportTestImpression()
- 位置: L421-421
- 役割: (未記入)
- 触るとき: (未記入)

## sendPageViewEvent()
- 位置: L428-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## setSnapPoints()
- 位置: L429-431
- 役割: (未記入)
- 触るとき: (未記入)

## setTestGroup()
- 位置: L432-434
- 役割: (未記入)
- 触るとき: (未記入)

## setVisibilityField()
- 位置: L435-435
- 役割: (未記入)
- 触るとき: (未記入)

## snapPoints()
- 位置: L436-438
- 役割: (未記入)
- 触るとき: (未記入)

## testGroup()
- 位置: L440-442
- 役割: (未記入)
- 触るとき: (未記入)

## trackVisibility()
- 位置: L445-445
- 役割: (未記入)
- 触るとき: (未記入)

## updateRecsClickUrls()
- 位置: L446-446
- 役割: (未記入)
- 触るとき: (未記入)

## addCustomerScript()
- 位置: L453-453
- 役割: (未記入)
- 触るとき: (未記入)

## addEventListener()
- 位置: L454-454
- 役割: (未記入)
- 触るとき: (未記入)

## addExternalId()
- 位置: L455-455
- 役割: (未記入)
- 触るとき: (未記入)

## afterInitializePage()
- 位置: L456-456
- 役割: (未記入)
- 触るとき: (未記入)

## allUserConsents()
- 位置: L457-457
- 役割: (未記入)
- 触るとき: (未記入)

## calculateAdSpaceSize()
- 位置: L459-459
- 役割: (未記入)
- 触るとき: (未記入)

## cint()
- 位置: L462-462
- 役割: (未記入)
- 触るとき: (未記入)

## clearCustomParameters()
- 位置: L463-463
- 役割: (未記入)
- 触るとき: (未記入)

## clearIds()
- 位置: L464-464
- 役割: (未記入)
- 触るとき: (未記入)

## clickTracker()
- 位置: L465-465
- 役割: (未記入)
- 触るとき: (未記入)

## combineArgs()
- 位置: L466-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## combineKeywordsIntoArray()
- 位置: L467-467
- 役割: (未記入)
- 触るとき: (未記入)

## createDelegate()
- 位置: L468-468
- 役割: (未記入)
- 触るとき: (未記入)

## decodeUrlEncodedNameValuePairs()
- 位置: L469-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## defaultAdRenderer()
- 位置: L470-470
- 役割: (未記入)
- 触るとき: (未記入)

## deleteCookie()
- 位置: L471-471
- 役割: (未記入)
- 触るとき: (未記入)

## getAllText()
- 位置: L472-472
- 役割: (未記入)
- 触るとき: (未記入)

## getClientStorageVariable()
- 位置: L473-473
- 役割: (未記入)
- 触るとき: (未記入)

## getCookie()
- 位置: L474-474
- 役割: (未記入)
- 触るとき: (未記入)

## getCxenseUserId()
- 位置: L475-475
- 役割: (未記入)
- 触るとき: (未記入)

## getElementPosition()
- 位置: L477-477
- 役割: (未記入)
- 触るとき: (未記入)

## getHashFragment()
- 位置: L478-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `location.hash.substr()`

## getLocalStats()
- 位置: L479-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## getNodeValue()
- 位置: L480-480
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `n.nodeValue`

## getScrollPos()
- 位置: L484-484
- 役割: (未記入)
- 触るとき: (未記入)

## getSessionId()
- 位置: L485-485
- 役割: (未記入)
- 触るとき: (未記入)

## getSiteId()
- 位置: L486-486
- 役割: (未記入)
- 触るとき: (未記入)

## getTimezoneOffset()
- 位置: L487-487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date().getTimezoneOffset()`

## getTopLevelDomain()
- 位置: L488-488
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `location.hostname`

## getUserId()
- 位置: L489-489
- 役割: (未記入)
- 触るとき: (未記入)

## hasConsent()
- 位置: L492-492
- 役割: (未記入)
- 触るとき: (未記入)

## hasHistory()
- 位置: L493-493
- 役割: (未記入)
- 触るとき: (未記入)

## hasLocalStorage()
- 位置: L494-494
- 役割: (未記入)
- 触るとき: (未記入)

## hasPassiveEventListeners()
- 位置: L495-495
- 役割: (未記入)
- 触るとき: (未記入)

## hasPostMessage()
- 位置: L496-496
- 役割: (未記入)
- 触るとき: (未記入)

## hasSessionStorage()
- 位置: L497-497
- 役割: (未記入)
- 触るとき: (未記入)

## initializePage()
- 位置: L498-498
- 役割: (未記入)
- 触るとき: (未記入)

## insertAdSpace()
- 位置: L499-499
- 役割: (未記入)
- 触るとき: (未記入)

## insertMultipleAdSpaces()
- 位置: L500-500
- 役割: (未記入)
- 触るとき: (未記入)

## insertWidget()
- 位置: L501-501
- 役割: (未記入)
- 触るとき: (未記入)

## isAmpIFrame()
- 位置: L503-503
- 役割: (未記入)
- 触るとき: (未記入)

## isArray()
- 位置: L504-504
- 役割: (未記入)
- 触るとき: (未記入)

## isCompatModeActive()
- 位置: L505-505
- 役割: (未記入)
- 触るとき: (未記入)

## isConsentRequired()
- 位置: L506-506
- 役割: (未記入)
- 触るとき: (未記入)

## isEdge()
- 位置: L507-507
- 役割: (未記入)
- 触るとき: (未記入)

## isFirefox()
- 位置: L508-508
- 役割: (未記入)
- 触るとき: (未記入)

## isIE6Or7()
- 位置: L509-509
- 役割: (未記入)
- 触るとき: (未記入)

## isRecsDestination()
- 位置: L511-511
- 役割: (未記入)
- 触るとき: (未記入)

## isSafari()
- 位置: L512-512
- 役割: (未記入)
- 触るとき: (未記入)

## isTextNode()
- 位置: L513-513
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `n?.nodeType`

## isTopWindow()
- 位置: L514-514
- 役割: (未記入)
- 触るとき: (未記入)

## jsonpRequest()
- 位置: L516-516
- 役割: (未記入)
- 触るとき: (未記入)

## loadScript()
- 位置: L518-518
- 役割: (未記入)
- 触るとき: (未記入)

## onClearIds()
- 位置: L520-520
- 役割: (未記入)
- 触るとき: (未記入)

## onFFP1()
- 位置: L521-521
- 役割: (未記入)
- 触るとき: (未記入)

## onP1()
- 位置: L522-522
- 役割: (未記入)
- 触るとき: (未記入)

## parseHashArgs()
- 位置: L523-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## parseMargins()
- 位置: L524-524
- 役割: (未記入)
- 触るとき: (未記入)

## parseUrlArgs()
- 位置: L525-525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`

## postMessageToParent()
- 位置: L526-526
- 役割: (未記入)
- 触るとき: (未記入)

## removeClientStorageVariable()
- 位置: L527-527
- 役割: (未記入)
- 触るとき: (未記入)

## removeEventListener()
- 位置: L528-528
- 役割: (未記入)
- 触るとき: (未記入)

## renderContainedImage()
- 位置: L529-529
- 役割: (未記入)
- 触るとき: (未記入)

## renderTemplate()
- 位置: L530-530
- 役割: (未記入)
- 触るとき: (未記入)

## reportActivity()
- 位置: L531-531
- 役割: (未記入)
- 触るとき: (未記入)

## requireActivityEvents()
- 位置: L532-532
- 役割: (未記入)
- 触るとき: (未記入)

## requireConsent()
- 位置: L533-533
- 役割: (未記入)
- 触るとき: (未記入)

## requireOnlyFirstPartyIds()
- 位置: L534-534
- 役割: (未記入)
- 触るとき: (未記入)

## requireSecureCookies()
- 位置: L535-535
- 役割: (未記入)
- 触るとき: (未記入)

## requireTcf20()
- 位置: L536-536
- 役割: (未記入)
- 触るとき: (未記入)

## sendPageViewEvent()
- 位置: L538-538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## sendSpaRecsClick()
- 位置: L539-539
- 役割: (未記入)
- 触るとき: (未記入)

## setAccountId()
- 位置: L540-540
- 役割: (未記入)
- 触るとき: (未記入)

## setAllConsentsTo()
- 位置: L541-541
- 役割: (未記入)
- 触るとき: (未記入)

## setClientStorageVariable()
- 位置: L542-542
- 役割: (未記入)
- 触るとき: (未記入)

## setCompatMode()
- 位置: L543-543
- 役割: (未記入)
- 触るとき: (未記入)

## setConsent()
- 位置: L544-544
- 役割: (未記入)
- 触るとき: (未記入)

## setCookie()
- 位置: L545-545
- 役割: (未記入)
- 触るとき: (未記入)

## setCustomParameters()
- 位置: L546-546
- 役割: (未記入)
- 触るとき: (未記入)

## setEventAttributes()
- 位置: L547-547
- 役割: (未記入)
- 触るとき: (未記入)

## setGeoPosition()
- 位置: L548-548
- 役割: (未記入)
- 触るとき: (未記入)

## setNodeValue()
- 位置: L549-549
- 役割: (未記入)
- 触るとき: (未記入)

## setRandomId()
- 位置: L550-550
- 役割: (未記入)
- 触るとき: (未記入)

## setRestrictionsToConsentClasses()
- 位置: L551-551
- 役割: (未記入)
- 触るとき: (未記入)

## setRetargetingParameters()
- 位置: L552-552
- 役割: (未記入)
- 触るとき: (未記入)

## setSiteId()
- 位置: L553-553
- 役割: (未記入)
- 触るとき: (未記入)

## setUserProfileParameters()
- 位置: L554-554
- 役割: (未記入)
- 触るとき: (未記入)

## setupIabCmp()
- 位置: L555-555
- 役割: (未記入)
- 触るとき: (未記入)

## setupTcfApi()
- 位置: L556-556
- 役割: (未記入)
- 触るとき: (未記入)

## shouldPollActivity()
- 位置: L557-557
- 役割: (未記入)
- 触るとき: (未記入)

## startLocalStats()
- 位置: L558-558
- 役割: (未記入)
- 触るとき: (未記入)

## startSessionAnnotation()
- 位置: L559-559
- 役割: (未記入)
- 触るとき: (未記入)

## stopAllSessionAnnotations()
- 位置: L560-560
- 役割: (未記入)
- 触るとき: (未記入)

## stopSessionAnnotation()
- 位置: L561-561
- 役割: (未記入)
- 触るとき: (未記入)

## sync()
- 位置: L562-562
- 役割: (未記入)
- 触るとき: (未記入)

## trackAmpIFrame()
- 位置: L563-563
- 役割: (未記入)
- 触るとき: (未記入)

## trackElement()
- 位置: L564-564
- 役割: (未記入)
- 触るとき: (未記入)

## trim()
- 位置: L565-565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `s.trim()`

## window.cx_pollActiveTime()
- 位置: L570-570
- 役割: (未記入)
- 触るとき: (未記入)

## window.cx_pollActivity()
- 位置: L571-571
- 役割: (未記入)
- 触るとき: (未記入)

## window.cx_pollFragmentMessage()
- 位置: L572-572
- 役割: (未記入)
- 触るとき: (未記入)

## execQueue()
- 位置: L574-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `invoke()`, `invokeOn()`, `setTimeout()`
- 参照: `queue.push`

## queue.push()
- 位置: L578-580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `invoke()`, `setTimeout()`
