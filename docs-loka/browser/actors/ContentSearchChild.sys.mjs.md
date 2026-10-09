# browser/actors/ContentSearchChild.sys.mjs

source: browser/actors/ContentSearchChild.sys.mjs
source-hash: 3012a16173f8bb3ab341515f00eea1f2726a9a7d
lines: 35

## <module>
- 役割: 検索 UI のコンテンツ側アクター。ページ内の ContentSearchClient イベントを親へ送り、親からの応答をページ向けの ContentSearchService イベントに変換する。

## ContentSearchChild.handleEvent()
- 位置: L6-12
- 役割: ContentSearchClient イベントの detail.type と data を、そのまま親への async メッセージとして送る。
- 触るとき: 検索ボックスからの要求が親に届かないときに見る。
- 条件付き依存: `if (event.type == "ContentSearchClient")` → `this.sendAsyncMessage()`
- 参照: `event.detail.data`, `event.detail.type`, `event.type`

## ContentSearchChild.receiveMessage()
- 位置: L14-18
- 役割: 親からのメッセージ名とデータを _fireEvent に渡し、ページ側へ転送する。
- 触るとき: 親から検索結果や状態をページへ返す経路を変えるときに見る。
- 呼び出し先: `this._fireEvent()`
- 参照: `msg.data`, `msg.name`

## ContentSearchChild._fireEvent()
- 位置: L20-33
- 役割: type と data を detail に詰めて Cu.cloneInto で複製し、ContentSearchService という CustomEvent としてページに発火する。
- 触るとき: ページ側が受け取るイベントの形式を変えるときに見る。
- 呼び出し先: `Cu.cloneInto()`, `this.contentWindow.dispatchEvent()`
- 参照: `this.contentWindow`, `this.contentWindow.CustomEvent`
