# browser/base/content/browser-pageActions.js

source: browser/base/content/browser-pageActions.js
source-hash: 00da33bc11189db17b6a2e656acb3a778531197c
lines: 1010

## <module>
- 役割: URL バーのページアクションボタンとパネルの配置・更新・実行を担う BrowserPageActions と、組み込みアクションの定義

## mainButtonNode()
- 位置: L10-13
- 役割: URL バーのページアクションのメインボタンを遅延取得する getter。
- 触るとき: メインボタンの参照元を追うとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.mainButtonNode`

## panelNode()
- 位置: L18-25
- 役割: ページアクションのパネルを、初回参照時にテンプレートから作って返す getter。
- 触るとき: パネルの生成タイミングを変えるとき。
- 条件付き依存: `if (!this._panelNode)` → `this.initializePanel()`
- 参照: `this._panelNode`, `this.panelNode`

## multiViewNode()
- 位置: L30-35
- 役割: メインパネルの panelmultiview 要素を遅延取得する getter。
- 触るとき: パネル内のサブビュー構造を調べるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.multiViewNode`

## mainViewNode()
- 位置: L40-45
- 役割: メインパネルのメインビュー要素を遅延取得する getter。
- 触るとき: メインビューの参照元を調べるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.mainViewNode`

## mainViewBodyNode()
- 位置: L50-55
- 役割: メインビュー内のボディ要素(.panel-subview-body)を遅延取得する getter。
- 触るとき: パネル内にボタンを挿入する位置を変えるとき。
- 呼び出し先: `this.mainViewNode.querySelector()`
- 参照: `this.mainViewBodyNode`

## init()
- 位置: L60-63
- 役割: 全アクションを URL バーに配置し、パネル表示時のハンドラを束縛する。
- 触るとき: ページアクションの初期化順を変えるとき。
- 呼び出し先: `this._onPanelShowing.bind()`, `this.placeAllActionsInUrlbar()`
- 参照: `this._onPanelShowing`

## _onPanelShowing()
- 位置: L65-71
- 役割: パネル表示時にパネルを初期化し、各パネル内アクションへ表示通知を送る。
- 触るとき: パネル表示時の通知内容を変えるとき。
- 呼び出し先: `PageActions.actionsInPanel()`, `action.onShowingInPanel()`, `this.initializePanel()`, `this.panelButtonNodeForActionID()`
- 参照: `action.id`

## placeLazyActionsInPanel()
- 位置: L73-79
- 役割: パネルが開かれるまで保留していたアクションを、まとめてパネルへ配置する。
- 触るとき: 遅延配置の対象や順序を変えるとき。
- 呼び出し先: `this._placeActionInPanelNow()`
- 参照: `this._actionsToLazilyPlaceInPanel`

## placeAllActionsInUrlbar()
- 位置: L88-94
- 役割: URL バーに表示されるべき全アクションを配置し、メインボタンの属性を更新する。
- 触るとき: 起動時や一括更新で URL バーの配置を変えるとき。
- 呼び出し先: `PageActions.actionsInUrlbar()`, `this._updateMainButtonAttributes()`, `this.placeActionInUrlbar()`

## initializePanel()
- 位置: L99-112
- 役割: パネルのテンプレートを初回に展開し、パネル内のアクションを配置する。
- 触るとき: パネルの初期化内容を変えるとき。
- 呼び出し先: `PageActions.actionsInPanel()`, `this.placeActionInPanel()`, `this.placeLazyActionsInPanel()`
- 条件付き依存: `if (!this._panelNode)` → `document.getElementById()`
- 条件付き依存: `if (!this._panelNode)` → `template.replaceWith()`
- 条件付き依存: `if (!this._panelNode)` → `this._panelNode.addEventListener()`
- 参照: `template.content`, `this._onPanelShowing`, `this._panelNode`

## placeAction()
- 位置: L120-124
- 役割: アクションをパネルと URL バーの両方に配置し、メインボタン属性を更新する。
- 触るとき: アクション追加・変更時の配置経路を調べるとき。
- 呼び出し先: `this._updateMainButtonAttributes()`, `this.placeActionInPanel()`, `this.placeActionInUrlbar()`

## placeActionInPanel()
- 位置: L132-151
- 役割: パネルが開いていればすぐ配置し、閉じていれば次の表示まで保留する。
- 触るとき: パネル配置の遅延条件を変えるとき。
- 条件付き依存: `if (this._panelNode && this.panelNode.state != "closed")` → `this._placeActionInPanelNow()`
- 条件付き依存: `if (!(this._panelNode && this.panelNode.state != "closed"))` → `this._actionsToLazilyPlaceInPanel.findIndex()`
- 条件付き依存: `if (!(this._panelNode && this.panelNode.state != "closed"))` → `this._actionsToLazilyPlaceInPanel.push()`
- 参照: `a.id`, `action.id`, `this._panelNode`, `this.panelNode.state`

## _placeActionInPanelNow()
- 位置: L153-159
- 役割: アクションをパネルに表示すべきか判定し、追加または削除する。
- 触るとき: パネル内の表示条件を変えるとき。
- 呼び出し先: `action.shouldShowInPanel()`
- 条件付き依存: `if (action.shouldShowInPanel(window))` → `this._addActionToPanel()`
- 条件付き依存: `if (!(action.shouldShowInPanel(window)))` → `this._removeActionFromPanel()`

## _addActionToPanel()
- 位置: L161-178
- 役割: アクションのボタンを作ってパネルの適切な位置に挿入し、セパレータを整える。
- 触るとき: パネルへのボタン挿入の動作を変えるとき。
- 呼び出し先: `action.onPlacedInPanel()`, `document.getElementById()`, `this._addOrRemoveSeparatorsInPanel()`, `this._getNextNode()`, `this._makePanelButtonNodeForAction()`, `this._maybeNotifyBeforePlacedInWindow()`, `this._updateActionDisabledInPanel()`, `this.mainViewBodyNode.insertBefore()`, `this.panelButtonNodeIDForActionID()`, `this.updateAction()`
- 参照: `action.id`, `node.id`

## _removeActionFromPanel()
- 位置: L180-200
- 役割: 保留中の指定とパネル内のボタン・サブビューを取り除き、セパレータを整える。
- 触るとき: パネルからの削除漏れを確認するとき。
- 呼び出し先: `action.getWantsSubview()`, `node.remove()`, `this._actionsToLazilyPlaceInPanel.findIndex()`, `this._addOrRemoveSeparatorsInPanel()`, `this.panelButtonNodeForActionID()`
- 条件付き依存: `if (lazyIndex >= 0)` → `this._actionsToLazilyPlaceInPanel.splice()`
- 条件付き依存: `if (action.getWantsSubview(window))` → `this._panelViewNodeIDForActionID()`
- 条件付き依存: `if (action.getWantsSubview(window))` → `document.getElementById()`
- 条件付き依存: `if (panelViewNode)` → `panelViewNode.remove()`
- 参照: `a.id`, `action.id`

## _addOrRemoveSeparatorsInPanel()
- 位置: L202-219
- 役割: 組み込みと一時のセパレータを、対象アクションがあれば追加し、無ければ削除する。
- 触るとき: セパレータの表示規則を変えるとき。
- 呼び出し先: `PageActions.actionsInPanel()`, `actions.find()`
- 条件付き依存: `if (sep)` → `this._addActionToPanel()`
- 条件付き依存: `if (!(sep))` → `this.panelButtonNodeForActionID()`
- 条件付き依存: `if (node)` → `node.remove()`
- 参照: `PageActions.ACTION_ID_BUILT_IN_SEPARATOR`, `PageActions.ACTION_ID_TRANSIENT_SEPARATOR`, `a.id`

## _updateMainButtonAttributes()
- 位置: L221-226
- 役割: アクションが複数あるときメインボタンに multiple-children を付ける。
- 触るとき: メインボタンの複数表示の判定を変えるとき。
- 呼び出し先: `this.mainButtonNode.toggleAttribute()`
- 参照: `PageActions.actions.length`

## _getNextNode()
- 位置: L239-256
- 役割: 指定アクションの後に続く、既に配置済みのボタンノードを返す。挿入位置を決めるために使う。
- 触るとき: ボタンの並び順を変えるとき。
- 呼び出し先: `PageActions.actionsInPanel()`, `PageActions.actionsInUrlbar()`, `actions.findIndex()`, `this.panelButtonNodeForActionID()`, `this.urlbarButtonNodeForActionID()`
- 参照: `a.id`, `action.id`, `actions.length`, `actions[i].id`

## _maybeNotifyBeforePlacedInWindow()
- 位置: L258-262
- 役割: まだウィンドウに配置されていなければ、配置前の通知を送る。
- 触るとき: 配置前通知の条件を変えるとき。
- 呼び出し先: `this._isActionPlacedInWindow()`
- 条件付き依存: `if (!this._isActionPlacedInWindow(action))` → `action.onBeforePlacedInWindow()`

## _isActionPlacedInWindow()
- 位置: L264-270
- 役割: アクションがパネルか URL バーのどちらかに、表示された状態で配置済みかを返す。
- 触るとき: 配置済みの判定条件を変えるとき。
- 呼び出し先: `this.panelButtonNodeForActionID()`, `this.urlbarButtonNodeForActionID()`
- 参照: `action.id`, `urlbarNode.hidden`

## _makePanelButtonNodeForAction()
- 位置: L272-291
- 役割: パネル用のボタン要素(セパレータなら toolbarseparator)を作り、コマンドで実行処理へつなぐ。
- 触るとき: パネルのボタンの見た目や動作を変えるとき。
- 呼び出し先: `buttonNode.addEventListener()`, `buttonNode.classList.add()`, `buttonNode.setAttribute()`, `document.createXULElement()`, `this.doCommandForAction()`
- 条件付き依存: `if (action.__isSeparator)` → `document.createXULElement()`
- 条件付き依存: `if (action.isBadged)` → `buttonNode.setAttribute()`
- 参照: `action.__isSeparator`, `action.id`, `action.isBadged`

## _makePanelViewNodeForAction()
- 位置: L293-302
- 役割: サブビュー用の panelview と本体の vbox を作る。
- 触るとき: サブビューの DOM 構造を変えるとき。
- 呼び出し先: `bodyNode.classList.add()`, `document.createXULElement()`, `panelViewNode.appendChild()`, `panelViewNode.classList.add()`, `this._panelViewNodeIDForActionID()`
- 参照: `action.id`, `bodyNode.id`, `panelViewNode.id`

## togglePanelForAction()
- 位置: L318-346
- 役割: アクションのパネルを開閉し、メインパネルを閉じてから表示する。
- 触るとき: アクション専用パネルの開閉の流れを変えるとき。
- 呼び出し先: `PanelMultiView.hidePopup()`, `PanelMultiView.openPopup()`, `PanelMultiView.openPopup(panelNode, anchorNode, { position: "bottomright topright", triggerEvent: event, }).catch()`, `this.panelAnchorNodeForAction()`
- 条件付き依存: `if (panelNode.state != "closed")` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (aaPanelNode)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (!(aaPanelNode))` → `this._makeActivatedActionPanelForAction()`
- 参照: `console.error`, `panelNode.state`, `this.activatedActionPanelNode`, `this.panelNode`

## _makeActivatedActionPanelForAction()
- 位置: L348-427
- 役割: アクション専用パネルを作り、サブビューや iframe の種類に応じた通知を結び付ける。
- 触るとき: アクション専用パネルの構造や通知を変えるとき。
- 呼び出し先: `PanelMultiView.removePopup()`, `action.getWantsSubview()`, `document.createXULElement()`, `document.getElementById()`, `panelNode.addEventListener()`, `panelNode.classList.add()`, `panelNode.setAttribute()`, `popupSet.appendChild()`
- 条件付き依存: `if (action.getWantsSubview(window))` → `document.createXULElement()`
- 条件付き依存: `if (action.getWantsSubview(window))` → `this._makePanelViewNodeForAction()`
- 条件付き依存: `if (action.getWantsSubview(window))` → `multiViewNode.setAttribute()`
- 条件付き依存: `if (action.getWantsSubview(window))` → `multiViewNode.appendChild()`
- 条件付き依存: `if (action.getWantsSubview(window))` → `panelNode.appendChild()`
- 条件付き依存: `if (action.wantsIframe)` → `document.createXULElement()`
- 条件付き依存: `if (action.wantsIframe)` → `iframeNode.setAttribute()`
- 条件付き依存: `if (action.wantsIframe)` → `panelNode.appendChild()`
- 条件付き依存: `if (iframeNode)` → `panelNode.addEventListener()`
- 条件付き依存: `if (iframeNode)` → `action.onIframeShowing()`
- 条件付き依存: `if (iframeNode)` → `iframeNode.focus()`
- 条件付き依存: `if (iframeNode)` → `action.onIframeHiding()`
- 条件付き依存: `if (iframeNode)` → `action.onIframeHidden()`
- 条件付き依存: `if (panelViewNode)` → `action.onSubviewPlaced()`
- 条件付き依存: `if (panelViewNode)` → `panelNode.addEventListener()`
- 条件付き依存: `if (panelViewNode)` → `action.onSubviewShowing()`
- 参照: `action.id`, `action.wantsIframe`, `panelNode.id`, `panelViewNode.id`, `this._activatedActionPanelID`

## panelAnchorNodeForAction()
- 位置: L441-465
- 役割: パネルを付けるアンカーを、上書き指定、URL バーのボタン、メインボタン、ID アイコンの順で可視なものから選ぶ。
- 触るとき: パネルの表示位置の決め方を変えるとき。
- 呼び出し先: `document.getElementById()`, `event.target.closest()`, `this.urlbarButtonNodeIDForActionID()`
- 条件付き依存: `if (node && !node.hidden)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `action.id`, `action?.anchorIDOverride`, `bounds.height`, `bounds.width`, `node.hidden`, `this.mainButtonNode`, `this.mainButtonNode.id`, `this.panelNode`

## activatedActionPanelNode()
- 位置: L467-469
- 役割: アクション専用パネルの要素を返す getter。
- 触るとき: アクション専用パネルの参照元を調べるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._activatedActionPanelID`

## _activatedActionPanelID()
- 位置: L471-473
- 役割: アクション専用パネルの固定 ID を返す。
- 触るとき: パネルの ID を変えるとき。

## placeActionInUrlbar()
- 位置: L481-524
- 役割: URL バーでのアクション表示条件を判定し、ボタンを作って挿入するか非表示・削除する。
- 触るとき: URL バーのボタンの表示条件や挿入を変えるとき。
- 呼び出し先: `action.onPlacedInUrlbar()`, `action.shouldShowInUrlbar()`, `document.getElementById()`, `this._getNextNode()`, `this.mainButtonNode.parentNode.insertBefore()`, `this.updateAction()`, `this.urlbarButtonNodeIDForActionID()`
- 条件付き依存: `if (!(action.__urlbarNodeInMarkup))` → `node.remove()`
- 条件付き依存: `if (action.__urlbarNodeInMarkup)` → `this._maybeNotifyBeforePlacedInWindow()`
- 条件付き依存: `if (action.__urlbarNodeInMarkup)` → `document.getElementById()`
- 条件付き依存: `if (!node)` → `this._maybeNotifyBeforePlacedInWindow()`
- 条件付き依存: `if (!node)` → `this._makeUrlbarButtonNode()`
- 参照: `action.__urlbarNodeInMarkup`, `action.id`, `node.hidden`, `node.id`

## _makeUrlbarButtonNode()
- 位置: L526-544
- 役割: URL バーのボタン(hbox と image)を作り、クリックとキー入力を実行処理へつなぐ。
- 触るとき: URL バーのボタンの見た目や操作を変えるとき。
- 呼び出し先: `buttonNode.addEventListener()`, `buttonNode.appendChild()`, `buttonNode.classList.add()`, `buttonNode.setAttribute()`, `document.createXULElement()`, `imageNode.classList.add()`
- 条件付き依存: `if (action.extensionID)` → `buttonNode.classList.add()`
- 参照: `action.extensionID`, `action.id`

## commandHandler()
- 位置: L534-536
- 役割: URL バーのボタンのクリックまたはキー入力を、アクションの実行処理へ渡す。
- 触るとき: URL バーのボタンの入力処理を変えるとき。
- 呼び出し先: `this.doCommandForAction()`

## removeAction()
- 位置: L552-557
- 役割: アクションのパネルと URL バーのノードを取り除き、削除通知を出してメインボタンを更新する。
- 触るとき: アクションの削除経路を調べるとき。
- 呼び出し先: `action.onRemovedFromWindow()`, `this._removeActionFromPanel()`, `this._removeActionFromUrlbar()`, `this._updateMainButtonAttributes()`

## _removeActionFromUrlbar()
- 位置: L559-564
- 役割: アクションの URL バーのボタンがあれば削除する。
- 触るとき: URL バーからの削除処理を変えるとき。
- 呼び出し先: `this.urlbarButtonNodeForActionID()`
- 条件付き依存: `if (node)` → `node.remove()`
- 参照: `action.id`

## updateAction()
- 位置: L581-602
- 役割: 指定されたプロパティ、または全プロパティについて、パネルと URL バーのノードへ反映する。
- 触るとき: アクションの属性変更を画面へ反映する経路を調べるとき。
- 呼び出し先: `this.panelButtonNodeForActionID()`, `this.urlbarButtonNodeForActionID()`
- 条件付き依存: `if (propertyName)` → `this[this._updateMethods[propertyName]]()`
- 条件付き依存: `if (!(propertyName))` → `this[this._updateMethods[name]]()`
- 参照: `action.id`, `opts.panelNode`, `opts.urlbarNode`, `opts.value`, `this._updateMethods`

## _updateActionDisabled()
- 位置: L612-634
- 役割: 無効状態を反映する。拡張機能のアクションとトランジェントなアクションはパネルへ移し、URL バーも再配置する。
- 触るとき: 無効化された拡張アクションの見せ方を変えるとき。
- 呼び出し先: `action.getDisabled()`, `this.placeActionInUrlbar()`
- 条件付き依存: `if (action.__transient || isProtonExtensionAction)` → `this.placeActionInPanel()`
- 条件付き依存: `if (!(action.__transient || isProtonExtensionAction))` → `this._updateActionDisabledInPanel()`
- 参照: `action.__transient`, `action.extensionID`

## _updateActionDisabledInPanel()
- 位置: L636-648
- 役割: パネル内のボタンに disabled 属性を付け外しする。
- 触るとき: パネルの無効表示を変えるとき。
- 呼び出し先: `action.getDisabled()`
- 条件付き依存: `if (disabled)` → `panelNode.setAttribute()`
- 条件付き依存: `if (!(disabled))` → `panelNode.removeAttribute()`

## _updateActionIconURL()
- 位置: L650-664
- 役割: アイコンのプロパティを、パネルと URL バーのノードのスタイルへ設定する。
- 触るとき: アイコンの反映方法を変えるとき。
- 呼び出し先: `Object.entries()`, `action.getIconProperties()`
- 条件付き依存: `if (panelNode)` → `panelNode.style.setProperty()`
- 条件付き依存: `if (urlbarNode)` → `urlbarNode.style.setProperty()`

## _updateActionLabeling()
- 位置: L666-683
- 役割: タイトルを、パネルのラベルと URL バーの aria-label に反映し、ツールチップ未設定なら tooltiptext も更新する。
- 触るとき: ラベルやアクセシブル名の反映を変えるとき。
- 呼び出し先: `action.getTitle()`
- 条件付き依存: `if (panelNode)` → `panelNode.setAttribute()`
- 条件付き依存: `if (urlbarNode)` → `urlbarNode.setAttribute()`
- 条件付き依存: `if (urlbarNode)` → `action.getTooltip()`
- 条件付き依存: `if (!tooltip)` → `urlbarNode.setAttribute()`

## _updateActionTooltip()
- 位置: L685-699
- 役割: ツールチップを URL バーのボタンへ反映し、無ければタイトルを使う。
- 触るとき: ツールチップの決め方を変えるとき。
- 呼び出し先: `action.getTooltip()`
- 条件付き依存: `if (!tooltip)` → `action.getTitle()`
- 条件付き依存: `if (tooltip)` → `urlbarNode.setAttribute()`

## _updateActionWantsSubview()
- 位置: L701-724
- 役割: サブビューの要否に応じて、パネルのボタンの見た目とサブビュー要素を作るか削除する。
- 触るとき: サブビューの作成・削除条件を変えるとき。
- 呼び出し先: `action.getWantsSubview()`, `document.getElementById()`, `panelNode.classList.toggle()`, `this._panelViewNodeIDForActionID()`
- 条件付き依存: `if (panelViewNode)` → `panelViewNode.remove()`
- 条件付き依存: `if (!panelViewNode)` → `this._makePanelViewNodeForAction()`
- 条件付き依存: `if (!panelViewNode)` → `this.multiViewNode.appendChild()`
- 条件付き依存: `if (!panelViewNode)` → `action.onSubviewPlaced()`
- 参照: `action.id`

## doCommandForAction()
- 位置: L726-760
- 役割: クリックやキー入力を判定し、サブビューを開くか、パネルを閉じてアクションのコマンドを実行する。
- 触るとき: アクションの実行経路を変えるとき。
- 呼び出し先: `PanelMultiView.hidePopup()`, `aaPanelNode.getAttribute()`, `action.getWantsSubview()`, `buttonNode.closest()`
- 条件付き依存: `if (event && event.type == "keypress")` → `event.stopPropagation()`
- 条件付き依存: `if ( action.getWantsSubview(window) && buttonNode && buttonNode.closest("panel") == this.panelNode )` → `this._panelViewNodeIDForActionID()`
- 条件付き依存: `if ( action.getWantsSubview(window) && buttonNode && buttonNode.closest("panel") == this.panelNode )` → `document.getElementById()`
- 条件付き依存: `if ( action.getWantsSubview(window) && buttonNode && buttonNode.closest("panel") == this.panelNode )` → `action.onSubviewShowing()`
- 条件付き依存: `if ( action.getWantsSubview(window) && buttonNode && buttonNode.closest("panel") == this.panelNode )` → `this.multiViewNode.showSubView()`
- 条件付き依存: `if (!aaPanelNode || aaPanelNode.getAttribute("actionID") != action.id)` → `action.onCommand()`
- 条件付き依存: `if (action.getWantsSubview(window) || action.wantsIframe)` → `this.togglePanelForAction()`
- 参照: `action.id`, `action.wantsIframe`, `event.button`, `event.key`, `event.type`, `this.activatedActionPanelNode`, `this.panelNode`

## actionForNode()
- 位置: L772-795
- 役割: DOM ノードや祖先をたどって対応するアクションを返す。セパレータは null とする。
- 触るとき: クリックされた要素からアクションを特定する方法を変えるとき。
- 呼び出し先: `PageActions.actionForID()`, `this._actionIDForNodeID()`
- 条件付き依存: `if (!action)` → `this._actionIDForNodeID()`
- 条件付き依存: `if (!action)` → `PageActions.actionForID()`
- 参照: `action.__isSeparator`, `n.id`, `n.localName`, `n.parentNode`, `node.id`, `node.parentNode`

## panelButtonNodeForActionID()
- 位置: L804-806
- 役割: アクション ID からパネルのボタン要素を取得する。
- 触るとき: パネルのボタンを参照する箇所を追うとき。
- 呼び出し先: `document.getElementById()`, `this.panelButtonNodeIDForActionID()`

## panelButtonNodeIDForActionID()
- 位置: L815-817
- 役割: アクション ID からパネルのボタン要素の ID を組み立てる。
- 触るとき: パネルのボタン ID の命名を変えるとき。

## urlbarButtonNodeForActionID()
- 位置: L826-830
- 役割: アクション ID から URL バーのボタン要素を取得する。
- 触るとき: URL バーのボタンを参照する箇所を追うとき。
- 呼び出し先: `document.getElementById()`, `this.urlbarButtonNodeIDForActionID()`

## urlbarButtonNodeIDForActionID()
- 位置: L839-845
- 役割: URL バーのボタン ID を返す。上書き指定があればそれを使い、無ければ既定の形式にする。
- 触るとき: URL バーのボタン ID の命名や上書きを変えるとき。
- 呼び出し先: `PageActions.actionForID()`
- 参照: `action.urlbarIDOverride`

## _panelViewNodeIDForActionID()
- 位置: L848-851
- 役割: パネルか URL バーの配置に応じたサブビュー要素の ID を組み立てる。
- 触るとき: サブビューの ID 規則を変えるとき。

## _actionIDForNodeID()
- 位置: L855-870
- 役割: ノード ID からアクション ID を取り出し、無ければ URL バーの ID 上書きを照合する。
- 触るとき: ノード ID からアクションへ戻す規則を変えるとき。
- 呼び出し先: `nodeID.match()`
- 参照: `PageActions.actions`, `action.id`, `action.urlbarIDOverride`

## mainButtonClicked()
- 位置: L878-906
- 役割: メインボタンの操作を判定し、アクション専用パネルを閉じるか、メインパネルを開閉する。
- 触るとき: メインボタンのクリックやキー操作の扱いを変えるとき。
- 呼び出し先: `event.stopPropagation()`
- 条件付き依存: `if (panelNode && panelNode.anchorNode.id == this.mainButtonNode.id)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (this.panelNode.state == "open")` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (this.panelNode.state == "closed")` → `this.showPanel()`
- 参照: `AppConstants.platform`, `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.ctrlKey`, `event.keyCode`, `event.type`, `panelNode.anchorNode.id`, `this.activatedActionPanelNode`, `this.mainButtonNode.id`, `this.panelNode`, `this.panelNode.state`

## showPanel()
- 位置: L915-921
- 役割: メインパネルを表示させ、メインボタンにアンカーして開く。
- 触るとき: メインパネルの表示方法を変えるとき。
- 呼び出し先: `PanelMultiView.openPopup()`
- 参照: `console.error`, `this.mainButtonNode`, `this.panelNode`, `this.panelNode.hidden`

## onContextMenuShowing()
- 位置: async L931-954
- 役割: 拡張のアクションなら、アドオンの情報を見て右クリックメニューの削除項目の状態を設定する。
- 触るとき: 拡張アクションの右クリックメニューを変えるとき。
- 呼び出し先: `AddonManager.getAddonByID()`, `popup.querySelector()`, `this.actionForNode()`
- 条件付き依存: `if (!action?.extensionID)` → `event.preventDefault()`
- 参照: `AddonManager.PERM_CAN_UNINSTALL`, `action?.extensionID`, `addon.permissions`, `event.target`, `popup.triggerNode`, `removeExtension.disabled`, `removeExtension.hidden`, `this._contextAction`

## openAboutAddonsForContextAction()
- 位置: L959-968
- 役割: 右クリックで選んだ拡張の詳細を、アドオン管理画面で開く。
- 触るとき: 右クリックからのアドオン画面表示を変えるとき。
- 呼び出し先: `encodeURIComponent()`, `window.BrowserAddonUI.openAddonsMgr()`
- 参照: `action.extensionID`, `this._contextAction`

## removeExtensionForContextAction()
- 位置: L973-981
- 役割: 右クリックで選んだ拡張を、アドオンの削除処理へ渡す。
- 触るとき: 右クリックからの拡張削除の経路を調べるとき。
- 呼び出し先: `BrowserAddonUI.removeAddon()`
- 参照: `action.extensionID`, `this._contextAction`

## onLocationChange()
- 位置: L988-992
- 役割: タブ切り替えや位置変更時に、全アクションへ位置変更を通知する。
- 触るとき: 位置変更時にアクションが更新される経路を変えるとき。
- 呼び出し先: `action.onLocationChange()`
- 参照: `PageActions.actions`

## onShowingInPanel()
- 位置: L999-1003
- 役割: ブックマーク項目の表示時に、ラベルが未設定ならブックマーク状態の表示を更新する。
- 触るとき: ブックマークのパネル項目の表示更新を変えるとき。
- 条件付き依存: `if (buttonNode.label == "null")` → `BookmarkingUI.updateBookmarkPageMenuItem()`
- 参照: `buttonNode.label`

## onCommand()
- 位置: L1005-1008
- 役割: ブックマークの実行時にパネルを閉じ、スターのコマンドを呼ぶ。
- 触るとき: ブックマーク操作の流れを変えるとき。
- 呼び出し先: `BookmarkingUI.onStarCommand()`, `PanelMultiView.hidePopup()`
- 参照: `BrowserPageActions.panelNode`
