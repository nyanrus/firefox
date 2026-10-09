# browser/components/tabbrowser/GroupsList.sys.mjs

source: browser/components/tabbrowser/GroupsList.sys.mjs
source-hash: a27650fd20c37af7206b4af2af8049c7eb549f1c
lines: 229

## <module>
- 役割: (未記入)

## GroupsPanel.constructor()
- 位置: L11-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.view.addEventListener()`

## GroupsPanel.handleEvent()
- 位置: L21-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleCommand()`
- 条件付き依存: `if (event.target == this.view)` → `this.#populate()`
- 条件付き依存: `if (event.target == this.view)` → `this.#addObservers()`
- 条件付き依存: `if (event.target == this.view)` → `this.win.addEventListener()`
- 条件付き依存: `if ((this.panelMultiView = event.target))` → `this.#cleanup()`
- 条件付き依存: `if ((this.panelMultiView = event.target))` → `this.#removeObservers()`
- 条件付き依存: `if (this.panelMultiView)` → `this.#removeObservers()`

## GroupsPanel.#addObservers()
- 位置: L49-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## GroupsPanel.#removeObservers()
- 位置: L54-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## GroupsPanel.observe()
- 位置: L59-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cleanup()`, `this.#populate()`

## GroupsPanel.#handleCommand()
- 位置: L69-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.documentGlobal.focus()`, `group.select()`, `this.win.SessionStore.openSavedTabGroup()`, `this.win.gBrowser.getTabGroupById()`

## GroupsPanel.#setupListeners()
- 位置: L88-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelMultiView.addEventListener()`, `this.view.addEventListener()`

## GroupsPanel.#cleanup()
- 位置: L93-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.view.removeEventListener()`

## GroupsPanel.#populate()
- 位置: L99-155
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!isOpen)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(!isOpen))` → `button.setAttribute()`
