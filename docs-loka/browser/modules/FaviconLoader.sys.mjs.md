# browser/modules/FaviconLoader.sys.mjs

source: browser/modules/FaviconLoader.sys.mjs
source-hash: 6f6a5b456ae4910edabe6c0fa7dacbf60c0c92c9
lines: 760

## <module>
- 役割: ページのリンクアイコンを選んで読み込み、結果を親プロセスへ Link:* メッセージで渡す FaviconLoader を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Components.Constructor()`

## decodeImage()
- 位置: async L57-102
- 役割: ImageDecoder で画像を復号し、幅・高さが 2048 を超えるものを拒否して Blob と形式情報を返す。
- 触るとき: アイコンの最大サイズや復号の失敗条件を変えるとき、または大きすぎるアイコンが弾かれる理由を調べるときに見る。
- 呼び出し先: `Components.Exception()`, `decoder.decode()`, `image.allocationSize()`, `image.copyTo()`
- 条件付き依存: `if ( image.displayWidth > MAX_ICON_SIZE || image.displayHeight > MAX_ICON_SIZE )` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_FAILURE`, `image.displayHeight`, `image.displayWidth`, `image.format`, `result.image`

## convertImage()
- 位置: async L105-140
- 役割: ICO なら内包する各サイズで復号し、それ以外や単一サイズは decodeImage で 1 枚だけ復号する。
- 触るとき: ICO の複数サイズを個別に扱いたいとき、または画像変換の結果の並びを調べるときに見る。
- 呼び出し先: `decodeImage()`
- 条件付き依存: `if (type == TYPE_ICO)` → `decoder.tracks[0].getSizes()`
- 条件付き依存: `if (sizes.length > 1)` → `Promise.all()`
- 条件付き依存: `if (sizes.length > 1)` → `sizes.map()`
- 条件付き依存: `if (sizes.length > 1)` → `decodeImage()`
- 参照: `decoder.tracks`, `decoder.tracks.ready`, `sizes.length`

## FaviconLoad.constructor()
- 位置: L143-210
- 役割: アイコン URI から、cross-origin 属性に応じたセキュリティフラグ付きのチャンネルを作り、リファラーと読み込みフラグを設定する。
- 触るとき: アイコン取得時の CORS・Cookie・キャッシュの扱いを変えるとき、または取得に失敗する原因を調べるときに見る。
- 呼び出し先: `Services.io.newChannelFromURI()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (this.channel instanceof Ci.nsIHttpChannel)` → `this.channel.QueryInterface()`
- 条件付き依存: `if (this.channel instanceof Ci.nsIHttpChannel)` → `Cc["@mozilla.org/referrer-info;1"].createInstance()`
- 条件付き依存: `if (iconInfo.node.nodeType == iconInfo.node.DOCUMENT_NODE)` → `referrerInfo.initWithDocument()`
- 条件付き依存: `if (!(iconInfo.node.nodeType == iconInfo.node.DOCUMENT_NODE))` → `referrerInfo.initWithElement()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("network.http.tailing.enabled", true) && this.channel instanceof Ci.nsIClassOfService )` → `this.channel.addClassFlags()`
- 参照: `Ci.nsIClassOfService`, `Ci.nsIClassOfService.Tail`, `Ci.nsIClassOfService.Throttleable`, `Ci.nsIContentPolicy.TYPE_INTERNAL_IMAGE_FAVICON`, `Ci.nsIHttpChannel`, `Ci.nsIHttpChannelInternal`, `Ci.nsILoadInfo.SEC_ALLOW_CHROME`, `Ci.nsILoadInfo.SEC_ALLOW_CROSS_ORIGIN_INHERITS_SEC_CONTEXT`, `Ci.nsILoadInfo.SEC_COOKIES_INCLUDE`, `Ci.nsILoadInfo.SEC_DISALLOW_SCRIPT`, `Ci.nsILoadInfo.SEC_REQUIRE_CORS_INHERITS_SEC_CONTEXT`, `Ci.nsIReferrerInfo`, `Ci.nsIRequest.LOAD_BACKGROUND`, `Ci.nsIRequest.LOAD_BYPASS_CACHE`, `Ci.nsIRequest.LOAD_FROM_CACHE`, `Ci.nsIRequest.VALIDATE_NEVER`, `iconInfo.iconUri`, `iconInfo.isForceReload`, `iconInfo.node`, `iconInfo.node.DOCUMENT_NODE`, `iconInfo.node.crossOrigin`, `iconInfo.node.documentGlobal.document.documentLoadGroup`, `iconInfo.node.nodePrincipal`, `iconInfo.node.nodeType`, `this.channel`, `this.channel.blockAuthPrompt`, `this.channel.loadFlags`, `this.channel.loadGroup`, `this.channel.notificationCallbacks`, `this.channel.referrerInfo`, `this.icon`
- XPCOM: [`nsIClassOfService`](../../netwerk/base/nsIClassOfService.idl.md) / [`nsIContentPolicy`](../../dom/base/nsIContentPolicy.idl.md) / [`nsIHttpChannel`](../../netwerk/protocol/http/nsIHttpChannel.idl.md) / [`nsIHttpChannelInternal`](../../netwerk/protocol/http/nsIHttpChannelInternal.idl.md) / [`nsILoadInfo`](../../dom/base/nsIContentPolicy.idl.md) / [`nsIReferrerInfo`](../../docshell/shistory/nsISHEntry.idl.md) / [`nsIRequest`](../../docshell/base/nsIDocShell.idl.md) / `@mozilla.org/referrer-info;1` / `Services.io` / `Services.prefs`

## FaviconLoad.load()
- 位置: L212-238
- 役割: ストレージストリームを用意し、チャンネルを非同期に開いて結果の Promise を返す。
- 触るとき: アイコンの取得開始処理を追うときや、開始時の例外の扱いを変えるときに見る。
- 呼び出し先: `Promise.withResolvers()`, `this._deferred.promise.then()`, `this._deferred.reject()`, `this.channel.asyncOpen()`, `this.dataBuffer.getOutputStream()`
- 参照: `this._deferred`, `this._deferred.promise`, `this.dataBuffer`, `this.stream`

## cleanup()
- 位置: L216-220
- 役割: Promise の完了時にチャンネル・データバッファ・ストリームの参照を外す。
- 触るとき: 読み込み後にメモリが解放されないとき、または完了後に参照されて失敗するときに見る。
- 参照: `this.channel`, `this.dataBuffer`, `this.stream`

## FaviconLoad.cancel()
- 位置: L240-246
- 役割: チャンネルが残っていれば NS_BINDING_ABORTED でキャンセルする。
- 触るとき: ページ遷移などで読み込みを中止する経路を追うときに見る。
- 呼び出し先: `this.channel.cancel()`
- 参照: `Cr.NS_BINDING_ABORTED`, `this.channel`

## FaviconLoad.onStartRequest()
- 位置: L248-248
- 役割: 開始時には何もしない空のハンドラ。
- 触るとき: 読み込み開始時に処理を足したくなったときに見る。

## FaviconLoad.onDataAvailable()
- 位置: L250-252
- 役割: 受信したデータをバッファ付きの出力ストリームに書き込む。
- 触るとき: 取得データの蓄積方法やサイズの扱いを変えるときに見る。
- 呼び出し先: `this.stream.writeFrom()`

## FaviconLoad.asyncOnChannelRedirect()
- 位置: L254-260
- 役割: リダイレクト時に監視中のチャンネルを新しいチャンネルへ差し替え、リダイレクトを許可する。
- 触るとき: リダイレクト先のアイコンが取れない、または旧チャンネルの結果を無視する仕組みを調べるときに見る。
- 呼び出し先: `callback.onRedirectVerifyCallback()`
- 参照: `Cr.NS_OK`, `this.channel`

## FaviconLoad.onStopRequest()
- 位置: async L262-383
- 役割: 取得の終了時にエラーを判定し、キャッシュ不可か確かめ、MIME を内容から判定して画像を変換し、結果を resolve する(失敗時は reject)。
- 触るとき: アイコンが保存されない、キャッシュ期限が効かない、または形式判定で失敗するときに見る。
- 呼び出し先: `Components.isSuccessCode()`, `Date.now()`, `stream.readArrayBuffer()`, `this._deferred.reject()`, `this._deferred.resolve()`, `this.dataBuffer.newInputStream()`, `this.stream.close()`
- 条件付き依存: `if (statusCode == Cr.NS_BINDING_ABORTED)` → `this._deferred.reject()`
- 条件付き依存: `if (statusCode == Cr.NS_BINDING_ABORTED)` → `Components.Exception()`
- 条件付き依存: `if (!(statusCode == Cr.NS_BINDING_ABORTED))` → `this._deferred.reject()`
- 条件付き依存: `if (!(statusCode == Cr.NS_BINDING_ABORTED))` → `Components.Exception()`
- 条件付き依存: `if (!this.channel.requestSucceeded)` → `this._deferred.reject()`
- 条件付き依存: `if (!this.channel.requestSucceeded)` → `Components.Exception()`
- 条件付き依存: `if (!(this.icon.iconUri.filePath == "/favicon.ico"))` → `this.channel.isNoStoreResponse()`
- 条件付き依存: `if (this.channel instanceof Ci.nsICacheInfoChannel)` → `Math.min()`
- 条件付き依存: `if (type != "image/svg+xml")` → `Cc["@mozilla.org/image/loader;1"].createInstance()`
- 条件付き依存: `if (type != "image/svg+xml")` → `sniffer.getMIMETypeFromContent()`
- 条件付き依存: `if (!type)` → `Components.Exception()`
- 条件付き依存: `if (type != "image/svg+xml")` → `convertImage()`
- 条件付き依存: `if (!(type != "image/svg+xml"))` → `blobAsDataURL()`
- 参照: `Ci.nsICacheInfoChannel`, `Ci.nsIContentSniffer`, `Ci.nsIHttpChannel`, `Cr.NS_BINDING_ABORTED`, `Cr.NS_ERROR_FAILURE`, `Cr.NS_ERROR_NOT_AVAILABLE`, `buffer.byteLength`, `ex.result`, `octets.length`, `this.channel`, `this.channel.cacheTokenExpirationTime`, `this.channel.contentType`, `this.channel.requestSucceeded`, `this.channel.responseStatus`, `this.channel.responseStatusText`, `this.dataBuffer.length`, `this.icon.beforePageShow`, `this.icon.iconUri.filePath`, `this.icon.iconUri.spec`, `this.stream`
- XPCOM: [`nsICacheInfoChannel`](../../netwerk/base/nsICacheInfoChannel.idl.md) / [`nsIContentSniffer`](../../netwerk/base/nsIContentSniffer.idl.md) / [`nsIHttpChannel`](../../netwerk/protocol/http/nsIHttpChannel.idl.md) / `@mozilla.org/image/loader;1` → `imgLoader` (image/build/components.conf)

## FaviconLoad.getInterface()
- 位置: L385-390
- 役割: nsIChannelEventSink を自身で応答し、それ以外の interface は NO_INTERFACE を返す。
- 触るとき: リダイレクト通知の受け口を変えるとき、またはチャンネルの要求する interface を追加したいときに見る。
- 呼び出し先: `Components.Exception()`, `iid.equals()`
- 参照: `Ci.nsIChannelEventSink`, `Cr.NS_ERROR_NO_INTERFACE`
- XPCOM: [`nsIChannelEventSink`](../../netwerk/base/nsIChannelEventSink.idl.md)

## extractIconSize()
- 位置: L400-434
- 役割: sizes 属性から幅を取り出し、属性の種別と幅を Glean の telemetry に記録する。
- 触るとき: sizes 属性の解析や telemetry の項目を変えるとき、またはアイコン幅が -1 になる理由を調べるときに見る。
- 呼び出し先: `Glean.linkIconSizesAttr.usage.accumulateSingleSample()`
- 条件付き依存: `if (aSizes.length)` → `size.toLowerCase()`
- 条件付き依存: `if (!(size.toLowerCase() == "any"))` → `re.exec()`
- 条件付き依存: `if (values && values.length > 1)` → `parseInt()`
- 条件付き依存: `if (width > 0)` → `Glean.linkIconSizesAttr.dimension.accumulateSingleSample()`
- 参照: `SIZES_TELEMETRY_ENUM.ANY`, `SIZES_TELEMETRY_ENUM.DIMENSION`, `SIZES_TELEMETRY_ENUM.INVALID`, `SIZES_TELEMETRY_ENUM.NO_SIZES`, `aSizes.length`, `values.length`

## getLinkIconURI()
- 位置: L442-451
- 役割: link の href を URI にし、可能なら userinfo を除いた URI を返す。
- 触るとき: アイコン URL の正規化を変えるとき、またはユーザー情報付き URL の扱いを確かめるときに見る。
- 呼び出し先: `Services.io.newURI()`, `uri.mutate()`, `uri.mutate().setUserPass()`, `uri.mutate().setUserPass("").finalize()`
- 参照: `aLink.href`, `aLink.ownerDocument`, `targetDoc.characterSet`
- XPCOM: `Services.io`

## guessType()
- 位置: L456-475
- 役割: 宣言された type がなければ拡張子で ico・svg を推定し、microsoft の icon 型は ICO とみなして、それ以外は宣言された型を返す。
- 触るとき: アイコンの形式判定を増やすとき、または SVG や ICO が別形式として扱われる原因を調べるときに見る。
- 条件付き依存: `if (!icon.type)` → `icon.iconUri.filePath.split(".").pop()`
- 条件付き依存: `if (!icon.type)` → `icon.iconUri.filePath.split()`
- 参照: `icon.type`

## selectIcons()
- 位置: L483-559
- 役割: rich でないアイコンから SVG 優先、次に preferredWidth 一致、ICO の順で tabIcon 候補を選び、96px 以上などを richIcon の候補とする。tabIcon は preferredIcon、bestSizedIcon、defaultIcon の順で決める。
- 触るとき: タブに表示されるアイコンの選定基準を変えるとき、または期待と違うアイコンが選ばれる理由を調べるときに見る。
- 条件付き依存: `if (!icon.isRichIcon)` → `guessType()`
- 条件付き依存: `if (!(guessType(icon) == TYPE_SVG))` → `guessType()`
- 条件付き依存: `if (!( icon.width == preferredWidth && guessType(preferredIcon) != TYPE_SVG ))` → `guessType()`
- 参照: `bestSizedIcon.width`, `icon.isRichIcon`, `icon.width`, `iconInfos.length`, `largestRichIcon.width`

## IconLoader.constructor()
- 位置: L562-564
- 役割: アイコンを送る先のアクターを保持する。
- 触るとき: アイコン読み込みの送信先を変えるときに見る。
- 参照: `this.actor`

## IconLoader.load()
- 位置: async L566-634
- 役割: 信頼されたスキームなら権限を検査してそのまま Link:SetIcon を送る。それ以外は Link:LoadingIcon を送ってから取得し、成功で Link:SetIcon、失敗で Link:SetFailedIcon を送る。同じ URL の読み込み中なら何もしない。
- 触るとき: タブのアイコンが更新されない、または失敗時のメッセージが届かないときに見る。
- 呼び出し先: `TRUSTED_FAVICON_SCHEMES.includes()`, `this._loader.load()`, `this.actor.sendAsyncMessage()`
- 条件付き依存: `if (this._loader)` → `this._loader.icon.iconUri.equals()`
- 条件付き依存: `if (this._loader)` → `this._loader.cancel()`
- 条件付き依存: `if (TRUSTED_FAVICON_SCHEMES.includes(iconInfo.iconUri.scheme))` → `Services.scriptSecurityManager.checkLoadURIWithPrincipal()`
- 条件付き依存: `if (TRUSTED_FAVICON_SCHEMES.includes(iconInfo.iconUri.scheme))` → `this.actor.sendAsyncMessage()`
- 条件付き依存: `if (TRUSTED_FAVICON_SCHEMES.includes(iconInfo.iconUri.scheme))` → `iconInfo.iconUri.schemeIs()`
- 条件付き依存: `if (typeof e.data?.wrappedJSObject?.httpStatus !== "number")` → `console.error()`
- 条件付き依存: `if (e.result != Cr.NS_BINDING_ABORTED)` → `this.actor.sendAsyncMessage()`
- 参照: `Cr.NS_BINDING_ABORTED`, `Services.scriptSecurityManager.ALLOW_CHROME`, `e.data?.wrappedJSObject?.httpStatus`, `e.result`, `iconInfo.beforePageShow`, `iconInfo.iconUri`, `iconInfo.iconUri.scheme`, `iconInfo.iconUri.spec`, `iconInfo.isRichIcon`, `iconInfo.node.nodePrincipal`, `this._loader`
- XPCOM: `Services.scriptSecurityManager`

## IconLoader.cancel()
- 位置: L636-643
- 役割: 読み込み中のアイコンがあればキャンセルして参照を外す。
- 触るとき: ページ離脱時に古いアイコンの読み込みを止める処理を確かめるときに見る。
- 呼び出し先: `this._loader.cancel()`
- 参照: `this._loader`

## FaviconLoader.constructor()
- 位置: L647-667
- 役割: アイコン候補の配列、起動前フラグ、リッチ用とタブ用の IconLoader、100ms(最大待機 3000ms)の DeferredTask を用意する。
- 触るとき: アイコン収集の待ち時間や初期状態を変えるとき、または DeferredTask の待機上限を調べるときに見る。
- 呼び出し先: `this.loadIcons()`
- 参照: `lazy.DeferredTask`, `this.actor`, `this.beforePageShow`, `this.iconInfos`, `this.iconTask`, `this.richIconLoader`, `this.tabIconLoader`

## FaviconLoader.loadIcons()
- 位置: L669-698
- 役割: devicePixelRatio から希望幅(16 の倍数)を求め、selectIcons で選んだアイコンを IconLoader に渡す。強制再読み込みなら Link:ExpireFavicons を先に送る。
- 触るとき: ページ読み込み中のアイコン選択の実行タイミングや強制再読み込み時の挙動を変えるときに見る。
- 呼び出し先: `Math.ceil()`, `selectIcons()`
- 条件付き依存: `if (isForceReload && (richIcon || tabIcon))` → `this.actor.sendAsyncMessage()`
- 条件付き依存: `if (richIcon)` → `this.richIconLoader.load(richIcon).catch()`
- 条件付き依存: `if (richIcon)` → `this.richIconLoader.load()`
- 条件付き依存: `if (tabIcon)` → `this.tabIconLoader.load(tabIcon).catch()`
- 条件付き依存: `if (tabIcon)` → `this.tabIconLoader.load()`
- 参照: `console.error`, `richIcon.isForceReload`, `tabIcon.isForceReload`, `this.actor.contentWindow.devicePixelRatio`, `this.actor.docShell?.isForceReloading`, `this.beforePageShow`, `this.iconInfos`, `this.iconInfos.length`

## FaviconLoader.addIconFromLink()
- 位置: L700-709
- 役割: link から iconInfo を作って候補に加え、タスクを arm する。作れなければ false を返す。
- 触るとき: 新しい種類のリンク要素をアイコン候補として扱うときに見る。
- 呼び出し先: `makeFaviconFromLink()`
- 条件付き依存: `if (iconInfo)` → `this.iconInfos.push()`
- 条件付き依存: `if (iconInfo)` → `this.iconTask.arm()`
- 参照: `iconInfo.beforePageShow`, `this.beforePageShow`

## FaviconLoader.addDefaultIcon()
- 位置: L711-723
- 役割: ページの /favicon.ico を ICO 型・幅 -1 の候補として加え、タスクを arm する。
- 触るとき: リンクがないページで既定アイコンを読むかどうかを変えるときに見る。
- 呼び出し先: `pageUri.mutate()`, `pageUri.mutate().setPathQueryRef()`, `pageUri.mutate().setPathQueryRef("/favicon.ico").finalize()`, `this.iconInfos.push()`, `this.iconTask.arm()`
- 参照: `this.actor.document`, `this.beforePageShow`

## FaviconLoader.onPageShow()
- 位置: L725-732
- 役割: 待機中の候補があれば即座に loadIcons を実行し、以後の候補を起動後扱いにする(beforePageShow を false にする)。
- 触るとき: pageshow 以降に追加されたアイコンを保存しない理由を追うとき、または読み込みの開始タイミングを変えるときに見る。
- 条件付き依存: `if (this.iconTask.isArmed)` → `this.iconTask.disarm()`
- 条件付き依存: `if (this.iconTask.isArmed)` → `this.loadIcons()`
- 参照: `this.beforePageShow`, `this.iconTask.isArmed`

## FaviconLoader.onPageHide()
- 位置: L734-740
- 役割: 両方の IconLoader を cancel し、タスクを disarm して候補を空にする。
- 触るとき: ページを離れたときに読み込みが残る、または候補が次のページへ混ざるときに見る。
- 呼び出し先: `this.iconTask.disarm()`, `this.richIconLoader.cancel()`, `this.tabIconLoader.cancel()`
- 参照: `this.iconInfos`

## makeFaviconFromLink()
- 位置: L743-759
- 役割: link から URI を取り、取れなければ null を返す。取れれば sizes から幅を求め、アイコン情報のオブジェクトを作る。
- 触るとき: アイコン情報に含める項目を増やすときや、link から候補が作られない理由を調べるときに見る。
- 呼び出し先: `extractIconSize()`, `getLinkIconURI()`
- 参照: `aLink.sizes`, `aLink.type`
