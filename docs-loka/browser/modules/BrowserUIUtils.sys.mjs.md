# browser/modules/BrowserUIUtils.sys.mjs

source: browser/modules/BrowserUIUtils.sys.mjs
source-hash: 09a3b842426b6433ba4b8c008c7ec396240db6e1
lines: 197

## <module>
- 役割: URL バーなどで使う表示用の共通ユーティリティ。空ページの判定、多言語文字列への要素の差し込み、URL の表示用の整形を担う。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## checkEmptyPageOrigin()
- 位置: L30-64
- 役割: ページが空の新しいタブ相当か、その起点が URI と一致するかを判定する。
- 触るとき: 空ページ判定や URL バーの更新条件を変えるとき。他のページから開かれた(hasContentOpener)ページは false になる。
- 条件付き依存: `if (contentPrincipal.isContentPrincipal)` → `contentPrincipal.equalsURI()`
- 参照: `browser.contentPrincipal`, `browser.currentURI`, `browser.documentURI`, `browser.hasContentOpener`, `contentPrincipal.isContentPrincipal`, `contentPrincipal.isNullPrincipal`, `contentPrincipal.isSystemPrincipal`, `contentPrincipal.spec`, `uriToCheck.spec`

## getLocalizedFragment()
- 位置: L87-137
- 役割: 多言語文字列の %S 部分を、文字列やノードで置き換えた DocumentFragment を作る。
- 触るとき: innerHTML を使わずに要素を差し込むラベルを作るとき。引数の数が挿入位置と合わないとコンソールにエラーを出す。
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
- 役割: http, https, ftp の URL の末尾の / を 1 つ取り除く。
- 触るとき: 表示用 URL の末尾のスラッシュの扱いを変えるとき。
- 呼び出し先: `aURL.replace()`

## trimURLProtocol()
- 位置: L144-148
- 役割: pref trimHttps が有効なら https:// を、無効なら http:// を返す。
- 触るとき: URL 表示で省くプロトコルを変えるとき。
- 呼び出し先: `UrlbarPrefs.getScotchBonnetPref()`

## getTrimmedURLPrefix()
- 位置: L159-169
- 役割: URL の先頭から省く接頭辞(プロトコル、必要なら www.)を返す。省かない時は空文字。
- 触るとき: 省く接頭辞の判定を変えるとき。ページ読み込みの経路でも使われるので、軽い処理を保つ。
- 呼び出し先: `aURL.startsWith()`
- 条件付き依存: `if (aURL.startsWith(this.trimURLProtocol))` → `aURL.substring()`
- 条件付き依存: `if (aURL.startsWith(this.trimURLProtocol))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (aURL.startsWith(this.trimURLProtocol))` → `aURL.startsWith()`
- 参照: `prefix.length`, `this.trimURLProtocol`

## trimURL()
- 位置: L184-188
- 役割: 末尾の / と接頭辞を取り除いた表示用の文字列を返す。
- 触るとき: URL バーに出す表示の形を変えるとき。取り除いた URL は読み込み先が変わることがあるため、そのまま読み込みに使わず URIFixup を通す。
- 呼び出し先: `this.getTrimmedURLPrefix()`, `this.removeSingleTrailingSlashFromURL()`, `url.substring()`
- 参照: `prefix.length`
