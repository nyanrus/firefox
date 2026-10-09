# browser/components/aboutlogins/content/utils/controllers.mjs

source: browser/components/aboutlogins/content/utils/controllers.mjs
source-hash: 13c46dfcafdae58b153e3e3a895a7f3aecb0d41f
lines: 19

## <module>
- 役割: lit のリアクティブコントローラを、ホストの接続と切断に合わせて後片付けできる形で包む補助関数を定義する

## withSimpleController()
- 位置: L7-18
- 役割: ホストに付けるコントローラのクラスを返す。接続時に functionToBind を実行し、その戻り値を切断時の後片付けとして保持する
- 触るとき: キーボード監視など、要素の接続中だけ有効にしたい処理を追加するとき

## constructor()
- 位置: L9-11
- 役割: 生成時にホストへ自分自身をコントローラとして登録する
- 触るとき: コントローラの登録タイミングを変えるとき
- 呼び出し先: `host.addController()`

## hostConnected()
- 位置: L12-14
- 役割: ホストの接続時に functionToBind を呼び、戻り値の後片付け関数を cleanup に保存する
- 触るとき: 接続時に何が走るかを確認するとき
- 呼び出し先: `functionToBind()`
- 参照: `this.cleanup`

## hostDisconnected()
- 位置: L15-17
- 役割: 保存された後片付け関数を実行する
- 触るとき: 切断時にリスナーが外れない問題を調べるとき
- 呼び出し先: `this.cleanup()`
