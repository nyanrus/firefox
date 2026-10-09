# browser/base/content/browser-customization.js

source: browser/base/content/browser-customization.js
source-hash: 11f9486794c1a6d0ba2e0d2bf923effa67788c81
lines: 182

## <module>
- 役割: ツールバーのカスタマイズモード開始・終了時の UI 調整と、メニューバーの自動非表示(AutoHideMenubar)を担う。

## handleEvent()
- 位置: L11-20
- 役割: customizationstarting と aftercustomization の各イベントを開始処理と終了処理に振り分ける。
- 触るとき: カスタマイズ開始・終了の通知の扱いを変えるとき。
- 呼び出し先: `this._afterCustomization()`, `this._customizationStarting()`
- 参照: `aEvent.type`

## isCustomizing()
- 位置: L22-24
- 役割: ドキュメントに customizing 属性があるかでカスタマイズ中かを返す。
- 触るとき: カスタマイズ中判定の条件を変えるとき。
- 呼び出し先: `document.documentElement.hasAttribute()`

## _customizationStarting()
- 位置: L26-40
- 役割: メニューバーを無効化し、プロファイル読み込み不可の policy を反映し、検索バーの分割線と Places ツールバーを準備する。
- 触るとき: カスタマイズ開始時に無効化する UI の範囲を変えるとき。
- 呼び出し先: `PlacesToolbarHelper.customizeStart()`, `Services.policies.isAllowed()`, `UpdateUrlbarSearchSplitterState()`, `childNode.setAttribute()`, `document.getElementById()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document.documentElement.setAttribute()`
- 参照: `menubar.children`
- XPCOM: `Services.policies`

## _afterCustomization()
- 位置: L42-62
- 役割: メニューバーを再有効化し、編集メニューやURL バーを更新して本体にフォーカスを戻す。
- 触るとき: カスタマイズ終了後の UI 再同期を変えるとき。
- 呼び出し先: `PlacesToolbarHelper.customizeDone()`, `UpdateUrlbarSearchSplitterState()`, `XULBrowserWindow.asyncUpdateUI()`, `childNode.removeAttribute()`, `document.getElementById()`, `gBrowser.selectedBrowser.focus()`, `gURLBar.setURI()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `updateEditUIVisibility()`
- 参照: `AppConstants.platform`, `menubar.children`

## _node()
- 位置: L66-69
- 役割: toolbar-menubar 要素を遅延取得してキャッシュする。
- 触るとき: メニューバー要素の取得方法を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._node`

## active()
- 位置: L74-76
- 役割: メニューバーのコンテキストメニューが開いているかを返す。
- 触るとき: コンテキストメニュー表示中に自動非表示を止める条件を変えるとき。
- 参照: `this.contextMenu`

## init()
- 位置: L78-89
- 役割: 右クリック時に、メニューバーのコンテキストメニューの開閉を監視するリスナーを張る。
- 触るとき: メニューバーのコンテキストメニューと自動非表示の連動を変えるとき。
- 呼び出し先: `AutoHideMenubar._node.addEventListener()`, `AutoHideMenubar._node.getAttribute()`, `document.getElementById()`, `event.target.closest()`, `this.contextMenu.addEventListener()`
- 参照: `this.contextMenu`

## handleEvent()
- 位置: L90-104
- 役割: コンテキストメニューの表示・非表示や mousemove に応じて、非表示へ戻すタイミングを決める。
- 触るとき: コンテキストメニュー閉じた後のメニューバーの戻り方を変えるとき。
- 呼び出し先: `AutoHideMenubar._node.removeEventListener()`, `AutoHideMenubar._setInactiveAsync()`, `this.contextMenu.removeEventListener()`
- 参照: `event.type`, `this.contextMenu`

## init()
- 位置: L107-112
- 役割: toolbarvisibilitychange を監視し、autohide 属性があれば自動非表示を有効にする。
- 触るとき: メニューバーの自動非表示の初期化を変えるとき。
- 呼び出し先: `this._node.addEventListener()`, `this._node.hasAttribute()`
- 条件付き依存: `if (this._node.hasAttribute("autohide"))` → `this._enable()`

## _updateState()
- 位置: L114-120
- 役割: autohide 属性の有無に応じて自動非表示を有効化か無効化する。
- 触るとき: ツールバー表示状態の変更に伴う自動非表示の切替を変えるとき。
- 呼び出し先: `this._node.hasAttribute()`
- 条件付き依存: `if (this._node.hasAttribute("autohide"))` → `this._enable()`
- 条件付き依存: `if (!(this._node.hasAttribute("autohide")))` → `this._disable()`

## _enable()
- 位置: L128-133
- 役割: メニューバーを inactive にし、表示切替に使うイベントの監視を始める。
- 触るとき: 自動非表示の監視対象イベントを変えるとき。
- 呼び出し先: `this._node.addEventListener()`, `this._node.setAttribute()`
- 参照: `this._events`

## _disable()
- 位置: L135-140
- 役割: メニューバーを active にし、監視していたイベントを外す。
- 触るとき: 自動非表示を解除する時の後始末を変えるとき。
- 呼び出し先: `this._node.removeEventListener()`, `this._setActive()`
- 参照: `this._events`

## handleEvent()
- 位置: L142-163
- 役割: メニューバーの表示切替イベントを受け、アクティブ化や非アクティブ化の処理に振り分ける。
- 触るとき: メニューバーの表示/非表示のトリガーを変えるとき。
- 呼び出し先: `this._setActive()`, `this._updateState()`
- 条件付き依存: `if (event.button == 2)` → `this._contextMenuListener.init()`
- 条件付き依存: `if (!this._contextMenuListener.active)` → `this._setInactiveAsync()`
- 参照: `event.button`, `event.type`, `this._contextMenuListener.active`

## _setInactiveAsync()
- 位置: L165-172
- 役割: 次のタイマーでメニューバーを inactive にする予約をする。
- 触るとき: メニューバーを隠すタイミングを変えるとき。
- 呼び出し先: `setTimeout()`, `this._node.hasAttribute()`
- 条件付き依存: `if (this._node.hasAttribute("autohide"))` → `this._node.setAttribute()`
- 参照: `this._inactiveTimeout`

## _setActive()
- 位置: L174-180
- 役割: 保留中の非表示予約を取り消し、メニューバーを active にする。
- 触るとき: メニューバーを表示状態に戻す処理を変えるとき。
- 呼び出し先: `this._node.removeAttribute()`
- 条件付き依存: `if (this._inactiveTimeout)` → `clearTimeout()`
- 参照: `this._inactiveTimeout`
