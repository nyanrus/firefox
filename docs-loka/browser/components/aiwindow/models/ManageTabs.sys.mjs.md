# browser/components/aiwindow/models/ManageTabs.sys.mjs

source: browser/components/aiwindow/models/ManageTabs.sys.mjs
source-hash: cc9b8299d2f7fb8bcc1cebe2eb79bc1851b889bb
lines: 467

## <module>
- 役割: AI ウィンドウの「タブを閉じる」「タブをグループ化する」操作を実行するモジュール。対象タブの収集、確認カードの要否判定、実行、結果の整形を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## findMatchingAIWindowTabs()
- 位置: L39-59
- 役割: AI ウィンドウが有効な窓を順に見て、URL が対象集合に入るタブを集める。最前面の AI 窓も返す。
- 触るとき: 操作対象になるタブの探し方(窓の条件や URL の照合)を変えるとき。
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `validUrls.has()`
- 条件付き依存: `if (validUrls.has(url))` → `matchedTabs.push()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser?.currentURI?.spec`, `tab.linkedPanel`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## shouldRequireUserConfirmation()
- 位置: L71-93
- 役割: 信頼できない入力があるか、ピン留め・選択中のタブを含むか、最前面の窓のタブを全部含むかで、確認カードが必要かを判定する。
- 触るとき: タブ操作で確認を出す条件を変えるとき。確認なし実行の安全側の境界なので注意。
- 呼び出し先: `tabs.some()`
- 条件付き依存: `if (topAIWin)` → `tabs.filter(({ win }) => win === topAIWin).map()`
- 条件付き依存: `if (topAIWin)` → `tabs.filter()`
- 条件付き依存: `if (topAIWin)` → `topAIWin.gBrowser.tabs.every()`
- 条件付き依存: `if (topAIWin)` → `topWinTabs.has()`
- 参照: `securityProperties?.untrustedInput`, `tab.pinned`, `topWinTabs.size`, `win.gBrowser.selectedTab`

## runManageTabsFlow()
- 位置: async L101-193
- 役割: 対象タブを集め、グループ化なら提案タブを足し、確認が必要ならカードを返して保留、不要なら即実行して結果とテレメトリを記録する。
- 触るとき: タブ操作の全体の流れ(確認、実行、失敗時の返却)を変えるとき。
- 呼び出し先: `Date.now()`, `gatherTabs()`, `lazy.ToolUITelemetry.recordBrowserActionComplete()`, `shouldRequireUserConfirmation()`, `toolHandler.getToolResults()`, `toolHandler.takeUIAction()`
- 条件付き依存: `if (toolHandler.action === GROUP_TABS)` → `offerChatTab()`
- 条件付き依存: `if ( state.askConfirmation || shouldRequireUserConfirmation( gatheredResult.matchedTabs, gatheredResult.topAIWin, state.conversation.securityProperties ) )` → `lazy.ToolUI.registerTabKeys()`
- 条件付き依存: `if ( state.askConfirmation || shouldRequireUserConfirmation( gatheredResult.matchedTabs, gatheredResult.topAIWin, state.conversation.securityProperties ) )` → `state.conversation.stashPendingBrowserActionTelemetry()`
- 条件付き依存: `if ( state.askConfirmation || shouldRequireUserConfirmation( gatheredResult.matchedTabs, gatheredResult.topAIWin, state.conversation.securityProperties ) )` → `toolHandler.getConfirmationProperties()`
- 条件付き依存: `if (!result || !result.operationIds?.length)` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 参照: `gatheredResult.earlyResult`, `gatheredResult.matchedTabs`, `gatheredResult.summarizedTabInfo`, `gatheredResult.tabKeyByToken`, `gatheredResult.tabs`, `gatheredResult.topAIWin`, `result.operationIds`, `result.operationIds?.length`, `state.askConfirmation`, `state.baseTelemetryInfo`, `state.conversation`, `state.conversation.securityProperties`, `state.toolCallId`, `state.validUrls`, `telemetryValues.affectedCount`, `telemetryValues.failedCount`, `telemetryValues.telemetryResult`, `toolHandler.action`, `toolHandler.failureError`, `toolHandler.failureMessage`, `toolHandler.verb`

## offerChatTab()
- 位置: L206-227
- 役割: AI チャットを表示しているタブを、グループ化の確認カードの候補に 1 行として追加する。ただし matchedTabs には入れない。
- 触るとき: グループ化の候補に何を含めるかを変えるとき。チャットのタブを既定で選ばせない点に注意。
- 呼び出し先: `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `gathered.tabKeyByToken.set()`, `gathered.tabs.push()`, `lazy.ToolUI.findChatTab()`, `sanitizeUntrustedContent()`
- 参照: `chatTab.documentGlobal?.gBrowser?.selectedTab`, `chatTab.label`, `chatTab.linkedBrowser?.currentURI?.spec`, `chatTab.permanentKey`, `chatTab.pinned`, `chatTab.userContextId`, `conversation?.id`
- XPCOM: `Services.uuid`

## gatherTabs()
- 位置: async L229-279
- 役割: 一致するタブを、トークン・URL・タイトル・選択状態などの行に整え、モデルへ渡す要約と照合用の対応表を作る。一致が無ければ早期結果を返す。
- 触るとき: 確認カードやモデルに渡すタブ情報の項目を増やすとき。
- 呼び出し先: `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `findMatchingAIWindowTabs()`, `matchedTabs.map()`, `sanitizeUntrustedContent()`, `tabKeyByToken.set()`, `tabs.map()`
- 条件付き依存: `if (!matchedTabs.length)` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 参照: `matchedTabs.length`, `tab.label`, `tab.permanentKey`, `tab.pinned`, `tab.userContextId`, `win.gBrowser.selectedTab`
- XPCOM: `Services.uuid`

## takeUIAction()
- 位置: async L290-296
- 役割: 閉じるための ToolUI の処理を、収集したタブと対応表を渡して呼ぶ。
- 触るとき: タブを閉じる実行経路を変えるとき。
- 呼び出し先: `lazy.ToolUI.closeSelectedTabs()`
- 参照: `gatheredResult.tabKeyByToken`, `gatheredResult.tabs`, `gatheredResult.topAIWin`

## getConfirmationProperties()
- 位置: L298-300
- 役割: 閉じる確認カードに渡すタブの一覧を返す。
- 触るとき: 閉じる確認カードの表示データを変えるとき。
- 参照: `gatheredResult.tabs`

## getToolResults()
- 位置: L302-332
- 役割: 閉じられたタブと失敗したタブを数え、説明文・結果一覧・テレメトリ値を作る。
- 触るとき: 閉じる結果の説明文や集計を変えるとき。
- 呼び出し先: `(result.failedTabs ?? []) .map()`, `(result.failedTabs ?? []) .map(failedTab => failedTab.tab?.permanentKey) .filter()`, `closedTabs.filter()`, `failedKeys.has()`, `gatheredResult.tabKeyByToken.get()`, `gatheredResult.tabs.map()`, `lazy.ToolUITelemetry.browserActionResult()`
- 参照: `closedTabs.filter(tab => tab.closed).length`, `closedTabs.length`, `failedTab.tab?.permanentKey`, `result.failedTabs`, `tab.closed`

## makeGroupTabsToolHandler()
- 位置: L343-425
- 役割: ラベルの決定と、グループ化の実行・結果整形を担うハンドラーを作る。ラベルは引数指定が優先で、無ければ SmartTabGroupingManager の予測、失敗時は「Tabs」。
- 触るとき: グループ化の挙動(ラベルの決め方や実行手順)を変えるとき。

## getLabel()
- 位置: async L344-359
- 役割: 指定があれば無害化して 40 字以内にしたラベルを返し、無ければ最前面窓のタブと他の可視タブから予測ラベルを作る。
- 触るとき: グループ名の決め方を変えるとき。
- 呼び出し先: `allVisible.filter()`, `gatheredResult.matchedTabs .filter()`, `gatheredResult.matchedTabs .filter(m => m.win === gatheredResult.topAIWin) .map()`, `manager.getPredictedLabelForGroup()`, `rawTabs.includes()`
- 条件付き依存: `if (rawLabel)` → `sanitizeUntrustedContent(rawLabel, true).slice(0, 40).trim()`
- 条件付き依存: `if (rawLabel)` → `sanitizeUntrustedContent(rawLabel, true).slice()`
- 条件付き依存: `if (rawLabel)` → `sanitizeUntrustedContent()`
- 参照: `gatheredResult.topAIWin`, `gatheredResult.topAIWin.gBrowser.visibleTabs`, `lazy.SmartTabGroupingManager`, `m.tab`, `m.win`, `t.pinned`

## getConfirmationProperties()
- 位置: async L367-372
- 役割: グループ化の確認カードにタブ一覧とラベルを渡す。
- 触るとき: グループ化の確認カードの表示データを変えるとき。
- 呼び出し先: `getLabel()`
- 参照: `gatheredResult.tabs`

## takeUIAction()
- 位置: async L374-389
- 役割: ラベルを決めてから ToolUI でタブグループを作り、作成されたグループ ID を操作 ID として返す。
- 触るとき: グループ作成の実行経路や操作 ID の扱いを変えるとき。
- 呼び出し先: `getLabel()`, `lazy.ToolUI.createTabGroup()`
- 参照: `gathered.tabKeyByToken`, `gathered.tabs`, `gathered.topAIWin`, `result.group.id`, `result?.group?.id`

## getToolResults()
- 位置: L391-423
- 役割: グループに入ったタブと失敗したタブを数え、説明文・結果一覧・テレメトリ値を作る。
- 触るとき: グループ化の結果の説明文や集計を変えるとき。
- 呼び出し先: `(result.failedTabs ?? []) .map()`, `(result.failedTabs ?? []) .map(failedTab => failedTab.tab?.linkedPanel) .filter()`, `failedPanels.has()`, `gatheredResult.tabs.map()`, `groupedTabs.filter()`, `lazy.ToolUITelemetry.browserActionResult()`
- 参照: `failedTab.tab?.linkedPanel`, `groupedTabs.filter(tab => tab.grouped).length`, `groupedTabs.length`, `result.failedTabs`, `result.label`, `tab.grouped`

## manageTabsAction()
- 位置: async L434-466
- 役割: action 名(close_tabs か group_tabs)からハンドラーを選び、共通の流れに渡す公開入口。不明な action は例外にする。
- 触るとき: タブ操作の種類を増やすとき、またはツールからの呼び出し経路を調べるとき。
- 呼び出し先: `makeHandler()`, `runManageTabsFlow()`

## [CLOSE_TABS]()
- 位置: L446-446
- 役割: action が close_tabs のときに閉じる処理のハンドラーを返す。
- 触るとき: 閉じる操作の振り分けを確認するとき。

## [GROUP_TABS]()
- 位置: L447-447
- 役割: action が group_tabs のときに、ラベルを渡してグループ化のハンドラーを作る。
- 触るとき: グループ化の振り分けやラベルの渡し方を確認するとき。
- 呼び出し先: `makeGroupTabsToolHandler()`
