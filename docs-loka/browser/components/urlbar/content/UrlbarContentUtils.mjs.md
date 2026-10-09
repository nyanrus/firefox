# browser/components/urlbar/content/UrlbarContentUtils.mjs

source: browser/components/urlbar/content/UrlbarContentUtils.mjs
source-hash: 27df028b09dbc0f471569096c41f7538f5ebed65
lines: 259

## <module>
- 役割: content 側(子プロセスを含む)から、特権側でしか得られない URL 処理やプラットフォーム情報などを取り出す UrlbarContentUtils を提供する。

## port()
- 位置: L41-43
- 役割: window に公開された UrlbarActorPort を返す。無ければ null を返し、呼び出し側は直接経路を使う。
- 触るとき: どの経路(actor 経由か直接か)で処理されるかを判定する箇所を追うとき。
- 参照: `globalThis.window?.UrlbarActorPort`

## UrlbarContentUtils.getPlatform()
- 位置: L63-78
- 役割: プラットフォーム名を初回に一度だけ取得してキャッシュする。ポートがあれば actor から、無ければ AppConstants から読む。
- 触るとき: OS 判定が必要な content 側の処理を書くとき、または取得元の違いを確認するとき。
- 呼び出し先: `port()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!(!port()))` → `port().getPlatform()`
- 条件付き依存: `if (!(!port()))` → `port()`
- 参照: `ChromeUtils.importESModule( "resource://gre/modules/AppConstants.sys.mjs" ).AppConstants.platform`

## UrlbarContentUtils.isWindowPrivate()
- 位置: L87-94
- 役割: ウィンドウがプライベートかどうかを、ポート経由または PrivateBrowsingUtils で判定する。
- 触るとき: プライベートウィンドウでの検索や表示の出し分けを変えるとき。
- 呼び出し先: `port()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule( "resource://gre/modules/PrivateBrowsingUtils.sys.mjs" ).PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`
- 参照: `port().isWindowPrivate`

## UrlbarContentUtils.getDisplaySpec()
- 位置: L104-113
- 役割: URL を表示用の IDN 対応形式に変換する。直接経路では解析に失敗すると null を返す。
- 触るとき: URL を画面に出す箇所で文字化けや解析失敗がないか調べるとき。
- 呼び出し先: `port()`, `port().getDisplaySpec()`
- 条件付き依存: `if (!port())` → `Services.io.newURI()`
- 参照: `Services.io.newURI(url).displaySpec`
- XPCOM: `Services.io`

## UrlbarContentUtils.unEscapeURIForUI()
- 位置: L123-128
- 役割: パーセントエンコードを表示用に戻す。偽装防止の処理は解除されない。
- 触るとき: URL の表示文字列をエスケープ解除する箇所を変えるとき。
- 呼び出し先: `port()`, `port().unEscapeURIForUI()`
- 条件付き依存: `if (!port())` → `Services.textToSubURI.unEscapeURIForUI()`
- XPCOM: `Services.textToSubURI`

## UrlbarContentUtils.getSupportUrl()
- 位置: L137-142
- 役割: SUMO のベース URL に指定トピックを連結してサポートページの URL を返す。
- 触るとき: ヘルプリンクの接続先を変えるとき。
- 呼び出し先: `port()`, `port().getSupportUrl()`
- 条件付き依存: `if (!port())` → `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## UrlbarContentUtils.getFixupPrimitives()
- 位置: L155-162
- 役割: 文字列に対する URI 修正の結果を、呼び出し側が扱える単純な形で返す。失敗時は null。
- 触るとき: 入力を URL として扱うか検索語として扱うかの判定を content 側で変えるとき。
- 呼び出し先: `port()`, `port().getFixupPrimitives()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule( "moz-src:///browser/components/urlbar/UrlbarUtils.sys.mjs" ).UrlbarUtils.getFixupPrimitives()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`

## UrlbarContentUtils.isTextDirectionRTL()
- 位置: L174-182
- 役割: 文字列が右から左に読むかを、ポート経由またはウィンドウの windowUtils で判定する。
- 触るとき: RTL 言語の表示方向を結果の描画で判定するとき。
- 呼び出し先: `port()`, `port().isTextDirectionRTL()`
- 条件付き依存: `if (!port())` → `win.windowUtils.getDirectionFromText()`
- 参照: `win.windowUtils.DIRECTION_RTL`

## UrlbarContentUtils.whereToOpenLink()
- 位置: L191-198
- 役割: イベントからリンクの開き先(現在のタブ、新規タブ、ウィンドウなど)を求める。
- 触るとき: クリックやキー操作による開き先の判定を変えるとき。
- 呼び出し先: `port()`, `port().whereToOpenLink()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule( "resource://gre/modules/BrowserUtils.sys.mjs" ).BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`

## UrlbarContentUtils.willLoadInBackground()
- 位置: L209-216
- 役割: 指定の開き先とパラメータで、リンクがバックグラウンドで読み込まれるかを判定する。
- 触るとき: 新規タブをフォーカスせず開く挙動を確認するとき。
- 呼び出し先: `port()`, `port().willLoadInBackground()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule( "resource://gre/modules/BrowserUtils.sys.mjs" ).BrowserUtils.willLoadInBackground()`
- 条件付き依存: `if (!port())` → `ChromeUtils.importESModule()`

## UrlbarContentUtils.getContainers()
- 位置: L225-244
- 役割: 公開されているコンテナー(コンテキスト識別子)の一覧を非同期で返す。ポートがあれば actor に問い合わせ、無ければ ContextualIdentityService から組み立てる。
- 触るとき: コンテナーのメニューに出す項目を変えるとき、または子プロセスで一覧が空になる問題を調べるとき。
- 呼び出し先: `ChromeUtils.importESModule()`, `ContextualIdentityService.getContainerColorCode()`, `ContextualIdentityService.getContainerIconURL()`, `ContextualIdentityService.getPublicIdentities()`, `ContextualIdentityService.getPublicIdentities().map()`, `ContextualIdentityService.getUserContextLabel()`, `Promise.resolve()`, `port()`
- 条件付き依存: `if (port())` → `port().sendQuery()`
- 条件付き依存: `if (port())` → `port()`
- 参照: `identity.color`, `identity.icon`, `identity.userContextId`

## UrlbarContentUtils.usesMessagePath()
- 位置: L251-257
- 役割: メッセージ経由の経路を使うかを判定する。ChromeUtils が無い realm、子プロセス、または ipc.chromeMessagePassing が有効なら真を返す。
- 触るとき: content から chrome への呼び出し経路を切り替える条件を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`
- XPCOM: `Services.appinfo`
