# browser/components/urlbar/content/UrlbarView.mjs

source: browser/components/urlbar/content/UrlbarView.mjs
source-hash: 625b58d963cfb10fd00ba44941433fb3c054f506
lines: 5058

## <module>
- 役割: アドレスバーの検索結果パネル UrlbarView を定義する。行の作成と更新、選択、キーボード操作、結果メニュー、パネルの開閉を担当する。

## getUniqueId()
- 位置: L44-46
- 役割: プレフィックスに連番を付けた行要素用の ID を返す。連番は 9999 で折り返す。
- 触るとき: 行の ID の形式を変えるとき、または行 ID を使った参照(aria の関連付けなど)が衝突していないか確かめるときに見る。

## UrlbarView.constructor()
- 位置: L88-120
- 役割: 入力欄とパネルの要素を取り込み、結果リストと結果メニューのイベントを登録し、コントローラーへの登録、クエリキャッシュ、L10n キャッシュ、折り返し監視を作る。
- 触るとき: ビューの初期化順序や、新しいイベントリスナーを付ける場所を決めるとき、またはパネルを開く前の状態で値が未設定になる原因を調べるときに見る。
- 呼び出し先: `this.#rows.addEventListener()`, `this.#updateOverflowState.bind()`, `this.controller.addListener()`, `this.controller.setView()`, `this.input.addEventListener()`, `this.input.toggleAttribute()`, `this.panel.querySelector()`, `this.resultMenu.addEventListener()`
- 参照: `input.controller`, `input.panel`, `this.#l10nCache`, `this.#overflowObserver`, `this.#rows`, `this.controller`, `this.input`, `this.panel`, `this.queryContextCache`, `this.resultMenu`

## UrlbarView.oneOffSearchButtons()
- 位置: L122-134
- 役割: メインのアドレスバーでだけ、ワンクリック検索ボタン(UrlbarSearchOneOffs)を遅れて生成して返す。他の入力欄では null を返す。
- 触るとき: ワンクリック検索ボタンを出す条件を変えるとき、またはスマートバーなど別の入力欄で検索ボタンが出ない理由を調べるときに見る。
- 条件付き依存: `if (!this.#oneOffSearchButtons)` → `this.#oneOffSearchButtons.addEventListener()`
- 参照: `lazy.UrlbarSearchOneOffs`, `this.#oneOffSearchButtons`, `this.input.sapName`

## UrlbarView.chromeWindow()
- 位置: L141-143
- 役割: 入力欄が属する chrome ウィンドウを返す。
- 触るとき: gBrowser など chrome 側の API を呼ぶ箇所を書くとき、またはスマートバーで別ウィンドウを参照していないか確かめるときに見る。
- 参照: `this.input.window`

## UrlbarView.#currentPage()
- 位置: L152-154
- 役割: chrome ウィンドウの選択中タブの URL(currentURI.spec)を返す。ブラウザウィンドウ以外では undefined になる。
- 触るとき: 結果を再利用してよい判定の対象を変えるとき、またはタブのドラッグ中に URL が取れず結果が表示されない原因を調べるときに見る。
- 参照: `this.chromeWindow.gBrowser?.currentURI?.spec`

## UrlbarView.#canReuseResults()
- 位置: L166-171
- 役割: クエリの検索語が現在の入力値と同じで、かつ現在のページも同じときに true を返し、結果の再利用を許す。
- 触るとき: 古い結果を表示しないための条件を変えるとき、またはタブを切り替えた後に前のページの結果が残って見える原因を調べるときに見る。
- 参照: `queryContext.currentPage`, `queryContext.searchString`, `this.#currentPage`, `this.input.value`

## UrlbarView.isOpen()
- 位置: L178-180
- 役割: 入力欄に open 属性があるかどうかで、パネルが開いているかを返す。
- 触るとき: パネルの開閉状態に依存する処理を書くとき、または閉じているのに選択が動く原因を調べるときに見る。
- 呼び出し先: `this.input.hasAttribute()`

## UrlbarView.queryContext()
- 位置: L185-187
- 役割: 最新のクエリのコンテキストを返す。
- 触るとき: 直前の検索の状態を参照する処理を書くとき、または古いクエリの結果が表示されていないか確かめるときに見る。
- 参照: `this.#queryContext`

## UrlbarView.allowEmptySelection()
- 位置: L189-192
- 役割: ヒューリスティック結果がないか、表示されていない場合に true を返し、何も選ばれていない状態を許す。
- 触るとき: Enter で先頭の結果を選ばせるかどうかを変えるとき、または先頭結果が選択されない理由を調べるときに見る。
- 呼び出し先: `this.#shouldShowHeuristic()`
- 参照: `this.#queryContext`

## UrlbarView.selectedRowIndex()
- 位置: L194-206
- 役割: getter として、パネルが開いていれば選択中の行の rowIndex を返し、選択が無ければ -1 を返す。
- 触るとき: 外部から選択位置を読む処理を書くとき、または選択位置が表示上の行の並びとずれる原因を調べるときに見る。
- 呼び出し先: `this.#getSelectedRow()`
- 参照: `selectedRow.result.rowIndex`, `this.isOpen`

## UrlbarView.selectedRowIndex()
- 位置: L208-236
- 役割: setter として、パネルが開いていれば表示中の行の中から指定番目の行の最初の選択可能な要素を選ぶ。負の値なら選択を解除し、範囲外なら例外を投げる。
- 触るとき: 外部から行を選ぶ処理を変えるとき、または範囲外のエラーが出る箇所を調べるときに見る。
- 呼び出し先: `Array.from()`, `Array.from(this.#rows.children).filter()`, `this.#getNextSelectableElement()`, `this.#getRowFromElement()`, `this.#isElementVisible()`, `this.#selectElement()`
- 条件付き依存: `if (val < 0)` → `this.#selectElement()`
- 参照: `items.length`, `this.#rows.children`, `this.isOpen`

## UrlbarView.selectedElementIndex()
- 位置: L238-244
- 役割: パネルが開いていて選択中の要素があれば、その elementIndex を返す。無ければ -1 を返す。
- 触るとき: 要素の番号付けを使う処理を書くとき、または選択要素の番号が更新されない原因を調べるときに見る。
- 参照: `this.#selectedElement`, `this.#selectedElement.elementIndex`, `this.isOpen`

## UrlbarView.selectedResult()
- 位置: L250-256
- 役割: パネルが開いていれば選択中の行の結果を返し、閉じていれば null を返す。
- 触るとき: Enter などで実行される結果を取り出す箇所を変えるとき、または選択中の結果が古いままになる原因を調べるときに見る。
- 呼び出し先: `this.#getSelectedRow()`
- 参照: `this.#getSelectedRow()?.result`, `this.isOpen`

## UrlbarView.selectedElement()
- 位置: L262-268
- 役割: パネルが開いていれば選択中の要素を返し、閉じていれば null を返す。
- 触るとき: 要素単位で操作する処理を書くとき、またはボタンへのキー操作が効かない原因を調べるときに見る。
- 参照: `this.#selectedElement`, `this.isOpen`

## UrlbarView.shouldSpaceActivateSelectedElement()
- 位置: L275-293
- 役割: 選択中が結果メニューなら true を返す。ボタンを選んでいて入力欄が空の場合も true を返し、それ以外は false を返す。
- 触るとき: スペースキーの動作を変えるとき、または検索語に空白を入れられない原因を調べるときに見る。
- 呼び出し先: `this.selectedElement?.getAttribute()`
- 参照: `this.input.value`, `this.selectedElement?.dataset.name`

## UrlbarView.clearSelection()
- 位置: L298-300
- 役割: ビューの開閉に関係なく選択を解除する。入力欄の値は変えない。
- 触るとき: 入力内容を残したまま選択だけ外したい箇所を書くとき、または選択が残り続ける原因を調べるときに見る。
- 呼び出し先: `this.#selectElement()`

## UrlbarView.visibleRowCount()
- 位置: L308-314
- 役割: 表示中の行の数を数えて返す。古い結果が残っている間は、クエリの件数より多くなることがある。
- 触るとき: 表示中の行数に依存する処理を書くとき、または件数が古い結果を含んでずれる原因を調べるときに見る。
- 呼び出し先: `Number()`, `this.#isElementVisible()`
- 参照: `this.#rows.children`

## UrlbarView.getResultFromElement()
- 位置: L325-329
- 役割: 結果メニューの項目なら最後に開いた結果メニューの対象の結果を、それ以外は要素が属する行の結果を返す。
- 触るとき: クリックされた要素から結果を求める処理を変えるとき、または結果メニューの操作が別の結果に効いてしまう原因を調べるときに見る。
- 呼び出し先: `element?.classList.contains()`, `this.#getRowFromElement()`
- 参照: `this.#getRowFromElement(element)?.result`, `this.#resultMenuResult`

## UrlbarView.telemetryTypeFromElement()
- 位置: L339-356
- 役割: 要素が無ければ "none"、ヘルプやリンクなら "help"、dismiss なら "block"、アクションボタンなら "action" を返す。それ以外は結果から求めた種類を返す。
- 触るとき: 要素ごとの計測名を追加・変更するとき、または計測に出る種類が想定と違う理由を調べるときに見る。
- 呼び出し先: `element.classList?.contains()`, `this.telemetryTypeFromResult()`
- 参照: `element.dataset.command`, `element.dataset.l10nName`

## UrlbarView.telemetryTypeFromResult()
- 位置: L364-459
- 役割: 結果の種類と提供元から計測用の種類名(switchtab、searchengine、bookmark、history、quicksuggest など)を返す。該当が無ければ "unknown"。
- 触るとき: 新しい結果の種類に計測名を付けるとき、または計測で "unknown" が増えた原因を調べるときに見る。
- 条件付き依存: `if (!type)` → `console.error()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.ACTION`, `UrlbarShared.RESTRICT_TOKENS.BOOKMARK`, `UrlbarShared.RESTRICT_TOKENS.HISTORY`, `UrlbarShared.RESTRICT_TOKENS.OPENPAGE`, `UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `result.autofill`, `result.autofill.type`, `result.heuristic`, `result.isRichSuggestion`, `result.payload.keyword`, `result.payload.suggestion`, `result.payload.trending`, `result.providerName`, `result.source`, `result.type`

## UrlbarView.getResultAtIndex()
- 位置: L468-478
- 役割: パネルが開いていて指定の位置に行があれば、その行の結果を返す。無ければ null を返す。
- 触るとき: 番号で結果を取り出す処理を書くとき、または閉じている間に null が返る理由を調べるときに見る。
- 参照: `this.#rows.children`, `this.#rows.children.length`, `this.#rows.children[index].result`, `this.isOpen`

## UrlbarView.resultIsSelected()
- 位置: L484-490
- 役割: 選択中の行番号と結果の rowIndex が一致するかを返す。選択が無ければ false を返す。
- 触るとき: 結果ごとに選択表示を切り替えるとき、または選択表示が実際の選択とずれる原因を調べるときに見る。
- 参照: `result.rowIndex`, `this.selectedRowIndex`

## UrlbarView.selectBy()
- 位置: L504-613
- 役割: Tab 以外では行単位、Tab では要素単位で選択を前後に動かす。端に来たときは allowEmptySelection に従って選択を外すか先頭と末尾へ戻す。操作前に検索を止める。
- 触るとき: 上下キーや Tab での選択移動の順序や端の扱いを変えるとき、または選択が飛ぶ・止まる不具合を調べるときに見る。
- 呼び出し先: `isSkippableTabToSearchAnnounce()`, `this.#getNextSelectableElement()`, `this.#getPreviousSelectableElement()`, `this.#selectElement()`, `this.getFirstSelectableElement()`, `this.getLastSelectableElement()`
- 条件付き依存: `if (!this.input.eventBufferer.isDeferringEvents)` → `this.controller.cancelQuery()`
- 条件付き依存: `if (this.allowEmptySelection)` → `this.#selectElement()`
- 条件付き依存: `if (selectedRowIndex != -1)` → `Math.min()`
- 条件付き依存: `if (selectedRowIndex != -1)` → `Math.max()`
- 条件付き依存: `if (!userPressedTab)` → `this.#isRowArrowSelectable()`
- 条件付き依存: `if (!selectedElement)` → `this.#selectElement()`
- 条件付き依存: `if (!selectedElement)` → `isSkippableTabToSearchAnnounce()`
- 条件付き依存: `if (endReached)` → `this.#selectElement()`
- 条件付き依存: `if (endReached)` → `isSkippableTabToSearchAnnounce()`
- 参照: `this.#selectedElement`, `this.allowEmptySelection`, `this.input.eventBufferer.isDeferringEvents`, `this.isOpen`, `this.selectedRowIndex`, `this.visibleRowCount`

## isSkippableTabToSearchAnnounce()
- 位置: L552-564
- 役割: Tab でタブで検索の結果に移るとき、読み上げで既に案内済みなら aria-activedescendant を設定しないよう判定する。一度 skip した後は skip しない。
- 触るとき: タブで検索の結果に移ったときの読み上げを変えるとき、または不要な選択通知が出る原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `this.getResultFromElement()`
- 参照: `result?.providerName`, `this.#announceTabToSearchOnSelection`

## UrlbarView.acknowledgeFeedback()
- 位置: async L618-635
- 役割: 指定 ID の行に「フィードバックを受け付けた」旨の文言を属性として付け、同じ文言をスクリーンリーダーにも通知する。文言の取得中に行の結果が変わっていれば何もしない。
- 触るとき: フィードバック確認の文言や通知の仕方を変えるとき、または確認が表示されない原因を調べるときに見る。
- 呼び出し先: `row._content.closest()`, `row._content.closest("[role=option]").ariaNotify()`, `row.setAttribute()`, `this.#getRowByResultId()`, `this.#l10nCache.ensure()`, `this.#l10nCache.get()`
- 参照: `row.result?.id`

## UrlbarView.#acknowledgeDismissal()
- 位置: L645-684
- 役割: 非表示にした結果の行を、非表示の確認ヒント(TIP)の行に置き換える。選択中なら先に選択を外し、置き換え後に確認ボタンへ選択を移す。
- 触るとき: 非表示後の確認表示を変えるとき、または非表示の直後に選択がおかしくなる原因を調べるときに見る。
- 呼び出し先: `this.#getRowByResultId()`, `this.#getSelectedRow()`, `this.#rowLabel()`, `this.#setRowSelectable()`, `this.#updateIndices()`, `this.#updateRow()`
- 条件付き依存: `if (isSelected)` → `this.#selectElement()`
- 条件付き依存: `if (isSelected)` → `this.#getNextSelectableElement()`
- 参照: `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.TIP`, `result.hideRowLabel`, `result.id`

## UrlbarView.removeAccessibleFocus()
- 位置: L686-688
- 役割: アクセシブルフォーカスの設定を外す(null を設定する)。
- 触るとき: フォーカスの表示をリセットしたい箇所を書くとき、またはフォーカス枠が残る原因を調べるときに見る。
- 呼び出し先: `this.#setAccessibleFocus()`

## UrlbarView.clear()
- 位置: L690-696
- 役割: 結果リストを空にし、actionmode を外して noresults を立て、選択と表示中の結果の一覧を消す。
- 触るとき: 結果を全て消す挙動を変えるとき、または空にしても残る状態を調べるときに見る。
- 呼び出し先: `this.#rows.toggleAttribute()`, `this.clearSelection()`, `this.input.toggleAttribute()`
- 参照: `this.#rows.textContent`, `this.visibleResults`

## UrlbarView.close()
- 位置: L707-770
- 役割: 必要ならクエリを止めてパネルを閉じる。検索モードのプレビューを戻し、aria-expanded を false にし、VIEW_CLOSE を通知し、作った blob URL を破棄する。ゼロ入力の場合は記録も行う。
- 触るとき: パネルの閉じ方や後始末(検索モードの復元、blob の破棄、計測)を変えるとき、または閉じた後も状態が残る原因を調べるときに見る。
- 呼び出し先: `getBoundsWithoutFlushing()`, `this.#stopTail150()`, `this.controller.cancelQuery()`, `this.controller.notify()`, `this.input.inputField.setAttribute()`, `this.input.toggleAttribute()`, `this.removeAccessibleFocus()`, `this.resultMenu.hide()`, `window.removeEventListener()`
- 条件付き依存: `if (!elementPicked && showFocusBorder)` → `this.input.removeAttribute()`
- 条件付き依存: `if (!this.isOpen)` → `this.input.updatePopover()`
- 条件付き依存: `if (!this.input.focused && !elementPicked)` → `this.controller.engagementEvent.discard()`
- 条件付き依存: `if (this.#blobUrlsByResultUrl)` → `this.#blobUrlsByResultUrl.values()`
- 条件付き依存: `if (this.#blobUrlsByResultUrl)` → `URL.revokeObjectURL()`
- 条件付き依存: `if (this.#blobUrlsByResultUrl)` → `this.#blobUrlsByResultUrl.clear()`
- 条件付き依存: `if (isShowingZeroPrefix)` → `this.controller.parentController.recordZeroPrefix()`
- 参照: `UrlbarShared.NOTIFICATIONS.VIEW_CLOSE`, `getBoundsWithoutFlushing( this.input.parentElement ).width`, `this.#blobUrlsByResultUrl`, `this.#containerWidthOnLastClose`, `this.#openPanelInstance`, `this.#previousTabToSearchEngine`, `this.#queryContext`, `this.#queryContext.searchString`, `this.input.focused`, `this.input.parentElement`, `this.input.searchMode`, `this.input.searchMode?.isPreview`, `this.input.userTypedValue`, `this.isOpen`

## UrlbarView.startTail150()
- 位置: L772-799
- 役割: 入力欄の上に 400px のキャンバスを重ねて隠しゲーム(tail150)を起動する。すでに起動中なら何もしない。
- 触るとき: 隠しゲームの表示や起動の条件を変えるとき、または入力欄の上にオーバーレイが残る原因を調べるときに見る。
- 呼び出し先: `canvas.getContext()`, `closeBtn.addEventListener()`, `closeBtn.setAttribute()`, `ctx.scale()`, `document.createElement()`, `overlay.append()`, `overlay.setAttribute()`, `overlay.showPopover()`, `this.#runTail150()`, `this.close()`, `this.input.appendChild()`
- 参照: `canvas.className`, `canvas.height`, `canvas.width`, `closeBtn.className`, `overlay.className`, `this.#tail150`, `window.devicePixelRatio`

## UrlbarView.#stopTail150()
- 位置: L801-810
- 役割: ゲームのキー監視を外し、オーバーレイを削除して、ゲームの状態を null に戻す。
- 触るとき: ゲームを閉じるときの後始末を変えるとき、またはキー入力が残り続ける原因を調べるときに見る。
- 呼び出し先: `this.#tail150.overlay.remove()`
- 条件付き依存: `if (this.#tail150.keyHandler)` → `window.removeEventListener()`
- 参照: `this.#tail150`, `this.#tail150.keyHandler`

## UrlbarView.#runTail150()
- 位置: L812-820
- 役割: キャンバスにゲームの描画を行い、蛇の移動、食べ物の配置、キー操作を動かす。実体は直後の無名の即時実行関数(行 819)にある。
- 触るとき: 隠しゲームの動きや描画を変えるとき、または速度や操作の挙動を調べるときに見る。
- 呼び出し先: `S.getPropertyValue()`, `W.addEventListener()`, `X.fillText()`, `c.getContext()`, `window.getComputedStyle()`
- 参照: `SP.src`, `X.fillStyle`, `X.font`, `X.textAlign`, `this.#tail150.keyHandler`, `window.Image`

## A()
- 位置: L819-819
- 役割: requestAnimationFrame に渡してフレームごとの更新を予約する短い関数。
- 触るとき: 隠しゲームのフレーム更新の仕組みを追うとき、またはフレーム間隔を変えるときに見る。
- 呼び出し先: `W.requestAnimationFrame()`

## CA()
- 位置: L819-819
- 役割: 指定の座標と半径で円を塗る。食べ物と蛇の体の描画に使う。
- 触るとき: 隠しゲームの食べ物や体の見た目を変えるとき、に見る。
- 呼び出し先: `X.arc()`, `X.beginPath()`, `X.fill()`

## g()
- 位置: L819-819
- 役割: 0 から 19 の乱数整数を返す。本文中では呼ばれていない(要確認)。
- 触るとき: 乱数で盤面の位置を決める箇所を増やすとき、に見る。
- 呼び出し先: `Math.random()`

## GO()
- 位置: L819-819
- 役割: ゲーム終了時に、引数の文言と得点を画面に描き、ゲームの実行状態を止める。
- 触るとき: ゲームオーバーの表示文言や位置を変えるとき、に見る。
- 呼び出し先: `X.fillText()`
- 参照: `X.fillStyle`, `X.shadowBlur`, `X.shadowColor`

## PF()
- 位置: L819-819
- 役割: 蛇の体と重ならない 20x20 の盤面の空きマスをランダムに選んで食べ物の位置にする。空きが無ければ GO("GG") を呼ぶ。
- 触るとき: 食べ物の出現位置の決め方を変えるとき、またはゲームが終わる条件を調べるときに見る。
- 呼び出し先: `GO()`, `Math.random()`, `a.push()`, `s.every()`
- 参照: `$.x`, `$.y`, `a.length`

## I()
- 位置: L819-819
- 役割: ゲームを初期化する。長さ 8 の蛇を (10,10) の周辺に置き、進行方向を右、得点を 0、食べ物を (15,15) に設定してループ L を開始する。
- 触るとき: ゲームの開始時の配置や初期速度を変えるとき、に見る。
- 呼び出し先: `A()`, `Array()`, `[...Array(8)].map()`

## L()
- 位置: L819-819
- 役割: フレームごとに呼ばれる更新関数。100ms ごとに蛇を 1 マス進め、壁か自分に当たると GO("GAME OVER") で終了し、食べ物を食べると得点を増やして置き直す。描画もここで行う。
- 触るとき: ゲームの速度、衝突判定、得点の加算を変えるとき、に見る。
- 呼び出し先: `A()`, `CA()`, `Math.max()`, `Math.min()`, `X.clearRect()`, `X.restore()`, `X.save()`, `X.translate()`, `s.map()`
- 条件付き依存: `if (p>=1)` → `s.some()`
- 条件付き依存: `if (t.x<0||t.x>19||t.y<0||t.y>19||s.some($=>$.x==t.x&&$.y==t.y))` → `GO()`
- 条件付き依存: `if (p>=1)` → `s.unshift()`
- 条件付き依存: `if (p>=1)` → `PF()`
- 条件付き依存: `if (p>=1)` → `s.pop()`
- 条件付き依存: `if (X.save(),X.translate(Math.min(390,Math.max(10,20*($.x+(!t&&d[0]*p))+10)),Math.min(390,Math.max(10,20*($.y+(!t&&d[1]*p))+10))),t)` → `CA()`
- 条件付き依存: `if (!(X.save(),X.translate(Math.min(390,Math.max(10,20*($.x+(!t&&d[0]*p))+10)),Math.min(390,Math.max(10,20*($.y+(!t&&d[1]*p))+10))),t))` → `X.drawImage()`
- 参照: `$.x`, `$.y`, `SP.complete`, `X.fillStyle`, `f.x`, `f.y`, `s.length`, `s[0].x`, `s[0].y`, `t.x`, `t.y`, `this.#tail150`

## this.#tail150.keyHandler()
- 位置: L819-819
- 役割: キー入力を処理する。Esc 以外のキーは既定の動作を止め、矢印キーで進行方向を変える(真逆の向きは無視する)。停止中に矢印キーを押すとゲームを始める。
- 触るとき: ゲームの操作キーを変えるとき、または Esc での閉じ方や矢印キーが他の操作と干渉する原因を調べるときに見る。
- 呼び出し先: `$.preventDefault()`, `$.stopPropagation()`, `I()`
- 参照: `$.keyCode`

## UrlbarView.autoOpen()
- 位置: L837-950
- 役割: 利用者の操作に応じてパネルを開き、前の結果を再利用するか新しい検索を始める。入力が空か固定ページなら mousedown と command でトップサイトを開き、入力がある場合はフォーカス中だけ前の検索を再開する。
- 触るとき: 入力欄を押したときにパネルがどう出るか、前の検索を再開する条件を変えるとき、またはパネルのちらつきの原因を調べるときに見る。
- 呼び出し先: `getBoundsWithoutFlushing()`, `this.#canReuseResults()`, `this.#pickSearchTipIfPresent()`, `this.controller.engagementEvent.discard()`, `this.input.getAttribute()`, `this.input.startQuery()`
- 条件付き依存: `if ( !this.input.value || this.input.getAttribute("pageproxystate") == "valid" )` → `["mousedown", "command"].includes()`
- 条件付き依存: `if (!this.input.searchMode && this.queryContextCache.topSitesContext)` → `this.onQueryResults()`
- 条件付き依存: `if (!this.isOpen && ["mousedown", "command"].includes(event.type))` → `this.input.startQuery()`
- 条件付き依存: `if (suppressFocusBorder)` → `this.input.toggleAttribute()`
- 条件付き依存: `if (!( this.#rows.firstElementChild && this.#canReuseResults(this.#queryContext) && this.#containerWidthOnLastClose == getBoundsWithoutFlushing(this.input.parentEl...))` → `this.queryContextCache.get()`
- 条件付き依存: `if (cachedQueryContext)` → `this.onQueryResults()`
- 条件付き依存: `if (this.input.sapName == "urlbar")` → `this.input.getBrowserState()`
- 条件付き依存: `if ( this.#queryContext?.results?.length && this.#canReuseResults(this.#queryContext) && this.#queryContext.results[0].type != UrlbarShared.RESULT_TYPE.TIP )` → `this.#openPanel()`
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `event.type`, `getBoundsWithoutFlushing(this.input.parentElement).width`, `queryOptions.allowAutofill`, `queryOptions.autofillIgnoresSelection`, `queryOptions.interactionType`, `queryOptions.searchString`, `state.persist?.shouldPersist`, `this.#containerWidthOnLastClose`, `this.#currentPage`, `this.#queryContext`, `this.#queryContext.allowAutofill`, `this.#queryContext.results`, `this.#queryContext.results[0].type`, `this.#queryContext?.results?.length`, `this.#rows.firstElementChild`, `this.chromeWindow.gBrowser.selectedBrowser`, `this.input.focused`, `this.input.inOverflowPanel`, `this.input.parentElement`, `this.input.readOnly`, `this.input.sapName`, `this.input.searchMode`, `this.input.value`, `this.isOpen`, `this.queryContextCache.topSitesContext`

## UrlbarView.onQueryStarted()
- 位置: L960-975
- 役割: 検索開始時に、キャンセルと更新のフラグを戻し、古い行を消すタイマーを始め、L10n 文字列を先読みする。
- 触るとき: 検索開始時の初期化や古い行を消すタイミングを変えるとき、に見る。
- 呼び出し先: `this.#cacheL10nStrings()`, `this.#startRemoveStaleRowsTimer()`
- 参照: `queryContext.searchString`, `this.#openPanelInstance`, `this.#previousTabToSearchEngine`, `this.#queryUpdatedResults`, `this.#queryWasCancelled`

## UrlbarView.onQueryCancelled()
- 位置: L980-983
- 役割: 検索がキャンセルされたことを記録し、古い行を消すタイマーを止める。
- 触るとき: キャンセル後に結果を残すか消すかを変えるとき、に見る。
- 呼び出し先: `this.#cancelRemoveStaleRowsTimer()`
- 参照: `this.#queryWasCancelled`

## UrlbarView.onQueryFinished()
- 位置: L991-1039
- 役割: キャンセルされていなければ、結果がある時は古い行を消し、無い時は全て消す。ゼロ入力では露出を記録し、結果が無く検索モードでもなければパネルを閉じる。検索モードで結果が無い時は、ワンクリックボタンを出せる場合だけパネルを開く。
- 触るとき: 検索完了後にパネルを開くか閉じるかの判定を変えるとき、または結果が無いのにパネルが残る原因を調べるときに見る。
- 呼び出し先: `(oneOffs?.willHide() ?? Promise.resolve(true)).then()`, `Promise.resolve()`, `oneOffs.enable()`, `oneOffs?.willHide()`, `this.#cancelRemoveStaleRowsTimer()`, `this.#openPanel()`
- 条件付き依存: `if (this.#queryUpdatedResults)` → `this.#removeStaleRows()`
- 条件付き依存: `if (!(this.#queryUpdatedResults))` → `this.clear()`
- 条件付き依存: `if (!queryContext.searchString)` → `this.controller.parentController.recordZeroPrefix()`
- 条件付き依存: `if (!this.input.searchMode)` → `this.close()`
- 条件付き依存: `if (this.isOpen)` → `this.close()`
- 参照: `queryContext.searchString`, `this.#openPanelInstance`, `this.#queryUpdatedResults`, `this.#queryWasCancelled`, `this.input.searchMode`, `this.isOpen`, `this.oneOffSearchButtons`

## UrlbarView.onQueryResults()
- 位置: L1047-1169
- 役割: 届いた結果をキャッシュに入れて行を更新する。初回なら選択を解除してワンクリックボタンを出し、先頭が見出し候補なら選択し、そうでなければ入力欄に結果を反映する。tab-to-search の読み上げを出し、必要ならパネルを開く。
- 触るとき: 結果が届いたときの表示更新の順序や、先頭の結果が選ばれる条件を変えるとき、または結果の表示が遅れる原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `this.#openPanel()`, `this.#updateResults()`, `this.queryContextCache.put()`
- 条件付き依存: `if (!this.isOpen)` → `this.clear()`
- 条件付き依存: `if (this.input.searchMode?.source == UrlbarShared.RESULT_SOURCE.ACTIONS)` → `this.#rows.toggleAttribute()`
- 条件付き依存: `if (queryContext.lastResultCount == 0)` → `this.#selectElement()`
- 条件付き依存: `if (queryContext.lastResultCount == 0)` → `this.oneOffSearchButtons?.enable()`
- 条件付き依存: `if (firstResult.heuristic)` → `this.#shouldShowHeuristic()`
- 条件付き依存: `if (this.#shouldShowHeuristic(firstResult))` → `this.#selectElement()`
- 条件付き依存: `if (this.#shouldShowHeuristic(firstResult))` → `this.getFirstSelectableElement()`
- 条件付き依存: `if (!(this.#shouldShowHeuristic(firstResult)))` → `this.input.setResultForCurrentValue()`
- 条件付き依存: `if ( firstResult.payload.providesSearchMode && queryContext.trimmedSearchString != "@" )` → `this.input.setResultForCurrentValue()`
- 条件付き依存: `if ( secondResult?.providerName == "UrlbarProviderTabToSearch" && UrlbarPrefs.get("accessibility.tabToSearch.announceResults") && this.#previousTabToSearchEngine...)` → `this.#ariaNotifyLocalizedString()`
- 条件付き依存: `if (this.#selectedElement && !this.oneOffSearchButtons?.selectedButton)` → `this.input.inputField.getAttribute()`
- 条件付き依存: `if (this.#selectedElement && !this.oneOffSearchButtons?.selectedButton)` → `document.getElementById()`
- 条件付き依存: `if (aadID && !document.getElementById(aadID))` → `this.#setAccessibleFocus()`
- 条件付き依存: `if (firstResult.heuristic)` → `this.input.formatValue()`
- 条件付き依存: `if (queryContext.deferUserSelectionProviders.size)` → `queryContext.results.forEach()`
- 条件付き依存: `if (queryContext.deferUserSelectionProviders.size)` → `queryContext.deferUserSelectionProviders.delete()`
- 条件付き依存: `if (UrlbarPrefs.get("unifiedSearchButton.always"))` → `this.input.searchModeSwitcher?.updateSearchIcon()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.SEARCH`, `UrlbarShared.RESULT_SOURCE.ACTIONS`, `firstResult.heuristic`, `firstResult.payload.providesSearchMode`, `firstResult.providerName`, `queryContext.deferUserSelectionProviders.size`, `queryContext.lastResultCount`, `queryContext.results`, `queryContext.trimmedSearchString`, `queryContext.trimmedSearchString.length`, `r.providerName`, `secondResult.payload.engine`, `secondResult.payload.isGeneralPurposeEngine`, `secondResult?.providerName`, `this.#announceTabToSearchOnSelection`, `this.#previousTabToSearchEngine`, `this.#queryContext`, `this.#queryUpdatedResults`, `this.#rows.children`, `this.#selectedElement`, `this.controller.userSelectionBehavior`, `this.input.searchMode?.source`, `this.isOpen`, `this.oneOffSearchButtons?.selectedButton`

## UrlbarView.onQueryResultRemoved()
- 位置: L1183-1225
- 役割: 指定 ID の行を探す。確認の文言があれば非表示の確認行に置き換え、無ければ行を削除して選択を同じ位置の次の行へ移す。行が無くなればパネルを閉じる。
- 触るとき: 結果を削除した後の選択位置を変えるとき、または削除後に選択が消えたり飛んだりする原因を調べるときに見る。
- 呼び出し先: `rowToRemove.remove()`, `this.#getSelectedRow()`, `this.#updateIndices()`
- 条件付き依存: `if (acknowledgeDismissalL10n)` → `this.#acknowledgeDismissal()`
- 条件付き依存: `if (updateSelection)` → `Math.min()`
- 条件付き依存: `if (!this.#rows.children.length)` → `this.close()`
- 参照: `this.#rows.children`, `this.#rows.children.length`, `this.#rows.children[i].result?.id`, `this.selectedRowIndex`

## UrlbarView.openResultMenu()
- 位置: L1227-1233
- 役割: 対象の結果を記録し、ResultMenuTriggered イベントを付けて結果メニューを開く。
- 触るとき: 結果メニューを開く経路を変えるとき、またはメニューが別の結果に結び付く原因を調べるときに見る。
- 呼び出し先: `this.resultMenu.toggle()`
- 参照: `this.#resultMenuResult`

## UrlbarView.updateResultMenuCommands()
- 位置: L1247-1254
- 役割: ID で行を探し、その結果のメニュー項目を差し替えて、メニュー項目の古いキャッシュを消す。
- 触るとき: 表示回数の上限到達などでメニュー項目を後から更新するとき、に見る。
- 呼び出し先: `this.#getRowByResultId()`, `this.#resultMenuCommands.delete()`
- 参照: `row.result`, `row.result.commands`

## UrlbarView.handleEvent()
- 位置: L1262-1269
- 役割: DOM イベントを on_<イベント種別> のメソッドへ振り分ける。対応するメソッドが無いイベントは例外を投げる。
- 触るとき: view で新しいイベントを受けるとき、または Unrecognized UrlbarView event のエラーが出た原因を調べるときに見る。
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.type`

## UrlbarView.isResultMenuOpen()
- 位置: L1271-1273
- 役割: 結果メニューに open 属性があるかどうかを返す。
- 触るとき: メニューが開いている間だけ動く処理を書くとき、またはメニュー表示中の挙動を調べるときに見る。
- 呼び出し先: `this.resultMenu.hasAttribute()`

## UrlbarView.#selectedElement()
- 位置: L1313-1317
- 役割: getter として、選択中の要素が DOM に接続されていれば返し、外れていれば null を返す。
- 触るとき: 選択要素を参照する処理を書くとき、または DOM から外れた要素が選択されたままになる原因を調べるときに見る。
- 参照: `this.#rawSelectedElement`, `this.#rawSelectedElement?.isConnected`

## UrlbarView.#showsActionLabels()
- 位置: L1325-1327
- 役割: getter として、入力欄が検索バーでなければ true を返す。検索バーでは行に操作ラベルを出さない。
- 触るとき: 行の操作ラベル(「〜で検索」など)を出す条件を変えるとき、に見る。
- 参照: `this.input.sapName`

## UrlbarView.#openPanel()
- 位置: L1329-1357
- 役割: スマートウィンドウのサイドバーでは何もしない。開いていればポップオーバーを更新し、閉じていれば選択方式を none にし、属性を立て、リサイズとブラーを監視し、VIEW_OPEN を通知して他のポップアップを閉じる。
- 触るとき: パネルを開くときの準備や属性を変えるとき、またはパネルが開かない原因や開いた直後に他のポップアップが閉じる理由を調べるときに見る。
- 呼び出し先: `this.#enableOrDisableRowWrap()`, `this.controller.notify()`, `this.input.inputField.setAttribute()`, `this.input.toggleAttribute()`, `this.maybeRollupPopups()`, `this.panel.removeAttribute()`, `window.addEventListener()`
- 条件付き依存: `if (this.isOpen)` → `this.input.updatePopover()`
- 参照: `UrlbarShared.NOTIFICATIONS.VIEW_OPEN`, `this.controller.userSelectionBehavior`, `this.input.isSidebarMode`, `this.isOpen`

## UrlbarView.maybeRollupPopups()
- 位置: L1364-1378
- 役割: closeOtherPanelsOnOpen が真でオーバーフローパネル内でなければ、ウィンドウ内の他のポップアップを全て閉じる。コンテンツ文書では何もしない。
- 触るとき: パネルを開くときに他のポップアップを閉じる挙動を変えるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if ( UrlbarPrefs.get("closeOtherPanelsOnOpen") && !this.input.inOverflowPanel )` → `window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsIAppWindow) .rollupAllPopups()`
- 条件付き依存: `if ( UrlbarPrefs.get("closeOtherPanelsOnOpen") && !this.input.inOverflowPanel )` → `window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if ( UrlbarPrefs.get("closeOtherPanelsOnOpen") && !this.input.inOverflowPanel )` → `window.docShell.treeOwner .QueryInterface()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `this.input.inOverflowPanel`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../../netwerk/base/nsIChannel.idl.md)

## UrlbarView.#shouldShowHeuristic()
- 位置: L1380-1388
- 役割: ヒューリスティック結果でなければ例外を投げる。experimental.hideHeuristic が偽か、結果が TIP のときに true を返す。
- 触るとき: 先頭のヒューリスティック結果を表示するかどうかを変えるとき、または hideHeuristic の設定で先頭結果が消える原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `result.type`, `result?.heuristic`

## UrlbarView.#resultIsSearchSuggestion()
- 位置: L1396-1402
- 役割: 結果が検索種別で、かつ検索候補(payload.suggestion あり)のときに true を返す。
- 触るとき: 検索候補の扱いや行の再利用の判定を変えるとき、に見る。
- 呼び出し先: `Boolean()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `result.payload.suggestion`, `result.type`

## UrlbarView.#rowCanUpdateToResult()
- 位置: L1415-1458
- 役割: 既存の行を新しい結果で置き換えてよいかを判定する。見出し候補は常に可。suggestedIndex の有無や値、提供元が違えば不可。検索候補と非候補の入れ替えは、直前に検索候補を見ていた場合だけ許す。
- 触るとき: 結果の更新で行を再利用する条件を変えるとき、または表示のちらつきや行の入れ替わりの原因を調べるときに見る。
- 呼び出し先: `this.#resultIsSearchSuggestion()`
- 参照: `result.hasSuggestedIndex`, `result.heuristic`, `result.providerName`, `result.suggestedIndex`, `row.result`, `row.result.hasSuggestedIndex`, `row.result.providerName`, `row.result.suggestedIndex`, `this.#rows.children`

## UrlbarView.#updateResults()
- 位置: L1460-1614
- 役割: 届いた結果を既存の行に順に当て、当てられない行は stale にする。残りの結果は新しい行を末尾に追加し、maxResults の枠に収まらない行は非表示にする。隠し露出は露出または暫定露出として記録し、最後に行の番号を振り直す。
- 触るとき: 結果を更新する順序、ちらつき防止、表示件数の上限を変えるとき、または行が重複したり欠けたりする原因を調べるときに見る。
- 呼び出し先: `UrlbarShared.getSpanForResult()`, `results.slice()`, `row.setAttribute()`, `this.#createRow()`, `this.#isElementVisible()`, `this.#rows.appendChild()`, `this.#shouldShowHeuristic()`, `this.#updateIndices()`, `this.#updateRow()`, `this.controller.engagementEvent.discardTentativeExposures()`
- 条件付き依存: `if (results[0]?.heuristic && !this.#shouldShowHeuristic(results[0]))` → `results.slice()`
- 条件付き依存: `if (this.#isElementVisible(row))` → `UrlbarShared.getSpanForResult()`
- 条件付き依存: `if (!seenMisplacedResult)` → `this.#resultIsSearchSuggestion()`
- 条件付き依存: `if (!seenMisplacedResult)` → `this.#rowCanUpdateToResult()`
- 条件付き依存: `if ( this.#rowCanUpdateToResult(rowIndex, result, seenSearchSuggestion) )` → `resultsToInsert.shift()`
- 条件付き依存: `if (result.isHiddenExposure)` → `this.controller.engagementEvent.addExposure()`
- 条件付き依存: `if ( this.#rowCanUpdateToResult(rowIndex, result, seenSearchSuggestion) )` → `this.#updateRow()`
- 条件付き依存: `if (!(result.isSuggestedIndexRelativeToGroup))` → `Math.min()`
- 条件付き依存: `if (!(result.isSuggestedIndexRelativeToGroup))` → `Math.max()`
- 条件付き依存: `if (canBeVisible)` → `this.controller.engagementEvent.addExposure()`
- 条件付き依存: `if (!(canBeVisible))` → `this.controller.engagementEvent.addTentativeExposure()`
- 条件付き依存: `if (!(canBeVisible))` → `this.#setRowVisibility()`
- 参照: `result.hasSuggestedIndex`, `result.isHiddenExposure`, `result.isSuggestedIndexRelativeToGroup`, `result.suggestedIndex`, `results.length`, `resultsToInsert.length`, `results[0]?.heuristic`, `row.result`, `row.result.hasSuggestedIndex`, `row.result.heuristic`, `this.#queryContext`, `this.#queryContext.maxResults`, `this.#queryContext.results`, `this.#rows.children`, `this.#rows.children.length`

## UrlbarView.#createRow()
- 位置: L1616-1644
- 役割: 結果 1 行分の div を作り、role=presentation を設定する。再利用時に消す属性とクラス名を記録しておく。
- 触るとき: 行の DOM 構造や行の再利用の仕組みを変えるとき、またはスクリーンリーダーに行がどう見えるかを調べるときに見る。
- 呼び出し先: `[...item.attributes].map()`, `[...item.attributes].map(v => v.name).concat()`, `document.createElement()`, `item.setAttribute()`
- 参照: `item._buttons`, `item._elements`, `item._sharedAttributes`, `item._sharedClassList`, `item.attributes`, `item.classList`, `item.className`, `v.name`

## UrlbarView.#createRowContent()
- 位置: L1649-1709
- 役割: 通常の結果行の中身(ファビコン、種類アイコン、タイトル、タグ、操作ラベル、URL など)を作り、要素を名前で引けるよう登録し、説明欄を追加する。
- 触るとき: 通常の行にどの要素を出すかや並び順を変えるとき、または要素が見つからない原因を調べるときに見る。
- 呼び出し先: `document.createElement()`, `item._content.appendChild()`, `item._elements.set()`, `noWrap.appendChild()`, `tagsContainer.classList.add()`, `tailPrefix.appendChild()`, `tailPrefix.toggleAttribute()`, `this.#createExplanation()`, `title.classList.add()`
- 参照: `action.className`, `favicon.className`, `item._content`, `noWrap.className`, `tailPrefix.className`, `tailPrefixChar.className`, `tailPrefixStr.className`, `titleSeparator.className`, `typeIcon.className`, `url.className`

## UrlbarView.#createExplanation()
- 位置: L1715-1734
- 役割: 結果説明機能が有効なときだけ、ブックマーク済みと最終訪問の説明欄を作って行に登録する。
- 触るとき: 結果の説明欄(ブックマーク、最終訪問)を出す条件や要素を変えるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`, `document.createElement()`, `explanation.appendChild()`, `explanation.classList.add()`, `item._elements.set()`, `parentNode.appendChild()`
- 参照: `bookmarked.className`, `lastVisited.className`

## UrlbarView.#updateExplanation()
- 位置: L1746-1797
- 役割: ブックマーク日と最終訪問日を整形して説明欄に設定し、どちらも無ければ説明欄の L10n を外す。どちらかあれば行に has-explanation を付ける。
- 触るとき: 説明欄の日付の表記や表示条件を変えるとき、または説明が古い日付のまま残る原因を調べるときに見る。
- 呼び出し先: `item._elements.get()`, `item.toggleAttribute()`
- 条件付き依存: `if (hasBookmark)` → `UrlbarShared.formatDate()`
- 条件付き依存: `if (hasBookmark)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(hasBookmark))` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (hasLastVisit)` → `UrlbarShared.formatDate()`
- 条件付き依存: `if (hasLastVisit)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(hasLastVisit))` → `this.#l10nCache.removeElementL10n()`
- 参照: `UrlbarShared.DATE_FORMAT_TYPE.ABSOLUTE`, `UrlbarShared.DATE_FORMAT_TYPE.DAYS_WEEKS_MONTHS_AGO`, `UrlbarShared.DATE_FORMAT_TYPE.YESTERDAY_TODAY_TOMORROW`, `result.payload.bookmarkDateMs`, `result.payload.lastVisit`

## UrlbarView.#updateElementForDynamicType()
- 位置: L1831-1901
- 役割: 動的結果の要素に、属性、style、dataset、classList の指定を反映する。id は外部で管理するため無視し、Blob は表示用 URL に変換する。
- 触るとき: 動的結果テンプレートで指定できる属性や style の扱いを変えるとき、または動的結果の表示が指定どおりにならない原因を調べるときに見る。
- 条件付き依存: `if (update.attributes)` → `Object.entries()`
- 条件付き依存: `if (key == "id")` → `console.error()`
- 条件付き依存: `if (value === null)` → `element.removeAttribute()`
- 条件付き依存: `if (typeof value == "boolean")` → `element.toggleAttribute()`
- 条件付き依存: `if (!(typeof value == "boolean"))` → `UrlbarShared.isInstance()`
- 条件付き依存: `if (UrlbarShared.isInstance(value, Blob) && result)` → `element.setAttribute()`
- 条件付き依存: `if (UrlbarShared.isInstance(value, Blob) && result)` → `this.#getBlobUrlForResult()`
- 条件付き依存: `if (!(UrlbarShared.isInstance(value, Blob) && result))` → `element.setAttribute()`
- 条件付き依存: `if (update.style)` → `Object.entries()`
- 条件付き依存: `if (update.style)` → `styleName.includes()`
- 条件付き依存: `if (value === null)` → `element.style.removeProperty()`
- 条件付き依存: `if (!(value === null))` → `element.style.setProperty()`
- 条件付き依存: `if (update.dataset)` → `Object.entries()`
- 条件付き依存: `if (typeof value != "string")` → `console.error()`
- 条件付き依存: `if (update.classList)` → `element.classList.add()`
- 参照: `element.className`, `element.dataset`, `element.style`, `item._content`, `update.attributes`, `update.classList`, `update.dataset`, `update.style`

## UrlbarView.#createRowContentForDynamicType()
- 位置: L1907-1926
- 役割: 結果の viewTemplate に従って動的結果の行の中身を組み立て、URL や操作の有無を行の属性に反映し、選択可否を設定する。テンプレートが無ければエラーを出して何もしない。
- 触るとき: 動的結果の行の組み立てを変えるとき、または viewTemplate が効かない原因を調べるときに見る。
- 呼び出し先: `classes.has()`, `item._content.hasAttribute()`, `item.toggleAttribute()`, `this.#buildViewForDynamicType()`, `this.#setRowSelectable()`
- 条件付き依存: `if (!viewTemplate)` → `console.error()`
- 参照: `item._content`, `item._elements`, `result.payload`, `result.providerName`, `this.#showsActionLabels`

## UrlbarView.#buildViewForDynamicType()
- 位置: L1951-1991
- 役割: テンプレートを再帰的にたどり、子要素を作って属性と名前を設定し、行の中の全要素の CSS クラス名を集めて返す。
- 触るとき: テンプレートの入れ子構造や要素名の登録方法を変えるとき、またはテンプレートの要素名で参照できない原因を調べるときに見る。
- 呼び出し先: `document.createElement()`, `parentNode.appendChild()`, `this.#buildViewForDynamicType()`, `this.#updateElementForDynamicType()`
- 条件付き依存: `if (template.classList)` → `classes.add()`
- 条件付き依存: `if (template.overflowable)` → `parentNode.classList.add()`
- 条件付き依存: `if (template.name)` → `parentNode.setAttribute()`
- 条件付き依存: `if (template.name)` → `parentNode.classList.add()`
- 条件付き依存: `if (template.name)` → `elementsByName.set()`
- 参照: `childTemplate.tag`, `template.children`, `template.classList`, `template.name`, `template.overflowable`

## UrlbarView.#createRowContentForRichSuggestion()
- 位置: L1997-2110
- 役割: リッチ候補の行の中身を組み立てる。ファビコン、種類アイコン、タイトル、タグ、操作、URL、説明、下段を作って要素を登録する。タブ切替用のユーザーコンテキストとタブグループの欄は Nova が有効なときだけ作る。
- 触るとき: リッチ候補の表示要素の構成を変えるとき、またはタブグループやユーザーコンテキストの欄が出ない原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `body.appendChild()`, `bodyTop.appendChild()`, `description.classList.add()`, `document.createElement()`, `item._content.appendChild()`, `item._content.toggleAttribute()`, `item._elements.set()`, `noWrap.appendChild()`, `tagsContainer.classList.add()`, `tailPrefix.appendChild()`, `tailPrefix.toggleAttribute()`, `this.#createExplanation()`, `title.classList.add()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `document.createElement()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `userContext.classList.add()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `noWrap.appendChild()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `item._elements.set()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `tabGroupContainer.classList.add()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `tabGroupLabelFull.classList.add()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `tabGroupContainer.appendChild()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.nova.enabled"))` → `tabGroupLabelShort.classList.add()`
- 条件付き依存: `if (result.payload.descriptionLearnMoreTopic)` → `document.createElement()`
- 条件付き依存: `if (result.payload.descriptionLearnMoreTopic)` → `learnMoreLink.setAttribute()`
- 条件付き依存: `if (result.payload.descriptionLearnMoreTopic)` → `description.appendChild()`
- 参照: `action.className`, `body.className`, `bodyTop.className`, `bottom.className`, `favicon.className`, `noWrap.className`, `result.payload.descriptionLearnMoreTopic`, `tailPrefix.className`, `tailPrefixChar.className`, `tailPrefixStr.className`, `titleSeparator.className`, `typeIcon.className`, `url.className`

## UrlbarView.#createRowContentForBottomUrl()
- 位置: L2116-2175
- 役割: 下段に URL を出す候補の行の中身を作る。ファビコン、タイトル、サブタイトル、説明、下段のラベルと区切り、URL の欄を作って要素を登録する。
- 触るとき: アドオンやスポンサー候補のように下段に URL を出す候補の見た目を変えるとき、に見る。
- 呼び出し先: `body.appendChild()`, `bodyTop.appendChild()`, `bottom.appendChild()`, `description.classList.add()`, `document.createElement()`, `item._content.appendChild()`, `item._content.toggleAttribute()`, `item._elements.set()`, `noWrap.appendChild()`, `title.classList.add()`
- 参照: `body.className`, `bodyTop.className`, `bottom.className`, `bottomLabel.className`, `bottomSeparator.className`, `favicon.className`, `noWrap.className`, `subtitle.className`, `subtitleSeparator.className`, `url.className`

## UrlbarView.#needsNewButtons()
- 位置: L2183-2207
- 役割: ボタンを作り直す必要があるかを判定する。古い結果が無い、結果メニューの有無が変わった、フィードバックメニューの有無が変わった、ボタンの内容が変わった、テスト用の強制指定がある、のいずれかで true を返す。
- 触るとき: ボタンを作り直す条件を変えるとき、またはボタンが古い内容のまま残る原因を調べるときに見る。
- 呼び出し先: `UrlbarShared.deepEqual()`, `item._buttons.has()`, `this.#hasMenuButton()`
- 参照: `newResult.payload.buttons`, `newResult.payload.buttons?.length`, `newResult.showFeedbackMenu`, `newResult.testForceNewContent`, `oldResult.payload.buttons`, `oldResult.payload.buttons?.length`, `oldResult.showFeedbackMenu`

## UrlbarView.#updateRowButtons()
- 位置: L2214-2271
- 役割: ボタンに名前を振り、作り直しが必要なら既存のボタンを消して、結果のボタン、tip 用のボタン、結果メニューのボタンを順に追加する。結果メニューは keyboard-accessible の設定で操作対象かが変わる。
- 触るとき: 行のボタン構成を変えるとき、または結果メニューのボタンがキーボードで操作できない原因を調べるときに見る。
- 呼び出し先: `i.toString()`, `item._buttons.clear()`, `item._elements.get()`, `item.toggleAttribute()`, `this.#hasMenuButton()`, `this.#needsNewButtons()`
- 条件付き依存: `if (!(container))` → `document.createElement()`
- 条件付き依存: `if (!(container))` → `item.appendChild()`
- 条件付き依存: `if (!(container))` → `item._elements.set()`
- 条件付き依存: `if (result.payload.buttons)` → `this.#addRowButton()`
- 条件付き依存: `if (result.payload.buttonText)` → `this.#addRowButton()`
- 条件付き依存: `if (result.payload.buttonText)` → `item._buttons.get()`
- 条件付き依存: `if (hasResultMenu)` → `this.#addRowButton()`
- 条件付き依存: `if (hasResultMenu)` → `UrlbarPrefs.get()`
- 参照: `button.name`, `container.className`, `container.innerHTML`, `item._buttons.get("tip").textContent`, `result.payload.buttonText`, `result.payload.buttonUrl`, `result.payload.buttons`, `result.payload.buttons?.length`, `result.showFeedbackMenu`

## UrlbarView.#addRowButton()
- 位置: L2286-2354
- 役割: ボタン要素 1 個を作り、role=button、クラス、data 属性、L10n を設定してボタンの並びに追加する。menu があれば本体と展開用のボタンを包む分割ボタンとして作る。
- 触るとき: 行のボタンの見た目や分割ボタンの構造を変えるとき、に見る。
- 呼び出し先: `button.classList.add()`, `container.appendChild()`, `container.classList.add()`, `document.createElement()`, `dropmarker.classList.add()`, `dropmarker.setAttribute()`, `item._buttons.set()`, `item._elements.get()`, `item._elements.get("buttons").appendChild()`, `this.#l10nCache.setElementL10n()`, `this.#updateElementForDynamicType()`
- 条件付き依存: `if (l10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!menu)` → `item._elements.get("buttons").appendChild()`
- 条件付き依存: `if (!menu)` → `item._elements.get()`
- 参照: `button.id`, `item.id`

## UrlbarView.#createSecondaryAction()
- 位置: L2356-2392
- 役割: 二次操作(アクション)のボタンを作って、アイコン、dataset、ラベル(L10n ID か直接指定のラベル)を設定し、コンテナに包んで返す。global の場合は全体用のクラスを付ける。
- 触るとき: 二次操作ボタンの見た目や属性を変えるとき、またはアクションのラベルが出ない原因を調べるときに見る。
- 呼び出し先: `actionContainer.appendChild()`, `actionContainer.classList.add()`, `button.appendChild()`, `button.classList.add()`, `button.setAttribute()`, `document.createElement()`
- 条件付き依存: `if (global)` → `button.classList.add()`
- 条件付き依存: `if (action.classList)` → `button.classList.add()`
- 条件付き依存: `if (action.icon)` → `document.createElement()`
- 条件付き依存: `if (action.icon)` → `button.appendChild()`
- 条件付き依存: `if (action.l10nId)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(action.l10nId))` → `document.l10n.setAttributes()`
- 参照: `action.classList`, `action.dataset`, `action.icon`, `action.key`, `action.l10nArgs`, `action.l10nId`, `action.label`, `action.providerName`, `button.dataset`, `button.dataset.action`, `button.dataset.providerName`, `icon.src`

## UrlbarView.#needsNewContent()
- 位置: L2394-2467
- 役割: 行の中身を作り直す必要があるかを判定する。動的種類、リッチ候補、heuristic、タブ切替、下段 URL 候補の種類が変わるときや、動的結果の提供元かテンプレートが変わるときに true を返す。
- 触るとき: 行の中身を作り直す条件を追加・変更するとき、または古い要素が残って表示が崩れる原因を調べるときに見る。
- 条件付き依存: `if (newResult.type == UrlbarShared.RESULT_TYPE.DYNAMIC)` → `UrlbarShared.deepEqual()`
- 参照: `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `newResult.heuristic`, `newResult.isBottomUrlSuggestion`, `newResult.isRichSuggestion`, `newResult.payload.dynamicType`, `newResult.payload.items?.length`, `newResult.payload.suggestionType`, `newResult.payload.viewTemplate`, `newResult.providerName`, `newResult.testForceNewContent`, `newResult.type`, `oldResult.heuristic`, `oldResult.isBottomUrlSuggestion`, `oldResult.isRichSuggestion`, `oldResult.payload.dynamicType`, `oldResult.payload.items?.length`, `oldResult.payload.suggestionType`, `oldResult.payload.viewTemplate`, `oldResult.providerName`, `oldResult.type`

## UrlbarView.#updateRow()
- 位置: L2470-2865
- 役割: 行に結果を反映する。必要なら中身を作り直し、ボタンを更新してから、結果の種類ごとの type 属性、ファビコン、タイトル、タグ、URL、説明、アクション欄を設定する。下段 URL 候補と動的結果はその場で処理を終える。
- 触るとき: 行の表示内容をまとめて変えるとき、または結果の種類によって表示が変わる理由を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `action?.toggleAttribute()`, `getUniqueId()`, `item._elements.get()`, `item.querySelector()`, `item.removeAttribute()`, `item.toggleAttribute()`, `result.getDisplayableValueAndHighlights()`, `result.payload.input.trim()`, `this.#iconForResult()`, `this.#needsNewContent()`, `this.#setResultTitle()`, `this.#setRowSelectable()`, `this.#updateExplanation()`, `this.#updateOverflowTooltip()`, `this.#updateRowButtons()`, `title.hasAttribute()`, `title.toggleAttribute()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item._elements.get()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item.lastChild.remove()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item._elements.clear()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `document.createElement()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item.appendChild()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item._sharedAttributes.has()`
- 条件付き依存: `if (!item._sharedAttributes.has(attribute.name))` → `item.removeAttribute()`
- 条件付き依存: `if (this.#needsNewContent(item, oldResult, result))` → `item._sharedClassList.has()`
- 条件付き依存: `if (!item._sharedClassList.has(className))` → `item.classList.remove()`
- 条件付き依存: `if (item.result.type == UrlbarShared.RESULT_TYPE.DYNAMIC)` → `this.#createRowContentForDynamicType()`
- 条件付き依存: `if (result.isBottomUrlSuggestion)` → `this.#createRowContentForBottomUrl()`
- 条件付き依存: `if (!(result.isBottomUrlSuggestion))` → `UrlbarPrefs.get()`
- 条件付き依存: `if ( result.isRichSuggestion || UrlbarPrefs.get("browser.nova.enabled") )` → `this.#createRowContentForRichSuggestion()`
- 条件付き依存: `if (!( result.isRichSuggestion || UrlbarPrefs.get("browser.nova.enabled") ))` → `this.#createRowContent()`
- 条件付き依存: `if (buttons)` → `item.appendChild()`
- 条件付き依存: `if (buttons)` → `item._elements.set()`
- 条件付き依存: `if (result.isBottomUrlSuggestion)` → `this.#updateRowContentForBottomUrl()`
- 条件付き依存: `if (secAction && !actionsContainer)` → `item.appendChild()`
- 条件付き依存: `if (secAction && !actionsContainer)` → `this.#createSecondaryAction()`
- 条件付き依存: `if ( secAction && secAction.key != actionsContainer.firstChild.dataset.action )` → `item.replaceChild()`
- 条件付き依存: `if ( secAction && secAction.key != actionsContainer.firstChild.dataset.action )` → `this.#createSecondaryAction()`
- 条件付き依存: `if (!secAction && actionsContainer)` → `item.removeChild()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.SEARCH && !result.payload.providesSearchMode && !result.payload.inPrivateWindow && result.providerName != "UrlbarPro...)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.REMOTE_TAB)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.TIP)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.TIP)` → `item.addEventListener()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.TIP)` → `this.input.focus()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderSearchTips" || result.payload.type == "dismissalAcknowledgment" )` → `this.#ariaNotifyLocalizedString()`
- 条件付き依存: `if (result.source == UrlbarShared.RESULT_SOURCE.BOOKMARKS)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.DYNAMIC)` → `item.setAttribute()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.DYNAMIC)` → `this.#updateRowForDynamicType()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderTabToSearch")` → `item.setAttribute()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderSemanticHistorySearch")` → `item.setAttribute()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderInputHistory")` → `item.setAttribute()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderTopSites" && result.source == UrlbarShared.RESULT_SOURCE.HISTORY )` → `item.setAttribute()`
- 条件付き依存: `if (!( result.providerName == "UrlbarProviderTopSites" && result.source == UrlbarShared.RESULT_SOURCE.HISTORY ))` → `item.setAttribute()`
- 条件付き依存: `if (!( result.providerName == "UrlbarProviderTopSites" && result.source == UrlbarShared.RESULT_SOURCE.HISTORY ))` → `UrlbarShared.searchEngagementTelemetryType()`
- 条件付き依存: `if (result.payload.tail && result.payload.tailOffsetIndex > 0)` → `this.#fillTailSuggestionPrefix()`
- 条件付き依存: `if (result.payload.tail && result.payload.tailOffsetIndex > 0)` → `title.setAttribute()`
- 条件付き依存: `if (result.payload.tail && result.payload.tailOffsetIndex > 0)` → `item.toggleAttribute()`
- 条件付き依存: `if (!(result.payload.tail && result.payload.tailOffsetIndex > 0))` → `item.removeAttribute()`
- 条件付き依存: `if (!(result.payload.tail && result.payload.tailOffsetIndex > 0))` → `title.removeAttribute()`
- 条件付き依存: `if (tagsContainer)` → `result.getDisplayableValueAndHighlights()`
- 条件付き依存: `if (tags?.length)` → `tagsContainer.append()`
- 条件付き依存: `if (tags?.length)` → `tags.map()`
- 条件付き依存: `if (tags?.length)` → `document.createElement()`
- 条件付き依存: `if (tags?.length)` → `UrlbarShared.addTextContentWithHighlights()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `title.toggleAttribute()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `this.#l10nCache.ensure(label).then()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `this.#l10nCache.ensure()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `this.#l10nCache.get()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `title.setAttribute()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderClipboard")` → `action.setAttribute()`
- 条件付き依存: `if (result.isRichSuggestion || UrlbarPrefs.get("browser.nova.enabled"))` → `this.#updateRowForRichSuggestion()`
- 条件付き依存: `if (setURL)` → `result.getDisplayableValueAndHighlights()`
- 条件付き依存: `if (setURL)` → `this.#updateOverflowTooltip()`
- 条件付き依存: `if (setURL)` → `UrlbarContentUtils.isTextDirectionRTL()`
- 条件付き依存: `if (UrlbarContentUtils.isTextDirectionRTL(displayedUrl, window))` → `this.#offsetHighlights()`
- 条件付き依存: `if (setURL)` → `UrlbarShared.addTextContentWithHighlights()`
- 条件付き依存: `if (!(setURL))` → `this.#updateOverflowTooltip()`
- 条件付き依存: `if (this.#showsActionLabels)` → `item.toggleAttribute()`
- 条件付き依存: `if (actionSetter)` → `actionSetter()`
- 条件付き依存: `if (!(actionSetter))` → `item._originalActionSetter()`
- 条件付き依存: `if (!title.hasAttribute("is-url"))` → `title.setAttribute()`
- 条件付き依存: `if (!(!title.hasAttribute("is-url")))` → `title.removeAttribute()`
- 参照: `UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `actionsContainer.firstChild.dataset.action`, `attribute.name`, `element.className`, `favicon.src`, `item._content`, `item._content.className`, `item._content.id`, `item._originalActionSetter`, `item.attributes`, `item.classList`, `item.id`, `item.lastChild`, `item.result`, `item.result.type`, `result.autofill?.noVisitAction`, `result.getDisplayableValueAndHighlights("title").value`, `result.heuristic`, `result.isBestMatch`, `result.isBottomUrlSuggestion`, `result.isRichSuggestion`, `result.payload.action`, `result.payload.inPrivateWindow`, `result.payload.isPinned`, `result.payload.isPrivateEngine`, `result.payload.isSponsored`, `result.payload.keyword`, `result.payload.providesSearchMode`, `result.payload.shouldShowUrl`, `result.payload.suggestion`, `result.payload.suggestionObject?.suggestionType`, `result.payload.tail`, `result.payload.tailOffsetIndex`, `result.payload.titleL10n.args`, `result.payload.titleL10n.id`, `result.payload.type`, `result.payload.url`, `result.providerName`, `result.source`, `result.type`, `secAction.key`, `tags?.length`, `tagsContainer.textContent`, `this.#queryContext.tokens`, `this.#rows.children`, `this.#showsActionLabels`, `title.innerText`, `url.textContent`

## actionSetter()
- 位置: L2672-2674
- 役割: タブ切替の行のアクション欄に、タブ切替のチップ(#setSwitchTabActionChiclet)を表示する。secondaryActions.switchToTab が真なら設定されない。
- 触るとき: タブ切替の行のアクション表示を変えるとき、に見る。
- 呼び出し先: `this.#setSwitchTabActionChiclet()`

## actionSetter()
- 位置: L2679-2682
- 役割: リモートタブの行のアクション欄に、接続先の端末名を表示する。
- 触るとき: リモートタブの行の表示内容を変えるとき、に見る。
- 呼び出し先: `this.#l10nCache.removeElementL10n()`
- 参照: `action.textContent`, `result.payload.device`

## actionSetter()
- 位置: L2686-2690
- 役割: AI チャットの行のアクション欄に、AI チャット用の L10n 文言を設定する。
- 触るとき: AI チャットの行の文言を変えるとき、に見る。
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## actionSetter()
- 位置: L2703-2708
- 役割: プライベートウィンドウで、プライベート用のエンジンを使う検索の行に、エンジン名つきのアクション文言を設定する。
- 触るとき: プライベートウィンドウの検索の文言を変えるとき、に見る。
- 呼び出し先: `this.#l10nCache.setElementL10n()`
- 参照: `result.payload.engine`

## actionSetter()
- 位置: L2710-2714
- 役割: プライベートウィンドウの検索の行に、プライベート検索用の文言を設定する。
- 触るとき: プライベートウィンドウの検索の文言を変えるとき、に見る。
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## actionSetter()
- 位置: L2717-2724
- 役割: タブで検索(tab-to-search)の行に、一般用の Web エンジンか他のエンジンかに応じた文言を、エンジン名つきで設定する。
- 触るとき: タブで検索の行の文言を変えるとき、に見る。
- 呼び出し先: `this.#l10nCache.setElementL10n()`
- 参照: `result.payload.engine`, `result.payload.isGeneralPurposeEngine`

## actionSetter()
- 位置: L2726-2731
- 役割: 通常の検索の行に、エンジン名つきの検索用の文言を設定する。検索モードを提供する結果には設定しない。
- 触るとき: 検索候補のアクション文言を変えるとき、または検索モードの結果に文言が出ない理由を調べるときに見る。
- 呼び出し先: `this.#l10nCache.setElementL10n()`
- 参照: `result.payload.engine`

## actionSetter()
- 位置: L2738-2741
- 役割: 拡張機能(omnibox)の行のアクション欄に、拡張機能が指定した内容を表示する。
- 触るとき: 拡張機能の候補の表示内容を変えるとき、に見る。
- 呼び出し先: `this.#l10nCache.removeElementL10n()`
- 参照: `action.textContent`, `result.payload.content`

## actionSetter()
- 位置: L2748-2752
- 役割: クリップボードの URL の行に、「クリップボードから開く」の文言を設定する。
- 触るとき: クリップボード候補の文言や読み上げを変えるとき、に見る。
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## actionSetter()
- 位置: L2801-2805
- 役割: スポンサー付きの結果のアクション欄に、スポンサー表示の文言を設定する。
- 触るとき: スポンサー表示の文言を変えるとき、またはスポンサー表示が出ない理由を調べるときに見る。
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## actionSetter()
- 位置: L2839-2843
- 役割: 訪問として扱う結果のアクション欄に、訪問用の文言を設定する。
- 触るとき: 訪問の文言を変えるとき、または先頭結果の文言が想定と違う理由を調べるときに見る。
- 呼び出し先: `this.#l10nCache.setElementL10n()`

## item._originalActionSetter()
- 位置: L2852-2855
- 役割: アクション設定が無い行で、アクション欄の文言を消す関数。行の属性 _originalActionSetter に保存される。
- 触るとき: アクション欄が空の行の扱いを変えるとき、に見る。
- 呼び出し先: `this.#l10nCache.removeElementL10n()`
- 参照: `action.textContent`

## UrlbarView.#setRowSelectable()
- 位置: L2867-2879
- 役割: 行と中身の selectable 属性を設定する。選択可能なときだけ中身に role=option を付け、不可のときは role が option なら外す。
- 触るとき: 行が選択可能かどうかの判定を変えるとき、またはスクリーンリーダーで選択肢として読まれない原因を調べるときに見る。
- 呼び出し先: `item._content.toggleAttribute()`, `item.toggleAttribute()`
- 条件付き依存: `if (isRowSelectable)` → `item._content.setAttribute()`
- 条件付き依存: `if (!(isRowSelectable))` → `item._content.getAttribute()`
- 条件付き依存: `if (item._content.getAttribute("role") == "option")` → `item._content.removeAttribute()`

## UrlbarView.#iconForResult()
- 位置: L2881-2919
- 役割: 結果に表示するアイコンの URL を決める。履歴の検索とキーワードは履歴アイコン、次に指定の上書き、payload の icon、iconBlob の blob URL、トレンドの専用アイコン、検索とキーワードは虫眼鏡、それ以外は既定のアイコンの順に選ぶ。
- 触るとき: 候補ごとのアイコンの優先順位を変えるとき、または表示されるアイコンが想定と違う理由を調べるときに見る。
- 条件付き依存: `if (result.payload.iconBlob)` → `this.#getBlobUrlForResult()`
- 参照: `UrlbarShared.ICON.DEFAULT`, `UrlbarShared.ICON.HISTORY`, `UrlbarShared.ICON.SEARCH_GLASS`, `UrlbarShared.ICON.TRENDING`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.SEARCH`, `result.payload.icon`, `result.payload.iconBlob`, `result.payload.trending`, `result.source`, `result.type`

## UrlbarView.#getBlobUrlForResult()
- 位置: L2921-2940
- 役割: 元の URL(無ければ url)をキーにして blob の表示用 URL を作り、同じ URL の間は作り直さず再利用する。URL が無ければ null を返す。
- 触るとき: blob のアイコンが更新されない原因や、表示用 URL の寿命を調べるときに見る。
- 条件付き依存: `if (resultUrl)` → `this.#blobUrlsByResultUrl?.get()`
- 条件付き依存: `if (!blobUrl)` → `URL.createObjectURL()`
- 条件付き依存: `if (!blobUrl)` → `this.#blobUrlsByResultUrl.set()`
- 参照: `result.payload.originalUrl`, `result.payload.url`, `this.#blobUrlsByResultUrl`

## UrlbarView.#updateRowForDynamicType()
- 位置: L2946-2978
- 役割: 動的結果の行に dynamicType を付け、要素に行の ID を含む ID を振り、viewUpdate の各要素を名前で探して内容を更新する。L10n があれば設定し、textContent があれば文字列を設定する。
- 触るとき: 動的結果の viewUpdate で行の一部だけを書き換える仕組みを変えるとき、または要素が名前で見つからない原因を調べるときに見る。
- 呼び出し先: `Object.entries()`, `item.querySelector()`, `item.setAttribute()`, `this.#updateElementForDynamicType()`
- 条件付き依存: `if (update.l10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(update.l10n))` → `update.hasOwnProperty()`
- 条件付き依存: `if (update.hasOwnProperty("textContent"))` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (update.hasOwnProperty("textContent"))` → `UrlbarShared.addTextContentWithHighlights()`
- 参照: `item._elements`, `item.id`, `node.id`, `result.payload`, `result.payload.dynamicType`, `update.highlights`, `update.l10n`, `update.textContent`

## UrlbarView.#updateRowForRichSuggestion()
- 位置: L2984-3044
- 役割: リッチ候補の行に、アイコンのサイズと種類、説明文(L10n なら学習リンクの URL も設定)、下段の文言を反映する。TIP 以外は選択可能にする。
- 触るとき: リッチ候補の説明文や下段の表示を変えるとき、または学習リンクが開けない原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `item._elements.get()`, `item.toggleAttribute()`, `this.#setRowSelectable()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `String()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `item.setAttribute()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `favicon.setAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconSize))` → `item.removeAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconSize))` → `favicon.removeAttribute()`
- 条件付き依存: `if (result.richSuggestionIconVariation)` → `favicon.setAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconVariation))` → `favicon.removeAttribute()`
- 条件付き依存: `if (result.payload.descriptionL10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (result.payload.descriptionLearnMoreTopic)` → `description.querySelector()`
- 条件付き依存: `if (learnMoreLink)` → `window.getHelpLinkURL()`
- 条件付き依存: `if (!(learnMoreLink))` → `console.warn()`
- 条件付き依存: `if (!(result.payload.descriptionL10n))` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (result.payload.bottomTextL10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(result.payload.bottomTextL10n))` → `this.#l10nCache.removeElementL10n()`
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `description.textContent`, `learnMoreLink.dataset.url`, `result.payload.bottomTextL10n`, `result.payload.description`, `result.payload.descriptionL10n`, `result.payload.descriptionLearnMoreTopic`, `result.richSuggestionIconSize`, `result.richSuggestionIconVariation`, `result.type`

## UrlbarView.#updateRowContentForBottomUrl()
- 位置: L3050-3102
- 役割: 下段 URL 候補の行に with-bottom-url を付け、種類、スポンサー表示、アイコン、タイトル、サブタイトル、説明、下段のラベル、URL を設定する。行は常に選択可能にする。
- 触るとき: 下段 URL 候補の表示内容を変えるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.prepareUrlForDisplay()`, `UrlbarShared.searchEngagementTelemetryType()`, `item._elements.get()`, `item.classList.add()`, `item.setAttribute()`, `item.toggleAttribute()`, `this.#iconForResult()`, `this.#l10nCache.setElementL10n()`, `this.#setResultTitle()`, `this.#setRowSelectable()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `String()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `item.setAttribute()`
- 条件付き依存: `if (result.richSuggestionIconSize)` → `favicon.setAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconSize))` → `item.removeAttribute()`
- 条件付き依存: `if (!(result.richSuggestionIconSize))` → `favicon.removeAttribute()`
- 条件付き依存: `if (result.payload.subtitleL10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(result.payload.subtitleL10n))` → `this.#l10nCache.removeElementL10n()`
- 参照: `description.textContent`, `favicon.src`, `result.payload.bottomTextL10n`, `result.payload.description`, `result.payload.isSponsored`, `result.payload.subtitle`, `result.payload.subtitleL10n`, `result.payload.url`, `result.richSuggestionIconSize`, `subtitle.textContent`, `url.textContent`

## UrlbarView.#updateIndices()
- 位置: L3110-3168
- 役割: 表示更新の後処理として、各行に rowIndex を振り、表示中の結果を visibleResults に集めて露出を記録し、折り返し監視を付ける。行のラベルを整え、選択可能な要素の elementIndex を振り直し、表示が無ければ noresults を立てる。
- 触るとき: 表示後の番号振りやグループラベルの扱いを変えるとき、または行番号が結果とずれる原因を調べるときに見る。
- 呼び出し先: `this.#getNextSelectableElement()`, `this.#isElementVisible()`, `this.#overflowObserver.disconnect()`, `this.#updateRowLabel()`, `this.getFirstSelectableElement()`, `this.input.toggleAttribute()`
- 条件付き依存: `if (visible)` → `this.visibleResults.push()`
- 条件付き依存: `if (result.exposureTelemetry)` → `this.controller.engagementEvent.addExposure()`
- 条件付き依存: `if (visible)` → `item.querySelectorAll()`
- 条件付き依存: `if (visible)` → `this.#overflowObserver.observe()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `result.exposureTelemetry`, `result.heuristic`, `result.payload.suggestion`, `result.rowIndex`, `result.type`, `selectableElement.elementIndex`, `this.#queryContext`, `this.#rows.children`, `this.#rows.children.length`, `this.visibleResults`, `this.visibleResults.length`

## UrlbarView.#updateRowLabel()
- 位置: L3190-3252
- 役割: 行のグループラベルを付けるか外す。表示中で直前と同じラベルでなく、検索候補が先頭の見出し候補や検索候補だけの後ろでなければラベルを付ける。スクリーンリーダー用の隠れた aria-label 要素も作成・削除する。
- 触るとき: グループラベルの出し方や重複の判定を変えるとき、またはラベルが二重に出る原因を調べるときに見る。
- 呼び出し先: `UrlbarShared.deepEqual()`, `groupAriaLabel.setAttribute()`, `item._elements.get()`, `this.#l10nCache.ensure()`, `this.#l10nCache.ensure(label).then()`, `this.#l10nCache.get()`, `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if ( isItemVisible && // Show the search suggestions label only if there are other visible // results before this one that aren't the heuristic or suggestions. !...)` → `this.#rowLabel()`
- 条件付き依存: `if ( !label || item.result.hideRowLabel || UrlbarShared.deepEqual(label, lastVisibleLabel) )` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (groupAriaLabel)` → `groupAriaLabel.remove()`
- 条件付き依存: `if (groupAriaLabel)` → `item._elements.delete()`
- 条件付き依存: `if (!groupAriaLabel)` → `document.createElement()`
- 条件付き依存: `if (!groupAriaLabel)` → `item._content.insertBefore()`
- 条件付き依存: `if (!groupAriaLabel)` → `item._elements.set()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `groupAriaLabel.className`, `item._content.firstChild`, `item.result.hideRowLabel`, `item.result.payload.suggestion`, `item.result.type`, `label.args`, `label.id`, `message?.attributes.label`

## UrlbarView.#rowLabel()
- 位置: L3264-3328
- 役割: 行のグループラベル(トレンド、最近の検索、Firefox Suggest、ベストマッチ、ショートカット、検索候補、クイックアクションなど)の L10n 情報を返す。ラベルを出さない行や機能が無効なときは null を返す。
- 触るとき: グループラベルの文言や付く条件を変えるとき、または見出しが付かない、違う見出しが付くといった原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.URL`, `row.result.heuristic`, `row.result.isBestMatch`, `row.result.payload.engine`, `row.result.payload.trending`, `row.result.providerName`, `row.result.rowLabel`, `row.result.type`, `this.#queryContext.results`, `this.#queryContext.results[0].providerName`, `this.#queryContext?.searchString`, `this.controller.engineStore.default?.name`

## UrlbarView.#setRowVisibility()
- 位置: L3334-3336
- 役割: 行の hidden 属性を、表示するかどうかに合わせて切り替える。
- 触るとき: 行を隠す仕組みを変えるとき、または古い行の表示が切り替わらない原因を調べるときに見る。
- 呼び出し先: `row.toggleAttribute()`

## UrlbarView.#ariaNotifyLocalizedString()
- 位置: async L3338-3341
- 役割: L10n の文字列を取得し、要素の ariaNotify で読み上げ通知を出す。
- 触るとき: 読み上げ通知の文言や発火のタイミングを変えるとき、に見る。
- 呼び出し先: `document.l10n.formatValue()`, `element.ariaNotify()`

## UrlbarView.#isElementVisible()
- 位置: L3351-3357
- 役割: 要素の display が none でなく、かつその行が hidden でなければ true を返す。
- 触るとき: 表示中かどうかの判定を変えるとき、または非表示の行が選ばれてしまう原因を調べるときに見る。
- 呼び出し先: `row.hasAttribute()`, `this.#getRowFromElement()`
- 参照: `element.style.display`

## UrlbarView.#removeStaleRows()
- 位置: L3359-3389
- 役割: 末尾から順に、stale の行は削除し、それ以外は表示する。行番号を振り直し、検索モードを抜けていれば actionmode を外し、保留中の露出を確定する。
- 触るとき: 古い行を消す仕組みや検索モード(アクション)の表示の切り替えを変えるとき、に見る。
- 呼び出し先: `row.hasAttribute()`, `this.#updateIndices()`, `this.controller.engagementEvent.acceptTentativeExposures()`
- 条件付き依存: `if (row.hasAttribute("stale"))` → `row.remove()`
- 条件付き依存: `if (!(row.hasAttribute("stale")))` → `this.#setRowVisibility()`
- 条件付き依存: `if ( this.input.searchMode?.source != UrlbarShared.RESULT_SOURCE.ACTIONS && this.visibleResults[0]?.source != UrlbarShared.RESULT_SOURCE.ACTIONS )` → `this.#rows.toggleAttribute()`
- 参照: `UrlbarShared.RESULT_SOURCE.ACTIONS`, `row.previousElementSibling`, `this.#rows.lastElementChild`, `this.input.searchMode?.source`, `this.visibleResults`, `this.visibleResults[0]?.source`

## UrlbarView.#startRemoveStaleRowsTimer()
- 位置: L3391-3400
- 役割: 既存のタイマーを止めてから、removeStaleRowsTimeout の時間が経ったら古い行を消すタイマーを開始する。
- 触るとき: 古い行を消すまでの待ち時間を変えるとき、または古い行が残り続ける原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `this.#cancelRemoveStaleRowsTimer()`, `this.#removeStaleRows()`, `window.setTimeout()`
- 参照: `this.#removeStaleRowsTimer`

## UrlbarView.#cancelRemoveStaleRowsTimer()
- 位置: L3402-3407
- 役割: 古い行を消すタイマーが動いていれば止める。
- 触るとき: タイマーの取り消し漏れで古い行が消えてしまう原因を調べるときに見る。
- 条件付き依存: `if (this.#removeStaleRowsTimer)` → `window.clearTimeout()`
- 参照: `this.#removeStaleRowsTimer`

## UrlbarView.#selectElement()
- 位置: L3409-3464
- 役割: 要素を選択状態にする。前の選択の属性を外し、要素と行に selected 系の属性を付け、検索バーでだけ行を見える位置へスクロールする。選択変更を親に通知し、updateInput が真なら入力欄の値を結果から更新し、偽なら結果だけ反映する。キーボード選択できない要素は例外になる。
- 触るとき: 選択の見た目や入力欄との連動を変えるとき、または選択が入力欄に反映されない原因を調べるときに見る。
- 呼び出し先: `element.matches()`, `this.#getRowFromElement()`, `this.#setAccessibleFocus()`
- 条件付き依存: `if (this.#selectedElement)` → `this.#selectedElement.toggleAttribute()`
- 条件付き依存: `if (this.#selectedElement)` → `this.#selectedElement.removeAttribute()`
- 条件付き依存: `if (this.#selectedElement)` → `this.#getSelectedRow()`
- 条件付き依存: `if (this.#selectedElement)` → `row?.toggleAttribute()`
- 条件付き依存: `if (element)` → `element.toggleAttribute()`
- 条件付き依存: `if (element)` → `element.setAttribute()`
- 条件付き依存: `if (element)` → `row?.hasAttribute()`
- 条件付き依存: `if (row?.hasAttribute("row-selectable"))` → `row?.toggleAttribute()`
- 条件付き依存: `if (element != row)` → `row?.toggleAttribute()`
- 条件付き依存: `if (element)` → `["smartbar", "newtab_searchbar"].includes()`
- 条件付き依存: `if (["smartbar", "newtab_searchbar"].includes(this.input.sapName))` → `(row ?? element).scrollIntoView()`
- 条件付き依存: `if (result)` → `this.controller.parentController.onBeforeSelection()`
- 条件付き依存: `if (updateInput)` → `element?.classList?.contains()`
- 条件付き依存: `if (updateInput)` → `this.input.setValueFromResult()`
- 条件付き依存: `if (!(updateInput))` → `this.input.setResultForCurrentValue()`
- 条件付き依存: `if (result)` → `this.controller.parentController.onSelection()`
- 参照: `row?.result`, `this.#rawSelectedElement`, `this.#selectedElement`, `this.input.sapName`

## UrlbarView.#getClosestSelectableElement()
- 位置: L3481-3501
- 役割: 要素から最も近い選択可能な要素を探す。マウス操作なら条件をゆるくする。表示されていなければ、選択可能な行の中身を返し、見つからなければ null を返す。
- 触るとき: クリックや選択の対象を決める条件を変えるとき、に見る。
- 呼び出し先: `element.classList.contains()`, `element.closest()`, `element.hasAttribute()`, `this.#isElementVisible()`
- 参照: `(element)._content`

## UrlbarView.#isSelectableElement()
- 位置: L3511-3513
- 役割: 要素が、キーボードで選べる最も近い要素そのものかどうかを返す。
- 触るとき: キーボードでの選択対象の判定を変えるとき、に見る。
- 呼び出し先: `this.#getClosestSelectableElement()`

## UrlbarView.#isRowArrowSelectable()
- 位置: L3524-3534
- 役割: 矢印キーで行を選べるかを返す。グローバルアクションの行は行数が 2 より多いときは選べず、それ以外は行の中に選択可能な要素があるかで決める。
- 触るとき: 矢印キーで飛ばす行の条件を変えるとき、に見る。
- 呼び出し先: `this.#getNextSelectableElement()`, `this.#getRowFromElement()`
- 参照: `row.result?.providerName`, `this.#rows.children`, `this.#rows.children.length`

## UrlbarView.getFirstSelectableElement()
- 位置: L3542-3549
- 役割: 行の先頭から、キーボードで選べる最初の要素を返す。
- 触るとき: 先頭の選択要素を取る処理を変えるとき、に見る。
- 呼び出し先: `this.#isSelectableElement()`
- 条件付き依存: `if (element && !this.#isSelectableElement(element))` → `this.#getNextSelectableElement()`
- 参照: `this.#rows.firstElementChild`

## UrlbarView.getLastSelectableElement()
- 位置: L3557-3564
- 役割: 行の末尾から、キーボードで選べる最後の要素を返す。
- 触るとき: 末尾の選択要素を取る処理を変えるとき、に見る。
- 呼び出し先: `this.#isSelectableElement()`
- 条件付き依存: `if (element && !this.#isSelectableElement(element))` → `this.#getPreviousSelectableElement()`
- 参照: `this.#rows.lastElementChild`

## UrlbarView.#getNextSelectableElement()
- 位置: L3576-3596
- 役割: 指定した要素の次に選べる要素を返す。同じ行に次の操作要素があればそれを、無ければ次の行の選べる要素を返す。最後なら null を返す。
- 触るとき: 次の要素へ移る順序を変えるとき、に見る。
- 呼び出し先: `this.#getKeyboardSelectablesInRow()`, `this.#getRowFromElement()`, `this.#isSelectableElement()`
- 条件付き依存: `if (selectables.length)` → `selectables.indexOf()`
- 条件付き依存: `if (next && !this.#isSelectableElement(next))` → `this.#getNextSelectableElement()`
- 参照: `row.nextElementSibling`, `selectables.length`

## UrlbarView.#getPreviousSelectableElement()
- 位置: L3608-3631
- 役割: 指定した要素の前に選べる要素を返す。同じ行に前の操作要素があればそれを、無ければ前の行の選べる要素を返す。先頭なら null を返す。
- 触るとき: 前の要素へ戻る順序を変えるとき、に見る。
- 呼び出し先: `this.#getKeyboardSelectablesInRow()`, `this.#getRowFromElement()`, `this.#isSelectableElement()`
- 条件付き依存: `if (selectables.length)` → `selectables.indexOf()`
- 条件付き依存: `if (previous && !this.#isSelectableElement(previous))` → `this.#getPreviousSelectableElement()`
- 参照: `row.previousElementSibling`, `selectables.length`

## UrlbarView.#getKeyboardSelectablesInRow()
- 位置: L3637-3650
- 役割: 行の中でキーボードで選べる要素を集め、リンク(a)は最後に回して順番を整える。
- 触るとき: 行の中でのキーボード操作の順番を変えるとき、に見る。
- 呼び出し先: `Number()`, `row.querySelectorAll()`, `selectables.sort()`
- 参照: `a.localName`, `b.localName`

## UrlbarView.#getSelectedRow()
- 位置: L3660-3662
- 役割: 選択中の要素を含む行を返す。
- 触るとき: 選択中の行を参照する処理を書くとき、に見る。
- 呼び出し先: `this.#getRowFromElement()`
- 参照: `this.#selectedElement`

## UrlbarView.#getRowFromElement()
- 位置: L3670-3672
- 役割: 要素を含む結果の行(urlbarView-row)を返す。
- 触るとき: 要素から行を求める処理を書くとき、に見る。
- 呼び出し先: `element?.closest()`

## UrlbarView.#getRowByResultId()
- 位置: L3681-3688
- 役割: 結果 ID が一致する行を返す。無ければ null を返す。
- 触るとき: 結果 ID で行を探す処理を書くとき、に見る。
- 参照: `row.result?.id`, `this.#rows.children`

## UrlbarView.#setAccessibleFocus()
- 位置: L3690-3700
- 役割: 入力欄の aria-activedescendant に選択要素の ID を設定する。ID が無い要素には一意な ID を振り、要素が無ければ属性を外す。
- 触るとき: スクリーンリーダーが読み上げる選択位置の仕組みを変えるとき、または aria-activedescendant が古い要素を指す原因を調べるときに見る。
- 条件付き依存: `if (!item.id)` → `getUniqueId()`
- 条件付き依存: `if (item)` → `this.input.inputField.setAttribute()`
- 条件付き依存: `if (!(item))` → `this.input.inputField.removeAttribute()`
- 参照: `item.id`

## UrlbarView.#setResultTitle()
- 位置: L3710-3773
- 役割: 結果のタイトルをタイトルのノードに設定する。L10n の ID、text の順に使い、検索モードを提供する結果では制限キーワードやエンジン名つきの文言を、通常は強調つきのタイトルを入れる。
- 触るとき: 候補のタイトル文言を変えるとき、または検索モードの候補でタイトルが想定と違う理由を調べるときに見る。
- 呼び出し先: `UrlbarShared.addTextContentWithHighlights()`, `result.getDisplayableValueAndHighlights()`, `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (result.payload.titleL10n)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `result.payload.l10nRestrictKeywords[0].toLowerCase()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `result.payload.l10nRestrictKeywords .map(keyword => `@${keyword.toLowerCase()}`) .join()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `result.payload.l10nRestrictKeywords .map()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `keyword.toLowerCase()`
- 条件付き依存: `if (result.type == UrlbarShared.RESULT_TYPE.RESTRICT)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(result.type == UrlbarShared.RESULT_TYPE.RESTRICT))` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderTokenAliasEngines" && UrlbarPrefs.getScotchBonnetPref("searchRestrictKeywords.featureGate") )` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!( result.providerName == "UrlbarProviderTokenAliasEngines" && UrlbarPrefs.getScotchBonnetPref("searchRestrictKeywords.featureGate") ))` → `this.#l10nCache.setElementL10n()`
- 参照: `UrlbarShared.RESULT_TYPE.RESTRICT`, `result.payload.engine`, `result.payload.keywords`, `result.payload.l10nRestrictKeywords`, `result.payload.providesSearchMode`, `result.payload.text`, `result.payload.titleL10n`, `result.providerName`, `result.type`, `this.#queryContext.tokens`, `titleAndHighlights.highlights`, `titleAndHighlights.value`, `titleNode.textContent`

## UrlbarView.#offsetHighlights()
- 位置: L3783-3791
- 役割: 強調範囲の開始位置を指定の数だけずらした配列を返す。強調が無ければそのまま返す。
- 触るとき: 表示 URL の先頭に文字を足したときなど、強調位置がずれる原因を調べるときに見る。
- 呼び出し先: `highlights.map()`

## UrlbarView.#setSwitchTabActionChiclet()
- 位置: L3804-3826
- 役割: タブ切替のチップに、タブへ切り替える文言か分割表示へ移す文言を設定する。Nova が無効なら Proton 用の補助チップを更新し、有効ならユーザー文脈とタブグループの欄を更新する。
- 触るとき: タブ切替のチップの文言や、コンテナとタブグループの表示を変えるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`, `actionNode.classList.add()`, `splitview.tabs.some()`, `this.#l10nCache.setElementL10n()`, `this.#updateTabGroupAction()`, `this.#updateUserContextAction()`
- 条件付き依存: `if (!UrlbarPrefs.get("browser.nova.enabled"))` → `this.#updateOtherActionChicletsProton()`
- 参照: `result.payload.url`, `tab.linkedBrowser.currentURI.spec`, `this.chromeWindow.gBrowser.selectedTab.splitview`

## UrlbarView.#updateOtherActionChicletsProton()
- 位置: L3829-3874
- 役割: Proton 向けに、コンテナのユーザー文脈とタブグループのチップを複製して追加し、不要になったものを削除する。
- 触るとき: Proton 表示のタブ切替チップを変えるとき、または余分なチップが残る原因を調べるときに見る。
- 呼び出し先: `UrlbarShared.isContainerUserContextId()`, `actionNode.parentNode.querySelector()`
- 条件付き依存: `if (!contextualIdentityAction)` → `actionNode.cloneNode()`
- 条件付き依存: `if (!contextualIdentityAction)` → `contextualIdentityAction.classList.add()`
- 条件付き依存: `if (!contextualIdentityAction)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (!contextualIdentityAction)` → `actionNode.parentNode.insertBefore()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && UrlbarShared.isContainerUserContextId(result.payload.userContext?.id) )` → `this.#addContextualIdentityToSwitchTabChiclet()`
- 条件付き依存: `if (!( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && UrlbarShared.isContainerUserContextId(result.payload.userContext?.id) ))` → `contextualIdentityAction?.remove()`
- 条件付き依存: `if (!tabGroupAction)` → `actionNode.cloneNode()`
- 条件付き依存: `if (!tabGroupAction)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (!tabGroupAction)` → `actionNode.parentNode.insertBefore()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && result.payload.tabGroup )` → `this.#addGroupToSwitchTabChiclet()`
- 条件付き依存: `if (!( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && result.payload.tabGroup ))` → `tabGroupAction?.remove()`
- 参照: `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.payload.tabGroup`, `result.payload.userContext?.id`, `result.type`

## UrlbarView.#addContextualIdentityToSwitchTabChiclet()
- 位置: L3877-3916
- 役割: Proton 向けに、コンテナのユーザー文脈の色、アイコン、名前をチップに描く。名前が無ければチップの中身を空にする。
- 触るとき: コンテナの名前、色、アイコンの表示を変えるとき、に見る。
- 呼び出し先: `actionNode.classList.contains()`
- 条件付き依存: `if (label)` → `actionNode.classList.add()`
- 条件付き依存: `if (label)` → `actionNode.classList.remove()`
- 条件付き依存: `if (color)` → `actionNode.className.replace()`
- 条件付き依存: `if (color)` → `actionNode.classList.add()`
- 条件付き依存: `if (label)` → `document.createElement()`
- 条件付き依存: `if (label)` → `textModeLabel.classList.add()`
- 条件付き依存: `if (label)` → `actionNode.appendChild()`
- 条件付き依存: `if (label)` → `iconModeLabel.classList.add()`
- 条件付き依存: `if (iconUrl)` → `document.createElement()`
- 条件付き依存: `if (iconUrl)` → `userContextIcon.classList.add()`
- 条件付き依存: `if (iconUrl)` → `userContextIcon.setAttribute()`
- 条件付き依存: `if (iconUrl)` → `iconModeLabel.appendChild()`
- 条件付き依存: `if (label)` → `actionNode.setAttribute()`
- 参照: `actionNode.className`, `actionNode.innerHTML`, `result.payload.userContext`, `textModeLabel.innerText`, `userContextIcon.src`

## UrlbarView.#addGroupToSwitchTabChiclet()
- 位置: L3919-3970
- 役割: Proton 向けに、タブグループの名前(無名なら L10n の文言)と色の CSS 変数をチップに設定する。グループが見つからなければチップを削除する。
- 触るとき: タブグループのチップの表示を変えるとき、またはグループの色が反映されない原因を調べるときに見る。
- 呼び出し先: `actionNode.appendChild()`, `actionNode.classList.add()`, `actionNode.classList.remove()`, `actionNode.style.setProperty()`, `document.createElement()`, `fullWidthModeLabel.classList.add()`, `group.style.getPropertyValue()`, `narrowWidthModeLabel.classList.add()`, `this.chromeWindow.gBrowser.getTabGroupById()`
- 条件付き依存: `if (!group)` → `actionNode.remove()`
- 条件付き依存: `if (!(group.label))` → `this.#l10nCache.setElementL10n()`
- 参照: `actionNode.innerHTML`, `fullWidthModeLabel.textContent`, `group.label`, `narrowWidthModeLabel.textContent`, `result.payload.tabGroup`

## UrlbarView.#updateUserContextAction()
- 位置: L3972-4017
- 役割: Nova 向けに、ユーザー文脈の欄へアイコンかラベル、色のクラス、title と aria-label を設定する。コンテナが無ければ欄を隠す。
- 触るとき: Nova のタブ切替でコンテナの表示を変えるとき、に見る。
- 呼び出し先: `UrlbarShared.isContainerUserContextId()`, `contextNode.toggleAttribute()`, `item._elements.get()`, `n.startsWith()`
- 条件付き依存: `if (!iconUrl && !label)` → `contextNode.toggleAttribute()`
- 条件付き依存: `if (!iconUrl && !label)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (iconUrl)` → `contextNode.style.setProperty()`
- 条件付き依存: `if (!(iconUrl))` → `contextNode.style.removeProperty()`
- 条件付き依存: `if (n.startsWith("identity-color-"))` → `contextNode.classList.remove()`
- 条件付き依存: `if (color)` → `contextNode.classList.add()`
- 条件付き依存: `if (label)` → `contextNode.setAttribute()`
- 条件付き依存: `if (!(label))` → `contextNode.removeAttribute()`
- 参照: `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `contextNode.classList`, `contextNode.textContent`, `result.payload.userContext`, `result.payload.userContext?.id`, `result.type`

## UrlbarView.#updateTabGroupAction()
- 位置: L4019-4083
- 役割: Nova 向けに、タブグループの欄へ全幅用と短縮用のラベル、title、aria-label、色の CSS 変数を設定する。グループが無ければ欄を隠し、グループ名が空なら無名の L10n 文言を使う。
- 触るとき: タブグループ欄の表示を変えるとき、に見る。
- 呼び出し先: `containerNode.style.setProperty()`, `containerNode.toggleAttribute()`, `group.label.trim()`, `group.style.getPropertyValue()`, `item._elements.get()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TAB_SWITCH && result.payload.tabGroup )` → `this.chromeWindow.gBrowser.getTabGroupById()`
- 条件付き依存: `if (!group)` → `containerNode.toggleAttribute()`
- 条件付き依存: `if (!group)` → `containerNode.removeAttribute()`
- 条件付き依存: `if (!group)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (label)` → `this.#l10nCache.removeElementL10n()`
- 条件付き依存: `if (label)` → `containerNode.setAttribute()`
- 条件付き依存: `if (!(label))` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (!(label))` → `containerNode.removeAttribute()`
- 参照: `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `fullLabelNode.textContent`, `result.payload.tabGroup`, `result.type`, `shortLabelNode.textContent`

## UrlbarView.#fillTailSuggestionPrefix()
- 位置: L4093-4103
- 役割: 末尾候補の行に、入力済みの前半部分と末尾の付加文字を別々のノードへ入れて表示する。
- 触るとき: 末尾補完の表示を変えるとき、または前半部分が二重に出る原因を調べるときに見る。
- 呼び出し先: `item._elements.get()`, `result.payload.suggestion.substring()`
- 参照: `result.payload.tailOffsetIndex`, `result.payload.tailPrefix`, `tailPrefixCharNode.textContent`, `tailPrefixStrNode.textContent`

## UrlbarView.#enableOrDisableRowWrap()
- 位置: L4105-4109
- 役割: 入力欄の幅が 650 未満なら、行とワンクリック検索ボタンに wrap 属性を付け、そうでなければ外す。
- 触るとき: 狭い幅で行を折り返す条件を変えるとき、または折り返しが効かない原因を調べるときに見る。
- 呼び出し先: `getBoundsWithoutFlushing()`, `this.#rows.toggleAttribute()`, `this.oneOffSearchButtons?.container.toggleAttribute()`
- 参照: `getBoundsWithoutFlushing(this.input).width`, `this.input`

## UrlbarView.#setElementOverflowing()
- 位置: L4119-4122
- 役割: 要素の overflow 属性を、はみ出しているかに合わせて設定し、ツールチップを更新する。
- 触るとき: はみ出し表示の判定の結果を要素へ反映する箇所を変えるとき、に見る。
- 呼び出し先: `element.toggleAttribute()`, `this.#updateOverflowTooltip()`

## UrlbarView.#updateOverflowTooltip()
- 位置: L4135-4147
- 役割: はみ出している要素にだけ title を付け、はみ出していなければ外す。ツールチップ文言は要素ごとに保存し、引数があれば保存し直す。
- 触るとき: はみ出した文字のツールチップ文言を変えるとき、または title が出ない原因を調べるときに見る。
- 呼び出し先: `element.hasAttribute()`
- 条件付き依存: `if (typeof tooltip == "string")` → `this.#tooltips.set()`
- 条件付き依存: `if (!(typeof tooltip == "string"))` → `this.#tooltips.get()`
- 条件付き依存: `if (element.hasAttribute("overflow") && tooltip)` → `element.setAttribute()`
- 条件付き依存: `if (!(element.hasAttribute("overflow") && tooltip))` → `element.removeAttribute()`

## UrlbarView.#updateOverflowState()
- 位置: L4149-4157
- 役割: リサイズ監視で届いた各要素について、内容の幅が表示幅を超えているかを判定し、はみ出し状態を更新する。
- 触るとき: はみ出し判定の条件を変えるとき、に見る。
- 呼び出し先: `entries.map()`, `this.#setElementOverflowing()`
- 参照: `target.clientWidth`, `target.scrollWidth`

## UrlbarView.#pickSearchTipIfPresent()
- 位置: L4169-4188
- 役割: 結果が検索のヒント 1 件だけのとき、そのヒントのボタンを選んだものとして扱い、true を返す。ボタンが無ければ例外を投げる。ユーザー操作から呼ぶ前提。
- 触るとき: 検索のヒントが出ている時のクリックや Enter の扱いを変えるとき、に見る。
- 呼び出し先: `buttons.get()`, `this.input.pickElement()`
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `result.type`, `this.#queryContext`, `this.#queryContext.results`, `this.#queryContext.results.length`, `this.#rows.firstElementChild._buttons`, `this.isOpen`

## UrlbarView.#cacheL10nStrings()
- 位置: async L4201-4227
- 役割: よく使う L10n 文字列を非同期に先読みしてキャッシュする。検索サービスの文言、グループラベル、スポンサー表示の文言は設定に応じて加える。
- 触るとき: 表示に使う文言を追加するとき、に見る。キャッシュは削除されないため、引数に検索語を含む文言は入れてはいけない。
- 呼び出し先: `UrlbarPrefs.get()`, `this.#cacheL10nIDArgsForSearchService()`, `this.#l10nCache.ensureAll()`
- 条件付き依存: `if (UrlbarPrefs.get("groupLabels.enabled"))` → `idArgs.push()`
- 条件付き依存: `if (suggestSponsoredEnabled)` → `idArgs.push()`

## UrlbarView.#cacheL10nIDArgsForSearchService()
- 位置: L4236-4274
- 役割: 検索サービスが初期化済みなら、既定の検索エンジン名を使う文言(タブで検索、エンジン名つきの検索など)の ID と引数を返す。未初期化なら空の配列を返す。
- 触るとき: 既定の検索エンジン名を使う文言を増やすとき、または起動直後に文言が出ない原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `idArgs.push()`
- 条件付き依存: `if (UrlbarPrefs.get("groupLabels.enabled"))` → `idArgs.push()`
- 参照: `this.controller.engineStore.default.name`, `this.controller.engineStore.initialized`

## UrlbarView.#openInCommands()
- 位置: L4282-4311
- 役割: 結果を新しいタブ、コンテナタブ(通常ウィンドウで利用者コンテキストが有効な時だけ)、新しいウィンドウ、プライベートウィンドウで開く項目の一覧を返す。
- 触るとき: 結果メニューの「開く先」の項目を変えるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`, `commands.push()`
- 条件付き依存: `if ( !this.input.isPrivate && UrlbarPrefs.get("privacy.userContext.enabled") )` → `commands.push()`
- 参照: `this.input.isPrivate`

## UrlbarView.#hasMenuButton()
- 位置: L4321-4326
- 役割: 結果に三点メニューのボタンを出すかを返す。見出し候補は自身のメニュー項目だけで判断し、それ以外は新しい対象で開けるか、メニュー項目があれば出す。
- 触るとき: 行にメニューボタンを出す条件を変えるとき、または Tab で次の行へ移る挙動を調べるときに見る。
- 呼び出し先: `this.#canOpenInNewTarget()`, `this.#getResultMenuCommands()`
- 参照: `result.heuristic`

## UrlbarView.#updateMenuButtonKeyboardAccessibility()
- 位置: L4333-4340
- 役割: 既存の行のメニューボタンに、resultMenu.keyboardAccessible の設定に合わせて keyboard-inaccessible 属性を付け外しする。
- 触るとき: キーボードでのメニュー操作の設定を既存の行へ反映させるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`, `button.toggleAttribute()`, `this.#rows.querySelectorAll()`

## UrlbarView.#canOpenInNewTarget()
- 位置: L4348-4355
- 役割: コンテキストメニューの機能フラグが有効で、入力欄が対応し、タブ切替以外で、読み込み要求を作れる結果なら true を返す。
- 触るとき: 「開く先」の項目を出す条件を変えるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.getLoadRequestFromResult()`
- 参照: `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.type`, `this.input.handlesOpenInCommands`

## UrlbarView.#getMenuCommands()
- 位置: L4367-4388
- 役割: 結果自身のメニュー項目の前に、開く先の項目と区切りを加え、最後に区切りとキーボード操作の切替チェック項目を付けて返す。何も無ければ null を返す。
- 触るとき: 結果メニュー全体の項目の並び順を変えるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`, `this.#canOpenInNewTarget()`, `this.#getResultMenuCommands()`
- 参照: `RESULT_MENU_COMMANDS.TOGGLE_KEYBOARD_ACCESSIBLE`, `this.#openInCommands`

## UrlbarView.#getResultMenuCommands()
- 位置: L4396-4439
- 役割: 結果が持つメニュー項目を返す。無ければ、削除可能なら削除、ヘルプが有るならヘルプ、管理可能なら管理の既定項目を作る。結果ごとにキャッシュする。
- 触るとき: 既定の結果メニュー項目を変えるとき、またはメニューの項目が古いまま残る原因を調べるときに見る。
- 呼び出し先: `this.#resultMenuCommands.has()`, `this.#resultMenuCommands.set()`
- 条件付き依存: `if (this.#resultMenuCommands.has(result))` → `this.#resultMenuCommands.get()`
- 条件付き依存: `if (commands)` → `this.#resultMenuCommands.set()`
- 条件付き依存: `if (result.payload.isBlockable)` → `commands.push()`
- 条件付き依存: `if (result.payload.helpUrl)` → `commands.push()`
- 条件付き依存: `if (result.payload.isManageable)` → `commands.push()`
- 参照: `RESULT_MENU_COMMANDS.DISMISS`, `RESULT_MENU_COMMANDS.HELP`, `RESULT_MENU_COMMANDS.MANAGE`, `commands.length`, `result.commands`, `result.payload.blockL10n`, `result.payload.helpL10n`, `result.payload.helpUrl`, `result.payload.isBlockable`, `result.payload.isManageable`

## UrlbarView.#populateResultMenu()
- 位置: async L4448-4490
- 役割: 結果メニューの中身を空にしてから項目を並べる。区切りは hr、開く先の項目は openIn、それ以外は command を設定し、サブメニューとチェック項目もここで作る。
- 触るとき: 結果メニューの項目の作り方や属性を変えるとき、に見る。
- 呼び出し先: `commands.map()`, `commands.map(e => e.l10n).filter()`, `document.createElement()`, `menuitem.classList.add()`, `panel.appendChild()`, `this.#l10nCache.ensureAll()`
- 条件付き依存: `if (data.name == "separator")` → `panel.appendChild()`
- 条件付き依存: `if (data.name == "separator")` → `document.createElement()`
- 条件付き依存: `if (data.submenu)` → `menuitem.toggleAttribute()`
- 条件付き依存: `if (data.submenu)` → `document.createElement()`
- 条件付き依存: `if (data.submenu)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (data.submenu)` → `label.hasAttribute()`
- 条件付き依存: `if (label.hasAttribute("accesskey"))` → `menuitem.setAttribute()`
- 条件付き依存: `if (label.hasAttribute("accesskey"))` → `label.getAttribute()`
- 条件付き依存: `if (label.hasAttribute("accesskey"))` → `label.removeAttribute()`
- 条件付き依存: `if (data.submenu)` → `menuitem.appendChild()`
- 条件付き依存: `if (!(data.submenu))` → `this.#l10nCache.setElementL10n()`
- 参照: `data.checked`, `data.l10n`, `data.name`, `data.openIn`, `data.submenu`, `data.type`, `e.l10n`, `menuitem.checked`, `menuitem.dataset.command`, `menuitem.dataset.openIn`, `menuitem.type`, `panel.textContent`, `submenu.slot`, `this.resultMenu`

## UrlbarView.#populateContainerSubmenu()
- 位置: async L4499-4534
- 役割: コンテナタブのサブメニューの中身を作り直す。コンテナの一覧を項目にし、最後にコンテナの追加と管理の項目を付ける。
- 触るとき: コンテナのサブメニューの項目を変えるとき、またはコンテナが一覧に出ない原因を調べるときに見る。
- 呼び出し先: `String()`, `UrlbarContentUtils.getContainers()`, `document.createElement()`, `menuitem.style.setProperty()`, `panel.appendChild()`, `this.#createContainerMenuItem()`, `this.controller.parentController.openContainerCreationPanel()`, `this.controller.parentController.openPreferences()`
- 参照: `container.colorCode`, `container.iconURL`, `container.name`, `container.userContextId`, `menuitem.dataset.usercontextid`, `menuitem.textContent`, `panel.textContent`

## UrlbarView.#createContainerMenuItem()
- 位置: L4546-4551
- 役割: L10n ID のラベルを持つ項目を作り、クリックされたら指定の処理を呼ぶ。結果を選ぶ処理は行わない。
- 触るとき: コンテナのサブメニューに結果を選ばない項目を足すとき、に見る。
- 呼び出し先: `document.createElement()`, `document.l10n.setAttributes()`, `menuitem.addEventListener()`

## UrlbarView.on_SelectedOneOffButtonChanged()
- 位置: L4555-4721
- 役割: ワンクリック検索ボタンの選択が変わったときに、各行の表示を選ばれたエンジンや検索モードに合わせる。対象は見出し候補、検索候補、プライベートの検索で、文言、アイコン、タイトル、結果のエンジンを差し替える。選択が外れたら元の表示へ戻す。
- 触るとき: ワンクリック検索ボタンを選んだときに行の見た目がどう変わるかを変えるとき、または元の表示に戻らない原因を調べるときに見る。
- 呼び出し先: `item._elements.get()`
- 条件付き依存: `if (source)` → `UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 条件付き依存: `if ( result.heuristic && !this.selectedElement && (localSearchMode || engine) )` → `item.setAttribute()`
- 条件付き依存: `if (!( result.heuristic && !this.selectedElement && (localSearchMode || engine) ))` → `item.removeAttribute()`
- 条件付き依存: `if (result.heuristic)` → `result.getDisplayableValueAndHighlights()`
- 条件付き依存: `if (localSearchMode || engine)` → `item.setAttribute()`
- 条件付き依存: `if (!(localSearchMode || engine))` → `item.removeAttribute()`
- 条件付き依存: `if (localSearchMode)` → `UrlbarShared.getResultSourceName()`
- 条件付き依存: `if (localSearchMode)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (result.heuristic)` → `item.setAttribute()`
- 条件付き依存: `if (engine && !result.payload.inPrivateWindow)` → `this.#l10nCache.setElementL10n()`
- 条件付き依存: `if (item._originalActionSetter)` → `item._originalActionSetter()`
- 条件付き依存: `if (!(item._originalActionSetter))` → `console.error()`
- 条件付き依存: `if (!(engine && !result.payload.inPrivateWindow))` → `item.removeAttribute()`
- 条件付き依存: `if ( result.heuristic || (result.payload.inPrivateWindow && !result.payload.isPrivateEngine) )` → `this.#iconForResult()`
- 参照: `UrlbarShared.ICON.DEFAULT`, `UrlbarShared.ICON.SEARCH_GLASS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.SEARCH`, `engine.name`, `favicon.src`, `item._originalActionSetter`, `item.result`, `localSearchMode.source`, `localSearchMode?.icon`, `m.source`, `result.getDisplayableValueAndHighlights("title").value`, `result.heuristic`, `result.payload.engine`, `result.payload.icon`, `result.payload.inPrivateWindow`, `result.payload.isPrivateEngine`, `result.payload.originalEngine`, `result.payload.suggestion`, `result.source`, `result.type`, `this.#queryContext`, `this.#queryContext.searchString`, `this.#rows.children`, `this.input.searchMode`, `this.input.searchMode.isPreview`, `this.isOpen`, `this.oneOffSearchButtons.selectedButton?.engine`, `this.oneOffSearchButtons.selectedButton?.image`, `this.oneOffSearchButtons.selectedButton?.source`, `this.selectedElement`, `title.textContent`

## UrlbarView.on_blur()
- 位置: L4723-4730
- 役割: ウィンドウがフォーカスを失ったときに、ui.popup.disable_autohide が偽ならパネルを閉じる。
- 触るとき: フォーカスを失ったときにパネルが閉じる条件を変えるとき、に見る。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.close()`

## UrlbarView.on_mousedown()
- 位置: L4732-4782
- 役割: 右クリック以外で、クリックされた位置の選択可能な要素を選択し、先読みの接続を張る。ボタンの場合は選択も接続もしない。離したときに処理するため window の mouseup を登録する。
- 触るとき: クリック時の選択や先読み接続の挙動を変えるとき、またはボタンを押したときに選択が動く原因を調べるときに見る。
- 呼び出し先: `element.classList.contains()`, `element.getAttribute()`, `this.#getClosestSelectableElement()`, `window.addEventListener()`
- 条件付き依存: `if (!element.classList.contains("urlbarView-button"))` → `this.#selectElement()`
- 条件付き依存: `if (!element.classList.contains("urlbarView-button"))` → `this.controller.parentController.speculativeConnect()`
- 参照: `event.button`, `event.target`, `this.#mousedownSelectedElement`, `this.#queryContext`, `this.selectedResult`

## UrlbarView.on_mouseup()
- 位置: L4784-4823
- 役割: 離した位置の選択可能な要素があれば、その結果を選んで実行する。押したときに選んだ要素がまだあれば、選択を解除する。
- 触るとき: クリックで結果を実行する判定や、押した後の選択解除の条件を変えるとき、に見る。
- 呼び出し先: `element.getAttribute()`, `event.composedPath()`, `this.#getClosestSelectableElement()`, `window.removeEventListener()`
- 条件付き依存: `if (element && element.getAttribute("aria-disabled") != "true")` → `this.input.pickElement()`
- 条件付き依存: `if (this.#mousedownSelectedElement?.isConnected)` → `this.clearSelection()`
- 参照: `event.button`, `eventTarget.ELEMENT_NODE`, `eventTarget.nodeType`, `this.#mousedownSelectedElement`, `this.#mousedownSelectedElement?.isConnected`

## UrlbarView.on_resize()
- 位置: L4825-4827
- 役割: ウィンドウの幅が変わったときに、行の折り返し設定を更新する。
- 触るとき: 幅による折り返しの条件を見直すとき、に見る。
- 呼び出し先: `this.#enableOrDisableRowWrap()`

## UrlbarView.on_click()
- 位置: L4829-4863
- 役割: 結果メニューの項目のクリックを処理する。表示切り替えの項目なら設定を反転し、それ以外は保持している結果と共に入力欄へ渡す。ヘルプの項目には URL を設定する。サブメニューの親とコンテナ管理の項目は無視する。
- 触るとき: 結果メニューの項目を押したときの動作を追加・変更するとき、または押しても反応しない項目を調べるときに見る。
- 呼び出し先: `event .composedPath()`, `event .composedPath() .find()`, `this.input.pickResult()`
- 条件付き依存: `if ( menuitem.dataset.command == RESULT_MENU_COMMANDS.TOGGLE_KEYBOARD_ACCESSIBLE )` → `UrlbarPrefs.toggleResultMenuKeyboardAccessible()`
- 条件付き依存: `if ( menuitem.dataset.command == RESULT_MENU_COMMANDS.TOGGLE_KEYBOARD_ACCESSIBLE )` → `this.#updateMenuButtonKeyboardAccessibility()`
- 条件付き依存: `if (menuitem.dataset.command == RESULT_MENU_COMMANDS.HELP)` → `UrlbarContentUtils.getSupportUrl()`
- 参照: `RESULT_MENU_COMMANDS.HELP`, `RESULT_MENU_COMMANDS.TOGGLE_KEYBOARD_ACCESSIBLE`, `menuitem.dataset.command`, `menuitem.dataset.openIn`, `menuitem.dataset.url`, `menuitem.dataset.usercontextid`, `menuitem.hasSubmenu`, `node.localName`, `result.payload.helpUrl`, `this.#resultMenuResult`

## UrlbarView.on_showing()
- 位置: L4865-4894
- 役割: 結果メニューが開くとき、トリガーの行に menu-trigger を付ける。分割ボタンなら対応する項目を、それ以外は結果の既定の項目を並べる。コンテナのサブメニューが開くときは中身を作る。
- 触るとき: メニューを開いたときに並ぶ項目を変えるとき、に見る。
- 条件付き依存: `if (event.target == this.resultMenu)` → `this.resultMenu.lastAnchorNode .closest(".urlbarView-row") .toggleAttribute()`
- 条件付き依存: `if (event.target == this.resultMenu)` → `this.resultMenu.lastAnchorNode .closest()`
- 条件付き依存: `if (event.target == this.resultMenu)` → `triggeringEvent.detail.target.closest()`
- 条件付き依存: `if (splitButton)` → `this.#resultMenuResult.payload.buttons.find()`
- 条件付き依存: `if (!(splitButton))` → `this.#getMenuCommands()`
- 条件付き依存: `if (event.target == this.resultMenu)` → `this.#populateResultMenu()`
- 条件付き依存: `if (event.target.dataset.openIn == "container-tab")` → `this.#populateContainerSubmenu()`
- 参照: `b.name`, `event.target`, `event.target.dataset.openIn`, `event.target.submenuPanel`, `mainButton.dataset.name`, `splitButton.firstElementChild`, `this.#resultMenuResult`, `this.#resultMenuResult.payload.buttons.find( b => b.name == buttonName ).menu`, `this.resultMenu`, `this.resultMenu.triggeringEvent`, `triggeringEvent.type`

## UrlbarView.on_hidden()
- 位置: L4896-4903
- 役割: 結果メニューが閉じたときに、トリガーの行から menu-trigger を外す。
- 触るとき: メニューを閉じた後も行が強調されたままになる原因を調べるときに見る。
- 呼び出し先: `event.currentTarget.lastAnchorNode ?.closest()`, `event.currentTarget.lastAnchorNode ?.closest(".urlbarView-row") ?.toggleAttribute()`
- 参照: `event.currentTarget`, `event.target`

## UrlbarView.on_contextmenu()
- 位置: L4905-4929
- 役割: 右クリックされた行があれば結果メニューを開く。入力欄の外のコンテキストメニューは抑止し、入力欄の中は伝えたままにする。機能フラグ contextMenu.featureGate が偽なら何もしない。
- 触るとき: 右クリックで結果メニューを出す条件を変えるとき、または右クリックで別のメニューが出てしまう原因を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `event.preventDefault()`, `event.target.closest()`, `this.#getMenuCommands()`, `this.resultMenu.toggle()`
- 参照: `row.result`, `this.#resultMenuResult`

## UrlbarView.clearTopSitesCache()
- 位置: L4931-4933
- 役割: トップサイトの文脈のキャッシュを消す。QueryContextCache の同名メソッドに委ねる。
- 触るとき: トップサイトの一覧が変わったときにキャッシュを消す箇所を追うとき、に見る。
- 呼び出し先: `this.queryContextCache.clearTopSitesCache()`

## UrlbarView.clearL10nCache()
- 位置: L4935-4937
- 役割: L10n 文字列のキャッシュを全て消す。
- 触るとき: 言語や文言が変わった後に古い文言が表示される原因を調べるとき、に見る。
- 呼び出し先: `this.#l10nCache.clear()`

## QueryContextCache.constructor()
- 位置: L4965-4967
- 役割: キャッシュの最大件数を保存する。
- 触るとき: キャッシュの大きさを変えるとき、に見る。UrlbarView のコンストラクタでは 5 件で作られる。
- 参照: `this.#size`

## QueryContextCache.size()
- 位置: L4972-4974
- 役割: キャッシュの最大件数を返す。
- 触るとき: 件数の上限を参照する処理を書くとき、に見る。
- 参照: `this.#size`

## QueryContextCache.topSitesContext()
- 位置: L4977-4979
- 役割: 保存されているトップサイトの文脈を返す。無ければ null を返す。
- 触るとき: ゼロ入力時に即座に表示する結果を変えるとき、または古いトップサイトが表示される原因を調べるときに見る。
- 参照: `this.#topSitesContext`

## QueryContextCache.clearTopSitesCache()
- 位置: L4981-4983
- 役割: 保存されているトップサイトの文脈を消す。
- 触るとき: トップサイトの文脈を消すタイミングを変えるとき、に見る。
- 参照: `this.#topSitesContext`

## QueryContextCache.clear()
- 位置: L4988-4991
- 役割: 保存されている文脈を全て消し、トップサイトの文脈も消す。
- 触るとき: キャッシュを全て消す箇所を変えるとき、に見る。
- 呼び出し先: `this.clearTopSitesCache()`
- 参照: `this.#cache`

## QueryContextCache.put()
- 位置: L5001-5042
- 役割: 結果が 1 件以上ある文脈を保存する。検索語が空ならトップサイトの文脈として別に保存する(契約の opt-in 表示があれば保存しない)。検索語があれば、同じ検索語とページの古い文脈を外して先頭に入れ、件数の上限を超えた分は末尾から捨てる。
- 触るとき: 再利用する結果の保存条件や件数の扱いを変えるとき、または古い結果が表示される原因を調べるときに見る。
- 呼び出し先: `this.#cache.findIndex()`, `this.#cache.unshift()`
- 条件付き依存: `if (!searchString)` → `queryContext.results?.some()`
- 条件付き依存: `if (!searchString)` → `queryContext.results.some()`
- 条件付き依存: `if (index != -1)` → `this.#cache.splice()`
- 参照: `e.currentPage`, `e.searchString`, `queryContext.currentPage`, `queryContext.results.length`, `queryContext.searchString`, `r.providerName`, `this.#cache`, `this.#cache.length`, `this.#topSitesContext`, `this.size`

## QueryContextCache.get()
- 位置: L5052-5056
- 役割: 検索語とページの URL が両方一致する文脈を返す。無ければ undefined を返す。
- 触るとき: 前の検索結果を再利用する処理を書くとき、または結果が再利用されない原因を調べるときに見る。
- 呼び出し先: `this.#cache.find()`
- 参照: `e.currentPage`, `e.searchString`
