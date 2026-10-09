# browser/extensions/newtab/lib/NewTabActorRegistry.sys.mjs

source: browser/extensions/newtab/lib/NewTabActorRegistry.sys.mjs
source-hash: 0492f65208d82b0a23c6c4502c0f8fafa8d503e7
lines: 81

## <module>
- 役割: (未記入)

## onAddActor()
- 位置: L30-33
- 役割: (未記入)
- 触るとき: (未記入)

## init()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ActorManagerParent.addJSWindowActors()`

## uninit()
- 位置: L51-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.unregisterWindowActor()`, `Object.entries()`, `console.error()`

## registerAttributionActor()
- 位置: L65-69
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (attributionActorRegister)` → `attributionActorRegister()`

## unregisterAttributionActor()
- 位置: L75-79
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (attributionActorUnregister)` → `attributionActorUnregister()`
