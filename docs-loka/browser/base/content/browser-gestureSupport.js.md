# browser/base/content/browser-gestureSupport.js

source: browser/base/content/browser-gestureSupport.js
source-hash: 89aef994819370b0577923f488690558f010cdec
lines: 1062

## <module>
- 役割: ページへのジェスチャーイベントを捕捉し、戻る・進む・ズーム・回転などのコマンドに変換する gGestureSupport と履歴スワイプアニメーションの gHistorySwipeAnimation を定義する
- 呼び出し先: `aArray.reduce()`

## init()
- 位置: L27-29
- 役割: ジェスチャー用のイベントリスナーを tabbox に登録する。
- 触るとき: ジェスチャーの有効化タイミングを変えるとき。
- 呼び出し先: `this._toggleListeners()`

## uninit()
- 位置: L34-36
- 役割: ジェスチャー用のイベントリスナーを tabbox から外す。
- 触るとき: ウィンドウ終了時の解除処理を調べるとき。
- 呼び出し先: `this._toggleListeners()`

## _toggleListeners()
- 位置: L44-68
- 役割: Moz で始まるジェスチャーイベント一覧を、キャプチャ段階で追加または削除する。
- 触るとき: 捕捉するジェスチャーイベントの種類を増減するとき。
- 条件付き依存: `if (aAddListener)` → `gBrowser.tabbox.addEventListener()`
- 条件付き依存: `if (!(aAddListener))` → `gBrowser.tabbox.removeEventListener()`

## GS_handleEvent()
- 位置: L78-139
- 役割: ジェスチャーイベントを伝播止めし、種類ごとに既定動作の抑止と各種処理への振り分けを行う。
- 触るとき: ジェスチャー種別ごとの処理を追加・変更するとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `aEvent.preventDefault()`, `def()`, `this._doAction()`, `this._doEnd()`, `this._doUpdate()`, `this._setupGesture()`, `this._setupSwipeGesture()`, `this._shouldDoSwipeGesture()`, `this.onSwipe()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref( "dom.debug.propagate_gesture_events_through_content" ) )` → `aEvent.stopPropagation()`
- 条件付き依存: `if (this._shouldDoSwipeGesture(aEvent))` → `aEvent.preventDefault()`
- 参照: `aEvent.type`
- XPCOM: `Services.prefs`

## def()
- 位置: L88-91
- 役割: 閾値と latch の設定を持つ既定値オブジェクトを作る小さな補助関数。
- 触るとき: ピンチや回転の既定値を変えるとき。

## GS__setupGesture()
- 位置: L156-198
- 役割: ピンチや回転の開始時に設定を読み、累積量が閾値を超えたら対応コマンドを実行する _doUpdate を用意する。
- 触るとき: ピンチや回転のしきい値・ラッチの挙動を変えるとき。
- 呼び出し先: `Object.entries()`, `this._doUpdate()`, `this._getPref()`
- 参照: `aEvent.delta`, `this._doUpdate`

## GS__doUpdate()
- 位置: L174-194
- 役割: ピンチや回転の累積量を更新し、閾値超過で方向に応じたコマンドを実行してラッチ状態を切り替える。
- 触るとき: ピンチや回転で発火するタイミングや方向判定を変えるとき。
- 呼び出し先: `Math.abs()`
- 条件付き依存: `if (!aPref.latched || isLatched ^ sameDir)` → `this._doAction()`
- 参照: `aPref.latched`, `aPref.threshold`, `updateEvent.delta`

## GS__swipeNavigatesHistory()
- 位置: L210-220
- 役割: 左右スワイプのどちらかに戻る・進むのコマンドが割り当てられているかを判定する。
- 触るとき: スワイプで履歴移動が起きる条件を変えるとき。

## GS__shouldDoSwipeGesture()
- 位置: L231-291
- 役割: スワイプで履歴移動できるかを判定し、可能な方向を allowedDirections に設定する。
- 触るとき: スワイプ開始の可否や許可方向のルールを変えるとき。
- 呼び出し先: `document.documentElement.hasAttribute()`, `gHistorySwipeAnimation.canGoBack()`, `gHistorySwipeAnimation.canGoForward()`, `this._getCommand()`, `this._swipeNavigatesHistory()`
- 参照: `aEvent.DIRECTION_DOWN`, `aEvent.DIRECTION_LEFT`, `aEvent.DIRECTION_RIGHT`, `aEvent.DIRECTION_UP`, `aEvent.allowedDirections`, `aEvent.direction`, `gHistorySwipeAnimation.isLTR`, `window.content.pageYOffset`, `window.content.scrollMaxY`

## GS__setupSwipeGesture()
- 位置: L302-318
- 役割: スワイプ開始時に履歴アニメーションを始め、更新・終了を gHistorySwipeAnimation へ流す関数を差し替える。
- 触るとき: スワイプ中の更新・終了の受け渡しを変えるとき。
- 呼び出し先: `gHistorySwipeAnimation.startAnimation()`
- 参照: `this._doEnd`, `this._doUpdate`

## GS__doUpdate()
- 位置: L305-310
- 役割: スワイプの更新量を履歴アニメーションの updateAnimation へ渡す。
- 触るとき: スワイプ中のアニメーション更新の入力を変えるとき。
- 呼び出し先: `gHistorySwipeAnimation.updateAnimation()`
- 参照: `aEvent.delta`

## GS__doEnd()
- 位置: L312-317
- 役割: スワイプ終了を履歴アニメーションへ伝え、以後の更新と終了処理を無効化する。
- 触るとき: スワイプ終了後の後始末を変えるとき。
- 呼び出し先: `gHistorySwipeAnimation.swipeEndEventReceived()`
- 参照: `this._doEnd`, `this._doUpdate`

## this._doUpdate()
- 位置: L315-315
- 役割: スワイプ終了後に更新処理を無効化する空関数を設定する。
- 触るとき: スワイプ終了後に更新が呼ばれないことを確認するとき。

## this._doEnd()
- 位置: L316-316
- 役割: スワイプ終了後に終了処理を無効化する空関数を設定する。
- 触るとき: スワイプ終了後に終了処理が二重に走らないことを確認するとき。

## GS__doAction()
- 位置: L353-356
- 役割: ジェスチャーに対応するコマンドを探して実行し、見つからなければ null を返す。
- 触るとき: ジェスチャーから実行されるコマンドの流れを追うとき。
- 呼び出し先: `this._doCommand()`, `this._getCommand()`

## GS__getCommand()
- 位置: L367-393
- 役割: 押下中の修飾キーの組み合わせを優先順に試し、ジェスチャーに対応する設定値のコマンド名を返す。
- 触るとき: 修飾キーごとのジェスチャー割り当ての解決順を変えるとき。
- 呼び出し先: `aGesture.concat()`, `aGesture.concat(subCombo).join()`, `this._getPref()`, `this._power()`
- 条件付き依存: `if (aEvent[key + "Key"])` → `keyCombos.push()`

## GS__doCommand()
- 位置: L403-427
- 役割: コマンド要素が無効でなければ xul command イベントを発火し、無ければ goDoCommand で実行する。
- 触るとき: ジェスチャーからのコマンド実行方法を変えるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (node)` → `node.getAttribute()`
- 条件付き依存: `if (node.getAttribute("disabled") != "true")` → `document.createEvent()`
- 条件付き依存: `if (node.getAttribute("disabled") != "true")` → `cmdEvent.initCommandEvent()`
- 条件付き依存: `if (node.getAttribute("disabled") != "true")` → `node.dispatchEvent()`
- 条件付き依存: `if (!(node))` → `goDoCommand()`
- 参照: `aEvent.altKey`, `aEvent.ctrlKey`, `aEvent.inputSource`, `aEvent.metaKey`, `aEvent.shiftKey`

## _doUpdate()
- 位置: L436-436
- 役割: 連続動作の更新処理の既定値で、何もしない。_setupGesture などで差し替えられる。
- 触るとき: 既定の更新処理が何をするかを確認するとき。

## _doEnd()
- 位置: L444-444
- 役割: ジェスチャー終了処理の既定値で、何もしない。_setupSwipeGesture で差し替えられる。
- 触るとき: 既定の終了処理が何をするかを確認するとき。

## GS_onSwipe()
- 位置: L452-460
- 役割: スワイプの方向を UP・RIGHT・DOWN・LEFT から一つ特定し、アニメーションとの調整に渡す。
- 触るとき: スワイプ方向の判定を変えるとき。
- 条件付き依存: `if (aEvent.direction == aEvent["DIRECTION_" + dir])` → `this._coordinateSwipeEventWithAnimation()`
- 参照: `aEvent.direction`

## GS_processSwipeEvent()
- 位置: L470-489
- 役割: RTL の場合は左右を入れ替えたうえで、スワイプ方向に対応するコマンドを実行する。
- 触るとき: RTL でのスワイプ方向の扱いを調べるとき。
- 呼び出し先: `aDir.toLowerCase()`, `this._doAction()`
- 参照: `gHistorySwipeAnimation.isLTR`

## GS__coordinateSwipeEventWithAnimation()
- 位置: L503-506
- 役割: 実行中の履歴アニメーションを止めてから、スワイプ処理を行う。
- 触るとき: スワイプとアニメーションの順序を変えるとき。
- 呼び出し先: `gHistorySwipeAnimation.stopAnimation()`, `this.processSwipeEvent()`

## GS__getPref()
- 位置: L516-533
- 役割: browser.gesture 配下の設定値を、既定値の型(bool・数値・文字列)に応じて読む。失敗時は既定値を返す。
- 触るとき: ジェスチャー設定の読み方や既定値の扱いを変えるとき。
- 呼び出し先: `Services.prefs["get" + getFunc + "Pref"]()`
- 参照: `Services.prefs`
- XPCOM: `Services.prefs`

## rotate()
- 位置: L541-558
- 役割: 画像ドキュメントの要素に回転変換を適用し、回転角を更新する。
- 触るとき: 画像の回転操作の挙動を変えるとき。
- 呼び出し先: `ImageDocument.isInstance()`, `Math.round()`, `contentElement.classList.contains()`
- 条件付き依存: `if (contentElement.classList.contains("completeRotation"))` → `this._clearCompleteRotation()`
- 参照: `aEvent.delta`, `contentElement.style.transform`, `this._lastRotateDelta`, `this.rotation`, `window.content.document`, `window.content.document.body.firstElementChild`

## rotateEnd()
- 位置: L563-615
- 役割: 回転終了時に最寄りの 90 度単位へスナップさせ、勢いが十分なら一段先まで進める。
- 触るとき: 回転終了時のスナップ先の決め方を変えるとき。
- 呼び出し先: `ImageDocument.isInstance()`
- 条件付き依存: `if (transitionRotation != this.rotation)` → `contentElement.classList.add()`
- 条件付き依存: `if (transitionRotation != this.rotation)` → `contentElement.addEventListener()`
- 参照: `contentElement.style.transform`, `this._clearCompleteRotation`, `this._lastRotateDelta`, `this._rotateMomentumThreshold`, `this.rotation`, `window.content.document`, `window.content.document.body.firstElementChild`

## rotation()
- 位置: L620-622
- 役割: 現在の回転角(_currentRotation)を返す getter。
- 触るとき: 回転角の参照元を調べるとき。
- 参照: `this._currentRotation`

## rotation()
- 位置: L631-636
- 役割: 回転角を 0 以上 360 未満に正規化して保存する setter。
- 触るとき: 回転角の範囲や正規化を変えるとき。
- 参照: `this._currentRotation`

## restoreRotationState()
- 位置: L642-667
- 役割: 画像ドキュメントの現在の transform 行列から回転角を読み戻す。
- 触るとき: ページ遷移後に回転状態を復元する処理を調べるとき。
- 呼び出し先: `ImageDocument.isInstance()`, `Math.atan2()`, `Math.round()`, `transformValue.split()`, `transformValue.split("(")[1].split()`, `transformValue.split("(")[1].split(")")[0].split()`, `window.content.window.getComputedStyle()`
- 参照: `Math.PI`, `this.rotation`, `window.content.document`, `window.content.document.body.firstElementChild`, `window.content.window.getComputedStyle(contentElement).transform`

## _clearCompleteRotation()
- 位置: L672-686
- 役割: 画像要素から completeRotation クラスとイベント監視を外す。
- 触るとき: 回転スナップのアニメーション後始末を変えるとき。
- 呼び出し先: `ImageDocument.isInstance()`, `contentElement.classList.remove()`, `contentElement.removeEventListener()`
- 参照: `this._clearCompleteRotation`, `window.content.document`, `window.content.document.body`, `window.content.document.body.firstElementChild`

## HSA_init()
- 位置: L698-719
- 役割: 履歴スワイプアニメーションの向きを判定し、対応環境かつ無効化されていなければ設定値を読み込んで有効化する。
- 触るとき: 履歴スワイプアニメーションの初期化条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.documentElement.matches()`, `document.getElementById()`, `this._addPrefObserver()`, `this._initPrefValues()`, `this._isSupported()`
- 参照: `this._icon`, `this._isStoppingAnimation`, `this.active`, `this.isLTR`
- XPCOM: `Services.prefs`

## HSA_uninit()
- 位置: L724-730
- 役割: アニメーションの設定監視を外し、状態をリセットして表示用の要素を削除する。
- 触るとき: 履歴スワイプアニメーションの終了処理を変えるとき。
- 呼び出し先: `this._removeBoxes()`, `this._removePrefObserver()`
- 参照: `this._icon`, `this.active`, `this.isLTR`

## HSA_startAnimation()
- 位置: L738-750
- 役割: 既存の要素を作り直し、戻る・進む可否を記録してアニメーションを開始する。
- 触るとき: スワイプ開始時の準備を変えるとき。
- 呼び出し先: `this._removeBoxes()`, `this.canGoBack()`, `this.canGoForward()`, `this.updateAnimation()`
- 条件付き依存: `if (this.active)` → `this._addBoxes()`
- 参照: `this._canGoBack`, `this._canGoForward`, `this._isStoppingAnimation`, `this.active`

## HSA_stopAnimation()
- 位置: L755-784
- 役割: 表示中の矢印を、戻る・進む・取り消しの経路に応じてフェードアウトさせる。
- 触るとき: スワイプ終了時の見た目の後始末を変えるとき。
- 呼び出し先: `this.isAnimationRunning()`
- 条件付き依存: `if (box != null)` → `box.addEventListener()`
- 条件付き依存: `if (box != null)` → `window.getComputedStyle()`
- 条件付き依存: `if (!(box != null))` → `this._removeBoxes()`
- 参照: `box.collapsed`, `box.style.opacity`, `box.style.transition`, `box.style.translate`, `this._isStoppingAnimation`, `this._lastVisibleBox`, `this._lastVisibleTranslate`, `this._nextBox`, `this._nextBox.collapsed`, `this._prevBox`, `this._prevBox.collapsed`, `window.getComputedStyle(box).opacity`

## HSA_swipeCommand()
- 位置: L786-795
- 役割: スワイプ量の符号と向きから、対応する swipe コマンド名を取得する。
- 触るとき: スワイプの向きから履歴操作を決める規則を変えるとき。
- 呼び出し先: `gGestureSupport._getCommand()`
- 参照: `aSwipeUpdate.delta`, `aSwipeUpdate.event`, `this.isLTR`

## HSA_willGoBack()
- 位置: L797-799
- 役割: スワイプが戻る操作になり、かつ戻れる場合に真を返す。
- 触るとき: 戻る操作を示すアニメーションの条件を変えるとき。
- 呼び出し先: `this._swipeCommand()`
- 参照: `this._canGoBack`

## HSA_willGoForward()
- 位置: L801-805
- 役割: スワイプが進む操作になり、かつ進める場合に真を返す。
- 触るとき: 進む操作を示すアニメーションの条件を変えるとき。
- 呼び出し先: `this._swipeCommand()`
- 参照: `this._canGoForward`

## HSA_updateAnimation()
- 位置: L817-887
- 役割: スワイプ量に応じて矢印の位置と半径を更新し、閾値 0.25 超で will-navigate を付けて確定を示す。
- 触るとき: スワイプ中の矢印の見た目や確定の表示を変えるとき。
- 呼び出し先: `Math.abs()`, `Math.min()`, `this._willGoBack()`, `this.isAnimationRunning()`
- 条件付き依存: `if (radius >= 0)` → `this._prevBox .querySelectorAll("circle")[1] .setAttribute()`
- 条件付き依存: `if (radius >= 0)` → `this._prevBox .querySelectorAll()`
- 条件付き依存: `if (this._willGoBack(aSwipeUpdate))` → `Math.abs()`
- 条件付き依存: `if (Math.abs(aSwipeUpdate.delta) >= 0.25)` → `this._prevBox.querySelector("svg").classList.add()`
- 条件付き依存: `if (Math.abs(aSwipeUpdate.delta) >= 0.25)` → `this._prevBox.querySelector()`
- 条件付き依存: `if (!(Math.abs(aSwipeUpdate.delta) >= 0.25))` → `this._prevBox.querySelector("svg").classList.remove()`
- 条件付き依存: `if (!(Math.abs(aSwipeUpdate.delta) >= 0.25))` → `this._prevBox.querySelector()`
- 条件付き依存: `if (!(this._willGoBack(aSwipeUpdate)))` → `this._willGoForward()`
- 条件付き依存: `if (radius >= 0)` → `this._nextBox .querySelectorAll("circle")[1] .setAttribute()`
- 条件付き依存: `if (radius >= 0)` → `this._nextBox .querySelectorAll()`
- 条件付き依存: `if (this._willGoForward(aSwipeUpdate))` → `Math.abs()`
- 条件付き依存: `if (Math.abs(aSwipeUpdate.delta) >= 0.25)` → `this._nextBox.querySelector("svg").classList.add()`
- 条件付き依存: `if (Math.abs(aSwipeUpdate.delta) >= 0.25)` → `this._nextBox.querySelector()`
- 条件付き依存: `if (!(Math.abs(aSwipeUpdate.delta) >= 0.25))` → `this._nextBox.querySelector("svg").classList.remove()`
- 条件付き依存: `if (!(Math.abs(aSwipeUpdate.delta) >= 0.25))` → `this._nextBox.querySelector()`
- 参照: `aSwipeUpdate.delta`, `this._isStoppingAnimation`, `this._lastVisibleBox`, `this._lastVisibleTranslate`, `this._nextBox`, `this._nextBox.collapsed`, `this._nextBox.style.translate`, `this._prevBox`, `this._prevBox.collapsed`, `this._prevBox.style.translate`, `this.isLTR`, `this.maxRadius`, `this.minRadius`, `this.translateEndPosition`, `this.translateStartPosition`

## HSA_isAnimationRunning()
- 位置: L894-896
- 役割: アニメーション用のコンテナが存在するかで、実行中かを返す。
- 触るとき: アニメーション実行中の判定を変えるとき。
- 参照: `this._container`

## HSA_canGoBack()
- 位置: L903-905
- 役割: 現在のブラウザで戻れるかを webNavigation から返す。
- 触るとき: 戻る可否の判定元を調べるとき。
- 参照: `gBrowser.webNavigation.canGoBack`

## HSA_canGoForward()
- 位置: L912-914
- 役割: 現在のブラウザで進めるかを webNavigation から返す。
- 触るとき: 進む可否の判定元を調べるとき。
- 参照: `gBrowser.webNavigation.canGoForward`

## HSA_swipeEndEventReceived()
- 位置: L921-923
- 役割: OS からのスワイプ終了を受け、アニメーションを止める。
- 触るとき: スワイプ終了の受信経路を調べるとき。
- 呼び出し先: `this.stopAnimation()`

## HSA__isSupported()
- 位置: L931-933
- 役割: -moz-swipe-animation-enabled のメディアクエリで、プラットフォームが対応するかを判定する。
- 触るとき: 対応プラットフォームの判定条件を変えるとき。
- 呼び出し先: `window.matchMedia()`
- 参照: `window.matchMedia("(-moz-swipe-animation-enabled)").matches`

## HSA_handleEvent()
- 位置: L935-941
- 役割: transitionend を受けてフェードアウトの後始末を行う。
- 触るとき: フェードアウトの完了処理を変えるとき。
- 呼び出し先: `this._completeFadeOut()`
- 参照: `aEvent.type`

## HSA__completeFadeOut()
- 位置: L943-951
- 役割: 停止中のフェードアウトが完了したら、矢印の要素を削除する。途中で再開されていれば何もしない。
- 触るとき: フェードアウト完了後の後始末を変えるとき。
- 呼び出し先: `gHistorySwipeAnimation._removeBoxes()`
- 参照: `this._isStoppingAnimation`

## HSA__addBoxes()
- 位置: L956-983
- 役割: ブラウザスタック内に前後の矢印の要素を作って追加し、アイコンを複製する。
- 触るとき: 矢印の DOM 構造や配置を変えるとき。
- 呼び出し先: `browserStack.appendChild()`, `gBrowser.getPanel()`, `gBrowser.getPanel().querySelector()`, `icon.classList.add()`, `this._container.appendChild()`, `this._createElement()`, `this._icon.cloneNode()`, `this._nextBox.appendChild()`, `this._prevBox.appendChild()`
- 参照: `this._container`, `this._nextBox`, `this._nextBox.collapsed`, `this._prevBox`, `this._prevBox.collapsed`

## HSA__removeBoxes()
- 位置: L988-997
- 役割: 矢印のコンテナと参照を取り除き、状態を初期化する。
- 触るとき: 矢印要素の破棄や状態のリセットを変えるとき。
- 条件付き依存: `if (this._container)` → `this._container.remove()`
- 参照: `this._container`, `this._lastVisibleBox`, `this._lastVisibleTranslate`, `this._nextBox`, `this._prevBox`

## HSA__createElement()
- 位置: L1008-1012
- 役割: 指定した id と tag の XUL 要素を作る。
- 触るとき: 矢印要素の生成方法を変えるとき。
- 呼び出し先: `document.createXULElement()`
- 参照: `element.id`

## observe()
- 位置: L1014-1019
- 役割: スワイプ矢印の位置や半径の設定が変わったら、値を読み直す。
- 触るとき: 設定変更時の反映を変えるとき。
- 呼び出し先: `this._initPrefValues()`

## HSA__initPrefValues()
- 位置: L1021-1038
- 役割: 矢印の開始・終了位置と最小・最大半径を設定から読み込む。
- 触るとき: 矢印の位置や半径の既定値を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`
- 参照: `this.maxRadius`, `this.minRadius`, `this.translateEndPosition`, `this.translateStartPosition`
- XPCOM: `Services.prefs`

## HSA__addPrefObserver()
- 位置: L1040-1049
- 役割: 矢印の位置と半径の設定を監視するオブザーバーを登録する。
- 触るとき: 監視対象の設定を増減するとき。
- 呼び出し先: `Services.prefs.addObserver()`
- XPCOM: `Services.prefs`

## HSA__removePrefObserver()
- 位置: L1051-1060
- 役割: 矢印の位置と半径の設定監視を解除する。
- 触るとき: 監視解除の漏れを確認するとき。
- 呼び出し先: `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`
