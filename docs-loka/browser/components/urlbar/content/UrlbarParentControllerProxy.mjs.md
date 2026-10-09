# browser/components/urlbar/content/UrlbarParentControllerProxy.mjs

source: browser/components/urlbar/content/UrlbarParentControllerProxy.mjs
source-hash: e8dad112e99881c7b701ef12dcb3bfd70a12b155
lines: 515

## <module>
- 役割: 子プロセス側の UrlbarChildController が親の UrlbarParentController の代わりに使う中継役。呼び出しを Urlbar actor のメッセージとして親へ送る。

## UrlbarParentControllerProxy.constructor()
- 位置: L38-46
- 役割: UrlbarInput を親側に登録して instanceId を得て、Init で sapName と isPrivate を親へ送る。
- 触るとき: 新しい urlbar 入力欄の親との対応付けが始まらない時や、Init で親に渡す項目を増やすとき。
- 呼び出し先: `this.#port.registerMessagePathInput()`, `this.#port.sendAsyncMessage()`
- 参照: `input.isPrivate`, `input.sapName`, `this.#instanceId`

## UrlbarParentControllerProxy.setChild()
- 位置: L57-59
- 役割: 親側の instanceId に対応する子コントローラーを登録し、親から子への通知を配送できるようにする。
- 触るとき: 親からの通知が子コントローラーに届かない時や、子の登録タイミングを変えるとき。
- 呼び出し先: `this.#port.registerChildController()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordEngagement()
- 位置: L68-73
- 役割: 子で組み立て・シリアライズ済みの engagement を RecordEngagement で親の記録処理へ送る。
- 触るとき: 検索エンゲージメントのテレメトリが親で記録されない時や、content 側の記録経路を変える時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.resetEngagement()
- 位置: L78-82
- 役割: 親側レコーダーのセッション横断のテレメトリ状態をリセットさせるメッセージを送る。
- 触るとき: 前のセッションの計測状態が次のセッションに持ち越される不具合を調べる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.startTrackingBuiltBounce()
- 位置: L92-97
- 役割: 子で作ったバウンス情報を親へ渡し、親側で追跡を開始させる。
- 触るとき: ページが閉じた後もバウンス計測が続く必要のある経路で、追跡が途切れていないか確かめる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordSearchMode()
- 位置: L105-110
- 役割: 検索モードに入った情報 (searchMode) を親の recordSearchMode へ送る。
- 触るとき: 検索モードへの入場が計測に出ない時、または検索モードの送信項目を変える時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordAutofillBackspace()
- 位置: L118-123
- 役割: バックスペースで消されたオートフィル結果の URL を親へ送る。
- 触るとき: オートフィル後のバックスペースが計測されない時や、親側のバックスペース管理を調べる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordAutofillDeletion()
- 位置: L129-133
- 役割: オートフィルの削除を親へ通知する。URL は渡さない。
- 触るとき: オートフィル削除の計測値が content と親で食い違う時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.dismissAutofill()
- 位置: L136-142
- 役割: オートフィルの却下を sendQuery で親へ問い合わせ、その結果を返す。
- 触るとき: オートフィル候補を却下した後の動作が親と content でずれる時。
- 呼び出し先: `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.clearAutofillBackspaceEntryForUrl()
- 位置: L151-156
- 役割: 採用されたオートフィル結果の URL について、親側のバックスペース記録を消させる。
- 触るとき: オートフィルを採用した後もバックスペース記録が残って誤って計測される時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.handleAutofillReintegration()
- 位置: L164-169
- 役割: オートフィルの再統合 (再びオートフィルすること) を親へ依頼する。
- 触るとき: 入力を戻した時にオートフィルが再び効かない問題を、content 経路から調べる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordSearchForm()
- 位置: L177-182
- 役割: 検索エンジンのフォームを訪れたことを engineName で親へ送り、親がエンジンを解決する。
- 触るとき: 検索フォーム訪問の計測が親に届かない時や、送る項目を変える時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordSearch()
- 位置: L190-195
- 役割: 検索の記録 options を展開して親の RecordSearch へ送る。
- 触るとき: 検索テレメトリの項目を追加し、content 経路からも送られるようにする時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordSearchInOpenedTab()
- 位置: L204-209
- 役割: 新しいタブで開いた検索を searchData と共に親へ送り、親側でそのタブの browser を解決させる。
- 触るとき: 新規タブでの検索が通常の検索と別に計上されるかを確かめる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordZeroPrefix()
- 位置: L218-223
- 役割: ゼロプレフィックス (入力前の候補表示) のイベント種別 kind を親へ送る。
- 触るとき: 入力前の候補表示の計測値がずれる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.checkKeywordURIFixup()
- 位置: L234-240
- 役割: 単語だけの入力に対する URI fixup の DNS 確認を親側で実行させる。browserId が null なら選択中のブラウザ。
- 触るとき: 単語だけの入力を検索にするか URL にするかの判定が content 経路で違う時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy._lastQueryContextWrapper()
- 位置: L243-245
- 役割: 直近のクエリ文脈を包んだ値を返す getter。
- 触るとき: キーボード操作や却下処理が直前のクエリを参照するとき、その値が正しいかを確かめる時。
- 参照: `this.#lastQueryContextWrapper`

## UrlbarParentControllerProxy.startQuery()
- 位置: L257-277
- 役割: 親でクエリを開始し、完了まで待って最終結果を持つ UrlbarQueryContext を返す。中断時は開始時の文脈を返す。
- 触るとき: content 側でクエリ完了を await する箇所の挙動や、AbortError 時の扱いを変える時。
- 呼び出し先: `UrlbarQueryContext.fromWire()`, `queryContext.toWire()`, `this.#port .sendQuery()`, `this.#port .sendQuery("StartQuery", { instanceId: this.#instanceId, queryContext: queryContext.toWire(), }) .then()`
- 参照: `error?.name`, `this.#instanceId`, `this.#lastQueryContextWrapper`

## UrlbarParentControllerProxy.getHeuristicResult()
- 位置: async L286-292
- 役割: 親で heuristic 結果を求め、wire 形式から UrlbarResult に戻して返す。無ければ null。
- 触るとき: Enter で選ばれる既定候補が content 側で取れない不具合を見る時。
- 呼び出し先: `UrlbarResult.fromWire()`, `queryContext.toWire()`, `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.resolveFallbackNavigation()
- 位置: async L301-309
- 役割: 選べる候補が無い Enter を親で解決させ、heuristicResult か fixup の結果を受け取る。
- 触るとき: 候補が無い状態の Enter 動作が親と content で食い違う時。
- 呼び出し先: `UrlbarResult.fromWire()`, `this.#port.sendQuery()`
- 参照: `outcome.heuristicResult`, `this.#instanceId`

## UrlbarParentControllerProxy.cancelQuery()
- 位置: L311-315
- 役割: 進行中のクエリをキャンセルする CancelQuery メッセージを親へ送る。
- 触るとき: 入力中に古いクエリの結果が残り続けるなど、キャンセルが効かない時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.speculativeConnect()
- 位置: L326-333
- 役割: 結果と文脈を親へ送り、接続の先読み (投機的接続) を依頼する。応答は待たない。
- 触るとき: 候補の接続先の先読みが効かない時や、先読みの理由を追加する時。
- 呼び出し先: `context.toWire()`, `result.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.loadURL()
- 位置: L342-347
- 役割: loadData を親へ送り、埋め込みブラウザで URL を読み込ませる。読み込み先の browserId を返す。
- 触るとき: 候補選択からの読み込みが content 側で始まらない時や、loadData の項目を増やす時。
- 呼び出し先: `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.focusBrowser()
- 位置: L356-361
- 役割: 遅延 Enter の読み込み先ブラウザを親で解決してフォーカスさせ、focused の結果を返す。
- 触るとき: 読み込み後にフォーカスがブラウザへ戻らない問題を調べる時。
- 呼び出し先: `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.switchToTab()
- 位置: L369-374
- 役割: 同じ URL のタブへ切り替える、またはタブを開く処理を、履歴・開いたタブの書き込みと共に親に依頼する。
- 触るとき: 既存のタブへ切り替えられず新しいタブが開いてしまう挙動を調べる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.addToInputHistory()
- 位置: L385-392
- 役割: 入力履歴 (URL と入力文字列の対応) を親で Places に書かせる。whenReady で書き込みを URL の登録後まで遅らせられる。
- 触るとき: 入力履歴が残らない時や、履歴を書くタイミングが早すぎる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.removeResult()
- 位置: L402-408
- 役割: 結果を親の removeResult に渡す。却下時は行の代わりに出す案内の l10n も渡せる。
- 触るとき: 候補を却下した後に案内の文言が出ない時や、削除の経路を変える時。
- 呼び出し先: `result.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.setLastQueryContextCache()
- 位置: L413-419
- 役割: 最後のクエリ文脈を完了済みとして内部に保持し、親にも同じキャッシュを作らせる。
- 触るとき: 直前の検索結果を再利用する時に結果が古い、または空になる時。
- 呼び出し先: `queryContext.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`, `this.#lastQueryContextWrapper`

## UrlbarParentControllerProxy.clearLastQueryContextCache()
- 位置: L421-426
- 役割: 内部と親の最後のクエリ文脈キャッシュを消す。
- 触るとき: 次の検索で前の検索の結果が表示されてしまう不具合を調べる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`, `this.#lastQueryContextWrapper`

## UrlbarParentControllerProxy.onBeforeSelection()
- 位置: L431-436
- 役割: 選択される直前の結果を親の onBeforeSelection へ通知する。
- 触るとき: 選択前のフックに依存するプロバイダーが content 経路で動かない時。
- 呼び出し先: `result.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.onSelection()
- 位置: L441-446
- 役割: 選ばれた結果を親の onSelection へ通知する。
- 触るとき: 選択時に親側のプロバイダーが反応しない時。
- 呼び出し先: `result.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.initEngineStore()
- 位置: L451-455
- 役割: 検索エンジンのストアを親で初期化させるメッセージを送り、送信の戻り値をそのまま返す。
- 触るとき: エンジン一覧が空のまま表示される時や、ストアの初期化タイミングを確かめる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.getEngineIconURL()
- 位置: L460-465
- 役割: エンジン ID に対するアイコン URL を親へ問い合わせ、その Promise を返す。
- 触るとき: 候補のエンジンアイコンが表示されない時。
- 呼び出し先: `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.markEngineAsUsed()
- 位置: L468-473
- 役割: エンジンが使われたことを親へ伝え、利用の記録を更新させる。
- 触るとき: エンジンの利用順や利用回数の反映がずれる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.openSERP()
- 位置: L476-485
- 役割: 検索結果ページ (SERP) を指定の場所・バックグラウンドの有無・ブラウザで開くよう親に依頼する。
- 触るとき: 検索語で結果ページを開く時の開き先 (背景タブなど) が期待と違う時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.openSearchForm()
- 位置: L488-496
- 役割: エンジンの検索フォームのページを指定の場所で開くよう親に依頼する。
- 触るとき: 検索フォームを開く操作に反応しない時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.openPreferences()
- 位置: L499-505
- 役割: 設定画面を paneID と追加の引数付きで親に開かせる。
- 触るとき: urlbar から設定の特定のペインへ飛ぶ経路を変える時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.openContainerCreationPanel()
- 位置: L508-513
- 役割: コンテナ作成パネルを entrypoint 付きで親に開かせる。
- 触るとき: コンテナ作成の入口ごとの計測を調べる時。
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`
