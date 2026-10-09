# browser/components/urlbar/UrlbarProviderSemanticHistorySearch.sys.mjs

source: browser/components/urlbar/UrlbarProviderSemanticHistorySearch.sys.mjs
source-hash: d3d6a9490a6308ff7a4a2687c404aa9c32f9a489
lines: 287

## <module>
- 役割: 履歴を埋め込みベクトルの類似度で検索し、結果を履歴 URL または開いているタブへの切り替えとして出す UrlbarProviderSemanticHistorySearch を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.prefs.getFloatPref()`, `getPlacesSemanticHistoryManager()`, `lazy.UrlbarShared.getLogger()`

## UrlbarProviderSemanticHistorySearch.semanticManager()
- 位置: L78-80
- 役割: 共有の PlacesSemanticHistoryManager を返す静的ゲッターで、遅延生成された lazy.semanticManager をそのまま渡す。
- 触るとき: 他の利用者が別のパラメータで初期化してしまわないよう、マネージャーの取得先をこの一箇所に保ちたいとき見る。
- 参照: `lazy.semanticManager`

## UrlbarProviderSemanticHistorySearch.type()
- 位置: L85-87
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: 意味検索の結果を他の履歴結果とどう混ぜるかを変えるとき見る。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderSemanticHistorySearch.isActive()
- 位置: async L95-121
- 役割: 履歴検索が有効で入力長が最小長以上のとき、サーフェスに応じたゲート(smartbar は SW 側、それ以外は CW 側)を確かめ、埋め込みの件数が十分なら有効にする。
- 触るとき: 意味検索が出ない原因を調べるとき、入力長、ゲート、埋め込みの件数のどれで弾かれているかを確かめる。smartbar の扱いを変えるときもここを見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 条件付き依存: `if (canUse)` → `lazy.semanticManager.hasSufficientEntriesForSearching()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.semanticManager.canUseSemanticSearch`, `lazy.semanticManager.isEnabledForSmartWindow`, `queryContext.sapName`, `queryContext.searchMode?.source`, `queryContext.searchString.length`

## UrlbarProviderSemanticHistorySearch.startQuery()
- 位置: async L130-169
- 役割: 意味推論の結果を取得して exposure を記録し、開いているタブと一致するものは切り替え結果に、それ以外は履歴の URL 結果として追加する。
- 触るとき: 意味検索の結果件数や、タブ切り替えへの振り分けを変えるとき見る。
- 呼び出し先: `lazy.UrlbarProviderOpenTabs.getOpenTabUrls()`, `lazy.semanticManager.infer()`, `openTabs.get()`, `this.#addAsSwitchToTab()`, `this.#maybeRecordExposure()`
- 条件付き依存: `if ( !this.#addAsSwitchToTab( openTabs.get(res.url), queryContext, res, addCallback ) )` → `lazy.UrlbarShared.getIconForUrl()`
- 条件付き依存: `if ( !this.#addAsSwitchToTab( openTabs.get(res.url), queryContext, res, addCallback ) )` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if ( !this.#addAsSwitchToTab( openTabs.get(res.url), queryContext, res, addCallback ) )` → `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.isPrivate`, `res.frecency`, `res.title`, `res.url`, `resultObject.results`, `this.queryInstance`
- XPCOM: `Services.urlFormatter`

## UrlbarProviderSemanticHistorySearch.#addAsSwitchToTab()
- 位置: L185-224
- 役割: 開いているタブ(同じ URL)の各コンテナー・タブグループについて TAB_SWITCH 結果を追加し、現在のページ自身は除外する。追加したかどうかを返す。
- 触るとき: 同じページを複数タブで開いているときの表示や、現在のページを候補から外す条件を確かめるとき見る。
- 呼び出し先: `UrlbarUtils.createTabSwitchSecondaryAction()`, `UrlbarUtils.getUserContextData()`, `addCallback()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `openTabs?.size`, `queryContext.currentPage`, `queryContext.isPrivate`, `queryContext.tabGroup`, `queryContext.userContextId`, `res.lastVisit`, `res.title`, `res.url`

## UrlbarProviderSemanticHistorySearch.#maybeRecordExposure()
- 位置: L230-262
- 役割: Nimbus の実験またはロールアウトに参加しているときに限り、exposure イベントを一度だけ送って以後は送らない。
- 触るとき: 意味検索の実験の露出計測が重複する、または送られない問題を調べるとき見る。
- 呼び出し先: `lazy.NimbusFeatures.urlbar.getEnrollmentMetadata()`, `lazy.NimbusFeatures.urlbar.recordExposureEvent()`, `lazy.logger.debug()`, `lazy.logger.warn()`
- 参照: `UrlbarProviderSemanticHistorySearch.#exposureRecorded`, `lazy.EnrollmentType.EXPERIMENT`, `lazy.EnrollmentType.ROLLOUT`, `metadata.slug`, `metadata?.slug`

## UrlbarProviderSemanticHistorySearch.getPriority()
- 位置: L269-271
- 役割: プロバイダーの優先度として 0 を返す。
- 触るとき: 意味検索結果を他の候補より前後させたいとき、この値を見直す。

## UrlbarProviderSemanticHistorySearch.onEngagement()
- 位置: L278-285
- 役割: 結果が dismiss された場合に、その URL を Places の履歴から削除し、結果も画面から取り除く。
- 触るとき: 候補の削除操作の挙動を変えるとき、または削除しても履歴が残る問題を調べるときに見る。
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history.remove(result.payload.url).catch()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 参照: `console.error`, `details.selType`, `result.payload.url`
