# browser/components/preferences/extensionControlled.js

source: browser/components/preferences/extensionControlled.js
source-hash: 235a625edf9705aba23aebf2e5e4929f7d915379
lines: 314

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## "websites.trackingProtectionMode"()
- 位置: L52-57
- 役割: (未記入)
- 触るとき: (未記入)

## getControllingExtensionInfo()
- 位置: async L74-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSettingsStore.getSetting()`, `ExtensionSettingsStore.initialize()`

## getControllingExtensionEls()
- 位置: L79-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `section.querySelector()`
- 参照: `idInfo.button`, `idInfo.section`

## getControllingExtension()
- 位置: async L92-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`, `getControllingExtensionInfo()`
- 参照: `info.id`

## handleControllingExtension()
- 位置: async L98-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getControllingExtension()`
- 条件付き依存: `if (addon)` → `showControllingExtension()`
- 条件付き依存: `if (!(addon))` → `getControllingExtensionEls()`
- 条件付き依存: `if ( extensionControlledIds[settingName] && !document.hidden && elements.button )` → `showEnableExtensionMessage()`
- 条件付き依存: `if (!( extensionControlledIds[settingName] && !document.hidden && elements.button ))` → `hideControllingExtension()`
- 参照: `addon.id`, `document.hidden`, `elements.button`

## settingNameToL10nID()
- 位置: L126-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extensionControlledL10nKeys.hasOwnProperty()`

## setControllingExtensionDescription()
- 位置: L153-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `elem.querySelector()`, `settingNameToL10nID()`
- 条件付き依存: `if (existingImg)` → `existingImg.remove()`
- 条件付き依存: `if (addon === null)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!existingImg)` → `document.createElementNS()`
- 条件付き依存: `if (!existingImg)` → `image.setAttribute()`
- 条件付き依存: `if (!existingImg)` → `image.classList.add()`
- 条件付き依存: `if (!existingImg)` → `elem.appendChild()`
- 条件付き依存: `if (!(!existingImg))` → `existingImg.getAttribute()`
- 条件付き依存: `if (existingImg.getAttribute("src") !== src)` → `existingImg.setAttribute()`
- 参照: `addon.iconURL`, `addon.name`

## showControllingExtension()
- 位置: async L187-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elements.section.classList.remove()`, `getControllingExtensionEls()`, `setControllingExtensionDescription()`
- 参照: `AddonManager.PERM_CAN_DISABLE`, `addon.permissions`, `elements.button`, `elements.button.hidden`, `elements.description`, `elements.section.hidden`

## hideControllingExtension()
- 位置: L206-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getControllingExtensionEls()`
- 参照: `elements.button`, `elements.button.hidden`, `elements.section.hidden`

## showEnableExtensionMessage()
- 位置: L214-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dismissButton.addEventListener()`, `dismissButton.setAttribute()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `elements.description.appendChild()`, `elements.description.removeAttribute()`, `elements.section.classList.add()`, `getControllingExtensionEls()`, `icon()`, `label.appendChild()`
- 参照: `elements.button.hidden`, `elements.description.textContent`

## icon()
- 位置: L238-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElementNS()`, `img.setAttribute()`
- 参照: `img.className`, `img.src`

## dismissHandler()
- 位置: L258-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dismissButton.removeEventListener()`, `hideControllingExtension()`

## makeDisableControllingExtension()
- 位置: L265-271
- 役割: (未記入)
- 触るとき: (未記入)

## disableExtension()
- 位置: async L266-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`, `addon.disable()`, `getControllingExtensionInfo()`

## initListenersForPrefChange()
- 位置: async L281-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Management.asyncLoadSettingsModules()`, `Management.off()`, `Management.on()`, `managementObserver()`, `window.addEventListener()`

## managementObserver()
- 位置: async L284-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`, `handleControllingExtension()`
- 参照: `controlledElement.disabled`
- XPCOM: `Services.prefs`

## initializeProxyUI()
- 位置: L298-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `container.updateProxySettingsUI()`, `window.addEventListener()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L303-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `API_PROXY_PREFS.includes()`
- 条件付き依存: `if (API_PROXY_PREFS.includes(data))` → `deferredUpdate.arm()`
