# browser/components/urlbar/UrlbarPrefs.sys.mjs

source: browser/components/urlbar/UrlbarPrefs.sys.mjs
source-hash: e044c8a6dfceb9028a0ac7b309df1d2f583cb8e1
lines: 1703

## <module>
- 役割: urlbar の pref と Nimbus 変数を一つの窓口から読み書きする UrlbarPrefs シングルトンを定義するモジュール。既定値の一覧、結果グループの組み立て、オブザーバーへの通知を含む。
- 呼び出し先: `(1000 * 60 * 60 * 24 * 3).toString()`, `XPCOMUtils.declareLazy()`

## makeDefaultResultGroups()
- 位置: L897-1038
- 役割: 通常の urlbar の結果グループ木を作る。ヒューリスティック(最大1件)、Omnibox 拡張、候補(フォーム履歴、最近の検索、リモート候補、尾部候補)、一般(入力履歴、リモートタブ、履歴、about ページ、検索制限キーワード)を flex 比率で配分する。semanticHistory を別グループにする場合は一般の枠を 9:1 に分ける。
- 触るとき: urlbar の候補の種類ごとの件数の比率や並び順を変えたいとき、semanticHistory の別グループ化が効いているかを確かめるとき。
- 呼び出し先: `rootGroup.children.push()`
- 条件付き依存: `if (!showSearchSuggestionsFirst)` → `mainGroup.children.reverse()`
- 参照: `lazy.UrlbarShared.RESULT_GROUP .HEURISTIC_RESTRICT_KEYWORD_AUTOFILL`, `lazy.UrlbarShared.RESULT_GROUP.ABOUT_PAGES`, `lazy.UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.GENERAL`, `lazy.UrlbarShared.RESULT_GROUP.GENERAL_PARENT`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_AUTOFILL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_BOOKMARK_KEYWORD`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_ENGINE_ALIAS`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_EXTENSION`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_FALLBACK`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_HISTORY_URL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_OMNIBOX`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_SEARCH_TIP`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TEST`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TOKEN_ALIAS_ENGINE`, `lazy.UrlbarShared.RESULT_GROUP.INPUT_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.OMNIBOX`, `lazy.UrlbarShared.RESULT_GROUP.RECENT_SEARCH`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_TAB`, `lazy.UrlbarShared.RESULT_GROUP.RESTRICT_SEARCH_KEYWORD`, `lazy.UrlbarShared.RESULT_GROUP.SEMANTIC_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `mainGroup.children`, `mainGroup.children[0].flex`, `mainGroup.children[1].flex`

## makeSmartBarGroups()
- 位置: L1048-1165
- 役割: スマートバー用の結果グループ木を作る。ヒューリスティック(最大1件)のあと、検索候補側と一般側に分け、検索候補側の flex を 2、一般側を 1 にする。AI 候補は先頭に2件分の枠を取る。
- 触るとき: スマートバーの候補の並びや件数を変えたい、または AI 候補の枠が検索候補を押しのけていないか確かめるとき。
- 条件付き依存: `if (!showSearchSuggestionsFirst)` → `mainGroup.children.reverse()`
- 参照: `generalBranch.flex`, `lazy.UrlbarShared.RESULT_GROUP.ABOUT_PAGES`, `lazy.UrlbarShared.RESULT_GROUP.AI`, `lazy.UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.GENERAL`, `lazy.UrlbarShared.RESULT_GROUP.GENERAL_PARENT`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_AI_CHAT`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_AUTOFILL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_FALLBACK`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_HISTORY_URL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TEST`, `lazy.UrlbarShared.RESULT_GROUP.INPUT_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.RECENT_SEARCH`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_TAB`, `lazy.UrlbarShared.RESULT_GROUP.SEMANTIC_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `mainGroup.children`, `searchBranch.flex`

## Preferences.constructor()
- 位置: L1174-1197
- 役割: urlbar ブランチと管理対象の既定 pref にオブザーバーを付け、Nimbus の更新を受け取る。shouldHandOffToSearchMode に関わる pref の一覧を用意する。
- 触るとき: pref を変えても urlbar の値が更新されない、または Nimbus の変更が届かないとき、登録の漏れを確かめるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `PREF_OTHER_DEFAULTS_MAP.keys()`, `Services.prefs.addObserver()`, `lazy.NimbusFeatures.urlbar.onUpdate()`, `this._onNimbusUpdate()`, `this.addObserver()`
- 参照: `this.QueryInterface`, `this._map`, `this._observerWeakRefs`, `this.shouldHandOffToSearchModePrefs`
- XPCOM: `Services.prefs`

## Preferences.get()
- 位置: L1209-1216
- 役割: キャッシュにあればその値を返す。無ければ _getPrefValue で値を求めてキャッシュしてから返す。
- 触るとき: pref を変えた直後なのに古い値が返るとき、キャッシュの消去のタイミングを確かめるとき。
- 呼び出し先: `this._map.get()`
- 条件付き依存: `if (value === undefined)` → `this._getPrefValue()`
- 条件付き依存: `if (value === undefined)` → `this._map.set()`

## Preferences.set()
- 位置: L1228-1234
- 役割: 既定値と同じ型の値だけを書き込む。型が違えば例外を投げる。
- 触るとき: pref の設定時に 'Invalid value type' が出るとき、既定値の型を確かめるとき。
- 呼び出し先: `set()`, `this._getPrefDescriptor()`

## Preferences.toggleResultMenuKeyboardAccessible()
- 位置: L1239-1244
- 役割: resultMenu.keyboardAccessible の真偽を反転させる。
- 触るとき: 結果メニューのボタンを Tab キーで到達できるかを切り替える処理を追うとき。
- 呼び出し先: `this.get()`, `this.set()`

## Preferences.add()
- 位置: L1255-1266
- 役割: カンマ区切りの pref を Set として読み、値を加えてカンマ区切りで保存し直す。Set でない pref を渡すと例外を投げる。
- 触るとき: exposureResults のようなカンマ区切りの一覧に値を足す処理を書くとき、対象の pref が Set として扱われるかを確かめるとき。
- 呼び出し先: `[...maybeSet].join()`, `maybeSet.add()`, `this._getPrefValue()`, `this.set()`

## Preferences.clear()
- 位置: L1274-1277
- 役割: pref のユーザー値を消す。
- 触るとき: 設定を既定値に戻す処理が効かないとき、対象が urlbar ブランチか他のブランチかを確かめるとき。
- 呼び出し先: `clear()`, `this._getPrefDescriptor()`

## Preferences.hasUserValue()
- 位置: L1287-1290
- 役割: pref にユーザー値があるかを返す。
- 触るとき: ユーザーが変えた値と既定値を区別して判定したいとき。
- 呼び出し先: `hasUserValue()`, `this._getPrefDescriptor()`

## Preferences.getScotchBonnetPref()
- 位置: L1301-1303
- 役割: scotchBonnet.enableOverride が真ならそれを返し、そうでなければ指定の pref の値を返す。
- 触るとき: まとめて有効化される機能が個別の pref に従わないとき。既定値が true なので常に真になる点を確かめるとき(要確認)。
- 呼び出し先: `this.get()`

## Preferences.#getShowSearchSuggestionsFirst()
- 位置: L1305-1318
- 役割: 検索語がある、または急上昇と最近の検索がどちらも無効なときに、指定の pref を採用して検索候補を先に出すかを決める。検索エンジンモード中は pref を使わずに判定する。
- 触るとき: 検索候補と一般の結果のどちらが先に出るかが想定と違うとき、エンジンモードでの判定を確かめるとき。
- 呼び出し先: `this.get()`
- 条件付き依存: `if (!inSearchEngineMode && showSearchSuggestionsFirst)` → `this.get()`
- 参照: `context.searchMode?.engineName`, `context.searchString`

## Preferences.getResultGroups()
- 位置: L1320-1368
- 役割: SAP 名と semanticHistory や候補の順序の設定からキャッシュキーを作り、結果グループを取得する。無ければ SAP に応じた builder で作る。未知の SAP では例外を投げる。
- 触るとき: SAP ごとに結果の組み方が違う、または設定を変えても結果グループが更新されないとき。
- 呼び出し先: `makeDefaultResultGroups()`, `makeSmartBarGroups()`, `this.#getOrCacheResultGroups()`, `this.#getShowSearchSuggestionsFirst()`, `this.get()`
- 参照: `context.sapName`

## Preferences.addObserver()
- 位置: L1382-1384
- 役割: オブザーバーを弱参照で登録する。
- 触るとき: オブザーバーが通知を受けなくなったとき、GC で消えていないか、強参照を保持すべきかを判断するとき。
- 呼び出し先: `Cu.getWeakReference()`, `this._observerWeakRefs.push()`

## Preferences.removeObserver()
- 位置: L1392-1400
- 役割: 弱参照の一覧から指定のオブザーバーを1件外す。
- 触るとき: オブザーバーを外した後も通知が届き続けるとき。
- 呼び出し先: `this._observerWeakRefs[i].get()`
- 条件付き依存: `if (obs && obs == observer)` → `this._observerWeakRefs.splice()`
- 参照: `this._observerWeakRefs`, `this._observerWeakRefs.length`

## Preferences.observe()
- 位置: L1412-1421
- 役割: 変わった pref が管理対象(urlbar の既定値か他の既定値)なら onPrefChanged を通知する。それ以外は無視する。
- 触るとき: pref の変更が反映されない、または関係ない pref で通知が走るとき。
- 呼び出し先: `PREF_OTHER_DEFAULTS_MAP.has()`, `PREF_URLBAR_DEFAULTS_MAP.has()`, `data.replace()`, `this.#notifyObservers()`

## Preferences.onPrefChanged()
- 位置: L1430-1457
- 役割: 変わった pref のキャッシュを消す。nova の変更では New Tab 用の値を、autoFill の閾値では対応する値を消す。結果グループに関わる pref ではグループのキャッシュを消す。suggest. で始まる pref では defaultBehavior も消す。
- 触るとき: pref を変えた後に関連する値が古いままになるとき、キャッシュの連動の対応表を確かめるとき。
- 呼び出し先: `pref.startsWith()`, `this.#cachedResultGroups.clear()`, `this._map.delete()`, `this.shouldHandOffToSearchModePrefs.includes()`
- 条件付き依存: `if (pref.startsWith("suggest."))` → `this._map.delete()`
- 条件付き依存: `if (this.shouldHandOffToSearchModePrefs.includes(pref))` → `this._map.delete()`

## Preferences._onNimbusUpdate()
- 位置: L1462-1479
- 役割: Nimbus のキャッシュを消し、新旧の値を比べて変わった変数ごとに onNimbusChanged を通知する。
- 触るとき: Nimbus の値を変えたのにオブザーバーが呼ばれないとき、通知条件を確かめるとき。
- 呼び出し先: `Object.keys()`, `newNimbus.hasOwnProperty()`, `oldNimbus.hasOwnProperty()`, `this._clearNimbusCache()`, `variableNames.add()`
- 条件付き依存: `if ( oldNimbus.hasOwnProperty(name) != newNimbus.hasOwnProperty(name) || oldNimbus[name] !== newNimbus[name] )` → `this.#notifyObservers()`
- 参照: `this._nimbus`

## Preferences._clearNimbusCache()
- 位置: L1489-1498
- 役割: キャッシュされた Nimbus 変数を _map から消し、消す前の値を返す。
- 触るとき: Nimbus 変数の古い値が残って使われるとき。
- 条件付き依存: `if (nimbus)` → `Object.keys()`
- 条件付き依存: `if (nimbus)` → `this._map.delete()`
- 参照: `this.__nimbus`

## Preferences._nimbus()
- 位置: L1500-1507
- 役割: NimbusFeatures.urlbar の全変数を NIMBUS_DEFAULTS を既定値として読み、キャッシュする。
- 触るとき: urlbar の Nimbus 変数の既定値を変えたいとき、どの変数が取得されるかを確かめるとき。
- 条件付き依存: `if (!this.__nimbus)` → `lazy.NimbusFeatures.urlbar.getAllVariables()`
- 参照: `this.__nimbus`

## Preferences._readPref()
- 位置: L1516-1519
- 役割: Services.prefs から、既定値を添えて生の値を読む。
- 触るとき: UrlbarPrefs の返す値が pref の生の値と違って見えるとき、変換前の値を確かめるとき。
- 呼び出し先: `get()`, `this._getPrefDescriptor()`

## Preferences._getPrefValue()
- 位置: L1534-1582
- 役割: 一部の pref を変換して返す。shortcuts.actions は scotchBonnet.enableOverride に、New Tab 系の値は browser.nova.enabled と親の変数に依存させ、defaultBehavior は suggest 系の設定を Places の動作ビットにまとめ、shouldHandOffToSearchMode は関連する2つの pref から求める。AutoFill の閾値は Nimbus の値を優先し、カンマ区切りの pref は Set にする。それ以外は生の値を返す。
- 触るとき: pref の値が変換されて見えて混乱するとき、新しい pref を変換の対象にするかを決めるとき。
- 呼び出し先: `Object.keys()`, `SUGGEST_PREF_TO_BEHAVIOR[ type ].toUpperCase()`, `parseFloat()`, `s.trim()`, `this._readPref()`, `this._readPref(pref) .split()`, `this._readPref(pref) .split(",") .map()`, `this._readPref(pref) .split(",") .map(s => s.trim()) .filter()`, `this.get()`, `this.shouldHandOffToSearchModePrefs.some()`
- 参照: `Ci.mozIPlacesAutoComplete`, `this._nimbus.autoFillAdaptiveHistoryUseCountThreshold`

## Preferences._getPrefDescriptor()
- 位置: L1591-1627
- 役割: pref 名から既定値と型に応じた get・set・clear・hasUserValue を返す。urlbar ブランチ、その他の pref、Nimbus の順に探し、どれにもなければ例外を投げる。
- 触るとき: 未定義の pref を読んで 'Trying to access an unknown pref' が出たとき、新しい pref の定義を追加する場所を確かめるとき。
- 呼び出し先: `Array.isArray()`, `PREF_URLBAR_DEFAULTS_MAP.get()`, `Services.prefs.getBranch()`
- 条件付き依存: `if (defaultValue === undefined)` → `PREF_OTHER_DEFAULTS_MAP.get()`
- 条件付き依存: `if (defaultValue === undefined)` → `this._getNimbusDescriptor()`
- 条件付き依存: `if (!Array.isArray(defaultValue))` → `PREF_TYPES.get()`
- 条件付き依存: `if (!(!Array.isArray(defaultValue)))` → `PREF_TYPES.get()`
- 参照: `Services.prefs`, `branch.clearUserPref`, `branch.prefHasUserValue`, `defaultValue.length`
- XPCOM: `Services.prefs`

## Preferences._getNimbusDescriptor()
- 位置: L1641-1660
- 役割: Nimbus の変数を pref と同じ形の記述子にして返す。値の取得だけができ、設定・削除・ユーザー値の問い合わせは例外を投げる。変数が無ければ null を返す。
- 触るとき: Nimbus の変数を pref と同じように扱おうとして例外になるとき。
- 呼び出し先: `this._nimbus.hasOwnProperty()`
- 参照: `this._nimbus`

## get()
- 位置: L1647-1647
- 役割: Nimbus 記述子の値を返す。呼ばれた時点の Nimbus の値を読む。
- 触るとき: Nimbus 変数の現在値が古いと疑うとき。
- 参照: `this._nimbus`

## Preferences.set()
- 位置: L1648-1650
- 役割: Nimbus 変数に書き込めないので、呼ぶと例外を投げる。
- 触るとき: Nimbus 変数を設定しようとして例外になったとき。

## Preferences.clear()
- 位置: L1651-1653
- 役割: Nimbus 変数は消せないので、呼ぶと例外を投げる。
- 触るとき: Nimbus 変数を削除しようとして例外になったとき。

## Preferences.hasUserValue()
- 位置: L1654-1658
- 役割: Nimbus 変数にはユーザー値が無いので、呼ぶと例外を投げる。
- 触るとき: Nimbus 変数に対してユーザー値の有無を調べようとして例外になったとき。

## Preferences.#getOrCacheResultGroups()
- 位置: L1667-1674
- 役割: キーに対応する結果グループをキャッシュから返し、無ければ builder で作って保存する。
- 触るとき: 結果グループのキャッシュが古いまま使われるとき、キーに含めるべき条件が抜けていないか確かめるとき。
- 呼び出し先: `this.#cachedResultGroups.get()`
- 条件付き依存: `if (!groups)` → `builder()`
- 条件付き依存: `if (!groups)` → `this.#cachedResultGroups.set()`

## Preferences.#notifyObservers()
- 位置: L1676-1699
- 役割: 生きているオブザーバーのうち、そのメソッドを持つものだけを呼ぶ。GC 済みは一覧から外し、例外は console.error に出して続ける。
- 触るとき: 一部のオブザーバーにだけ通知が届かないとき、通知の流れを追うとき。
- 呼び出し先: `this._observerWeakRefs[i].get()`
- 条件付き依存: `if (!observer)` → `this._observerWeakRefs.splice()`
- 条件付き依存: `if (!inParent)` → `Cu.waiveXrays()`
- 条件付き依存: `if (method in observer)` → `observer[method]()`
- 条件付き依存: `if (method in observer)` → `console.error()`
- 参照: `this._observerWeakRefs`, `this._observerWeakRefs.length`
