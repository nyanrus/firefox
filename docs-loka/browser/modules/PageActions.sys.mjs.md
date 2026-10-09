# browser/modules/PageActions.sys.mjs

source: browser/modules/PageActions.sys.mjs
source-hash: 6014ddbb406821a10937c2666ae7cc614e55bd16
lines: 1290

## <module>
- 役割: アドレスバーとページ操作パネルに置く「ページアクション」を登録・配置・永続化する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## escapeCSSURL()
- 位置: L24-26
- 役割: URL を CSS の url() 値にエスケープして包む。
- 触るとき: アイコン URL を CSS 変数に入れる箇所で、特殊文字の扱いを変えるとき。
- 呼び出し先: `url.replace()`

## init()
- 位置: L36-77
- 役割: 組み込みアクションを登録し、保存済みの配置を読み込み、全ウィンドウのアドレスバーに配置する。
- 触るとき: 起動時の初期化順序を変えるとき。init 前の addAction は保留され、ここで順に実行される。終了時の掃除処理もここで登録する (テストでは addShutdownBlocker を偽にできる)。
- 呼び出し先: `allBrowserPageActions()`, `bpa.placeAllActionsInUrlbar()`, `callbacks.shift()`, `callbacks.shift()()`, `this._initBuiltInActions()`, `this._loadPersistedActions()`, `this.actionForID()`
- 条件付き依存: `if (!this.actionForID(options.id))` → `this._registerAction()`
- 条件付き依存: `if (addShutdownBlocker)` → `lazy.AsyncShutdown.profileBeforeChange.addBlocker()`
- 条件付き依存: `if (addShutdownBlocker)` → `this._purgeUnregisteredPersistedActions()`
- 参照: `callbacks.length`, `options.id`, `this._deferredAddActionCalls`

## actions()
- 位置: L85-92
- 役割: 組み込み、非組み込み、一時の3種類のアクションを連結して返す。
- 触るとき: 登録済みの全アクションを列挙する箇所を変えるとき。返り値はコピーで、ライブではない。
- 呼び出し先: `lists.reduce()`, `memo.concat()`
- 参照: `this._builtInActions`, `this._nonBuiltInActions`, `this._transientActions`

## actionsInPanel()
- 位置: L105-135
- 役割: 指定ウィンドウのパネルに出すアクションを、区切り線を挟みながら順に返す。
- 触るとき: ページアクションパネルの項目順や区切り線を変えるとき。各グループは shouldShowInPanel の判定で絞り込む。
- 呼び出し先: `this._builtInActions.filter()`, `this._nonBuiltInActions.filter()`, `this._transientActions.filter()`
- 条件付き依存: `if (actions.length)` → `actions.push()`
- 条件付き依存: `if (nonBuiltInActions.length)` → `actions.push()`
- 条件付き依存: `if (transientActions.length)` → `actions.push()`
- 参照: `actions.length`, `nonBuiltInActions.length`, `transientActions.length`

## filter()
- 位置: L106-108
- 役割: パネルに表示するかを、そのアクションの判定に任せる。
- 触るとき: パネル表示の判定が一覧に効いていない報告を調べるとき。
- 呼び出し先: `action.shouldShowInPanel()`

## actionsInUrlbar()
- 位置: L146-156
- 役割: 保存された urlbar の並びから、そのウィンドウで表示すべきアクションを返す。
- 触るとき: アドレスバーに出るボタンの並びや表示条件を変えるとき。未登録の ID は読み飛ばす。
- 呼び出し先: `action.shouldShowInUrlbar()`, `this._persistedActions.idsInUrlbar.reduce()`, `this.actionForID()`
- 条件付き依存: `if (action && action.shouldShowInUrlbar(browserWindow))` → `actions.push()`

## actionForID()
- 位置: L165-167
- 役割: ID から登録済みアクションを返す。無ければ undefined。
- 触るとき: アクション ID の参照箇所で、登録済みかどうかの扱いを確かめるとき。
- 呼び出し先: `this._actionsByID.get()`

## addAction()
- 位置: L184-196
- 役割: アクションを登録し、開いている全ウィンドウに配置する。init 前なら保留する。
- 触るとき: 拡張や内部コードからページアクションを追加する処理を変えるとき。
- 呼び出し先: `allBrowserPageActions()`, `bpa.placeAction()`, `this._registerAction()`
- 条件付き依存: `if (this._deferredAddActionCalls)` → `this._deferredAddActionCalls.push()`
- 条件付き依存: `if (this._deferredAddActionCalls)` → `this.addAction()`
- 参照: `this._deferredAddActionCalls`

## _registerAction()
- 位置: L198-253
- 役割: アクションを ID で登録し、種類に応じた一覧へ入れて永続状態を更新する。
- 触るとき: 同じ ID の二重登録、並び順(組み込み、拡張はタイトル順、一時)、urlbar 既定配置の挙動を調べるとき。同じ ID が既にあれば例外を投げる。
- 呼び出し先: `this._actionsByID.set()`, `this._persistedActions.ids.includes()`, `this._updateIDsPinnedToUrlbarForAction()`, `this.actionForID()`
- 条件付き依存: `if ("__insertBeforeActionID" in action)` → `this._builtInActions.findIndex()`
- 条件付き依存: `if (index < 0)` → `this._builtInActions.filter()`
- 条件付き依存: `if ("__insertBeforeActionID" in action)` → `this._builtInActions.splice()`
- 条件付き依存: `if (action.__transient)` → `this._transientActions.push()`
- 条件付き依存: `if (action._isBuiltIn)` → `this._builtInActions.push()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `lazy.BinarySearch.insertionIndexOf()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `a1.getTitle().localeCompare()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `a1.getTitle()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `a2.getTitle()`
- 条件付き依存: `if (!(action._isBuiltIn))` → `this._nonBuiltInActions.splice()`
- 条件付き依存: `if (isNew)` → `this._persistedActions.ids.push()`
- 参照: `a.__transient`, `a.id`, `action.__insertBeforeActionID`, `action.__isSeparator`, `action.__transient`, `action._isBuiltIn`, `action._pinnedToUrlbar`, `action.id`, `this._builtInActions.filter(a => !a.__transient).length`, `this._nonBuiltInActions`

## _updateIDsPinnedToUrlbarForAction()
- 位置: L255-272
- 役割: アクションが urlbar にピン留めされているかに応じて、永続リストの ID を追加か削除する。
- 触るとき: urlbar での並び位置を変えるとき。新規の ID は、ブックマークより前に入る (ブックマークが無ければ末尾)。最後に永続状態を保存する。
- 呼び出し先: `this._persistedActions.idsInUrlbar.indexOf()`, `this._storePersistedActions()`
- 条件付き依存: `if (index < 0)` → `this._persistedActions.idsInUrlbar.indexOf()`
- 条件付き依存: `if (index < 0)` → `this._persistedActions.idsInUrlbar.splice()`
- 条件付き依存: `if (index >= 0)` → `this._persistedActions.idsInUrlbar.splice()`
- 参照: `action.id`, `action.pinnedToUrlbar`, `this._persistedActions.idsInUrlbar.length`

## onActionRemoved()
- 位置: L286-309
- 役割: アクションを登録から外し、各ウィンドウからも取り除く。
- 触るとき: 拡張のアンインストールや無効化で、ボタンが残る報告を調べるとき。永続状態は終了時まで残す。
- 呼び出し先: `allBrowserPageActions()`, `bpa.removeAction()`, `list.findIndex()`, `this._actionsByID.delete()`, `this.actionForID()`
- 条件付き依存: `if (index >= 0)` → `list.splice()`
- 参照: `a.id`, `action.id`, `this._builtInActions`, `this._nonBuiltInActions`, `this._transientActions`

## onActionToggledPinnedToUrlbar()
- 位置: L317-326
- 役割: ピン留め状態が変わったとき、永続リストを更新して各ウィンドウの配置を直す。
- 触るとき: アドレスバーへのピン留めの切り替え処理を変えるとき。
- 呼び出し先: `allBrowserPageActions()`, `bpa.placeActionInUrlbar()`, `this._updateIDsPinnedToUrlbarForAction()`, `this.actionForID()`
- 参照: `action.id`

## _reset()
- 位置: L329-335
- 役割: テスト用に、未登録の永続状態を消して内部の登録一覧を空にする。
- 触るとき: テストの前後で登録状態をリセットする処理を変えるとき。本番では使わない。
- 呼び出し先: `PageActions._purgeUnregisteredPersistedActions()`
- 参照: `PageActions._actionsByID`, `PageActions._builtInActions`, `PageActions._nonBuiltInActions`, `PageActions._transientActions`

## _storePersistedActions()
- 位置: L337-340
- 役割: 永続状態を JSON にして、設定値に保存する。
- 触るとき: 保存形式や保存先の設定名を変えるとき。
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`
- 参照: `this._persistedActions`
- XPCOM: `Services.prefs`

## _loadPersistedActions()
- 位置: L342-366
- 役割: 保存済みの JSON を読み、旧版の移行と Proton の移行を順に適用する。
- 触るとき: 起動時の永続状態の読み込みを変えるとき、または Proton の切り替え(ダウングレード含む)の挙動を確かめるとき。読めなければ既定値を使う。
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`, `this._migratePersistedActions()`, `this._migratePersistedActionsProton()`
- 参照: `this._persistedActions`
- XPCOM: `Services.prefs`

## _purgeUnregisteredPersistedActions()
- 位置: L368-377
- 役割: 登録されていない ID を永続状態から取り除いて保存する。
- 触るとき: 終了時に古い拡張の配置を消す処理を変えるとき。
- 呼び出し先: `this._persistedActions[name].filter()`, `this._storePersistedActions()`, `this.actionForID()`
- 参照: `this._persistedActions`

## _migratePersistedActions()
- 位置: L379-392
- 役割: 永続状態のバージョンを1つずつ上げ、現在のバージョンまで移行する。
- 触るとき: 永続状態の形式を変えてバージョンを上げるとき。新しい移行関数は _migratePersistedActionsTo<N> の名前で追加する。
- 呼び出し先: `this[methodName]()`
- 参照: `actions.version`

## _migratePersistedActionsTo1()
- 位置: L394-412
- 役割: ids を配列にし、ブックマークの ID を urlbar の末尾へ移す。
- 触るとき: ver 1 への移行結果を確かめるとき。ブックマークは常に urlbar の末尾に残す。
- 呼び出し先: `actions.idsInUrlbar.indexOf()`, `ids.push()`
- 条件付き依存: `if (bookmarkIndex >= 0)` → `actions.idsInUrlbar.splice()`
- 条件付き依存: `if (bookmarkIndex >= 0)` → `actions.idsInUrlbar.push()`
- 参照: `actions.ids`, `actions.idsInUrlbar`

## _migratePersistedActionsProton()
- 位置: L414-430
- 役割: Proton の移行用に、移行前の urlbar 一覧を保存する。無ければ新規の既定値を作る。
- 触るとき: Proton の有効・無効の切り替え時に urlbar の並びが戻る理由を調べるとき。
- 参照: `actions.idsInUrlbar`, `actions.idsInUrlbarPreProton`, `actions?.idsInUrlbarPreProton`

## sendPlacedInUrlbarTrigger()
- 位置: L438-464
- 役割: urlbar に配置されたボタンについて、500ms 後に ASRouter のトリガーを送る。
- 触るとき: urlbar の配置をきっかけにしたメッセージを追加・変更するとき。URL とホストを param として付ける。
- 呼び出し先: `lazy.ASRouter.sendTriggerMessage()`, `lazy.setTimeout()`
- 参照: `buttonNode.hidden`, `buttonNode.id`, `buttonNode?.documentGlobal`, `lazy.ASRouter.waitForInitialized`, `param.host`, `trigger.param`, `win.gBrowser.selectedBrowser`, `win.gBrowser.selectedBrowser?.currentURI`

## Action()
- 位置: L588-668
- 役割: オプションを検証してアクションの状態を作る。未知のオプションは例外にする。
- 触るとき: アクションに新しいオプションを追加するとき。必須の id 以外は省略可能。_ で始まる項目は内部用。
- 呼び出し先: `setProperties()`, `this._createIconProperties()`
- 参照: `this._disabled`, `this._globalProps`, `this._iconProperties`, `this._iconURL`, `this._title`, `this._tooltip`, `this._wantsSubview`, `this._windowProps`

## extensionID()
- 位置: L674-676
- 役割: アクションが属する拡張の ID を返す。
- 触るとき: 拡張由来のアクションかを判定する箇所を確かめるとき。
- 参照: `this._extensionID`

## id()
- 位置: L681-683
- 役割: アクションの ID を返す。
- 触るとき: ID による照合の元を確かめるとき。
- 参照: `this._id`

## disablePrivateBrowsing()
- 位置: L685-687
- 役割: プライベートウィンドウで出さないかを真偽で返す。
- 触るとき: プライベートブラウジングでの表示可否を変えるとき。
- 参照: `this._disablePrivateBrowsing`

## canShowInWindow()
- 位置: L693-704
- 役割: 拡張がそのウィンドウへのアクセス権を持ち、かつプライベート制限に反しないかを返す。
- 触るとき: 特定ウィンドウで項目が消える報告を調べるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (this._extensionID)` → `WebExtensionPolicy.getByID()`
- 条件付き依存: `if (this._extensionID)` → `policy.canAccessWindow()`
- 参照: `this._extensionID`, `this.disablePrivateBrowsing`

## pinnedToUrlbar()
- 位置: L710-712
- 役割: urlbar にピン留めされているかを返す。
- 触るとき: アドレスバーに出すかの判定元を確かめるとき。
- 参照: `this._pinnedToUrlbar`

## pinnedToUrlbar()
- 位置: L713-719
- 役割: ピン留め状態を設定し、値が変わったときだけ通知する。
- 触るとき: ピン留めの切り替えで各ウィンドウの表示を更新させたいとき。
- 条件付き依存: `if (this.pinnedToUrlbar != shown)` → `PageActions.onActionToggledPinnedToUrlbar()`
- 条件付き依存: `if (this.pinnedToUrlbar != shown)` → `this.onPinToUrlbarToggled()`
- 参照: `this._pinnedToUrlbar`, `this.pinnedToUrlbar`

## getDisabled()
- 位置: L724-726
- 役割: 無効状態を、指定ウィンドウの値(無ければ全体の値)で返す。
- 触るとき: ウィンドウ単位の無効化が効かない報告を調べるとき。
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).disabled`

## setDisabled()
- 位置: L727-729
- 役割: 無効状態を設定する。ウィンドウ指定があればそのウィンドウだけに効く。
- 触るとき: 拡張のボタンを無効にする処理の範囲を確かめるとき。
- 呼び出し先: `this._setProperty()`

## getIconURL()
- 位置: L735-737
- 役割: アイコン URL(文字列またはサイズ別のオブジェクト)を返す。
- 触るとき: アイコンの参照元を確かめるとき。
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).iconURL`

## setIconURL()
- 位置: L738-745
- 役割: アイコン URL を設定し、CSS 変数の値も作り直して反映する。
- 触るとき: アイコンを動的に変える処理を追加・変更するとき。
- 呼び出し先: `this._createIconProperties()`, `this._getProperties()`, `this._updateProperty()`
- 参照: `props.iconProps`, `props.iconURL`

## getIconProperties()
- 位置: L751-753
- 役割: アイコン用の CSS 変数の一式を返す。
- 触るとき: ボタンに適用される CSS 変数の値を確かめるとき。
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).iconProps`

## _createIconProperties()
- 位置: L755-774
- 役割: アイコン URL から CSS 変数を作る。サイズ別なら 16px と 32px(2x)の image-set にする。
- 触るとき: アイコンの解像度の出し分けを変えるとき。作った値はキャッシュされ、同じ入力には同じ値を返す。
- 呼び出し先: `Object.freeze()`, `escapeCSSURL()`
- 条件付き依存: `if (urls && typeof urls == "object")` → `this._iconProperties.get()`
- 条件付き依存: `if (!props)` → `Object.freeze()`
- 条件付き依存: `if (!props)` → `escapeCSSURL()`
- 条件付き依存: `if (!props)` → `this._iconURLForSize()`
- 条件付き依存: `if (!props)` → `this._iconProperties.set()`

## getTitle()
- 位置: L780-782
- 役割: タイトルを返す。組み込みアクションには無い。
- 触るとき: パネルや urlbar の名前を取り出す箇所を確かめるとき。
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).title`

## setTitle()
- 位置: L783-785
- 役割: タイトルを設定し、表示を更新する。
- 触るとき: 拡張がタイトルを変えたときの反映を確かめるとき。
- 呼び出し先: `this._setProperty()`

## getTooltip()
- 位置: L790-792
- 役割: ツールチップ文字列を返す。
- 触るとき: ボタンのツールチップの元を確かめるとき。
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).tooltip`

## setTooltip()
- 位置: L793-795
- 役割: ツールチップを設定し、表示を更新する。
- 触るとき: ツールチップの変更が反映されない報告を調べるとき。
- 呼び出し先: `this._setProperty()`

## getWantsSubview()
- 位置: L800-802
- 役割: サブビューを持つかを真偽で返す。
- 触るとき: クリックでサブビューを開くかどうかの判定元を確かめるとき。
- 呼び出し先: `this._getProperties()`
- 参照: `this._getProperties(browserWindow).wantsSubview`

## setWantsSubview()
- 位置: L803-805
- 役割: サブビューを持つかを設定する。
- 触るとき: サブビュー表示に切り替える処理を変えるとき。
- 呼び出し先: `this._setProperty()`

## _setProperty()
- 位置: L818-824
- 役割: プロパティ値を保存し、表示を更新する。ウィンドウ指定があれば、そのウィンドウ用の値を作る。
- 触るとき: ウィンドウ単位の状態を追加するとき。値は全体の値を継承する。
- 呼び出し先: `this._getProperties()`, `this._updateProperty()`

## _updateProperty()
- 位置: L826-833
- 役割: 登録済みのアクションについて、対象の各ウィンドウに値の変化を反映する。
- 触るとき: 表示の更新が特定のウィンドウだけ抜ける報告を調べるとき。登録前の呼び出しは無視する。
- 呼び出し先: `PageActions.actionForID()`
- 条件付き依存: `if (PageActions.actionForID(this.id))` → `allBrowserPageActions()`
- 条件付き依存: `if (PageActions.actionForID(this.id))` → `bpa.updateAction()`
- 参照: `this.id`

## _getProperties()
- 位置: L849-858
- 役割: ウィンドウ用の値があればそれを、無ければ全体の値を返す。必要なら作って返す。
- 触るとき: ウィンドウごとの状態の参照規則を変えるとき。
- 呼び出し先: `this._windowProps.get()`
- 条件付き依存: `if (!props && forceWindowSpecific)` → `Object.create()`
- 条件付き依存: `if (!props && forceWindowSpecific)` → `this._windowProps.set()`
- 参照: `this._globalProps`

## anchorIDOverride()
- 位置: L863-865
- 役割: パネルを開くときの基準となる要素 ID の上書き値を返す。
- 触るとき: パネルの位置合わせの基準を差し替えたいとき。
- 参照: `this._anchorIDOverride`

## urlbarIDOverride()
- 位置: L870-872
- 役割: アドレスバーのボタン ID の上書き値を返す。
- 触るとき: 既存のマークアップのボタンと結び付けるとき。
- 参照: `this._urlbarIDOverride`

## wantsIframe()
- 位置: L877-879
- 役割: クリックで iframe を出すかを真偽で返す。
- 触るとき: iframe 型のアクションの判定元を確かめるとき。
- 参照: `this._wantsIframe`

## isBadged()
- 位置: L881-883
- 役割: バッジ表示の有無を真偽で返す。
- 触るとき: ボタンに badged 属性を付けるかを確かめるとき。
- 参照: `this._isBadged`

## labelForHistogram()
- 位置: L885-893
- 役割: テレメトリ用のラベルを返す。指定が無ければ ID から作り、20 文字以内にする。
- 触るとき: テレメトリのラベルが長すぎる、または不正になる報告を調べるとき。20 文字の上限はテレメトリ側の制約による。
- 呼び出し先: `match[1].toUpperCase()`, `this._id.replace()`, `this._id.replace(/_\w{1}/g, match => match[1].toUpperCase()).substr()`
- 参照: `this._labelForHistogram`

## _iconURLForSize()
- 位置: L911-928
- 役割: 優先サイズに合うアイコンを、同サイズ、2倍、次に大きい、最大の順に選ぶ。
- 触るとき: アイコンの解像度の選び方を変えるとき。WebExtension の挙動に合わせてある。
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `Object.keys(urls) .map(key => parseInt(key, 10)) .sort()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `Object.keys(urls) .map()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `Object.keys()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `parseInt()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `sizes.find()`
- 条件付き依存: `if (!(urls[2 * preferredSize]))` → `sizes.pop()`

## doCommand()
- 位置: L938-940
- 役割: アクションの実行を、ウィンドウのページアクション管理へ渡す。
- 触るとき: ボタンを押したときの処理の入口を確かめるとき。
- 呼び出し先: `browserPageActions()`, `browserPageActions(browserWindow).doCommandForAction()`

## onBeforePlacedInWindow()
- 位置: L948-952
- 役割: ウィンドウに配置される前に、登録されたコールバックを呼ぶ。
- 触るとき: 配置の直前に行う準備を追加するとき。
- 条件付き依存: `if (this._onBeforePlacedInWindow)` → `this._onBeforePlacedInWindow()`
- 参照: `this._onBeforePlacedInWindow`

## onCommand()
- 位置: L962-966
- 役割: クリック時に登録されたコールバックを呼ぶ。
- 触るとき: ボタンのクリック処理が呼ばれない報告を調べるとき。サブビューや iframe を持つ場合は呼ばれない。
- 条件付き依存: `if (this._onCommand)` → `this._onCommand()`
- 参照: `this._onCommand`

## onIframeHiding()
- 位置: L976-980
- 役割: iframe が隠れ始めるときに、登録されたコールバックを呼ぶ。
- 触るとき: iframe の表示切り替えに合わせた後始末を変えるとき。
- 条件付き依存: `if (this._onIframeHiding)` → `this._onIframeHiding()`
- 参照: `this._onIframeHiding`

## onIframeHidden()
- 位置: L990-994
- 役割: iframe が隠れ終わったときに、登録されたコールバックを呼ぶ。
- 触るとき: iframe を隠した後の後始末を変えるとき。
- 条件付き依存: `if (this._onIframeHidden)` → `this._onIframeHidden()`
- 参照: `this._onIframeHidden`

## onIframeShowing()
- 位置: L1004-1008
- 役割: iframe が表示されるときに、登録されたコールバックを呼ぶ。
- 触るとき: iframe を表示するときの準備を変えるとき。
- 条件付き依存: `if (this._onIframeShowing)` → `this._onIframeShowing()`
- 参照: `this._onIframeShowing`

## onLocationChange()
- 位置: L1016-1020
- 役割: タブ切り替えや読み込み先の変化時に、登録されたコールバックを呼ぶ。
- 触るとき: タブごとに表示を変える処理が遅れる報告を調べるとき。
- 条件付き依存: `if (this._onLocationChange)` → `this._onLocationChange()`
- 参照: `this._onLocationChange`

## onPlacedInPanel()
- 位置: L1028-1032
- 役割: パネルに項目が追加されたときに、登録されたコールバックを呼ぶ。
- 触るとき: パネルの項目の初期化を変えるとき。
- 条件付き依存: `if (this._onPlacedInPanel)` → `this._onPlacedInPanel()`
- 参照: `this._onPlacedInPanel`

## onPlacedInUrlbar()
- 位置: L1040-1044
- 役割: アドレスバーに項目が追加されたときに、登録されたコールバックを呼ぶ。
- 触るとき: アドレスバーのボタンの初期化を変えるとき。
- 条件付き依存: `if (this._onPlacedInUrlbar)` → `this._onPlacedInUrlbar()`
- 参照: `this._onPlacedInUrlbar`

## onRemovedFromWindow()
- 位置: L1053-1057
- 役割: ウィンドウから項目が外れたときに、登録されたコールバックを呼ぶ。
- 触るとき: ウィンドウを閉じた後の後始末を確かめるとき。
- 条件付き依存: `if (this._onRemovedFromWindow)` → `this._onRemovedFromWindow()`
- 参照: `this._onRemovedFromWindow`

## onShowingInPanel()
- 位置: L1065-1069
- 役割: パネルが開いて項目が表示されるときに、登録されたコールバックを呼ぶ。
- 触るとき: パネルを開いたときの更新処理を変えるとき。
- 条件付き依存: `if (this._onShowingInPanel)` → `this._onShowingInPanel()`
- 参照: `this._onShowingInPanel`

## onSubviewPlaced()
- 位置: L1078-1082
- 役割: サブビューがパネルに追加されたときに、登録されたコールバックを呼ぶ。
- 触るとき: サブビューの初期化を変えるとき。
- 条件付き依存: `if (this._onSubviewPlaced)` → `this._onSubviewPlaced()`
- 参照: `this._onSubviewPlaced`

## onSubviewShowing()
- 位置: L1090-1094
- 役割: サブビューが表示されるときに、登録されたコールバックを呼ぶ。
- 触るとき: サブビューを開くときの準備を変えるとき。
- 条件付き依存: `if (this._onSubviewShowing)` → `this._onSubviewShowing()`
- 参照: `this._onSubviewShowing`

## onPinToUrlbarToggled()
- 位置: L1098-1102
- 役割: ピン留めの切り替え後に、登録されたコールバックを呼ぶ。
- 触るとき: ピン留めに連動する処理を追加するとき。
- 条件付き依存: `if (this._onPinToUrlbarToggled)` → `this._onPinToUrlbarToggled()`
- 参照: `this._onPinToUrlbarToggled`

## remove()
- 位置: L1112-1114
- 役割: アクションを全ウィンドウから取り除く。
- 触るとき: 拡張の終了時にボタンを消す処理を確かめるとき。
- 呼び出し先: `PageActions.onActionRemoved()`

## shouldShowInPanel()
- 位置: L1125-1141
- 役割: パネルに出すかを判定する。一時項目と拡張項目は、無効なら出さない。
- 触るとき: 無効な拡張項目がパネルに残る、または消える報告を調べるとき。プライベート制限も判定に入る。
- 呼び出し先: `this.canShowInWindow()`, `this.getDisabled()`
- 参照: `this.__transient`, `this.extensionID`

## shouldShowInUrlbar()
- 位置: L1151-1157
- 役割: アドレスバーに出すかを判定する。ピン留めされ、無効でなく、表示可能なウィンドウのとき真。
- 触るとき: アドレスバーのボタンが出ない条件を確かめるとき。
- 呼び出し先: `this.canShowInWindow()`, `this.getDisabled()`
- 参照: `this.pinnedToUrlbar`

## _isBuiltIn()
- 位置: L1159-1164
- 役割: 組み込みアクション(スクリーンショットを含む)かを判定する。
- 触るとき: 組み込みと拡張の扱いを分けるとき。
- 呼び出し先: `["screenshots_mozilla_org"].concat()`, `builtInIDs.includes()`, `gBuiltInActions.filter()`, `gBuiltInActions.filter(a => !a.__isSeparator).map()`
- 参照: `a.__isSeparator`, `a.id`, `this.id`

## _isMozillaAction()
- 位置: L1166-1168
- 役割: Mozilla 提供のアクション(組み込みと Web 互換性報告)かを判定する。
- 触るとき: Mozilla 提供の項目だけに別の扱いをするとき。
- 参照: `this._isBuiltIn`, `this.id`

## PageActions._initBuiltInActions()
- 位置: L1188-1204
- 役割: 組み込みアクションの定義一覧を作る。現在はブックマーク1件だけ。
- 触るとき: 組み込みアクションを追加するとき。並び順はパネルの表示順になり、テレメトリの定義も合わせて変える必要がある。

## onShowingInPanel()
- 位置: L1196-1198
- 役割: ブックマークのパネル項目が表示されるときに、ブックマーク側の処理へ渡す。
- 触るとき: ブックマーク項目のパネル表示を変えるとき。
- 呼び出し先: `browserPageActions()`, `browserPageActions(buttonNode).bookmark.onShowingInPanel()`

## onCommand()
- 位置: L1199-1201
- 役割: ブックマーク項目のクリックを、ブックマーク側の処理へ渡す。
- 触るとき: ブックマーク項目の操作が効かない報告を調べるとき。
- 呼び出し先: `browserPageActions()`, `browserPageActions(buttonNode).bookmark.onCommand()`

## browserPageActions()
- 位置: L1214-1219
- 役割: ノードかウィンドウから、そのウィンドウの BrowserPageActions を返す。
- 触るとき: ノードから対応するウィンドウの管理オブジェクトを引く箇所を確かめるとき。
- 参照: `obj.BrowserPageActions`, `obj.documentGlobal.BrowserPageActions`

## allBrowserWindows()
- 位置: L1230-1236
- 役割: 指定ウィンドウ、または全ての通常ウィンドウを順に返す。
- 触るとき: 全ウィンドウへの一斉反映の範囲を変えるとき。
- 呼び出し先: `Services.wm.getEnumerator()`
- XPCOM: `Services.wm`

## allBrowserPageActions()
- 位置: L1245-1249
- 役割: 対象の各ウィンドウの BrowserPageActions を順に返す。
- 触るとき: ウィンドウごとの配置更新の対象を変えるとき。
- 呼び出し先: `allBrowserWindows()`, `browserPageActions()`

## setProperties()
- 位置: L1266-1289
- 役割: スキーマに従ってオプションを対応するプロパティへ設定し、必須の欠落と未知の項目を例外にする。
- 触るとき: Action に受け付けるオプションを増やすとき。_ で始まる名前は内部用としてそのまま入る。
