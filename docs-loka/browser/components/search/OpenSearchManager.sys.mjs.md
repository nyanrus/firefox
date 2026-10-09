# browser/components/search/OpenSearchManager.sys.mjs

source: browser/components/search/OpenSearchManager.sys.mjs
source-hash: 9cef0f93c090c991a7bdc340e16c3efbf19a411a
lines: 250

## <module>
- 役割: ブラウザごとに、表示中のページが提供する OpenSearch エンジンの提案を管理する
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _OpenSearchManager.constructor()
- 位置: L41-43
- 役割: browser-search-engine-modified の observer として自身を登録する
- 触るとき: 検索エンジンの追加・削除の通知が届かない不具合を調べるとき
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## _OpenSearchManager.observe()
- 位置: L55-75
- 役割: エンジン追加では提案一覧から同名を外し、削除では隠し一覧から提案一覧へ戻す
- 触るとき: 検索エンジンを追加・削除したあとに追加ボタンの表示が合わないとき。engine-added と engine-removed の分岐を見る
- 呼び出し先: `this.#addMaybeOfferedEngine()`, `this.#removeMaybeOfferedEngine()`
- 参照: `engine.name`, `subject.wrappedJSObject`

## _OpenSearchManager.addEngine()
- 位置: L87-126
- 役割: ページ由来の OpenSearch エンジンを提案一覧に加える。同名のエンジンが既に導入済みなら隠し一覧へ入れる
- 触るとき: ページの検索エンジン提案を受けたときの扱いを変えるとき。検索サービスの初期化前は何もせず戻るので、起動直後の提案が消える原因になりうる
- 呼び出し先: `engines.push()`, `lazy.SearchService.getEngineByName()`, `this.#hiddenEngines.get()`, `this.#offeredEngines.get()`, `this.#offeredEngines.get(browser)?.some()`
- 条件付き依存: `if (shouldBeHidden)` → `this.#hiddenEngines.set()`
- 条件付き依存: `if (!(shouldBeHidden))` → `this.#offeredEngines.set()`
- 条件付き依存: `if (browser == win.gBrowser.selectedBrowser)` → `this.updateOpenSearchBadge()`
- 参照: `browser.documentGlobal`, `e.title`, `engine.href`, `engine.title`, `lazy.SearchService.hasSuccessfullyInitialized`, `win.gBrowser.selectedBrowser`

## _OpenSearchManager.icon()
- 位置: L112-114
- 役割: 提案エンジンのアイコンとして、提案元ブラウザの mIconURL を返す getter
- 触るとき: 提案エンジンのアイコンが別のページのものになる、または出ないときに見る
- 参照: `browser.mIconURL`

## _OpenSearchManager.updateOpenSearchBadge()
- 位置: L136-163
- 役割: 選択中タブの提案エンジンを各 URL バーの追加ボタンと検索バーの addengines 属性へ反映する
- 触るとき: タブを切り替えたり読み込みを終えたりしたあとに追加ボタンが出ない、または残るとき
- 呼び出し先: `this.getInstallableEngines()`, `urlbar.addSearchEngineHelper.setEnginesFromBrowser()`, `urlbar.searchModeSwitcher.toggleAddEnginesBadge()`, `win.document.getElementById()`, `win.document.querySelectorAll()`
- 条件付き依存: `if (engines && engines.length)` → `searchBar.setAttribute()`
- 条件付き依存: `if (!(engines && engines.length))` → `searchBar.removeAttribute()`
- 参照: `engines.length`, `engines?.length`, `urlbar.controller`, `win.gBrowser.selectedBrowser`

## _OpenSearchManager.#addMaybeOfferedEngine()
- 位置: L165-187
- 役割: 全ウィンドウのタブを走査し、同名の隠しエンジンを提案一覧へ戻す。選択中タブなら表示も更新する
- 触るとき: 検索エンジンを削除した後に、ページの提案が再び出てこないとき
- 呼び出し先: `this.#hiddenEngines.get()`, `this.#offeredEngines.get()`
- 条件付き依存: `if (hiddenEngines[i].title == engineName)` → `offeredEngines.push()`
- 条件付き依存: `if (offeredEngines.length == 1)` → `this.#offeredEngines.set()`
- 条件付き依存: `if (hiddenEngines[i].title == engineName)` → `hiddenEngines.splice()`
- 条件付き依存: `if (browser == win.gBrowser.selectedBrowser)` → `this.updateOpenSearchBadge()`
- 参照: `hiddenEngines.length`, `hiddenEngines[i].title`, `lazy.BrowserWindowTracker.orderedWindows`, `offeredEngines.length`, `win.gBrowser.browsers`, `win.gBrowser.selectedBrowser`

## _OpenSearchManager.#removeMaybeOfferedEngine()
- 位置: L189-211
- 役割: 全ウィンドウのタブを走査し、同名の提案エンジンを隠し一覧へ移す。選択中タブなら表示も更新する
- 触るとき: 検索エンジンを追加した後に、同名の提案が追加ボタンに残るとき
- 呼び出し先: `this.#hiddenEngines.get()`, `this.#offeredEngines.get()`
- 条件付き依存: `if (offeredEngines[i].title == engineName)` → `hiddenEngines.push()`
- 条件付き依存: `if (hiddenEngines.length == 1)` → `this.#hiddenEngines.set()`
- 条件付き依存: `if (offeredEngines[i].title == engineName)` → `offeredEngines.splice()`
- 条件付き依存: `if (browser == win.gBrowser.selectedBrowser)` → `this.updateOpenSearchBadge()`
- 参照: `hiddenEngines.length`, `lazy.BrowserWindowTracker.orderedWindows`, `offeredEngines.length`, `offeredEngines[i].title`, `win.gBrowser.browsers`, `win.gBrowser.selectedBrowser`

## _OpenSearchManager.getEngines()
- 位置: L221-223
- 役割: ブラウザが提案中の OpenSearch エンジン一覧を返す。無ければ空配列
- 触るとき: 提案一覧を読んでいる呼び出し元を追うとき。隠し一覧は含まれない
- 呼び出し先: `this.#offeredEngines.get()`

## _OpenSearchManager.getInstallableEngines()
- 位置: L236-241
- 役割: installSearchEngine ポリシーが許可するときだけ提案一覧を返し、禁止なら空配列を返す
- 触るとき: 企業ポリシーで検索エンジンの追加を止める挙動を変えるとき。禁止時も一覧自体は残り、一回限りの検索には使われる
- 呼び出し先: `Services.policies.isAllowed()`, `this.getEngines()`
- XPCOM: `Services.policies`

## _OpenSearchManager.clearEngines()
- 位置: L243-246
- 役割: ブラウザについて提案一覧と隠し一覧の両方を削除する
- 触るとき: タブの提案が前のページから残る不具合を調べるとき。呼び出し元は本文からは分からない(要確認)
- 呼び出し先: `this.#hiddenEngines.delete()`, `this.#offeredEngines.delete()`
