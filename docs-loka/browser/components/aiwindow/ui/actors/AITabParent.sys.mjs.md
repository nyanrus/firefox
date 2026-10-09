# browser/components/aiwindow/ui/actors/AITabParent.sys.mjs

source: browser/components/aiwindow/ui/actors/AITabParent.sys.mjs
source-hash: 004540ea8ab2e28872785d6eaf99ef5cd71eb7f2
lines: 237

## <module>
- 役割: about:smartpage の親アクター。ページの取得、削除、リンクを開く処理を受け持つ。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## formatCreatedAt()
- 位置: L39-53
- 役割: 作成時刻(マイクロ秒)を、ローカル時刻で同じ日なら「今日」、それ以外は日付つきの文言に変える。日付として使えない値は空文字を返す。
- 触るとき: about:smartpage の作成日表示が日付の境目で「今日」にならない、または時刻の単位を変えるときに見る。now を渡せばテストで境界を固定できる。
- 呼び出し先: `Date.now()`, `Math.round()`, `Number.isNaN()`, `created.getTime()`, `created.toDateString()`, `created.valueOf()`, `lazy.fluentStrings.formatValueSync()`, `new Date(now).toDateString()`
- 条件付き依存: `if (created.toDateString() == new Date(now).toDateString())` → `lazy.fluentStrings.formatValueSync()`

## AITabParent.receiveMessage()
- 位置: async L61-74
- 役割: AITab:GetPage、AITab:DeletePage、AITab:OpenLink を対応する処理へ振り分ける。OpenLink は応答を返さず null を返す。未知の名前は警告を出す。
- 触るとき: about:smartpage に新しいメッセージを足すとき、または content から送った要求が親で処理されないときに見る。
- 呼び出し先: `console.warn()`, `this.#handleDeletePage()`, `this.#handleGetPage()`, `this.#handleOpenLink()`

## AITabParent.#pageName()
- 位置: L84-91
- 役割: タブの現在の URL から page 名を取り出す。content が送ってきた名前は使わない。
- 触るとき: 取得や削除が別のページに作用していないか確かめるとき、または about:smartpage の URL 形式を変えるときに見る。ここを content 由来の値に置き換えると、破壊的な操作が別ページに当たる。
- 呼び出し先: `URL.parse()`, `getSmartPageName()`
- 参照: `this.browsingContext?.currentURI?.spec`

## AITabParent.#handleGetPage()
- 位置: async L93-123
- 役割: slug で保存済みページを引き、A2UI の surface を UI 形式に変換して作成日ラベルを足して返す。surface が無ければ page: null を返す。
- 触るとき: about:smartpage の表示が空になる、または作成日ラベルが出ないときに見る。
- 呼び出し先: `AITabStore.getBySlug()`, `a2ui.toUI()`, `console.error()`, `formatCreatedAt()`
- 参照: `pageData.createdAt`, `pageData?.components?.surface`, `this.#pageName`

## AITabParent.#handleDeletePage()
- 位置: async L135-178
- 役割: slug でページを削除し、そのページの会話(toolConvId)も消す。会話の削除が失敗してもページ削除は成功扱いにする。最後に非同期でスマートウィンドウのホームへ戻す。
- 触るとき: ページ削除の順序や失敗時の扱いを変えるとき、またはページは消えたのに会話が残っていないか調べるときに見る。
- 呼び出し先: `AITabStore.getBySlug()`, `Services.tm.dispatchToMainThread()`, `console.error()`, `this.#returnToSmartWindowHome()`
- 条件付き依存: `if (page)` → `AITabStore.deleteBySlug()`
- 条件付き依存: `if (page.toolConvId)` → `ConversationStore.deleteConversationById()`
- 条件付き依存: `if (page.toolConvId)` → `console.error()`
- 参照: `page.slug`, `page.toolConvId`, `this.#pageName`
- XPCOM: `Services.tm`

## AITabParent.#handleOpenLink()
- 位置: L189-219
- 役割: http と https の URL だけを開く。指定があれば既存のタブへ切り替え、無ければ新しいタブで開く。null principal を使う。
- 触るとき: about:smartpage のリンクが開かないとき、または不正なスキームが通っていないか確かめるときに見る。AIChatContentParent と分けてあるのは、チャットの recordUriLoad 計測に混ざらないため。
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `URL.parse()`, `lazy.URILoadingHelper.openWebLinkIn()`, `lazy.URILoadingHelper.switchToTabHavingURI()`
- 参照: `this.browsingContext?.topChromeWindow`, `uri?.protocol`, `window.gBrowser.selectedBrowser.browsingContext.originAttributes`
- XPCOM: `Services.scriptSecurityManager`

## AITabParent.#returnToSmartWindowHome()
- 位置: L228-235
- 役割: タブのトップレベルを AIWINDOW_URL(chrome: のホーム)へ読み込み直す。
- 触るとき: 削除後の遷移先を変えるとき、または削除後に about:smartpage に留まるときに見る。content からは chrome: へ遷移できないため親で行う。
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `this.browsingContext?.loadURI()`
- 参照: `lazy.AIWINDOW_URL`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`
