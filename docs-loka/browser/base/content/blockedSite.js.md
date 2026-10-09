# browser/base/content/blockedSite.js

source: browser/base/content/blockedSite.js
source-hash: 14f0cf03a65eb4f8f753f56a91d280c733d1cc8d
lines: 221

## <module>
- 役割: 安全性の警告で止められたページ(about:blocked)の表示を組み立てる。エラー種別に応じて、タイトル、説明、リンクの文言を設定する。
- 呼び出し先: `document.getElementById()`, `initPage()`, `seeDetailsButton.addEventListener()`

## getErrorCode()
- 位置: L15-20
- 役割: URL の e= パラメータからエラーコードを取り出す。
- 触るとき: エラーの種類の判定方法を変えるとき。
- 呼び出し先: `decodeURIComponent()`, `url.search()`, `url.slice()`
- 参照: `document.documentURI`

## getURL()
- 位置: L22-39
- 役割: URL の u= パラメータから元のページ URL を取り出し、view-source: の接頭辞を外す。
- 触るとき: 警告ページに表示する元 URL の扱いを変えるとき。
- 呼び出し先: `decodeURIComponent()`, `url.match()`, `url.startsWith()`
- 条件付き依存: `if (url.startsWith("view-source:"))` → `url.slice()`
- 参照: `document.documentURI`

## getAddonName()
- 位置: L41-52
- 役割: URL の a= パラメータからアドオン名を取り出す。無ければ空文字。
- 触るとき: アドオン由来の警告の文言を変えるとき。
- 呼び出し先: `decodeURIComponent()`, `url.match()`
- 参照: `document.documentURI`

## getOverride()
- 位置: L59-63
- 役割: URL に o=1 があるかを見て、無視して進める操作が許されるかを判定する。
- 触るとき: 無視して進むリンクの表示条件を変えるとき。
- 呼び出し先: `url.match()`
- 参照: `document.documentURI`

## getHostString()
- 位置: L69-75
- 役割: document.location の hostname を返す。取れなければ getURL の結果を返す。
- 触るとき: 警告文に出すサイト名の決め方を変えるとき。
- 呼び出し先: `getURL()`
- 参照: `document.location.hostname`

## onClickSeeDetails()
- 位置: L77-80
- 役割: 詳細欄の表示と非表示を切り替える。
- 触るとき: 詳細欄の開閉を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `details.hidden`

## initPage()
- 位置: L82-213
- 役割: エラー種別ごとの文言 ID を選び、タイトル、説明、詳細、リンクを設定する。不要な要素を削除し、読み込み完了イベントを出す。
- 触るとき: 警告ページの文言や種別ごとの表示を追加・変更するとき。
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
