# browser/components/urlbar/content/UrlbarQueryContext.mjs

source: browser/components/urlbar/content/UrlbarQueryContext.mjs
source-hash: 1cb514a3074bc37972753505c1ad5a7eadf489c7
lines: 516

## <module>
- 役割: 1 回の urlbar クエリの条件 (検索文字列、SAP、許可された結果源など) を保持し、親子間で送るクラス。

## UrlbarQueryContext.constructor()
- 位置: L69-133
- 役割: オプションを複製し、必須項目を検査した上で任意項目を既定値付きで設定し、ID と検索文字列の正規化値を用意する。
- 触るとき: 新しいクエリオプションを増やす時や、userContextId や tabGroup の既定値がずれる時。
- 呼び出し先: `Array.isArray()`, `UrlbarShared.normalizedUserContextId()`, `isNaN()`, `structuredClone()`, `this._checkRequiredOptions()`, `this.searchString.toLowerCase()`, `this.searchString.trim()`, `this.trimmedSearchString.toLowerCase()`
- 条件付き依存: `if (prop in options)` → `checkFn()`
- 参照: `options.maxResults`, `options.tabGroup`, `options.userContextId`, `this.deferUserSelectionProviders`, `this.firstTimerId`, `this.id`, `this.isPrivate`, `this.lastResultCount`, `this.lowerCaseSearchString`, `this.pendingHeuristicProviders`, `this.sixthTimerId`, `this.tabGroup`, `this.trimmedLowerCaseSearchString`, `this.trimmedSearchString`, `this.userContextId`, `v.length`

## UrlbarQueryContext.isSearchbarSAP()
- 位置: L265-267
- 役割: この文脈の SAP が検索バー専用かを UrlbarShared.isSearchbarSAP に委ねて返す。
- 触るとき: 検索バーと urlbar で結果の種類が分かれる分岐を調べる時。
- 呼び出し先: `UrlbarShared.isSearchbarSAP()`
- 参照: `this.sapName`

## UrlbarQueryContext.keywordEnabled()
- 位置: L276-278
- 役割: 非 URL の文字列を検索に回してよいかを、SAP から UrlbarShared.keywordEnabled で判定する。
- 触るとき: URL でない入力が検索されない、または検索されすぎる時。
- 呼び出し先: `UrlbarShared.keywordEnabled()`
- 参照: `this.sapName`

## UrlbarQueryContext.navigationEnabled()
- 位置: L287-289
- 役割: URL として移動してよいかを、SAP から UrlbarShared.navigationEnabled で判定する。
- 触るとき: 検索バーで URL を入れても移動しない、といった挙動を確かめる時。
- 呼び出し先: `UrlbarShared.navigationEnabled()`
- 参照: `this.sapName`

## UrlbarQueryContext.navigationInSearchModeEnabled()
- 位置: L299-301
- 役割: エンジン検索モード中に URL への移動を許すかを、SAP から判定する。
- 触るとき: 検索モード中に URL を入れた時の扱いを変える時。
- 呼び出し先: `UrlbarShared.navigationInSearchModeEnabled()`
- 参照: `this.sapName`

## UrlbarQueryContext.restrictInSearchMode()
- 位置: L318-324
- 役割: 検索モード中に結果を検索候補だけに絞るかを判定する。historyInSearchMode が有効なら、エンジン検索モード以外の局所検索モードだけを絞る。
- 触るとき: 検索モードで履歴やブックマークが出なくなる、または出すぎる時。
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `this.searchMode`, `this.searchMode.engineName`

## UrlbarQueryContext._checkRequiredOptions()
- 位置: L351-360
- 役割: 必須オプションが無ければ例外を投げ、あれば this に保存する。
- 触るとき: 必須オプションを追加し、呼び出し側で渡し忘れを見つける時。

## UrlbarQueryContext.fixupInfo()
- 位置: L370-396
- 役割: 検索文字列を URI fixup にかけ、href・isSearch・scheme を初回だけ計算して保持する。失敗時は _fixupError に記録する。
- 触るとき: 入力が URL か検索語かの判定結果がずれる時。特権コードでしか動かないので、content 側から呼ばれていないかも確かめる。
- 条件付き依存: `if (!this._fixupError && !this._fixupInfo && this.trimmedSearchString)` → `Services.uriFixup.getFixupURIInfo()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_FORCE_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `ex.result`, `info.fixedURI.scheme`, `info.fixedURI.spec`, `info.keywordAsSent`, `this._fixupError`, `this._fixupInfo`, `this.isPrivate`, `this.isSearchbarSAP`, `this.searchString`, `this.trimmedSearchString`
- XPCOM: [`nsIURIFixup`](../../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## UrlbarQueryContext.fixupError()
- 位置: L405-411
- 役割: fixupInfo が無い場合に、記録済みの fixup 失敗の結果コードを返す。
- 触るとき: fixup が失敗した理由を分岐やテストで判定する時。
- 参照: `this._fixupError`, `this.fixupInfo`

## UrlbarQueryContext.allowRemoteResults()
- 位置: L426-468
- 役割: リモート候補を取ってよいかを判定する。短すぎる文字列、origin らしい文字列、URL らしい文字列では false を返す。
- 触るとき: リモート候補が出ない、または出すぎる原因を調べる時や、プライバシー上の判定を変える時。
- 参照: `UrlbarShared.TOKEN_TYPE.POSSIBLE_ORIGIN`, `UrlbarShared.TOKEN_TYPE.POSSIBLE_ORIGIN_BUT_SEARCH_ALLOWED`, `searchString.length`, `this.fixupInfo?.href`, `this.fixupInfo?.isSearch`, `this.navigationEnabled`, `this.prohibitRemoteResults`, `this.searchString`, `this.tokens`, `this.tokens.length`, `this.tokens[0].type`

## UrlbarQueryContext.toWire()
- 位置: L478-484
- 役割: 文脈を構造化複製できる素のオブジェクトにし、結果と heuristic 結果を wire 形式に変える。
- 触るとき: 文脈に新しいフィールドを足し、actor 越しに届くかを確かめる時。
- 呼び出し先: `result.toWire()`, `this.heuristicResult?.toWire()`, `this.results?.map()`

## UrlbarQueryContext.fromWire()
- 位置: L496-503
- 役割: wire 形式の文脈にクラスのプロトタイプを戻し、結果を UrlbarResult に復元する。
- 触るとき: 親子間で受け取った文脈の結果が欠けたり型が崩れたりする時。
- 呼び出し先: `Object.setPrototypeOf()`, `UrlbarResult.fromWire()`, `wire.results?.map()`
- 条件付き依存: `if (wire.heuristicResult)` → `UrlbarResult.fromWire()`
- 参照: `UrlbarQueryContext.prototype`, `wire.heuristicResult`, `wire.results`
