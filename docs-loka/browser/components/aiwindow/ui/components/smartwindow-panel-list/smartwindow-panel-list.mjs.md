# browser/components/aiwindow/ui/components/smartwindow-panel-list/smartwindow-panel-list.mjs

source: browser/components/aiwindow/ui/components/smartwindow-panel-list/smartwindow-panel-list.mjs
source-hash: 136800921d5153b349afb2f6344b378503e1d45d
lines: 462

## <module>
- 役割: グループ化された項目を popup として出す汎用の smartwindow-panel-list を定義するモジュール。データの絞り込みは持たず、描画・選択・位置決めを担う。
- 呼び出し先: `customElements.define()`

## SmartwindowPanelList.constructor()
- 位置: L50-58
- 役割: groups・anchor・placeholder・alwaysOpen・sidebarMode・selectedItemId を既定値にして初期化する。
- 触るとき: 初期値を変えるとき、または選択も項目も無い状態で何が出るかを調べるとき。
- 呼び出し先: `super()`
- 参照: `this.alwaysOpen`, `this.anchor`, `this.groups`, `this.placeholderL10nId`, `this.selectedItemId`, `this.sidebarMode`

## SmartwindowPanelList.willUpdate()
- 位置: L60-70
- 役割: groups が変わったとき、先頭の項目を選択状態に戻す。
- 触るとき: groups 更新時の既定の選択の扱いを変えるとき。
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (changedProperties.has("groups"))` → `this.#selectableItems()`
- 参照: `first?.id`, `this.selectedItemId`

## SmartwindowPanelList.#selectableItems()
- 位置: L72-74
- 役割: 全グループの項目を1つの配列にして返す。
- 触るとき: キー操作や選択の対象となる項目の範囲を変えるとき。
- 呼び出し先: `this.groups.flatMap()`
- 参照: `group.items`

## SmartwindowPanelList.moveSelection()
- 位置: L81-90
- 役割: 選択中の項目から delta だけ前後に移し、端では反対側へ循環させる。項目が無ければ何もしない。
- 触るとき: 上下キーで項目を移動する挙動を変えるとき。
- 呼び出し先: `items.findIndex()`, `this.#selectableItems()`
- 参照: `item.id`, `items.length`, `items[next].id`, `this.selectedItemId`

## SmartwindowPanelList.getSelectedItem()
- 位置: L95-100
- 役割: 選択中の id に一致する項目を返し、無ければ null を返す。
- 触るとき: 選択された項目を確定する処理を変えるとき。
- 呼び出し先: `this.#selectableItems()`, `this.#selectableItems().find()`
- 参照: `item.id`, `this.selectedItemId`

## SmartwindowPanelList.#hasCustomItems()
- 位置: L102-109
- 役割: panel-list の子に panel-item 以外の要素があるかを判定する。
- 触るとき: 消費側が独自の項目を渡したときに既定の項目描画を止める条件を変えるとき。
- 呼び出し先: `[...itemsHost.children].some()`, `element.classList.contains()`
- 参照: `element.localName`, `itemsHost.children`, `this.#panelList`

## SmartwindowPanelList.#isCommandMode()
- 位置: L111-113
- 役割: data-triggered-by が inline-command なら true を返す。
- 触るとき: コマンドパレットとしての表示や位置決めを変えるとき。
- 呼び出し先: `this.getAttribute()`

## SmartwindowPanelList.firstUpdated()
- 位置: L115-131
- 役割: panel-list の参照を取り、開いたときに位置を合わせ直し、外から渡された子要素を取り込み、alwaysOpen なら表示する。
- 触るとき: 初回描画後の準備や、表示時の位置合わせを変えるとき。
- 呼び出し先: `this.#maybeMoveChildrenIntoPanel()`, `this.#panelList.addEventListener()`, `this.shadowRoot.querySelector()`
- 条件付き依存: `if (this.#isCommandMode)` → `this.#reposition()`
- 条件付き依存: `if (this.sidebarMode)` → `this.#clampToViewport()`
- 条件付き依存: `if (this.alwaysOpen)` → `this.show()`
- 参照: `this.#isCommandMode`, `this.#panelList`, `this.alwaysOpen`, `this.sidebarMode`

## SmartwindowPanelList.#maybeMoveChildrenIntoPanel()
- 位置: L133-139
- 役割: 消費側が子要素として渡した要素を、すべて panel-list の中へ移す。
- 触るとき: 外から渡される独自の項目の扱いを変えるとき。
- 呼び出し先: `Array.from()`, `this.#panelList.append()`
- 参照: `custom.length`, `this.children`

## SmartwindowPanelList.#clampToViewport()
- 位置: L141-159
- 役割: panel-list の left と top を、画面の幅と高さの内側に収まるように補正する。
- 触るとき: ポップアップが画面からはみ出す問題を調べるとき。
- 呼び出し先: `Math.max()`, `Math.min()`, `getComputedStyle()`, `panelEl.getBoundingClientRect()`, `parseFloat()`
- 参照: `getComputedStyle(panelEl).marginInlineStart`, `panelEl.style.left`, `panelEl.style.top`, `panelRect.height`, `panelRect.width`, `this.#panelList`, `window.innerHeight`, `window.innerWidth`

## SmartwindowPanelList.#reposition()
- 位置: L161-192
- 役割: 次のフレームで、アンカーの位置から panel の top を決める。コマンドモードではアンカーの幅と左端に合わせ、最後に画面内へ収める。
- 触るとき: ポップアップを上に出すか下に出すか、また幅をどう決めるかを変えるとき。
- 呼び出し先: `anchorElement.getBoundingClientRect()`, `panelEl.getAttribute()`, `requestAnimationFrame()`, `this.#clampToViewport()`
- 条件付き依存: `if (valign === "top")` → `Math.max()`
- 参照: `anchorRect.bottom`, `anchorRect.left`, `anchorRect.top`, `anchorRect.width`, `panelEl.scrollHeight`, `panelEl.style.left`, `panelEl.style.top`, `panelEl.style.width`, `this.#anchorElement`, `this.#isCommandMode`, `this.#panelList`, `this.#panelList?.open`, `window.scrollX`, `window.scrollY`

## SmartwindowPanelList.updated()
- 位置: L194-210
- 役割: anchor が変わったら anchor 要素を決め、開いているときに anchor か groups が変わったら再配置する。
- 触るとき: アンカーの指定方法や、内容が変わったときの再配置を変えるとき。
- 呼び出し先: `changedProperties.has()`, `super.updated()`
- 条件付き依存: `if (changedProperties.has("anchor"))` → `this.renderRoot.querySelector()`
- 条件付き依存: `if ( this.#panelList?.open && (changedProperties.has("anchor") || changedProperties.has("groups")) )` → `this.#reposition()`
- 参照: `this.#anchorElement`, `this.#panelList?.open`, `this.anchor`

## SmartwindowPanelList.show()
- 位置: async L212-215
- 役割: 描画完了を待ってから、アンカーを付けて panel-list を開く。
- 触るとき: 表示の開始タイミングや引数の渡し方を変えるとき。
- 呼び出し先: `this.#panelList.show()`
- 参照: `this.#anchorElement`, `this.updateComplete`

## SmartwindowPanelList.hide()
- 位置: async L217-220
- 役割: 描画完了を待ってから panel-list を閉じる。
- 触るとき: 閉じる処理の前後の待ちを変えるとき。
- 呼び出し先: `this.#panelList.hide()`
- 参照: `this.updateComplete`

## SmartwindowPanelList.toggle()
- 位置: async L222-225
- 役割: 描画完了を待ってから panel-list の開閉を切り替える。
- 触るとき: トグル操作の挙動を変えるとき。
- 呼び出し先: `this.#panelList.toggle()`
- 参照: `this.#anchorElement`, `this.updateComplete`

## SmartwindowPanelList.handlePanelClick()
- 位置: L227-246
- 役割: クリックされた panel-item(見出しを除く)から id・種別・ラベル・アイコン・色を取り出し、item-selected を発火する。
- 触るとき: 項目を選んだときに親へ渡す情報を変えるとき。
- 呼び出し先: `e.target.closest()`, `e.target.closest(".panel-item-container")?.querySelector()`, `panelItem.classList.contains()`
- 条件付き依存: `if (panelItem && !panelItem.classList.contains("panel-section-header"))` → `panelItem.textContent.trim()`
- 条件付き依存: `if (panelItem && !panelItem.classList.contains("panel-section-header"))` → `this.dispatchEvent()`
- 参照: `panelItem.itemColor`, `panelItem.itemIcon`, `panelItem.itemId`, `panelItem.itemLabel`, `panelItem.itemType`

## SmartwindowPanelList.handleKeyDown()
- 位置: L248-256
- 役割: キー入力を元のイベントごと panel-keydown として発火する。
- 触るとき: キー操作を親へ転送する仕組みを変えるとき。
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowPanelList.#isEmpty()
- 位置: L262-264
- 役割: groups が無い、または全グループの項目が空なら true を返す。
- 触るとき: 空の状態を表示する条件を変えるとき。
- 呼び出し先: `this.groups.every()`
- 参照: `g.items?.length`, `this.groups.length`

## SmartwindowPanelList.#renderAnchor()
- 位置: L266-282
- 役割: anchor が座標で指定されているときだけ、その位置の CSS 変数を持つ目印の span を描く。
- 触るとき: 座標でアンカーを指定する仕組みを変えるとき。
- 呼び出し先: `html()`, `styleMap()`, `this.getBoundingClientRect()`
- 参照: `rect.left`, `rect.top`, `this.anchor`, `this.anchor.height`, `this.anchor.left`, `this.anchor.top`, `this.anchor.width`

## SmartwindowPanelList.#renderEmptyState()
- 位置: L284-291
- 役割: placeholderL10nId を持つ無効化された見出し用の panel-item を描く。
- 触るとき: 項目が無いときの文言を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.placeholderL10nId`

## SmartwindowPanelList.#renderGroupHeader()
- 位置: L293-300
- 役割: headerL10nId を持つ無効化された見出しを描く。
- 触るとき: 翻訳付きのグループ見出しの表示を変えるとき。
- 呼び出し先: `html()`

## SmartwindowPanelList.#renderPlainHeader()
- 位置: L302-310
- 役割: header の文字列をそのまま入れた無効化された見出しを描く。
- 触るとき: 翻訳を使わないグループ見出しの表示を変えるとき。
- 呼び出し先: `html()`

## SmartwindowPanelList.#computeItemStyles()
- 位置: L312-320
- 役割: アイコンがあれば --panel-item-icon-url の CSS 変数を作って返す。
- 触るとき: アイコンを CSS 変数で渡す方法を変えるとき。
- 参照: `item.icon`

## SmartwindowPanelList.#renderTabGroupItem()
- 位置: L324-347
- 役割: タブグループの項目を、グループ色のアイコンと panel-item のラベルを並べた、選べる行として描く。
- 触るとき: タブグループ項目の見た目や選択状態の表示を変えるとき。
- 呼び出し先: `classMap()`, `html()`
- 参照: `item.color`, `item.id`, `item.label`, `item.type`

## SmartwindowPanelList.#renderItem()
- 位置: L349-388
- 役割: タブグループ種別なら専用の行を、それ以外は説明の有無に応じてアイコン付きの panel-item か説明文付きの行を描く。選択中の行には selected を付ける。
- 触るとき: 通常の項目の見た目、アイコン、説明文の出し方を変えるとき。
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `styleMap()`, `this.#computeItemStyles()`
- 条件付き依存: `if (item.type == CONTEXT_MENTION_TYPE.TAB_GROUP)` → `this.#renderTabGroupItem()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `item.description`, `item.descriptionL10nId`, `item.icon`, `item.id`, `item.l10nId`, `item.label`, `item.type`

## SmartwindowPanelList.#renderGroup()
- 位置: L390-414
- 役割: 項目が無いグループは何も描かず、見出しと項目群を描く。見出しは翻訳 ID を優先し、無ければ文字列を使う。
- 触るとき: グループの見出しや項目の並びの描画を変えるとき。
- 呼び出し先: `html()`, `repeat()`, `this.#renderItem()`
- 条件付き依存: `if (group.headerL10nId)` → `this.#renderGroupHeader()`
- 条件付き依存: `if (group.header)` → `this.#renderPlainHeader()`
- 参照: `group.header`, `group.headerL10nId`, `group.items`, `group.items?.length`, `item.id`, `this.#isCommandMode`, `this.selectedItemId`

## SmartwindowPanelList.#renderGroups()
- 位置: L416-422
- 役割: 全グループを index をキーにして描く。
- 触るとき: グループ数が変わったときの描画の再利用の仕方を変えるとき。
- 呼び出し先: `repeat()`, `this.#renderGroup()`
- 参照: `this.groups`

## SmartwindowPanelList.#renderContent()
- 位置: L424-430
- 役割: 消費側の独自項目があれば何も描かず、無ければ空の状態かグループ一覧を描く。
- 触るとき: 独自項目を渡す場合と既定の項目を使う場合の切り替えを変えるとき。
- 呼び出し先: `this.#isEmpty()`, `this.#renderEmptyState()`, `this.#renderGroups()`
- 参照: `this.#hasCustomItems`

## SmartwindowPanelList.#renderCommandFooter()
- 位置: L432-442
- 役割: コマンドモードで項目があり独自項目が無いときだけ「準備中」の注記行を描く。
- 触るとき: コマンドパレットの注記の表示条件を変えるとき。
- 呼び出し先: `html()`, `this.#isEmpty()`
- 参照: `this.#hasCustomItems`, `this.#isCommandMode`

## SmartwindowPanelList.render()
- 位置: L444-458
- 役割: スタイルシートを読み込み、アンカーの目印、クリックとキー入力を転送する panel-list、中身、コマンド注記を描く。
- 触るとき: パネル全体の構造や、クリック・キー入力の転送先を変えるとき。
- 呼び出し先: `html()`, `this.#renderAnchor()`, `this.#renderCommandFooter()`, `this.#renderContent()`
- 参照: `this.handleKeyDown`, `this.handlePanelClick`
