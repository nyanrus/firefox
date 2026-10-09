# browser/components/sessionstore/GlobalState.sys.mjs

source: browser/components/sessionstore/GlobalState.sys.mjs
source-hash: 01acbe10773c42ecdf790e20ec53e6af29b642b4
lines: 75

## <module>
- 役割: セッションストアのグローバル状態(ウィンドウやタブに属さない任意の文字列キーと値)を保持する。

## GlobalState.getState()
- 位置: L19-21
- 役割: 保持しているグローバル状態オブジェクトを返す。内部オブジェクトそのものなので、戻り値を書き換えると保持値も変わる。
- 触るとき: セッション状態を丸ごと保存する処理で global の中身を取り出す箇所を調べるとき。
- 参照: `this.#state`

## GlobalState.clear()
- 位置: L26-28
- 役割: グローバル状態を空のオブジェクトに置き換えて全消去する。
- 触るとき: セッションを初期化する処理や、前のセッションの値を残したくない場面で呼ばれるかを確認するとき。
- 参照: `this.#state`

## GlobalState.get()
- 位置: L38-40
- 役割: キーに対応する値を返す。未設定、または値が偽の場合は空文字列を返す。
- 触るとき: 保存済みのグローバル値を読む側で、未設定と空文字の区別が必要かを判断するとき。
- 参照: `this.#state`

## GlobalState.set()
- 位置: L49-51
- 役割: キーに文字列値を格納する。
- 触るとき: 新しいグローバル値を保存する機能を足すとき、値が文字列に限られる前提を守れているか確認する。
- 参照: `this.#state`

## GlobalState.delete()
- 位置: L59-61
- 役割: キーに対応する値を内部状態から削除する。
- 触るとき: 保存済みの値を後から取り消す処理を足すとき、該当キーが他の箇所で読まれていないかを見る。
- 参照: `this.#state`

## GlobalState.setFromState()
- 位置: L71-73
- 役割: 渡された状態オブジェクトの global 部分で状態を置き換える。引数が無い、または global が無い場合は空にする。
- 触るとき: セッションファイルを読み込んで状態を復元する経路を変えるとき。global キーを持たない古い状態を受け取ったときの扱いを確認する。
- 参照: `aState.global`, `this.#state`
