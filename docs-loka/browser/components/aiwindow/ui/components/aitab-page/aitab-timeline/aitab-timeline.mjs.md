# browser/components/aiwindow/ui/components/aitab-page/aitab-timeline/aitab-timeline.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-timeline/aitab-timeline.mjs
source-hash: 03d03cae64f59ae609bea6fb3da38916e157f6f5
lines: 129

## <module>
- 役割: AI Tab ページの時系列ブロック aitab-timeline を定義する
- 呼び出し先: `customElements.define()`

## AITabTimeline.constructor()
- 位置: L34-39
- 役割: title・description を空、items を空配列にする
- 触るとき: 時系列ブロックの既定値を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.description`, `this.items`, `this.title`

## AITabTimeline.#renderIntro()
- 位置: L41-58
- 役割: タイトルと説明文があれば見出し部分を出す
- 触るとき: 時系列の上部見出しの表示条件や要素を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.description`, `this.title`

## AITabTimeline.#renderEntryTitle()
- 位置: L67-72
- 役割: 項目見出しを、ブロック見出しの有無で h3 か h2 にする
- 触るとき: 項目見出しの見出しレベル（アウトライン）を変えるとき。見た目のサイズはクラスで決まる。
- 呼び出し先: `html()`
- 参照: `this.title`

## AITabTimeline.#renderItem()
- 位置: L74-99
- 役割: 日付欄と本文欄からなる項目1件の li を組み立てる
- 触るとき: 日付ラベルや補足ラベル、説明文の表示条件を変えるとき。
- 呼び出し先: `html()`, `this.#renderEntryTitle()`
- 参照: `item.date_eyebrow`, `item.date_label`, `item.description`, `item.title`

## AITabTimeline.render()
- 位置: L101-125
- 役割: 日付かタイトルのある項目だけを ol に並べて描画する
- 触るとき: 項目を表示から外す条件を変えるとき。空ならセクションごと出さない。
- 呼び出し先: `(this.items ?? []).filter()`, `html()`, `items.map()`, `this.#renderIntro()`, `this.#renderItem()`
- 参照: `item?.date_label`, `item?.title`, `items.length`, `this.items`
