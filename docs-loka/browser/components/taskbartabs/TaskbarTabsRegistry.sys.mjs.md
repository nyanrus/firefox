# browser/components/taskbartabs/TaskbarTabsRegistry.sys.mjs

source: browser/components/taskbartabs/TaskbarTabsRegistry.sys.mjs
source-hash: 72ad9b6cde0727a81da2e3712045a24aa7be3c73
lines: 569

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Promise.resolve()`, `console.createInstance()`

## getJsonSchema()
- 位置: async L26-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`, `res.json()`
- 参照: `lazy.JsonSchema.Validator`

## TaskbarTab.constructor()
- 位置: L59-74
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#id`, `this.#name`, `this.#scopes`, `this.#shortcutRelativePath`, `this.#startUrl`, `this.#userContextId`

## TaskbarTab.id()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#id`

## TaskbarTab.scopes()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scopes`

## TaskbarTab.userContextId()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#userContextId`

## TaskbarTab.startUrl()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#startUrl`

## TaskbarTab.name()
- 位置: L92-94
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#name`

## TaskbarTab.shortcutRelativePath()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#shortcutRelativePath`

## TaskbarTab.isScopeNavigable()
- 位置: L107-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomain()`, `Services.eTLD.getBaseDomainFromHost()`, `lazy.logConsole.info()`
- 条件付き依存: `if (baseDomain === scopeBaseDomain)` → `lazy.logConsole.info()`
- 参照: `scope.hostname`, `this.#id`, `this.#scopes`
- XPCOM: `Services.eTLD`

## TaskbarTab.toJSON()
- 位置: L126-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `maybe()`
- 参照: `this.id`, `this.name`, `this.scopes`, `this.startUrl`, `this.userContextId`

## maybe()
- 位置: L127-127
- 役割: (未記入)
- 触るとき: (未記入)

## TaskbarTab._applyPatch()
- 位置: L147-151
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aPatch.shortcutRelativePath`, `this.#shortcutRelativePath`

## TaskbarTabsRegistry.constructor()
- 位置: L180-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTaskbarTabs.map()`, `migrateStoredTaskbarTab()`
- 参照: `this.#storage`, `this.#taskbarTabs`

## TaskbarTabsRegistry.toJSON()
- 位置: L187-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#taskbarTabs.map()`, `tt.toJSON()`

## TaskbarTabsRegistry.findOrCreateTaskbarTab()
- 位置: L208-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webApp.install.record()`, `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `Services.uuid.generateUUID().toString().slice()`, `generateName()`, `lazy.logConsole.info()`, `this.#storage.save()`, `this.#taskbarTabs.push()`, `this.findTaskbarTab()`
- 条件付き依存: `if ("scope" in manifest)` → `Services.io.newURI()`
- 条件付き依存: `if (!(manifest.start_url))` → `aUrl.schemeIs()`
- 条件付き依存: `if (aUrl.schemeIs("moz-extension"))` → `aUrl.mutate().setQuery("").setRef("").finalize()`
- 条件付き依存: `if (aUrl.schemeIs("moz-extension"))` → `aUrl.mutate().setQuery("").setRef()`
- 条件付き依存: `if (aUrl.schemeIs("moz-extension"))` → `aUrl.mutate().setQuery()`
- 条件付き依存: `if (aUrl.schemeIs("moz-extension"))` → `aUrl.mutate()`
- 参照: `aUrl.host`, `aUrl.mutate().setQuery("").setRef("").finalize().spec`, `aUrl.prePath`, `manifest.name`, `manifest.scope`, `manifest.start_url`, `scopeUri.filePath`, `scopeUri.host`
- XPCOM: `Services.io` / `Services.uuid`

## TaskbarTabsRegistry.removeTaskbarTab()
- 位置: L273-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.error()`, `tts.findIndex()`
- 条件付き依存: `if (i > -1)` → `lazy.logConsole.info()`
- 条件付き依存: `if (i > -1)` → `tts.splice()`
- 条件付き依存: `if (i > -1)` → `Glean.webApp.uninstall.record()`
- 条件付き依存: `if (i > -1)` → `this.#storage.save()`
- 参照: `this.#taskbarTabs`, `tt.id`, `tts[i].id`

## TaskbarTabsRegistry.findTaskbarTab()
- 位置: L299-348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.info()`
- 条件付き依存: `if ("prefix" in scope)` → `aUrl.filePath.startsWith()`
- 条件付き依存: `if (aUserContextId !== tt.userContextId)` → `lazy.logConsole.info()`
- 条件付き依存: `if (!(aUserContextId !== tt.userContextId))` → `lazy.logConsole.info()`
- 参照: `Ci.nsIURL`, `aUrl.host`, `aUrl.spec`, `bestPrefix.length`, `scope.hostname`, `scope.prefix`, `scope.prefix.length`, `this.#taskbarTabs`, `tt.scopes`, `tt.userContextId`
- XPCOM: [`nsIURL`](../../../netwerk/base/nsIURL.idl.md)

## TaskbarTabsRegistry.getTaskbarTab()
- 位置: L357-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#taskbarTabs.find()`
- 条件付き依存: `if (!tt)` → `lazy.logConsole.error()`
- 参照: `aTaskbarTab.id`

## TaskbarTabsRegistry.patchTaskbarTab()
- 位置: L379-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTaskbarTab._applyPatch()`, `this.#storage.save()`

## TaskbarTabsRegistry.countTaskbarTabs()
- 位置: L391-393
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#taskbarTabs.length`

## TaskbarTabsRegistry.resetForTests()
- 位置: L398-400
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#taskbarTabs`

## TaskbarTabsRegistryStorage.constructor()
- 位置: L421-423
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#file`

## TaskbarTabsRegistryStorage.load()
- 位置: async L430-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readJSON()`, `IOUtils.readJSON(this.#file.path).catch()`, `Promise.all()`, `getJsonSchema()`, `lazy.logConsole.info()`, `schema.validate()`
- 条件付き依存: `if (err.name !== "NotFoundError")` → `lazy.logConsole.error()`
- 参照: `err.name`, `jsonObject.taskbarTabs`, `jsonObject.version`, `schema.validate(jsonObject).valid`, `this.#file.path`

## TaskbarTabsRegistryStorage.save()
- 位置: L478-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.makeDirectory()`, `IOUtils.writeJSON()`, `aRegistry.toJSON()`, `getJsonSchema()`, `lazy.AsyncShutdown.profileBeforeChange.addBlocker()`, `lazy.logConsole.error()`, `lazy.logConsole.info()`, `schema.validate()`, `this.#saveQueue .finally()`
- 条件付き依存: `if (!result.valid)` → `JSON.stringify()`
- 参照: `result.errors`, `result.valid`, `this.#file.parent.path`, `this.#file.path`, `this.#saveQueue`

## migrateStoredTaskbarTab()
- 位置: L523-533
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof aStored.name !== "string")` → `generateName()`
- 条件付き依存: `if (typeof aStored.name !== "string")` → `Services.io.newURI()`
- 条件付き依存: `if (typeof aStored.name !== "string")` → `lazy.logConsole.warn()`
- 参照: `aStored.id`, `aStored.name`, `aStored.startUrl`
- XPCOM: `Services.io`

## generateName()
- 位置: L541-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD .getKnownPublicSuffix()`, `Services.eTLD .getKnownPublicSuffix(aUri) .split()`, `aUri.host.split()`, `hostParts // ["example", "subdomain"] .reverse()`, `hostParts // ["example", "subdomain"] .reverse() // ["Example", "Subdomain"] .map()`, `hostParts.splice()`, `s.charAt()`, `s.charAt(0).toUpperCase()`, `s.slice()`
- 条件付き依存: `if (hostParts[0] === "www")` → `hostParts.shift()`
- 参照: `Services.eTLD .getKnownPublicSuffix(aUri) .split(".").length`
- XPCOM: `Services.eTLD`
