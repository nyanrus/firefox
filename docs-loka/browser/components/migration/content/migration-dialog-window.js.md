# browser/components/migration/content/migration-dialog-window.js

source: browser/components/migration/content/migration-dialog-window.js
source-hash: eefb290dc99ef1289d79a89c474f847cb93fb665
lines: 118

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `MigrationDialog.init()`

## init()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addEventListener()`

## onLoad()
- 位置: L39-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `customElements.whenDefined()`, `customElements.whenDefined("migration-wizard").then()`, `document.addEventListener()`, `document.getElementById()`, `observer.observe()`, `this._wiz.addEventListener()`, `window.sizeToContent()`
- 条件付き依存: `if (args.options?.skipSourceSelection)` → `this.doProfileRefresh()`
- 条件付き依存: `if (!(args.options?.skipSourceSelection))` → `this._wiz.requestState()`
- 参照: `Ci.nsISupports`, `args.options.migrator`, `args.options.migratorKey`, `args.options.profileId`, `args.options?.skipSourceSelection`, `args.wrappedJSObject`, `this._wiz`, `window.arguments`
- XPCOM: [`nsISupports`](../../../../netwerk/base/nsIEncodedChannel.idl.md)

## handleEvent()
- 位置: L73-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onLoad()`, `window.close()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE)` → `window.close()`
- 参照: `KeyEvent.DOM_VK_ESCAPE`, `event.keyCode`, `event.type`

## doProfileRefresh()
- 位置: async L92-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `migrator.getMigrateData()`, `setTimeout()`, `this._wiz.addEventListener()`, `this._wiz.doAutoImport()`, `window.close()`
- 条件付き依存: `if (resourceTypeData & lazy.MigrationUtils.resourceTypes[type])` → `resourceTypeStrs.push()`
- 参照: `lazy.MigrationUtils.resourceTypes`, `lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES`
