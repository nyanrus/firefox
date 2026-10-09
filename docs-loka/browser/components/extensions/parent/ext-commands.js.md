# browser/components/extensions/parent/ext-commands.js

source: browser/components/extensions/parent/ext-commands.js
source-hash: 4b98268ed1146cd77382c4dc099e98fe09278067
lines: 88

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## onCommand()
- 位置: L13-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.on()`

## listener()
- 位置: L17-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `tabManager.addActiveTabPermission()`, `tabManager.convert()`
- 参照: `tabTracker.activeTab`

## unregister()
- 位置: L24-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.off()`

## convert()
- 位置: L25-27
- 役割: (未記入)
- 触るとき: (未記入)

## onChanged()
- 位置: L30-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.on()`

## listener()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`

## unregister()
- 位置: L36-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.off()`

## convert()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)

## onUninstall()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionShortcuts.removeCommandsFromStorage()`

## onManifestEntry()
- 位置: async L48-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `shortcuts.loadCommands()`, `shortcuts.register()`
- 参照: `this.extension`, `this.extension.shortcuts`

## onCommand()
- 位置: L51-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`

## onShortcutChanged()
- 位置: L52-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`

## onShutdown()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.shortcuts.unregister()`

## getAPI()
- 位置: L63-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module: "commands", event: "onChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "commands", event: "onCommand", inputHandling: true, extensionApi: this, }).api()`

## getAll()
- 位置: L66-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.shortcuts.allCommands()`

## update()
- 位置: L67-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.shortcuts.updateCommand()`

## reset()
- 位置: L68-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.shortcuts.resetCommand()`

## openShortcutSettings()
- 位置: L69-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.shortcuts.openShortcutSettings()`
