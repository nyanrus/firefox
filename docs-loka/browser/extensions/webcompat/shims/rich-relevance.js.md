# browser/extensions/webcompat/shims/rich-relevance.js

source: browser/extensions/webcompat/shims/rich-relevance.js
source-hash: aea85c030a91e7104742132d2c06bdb58aa053b7
lines: 289

## <module>
- 役割: (未記入)

## getRandomString()
- 位置: L19-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(v, c => c.toString(16)).join()`, `c.toString()`, `crypto.getRandomValues()`, `s.slice()`

## call()
- 位置: L25-33
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof fn === "function")` → `fn()`
- 条件付き依存: `if (typeof fn === "function")` → `console.error()`

## r3_generic.createScript()
- 位置: L37-37
- 役割: (未記入)
- 触るとき: (未記入)

## r3_generic.destroy()
- 位置: L38-38
- 役割: (未記入)
- 触るとき: (未記入)

## r3_addtocart.addItemIdToCart()
- 位置: L43-43
- 役割: (未記入)
- 触るとき: (未記入)

## r3_addtoregistry.addItemIdCentsQuantity()
- 位置: L48-48
- 役割: (未記入)
- 触るとき: (未記入)

## r3_cart.addItemId()
- 位置: L57-57
- 役割: (未記入)
- 触るとき: (未記入)

## r3_cart.addItemIdCentsQuantity()
- 位置: L58-58
- 役割: (未記入)
- 触るとき: (未記入)

## r3_cart.addItemIdDollarsAndCentsQuantity()
- 位置: L59-59
- 役割: (未記入)
- 触るとき: (未記入)

## r3_cart.addItemIdPriceQuantity()
- 位置: L60-60
- 役割: (未記入)
- 触るとき: (未記入)

## r3_category.addItemId()
- 位置: L65-65
- 役割: (未記入)
- 触るとき: (未記入)

## r3_category.setId()
- 位置: L66-66
- 役割: (未記入)
- 触るとき: (未記入)

## r3_category.setName()
- 位置: L67-67
- 役割: (未記入)
- 触るとき: (未記入)

## r3_category.setParentId()
- 位置: L68-68
- 役割: (未記入)
- 触るとき: (未記入)

## r3_category.setTopName()
- 位置: L69-69
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.paginate()
- 位置: L78-78
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.filterPrice()
- 位置: L79-79
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.filterAttribute()
- 位置: L80-80
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addCategoryHintId()
- 位置: L82-82
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addClickthruParams()
- 位置: L83-83
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addContext()
- 位置: L84-84
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addFilter()
- 位置: L85-85
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addFilterBrand()
- 位置: L86-86
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addFilterCategory()
- 位置: L87-87
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addItemId()
- 位置: L88-88
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addItemIdToCart()
- 位置: L89-89
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addPlacementType()
- 位置: L90-90
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addRefinement()
- 位置: L91-91
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addSearchTerm()
- 位置: L92-92
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.addSegment()
- 位置: L93-93
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.blockItemId()
- 位置: L94-94
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.enableCfrad()
- 位置: L95-95
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.enableRad()
- 位置: L96-96
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.forceDebugMode()
- 位置: L97-97
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.forceDevMode()
- 位置: L98-98
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.forceDisplayMode()
- 位置: L99-99
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.forceLocale()
- 位置: L100-100
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.initFromParams()
- 位置: L101-101
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setApiKey()
- 位置: L102-102
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setBaseUrl()
- 位置: L103-103
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setCartValue()
- 位置: L104-104
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setChannel()
- 位置: L105-105
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setClickthruServer()
- 位置: L106-106
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setCurrency()
- 位置: L107-107
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setDeviceId()
- 位置: L108-108
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setFilterBrandsIncludeMatchingElements()
- 位置: L109-109
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setForcedTreatment()
- 位置: L110-110
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setImageServer()
- 位置: L111-111
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setLanguage()
- 位置: L112-112
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setMVTForcedTreatment()
- 位置: L113-113
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setNoCookieMode()
- 位置: L114-114
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setPageBrand()
- 位置: L115-115
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setPrivateMode()
- 位置: L116-116
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setRefinementFallback()
- 位置: L117-117
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setRegionId()
- 位置: L118-118
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setRegistryId()
- 位置: L119-119
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setRegistryType()
- 位置: L120-120
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setSessionId()
- 位置: L121-121
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.setUserId()
- 位置: L122-122
- 役割: (未記入)
- 触るとき: (未記入)

## r3_common.useDummyData()
- 位置: L123-123
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.addAttribute()
- 位置: L136-136
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.addCategory()
- 位置: L137-137
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.addCategoryId()
- 位置: L138-138
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setBrand()
- 位置: L139-139
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setEndDate()
- 位置: L140-140
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setId()
- 位置: L141-141
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setImageId()
- 位置: L142-142
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setLinkId()
- 位置: L143-143
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setName()
- 位置: L144-144
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setPrice()
- 位置: L145-145
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setRating()
- 位置: L146-146
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setRecommendable()
- 位置: L147-147
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setReleaseDate()
- 位置: L148-148
- 役割: (未記入)
- 触るとき: (未記入)

## r3_item.setSalePrice()
- 位置: L149-149
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.addItemId()
- 位置: L158-158
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.addItemIdCentsQuantity()
- 位置: L159-159
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.addItemIdDollarsAndCentsQuantity()
- 位置: L160-160
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.addItemIdPriceQuantity()
- 位置: L161-161
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.setOrderNumber()
- 位置: L162-162
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.setPromotionCode()
- 位置: L163-163
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.setShippingCost()
- 位置: L164-164
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.setTaxes()
- 位置: L165-165
- 役割: (未記入)
- 触るとき: (未記入)

## r3_purchased.setTotalPrice()
- 位置: L166-166
- 役割: (未記入)
- 触るとき: (未記入)

## r3_search.addItemId()
- 位置: L171-171
- 役割: (未記入)
- 触るとき: (未記入)

## r3_search.setTerms()
- 位置: L172-172
- 役割: (未記入)
- 触るとき: (未記入)

## r3_wishlist.addItemId()
- 位置: L177-177
- 役割: (未記入)
- 触るとき: (未記入)

## add()
- 位置: L181-181
- 役割: (未記入)
- 触るとき: (未記入)

## addItemId()
- 位置: L182-182
- 役割: (未記入)
- 触るとき: (未記入)

## addItemIdCentsQuantity()
- 位置: L183-183
- 役割: (未記入)
- 触るとき: (未記入)

## addItemIdDollarsAndCentsQuantity()
- 位置: L184-184
- 役割: (未記入)
- 触るとき: (未記入)

## addItemIdPriceQuantity()
- 位置: L185-185
- 役割: (未記入)
- 触るとき: (未記入)

## addItemIdToCart()
- 位置: L186-186
- 役割: (未記入)
- 触るとき: (未記入)

## addObject()
- 位置: L187-187
- 役割: (未記入)
- 触るとき: (未記入)

## addSearchTerm()
- 位置: L188-188
- 役割: (未記入)
- 触るとき: (未記入)

## c()
- 位置: L189-189
- 役割: (未記入)
- 触るとき: (未記入)

## checkParamCookieValue()
- 位置: L191-191
- 役割: (未記入)
- 触るとき: (未記入)

## debugWindow()
- 位置: L198-198
- 役割: (未記入)
- 触るとき: (未記入)

## defaultCallback()
- 位置: L199-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## fixName()
- 位置: L202-202
- 役割: (未記入)
- 触るとき: (未記入)

## genericAddItemPriceQuantity()
- 位置: L203-203
- 役割: (未記入)
- 触るとき: (未記入)

## get()
- 位置: L204-204
- 役割: (未記入)
- 触るとき: (未記入)

## getDomElement()
- 位置: L205-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`

## id()
- 位置: L208-208
- 役割: (未記入)
- 触るとき: (未記入)

## insert()
- 位置: L209-209
- 役割: (未記入)
- 触るとき: (未記入)

## insertDynamicPlacement()
- 位置: L210-210
- 役割: (未記入)
- 触るとき: (未記入)

## isArray()
- 位置: L211-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`

## js()
- 位置: L212-212
- 役割: (未記入)
- 触るとき: (未記入)

## jsonCallback()
- 位置: L213-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `call()`

## lc()
- 位置: L217-217
- 役割: (未記入)
- 触るとき: (未記入)

## ol()
- 位置: L219-219
- 役割: (未記入)
- 触るとき: (未記入)

## pq()
- 位置: L221-221
- 役割: (未記入)
- 触るとき: (未記入)

## registerPageType()
- 位置: L223-223
- 役割: (未記入)
- 触るとき: (未記入)

## renderDynamicPlacements()
- 位置: L240-240
- 役割: (未記入)
- 触るとき: (未記入)

## set()
- 位置: L241-241
- 役割: (未記入)
- 触るとき: (未記入)

## setCharset()
- 位置: L242-242
- 役割: (未記入)
- 触るとき: (未記入)

## unregisterAllPageType()
- 位置: L244-244
- 役割: (未記入)
- 触るとき: (未記入)

## unregisterPageType()
- 位置: L245-245
- 役割: (未記入)
- 触るとき: (未記入)

## r3()
- 位置: L249-249
- 役割: (未記入)
- 触るとき: (未記入)

## r3_placement()
- 位置: L261-261
- 役割: (未記入)
- 触るとき: (未記入)

## rr_addLoadEvent()
- 位置: L266-266
- 役割: (未記入)
- 触るとき: (未記入)

## rr_call_after_flush()
- 位置: L268-268
- 役割: (未記入)
- 触るとき: (未記入)

## rr_create_script()
- 位置: L269-269
- 役割: (未記入)
- 触るとき: (未記入)

## rr_flush()
- 位置: L273-273
- 役割: (未記入)
- 触るとき: (未記入)

## rr_flush_onload()
- 位置: L274-274
- 役割: (未記入)
- 触るとき: (未記入)

## rr_insert_placement()
- 位置: L275-275
- 役割: (未記入)
- 触るとき: (未記入)
