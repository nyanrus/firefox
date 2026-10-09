# browser/actors/LinkHandlerChild.sys.mjs

source: browser/actors/LinkHandlerChild.sys.mjs
source-hash: 387edd75a3accd9270ec02caa87c19f909b2096c
lines: 169

## <module>
- 役割: ページの link 要素を読み、タブのアイコンと検索エンジン追加の要求を親へ伝える子側アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## LinkHandlerChild.constructor()
- 位置: L12-17
- 役割: タブアイコン取得済みフラグとアイコンローダーの参照を初期化する。
- 触るとき: アイコン取得の状態管理を変えるとき。
- 呼び出し先: `super()`
- 参照: `this._iconLoader`, `this.seenTabIcon`

## LinkHandlerChild.iconLoader()
- 位置: L19-24
- 役割: 初めて使う時に FaviconLoader を作り、以後は同じものを返す。
- 触るとき: アイコン読み込みの生成条件を変えるとき。
- 参照: `lazy.FaviconLoader`, `this._iconLoader`

## LinkHandlerChild.addRootIcon()
- 位置: L26-40
- 役割: まだアイコンが無く設定が有効で http か https のページなら、ルートの既定アイコンを追加する。
- 触るとき: 既定アイコンの扱いを変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !this.seenTabIcon && Services.prefs.getBoolPref("browser.chrome.guess_favicon", true) && Services.prefs.getBoolPref("browser.chrome.site_icons", true) )` → `["http", "https"].includes()`
- 条件付き依存: `if (["http", "https"].includes(pageURI.scheme))` → `this.iconLoader.addDefaultIcon()`
- 参照: `pageURI.scheme`, `this.document.documentURIObject`, `this.seenTabIcon`
- XPCOM: `Services.prefs`

## LinkHandlerChild.onHeadParsed()
- 位置: L42-56
- 役割: 自分の文書の head 解析が終わったら既定アイコンを試し、保留中のアイコンを読み込む。
- 触るとき: アイコン読み込みの開始タイミングを変えるとき。
- 呼び出し先: `this.addRootIcon()`
- 条件付き依存: `if (this._iconLoader)` → `this._iconLoader.onPageShow()`
- 参照: `event.target.ownerDocument`, `this._iconLoader`, `this.document`

## LinkHandlerChild.onPageShow()
- 位置: L58-68
- 役割: 自分の文書の pageshow で既定アイコンを試し、保留中のアイコンを読み込む。
- 触るとき: ページ表示時のアイコン処理を変えるとき。
- 呼び出し先: `this.addRootIcon()`
- 条件付き依存: `if (this._iconLoader)` → `this._iconLoader.onPageShow()`
- 参照: `event.target`, `this._iconLoader`, `this.document`

## LinkHandlerChild.onPageHide()
- 位置: L70-80
- 役割: アイコン読み込みを止め、タブアイコン取得済みフラグを戻す。
- 触るとき: ページを離れた時の後始末を変えるとき。
- 条件付き依存: `if (this._iconLoader)` → `this._iconLoader.onPageHide()`
- 参照: `event.target`, `this._iconLoader`, `this.document`, `this.seenTabIcon`

## LinkHandlerChild.onLinkEvent()
- 位置: L82-154
- 役割: rel が icon 系ならアイコンを追加し、search の OpenSearch 定義なら Link:AddSearch を親へ送る。サブフレームは無視する。
- 触るとき: リンクからアイコンや検索エンジンを拾う条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `link.getAttribute()`, `link.hasAttribute()`, `link.rel.toLowerCase()`, `rel.includes()`, `rel.split()`, `this.iconLoader.addIconFromLink()`
- 条件付き依存: `if (!searchAdded && event.type == "DOMLinkAdded")` → `link.type.toLowerCase()`
- 条件付き依存: `if (!searchAdded && event.type == "DOMLinkAdded")` → `type.replace()`
- 条件付き依存: `if (!searchAdded && event.type == "DOMLinkAdded")` → `re.test()`
- 条件付き依存: `if ( type == "application/opensearchdescription+xml" && link.title && re.test(link.href) )` → `this.sendAsyncMessage()`
- 参照: `event.target`, `event.type`, `link.documentGlobal`, `link.href`, `link.rel`, `link.title`, `link.type`, `this.contentWindow`, `this.seenTabIcon`
- XPCOM: `Services.prefs`

## LinkHandlerChild.handleEvent()
- 位置: L156-167
- 役割: pageshow、pagehide、DOMHeadElementParsed を対応する処理へ振り分け、それ以外は link のイベントとして扱う。
- 触るとき: 受け取るイベントを増やすとき。
- 呼び出し先: `this.onHeadParsed()`, `this.onLinkEvent()`, `this.onPageHide()`, `this.onPageShow()`
- 参照: `event.type`
