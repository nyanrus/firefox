# browser/components/aiwindow/ui/components/smartwindow-resume-card/smartwindow-resume-card.mjs

source: browser/components/aiwindow/ui/components/smartwindow-resume-card/smartwindow-resume-card.mjs
source-hash: db4988b606910e6ed850d7a3dc9c0d9230831023
lines: 181

## <module>
- 役割: 途中だった閲覧や会話を再開するための再開カード smartwindow-resume-card を定義するモジュール。
- 呼び出し先: `customElements.define()`

## SmartwindowResumeCard.constructor()
- 位置: L28-32
- 役割: content と journeyId を null で初期化する。
- 触るとき: カードの初期値を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.content`, `this.journeyId`

## SmartwindowResumeCard.#dispatch()
- 位置: L34-42
- 役割: smartwindow-resume-card:種別 の名前で、バブルしてシャドウ境界を越える CustomEvent を発火する。
- 触るとき: 親へ送るカードのイベント名や detail の形式を変えるとき。
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowResumeCard.#onCardPointerDown()
- 位置: L47-50
- 役割: ポインターを押した時点で更新メニューが開いていたかを記録し、直後の click の判定に使えるようにする。
- 触るとき: カードのクリックと更新メニューを閉じる操作が競合して、意図せず再開してしまう問題を調べるとき。
- 呼び出し先: `this.shadowRoot.getElementById()`
- 参照: `this.#wasMoreMenuOpenOnPointerDown`, `this.shadowRoot.getElementById(MORE_MENU_ID)?.open`

## SmartwindowResumeCard.#onCardClick()
- 位置: L52-67
- 役割: 直前に更新メニューが開いていたクリックや文字の選択中は無視し、それ以外は resume を発火する。キーボード由来のクリックは常に通す。
- 触るとき: カード全体を押したときに再開するかどうかの条件を変えるとき。
- 呼び出し先: `this.#dispatch()`, `this.ownerDocument.getSelection()`
- 参照: `event.detail`, `selection.isCollapsed`, `this.#wasMoreMenuOpenOnPointerDown`, `this.journeyId`

## SmartwindowResumeCard.#onDismissClick()
- 位置: L69-72
- 役割: 伝播を止め、dismiss を発火する。
- 触るとき: 閉じるボタンの通知内容を変えるとき。
- 呼び出し先: `e.stopPropagation()`, `this.#dispatch()`
- 参照: `this.journeyId`

## SmartwindowResumeCard.#stopPropagation()
- 位置: L74-76
- 役割: イベントの伝播を止める。
- 触るとき: メニューやボタンのクリックがカードに伝わらないようにする処理を変えるとき。
- 呼び出し先: `e.stopPropagation()`

## SmartwindowResumeCard.#onMenuItemClick()
- 位置: L78-83
- 役割: 選ばれた項目の ID を入れた menu-item-selected を発火する。
- 触るとき: 更新メニューの項目を増やしたり通知内容を変えるとき。
- 呼び出し先: `this.#dispatch()`
- 参照: `this.journeyId`

## SmartwindowResumeCard.#renderFavicons()
- 位置: L85-107
- 役割: previewTabs の先頭3件を page-icon の画像として並べ、読み込みに失敗したら既定の favicon にする。タブが無ければ何も描かない。
- 触るとき: カードに出すタブのアイコンの数や取得元を変えるとき。
- 呼び出し先: `html()`, `tabs.slice()`, `tabs.slice(0, MAX_VISIBLE_FAVICONS).map()`
- 参照: `e.target.src`, `tab.url`, `tabs.length`, `this.content?.previewTabs`

## SmartwindowResumeCard.render()
- 位置: L109-177
- 役割: content が無ければ何も描かず、ある場合はタブ数・見出し・説明・閉じるボタン・更新メニュー・再開ボタンを組み立てる。
- 触るとき: カードの構成、ボタンの並び、ラベルに渡す値を変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#onMenuItemClick()`, `this.#renderFavicons()`
- 条件付き依存: `if (!this.content)` → `html()`
- 参照: `this.#onCardClick`, `this.#onCardPointerDown`, `this.#onDismissClick`, `this.#stopPropagation`, `this.content`, `this.content.headline`, `this.content.previewTabs?.length`, `this.content.status`
