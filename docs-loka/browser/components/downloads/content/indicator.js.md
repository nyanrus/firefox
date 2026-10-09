# browser/components/downloads/content/indicator.js

source: browser/components/downloads/content/indicator.js
source-hash: 3d7d4aece537362831f16c3258e160f28f23b390
lines: 689

## <module>
- 役割: ダウンロードの進捗を示すボタン(ツールバーのインジケーター)と、そのパネルのアンカーを管理する。DownloadsButton と DownloadsIndicatorView を定義する。
- 呼び出し先: `Object.defineProperty()`

## _placeholder()
- 位置: L41-43
- 役割: ツールバー上の downloads-button 要素を id で取得する。
- 触るとき: ボタンの要素 ID を変えるとき、またはボタンが取り外されているかを判定するとき。
- 呼び出し先: `document.getElementById()`

## initializeIndicator()
- 位置: L56-58
- 役割: インジケーターの表示用ビューを初期化する。ウィンドウ生成の後に非同期で呼ばれる。
- 触るとき: 起動時に読み込む処理を増やしてウィンドウの起動が遅くならないか確かめるとき。
- 呼び出し先: `DownloadsIndicatorView.ensureInitialized()`

## _getAnchorInternal()
- 位置: L66-85
- 役割: パネルの表示要求の有無に応じてボタンの open を切り替え、表示できるならそのアンカー要素を返す。非表示ツールバー上なら null を返す。
- 触るとき: パネルのアンカーがどの要素になるかを変えるとき、または非表示ツールバーでの扱いを調べるとき。
- 呼び出し先: `CustomizableUI.getWidget()`, `isElementVisible()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `DownloadsIndicatorView.indicator`, `DownloadsIndicatorView.indicatorAnchor`, `indicator.open`, `indicator.parentNode`, `this._anchorRequested`, `widget.areaType`

## getAnchor()
- 位置: L100-108
- 役割: カスタマイズ中は null を返し、それ以外はアンカーを要求して _getAnchorInternal の結果を返す。
- 触るとき: パネルを開く直前にアンカーを確保する仕組みを変えるとき。
- 呼び出し先: `this._getAnchorInternal()`
- 参照: `this._anchorRequested`, `this._customizing`

## releaseAnchor()
- 位置: L113-116
- 役割: 一時アンカーの要求を取り消し、_getAnchorInternal で不要なら隠せるようにする。
- 触るとき: パネルを閉じた後にボタンを隠すタイミングを変えるとき。
- 呼び出し先: `this._getAnchorInternal()`
- 参照: `this._anchorRequested`

## unhide()
- 位置: L130-144
- 役割: 隠れている downloads-button を表示にする。includePalette が true ならパレット内の要素も探し、ナビバーに出ている時は属性を付ける。
- 触るとき: ボタンを表示させる経路を増やすとき、またはカスタマイズ開始時に隠れたボタンを見せる処理を調べるとき。
- 呼び出し先: `button.hasAttribute()`
- 条件付き依存: `if (!button && includePalette)` → `gNavToolbox.palette.querySelector()`
- 条件付き依存: `if (button && button.hasAttribute("hidden"))` → `button.removeAttribute()`
- 条件付き依存: `if (button && button.hasAttribute("hidden"))` → `this._navBar.contains()`
- 条件付き依存: `if (this._navBar.contains(button))` → `this._navBar.setAttribute()`
- 参照: `this._placeholder`

## hide()
- 位置: L146-153
- 役割: 自動非表示が有効でボタンがツールバー内にあれば、パネルを閉じてボタンを隠す。
- 触るとき: 自動非表示の条件や、隠すときに閉じる対象を変えるとき。
- 呼び出し先: `button.closest()`
- 条件付き依存: `if (this.autoHideDownloadsButton && button && button.closest("toolbar"))` → `DownloadsPanel.hidePanel()`
- 条件付き依存: `if (this.autoHideDownloadsButton && button && button.closest("toolbar"))` → `this._navBar.removeAttribute()`
- 参照: `button.hidden`, `this._placeholder`, `this.autoHideDownloadsButton`

## startAutoHide()
- 位置: L155-161
- 役割: ダウンロードがあれば表示し、なければ隠す。
- 触るとき: ダウンロードの有無と表示状態の対応を変えるとき。
- 条件付き依存: `if (DownloadsIndicatorView.hasDownloads)` → `this.unhide()`
- 条件付き依存: `if (!(DownloadsIndicatorView.hasDownloads))` → `this.hide()`
- 参照: `DownloadsIndicatorView.hasDownloads`

## checkForAutoHide()
- 位置: L163-175
- 役割: カスタマイズ中でなく自動非表示が有効で、ツールバー上にあるときだけ自動非表示を判定し、それ以外は表示する。
- 触るとき: 自動非表示の判定条件(設定、カスタマイズ中、配置先)を変えるとき。
- 呼び出し先: `button.closest()`
- 条件付き依存: `if ( !this._customizing && this.autoHideDownloadsButton && button && button.closest("toolbar") )` → `this.startAutoHide()`
- 条件付き依存: `if (!( !this._customizing && this.autoHideDownloadsButton && button && button.closest("toolbar") ))` → `this.unhide()`
- 参照: `this._customizing`, `this._placeholder`, `this.autoHideDownloadsButton`

## onWidgetAfterDOMChange()
- 位置: L180-184
- 役割: CustomizableUI でウィジェットの DOM が動いたとき、対象がボタンなら自動非表示を判定し直す。
- 触るとき: ボタンを別の場所へ移したときの表示状態が正しいかを確かめるとき。
- 条件付き依存: `if (node == this._placeholder)` → `this.checkForAutoHide()`
- 参照: `this._placeholder`

## onCustomizeStart()
- 位置: L194-202
- 役割: このウィンドウのカスタマイズ開始時に、一時アンカーを止め、ボタンを表示して placeholder として使えるようにする。
- 触るとき: カスタマイズ中のボタンの扱いを変えるとき。
- 条件付き依存: `if (win == window)` → `this.unhide()`
- 参照: `this._anchorRequested`, `this._customizing`

## onCustomizeEnd()
- 位置: L204-210
- 役割: カスタマイズ終了時にカスタマイズ中の状態を戻し、自動非表示を判定し直して afterCustomize を呼ぶ。
- 触るとき: カスタマイズ後にビューを作り直す条件を変えるとき。
- 条件付き依存: `if (win == window)` → `this.checkForAutoHide()`
- 条件付き依存: `if (win == window)` → `DownloadsIndicatorView.afterCustomize()`
- 参照: `this._customizing`

## init()
- 位置: L212-223
- 役割: browser.download.autohideButton の設定を監視対象にし、CustomizableUI のリスナを登録して、初期の自動非表示を判定する。
- 触るとき: 自動非表示の設定を読む仕組みや、初期化の順序を変えるとき。
- 呼び出し先: `CustomizableUI.addListener()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `this.checkForAutoHide()`, `this.checkForAutoHide.bind()`

## uninit()
- 位置: L225-227
- 役割: CustomizableUI のリスナを外す。
- 触るとき: ウィンドウ終了時の後始末を確かめるとき。
- 呼び出し先: `CustomizableUI.removeListener()`

## _tabsToolbar()
- 位置: L229-232
- 役割: TabsToolbar 要素を遅延取得する。
- 触るとき: タブバーの ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._tabsToolbar`

## _navBar()
- 位置: L234-237
- 役割: nav-bar 要素を遅延取得する。
- 触るとき: ナビゲーションバーの ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._navBar`

## ensureInitialized()
- 位置: L269-278
- 役割: ビューを一度だけ初期化し、unload と visibilitychange を監視して、インジケーターのデータビューとして登録する。
- 触るとき: インジケーターがデータ更新を受け取り始める条件を変えるとき。
- 呼び出し先: `DownloadsCommon.getIndicatorData()`, `DownloadsCommon.getIndicatorData(window).addView()`, `window.addEventListener()`
- 参照: `this._initialized`

## ensureTerminated()
- 位置: L283-297
- 役割: ビューの購読と監視を外し、進捗と注目の表示を初期値に戻して、一時アンカーでも中立の表示になるようにする。
- 触るとき: ウィンドウを閉じたときや作り直すときの表示のリセットを変えるとき。
- 呼び出し先: `DownloadsCommon.getIndicatorData()`, `DownloadsCommon.getIndicatorData(window).removeView()`, `window.removeEventListener()`
- 参照: `DownloadsCommon.ATTENTION_NONE`, `this._initialized`, `this.attention`, `this.percentComplete`

## _ensureOperational()
- 位置: L303-321
- 役割: ボタン要素が見つかった時に運用可能の状態にし、初期化済みなら表示を更新する。要素がなければ何もしない。
- 触るとき: 要素の読み込みタイミングと表示更新の関係を変えるとき。
- 条件付き依存: `if (this._initialized)` → `DownloadsCommon.getIndicatorData(window).refreshView()`
- 条件付き依存: `if (this._initialized)` → `DownloadsCommon.getIndicatorData()`
- 参照: `DownloadsButton._placeholder`, `this._initialized`, `this._operational`

## _isAncestorPanelOpen()
- 位置: L342-347
- 役割: 指定ノードの祖先にある panel が open かを返す。
- 触るとき: メニューパネルの中にあるボタンでの通知表示の条件を変えるとき。
- 参照: `aNode.localName`, `aNode.parentNode`, `aNode.state`

## showEventNotification()
- 位置: L355-369
- 役割: 初期化済みなら、開始または完了の通知を表示する。表示中なら、種類が違う時だけ次の通知として待たせる。
- 触るとき: ダウンロードの開始や完了時にボタンを光らせる通知の条件を変えるとき。
- 条件付き依存: `if (!(this._currentNotificationType))` → `this._showNotification()`
- 参照: `this._currentNotificationType`, `this._initialized`, `this._nextNotificationType`

## _showNotification()
- 位置: L378-443
- 役割: ボタンが見えていて reduced-motion でなければ、通知の属性を付けてアニメーションを開始する。アニメーション終了か時間切れで後始末し、待ちの通知があれば続けて出す。
- 触るとき: 通知アニメーションの時間、終了判定、待ち行列の扱いを変えるとき。時間は indicator.css と合わせる必要がある。
- 呼び出し先: `anchor.addEventListener()`, `anchor.documentGlobal.matchMedia()`, `anchor.documentGlobal.setTimeout()`, `anchor.setAttribute()`, `anchor.toggleAttribute()`, `isElementVisible()`
- 参照: `DownloadsButton._placeholder`, `anchor.documentGlobal.matchMedia("(prefers-reduced-motion)").matches`, `anchor.parentNode`, `this._currentNotificationType`, `this._wasHidden`

## finalize()
- 位置: L402-423
- 役割: 通知の後始末を一度だけ行い、属性を外して、待ちの通知があれば次を表示する。
- 触るとき: 通知が終わった後の状態遷移を変えるとき。
- 呼び出し先: `anchor.documentGlobal.clearTimeout()`, `anchor.removeAttribute()`, `anchor.removeEventListener()`, `isElementVisible()`, `requestAnimationFrame()`
- 条件付き依存: `if (nextType && isElementVisible(anchor.parentNode))` → `this._showNotification()`
- 参照: `anchor.parentNode`, `this._currentNotificationType`, `this._nextNotificationType`

## onNotificationAnimEnd()
- 位置: L425-433
- 役割: 対象のアニメーション名で終わったときだけ finalize を呼ぶ。
- 触るとき: 通知アニメーションの名前を変えるとき。
- 呼び出し先: `finalize()`
- 参照: `event.animationName`

## hasDownloads()
- 位置: L451-464
- 役割: ダウンロードの有無を保存する。有効化のときは隠れていたボタンを表示して運用可能にし、無効化のときは自動非表示を判定する。
- 触るとき: ダウンロードが増えたときや無くなったときに、ボタンの表示をどう変えるかを変えるとき。
- 条件付き依存: `if (aValue)` → `DownloadsButton.unhide()`
- 条件付き依存: `if (aValue)` → `this._ensureOperational()`
- 条件付き依存: `if (!(aValue))` → `DownloadsButton.checkForAutoHide()`
- 参照: `this._hasDownloads`, `this._operational`, `this._wasHidden`

## hasDownloads()
- 位置: L465-467
- 役割: 保存した hasDownloads の値を返す。
- 触るとき: ボタンを表示すべきかの判定を他の処理から参照するとき。
- 参照: `this._hasDownloads`

## percentComplete()
- 位置: L474-489
- 役割: 進捗率(0から100、不明は -1)を保存し、初めての進捗では開始通知を先に出し、注目と進捗の表示を更新する。
- 触るとき: 進捗表示のちらつき対策や進捗の更新条件を変えるとき。
- 呼び出し先: `Math.min()`
- 条件付き依存: `if (this._percentComplete < 0 && aValue >= 0)` → `this.showEventNotification()`
- 条件付き依存: `if (this._percentComplete !== aValue)` → `this._refreshAttention()`
- 条件付き依存: `if (this._percentComplete !== aValue)` → `this._maybeScheduleProgressUpdate()`
- 参照: `this._operational`, `this._percentComplete`

## _maybeScheduleProgressUpdate()
- 位置: L491-519
- 役割: ボタンが見えていて再描画待ちでなければ、次のフレームで進捗のクラスと円グラフの割合を更新する。割合は最低10%で表示する。
- 触るとき: 進捗の見た目(円グラフの割合、不確定の表示)を変えるとき。
- 条件付き依存: `if ( this.indicator && !this._progressRaf && document.visibilityState == "visible" )` → `requestAnimationFrame()`
- 条件付き依存: `if (this._percentComplete >= 0)` → `this.indicator.hasAttribute()`
- 条件付き依存: `if (!this.indicator.hasAttribute("progress"))` → `this.indicator.setAttribute()`
- 条件付き依存: `if (this._percentComplete >= 0)` → `this._progressIcon.style.setProperty()`
- 条件付き依存: `if (this._percentComplete >= 0)` → `Math.max()`
- 条件付き依存: `if (!(this._percentComplete >= 0))` → `this.indicator.removeAttribute()`
- 条件付き依存: `if (!(this._percentComplete >= 0))` → `this._progressIcon.style.setProperty()`
- 参照: `document.visibilityState`, `this._percentComplete`, `this._progressRaf`, `this.indicator`

## attention()
- 位置: L525-533
- 役割: 注目の状態を保存し、変わっていれば表示を更新する。
- 触るとき: 注目表示の状態を別の処理から設定するとき。
- 条件付き依存: `if (this._attention != aValue)` → `this._refreshAttention()`
- 参照: `this._attention`, `this._operational`

## _refreshAttention()
- 位置: L535-556
- 役割: 注目の属性を反映する。ツールバーで進捗表示中の成功は抑え、メニュー内のボタンなら注目を出す。
- 触るとき: 成功時の注目表示をどの場所で抑えるかを変えるとき。
- 呼び出し先: `CustomizableUI.getWidget()`
- 条件付き依存: `if ( suppressAttention || this._attention == DownloadsCommon.ATTENTION_NONE )` → `this.indicator.removeAttribute()`
- 条件付き依存: `if (!( suppressAttention || this._attention == DownloadsCommon.ATTENTION_NONE ))` → `this.indicator.setAttribute()`
- 参照: `CustomizableUI.TYPE_PANEL`, `DownloadsCommon.ATTENTION_NONE`, `DownloadsCommon.ATTENTION_SUCCESS`, `this._attention`, `this._percentComplete`, `widgetGroup.areaType`

## handleEvent()
- 位置: L560-570
- 役割: unload では ensureTerminated を呼び、visibilitychange では進捗の更新を予約する。
- 触るとき: ウィンドウの状態変化に対する反応を増やすとき。
- 呼び出し先: `this._maybeScheduleProgressUpdate()`, `this.ensureTerminated()`
- 参照: `aEvent.type`

## onCommand()
- 位置: L572-589
- 役割: ボタンのクリックや Enter、Space でダウンロードパネルを手動で開き、イベントを止める。Mac で ctrl を押したクリックや、主ボタン以外は無視する。
- 触るとき: ボタンを押したときのパネルの開き方や、無視する入力を変えるとき。
- 呼び出し先: `DownloadsPanel.showPanel()`, `aEvent.stopPropagation()`, `aEvent.type.startsWith()`
- 参照: `AppConstants.platform`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.key`, `aEvent.type`

## onDragOver()
- 位置: L591-593
- 役割: ドラッグの移動を ToolbarDropHandler に任せる。
- 触るとき: ボタン上へのドラッグ時の受け入れ判定を変えるとき。
- 呼び出し先: `ToolbarDropHandler.onDragOver()`

## onDrop()
- 位置: L595-631
- 役割: ボタンへドロップされたリンクを、about: 以外は saveURL で保存する。ダウンロード項目自身のドラッグは無視する。
- 触るとき: ドロップによるダウンロードの対象や保存の仕方を変えるとき。
- 呼び出し先: `Services.droppedLinkHandler.dropLinks()`, `dt.mozGetDataAt()`, `link.url.startsWith()`, `saveURL()`
- 条件付き依存: `if (handled)` → `aEvent.preventDefault()`
- 参照: `aEvent.dataTransfer`, `dt.mozSourceNode`, `dt.mozSourceNode.ownerDocument`, `link.name`, `link.url`, `links.length`
- XPCOM: `Services.droppedLinkHandler`

## indicator()
- 位置: L640-646
- 役割: downloads-button 要素を遅延取得して保持する。
- 触るとき: インジケーターの ID を変えるとき。
- 条件付き依存: `if (!this._indicator)` → `document.getElementById()`
- 参照: `this._indicator`

## indicatorAnchor()
- 位置: L648-656
- 役割: ボタンがメニュー内にあればそのオーバーフローアイコンを、ツールバーにあればバッジのスタックを返す。
- 触るとき: パネルのアンカーの位置を変えるとき。
- 呼び出し先: `CustomizableUI.getWidget()`
- 条件付き依存: `if (widgetGroup.areaType == CustomizableUI.TYPE_PANEL)` → `widgetGroup.forWindow()`
- 参照: `CustomizableUI.TYPE_PANEL`, `overflowIcon.icon`, `this.indicator.badgeStack`, `widgetGroup.areaType`, `widgetGroup.forWindow(window).anchor`

## _progressIcon()
- 位置: L658-665
- 役割: 進捗の円グラフ要素 downloads-indicator-progress-inner を取得し、保持する。
- 触るとき: 進捗アイコンの ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.__progressIcon`

## _onCustomizedAway()
- 位置: L667-670
- 役割: カスタマイズでボタンの要素が変わったとき、保持している要素の参照を消す。
- 触るとき: 要素の参照の持ち方を変えるとき。
- 参照: `this.__progressIcon`, `this._indicator`

## afterCustomize()
- 位置: L672-681
- 役割: 保持している要素が現在の文書の要素と違えば、参照を消して終了と初期化をやり直す。
- 触るとき: カスタマイズ後にボタンの表示が古いままにならないかを確かめるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (this._indicator != document.getElementById("downloads-button"))` → `this._onCustomizedAway()`
- 条件付き依存: `if (this._indicator != document.getElementById("downloads-button"))` → `this.ensureTerminated()`
- 条件付き依存: `if (this._indicator != document.getElementById("downloads-button"))` → `this.ensureInitialized()`
- 参照: `this._indicator`, `this._operational`
