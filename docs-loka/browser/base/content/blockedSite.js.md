# browser/base/content/blockedSite.js

source: browser/base/content/blockedSite.js
source-hash: 14f0cf03a65eb4f8f753f56a91d280c733d1cc8d
lines: 221

## <module>
- 役割: (未記入)
- 呼び出し先: `document.getElementById()`, `initPage()`, `seeDetailsButton.addEventListener()`

## getErrorCode()
- 位置: L15-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decodeURIComponent()`, `url.search()`, `url.slice()`
- 参照: `document.documentURI`

## getURL()
- 位置: L22-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decodeURIComponent()`, `url.match()`, `url.startsWith()`
- 条件付き依存: `if (url.startsWith("view-source:"))` → `url.slice()`
- 参照: `document.documentURI`

## getAddonName()
- 位置: L41-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decodeURIComponent()`, `url.match()`
- 参照: `document.documentURI`

## getOverride()
- 位置: L59-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.match()`
- 参照: `document.documentURI`

## getHostString()
- 位置: L69-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getURL()`
- 参照: `document.location.hostname`

## onClickSeeDetails()
- 位置: L77-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `details.hidden`

## initPage()
- 位置: L82-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `document.createElement()`, `document.dispatchEvent()`, `document.getElementById()`, `document.head.appendChild()`, `document.l10n.setAttributes()`, `errorSitename.setAttribute()`, `getAddonName()`, `getErrorCode()`, `getHostString()`, `getOverride()`, `this.getURL()`
- 条件付き依存: `if (!getOverride())` → `document.getElementById("ignore_warning_link").remove()`
- 条件付き依存: `if (!getOverride())` → `document.getElementById()`
- 条件付き依存: `if (error == "unwanted" || error == "harmful" || error == "addon")` → `document.getElementById("report_detection").remove()`
- 条件付き依存: `if (error == "unwanted" || error == "harmful" || error == "addon")` → `document.getElementById()`
- 条件付き依存: `if (Array.isArray(innerDescL10nID))` → `innerDesc.cloneNode()`
- 条件付き依存: `if (Array.isArray(innerDescL10nID))` → `innerDesc.firstChild.remove()`
- 条件付き依存: `if (id === "")` → `innerDesc.appendChild()`
- 条件付き依存: `if (id === "")` → `document.createElement()`
- 条件付き依存: `if (Array.isArray(innerDescL10nID))` → `template.cloneNode()`
- 条件付き依存: `if (Array.isArray(innerDescL10nID))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (Array.isArray(innerDescL10nID))` → `innerDesc.appendChild()`
- 条件付き依存: `if (!(Array.isArray(innerDescL10nID)))` → `document.l10n.setAttributes()`
- 参照: `innerDesc.firstChild`, `messageIDs[error].innerDescNoOverride`, `messageIDs[error].innerDescOverride`, `messageIDs[error].learnMore`, `messageIDs[error].shortDesc`, `messageIDs[error].title`
