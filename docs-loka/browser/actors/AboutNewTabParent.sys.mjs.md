# browser/actors/AboutNewTabParent.sys.mjs

source: browser/actors/AboutNewTabParent.sys.mjs
source-hash: 1b0427ef7444efa08c1ba18b207cf2285ae98f07
lines: 222

## <module>
- 役割: about:newtab の親側アクター。タブごとの newtab 状態の登録・追跡、ASRouter へのトリガー送信、Activity Stream チャネルへの中継を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutNewTabParent.loadedTabs()
- 位置: L17-19
- 役割: 読み込み済み newtab タブの browser → タブ詳細マップを static に返す。
- 触るとき: 開いている newtab タブを列挙・照合する処理を追加・変更するときに見る。

## AboutNewTabParent.getTabDetails()
- 位置: L21-24
- 役割: このアクターの最上位ブラウジングコンテキストの embedderElement に対応するタブ詳細を返す。
- 触るとき: 子プロセスからのメッセージを対応するタブへ結び付ける経路を調べるときに見る。
- 呼び出し先: `gLoadedTabs.get()`
- 参照: `this.browsingContext.top.embedderElement`

## AboutNewTabParent.handleEvent()
- 位置: L26-41
- 役割: SwapDocShells 時に、タブ詳細の browser 参照を古い要素から新しい要素へ付け替える。
- 触るとき: タブのドラッグ移動や docshell の入れ替えで newtab の状態が失われる問題を調べるときに見る。
- 条件付き依存: `if (event.type == "SwapDocShells")` → `gLoadedTabs.get()`
- 条件付き依存: `if (tabDetails)` → `gLoadedTabs.delete()`
- 条件付き依存: `if (tabDetails)` → `gLoadedTabs.set()`
- 条件付き依存: `if (tabDetails)` → `oldBrowser.removeEventListener()`
- 条件付き依存: `if (tabDetails)` → `newBrowser.addEventListener()`
- 参照: `event.detail`, `event.type`, `tabDetails.browser`, `this.browsingContext.top.embedderElement`

## AboutNewTabParent.makeTransientIfDisabledAndInitial()
- 位置: L48-62
- 役割: newtab 無効時に、初期の about:newtab 履歴エントリを一時扱いにしてセッション履歴へ残さない。
- 触るとき: newtab 無効化時の履歴の挙動や about:blank 相当の扱いを変えるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `sh.getEntryAtIndex()`
- 条件付き依存: `if (entry.URI.spec === "about:newtab")` → `entry.setTransient()`
- 参照: `entry.URI.spec`, `sh.count`, `this.browsingContext.sessionHistory`
- XPCOM: `Services.prefs`

## AboutNewTabParent.receiveMessage()
- 位置: async L64-159
- 役割: 子からの Init/Load/Unload/AboutNewTabVisible/ContentToMain/AssignRenderer を処理し、登録・通知・ASRouter トリガー・レンダラー割り当てを行う。
- 触るとき: newtab の子親間メッセージの流れやライフサイクル処理を変更するときに見る。
- 呼び出し先: `browser.addEventListener()`, `gLoadedTabs.delete()`, `gLoadedTabs.set()`, `rendererActor.assignRenderer()`, `tabDetails.browser.removeEventListener()`, `this.browsingContext.currentWindowGlobal.getActor()`, `this.getTabDetails()`, `this.makeTransientIfDisabledAndInitial()`, `this.notifyActivityStreamChannel()`
- 条件付き依存: `if (!browsingContext.isDiscarded)` → `lazy.ASRouter.sendTriggerMessage()`
- 条件付き依存: `if (!tabDetails)` → `this.getByBrowsingContext()`
- 参照: `browsingContext.isDiscarded`, `browsingContext.top.embedderElement`, `lazy.ASRouter.waitForInitialized`, `lazy.AboutNewTab.activityStream`, `lazy.AboutNewTab.activityStreamPromise`, `message.data.portID`, `message.data.url`, `message.name`, `tabDetails.browser`, `this.browsingContext`

## AboutNewTabParent.notifyActivityStreamChannel()
- 位置: L161-189
- 役割: タブ詳細を付けて Activity Stream のチャネルへ通知を渡す。チャネル未準備ならキューに積む。
- 触るとき: newtab から Activity Stream へ届くイベントが欠ける、または順序が乱れるときに見る。
- 呼び出し先: `channel[name]()`, `this.getChannel()`
- 条件付き依存: `if (!tabDetails)` → `this.getTabDetails()`
- 条件付き依存: `if (!channel)` → `AboutNewTabParent.#queuedMessages.push()`
- 参照: `message.data`

## AboutNewTabParent.getByBrowsingContext()
- 位置: L191-199
- 役割: 読み込み済みタブの中から、指定したブラウジングコンテキストに一致する詳細を探す。
- 触るとき: タブを閉じる途中などで embedderElement が取れないときの照合経路を調べるときに見る。
- 呼び出し先: `AboutNewTabParent.loadedTabs.values()`
- 参照: `tabDetails.browsingContext`

## AboutNewTabParent.getChannel()
- 位置: L201-203
- 役割: AboutNewTab の Activity Stream store からメッセージチャネルを取り出す。未初期化なら undefined を返す。
- 触るとき: Activity Stream チャネルの初期化タイミングや未準備時の挙動を調べるときに見る。
- 呼び出し先: `lazy.AboutNewTab.activityStream?.store?.getMessageChannel()`

## AboutNewTabParent.flushQueuedMessagesFromContent()
- 位置: L214-220
- 役割: チャネル準備前にキューへ積んだ子プロセス由来のメッセージを、順に通知し直して空にする。
- 触るとき: 起動直後の newtab メッセージが取りこぼされる、または二重に届く問題を調べるときに見る。
- 呼び出し先: `actor.notifyActivityStreamChannel()`
- 参照: `AboutNewTabParent.#queuedMessages`
