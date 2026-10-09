# browser/components/preferences/widgets/update-information/update-information.mjs

source: browser/components/preferences/widgets/update-information/update-information.mjs
source-hash: 0057bb42a574972fd264156affffd1851f1bf1fe
lines: 87

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## UpdateInformation.constructor()
- 位置: L16-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.distribution`, `this.distributionId`, `this.releaseNotesURL`, `this.version`

## UpdateInformation.labelTemplate()
- 位置: L32-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.releaseNotesURL`, `this.version`

## UpdateInformation.descriptionTemplate()
- 位置: L56-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.distribution`, `this.distributionId`

## UpdateInformation.render()
- 位置: L68-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.descriptionTemplate()`, `this.labelTemplate()`
