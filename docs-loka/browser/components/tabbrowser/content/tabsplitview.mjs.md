# browser/components/tabbrowser/content/tabsplitview.mjs

source: browser/components/tabbrowser/content/tabsplitview.mjs
source-hash: 525dc14c8df28cf6d9223cad8c7f7a052d1beb87
lines: 502

## <module>
- 役割: 分割ビューのタブをまとめる MozTabSplitViewWrapper と、URL バーの分割ボタンを更新する共有タスクを定義する。
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`, `document.getElementById()`

## MozTabSplitViewWrapper.hasActiveTab()
- 位置: L63-65
- 役割: hasactivetab 属性の有無で、分割ビュー内に選択中タブがあるかを返す。
- 触るとき: 分割ビューがアクティブかどうかの判定を調べるとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabSplitViewWrapper.shouldMoveAllTabsAtOnce()
- 位置: L67-69
- 役割: タブを一括で移動するかのフラグを返す。
- 触るとき: 分割ビューのタブ移動がまとめて行われるか個別かを調べるとき。
- 参照: `this.#shouldMoveAllTabsAtOnce`

## MozTabSplitViewWrapper.group()
- 位置: L74-78
- 役割: 親要素がタブグループならそれを、そうでなければ null を返す。
- 触るとき: 分割ビューが属するタブグループを参照・変更するとき。
- 呼び出し先: `Tabbrowser.isTabGroup()`
- 参照: `this.parentElement`

## MozTabSplitViewWrapper.state()
- 位置: L86-91
- 役割: 分割ビューの ID とタブ数を同期的にまとめて返す。
- 触るとき: セッション保存などで分割ビューの状態を取り出す処理を変えるとき。
- 参照: `this.splitViewId`, `this.tabs.length`

## MozTabSplitViewWrapper.hasActiveTab()
- 位置: L96-98
- 役割: hasactivetab 属性を指定値で付け外しする。
- 触るとき: アクティブ状態の属性反映が合わないとき。
- 呼び出し先: `this.toggleAttribute()`

## MozTabSplitViewWrapper.multiselected()
- 位置: L100-102
- 役割: multiselected 属性があるかを返す。
- 触るとき: 複数選択された分割ビューの扱いを調べるとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabSplitViewWrapper.constructor()
- 位置: L104-112
- 役割: 分割ビュー使用済みを示す pref を遅延取得できるよう登録する。
- 触るとき: browser.tabs.splitview.hasUsed の読み取りを調べるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`

## MozTabSplitViewWrapper.connectedCallback()
- 位置: L114-140
- 役割: DOM 接続時に TabSelect 監視・タブ変更の監視・幅の復元を設定し、初回は pref と初期化を行う。
- 触るとき: 分割ビューが DOM に追加された時の初期化や再接続の挙動を変えるとき。
- 呼び出し先: `this.#observeTabChanges()`, `this.#restorePanelWidths()`, `this.documentGlobal.addEventListener()`
- 条件付き依存: `if (this.hasActiveTab)` → `this.#activate()`
- 条件付き依存: `if (!this._hasUsedSplitView)` → `Services.prefs.setBoolPref()`
- 参照: `gBrowser.tabContainer`, `this._hasUsedSplitView`, `this._initialized`, `this.container`, `this.hasActiveTab`, `this.textContent`
- XPCOM: `Services.prefs`

## MozTabSplitViewWrapper.disconnectedCallback()
- 位置: L142-153
- 役割: DOM 切断時に監視を解除し、パネルを分割から外して幅を保存し SplitViewRemoved を通知する。
- 触るとき: 分割ビュー削除時の後始末や SplitViewRemoved の通知を調べるとき。
- 呼び出し先: `this.#deactivate()`, `this.#resetPanelWidths()`, `this.#tabChangeObserver?.disconnect()`, `this.container.dispatchEvent()`, `this.documentGlobal.removeEventListener()`

## MozTabSplitViewWrapper.#observeTabChanges()
- 位置: L155-189
- 役割: 子タブの増減を監視し、aria 属性の更新、変更イベント発火、空なら自身の削除、1枚になれば分割解除を行う。
- 触るとき: タブ数の変化に伴う分割ビューの自動解除や a11y の番号付けを調べるとき。
- 呼び出し先: `this.#tabChangeObserver.observe()`
- 条件付き依存: `if (this.tabs.length)` → `this.tabs.some()`
- 条件付き依存: `if (this.tabs.length)` → `this.tabs.forEach()`
- 条件付き依存: `if (this.tabs.length)` → `tab.setAttribute()`
- 条件付き依存: `if (this.tabs.length)` → `tab.updateSplitViewAriaLabel()`
- 条件付き依存: `if (this.tabs.length)` → `this.dispatchEvent()`
- 条件付き依存: `if (!(this.tabs.length))` → `this.remove()`
- 条件付き依存: `if (!this.#tabChangeObserver)` → `mutations.some()`
- 条件付き依存: `if ( this.tabs.length == 1 && mutations.some(mutation => mutation.removedNodes.length == 1) )` → `this.unsplitTabs()`
- 参照: `mutation.removedNodes.length`, `tab.selected`, `this.#tabChangeObserver`, `this.hasActiveTab`, `this.tabs.length`, `window.MutationObserver`

## MozTabSplitViewWrapper.splitViewId()
- 位置: L191-193
- 役割: splitViewId 属性を整数で返す。
- 触るとき: 分割ビューの識別子の取得元を調べるとき。
- 呼び出し先: `parseInt()`, `this.getAttribute()`

## MozTabSplitViewWrapper.splitViewId()
- 位置: L195-197
- 役割: splitViewId 属性を設定する。
- 触るとき: 分割ビューの ID 付与を調べるとき。
- 呼び出し先: `this.setAttribute()`

## MozTabSplitViewWrapper.tabs()
- 位置: L202-204
- 役割: 子要素のうち tab 要素だけを配列で返す。
- 触るとき: 分割ビューに属するタブの一覧の取得方法を調べるとき。
- 呼び出し先: `Array.from()`, `Array.from(this.children).filter()`, `node.matches()`
- 参照: `this.children`

## MozTabSplitViewWrapper.visible()
- 位置: L206-208
- 役割: すべてのタブが visible のときに true を返す。
- 触るとき: 分割ビューの表示可否の判定を調べるとき。
- 呼び出し先: `this.tabs.every()`
- 参照: `tab.visible`

## MozTabSplitViewWrapper.pinned()
- 位置: L210-212
- 役割: 常に false を返す(分割ビューはピン留めされない)。
- 触るとき: ピン留め判定でタブと分割ビューを同列に扱う処理を調べるとき。

## MozTabSplitViewWrapper.splitview()
- 位置: L220-222
- 役割: 常に null を返し、タブと同じ形で扱われる際の splitview 参照を満たす。
- 触るとき: タブを受け取る処理に分割ビューが渡る場合の挙動を調べるとき。

## MozTabSplitViewWrapper.panels()
- 位置: L229-238
- 役割: 分割ビューの各タブに対応する tabpanel 要素を集めて返す。
- 触るとき: 分割ビューのパネル幅やレイアウトの処理を調べるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (el)` → `panels.push()`
- 参照: `this.#tabs`

## MozTabSplitViewWrapper.#activate()
- 位置: L243-252
- 役割: 分割ビューのパネルを表示し、URL バーボタン更新と TabSplitViewActivate 通知を行う。
- 触るとき: 分割ビューが選択された際の表示切り替えを変えるとき。
- 呼び出し先: `gBrowser.showSplitViewPanels()`, `this.container.dispatchEvent()`, `updateUrlbarButton.arm()`
- 参照: `this.#tabs`

## MozTabSplitViewWrapper.#deactivate()
- 位置: L258-269
- 役割: 分割ビューのタブをパネルから外し、TabSplitViewDeactivate を通知する。
- 触るとき: 分割ビュー解除時のパネル状態のリセットを調べるとき。
- 呼び出し先: `gBrowser.tabpanels.removeTabsFromSplitview()`, `this.#tabs.filter()`, `this.container.dispatchEvent()`, `updateUrlbarButton.arm()`
- 参照: `tab.splitview`, `this.#tabs`

## MozTabSplitViewWrapper.#suspend()
- 位置: L277-288
- 役割: 非分割タブへ切り替える際に、分割属性を保ったままパネルを一時的に隠す。
- 触るとき: 分割ビュー再選択時のちらつきや再レイアウトの問題を調べるとき。
- 呼び出し先: `gBrowser.tabpanels.suspendSplitViewPanels()`, `this.#tabs.filter()`, `this.container.dispatchEvent()`, `updateUrlbarButton.arm()`
- 参照: `tab.splitview`, `this.#tabs`

## MozTabSplitViewWrapper.#resetPanelWidths()
- 位置: L294-303
- 役割: パネルの独自幅を記憶したうえで属性とスタイルから取り除く。
- 触るとき: 分割ビューのパネル幅の保存と解除を調べるとき。
- 呼び出し先: `panel.getAttribute()`
- 条件付き依存: `if (width)` → `this.#storedPanelWidths.set()`
- 条件付き依存: `if (width)` → `panel.removeAttribute()`
- 条件付き依存: `if (width)` → `panel.style.removeProperty()`
- 参照: `this.panels`

## MozTabSplitViewWrapper.#restorePanelWidths()
- 位置: L308-316
- 役割: 記憶しておいたパネル幅を属性とスタイルに戻す。
- 触るとき: 再接続時にパネル幅が復元されない問題を調べるとき。
- 呼び出し先: `this.#storedPanelWidths.get()`
- 条件付き依存: `if (width)` → `panel.setAttribute()`
- 条件付き依存: `if (width)` → `panel.style.setProperty()`
- 参照: `this.panels`

## MozTabSplitViewWrapper.resetRightPanelWidth()
- 位置: L322-327
- 役割: 右側パネルの記憶幅と独自幅を消し、残り領域を埋めさせる。
- 触るとき: 分割の仕切りのリセット操作を変えるとき。
- 呼び出し先: `panel.removeAttribute()`, `panel.style.removeProperty()`, `this.#storedPanelWidths.delete()`
- 参照: `this.panels`

## MozTabSplitViewWrapper.addTabs()
- 位置: L337-376
- 役割: タブ(別ウィンドウなら採用して)を分割ビューに追加し、アクティブなら表示し、URI 数の telemetry を記録する。
- 触るとき: 分割ビューへのタブ追加やセッション復元、置き換え時の挙動を変えるとき。
- 呼び出し先: `gBrowser.adoptTab()`, `gBrowser.moveTabToSplitView()`, `gBrowser.tabs.at()`, `isBlankPageURL()`, `this.appendChild()`
- 条件付き依存: `if (!(indexOfReplacedTab > -1 && indexOfReplacedTab < this.#tabs.length))` → `this.#tabs.push()`
- 条件付き依存: `if (this.hasActiveTab)` → `this.#activate()`
- 条件付き依存: `if (!isBlankPageURL(tabURI) && tabURI !== "about:opentabs")` → `tabs.indexOf()`
- 条件付き依存: `if (!isBlankPageURL(tabURI) && tabURI !== "about:opentabs")` → `String()`
- 条件付き依存: `if (!isBlankPageURL(tabURI) && tabURI !== "about:opentabs")` → `Glean.splitview.uriCount[label].add()`
- 参照: `Glean.splitview.uriCount`, `gBrowser.selectedTab`, `gBrowser.tabs.at(-1).index`, `tab.documentGlobal`, `tab.linkedBrowser.currentURI.spec`, `tab.pinned`, `tab.selected`, `this.#tabs`, `this.#tabs.length`, `this.documentGlobal`, `this.hasActiveTab`, `this.tabs`

## MozTabSplitViewWrapper.unsplitTabs()
- 位置: L386-420
- 役割: about:opentabs を閉じ、全タブを分割ビューの外へ移動して分割を解除し、終了 telemetry を記録する。
- 触るとき: 分割解除の動作や終了トリガーの telemetry を変えるとき。
- 呼び出し先: `aboutOpenTabs.forEach()`, `gBrowser.handleTabMove()`, `gBrowser.removeTab()`, `gBrowser.tabContainer.insertBefore()`, `this.#tabs.filter()`
- 条件付き依存: `if (telemetryTrigger)` → `Glean.splitview.end.record()`
- 参照: `gBrowser.tabContainer.verticalMode`, `tab?.linkedBrowser?.currentURI?.spec`, `this.#isClosing`, `this.#isUnsplitting`, `this.nextElementSibling`, `this.tabs`, `this.tabs.length`

## MozTabSplitViewWrapper.replaceTab()
- 位置: L425-438
- 役割: 分割ビュー内のタブを別のタブに入れ替え、再度アクティブにする。
- 触るとき: 分割ビュー内でタブを差し替える機能を調べるとき。
- 呼び出し先: `gBrowser.removeTab()`, `this.#activate()`, `this.addTabs()`, `this.tabs.indexOf()`
- 参照: `gBrowser.selectedTab`, `tabToReplace.selected`

## MozTabSplitViewWrapper.reverseTabs()
- 位置: L446-461
- 役割: 分割ビュー内の2つのタブの順序を入れ替え、表示を更新して telemetry を記録する。
- 触るとき: 左右入れ替え操作の挙動を変えるとき。
- 呼び出し先: `gBrowser.moveTabBefore()`
- 条件付き依存: `if (this.hasActiveTab)` → `gBrowser.showSplitViewPanels()`
- 条件付き依存: `if (this.hasActiveTab)` → `updateUrlbarButton.arm()`
- 条件付き依存: `if (trigger)` → `Glean.splitview.reverse.record()`
- 参照: `this.#shouldMoveAllTabsAtOnce`, `this.#tabs`, `this.hasActiveTab`

## MozTabSplitViewWrapper.close()
- 位置: L469-482
- 役割: 終了 telemetry を記録し、分割ビュー内の全タブを閉じる。
- 触るとき: 分割ビューごと閉じる処理を調べるとき。
- 呼び出し先: `gBrowser.removeTabs()`
- 条件付き依存: `if (trigger)` → `Glean.splitview.end.record()`
- 参照: `gBrowser.tabContainer.verticalMode`, `this.#isClosing`, `this.#tabs`

## MozTabSplitViewWrapper.on_TabSelect()
- 位置: L487-498
- 役割: タブ選択に応じて分割ビューのアクティブ状態を更新し、有効化または一時停止する。
- 触るとき: タブ切り替え時の分割ビューの表示・非表示を調べるとき。
- 条件付き依存: `if (this.hasActiveTab)` → `this.#activate()`
- 条件付き依存: `if (wasActive && !event.detail.previousTabInAdoptedSplitView)` → `this.#suspend()`
- 参照: `event.detail.previousTabInAdoptedSplitView`, `event.target.splitview`, `this.hasActiveTab`
