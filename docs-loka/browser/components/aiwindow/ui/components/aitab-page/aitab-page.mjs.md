# browser/components/aiwindow/ui/components/aitab-page/aitab-page.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-page.mjs
source-hash: 1c8dca9d162cc1f0fe0700289b23cdc57ca14e02
lines: 294

## <module>
- 役割: about:smartpage の根となる aitab-page 要素を定義する
- 呼び出し先: `customElements.define()`

## AITabPage.constructor()
- 位置: L44-57
- 役割: 状態を loading にし、ブロック種別名から描画関数への Map を作る
- 触るとき: 新しいブロック種別を足すときや、対応する描画関数を差し替えるときに見る。
- 呼び出し先: `super()`, `this.#renderCards.bind()`, `this.#renderHighlights.bind()`, `this.#renderList.bind()`, `this.#renderRankedTable.bind()`, `this.#renderSourceLinks.bind()`, `this.#renderTextBlock.bind()`, `this.#renderTimeline.bind()`, `this.#renderers.set()`
- 参照: `this.#renderers`, `this.page`, `this.status`

## AITabPage.connectedCallback()
- 位置: L59-65
- 役割: 接続時にページを読み込み、失敗したら status を error にする
- 触るとき: ページ読み込みの開始条件や失敗時の扱いを変えるとき。
- 呼び出し先: `console.error()`, `super.connectedCallback()`, `this.#loadPage()`, `this.#loadPage().catch()`
- 参照: `this.status`

## AITabPage.pageName()
- 位置: L73-75
- 役割: URL の page クエリを取り出す
- 触るとき: ページを特定するキーの渡し方を変えるとき。パスとしては扱わない。
- 呼び出し先: `new URLSearchParams(window.location.search).get()`
- 参照: `window.location.search`

## AITabPage.#loadPage()
- 位置: async L77-90
- 役割: page 名が無ければ unavailable、あれば親に GET 要求して page を保持する
- 触るとき: ページ取得の結果による loading・ready・unavailable の遷移を変えるとき。
- 呼び出し先: `this.#request()`
- 参照: `response.page`, `response?.error`, `response?.success`, `this.page`, `this.pageName`, `this.status`

## AITabPage.#deletePage()
- 位置: async L97-105
- 役割: 親に削除を要求し、成功したら page を消して unavailable にする
- 触るとき: 削除後の表示を変えるとき。タブは閉じず unavailable 表示のまま残す。
- 呼び出し先: `this.#request()`
- 参照: `response?.error`, `response?.success`, `this.page`, `this.status`

## AITabPage.#request()
- 位置: L114-132
- 役割: 子アクターへ要求イベントを送り、応答か失敗を Promise で返す
- 触るとき: 親アクターとのメッセージ名や応答の待ち方を変えるとき。応答と失敗のどちらか一方で両リスナーを外す。
- 呼び出し先: `this.addEventListener()`, `this.dispatchEvent()`

## onResponse()
- 位置: L116-119
- 役割: 応答イベントを受け、失敗側のリスナーを外して結果を返す
- 触るとき: 応答データの取り出し方を変えるとき。
- 呼び出し先: `resolve()`, `this.removeEventListener()`
- 参照: `event.detail`

## onError()
- 位置: L120-123
- 役割: 失敗イベントを受け、応答側のリスナーを外して拒否する
- 触るとき: エラーメッセージの組み立てや失敗時の後始末を変えるとき。
- 呼び出し先: `reject()`, `this.removeEventListener()`
- 参照: `event.detail?.error`

## AITabPage.#renderHeader()
- 位置: L134-156
- 役割: ページのタイトルを document.title に設定し、ヘッダー要素を返す
- 触るとき: ヘッダーに渡す値や、削除ボタンからの削除イベントの受け方を変えるとき。削除失敗時は status を error にする。
- 呼び出し先: `console.error()`, `html()`, `this.#deletePage()`, `this.#deletePage().catch()`
- 参照: `document.title`, `header.references?.items`, `header.subhead`, `header.title`, `this.page?.createdAtLabel`, `this.status`

## AITabPage.#renderHighlights()
- 位置: L158-168
- 役割: highlights ブロックを aitab-highlights でブロックに包む
- 触るとき: ハイライトに渡すプロパティを変えるとき。
- 呼び出し先: `highlights.component.toLowerCase()`, `html()`, `this.#renderBlock()`
- 参照: `highlights.items`, `highlights.title`

## AITabPage.#renderSourceLinks()
- 位置: L173-175
- 役割: sourcelinks ブロックを何も描画せず nothing を返す（未実装）
- 触るとき: 出典リンクのブロックを実装するとき。TODO のとおり別コンポーネントに切り出す必要がある。

## AITabPage.#renderTextBlock()
- 位置: L177-188
- 役割: textblock を aitab-text-block に渡してブロックに包む
- 触るとき: 本文ブロックに渡す lead・段落・参照元の扱いを変えるとき。
- 呼び出し先: `html()`, `textBlock.component.toLowerCase()`, `this.#renderBlock()`
- 参照: `textBlock.lead`, `textBlock.paragraphs`, `textBlock.references`

## AITabPage.#renderRankedTable()
- 位置: L190-202
- 役割: rankedtable を aitab-table に渡してブロックに包む
- 触るとき: 表の見出し・説明・列・行をどう渡すかを変えるとき。
- 呼び出し先: `html()`, `rankedTable.component.toLowerCase()`, `this.#renderBlock()`
- 参照: `rankedTable.columns`, `rankedTable.description`, `rankedTable.rows`, `rankedTable.title`

## AITabPage.#renderCards()
- 位置: L204-206
- 役割: cards ブロックを何も描画せず nothing を返す（未実装）
- 触るとき: カード形式のブロックを実装するとき。

## AITabPage.#renderTimeline()
- 位置: L208-219
- 役割: timeline を aitab-timeline に渡してブロックに包む
- 触るとき: 時系列ブロックに渡すプロパティを変えるとき。
- 呼び出し先: `html()`, `this.#renderBlock()`, `timeline.component.toLowerCase()`
- 参照: `timeline.description`, `timeline.items`, `timeline.title`

## AITabPage.#renderList()
- 位置: L221-233
- 役割: list を aitab-list に渡してブロックに包む。layout の既定は column
- 触るとき: リストブロックに渡すプロパティや既定の layout を変えるとき。
- 呼び出し先: `html()`, `list.component.toLowerCase()`, `this.#renderBlock()`
- 参照: `list.description`, `list.groups`, `list.layout`, `list.title`

## AITabPage.#renderBlock()
- 位置: L235-245
- 役割: 種別が無いブロックは捨て、あれば data-block-type 付きの section で包む
- 触るとき: 全ブロック共通の外枠や、種別が無いときの扱いを変えるとき。
- 呼び出し先: `html()`
- 参照: `block.html`, `block.type`, `block?.type`

## AITabPage.#renderFooter()
- 位置: L247-249
- 役割: フッターを描画せず nothing を返す（未実装）
- 触るとき: ページ末尾に要素を出すことになったとき。

## AITabPage.#renderStatus()
- 位置: L251-257
- 役割: loading 中は何も出さず、それ以外は aitab-error を出す
- 触るとき: 読み込み中の表示や、エラー表示に切り替える条件を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.status`

## AITabPage.render()
- 位置: L259-267
- 役割: ready ならページ本体、それ以外は状態表示を描画する
- 触るとき: 表示する状態の分岐を変えるとき。
- 呼び出し先: `html()`, `this.#renderPage()`, `this.#renderStatus()`
- 参照: `this.status`

## AITabPage.#renderPage()
- 位置: L269-278
- 役割: 先頭が Header ならヘッダーに分け、残りのブロックと下部を並べる
- 触るとき: ページの大枠（main・ヘッダー・ブロック列）の構成を変えるとき。
- 呼び出し先: `children.slice()`, `html()`, `this.#renderBlocks()`, `this.#renderFooter()`, `this.#renderHeader()`
- 参照: `children[0]?.component`, `this.page.children`

## AITabPage.#renderBlocks()
- 位置: L280-290
- 役割: 各ブロックの component 名を小文字にし、対応する描画関数に渡す
- 触るとき: ブロックの振り分け方法を変えるとき。対応が無いブロックは描画されない。
- 呼び出し先: `block.component?.toLowerCase()`, `blocks.map()`, `html()`, `renderer()`, `this.#renderers.get()`
