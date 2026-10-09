# browser/actors/PageStyleChild.sys.mjs

source: browser/actors/PageStyleChild.sys.mjs
source-hash: 3970d010b05abff61aad4fa325c0931491e6ec82
lines: 200

## <module>
- 役割: ページのスタイルシートの一覧を親へ送り、親からの代替スタイル切り替えや No Style を適用する子側アクター。

## PageStyleChild.actorCreated()
- 位置: L6-23
- 役割: 読み込みが完了していればスタイルシート一覧を送る。未完了なら pageshow を待つ。
- 触るとき: 一覧の送信タイミングを変えるとき。
- 呼び出し先: `this.#collectAndSendSheets()`
- 参照: `document.readyState`, `this.browsingContext`, `this.browsingContext.associatedWindow`

## PageStyleChild.handleEvent()
- 位置: L25-38
- 役割: pageshow の時に、トップ文書なら前ページの情報を消す指示を送ってから一覧を送る。pageshow 以外は例外にする。
- 触るとき: ページ表示時のスタイル情報の再送を変えるとき。
- 呼び出し先: `this.#collectAndSendSheets()`
- 条件付き依存: `if (this.browsingContext.top === this.browsingContext)` → `this.sendAsyncMessage()`
- 参照: `event?.type`, `this.browsingContext`, `this.browsingContext.top`

## PageStyleChild.receiveMessage()
- 位置: L40-58
- 役割: Switch では既定の無効化を解いて指定タイトルのシートを有効にし、Disable では文書のスタイルを全体で無効にする。
- 触るとき: No Style と代替スタイルの切り替えを変えるとき。
- 呼び出し先: `this._switchStylesheet()`
- 参照: `msg.data.title`, `msg.name`, `this.browsingContext`, `this.browsingContext.authorStyleDisabledDefault`, `this.browsingContext.top`, `this.docShell.docViewer.authorStyleDisabled`

## PageStyleChild._collectLinks()
- 位置: L63-81
- 役割: XHTML の link のうち rel に stylesheet を含み href を持つものを集める。
- 触るとき: link 形式のスタイルシートの拾い方を変えるとき。
- 呼び出し先: `Array.from()`, `Array.from(link.relList).some()`, `document.querySelectorAll()`, `r.toLowerCase()`, `result.push()`
- 参照: `link.href`, `link.namespaceURI`, `link.relList`

## PageStyleChild._switchStylesheet()
- 位置: L86-125
- 役割: 指定タイトルのシートだけを有効にし、タイトルの無いシートが無効なら有効に戻す。link 要素も同様に扱う。
- 触るとき: 代替スタイルの切り替え方法を変えるとき。
- 呼び出し先: `Array.from()`
- 条件付き依存: `if (title)` → `this._collectLinks()`
- 条件付き依存: `if (title)` → `docStyleSheets.some()`
- 条件付き依存: `if (title)` → `links.some()`
- 参照: `document.styleSheets`, `link.disabled`, `link.title`, `sheet.disabled`, `sheet.title`, `this.document`

## PageStyleChild.#collectAndSendSheets()
- 位置: L127-139
- 役割: アイドル時に、タイトル付きのシート一覧と既定スタイルの選択状態を PageStyle:Add で親へ送る。
- 触るとき: 情報を送るタイミングを変えるとき。
- 呼び出し先: `this.#collectStyleSheets()`, `this.sendAsyncMessage()`, `window.requestIdleCallback()`
- 参照: `this.browsingContext.associatedWindow`, `this.document.preferredStyleSheetSet`, `window.closed`

## PageStyleChild.#collectStyleSheets()
- 位置: L147-198
- 役割: 表示メディアに合うタイトル付きのシートを styleSheets と link 要素から集め、無効かどうかを付けて返す。
- 触るとき: 代替スタイルの一覧に何を含めるかを変えるとき。
- 呼び出し先: `content.matchMedia()`, `result.push()`, `sheet.ownerNode.nodeName.toLowerCase()`, `this._collectLinks()`
- 参照: `content.document`, `content.matchMedia(media).matches`, `document.preferredStyleSheetSet`, `document.styleSheets`, `link.disabled`, `link.media`, `link.sheet?.disabled`, `link.title`, `sheet.disabled`, `sheet.href`, `sheet.media.mediaText`, `sheet.ownerNode`, `sheet.title`
