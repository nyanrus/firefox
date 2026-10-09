# browser/components/urlbar/UrlbarSearchTermsPersistence.sys.mjs

source: browser/components/urlbar/UrlbarSearchTermsPersistence.sys.mjs
source-hash: 05db07d0ed434bdac88487acdbc0332e1e8c9f37
lines: 508

## <module>
- 役割: 既定の検索結果ページで入力された検索語を、urlbar に残し続ける条件を判定する UrlbarSearchTermsPersistence を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `lazy.UrlbarShared.getLogger()`

## _UrlbarSearchTermsPersistence.init()
- 位置: async L66-92
- 役割: リモート設定から provider 情報を取得して保存し、同期イベントの監視を登録する。取得に失敗しても例外にせず空の情報で続ける。
- 触るとき: 検索語の保持のための設定が読み込まれない問題を調べるとき見る。設定の取得元の変更もここで行う。
- 呼び出し先: `lazy.RemoteSettings()`, `lazy.logger.error()`, `this.#setSearchProviderInfo()`, `this.#urlbarSearchTermsPersistenceSettings.get()`, `this.#urlbarSearchTermsPersistenceSettings.on()`
- 参照: `this.#initialized`, `this.#originalProviderInfo`, `this.#urlbarSearchTermsPersistenceSettings`, `this.#urlbarSearchTermsPersistenceSettingsSync`

## this.#urlbarSearchTermsPersistenceSettingsSync()
- 位置: L81-82
- 役割: リモート設定の sync イベントを #onSettingsSync に渡す無名関数を保持し、uninit で監視を外せるようにする。
- 触るとき: 同期の監視の登録や解除の対象を変えるとき見る。
- 呼び出し先: `this.#onSettingsSync()`

## _UrlbarSearchTermsPersistence.uninit()
- 位置: L94-114
- 役割: 同期の監視を外し、設定の参照を消して初期化済みの状態を戻す。外す処理が失敗しても例外は記録だけする。
- 触るとき: 終了時や再初期化の後に監視が残る不具合を調べるとき見る。
- 呼び出し先: `lazy.logger.error()`, `this.#urlbarSearchTermsPersistenceSettings.off()`
- 参照: `this.#initialized`, `this.#urlbarSearchTermsPersistenceSettings`, `this.#urlbarSearchTermsPersistenceSettingsSync`

## _UrlbarSearchTermsPersistence.getSearchProviderInfo()
- 位置: L116-118
- 役割: 現在の provider 情報の配列をそのまま返す。
- 触るとき: provider 情報を外から参照する箇所の挙動を調べるとき見る。
- 参照: `this.#searchProviderInfo`

## _UrlbarSearchTermsPersistence.overrideSearchTermsPersistenceForTests()
- 位置: L127-130
- 役割: テスト専用で provider 情報を差し替え、引数が無ければ元の情報に戻す。
- 触るとき: テストで provider 情報を固定したいときに使う。本番のコードからは呼ばない。
- 呼び出し先: `this.#setSearchProviderInfo()`
- 参照: `this.#originalProviderInfo`

## _UrlbarSearchTermsPersistence.getSearchTerm()
- 位置: L145-213
- 役割: http(s) の URL から既定 SERP の検索語を取り出す。provider の規則があればそれを使い、URL のような語句や長すぎる語は空にする。
- 触るとき: どの URL から検索語を拾うか、URL に見える語を除外する条件を変えるとき見る。検索語が保持されない原因を調べるときにも見る。
- 呼び出し先: `/^https?:\/\//.test()`, `Services.uriFixup.getFixupURIInfo()`, `searchTerm.replaceAll()`, `searchTermWithSpacesRemoved.startsWith()`, `this.#getProviderInfoForURL()`
- 条件付き依存: `if (provider)` → `lazy.SearchService.parseSubmissionURL()`
- 条件付き依存: `if (provider)` → `this.isDefaultPage()`
- 条件付き依存: `if (!(provider))` → `lazy.SearchService.parseSubmissionURL()`
- 条件付き依存: `if (!(provider))` → `result.engine.searchTermFromResult()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `info.keywordAsSent`, `lazy.ConfigSearchEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `lazy.UrlbarShared.MAX_TEXT_LENGTH`, `result.engine`, `result.terms`, `searchTerm.length`, `uri.spec`, `uri?.spec`
- XPCOM: [`nsIURIFixup`](../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## _UrlbarSearchTermsPersistence.shouldPersist()
- 位置: L215-273
- 役割: 保持中の状態について、ユーザーが入力を変えていないか、同じ文書内でも既定ページか、検索モードが一致するか、オリジンとパスが同じかを順に確かめ、全てを満たすときだけ true を返す。
- 触るとき: 検索語が消える、または残りすぎるときに、どの条件で false になったかを確かめるとき見る。Bug 1972464 の制限もここにある。
- 呼び出し先: `URL.fromURI()`, `this.isDefaultPage()`, `this.searchModeMatchesState()`
- 参照: `persist.searchTerms`, `state.persist`, `state.persist.origin`, `state.persist.pathname`, `state.persist.provider`, `state.searchModes?.confirmed`, `url.origin`, `url.pathname`

## _UrlbarSearchTermsPersistence.setPersistenceState()
- 位置: L276-336
- 役割: 状態を初期化し、URL の検索語、オリジン、パス、provider、元の検索エンジン名と既定かどうかを記録する。検索語が取れなければ状態を設定しない。
- 触るとき: 保持する検索状態に新しい項目を足すとき、または保持開始時の値を変えるとき見る。
- 呼び出し先: `URL.fromURI()`, `this.#getProviderInfoForURL()`, `this.#searchModeForUrl()`, `this.getSearchTerm()`
- 参照: `result.engineName`, `result.isDefaultEngine`, `state.persist`, `state.persist.isDefaultEngine`, `state.persist.origin`, `state.persist.originalEngineName`, `state.persist.originalURI`, `state.persist.pathname`, `state.persist.provider`, `state.persist.searchTerms`, `uri.spec`, `uri?.spec`, `url.origin`, `url.pathname`

## _UrlbarSearchTermsPersistence.searchModeMatchesState()
- 位置: L351-359
- 役割: 現在の検索モードが保持中のエンジンと一致するか、検索モードが無く保持中のエンジンが既定なら true を返す。
- 触るとき: 検索モードの変更で保持を続けてよいかを変えるとき見る。
- 参照: `searchMode?.engineName`, `state.persist?.isDefaultEngine`, `state.persist?.originalEngineName`

## _UrlbarSearchTermsPersistence.onSearchModeChanged()
- 位置: L361-376
- 役割: 保持中で検索モードが保持エンジンと合わなくなったら、保持を止めて persistsearchterms 属性を外す。
- 触るとき: 検索モードを切り替えた後に検索語が残る、または消える問題を調べるとき見る。
- 呼び出し先: `this.searchModeMatchesState()`, `window.gURLBar.getBrowserState()`
- 条件付き依存: `if ( state.persist.shouldPersist && !this.searchModeMatchesState(state.searchModes?.confirmed, state) )` → `window.gURLBar.removeAttribute()`
- 参照: `state.persist.shouldPersist`, `state.searchModes?.confirmed`, `state?.persist`, `window.gBrowser.selectedBrowser`

## _UrlbarSearchTermsPersistence.#onSettingsSync()
- 位置: async L378-390
- 役割: 同期で届いた current の情報を保存し直し、同期完了の通知を流す。current が無ければ情報は変えない。
- 触るとき: リモート設定の同期後に新しい provider 情報が反映されない問題を調べるとき見る。
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (current)` → `lazy.logger.debug()`
- 条件付き依存: `if (current)` → `this.#setSearchProviderInfo()`
- 条件付き依存: `if (!(current))` → `lazy.logger.debug()`
- 参照: `event.data?.current`, `this.#originalProviderInfo`
- XPCOM: `Services.obs`

## _UrlbarSearchTermsPersistence.#searchModeForUrl()
- 位置: L397-410
- 役割: 既定エンジンが無ければ null を返し、URL が標準エンジンの検索結果なら、そのエンジン名と既定かどうかを返す。
- 触るとき: URL から検索エンジンを特定する判定を変えるとき見る。
- 呼び出し先: `lazy.SearchService.parseSubmissionURL()`
- 参照: `lazy.ConfigSearchEngine`, `lazy.SearchService.defaultEngine`, `result.engine`, `result.engine.name`

## _UrlbarSearchTermsPersistence.#setSearchProviderInfo()
- 位置: L420-428
- 役割: provider 情報の searchPageRegexp を RegExp に変換して保存する。
- 触るとき: provider 情報の正規表現の扱い(フラグや変換)を変えるとき見る。
- 呼び出し先: `providerInfo.map()`
- 参照: `provider.searchPageRegexp`, `this.#searchProviderInfo`

## _UrlbarSearchTermsPersistence.#getProviderInfoForURL()
- 位置: L438-442
- 役割: 保存済みの provider 情報のうち、URL が searchPageRegexp に一致する最初のものを返す。
- 触るとき: provider 情報の一致の優先順位を調べるとき見る。
- 呼び出し先: `info.searchPageRegexp.test()`, `this.#searchProviderInfo.find()`

## _UrlbarSearchTermsPersistence.isDefaultPage()
- 位置: L455-504
- 役割: URL の検索パラメーターが provider の includeParams を満たし、excludeParams に当たらないかを確かめ、既定の検索結果ページかどうかを返す。
- 触るとき: 既定ページとみなす条件を provider ごとに変えるとき、この包含と除外の規則を見る。
- 呼び出し先: `URL.fromURI()`
- 条件付き依存: `if (provider.includeParams?.length)` → `searchParams.has()`
- 条件付き依存: `if (provider.includeParams?.length)` → `searchParams.get()`
- 条件付き依存: `if (provider.includeParams?.length)` → `param?.values.includes()`
- 条件付き依存: `if (provider.excludeParams)` → `searchParams.get()`
- 条件付き依存: `if (provider.excludeParams)` → `param.values?.includes()`
- 参照: `param.canBeMissing`, `param.key`, `param.values?.length`, `provider.excludeParams`, `provider.includeParams`, `provider.includeParams?.length`, `searchParams.size`
