# browser/base/content/browser-toolbarKeyNav.js

source: browser/base/content/browser-toolbarKeyNav.js
source-hash: fb43a8aef29c087a9d7e0e0390fa0d932319321e
lines: 463

## <module>
- 役割: ツールバーのボタンを少数の tab stop にまとめ、矢印キーと文字入力で移動できるようにするキーボード操作の仕組み。

## _isButton()
- 位置: L38-50
- 役割: keyNav="false" でない XUL toolbarbutton、HTML moz-button、role=button の要素をボタンとみなす。
- 触るとき: 矢印キーや文字キーの移動対象になる要素の種類を増やす・減らすとき。
- 呼び出し先: `aElem.getAttribute()`
- 参照: `aElem.localName`, `aElem.namespaceURI`

## _getWalker()
- 位置: L54-105
- 役割: ツールバー配下を歩く TreeWalker を作ってルートに保持する。歩くのは toolbartabstop と有効なボタンだけ。
- 触るとき: 矢印キーで飛ばされるボタンや、移動先の判定基準を変えたいとき。
- 呼び出し先: `document.createTreeWalker()`
- 参照: `NodeFilter.SHOW_ELEMENT`, `aRoot._toolbarKeyNavWalker`

## filter()
- 位置: L59-98
- 役割: TreeWalker が各要素を採用するか判定する。toolbartabstop は採用、identity-box は urlbar が invalid のとき除外、無効・非表示・幅 0 の要素を除く。
- 触るとき: 特定のボタン(例えば identity-box)が移動先に出たり消えたりする問題を調べるとき。
- 呼び出し先: `aNode.checkVisibility()`, `document.getElementById()`, `document.getElementById("urlbar").getAttribute()`, `this._isButton()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `NodeFilter.FILTER_ACCEPT`, `NodeFilter.FILTER_REJECT`, `NodeFilter.FILTER_SKIP`, `aNode.disabled`, `aNode.id`, `aNode.tagName`, `bounds.width`

## _initTabStops()
- 位置: L107-115
- 役割: ツールバー内の toolbartabstop に aria-hidden を付け、focus リスナーを登録する。
- 触るとき: tab stop 要素を新しく置くとき、ウィジェット追加時の登録処理を調べるとき。
- 呼び出し先: `aRoot.getElementsByTagName()`, `stop.addEventListener()`, `stop.setAttribute()`

## init()
- 位置: L117-133
- 役割: 有効時に kToolbars の各ツールバーへ keyNav=true を付け、tab stop 初期化と keydown/keypress リスナー登録を行い、CustomizableUI のリスナーも登録する。
- 触るとき: キーボード操作を有効にする条件や対象ツールバーを変えるとき。
- 呼び出し先: `CustomizableUI.addListener()`, `document.getElementById()`, `this._initTabStops()`, `toolbar.addEventListener()`, `toolbar.setAttribute()`
- 参照: `this._initialized`, `this.kToolbars`

## uninit()
- 位置: L135-150
- 役割: init の逆に、リスナー除去、keyNav 属性の削除、CustomizableUI リスナーの解除を行う。
- 触るとき: 無効化した後に属性やリスナーが残らないか確かめるとき。
- 呼び出し先: `CustomizableUI.removeListener()`, `document.getElementById()`, `stop.removeEventListener()`, `toolbar.getElementsByTagName()`, `toolbar.removeAttribute()`, `toolbar.removeEventListener()`
- 参照: `this._initialized`, `this.kToolbars`

## onWidgetAdded()
- 位置: L153-162
- 役割: CustomizableUI で kToolbars のエリアにウィジェットが追加されたとき、その要素の tab stop を初期化する。
- 触るとき: ツールバーのカスタマイズで追加したボタンが Tab で届かない問題を調べるとき。
- 呼び出し先: `document.getElementById()`, `this._initTabStops()`, `this.kToolbars.includes()`

## _focusButton()
- 位置: L164-182
- 役割: tabindex を持たないボタンには一時的に tabindex=-1 を付けて focus し、blur で後始末するリスナーを登録する。
- 触るとき: ボタンへのフォーカス移動の仕組みを変えるとき、フォーカス後に tabindex が残る問題を調べるとき。
- 呼び出し先: `aButton.addEventListener()`, `aButton.focus()`, `aButton.hasAttribute()`, `aButton.setAttribute()`
- 条件付き依存: `if (aButton.hasAttribute("tabindex"))` → `aButton.focus()`

## _onButtonBlur()
- 位置: L184-197
- 役割: ウィンドウ切り替えや open=true のパネル表示中は何もせず、それ以外では blur したボタンから tabindex とリスナーを外す。
- 触るとき: フォーカスを失ったボタンが Tab 順序に残る、またはパネルを閉じた後にフォーカスが戻らない問題を調べるとき。
- 呼び出し先: `aEvent.target.getAttribute()`, `aEvent.target.removeAttribute()`, `aEvent.target.removeEventListener()`
- 参照: `aEvent.target`, `document.activeElement`

## _onTabStopFocus()
- 位置: L199-263
- 役割: toolbartabstop が focus されたら移動方向を判定し、次の有効なボタンに focus する。見つからなければ commandDispatcher で前後の要素へ送る。
- 触るとき: Tab や Shift+Tab でツールバーに入る・抜ける挙動を変えるとき、折りたたまれたツールバーを飛ばす処理を調べるとき。
- 呼び出し先: `aEvent.target.closest()`, `button?.getAttribute()`, `this._focusButton()`, `this._getWalker()`, `this._isButton()`, `walker.nextNode()`
- 条件付き依存: `if (oldFocus)` → `oldFocus.compareDocumentPosition()`
- 条件付き依存: `if (oldFocus)` → `this._isButton()`
- 条件付き依存: `if (this._isFocusMovingBackward && oldFocus && this._isButton(oldFocus))` → `document.commandDispatcher.rewindFocus()`
- 条件付き依存: `if (!button || !this._isButton(button))` → `gNavToolbox.contains()`
- 条件付き依存: `if ( this._isFocusMovingBackward && (!oldFocus || !gNavToolbox.contains(oldFocus)) )` → `Array.from()`
- 条件付き依存: `if ( this._isFocusMovingBackward && (!oldFocus || !gNavToolbox.contains(oldFocus)) )` → `gNavToolbox.querySelectorAll()`
- 条件付き依存: `if ( this._isFocusMovingBackward && (!oldFocus || !gNavToolbox.contains(oldFocus)) )` → `allStops.indexOf()`
- 条件付き依存: `if ( this._isFocusMovingBackward && (!oldFocus || !gNavToolbox.contains(oldFocus)) )` → `allStops[earlierVisibleStopIndex].closest()`
- 条件付き依存: `if (this._isFocusMovingBackward)` → `document.commandDispatcher.rewindFocus()`
- 条件付き依存: `if (!(this._isFocusMovingBackward))` → `document.commandDispatcher.advanceFocus()`
- 参照: `Node.DOCUMENT_POSITION_PRECEDING`, `aEvent.relatedTarget`, `aEvent.target`, `stopToolbar.collapsed`, `this._isFocusMovingBackward`, `walker.currentNode`

## navigateButtons()
- 位置: L265-281
- 役割: 現在の要素から TreeWalker で次(または前)のボタンを探し、見つかって tab stop でなければ focus する。
- 触るとき: 矢印キーによるボタン間の移動を変えるとき。
- 呼び出し先: `this._focusButton()`, `this._getWalker()`
- 条件付き依存: `if (aPrevious)` → `walker.previousNode()`
- 条件付き依存: `if (!(aPrevious))` → `walker.nextNode()`
- 参照: `document.activeElement`, `newFocus.tagName`, `walker.currentNode`

## _onKeyDown()
- 位置: L283-322
- 役割: 1 文字のキーは文字検索に回し、それ以外では検索をクリアする。修飾キーなしの左右矢印で navigateButtons を呼ぶ。
- 触るとき: 矢印キーや文字キーの振る舞い、RTL のときの左右の扱いを変えるとき。
- 呼び出し先: `aEvent.preventDefault()`, `focus.closest()`, `this._clearSearch()`, `this._isButton()`, `this.navigateButtons()`
- 条件付き依存: `if ( aEvent.key != " " && aEvent.key.length == 1 && this._isButton(focus) && // Don't handle characters if the user is focused in a panel anchored // to the tool...)` → `this._onSearchChar()`
- 参照: `aEvent.altKey`, `aEvent.controlKey`, `aEvent.currentTarget`, `aEvent.key`, `aEvent.key.length`, `aEvent.metaKey`, `aEvent.shiftKey`, `document.activeElement`, `window.RTL_UI`

## _clearSearch()
- 位置: L324-330
- 役割: 入力中の検索文字列と、そのクリア用タイマーを消す。
- 触るとき: 文字キー検索の状態がリセットされない問題を調べるとき。
- 条件付き依存: `if (this._clearSearchTimeout)` → `clearTimeout()`
- 参照: `this._clearSearchTimeout`, `this._searchText`

## _onSearchChar()
- 位置: L332-380
- 役割: 1 秒以内に打たれた文字を連結し、現在位置の後ろから、なければ先頭から、ラベルが前方一致するボタンに focus する。
- 触るとき: 文字キーによる頭出し検索の順序やタイムアウトを変えるとき。
- 呼び出し先: `aChar.toLowerCase()`, `setTimeout()`, `this._clearSearch.bind()`, `this._doesSearchMatch()`, `this._getWalker()`, `walker.firstChild()`, `walker.nextNode()`
- 条件付き依存: `if (this._clearSearchTimeout)` → `clearTimeout()`
- 条件付き依存: `if (this._doesSearchMatch(newFocus))` → `this._focusButton()`
- 参照: `document.activeElement`, `this._clearSearchTimeout`, `this._searchText`, `this.kSearchClearTimeout`, `walker.currentNode`, `walker.root`

## _doesSearchMatch()
- 位置: L382-399
- 役割: ボタンの aria-label、label、tooltiptext のいずれかが検索文字列で始まるかを小文字で比較して判定する。
- 触るとき: 文字キー検索で対象にするラベルの種類を変えるとき。
- 呼び出し先: `aElem.getAttribute()`, `label.startsWith()`, `label.toLowerCase()`, `this._isButton()`
- 参照: `this._searchText`

## _onKeyPress()
- 位置: L401-444
- 役割: Enter か Space を受けたボタンを処理する。type=menu は open にし、moz-button は何もせず、commandを使わないボタンには PointerEvent の click を発火させる。
- 触るとき: キーボードでツールバーのボタンを押しても動かないボタンを直すとき。
- 呼び出し先: `focus.dispatchEvent()`, `focus.getAttribute()`, `focus.hasAttribute()`, `this._isButton()`
- 参照: `aEvent.altKey`, `aEvent.ctrlKey`, `aEvent.key`, `aEvent.metaKey`, `aEvent.shiftKey`, `document.activeElement`, `focus.localName`, `focus.open`, `focus.tagName`

## handleEvent()
- 位置: L446-461
- 役割: focus、keydown、keypress、blur の各イベントを対応するハンドラへ振り分ける。
- 触るとき: この仕組みで扱うイベントの種類を増やすとき。
- 呼び出し先: `this._onButtonBlur()`, `this._onKeyDown()`, `this._onKeyPress()`, `this._onTabStopFocus()`
- 参照: `aEvent.type`
