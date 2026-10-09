# browser/components/DesktopActorRegistry.sys.mjs

source: browser/components/DesktopActorRegistry.sys.mjs
source-hash: 4ceb32d5517d39074842e78c4f48b06c48e0881d
lines: 1124

## <module>
- 役割: Fission 対応の JS プロセスアクターとウィンドウアクターの登録表を持ち、起動時に ActorManagerParent へ一括登録する DesktopActorRegistry を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## onPreferenceChanged()
- 位置: L58-71
- 役割: RefreshBlockerObserver の有効/無効が変わったとき、全ウィンドウの各ブラウザに PreferenceChanged を isEnabled 付きで送る。
- 触るとき: accessibility.blockautorefresh の切り替えが反映されないとき、またはコンテンツ側への通知方法を変えるときに見る。
- 呼び出し先: `browser.sendMessageToActor()`, `lazy.BrowserWindowTracker.orderedWindows.forEach()`
- 参照: `win.gBrowser.browsers`

## onPreferenceChanged()
- 位置: L409-418
- 役割: CanonicalURL の tabs.notes 設定が変わったとき、CanonicalURL:ActorRegistered か CanonicalURL:ActorUnregistered を observer で通知する。
- 触るとき: ノート機能の切り替え後に canonical URL 連携が働かない、または通知名を変えるときに見る。
- 条件付き依存: `if (isEnabled)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(isEnabled))` → `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## onAddActor()
- 位置: L611-652
- 役割: GenAI アクターの登録条件を見る。チャットプロバイダーやページ要約などのいずれかの pref が有効なら登録し、どれも無効なら解除する。
- 触るとき: AI チャット関連の設定を変えてもアクターが登録されない、または不要な登録が残るときに見る。
- 呼び出し先: `Services.prefs.addObserver()`, `maybeRegister()`
- XPCOM: `Services.prefs`

## maybeRegister()
- 位置: L615-634
- 役割: GenAI の pref 群を評価し、有効なら未登録時のみ register()、無効で登録済みなら unregister() を呼ぶ。
- 触るとき: GenAI の有効条件に pref を足す・外すとき、または登録状態が二重にならないか確かめるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`
- 条件付き依存: `if (!isRegistered)` → `register()`
- 条件付き依存: `if (isRegistered)` → `unregister()`
- XPCOM: `Services.prefs`

## onAddActor()
- 位置: L965-992
- 役割: SmartFormFill アクターについて、browser.smartwindow.enabled と smartformfill.enabled の両方が真なら登録し、そうでなければ解除する。
- 触るとき: スマートウィンドウ版のフォーム補完が有効にならない、または無効化しても動き続けるときに見る。
- 呼び出し先: `Services.prefs.addObserver()`, `maybeRegister()`
- XPCOM: `Services.prefs`

## maybeRegister()
- 位置: L968-984
- 役割: SmartFormFill の二つの pref を評価して register() / unregister() を切り替える。登録状態は isRegistered で管理する。
- 触るとき: SmartFormFill の有効条件を変えるとき、またはアクターの登録と解除が正しく対になるか確かめるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!isRegistered)` → `register()`
- 条件付き依存: `if (isRegistered)` → `unregister()`
- XPCOM: `Services.prefs`

## init()
- 位置: L1119-1122
- 役割: JSPROCESSACTORS と JSWINDOWACTORS を ActorManagerParent に登録し、各アクターを起動時に有効にする。
- 触るとき: 新しいアクターを追加したのに読み込まれない、または起動時の登録順を変えたいときに見る。
- 呼び出し先: `ActorManagerParent.addJSProcessActors()`, `ActorManagerParent.addJSWindowActors()`
