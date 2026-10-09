# browser/components/tabbrowser/content/tab.mjs

source: browser/components/tabbrowser/content/tab.mjs
source-hash: 81c6e5dd4047fc7d57b5938e797a014c71d07cf9
lines: 1107

## <module>
- 役割: 個々のタブ要素 MozTabbrowserTab を定義し、tab を拡張するカスタム要素として登録するモジュール。
- 呼び出し先: `XPCOMUtils.declareLazy()`, `customElements.define()`

## MozTabbrowserTab.constructor()
- 位置: L39-105
- 役割: マウス・ドラッグ・アニメーション・フォーカスのリスナーを登録し、ホバー、ミュート理由、閉じ中などの初期状態を設定する。
- 触るとき: タブ要素が受け取るイベントや、タブの初期プロパティを追加・変更するとき。
- 呼び出し先: `super()`, `this.addEventListener()`

## MozTabbrowserTab.inheritedAttributes()
- 位置: L107-132
- 役割: タブ自身の属性を、内部の各部品(背景、アイコン、ラベル、閉じるボタン等)へ引き継ぐ対応表を返す。
- 触るとき: タブの属性を内部要素のスタイルや表示に反映させたいとき。

## MozTabbrowserTab.connectedCallback()
- 位置: L135-141
- 役割: DOM 接続時にグループ・分割表示の状態を反映し、直前のグループを記憶して初期化する。
- 触るとき: タブがグループや分割表示へ入った直後の状態更新を調べるとき。
- 呼び出し先: `this.#updateOnTabGrouped()`, `this.#updateOnTabSplit()`, `this.initialize()`

## MozTabbrowserTab.disconnectedCallback()
- 位置: L143-146
- 役割: DOM から外れたとき、グループ離脱・分割解除の後始末を行う。
- 触るとき: タブがグループや分割表示から外れたときの状態を調べるとき。
- 呼び出し先: `this.#updateOnTabUngrouped()`, `this.#updateOnTabUnsplit()`

## MozTabbrowserTab.initialize()
- 位置: L148-171
- 役割: 初回のみ、内部のマークアップを追加して属性の引き継ぎ、コンテキストメニュー、ラベルのあふれ監視、aria-level を設定する。
- 触るとき: タブの内部構造や初期化処理を変えるとき。
- 呼び出し先: `labelContainer.addEventListener()`, `this.appendChild()`, `this.initializeAttributeInheritance()`, `this.querySelector()`, `this.setAttribute()`
- 条件付き依存: `if (!("_lastAccessed" in this))` → `this.updateLastAccessed()`

## MozTabbrowserTab.index()
- 位置: L179-181
- 役割: gBrowser.tabs 内でのこのタブの位置(_index)を返す。
- 触るとき: 全タブ内の位置と、表示上の位置(elementIndex)の違いを調べるとき。

## MozTabbrowserTab.elementIndex()
- 位置: L184-191
- 役割: タブ列の表示要素の中での位置を返す。非表示のタブでは例外を投げる。
- 触るとき: ドラッグ&ドロップなどで表示上の位置を使う箇所を調べるとき。

## MozTabbrowserTab.elementIndex()
- 位置: L193-195
- 役割: 表示要素内での位置を保存する。
- 触るとき: 位置番号がどこで設定されるかを調べるとき。

## MozTabbrowserTab.owner()
- 位置: L198-204
- 役割: このタブを開いた元のタブを弱参照から返す。閉じ中なら null を返す。
- 触るとき: タブを閉じたあとに戻る先(オーナー)の判定を調べるとき。
- 呼び出し先: `this.#owner?.deref()`

## MozTabbrowserTab.owner()
- 位置: L206-208
- 役割: 元のタブを弱参照として保存する。
- 触るとき: オーナーの設定箇所を調べるとき。

## MozTabbrowserTab.container()
- 位置: L210-212
- 役割: タブを収める gBrowser.tabContainer を返す。
- 触るとき: タブからタブ列へ参照する経路を調べるとき。

## MozTabbrowserTab.attention()
- 位置: L214-221
- 役割: attention 属性を切り替え、変更を gBrowser に通知する。
- 触るとき: タブの注意表示の付け外しを調べるとき。
- 呼び出し先: `gBrowser._tabAttrModified()`, `this.hasAttribute()`, `this.toggleAttribute()`

## MozTabbrowserTab._visuallySelected()
- 位置: L223-230
- 役割: visuallyselected 属性を切り替え、変更を通知する。
- 触るとき: 見た目上の選択状態の更新を調べるとき。
- 呼び出し先: `gBrowser._tabAttrModified()`, `this.hasAttribute()`, `this.toggleAttribute()`

## MozTabbrowserTab._selected()
- 位置: L232-243
- 役割: selected 属性を切り替え、非マルチプロセス時は見た目の選択も同時に更新する。
- 触るとき: タブ選択と描画完了のタイミングのずれを調べるとき。
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTab.pinned()
- 位置: L245-247
- 役割: pinned 属性があるか(固定タブか)を返す。
- 触るとき: 固定タブの判定を参照するとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.isOpen()
- 位置: L249-251
- 役割: 接続済みで閉じ中でなく、Firefox View のタブでもないかを返す。
- 触るとき: 開いているタブの定義を調べるとき。

## MozTabbrowserTab.visible()
- 位置: L253-259
- 役割: 開いていて、隠れておらず、グループ内でも見えている状態かを返す。
- 触るとき: タブが見えると判定される条件を調べるとき。
- 呼び出し先: `this.group.isTabVisibleInGroup()`

## MozTabbrowserTab.hidden()
- 位置: L261-264
- 役割: 親クラスの hidden を返す。設定側は定義せず読み取り専用にしている。
- 触るとき: hidden を直接書き換えられない理由を調べるとき。

## MozTabbrowserTab.muted()
- 位置: L266-268
- 役割: muted 属性があるか(ミュート中か)を返す。
- 触るとき: ミュート状態の判定を参照するとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.multiselected()
- 位置: L270-272
- 役割: multiselected 属性があるか(複数選択中か)を返す。
- 触るとき: 複数選択状態の判定を参照するとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.userContextId()
- 位置: L274-278
- 役割: usercontextid 属性を数値で返す。なければ 0 を返す。
- 触るとき: コンテナタブの ID 取得を調べるとき。
- 呼び出し先: `parseInt()`, `this.getAttribute()`, `this.hasAttribute()`

## MozTabbrowserTab.permanentKey()
- 位置: L286-288
- 役割: リンクされたブラウザーの permanentKey を返す。閉じた後は undefined。
- 触るとき: タブを永続的に識別するキーの取得元を調べるとき。

## MozTabbrowserTab.soundPlaying()
- 位置: L290-292
- 役割: soundplaying 属性があるか(音が鳴っているか)を返す。
- 触るとき: 音再生状態の判定を参照するとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.pictureinpicture()
- 位置: L294-296
- 役割: pictureinpicture 属性があるか(PiP 中か)を返す。
- 触るとき: PiP 状態の判定を参照するとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.activeMediaBlocked()
- 位置: L298-300
- 役割: activemedia-blocked 属性があるか(メディア再生がブロック中か)を返す。
- 触るとき: 自動再生ブロック状態の判定を参照するとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.undiscardable()
- 位置: L302-304
- 役割: undiscardable 属性があるか(破棄不可か)を返す。
- 触るとき: タブの破棄対象から外す条件を調べるとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.undiscardable()
- 位置: L306-313
- 役割: undiscardable 属性を切り替え、変更を通知する。
- 触るとき: 破棄不可の設定箇所を調べるとき。
- 呼び出し先: `gBrowser._tabAttrModified()`, `this.hasAttribute()`, `this.toggleAttribute()`

## MozTabbrowserTab.animationsEnabled()
- 位置: L315-317
- 役割: スタイルの transition が空か(アニメーション有効か)を返す。
- 触るとき: タブ幅ロック中などにアニメーションを止める仕組みを調べるとき。

## MozTabbrowserTab.animationsEnabled()
- 位置: L319-321
- 役割: transition を none にするか空に戻すかでアニメーションの有効/無効を切り替える。
- 触るとき: タブのアニメーションを一時的に止める処理を調べるとき。

## MozTabbrowserTab.isEmpty()
- 位置: L323-331
- 役割: 読み込み中でなければ、空タブ(空白ページで履歴なし)かどうかを返す。
- 触るとき: タブを閉じてよい空タブとみなす条件を調べるとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.isEmptyIgnoringLoad()
- 位置: L335-354
- 役割: 読み込み状態を無視して、空白ページかつ履歴なしでカスタマイズ中でないかを返す。
- 触るとき: 読み込みを取り除く側の呼び出しでの空タブ判定を調べるとき。
- 呼び出し先: `BrowserUIUtils.checkEmptyPageOrigin()`, `isBlankPageURL()`, `this.hasAttribute()`

## MozTabbrowserTab.lastAccessed()
- 位置: L356-358
- 役割: 最後にアクセスした時刻を返す。選択中(Infinity)なら現在時刻を返す。
- 触るとき: タブの最終アクセス時刻の扱いを調べるとき。
- 呼び出し先: `Date.now()`

## MozTabbrowserTab.lastSeenActive()
- 位置: L368-391
- 役割: ユーザーが最後に見た時刻を推定して返す。前面ウィンドウの選択タブは現在時刻、未表示なら起動時刻か最終アクセスを使う。
- 触るとき: タブの最後に見た時刻の推定ロジックを調べるとき(タブ破棄の判断など)。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (isForegroundWindow && this.selected)` → `Date.now()`

## MozTabbrowserTab._overPlayingIcon()
- 位置: L393-395
- 役割: オーバーレイアイコンにマウスが乗っているかを返す。
- 触るとき: 音アイコン上のホバー判定を調べるとき。
- 呼び出し先: `this.overlayIcon?.matches()`

## MozTabbrowserTab._overAudioButton()
- 位置: L397-399
- 役割: 音声ボタンにマウスが乗っているかを返す。
- 触るとき: 音声ボタン上のホバー判定を調べるとき。
- 呼び出し先: `this.audioButton?.matches()`

## MozTabbrowserTab.overlayIcon()
- 位置: L401-403
- 役割: .tab-icon-overlay 要素を返す。
- 触るとき: オーバーレイアイコンの参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.audioButton()
- 位置: L405-407
- 役割: .tab-audio-button 要素を返す。
- 触るとき: 音声ボタンの参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.throbber()
- 位置: L409-411
- 役割: .tab-throbber 要素を返す。
- 触るとき: 読み込み中の表示要素の参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.iconImage()
- 位置: L413-415
- 役割: .tab-icon-image 要素を返す。
- 触るとき: ファビコン画像要素の参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.sharingIcon()
- 位置: L417-419
- 役割: .tab-sharing-icon-overlay 要素を返す。
- 触るとき: 共有中アイコンの参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.textLabel()
- 位置: L421-423
- 役割: .tab-label 要素を返す。
- 触るとき: タブのラベル要素の参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.closeButton()
- 位置: L425-427
- 役割: .tab-close-button 要素を返す。
- 触るとき: 閉じるボタンの参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.noteIcon()
- 位置: L429-431
- 役割: .tab-note-icon 要素を返す。
- 触るとき: メモアイコンの参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.noteIconOverlay()
- 位置: L433-435
- 役割: .tab-note-icon-overlay 要素を返す。
- 触るとき: メモアイコンのオーバーレイの参照元を調べるとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.group()
- 位置: L438-442
- 役割: タブが属する tab-group 要素を返す。なければ null。
- 触るとき: タブとグループの関係を参照するとき。
- 呼び出し先: `this.closest()`

## MozTabbrowserTab.splitview()
- 位置: L445-450
- 役割: 親が分割表示ラッパーならそれを返し、そうでなければ null を返す。
- 触るとき: タブが分割表示に入っているかの判定を調べるとき。

## MozTabbrowserTab.hasTabNote()
- 位置: L455-457
- 役割: tab-note 属性があるか(メモ付きか)を返す。
- 触るとき: タブメモの有無の判定を参照するとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.hasTabNote()
- 位置: L462-464
- 役割: tab-note 属性を切り替える。
- 触るとき: タブメモの有無を設定する箇所を調べるとき。
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTab.updateLastAccessed()
- 位置: L466-468
- 役割: 最終アクセス時刻を更新する。選択中なら Infinity を入れる。
- 触るとき: 最終アクセス時刻の更新タイミングを調べるとき。
- 呼び出し先: `Date.now()`

## MozTabbrowserTab.updateLastSeenActive()
- 位置: L470-472
- 役割: 最後に見た時刻を現在時刻にする。
- 触るとき: 最後に見た時刻の記録タイミングを調べるとき。
- 呼び出し先: `Date.now()`

## MozTabbrowserTab.updateLastUnloadedByTabUnloader()
- 位置: L474-477
- 役割: タブアンローダーによる破棄時刻を記録し、破棄回数の計測を加算する。
- 触るとき: タブ破棄の計測を調べるとき。
- 呼び出し先: `Date.now()`, `Glean.browserEngagement.tabUnloadCount.add()`

## MozTabbrowserTab.recordTimeFromUnloadToReload()
- 位置: L479-490
- 役割: 破棄から再読み込みまでの時間と再読み込み回数を計測に記録し、破棄時刻を消す。
- 触るとき: 破棄したタブの再読み込み計測を調べるとき。
- 呼び出し先: `Date.now()`, `Glean.browserEngagement.tabReloadCount.add()`, `Glean.browserEngagement.tabUnloadToReload.accumulateSingleSample()`

## MozTabbrowserTab.on_mouseover()
- 位置: L492-528
- 役割: 表示中のタブで接続の先読みを行い、メモアイコンのホバーを通知し、タブ外から入った場合は mouseenter 処理を呼ぶ。
- 触るとき: タブのホバー開始時の処理や先読みを調べるとき。
- 呼び出し先: `event.target.classList.contains()`, `gBrowser._findTabToBlurTo()`, `gBrowser.warmupTab()`, `this.contains()`
- 条件付き依存: `if (this.hasTabNote)` → `noteIcon.contains()`
- 条件付き依存: `if (this.hasTabNote)` → `noteIconOverlay.contains()`
- 条件付き依存: `if (isOverNoteIcon && !this._noteIconHover)` → `this.dispatchEvent()`
- 条件付き依存: `if (isOverNoteIcon && !this._noteIconHover)` → `noteIcon?.contains()`
- 条件付き依存: `if (!this.contains(event.relatedTarget))` → `this._mouseenter()`

## MozTabbrowserTab.on_mouseout()
- 位置: L530-553
- 役割: メモアイコンのホバー終了を通知し、タブ外へ出た場合は mouseleave 処理を呼ぶ。
- 触るとき: タブのホバー終了時の処理を調べるとき。
- 呼び出し先: `this.contains()`
- 条件付き依存: `if (this._noteIconHover)` → `noteIcon.contains()`
- 条件付き依存: `if (this._noteIconHover)` → `noteIconOverlay.contains()`
- 条件付き依存: `if (!stillOverNoteIcon)` → `this.dispatchEvent()`
- 条件付き依存: `if (!stillOverNoteIcon)` → `this.contains()`
- 条件付き依存: `if (!this.contains(event.relatedTarget))` → `this._mouseleave()`

## MozTabbrowserTab.on_dragstart()
- 位置: L555-569
- 役割: ドラッグ開始時に失敗アニメーションを抑え、閉じるボタンや共有警告表示時はドラッグを止める。
- 触るとき: タブのドラッグ開始時の動作を調べるとき。
- 条件付き依存: `if (!(event.eventPhase == Event.CAPTURING_PHASE))` → `event.target.classList?.contains()`
- 条件付き依存: `if (!(event.eventPhase == Event.CAPTURING_PHASE))` → `gSharedTabWarning.willShowSharedTabWarning()`
- 条件付き依存: `if ( event.target.classList?.contains("tab-close-button") || gSharedTabWarning.willShowSharedTabWarning(this) )` → `event.stopPropagation()`

## MozTabbrowserTab.on_mousedown()
- 位置: L571-648
- 役割: クリックによるタブ選択、Shift/Ctrl での複数選択、閉じるボタン等を除外する判定を行い、選択時は計測も記録する。
- 触るとき: タブのクリック選択や複数選択の挙動を変えるとき。
- 呼び出し先: `gSharedTabWarning.willShowSharedTabWarning()`
- 条件付き依存: `if (!(this.selected))` → `event.target.classList.contains()`
- 条件付き依存: `if (event.button == 1)` → `gBrowser.warmupTab()`
- 条件付き依存: `if (event.button == 1)` → `gBrowser._findTabToBlurTo()`
- 条件付き依存: `if (event.button == 0)` → `event.getModifierState()`
- 条件付き依存: `if (!accelKey)` → `gBrowser.clearMultiSelectedTabs()`
- 条件付き依存: `if (shiftKey)` → `gBrowser.addRangeToMultiSelectedTabs()`
- 条件付き依存: `if (this.multiselected)` → `gBrowser.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (this != gBrowser.selectedTab)` → `gBrowser.addToMultiSelectedTabs()`
- 条件付き依存: `if (!(accelKey))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!this.selected && this.multiselected)` → `gBrowser.lockClearMultiSelectionOnce()`
- 条件付き依存: `if (eventMaySelectTab)` → `super.on_mousedown()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.TabMetrics.userTriggeredContext()`
- XPCOM: `Services.prefs`

## MozTabbrowserTab.on_mouseup()
- 位置: L650-656
- 役割: 複数選択のクリア抑止を解除し、フォーカス設定を戻す。
- 触るとき: Shift 選択が壊れる問題を調べるとき。
- 呼び出し先: `gBrowser.unlockClearMultiSelection()`

## MozTabbrowserTab.on_click()
- 位置: L658-739
- 役割: Alt クリックで分割表示を作り、音声ボタン操作と閉じるボタン操作(複数選択時は一括)を処理する。
- 触るとき: タブのクリック時の挙動(閉じる、ミュート、分割表示)を変えるとき。
- 呼び出し先: `event.getModifierState()`, `event.target.classList.contains()`
- 条件付き依存: `if (event.altKey)` → `event.target.classList.contains()`
- 条件付き依存: `if (event.altKey)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !event.target.classList.contains("tab-close-button") && !event.target.classList.contains("tab-icon-overlay") && !event.target.classList.contains("tab-audio-...)` → `gBrowser.addTabSplitView()`
- 条件付き依存: `if ( gBrowser.multiSelectedTabsCount > 0 && !event.target.classList.contains("tab-close-button") && !event.target.classList.contains("tab-icon-overlay") && !even...)` → `gBrowser.clearMultiSelectedTabs()`
- 条件付き依存: `if (this.multiselected)` → `gBrowser.resumeDelayedMediaOnMultiSelectedTabs()`
- 条件付き依存: `if (!(this.multiselected))` → `this.resumeDelayedMedia()`
- 条件付き依存: `if (this.multiselected)` → `gBrowser.toggleMuteAudioOnMultiSelectedTabs()`
- 条件付き依存: `if (!(this.multiselected))` → `this.toggleMuteAudio()`
- 条件付き依存: `if (this.multiselected)` → `gBrowser.removeMultiSelectedTabs()`
- 条件付き依存: `if (this.multiselected)` → `lazy.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(this.multiselected))` → `gBrowser.removeTab()`
- 条件付き依存: `if (!(this.multiselected))` → `lazy.TabMetrics.userTriggeredContext()`
- XPCOM: `Services.prefs`

## MozTabbrowserTab.on_dblclick()
- 位置: L741-766
- 役割: 設定が有効で選択中タブをダブルクリックした場合に、そのタブを閉じる。
- 触るとき: ダブルクリックでタブを閉じる機能を調べるとき。
- 呼び出し先: `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("tab-close-button"))` → `event.stopPropagation()`
- 条件付き依存: `if ( tabContainer._closeTabByDblclick && this._selectedOnFirstMouseDown && this.selected && !event.target.classList.contains("tab-icon-overlay") )` → `gBrowser.removeTab()`
- 条件付き依存: `if ( tabContainer._closeTabByDblclick && this._selectedOnFirstMouseDown && this.selected && !event.target.classList.contains("tab-icon-overlay") )` → `lazy.TabMetrics.userTriggeredContext()`

## MozTabbrowserTab.on_animationstart()
- 位置: L768-781
- 役割: 読み込みアニメーションの開始時刻を揃えて、全タブのスロバーを同期させる。
- 触るとき: 読み込み中アイコンの動きがずれる問題を調べるとき。
- 呼び出し先: `event.animationName.startsWith()`, `event.target.getAnimations()`

## MozTabbrowserTab.on_animationend()
- 位置: L783-787
- 役割: 読み込みバーストのアニメーション終了時に bursting 属性を外す。
- 触るとき: 読み込み完了時のバースト表示を調べるとき。
- 呼び出し先: `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("tab-loading-burst"))` → `this.removeAttribute()`

## MozTabbrowserTab._mouseenter()
- 位置: L806-823
- 役割: ホバー状態にし、選択中タブの位置合わせや非選択タブのホバー通知、接続の先読み、TabHoverStart の発火を行う。
- 触るとき: タブにマウスが乗ったときの処理を変えるとき。
- 呼び出し先: `SessionStore.speculativeConnectOnTabHover()`, `this.dispatchEvent()`
- 条件付き依存: `if (this.selected)` → `this.container._handleTabSelect()`
- 条件付き依存: `if (this.linkedPanel)` → `this.linkedBrowser.unselectedTabHover()`
- 条件付き依存: `if (withoutPointerEvent)` → `this.#endHoverUnlessPointerArrives()`

## MozTabbrowserTab.#endHoverUnlessPointerArrives()
- 位置: L825-843
- 役割: ポインターが来ないままタブが動いた場合に、次のマウスイベントでホバーを終了する監視を設定する。
- 触るとき: タブ移動後にホバー状態が残る問題を調べるとき。
- 呼び出し先: `this.#stopWaitingForPointer()`, `window.addEventListener()`

## onMouseEvent()
- 位置: L827-832
- 役割: 次のマウスイベントで監視を止め、タブ上にポインターがなければ mouseleave 処理を呼ぶ。
- 触るとき: ホバー状態が残る問題を調べるとき。
- 呼び出し先: `this.#stopWaitingForPointer()`, `this.matches()`
- 条件付き依存: `if (!this.matches(":hover"))` → `this._mouseleave()`

## this.#stopWaitingForPointer()
- 位置: L834-839
- 役割: ポインター待ちのリスナーを外し、自分自身を null に戻す。
- 触るとき: ポインター待ちの解除を調べるとき。
- 呼び出し先: `window.removeEventListener()`

## MozTabbrowserTab._mouseleave()
- 位置: L845-855
- 役割: ホバーを解除し、非選択タブのホバー通知を戻して TabHoverEnd を発火する。
- 触るとき: タブからマウスが外れたときの処理を変えるとき。
- 呼び出し先: `this.#stopWaitingForPointer()`, `this.dispatchEvent()`
- 条件付き依存: `if (this.linkedPanel && !this.selected)` → `this.linkedBrowser.unselectedTabHover()`

## MozTabbrowserTab.resumeDelayedMedia()
- 位置: L857-863
- 役割: ブロックされていたメディアの再生を再開し、属性を外して通知する。
- 触るとき: ブロックされた自動再生の再開処理を調べるとき。
- 条件付き依存: `if (this.activeMediaBlocked)` → `this.removeAttribute()`
- 条件付き依存: `if (this.activeMediaBlocked)` → `this.linkedBrowser.resumeMedia()`
- 条件付き依存: `if (this.activeMediaBlocked)` → `gBrowser._tabAttrModified()`

## MozTabbrowserTab.toggleMuteAudio()
- 位置: L865-883
- 役割: タブのミュートと解除を切り替え、ミュート理由を記録して通知する。
- 触るとき: タブのミュート操作の挙動を変えるとき。
- 呼び出し先: `gBrowser._tabAttrModified()`
- 条件付き依存: `if (this.linkedPanel)` → `browser.browsingContext?.mediaController?.unmute()`
- 条件付き依存: `if (browser.audioMuted)` → `this.removeAttribute()`
- 条件付き依存: `if (this.linkedPanel)` → `browser.browsingContext?.mediaController?.mute()`
- 条件付き依存: `if (!(browser.audioMuted))` → `this.toggleAttribute()`

## MozTabbrowserTab.registerAudibleChangeHandler()
- 位置: L896-961
- 役割: メディアコントローラーの音声状態変化を監視し、soundplaying 属性の付与と、遅延付きの除去を行う。
- 触るとき: タブの音再生アイコンの表示・消去タイミングを変えるとき。
- 呼び出し先: `mediaController.addEventListener()`, `this.unregisterAudibleChangeHandler()`

## this.#audibleChangeHandler()
- 位置: L902-955
- 役割: 音が鳴り始めたら属性を付け、止まったら遅延して属性を外す。ミュート中は即時に外す。
- 触るとき: 音アイコンのちらつきや消えるまでの遅延を調べるとき。
- 条件付き依存: `if (mediaController.isAudible)` → `clearTimeout()`
- 条件付き依存: `if (mediaController.isAudible)` → `this.hasAttribute()`
- 条件付き依存: `if (this.hasAttribute("soundplaying-scheduledremoval"))` → `this.removeAttribute()`
- 条件付き依存: `if (this.hasAttribute("soundplaying-scheduledremoval"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (!this.hasAttribute("soundplaying"))` → `this.toggleAttribute()`
- 条件付き依存: `if (!this.hasAttribute("soundplaying"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (modifiedAttrs.length)` → `getComputedStyle()`
- 条件付き依存: `if (mediaController.isAudible)` → `gBrowser._tabAttrModified()`
- 条件付き依存: `if (!(mediaController.isAudible))` → `this.hasAttribute()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `Math.max()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `this.toggleAttribute()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `gBrowser._tabAttrModified()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `setTimeout()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `this.removeAttribute()`
- XPCOM: `Services.prefs`

## MozTabbrowserTab.unregisterAudibleChangeHandler()
- 位置: L963-970
- 役割: 登録済みの音声状態の監視を、登録時のコントローラーから解除する。
- 触るとき: 音声監視の解除漏れを調べるとき。
- 呼び出し先: `this.#audibleChangeController?.removeEventListener()`

## MozTabbrowserTab.setUserContextId()
- 位置: L972-986
- 役割: タブとブラウザーの usercontextid 属性を設定または削除し、コンテナのスタイルを反映する。
- 触るとき: コンテナタブの ID 設定とスタイル反映を調べるとき。
- 呼び出し先: `ContextualIdentityService.setTabStyle()`
- 条件付き依存: `if (this.linkedBrowser)` → `this.linkedBrowser.setAttribute()`
- 条件付き依存: `if (aUserContextId)` → `this.setAttribute()`
- 条件付き依存: `if (this.linkedBrowser)` → `this.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (!(aUserContextId))` → `this.removeAttribute()`

## MozTabbrowserTab.updateA11yDescription()
- 位置: L988-999
- 役割: フォーカス中のタブにだけ、ツールチップ文を使った aria-describedby の説明を付ける。
- 触るとき: タブの読み上げ用説明を変えるとき。
- 呼び出し先: `document.getElementById()`, `gBrowser.getTabTooltip()`, `gBrowser.tabContainer.querySelector()`, `this.setAttribute()`
- 条件付き依存: `if (prevDescTab)` → `prevDescTab.removeAttribute()`

## MozTabbrowserTab.on_focus()
- 位置: L1001-1003
- 役割: フォーカス時にアクセシビリティ用の説明を更新する。
- 触るとき: フォーカス時の読み上げ説明を調べるとき。
- 呼び出し先: `this.updateA11yDescription()`

## MozTabbrowserTab.on_AriaFocus()
- 位置: L1005-1007
- 役割: ARIA フォーカス時にアクセシビリティ用の説明を更新する。
- 触るとき: ARIA フォーカス時の読み上げ説明を調べるとき。
- 呼び出し先: `this.updateA11yDescription()`

## MozTabbrowserTab.on_overflow()
- 位置: L1009-1011
- 役割: ラベルがあふれたとき textoverflow 属性を付ける。
- 触るとき: 長いタイトルのフェード表示などを調べるとき。
- 呼び出し先: `event.currentTarget.toggleAttribute()`

## MozTabbrowserTab.on_underflow()
- 位置: L1013-1015
- 役割: ラベルのあふれが解消したとき textoverflow 属性を外す。
- 触るとき: 長いタイトルのフェード表示などを調べるとき。
- 呼び出し先: `event.currentTarget.removeAttribute()`

## MozTabbrowserTab.#updateOnTabGrouped()
- 位置: L1017-1031
- 役割: 新たにグループに入ったとき、グループ側へ TabGrouped を発火し aria-level を 2 にする。
- 触るとき: グループ追加時のイベントやアクセシビリティ属性を調べるとき。
- 条件付き依存: `if (this.group && this.#lastGroup != this.group)` → `this.group.dispatchEvent()`
- 条件付き依存: `if (this.group && this.#lastGroup != this.group)` → `this.setAttribute()`

## MozTabbrowserTab.#updateOnTabUngrouped()
- 位置: L1033-1054
- 役割: グループから外れたとき、元グループへ TabUngrouped を発火し、aria-level と位置属性を更新する。
- 触るとき: グループ離脱時のイベントやアクセシビリティ属性を調べるとき。
- 条件付き依存: `if (this.#lastGroup && this.#lastGroup != this.group)` → `this.#lastGroup.dispatchEvent()`
- 条件付き依存: `if (this.#lastGroup && this.#lastGroup != this.group)` → `this.setAttribute()`
- 条件付き依存: `if (this.#lastGroup && this.#lastGroup != this.group)` → `this.removeAttribute()`

## MozTabbrowserTab.#updateOnTabSplit()
- 位置: L1056-1060
- 役割: 分割表示に入ったタブの aria-level を 2 にする。
- 触るとき: 分割表示でのタブの階層属性を調べるとき。
- 条件付き依存: `if (this.splitview)` → `this.setAttribute()`

## MozTabbrowserTab.#updateOnTabUnsplit()
- 位置: L1062-1072
- 役割: 分割表示から外れたタブの aria-level を 1 に戻し、位置・個数・ラベルの属性を消す。
- 触るとき: 分割表示解除時のアクセシビリティ属性を調べるとき。
- 条件付き依存: `if (!this.splitview)` → `this.setAttribute()`
- 条件付き依存: `if (!this.splitview)` → `this.removeAttribute()`

## MozTabbrowserTab.updateSplitViewAriaLabel()
- 位置: L1081-1101
- 役割: 分割表示内の位置(左/右)に応じた aria-label を設定する。RTL では左右が逆になる。
- 触るとき: 分割表示のタブの読み上げラベルを変えるとき。
- 条件付き依存: `if (l10nId)` → `gBrowser.tabLocalization.formatValueSync()`
- 条件付き依存: `if (l10nId)` → `this.getAttribute()`
- 条件付き依存: `if (l10nId)` → `this.setAttribute()`
