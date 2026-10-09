# browser/components/aiwindow/ui/components/aitab-tool-ui/aitab-tool-ui.mjs

source: browser/components/aiwindow/ui/components/aitab-tool-ui/aitab-tool-ui.mjs
source-hash: 9f6c2e4f6e5e8b8a03e81607b7cae337bd54bf96
lines: 146

## <module>
- 役割: AI タブ作成の進行状態(作成中・選択・完了)を描く aitab-tool-ui カスタム要素を定義するモジュール。
- 呼び出し先: `customElements.define()`

## AITabToolUI.constructor()
- 位置: L21-26
- 役割: state を creating、title を空、completeStateOpen を true にして初期化する。
- 触るとき: 初期表示の状態を変えるとき、または完了メッセージが最初から開いて見える理由を調べるとき。
- 呼び出し先: `super()`
- 参照: `this.completeStateOpen`, `this.state`, `this.title`

## AITabToolUI.#handleKeyboardActivation()
- 位置: L28-33
- 役割: Enter か Space が押されたら既定動作を止めて完了メッセージの開閉を切り替える。
- 触るとき: 完了見出しのキー操作を追加・変更するとき。
- 条件付き依存: `if (event.key === "Enter" || event.key === " ")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Enter" || event.key === " ")` → `this.#toggleCompleteMessage()`
- 参照: `event.key`

## AITabToolUI.#toggleCompleteMessage()
- 位置: L35-37
- 役割: completeStateOpen を反転させる。
- 触るとき: 完了メッセージの開閉の条件を変えるとき。
- 参照: `this.completeStateOpen`

## AITabToolUI.#requestOpen()
- 位置: L39-47
- 役割: 開く先(current か new)を detail に入れた aitab-open-request イベントを bubbles・composed で発火する。
- 触るとき: 開く先の選択を親の要素へ伝える経路や、イベント名の受け側を変えるとき。
- 呼び出し先: `this.dispatchEvent()`

## AITabToolUI.#renderCreating()
- 位置: L49-55
- 役割: 作成中であることを示す role=status の段落を描く。
- 触るとき: 作成中の表示文言やアクセシビリティ属性を変えるとき。
- 呼び出し先: `html()`

## AITabToolUI.#renderChoose()
- 位置: L57-83
- 役割: タイトルと「ここで開く」「新しいタブで開く」の2つの moz-button を描き、押すと #requestOpen を呼ぶ。
- 触るとき: 選択状態のボタン構成や、押したときの開く先を変えるとき。
- 呼び出し先: `html()`, `this.#requestOpen()`
- 参照: `this.title`

## AITabToolUI.#renderComplete()
- 位置: L85-116
- 役割: 完了見出し(開閉ボタン)を描き、開いているときだけタイトルを表示する。
- 触るとき: 完了表示の開閉の矢印やタイトルの表示条件を変えるとき。
- 呼び出し先: `html()`, `this.#handleKeyboardActivation()`, `this.#toggleCompleteMessage()`
- 参照: `this.completeStateOpen`, `this.title`

## AITabToolUI.#renderState()
- 位置: L118-132
- 役割: state の値で creating・choose・complete のどれを描くか切り替え、該当しなければ何も描かない。
- 触るとき: 状態を増やしたり名前を変えたりするとき、または想定外の state で何も表示されないときに確認するとき。
- 呼び出し先: `this.#renderChoose()`, `this.#renderComplete()`, `this.#renderCreating()`
- 参照: `this.state`

## AITabToolUI.render()
- 位置: L134-142
- 役割: スタイルシートの link を入れ、#renderState の結果を返す。
- 触るとき: 要素全体のスタイルシートの読み込みを変えるとき。
- 呼び出し先: `html()`, `this.#renderState()`
