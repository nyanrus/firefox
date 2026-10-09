# browser/components/urlbar/UrlbarUtils.sys.mjs

source: browser/components/urlbar/UrlbarUtils.sys.mjs
source-hash: 8757427707dcf6cf26d83d1b52055ddf3e0cea2b
lines: 2563

## <module>
- 役割: urlbar 全体で共有する定数と補助関数(URL 解析、入力履歴、autofill ブロック、フォーム履歴など)を UrlbarUtils にまとめ、プロバイダー・ミューザー・タイマー・タスクキューの基底クラスも置く。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Promise.resolve()`, `Services.strings.createBundle()`, `XPCOMUtils.declareLazy()`

## parseOriginParts()
- 位置: L73-79
- 役割: URL を解析して prefix(scheme と //)と host を返す。解析できなければ null。
- 触るとき: origin 単位の autofill ブロックや moz_origins の検索キーを変えるとき、解析失敗時の扱いを調べるときに見る。
- 呼び出し先: `URL.parse()`
- 参照: `parsed.host`, `parsed.protocol`

## getPayloadSchema()
- 位置: L88-90
- 役割: 結果の型に対応するペイロードスキーマを RESULT_PAYLOAD_SCHEMA から返す。
- 触るとき: 新しい結果型を追加してペイロードの検証内容を決めるときに見る。
- 参照: `this.RESULT_PAYLOAD_SCHEMA`

## addToUrlbarHistory()
- 位置: L99-109
- 役割: 非プライベートウィンドウで、空白や制御文字を含まない有効な URL を PlacesUIUtils.markPageAsTyped で入力済みとして記録する。
- 触るとき: 入力した URL が履歴の入力済み扱いにならない不具合を調べるときに見る。
- 呼び出し先: `/[\x00-\x1F]/.test()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `url.includes()`
- 条件付き依存: `if ( !lazy.PrivateBrowsingUtils.isWindowPrivate(window) && url && !url.includes(" ") && // eslint-disable-next-line no-control-regex !/[\x00-\x1F]/.test(url) )` → `lazy.PlacesUIUtils.markPageAsTyped()`

## getShortcutOrURIAndPostData()
- 位置: async L122-174
- 役割: 先頭の語が検索エンジンのエイリアスならその送信 URL を、Places のキーワードならブックマークの URL とパラメータを組み立てて返す。どちらでもなければ入力をそのまま返す。
- 触るとき: キーワードやエイリアスで検索・ブックマークを開く動作を変えるときに見る。
- 呼び出し先: `console.error()`, `lazy.KeywordUtils.parseUrlAndPostData()`, `lazy.PlacesUtils.keywords.fetch()`, `lazy.SearchService.getEngineByAlias()`, `url.trim()`, `url.trim().split()`
- 条件付き依存: `if (engine)` → `engine.getSubmission()`
- 条件付き依存: `if (postData)` → `this.getPostDataStream()`
- 参照: `entry.postData`, `entry.url`, `entry.url.href`, `submission.postData`, `submission.uri.spec`

## getPostDataStream()
- 位置: L183-198
- 役割: 文字列の POST データを MIME 入力ストリームに包む。Content-Type は既定で x-www-form-urlencoded。
- 触るとき: POST を伴う読み込みの実装を変えるときに見る。
- 呼び出し先: `Cc[ "@mozilla.org/network/mime-input-stream;1" ].createInstance()`, `Cc["@mozilla.org/io/string-input-stream;1"].createInstance()`, `dataStream.setByteStringData()`, `mimeStream.QueryInterface()`, `mimeStream.addHeader()`, `mimeStream.setData()`
- 参照: `Ci.nsIInputStream`, `Ci.nsIMIMEInputStream`, `Ci.nsIStringInputStream`
- XPCOM: [`nsIInputStream`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIMIMEInputStream`](../../../netwerk/base/nsIMIMEInputStream.idl.md) / [`nsIStringInputStream`](../../../xpcom/io/nsIStringStream.idl.md) / `@mozilla.org/io/string-input-stream;1` / `@mozilla.org/network/mime-input-stream;1`

## getPostDataString()
- 位置: L210-214
- 役割: getPostDataStream で包んだ MIME ストリームから元の文字列を取り出す。
- 触るとき: POST データを文字列へ戻す処理が壊れたときに見る。
- 呼び出し先: `postData .QueryInterface()`, `postData .QueryInterface(Ci.nsIMIMEInputStream) .data.QueryInterface()`
- 参照: `Ci.nsIMIMEInputStream`, `Ci.nsISupportsCString`, `postData .QueryInterface(Ci.nsIMIMEInputStream) .data.QueryInterface(Ci.nsISupportsCString).data`
- XPCOM: [`nsIMIMEInputStream`](../../../netwerk/base/nsIMIMEInputStream.idl.md) / [`nsISupportsCString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md)

## getUrlFromResult()
- 位置: L231-240
- 役割: 結果から読み込み要求(UrlbarLoadRequest)を取り出し、loadRequestToUrl で URL と POST データに変換する。
- 触るとき: 結果を選んだときに開く URL の決まり方を変えるときに見る。
- 呼び出し先: `UrlbarShared.getLoadRequestFromResult()`, `this.loadRequestToUrl()`

## loadRequestToUrl()
- 位置: L250-267
- 役割: 検索要求ならエンジン名から検索エンジンを引いて検索 URL を作り、そうでなければ要求の URL と POST データを返す。エンジンが無ければ url は null。
- 触るとき: 検索エンジン指定の読み込みが失敗する、またはエンジンの検索 URL が違うときに見る。
- 呼び出し先: `this.getPostDataStream()`
- 条件付き依存: `if (loadRequest.engineSearch)` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (loadRequest.engineSearch)` → `this.getSearchQueryUrl()`
- 参照: `loadRequest.engineSearch`, `loadRequest.urlLoad.postData`, `loadRequest.urlLoad.url`

## getSearchQueryUrl()
- 位置: L280-283
- 役割: 検索エンジンの getSubmission で検索 URL と POST データを作り、配列で返す。
- 触るとき: 検索語からの送信 URL を組み立てる箇所を追うときに見る。
- 呼び出し先: `engine.getSubmission()`
- 参照: `submission.postData`, `submission.uri.spec`

## getPrefixRank()
- 位置: L293-297
- 役割: URL の prefix を重複排除用の順位に変換する。https:// が最上位、http://www. が最下位で、一致しなければ -1。
- 触るとき: 同じ URL の http と https、www の有無の重複判定を変えるときに見る。
- 呼び出し先: `["http://www.", "http://", "https://www.", "https://"].indexOf()`

## getRemoteImageUrl()
- 位置: L322-349
- 役割: 信頼されないスキームの画像を、親プロセスでデコードしないよう remote image URL に変換する。コンテンツプロセスで描画する場合やスキームが信頼されている場合はそのまま返す。
- 触るとき: urlbar の画像がデコードされない、または remote 化されず読めないときに見る(bug 2012436 の経緯)。
- 呼び出し先: `URL.parse()`, `lazy.FaviconUtils.TRUSTED_FAVICON_SCHEMES.includes()`, `parsedUrl.protocol.slice()`
- 条件付き依存: `if ( !controller?.rendersInContentProcess && !lazy.FaviconUtils.TRUSTED_FAVICON_SCHEMES.includes(scheme) )` → `controller?.browserWindow?.matchMedia()`
- 条件付き依存: `if (size)` → `Math.floor()`
- 条件付き依存: `if ( !controller?.rendersInContentProcess && !lazy.FaviconUtils.TRUSTED_FAVICON_SCHEMES.includes(scheme) )` → `lazy.FaviconUtils.getMozRemoteImageURL()`
- 参照: `controller?.browserWindow?.devicePixelRatio`, `controller?.browserWindow?.matchMedia?.( "(prefers-color-scheme: dark)" ).matches`, `controller?.rendersInContentProcess`, `opts.size`

## getEngineIconUrl()
- 位置: async L365-390
- 役割: エンジンのアイコン URL を取得する。コンテンツプロセスで表示する場合、blob: や moz-extension: を fetch して data URL に変換し、URL 単位でキャッシュする。
- 触るとき: コンテンツプロセスの urlbar でエンジンアイコンが出ない問題を調べるときに見る。
- 呼び出し先: `/^(?:blob|moz-extension):/.test()`, `engine.getIconURL()`, `gEngineIconDataUrls.get()`
- 条件付き依存: `if (!dataUrl)` → `fetch()`
- 条件付き依存: `if (!dataUrl)` → `lazy.blobAsDataURL()`
- 条件付き依存: `if (!dataUrl)` → `response.blob()`
- 条件付き依存: `if (!dataUrl)` → `console.error()`
- 条件付き依存: `if (!dataUrl)` → `gEngineIconDataUrls.delete()`
- 条件付き依存: `if (!dataUrl)` → `gEngineIconDataUrls.set()`
- 参照: `controller?.rendersInContentProcess`, `engine.id`

## setupSpeculativeConnection()
- 位置: L403-437
- 役割: speculativeConnect.enabled が真のとき、エンジンか URL に対して投機的接続を張る。失敗は無視する。
- 触るとき: 検索候補の接続先を先読みする条件や対象を変えるときに見る。
- 呼び出し先: `Services.io.newURI()`, `Services.io.speculativeConnect()`, `URL.isInstance()`, `lazy.UrlbarPrefs.get()`, `window.docShell.QueryInterface()`
- 条件付き依存: `if (urlOrEngine instanceof lazy.SearchEngine)` → `urlOrEngine.speculativeConnect()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIURI`, `lazy.SearchEngine`, `urlOrEngine.href`, `window.gBrowser.contentPrincipal`, `window.gBrowser.contentPrincipal.originAttributes`
- XPCOM: [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## extractRefFromUrl()
- 位置: L449-455
- 役割: URL を fragment 抜きの base と ref に分ける。解析できなければ base に元の URL を入れて返す。
- 触るとき: URL の比較や重複判定で fragment の扱いがずれるときに見る。
- 呼び出し先: `URL.parse()`
- 参照: `URL.parse(url)?.URI`, `uri.ref`, `uri.specIgnoringRef`

## stripPublicSuffixFromHost()
- 位置: L467-479
- 役割: ホスト名から既知の公開サフィックス(PSL)を取り除く。IP アドレスはそのまま返す。
- 触るとき: ホスト名の表示用の短縮やドメイン比較を変えるときに見る(ホットパスでは使わない前提)。
- 呼び出し先: `Services.eTLD.getKnownPublicSuffixFromHost()`, `host.substring()`
- 参照: `Cr.NS_ERROR_HOST_IS_IP_ADDRESS`, `Services.eTLD.getKnownPublicSuffixFromHost(host).length`, `ex.result`, `host.length`
- XPCOM: `Services.eTLD`

## getURIFixupInfo()
- 位置: L491-507
- 役割: スキームの typo 修正とキーワード検索を有効にして URIFixup を呼ぶ。private 指定時は private context を付ける。例外時は null。
- 触るとき: 入力文字列を URL として解決する条件を変えるときに見る。
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `console.error()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`
- XPCOM: [`nsIURIFixup`](../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## getFixupPrimitives()
- 位置: L521-529
- 役割: URIFixup の結果から keywordAsSent と表示用 URL(preferredURI の displaySpec)だけを取り出す。
- 触るとき: UrlbarChild 越しに fixup 結果を渡す形式を変えるときに見る。
- 呼び出し先: `this.getURIFixupInfo()`
- 参照: `info.keywordAsSent`, `info.preferredURI?.displaySpec`

## addToInputHistory()
- 位置: async L541-568
- 役割: moz_inputhistory に (URL, 入力語) の行を追加または更新する。use_count は既存値に 0.9 を掛けて 1 を足す。URL が moz_places に無い、または履歴が無効なら false。
- 触るとき: アダプティブ履歴の学習量や減衰を変える、または学習されない不具合を調べるときに見る。
- 呼び出し先: `db.executeCached()`, `input.toLowerCase()`, `lazy.PlacesUtils.withConnectionWrapper()`
- 参照: `lazy.historyEnabled`, `rows.length`

## addToInputHistoryWhenReady()
- 位置: async L578-616
- 役割: まず addToInputHistory を試し、失敗したら page-visited の通知を最大 1000ms 待ち、訪問後に再度書き込む。
- 触るとき: 訪問直後の URL で入力履歴が落ちる競合を調べるときに見る。
- 呼び出し先: `PlacesObservers.addListener()`, `PlacesObservers.removeListener()`, `Promise.withResolvers()`, `lazy.clearTimeout()`, `lazy.setTimeout()`, `this.addToInputHistory()`, `visitedResolve()`
- 条件付き依存: `if (await this.addToInputHistory(url, input))` → `PlacesObservers.removeListener()`
- 条件付き依存: `if (await this.addToInputHistory(url, input))` → `lazy.clearTimeout()`
- 条件付き依存: `if (visited)` → `this.addToInputHistory()`
- 参照: `lazy.historyEnabled`

## listener()
- 位置: L586-594
- 役割: page-visited 通知の中で対象 URL の訪問を見つけたら、リスナーを外して待機を解決する。
- 触るとき: 訪問通知の待機の仕組みを変えるときに見る。
- 条件付き依存: `if (event.type == "page-visited" && event.url == url)` → `PlacesObservers.removeListener()`
- 条件付き依存: `if (event.type == "page-visited" && event.url == url)` → `visitedResolve()`
- 参照: `event.type`, `event.url`

## removeInputHistory()
- 位置: async L627-639
- 役割: 入力語で始まる moz_inputhistory の行を、指定 URL の place から削除する。
- 触るとき: アダプティブ履歴から特定の候補を消す動作を調べるときに見る。
- 呼び出し先: `db.executeCached()`, `input.toLowerCase()`, `lazy.PlacesUtils.withConnectionWrapper()`

## blockAutofill()
- 位置: async L651-657
- 役割: URL が origin なら blockOriginAutofill、そうでなければ blockOriginPageAutofill に振り分けて autofill を一時停止する。
- 触るとき: autofill の停止対象を origin とページのどちらにするか変えるときに見る。
- 呼び出し先: `UrlbarShared.isOriginUrl()`
- 条件付き依存: `if (UrlbarShared.isOriginUrl(url))` → `this.blockOriginAutofill()`
- 条件付き依存: `if (!(UrlbarShared.isOriginUrl(url)))` → `this.blockOriginPageAutofill()`

## blockOriginAutofill()
- 位置: async L673-692
- 役割: www の有無と http/https の組み合わせを含む moz_origins の行の block_until_ms を指定時刻まで設定する。URL が解析できなければ何もしない。
- 触るとき: origin 単位の autofill 停止が効かない、または範囲がずれるときに見る。
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `origin.host.replace()`, `parseOriginParts()`

## blockOriginPageAutofill()
- 位置: async L707-729
- 役割: 同じ origin の組み合わせについて moz_origins の block_pages_until_ms を設定し、ページ単位の autofill を止める。
- 触るとき: ページ単位の autofill 停止の範囲や期限を変えるときに見る。
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `origin.host.replace()`, `parseOriginParts()`

## clearOriginAutofillBlock()
- 位置: async L747-772
- 役割: 同じ origin の組み合わせで block_until_ms が設定された行を NULL に戻す。消した行があれば true。
- 触るとき: origin 単位の autofill 停止を解除する経路を追うときに見る。
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `origin.host.replace()`, `parseOriginParts()`
- 参照: `rows.length`

## clearOriginPageAutofillBlock()
- 位置: async L788-813
- 役割: 同じ origin の組み合わせで block_pages_until_ms を NULL に戻す。消した行があれば true。
- 触るとき: ページ単位の autofill 停止の解除が効かないときに見る。
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `origin.host.replace()`, `parseOriginParts()`
- 参照: `rows.length`

## _backspaceBlockKey()
- 位置: L875-885
- 役割: URL から "scope:host" 形式のキーを作る。scope は origin か page、host は先頭の www. を除いたもの。解析できなければ null。
- 触るとき: バックスペース回数の管理キーの粒度を変えるときに見る。
- 呼び出し先: `UrlbarShared.isOriginUrl()`, `origin.host.replace()`, `parseOriginParts()`

## recordAutofillBackspace()
- 位置: L903-907
- 役割: _doRecordAutofillBackspace の Promise を保持しつつ呼び出す。テストが書き込み完了を待てるようにする。
- 触るとき: バックスペースによる autofill 停止の記録を非同期に待つ必要がある箇所を書くときに見る。
- 呼び出し先: `this._doRecordAutofillBackspace()`
- 参照: `this._lastRecordAutofillBackspacePromise`

## _doRecordAutofillBackspace()
- 位置: async L909-946
- 役割: キーごとにバックスペース回数を増やし、autoFill.backspaceThreshold に達したら autoFill.backspaceBlockDurationMs の間 autofill を止めて blockedAt を記録する。LRU で 512 件を超えた古い項目を捨てる。
- 触るとき: 何回のバックスペースで autofill を止めるか、停止期間や件数上限を変えるときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._backspaceBlockKey()`, `this._backspaceBlocks.delete()`, `this._backspaceBlocks.get()`, `this._backspaceBlocks.set()`
- 条件付き依存: `if (newCount >= lazy.UrlbarPrefs.get("autoFill.backspaceThreshold"))` → `Date.now()`
- 条件付き依存: `if (newCount >= lazy.UrlbarPrefs.get("autoFill.backspaceThreshold"))` → `this.blockAutofill( url, Date.now() + lazy.UrlbarPrefs.get("autoFill.backspaceBlockDurationMs") ).catch()`
- 条件付き依存: `if (newCount >= lazy.UrlbarPrefs.get("autoFill.backspaceThreshold"))` → `this.blockAutofill()`
- 条件付き依存: `if (newCount >= lazy.UrlbarPrefs.get("autoFill.backspaceThreshold"))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (this._backspaceBlocks.size > this._BACKSPACE_BLOCKS_MAX)` → `this._backspaceBlocks.keys().next()`
- 条件付き依存: `if (this._backspaceBlocks.size > this._BACKSPACE_BLOCKS_MAX)` → `this._backspaceBlocks.keys()`
- 条件付き依存: `if (this._backspaceBlocks.size > this._BACKSPACE_BLOCKS_MAX)` → `this._backspaceBlocks.delete()`
- 参照: `console.error`, `entry.blockedAt`, `entry.count`, `this._BACKSPACE_BLOCKS_MAX`, `this._backspaceBlocks.keys().next().value`, `this._backspaceBlocks.size`

## getBackspaceBlock()
- 位置: L962-982
- 役割: キーに記録された blockedAt を取り出して削除する。24 時間を超えて古ければ null を返す。
- 触るとき: 再統合のテレメトリで停止からの経過時間が取れない問題を調べるときに見る。
- 呼び出し先: `Date.now()`, `this._backspaceBlockKey()`, `this._backspaceBlocks.delete()`, `this._backspaceBlocks.get()`
- 参照: `entry.blockedAt`, `entry?.blockedAt`, `this._BACKSPACE_BLOCK_MAX_AGE_HOURS`

## clearAutofillBackspaceEntryForUrl()
- 位置: L990-995
- 役割: URL に対応するバックスペース記録(回数と blockedAt)を削除する。
- 触るとき: autofill を解除または無効化した後に記録が残る問題を調べるときに見る。
- 呼び出し先: `this._backspaceBlockKey()`
- 条件付き依存: `if (key)` → `this._backspaceBlocks.delete()`

## dismissAutofill()
- 位置: async L1011-1022
- 役割: removeFromHistory なら履歴から URL を削除し、そうでなければ autoFill.dismissalBlockDurationMs の間ブロックする。最後にバックスペース記録を消す。エラーは出力して握りつぶす。
- 触るとき: autofill 候補の「非表示」操作の挙動や停止期間を変えるときに見る。
- 呼び出し先: `this.clearAutofillBackspaceEntryForUrl()`
- 条件付き依存: `if (removeFromHistory)` → `lazy.PlacesUtils.history.remove(url).catch()`
- 条件付き依存: `if (removeFromHistory)` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (!(removeFromHistory))` → `this.blockAutofill( url, Date.now() + lazy.UrlbarPrefs.get("autoFill.dismissalBlockDurationMs") ).catch()`
- 条件付き依存: `if (!(removeFromHistory))` → `this.blockAutofill()`
- 条件付き依存: `if (!(removeFromHistory))` → `Date.now()`
- 条件付き依存: `if (!(removeFromHistory))` → `lazy.UrlbarPrefs.get()`
- 参照: `console.error`

## reintegrateAutofill()
- 位置: async L1036-1051
- 役割: ユーザーがブロック済みの URL に再訪した場合、DB のブロックを解除し、テレメトリ用に blockedAt を取り出し、回数記録も消す。結果として wasBlocked、level、backspaceBlock を返す。
- 触るとき: autofill の再統合テレメトリの値がずれるとき、または再訪でブロックが外れない問題を調べるときに見る。
- 呼び出し先: `UrlbarShared.isOriginUrl()`, `this.clearAutofillBackspaceEntryForUrl()`, `this.clearOriginAutofillBlock()`, `this.clearOriginPageAutofillBlock()`, `this.getBackspaceBlock()`

## isPersistedSearchTermsEnabled()
- 位置: L1058-1064
- 役割: showSearchTerms の feature gate と showSearchTerms.enabled が真で、search-container ウィジェットが配置されていないときに true を返す。
- 触るとき: 検索語の永続表示の出し分け条件を変えるときに見る。
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.getScotchBonnetPref()`

## substringAt()
- 位置: L1077-1080
- 役割: sourceStr の中で targetStr が最初に現れる位置から末尾までを返す。見つからなければ空文字。
- 触るとき: 検索語のハイライトや候補の切り出しで文字列を使うときに見る。
- 呼び出し先: `sourceStr.indexOf()`, `sourceStr.substr()`

## substringAfter()
- 位置: L1093-1096
- 役割: sourceStr の中で targetStr の直後から末尾までを返す。見つからなければ空文字。
- 触るとき: targetStr の後ろだけを使う切り出し処理を変えるときに見る。
- 呼び出し先: `sourceStr.indexOf()`, `sourceStr.substr()`
- 参照: `targetStr.length`

## stripURLPrefix()
- 位置: L1109-1129
- 役割: REGEXP_PREFIX に合う prefix を取り除き、[prefix, 残り] を返す。prefix の後が空白、または認識しない scheme(localhost:8888 など)の場合は ["", 元の文字列]。
- 触るとき: 入力の http:// などを無視して検索語として扱う条件を変えるときに見る。
- 呼び出し先: `UrlbarShared.PROTOCOLS_WITHOUT_AUTHORITY.includes()`, `lazy.UrlUtils.REGEXP_PREFIX.exec()`, `prefix.endsWith()`, `prefix.toLowerCase()`, `str.substring()`
- 参照: `prefix.length`, `str.length`

## addToFormHistory()
- 位置: async L1142-1162
- 役割: 値が空、プライベート、または SEARCH_HISTORY_MAX_VALUE_LENGTH を超える場合は何もせず、そうでなければ FormHistory に bump で追加する。
- 触るとき: 検索フォーム履歴に残す条件を変えるとき、履歴が増えない問題を調べるときに見る。
- 呼び出し先: `lazy.FormHistory.update()`
- 参照: `lazy.DEFAULT_FORM_HISTORY_PARAM`, `lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VALUE_LENGTH`, `value.length`

## clearFormHistory()
- 位置: L1169-1174
- 役割: 検索用フォーム履歴をすべて削除する。
- 触るとき: 履歴の消去操作がどの欄を消すかを確認するときに見る。
- 呼び出し先: `lazy.FormHistory.update()`
- 参照: `lazy.DEFAULT_FORM_HISTORY_PARAM`

## tupleString()
- 位置: L1184-1186
- 役割: 空でない引数を "|" で連結してキー文字列を作る。
- 触るとき: 複数の値を辞書キーにまとめる箇所を追うときに見る。
- 呼び出し先: `tokens.filter()`, `tokens.filter(t => t).join()`

## copySnakeKeysToCamel()
- 位置: L1201-1225
- 役割: オブジェクトを再帰的に走査し、snake_case のキーに対応する camelCase のキーを追加する。先頭のアンダースコアは保つ。overwrite が false で衝突すると例外。
- 触るとき: Places や Nimbus などの snake_case データを camelCase で参照させる箇所を変えるときに見る。
- 呼び出し先: `Object.entries()`, `key.match()`, `key.replace()`, `obj.hasOwnProperty()`, `p1.toUpperCase()`
- 条件付き依存: `if (match)` → `key.substring()`
- 条件付き依存: `if (value && typeof value == "object")` → `this.copySnakeKeysToCamel()`
- 参照: `match[0].length`

## createTabSwitchSecondaryAction()
- 位置: L1234-1257
- 役割: タブ切り替えのセカンダリアクションを作る。コンテナのアイデンティティがあればコンテナ名入りのラベルと色のクラスを付け、なければ通常のタブ切り替えラベルにする。
- 触るとき: タブ切り替えボタンの文言や色の出し分けを変えるときに見る。
- 呼び出し先: `lazy.ContextualIdentityService.getPublicIdentityFromId()`
- 条件付き依存: `if (identity)` → `lazy.ContextualIdentityService.getUserContextLabel( userContextId ).toLowerCase()`
- 条件付き依存: `if (identity)` → `lazy.ContextualIdentityService.getUserContextLabel()`
- 参照: `action.classList`, `action.l10nArgs`, `action.l10nId`, `identity.color`

## getUserContextData()
- 位置: L1270-1288
- 役割: タブのコンテナ ID を返す。公開アイデンティティがあれば、トリムしたラベル、色、アイコン URL を加える。
- 触るとき: コンテナ付きタブの表示データを結果に渡す形式を変えるときに見る。
- 呼び出し先: `lazy.ContextualIdentityService.getContainerIconURL()`, `lazy.ContextualIdentityService.getPublicIdentityFromId()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `lazy.ContextualIdentityService.getUserContextLabel( userContextId ).trim()`
- 参照: `identity.color`, `identity.icon`

## getURLBarForFocus()
- 位置: L1300-1314
- 役割: フォーカス対象の URL バーを返す。AI ウィンドウの没入表示なら smartbar、それ以外は gURLBar。
- 触るとき: AI ウィンドウでフォーカスが入力欄に行かない問題を調べるときに見る。
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `lazy.AIWindow.shouldUseImmersiveView()`
- 条件付き依存: `if ( lazy.AIWindow.isAIWindowActive(window) && lazy.AIWindow.shouldUseImmersiveView(window.gBrowser.currentURI) )` → `lazy.AIWindow.getSmartbarForWindow()`
- 参照: `window.gBrowser.currentURI`, `window.gURLBar`

## formatUnitConversionResult()
- 位置: L1322-1358
- 役割: 単位変換の結果を表示用の文字列にする。1e10 以上か 1e-5 以下(0 以外)は科学表記、1 以上は最大 15 有効桁、それ未満は 10 有効桁で、ロケールに従って整形する。
- 触るとき: 単位変換の表示桁数や表記を変えるとき、桁落ちや指数表記の不具合を調べるときに見る。
- 呼び出し先: `Math.abs()`
- 条件付き依存: `if (!( Math.abs(result) >= FULL_NUMBER_MAX_THRESHOLD || (Math.abs(result) <= FULL_NUMBER_MIN_THRESHOLD && result !== 0) ))` → `Math.abs()`
- 参照: `Intl.NumberFormat`, `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## UrlbarMuxer.name()
- 位置: L1897-1899
- 役割: ミューザーの一意な名前を返す。基底は "UrlbarMuxerBase" で、派生クラスは別名にする必要がある。
- 触るとき: 独自のミューザーを登録して、既存のものと名前が衝突しないようにするときに見る。

## UrlbarMuxer.sort()
- 位置: L1909-1911
- 役割: 抽象メソッド。派生クラスが未定義結果をクエリ文脈に沿って並べ替える。基底では例外を投げる。
- 触るとき: 結果の並び順のルールを独自に定めるミューザーを書くときに見る。

## logger()
- 位置: L1920-1920
- 役割: UrlbarProvider のロガーを遅延生成する。プレフィックスは Provider.<名前>。
- 触るとき: プロバイダーのログを追うとき、ログの接頭辞を変えたいときに見る。
- 呼び出し先: `UrlbarShared.getLogger()`
- 参照: `this.name`

## UrlbarProvider.logger()
- 位置: L1923-1925
- 役割: 遅延生成したプロバイダー用ロガーを返す。
- 触るとき: プロバイダーの派生クラスからログを出す箇所を書くときに見る。
- 参照: `this.#lazy.logger`

## UrlbarProvider.name()
- 位置: L1933-1935
- 役割: プロバイダーの名前を返す。既定ではクラス名。クエリ文脈でプロバイダーを絞り込むのに使う。
- 触るとき: プロバイダーを名前で指定する設定やテストを扱うときに見る。名前が重複すると後から登録されたものが優先される。
- 参照: `this.constructor.name`

## UrlbarProvider.type()
- 位置: L1943-1945
- 役割: 抽象ゲッター。プロバイダーの種類(PROVIDER_TYPE)を返す必要がある。基底では例外。
- 触るとき: 新しいプロバイダーを書いて種類を決めるときに見る。

## UrlbarProvider.tryMethod()
- 位置: L1974-1981
- 役割: 指定名のメソッドを try/catch で呼び、例外は console.error に出して undefined を返す。派生クラスは上書きしない前提。
- 触るとき: プロバイダーのメソッドが例外で止まる、または呼ばれていないと疑うときに見る。
- 呼び出し先: `console.error()`, `this[methodName]()`

## UrlbarProvider.isActive()
- 位置: async L1996-1998
- 役割: 抽象メソッド。このクエリでプロバイダーを起動するかを Promise<boolean> で返す。false ならクエリを始めない。
- 触るとき: 特定条件でだけプロバイダーを動かしたいとき、または動いていないプロバイダーを調べるときに見る。

## UrlbarProvider.getPriority()
- 位置: L2010-2013
- 役割: プロバイダーの優先度を数値で返す。既定は全員 0。最も高い優先度の有効なプロバイダーだけが startQuery を受ける。
- 触るとき: どのプロバイダーが検索を担当するかを変えるときに見る。

## UrlbarProvider.startQuery()
- 位置: L2030-2032
- 役割: 抽象メソッド。検索を開始し、結果を addCallback で追加する。完了を示す Promise を返すのが約束。
- 触るとき: 新しいプロバイダーで検索本体を実装するとき、結果が出ない問題を調べるときに見る。

## UrlbarProvider.cancelQuery()
- 位置: L2041-2043
- 役割: 実行中の検索を止める。既定では何もしない。
- 触るとき: 検索の取り消し時に後始末が必要なプロバイダーを書くときに見る。

## UrlbarProvider.onBeforeSelection()
- 位置: L2168-2168
- 役割: 結果が選ばれる前に呼ばれるフック。既定では何もしない。
- 触るとき: 選択前に結果を補うプロバイダーを書くとき、またはフックが呼ばれないと疑うときに見る。

## UrlbarProvider.onSelection()
- 位置: L2181-2181
- 役割: 結果が選択されたとき(ハイライト、クリック時は engagement の直前)に呼ばれるフック。既定では何もしない。
- 触るとき: 選択時の状態更新をプロバイダーに持たせるときに見る。

## UrlbarProvider.getViewTemplate()
- 位置: L2259-2261
- 役割: 動的結果型のビュー構造(ViewTemplate)を返す。既定は null。
- 触るとき: 動的結果の DOM をプロバイダーから定義するときに見る。

## UrlbarProvider.getViewUpdate()
- 位置: L2332-2334
- 役割: 動的結果のビューを更新する内容を返す。既定は null。名前付き要素ごとに属性、style、l10n などを指定する。
- 触るとき: 動的結果の表示をクエリ後に差し替えるときに見る。

## UrlbarProvider.getResultCommands()
- 位置: L2348-2350
- 役割: 結果のメニューに出すコマンドの一覧を返す。既定は null。
- 触るとき: 結果メニューに項目を足すプロバイダーを書くときに見る。

## UrlbarProvider.deferUserSelection()
- 位置: L2362-2364
- 役割: 最初の結果が来るまでユーザーの選択イベントを保留するかを返す。既定は false。
- 触るとき: 結果が揃う前の選択操作がずれるときに見る。

## SkippableTimer.constructor()
- 位置: L2396-2442
- 役割: 指定時間後に callback を呼ぶ nsITimer を作る。fire で即時実行、cancel で実行を取り消せる。
- 触るとき: 遅延表示の待ち時間を調整したり、ユーザー操作で待ちを飛ばす処理を書いたりするときに見る。
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `Promise.race()`, `Promise.race([timerPromise, firePromise]).then()`, `resolve()`, `this._log()`, `this._timer.initWithCallback()`
- 条件付き依存: `if (callback && !this._canceled)` → `callback()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `this._canceled`, `this._timer`, `this.done`, `this.fire`, `this.logger`, `this.name`, `this.promise`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## this.fire()
- 位置: async L2422-2433
- 役割: タイマーを止めて待機を即座に解決し、callback を即時実行させる。
- 触るとき: 待ち時間を省いて先に進める箇所の動きを調べるときに見る。
- 条件付き依存: `if (!this._canceled)` → `this._log()`
- 条件付き依存: `if (this._timer)` → `this._timer.cancel()`
- 条件付き依存: `if (this._timer)` → `resolve()`
- 参照: `this._canceled`, `this._timer`, `this.done`, `this.promise`

## SkippableTimer.cancel()
- 位置: async L2449-2455
- 役割: 取り消しフラグを立ててから fire する。このため callback は呼ばれない。
- 触るとき: 待ちをキャンセルして副作用を出さないようにする箇所を書くときに見る。
- 呼び出し先: `this.fire()`
- 条件付き依存: `if (this._timer)` → `this._log()`
- 参照: `this._canceled`, `this._timer`

## SkippableTimer._log()
- 位置: L2457-2465
- 役割: タイマー名付きのメッセージを logger.debug に出す。isError が真なら console.error にも出す。
- 触るとき: タイマーのログを増やす、またはタイムアウト時のエラー報告を変えるときに見る。
- 条件付き依存: `if (this.logger)` → `this.logger.debug()`
- 条件付き依存: `if (isError)` → `console.error()`
- 参照: `this.logger`, `this.name`

## TaskQueue.emptyPromise()
- 位置: L2479-2481
- 役割: キューが空になったときに解決される Promise を返す。空なら解決済みの Promise。
- 触るとき: キューの処理完了を待つ箇所を書くときに見る。
- 参照: `this.#emptyPromise`

## TaskQueue.queue()
- 位置: L2496-2505
- 役割: コールバックを末尾に積み、前の処理が終わったら順に await して実行する。空の状態から積んだ場合は処理を開始する。
- 触るとき: 同じリソースへのアクセスを直列化する箇所を書くときに見る。
- 呼び出し先: `this.#queue.push()`
- 条件付き依存: `if (this.#queue.length == 1)` → `Promise.withResolvers()`
- 条件付き依存: `if (this.#queue.length == 1)` → `this.#doNextTask()`
- 参照: `this.#emptyDeferred`, `this.#emptyDeferred.promise`, `this.#emptyPromise`, `this.#queue.length`

## TaskQueue.queueIdleCallback()
- 位置: L2517-2531
- 役割: コールバックを ChromeUtils.idleDispatch の中で実行するタスクとして queue に積む。
- 触るとき: 重い処理をアイドル時に回したいとき、またはアイドル実行されない問題を調べるときに見る。
- 呼び出し先: `ChromeUtils.idleDispatch()`, `callback()`, `console.error()`, `reject()`, `resolve()`, `this.queue()`

## TaskQueue.#doNextTask()
- 位置: async L2537-2557
- 役割: 先頭のタスクを await し、解決か拒否を伝えてから取り除き、キューが空になるまで再帰的に処理する。
- 触るとき: キューが止まる、または順序が崩れる不具合を調べるときに見る。
- 呼び出し先: `callback()`, `console.error()`, `reject()`, `resolve()`, `this.#doNextTask()`, `this.#queue.shift()`
- 条件付き依存: `if (!this.#queue.length)` → `this.#emptyDeferred.resolve()`
- 参照: `this.#emptyDeferred`, `this.#queue`, `this.#queue.length`
