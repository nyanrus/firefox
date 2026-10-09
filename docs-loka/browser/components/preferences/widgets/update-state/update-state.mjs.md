# browser/components/preferences/widgets/update-state/update-state.mjs

source: browser/components/preferences/widgets/update-state/update-state.mjs
source-hash: 8206f07366022721fa031ba64c18cef57eb4a3bd
lines: 317

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## UpdateState.constructor()
- 位置: L116-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.linkURL`, `this.transfer`, `this.updateVersion`, `this.value`

## UpdateState.update()
- 位置: L129-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `super.update()`
- 条件付き依存: `if (changedProperties.has("transfer") && this.value === "downloading")` → `this.dispatchEvent()`
- 参照: `this.value`

## UpdateState.manualURL()
- 位置: L137-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- 参照: `window.IS_STORYBOOK`
- XPCOM: `Services.urlFormatter`

## UpdateState.handleButtonClick()
- 位置: L147-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gAppUpdater.buttonRestartAfterDownload()`, `window.gAppUpdater.checkForUpdates()`, `window.gAppUpdater.startDownload()`
- 参照: `this.value`, `window.gAppUpdater`

## UpdateState.labelWithLinkTemplate()
- 位置: L166-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 条件付き依存: `if (this.value === "unsupportedSystem")` → `html()`
- 条件付き依存: `if (this.value === "downloadFailed")` → `html()`
- 参照: `this.linkURL`, `this.manualURL.href`, `this.manualURL.origin`, `this.manualURL.pathname`, `this.value`

## UpdateState.buttonTemplate()
- 位置: L217-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 条件付き依存: `if (this.value === "downloadAndInstall")` → `Services.strings.createBundle()`
- 条件付き依存: `if (this.value === "downloadAndInstall")` → `bundle.formatStringFromName()`
- 条件付き依存: `if (this.value === "downloadAndInstall")` → `bundle.GetStringFromName()`
- 条件付き依存: `if (this.value === "downloadAndInstall")` → `html()`
- 条件付き依存: `if (!l10nId)` → `html()`
- 条件付き依存: `if (!l10nId)` → `ifDefined()`
- 参照: `this.handleButtonClick`, `this.updateVersion`, `this.value`
- XPCOM: `Services.strings`

## UpdateState.render()
- 位置: L267-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `ifDefined()`, `this.buttonTemplate()`
- 条件付き依存: `if (!l10nId)` → `this.buttonTemplate()`
- 条件付き依存: `if ( this.value === "manualUpdate" || this.value === "internalError" || this.value === "unsupportedSystem" || this.value === "downloadFailed" )` → `html()`
- 条件付き依存: `if ( this.value === "manualUpdate" || this.value === "internalError" || this.value === "unsupportedSystem" || this.value === "downloadFailed" )` → `this.labelWithLinkTemplate()`
- 条件付き依存: `if ( this.value === "manualUpdate" || this.value === "internalError" || this.value === "unsupportedSystem" || this.value === "downloadFailed" )` → `this.buttonTemplate()`
- 参照: `dataL10nArgs.transfer`, `this.transfer`, `this.value`
