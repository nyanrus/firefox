# browser/components/aiwindow/ui/components/aitab-page/aitab-header/aitab-header.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-header/aitab-header.mjs
source-hash: 06838b91731519349a06bd409f63a0fd463980ef
lines: 99

## <module>
- 役割: AI Tab ページ上部のヘッダー aitab-header を定義する
- 呼び出し先: `customElements.define()`

## AITabHeader.constructor()
- 位置: L39-46
- 役割: 各プロパティを空値または false で初期化する
- 触るとき: ヘッダー要素に値が渡されない状態での既定表示を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.createdAt`, `this.references`, `this.refreshing`, `this.subhead`, `this.title`

## AITabHeader.#renderCreatedAt()
- 位置: L48-54
- 役割: createdAt があるときだけ日付ラベルを出す
- 触るとき: 作成日の表示位置や条件を変えるとき。日付の整形は呼び出し側で済んでいる。
- 呼び出し先: `html()`
- 参照: `this.createdAt`

## AITabHeader.#renderReferences()
- 位置: L56-70
- 役割: 参照元を chip に変換し grouped-chip-container で並べる
- 触るとき: 参照元リンクの表示名やアイコンの扱いを変えるとき。title が空なら href を表示名にする。
- 呼び出し先: `html()`, `this.references.map()`
- 参照: `source.favicon`, `source.href`, `source.title`, `this.references.length`

## AITabHeader.render()
- 位置: L72-95
- 役割: 操作ボタン・日付・タイトル・副題・参照元をヘッダーに組み立てる
- 触るとき: ヘッダー内の並び順や、refreshing 中のボタン表示を変えるとき。
- 呼び出し先: `html()`, `this.#renderCreatedAt()`, `this.#renderReferences()`
- 参照: `this.refreshing`, `this.subhead`, `this.title`
