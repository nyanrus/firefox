# browser/components/tabbrowser/GroupsList.sys.mjs

source: browser/components/tabbrowser/GroupsList.sys.mjs
source-hash: a27650fd20c37af7206b4af2af8049c7eb549f1c
lines: 229

## <module>
- 役割: すべてのタブメニューのタブグループ一覧パネル GroupsPanel を定義する。

## GroupsPanel.constructor()
- 位置: L11-19
- 役割: ビューやコンテナを保持し、ViewShowing を待ち受ける。
- 触るとき: パネルの生成と初期状態を調べるとき。
- 呼び出し先: `this.view.addEventListener()`

## GroupsPanel.handleEvent()
- 位置: L21-47
- 役割: ビュー表示で一覧の構築と observer 登録を、非表示で後始末を、command でコマンド処理を行う。
- 触るとき: パネルの表示・非表示やイベントの流れを調べるとき。
- 呼び出し先: `this.#handleCommand()`
- 条件付き依存: `if (event.target == this.view)` → `this.#populate()`
- 条件付き依存: `if (event.target == this.view)` → `this.#addObservers()`
- 条件付き依存: `if (event.target == this.view)` → `this.win.addEventListener()`
- 条件付き依存: `if ((this.panelMultiView = event.target))` → `this.#cleanup()`
- 条件付き依存: `if ((this.panelMultiView = event.target))` → `this.#removeObservers()`
- 条件付き依存: `if (this.panelMultiView)` → `this.#removeObservers()`

## GroupsPanel.#addObservers()
- 位置: L49-52
- 役割: 閉じたオブジェクトの変更とタブグループ DOM 削除の通知を購読する。
- 触るとき: 一覧が自動更新される契機を調べるとき。
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## GroupsPanel.#removeObservers()
- 位置: L54-57
- 役割: #addObservers で登録した二つの通知購読を解除する。
- 触るとき: observer の解除漏れを調べるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## GroupsPanel.observe()
- 位置: L59-67
- 役割: 通知を受けて一覧を作り直す。
- 触るとき: 保存済み/開いているグループの変更が反映されないとき。
- 呼び出し先: `this.#cleanup()`, `this.#populate()`

## GroupsPanel.#handleCommand()
- 位置: L69-86
- 役割: 行ボタンの command に応じて開いているグループを選択するか保存済みグループを復元する。
- 触るとき: 行クリック時の動作を変えるとき。
- 呼び出し先: `group.documentGlobal.focus()`, `group.select()`, `this.win.SessionStore.openSavedTabGroup()`, `this.win.gBrowser.getTabGroupById()`

## GroupsPanel.#setupListeners()
- 位置: L88-91
- 役割: ビューの command とパネル非表示のリスナーを登録する。
- 触るとき: パネルのイベント登録を調べるとき。
- 呼び出し先: `this.panelMultiView.addEventListener()`, `this.view.addEventListener()`

## GroupsPanel.#cleanup()
- 位置: L93-96
- 役割: コンテナの中身を空にして command リスナーを外す。
- 触るとき: 一覧の破棄処理を調べるとき。
- 呼び出し先: `this.view.removeEventListener()`

## GroupsPanel.#populate()
- 位置: L99-155
- 役割: 開いているグループと保存済みグループから行を作り、件数上限と「すべて表示」ボタンを含めて一覧を構築する。
- 触るとき: 表示件数や並び順、見出しを変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `fragment.appendChild()`, `this.#createRow()`, `this.#setupListeners()`, `this.containerNode.replaceChildren()`, `this.doc.createDocumentFragment()`, `this.win.gBrowser.getAllTabGroups()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(this.win))` → `this.win.SessionStore.savedGroups.toSorted()`
- 条件付き依存: `if (totalItemCount && !this.#showAll)` → `this.doc.createElement()`
- 条件付き依存: `if (totalItemCount && !this.#showAll)` → `header.setAttribute()`
- 条件付き依存: `if (totalItemCount && !this.#showAll)` → `this.doc.l10n.setAttributes()`
- 条件付き依存: `if (totalItemCount && !this.#showAll)` → `fragment.appendChild()`
- 条件付き依存: `if (addShowAllButton)` → `this.doc.createXULElement()`
- 条件付き依存: `if (addShowAllButton)` → `button.setAttribute()`
- 条件付き依存: `if (addShowAllButton)` → `this.doc.l10n.setAttributes()`
- 条件付き依存: `if (addShowAllButton)` → `fragment.appendChild()`

## GroupsPanel.#createRow()
- 位置: L164-227
- 役割: グループ一つ分の行を作り、色と開閉状態に応じたボタン・コマンド・コンテキストメニューを設定する。
- 触るとき: 行の見た目や開いている/保存済みの扱いを変えるとき。
- 呼び出し先: `button.setAttribute()`, `doc.createXULElement()`, `row.appendChild()`, `row.setAttribute()`, `row.style.setProperty()`
- 条件付き依存: `if (!isOpen)` → `button.classList.add()`
- 条件付き依存: `if (!isOpen)` → `button.setAttribute()`
- 条件付き依存: `if (!(!isOpen))` → `button.setAttribute()`
- 条件付き依存: `if (group.name)` → `setName()`
- 条件付き依存: `if (!(group.name))` → `doc.l10n .formatValues([{ id: "tab-group-name-default" }]) .then()`
- 条件付き依存: `if (!(group.name))` → `doc.l10n .formatValues()`
- 条件付き依存: `if (!(group.name))` → `setName()`

## setName()
- 位置: L205-214
- 役割: 開いているグループはラベルとツールチップに、保存済みは l10n 属性にグループ名を設定する。
- 触るとき: 行に表示される名前の出し方を変えるとき。
- 条件付き依存: `if (!isOpen)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(!isOpen))` → `button.setAttribute()`
