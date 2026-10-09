# browser/components/urlbar/UrlbarValueFormatter.sys.mjs

source: browser/components/urlbar/UrlbarValueFormatter.sys.mjs
source-hash: 7ac2e345ea619d60c90bdde4c274786c9ade8e89
lines: 709

## <module>
- 役割: urlbar の入力欄に URL のホスト強調、スキームの取り消し線、@エイリアスの着色を適用するフォーマッタ。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## UrlbarValueFormatter.constructor()
- 位置: L24-28
- 役割: UrlbarInput を保持し、window の resize イベントを購読する。
- 触るとき: リサイズ後にホストが見切れる、またはフォーマッタの初期化タイミングを変えるときに見る。
- 呼び出し先: `this.#window.addEventListener()`
- 参照: `this.#urlbarInput`

## UrlbarValueFormatter.update()
- 位置: async L30-82
- 役割: 入力値の書式を非同期に更新する。起動完了と SearchService の初期化を待ち、古い呼び出しは instance で破棄して、次の描画フレームで URL 書式かエイリアス書式を適用する。
- 触るとき: 起動直後や入力直後に書式が出ない、古い書式が残るといった不具合を調べるとき。
- 呼び出し先: `this.#formatSearchAlias()`, `this.#formatURL()`, `this.#removeSearchAliasFormat()`, `this.#removeURLFormat()`, `this.#urlbarInput.removeAttribute()`, `this.#window.requestAnimationFrame()`
- 条件付き依存: `if (!lazy.SearchService.isInitialized)` → `lazy.SearchService.init()`
- 参照: `lazy.SearchService.isInitialized`, `this.#formattingApplied`, `this.#scheme.value`, `this.#updateInstance`, `this.#urlbarInput.value`, `this.#window.delayedStartupPromise`, `this.#window.docShell`, `this.#window.gBrowserInit.delayedStartupFinished`

## UrlbarValueFormatter.#document()
- 位置: L91-93
- 役割: urlbarInput の document を返す。
- 触るとき: フォーマッタが参照する DOM の取得元を変えるときに見る。
- 参照: `this.#urlbarInput.document`

## UrlbarValueFormatter.#inputField()
- 位置: L95-97
- 役割: urlbarInput の inputField(実際の入力要素)を返す。
- 触るとき: スクロール位置やスタイルを設定する対象を変えるときに見る。
- 参照: `this.#urlbarInput.inputField`

## UrlbarValueFormatter.#window()
- 位置: L99-101
- 役割: urlbarInput の window を返す。
- 触るとき: resize や matchMedia などウィンドウ単位の処理を追うときに見る。
- 参照: `this.#urlbarInput.window`

## UrlbarValueFormatter.#scheme()
- 位置: L103-107
- 役割: #urlbar-scheme 要素(スキーム表示用の入力欄)を取得する。
- 触るとき: スキーム表示の要素の ID や取得方法を変えるときに見る。
- 呼び出し先: `this.#urlbarInput.querySelector()`

## UrlbarValueFormatter.#scrollHostIntoView()
- 位置: L109-126
- 役割: ホストが見えるように入力欄の scrollLeft を調整する。ホスト範囲がなければ先頭か末尾に寄せる。RTL では scrollLeftMax で上限を抑える。
- 触るとき: 長い URL でホストが画面外に出る、または RTL 入力のスクロール位置がおかしいときに見る。
- 条件付き依存: `if (this.#hostRange)` → `this.#hostRange.getBoundingClientRect()`
- 条件付き依存: `if (this.#hostRange)` → `this.#inputField.getBoundingClientRect()`
- 条件付き依存: `if (this.#hostRange)` → `Math.min()`
- 条件付き依存: `if (this.#hostRange)` → `Math.max()`
- 参照: `hostRect.left`, `hostRect.right`, `this.#hostRange`, `this.#inputField.scrollLeft`, `this.#inputField.scrollLeftMax`, `urlbarRect.left`, `urlbarRect.right`

## UrlbarValueFormatter.#ensureFormattedHostVisible()
- 位置: L128-154
- 役割: ホストの方向性を判定して domaindir 属性を rtl か ltr に設定し、ホストが見えるよう scroll を合わせ、text-overflow を更新する。urlMetaData が無ければ domaindir を外して戻る。
- 触るとき: RTL ドメインの表示位置や domaindir 属性の扱いを変えるときに見る。
- 呼び出し先: `this.#getUrlMetaData()`, `this.#urlbarInput.updateTextOverflow()`, `this.#window.windowUtils.getDirectionFromText()`
- 条件付き依存: `if (!urlMetaData)` → `this.#urlbarInput.removeAttribute()`
- 条件付き依存: `if ( directionality == this.#window.windowUtils.DIRECTION_RTL && url[preDomain.length + domain.length] != "\u200E" )` → `this.#urlbarInput.setAttribute()`
- 条件付き依存: `if ( directionality == this.#window.windowUtils.DIRECTION_RTL && url[preDomain.length + domain.length] != "\u200E" )` → `this.#scrollHostIntoView()`
- 条件付き依存: `if (!( directionality == this.#window.windowUtils.DIRECTION_RTL && url[preDomain.length + domain.length] != "\u200E" ))` → `this.#urlbarInput.setAttribute()`
- 条件付き依存: `if (!( directionality == this.#window.windowUtils.DIRECTION_RTL && url[preDomain.length + domain.length] != "\u200E" ))` → `this.#scrollHostIntoView()`
- 参照: `domain.length`, `preDomain.length`, `this.#window.windowUtils.DIRECTION_RTL`

## UrlbarValueFormatter.#getUrlMetaData()
- 位置: L156-294
- 役割: 入力値を URL として解析し、プレドメインとホストの位置を返す。フォーカス中や URL でない入力は null を返す。結果はブラウザごとに状態へキャッシュし、http(s) は直接パース、それ以外は URIFixup で解決する。解決後のホストが表示用と違えば入力を置き換えて再帰する。
- 触るとき: URL の強調範囲がずれる、タブ切り替えで古い強調が残るといった問題を調べるときに見る。
- 呼び出し先: `Services.io.newURI()`, `inputValue.startsWith()`, `this.#urlbarInput.getBrowserState()`, `untrimmedValue.startsWith()`, `url.match()`
- 条件付き依存: `if ( untrimmedValue.startsWith("http://") || untrimmedValue.startsWith("https://") )` → `Services.io.newURI()`
- 条件付き依存: `if (!uri)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!uri)` → `Services.uriFixup.getFixupURIInfo()`
- 条件付き依存: `if (!uri)` → `["http", "https"].includes()`
- 条件付き依存: `if (replaceUrl)` → `this.#urlbarInput.setURI()`
- 条件付き依存: `if (replaceUrl)` → `this.#getUrlMetaData()`
- 参照: `Ci.nsILoadInfo.SchemelessInputTypeSchemeless`, `Services.io.newURI("http://" + domain).displayHost`, `Services.uriFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Services.uriFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Services.uriFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `browserState.urlMetaData`, `browserState.urlMetaData.data`, `browserState.urlMetaData.inputValue`, `browserState.urlMetaData.untrimmedValue`, `lazy.BrowserUIUtils.trimURLProtocol`, `scheme.length`, `this.#inGetUrlMetaData`, `this.#urlbarInput.focused`, `this.#urlbarInput.untrimmedValue`, `this.#urlbarInput.value`, `this.#window`, `this.#window.gBrowser.selectedBrowser`, `this.#window.gBrowser.userTypedValue`, `trimmedProtocol.length`, `uri.displayHost`, `uri.host`, `uri.scheme`, `uriInfo.fixedURI`, `uriInfo.fixedURI.scheme`, `uriInfo.keywordProviderId`, `uriInfo?.schemelessInput`
- XPCOM: [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / `Services.io` / `Services.uriFixup`

## UrlbarValueFormatter.#removeURLFormat()
- 位置: L296-309
- 役割: URL 強調の取り消し線と secondary の選択範囲を消し、スキーム表示と --urlbar-scheme-size を初期化する。書式が適用されていなければ何もしない。
- 触るとき: 書式を付け直す前の掃除で選択範囲が残る不具合を調べるときに見る。
- 呼び出し先: `controller.getSelection()`, `selection.removeAllRanges()`, `strikeOut.removeAllRanges()`, `this.#formatScheme()`, `this.#inputField.style.setProperty()`
- 参照: `controller.SELECTION_URLSECONDARY`, `controller.SELECTION_URLSTRIKEOUT`, `this.#formattingApplied`, `this.#hostRange`, `this.#urlbarInput.editor.selectionController`

## UrlbarValueFormatter.formattingEnabled()
- 位置: L316-318
- 役割: UrlbarPrefs の formatting.enabled を返す。
- 触るとき: URL 書式の有効・無効の判定条件を変えるときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`

## UrlbarValueFormatter.willShowFormattedMixedContentProtocol()
- 位置: L329-337
- 役割: https の混在コンテンツ表示で取り消し線を出すべきかを判定する。書式有効、insecure_connection_text 無効、val が現在の入力値、混在アクティブコンテンツの読込み中のとき true。
- 触るとき: 混在コンテンツ時の https 取り消し線が出ない、または出すぎるときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `val.startsWith()`
- 参照: `this.#showingMixedContentLoadedPageUrl`, `this.#urlbarInput.value`, `this.formattingEnabled`

## UrlbarValueFormatter.#showingMixedContentLoadedPageUrl()
- 位置: L387-395
- 役割: pageproxystate が valid で、表示中ページが混在アクティブコンテンツを読み込んでいるかを返す。
- 触るとき: 混在コンテンツの判定が表示とずれる不具合を調べるときに見る。
- 呼び出し先: `this.#urlbarInput.getAttribute()`
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_ACTIVE_CONTENT`, `this.#window.gBrowser.securityUI.state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## UrlbarValueFormatter.#formatURL()
- 位置: L406-517
- 役割: 入力が URL で入力欄が非フォーカスのとき、スキームを scheme 要素に出し、ホストを強調する。混在時は https を取り消し線にし、baseDomain より前をサブドメインとして薄く表示する。検索語表示中は何もしない。
- 触るとき: URL の強調範囲や色分けを変えるとき、検索語表示中に URL 書式が出る不具合を調べるときに見る。
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`, `controller.getSelection()`, `domain.endsWith()`, `lazy.UrlbarPrefs.get()`, `this.#ensureFormattedHostVisible()`, `this.#formatScheme()`, `this.#getUrlMetaData()`, `this.#urlbarInput.getBrowserState()`, `this.#urlbarInput.value.startsWith()`, `this.willShowFormattedMixedContentProtocol()`
- 条件付き依存: `if ( !lazy.UrlbarPrefs.get("security.insecure_connection_text.enabled") && !isUnformattedMixedContent && this.#urlbarInput.value.startsWith(schemeWSlashes) )` → `this.#inputField.style.setProperty()`
- 条件付き依存: `if (hostStart < hostEnd)` → `this.#document.createRange()`
- 条件付き依存: `if (hostStart < hostEnd)` → `this.#hostRange.setStart()`
- 条件付き依存: `if (hostStart < hostEnd)` → `this.#hostRange.setEnd()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `this.#document.createRange()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `range.setStart()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `range.setEnd()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `controller.getSelection()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `strikeOut.addRange()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `this.#formatScheme()`
- 条件付き依存: `if (!domain.endsWith(baseDomain))` → `Cc["@mozilla.org/network/idn-service;1"].getService()`
- 条件付き依存: `if (!domain.endsWith(baseDomain))` → `IDNService.domainToDisplay()`
- 条件付き依存: `if (baseDomain != domain)` → `domain.slice()`
- 条件付き依存: `if (rangeLength)` → `this.#document.createRange()`
- 条件付き依存: `if (rangeLength)` → `range.setStart()`
- 条件付き依存: `if (rangeLength)` → `range.setEnd()`
- 条件付き依存: `if (rangeLength)` → `selection.addRange()`
- 条件付き依存: `if (startRest < url.length - trimmedLength)` → `this.#document.createRange()`
- 条件付き依存: `if (startRest < url.length - trimmedLength)` → `range.setStart()`
- 条件付き依存: `if (startRest < url.length - trimmedLength)` → `range.setEnd()`
- 条件付き依存: `if (startRest < url.length - trimmedLength)` → `selection.addRange()`
- 参照: `Ci.nsIIDNService`, `baseDomain.length`, `controller.SELECTION_URLSECONDARY`, `controller.SELECTION_URLSTRIKEOUT`, `domain.length`, `editor.rootElement.firstChild`, `editor.selectionController`, `preDomain.length`, `schemeWSlashes.length`, `state.searchTerms`, `subDomain.length`, `this.#hostRange`, `this.#scheme.value`, `this.#showingMixedContentLoadedPageUrl`, `this.#urlbarInput.editor`, `this.#urlbarInput.value`, `this.#window.gBrowser.selectedBrowser`, `this.formattingEnabled`, `url.length`
- XPCOM: [`nsIIDNService`](../../../netwerk/dns/nsIIDNService.idl.md) / `@mozilla.org/network/idn-service;1` / `Services.eTLD`

## UrlbarValueFormatter.#formatScheme()
- 位置: L519-532
- 役割: scheme 要素の全文を指定の選択種別に登録する。clear が true なら選択範囲を消す。
- 触るとき: スキーム要素の取り消し線や secondary 表示を直すときに見る。
- 呼び出し先: `controller.getSelection()`
- 条件付き依存: `if (clear)` → `selection.removeAllRanges()`
- 条件付き依存: `if (!(clear))` → `this.#document.createRange()`
- 条件付き依存: `if (!(clear))` → `r.setStart()`
- 条件付き依存: `if (!(clear))` → `r.setEnd()`
- 条件付き依存: `if (!(clear))` → `selection.addRange()`
- 参照: `editor.rootElement.firstChild`, `editor.selectionController`, `textNode.textContent.length`, `this.#scheme.editor`

## UrlbarValueFormatter.#removeSearchAliasFormat()
- 位置: L534-542
- 役割: @エイリアス強調に使った SELECTION_FIND の選択範囲を消す。書式が適用されていなければ何もしない。
- 触るとき: エイリアス強調が消えない、または残るときに見る。
- 呼び出し先: `selection.removeAllRanges()`, `this.#urlbarInput.editor.selectionController.getSelection()`
- 参照: `Ci.nsISelectionController.SELECTION_FIND`, `this.#formattingApplied`
- XPCOM: [`nsISelectionController`](../../../dom/base/nsISelectionController.idl.md)

## UrlbarValueFormatter.#formatSearchAlias()
- 位置: L550-632
- 役割: 入力が @ で始まりボタン選択が無いとき、対象エイリアスを SELECTION_FIND で強調する。末尾の空白も含め、テーマやコントラスト設定に応じて前景色と背景色を決める。
- 触るとき: @エイリアスの見た目や配色、テーマ別の色の扱いを変えるときに見る。
- 呼び出し先: `editor.selectionController.getSelection()`, `range.setEnd()`, `range.setStart()`, `selection.addRange()`, `this.#document.createRange()`, `this.#document.documentElement.hasAttribute()`, `this.#findEngineAliasOrRestrictKeyword()`, `this.#window.matchMedia()`, `trimmedValue.startsWith()`, `value.indexOf()`, `value.trim()`
- 条件付き依存: `if ( this.#document.documentElement.hasAttribute("lwtheme") || this.#window.matchMedia("(prefers-contrast)").matches )` → `selection.setColors()`
- 条件付き依存: `if (!( this.#document.documentElement.hasAttribute("lwtheme") || this.#window.matchMedia("(prefers-contrast)").matches ))` → `selection.setColors()`
- 参照: `Ci.nsISelectionController.SELECTION_FIND`, `alias.length`, `editor.rootElement.firstChild`, `textNode.textContent`, `this.#urlbarInput.editor`, `this.#urlbarInput.view.oneOffSearchButtons.selectedButton`, `this.#window.matchMedia("(prefers-contrast)").matches`, `this.formattingEnabled`
- XPCOM: [`nsISelectionController`](../../../dom/base/nsISelectionController.idl.md)

## UrlbarValueFormatter.#findEngineAliasOrRestrictKeyword()
- 位置: L634-662
- 役割: 選択中の結果、無ければ先頭の結果、さらに前回の結果から、SEARCH の keyword か RESTRICT の autofillKeyword を取り出す。
- 触るとき: どの結果のエイリアスを強調するかの決め方を変えるときに見る。
- 呼び出し先: `this.#urlbarInput.view.getResultAtIndex()`
- 参照: `lazy.UrlbarShared.RESULT_TYPE.RESTRICT`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `payload.autofillKeyword`, `payload.keyword`, `this.#selectedResult`, `this.#urlbarInput.view.selectedResult`

## UrlbarValueFormatter.handleEvent()
- 位置: L670-677
- 役割: DOM イベントを _on_<type> メソッドへ振り分ける。対応メソッドが無いイベントは例外を投げる。
- 触るとき: フォーマッタが新しいイベントを購読するように変えるときに見る。
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.type`

## UrlbarValueFormatter._on_resize()
- 位置: L679-707
- 役割: resize 後 100ms 経ってから描画フレームで、ホスト範囲が切れていれば書式を付け直し、そうでなければ表示位置だけ合わせる。連続 resize は最後の一回にまとめる。
- 触るとき: リサイズ時にホストの表示位置が崩れる不具合を調べるときに見る。
- 呼び出し先: `this.#window.requestAnimationFrame()`, `this.#window.setTimeout()`
- 条件付き依存: `if (this.#resizeThrottleTimeout)` → `this.#window.clearTimeout()`
- 条件付き依存: `if ( this.#hostRange && !this.#hostRange.commonAncestorContainer.isConnected )` → `this.#removeURLFormat()`
- 条件付き依存: `if ( this.#hostRange && !this.#hostRange.commonAncestorContainer.isConnected )` → `this.#formatURL()`
- 条件付き依存: `if (!( this.#hostRange && !this.#hostRange.commonAncestorContainer.isConnected ))` → `this.#ensureFormattedHostVisible()`
- 参照: `event.target`, `this.#hostRange`, `this.#hostRange.commonAncestorContainer.isConnected`, `this.#resizeInstance`, `this.#resizeThrottleTimeout`, `this.#window`
