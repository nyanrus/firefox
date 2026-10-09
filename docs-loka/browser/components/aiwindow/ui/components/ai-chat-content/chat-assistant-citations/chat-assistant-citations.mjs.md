# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-citations/chat-assistant-citations.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-citations/chat-assistant-citations.mjs
source-hash: f4807dbc2283ee77d43c54336a0237b54f2d2ec9
lines: 165

## <module>
- 役割: アシスタント回答の出典をピルで並べ、入りきらない分は +n more のパネルに入れる要素を定義する。
- 呼び出し先: `SmartwindowOverflowRowMixin()`, `customElements.define()`

## ChatAssistantCitations.constructor()
- 位置: L38-42
- 役割: 出典配列を空に、パネルの開閉状態を閉じに初期化する。
- 触るとき: 出典の既定値や開閉の初期状態を変えるときに見る。
- 呼び出し先: `super()`
- 参照: `this.citations`, `this.isPanelOpen`

## ChatAssistantCitations.overflowContainerSelector()
- 位置: L47-49
- 役割: 溢れ計算の対象となる出典の行（.citations）のセレクターを返す。
- 触るとき: 出典行のクラス名を変えたとき、溢れ判定が効かなくなるので合わせて直す。

## ChatAssistantCitations.overflowTriggerSelector()
- 位置: L54-56
- 役割: 「+n more」ボタン（.citations-more）のセレクターを返す。
- 触るとき: more ボタンのクラス名を変えるとき、または溢れ判定の起点がずれるときに見る。

## ChatAssistantCitations.overflowItems()
- 位置: L61-63
- 役割: 溢れ計算に使う出典配列を返し、未設定時は空配列にする。
- 触るとき: 溢れ判定の対象を出典以外に広げるとき、または出典が未設定で例外が出るときに見る。
- 参照: `this.citations`

## ChatAssistantCitations.#panel()
- 位置: L65-67
- 役割: シャドウルート内の smartwindow-panel-list 要素を取得する。
- 触るとき: +n more のパネルが開かない、または別の要素を掴んでいると感じたときに見る。
- 呼び出し先: `this.shadowRoot.querySelector()`

## ChatAssistantCitations.#onToggleClick()
- 位置: L69-75
- 役割: more ボタンを anchor にしてパネルを開閉する。
- 触るとき: more ボタンを押してもパネルが出ない、または位置がずれるときに見る。
- 呼び出し先: `this.#panel()`
- 条件付き依存: `if (panel)` → `panel.toggle()`
- 参照: `event.currentTarget`, `panel.anchor`

## ChatAssistantCitations.#onPanelOpenLink()
- 位置: L77-79
- 役割: パネル内の出典リンクが開かれたとき、パネルを閉じる。
- 触るとき: リンクを開いた後にパネルが残る、または閉じるタイミングを変えるときに見る。
- 呼び出し先: `this.#panel()`, `this.#panel()?.hide()`

## ChatAssistantCitations.#label()
- 位置: L81-85
- 役割: 表示名として title、無ければ URL のホスト名、さらに無ければ URL 全体を返す。
- 触るとき: 出典ピルの文字列を変えるとき、またはタイトルが無い出典の表示を確認するときに見る。
- 呼び出し先: `URL.parse()`
- 参照: `URL.parse(citation.url)?.hostname`, `citation.title`, `citation.url`

## ChatAssistantCitations.#titleText()
- 位置: L87-89
- 役割: ツールチップ用に title、無ければ URL を返す。
- 触るとき: ピルのホバー時の文字を変えるとき、または title の扱いを揃えるときに見る。
- 参照: `citation.title`, `citation.url`

## ChatAssistantCitations.#icon()
- 位置: L91-98
- 役割: faviconUrl、次に page-icon、最後に既定のファビコンの順でアイコン URL を決める。
- 触るとき: 出典のアイコンが既定のまま変わらないときや、アイコン取得元を増やすときに見る。
- 参照: `citation.faviconUrl`, `citation.hasFavicon`, `citation.url`

## ChatAssistantCitations.#renderPill()
- 位置: L100-111
- 役割: 出典 1 件分の ai-website-chip を描画し、メニュー項目としての role を付け替えられる。
- 触るとき: ピルの見た目や属性（size、type、role）を変えるとき、またはパネル内の項目が menuitem にならないときに見る。
- 呼び出し先: `html()`, `this.#icon()`, `this.#label()`, `this.#titleText()`
- 参照: `citation.url`

## ChatAssistantCitations.render()
- 位置: L113-161
- 役割: 表示上限を超える分を隠し、残りを +n more パネルに入れて描画する。
- 触るとき: 出典の表示件数や溢れ時の振る舞いを変えるとき、またはパネルの開閉状態が同期しないときに見る。
- 呼び出し先: `JSON.stringify()`, `Math.min()`, `String()`, `citationsOverflow.map()`, `html()`, `this.#renderPill()`, `this.citations.map()`, `this.citations.slice()`
- 参照: `citationsOverflow.length`, `this.#onPanelOpenLink`, `this.#onToggleClick`, `this.citations.length`, `this.citations?.length`, `this.isPanelOpen`, `this.visibleCount`
