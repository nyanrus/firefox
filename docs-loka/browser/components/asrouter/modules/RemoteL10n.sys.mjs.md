# browser/components/asrouter/modules/RemoteL10n.sys.mjs

source: browser/components/asrouter/modules/RemoteL10n.sys.mjs
source-hash: 822b3aec1593eddddca186976fb525756616c1c8
lines: 270

## <module>
- 役割: (未記入)

## _RemoteL10n.constructor()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._l10n`

## _RemoteL10n.createElement()
- 位置: L139-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setString()`
- 条件付き依存: `if (options.content && options.content.string_id)` → `doc.createElement()`
- 条件付き依存: `if (!(options.content && options.content.string_id))` → `doc.createElementNS()`
- 条件付き依存: `if (options.classList)` → `node.classList.add()`
- 参照: `options.classList`, `options.content`, `options.content.string_id`

## _RemoteL10n.setString()
- 位置: L157-166
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (content && content.string_id)` → `Object.entries()`
- 条件付き依存: `if (content && content.string_id)` → `el.setAttribute()`
- 参照: `content.string_id`, `el.textContent`

## _RemoteL10n.cfrFluentFileDir()
- 位置: L168-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("ProfLD", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `Services.dirsvc`

## _RemoteL10n.cfrFluentFilePath()
- 位置: L177-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`
- 参照: `this.cfrFluentFileDir`

## _RemoteL10n._createDOML10n()
- 位置: L193-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `L10nRegistry.getInstance()`, `L10nRegistry.getInstance().hasSource()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (useRemoteL10n && !L10nRegistry.getInstance().hasSource("cfr"))` → `PathUtils.toFileURI()`
- 条件付き依存: `if (useRemoteL10n && !L10nRegistry.getInstance().hasSource("cfr"))` → `L10nRegistry.getInstance().registerSources()`
- 条件付き依存: `if (useRemoteL10n && !L10nRegistry.getInstance().hasSource("cfr"))` → `L10nRegistry.getInstance()`
- 条件付き依存: `if (!(useRemoteL10n && !L10nRegistry.getInstance().hasSource("cfr")))` → `L10nRegistry.getInstance().hasSource()`
- 条件付き依存: `if (!(useRemoteL10n && !L10nRegistry.getInstance().hasSource("cfr")))` → `L10nRegistry.getInstance()`
- 条件付き依存: `if (!useRemoteL10n && L10nRegistry.getInstance().hasSource("cfr"))` → `L10nRegistry.getInstance().removeSources()`
- 条件付き依存: `if (!useRemoteL10n && L10nRegistry.getInstance().hasSource("cfr"))` → `L10nRegistry.getInstance()`
- 参照: `Services.locale.appLocaleAsBCP47`, `this.cfrFluentFileDir`, `this.cfrFluentFilePath`
- XPCOM: `Services.locale` / `Services.prefs`

## _RemoteL10n.l10n()
- 位置: L230-235
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._l10n)` → `this._createDOML10n()`
- 参照: `this._l10n`

## _RemoteL10n.reloadL10n()
- 位置: L237-239
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._l10n`

## _RemoteL10n.isLocaleSupported()
- 位置: L241-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALL_LOCALES.has()`

## _RemoteL10n.formatLocalizableText()
- 位置: async L255-266
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof localizableText !== "string")` → `this.l10n.formatValue()`
- 参照: `localizableText.string_id`
