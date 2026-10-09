# browser/components/aboutlogins/content/aboutLoginsImportReport.mjs

source: browser/components/aboutlogins/content/aboutLoginsImportReport.mjs
source-hash: 7d71a3490c68419cda044367ff73ec12b03a8a2b
lines: 85

## <module>
- 役割: インポート報告ページの初期化を行い、親からの ImportReportData を受けて件数と行一覧を描画する。
- 呼び出し先: `document.dispatchEvent()`, `document.querySelector()`, `window.addEventListener()`

## importReportDataHandler()
- 位置: L17-82
- 役割: ImportReportData を受けて result ごとに件数を数え(error を含むものはエラー扱い)、4つの件数欄を l10n で設定する。0 件でなければ注記を表示し、行一覧を作り直してから受信リスナーを外し、ready イベントを発行する。
- 触るとき: インポート結果の件数の数え方や行一覧の更新を変えるとき。件数欄の名前(exiting は変更分)と対応を確認する必要がある。
- 呼び出し先: `detailsLoginsList.appendChild()`, `document.createDocumentFragment()`, `document.dispatchEvent()`, `document.l10n.setAttributes()`, `fragment.appendChild()`, `loginRow.result.includes()`, `window.removeEventListener()`
- 条件付き依存: `if (report.no_change > 0)` → `detailedDuplicateCount .querySelector(".not-imported") .classList.toggle()`
- 条件付き依存: `if (report.no_change > 0)` → `detailedDuplicateCount .querySelector()`
- 条件付き依存: `if (report.error > 0)` → `detailedErrorsCount .querySelector(".not-imported") .classList.toggle()`
- 条件付き依存: `if (report.error > 0)` → `detailedErrorsCount .querySelector()`
- 参照: `detailsLoginsList.innerHTML`, `event.detail.messageType`, `event.detail.value`, `loginRow.result`, `logins.length`, `report.added`, `report.error`, `report.modified`, `report.no_change`
