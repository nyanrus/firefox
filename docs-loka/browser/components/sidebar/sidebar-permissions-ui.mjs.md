# browser/components/sidebar/sidebar-permissions-ui.mjs

source: browser/components/sidebar/sidebar-permissions-ui.mjs
source-hash: 677a84f87e589f126fea66c28676ab8e645f7f1b
lines: 368

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SidebarPermissionsUI.constructor()
- 位置: L28-31
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#browser`, `this.#window`

## SidebarPermissionsUI.setContentBrowser()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contentBrowser`

## SidebarPermissionsUI.build()
- 位置: L45-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `el.classList.add()`, `el.setAttribute()`, `this.#createChild()`, `this.#ensureMicIcon()`, `this.#ensureSharingIcon()`, `this.#handlePanelClick.bind()`, `this.#identityBox.addEventListener()`
- 条件付き依存: `if (this.#onPanelClick)` → `this.#identityBox.removeEventListener()`
- 参照: `this.#blockedContainer`, `this.#browser.contentDocument`, `this.#identityBox`, `this.#notificationBox`, `this.#onPanelClick`, `this.#sharingContainer`

## SidebarPermissionsUI.isReady()
- 位置: L92-94
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#identityBox`

## SidebarPermissionsUI.isIdentityBoxOpen()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#identityBox?.getAttribute()`

## SidebarPermissionsUI.showMicRequestUI()
- 位置: L103-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#notificationBox.classList.add()`

## SidebarPermissionsUI.showGrantedUI()
- 位置: L112-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureSharingIcon()`, `this.#identityBox.classList.add()`, `this.#notificationBox.classList.remove()`, `this.#sharingIcon.setAttribute()`

## SidebarPermissionsUI.showBlockedUI()
- 位置: L126-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.appendChild()`, `container.replaceChildren()`, `icon.setAttribute()`, `this.#createBlockedIcon()`, `this.#identityBox.classList.add()`, `this.#notificationBox.classList.remove()`
- 条件付き依存: `if (!showIcon)` → `this.#identityBox.classList.remove()`
- 参照: `container.hidden`, `this.#blockedContainer`

## SidebarPermissionsUI.updateFromBrowserState()
- 位置: L150-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SitePermissions.getAllForBrowser()`, `sidebarAllPerms.some()`, `this.#identityBox.classList.add()`, `this.#notificationBox.classList.remove()`
- 条件付き依存: `if (!webRTC)` → `this.#sharingIcon.removeAttribute()`
- 条件付き依存: `if (!webRTC)` → `this.#identityBox.classList.remove()`
- 条件付き依存: `if (sidebarHasAllow)` → `this.#sharingIcon.setAttribute()`
- 条件付き依存: `if (webRTC?.sharing)` → `this.#sharingIcon.setAttribute()`
- 条件付き依存: `if (webRTC?.sharing)` → `this.#sharingIcon.removeAttribute()`
- 参照: `lazy.SitePermissions.ALLOW`, `p.state`, `this.#contentBrowser`, `webRTC.sharing`, `webRTC?.camera`, `webRTC?.microphone`, `webRTC?.sharing`

## SidebarPermissionsUI.clearUI()
- 位置: L191-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#blockedContainer?.replaceChildren()`, `this.#identityBox?.classList.remove()`, `this.#notificationBox?.classList.remove()`, `this.#sharingIcon?.removeAttribute()`
- 参照: `this.#blockedIcon`

## SidebarPermissionsUI.destroy()
- 位置: L209-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#identityBox?.removeEventListener()`
- 参照: `this.#blockedContainer`, `this.#blockedIcon`, `this.#blockedOpenPanel`, `this.#browser`, `this.#contentBrowser`, `this.#identityBox`, `this.#notificationBox`, `this.#onPanelClick`, `this.#sharingContainer`, `this.#sharingIcon`, `this.#sharingOpenPanel`, `this.#window`

## SidebarPermissionsUI.#handlePanelClick()
- 位置: L229-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#blockedIcon?.hasAttribute()`, `this.#sharingIcon?.hasAttribute()`
- 条件付き依存: `if (this.#sharingIcon?.hasAttribute("showing"))` → `this.#sharingOpenPanel()`
- 条件付き依存: `if (this.#blockedIcon?.hasAttribute("showing"))` → `this.#blockedOpenPanel()`

## SidebarPermissionsUI.#ensureMicIcon()
- 位置: L239-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`
- 条件付き依存: `if (!icon)` → `doc.createXULElement()`
- 条件付き依存: `if (!icon)` → `icon.classList.add()`
- 条件付き依存: `if (!icon)` → `icon.setAttribute()`
- 条件付き依存: `if (!icon)` → `this.#notificationBox.appendChild()`
- 参照: `icon.id`, `this.#browser.contentDocument`

## SidebarPermissionsUI.#ensureSharingIcon()
- 位置: L259-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`
- 条件付き依存: `if (!icon)` → `doc.createXULElement()`
- 条件付き依存: `if (!icon)` → `icon.classList.add()`
- 条件付き依存: `if (!icon)` → `this.#sharingContainer.appendChild()`
- 参照: `icon.id`, `this.#browser.contentDocument`, `this.#sharingIcon`, `this.#sharingOpenPanel`

## this.#sharingOpenPanel()
- 位置: L269-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openPermissionPanel()`
- 参照: `this.#contentBrowser`, `this.#identityBox`

## resetCallback()
- 位置: L274-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `icon.removeAttribute()`, `this.#identityBox.classList.remove()`

## SidebarPermissionsUI.#createBlockedIcon()
- 位置: L288-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `icon.classList.add()`, `icon.setAttribute()`
- 参照: `this.#blockedIcon`, `this.#blockedOpenPanel`, `this.#browser.contentDocument`

## this.#blockedOpenPanel()
- 位置: L294-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openPermissionPanel()`
- 参照: `this.#blockedContainer`, `this.#contentBrowser`

## resetCallback()
- 位置: L299-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `icon.removeAttribute()`, `this.#identityBox.classList.remove()`

## SidebarPermissionsUI.#openPermissionPanel()
- 位置: L319-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `gPanel._permissionPopup.addEventListener()`, `gPanel.clearBrowserOverride()`, `gPanel.openPopup()`, `gPanel.setAnchor()`, `gPanel.setBrowserOverride()`
- 条件付き依存: `if (!gPanel._permissionReloadHint.hidden)` → `resetCallback()`
- 参照: `gPanel._permissionReloadHint.hidden`, `gPanel._popupAnchorNode`, `this.#window`, `win.gPermissionPanel`

## SidebarPermissionsUI.#createChild()
- 位置: L352-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `doc.getElementById()`, `parentEle.appendChild()`
- 条件付き依存: `if (setupFn)` → `setupFn()`
- 参照: `el.id`
