# browser/components/aiwindow/ui/modules/AutoTabGroupingSuggestions.sys.mjs

source: browser/components/aiwindow/ui/modules/AutoTabGroupingSuggestions.sys.mjs
source-hash: 757b543529c54ba534da08d33abb06e5bb6cd9b3
lines: 432

## <module>
- 役割: Organize Tabs の候補生成を担う。オンデバイスのクラスタリングとグループ名の付与を呼び、パネルに出す提案データを作る。DOM は扱わない。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`, `console.createInstance()`, `parseFloat()`

## normalizeLabel()
- 位置: L110-112
- 役割: グループ名の前後の空白を除き、小文字に変えて比較用の形にする。
- 触るとき: グループ名の重複判定を変えるとき。
- 呼び出し先: `label.trim()`, `label.trim().toLocaleLowerCase()`

## isAvailable()
- 位置: L145-151
- 役割: オンデバイス ML が有効で、地域判定を通り、メモリも足りるときに true を返す。Smart Window の opt-in は見ない。
- 触るとき: Organize Tabs のボタンを出すかどうかの条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.SmartTabGroupingManager.isAllowed`, `this.hasEnoughMemory`
- XPCOM: `Services.prefs`

## hasEnoughMemory()
- 位置: L159-165
- 役割: メモリ確認が無効か、物理メモリが最小値以上なら true を返す。
- 触るとき: メモリ不足時にボタンを止める閾値を変えるとき。
- 参照: `lazy.checkForMemory`, `lazy.minimumPhysicalMemoryGiB`, `lazy.mlUtils.totalPhysicalMemory`

## manager()
- 位置: L167-175
- 役割: Smart Window 用の設定で SmartTabGroupingManager を初回だけ作り、以後は同じものを返す。
- 触るとき: 使うモデルの feature id や engine id を変えるとき。
- 条件付き依存: `if (!this._manager)` → `structuredClone()`
- 参照: `config.topicGeneration.engineId`, `config.topicGeneration.featureId`, `lazy.SMART_TAB_GROUPING_CONFIG`, `lazy.SmartTabGroupingManager`, `this._manager`

## preloadModels()
- 位置: L189-197
- 役割: モデルを事前に取得する。事前読み込みが無効か利用できなければ何もせず、2回目以降は同じ Promise を返す。
- 触るとき: モデルの取得をいつ、どの条件で行うかを変えるとき。
- 条件付き依存: `if (!lazy.preloadEnabled || !this.isAvailable)` → `Promise.resolve()`
- 条件付き依存: `if (!this._preloadPromise)` → `this._preloadModels()`
- 参照: `lazy.preloadEnabled`, `this._preloadPromise`, `this.isAvailable`

## _preloadModels()
- 位置: async L199-205
- 役割: manager.preloadAllModels を呼ぶ。失敗したら警告を出すだけで例外は外に出さない。
- 触るとき: モデル取得に失敗したときの扱いを変えるとき。
- 呼び出し先: `lazy.console.warn()`, `this.manager.preloadAllModels()`

## getCandidateTabs()
- 位置: L215-228
- 役割: ピン留め、グループ済み、非表示、読み込み中、ラベルなしのタブを除き、http と https のタブだけを候補にする。
- 触るとき: グループ候補に入るタブの条件を変えるとき。
- 呼び出し先: `tab.hasAttribute()`, `uri.schemeIs()`, `win.gBrowser.tabs.filter()`
- 参照: `tab.closing`, `tab.group`, `tab.hidden`, `tab.label`, `tab.linkedBrowser?.currentURI`, `tab.pinned`

## buildProposals()
- 位置: async L238-270
- 役割: 候補をクラスタリングし、各グループに名前を並列で付け、名前が空のものを外し、既存のグループ名と重ならない形で返す。
- 触るとき: 提案の数や名前の付き方、既存グループとの衝突の扱いを変えるとき。
- 呼び出し先: `Promise.all()`, `candidates.filter()`, `clusters.flatMap()`, `clusters.map()`, `groupedTabs.has()`, `label?.trim()`, `labeled .filter()`, `labeled .filter(proposal => proposal.label) .map()`, `lazy.console.warn()`, `takenLabels.map()`, `this._labelForGroup()`, `this.manager.generateClusters()`, `this.selectClusters()`, `this.uniqueLabel()`
- 参照: `c.tabs`, `cluster.tabs`, `clusters.length`, `proposal.label`, `result?.clusterRepresentations`

## uniqueLabel()
- 位置: L278-285
- 役割: 使用中の名前と重なるなら「名前 2」「名前 3」のように番号を付け、選んだ名前を使用済みに加える。
- 触るとき: 重複したグループ名の表記を変えるとき。
- 呼び出し先: `normalizeLabel()`, `taken.add()`, `taken.has()`

## _labelForGroup()
- 位置: async L294-316
- 役割: タブの URL から作ったキーで名前を探し、無ければ LLM で付け、LLM が失敗したらオンデバイスで付ける。結果は50件まで保持する。
- 触るとき: グループ名の取得元の順序やキャッシュの扱いを変えるとき。
- 呼び出し先: `lazy.console.warn()`, `tabs .map()`, `tabs .map(t => t.linkedBrowser?.currentURI?.spec ?? "") .sort()`, `tabs .map(t => t.linkedBrowser?.currentURI?.spec ?? "") .sort() .join()`, `this._labelCache.has()`, `this._labelCache.set()`, `this._llmLabelForGroup()`, `this.manager.getPredictedLabelForGroup()`
- 条件付き依存: `if (this._labelCache.has(key))` → `this._labelCache.get()`
- 条件付き依存: `if (this._labelCache.size >= MAX_LABEL_CACHE_ENTRIES)` → `this._labelCache.delete()`
- 条件付き依存: `if (this._labelCache.size >= MAX_LABEL_CACHE_ENTRIES)` → `this._labelCache.keys().next()`
- 条件付き依存: `if (this._labelCache.size >= MAX_LABEL_CACHE_ENTRIES)` → `this._labelCache.keys()`
- 参照: `t.linkedBrowser?.currentURI?.spec`, `this._labelCache.keys().next().value`, `this._labelCache.size`

## _llmLabelForGroup()
- 位置: async L320-358
- 役割: アカウントのトークンでグループ名付けの LLM を呼び、タイトルを最大10件渡す。結果は25字以内に切り、末尾の and や or などを落とす。トークンが無ければ例外にする。
- 触るとき: LLM に渡すタイトルの量、名前の長さや整形の規則を変えるとき。
- 呼び出し先: `Promise.all()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `label.replace()`, `label.replace(/\s+(and|or|&)$/i, "").trim()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `lazy.openAIEngine.getFxAccountToken()`, `lazy.renderPrompt()`, `lazy.sanitizeUntrustedContent()`, `lazy.sanitizeUntrustedContent(raw, true).trim()`, `response?.finalOutput?.trim()`, `tabs .slice()`, `tabs .slice(0, MAX_LABEL_TABS) .map()`, `tabs .slice(0, MAX_LABEL_TABS) .map(tab => lazy.sanitizeUntrustedContent(tab.label || "")) .filter()`, `tabs .slice(0, MAX_LABEL_TABS) .map(tab => lazy.sanitizeUntrustedContent(tab.label || "")) .filter(Boolean) .join()`
- 条件付き依存: `if (label.length > MAX_LABEL_LENGTH)` → `label.slice()`
- 条件付き依存: `if (label.length > MAX_LABEL_LENGTH)` → `cut.lastIndexOf()`
- 条件付き依存: `if (label.length > MAX_LABEL_LENGTH)` → `cut.slice()`
- 参照: `conversation.engine.model`, `label.length`, `lazy.MODEL_FEATURES.TAB_GROUP_NAMING`, `tab.label`

## selectClusters()
- 位置: L368-381
- 役割: タブ数が最小以上で凝集度が閾値以上のクラスターを、タブ数の多い順に最大 maxGroups 件まで残す。
- 触るとき: 提案するグループの件数や、凝集度の閾値を変えるとき。
- 呼び出し先: `clusterRepresentations .filter()`
- 参照: `a.tabs.length`, `b.tabs.length`, `c.cohesion`, `c.tabs`, `c.tabs.length`, `clusterRepresentations?.length`, `lazy.maxGroups`, `lazy.minCohesion`, `lazy.minTabsPerGroup`

## toSuggestionData()
- 位置: L392-399
- 役割: 提案に色(順番に循環して割り当て)とタブごとの表示データを付け、パネル用の形にする。
- 触るとき: グループの色の割り当てや、パネルの行データを変えるとき。
- 呼び出し先: `proposal.tabs.map()`, `this.toTabInfo()`
- 参照: `TAB_GROUP_COLORS.length`, `proposal.label`, `proposal.tabs`

## toTabInfo()
- 位置: L407-421
- 役割: タブの表示名(タイトル、無ければ基底ドメイン)とファビコンの URL を返す。
- 触るとき: 候補行に出るタブ名の表記を変えるとき。
- 呼び出し先: `this._faviconUrl()`
- 条件付き依存: `if (uri)` → `lazy.BrowserUtils.formatURIForDisplay()`
- 参照: `tab.label`, `tab.linkedBrowser?.currentURI`

## _faviconUrl()
- 位置: L423-430
- 役割: ファビコンの URL を決める。http のページやアイコンが無いタブは page-icon 形式、それ以外は取得済みのアイコンか既定のアイコンを使う。
- 触るとき: 候補行のアイコンが出ない不具合を調べるとき。
- 呼び出し先: `icon.startsWith()`
- 参照: `tab.linkedBrowser?.currentURI`, `tab.linkedBrowser?.mIconURL`, `uri.spec`
