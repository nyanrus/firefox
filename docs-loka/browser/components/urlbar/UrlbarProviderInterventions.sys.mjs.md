# browser/components/urlbar/UrlbarProviderInterventions.sys.mjs

source: browser/components/urlbar/UrlbarProviderInterventions.sys.mjs
source-hash: 5ddd82ec5962df1d7b39637a0d752e52b4551048
lines: 777

## <module>
- 役割: 英語の検索語が「ブラウザを消す」「リフレッシュ」「更新」に関係するとき、その場で解決できる案内(Tip)を URL バーに出すプロファイル系プロバイダー。文字列の編集距離で語句を照合する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.declareLazy()`

## Node.constructor()
- 位置: L110-114
- 役割: フレーズ木の 1 ノードを作る。単語、所属する文書の集合、子ノードの対応表を持つ。
- 触るとき: フレーズ木の構造(子の持ち方)を変えるとき。
- 参照: `this.childrenByWord`, `this.documents`, `this.word`

## QueryScorer.constructor()
- 位置: L158-163
- 役割: 編集距離の閾値(既定 1)と言い換え表(variations)を受け取り、空のフレーズ木を作る。
- 触るとき: 照合の許容差や言い換えの仕組みを変えるとき。
- 参照: `this._distanceThreshold`, `this._documents`, `this._rootNode`, `this._variations`

## QueryScorer.addDocument()
- 位置: L175-204
- 役割: 文書のフレーズを小文字の単語列に分け、言い換えを加えた各フレーズをフレーズ木に登録する。
- 触るとき: Tip の検索語を追加したり、言い換えが効かない原因を調べるとき。
- 呼び出し先: `phrase.indexOf()`, `phraseStr .trim()`, `phraseStr .trim() .split()`, `phraseStr .trim() .split(/\s+/) .map()`, `this._buildPhraseTree()`, `this._documents.add()`, `word.toLocaleLowerCase()`
- 条件付き依存: `if (index >= 0)` → `Array.from()`
- 条件付き依存: `if (index >= 0)` → `variationPhrase.splice()`
- 条件付き依存: `if (index >= 0)` → `variation.split()`
- 条件付き依存: `if (index >= 0)` → `phrases.push()`
- 参照: `doc.phrases`, `this._rootNode`, `this._variations`

## QueryScorer.score()
- 位置: L217-233
- 役割: 検索語を単語に分けてフレーズ木を辿り、各文書の最小編集距離を求めて昇順で返す。一致しない文書は Infinity になる。
- 触るとき: Tip の一致度の計算結果を確認したり、スコアの並べ方を変えるとき。
- 呼び出し先: `minDistanceByDoc.get()`, `queryString .trim()`, `queryString .trim() .split()`, `queryString .trim() .split(/\s+/) .map()`, `results.push()`, `results.sort()`, `this._traverse()`, `word.toLocaleLowerCase()`
- 参照: `a.score`, `b.score`, `this._documents`

## QueryScorer._buildPhraseTree()
- 位置: L258-274
- 役割: フレーズの単語を順にたどり、無いノードを作って文書を紐付ける再帰処理。
- 触るとき: フレーズ木への登録規則(接頭辞の共有など)を変えるとき。
- 呼び出し先: `child.documents.add()`, `node.childrenByWord.get()`, `phrase[wordIndex].toLocaleLowerCase()`, `this._buildPhraseTree()`
- 条件付き依存: `if (!child)` → `node.childrenByWord.set()`
- 参照: `phrase.length`

## QueryScorer._traverse()
- 位置: L296-347
- 役割: 検索語の各単語をフレーズ木の子と編集距離で比べ、閾値以内なら再帰的に進む。葉に達したら距離を文書ごとに記録する。
- 触るとき: 語句の一致判定(閾値、語数の違い)を変えるとき。
- 呼び出し先: `lazy.NLP.levenshtein()`
- 条件付き依存: `if (!node.childrenByWord.size)` → `minDistanceByDoc.set()`
- 条件付き依存: `if (!node.childrenByWord.size)` → `Math.min()`
- 条件付き依存: `if (!node.childrenByWord.size)` → `minDistanceByDoc.has()`
- 条件付き依存: `if (!node.childrenByWord.size)` → `minDistanceByDoc.get()`
- 条件付き依存: `if (distance <= this._distanceThreshold)` → `this._traverse()`
- 参照: `node.childrenByWord`, `node.childrenByWord.size`, `node.documents`, `queryWords.length`, `this._distanceThreshold`, `this._rootNode`

## getPayloadForTip()
- 位置: L356-398
- 役割: Tip の種類ごとに、タイトル(l10n ID)、ボタン、ヘルプ URL(app.support.baseURL 由来)を返す。未知の種類は例外にする。
- 触るとき: Tip の文言やボタン、ヘルプ先を変えるとき。新しい Tip 種別を足すときもここに追加する。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- 参照: `UrlbarShared.INTERVENTION_TIP_TYPE.CLEAR`, `UrlbarShared.INTERVENTION_TIP_TYPE.REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_ASK`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_RESTART`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_WEB`
- XPCOM: `Services.urlFormatter`

## queryScorer()
- 位置: L407-422
- 役割: Tip 用の QueryScorer を遅延生成し、文書を登録する。firefox の言い換え(fire fox など)と mozilla の誤字(mozila)を登録する。
- 触るとき: Tip に効く言い換えや誤字の扱いを増やすとき。
- 呼び出し先: `Object.entries()`, `queryScorer.addDocument()`

## UrlbarProviderInterventions.type()
- 位置: L435-437
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: Tip 結果の種別と並び順を確認するとき。
- 参照: `UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderInterventions.isActive()
- 位置: async L446-498
- 役割: 英語ロケールで、検索語があり長すぎず、URL 風でなく、ポリシーで許可され、GlobalActions が有効でない場合に、スコアの最も高い文書を調べて現在の Tip を決める。update 文書が一致すれば更新系の処理へ、clear なら非プライベート時に消去の Tip、refresh なら初期化の Tip を選ぶ。
- 触るとき: どの検索語で Tip が出るか、優先順位(update が clear と refresh より優先)、プライベートでの抑止を変えるとき。
- 呼び出し先: `EN_LOCALE_MATCH.test()`, `Services.policies.isAllowed()`, `UrlbarProviderInterventions.lazy.queryScorer.score()`, `lazy.UrlUtils.REGEXP_LIKE_PROTOCOL.test()`, `this.queryInstance .getProvider()`, `this.queryInstance .getProvider(lazy.UrlbarProviderGlobalActions.name) ?.isActive()`, `topDocIDs.has()`
- 条件付き依存: `if (topDocScore.score != Infinity)` → `topDocIDs.add()`
- 条件付き依存: `if (topDocIDs.has("update"))` → `this._setCurrentTipFromAppUpdaterStatus()`
- 条件付き依存: `if (!(topDocIDs.has("update")))` → `topDocIDs.has()`
- 条件付き依存: `if (topDocIDs.has("clear"))` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (topDocIDs.has("clear"))` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!(topDocIDs.has("clear")))` → `topDocIDs.has()`
- 参照: `Services.locale.appLocaleAsBCP47`, `UrlbarShared.INTERVENTION_TIP_TYPE.CLEAR`, `UrlbarShared.INTERVENTION_TIP_TYPE.NONE`, `UrlbarShared.INTERVENTION_TIP_TYPE.REFRESH`, `UrlbarShared.MAX_TEXT_LENGTH`, `document.id`, `lazy.UrlbarProviderGlobalActions.name`, `queryContext.searchString`, `queryContext.searchString.length`, `this.currentTip`, `topDocScore.score`
- XPCOM: `Services.locale` / `Services.policies`

## UrlbarProviderInterventions._setCurrentTipFromAppUpdaterStatus()
- 位置: async L500-549
- 役割: 約 12 時間に一度アップデート確認を行い、その状態(再起動待ち、ダウンロード可、最新、確認中、更新不可など)に応じて現在の更新 Tip を決める。確認に失敗したら何もしない。
- 触るとき: 更新 Tip の種類と、アップデート状態との対応を変えるとき。
- 呼び出し先: `UrlbarProviderInterventions.checkForBrowserUpdate()`
- 参照: `UrlbarShared.INTERVENTION_TIP_TYPE.NONE`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_ASK`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_RESTART`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_WEB`, `lazy.AppUpdater.STATUS.CHECKING`, `lazy.AppUpdater.STATUS.DOWNLOAD_AND_INSTALL`, `lazy.AppUpdater.STATUS.NO_UPDATER`, `lazy.AppUpdater.STATUS.NO_UPDATES_FOUND`, `lazy.AppUpdater.STATUS.READY_FOR_RESTART`, `lazy.AppUpdater.STATUS.UPDATE_DISABLED_BY_POLICY`, `lazy.appUpdater.status`, `this.currentTip`

## UrlbarProviderInterventions.startQuery()
- 位置: async L558-622
- 役割: 現在の Tip が「確認中」なら、アップデータの確認完了を待ってから Tip を決め直す。最後に Tip の結果(提案位置 1、ヘルプ付き)を追加する。
- 触るとき: 更新確認中の表示の待ち方や、Tip 結果の見た目(アイコン、ヘルプ文言)を変えるとき。
- 呼び出し先: `addCallback()`, `getPayloadForTip()`
- 条件付き依存: `if (this.currentTip == UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING)` → `this._setCurrentTipFromAppUpdaterStatus()`
- 条件付き依存: `if ( this.currentTip == UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING )` → `lazy.appUpdater.addListener()`
- 条件付き依存: `if ( this.currentTip == UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING )` → `this._setCurrentTipFromAppUpdaterStatus()`
- 参照: `UrlbarShared.ICON.TIP`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING`, `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.TIP`, `lazy.UrlbarResult`, `this._appUpdaterListener`, `this.currentTip`, `this.queryInstance`

## this._appUpdaterListener()
- 位置: L583-587
- 役割: アップデータの状態変化を受けて、自分自身を外し、待機中の Promise を解決する一時的なリスナー。
- 触るとき: 更新確認の完了待ちが終わらない、またはクエリ取り消し後にリスナーが残る問題を調べるとき。
- 呼び出し先: `lazy.appUpdater.removeListener()`, `resolve()`
- 参照: `this._appUpdaterListener`

## UrlbarProviderInterventions.cancelQuery()
- 位置: L627-634
- 役割: 待機中のアップデータのリスナーがあれば外す。
- 触るとき: 入力が変わったときに更新確認の待ちを止める挙動を調べるとき。
- 条件付き依存: `if (this._appUpdaterListener)` → `lazy.appUpdater.removeListener()`
- 参照: `this._appUpdaterListener`

## UrlbarProviderInterventions.#pickResult()
- 位置: L636-660
- 役割: Tip の種類に応じて動作を実行する。消去は履歴消去ダイアログ、初期化はプロファイルリセット、更新はダウンロードして再起動、再起動は再起動、Web 更新は公式ダウンロードページを新しいタブで開く。
- 触るとき: Tip のボタンを押した後の動作を変えるとき。
- 呼び出し先: `installBrowserUpdateAndRestart()`, `openClearHistoryDialog()`, `resetBrowser()`, `restartBrowser()`, `window.gBrowser.addWebTab()`
- 参照: `UrlbarShared.INTERVENTION_TIP_TYPE.CLEAR`, `UrlbarShared.INTERVENTION_TIP_TYPE.REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_ASK`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_RESTART`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_WEB`, `result.payload.type`, `window.gBrowser.selectedTab`

## UrlbarProviderInterventions.onEngagement()
- 位置: L667-675
- 役割: selType が tip(メインボタン)のときだけ、その結果の動作を実行する。ヘルプの操作は UrlbarInput 側に任せる。
- 触るとき: Tip の操作を選んだときの振り分けを変えるとき。
- 条件付き依存: `if (details.selType == "tip")` → `this.#pickResult()`
- 参照: `controller.browserWindow`, `details.result`, `details.selType`

## UrlbarProviderInterventions.checkForBrowserUpdate()
- 位置: L685-695
- 役割: 強制指定がなければ前回確認から 12 時間を過ぎたときだけ、アップデータの確認を開始する。
- 触るとき: アップデート確認の頻度や、強制確認の扱いを変えるとき。
- 呼び出し先: `Date.now()`
- 条件付き依存: `if ( force || !UrlbarProviderInterventions._lastUpdateCheckTime || Date.now() - UrlbarProviderInterventions._lastUpdateCheckTime >= UPDATE_CHECK_PERIOD_MS )` → `Date.now()`
- 条件付き依存: `if ( force || !UrlbarProviderInterventions._lastUpdateCheckTime || Date.now() - UrlbarProviderInterventions._lastUpdateCheckTime >= UPDATE_CHECK_PERIOD_MS )` → `lazy.appUpdater.check()`
- 参照: `UrlbarProviderInterventions._lastUpdateCheckTime`

## UrlbarProviderInterventions.resetAppUpdater()
- 位置: L701-706
- 役割: アップデータの遅延取得が済んでいれば、新しいアップデータに差し替える(テスト用)。
- 触るとき: テストでアップデータの状態をリセットしたいとき。
- 呼び出し先: `Object.getOwnPropertyDescriptor()`
- 参照: `Object.getOwnPropertyDescriptor(lazy, "appUpdater").get`, `lazy.AppUpdater`, `lazy.appUpdater`

## installBrowserUpdateAndRestart()
- 位置: L713-736
- 役割: ダウンロード可の状態ならダウンロードを許可し、完了(再起動待ち)なら再起動し、失敗ならそのまま終える。
- 触るとき: 更新のダウンロードから再起動までの流れを変えるとき。
- 呼び出し先: `lazy.appUpdater.addListener()`, `lazy.appUpdater.allowUpdateDownload()`
- 条件付き依存: `if (lazy.appUpdater.status != lazy.AppUpdater.STATUS.DOWNLOAD_AND_INSTALL)` → `Promise.resolve()`
- 参照: `lazy.AppUpdater.STATUS.DOWNLOAD_AND_INSTALL`, `lazy.appUpdater.status`

## listener()
- 位置: L718-732
- 役割: アップデータの状態が再起動待ちか失敗になったら、リスナーを外し、再起動が必要なら再起動して Promise を解決する。
- 触るとき: ダウンロード後の状態遷移への応答を変えるとき。
- 呼び出し先: `lazy.appUpdater.removeListener()`, `resolve()`
- 条件付き依存: `if (lazy.appUpdater.status == lazy.AppUpdater.STATUS.READY_FOR_RESTART)` → `restartBrowser()`
- 参照: `lazy.AppUpdater.STATUS.DOWNLOAD_FAILED`, `lazy.AppUpdater.STATUS.READY_FOR_RESTART`, `lazy.appUpdater.status`

## openClearHistoryDialog()
- 位置: L738-745
- 役割: プライベートウィンドウでは何もせず、それ以外は履歴消去の UI を開く。
- 触るとき: 消去 Tip の開き方や、プライベート時の抑止を変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.Sanitizer.showUI()`

## restartBrowser()
- 位置: L747-769
- 役割: 終了要求を通知して、取り消されなければ(セーフモードなら安全モードで)ブラウザを再起動する。
- 触るとき: 再起動の挙動(終了の取り消し、セーフモード)を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.startup.restartInSafeMode()`
- 条件付き依存: `if (!(Services.appinfo.inSafeMode))` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `Ci.nsISupportsPRBool`, `Services.appinfo.inSafeMode`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.appinfo` / `Services.obs` / `Services.startup`

## resetBrowser()
- 位置: L771-776
- 役割: プロファイルリセットがサポートされていれば確認ダイアログを開く。
- 触るとき: 初期化 Tip の確認画面の表示条件を変えるとき。
- 呼び出し先: `lazy.ResetProfile.openConfirmationDialog()`, `lazy.ResetProfile.resetSupported()`
