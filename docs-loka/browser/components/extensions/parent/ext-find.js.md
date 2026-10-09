# browser/components/extensions/parent/ext-find.js

source: browser/components/extensions/parent/ext-find.js
source-hash: 4752b8b3dddb29b21880047b09f69d29b01a920a
lines: 271

## <module>
- 役割: find API を実装し、タブ内の全フレームで検索・ハイライト・ハイライト解除を行い、結果を各フレームの ExtFind アクターから集める。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getActorForBrowsingContext()
- 位置: L17-20
- 役割: ブラウジングコンテキストの現在のウィンドウグローバルから ExtFind アクターを取り出す。
- 触るとき: フレームごとの ExtFind アクターが見つからず検索が効かないときに調べる。
- 呼び出し先: `windowGlobal.getActor()`
- 参照: `browsingContext.currentWindowGlobal`

## getTopLevelActor()
- 位置: L22-24
- 役割: ブラウザ要素のトップレベルの ExtFind アクターを返す。
- 触るとき: 検索結果をトップレベルのアクターに紐づけ直す処理を変えるとき。
- 呼び出し先: `getActorForBrowsingContext()`
- 参照: `browser.browsingContext`

## gatherActors()
- 位置: L26-40
- 役割: ブラウジングコンテキストとその子を再帰的にたどり、ExtFind アクターを持つものを列挙する。
- 触るとき: iframe を含むページで検索対象のフレームが漏れる問題を調べるとき。
- 呼び出し先: `gatherActors()`, `getActorForBrowsingContext()`, `list.push()`
- 条件付き依存: `if (actor)` → `list.push()`
- 参照: `browsingContext.children`

## mergeFindResults()
- 位置: L42-78
- 役割: 各フレームの検索結果を合算し、件数と、要求があれば範囲データ・矩形データを連結し、一致のあるフレームごとに framePos を振る。
- 触るとき: find の戻り値の件数や rangeData の framePos の付け方を変えるとき。
- 条件付き依存: `if (params.includeRangeData && item.result.rangeData)` → `finalResult.rangeData.push()`
- 条件付き依存: `if (params.includeRectData && item.result.rectData)` → `finalResult.rectData.push()`
- 参照: `finalResult.count`, `finalResult.rangeData`, `finalResult.rectData`, `item.result.count`, `item.result.rangeData`, `item.result.rectData`, `params.includeRangeData`, `params.includeRectData`, `range.framePos`

## sendMessageToAllActors()
- 位置: L80-84
- 役割: 全フレームの ExtFind アクターに ext-Finder: 付きのメッセージを非同期送信する。
- 触るとき: ハイライト解除などを全フレームに届けたい処理を追加・変更するとき。
- 呼び出し先: `actor.sendAsyncMessage()`, `gatherActors()`
- 参照: `browser.browsingContext`

## getFindResultsForActor()
- 位置: async L86-92
- 役割: 1つのアクターに検索クエリを送り、戻った結果をその検索コンテキストに格納して返す。
- 触るとき: 個々のフレームへの検索問い合わせが失敗したときの扱いを見直すとき。
- 呼び出し先: `findContext.actor.sendQuery()`
- 参照: `findContext.result`

## queryAllActors()
- 位置: L94-100
- 役割: 全フレームのアクターに同じクエリを並行して送り、全部の結果が揃うのを待つ。
- 触るとき: 検索を全フレームに並列実行する仕組みを変えるとき。
- 呼び出し先: `Promise.all()`, `gatherActors()`, `getFindResultsForActor()`, `promises.push()`
- 参照: `browser.browsingContext`

## collectFindResults()
- 位置: async L102-106
- 役割: CollectResults を全フレームに送って結果を集め、トップレベルアクターごとに保存してから合算結果を返す。
- 触るとき: find の結果が次の highlight で使われる保存の仕組みを変えるとき。
- 呼び出し先: `findResults.set()`, `getTopLevelActor()`, `mergeFindResults()`, `queryAllActors()`

## runHighlight()
- 位置: async L108-157
- 役割: 保存済みの検索結果から、指定 rangeIndex のフレームだけをハイライトし、他はハイライトを消す。範囲外や結果なしは拒否する。
- 触るとき: highlightResults が正しい範囲をハイライトしない、または範囲外のエラーを返すときに調べる。
- 呼び出し先: `Promise.all()`, `Promise.reject()`, `findResults.get()`, `getTopLevelActor()`
- 条件付き依存: `if (!list)` → `Promise.reject()`
- 条件付き依存: `if (highlightAll)` → `highlightPromises.push()`
- 条件付き依存: `if (highlightAll)` → `actor.sendQuery()`
- 条件付き依存: `if (!foundResults && index < list[c].result.count)` → `highlightPromises.push()`
- 条件付き依存: `if (!foundResults && index < list[c].result.count)` → `actor.sendQuery()`
- 条件付き依存: `if (!(!foundResults && index < list[c].result.count))` → `highlightPromises.push()`
- 条件付き依存: `if (!(!foundResults && index < list[c].result.count))` → `actor.sendQuery()`
- 条件付き依存: `if (hasResults)` → `responses.includes()`
- 条件付き依存: `if (responses.includes("OutOfRange") || index >= 0)` → `Promise.reject()`
- 条件付き依存: `if (!(responses.includes("OutOfRange") || index >= 0))` → `responses.includes()`
- 参照: `list.length`, `list[c].actor`, `list[c].result.count`, `params.rangeIndex`

## runFindOperation()
- 位置: L170-199
- 役割: タブを解決し、非公開ウィンドウ権限や about:・chrome: などの禁止 URL を検査したうえで、CollectResults か HighlightResults を実行する。
- 触るとき: 検索を拒否する条件(非公開・禁止 URL)を変えるとき、または検索が特定のページで動かないときに見る。
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`, `["about", "chrome", "resource"].includes()`, `tabTracker.getId()`, `tabTracker.getTab()`
- 条件付き依存: `if ( !context.privateBrowsingAllowed && PrivateBrowsingUtils.isBrowserPrivate(browser) )` → `Promise.reject()`
- 条件付き依存: `if ( tab.linkedBrowser.contentPrincipal.isSystemPrincipal || (["about", "chrome", "resource"].includes( tab.linkedBrowser.currentURI.scheme ) && tab.linkedBrowse...)` → `Promise.reject()`
- 条件付き依存: `if (message == "HighlightResults")` → `runHighlight()`
- 条件付き依存: `if (message == "CollectResults")` → `findResults.delete()`
- 条件付き依存: `if (message == "CollectResults")` → `getTopLevelActor()`
- 条件付き依存: `if (message == "CollectResults")` → `collectFindResults()`
- 参照: `context.privateBrowsingAllowed`, `tab.linkedBrowser`, `tab.linkedBrowser.contentPrincipal.isSystemPrincipal`, `tab.linkedBrowser.currentURI.scheme`, `tab.linkedBrowser.currentURI.spec`, `tabTracker.activeTab`

## getAPI()
- 位置: L202-269
- 役割: browser.find の API を組み立て、find・highlightResults・removeHighlighting を公開する。
- 触るとき: find API の公開メソッドや引数を追加・変更するとき。

## find()
- 位置: L224-228
- 役割: 検索語と指定パラメーターを付けて CollectResults を実行し、件数などの結果を返す。
- 触るとき: 拡張の find 呼び出しの引数や戻り値を変えるとき。
- 呼び出し先: `runFindOperation()`
- 参照: `params.queryphrase`

## highlightResults()
- 位置: L245-248
- 役割: 直前の find の結果を、指定された範囲または全体でハイライトする。
- 触るとき: ハイライト結果の文字列(Success, OutOfRange, NoResults)の扱いを変えるとき。
- 呼び出し先: `runFindOperation()`

## removeHighlighting()
- 位置: L257-266
- 役割: 指定タブの全フレームのハイライトを消す。非公開ウィンドウでアクセス権がなければエラーを投げる。
- 触るとき: ハイライトが消えない、または非公開タブのエラー扱いに問題があるときに確認する。
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`, `sendMessageToAllActors()`, `tabTracker.getTab()`
- 参照: `context.privateBrowsingAllowed`, `tab.linkedBrowser`, `tabTracker.activeTab`
