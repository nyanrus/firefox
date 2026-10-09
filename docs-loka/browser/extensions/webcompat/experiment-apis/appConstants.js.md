# browser/extensions/webcompat/experiment-apis/appConstants.js

source: browser/extensions/webcompat/experiment-apis/appConstants.js
source-hash: 578430caac12516d4ff7ac35db9858c736597931
lines: 70

## <module>
- 役割: (未記入)

## getAPI()
- 位置: L30-68
- 役割: (未記入)
- 触るとき: (未記入)

## getAndroidPackageName()
- 位置: L33-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.get()`
- XPCOM: `Services.env`

## getAppVersion()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo.version`
- XPCOM: `Services.appinfo`

## getEffectiveUpdateChannel()
- 位置: L39-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ver.includes()`
- 条件付き依存: `if (!(ver.includes("a")))` → `ver.includes()`
- 条件付き依存: `if (!(ver.includes("b")))` → `ver.includes()`
- 参照: `AppConstants.MOZ_APP_VERSION_DISPLAY`

## getPlatform()
- 位置: L50-58
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## isInAutomation()
- 位置: L59-65
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Cu.isInAutomation`, `lazy.Marionette.running`, `lazy.RemoteAgent.running`
