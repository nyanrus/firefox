# browser/components/preferences/config/browser-icon.mjs

source: browser/components/preferences/config/browser-icon.mjs
source-hash: 087555d7ed7c07159723fe46773ce573d30db023
lines: 363

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Preferences.addAll()`, `Preferences.addSetting()`, `SettingGroupManager.registerGroups()`, `XPCOMUtils.defineLazyServiceGetters()`, `document.addEventListener()`, `getOptions()`, `matchMedia()`

## currentScheme()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `COLOR_SCHEME_QUERY.matches`

## watchScheme()
- 位置: L30-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `COLOR_SCHEME_QUERY.addEventListener()`, `COLOR_SCHEME_QUERY.removeEventListener()`

## refreshUnlockState()
- 位置: async L60-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window .getShellService()`, `window .getShellService() .shellService.isCurrentAppPinnedToTaskbar()`
- 条件付き依存: `if ( isDefault !== gIsDefault || isPinned !== gIsPinned || unlocked !== gIconsUnlocked )` → `notify()`
- 参照: `DefaultBrowserHelper.isBrowserDefault`, `lazy.WinTaskbar.defaultGroupId`

## watchUnlockState()
- 位置: L104-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gUnlockListeners.add()`, `gUnlockListeners.delete()`, `refreshUnlockState()`
- 条件付き依存: `if (!gUnlockListeners.size && DefaultBrowserHelper.canCheck)` → `DefaultBrowserHelper.pollForDefaultChanges()`
- 条件付き依存: `if (!gUnlockListeners.size && gPollUnsubscribe)` → `gPollUnsubscribe()`
- 参照: `DefaultBrowserHelper.canCheck`, `gUnlockListeners.size`

## iconOption()
- 位置: L140-150
- 役割: (未記入)
- 触るとき: (未記入)

## getOptions()
- 位置: L161-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `currentScheme()`
- 条件付き依存: `if (!!entry.gated == isGated)` → `options.push()`
- 条件付き依存: `if (!!entry.gated == isGated)` → `iconOption()`
- 条件付き依存: `if (!!entry.gated == isGated)` → `lazy.resolvePreview()`
- 参照: `entry.gated`, `entry.l10nId`, `lazy.ICON_CATALOG`

## resolveOptionPreviews()
- 位置: L177-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentScheme()`
- 条件付き依存: `if (entry)` → `lazy.resolvePreview()`
- 参照: `config.options`, `lazy.ICON_CATALOG`, `option.controlAttrs`, `option.value`

## isBonusId()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ICON_CATALOG`, `lazy.ICON_CATALOG[id]?.gated`

## isBasicId()
- 位置: L196-199
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `entry.gated`, `lazy.ICON_CATALOG`

## selectIcon()
- 位置: async L208-214
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (val === "default")` → `lazy.CustomIconManager.revert()`
- 条件付き依存: `if (!(val === "default"))` → `lazy.CustomIconManager.apply()`

## get()
- 位置: L229-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isBasicId()`
- 参照: `customIconIdPref.value`

## get()
- 位置: L243-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isBonusId()`
- 参照: `customIconIdPref.value`

## setup()
- 位置: L248-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `stopScheme()`, `stopUnlock()`, `watchScheme()`, `watchUnlockState()`

## getControlConfig()
- 位置: L256-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolveOptionPreviews()`
- 参照: `config.options`, `option.disabled`

## visible()
- 位置: L269-269
- 役割: (未記入)
- 触るとき: (未記入)

## visible()
- 位置: L278-278
- 役割: (未記入)
- 触るとき: (未記入)

## visible()
- 位置: L287-287
- 役割: (未記入)
- 触るとき: (未記入)

## onUserClick()
- 位置: async L288-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DefaultBrowserHelper.setDefaultBrowser()`, `refreshUnlockState()`

## visible()
- 位置: L296-296
- 役割: (未記入)
- 触るとき: (未記入)

## onUserClick()
- 位置: async L297-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `refreshUnlockState()`, `window.getShellService()`, `window.getShellService().pinToTaskbar()`
