# browser/components/aboutlogins/content/components/login-list.mjs

source: browser/components/aboutlogins/content/components/login-list.mjs
source-hash: 510d55f2e2327aeee29a805dc58b49ee564ea026
lines: 938

## <module>
- 役割: (未記入)
- 呼び出し先: `LoginListItemFactory.create()`, `customElements.define()`

## name()
- 位置: L17-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `collator.compare()`
- 参照: `a.title`, `b.title`

## "name-reverse"()
- 位置: L18-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `collator.compare()`
- 参照: `a.title`, `b.title`

## username()
- 位置: L19-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `collator.compare()`
- 参照: `a.username`, `b.username`

## "username-reverse"()
- 位置: L20-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `collator.compare()`
- 参照: `a.username`, `b.username`

## "last-used"()
- 位置: L21-21
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.timeLastUsed`, `b.timeLastUsed`

## "last-changed"()
- 位置: L22-22
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.timePasswordChanged`, `b.timePasswordChanged`

## alerts()
- 位置: L23-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `breachesByLoginGUID.has()`, `sortFnOptions.name()`, `vulnerableLoginsByLoginGUID.has()`
- 参照: `a.guid`, `b.guid`

## name()
- 位置: L49-49
- 役割: (未記入)
- 触るとき: (未記入)

## "name-reverse"()
- 位置: L50-50
- 役割: (未記入)
- 触るとき: (未記入)

## username()
- 位置: L51-51
- 役割: (未記入)
- 触るとき: (未記入)

## "username-reverse"()
- 位置: L52-52
- 役割: (未記入)
- 触るとき: (未記入)

## "last-used"()
- 位置: L53-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `headerFromDate()`
- 参照: `l.timeLastUsed`

## "last-changed"()
- 位置: L54-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `headerFromDate()`
- 参照: `l.timePasswordChanged`

## alerts()
- 位置: L55-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `breachesByLoginGUID.has()`, `vulnerableLoginsByLoginGUID.has()`
- 参照: `LoginListSectionFactory.ID_PREFIX`, `l.guid`

## headerFromDate()
- 位置: L75-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `date.getFullYear()`, `now.setHours()`
- 条件付き依存: `if (!(now - 7 * dayDuration < date))` → `now.getFullYear()`
- 条件付き依存: `if (!(now - 7 * dayDuration < date))` → `date.getFullYear()`
- 条件付き依存: `if (now.getFullYear() == date.getFullYear())` → `monthFormatter.format()`
- 条件付き依存: `if (!(now.getFullYear() == date.getFullYear()))` → `now.getFullYear()`
- 条件付き依存: `if (!(now.getFullYear() == date.getFullYear()))` → `date.getFullYear()`
- 条件付き依存: `if (now.getFullYear() - 1 == date.getFullYear())` → `yearMonthFormatter.format()`
- 参照: `LoginListSectionFactory.ID_PREFIX`

## LoginList.constructor()
- 位置: L109-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._blankLoginListItem.hidden`

## LoginList.connectedCallback()
- 位置: L114-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `loginListTemplate.content.cloneNode()`, `shadowRoot.appendChild()`, `shadowRoot.querySelector()`, `this._createLoginButton.addEventListener()`, `this._list.addEventListener()`, `this._list.appendChild()`, `this.addEventListener()`, `this.attachShadow()`, `this.handleCreateNewLogin()`, `this.render()`, `this.shadowRoot .getElementById()`, `this.shadowRoot .getElementById("login-sort") .addEventListener()`, `window.addEventListener()`
- 参照: `this._blankLoginListItem`, `this._count`, `this._createLoginButton`, `this._list`, `this._sortSelect`, `this.shadowRoot`

## LoginList.#activeDescendant()
- 位置: L153-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._list.getAttribute()`, `this.shadowRoot.getElementById()`

## LoginList.selectLoginByDomainOrGuid()
- 位置: L160-162
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._preselectLogin`

## LoginList.render()
- 位置: L164-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LoginListItemFactory.create()`, `Object.assign()`, `Object.keys()`, `document.createDocumentFragment()`, `document.documentElement.classList.toggle()`, `fragment.appendChild()`, `this.#updateVisibleLoginCount()`, `this._applyFilter()`, `this._breachesByLoginGUID.has()`, `this._list.appendChild()`, `this._loginGuidsSortedOrder.some()`, `this._sortSelect.namedItem()`, `this._vulnerableLoginsByLoginGUID.has()`, `this.classList.toggle()`, `visibleLoginGuids.has()`
- 条件付き依存: `if (guid == this._selectedGuid)` → `this._setListItemAsSelected()`
- 条件付き依存: `if (!( !!this._breachesByLoginGUID && this._breachesByLoginGUID.has(listItem.dataset.guid) ))` → `this._vulnerableLoginsByLoginGUID.has()`
- 条件付き依存: `if (currentHeader != _header)` → `this.renderSectionHeader()`
- 条件付き依存: `if (!listItem.hidden)` → `section.insertBefore()`
- 条件付き依存: `if (!activeDescendant || activeDescendant.hidden)` → `this._list.querySelector()`
- 条件付き依存: `if (visibleListItem)` → `this._list.setAttribute()`
- 条件付き依存: `if ( this._sortSelect.namedItem("alerts").hidden && ((this._breachesByLoginGUID && this._loginGuidsSortedOrder.some(loginGuid => this._breachesByLoginGUID.has(lo...)` → `this._sortSelect.namedItem()`
- 参照: `activeDescendant.hidden`, `listItem.dataset.guid`, `listItem.hidden`, `listItem.notificationIcon`, `login.guid`, `section._inUse`, `section.firstElementChild.nextElementSibling`, `section.hidden`, `this.#activeDescendant`, `this._breachesByLoginGUID`, `this._filter`, `this._loginGuidsSortedOrder`, `this._loginGuidsSortedOrder.length`, `this._logins`, `this._logins[guid].listItem`, `this._logins[guid].login`, `this._sections`, `this._sections[sectionKey]._inUse`, `this._selectedGuid`, `this._sortSelect.disabled`, `this._sortSelect.namedItem("alerts").hidden`, `this._vulnerableLoginsByLoginGUID`, `visibleListItem.id`, `visibleLoginGuids.size`

## LoginList.renderSectionHeader()
- 位置: L280-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._list.insertBefore()`
- 条件付き依存: `if (!section)` → `LoginListSectionFactory.create()`
- 参照: `section._inUse`, `section.hidden`, `this._blankLoginListItem.nextElementSibling`, `this._sections`

## LoginList.handleCreateNewLogin()
- 位置: L296-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordTelemetryEvent()`, `window.dispatchEvent()`

## LoginList.handleEvent()
- 位置: L305-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `document.dispatchEvent()`, `event.detail.hasOwnProperty()`, `event.detail.toLocaleLowerCase()`, `recordTelemetryEvent()`, `this._applyHeaders()`, `this._applySortAndScrollToTop()`, `this._handleKeyboardNavWithinList()`, `this._list.querySelector()`, `this._selectFirstVisibleLogin()`, `this.dispatchEvent()`, `this.render()`, `window.dispatchEvent()`
- 条件付き依存: `if (!(event.originalTarget.tagName === "LOGIN-LIST-ITEM"))` → `event.originalTarget.getRootNode()`
- 条件付き依存: `if (!this._loginGuidsSortedOrder.length)` → `this.classList.remove()`
- 条件付き依存: `if (!(firstVisibleListItem))` → `this.classList.remove()`
- 条件付き依存: `if (!(firstVisibleListItem))` → `window.dispatchEvent()`
- 条件付き依存: `if ( Object.keys(event.detail).length == 1 && event.detail.hasOwnProperty("guid") )` → `window.dispatchEvent()`
- 条件付き依存: `if (listItem)` → `this._setListItemAsSelected()`
- 条件付き依存: `if (!(listItem))` → `this.render()`
- 条件付き依存: `if (!event.defaultPrevented)` → `this._setListItemAsSelected()`
- 条件付き依存: `if (event.type == "keydown")` → `this.shadowRoot.activeElement.closest()`
- 条件付き依存: `if ( this.shadowRoot.activeElement && this.shadowRoot.activeElement.closest("ol") && (event.key == " " || event.key == "ArrowUp" || event.key == "ArrowDown") )` → `event.preventDefault()`
- 参照: `Object.keys(event.detail).length`, `event.defaultPrevented`, `event.detail`, `event.detail.guid`, `event.key`, `event.originalTarget`, `event.originalTarget.getRootNode().host`, `event.originalTarget.tagName`, `event.type`, `firstVisibleListItem.dataset.guid`, `listItem.dataset.guid`, `listItem.notificationIcon`, `this._blankLoginListItem`, `this._createLoginButton.disabled`, `this._filter`, `this._loginGuidsSortedOrder`, `this._loginGuidsSortedOrder.length`, `this._logins`, `this._logins[event.detail.guid].login`, `this._logins[firstVisibleListItem.dataset.guid].login`, `this._logins[this._loginGuidsSortedOrder[0]].login`, `this._selectedGuid`, `this._sortSelect.value`, `this.shadowRoot.activeElement`

## LoginList.setLogins()
- 位置: L461-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `logins.reduce()`, `this._applyHeaders()`, `this._applySort()`, `this._list.appendChild()`, `this._loginGuidsSortedOrder.push()`, `this.render()`
- 条件付き依存: `if (!this._selectedGuid || !this._logins[this._selectedGuid])` → `this._selectFirstVisibleLogin()`
- 参照: `login.guid`, `this._blankLoginListItem`, `this._list.textContent`, `this._loginGuidsSortedOrder`, `this._logins`, `this._sections`, `this._selectedGuid`

## LoginList.setBreaches()
- 位置: L484-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalSetMonitorData()`

## LoginList.updateBreaches()
- 位置: L493-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginList.setVulnerableLogins()
- 位置: L500-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalSetMonitorData()`

## LoginList.updateVulnerableLogins()
- 位置: L507-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginList.setChangePasswordURLs()
- 位置: L514-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginList.updateChangePasswordURLs()
- 位置: L521-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalSetMonitorData()`

## LoginList._internalSetMonitorData()
- 位置: L528-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.render()`
- 条件付き依存: `if (this._logins[loginGuid])` → `LoginListItemFactory.update()`
- 条件付き依存: `if (updateSortAndSelectedLogin)` → `this._sortSelect.namedItem()`
- 条件付き依存: `if (updateSortAndSelectedLogin)` → `this._applyHeaders()`
- 条件付き依存: `if (updateSortAndSelectedLogin)` → `this._applySortAndScrollToTop()`
- 条件付き依存: `if (updateSortAndSelectedLogin)` → `this._selectFirstVisibleLogin()`
- 参照: `alertsSortOptionElement.hidden`, `alertsSortOptionElement.index`, `this._logins`, `this._sortSelect.selectedIndex`, `this[internalMemberName].size`

## LoginList._internalUpdateMonitorData()
- 位置: L553-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalSetMonitorData()`
- 条件付き依存: `if (data)` → `this[internalMemberName].set()`
- 条件付き依存: `if (!(data))` → `this[internalMemberName].delete()`

## LoginList.setSortDirection()
- 位置: L571-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._applyHeaders()`, `this._applySortAndScrollToTop()`, `this._selectFirstVisibleLogin()`, `this._sortSelect.namedItem()`
- 参照: `this._sortSelect.namedItem("alerts").hidden`, `this._sortSelect.value`

## LoginList.loginAdded()
- 位置: L589-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._applyHeaders()`, `this._applySort()`, `this._loginGuidsSortedOrder.push()`, `this.classList.contains()`, `this.render()`
- 条件付き依存: `if ( this.classList.contains("no-logins") && !this.classList.contains("create-login-selected") )` → `this._selectFirstVisibleLogin()`
- 参照: `login.guid`, `this._logins`

## LoginList.loginModified()
- 位置: L611-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LoginListItemFactory.update()`, `Object.assign()`, `this._applyHeaders()`, `this._applySort()`, `this.render()`
- 参照: `login.guid`, `loginObject.listItem`, `this._logins`

## LoginList.loginRemoved()
- 位置: L632-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._loginGuidsSortedOrder.filter()`, `this._logins[login.guid].listItem.remove()`, `this.render()`
- 条件付き依存: `if (this._selectedGuid == login.guid)` → `this._list.querySelectorAll()`
- 条件付き依存: `if (visibleListItems.length > 1)` → `[...visibleListItems].findIndex()`
- 条件付き依存: `if (visibleListItems.length > 1)` → `window.dispatchEvent()`
- 参照: `listItem.dataset.guid`, `login.guid`, `this._loginGuidsSortedOrder`, `this._logins`, `this._logins[visibleListItems[newlySelectedIndex].dataset.guid].login`, `this._selectedGuid`, `visibleListItems.length`, `visibleListItems[newlySelectedIndex].dataset.guid`

## LoginList._applyFilter()
- 位置: L670-690
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._filter)` → `this._loginGuidsSortedOrder.filter()`
- 条件付き依存: `if (this._filter)` → `login.origin.toLocaleLowerCase().includes()`
- 条件付き依存: `if (this._filter)` → `login.origin.toLocaleLowerCase()`
- 条件付き依存: `if (this._filter)` → `login.httpRealm.toLocaleLowerCase().includes()`
- 条件付き依存: `if (this._filter)` → `login.httpRealm.toLocaleLowerCase()`
- 条件付き依存: `if (this._filter)` → `login.username.toLocaleLowerCase().includes()`
- 条件付き依存: `if (this._filter)` → `login.username.toLocaleLowerCase()`
- 条件付き依存: `if (this._filter)` → `login.password.toLocaleLowerCase().includes()`
- 条件付き依存: `if (this._filter)` → `login.password.toLocaleLowerCase()`
- 参照: `login.httpRealm`, `this._filter`, `this._loginGuidsSortedOrder`, `this._logins`

## LoginList._applySort()
- 位置: L692-704
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sortFnOptions[sort]()`, `this._loginGuidsSortedOrder.sort()`
- 参照: `this._breachesByLoginGUID`, `this._loginGuidsSortedOrder`, `this._logins`, `this._logins[a].login`, `this._logins[b].login`, `this._sortSelect.value`, `this._vulnerableLoginsByLoginGUID`

## LoginList._applyHeaders()
- 位置: L706-718
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (updateAll || !login._header)` → `headerFn()`
- 参照: `login._header`, `login.login`, `this._breachesByLoginGUID`, `this._loginGuidsSortedOrder`, `this._logins`, `this._sortSelect.value`, `this._vulnerableLoginsByLoginGUID`

## LoginList._applySortAndScrollToTop()
- 位置: L720-724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._applySort()`, `this.render()`
- 参照: `this._list.scrollTop`

## LoginList.#updateVisibleLoginCount()
- 位置: L726-735
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.getAttributes()`
- 条件付き依存: `if (count != args.count || total != args.total)` → `document.l10n.setAttributes()`
- 参照: `args.count`, `args.total`, `document.l10n.getAttributes(this._count).args`, `this._count`

## LoginList.#findPreviousItem()
- 位置: L737-752
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `previousItem.hidden`, `previousItem.lastElementChild`, `previousItem.parentElement.previousElementSibling`, `previousItem.parentElement.tagName`, `previousItem.previousElementSibling`, `previousItem.tagName`

## LoginList.#findNextItem()
- 位置: L754-768
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `nextItem.firstElementChild.nextElementSibling`, `nextItem.hidden`, `nextItem.nextElementSibling`, `nextItem.parentElement.nextElementSibling`, `nextItem.parentElement.tagName`, `nextItem.tagName`

## LoginList.#pickByDirection()
- 位置: L770-772
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `document.dir`

## LoginList.#activeDescendantForSelection()
- 位置: L775-787
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !activeDescendant || activeDescendant.hidden || activeDescendant.tagName !== "LOGIN-LIST-ITEM" )` → `this._list.querySelector()`
- 参照: `activeDescendant.hidden`, `activeDescendant.tagName`, `this.#activeDescendant`, `this._list.firstElementChild`

## LoginList._handleKeyboardNavWithinList()
- 位置: L789-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pickByDirection()`
- 条件付き依存: `if (command)` → `event.preventDefault()`
- 条件付き依存: `if (command)` → `this.clickSelected()`
- 条件付き依存: `if (command)` → `this.selectNext()`
- 条件付き依存: `if (command)` → `this.selectPrevious()`
- 参照: `event.key`, `event.type`, `this._list`, `this.shadowRoot.activeElement`

## LoginList.clickSelected()
- 位置: L840-842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#activeDescendantForSelection?.click()`

## LoginList.selectNext()
- 位置: L844-852
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (activeDescendant)` → `this.#moveSelection()`
- 条件付き依存: `if (activeDescendant)` → `this.#findNextItem()`
- 参照: `this.#activeDescendantForSelection`

## LoginList.selectPrevious()
- 位置: L854-862
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (activeDescendant)` → `this.#moveSelection()`
- 条件付き依存: `if (activeDescendant)` → `this.#findPreviousItem()`
- 参照: `this.#activeDescendantForSelection`

## LoginList.#moveSelection()
- 位置: L864-872
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (to)` → `this._list.setAttribute()`
- 条件付き依存: `if (to)` → `from?.classList.remove()`
- 条件付き依存: `if (to)` → `to.classList.add()`
- 条件付き依存: `if (to)` → `to.scrollIntoView()`
- 条件付き依存: `if (to)` → `this.clickSelected()`
- 参照: `to.id`

## LoginList._selectFirstVisibleLogin()
- 位置: L879-901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[ selectedLoginGuid, ...this._loginGuidsSortedOrder, ].find()`, `this._applyFilter()`, `this._loginGuidsSortedOrder.find()`, `this.findLoginGuidFromDomain()`, `visibleLoginsGuids.has()`
- 条件付き依存: `if (selectedLogin)` → `window.dispatchEvent()`
- 条件付き依存: `if (selectedLogin)` → `this.updateSelectedLocationHash()`
- 参照: `this._loginGuidsSortedOrder`, `this._logins`, `this._logins[selectedLoginGuid]?.login`, `this._preselectLogin`

## LoginList._setListItemAsSelected()
- 位置: L903-921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listItem.classList.add()`, `listItem.scrollIntoView()`, `listItem.setAttribute()`, `this._list.querySelector()`, `this._list.setAttribute()`, `this.classList.toggle()`, `this.updateSelectedLocationHash()`
- 条件付き依存: `if (oldSelectedItem)` → `oldSelectedItem.classList.remove()`
- 条件付き依存: `if (oldSelectedItem)` → `oldSelectedItem.removeAttribute()`
- 参照: `listItem.dataset.guid`, `listItem.id`, `listItem.selected`, `oldSelectedItem.selected`, `this._blankLoginListItem.hidden`, `this._createLoginButton.disabled`, `this._selectedGuid`

## LoginList.updateSelectedLocationHash()
- 位置: L923-925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `encodeURIComponent()`
- 参照: `window.location.hash`

## LoginList.findLoginGuidFromDomain()
- 位置: L927-935
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `login.hostname`, `this._loginGuidsSortedOrder`, `this._logins`, `this._logins[guid].login`
