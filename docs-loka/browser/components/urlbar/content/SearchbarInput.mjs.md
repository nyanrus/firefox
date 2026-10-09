# browser/components/urlbar/content/SearchbarInput.mjs

source: browser/components/urlbar/content/SearchbarInput.mjs
source-hash: e752d326b7ebae16dbd726fdbdbd6d6d4bcaf105
lines: 122

## <module>
- 役割: moz-searchbar 要素を支える SearchbarInput(UrlbarInputBase の派生)を定義し、新しい検索バーが有効なときだけ接続する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## SearchbarInput.#shouldConnect()
- 位置: L26-28
- 役割: browser.search.widget.new が真のときだけ true を返す。偽なら従来の XUL 検索バーが使われる。
- 触るとき: 新しい検索バーの有効化条件や切り替えの挙動を変えるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`

## SearchbarInput.connectedCallback()
- 位置: L30-35
- 役割: 新しい検索バーが有効なときだけ親の connectedCallback を呼ぶ。
- 触るとき: 検索バーを DOM に挿入したときに初期化が走らない問題を調べるときに見る。
- 呼び出し先: `super.connectedCallback()`, `this.#shouldConnect()`

## SearchbarInput.disconnectedCallback()
- 位置: L37-42
- 役割: 新しい検索バーが有効なときだけ親の disconnectedCallback を呼ぶ。
- 触るとき: 検索バーを外したときの後始末が漏れる問題を調べるときに見る。
- 呼び出し先: `super.disconnectedCallback()`, `this.#shouldConnect()`

## SearchbarInput.sapInit()
- 位置: L44-47
- 役割: 入力欄の type を search にして、ネイティブのクリアボタンを出す。
- 触るとき: 検索バーのクリアボタンが出ない、または二重に出る問題を調べるときに見る。
- 呼び出し先: `this.inputField.setAttribute()`

## SearchbarInput.sapConnectedCallback()
- 位置: L49-64
- 役割: カスタマイズ中でなければ、xulstore に保存された幅を親要素へ適用する。
- 触るとき: パレットから戻したときに検索バーの幅が元に戻らない問題を調べるときに見る。
- 呼び出し先: `Services.xulStore.getValue()`, `document.documentElement.hasAttribute()`
- 条件付き依存: `if (storedWidth)` → `this.parentElement.setAttribute()`
- 参照: `(this.parentElement).style.width`, `document.documentURI`, `this.parentElement`, `this.parentElement.id`
- XPCOM: `Services.xulStore`

## SearchbarInput.sapDisconnectedCallback()
- 位置: L66-71
- 役割: 検索バーが見えなくなるとき searchMode を null にして検索モードを抜ける。
- 触るとき: 非表示の間にエンジンが削除されても気づかない問題を調べるときに見る。
- 参照: `this.searchMode`

## SearchbarInput.initSapContextMenuItems()
- 位置: L73-93
- 役割: コンテキストメニューの「すべて選択」の後に、区切りと「検索履歴を消去」の項目を追加する。
- 触るとき: 検索バーの右クリックメニューの項目や並び順を変えるときに見る。
- 呼び出し先: `this.addContextMenuItems()`

## createItems()
- 位置: L77-91
- 役割: 区切り線と「検索履歴を消去」の menuitem を作り、押されたら UrlbarUtils.clearFormHistory を呼んでから handleRevert する。
- 触るとき: 検索履歴消去の動作や、メニュー項目の文言を変えるときに見る。
- 呼び出し先: `clearHistory.addEventListener()`, `clearHistory.setAttribute()`, `fragment.append()`, `lazy.UrlbarUtils.clearFormHistory()`, `this.document.createDocumentFragment()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`, `this.handleRevert()`

## SearchbarInput.onPrefChanged()
- 位置: L95-106
- 役割: browser.search.widget.new が変わったとき、接続中なら親の connectedCallback か disconnectedCallback を手動で呼ぶ。
- 触るとき: 設定を切り替えた直後に検索バーの状態が合わない問題を調べるときに見る。
- 呼び出し先: `super.onPrefChanged()`
- 条件付き依存: `if (pref == "browser.search.widget.new" && this.isConnected)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.search.widget.new"))` → `super.connectedCallback()`
- 条件付き依存: `if (!(UrlbarPrefs.get("browser.search.widget.new")))` → `super.disconnectedCallback()`
- 参照: `this.isConnected`

## SearchbarInput.handleEmptyValueNavigation()
- 位置: L108-118
- 役割: 入力が空の状態で操作されたとき、検索モードのエンジン(無ければ既定エンジン)の検索ページを開く。
- 触るとき: 空の入力欄から検索エンジンのページを開く動作を変えるときに見る。
- 呼び出し先: `lazy.UrlbarSearchUtils.getDefaultEngine()`, `lazy.UrlbarSearchUtils.getEngineByName()`, `this.controller.whereToOpen()`, `this.openSearchEnginePage()`
- 参照: `this.isPrivate`, `this.searchMode`, `this.searchMode.engineName`
