# browser/components/aboutlogins/content/aboutLoginsImportReport.mjs

source: browser/components/aboutlogins/content/aboutLoginsImportReport.mjs
source-hash: 7d71a3490c68419cda044367ff73ec12b03a8a2b
lines: 85

## <module>
- 役割: (未記入)
- 呼び出し先: `document.dispatchEvent()`, `document.querySelector()`, `window.addEventListener()`

## importReportDataHandler()
- 位置: L17-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `detailsLoginsList.appendChild()`, `document.createDocumentFragment()`, `document.dispatchEvent()`, `document.l10n.setAttributes()`, `fragment.appendChild()`, `loginRow.result.includes()`, `window.removeEventListener()`
- 条件付き依存: `if (report.no_change > 0)` → `detailedDuplicateCount .querySelector(".not-imported") .classList.toggle()`
- 条件付き依存: `if (report.no_change > 0)` → `detailedDuplicateCount .querySelector()`
- 条件付き依存: `if (report.error > 0)` → `detailedErrorsCount .querySelector(".not-imported") .classList.toggle()`
- 条件付き依存: `if (report.error > 0)` → `detailedErrorsCount .querySelector()`
- 参照: `detailsLoginsList.innerHTML`, `event.detail.messageType`, `event.detail.value`, `loginRow.result`, `logins.length`, `report.added`, `report.error`, `report.modified`, `report.no_change`
