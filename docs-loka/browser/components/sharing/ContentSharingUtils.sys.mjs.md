# browser/components/sharing/ContentSharingUtils.sys.mjs

source: browser/components/sharing/ContentSharingUtils.sys.mjs
source-hash: d3d0b2d7e4ee3d7205263c91d9d831862e0cab44
lines: 728

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## loadContentSharingSchema()
- 位置: async L51-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SCHEMA_MAP.has()`, `SCHEMA_MAP.set()`, `fetch()`, `response.json()`
- 条件付き依存: `if (SCHEMA_MAP.has("CONTENT_SHARING_SCHEMA"))` → `SCHEMA_MAP.get()`
- 参照: `response.ok`, `response.statusText`

## makeShareResult()
- 位置: L89-98
- 役割: (未記入)
- 触るとき: (未記入)

## ContentSharingUtilsClass.isEnabled()
- 位置: L107-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `lazy.CONTENT_SHARING_ENABLED`
- XPCOM: `Services.wm`

## ContentSharingUtilsClass.serverURL()
- 位置: L114-116
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.CONTENT_SHARING_SERVER_URL`

## ContentSharingUtilsClass.redirectURL()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.serverURL`

## ContentSharingUtilsClass.disable()
- 位置: L122-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## ContentSharingUtilsClass.getValidator()
- 位置: async L127-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadContentSharingSchema()`
- 参照: `lazy.JsonSchema.Validator`, `this.#validator`

## ContentSharingUtilsClass.getLinkValidator()
- 位置: async L142-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadContentSharingSchema()`
- 参照: `lazy.JsonSchema.Validator`, `schema.$defs.Link`, `schema.$schema`, `this.#linkValidator`

## ContentSharingUtilsClass.createShareableLinkFromBookmarkFolders()
- 位置: async L161-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.buildShareFromBookmarkFolders()`
- 条件付き依存: `if (shareResult)` → `this.#createLinkAndOpenModal()`

## ContentSharingUtilsClass.handleShareTabs()
- 位置: async L179-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.contentSharingL10n.formatValue()`, `tabs.map()`, `this.#createLinkAndOpenModal()`, `this.buildShare()`, `this.countItems()`, `this.getLinkValidator()`
- 参照: `result.share`, `result.share.title`, `t.label`, `t.linkedBrowser.currentURI.spec`, `tabs.length`

## ContentSharingUtilsClass.handleShareTabGroup()
- 位置: async L212-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabGroup.tabs.map()`, `this.#createLinkAndOpenModal()`, `this.buildShare()`, `this.getLinkValidator()`
- 条件付き依存: `if (!title)` → `tabGroup.ownerDocument.l10n.formatValue()`
- 参照: `t.label`, `t.linkedBrowser.currentURI.displaySpec`, `tabGroup.label`

## ContentSharingUtilsClass.buildShareFromBookmarkFolders()
- 位置: async L246-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buildShare()`, `this.getLinkValidator()`
- 条件付き依存: `if (bookmarkFolderGuids.length === 1)` → `lazy.PlacesUtils.promiseBookmarksTree()`
- 条件付き依存: `if (!(bookmarkFolderGuids.length === 1))` → `lazy.PlacesUtils.promiseBookmarksTree()`
- 条件付き依存: `if (!(bookmarkFolderGuids.length === 1))` → `bookmarkFolderGuids.slice()`
- 条件付き依存: `if (!(bookmarkFolderGuids.length === 1))` → `bookmark.children.push()`
- 参照: `bookmark.children`, `bookmark.type`, `bookmarkFolderGuids.length`

## ContentSharingUtilsClass.makeValidLink()
- 位置: L286-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `linkObject.title?.slice()`, `linkObject.uri.match()`, `this.#linkValidator?.validate()`, `url.toString()`, `url.toString().slice()`
- 参照: `linkObject.uri`, `this.#linkValidator?.validate(link).valid`

## ContentSharingUtilsClass.buildShare()
- 位置: L340-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeShareResult()`, `shareObject.title.slice()`
- 条件付き依存: `if (linkOrNestShare.uri)` → `this.makeValidLink()`
- 条件付き依存: `if (validLink)` → `links.push()`
- 条件付き依存: `if (linkOrNestShare.children)` → `this.buildShare()`
- 条件付き依存: `if (nestedShare.links.length)` → `links.push()`
- 参照: `WARNINGS.TOO_MANY_LINKS`, `currentCount.value`, `linkOrNestShare.children`, `linkOrNestShare.type`, `linkOrNestShare.uri`, `nestedShare.links.length`, `share.links`, `shareObject.children`, `shareObject.type`, `shareResult.share`, `shareResult.warning`

## ContentSharingUtilsClass.#createLinkAndOpenModal()
- 位置: async L398-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.collectionShare.dialogOpen.record()`, `Services.wm.getMostRecentBrowserWindow()`, `console.error()`, `lazy.URILoadingHelper.switchToTabHavingURI()`, `resolveLoading()`, `this.createShareableLink()`, `this.detectLogin()`, `this.isSignedIn()`, `window.gDialogBox.open()`, `window.openWebLinkIn()`, `window.top.document.documentElement.removeAttribute()`
- 条件付き依存: `if (shareResult.error && !shareResult.isSignedIn)` → `console.error()`
- 条件付き依存: `if (shareResult.error)` → `console.error()`
- 参照: `ERRORS.UNAUTHORIZED`, `shareResult.error`, `shareResult.isSignedIn`, `shareResult.url`, `this.redirectURL`, `window.innerWidth`
- XPCOM: `Services.wm`

## ContentSharingUtilsClass.#doRequest()
- 位置: async L490-608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.collectionShare.error.record()`, `JSON.stringify()`, `URL.parse()`, `console.error()`, `fetch()`, `response.json()`, `this.isSignedIn()`, `this.serverURL.startsWith()`
- 条件付き依存: `if (!this.serverURL)` → `console.error()`
- 条件付き依存: `if (!this.serverURL)` → `Glean.collectionShare.error.record()`
- 条件付き依存: `if ( !Cu.isInAutomation && AppConstants.MOZILLA_OFFICIAL && !this.serverURL.startsWith("https://") )` → `console.error()`
- 条件付き依存: `if (attempts >= MAX_REQUEST_ATTEMPTS)` → `console.error()`
- 条件付き依存: `if (attempts > 0)` → `Math.random()`
- 条件付き依存: `if (attempts > 0)` → `Math.min()`
- 条件付き依存: `if (attempts > 0)` → `Math.pow()`
- 条件付き依存: `if (attempts > 0)` → `lazy.setTimeout()`
- 条件付き依存: `if (!response.ok)` → `Glean.collectionShare.error.record()`
- 条件付き依存: `if (response.status === 410)` → `this.disable()`
- 条件付き依存: `if (!shareURL || !serverOrigin || shareURL.origin !== serverOrigin)` → `console.error()`
- 参照: `AppConstants.MOZILLA_OFFICIAL`, `Cu.isInAutomation`, `ERRORS.DISABLED`, `ERRORS.GENERIC`, `ERRORS.MAX_REQUEST_ATTEMPTS`, `ERRORS.MAX_RETRY_ATTEMPTS`, `ERRORS.UNAUTHORIZED`, `URL.parse(this.serverURL)?.origin`, `response.ok`, `response.status`, `shareResult.error`, `shareResult.share`, `shareResult.url`, `shareURL.origin`, `this.serverURL`

## ContentSharingUtilsClass.createShareableLink()
- 位置: async L610-617
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#doRequest()`, `this.validateSchema()`
- 参照: `shareResult.error`

## ContentSharingUtilsClass.countItems()
- 位置: L619-634
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (item.links)` → `this.countItems()`
- 参照: `item.links`, `share.links`, `share.links.length`

## ContentSharingUtilsClass.validateSchema()
- 位置: async L636-647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.countItems()`, `this.getValidator()`, `validator.validate()`
- 条件付き依存: `if (!result.valid || this.countItems(shareResult.share) > MAX_ITEM_COUNT)` → `Glean.collectionShare.error.record()`
- 参照: `ERRORS.INVALID_SCHEMA`, `result.valid`, `shareResult.error`, `shareResult.isSchemaValid`, `shareResult.share`

## ContentSharingUtilsClass.getCookie()
- 位置: L649-677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Services.cookies.getCookiesFromHost()`, `console.error()`, `cookies.find()`
- 参照: `authCookie?.value`, `cookie.expiry`, `cookie.host`, `cookie.name`, `lazy.CONTENT_SHARING_SERVER_URL`, `serverURL.hostname`
- XPCOM: `Services.cookies`

## ContentSharingUtilsClass.isSignedIn()
- 位置: L679-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getCookie()`

## ContentSharingUtilsClass.detectLogin()
- 位置: async L690-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `lazy.clearTimeout()`, `lazy.setTimeout()`, `promise.finally()`, `reject()`
- 参照: `Cu.isInAutomation`, `lazy.CONTENT_SHARING_LOGIN_TIMEOUT_MS`, `this.cookieChangeObserver`, `this.cookieChangePromise`, `this.cookieChangeTimer`, `this.observingCookieChange`
- XPCOM: `Services.obs`

## observe()
- 位置: L704-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isSignedIn()`
- 条件付き依存: `if (this.isSignedIn())` → `resolve()`
