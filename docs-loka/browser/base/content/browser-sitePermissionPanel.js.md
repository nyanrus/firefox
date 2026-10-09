# browser/base/content/browser-sitePermissionPanel.js

source: browser/base/content/browser-sitePermissionPanel.js
source-hash: 6a4ed1d46f50c1c25423f6e2be25508dde0f4fae
lines: 1270

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## _initializePopup()
- 位置: L24-32
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._popupInitialized)` → `document.getElementById()`
- 条件付き依存: `if (!this._popupInitialized)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this._popupInitialized)` → `this._permissionPopup.addEventListener()`
- 参照: `this._popupInitialized`, `wrapper.content`

## hidePopup()
- 位置: L34-38
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._popupInitialized)` → `PanelMultiView.hidePopup()`
- 参照: `this._permissionPopup`, `this._popupInitialized`

## setAnchor()
- 位置: L48-51
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._popupAnchorNode`, `this._popupPosition`

## setBrowserOverride()
- 位置: L56-58
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._browserOverride`

## clearBrowserOverride()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._browserOverride`

## _activeBrowser()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gBrowser.selectedBrowser`, `this._browserOverride`

## browser()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._activeBrowser`

## _popupAnchor()
- 位置: L70-75
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._identityPermissionBox`, `this._popupAnchorNode`

## _identityPermissionBox()
- 位置: L76-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPermissionBox`

## _permissionGrantedIcon()
- 位置: L82-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionGrantedIcon`

## _permissionPopup()
- 位置: L88-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionPopup`, `this._popupInitialized`

## _permissionPopupMainView()
- 位置: L96-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionPopupPopupMainView`

## _permissionPopupMainViewHeaderLabel()
- 位置: L102-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionPopupMainViewHeaderLabel`

## _permissionList()
- 位置: L108-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionList`

## _defaultPermissionAnchor()
- 位置: L114-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._defaultPermissionAnchor`

## _permissionReloadHint()
- 位置: L120-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionReloadHint`

## _permissionAnchors()
- 位置: L126-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchor.getAttribute()`, `document.getElementById()`
- 参照: `document.getElementById("blocked-permissions-container") .children`, `this._permissionAnchors`

## _geoSharingIcon()
- 位置: L136-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._geoSharingIcon`

## _xrSharingIcon()
- 位置: L141-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._xrSharingIcon`

## _serialSharingIcon()
- 位置: L146-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._serialSharingIcon`

## _webRTCSharingIcon()
- 位置: L153-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._webRTCSharingIcon`

## _refreshPermissionPopup()
- 位置: L164-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gIdentityHandler.getHostForDisplay()`, `gNavigatorBundle.getFormattedString()`, `this.updateSitePermissions()`
- 参照: `this._browserOverride?.currentURI`, `this._permissionPopupMainViewHeaderLabel.textContent`

## hidePermissionIcons()
- 位置: L181-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._identityPermissionBox.removeAttribute()`

## refreshPermissionIcons()
- 位置: L189-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `SitePermissions.getAllForBrowser()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.getBlockedPopupCount()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.isRedirectBlocked()`, `icon.removeAttribute()`, `this._identityPermissionBox.toggleAttribute()`
- 条件付き依存: `if (icon)` → `icon.setAttribute()`
- 条件付き依存: `if ( gBrowser.selectedBrowser.popupAndRedirectBlocker.getBlockedPopupCount() || gBrowser.selectedBrowser.popupAndRedirectBlocker.isRedirectBlocked() )` → `icon.setAttribute()`
- 参照: `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`, `SitePermissions.PROMPT`, `SitePermissions.UNKNOWN`, `gBrowser.selectedBrowser`, `permission.id`, `permission.state`, `permissionAnchors.popup`, `this._gumShowAlwaysAsk`, `this._permissionAnchors`

## openPopup()
- 位置: L249-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `PanelMultiView.hidePopup()`, `PanelMultiView.openPopup()`, `document.querySelectorAll()`, `this._initializePopup()`, `this._refreshPermissionPopup()`
- 条件付き依存: `if (document.fullscreen)` → `Services.obs.addObserver()`
- 条件付き依存: `if (document.fullscreen)` → `window.addEventListener()`
- 条件付き依存: `if (document.fullscreen)` → `document.exitFullscreen()`
- 参照: `console.error`, `document.fullscreen`, `this._event`, `this._exitedEventReceived`, `this._permissionPopup`, `this._permissionReloadHint.hidden`, `this._popupAnchor`, `this._popupPosition`
- XPCOM: `Services.obs`

## updateSharingIndicator()
- 位置: L298-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._geoSharingIcon.removeAttribute()`, `this._identityPermissionBox.toggleAttribute()`, `this._serialSharingIcon.removeAttribute()`, `this._webRTCSharingIcon.removeAttribute()`, `this._xrSharingIcon.removeAttribute()`
- 条件付き依存: `if (this._sharingState.webRTC.sharing)` → `this._webRTCSharingIcon.setAttribute()`
- 条件付き依存: `if (this._sharingState.webRTC.paused)` → `this._webRTCSharingIcon.setAttribute()`
- 条件付き依存: `if (!(this._sharingState.webRTC.sharing))` → `hasMicCamGracePeriodsSolely()`
- 条件付き依存: `if (micGrace || camGrace)` → `this._webRTCSharingIcon.setAttribute()`
- 条件付き依存: `if (this._sharingState.geo)` → `this._geoSharingIcon.setAttribute()`
- 条件付き依存: `if (this._sharingState.xr)` → `this._xrSharingIcon.setAttribute()`
- 条件付き依存: `if (this._sharingState.serial)` → `this._serialSharingIcon.setAttribute()`
- 条件付き依存: `if (this._popupInitialized && this._permissionPopup.state != "closed")` → `this.updateSitePermissions()`
- 参照: `browser._sharingState`, `gBrowser.selectedBrowser`, `this._permissionPopup.state`, `this._popupInitialized`, `this._sharingState`, `this._sharingState.geo`, `this._sharingState.serial`, `this._sharingState.webRTC`, `this._sharingState.webRTC.paused`, `this._sharingState.webRTC.sharing`, `this._sharingState.xr`

## handleIdentityButtonEvent()
- 位置: L368-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `gURLBar.getAttribute()`, `gURLBar.hasAttribute()`, `this.openPopup()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`, `this._sharingState`

## handleEvent()
- 位置: L399-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elem.compareDocumentPosition()`, `this._permissionPopup.hasAttribute()`
- 条件付き依存: `if (event.target == this._permissionPopup)` → `window.addEventListener()`
- 条件付き依存: `if (event.target == this._permissionPopup)` → `window.removeEventListener()`
- 条件付き依存: `if ( !( position & (Node.DOCUMENT_POSITION_CONTAINS | Node.DOCUMENT_POSITION_CONTAINED_BY) ) && !this._permissionPopup.hasAttribute("noautohide") )` → `PanelMultiView.hidePopup()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `Node.DOCUMENT_POSITION_CONTAINS`, `document.activeElement`, `event.target`, `event.type`, `this._permissionPopup`

## observe()
- 位置: L434-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this.openPopup()`
- 参照: `this._event`, `this._exitedEventReceived`
- XPCOM: `Services.obs`

## onLocationChange()
- 位置: L448-452
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._permissionPopup.state`, `this._permissionReloadHint.hidden`, `this._popupInitialized`

## updateSitePermissions()
- 位置: L457-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getSite()`, `Services.io.newURI()`, `SitePermissions.getAllPermissionDetailsForBrowser()`, `e.remove()`, `permission.id.split()`, `permissions .map()`, `permissions.filter()`, `thirdPartyStorageSites.has()`, `this._permissionList .querySelectorAll()`, `this._permissionList .querySelectorAll(permissionItemSelector) .forEach()`, `this._permissionList.querySelector()`, `this.browser.popupAndRedirectBlocker.getBlockedPopupCount()`, `this.browser.popupAndRedirectBlocker.isRedirectBlocked()`
- 条件付き依存: `if (this._sharingState?.geo)` → `permissions.find()`
- 条件付き依存: `if (!(geoPermission))` → `permissions.push()`
- 条件付き依存: `if (this._sharingState?.xr)` → `permissions.find()`
- 条件付き依存: `if (!(xrPermission))` → `permissions.push()`
- 条件付き依存: `if (this._sharingState?.serial)` → `permissions.find()`
- 条件付き依存: `if (!(serialPermission))` → `permissions.push()`
- 条件付き依存: `if (webrtcState[id])` → `permission.id.split()`
- 条件付き依存: `if (!found)` → `permissions.push()`
- 条件付き依存: `if (id == "open-protocol-handler")` → `this._createProtocolHandlerPermissionItem()`
- 条件付き依存: `if (permContainer)` → `anchor.appendChild()`
- 条件付き依存: `if (!(id == "open-protocol-handler"))` → `["camera", "screen", "microphone", "speaker"].includes()`
- 条件付き依存: `if (["camera", "screen", "microphone", "speaker"].includes(id))` → `this._createWebRTCPermissionItem()`
- 条件付き依存: `if (["camera", "screen", "microphone", "speaker"].includes(id))` → `anchor.appendChild()`
- 条件付き依存: `if (!(["camera", "screen", "microphone", "speaker"].includes(id)))` → `this._createPermissionItem()`
- 条件付き依存: `if (id == "3rdPartyFrameStorage")` → `this._permissionList.querySelector()`
- 条件付き依存: `if (!(["camera", "screen", "microphone", "speaker"].includes(id)))` → `anchor.appendChild()`
- 条件付き依存: `if (id == "popup" && showBlockedIndicator)` → `this._createBlockedPopupIndicator()`
- 条件付き依存: `if (id == "geo" && permission.state === SitePermissions.ALLOW)` → `this._createGeoLocationLastAccessIndicator()`
- 条件付き依存: `if (showBlockedIndicator && !hasBlockedIndicator)` → `SitePermissions.getDefault()`
- 条件付き依存: `if (showBlockedIndicator && !hasBlockedIndicator)` → `this._createPermissionItem()`
- 条件付き依存: `if (showBlockedIndicator && !hasBlockedIndicator)` → `this._defaultPermissionAnchor.appendChild()`
- 条件付き依存: `if (showBlockedIndicator && !hasBlockedIndicator)` → `this._createBlockedPopupIndicator()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.PERM_KEY_DELIMITER`, `SitePermissions.PROMPT`, `SitePermissions.SCOPE_PERSISTENT`, `SitePermissions.SCOPE_REQUEST`, `geoPermission.sharingState`, `perm.id`, `permission.sharingState`, `permission.state`, `serialPermission.sharingState`, `this._defaultPermissionAnchor`, `this._gumShowAlwaysAsk`, `this._permissionLabelIndex`, `this._sharingState`, `this._sharingState.webRTC`, `this._sharingState?.geo`, `this._sharingState?.serial`, `this._sharingState?.webRTC`, `this._sharingState?.xr`, `this.browser`, `this.browser._sharingState`, `xrPermission.sharingState`
- XPCOM: `Services.eTLD` / `Services.io`

## _createPermissionItem()
- 位置: L686-868
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.getPermissionLabel()`, `[ SitePermissions.SCOPE_POLICY, SitePermissions.SCOPE_GLOBAL, ].includes()`, `container.appendChild()`, `container.classList.add()`, `container.setAttribute()`, `document.createXULElement()`, `img.classList.add()`, `nameLabel.setAttribute()`, `permission.sharingState.includes()`
- 条件付き依存: `if ( permission.state == SitePermissions.BLOCK || permission.state == SitePermissions.AUTOPLAY_BLOCKED_ALL )` → `img.classList.add()`
- 条件付き依存: `if ( permission.sharingState == Ci.nsIMediaManagerService.STATE_CAPTURE_ENABLED || (idNoSuffix == "screen" && permission.sharingState && !permission.sharingState...)` → `img.classList.add()`
- 条件付き依存: `if (nowrapLabel)` → `nameLabel.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `document.createXULElement()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `block.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menulist.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `Services.prefs.prefIsLocked()`
- 条件付き依存: `if ( idNoSuffix == "popup" && Services.prefs.prefIsLocked("dom.disable_open_during_load") )` → `menulist.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `SitePermissions.getAvailableStates()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `SitePermissions.getDefault()`
- 条件付き依存: `if (state == SitePermissions.getDefault(idNoSuffix))` → `menuitem.setAttribute()`
- 条件付き依存: `if (!(state == SitePermissions.getDefault(idNoSuffix)))` → `menuitem.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menuitem.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `SitePermissions.getMultichoiceStateLabel()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menupopup.appendChild()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menulist.appendChild()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menulist.addEventListener()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `container.appendChild()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `container.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `block.appendChild()`
- 条件付き依存: `if (showStateLabel)` → `this._createStateLabel()`
- 条件付き依存: `if (stateLabel)` → `container.appendChild()`
- 条件付き依存: `if (isContainer)` → `document.createXULElement()`
- 条件付き依存: `if (isContainer)` → `block.setAttribute()`
- 条件付き依存: `if (permClearButton)` → `this._createPermissionClearButton()`
- 条件付き依存: `if (stateLabel)` → `button.appendChild()`
- 条件付き依存: `if (permClearButton)` → `container.appendChild()`
- 条件付き依存: `if (isContainer)` → `block.appendChild()`
- 参照: `Ci.nsIMediaManagerService.STATE_CAPTURE_ENABLED`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`, `SitePermissions.SCOPE_GLOBAL`, `SitePermissions.SCOPE_POLICY`, `gBrowser.contentPrincipal`, `menulist.selectedItem.value`, `menulist.value`, `nameLabel.textContent`, `permission.id`, `permission.scope`, `permission.sharingState`, `permission.state`, `stateLabel.id`, `this ._permissionLabelIndex`
- XPCOM: [`nsIMediaManagerService`](../../../dom/media/nsIMediaManager.idl.md) / `Services.prefs`

## _createStateLabel()
- 位置: L870-889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.getCurrentStateLabel()`, `document.createXULElement()`, `label.setAttribute()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.SCOPE_REQUEST`, `aPermission.sharingState`, `label.textContent`, `this ._permissionLabelIndex`

## _removePermPersistentAllow()
- 位置: L891-899
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.getForPrincipal()`
- 条件付き依存: `if ( perm.state == SitePermissions.ALLOW && perm.scope == SitePermissions.SCOPE_PERSISTENT )` → `SitePermissions.removeFromPrincipal()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.SCOPE_PERSISTENT`, `perm.scope`, `perm.state`

## _createPermissionClearButton()
- 位置: L901-998
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.removeFromPrincipal()`, `button.addEventListener()`, `button.setAttribute()`, `clearCallback()`, `container.remove()`, `document.createXULElement()`, `gNavigatorBundle.getString()`
- 条件付き依存: `if (permission.sharingState && idNoSuffix === "xr")` → `browser.getDevicePermissionOrigins()`
- 条件付き依存: `if (permission.sharingState && idNoSuffix === "xr")` → `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`
- 条件付き依存: `if (permission.sharingState && idNoSuffix === "xr")` → `this._removePermPersistentAllow()`
- 条件付き依存: `if (permission.sharingState && idNoSuffix === "xr")` → `origins.clear()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `permission.id.split()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `SitePermissions.getAllForBrowser()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `permissions.filter()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `removePermission.id.split()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `Services.io.newURI()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `Services.eTLD.getSite()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `SitePermissions.removeFromPrincipal()`
- 条件付き依存: `if (idNoSuffix === "desktop-notification")` → `Glean.webNotificationPermission.permissionRevokedToolbar.record()`
- 条件付き依存: `if (idNoSuffix === "desktop-notification")` → `SiteCategory.getCategory()`
- 条件付き依存: `if (idNoSuffix === "geo")` → `gBrowser.updateBrowserSharing()`
- 条件付き依存: `if (idNoSuffix === "xr")` → `gBrowser.updateBrowserSharing()`
- 条件付き依存: `if (idNoSuffix === "serial")` → `SerialDeviceSharingHelper.resetBrowserCount()`
- 条件付き依存: `if (idNoSuffix === "serial")` → `gBrowser.updateBrowserSharing()`
- 条件付き依存: `if (idNoSuffix === "serial")` → `Services.obs.notifyObservers()`
- 参照: `SitePermissions.PERM_KEY_DELIMITER`, `browser.browsingContext`, `browser.contentPrincipal`, `gBrowser.contentPrincipal`, `permission.id`, `permission.sharingState`, `removePermission.id`, `this._permissionReloadHint.hidden`, `this.browser`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.obs` / `Services.scriptSecurityManager`

## _getGeoLocationLastAccess()
- 位置: L1000-1017
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentPrefService2.getByDomainAndName()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.loadContext`

## handleResult()
- 位置: L1008-1010
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `pref.value`

## handleCompletion()
- 位置: L1011-1013
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## _createGeoLocationLastAccessIndicator()
- 位置: async L1019-1062
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `document.getElementById()`, `gNavigatorBundle.getFormattedString()`, `geoContainer.appendChild()`, `indicator.appendChild()`, `indicator.setAttribute()`, `isNaN()`, `text.setAttribute()`, `this._getGeoLocationLastAccess()`, `timeFormat.formatBestUnit()`
- 条件付き依存: `if (isNaN(lastAccess))` → `console.error()`
- 参照: `Services.intl.RelativeTimeFormat`, `text.textContent`
- XPCOM: `Services.intl`

## _createWebRTCPermissionItem()
- 位置: L1074-1113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["camera", "screen", "microphone", "speaker"].includes()`, `document.querySelector()`, `this._createPermissionItem()`
- 条件付き依存: `if (item)` → `item.remove()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.PROMPT`, `permission.state`

## clearCallback()
- 位置: L1109-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `webrtcUI.clearPermissionsAndStopSharing()`
- 参照: `this.browser`

## _createProtocolHandlerPermissionItem()
- 位置: L1115-1172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.appendChild()`, `container.appendChild()`, `document.createXULElement()`, `document.getElementById()`, `gNavigatorBundle.getFormattedString()`, `item.appendChild()`, `item.setAttribute()`, `text.setAttribute()`, `this._createPermissionClearButton()`, `this._createStateLabel()`
- 条件付き依存: `if (!container)` → `this._createPermissionItem()`
- 参照: `text.textContent`

## clearCallback()
- 位置: L1156-1163
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (container.childElementCount <= 1)` → `container.remove()`
- 参照: `container.childElementCount`

## _createBlockedRedirectText()
- 位置: L1174-1184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.unblockFirstRedirect()`, `text.addEventListener()`, `text.setAttribute()`

## _createBlockedPopupText()
- 位置: L1186-1198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.unblockAllPopups()`, `text.addEventListener()`, `text.setAttribute()`

## _createBlockedPopupIndicator()
- 位置: L1200-1219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `document .getElementById()`, `document .getElementById("permission-popup-container") .appendChild()`, `document.createXULElement()`, `indicator.setAttribute()`
- 条件付き依存: `if (aIsRedirectBlocked)` → `indicator.appendChild()`
- 条件付き依存: `if (aIsRedirectBlocked)` → `this._createBlockedRedirectText()`
- 条件付き依存: `if (aTotalBlockedPopups)` → `indicator.appendChild()`
- 条件付き依存: `if (aTotalBlockedPopups)` → `this._createBlockedPopupText()`

## hasMicCamGracePeriodsSolely()
- 位置: L1229-1262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.getAllForBrowser()`, `perm.id.split()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.PERM_KEY_DELIMITER`, `SitePermissions.SCOPE_PERSISTENT`, `SitePermissions.SCOPE_TEMPORARY`, `perm.scope`, `perm.state`
