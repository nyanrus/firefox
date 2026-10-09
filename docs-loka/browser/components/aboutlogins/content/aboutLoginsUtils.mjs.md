# browser/components/aboutlogins/content/aboutLoginsUtils.mjs

source: browser/components/aboutlogins/content/aboutLoginsUtils.mjs
source-hash: 2ecea6295031d8edbe66850ecd180df01149fd0b
lines: 79

## <module>
- 役割: (未記入)
- 呼び出し先: `" ".repeat()`

## recordTelemetryEvent()
- 位置: L15-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`

## setKeyboardAccessForNonDialogElements()
- 位置: L24-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `docActiveElement.closest()`, `document.querySelectorAll()`, `pageElements.forEach()`
- 条件付き依存: `if ( !enableKeyboardAccess && docActiveElement && !docActiveElement.closest("confirmation-dialog") )` → `elementToBlur.blur()`
- 条件付き依存: `if (!(el.dataset.oldTabIndex))` → `el.removeAttribute()`
- 参照: `docActiveElement?.shadowRoot?.activeElement`, `el.dataset.oldTabIndex`, `el.tabIndex`

## promptForPrimaryPassword()
- 位置: L55-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AboutLoginsUtils.promptForPrimaryPassword()`

## initDialog()
- 位置: L72-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `element.attachShadow()`, `shadowRoot.appendChild()`, `template.content.cloneNode()`
