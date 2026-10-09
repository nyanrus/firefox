# browser/components/extensions/parent/ext-omnibox.js

source: browser/components/extensions/parent/ext-omnibox.js
source-hash: 95bed5cb0078d8aa1d7023666e7c342b24bdcc8c
lines: 178

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## onInputStarted()
- 位置: L14-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_STARTED`

## listener()
- 位置: L16-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L21-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_STARTED`

## convert()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)

## onInputCancelled()
- 位置: L29-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_CANCELLED`

## listener()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_CANCELLED`

## convert()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)

## onInputEntered()
- 位置: L44-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_ENTERED`

## listener()
- 位置: L46-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.tabManager.addActiveTabPermission()`, `fire.sync()`

## unregister()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_ENTERED`

## convert()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)

## onInputChanged()
- 位置: L60-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_CHANGED`

## listener()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L67-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_CHANGED`

## convert()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)

## onDeleteSuggestion()
- 位置: L75-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_DELETED`

## listener()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`

## unregister()
- 位置: L82-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.off()`
- 参照: `ExtensionSearchHandler.MSG_INPUT_DELETED`

## convert()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)

## onManifestEntry()
- 位置: L92-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSearchHandler.registerKeyword()`, `extension.manifestError()`
- 参照: `e.message`, `manifest.omnibox.keyword`, `this.keyword`

## onShutdown()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSearchHandler.unregisterKeyword()`
- 参照: `this.keyword`

## getAPI()
- 位置: L110-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module: "omnibox", event: "onDeleteSuggestion", extensionApi: this, }).api()`, `new EventManager({ context, module: "omnibox", event: "onInputCancelled", extensionApi: this, }).api()`, `new EventManager({ context, module: "omnibox", event: "onInputChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "omnibox", event: "onInputEntered", extensionApi: this, inputHandling: true, }).api()`, `new EventManager({ context, module: "omnibox", event: "onInputStarted", extensionApi: this, }).api()`

## setDefaultSuggestion()
- 位置: L113-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSearchHandler.setDefaultSuggestion()`, `Promise.reject()`
- 参照: `e.message`, `this.keyword`

## addSuggestions()
- 位置: L162-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSearchHandler.addSuggestions()`
- 参照: `this.keyword`
