# browser/components/profiles/content/profile-selector.mjs

source: browser/components/profiles/content/profile-selector.mjs
source-hash: e1378f304c276e1c0162fc565a4518c306480be1
lines: 202

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## ProfileSelector.constructor()
- 位置: L35-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.init()`
- 参照: `Ci.nsIDialogParamBlock`, `this.#initPromise`, `this.#startupParams`, `window.arguments`
- XPCOM: [`nsIDialogParamBlock`](../../../../toolkit/components/windowwatcher/nsIDialogParamBlock.idl.md)

## ProfileSelector.isStartupUI()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#startupParams`

## ProfileSelector.setLaunchArguments()
- 位置: async L54-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#startupParams.SetInt()`, `this.#startupParams.SetNumberStrings()`, `this.#startupParams.SetString()`, `this.#startupParams.objects.insertElementAt()`
- 参照: `Ci.nsIToolkitProfileService.launchWithProfile`, `args.length`, `profile.localDir`, `profile.rootDir`, `this.#startupParams`
- XPCOM: [`nsIToolkitProfileService`](../../../../toolkit/profile/nsIToolkitProfileService.idl.md)

## ProfileSelector.getUpdateComplete()
- 位置: async L77-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.getUpdateComplete()`
- 参照: `this.#initPromise`

## ProfileSelector.init()
- 位置: async L83-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `this.selectableProfileService.getAllProfiles()`, `this.selectableProfileService.init()`, `this.selectableProfileService.maybeSetupDataStore()`
- 条件付き依存: `if (!this.profiles.length)` → `this.selectableProfileService.setShowProfileSelectorWindow()`
- 条件付き依存: `if (this.isStartupUI)` → `window.addEventListener()`
- 条件付き依存: `if (this.isStartupUI)` → `this.selectableProfileService.uninit()`
- 参照: `this.#initPromise`, `this.initialized`, `this.isStartupUI`, `this.profiles`, `this.profiles.length`, `this.selectableProfileService`, `this.selectableProfileService.groupToolkitProfile.showProfileSelector`, `this.showSelector`

## ProfileSelector.handleCheckboxToggle()
- 位置: L115-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.profilesSelectorWindow.showAtStartup.record()`, `this.selectableProfileService.setShowProfileSelectorWindow()`
- 参照: `this.checkbox.checked`, `this.showSelector`

## ProfileSelector.launchProfile()
- 位置: async L124-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.close()`
- 条件付き依存: `if (this.isStartupUI)` → `this.setLaunchArguments()`
- 条件付き依存: `if (this.isStartupUI)` → `this.selectableProfileService.uninit()`
- 条件付き依存: `if (!(this.isStartupUI))` → `this.selectableProfileService.launchInstance()`
- 参照: `this.isStartupUI`

## ProfileSelector.handleEvent()
- 位置: async L135-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.profilesSelectorWindow.launch.record()`, `this.launchProfile()`, `this.selectableProfileService.createNewProfile()`
- 参照: `event.detail`, `event.type`, `this.isStartupUI`

## ProfileSelector.render()
- 位置: L160-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.profiles.map()`
- 参照: `this.handleCheckboxToggle`, `this.profiles`, `this.showSelector`
