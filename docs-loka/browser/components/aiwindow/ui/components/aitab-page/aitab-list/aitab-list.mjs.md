# browser/components/aiwindow/ui/components/aitab-page/aitab-list/aitab-list.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-list/aitab-list.mjs
source-hash: 5cb359ac26a03c65804fd27af55e3e8cc46bc3d9
lines: 101

## <module>
- 役割: AI Tab ページの項目リスト aitab-list を定義する
- 呼び出し先: `customElements.define()`

## AITabList.constructor()
- 位置: L37-43
- 役割: title・description を空、groups を空配列、layout を column にする
- 触るとき: layout の既定値を変えたいとき、属性が無い場合の初期表示を見直すとき。
- 呼び出し先: `super()`
- 参照: `this.description`, `this.groups`, `this.layout`, `this.title`

## AITabList.#renderIntro()
- 位置: L45-60
- 役割: タイトルと説明文があれば見出し部分を出す
- 触るとき: リスト上部の見出し・説明の表示条件や要素を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.description`, `this.title`

## AITabList.#renderGroup()
- 位置: L62-73
- 役割: 見出し付きの項目グループを ul として組み立てる
- 触るとき: グループ見出しの有無による表示や、項目テキストの扱いを変えるとき。text が無い項目は空文字になる。
- 呼び出し先: `group.items.map()`, `html()`
- 参照: `group.heading`, `item?.text`

## AITabList.render()
- 位置: L75-97
- 役割: 項目を持つグループだけを選んで一覧セクションを描画する
- 触るとき: 項目が空のグループを隠す条件や、全体の構造を変えるとき。全グループが空なら何も出さない。
- 呼び出し先: `(this.groups ?? []).filter()`, `groups.map()`, `html()`, `this.#renderGroup()`, `this.#renderIntro()`
- 参照: `group?.items?.length`, `groups.length`, `this.groups`
