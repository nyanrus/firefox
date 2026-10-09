# browser/components/places/metadataViewer/interactionsViewer.js

source: browser/components/places/metadataViewer/interactionsViewer.js
source-hash: d552ee755af6d631b27b3f00984461374b807c62
lines: 673

## <module>
- 役割: places の metadata viewer ページのスクリプト。Interactions のメタデータ、Places DB の統計、frecency 一覧の 3 つの表を表示し、メタデータを JSON と CSV で書き出す
- 呼び出し先: `Cc["@mozilla.org/places/frecency-recalculator;1"].getService()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`

## TableViewer.start()
- 位置: async L102-106
- 役割: 表を組み立ててすぐ一度描画し、10 秒ごとに再描画するタイマーを張る
- 触るとき: 表を開いても値が更新されない、または更新が重なるときに見る。metadata の選択時は start が二度呼ばれ、タイマーも二つ張られる
- 呼び出し先: `setInterval()`, `this.setupUI()`, `this.updateDisplay()`, `this.updateDisplay.bind()`
- 参照: `this.#timer`

## TableViewer.pause()
- 位置: L111-116
- 役割: 再描画タイマーを止める。再開するには start を呼ぶ
- 触るとき: カテゴリーを切り替えた後も、離れた表が更新され続けないかを確かめるとき
- 条件付き依存: `if (this.#timer)` → `clearInterval()`
- 参照: `this.#timer`

## TableViewer.setupUI()
- 位置: L122-185
- 役割: タイトルと上限件数の表示を設定し、列見出しと maxRows 行の空セルを作って、列数に合わせた縞模様の CSS を組み直す
- 触るとき: 列を増やしたり減らしたりしたとき。縞模様の数式は列数に依存するので、見た目が崩れないか確かめる
- 呼び出し先: `columnDiv.classList.add()`, `columnDiv.setAttribute()`, `document.createDocumentFragment()`, `document.createElement()`, `document.getElementById()`, `header.appendChild()`, `row.appendChild()`, `tableBody.appendChild()`, `this.columnMap.entries()`, `viewer.appendChild()`
- 参照: `columnDiv.textContent`, `details.header`, `document.getElementById("title").textContent`, `existingStyle.innerText`, `limit.textContent`, `this.#lastFilledRows`, `this.columnMap.size`, `this.cssGridTemplateColumns`, `this.maxRows`, `this.title`, `viewer.textContent`

## TableViewer.displayData()
- 位置: L194-229
- 役割: 表示中のハンドラーと一致するときだけ行を書き込み、前回より減った行は空にして、最後に並び順の表示を更新する
- 触るとき: 表の値がずれる、または古い行が残るとき。modifier による整形はここで適用される
- 呼び出し先: `details.modifier()`, `document.getElementById()`, `this.columnMap.entries()`, `this.updateDisplayedSort()`
- 条件付き依存: `if (details.includeTitle)` → `viewer.children[index].setAttribute()`
- 条件付き依存: `if (numRows < this.#lastFilledRows)` → `viewer.children[index].removeAttribute()`
- 参照: `details.includeTitle`, `details.modifier`, `rows.length`, `this.#lastFilledRows`, `this.columnMap.size`, `viewer.children`, `viewer.children[index].textContent`

## TableViewer.updateDisplayedSort()
- 位置: L231-251
- 役割: 並び替えの対象列の見出しに、昇順または降順を示す矢印を付ける
- 触るとき: 並び替えの向きの表示が実際の並びと合わないとき
- 条件付き依存: `if (this.sortable)` → `document.getElementById()`
- 条件付き依存: `if (this.sortable)` → `viewer.querySelector()`
- 条件付き依存: `if (!symbolHolder)` → `document.createElement()`
- 条件付き依存: `if (this.sortable)` → `element.appendChild()`
- 参照: `SortingType.DESCENDING`, `symbolHolder.id`, `symbolHolder.style.marginLeft`, `symbolHolder.style.pointerEvents`, `symbolHolder.textContent`, `this.sortSetting.column`, `this.sortSetting.order`, `this.sortable`

## TableViewer.changeSort()
- 位置: L253-262
- 役割: 同じ列なら昇順と降順を入れ替え、別の列なら降順で並べ直す
- 触るとき: 列見出しをクリックしたときの並び順の決まり方を変えるとき
- 参照: `SortingType.ASCENDING`, `SortingType.DESCENDING`, `this.sortSetting`, `this.sortSetting.column`, `this.sortSetting.order`

## TableViewer.sortable()
- 位置: L264-266
- 役割: 並び替えの設定があるかどうかを返す getter
- 触るとき: 並び替えを許さない表を作るとき。sortSetting を null にすると列見出しのクリックが無効になる
- 参照: `this.sortSetting`

## modifier()
- 位置: L287-287
- 役割: updated_at のミリ秒を、ローカルの日時文字列に変換する
- 触るとき: メタデータ表の更新日時の表示形式を変えるとき
- 呼び出し先: `new Date(updatedAt).toLocaleString()`

## modifier()
- 位置: L294-294
- 役割: 総閲覧時間をミリ秒から秒にし、小数第 2 位まで表示する
- 触るとき: 閲覧時間の単位や桁数を変えるとき
- 呼び出し先: `(totalViewTime / 1000).toFixed()`

## modifier()
- 位置: L301-301
- 役割: 入力時間をミリ秒から秒にし、小数第 2 位まで表示する
- 触るとき: 入力時間の単位や桁数を変えるとき
- 呼び出し先: `(typingTime / 1000).toFixed()`

## modifier()
- 位置: L309-309
- 役割: スクロール時間をミリ秒から秒にし、小数第 2 位まで表示する
- 触るとき: スクロール時間の単位や桁数を変えるとき
- 呼び出し先: `(scrollingTime / 1000).toFixed()`

## #getRows()
- 位置: async L325-337
- 役割: DB 接続を初回だけ開いてクエリを実行し、指定した列だけを持つオブジェクトの配列にする
- 触るとき: メタデータ表が読む列や SQL を変えるとき。接続はインスタンス内で使い回される
- 呼び出し先: `r.getResultByName()`, `rows.map()`, `this.#db.executeCached()`, `this.columnMap.keys()`
- 条件付き依存: `if (!this.#db)` → `PlacesUtils.promiseDBConnection()`
- 参照: `this.#db`

## updateDisplay()
- 位置: async L342-353
- 役割: moz_places_metadata を現在の並び順で maxRows 件まで読み、表に表示する
- 触るとき: メタデータ表の件数や並び順の既定値を変えるとき。LIMIT は maxRows の値で決まる
- 呼び出し先: `this.#getRows()`, `this.displayData()`
- 参照: `this.maxRows`, `this.sortSetting.column`, `this.sortSetting.order`

## export()
- 位置: L355-407
- 役割: メタデータを全件読み出す。includeUrlAndTitle が true なら URL とタイトルを含め、false なら place_id などの ID を含める
- 触るとき: JSON や CSV の書き出し項目を変えるとき。引数によって select する列が変わる点に注意
- 呼び出し先: `this.#getRows()`

## modifier()
- 位置: L427-427
- 役割: Places の各エンティティのサイズをバイトから KiB に換算する
- 触るとき: 統計表のサイズの単位を変えるとき

## updateDisplay()
- 位置: async L453-456
- 役割: PlacesDBUtils から統計と件数を取得し、統計表に表示する
- 触るとき: 統計表の中身を変えるとき。10 秒ごとの再描画のたびに取得し直す
- 呼び出し先: `PlacesDBUtils.getEntitiesStatsAndCounts()`, `this.displayData()`

## modifier()
- 位置: L478-479
- 役割: 最終訪問日時を 1000 で割ってミリ秒にし、ローカルの日時文字列に変換する
- 触るとき: frecency 一覧の最終訪問日時の表示を変えるとき。元の値はマイクロ秒として扱われている
- 呼び出し先: `new Date(lastVisitDate / 1000).toLocaleString()`

## #getRows()
- 位置: async L505-517
- 役割: DB 接続を初回だけ開いてクエリを実行し、指定した列だけを持つオブジェクトの配列にする
- 触るとき: frecency 一覧が読む列や SQL を変えるとき
- 呼び出し先: `r.getResultByName()`, `rows.map()`, `this.#db.executeCached()`, `this.columnMap.keys()`
- 条件付き依存: `if (!this.#db)` → `PlacesUtils.promiseDBConnection()`
- 参照: `this.#db`

## updateDisplay()
- 位置: async L522-538
- 役割: moz_places を現在の並び順で 100 件まで読み、frecency 一覧に表示する
- 触るとき: frecency 一覧に出す列や件数を変えるとき
- 呼び出し先: `this.#getRows()`, `this.displayData()`
- 参照: `this.#maxRows`, `this.sortSetting.column`, `this.sortSetting.order`

## checkPrefs()
- 位置: L541-548
- 役割: browser.places.interactions.enabled が false のとき、無効であることを示す警告欄を表示する
- 触るとき: Interactions 機能が無効なときの案内を変えるとき
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("browser.places.interactions.enabled", false) )` → `document.getElementById()`
- 参照: `warning.hidden`
- XPCOM: `Services.prefs`

## show()
- 位置: L550-571
- 役割: 選んだカテゴリーの表示を切り替え、現在のハンドラーを止めてから選ばれた表のハンドラーを起動する
- 触るとき: カテゴリーを切り替えて表示が乱れる、または更新が二重になるとき。metadata の分岐では start() が二回呼ばれ、片方のタイマー参照が失われる
- 呼び出し先: `(gCurrentHandler = metadataHandler).start()`, `(gCurrentHandler = placesStatsHandler).start()`, `(gCurrentHandler = placesViewerHandler).start()`, `currentButton.classList.remove()`, `document.querySelector()`, `gCurrentHandler.pause()`, `metadataHandler.start()`, `selectedButton.classList.add()`, `selectedButton.getAttribute()`

## createObjectURL()
- 位置: L573-594
- 役割: データを Blob の object URL にする。デバッグビルドでは null principal の sandbox 内で作る
- 触るとき: 書き出しファイルの URL 生成を変えるとき。デバッグビルドでは eval 相当の経路を通る点に注意
- 呼び出し先: `window.URL.createObjectURL()`
- 条件付き依存: `if (AppConstants.DEBUG)` → `data.replaceAll("'", "\\'").replaceAll()`
- 条件付き依存: `if (AppConstants.DEBUG)` → `data.replaceAll()`
- 条件付き依存: `if (AppConstants.DEBUG)` → `Cu.evalInSandbox()`
- 参照: `AppConstants.DEBUG`, `Cu.Sandbox`

## downloadFile()
- 位置: L596-602
- 役割: places-<時刻>.<拡張子> という名前で、データを一時的なリンクからダウンロードさせる
- 触るとき: 書き出しファイルの名前や種類を変えるとき
- 呼び出し先: `Date.now()`, `a.click()`, `a.remove()`, `a.setAttribute()`, `createObjectURL()`, `document.createElement()`

## getData()
- 位置: async L604-608
- 役割: 「URL とタイトルを含める」のチェックボックスの状態に応じて、メタデータを書き出し用に読み出す
- 触るとき: 書き出しに URL やタイトルが含まれない理由を調べるとき
- 呼び出し先: `document.getElementById()`, `metadataHandler.export()`
- 参照: `document.getElementById("include-place-data").checked`

## setupListeners()
- 位置: L610-656
- 役割: カテゴリーの切り替え、JSON と CSV の書き出し、frecency の再計算ボタン、列見出しのクリックにイベントを割り当てる
- 触るとき: 画面の操作を追加・変更するとき。列見出しのクリックは並び替え可能な表でだけ動く
- 呼び出し先: `JSON.stringify()`, `Object.keys()`, `data.at()`, `data.map()`, `document .getElementById()`, `document .getElementById("recalc-alt-frecency") .addEventListener()`, `document.getElementById()`, `document.getElementById("export-csv").addEventListener()`, `document.getElementById("export-json").addEventListener()`, `document.getElementById("tableViewer").addEventListener()`, `downloadFile()`, `e.preventDefault()`, `getData()`, `headers.join()`, `headers.map()`, `headers.map(field => JSON.stringify(obj[field] ?? "")).join()`, `lazy.PlacesFrecencyRecalculator.recalculateAnyOutdatedFrecencies()`, `menu.addEventListener()`, `rows.join()`
- 条件付き依存: `if (e.target && e.target.parentNode == menu)` → `show()`
- 条件付き依存: `if (gCurrentHandler.sortable && e.target.dataset.columnTitle)` → `gCurrentHandler.changeSort()`
- 条件付き依存: `if (gCurrentHandler.sortable && e.target.dataset.columnTitle)` → `gCurrentHandler.updateDisplay()`
- 参照: `e.target`, `e.target.dataset.columnTitle`, `e.target.parentNode`, `gCurrentHandler.sortable`
