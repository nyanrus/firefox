# browser/components/aiwindow/ui/actors/AITabChild.sys.mjs

source: browser/components/aiwindow/ui/actors/AITabChild.sys.mjs
source-hash: 4b884342ece3fbb456eaff8044694e98674f36c2
lines: 65

## <module>
- 役割: about:smartpage (AITab) のページ側イベントを親プロセスへ中継する子アクター。イベント名を変えずに転送する。

## AITabChild.handleEvent()
- 位置: L11-25
- 役割: AITab:GetPage と AITab:DeletePage は応答つきで親へ問い合わせ、AITab:OpenLink は応答を待たずに送る。未知のイベントは警告を出して捨てる。
- 触るとき: about:smartpage に新しいイベントを追加するとき、または AITab のページ操作が親に届かないときに見る。新しいイベントは switch に足さないと捨てられる。
- 呼び出し先: `console.warn()`, `this.#query()`, `this.sendAsyncMessage()`
- 参照: `event.detail`, `event.type`

## AITabChild.#query()
- 位置: L33-42
- 役割: sendQuery で親へ問い合わせ、成功なら :Response、失敗なら :Error を要素へ返す。
- 触るとき: about:smartpage でページ取得や削除の結果が返らない、またはエラーが画面に出ないときに見る。
- 呼び出し先: `console.error()`, `this.#respond()`, `this.sendQuery()`, `this.sendQuery(event.type, event.detail) .then()`
- 参照: `error.message`, `event.detail`, `event.type`

## AITabChild.#respond()
- 位置: L52-63
- 役割: 要求元の要素に "<イベント名>:Response" か ":Error" の CustomEvent を発火する。ページが既に無ければ何もしない。
- 触るとき: 応答イベント名や detail の形を変えるとき、または content 側で応答オブジェクトが読めないとき(Cu.cloneInto の扱い)に見る。
- 呼び出し先: `Cu.cloneInto()`, `event.target.dispatchEvent()`
- 参照: `event.type`, `this.contentWindow`, `this.contentWindow.CustomEvent`
