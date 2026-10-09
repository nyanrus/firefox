# browser/components/tabbrowser/TabUnloader.sys.mjs

source: browser/components/tabbrowser/TabUnloader.sys.mjs
source-hash: ac31a260565465c062b31fdd204acc86324fefbe
lines: 517

## <module>
- 役割: メモリ不足時に、最近使われていないタブを重み付けの規則で選んで破棄する TabUnloader と、その判定用ヘルパーを定義する。
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.prefs.getIntPref()`, `XPCOMUtils.declareLazy()`

## isNonDiscardable()
- 位置: L53-59
- 役割: 未接続のブラウザなら -1(対象外)、破棄不可または選択中のタブなら重みを返し、それ以外は 0 を返す。
- 触るとき: どのタブを破棄不可とみなすかを変えるとき。
- 参照: `tab.linkedBrowser.isConnected`, `tab.selected`, `tab.undiscardable`

## isPinned()
- 位置: L61-63
- 役割: ピン留めタブなら重みを、そうでなければ 0 を返す。
- 触るとき: ピン留めタブの破棄されにくさを調整するとき。
- 参照: `tab.pinned`

## isLoading()
- 位置: L65-67
- 役割: 常に 0 を返す。読み込み中の判定はここでは行われていない(要確認)。
- 触るとき: 読み込み中タブを破棄対象から外したいとき、この実装が空である点を確認する。

## usingPictureInPicture()
- 位置: L69-72
- 役割: ピクチャインピクチャ使用中のタブなら重みを返す。
- 触るとき: PiP 中のタブの保護を調べるとき。
- 参照: `tab.pictureinpicture`

## playingMedia()
- 位置: L74-76
- 役割: 音声再生中のタブなら重みを返す。
- 触るとき: 再生中タブの保護を調べるとき。
- 参照: `tab.soundPlaying`

## usingWebRTC()
- 位置: L78-90
- 役割: WebRTC のストリームまたは接続を持つタブなら重みを返す。
- 触るとき: 通話中タブの保護を調べるとき。
- 呼び出し先: `browser.browsingContext?.currentWindowGlobal?.hasActivePeerConnections()`, `lazy.webrtcUI.browserHasStreams()`
- 参照: `tab.linkedBrowser`

## isPrivate()
- 位置: L92-96
- 役割: プライベートブラウジングのタブなら重みを返す。
- 触るとき: プライベートタブを破棄対象に含めるか変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `tab.linkedBrowser`

## getMinTabCount()
- 位置: L98-100
- 役割: 追加の重み付けを省く末尾タブ数(MIN_TABS_COUNT)を返す。
- 触るとき: リソース使用による再重み付けの対象範囲を変える、またはテストで差し替えるとき。

## getNow()
- 位置: L102-104
- 役割: 現在時刻をミリ秒で返す。
- 触るとき: テストで時刻を差し替えるとき。
- 呼び出し先: `Date.now()`

## iterateTabs()
- 位置: L106-112
- 役割: 全ブラウザウィンドウの全タブを、gBrowser と組にして順に返す。
- 触るとき: 破棄候補とするタブの範囲を変えるとき。
- 呼び出し先: `Services.wm.getEnumerator()`
- 参照: `win.gBrowser`, `win.gBrowser.tabs`
- XPCOM: `Services.wm`

## iterateBrowsingContexts()
- 位置: L114-119
- 役割: ブラウジングコンテキストとその子孫を再帰的に順に返す。
- 触るとき: サブフレームを含めた走査を調べるとき。
- 呼び出し先: `this.iterateBrowsingContexts()`
- 参照: `bc.children`

## iterateProcesses()
- 位置: L121-133
- 役割: タブのトップと子フレームが使うプロセス ID(osPid)を順に返す。
- 触るとき: タブごとのプロセス使用を調べるとき。
- 呼び出し先: `this.iterateBrowsingContexts()`
- 参照: `childBC.currentWindowGlobal.osPid`, `childBC?.currentWindowGlobal`, `tab?.linkedBrowser?.browsingContext`

## calculateMemoryUsage()
- 位置: async L141-152
- 役割: 子プロセスの情報を取得し、プロセスマップに各プロセスのメモリ量を書き込む。
- 触るとき: メモリ使用量の取得方法を変える、またはテストで差し替えるとき。
- 呼び出し先: `ChromeUtils.requestProcInfo()`, `processMap.get()`
- 条件付き依存: `if (!processInfo)` → `processMap.set()`
- 参照: `childProcInfo.memory`, `childProcInfo.pid`, `parentProcessInfo.children`, `processInfo.memory`

## init()
- 位置: L164-169
- 役割: メモリ監視サービスに自身をタブアンローダとして登録する。
- 触るとき: 低メモリ検知との接続や起動時の登録を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/xpcom/memory-watcher;1"].getService()`, `watcher.registerTabUnloader()`
- 参照: `Ci.nsIAvailableMemoryWatcherBase`
- XPCOM: [`nsIAvailableMemoryWatcherBase`](../../../xpcom/base/nsIAvailableMemoryWatcherBase.idl.md) / `@mozilla.org/xpcom/memory-watcher;1`

## isDiscardable()
- 位置: L171-176
- 役割: タブの重みが NEVER_DISCARD 未満なら破棄可能と判定する。
- 触るとき: 破棄可否の閾値の扱いを調べるとき。
- 参照: `tab.weight`

## unloadTabAsync()
- 位置: async L179-205
- 役割: pref と実行中かを確認したうえでタブを1つ破棄し、結果をメモリ監視サービスへ通知する。
- 触るとき: 低メモリ時のアンロード要求の入口や、結果コードの扱いを調べるとき。
- 呼び出し先: `Cc["@mozilla.org/xpcom/memory-watcher;1"].getService()`, `Services.prefs.getBoolPref()`, `this.unloadLeastRecentlyUsedTab()`, `watcher.onUnloadAttemptCompleted()`
- 条件付き依存: `if (!Services.prefs.getBoolPref("browser.tabs.unloadOnLowMemory", true))` → `watcher.onUnloadAttemptCompleted()`
- 条件付き依存: `if (this._isUnloading)` → `Services.console.logStringMessage()`
- 条件付き依存: `if (this._isUnloading)` → `watcher.onUnloadAttemptCompleted()`
- 参照: `Ci.nsIAvailableMemoryWatcherBase`, `Cr.NS_ERROR_ABORT`, `Cr.NS_ERROR_NOT_AVAILABLE`, `Cr.NS_OK`, `this._isUnloading`
- XPCOM: [`nsIAvailableMemoryWatcherBase`](../../../xpcom/base/nsIAvailableMemoryWatcherBase.idl.md) / `@mozilla.org/xpcom/memory-watcher;1` / `Services.console` / `Services.prefs`

## getSortedTabs()
- 位置: async L239-315
- 役割: 全タブに重みを付けて並べ、必要ならプロセス数とメモリで再重み付けし、破棄すべき順の一覧を返す。
- 触るとき: どのタブから破棄されるかの順序付けを変えるとき。
- 呼び出し先: `determineTabBaseWeight()`, `tabMethods.getMinTabCount()`, `tabMethods.getNow()`, `tabMethods.iterateTabs()`, `tabs.sort()`, `this.isDiscardable()`
- 条件付き依存: `if (weight != -1)` → `tabs.push()`
- 条件付き依存: `if (lowestWeightedCount > 1)` → `getAllProcesses()`
- 条件付き依存: `if (lowestWeightedCount > 1)` → `tabs.splice()`
- 条件付き依存: `if (lowestWeightedCount > 1)` → `adjustForResourceUse()`
- 条件付き依存: `if (lowestWeightedCount > 1)` → `tabs.concat()`
- 参照: `a.tab.lastAccessed`, `a.weight`, `b.tab.lastAccessed`, `b.weight`, `tab.tab.lastAccessed`, `tab.weight`, `tabs.length`, `tabs[idx].weight`

## unloadLeastRecentlyUsedTab()
- 位置: async L322-345
- 役割: 並べたタブの先頭から順に破棄を試み、成功したら true を返す。
- 触るとき: 実際の破棄処理と、破棄不可に当たった時の打ち切りを調べるとき。
- 呼び出し先: `tabInfo.gBrowser.discardBrowser()`, `tabInfo.gBrowser.prepareDiscardBrowser()`, `this.getSortedTabs()`, `this.isDiscardable()`
- 条件付き依存: `if (tabInfo.gBrowser.discardBrowser(tabInfo.tab))` → `Services.console.logStringMessage()`
- 条件付き依存: `if (tabInfo.gBrowser.discardBrowser(tabInfo.tab))` → `tabInfo.tab.updateLastUnloadedByTabUnloader()`
- 参照: `tabInfo.tab`, `tabInfo.tab?.linkedBrowser?.remoteType`
- XPCOM: `Services.console`

## determineTabBaseWeight()
- 位置: L359-377
- 役割: 各判定基準の重みを合計してタブの基本重みを返し、-1 があれば除外を示す -1 を返す。
- 触るとき: 判定基準の追加や重みの調整をするとき。
- 呼び出し先: `tabMethods[criteriaType[CRITERIA_METHOD]]()`
- 参照: `tab.tab`

## getAllProcesses()
- 位置: L390-445
- 役割: 各タブが使うプロセスを調べ、プロセスごとのタブ数とフレーム数のマップを作る。
- 触るとき: プロセス共有の数え方を調べるとき。
- 呼び出し先: `processMap.get()`, `tab.processes.get()`, `tabMethods.iterateProcesses()`
- 条件付き依存: `if (processInfo)` → `processInfo.tabSet.add()`
- 条件付き依存: `if (!(processInfo))` → `processMap.set()`
- 条件付き依存: `if (!(tabProcessEntry))` → `tab.processes.set()`
- 参照: `processInfo.count`, `processInfo.topCount`, `tab.processes`, `tab.tab`, `tabProcessEntry.frameCount`, `tabs.length`

## adjustForResourceUse()
- 位置: async L455-516
- 役割: 固有プロセス数と推定メモリ量でタブを順位付けし、最終的な破棄順に並べ替える。
- 触るとき: メモリやプロセス数が破棄順に与える影響を調整するとき。
- 呼び出し先: `tab.processes.values()`, `tabMethods.calculateMemoryUsage()`, `tabs.sort()`
- 参照: `a.memory`, `a.sortWeight`, `a.tab.lastAccessed`, `a.uniqueCount`, `b.memory`, `b.sortWeight`, `b.tab.lastAccessed`, `b.uniqueCount`, `procEntry.entryToProcessMap`, `procEntry.frameCount`, `processInfo.count`, `processInfo.memory`, `processInfo.tabSet.size`, `processInfo.topCount`, `tab.memory`, `tab.sortWeight`, `tab.uniqueCount`
