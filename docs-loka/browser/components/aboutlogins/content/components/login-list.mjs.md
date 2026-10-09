# browser/components/aboutlogins/content/components/login-list.mjs

source: browser/components/aboutlogins/content/components/login-list.mjs
source-hash: 510d55f2e2327aeee29a805dc58b49ee564ea026
lines: 938

## <module>
- 役割: about:logins のログイン一覧(login-list 要素)の並び替え、見出し分け、検索絞り込み、キーボード選択、監視データ(侵害・脆弱)の反映を担うモジュール
- 呼び出し先: `LoginListItemFactory.create()`, `customElements.define()`

## name()
- 位置: L17-17
- 役割: タイトルを照合順序(Intl.Collator)で昇順比較する並び替え関数
- 触るとき: 一覧の「名前」順の並びを変えるとき
- 呼び出し先: `collator.compare()`
- 参照: `a.title`, `b.title`

## "name-reverse"()
- 位置: L18-18
- 役割: タイトルを照合順序で降順比較する並び替え関数
- 触るとき: 「名前(逆順)」の並びを変えるとき
- 呼び出し先: `collator.compare()`
- 参照: `a.title`, `b.title`

## username()
- 位置: L19-19
- 役割: ユーザー名を照合順序で昇順比較する並び替え関数
- 触るとき: 「ユーザー名」順の並びを変えるとき
- 呼び出し先: `collator.compare()`
- 参照: `a.username`, `b.username`

## "username-reverse"()
- 位置: L20-20
- 役割: ユーザー名を照合順序で降順比較する並び替え関数
- 触るとき: 「ユーザー名(逆順)」の並びを変えるとき
- 呼び出し先: `collator.compare()`
- 参照: `a.username`, `b.username`

## "last-used"()
- 位置: L21-21
- 役割: 最終使用日時を比較する並び替え関数。真偽値を返す
- 触るとき: 「最近使った順」の並びを調べるとき。戻り値が真偽値のため、ソートの安定性に依存する点に注意
- 参照: `a.timeLastUsed`, `b.timeLastUsed`

## "last-changed"()
- 位置: L22-22
- 役割: パスワード変更日時を比較する並び替え関数。真偽値を返す
- 触るとき: 「パスワード変更順」の並びを調べるとき。戻り値が真偽値のため、ソートの結果が意図どおりか確認が要る
- 参照: `a.timePasswordChanged`, `b.timePasswordChanged`

## alerts()
- 位置: L23-39
- 役割: 侵害済み、次に脆弱なパスワードのログインを先頭に寄せ、同じ群の中は名前順で並べる
- 触るとき: 「警告順」の優先規則を変えるとき。侵害と脆弱の優先順位はここで決まる
- 呼び出し先: `breachesByLoginGUID.has()`, `sortFnOptions.name()`, `vulnerableLoginsByLoginGUID.has()`
- 参照: `a.guid`, `b.guid`

## name()
- 位置: L49-49
- 役割: 名前順のセクション見出しを空文字にする
- 触るとき: 名前順のときセクション見出しを出さない仕様を変えるとき

## "name-reverse"()
- 位置: L50-50
- 役割: 名前(逆順)のセクション見出しを空文字にする
- 触るとき: 逆順の見出し表示を変えるとき

## username()
- 位置: L51-51
- 役割: ユーザー名順のセクション見出しを空文字にする
- 触るとき: ユーザー名順の見出し表示を変えるとき

## "username-reverse"()
- 位置: L52-52
- 役割: ユーザー名(逆順)のセクション見出しを空文字にする
- 触るとき: ユーザー名(逆順)の見出し表示を変えるとき

## "last-used"()
- 位置: L53-53
- 役割: 最終使用日時からセクション見出しを決める(headerFromDate に委譲)
- 触るとき: 最近使った順の見出しの区切り方を変えるとき
- 呼び出し先: `headerFromDate()`
- 参照: `l.timeLastUsed`

## "last-changed"()
- 位置: L54-54
- 役割: パスワード変更日時からセクション見出しを決める(headerFromDate に委譲)
- 触るとき: パスワード変更順の見出しの区切り方を変えるとき
- 呼び出し先: `headerFromDate()`
- 参照: `l.timePasswordChanged`

## alerts()
- 位置: L55-72
- 役割: 侵害済みなら breach、脆弱なら vulnerable、それ以外は nothing のセクション ID を返す
- 触るとき: 警告セクションの見出しを増やしたり文言の対応を変えたりするとき
- 呼び出し先: `breachesByLoginGUID.has()`, `vulnerableLoginsByLoginGUID.has()`
- 参照: `LoginListSectionFactory.ID_PREFIX`, `l.guid`

## headerFromDate()
- 位置: L75-96
- 役割: 日時を今日、昨日、今週、同じ年の月名、前年の年月、それ以前の年の順に区切り、見出し ID か文字列を返す
- 触るとき: 日付の見出しの粒度(何日前まで区切るか)を変えるとき。今日を基準に計算する
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
- 役割: ログイン GUID の順序配列、GUID からログインと行への対応表、セクション表を初期化し、空白の新規行を隠す
- 触るとき: リストの内部状態を増やすとき。_blankLoginListItem は生成時に作られる
- 呼び出し先: `super()`
- 参照: `this._blankLoginListItem.hidden`

## LoginList.connectedCallback()
- 位置: L114-151
- 役割: テンプレートから shadow DOM を組み立て、件数、並び替え、作成ボタンの参照を取り、ウィンドウとリストのイベントを登録する
- 触るとき: リストが受けるイベント(AboutLogins 系)を追加・削除するとき
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `loginListTemplate.content.cloneNode()`, `shadowRoot.appendChild()`, `shadowRoot.querySelector()`, `this._createLoginButton.addEventListener()`, `this._list.addEventListener()`, `this._list.appendChild()`, `this.addEventListener()`, `this.attachShadow()`, `this.handleCreateNewLogin()`, `this.render()`, `this.shadowRoot .getElementById()`, `this.shadowRoot .getElementById("login-sort") .addEventListener()`, `window.addEventListener()`
- 参照: `this._blankLoginListItem`, `this._count`, `this._createLoginButton`, `this._list`, `this._sortSelect`, `this.shadowRoot`

## LoginList.#activeDescendant()
- 位置: L153-158
- 役割: リストの aria-activedescendant が指す要素を返す
- 触るとき: キーボード操作の現在位置を調べるとき
- 呼び出し先: `this._list.getAttribute()`, `this.shadowRoot.getElementById()`

## LoginList.selectLoginByDomainOrGuid()
- 位置: L160-162
- 役割: 初期選択の対象を、後で _selectFirstVisibleLogin が使う _preselectLogin に保存する
- 触るとき: URL のハッシュや外部からの指定で初期選択を変えたいとき
- 参照: `this._preselectLogin`

## LoginList.render()
- 位置: L164-278
- 役割: フィルタと並び順を適用し、未描画の行を追加し、警告アイコンと表示・非表示、セクション見出しの並びを更新する
- 触るとき: 一覧の見た目が古いまま残る、または行の並びやセクションがずれる不具合を調べるとき。一覧の再描画の中心
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
- 役割: 見出し名に対応するセクションを作る(なければ)か再利用し、一覧の先頭寄りに差し込んで使用中にする
- 触るとき: セクション見出しの生成や重複の扱いを変えるとき
- 呼び出し先: `this._list.insertBefore()`
- 条件付き依存: `if (!section)` → `LoginListSectionFactory.create()`
- 参照: `section._inUse`, `section.hidden`, `this._blankLoginListItem.nextElementSibling`, `this._sections`

## LoginList.handleCreateNewLogin()
- 位置: L296-303
- 役割: 新規作成ボタン押下で AboutLoginsShowBlankLogin を発火し、テレメトリ newNewLogin を記録する
- 触るとき: 新規作成ボタンの動作や計測を変えるとき
- 呼び出し先: `recordTelemetryEvent()`, `window.dispatchEvent()`

## LoginList.handleEvent()
- 位置: L305-456
- 役割: 一覧のクリック、並び替え変更、選択、フィルタ、キー操作などのイベントを種類ごとに振り分けて処理する
- 触るとき: 一覧のイベント処理を追加・変更するとき。クリックされた行の判定と、AboutLoginsLoginSelected の再発火による全データ解決がここにある
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
- 役割: ログイン一覧全体を差し替え、セクションと並び順を作り直して描画し、必要なら先頭のログインを選ぶ
- 触るとき: 一覧の初期読み込みや全件の入れ替え時の挙動を調べるとき
- 呼び出し先: `logins.reduce()`, `this._applyHeaders()`, `this._applySort()`, `this._list.appendChild()`, `this._loginGuidsSortedOrder.push()`, `this.render()`
- 条件付き依存: `if (!this._selectedGuid || !this._logins[this._selectedGuid])` → `this._selectFirstVisibleLogin()`
- 参照: `login.guid`, `this._blankLoginListItem`, `this._list.textContent`, `this._loginGuidsSortedOrder`, `this._logins`, `this._sections`, `this._selectedGuid`

## LoginList.setBreaches()
- 位置: L484-486
- 役割: 侵害データを置き換えて監視データを反映する
- 触るとき: 侵害情報の供給経路を変えるとき
- 呼び出し先: `this._internalSetMonitorData()`

## LoginList.updateBreaches()
- 位置: L493-498
- 役割: 侵害データを差分で更新する
- 触るとき: 侵害情報の個別更新を調べるとき
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginList.setVulnerableLogins()
- 位置: L500-505
- 役割: 脆弱なパスワードのデータを置き換えて反映する
- 触るとき: 脆弱性情報の供給経路を変えるとき
- 呼び出し先: `this._internalSetMonitorData()`

## LoginList.updateVulnerableLogins()
- 位置: L507-512
- 役割: 脆弱性データを差分で更新する
- 触るとき: 脆弱性情報の個別更新を調べるとき
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginList.setChangePasswordURLs()
- 位置: L514-519
- 役割: パスワード変更 URL のデータを、_internalUpdateMonitorData 経由で差分更新する(下記の update 版と呼び出し先が逆)
- 触るとき: 変更 URL の反映が効かない問題を調べるとき。setter と updater の呼び先が他の監視系と入れ替わっているため注意
- 呼び出し先: `this._internalUpdateMonitorData()`

## LoginList.updateChangePasswordURLs()
- 位置: L521-526
- 役割: パスワード変更 URL のデータを、_internalSetMonitorData で置き換える(上記の set 版と呼び出し先が逆)
- 触るとき: 変更 URL の差分更新の挙動を調べるとき。呼び先の入れ替えを直す場合は両方を揃えて確認する
- 呼び出し先: `this._internalSetMonitorData()`

## LoginList._internalSetMonitorData()
- 位置: L528-551
- 役割: 監視データを保存し、該当行を更新してから、必要ならアラート並びに切り替えて先頭を選び直し、最後に再描画する
- 触るとき: 侵害や脆弱性の反映で並び順や選択がどう変わるかを調べるとき。updateSortAndSelectedLogin が false のときは並びを変えない
- 呼び出し先: `this.render()`
- 条件付き依存: `if (this._logins[loginGuid])` → `LoginListItemFactory.update()`
- 条件付き依存: `if (updateSortAndSelectedLogin)` → `this._sortSelect.namedItem()`
- 条件付き依存: `if (updateSortAndSelectedLogin)` → `this._applyHeaders()`
- 条件付き依存: `if (updateSortAndSelectedLogin)` → `this._applySortAndScrollToTop()`
- 条件付き依存: `if (updateSortAndSelectedLogin)` → `this._selectFirstVisibleLogin()`
- 参照: `alertsSortOptionElement.hidden`, `alertsSortOptionElement.index`, `this._logins`, `this._sortSelect.selectedIndex`, `this[internalMemberName].size`

## LoginList._internalUpdateMonitorData()
- 位置: L553-569
- 役割: マップの各項目を追加(データあり)か削除(null)し、並び順の更新なしで _internalSetMonitorData に渡す
- 触るとき: 監視データの差分更新で、削除扱いが効かない原因を調べるとき
- 呼び出し先: `this._internalSetMonitorData()`
- 条件付き依存: `if (data)` → `this[internalMemberName].set()`
- 条件付き依存: `if (!(data))` → `this[internalMemberName].delete()`

## LoginList.setSortDirection()
- 位置: L571-584
- 役割: 並び替えの値を設定し、見出し、並び、先頭選択を更新する。警告順は警告がないときは無視する
- 触るとき: 保存された並び順を復元する処理を変えるとき
- 呼び出し先: `this._applyHeaders()`, `this._applySortAndScrollToTop()`, `this._selectFirstVisibleLogin()`, `this._sortSelect.namedItem()`
- 参照: `this._sortSelect.namedItem("alerts").hidden`, `this._sortSelect.value`

## LoginList.loginAdded()
- 位置: L589-605
- 役割: 新しいログインを追加して見出しと並びを更新し、一覧が空のときは先頭を選ぶ
- 触るとき: ログイン追加直後の一覧の見え方や選択を変えるとき
- 呼び出し先: `this._applyHeaders()`, `this._applySort()`, `this._loginGuidsSortedOrder.push()`, `this.classList.contains()`, `this.render()`
- 条件付き依存: `if ( this.classList.contains("no-logins") && !this.classList.contains("create-login-selected") )` → `this._selectFirstVisibleLogin()`
- 参照: `login.guid`, `this._logins`

## LoginList.loginModified()
- 位置: L611-624
- 役割: ログインを更新し、見出しをリセットして並びと行の内容を作り直す
- 触るとき: 編集後に行の位置やセクションが変わる挙動を調べるとき
- 呼び出し先: `LoginListItemFactory.update()`, `Object.assign()`, `this._applyHeaders()`, `this._applySort()`, `this.render()`
- 参照: `login.guid`, `loginObject.listItem`, `this._logins`

## LoginList.loginRemoved()
- 位置: L632-665
- 役割: 削除したログインが選択中なら前の可視行(なければ次の行)を選び直し、行とデータを消して再描画する
- 触るとき: 削除後に選ぶ行の決め方を変えるとき
- 呼び出し先: `this._loginGuidsSortedOrder.filter()`, `this._logins[login.guid].listItem.remove()`, `this.render()`
- 条件付き依存: `if (this._selectedGuid == login.guid)` → `this._list.querySelectorAll()`
- 条件付き依存: `if (visibleListItems.length > 1)` → `[...visibleListItems].findIndex()`
- 条件付き依存: `if (visibleListItems.length > 1)` → `window.dispatchEvent()`
- 参照: `listItem.dataset.guid`, `login.guid`, `this._loginGuidsSortedOrder`, `this._logins`, `this._logins[visibleListItems[newlySelectedIndex].dataset.guid].login`, `this._selectedGuid`, `visibleListItems.length`, `visibleListItems[newlySelectedIndex].dataset.guid`

## LoginList._applyFilter()
- 位置: L670-690
- 役割: 検索語が空なら全件を、あれば origin、httpRealm、username、password のいずれかに一致するログイン GUID の集合を返す
- 触るとき: 検索の対象項目を増減させるとき。パスワードも一致判定に使われている点に注意
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
- 役割: 現在の並び替えキーで GUID の順序配列を並べ替える
- 触るとき: 並び替えの対象データや比較関数の受け渡しを変えるとき
- 呼び出し先: `sortFnOptions[sort]()`, `this._loginGuidsSortedOrder.sort()`
- 参照: `this._breachesByLoginGUID`, `this._loginGuidsSortedOrder`, `this._logins`, `this._logins[a].login`, `this._logins[b].login`, `this._sortSelect.value`, `this._vulnerableLoginsByLoginGUID`

## LoginList._applyHeaders()
- 位置: L706-718
- 役割: 並び替えキーに応じた見出し関数で各ログインの見出しを求める。updateAll が false なら既存の見出しを残す
- 触るとき: 見出しが古いまま残る、または並び替え直後に見出しが更新されない不具合を調べるとき
- 条件付き依存: `if (updateAll || !login._header)` → `headerFn()`
- 参照: `login._header`, `login.login`, `this._breachesByLoginGUID`, `this._loginGuidsSortedOrder`, `this._logins`, `this._sortSelect.value`, `this._vulnerableLoginsByLoginGUID`

## LoginList._applySortAndScrollToTop()
- 位置: L720-724
- 役割: 並び替え、再描画を行い、一覧を先頭へスクロールする
- 触るとき: 並び替え後のスクロール位置の扱いを変えるとき
- 呼び出し先: `this._applySort()`, `this.render()`
- 参照: `this._list.scrollTop`

## LoginList.#updateVisibleLoginCount()
- 位置: L726-735
- 役割: 表示件数と全件数を、件数表示の文言に反映する。値が変わったときだけ更新する
- 触るとき: 件数表示の文言(全件か絞り込み後か)を変えるとき
- 呼び出し先: `document.l10n.getAttributes()`
- 条件付き依存: `if (count != args.count || total != args.total)` → `document.l10n.setAttributes()`
- 参照: `args.count`, `args.total`, `document.l10n.getAttributes(this._count).args`, `this._count`

## LoginList.#findPreviousItem()
- 位置: L737-752
- 役割: 直前の可視なログイン行を、セクションをまたいで探す
- 触るとき: 上キーでの移動先の探し方を変えるとき
- 参照: `previousItem.hidden`, `previousItem.lastElementChild`, `previousItem.parentElement.previousElementSibling`, `previousItem.parentElement.tagName`, `previousItem.previousElementSibling`, `previousItem.tagName`

## LoginList.#findNextItem()
- 位置: L754-768
- 役割: 直後の可視なログイン行を、セクションをまたいで探す
- 触るとき: 下キーでの移動先の探し方を変えるとき
- 参照: `nextItem.firstElementChild.nextElementSibling`, `nextItem.hidden`, `nextItem.nextElementSibling`, `nextItem.parentElement.nextElementSibling`, `nextItem.parentElement.tagName`, `nextItem.tagName`

## LoginList.#pickByDirection()
- 位置: L770-772
- 役割: 文書の方向(ltr か rtl)に応じて、左右キーに割り当てる操作を返す
- 触るとき: RTL 対応で左右キーの向きがずれる問題を調べるとき
- 参照: `document.dir`

## LoginList.#activeDescendantForSelection()
- 位置: L775-787
- 役割: 操作の対象になる行を、現在の aria-activedescendant か最初の可視行から選ぶ
- 触るとき: キーボード選択の起点が飛ぶ問題を調べるとき
- 条件付き依存: `if ( !activeDescendant || activeDescendant.hidden || activeDescendant.tagName !== "LOGIN-LIST-ITEM" )` → `this._list.querySelector()`
- 参照: `activeDescendant.hidden`, `activeDescendant.tagName`, `this.#activeDescendant`, `this._list.firstElementChild`

## LoginList._handleKeyboardNavWithinList()
- 位置: L789-838
- 役割: リストにフォーカスがあるときのキー(Space、Enter、矢印キー)を、クリック、次へ、前へのコマンドに変換して実行する
- 触るとき: キーボード操作を追加・変更するとき
- 呼び出し先: `this.#pickByDirection()`
- 条件付き依存: `if (command)` → `event.preventDefault()`
- 条件付き依存: `if (command)` → `this.clickSelected()`
- 条件付き依存: `if (command)` → `this.selectNext()`
- 条件付き依存: `if (command)` → `this.selectPrevious()`
- 参照: `event.key`, `event.type`, `this._list`, `this.shadowRoot.activeElement`

## LoginList.clickSelected()
- 位置: L840-842
- 役割: 現在選ばれている行をクリックする
- 触るとき: キー操作で選択済みの行を開く動作を変えるとき
- 呼び出し先: `this.#activeDescendantForSelection?.click()`

## LoginList.selectNext()
- 位置: L844-852
- 役割: 次の可視行へ移動して選択する
- 触るとき: 下方向の移動挙動を変えるとき
- 条件付き依存: `if (activeDescendant)` → `this.#moveSelection()`
- 条件付き依存: `if (activeDescendant)` → `this.#findNextItem()`
- 参照: `this.#activeDescendantForSelection`

## LoginList.selectPrevious()
- 位置: L854-862
- 役割: 前の可視行へ移動して選択する
- 触るとき: 上方向の移動挙動を変えるとき
- 条件付き依存: `if (activeDescendant)` → `this.#moveSelection()`
- 条件付き依存: `if (activeDescendant)` → `this.#findPreviousItem()`
- 参照: `this.#activeDescendantForSelection`

## LoginList.#moveSelection()
- 位置: L864-872
- 役割: 移動先の行に keyboard-selected を付け、aria-activedescendant を更新し、表示範囲へスクロールしてクリックする
- 触るとき: キー移動時の見た目や、移動と選択が連動する挙動を変えるとき
- 条件付き依存: `if (to)` → `this._list.setAttribute()`
- 条件付き依存: `if (to)` → `from?.classList.remove()`
- 条件付き依存: `if (to)` → `to.classList.add()`
- 条件付き依存: `if (to)` → `to.scrollIntoView()`
- 条件付き依存: `if (to)` → `this.clickSelected()`
- 参照: `to.id`

## LoginList._selectFirstVisibleLogin()
- 位置: L879-901
- 役割: _preselectLogin、ドメイン、先頭の順で候補を決め、可視な最初のログインを初期選択として通知し、ハッシュを更新する
- 触るとき: 起動時にどのログインが選ばれるかを調べる、または変えるとき
- 呼び出し先: `[ selectedLoginGuid, ...this._loginGuidsSortedOrder, ].find()`, `this._applyFilter()`, `this._loginGuidsSortedOrder.find()`, `this.findLoginGuidFromDomain()`, `visibleLoginsGuids.has()`
- 条件付き依存: `if (selectedLogin)` → `window.dispatchEvent()`
- 条件付き依存: `if (selectedLogin)` → `this.updateSelectedLocationHash()`
- 参照: `this._loginGuidsSortedOrder`, `this._logins`, `this._logins[selectedLoginGuid]?.login`, `this._preselectLogin`

## LoginList._setListItemAsSelected()
- 位置: L903-921
- 役割: 前の選択を外し、指定行を選択状態にして、新規作成ボタンと空の行の表示、ハッシュ、スクロールを更新する
- 触るとき: 選択状態の見た目や新規作成ボタンの有効無効を変えるとき
- 呼び出し先: `listItem.classList.add()`, `listItem.scrollIntoView()`, `listItem.setAttribute()`, `this._list.querySelector()`, `this._list.setAttribute()`, `this.classList.toggle()`, `this.updateSelectedLocationHash()`
- 条件付き依存: `if (oldSelectedItem)` → `oldSelectedItem.classList.remove()`
- 条件付き依存: `if (oldSelectedItem)` → `oldSelectedItem.removeAttribute()`
- 参照: `listItem.dataset.guid`, `listItem.id`, `listItem.selected`, `oldSelectedItem.selected`, `this._blankLoginListItem.hidden`, `this._createLoginButton.disabled`, `this._selectedGuid`

## LoginList.updateSelectedLocationHash()
- 位置: L923-925
- 役割: 選択中の GUID を window.location.hash に設定する(空なら消す)
- 触るとき: URL の選択位置の表示を変えるとき
- 呼び出し先: `encodeURIComponent()`
- 参照: `window.location.hash`

## LoginList.findLoginGuidFromDomain()
- 位置: L927-935
- 役割: ホスト名が一致する最初のログインの GUID を返す。見つからなければ null
- 触るとき: ドメイン指定での初期選択を変えるとき
- 参照: `login.hostname`, `this._loginGuidsSortedOrder`, `this._logins`, `this._logins[guid].login`
