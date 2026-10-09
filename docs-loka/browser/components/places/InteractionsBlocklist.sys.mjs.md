# browser/components/places/InteractionsBlocklist.sys.mjs

source: browser/components/places/InteractionsBlocklist.sys.mjs
source-hash: 172141f195a23558a7ac66dafae7216efe2d2b66
lines: 278

## <module>
- 役割: インタラクションとして記録してよい URL を判定する遮断リストを持つモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## get()
- 位置: L75-93
- 役割: 遮断リストの文字列の正規表現を初回参照時に RegExp へ変換し、配列へ書き戻す。
- 触るとき: 遮断リストの書式を変えるとき、ホスト別の正規表現がいつ生成されるかを追うとき。
- 呼び出し先: `Array.isArray()`
- 参照: `regexes.length`

## _InteractionsBlocklist.constructor()
- 位置: L101-120
- 役割: pref places.interactions.customBlocklist の JSON 配列を正規表現にして '*' の遮断リストへ入れる。形式が不正なら警告を出す。
- 触るとき: カスタム遮断リストの pref 形式を変えるとき、起動時にリストが反映されない問題を調べるとき。
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Services.prefs.getStringPref()`, `customBlocklist.map()`, `lazy.logConsole.warn()`
- XPCOM: `Services.prefs`

## _InteractionsBlocklist.urlRequirements()
- 位置: L129-135
- 役割: 記録できるプロトコルと追加条件の Map を返す。http と https は条件なし、file は拡張子 pdf のみ。
- 触るとき: 記録対象のスキームを増減するとき、ローカルの PDF が記録されない理由を調べるとき。

## _InteractionsBlocklist.canRecordUrl()
- 位置: L144-161
- 役割: URL のプロトコルと、必要なら末尾の拡張子が urlRequirements を満たすかを返す。
- 触るとき: 新しいスキームや拡張子を許可するとき、URL が記録対象外になる理由を調べるとき。
- 呼び出し先: `InteractionsBlocklist.urlRequirements.get()`, `pathname.endsWith()`
- 参照: `Ci.nsIURI`, `requirements.extension`, `url.filePath`, `url.pathname`, `url.protocol`, `url.scheme`
- XPCOM: [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md)

## _InteractionsBlocklist.isUrlBlocklisted()
- 位置: L172-217
- 役割: 成人向けサイト、記録不可の URL、基底ホストごとの正規表現と '*' の正規表現で、記録してはならない URL を判定する。
- 触るとき: 検索結果や認証ページを記録対象から外す判定を変えるとき、誤って除外される URL を調べるとき。呼び出しごとに '*' の正規表現が基底ホストの配列へ追記されるので、その副作用も確認する。
- 呼び出し先: `URL.parse()`, `baseHost.toLocaleLowerCase()`, `hostWithSubdomains.lastIndexOf()`, `hostWithSubdomains.substring()`, `lazy.FilterAdult.isAdultUrl()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `lazy.UrlbarUtils.stripPublicSuffixFromHost()`, `r.test()`, `regexes.push()`, `regexes.some()`, `this.canRecordUrl()`
- 条件付き依存: `if (!url)` → `lazy.logConsole.warn()`
- 参照: `url.host`, `url.href`, `url.protocol`

## _InteractionsBlocklist.addRegexToBlocklist()
- 位置: L228-245
- 役割: 正規表現を大文字小文字を区別せず作り、'*' の遮断リストへ加えて pref に保存する。
- 触るとき: テストやコンソールから遮断パターンを追加する経路を変えるとき、保存形式を確認するとき。
- 呼び出し先: `HOST_BLOCKLIST["*"].map()`, `HOST_BLOCKLIST["*"].push()`, `JSON.stringify()`, `Services.prefs.setStringPref()`, `lazy.logConsole.warn()`, `reg.toString()`
- XPCOM: `Services.prefs`

## _InteractionsBlocklist.removeRegexFromBlocklist()
- 位置: L255-274
- 役割: '*' の遮断リストから source が一致する正規表現を取り除き、pref を更新する。
- 触るとき: 遮断パターンを削除したのに実効リストと pref がずれる問題を調べるとき。
- 呼び出し先: `Array.isArray()`, `HOST_BLOCKLIST["*"].filter()`, `HOST_BLOCKLIST["*"].map()`, `JSON.stringify()`, `Services.prefs.setStringPref()`, `lazy.logConsole.warn()`, `reg.toString()`
- 参照: `curr.source`, `regex.source`
- XPCOM: `Services.prefs`
