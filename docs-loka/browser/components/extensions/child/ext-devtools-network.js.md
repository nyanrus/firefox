# browser/components/extensions/child/ext-devtools-network.js

source: browser/components/extensions/child/ext-devtools-network.js
source-hash: e4981aaa47c51c1dbff723facadfa22b00aa78b2
lines: 69

## <module>
- 役割: devtools.network の子側 API を定義する。親から届く完了リクエストの HAR エントリに本文取得の関数を付け、拡張へ複製して渡す。

## ChildNetworkResponseLoader.constructor()
- 位置: L15-18
- 役割: 拡張コンテキストとリクエスト ID を保持する。
- 触るとき: 本文取得に使うリクエスト ID の持ち方を変えるとき。
- 参照: `this.context`, `this.requestId`

## ChildNetworkResponseLoader.api()
- 位置: L20-31
- 役割: getContent を持つオブジェクトを返し、HAR エントリに結合できるようにする。
- 触るとき: 拡張の HAR エントリに付くメソッドを変えるとき。

## ChildNetworkResponseLoader.getContent()
- 位置: L23-29
- 役割: 親の devtools.network.Request.getContent を呼び、本文を callback で受け取る。
- 触るとき: レスポンス本文の取得経路を変えるとき。
- 呼び出し先: `context.childManager.callParentAsyncFunction()`

## getAPI()
- 位置: L35-67
- 役割: devtools.network.onRequestFinished を EventManager で作って公開する。
- 触るとき: イベント名や公開の形式を変えるとき。

## register()
- 位置: L42-62
- 役割: 親の onRequestFinished を購読し、届いたエントリを拡張へ発火させる。解除関数も返す。
- 触るとき: 拡張がリスナを登録、解除したときの親側の購読の扱いを変えるとき。
- 呼び出し先: `context.childManager.getParentEvent()`, `parent.addListener()`, `parent.removeListener()`

## onFinished()
- 位置: L43-53
- 役割: 受け取ったデータに本文取得の関数を足し、cloneInto で拡張側へ複製して asyncWithoutClone で発火させる。
- 触るとき: 拡張へ渡す HAR エントリの形式や複製の方法を変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `fire.asyncWithoutClone()`, `loader.api()`
- 参照: `context.cloneScope`, `data.harEntry`, `data.requestId`
