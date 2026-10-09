# browser/extensions/webcompat/shims/adnexus-ast.js

source: browser/extensions/webcompat/shims/adnexus-ast.js
source-hash: ae07fa6a0363ffa5c540713925bd98862a448bef
lines: 211

## <module>
- 役割: (未記入)

## constructor()
- 位置: L48-51
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.tagId`, `this.targetId`

## fireAdEvent()
- 位置: L54-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb()`, `console.error()`, `done()`, `setTimeout()`
- 条件付き依存: `if (!handlers)` → `Promise.resolve()`

## refreshTag()
- 位置: L75-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fireAdEvent()`, `fireAdEvent("adRequested", adObj).then()`, `gAds.get()`, `gAds.has()`, `gTags.get()`
- 条件付き依存: `if (!gAds.has(targetId))` → `gAds.set()`
- 参照: `tag.tagId`

## off()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gEventHandlers[type]?.[targetId]?.delete()`

## on()
- 位置: L94-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gEventHandlers[type][targetId].add()`

## constructor()
- 位置: L117-123
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Tag.#nextId`, `this.keywords`, `this.sizes`, `this.tagId`, `this.targetId`

## modifyTag()
- 位置: L124-124
- 役割: (未記入)
- 触るとき: (未記入)

## off()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `off()`
- 参照: `this.targetId`

## on()
- 位置: L128-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `on()`
- 参照: `this.targetId`

## setKeywords()
- 位置: L131-133
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.keywords`

## attachClickTrackers()
- 位置: L138-138
- 役割: (未記入)
- 触るとき: (未記入)

## checkAdAvailable()
- 位置: L139-139
- 役割: (未記入)
- 触るとき: (未記入)

## clearPageTargeting()
- 位置: L140-140
- 役割: (未記入)
- 触るとき: (未記入)

## clearRequest()
- 位置: L141-141
- 役割: (未記入)
- 触るとき: (未記入)

## collapseAd()
- 位置: L142-142
- 役割: (未記入)
- 触るとき: (未記入)

## defineTag()
- 位置: L144-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTags.set()`

## disableDebug()
- 位置: L151-151
- 役割: (未記入)
- 触るとき: (未記入)

## emitEvent()
- 位置: L153-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fireAdEvent()`

## enableCookieSet()
- 位置: L156-156
- 役割: (未記入)
- 触るとき: (未記入)

## enableDebug()
- 位置: L157-157
- 役割: (未記入)
- 触るとき: (未記入)

## fireImpressionTrackers()
- 位置: L158-158
- 役割: (未記入)
- 触るとき: (未記入)

## getAdMarkup()
- 位置: L159-159
- 役割: (未記入)
- 触るとき: (未記入)

## getAdWrap()
- 位置: L160-160
- 役割: (未記入)
- 触るとき: (未記入)

## getAstVersion()
- 位置: L161-161
- 役割: (未記入)
- 触るとき: (未記入)

## getPageTargeting()
- 位置: L162-162
- 役割: (未記入)
- 触るとき: (未記入)

## getTag()
- 位置: L163-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTags.get()`

## handleCb()
- 位置: L166-166
- 役割: (未記入)
- 触るとき: (未記入)

## handleMediationBid()
- 位置: L167-167
- 役割: (未記入)
- 触るとき: (未記入)

## highlightAd()
- 位置: L168-168
- 役割: (未記入)
- 触るとき: (未記入)

## loadTags()
- 位置: L170-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTags.keys()`, `refreshTag()`

## modifyTag()
- 位置: L175-175
- 役割: (未記入)
- 触るとき: (未記入)

## notify()
- 位置: L176-176
- 役割: (未記入)
- 触るとき: (未記入)

## offEvent()
- 位置: L177-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `off()`

## onEvent()
- 位置: L180-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `on()`

## recordErrorEvent()
- 位置: L183-183
- 役割: (未記入)
- 触るとき: (未記入)

## refresh()
- 位置: L184-184
- 役割: (未記入)
- 触るとき: (未記入)

## registerRenderer()
- 位置: L185-185
- 役割: (未記入)
- 触るとき: (未記入)

## resizeAd()
- 位置: L187-187
- 役割: (未記入)
- 触るとき: (未記入)

## setEndpoint()
- 位置: L188-188
- 役割: (未記入)
- 触るとき: (未記入)

## setKeywords()
- 位置: L189-189
- 役割: (未記入)
- 触るとき: (未記入)

## setPageOpts()
- 位置: L190-190
- 役割: (未記入)
- 触るとき: (未記入)

## setPageTargeting()
- 位置: L191-191
- 役割: (未記入)
- 触るとき: (未記入)

## setSafeFrameConfig()
- 位置: L192-192
- 役割: (未記入)
- 触るとき: (未記入)

## setSizes()
- 位置: L193-193
- 役割: (未記入)
- 触るとき: (未記入)

## showTag()
- 位置: L194-194
- 役割: (未記入)
- 触るとき: (未記入)

## push()
- 位置: L197-205
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof fn === "function")` → `fn()`
- 条件付き依存: `if (typeof fn === "function")` → `console.trace()`
