# browser/components/defaultlaunchonlogin/DefaultLaunchOnLogin.sys.mjs

source: browser/components/defaultlaunchonlogin/DefaultLaunchOnLogin.sys.mjs
source-hash: ac2c1e9adb3a4b9569013f1ca01cfb9a2d476094
lines: 123

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## maybeEnableOnFirstRun()
- 位置: async L45-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.get()`, `Services.prefs.getBoolPref()`, `this.enableOnFirstRunIfNeeded()`
- 参照: `lazy.AppConstants.DEBUG`, `lazy.AppConstants.MOZILLA_OFFICIAL`, `lazy.profileService.isFirstRun`
- XPCOM: `Services.env` / `Services.prefs`

## enableOnFirstRunIfNeeded()
- 位置: async L83-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`, `lazy.LaunchOnLogin.enable()`, `lazy.LaunchOnLogin.isAllowed()`, `lazy.LaunchOnLogin.isSupported()`, `this.waitForNimbusReady()`
- XPCOM: `Services.prefs`

## waitForNimbusReady()
- 位置: async L118-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExperimentAPI._rsLoader.finishedUpdating()`, `lazy.ExperimentAPI.init()`
