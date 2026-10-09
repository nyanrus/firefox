# browser/modules/BrowserUIUtils.sys.mjs

source: browser/modules/BrowserUIUtils.sys.mjs
source-hash: 09a3b842426b6433ba4b8c008c7ec396240db6e1
lines: 197

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## checkEmptyPageOrigin()
- 位置: L30-64
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (contentPrincipal.isContentPrincipal)` → `contentPrincipal.equalsURI()`
- 参照: `browser.contentPrincipal`, `browser.currentURI`, `browser.documentURI`, `browser.hasContentOpener`, `contentPrincipal.isContentPrincipal`, `contentPrincipal.isNullPrincipal`, `contentPrincipal.isSystemPrincipal`, `contentPrincipal.spec`, `uriToCheck.spec`

## getLocalizedFragment()
- 位置: L87-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createDocumentFragment()`, `msg.includes()`, `msg.match()`, `part.includes()`, `parts.findIndex()`
- 条件付き依存: `if (!msg.includes("%" + i + "$S"))` → `msg.replace()`
- 条件付き依存: `if (numberOfInsertionPoints != nodesOrStrings.length)` → `console.error()`
- 条件付き依存: `if (partIndex == -1)` → `fragment.appendChild()`
- 条件付き依存: `if (partIndex == -1)` → `doc.createTextNode()`
- 条件付き依存: `if (typeof replacement == "string")` → `parts[partIndex].replace()`
- 条件付き依存: `if (!(typeof replacement == "string"))` → `parts[partIndex].split()`
- 条件付き依存: `if (!(typeof replacement == "string"))` → `parts.splice()`
- 条件付き依存: `if (part)` → `fragment.appendChild()`
- 条件付き依存: `if (part)` → `doc.createTextNode()`
- 条件付き依存: `if (!(typeof part == "string"))` → `fragment.appendChild()`
- 参照: `msg.match(/%\d+\$S/g).length`, `nodesOrStrings.length`

## removeSingleTrailingSlashFromURL()
- 位置: L139-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aURL.replace()`

## trimURLProtocol()
- 位置: L144-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.getScotchBonnetPref()`

## getTrimmedURLPrefix()
- 位置: L159-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aURL.startsWith()`
- 条件付き依存: `if (aURL.startsWith(this.trimURLProtocol))` → `aURL.substring()`
- 条件付き依存: `if (aURL.startsWith(this.trimURLProtocol))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (aURL.startsWith(this.trimURLProtocol))` → `aURL.startsWith()`
- 参照: `prefix.length`, `this.trimURLProtocol`

## trimURL()
- 位置: L184-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTrimmedURLPrefix()`, `this.removeSingleTrailingSlashFromURL()`, `url.substring()`
- 参照: `prefix.length`
