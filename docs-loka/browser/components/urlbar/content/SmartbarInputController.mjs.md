# browser/components/urlbar/content/SmartbarInputController.mjs

source: browser/components/urlbar/content/SmartbarInputController.mjs
source-hash: 64b52574dca6b2671508c745ccf64992148d2eb1
lines: 209

## <module>
- 役割: Smartbar の編集部品を抽象化するコントローラーで、MultilineEditor と標準 HTML input の両方を同じ API で扱えるようにする。

## SmartbarInputController.constructor()
- 位置: L24-29
- 役割: adapter から input 要素と editor オブジェクトを受け取って保持する。
- 触るとき: Smartbar 生成時に adapter の input と editor の対応が正しいか確認するとき。
- 参照: `adapter.editor`, `adapter.input`, `this.editor`, `this.input`

## SmartbarInputController.focus()
- 位置: L34-36
- 役割: input 要素にフォーカスを移す。
- 触るとき: Smartbar を開いたときや候補選択後に入力欄へ戻すフォーカス制御を見直すとき。
- 呼び出し先: `this.input.focus()`

## SmartbarInputController.blur()
- 位置: L41-43
- 役割: input 要素からフォーカスを外す。
- 触るとき: パネル外クリックなどで Smartbar の入力を離脱させる処理を調べるとき。
- 呼び出し先: `this.input.blur()`

## SmartbarInputController.readOnly()
- 位置: L50-52
- 役割: input の readOnly 状態を返す。
- 触るとき: 読み取り専用化の判定を呼び出し側で参照するとき。
- 参照: `this.input.readOnly`

## SmartbarInputController.readOnly()
- 位置: L54-56
- 役割: input の readOnly 状態を設定する。
- 触るとき: 入力を一時的に止める状況で readOnly を切り替える処理を追加するとき。
- 参照: `this.input.readOnly`

## SmartbarInputController.placeholder()
- 位置: L63-65
- 役割: input の placeholder 文字列を返し、未設定なら空文字を返す。
- 触るとき: Smartbar の案内文言がどこから来るか追うとき。
- 参照: `this.input.placeholder`

## SmartbarInputController.placeholder()
- 位置: L67-69
- 役割: placeholder を設定し、null や undefined は空文字として扱う。
- 触るとき: モードごとに案内文を切り替える処理を変えるとき。
- 参照: `this.input.placeholder`

## SmartbarInputController.value()
- 位置: L76-78
- 役割: input の現在値を返し、未設定なら空文字を返す。
- 触るとき: 入力欄の文字列を読み取る箇所の null 扱いを確認するとき。
- 参照: `this.input.value`

## SmartbarInputController.setValue()
- 位置: L85-87
- 役割: input の値を設定し、null や undefined は空文字にする。
- 触るとき: 候補選択などでプログラムから入力欄の文字列を差し替えるとき。
- 参照: `this.input.value`

## SmartbarInputController.selectionStart()
- 位置: L94-96
- 役割: 選択開始オフセットを返し、取得できなければ 0 を返す。
- 触るとき: カーソル位置を基準にした文字列処理を書くとき。
- 参照: `this.input.selectionStart`

## SmartbarInputController.selectionStart()
- 位置: L98-100
- 役割: 選択開始位置を設定し、終了位置は現在値を維持して setSelectionRange に渡す。
- 触るとき: 選択開始だけを動かす操作を追加するとき。
- 呼び出し先: `this.setSelectionRange()`
- 参照: `this.selectionEnd`

## SmartbarInputController.selectionEnd()
- 位置: L107-109
- 役割: 選択終了オフセットを返し、取得できなければ 0 を返す。
- 触るとき: 選択範囲の末尾を基準にした処理を書くとき。
- 参照: `this.input.selectionEnd`

## SmartbarInputController.selectionEnd()
- 位置: L111-113
- 役割: 選択終了位置を設定し、開始位置は現在値を維持して setSelectionRange に渡す。
- 触るとき: 選択終了だけを動かす操作を追加するとき。
- 呼び出し先: `this.setSelectionRange()`
- 参照: `this.selectionStart`

## SmartbarInputController.setSelectionRange()
- 位置: L123-130
- 役割: 選択範囲を設定する。開始は 0 以上に丸め、終了は開始以上に丸めてから input に渡す。
- 触るとき: 選択範囲が逆転したり負値になったりする入力に対する挙動を確認するとき。
- 呼び出し先: `Math.max()`, `this.input.setSelectionRange()`
- 参照: `this.input.setSelectionRange`

## SmartbarInputController.setRangeText()
- 位置: L140-142
- 役割: 指定範囲のテキストを置き換え、選択範囲も selectionMode に従って更新する。
- 触るとき: 補完や挿入で一部の文字列だけを差し替える処理を書くとき。
- 呼び出し先: `this.input.setRangeText()`

## SmartbarInputController.select()
- 位置: L147-149
- 役割: input の全文を選択する。select が無い要素では何もしない。
- 触るとき: 入力欄を開いたときに全選択させる挙動を変えるとき。
- 呼び出し先: `this.input.select()`

## SmartbarInputController.dispatchInput()
- 位置: L161-170
- 役割: bubbles と composed を立てた input イベントを input 要素に発火させる。
- 触るとき: プログラムによる値変更を入力として他のリスナーに通知する必要があるとき。
- 呼び出し先: `this.input.dispatchEvent()`

## SmartbarInputController.dispatchSelectionChange()
- 位置: L175-179
- 役割: selectionchange イベントを input 要素に発火させる。
- 触るとき: 選択範囲を変えた後に選択変更を購読側へ伝えるとき。
- 呼び出し先: `this.input.dispatchEvent()`

## SmartbarInputController.composing()
- 位置: L186-188
- 役割: editor が IME 変換中かどうかを返し、不明なら false を返す。
- 触るとき: 変換中の確定前入力を候補更新から除外する判定を見直すとき。
- 参照: `this.editor.composing`

## SmartbarInputController.selectionRangeCount()
- 位置: L195-197
- 役割: editor の選択範囲の数を返し、取得できなければ 0 を返す。
- 触るとき: 複数選択の有無で分岐する処理を追加するとき。
- 参照: `this.editor.selection?.rangeCount`

## SmartbarInputController.selectionToStringWithFormat()
- 位置: L205-207
- 役割: editor の現在の選択を書式付き文字列として返し、取得できなければ空文字を返す。
- 触るとき: 選択中のテキストを書式ごと取り出してメンションや貼り付けに使うとき。
- 呼び出し先: `this.editor.selection?.toStringWithFormat()`
